# `src/landscout/stages/bess_planning_feature_policy.py`

## File identity

- Repository path: `src/landscout/stages/bess_planning_feature_policy.py`
- File type: Python source
- Primary responsibility: Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.
- Layer / domain: `stage` / `planning`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `9ca9a70b5930e6e3054dd80bf83e04a658916d64d24133162140f713bd5c23d0`

## 1. Purpose

Compiles and validates the checked-in BESS policy for official CNIG planning-feature meanings.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import math` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `from collections.abc import Mapping` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass, replace` — required by the implementation paths and symbols documented below.
- `from datetime import date, datetime` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from io import BytesIO` — required by the implementation paths and symbols documented below.
- `from numbers import Integral, Real` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Literal` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.
- `from pydantic import ( BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr, model_validator, )` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.artifact_paths import validate_portable_parquet_filename` — required by the implementation paths and symbols documented below.
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature` — required by the implementation paths and symbols documented below.
- `from landscout.sources.gpu_fr import GpuPlanningDocument` — required by the implementation paths and symbols documented below.
- `from landscout.stages.resolve_planning_feature_codes import ( CnigFeatureCodeProfile, PlanningFeatureCodeResult, validate_planning_feature_code_result, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `POLICY_SCHEMA_VERSION` | `1` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RESULT_HASH_SCHEMA_VERSION` | `1` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARTIFACT_MANIFEST_SCHEMA_VERSION` | `2` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_SCOPE` | `"OFFICIAL_CNIG_CODE_MEANING_ONLY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARTIFACT_KIND` | `"BESS_CNIG_FEATURE_POLICY_RESULT"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ALLOWED_STATUSES` | `frozenset( { "LIKELY_MATERIAL_CONSTRAINT", "MATERIAL_REVIEW_REQUIRED", "DESIGN_REVIEW_REQUIRED", "CONTEXT_REVIEW_REQUIRED", "UNKNOWN", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ALLOWED_CONFIDENCES` | `frozenset({"HIGH", "MEDIUM", "LOW"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CODE_PATTERN` | `re.compile(r"[0-9]{2}")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SHA_PATTERN` | `re.compile(r"[0-9a-f]{64}")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_TABLE_COLUMNS` | `( "feature_family", "type_code", "subtype_code", "official_label", "official_legal_reference", "official_regulation_reference", "precheck_status", "confidence", "status_priority", "rationale", "required_human_action", "limitations", "policy_scope", "local_feature_text_interpreted", "local_regulation_content_interpreted", "legal_conclusion_produced", "policy_profile", "policy_sha256", "cnig_profile", "cnig_profile_sha256", "cnig_complete_result_content_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_TABLE_DTYPES` | `tuple( "int64" if column == "status_priority" else "bool" if column in { "local_feature_text_interpreted", "local_regulation_content_interpreted", "legal_conclusion_produced", } else "str" for column in POLICY_TABLE_COLUMNS )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_TABLE_SCHEMA_SIGNATURE` | `{ "columns": list(POLICY_TABLE_COLUMNS), "dtypes": list(POLICY_TABLE_DTYPES), "index_class": "pandas.Index", "index_names": [None], "index_level_dtypes": ["int64"], }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `NULL_REFERENCE_LITERALS` | `frozenset({"None", "nan", "<NA>"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_RESULT_SCALAR_FIELDS` | `( "policy_schema_version", "result_hash_schema_version", "policy_profile", "policy_scope", "policy_sha256", "source_document_id", "source_archive_sha256", "cnig_profile", "cnig_profile_schema_version", "cnig_profile_sha256", "cnig_result_hash_schema_version", "cnig_complete_result_content_sha256", "policy_table_content_sha256", "complete_result_content_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `BessPlanningFeaturePolicyError`

**Purpose:** Raised when the official-code BESS policy cannot be proven exact.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `_StrictPolicyModel`

**Purpose:** Represents a validated policy configuration or compiled policy evidence envelope.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid", frozen=True)`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `PolicyTableSchemaSignature`

**Purpose:** Immutable persisted schema identity for the normalized policy table.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `columns` | `tuple[StrictStr, ...]` | `required` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `dtypes` | `tuple[StrictStr, ...]` | `required` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `index_class` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `index_names` | `tuple[StrictStr | None, ...]` | `required` | `tuple[StrictStr | None, ...]` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `index_level_dtypes` | `tuple[StrictStr, ...]` | `required` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `PolicySourceLock`

**Purpose:** Represents a validated policy configuration or compiled policy evidence envelope.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `document_id` | `StrictStr` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `archive_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_profile` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cnig_profile_schema_version` | `StrictInt` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `cnig_profile_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_result_hash_schema_version` | `StrictInt` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `cnig_complete_result_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |

**Validators and methods:**

- `_validate_lock` — `def _validate_lock(self) -> PolicySourceLock:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `PolicyEntry`

**Purpose:** Represents a validated policy configuration or compiled policy evidence envelope.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `feature_family` | `FeatureFamily` | `required` | `FeatureFamily` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `type_code` | `StrictStr` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `subtype_code` | `StrictStr` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `expected_official_label` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `expected_legal_reference` | `StrictStr | None` | `required` | `StrictStr | None` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `expected_regulation_reference` | `StrictStr | None` | `required` | `StrictStr | None` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `precheck_status` | `PrecheckStatus` | `required` | Categorical factual, technical, policy, or diagnostic status; the owning constants/validators define the closed vocabulary. |
| `confidence` | `Confidence` | `required` | `Confidence` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `rationale` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `required_human_action` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `limitations` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_entry` — `def _validate_entry(self) -> PolicyEntry:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `BessPlanningFeaturePolicyConfig`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `StrictInt` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `profile` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_scope` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` | `required` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `local_feature_text_interpreted` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `local_regulation_content_interpreted` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `legal_conclusion_produced` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_lock` | `PolicySourceLock` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `status_priority` | `dict[PrecheckStatus, StrictInt]` | `required` | `dict[PrecheckStatus, StrictInt]` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `canonical_policy_entries_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `entries` | `tuple[PolicyEntry, ...]` | `required` | `tuple[PolicyEntry, ...]` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_policy` — `def _validate_policy(self) -> BessPlanningFeaturePolicyConfig:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `_UniqueKeyLoader`

**Purpose:** Groups the `UniqueKeyLoader` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `yaml.SafeLoader`.

**Model form and mutability:** class inheriting from `yaml.SafeLoader`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `BessPlanningFeaturePolicyResult`

**Purpose:** Immutable normalized policy table and its source-complete hash envelope.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `policy_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `result_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `policy_profile` | `str` | `required` | `str` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_scope` | `str` | `required` | `str` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `source_archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_profile` | `str` | `required` | `str` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cnig_profile_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `cnig_profile_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_result_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `cnig_complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `policy_table_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `policy_table` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `BessPlanningFeaturePolicyArtifactManifest`

**Purpose:** Strict physical binding between one policy table and its hash envelope.

**Inheritance:** `_StrictPolicyModel`.

**Model form and mutability:** class inheriting from `_StrictPolicyModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `StrictInt` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `artifact_kind` | `Literal['BESS_CNIG_FEATURE_POLICY_RESULT']` | `required` | `Literal['BESS_CNIG_FEATURE_POLICY_RESULT']` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_schema_version` | `StrictInt` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `result_hash_schema_version` | `StrictInt` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `policy_profile` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_scope` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` | `required` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_document_id` | `StrictStr` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `source_archive_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_profile` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cnig_profile_schema_version` | `StrictInt` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `cnig_profile_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_result_hash_schema_version` | `StrictInt` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `cnig_complete_result_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `policy_table_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `complete_result_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `parquet_filename` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parquet_row_count` | `StrictInt` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `parquet_size_bytes` | `StrictInt` | `required` | `StrictInt` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parquet_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `policy_table_schema_signature` | `PolicyTableSchemaSignature` | `required` | `PolicyTableSchemaSignature` state used by `src/landscout/stages/bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_manifest` — `def _validate_manifest(self) -> BessPlanningFeaturePolicyArtifactManifest:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

## 6. Functions and methods

### `_exact_string`

**Signature**

```python
def _exact_string(value: object, label: str) -> str:
```

**Purpose**

Implements exact string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `ValueError(f'{label} must be an exact non-empty string without edge whitespace')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `isinstance`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `BessPlanningFeaturePolicyArtifactManifest._validate_manifest`
- `src/landscout/stages/bess_planning_feature_policy.py` — `BessPlanningFeaturePolicyConfig._validate_policy`
- `src/landscout/stages/bess_planning_feature_policy.py` — `PolicyEntry._validate_entry`
- `src/landscout/stages/bess_planning_feature_policy.py` — `PolicySourceLock._validate_lock`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_optional_exact_string`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_sha256_string`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_validate_policy_table_rows`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_optional_exact_string`

**Signature**

```python
def _optional_exact_string(value: object, label: str) -> str | None:
```

**Purpose**

Implements optional exact string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str | None`. Observed return expression(s): `_exact_string(value, label)`; `None`.

**Algorithm**

1. Checks `value is None`. When true: Returns `None`.
2. Returns `_exact_string(value, label)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_exact_string`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `PolicyEntry._validate_entry`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_sha256_string`

**Signature**

```python
def _sha256_string(value: object, label: str) -> str:
```

**Purpose**

Implements sha256 string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `text`.

**Algorithm**

1. Computes `text` from `_exact_string(value, label)`.
2. Checks `SHA_PATTERN.fullmatch(text) is None`. When true: Raises `ValueError(f'{label} must be a lowercase SHA256')`.
3. Returns `text`.

**Validation and invariants**

- Rejects or diverts the path when `SHA_PATTERN.fullmatch(text) is None` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SHA_PATTERN.fullmatch`, `ValueError`, `_exact_string`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `BessPlanningFeaturePolicyArtifactManifest._validate_manifest`
- `src/landscout/stages/bess_planning_feature_policy.py` — `BessPlanningFeaturePolicyConfig._validate_policy`
- `src/landscout/stages/bess_planning_feature_policy.py` — `PolicySourceLock._validate_lock`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `PolicySourceLock._validate_lock`

**Signature**

```python
def _validate_lock(self) -> PolicySourceLock:
```

**Purpose**

Validates and rejects malformed lock according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PolicySourceLock`. Observed return expression(s): `self`.

**Algorithm**

1. Calls `_exact_string(self.document_id, 'document_id')` for its validation or side effect.
2. Calls `_sha256_string(self.archive_sha256, 'archive_sha256')` for its validation or side effect.
3. Calls `_exact_string(self.cnig_profile, 'cnig_profile')` for its validation or side effect.
4. Calls `_sha256_string(self.cnig_profile_sha256, 'cnig_profile_sha256')` for its validation or side effect.
5. Calls `_sha256_string(self.cnig_complete_result_content_sha256, 'cnig_complete_result_content_sha256')` for its validation or side effect.
6. Iterates `(value, label)` over `((self.cnig_profile_schema_version, 'cnig_profile_schema_version'), (self.cnig_result_hash_schema_version, 'cnig_result_hash_schema_version'))`. For each value: Checks `type(value) is not int or value < 1`. When true: Raises `ValueError(f'{label} must be a strict positive integer')`.
7. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `type(value) is not int or value < 1` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_exact_string`, `_sha256_string`, `model_validator`, `type`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `PolicyEntry._validate_entry`

**Signature**

```python
def _validate_entry(self) -> PolicyEntry:
```

**Purpose**

Validates and rejects malformed entry according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PolicyEntry`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `CODE_PATTERN.fullmatch(self.type_code) is None`. When true: Raises `ValueError('type_code must be an exact two-character digit string')`.
2. Checks `CODE_PATTERN.fullmatch(self.subtype_code) is None`. When true: Raises `ValueError('subtype_code must be an exact two-character digit string')`.
3. Calls `_exact_string(self.expected_official_label, 'expected_official_label')` for its validation or side effect.
4. Calls `_optional_exact_string(self.expected_legal_reference, 'expected_legal_reference')` for its validation or side effect.
5. Calls `_optional_exact_string(self.expected_regulation_reference, 'expected_regulation_reference')` for its validation or side effect.
6. Calls `_exact_string(self.rationale, 'rationale')` for its validation or side effect.
7. Calls `_exact_string(self.required_human_action, 'required_human_action')` for its validation or side effect.
8. Calls `_exact_string(self.limitations, 'limitations')` for its validation or side effect.
9. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `CODE_PATTERN.fullmatch(self.type_code) is None` is true.
- Rejects or diverts the path when `CODE_PATTERN.fullmatch(self.subtype_code) is None` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CODE_PATTERN.fullmatch`, `ValueError`, `_exact_string`, `_optional_exact_string`, `model_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_json_sha256`

**Signature**

```python
def _canonical_json_sha256(value: object) -> str:
```

**Purpose**

Implements canonical json sha256 according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `sha256(encoded).hexdigest()`.

**Algorithm**

1. Runs guarded operation: Computes `encoded` from `json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')`. Handles `(TypeError, ValueError)`.
2. Returns `sha256(encoded).hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`, `json.dumps`, `json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode`, `sha256`, `sha256(encoded).hexdigest`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_complete_result_sha256`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_policy_entries_sha256`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_policy_sha256`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_policy_table_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_entries_sha256`

**Signature**

```python
def _policy_entries_sha256(entries: tuple[PolicyEntry, ...]) -> str:
```

**Purpose**

Implements policy entries sha256 according to the exact implementation and guards in this file.

**Inputs**

- `entries` (`tuple[PolicyEntry, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256([entry.model_dump(mode='json') for entry in entries])`.

**Algorithm**

1. Returns `_canonical_json_sha256([entry.model_dump(mode='json') for entry in entries])`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_json_sha256`, `entry.model_dump`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `BessPlanningFeaturePolicyConfig._validate_policy`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessPlanningFeaturePolicyConfig._validate_policy`

**Signature**

```python
def _validate_policy(self) -> BessPlanningFeaturePolicyConfig:
```

**Purpose**

Validates and rejects malformed policy according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeaturePolicyConfig`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `type(self.schema_version) is not int or self.schema_version != POLICY_SCHEMA_VERSION`. When true: Raises `ValueError(f'policy schema version must equal {POLICY_SCHEMA_VERSION}')`.
2. Calls `_exact_string(self.profile, 'profile')` for its validation or side effect.
3. Checks `self.policy_scope != POLICY_SCOPE`. When true: Raises `ValueError('policy_scope is unsupported')`.
4. Checks `self.local_feature_text_interpreted is not False or self.local_regulation_content_interpreted is not False or self.legal_conclusion_produced is not False`. When true: Raises `ValueError('policy interpretation and legal-conclusion flags must be false')`.
5. Checks `set(self.status_priority) != ALLOWED_STATUSES`. When true: Raises `ValueError('status priority must contain every allowed status exactly once')`.
6. Computes `priorities` from `list(self.status_priority.values())`.
7. Checks `any((type(value) is not int or value <= 0 for value in priorities))`. When true: Raises `ValueError('status priority values must be strict positive integers')`.
8. Checks `len(set(priorities)) != len(priorities)`. When true: Raises `ValueError('status priority values must be unique')`.
9. Computes `keys` from `[(entry.feature_family, entry.type_code, entry.subtype_code) for entry in self.entries]`.
10. Checks `len(keys) != len(set(keys))`. When true: Raises `ValueError('policy entries contain a duplicate family/type/subtype pair')`.
11. Checks `keys != sorted(keys)`. When true: Raises `ValueError('policy entries must use deterministic family/type/subtype order')`.
12. Calls `_sha256_string(self.canonical_policy_entries_sha256, 'canonical_policy_entries_sha256')` for its validation or side effect.
13. Checks `_policy_entries_sha256(self.entries) != self.canonical_policy_entries_sha256`. When true: Raises `ValueError('canonical policy-entry SHA256 differs from policy entries')`.
14. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `type(self.schema_version) is not int or self.schema_version != POLICY_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `self.policy_scope != POLICY_SCOPE` is true.
- Rejects or diverts the path when `self.local_feature_text_interpreted is not False or self.local_regulation_content_interpreted is not False or self.legal_conclusion_produced is not False` is true.
- Rejects or diverts the path when `set(self.status_priority) != ALLOWED_STATUSES` is true.
- Rejects or diverts the path when `any((type(value) is not int or value <= 0 for value in priorities))` is true.
- Rejects or diverts the path when `len(set(priorities)) != len(priorities)` is true.
- Rejects or diverts the path when `len(keys) != len(set(keys))` is true.
- Rejects or diverts the path when `keys != sorted(keys)` is true.
- Rejects or diverts the path when `_policy_entries_sha256(self.entries) != self.canonical_policy_entries_sha256` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_exact_string`, `_policy_entries_sha256`, `_sha256_string`, `any`, `len`, `list`, `model_validator`, `self.status_priority.values`, `set`, `sorted`, `type`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_construct_unique_mapping`

**Signature**

```python
def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
```

**Purpose**

Implements construct unique mapping according to the exact implementation and guards in this file.

**Inputs**

- `loader` (`yaml.SafeLoader`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `node` (`yaml.MappingNode`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `deep` (`bool`; optional/default `False`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[object, object]`. Observed return expression(s): `result`.

**Algorithm**

1. Defines `result` with annotation `dict[object, object]` from `{}`.
2. Iterates `(key_node, value_node)` over `node.value`. For each value: Computes `key` from `loader.construct_object(key_node, deep=deep)`. Checks `key in result`. When true: Raises `BessPlanningFeaturePolicyError(f'Duplicate YAML policy key: {key!r}')`. Computes `result[key]` from `loader.construct_object(value_node, deep=deep)`.
3. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `key in result` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`, `loader.construct_object`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_bess_planning_feature_policy_config`

**Signature**

```python
def load_bess_planning_feature_policy_config(
    path: str | Path,
) -> BessPlanningFeaturePolicyConfig:
```

**Purpose**

Load a strict offline BESS policy for official CNIG feature-code pairs.

**Inputs**

- `path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeaturePolicyConfig`. Observed return expression(s): `BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Algorithm**

1. Runs guarded operation: Computes `payload` from `yaml.load(Path(path).read_text(encoding='utf-8'), Loader=_UniqueKeyLoader)`. Checks `not isinstance(payload, Mapping)`. When true: Raises `BessPlanningFeaturePolicyError('BESS CNIG policy must be a mapping')`. Returns `BessPlanningFeaturePolicyConfig.model_validate(payload)`. Handles `BessPlanningFeaturePolicyError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(payload, Mapping)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `Path(path).read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `BessPlanningFeaturePolicyError`, `Path`, `Path(path).read_text`, `isinstance`, `yaml.load`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_resolved_policy_config`
- `tests/unit/test_bess_planning_feature_policy.py` — `_checked_in_policy_result`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_checked_in_policy_complete_snapshot_is_immutable`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_checked_in_policy_pins_all_twelve_exact_muret_decisions`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_duplicate_yaml_key_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_profile_v1_snapshot_detects_policy_text_drift`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_profile_v1_snapshot_detects_source_lock_drift`

**Tests**

- `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_policy_complete_snapshot_is_immutable`
- `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_policy_pins_all_twelve_exact_muret_decisions`
- `tests/unit/test_bess_planning_feature_policy.py::test_duplicate_yaml_key_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_policy_text_drift`
- `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_source_lock_drift`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_resolved_policy_config`

**Signature**

```python
def _resolved_policy_config(
    config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyConfig:
```

**Purpose**

Implements resolved policy config according to the exact implementation and guards in this file.

**Inputs**

- `config` (`BessPlanningFeaturePolicyConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeaturePolicyConfig`. Observed return expression(s): `load_bess_planning_feature_policy_config(config)`; `BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Algorithm**

1. Checks `not isinstance(config, BessPlanningFeaturePolicyConfig)`. When true: Returns `load_bess_planning_feature_policy_config(config)`.
2. Runs guarded operation: Computes `payload` from `config.model_dump(mode='python', warnings='error')`. Returns `BessPlanningFeaturePolicyConfig.model_validate(payload)`. Handles `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_bess_planning_feature_policy_config`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `BessPlanningFeaturePolicyError`, `config.model_dump`, `isinstance`, `load_bess_planning_feature_policy_config`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `compile_bess_planning_feature_policy`
- `src/landscout/stages/bess_planning_feature_policy.py` — `validate_bess_planning_feature_policy_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_sha256`

**Signature**

```python
def _policy_sha256(config: BessPlanningFeaturePolicyConfig) -> str:
```

**Purpose**

Implements policy sha256 according to the exact implementation and guards in this file.

**Inputs**

- `config` (`BessPlanningFeaturePolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256(config.model_dump(mode='json'))`.

**Algorithm**

1. Returns `_canonical_json_sha256(config.model_dump(mode='json'))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_json_sha256`, `config.model_dump`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessPlanningFeaturePolicyArtifactManifest._validate_manifest`

**Signature**

```python
def _validate_manifest(self) -> BessPlanningFeaturePolicyArtifactManifest:
```

**Purpose**

Validates and rejects malformed manifest according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeaturePolicyArtifactManifest`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `type(self.schema_version) is not int or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION`. When true: Raises `ValueError(f'artifact manifest schema version must equal {ARTIFACT_MANIFEST_SCHEMA_VERSION}')`.
2. Checks `type(self.policy_schema_version) is not int or self.policy_schema_version != POLICY_SCHEMA_VERSION`. When true: Raises `ValueError('artifact policy schema version is unsupported')`.
3. Checks `type(self.result_hash_schema_version) is not int or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`. When true: Raises `ValueError('artifact result hash schema version is unsupported')`.
4. Checks `type(self.cnig_profile_schema_version) is not int or self.cnig_profile_schema_version != 2`. When true: Raises `ValueError('artifact CNIG profile schema version is unsupported')`.
5. Checks `type(self.cnig_result_hash_schema_version) is not int or self.cnig_result_hash_schema_version != 5`. When true: Raises `ValueError('artifact CNIG result hash schema version is unsupported')`.
6. Iterates `(exact_value, label)` over `((self.policy_profile, 'policy_profile'), (self.source_document_id, 'source_document_id'), (self.cnig_profile, 'cnig_profile'))`. For each value: Calls `_exact_string(exact_value, label)` for its validation or side effect.
7. Iterates `(hash_value, label)` over `((self.policy_sha256, 'policy_sha256'), (self.source_archive_sha256, 'source_archive_sha256'), (self.cnig_profile_sha256, 'cnig_profile_sha256'), (self.cnig_complete_result_content_sha256, 'cnig_complete_result_content_sha256'), (self.policy_table_content_sha256, 'policy_table_content_sha256'), (self.complete_result_c…`. For each value: Calls `_sha256_string(hash_value, label)` for its validation or side effect.
8. Iterates `(integer_value, label, allow_zero)` over `((self.parquet_row_count, 'parquet_row_count', True), (self.parquet_size_bytes, 'parquet_size_bytes', False))`. For each value: Computes `minimum` from `0 if allow_zero else 1`. Checks `type(integer_value) is not int or integer_value < minimum`. When true: Raises `ValueError(f'{label} is invalid')`.
9. Calls `validate_portable_parquet_filename(self.parquet_filename, 'parquet_filename')` for its validation or side effect.
10. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `type(self.schema_version) is not int or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `type(self.policy_schema_version) is not int or self.policy_schema_version != POLICY_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `type(self.result_hash_schema_version) is not int or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `type(self.cnig_profile_schema_version) is not int or self.cnig_profile_schema_version != 2` is true.
- Rejects or diverts the path when `type(self.cnig_result_hash_schema_version) is not int or self.cnig_result_hash_schema_version != 5` is true.
- Rejects or diverts the path when `type(integer_value) is not int or integer_value < minimum` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_exact_string`, `_sha256_string`, `model_validator`, `type`, `validate_portable_parquet_filename`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_null_value`

**Signature**

```python
def _null_value(value: object) -> object:
```

**Purpose**

Implements null value according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `value`; `None`.

**Algorithm**

1. Checks `value is None or value is pd.NA`. When true: Returns `None`.
2. Runs guarded operation: Computes `missing` from `pd.isna(value)`. Handles `(TypeError, ValueError)`.
3. Checks `isinstance(missing, (bool, np.bool_)) and bool(missing)`. When true: Returns `None`.
4. Returns `value`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `bool`, `isinstance`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_canonical_value`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_null_safe_equal`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_validate_policy_table_rows`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_null_safe_equal`

**Signature**

```python
def _null_safe_equal(left: object, right: object) -> bool:
```

**Purpose**

Implements null safe equal according to the exact implementation and guards in this file.

**Inputs**

- `left` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `right` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `normalized_left is None and normalized_right is None`; `bool(normalized_left == normalized_right)`; `False`.

**Algorithm**

1. Computes `normalized_left` from `_null_value(left)`.
2. Computes `normalized_right` from `_null_value(right)`.
3. Checks `normalized_left is None or normalized_right is None`. When true: Returns `normalized_left is None and normalized_right is None`.
4. Runs guarded operation: Returns `bool(normalized_left == normalized_right)`. Handles `(TypeError, ValueError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_null_value`, `bool`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_validate_policy_completeness`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_value`

**Signature**

```python
def _canonical_value(value: object) -> object:
```

**Purpose**

Implements canonical value according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `None`; `value.isoformat()`; `_canonical_value(value.item())`; `value`; `int(value)`; `number`.

**Algorithm**

1. Computes `value` from `_null_value(value)`.
2. Checks `value is None`. When true: Returns `None`.
3. Checks `isinstance(value, (datetime, date, pd.Timestamp))`. When true: Returns `value.isoformat()`.
4. Checks `isinstance(value, np.generic)`. When true: Returns `_canonical_value(value.item())`.
5. Checks `isinstance(value, bool)`. When true: Returns `value`.
6. Checks `isinstance(value, Integral)`. When true: Returns `int(value)`.
7. Checks `isinstance(value, Real)`. When true: Computes `number` from `float(value)`. Checks `not math.isfinite(number)`. When true: Raises `BessPlanningFeaturePolicyError('Policy integrity payload contains non-finite data')`. Returns `number`.
8. Checks `isinstance(value, str)`. When true: Returns `value`.
9. Raises `BessPlanningFeaturePolicyError(f'Policy integrity payload contains unsupported {type(value).__name__}')`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, Real)` is true.
- Rejects or diverts the path when `not math.isfinite(number)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`, `_canonical_value`, `_null_value`, `float`, `int`, `isinstance`, `math.isfinite`, `type`, `value.isoformat`, `value.item`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_frame_payload`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_frame_payload`

**Signature**

```python
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
```

**Purpose**

Implements frame payload according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'schema': deterministic_frame_schema_signature(frame), 'index': [_canonical_value(value) for value in frame.index.tolist()], 'rows': [[_canonical_value(value) for value in row] for row in frame.itertuples(index=False, name=None)]}`.

**Algorithm**

1. Returns `{'schema': deterministic_frame_schema_signature(frame), 'index': [_canonical_value(value) for value in frame.index.tolist()], 'rows': [[_canonical_value(value) for value in row] for row in frame.itertuples(index=False, name=None)]}`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_value`, `deterministic_frame_schema_signature`, `frame.index.tolist`, `frame.itertuples`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_policy_table_sha256`
- `src/landscout/stages/bess_planning_feature_policy.py` — `validate_bess_planning_feature_policy_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_source_lock`

**Signature**

```python
def _validate_source_lock(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> None:
```

**Purpose**

Validates and rejects malformed source lock according to the exact implementation and guards in this file.

**Inputs**

- `config` (`BessPlanningFeaturePolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded_result` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `lock` from `config.source_lock`.
2. Computes `comparisons` from `((lock.document_id, coded_result.source_document_id, 'document ID'), (lock.archive_sha256, coded_result.source_archive_sha256, 'archive SHA256'), (lock.cnig_profile, coded_result.profile, 'CNIG profile'), (lock.cnig_profile_schema_version, coded_result.profile_schema_version, 'CNIG profile schema version'), (lock.cnig…`.
3. Iterates `(configured, actual, label)` over `comparisons`. For each value: Checks `configured != actual`. When true: Raises `BessPlanningFeaturePolicyError(f'Policy source lock differs from validated {label}')`.

**Validation and invariants**

- Rejects or diverts the path when `configured != actual` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `compile_bess_planning_feature_policy`
- `src/landscout/stages/bess_planning_feature_policy.py` — `validate_bess_planning_feature_policy_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_dictionary_by_pair`

**Signature**

```python
def _dictionary_by_pair(
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

**Purpose**

Implements dictionary by pair according to the exact implementation and guards in this file.

**Inputs**

- `coded_result` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[tuple[str, str, str], dict[str, object]]`. Observed return expression(s): `indexed`.

**Algorithm**

1. Computes `rows` from `coded_result.code_dictionary.to_dict('records')`.
2. Defines `indexed` with annotation `dict[tuple[str, str, str], dict[str, object]]` from `{}`.
3. Iterates `row` over `rows`. For each value: Computes `key` from `(str(row['feature_family']), str(row['type_code']), str(row['subtype_code']))`. Checks `key in indexed`. When true: Raises `BessPlanningFeaturePolicyError('Validated CNIG code dictionary contains a duplicate pair')`. Computes `indexed[key]` from `row`.
4. Returns `indexed`.

**Validation and invariants**

- Rejects or diverts the path when `key in indexed` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`, `coded_result.code_dictionary.to_dict`, `str`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_validate_policy_completeness`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_policy_completeness`

**Signature**

```python
def _validate_policy_completeness(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

**Purpose**

Validates and rejects malformed policy completeness according to the exact implementation and guards in this file.

**Inputs**

- `config` (`BessPlanningFeaturePolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded_result` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[tuple[str, str, str], dict[str, object]]`. Observed return expression(s): `dictionary`.

**Algorithm**

1. Computes `dictionary` from `_dictionary_by_pair(coded_result)`.
2. Defines `entries` with annotation `dict[tuple[str, str, str], PolicyEntry]` from `{(entry.feature_family, entry.type_code, entry.subtype_code): entry for entry in config.entries}`.
3. Computes `missing` from `sorted(set(dictionary) - set(entries))`.
4. Computes `extra` from `sorted(set(entries) - set(dictionary))`.
5. Checks `missing`. When true: Raises `BessPlanningFeaturePolicyError(f'Policy is missing validated CNIG pair(s): {missing}')`.
6. Checks `extra`. When true: Raises `BessPlanningFeaturePolicyError(f'Policy contains extra CNIG pair(s): {extra}')`.
7. Iterates `(key, row)` over `dictionary.items()`. For each value: Computes `entry` from `entries[key]`. Checks `entry.expected_official_label != row['official_label']`. When true: Raises `BessPlanningFeaturePolicyError(f'Policy official label mismatch for pair {key}')`. Checks `not _null_safe_equal(entry.expected_legal_reference, row['legal_reference'])`. When true: Raises `BessPlanningFeaturePolicyError(f'Policy legal reference mismatch for pair {key}')`. Executes 1 additional source-ordered statement(s).
8. Returns `dictionary`.

**Validation and invariants**

- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `extra` is true.
- Rejects or diverts the path when `entry.expected_official_label != row['official_label']` is true.
- Rejects or diverts the path when `not _null_safe_equal(entry.expected_legal_reference, row['legal_reference'])` is true.
- Rejects or diverts the path when `not _null_safe_equal(entry.expected_regulation_reference, row['regulation_or_annex_reference'])` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`, `_dictionary_by_pair`, `_null_safe_equal`, `dictionary.items`, `set`, `sorted`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_table`

**Signature**

```python
def _policy_table(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
    dictionary: dict[tuple[str, str, str], dict[str, object]],
    policy_hash: str,
) -> pd.DataFrame:
```

**Purpose**

Implements policy table according to the exact implementation and guards in this file.

**Inputs**

- `config` (`BessPlanningFeaturePolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded_result` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `dictionary` (`dict[tuple[str, str, str], dict[str, object]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_hash` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Defines `rows` with annotation `list[dict[str, object]]` from `[]`.
2. Iterates `entry` over `config.entries`. For each value: Computes `key` from `(entry.feature_family, entry.type_code, entry.subtype_code)`. Computes `official` from `dictionary[key]`. Calls `rows.append({'feature_family': entry.feature_family, 'type_code': entry.type_code, 'subtype_code': entry.subtype_code, 'official_label': official['official_label'], 'official_legal_reference': official['legal_reference'], 'official_regulation_reference': official['regulation_or_annex_reference'], 'precheck_status': entry.precheck_status, 'confidence': entry…` for its validation or side effect.
3. Computes `output` from `pd.DataFrame(rows, columns=POLICY_TABLE_COLUMNS)`.
4. Computes `string_columns` from `tuple((column for column in POLICY_TABLE_COLUMNS if column not in {'status_priority', 'local_feature_text_interpreted', 'local_regulation_content_interpreted', 'legal_conclusion_produced'}))`.
5. Iterates `column` over `string_columns`. For each value: Computes `output[column]` from `pd.array(output[column].tolist(), dtype='str')`.
6. Computes `output['status_priority']` from `output['status_priority'].astype('int64')`.
7. Iterates `column` over `('local_feature_text_interpreted', 'local_regulation_content_interpreted', 'legal_conclusion_produced')`. For each value: Computes `output[column]` from `output[column].astype('bool')`.
8. Computes `output.index` from `pd.Index(output.index.to_numpy(copy=True), name=output.index.name)`.
9. Returns `output`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `output.index.to_numpy`, `output['status_priority'].astype`, `output[column].astype`, `output[column].tolist`, `pd.DataFrame`, `pd.Index`, `pd.array`, `rows.append`, `tuple`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_component_metadata`

**Signature**

```python
def _component_metadata(result: BessPlanningFeaturePolicyResult) -> dict[str, object]:
```

**Purpose**

Implements component metadata according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeaturePolicyResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'policy_schema_version': result.policy_schema_version, 'result_hash_schema_version': result.result_hash_schema_version, 'policy_profile': result.policy_profile, 'policy_scope': result.policy_scope, 'policy_sha256': result.policy_sha256, 'source_document_id': result.source_document_id, 'source_archive_sha256': result.source_archive_sha256, 'cnig_profile': result.cnig_profile, 'cnig_profile_schema…`.

**Algorithm**

1. Returns `{'policy_schema_version': result.policy_schema_version, 'result_hash_schema_version': result.result_hash_schema_version, 'policy_profile': result.policy_profile, 'policy_scope': result.policy_scope, 'policy_sha256': result.policy_sha256, 'source_document_id': result.source_document_id, 'source_archive_sha256': result.source_archive_sha256, 'cnig_profile': r…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_complete_result_sha256`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_policy_table_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_table_sha256`

**Signature**

```python
def _policy_table_sha256(result: BessPlanningFeaturePolicyResult) -> str:
```

**Purpose**

Implements policy table sha256 according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeaturePolicyResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256({'domain': 'landscout.bess_cnig_feature_policy.table', **_component_metadata(result), 'frame': _frame_payload(result.policy_table)})`.

**Algorithm**

1. Returns `_canonical_json_sha256({'domain': 'landscout.bess_cnig_feature_policy.table', **_component_metadata(result), 'frame': _frame_payload(result.policy_table)})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_json_sha256`, `_component_metadata`, `_frame_payload`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_result_with_hashes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_complete_result_sha256`

**Signature**

```python
def _complete_result_sha256(result: BessPlanningFeaturePolicyResult) -> str:
```

**Purpose**

Implements complete result sha256 according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeaturePolicyResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256({'domain': 'landscout.bess_cnig_feature_policy.result', **_component_metadata(result), 'policy_table_content_sha256': result.policy_table_content_sha256})`.

**Algorithm**

1. Returns `_canonical_json_sha256({'domain': 'landscout.bess_cnig_feature_policy.result', **_component_metadata(result), 'policy_table_content_sha256': result.policy_table_content_sha256})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_json_sha256`, `_component_metadata`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_result_with_hashes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_result_with_hashes`

**Signature**

```python
def _result_with_hashes(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
```

**Purpose**

Implements result with hashes according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeaturePolicyResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeaturePolicyResult`. Observed return expression(s): `replace(component, complete_result_content_sha256=_complete_result_sha256(component))`.

**Algorithm**

1. Computes `component` from `replace(result, policy_table_content_sha256=_policy_table_sha256(result))`.
2. Returns `replace(component, complete_result_content_sha256=_complete_result_sha256(component))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_complete_result_sha256`, `_policy_table_sha256`, `replace`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_build_result`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_policy_table_rows`

**Signature**

```python
def _validate_policy_table_rows(result: BessPlanningFeaturePolicyResult) -> None:
```

**Purpose**

Validates and rejects malformed policy table rows according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeaturePolicyResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Defines `records` with annotation `dict[tuple[str, str, str], dict[str, object]]` from `{}`.
2. Defines `ordered_keys` with annotation `list[tuple[str, str, str]]` from `[]`.
3. Defines `priority_to_status` with annotation `dict[int, str]` from `{}`.
4. Defines `status_to_priority` with annotation `dict[str, int]` from `{}`.
5. Iterates `(position, row)` over `enumerate(result.policy_table.to_dict('records'))`. For each value: Computes `family` from `row['feature_family']`. Computes `type_code` from `row['type_code']`. Computes `subtype_code` from `row['subtype_code']`. Executes 20 additional source-ordered statement(s).
6. Checks `ordered_keys != sorted(ordered_keys)`. When true: Raises `BessPlanningFeaturePolicyError('policy table pair order is not canonical')`.

**Validation and invariants**

- Rejects or diverts the path when `ordered_keys != sorted(ordered_keys)` is true.
- Rejects or diverts the path when `family not in {'PRESCRIPTION', 'INFORMATION'}` is true.
- Rejects or diverts the path when `key in records` is true.
- Rejects or diverts the path when `status not in ALLOWED_STATUSES` is true.
- Rejects or diverts the path when `confidence not in ALLOWED_CONFIDENCES` is true.
- Rejects or diverts the path when `type(priority) is not int or priority <= 0` is true.
- Rejects or diverts the path when `previous_status != status or previous_priority != priority` is true.
- Rejects or diverts the path when `row['policy_scope'] != result.policy_scope` is true.
- Rejects or diverts the path when `row['policy_profile'] != result.policy_profile or row['policy_sha256'] != result.policy_sha256 or row['cnig_profile'] != result.cnig_profile or (row['cnig_profile_sha256'] != result.cnig_profile_sha256) or (row['cnig_complete_result_content_sha256'] != result.cnig_complete_result_content_sha256)` is true.
- Rejects or diverts the path when `not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None` is true.
- Rejects or diverts the path when `isinstance(value, str) and value in NULL_REFERENCE_LITERALS` is true.
- Rejects or diverts the path when `row[field] is not False` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`, `CODE_PATTERN.fullmatch`, `_exact_string`, `_null_value`, `enumerate`, `isinstance`, `ordered_keys.append`, `priority_to_status.setdefault`, `result.policy_table.to_dict`, `sorted`, `status_to_priority.setdefault`, `str`, `type`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_result`

**Signature**

```python
def _build_result(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> BessPlanningFeaturePolicyResult:
```

**Purpose**

Builds result according to the exact implementation and guards in this file.

**Inputs**

- `config` (`BessPlanningFeaturePolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded_result` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeaturePolicyResult`. Observed return expression(s): `_result_with_hashes(result)`.

**Algorithm**

1. Computes `dictionary` from `_validate_policy_completeness(config, coded_result)`.
2. Computes `policy_hash` from `_policy_sha256(config)`.
3. Computes `result` from `BessPlanningFeaturePolicyResult(policy_schema_version=config.schema_version, result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION, policy_profile=config.profile, policy_scope=config.policy_scope, policy_sha256=policy_hash, source_document_id=coded_result.source_document_id, source_archive_sha256=coded_result.source_a…`.
4. Returns `_result_with_hashes(result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyResult`, `_policy_sha256`, `_policy_table`, `_result_with_hashes`, `_validate_policy_completeness`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `compile_bess_planning_feature_policy`
- `src/landscout/stages/bess_planning_feature_policy.py` — `validate_bess_planning_feature_policy_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result_envelope`

**Signature**

```python
def _validate_result_envelope(result: BessPlanningFeaturePolicyResult) -> None:
```

**Purpose**

Validates and rejects malformed result envelope according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeaturePolicyResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `type(result) is not BessPlanningFeaturePolicyResult`. When true: Raises `BessPlanningFeaturePolicyError('result must be a BessPlanningFeaturePolicyResult')`.
2. Iterates `(version, expected, label)` over `((result.policy_schema_version, POLICY_SCHEMA_VERSION, 'policy schema'), (result.result_hash_schema_version, RESULT_HASH_SCHEMA_VERSION, 'result hash schema'), (result.cnig_profile_schema_version, 2, 'CNIG profile schema'), (result.cnig_result_hash_schema_version, 5, 'CNIG result hash schema'))`. For each value: Checks `type(version) is not int or version != expected`. When true: Raises `BessPlanningFeaturePolicyError(f'unsupported {label} version')`.
3. Checks `result.policy_scope != POLICY_SCOPE`. When true: Raises `BessPlanningFeaturePolicyError('result policy scope is invalid')`.
4. Iterates `(value, label)` over `((result.policy_profile, 'policy profile'), (result.source_document_id, 'source document ID'), (result.cnig_profile, 'CNIG profile'))`. For each value: Runs guarded operation: Calls `_exact_string(value, label)` for its validation or side effect. Handles `ValueError`.
5. Checks `not isinstance(result.policy_table, pd.DataFrame) or isinstance(result.policy_table, gpd.GeoDataFrame)`. When true: Raises `BessPlanningFeaturePolicyError('policy table must be a DataFrame')`.
6. Checks `result.policy_table.columns.duplicated().any() or tuple(result.policy_table.columns) != POLICY_TABLE_COLUMNS`. When true: Raises `BessPlanningFeaturePolicyError('policy table schema is invalid')`.
7. Checks `deterministic_frame_schema_signature(result.policy_table) != POLICY_TABLE_SCHEMA_SIGNATURE`. When true: Raises `BessPlanningFeaturePolicyError('policy table schema is invalid')`.
8. Checks `result.policy_table.empty`. When true: Raises `BessPlanningFeaturePolicyError('policy table must contain at least one policy entry')`.
9. Iterates `field` over `POLICY_RESULT_SCALAR_FIELDS`. For each value: Checks `not field.endswith('_sha256')`. When true: Executes `continue` control flow. Runs guarded operation: Calls `_sha256_string(getattr(result, field), field)` for its validation or side effect. Handles `ValueError`.
10. Calls `_validate_policy_table_rows(result)` for its validation or side effect.
11. Computes `rebuilt` from `_result_with_hashes(result)`.
12. Checks `result.policy_table_content_sha256 != rebuilt.policy_table_content_sha256`. When true: Raises `BessPlanningFeaturePolicyError('policy table hash is invalid')`.
13. Checks `result.complete_result_content_sha256 != rebuilt.complete_result_content_sha256`. When true: Raises `BessPlanningFeaturePolicyError('complete result hash is invalid')`.

**Validation and invariants**

- Rejects or diverts the path when `type(result) is not BessPlanningFeaturePolicyResult` is true.
- Rejects or diverts the path when `result.policy_scope != POLICY_SCOPE` is true.
- Rejects or diverts the path when `not isinstance(result.policy_table, pd.DataFrame) or isinstance(result.policy_table, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `result.policy_table.columns.duplicated().any() or tuple(result.policy_table.columns) != POLICY_TABLE_COLUMNS` is true.
- Rejects or diverts the path when `deterministic_frame_schema_signature(result.policy_table) != POLICY_TABLE_SCHEMA_SIGNATURE` is true.
- Rejects or diverts the path when `result.policy_table.empty` is true.
- Rejects or diverts the path when `result.policy_table_content_sha256 != rebuilt.policy_table_content_sha256` is true.
- Rejects or diverts the path when `result.complete_result_content_sha256 != rebuilt.complete_result_content_sha256` is true.
- Rejects or diverts the path when `type(version) is not int or version != expected` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`, `_exact_string`, `_result_with_hashes`, `_sha256_string`, `_validate_policy_table_rows`, `deterministic_frame_schema_signature`, `field.endswith`, `getattr`, `isinstance`, `result.policy_table.columns.duplicated`, `result.policy_table.columns.duplicated().any`, `str`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `compile_bess_planning_feature_policy`
- `src/landscout/stages/bess_planning_feature_policy.py` — `load_bess_planning_feature_policy_artifacts`
- `src/landscout/stages/bess_planning_feature_policy.py` — `validate_bess_planning_feature_policy_result_envelope`
- `src/landscout/stages/bess_planning_feature_policy.py` — `validate_bess_planning_feature_policy_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_bess_planning_feature_policy_result_envelope`

**Signature**

```python
def validate_bess_planning_feature_policy_result_envelope(
    result: BessPlanningFeaturePolicyResult,
) -> None:
```

**Purpose**

Validate one compiled-policy envelope without rebuilding CNIG sources.

**Inputs**

- `result` (`BessPlanningFeaturePolicyResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `_validate_result_envelope(result)` for its validation or side effect. Handles `BessPlanningFeaturePolicyError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`, `_validate_result_envelope`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `load_bess_planning_feature_application_artifacts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_unique_json_object`

**Signature**

```python
def _unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
```

**Purpose**

Implements unique json object according to the exact implementation and guards in this file.

**Inputs**

- `pairs` (`list[tuple[str, object]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `output`.

**Algorithm**

1. Defines `output` with annotation `dict[str, object]` from `{}`.
2. Iterates `(key, value)` over `pairs`. For each value: Checks `key in output`. When true: Raises `BessPlanningFeaturePolicyError(f'Duplicate JSON artifact key: {key!r}')`. Computes `output[key]` from `value`.
3. Returns `output`.

**Validation and invariants**

- Rejects or diverts the path when `key in output` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_bess_planning_feature_policy_artifacts`

**Signature**

```python
def load_bess_planning_feature_policy_artifacts(
    parquet_path: str | Path,
    manifest_path: str | Path,
) -> BessPlanningFeaturePolicyResult:
```

**Purpose**

Load and locally validate one physically sealed compiled-policy artifact.

**Inputs**

- `parquet_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `manifest_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeaturePolicyResult`. Observed return expression(s): `result`.

**Algorithm**

1. Runs guarded operation: Computes `parquet` from `Path(parquet_path)`. Computes `manifest_file` from `Path(manifest_path)`. Computes `payload` from `json.loads(manifest_file.read_text(encoding='utf-8'), object_pairs_hook=_unique_json_object)`. Computes `manifest` from `BessPlanningFeaturePolicyArtifactManifest.model_validate(payload)`. Executes 12 additional source-ordered statement(s). Handles `BessPlanningFeaturePolicyError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `manifest.parquet_filename != parquet.name` is true.
- Rejects or diverts the path when `len(parquet_payload) != manifest.parquet_size_bytes` is true.
- Rejects or diverts the path when `sha256(parquet_payload).hexdigest() != manifest.parquet_sha256` is true.
- Rejects or diverts the path when `len(table) != manifest.parquet_row_count` is true.
- Rejects or diverts the path when `actual_schema != declared_schema` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `manifest_file.read_text`, `parquet.read_bytes`, `pd.read_parquet`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessPlanningFeaturePolicyArtifactManifest.model_validate`, `BessPlanningFeaturePolicyError`, `BessPlanningFeaturePolicyResult`, `BytesIO`, `Path`, `_validate_result_envelope`, `deterministic_frame_schema_signature`, `getattr`, `json.loads`, `len`, `manifest.policy_table_schema_signature.model_dump`, `manifest_file.read_text`, `parquet.read_bytes`, `pd.read_parquet`, `sha256`, `sha256(parquet_payload).hexdigest`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_coded_source`

**Signature**

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

Validates and rejects malformed coded source according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `code_profile` (`CnigFeatureCodeProfile | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded_result` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `validate_planning_feature_code_result(planning_document, parcels, surface_features, line_features, point_features, relations, code_profile, coded_result)` for its validation or side effect. Handles `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`, `validate_planning_feature_code_result`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `compile_bess_planning_feature_policy`
- `src/landscout/stages/bess_planning_feature_policy.py` — `validate_bess_planning_feature_policy_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `compile_bess_planning_feature_policy`

**Signature**

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

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `code_profile` (`CnigFeatureCodeProfile | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded_result` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_config` (`BessPlanningFeaturePolicyConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeaturePolicyResult`. Observed return expression(s): `result`.

**Algorithm**

1. Runs guarded operation: Computes `config` from `_resolved_policy_config(policy_config)`. Calls `_validate_source_lock(config, coded_result)` for its validation or side effect. Calls `_validate_coded_source(planning_document, parcels, surface_features, line_features, point_features, relations, code_profile, coded_result)` for its validation or side effect. Computes `result` from `_build_result(config, coded_result)`. Executes 2 additional source-ordered statement(s). Handles `BessPlanningFeaturePolicyError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`, `_build_result`, `_resolved_policy_config`, `_validate_coded_source`, `_validate_result_envelope`, `_validate_source_lock`.

**Known repository callers**

- `tests/unit/test_bess_planning_feature_policy.py` — `_compiled_fixture`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_extra_policy_pair_is_rejected_without_type_fallback`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_in_memory_config_is_revalidated_before_compilation`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_missing_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_official_meaning_mismatch_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_prescription_information_code_spaces_remain_separate`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_source_lock_mismatch_is_rejected`

**Tests**

- `tests/unit/test_bess_planning_feature_policy.py::test_extra_policy_pair_is_rejected_without_type_fallback`
- `tests/unit/test_bess_planning_feature_policy.py::test_in_memory_config_is_revalidated_before_compilation`
- `tests/unit/test_bess_planning_feature_policy.py::test_missing_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_official_meaning_mismatch_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_prescription_information_code_spaces_remain_separate`
- `tests/unit/test_bess_planning_feature_policy.py::test_source_lock_mismatch_is_rejected`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_bess_planning_feature_policy_result`

**Signature**

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

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `code_profile` (`CnigFeatureCodeProfile | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded_result` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_config` (`BessPlanningFeaturePolicyConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`BessPlanningFeaturePolicyResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `_validate_result_envelope(result)` for its validation or side effect. Computes `config` from `_resolved_policy_config(policy_config)`. Calls `_validate_source_lock(config, coded_result)` for its validation or side effect. Calls `_validate_coded_source(planning_document, parcels, surface_features, line_features, point_features, relations, code_profile, coded_result)` for its validation or side effect. Executes 3 additional source-ordered statement(s). Handles `BessPlanningFeaturePolicyError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `_frame_payload(result.policy_table) != _frame_payload(expected.policy_table)` is true.
- Rejects or diverts the path when `getattr(result, field) != getattr(expected, field)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeaturePolicyError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyError`, `_build_result`, `_frame_payload`, `_resolved_policy_config`, `_validate_coded_source`, `_validate_result_envelope`, `_validate_source_lock`, `getattr`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_validate_policy_source`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_coordinated_policy_table_and_hash_mutation_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_persisted_parquet_and_json_readback_is_source_complete`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_table_mutation_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status`

**Tests**

- `tests/unit/test_bess_planning_feature_policy.py::test_coordinated_policy_table_and_hash_mutation_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_persisted_parquet_and_json_readback_is_source_complete`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_table_mutation_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `BESS_CNIG_FEATURE_POLICY_RESULT` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `CONTEXT_REVIEW_REQUIRED` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `DESIGN_REVIEW_REQUIRED` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `HIGH` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `INFORMATION` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `LIKELY_MATERIAL_CONSTRAINT` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LOW` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `MATERIAL_REVIEW_REQUIRED` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `MEDIUM` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `OFFICIAL_CNIG_CODE_MEANING_ONLY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `PRESCRIPTION` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `UNKNOWN` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `cnig_complete_result_content_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `cnig_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `cnig_profile_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_family` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `legal_conclusion_produced` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `legal_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `limitations` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `local_feature_text_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `local_regulation_content_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_legal_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_regulation_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `policy_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `policy_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `policy_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `rationale` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `regulation_or_annex_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `required_human_action` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `status_priority` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `subtype_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `type_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `planning` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
