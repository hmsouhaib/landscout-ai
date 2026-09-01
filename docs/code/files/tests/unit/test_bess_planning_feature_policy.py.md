# `tests/unit/test_bess_planning_feature_policy.py`

## File identity

- Repository path: `tests/unit/test_bess_planning_feature_policy.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.
- Source SHA256: `49d02758c7dd407fe95e10340c0b80d7da71cb9d39b27aac18f5cfacca9888d8`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for bess planning feature policy; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import importlib`
- `import json`
- `import tomllib`
- `from dataclasses import fields, replace`
- `from hashlib import sha256`
- `from io import BytesIO`
- `from pathlib import Path`

### Third-party packages

- `import pandas as pd`
- `import pytest`
- `from pandas.testing import assert_frame_equal`
- `from pydantic import ValidationError`
- `from test_resolve_planning_feature_codes import _integration_inputs`

### Internal LandScout imports

- `from landscout import stages`
- `from landscout.common.artifact_paths import validate_portable_parquet_filename`
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature`
- `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`
- `from landscout.stages.resolve_planning_feature_codes import (
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `POLICY_PATH`

- Category: module constant or closed domain.
- Exact declaration:

```python
POLICY_PATH = Path("configs/planning/muret_bess_cnig_feature_policy.yaml")
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

### `STATUS_PRIORITIES`

- Category: module constant or closed domain.
- Exact declaration:

```python
STATUS_PRIORITIES = {
    "LIKELY_MATERIAL_CONSTRAINT": 50,
    "UNKNOWN": 40,
    "MATERIAL_REVIEW_REQUIRED": 30,
    "DESIGN_REVIEW_REQUIRED": 20,
    "CONTEXT_REVIEW_REQUIRED": 10,
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact mapping keys:
  - `LIKELY_MATERIAL_CONSTRAINT`
  - `UNKNOWN`
  - `MATERIAL_REVIEW_REQUIRED`
  - `DESIGN_REVIEW_REQUIRED`
  - `CONTEXT_REVIEW_REQUIRED`

### `EXPECTED_MURET_DECISIONS`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXPECTED_MURET_DECISIONS = {
    ("INFORMATION", "02", "00"): ("CONTEXT_REVIEW_REQUIRED", "HIGH"),
    ("INFORMATION", "14", "00"): ("CONTEXT_REVIEW_REQUIRED", "HIGH"),
    ("INFORMATION", "27", "00"): ("CONTEXT_REVIEW_REQUIRED", "HIGH"),
    ("INFORMATION", "99", "00"): ("UNKNOWN", "LOW"),
    ("PRESCRIPTION", "01", "00"): ("LIKELY_MATERIAL_CONSTRAINT", "HIGH"),
    ("PRESCRIPTION", "05", "00"): ("MATERIAL_REVIEW_REQUIRED", "HIGH"),
    ("PRESCRIPTION", "07", "00"): ("LIKELY_MATERIAL_CONSTRAINT", "MEDIUM"),
    ("PRESCRIPTION", "07", "04"): ("LIKELY_MATERIAL_CONSTRAINT", "HIGH"),
    ("PRESCRIPTION", "15", "00"): ("DESIGN_REVIEW_REQUIRED", "MEDIUM"),
    ("PRESCRIPTION", "15", "01"): ("DESIGN_REVIEW_REQUIRED", "HIGH"),
    ("PRESCRIPTION", "17", "00"): ("MATERIAL_REVIEW_REQUIRED", "MEDIUM"),
    ("PRESCRIPTION", "18", "00"): ("MATERIAL_REVIEW_REQUIRED", "HIGH"),
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXPECTED_POLICY_ENTRIES_SHA256`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXPECTED_POLICY_ENTRIES_SHA256 = (
    "1d3e63f1123000402065b74402cb1e2295db2ac5655209ce410aaf36bfc2be91"
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXPECTED_POLICY_SHA256`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXPECTED_POLICY_SHA256 = (
    "1cfca0eb3d777e9b6604748e8a81609abe7b728de8d0695711cd569180df6489"
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXPECTED_POLICY_TABLE_SHA256`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXPECTED_POLICY_TABLE_SHA256 = (
    "225105fe488e21f8aa080751812dde1671340c26620cae1d8372c2e59488ed41"
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXPECTED_COMPLETE_RESULT_SHA256`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXPECTED_COMPLETE_RESULT_SHA256 = (
    "84a59b418f5a53bc61df73296964b2847cc5d3529c10d0c6912c96222edba09c"
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EXPECTED_SOURCE_LOCK`

- Category: module constant or closed domain.
- Exact declaration:

```python
EXPECTED_SOURCE_LOCK = {
    "document_id": "33edb4c9f6943c88d8d92518bff20bec",
    "archive_sha256": (
        "9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93"
    ),
    "cnig_profile": "cnig_plu_2017_muret_observed_pairs_v2",
    "cnig_profile_schema_version": 2,
    "cnig_profile_sha256": (
        "5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"
    ),
    "cnig_result_hash_schema_version": 5,
    "cnig_complete_result_content_sha256": (
        "b56b195b32914583e6599fe96b3d29977c52450c9755228d89ce7e192903ab3e"
    ),
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact mapping keys:
  - `document_id`
  - `archive_sha256`
  - `cnig_profile`
  - `cnig_profile_schema_version`
  - `cnig_profile_sha256`
  - `cnig_result_hash_schema_version`
  - `cnig_complete_result_content_sha256`

### `ARTIFACT_KIND`

- Category: module constant or closed domain.
- Exact declaration:

```python
ARTIFACT_KIND = "BESS_CNIG_FEATURE_POLICY_RESULT"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1.DerivedPolicyResult`

**Source purpose:** Defines `test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1.DerivedPolicyResult`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BessPlanningFeaturePolicyResult`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class DerivedPolicyResult(BessPlanningFeaturePolicyResult):
        pass
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_canonical_sha256`

**Purpose:** Implements `canonical sha256` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

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
  - `sha256(<br>        json.dumps(<br>            value,<br>            ensure_ascii=False,<br>            allow_nan=False,<br>            sort_keys=True,<br>            separators=(",", ":"),<br>        ).encode("utf-8")<br>    ).hexdigest()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_bess_planning_feature_policy::_policy_payload` via `_canonical_sha256`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_policy_payload` via `_canonical_sha256`
- direct call: `tests.unit.test_bess_planning_feature_policy::_validated_config` via `_canonical_sha256`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_validated_config` via `_canonical_sha256`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_checked_in_policy_complete_snapshot_is_immutable` via `_canonical_sha256`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_checked_in_policy_complete_snapshot_is_immutable` via `_canonical_sha256`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_profile_v1_snapshot_detects_policy_text_drift` via `_canonical_sha256`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_profile_v1_snapshot_detects_policy_text_drift` via `_canonical_sha256`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_profile_v1_snapshot_detects_source_lock_drift` via `_canonical_sha256`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_profile_v1_snapshot_detects_source_lock_drift` via `_canonical_sha256`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_duplicate_policy_pair_is_rejected` via `_canonical_sha256`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_duplicate_policy_pair_is_rejected` via `_canonical_sha256`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_invalid_or_legal_conclusion_status_is_rejected` via `_canonical_sha256`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_invalid_or_legal_conclusion_status_is_rejected` via `_canonical_sha256`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_invalid_confidence_is_rejected` via `_canonical_sha256`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_invalid_confidence_is_rejected` via `_canonical_sha256`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_noncanonical_whitespace_is_rejected` via `_canonical_sha256`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_noncanonical_whitespace_is_rejected` via `_canonical_sha256`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_entries_require_deterministic_order` via `_canonical_sha256`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_entries_require_deterministic_order` via `_canonical_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sha256(<br>        json.dumps(<br>            value,<br>            ensure_ascii=False,<br>            allow_nan=False,<br>            sort_keys=True,<br>            separators=(",", ":"),<br>        ).encode("utf-8")<br>    ).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `json.dumps(<br>            value,<br>            ensure_ascii=False,<br>            allow_nan=False,<br>            sort_keys=True,<br>            separators=(",", ":"),<br>        ).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(<br>        json.dumps(<br>            value,<br>            ensure_ascii=False,<br>            allow_nan=False,<br>            sort_keys=True,<br>            separators=(",", ":"),<br>        ).encode("utf-8")<br>    ).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _canonical_sha256(value: object) -> str:
    return sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_policy_entry`

**Purpose:** Implements `policy entry` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _policy_entry(row: object, position: int) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `row` | positional-or-keyword | `object` | `required` |
| `position` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "feature_family": row.feature_family,<br>        "type_code": row.type_code,<br>        "subtype_code": row.subtype_code,<br>        "expected_official_label": row.official_label,<br>        "expected_legal_reference": (<br>            None if pd.isna(legal_reference) else legal_reference<br>        ),<br>        "expected_regulation_reference": (<br>            None if pd.isna(regulation_reference) else regulation_reference<br>        ),<br>        "precheck_status": status,<br>        "confidence": ("HIGH", "MEDIUM", "LOW")[position % 3],<br>        "rationale": f"Official pair {row.feature_family} {row.type_code}/{row.subtype_code} requires conservative review.",<br>        "required_human_action": "Review the official code meaning and the separate local planning material.",<br>        "limitations": "This entry does not interpret local text or establish authorization or prohibition.",<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_bess_planning_feature_policy::_policy_payload` via `_policy_entry`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_policy_payload` via `_policy_entry`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |

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
def _policy_entry(row: object, position: int) -> dict[str, object]:
    statuses = tuple(STATUS_PRIORITIES)
    status = statuses[position % len(statuses)]
    legal_reference = row.legal_reference
    regulation_reference = row.regulation_or_annex_reference
    return {
        "feature_family": row.feature_family,
        "type_code": row.type_code,
        "subtype_code": row.subtype_code,
        "expected_official_label": row.official_label,
        "expected_legal_reference": (
            None if pd.isna(legal_reference) else legal_reference
        ),
        "expected_regulation_reference": (
            None if pd.isna(regulation_reference) else regulation_reference
        ),
        "precheck_status": status,
        "confidence": ("HIGH", "MEDIUM", "LOW")[position % 3],
        "rationale": f"Official pair {row.feature_family} {row.type_code}/{row.subtype_code} requires conservative review.",
        "required_human_action": "Review the official code meaning and the separate local planning material.",
        "limitations": "This entry does not interpret local text or establish authorization or prohibition.",
    }
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_compiled_fixture`

**Purpose:** Implements `compiled fixture` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _compiled_fixture() -> tuple[
    tuple[object, ...],
    object,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[tuple[object, ...], object, BessPlanningFeaturePolicyConfig, BessPlanningFeaturePolicyResult]`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `inputs, coded, config, result`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_bess_planning_feature_policy::test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_information_9900_official_references_remain_missing` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_information_9900_official_references_remain_missing` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_null_reference_literal_is_rejected_by_local_envelope` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_null_reference_literal_is_rejected_by_local_envelope` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_source_lock_mismatch_is_rejected` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_source_lock_mismatch_is_rejected` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_status_priority_mapping_is_deeply_immutable` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_status_priority_mapping_is_deeply_immutable` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_in_memory_config_is_revalidated_before_compilation` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_in_memory_config_is_revalidated_before_compilation` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_table_is_sorted_and_preserves_leading_zero_codes` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_table_is_sorted_and_preserves_leading_zero_codes` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_table_mutation_is_rejected` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_table_mutation_is_rejected` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_coordinated_policy_table_and_hash_mutation_is_rejected` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_coordinated_policy_table_and_hash_mutation_is_rejected` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_persisted_parquet_and_json_readback_is_source_complete` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_persisted_parquet_and_json_readback_is_source_complete` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_artifact_manifest_model_is_strict_and_frozen` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_manifest_model_is_strict_and_frozen` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_rejects_manifest_mismatch` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_rejects_manifest_mismatch` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_uses_strict_json_before_parquet_read` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_uses_strict_json_before_parquet_read` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_rejects_parquet_replacement` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_rejects_parquet_replacement` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_parses_the_exact_verified_parquet_bytes` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_parses_the_exact_verified_parquet_bytes` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_locally_invalid_result_fast_fails_before_source_validation` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_locally_invalid_result_fast_fails_before_source_validation` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_forged_matching_lock_still_runs_source_complete_validation` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_forged_matching_lock_still_runs_source_complete_validation` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_manifest_rejects_nonportable_parquet_filename` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_manifest_rejects_nonportable_parquet_filename` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_manifest_rejects_unsupported_cnig_source_schema` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_manifest_rejects_unsupported_cnig_source_schema` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_artifact_loader_rejects_source_schema_before_parquet_read` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_artifact_loader_rejects_source_schema_before_parquet_read` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_rejects_canonical_empty_policy_table` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_rejects_canonical_empty_policy_table` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_accepts_one_exact_policy_row` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_accepts_one_exact_policy_row` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_requires_cnig_profile_schema_two` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_requires_cnig_profile_schema_two` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_requires_cnig_result_schema_five` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_requires_cnig_result_schema_five` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_validates_every_intrinsic_row_contract` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_validates_every_intrinsic_row_contract` via `_compiled_fixture`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1` via `_compiled_fixture`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1` via `_compiled_fixture`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `compile_bess_planning_feature_policy` | `landscout.stages.bess_planning_feature_policy.compile_bess_planning_feature_policy` |

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
def _compiled_fixture() -> tuple[
    tuple[object, ...],
    object,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
]:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    config = BessPlanningFeaturePolicyConfig.model_validate(
        _policy_payload(inputs, coded)
    )
    result = compile_bess_planning_feature_policy(*inputs, coded, config)
    return inputs, coded, config, result
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_policy_payload`

**Purpose:** Implements `policy payload` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _policy_payload(inputs: tuple[object, ...], coded: object) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `inputs` | positional-or-keyword | `tuple[object, ...]` | `required` |
| `coded` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "schema_version": 1,<br>        "profile": "synthetic_bess_cnig_feature_policy_v1",<br>        "policy_scope": POLICY_SCOPE,<br>        "local_feature_text_interpreted": False,<br>        "local_regulation_content_interpreted": False,<br>        "legal_conclusion_produced": False,<br>        "source_lock": {<br>            "document_id": coded.source_document_id,<br>            "archive_sha256": coded.source_archive_sha256,<br>            "cnig_profile": coded.profile,<br>            "cnig_profile_schema_version": coded.profile_schema_version,<br>            "cnig_profile_sha256": coded.profile_sha256,<br>            "cnig_result_hash_schema_version": coded.result_hash_schema_version,<br>            "cnig_complete_result_content_sha256": (<br>                coded.complete_result_content_sha256<br>            ),<br>        },<br>        "status_priority": dict(STATUS_PRIORITIES),<br>        "canonical_policy_entries_sha256": _canonical_sha256(entries),<br>        "entries": entries,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_bess_planning_feature_policy::_compiled_fixture` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_compiled_fixture` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_missing_policy_pair_is_rejected` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_missing_policy_pair_is_rejected` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_extra_policy_pair_is_rejected_without_type_fallback` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_extra_policy_pair_is_rejected_without_type_fallback` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_duplicate_policy_pair_is_rejected` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_duplicate_policy_pair_is_rejected` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_prescription_information_code_spaces_remain_separate` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_prescription_information_code_spaces_remain_separate` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_official_meaning_mismatch_is_rejected` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_official_meaning_mismatch_is_rejected` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_invalid_or_legal_conclusion_status_is_rejected` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_invalid_or_legal_conclusion_status_is_rejected` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_invalid_confidence_is_rejected` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_invalid_confidence_is_rejected` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_status_priority_contract_is_strict` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_status_priority_contract_is_strict` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_unknown_yaml_field_is_rejected` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_unknown_yaml_field_is_rejected` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_noncanonical_whitespace_is_rejected` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_noncanonical_whitespace_is_rejected` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_malformed_sha256_is_rejected` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_malformed_sha256_is_rejected` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_entries_require_deterministic_order` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_entries_require_deterministic_order` via `_policy_payload`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `_policy_payload`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `_policy_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_policy_entry` | `tests.unit.test_bess_planning_feature_policy._policy_entry` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `coded.code_dictionary.itertuples` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_sha256` | `tests.unit.test_bess_planning_feature_policy._canonical_sha256` |

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
def _policy_payload(inputs: tuple[object, ...], coded: object) -> dict[str, object]:
    entries = [
        _policy_entry(row, position)
        for position, row in enumerate(
            coded.code_dictionary.itertuples(index=False),
        )
    ]
    return {
        "schema_version": 1,
        "profile": "synthetic_bess_cnig_feature_policy_v1",
        "policy_scope": POLICY_SCOPE,
        "local_feature_text_interpreted": False,
        "local_regulation_content_interpreted": False,
        "legal_conclusion_produced": False,
        "source_lock": {
            "document_id": coded.source_document_id,
            "archive_sha256": coded.source_archive_sha256,
            "cnig_profile": coded.profile,
            "cnig_profile_schema_version": coded.profile_schema_version,
            "cnig_profile_sha256": coded.profile_sha256,
            "cnig_result_hash_schema_version": coded.result_hash_schema_version,
            "cnig_complete_result_content_sha256": (
                coded.complete_result_content_sha256
            ),
        },
        "status_priority": dict(STATUS_PRIORITIES),
        "canonical_policy_entries_sha256": _canonical_sha256(entries),
        "entries": entries,
    }
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_validated_config`

**Purpose:** Implements `validated config` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _validated_config(payload: dict[str, object]) -> BessPlanningFeaturePolicyConfig:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeaturePolicyConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `payload` | positional-or-keyword | `dict[str, object]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `BessPlanningFeaturePolicyConfig.model_validate(payload)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert isinstance(entries, list)`

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_bess_planning_feature_policy::test_missing_policy_pair_is_rejected` via `_validated_config`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_missing_policy_pair_is_rejected` via `_validated_config`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_extra_policy_pair_is_rejected_without_type_fallback` via `_validated_config`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_extra_policy_pair_is_rejected_without_type_fallback` via `_validated_config`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_prescription_information_code_spaces_remain_separate` via `_validated_config`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_prescription_information_code_spaces_remain_separate` via `_validated_config`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_official_meaning_mismatch_is_rejected` via `_validated_config`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_official_meaning_mismatch_is_rejected` via `_validated_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_sha256` | `tests.unit.test_bess_planning_feature_policy._canonical_sha256` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |

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
| In-memory mutation | `payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)` |
| Direct parameter mutation | `payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)` |

**Complete source-ordered implementation**

```python
def _validated_config(payload: dict[str, object]) -> BessPlanningFeaturePolicyConfig:
    entries = payload["entries"]
    assert isinstance(entries, list)
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    return BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_artifact_manifest`

**Purpose:** Implements `artifact manifest` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _artifact_manifest(
    result: BessPlanningFeaturePolicyResult,
    parquet: Path,
) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |
| `parquet` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "schema_version": 2,<br>        "artifact_kind": ARTIFACT_KIND,<br>        **{name: getattr(result, name) for name in scalar_names},<br>        "parquet_filename": parquet.name,<br>        "parquet_row_count": len(result.policy_table),<br>        "parquet_size_bytes": parquet.stat().st_size,<br>        "parquet_sha256": sha256(parquet.read_bytes()).hexdigest(),<br>        "policy_table_schema_signature": deterministic_frame_schema_signature(<br>            result.policy_table<br>        ),<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_bess_planning_feature_policy::_write_artifacts` via `_artifact_manifest`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_write_artifacts` via `_artifact_manifest`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `fields` | `dataclasses.fields` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `parquet.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(parquet.read_bytes()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `parquet.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `parquet.stat`<br>`sha256(parquet.read_bytes()).hexdigest`<br>`parquet.read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(parquet.read_bytes()).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _artifact_manifest(
    result: BessPlanningFeaturePolicyResult,
    parquet: Path,
) -> dict[str, object]:
    scalar_names = tuple(
        field.name
        for field in fields(BessPlanningFeaturePolicyResult)
        if field.name != "policy_table"
    )
    return {
        "schema_version": 2,
        "artifact_kind": ARTIFACT_KIND,
        **{name: getattr(result, name) for name in scalar_names},
        "parquet_filename": parquet.name,
        "parquet_row_count": len(result.policy_table),
        "parquet_size_bytes": parquet.stat().st_size,
        "parquet_sha256": sha256(parquet.read_bytes()).hexdigest(),
        "policy_table_schema_signature": deterministic_frame_schema_signature(
            result.policy_table
        ),
    }
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_artifacts`

**Purpose:** Implements `write artifacts` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeaturePolicyResult,
) -> tuple[Path, Path, dict[str, object]]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[Path, Path, dict[str, object]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `parquet, manifest_path, manifest`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_bess_planning_feature_policy::test_persisted_parquet_and_json_readback_is_source_complete` via `_write_artifacts`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_persisted_parquet_and_json_readback_is_source_complete` via `_write_artifacts`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_artifact_manifest_model_is_strict_and_frozen` via `_write_artifacts`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_manifest_model_is_strict_and_frozen` via `_write_artifacts`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_rejects_manifest_mismatch` via `_write_artifacts`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_rejects_manifest_mismatch` via `_write_artifacts`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_uses_strict_json_before_parquet_read` via `_write_artifacts`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_uses_strict_json_before_parquet_read` via `_write_artifacts`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_rejects_parquet_replacement` via `_write_artifacts`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_rejects_parquet_replacement` via `_write_artifacts`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_parses_the_exact_verified_parquet_bytes` via `_write_artifacts`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_artifact_loader_parses_the_exact_verified_parquet_bytes` via `_write_artifacts`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_manifest_rejects_nonportable_parquet_filename` via `_write_artifacts`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_manifest_rejects_nonportable_parquet_filename` via `_write_artifacts`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_manifest_rejects_unsupported_cnig_source_schema` via `_write_artifacts`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_manifest_rejects_unsupported_cnig_source_schema` via `_write_artifacts`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_artifact_loader_rejects_source_schema_before_parquet_read` via `_write_artifacts`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_artifact_loader_rejects_source_schema_before_parquet_read` via `_write_artifacts`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.policy_table.to_parquet` | `unresolved local/third-party receiver; no ownership inferred` |
| `_artifact_manifest` | `tests.unit.test_bess_planning_feature_policy._artifact_manifest` |
| `manifest_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `result.policy_table.to_parquet`<br>`manifest_path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeaturePolicyResult,
) -> tuple[Path, Path, dict[str, object]]:
    parquet = tmp_path / "policy.parquet"
    manifest_path = tmp_path / "policy.json"
    result.policy_table.to_parquet(parquet, index=True)
    manifest = _artifact_manifest(result, parquet)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return parquet, manifest_path, manifest
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_checked_in_policy_result`

**Purpose:** Implements `checked in policy result` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _checked_in_policy_result() -> BessPlanningFeaturePolicyResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeaturePolicyResult`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `policy_module._build_result(config, locked_coded)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_bess_planning_feature_policy::test_checked_in_compiled_policy_result_hashes_are_pinned` via `_checked_in_policy_result`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_checked_in_compiled_policy_result_hashes_are_pinned` via `_checked_in_policy_result`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_accepts_current_twelve_row_snapshot` via `_checked_in_policy_result`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_accepts_current_twelve_row_snapshot` via `_checked_in_policy_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `load_bess_planning_feature_policy_config` | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config` |
| `load_cnig_feature_code_profile` | `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile` |
| `Path` | `pathlib.Path` |
| `importlib.import_module` | `importlib.import_module` |
| `replace` | `dataclasses.replace` |
| `cnig_module._dictionary` | `unresolved local/third-party receiver; no ownership inferred` |
| `policy_module._build_result` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _checked_in_policy_result() -> BessPlanningFeaturePolicyResult:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    cnig_profile = load_cnig_feature_code_profile(
        Path("configs/planning/cnig_plu_2017_feature_codes.yaml")
    )
    cnig_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    policy_module = importlib.import_module(
        "landscout.stages.bess_planning_feature_policy"
    )
    locked_coded = replace(
        coded,
        profile=config.source_lock.cnig_profile,
        profile_schema_version=config.source_lock.cnig_profile_schema_version,
        profile_sha256=config.source_lock.cnig_profile_sha256,
        source_document_id=config.source_lock.document_id,
        source_archive_sha256=config.source_lock.archive_sha256,
        result_hash_schema_version=(config.source_lock.cnig_result_hash_schema_version),
        complete_result_content_sha256=(
            config.source_lock.cnig_complete_result_content_sha256
        ),
        code_dictionary=cnig_module._dictionary(
            cnig_profile, config.source_lock.cnig_profile_sha256
        ),
    )
    return policy_module._build_result(config, locked_coded)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status`

**Purpose:** Regression invariant: valid exact policy compiles without applying feature or parcel status. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status() -> (
    None
):
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.policy_schema_version == 1`
  - `assert result.result_hash_schema_version == 1`
  - `assert result.policy_scope == POLICY_SCOPE`
  - `assert len(result.policy_table) == len(coded.code_dictionary)`
  - `assert not any(<br>        column in result.policy_table.columns<br>        for column in ("parcel_id", "planning_feature_id", "relation_type")<br>    )`
  - `assert result.policy_table["local_feature_text_interpreted"].eq(False).all()`
  - `assert result.policy_table["local_regulation_content_interpreted"].eq(False).all()`
  - `assert result.policy_table["legal_conclusion_produced"].eq(False).all()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `validate_bess_planning_feature_policy_result` | `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.policy_table["local_feature_text_interpreted"].eq(False).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.policy_table["local_feature_text_interpreted"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.policy_table["local_regulation_content_interpreted"].eq(False).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.policy_table["local_regulation_content_interpreted"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.policy_table["legal_conclusion_produced"].eq(False).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.policy_table["legal_conclusion_produced"].eq` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status() -> (
    None
):
    inputs, coded, config, result = _compiled_fixture()
    validate_bess_planning_feature_policy_result(*inputs, coded, config, result)
    assert result.policy_schema_version == 1
    assert result.result_hash_schema_version == 1
    assert result.policy_scope == POLICY_SCOPE
    assert len(result.policy_table) == len(coded.code_dictionary)
    assert not any(
        column in result.policy_table.columns
        for column in ("parcel_id", "planning_feature_id", "relation_type")
    )
    assert result.policy_table["local_feature_text_interpreted"].eq(False).all()
    assert result.policy_table["local_regulation_content_interpreted"].eq(False).all()
    assert result.policy_table["legal_conclusion_produced"].eq(False).all()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_checked_in_policy_pins_all_twelve_exact_muret_decisions`

**Purpose:** Regression invariant: checked in policy pins all twelve exact muret decisions. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_checked_in_policy_pins_all_twelve_exact_muret_decisions() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert actual == EXPECTED_MURET_DECISIONS`
  - `assert config.status_priority == STATUS_PRIORITIES`
  - `assert config.policy_scope == POLICY_SCOPE`
  - `assert config.local_feature_text_interpreted is False`
  - `assert config.local_regulation_content_interpreted is False`
  - `assert config.legal_conclusion_produced is False`
  - `assert len(config.entries) == 12`
  - `assert ("PRESCRIPTION", "15", "00") in actual`
  - `assert ("PRESCRIPTION", "15", "01") in actual`
  - `assert all(len(key[1]) == len(key[2]) == 2 for key in actual)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_bess_planning_feature_policy_config` | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_checked_in_policy_pins_all_twelve_exact_muret_decisions() -> None:
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    actual = {
        (entry.feature_family, entry.type_code, entry.subtype_code): (
            entry.precheck_status,
            entry.confidence,
        )
        for entry in config.entries
    }
    assert actual == EXPECTED_MURET_DECISIONS
    assert config.status_priority == STATUS_PRIORITIES
    assert config.policy_scope == POLICY_SCOPE
    assert config.local_feature_text_interpreted is False
    assert config.local_regulation_content_interpreted is False
    assert config.legal_conclusion_produced is False
    assert len(config.entries) == 12
    assert ("PRESCRIPTION", "15", "00") in actual
    assert ("PRESCRIPTION", "15", "01") in actual
    assert all(len(key[1]) == len(key[2]) == 2 for key in actual)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_checked_in_policy_complete_snapshot_is_immutable`

**Purpose:** Regression invariant: checked in policy complete snapshot is immutable. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_checked_in_policy_complete_snapshot_is_immutable() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert config.schema_version == 1`
  - `assert config.profile == "muret_bess_cnig_feature_policy_v1"`
  - `assert config.policy_scope == POLICY_SCOPE`
  - `assert config.local_feature_text_interpreted is False`
  - `assert config.local_regulation_content_interpreted is False`
  - `assert config.legal_conclusion_produced is False`
  - `assert config.source_lock.model_dump(mode="json") == EXPECTED_SOURCE_LOCK`
  - `assert config.status_priority == STATUS_PRIORITIES`
  - `assert config.canonical_policy_entries_sha256 == EXPECTED_POLICY_ENTRIES_SHA256`
  - `assert (<br>        _canonical_sha256([entry.model_dump(mode="json") for entry in config.entries])<br>        == EXPECTED_POLICY_ENTRIES_SHA256<br>    )`
  - `assert _canonical_sha256(config.model_dump(mode="json")) == EXPECTED_POLICY_SHA256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_bess_planning_feature_policy_config` | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config` |
| `config.source_lock.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_sha256` | `tests.unit.test_bess_planning_feature_policy._canonical_sha256` |
| `entry.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_checked_in_policy_complete_snapshot_is_immutable() -> None:
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    assert config.schema_version == 1
    assert config.profile == "muret_bess_cnig_feature_policy_v1"
    assert config.policy_scope == POLICY_SCOPE
    assert config.local_feature_text_interpreted is False
    assert config.local_regulation_content_interpreted is False
    assert config.legal_conclusion_produced is False
    assert config.source_lock.model_dump(mode="json") == EXPECTED_SOURCE_LOCK
    assert config.status_priority == STATUS_PRIORITIES
    assert config.canonical_policy_entries_sha256 == EXPECTED_POLICY_ENTRIES_SHA256
    assert (
        _canonical_sha256([entry.model_dump(mode="json") for entry in config.entries])
        == EXPECTED_POLICY_ENTRIES_SHA256
    )
    assert _canonical_sha256(config.model_dump(mode="json")) == EXPECTED_POLICY_SHA256
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_checked_in_compiled_policy_result_hashes_are_pinned`

**Purpose:** Regression invariant: checked in compiled policy result hashes are pinned. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_checked_in_compiled_policy_result_hashes_are_pinned() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.policy_table_content_sha256 == EXPECTED_POLICY_TABLE_SHA256`
  - `assert result.complete_result_content_sha256 == EXPECTED_COMPLETE_RESULT_SHA256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_checked_in_policy_result` | `tests.unit.test_bess_planning_feature_policy._checked_in_policy_result` |

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
def test_checked_in_compiled_policy_result_hashes_are_pinned() -> None:
    result = _checked_in_policy_result()
    assert result.policy_table_content_sha256 == EXPECTED_POLICY_TABLE_SHA256
    assert result.complete_result_content_sha256 == EXPECTED_COMPLETE_RESULT_SHA256
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_v1_snapshot_detects_policy_text_drift`

**Purpose:** Regression invariant: profile v1 snapshot detects policy text drift. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_v1_snapshot_detects_policy_text_drift(field: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "field",
    ["rationale", "required_human_action", "limitations"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert isinstance(entries, list)`
  - `assert changed.profile == "muret_bess_cnig_feature_policy_v1"`
  - `assert _canonical_sha256(changed.model_dump(mode="json")) != EXPECTED_POLICY_SHA256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_bess_planning_feature_policy_config` | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_sha256` | `tests.unit.test_bess_planning_feature_policy._canonical_sha256` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |
| `changed.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `entries[0][field] = f"{entries[0][field]} Changed."`<br>`payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_profile_v1_snapshot_detects_policy_text_drift(field: str) -> None:
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    payload = config.model_dump(mode="json")
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0][field] = f"{entries[0][field]} Changed."
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    changed = BessPlanningFeaturePolicyConfig.model_validate(payload)
    assert changed.profile == "muret_bess_cnig_feature_policy_v1"
    assert _canonical_sha256(changed.model_dump(mode="json")) != EXPECTED_POLICY_SHA256
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_profile_v1_snapshot_detects_source_lock_drift`

**Purpose:** Regression invariant: profile v1 snapshot detects source lock drift. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_profile_v1_snapshot_detects_source_lock_drift() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert isinstance(source_lock, dict)`
  - `assert changed.profile == "muret_bess_cnig_feature_policy_v1"`
  - `assert _canonical_sha256(changed.model_dump(mode="json")) != EXPECTED_POLICY_SHA256`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `load_bess_planning_feature_policy_config` | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |
| `_canonical_sha256` | `tests.unit.test_bess_planning_feature_policy._canonical_sha256` |
| `changed.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `source_lock["document_id"] = "another-document"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_profile_v1_snapshot_detects_source_lock_drift() -> None:
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    payload = config.model_dump(mode="json")
    source_lock = payload["source_lock"]
    assert isinstance(source_lock, dict)
    source_lock["document_id"] = "another-document"
    changed = BessPlanningFeaturePolicyConfig.model_validate(payload)
    assert changed.profile == "muret_bess_cnig_feature_policy_v1"
    assert _canonical_sha256(changed.model_dump(mode="json")) != EXPECTED_POLICY_SHA256
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_pandas_is_a_direct_bounded_runtime_dependency`

**Purpose:** Regression invariant: pandas is a direct bounded runtime dependency. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_pandas_is_a_direct_bounded_runtime_dependency() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert "pandas>=3.0,<4" in project["dependencies"]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tomllib.loads` | `tomllib.loads` |
| `Path("pyproject.toml").read_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `Path("pyproject.toml").read_text` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_pandas_is_a_direct_bounded_runtime_dependency() -> None:
    project = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))[
        "project"
    ]
    assert "pandas>=3.0,<4" in project["dependencies"]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_information_9900_official_references_remain_missing`

**Purpose:** Regression invariant: information 9900 official references remain missing. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_information_9900_official_references_remain_missing() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert pd.isna(row["official_legal_reference"])`
  - `assert pd.isna(row["official_regulation_reference"])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `pd.isna` | `pandas.isna` |

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
def test_information_9900_official_references_remain_missing() -> None:
    _, _, _, result = _compiled_fixture()
    row = result.policy_table.loc[
        (result.policy_table["feature_family"] == "INFORMATION")
        & (result.policy_table["type_code"] == "99")
        & (result.policy_table["subtype_code"] == "00")
    ].iloc[0]
    assert pd.isna(row["official_legal_reference"])
    assert pd.isna(row["official_regulation_reference"])
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_null_reference_literal_is_rejected_by_local_envelope`

**Purpose:** Regression invariant: null reference literal is rejected by local envelope. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_null_reference_literal_is_rejected_by_local_envelope(
    column: str,
    literal: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "literal"),
    [
        (column, literal)
        for column in (
            "official_legal_reference",
            "official_regulation_reference",
        )
        for literal in ("None", "nan", "<NA>")
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `literal` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match="reference\|null\|missing")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `result.policy_table.copy` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `table.loc[row, column] = literal` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_null_reference_literal_is_rejected_by_local_envelope(
    column: str,
    literal: str,
) -> None:
    _, _, _, result = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    table = result.policy_table.copy(deep=True)
    row = table.index[
        (table["feature_family"] == "INFORMATION")
        & (table["type_code"] == "99")
        & (table["subtype_code"] == "00")
    ][0]
    table.loc[row, column] = literal
    coordinated = module._result_with_hashes(replace(result, policy_table=table))
    with pytest.raises(BessPlanningFeaturePolicyError, match="reference|null|missing"):
        module._validate_result_envelope(coordinated)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_lock_mismatch_is_rejected`

**Purpose:** Regression invariant: source lock mismatch is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_lock_mismatch_is_rejected(field: str, value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("document_id", "another-document"),
        ("archive_sha256", "f" * 64),
        ("cnig_profile", "another-profile"),
        ("cnig_profile_schema_version", 1),
        ("cnig_profile_sha256", "f" * 64),
        ("cnig_result_hash_schema_version", 4),
        ("cnig_complete_result_content_sha256", "f" * 64),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match="lock\|source\|CNIG")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `config.source_lock.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `config.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `compile_bess_planning_feature_policy` | `landscout.stages.bess_planning_feature_policy.compile_bess_planning_feature_policy` |
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
def test_source_lock_mismatch_is_rejected(field: str, value: object) -> None:
    inputs, coded, config, _ = _compiled_fixture()
    changed_lock = config.source_lock.model_copy(update={field: value})
    changed = config.model_copy(update={"source_lock": changed_lock})
    with pytest.raises(BessPlanningFeaturePolicyError, match="lock|source|CNIG"):
        compile_bess_planning_feature_policy(*inputs, coded, changed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_policy_pair_is_rejected`

**Purpose:** Regression invariant: missing policy pair is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_policy_pair_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match="missing\|pair")`
- Exact assertions:
  - `assert isinstance(entries, list)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `entries.pop` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_config` | `tests.unit.test_bess_planning_feature_policy._validated_config` |
| `pytest.raises` | `pytest.raises` |
| `compile_bess_planning_feature_policy` | `landscout.stages.bess_planning_feature_policy.compile_bess_planning_feature_policy` |

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
| In-memory mutation | `entries.pop()` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_policy_pair_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries.pop()
    config = _validated_config(payload)
    with pytest.raises(BessPlanningFeaturePolicyError, match="missing|pair"):
        compile_bess_planning_feature_policy(*inputs, coded, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_extra_policy_pair_is_rejected_without_type_fallback`

**Purpose:** Regression invariant: extra policy pair is rejected without type fallback. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_extra_policy_pair_is_rejected_without_type_fallback() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match="extra\|pair")`
- Exact assertions:
  - `assert isinstance(entries, list)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `extra.update` | `unresolved local/third-party receiver; no ownership inferred` |
| `entries.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `entries.sort` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_config` | `tests.unit.test_bess_planning_feature_policy._validated_config` |
| `pytest.raises` | `pytest.raises` |
| `compile_bess_planning_feature_policy` | `landscout.stages.bess_planning_feature_policy.compile_bess_planning_feature_policy` |

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
| In-memory mutation | `extra.update(<br>        {<br>            "feature_family": "INFORMATION",<br>            "type_code": "98",<br>            "subtype_code": "00",<br>            "expected_official_label": "Synthetic extra official pair",<br>            "expected_legal_reference": None,<br>            "expected_regulation_reference": None,<br>        }<br>    )`<br>`entries.append(extra)`<br>`entries.sort(<br>        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"])<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_extra_policy_pair_is_rejected_without_type_fallback() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    extra = dict(entries[-1])
    extra.update(
        {
            "feature_family": "INFORMATION",
            "type_code": "98",
            "subtype_code": "00",
            "expected_official_label": "Synthetic extra official pair",
            "expected_legal_reference": None,
            "expected_regulation_reference": None,
        }
    )
    entries.append(extra)
    entries.sort(
        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"])
    )
    config = _validated_config(payload)
    with pytest.raises(BessPlanningFeaturePolicyError, match="extra|pair"):
        compile_bess_planning_feature_policy(*inputs, coded, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_policy_pair_is_rejected`

**Purpose:** Regression invariant: duplicate policy pair is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_policy_pair_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="duplicate\|pair")`
- Exact assertions:
  - `assert isinstance(entries, list)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `entries.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_sha256` | `tests.unit.test_bess_planning_feature_policy._canonical_sha256` |
| `pytest.raises` | `pytest.raises` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |

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
| In-memory mutation | `entries.append(dict(entries[0]))`<br>`payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_policy_pair_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries.append(dict(entries[0]))
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError, match="duplicate|pair"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_prescription_information_code_spaces_remain_separate`

**Purpose:** Regression invariant: prescription information code spaces remain separate. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_prescription_information_code_spaces_remain_separate() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match="missing\|extra\|pair")`
- Exact assertions:
  - `assert isinstance(entries, list)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `entries.sort` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_config` | `tests.unit.test_bess_planning_feature_policy._validated_config` |
| `pytest.raises` | `pytest.raises` |
| `compile_bess_planning_feature_policy` | `landscout.stages.bess_planning_feature_policy.compile_bess_planning_feature_policy` |

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
| In-memory mutation | `entries[0]["feature_family"] = "PRESCRIPTION"`<br>`entries.sort(<br>        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"])<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_prescription_information_code_spaces_remain_separate() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0]["feature_family"] = "PRESCRIPTION"
    entries.sort(
        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"])
    )
    config = _validated_config(payload)
    with pytest.raises(BessPlanningFeaturePolicyError, match="missing|extra|pair"):
        compile_bess_planning_feature_policy(*inputs, coded, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_official_meaning_mismatch_is_rejected`

**Purpose:** Regression invariant: official meaning mismatch is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_official_meaning_mismatch_is_rejected(
    field: str,
    value: object,
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("expected_official_label", "Wrong official label", "label"),
        ("expected_legal_reference", "Wrong legal reference", "legal"),
        ("expected_regulation_reference", "Wrong regulation reference", "regulation"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match=message)`
- Exact assertions:
  - `assert isinstance(entries, list)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_config` | `tests.unit.test_bess_planning_feature_policy._validated_config` |
| `pytest.raises` | `pytest.raises` |
| `compile_bess_planning_feature_policy` | `landscout.stages.bess_planning_feature_policy.compile_bess_planning_feature_policy` |
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
| In-memory mutation | `entries[0][field] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_official_meaning_mismatch_is_rejected(
    field: str,
    value: object,
    message: str,
) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0][field] = value
    config = _validated_config(payload)
    with pytest.raises(BessPlanningFeaturePolicyError, match=message):
        compile_bess_planning_feature_policy(*inputs, coded, config)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_or_legal_conclusion_status_is_rejected`

**Purpose:** Regression invariant: invalid or legal conclusion status is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_or_legal_conclusion_status_is_rejected(status: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("status", ["ALLOWED", "FORBIDDEN", "PROHIBITED"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `status` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`
- Exact assertions:
  - `assert isinstance(entries, list)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_sha256` | `tests.unit.test_bess_planning_feature_policy._canonical_sha256` |
| `pytest.raises` | `pytest.raises` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

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
| In-memory mutation | `entries[0]["precheck_status"] = status`<br>`payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_or_legal_conclusion_status_is_rejected(status: str) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0]["precheck_status"] = status
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_invalid_confidence_is_rejected`

**Purpose:** Regression invariant: invalid confidence is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_invalid_confidence_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`
- Exact assertions:
  - `assert isinstance(entries, list)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_sha256` | `tests.unit.test_bess_planning_feature_policy._canonical_sha256` |
| `pytest.raises` | `pytest.raises` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |

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
| In-memory mutation | `entries[0]["confidence"] = "CERTAIN"`<br>`payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_invalid_confidence_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0]["confidence"] = "CERTAIN"
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_status_priority_contract_is_strict`

**Purpose:** Regression invariant: status priority contract is strict. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_status_priority_contract_is_strict(mutation: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["duplicate", "missing", "zero", "bool", "string"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="priority\|integer")`
- Exact assertions:
  - `assert isinstance(priorities, dict)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `priorities.pop` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |
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
| In-memory mutation | `priorities["UNKNOWN"] = priorities["LIKELY_MATERIAL_CONSTRAINT"]`<br>`priorities.pop("UNKNOWN")`<br>`priorities["UNKNOWN"] = 0`<br>`priorities["UNKNOWN"] = True`<br>`priorities["UNKNOWN"] = "40"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_status_priority_contract_is_strict(mutation: str) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    priorities = payload["status_priority"]
    assert isinstance(priorities, dict)
    if mutation == "duplicate":
        priorities["UNKNOWN"] = priorities["LIKELY_MATERIAL_CONSTRAINT"]
    elif mutation == "missing":
        priorities.pop("UNKNOWN")
    elif mutation == "zero":
        priorities["UNKNOWN"] = 0
    elif mutation == "bool":
        priorities["UNKNOWN"] = True
    else:
        priorities["UNKNOWN"] = "40"
    with pytest.raises(ValidationError, match="priority|integer"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_status_priority_mapping_is_deeply_immutable`

**Purpose:** Regression invariant: status priority mapping is deeply immutable. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_status_priority_mapping_is_deeply_immutable() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(TypeError, match="frozen mapping")`
- Exact assertions:
  - `assert config.model_dump(mode="python") == snapshot`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |

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
| In-memory mutation | `config.status_priority["UNKNOWN"] = 999` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_status_priority_mapping_is_deeply_immutable() -> None:
    _, _, config, _ = _compiled_fixture()
    snapshot = config.model_dump(mode="python")

    with pytest.raises(TypeError, match="frozen mapping"):
        config.status_priority["UNKNOWN"] = 999

    assert config.model_dump(mode="python") == snapshot
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_yaml_key_is_rejected`

**Purpose:** Regression invariant: duplicate yaml key is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
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
  - `pytest.raises(BessPlanningFeaturePolicyError, match="Duplicate YAML")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_bess_planning_feature_policy_config` | `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.yaml"
    path.write_text("schema_version: 1\nschema_version: 1\n", encoding="utf-8")
    with pytest.raises(BessPlanningFeaturePolicyError, match="Duplicate YAML"):
        load_bess_planning_feature_policy_config(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_yaml_field_is_rejected`

**Purpose:** Regression invariant: unknown yaml field is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_yaml_field_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `pytest.raises` | `pytest.raises` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |

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
| In-memory mutation | `payload["unknown_field"] = "not allowed"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unknown_yaml_field_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    payload["unknown_field"] = "not allowed"
    with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_noncanonical_whitespace_is_rejected`

**Purpose:** Regression invariant: noncanonical whitespace is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_noncanonical_whitespace_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="whitespace\|exact")`
- Exact assertions:
  - `assert isinstance(entries, list)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_sha256` | `tests.unit.test_bess_planning_feature_policy._canonical_sha256` |
| `pytest.raises` | `pytest.raises` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |

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
| In-memory mutation | `entries[0]["rationale"] = " leading whitespace"`<br>`payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_noncanonical_whitespace_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0]["rationale"] = " leading whitespace"
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError, match="whitespace|exact"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_sha256_is_rejected`

**Purpose:** Regression invariant: malformed sha256 is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_sha256_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="SHA256")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `pytest.raises` | `pytest.raises` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |

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
| In-memory mutation | `payload["canonical_policy_entries_sha256"] = "NOT-A-SHA"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_malformed_sha256_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    payload["canonical_policy_entries_sha256"] = "NOT-A-SHA"
    with pytest.raises(ValidationError, match="SHA256"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_in_memory_config_is_revalidated_before_compilation`

**Purpose:** Regression invariant: in memory config is revalidated before compilation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_in_memory_config_is_revalidated_before_compilation() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match="in-memory\|canonical")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `config.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `compile_bess_planning_feature_policy` | `landscout.stages.bess_planning_feature_policy.compile_bess_planning_feature_policy` |

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
def test_in_memory_config_is_revalidated_before_compilation() -> None:
    inputs, coded, config, _ = _compiled_fixture()
    corrupted = config.model_copy(update={"canonical_policy_entries_sha256": "f" * 64})
    with pytest.raises(BessPlanningFeaturePolicyError, match="in-memory|canonical"):
        compile_bess_planning_feature_policy(*inputs, coded, corrupted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_entries_require_deterministic_order`

**Purpose:** Regression invariant: policy entries require deterministic order. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_entries_require_deterministic_order() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="order")`
- Exact assertions:
  - `assert isinstance(entries, list)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `entries.reverse` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_sha256` | `tests.unit.test_bess_planning_feature_policy._canonical_sha256` |
| `pytest.raises` | `pytest.raises` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |

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
| In-memory mutation | `entries.reverse()`<br>`payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_policy_entries_require_deterministic_order() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries.reverse()
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError, match="order"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_table_is_sorted_and_preserves_leading_zero_codes`

**Purpose:** Regression invariant: policy table is sorted and preserves leading zero codes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_table_is_sorted_and_preserves_leading_zero_codes() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert keys == sorted(keys)`
  - `assert all(<br>        len(type_code) == len(subtype_code) == 2 for _, type_code, subtype_code in keys<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.policy_table[["feature_family", "type_code", "subtype_code"]].itertuples` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_policy_table_is_sorted_and_preserves_leading_zero_codes() -> None:
    _, _, _, result = _compiled_fixture()
    keys = list(
        result.policy_table[["feature_family", "type_code", "subtype_code"]].itertuples(
            index=False, name=None
        )
    )
    assert keys == sorted(keys)
    assert all(
        len(type_code) == len(subtype_code) == 2 for _, type_code, subtype_code in keys
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_table_mutation_is_rejected`

**Purpose:** Regression invariant: policy table mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_table_mutation_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match="hash\|table\|rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `result.policy_table.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `validate_bess_planning_feature_policy_result` | `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result` |
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
| In-memory mutation | `table.loc[table.index[0], "precheck_status"] = "UNKNOWN"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_policy_table_mutation_is_rejected() -> None:
    inputs, coded, config, result = _compiled_fixture()
    table = result.policy_table.copy(deep=True)
    table.loc[table.index[0], "precheck_status"] = "UNKNOWN"
    with pytest.raises(BessPlanningFeaturePolicyError, match="hash|table|rebuilt"):
        validate_bess_planning_feature_policy_result(
            *inputs, coded, config, replace(result, policy_table=table)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_policy_table_and_hash_mutation_is_rejected`

**Purpose:** Regression invariant: coordinated policy table and hash mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_policy_table_and_hash_mutation_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match="table\|rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `result.policy_table.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `validate_bess_planning_feature_policy_result` | `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result` |

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
| In-memory mutation | `table.loc[table.index[0], "rationale"] = "Coordinated but false rationale."` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coordinated_policy_table_and_hash_mutation_is_rejected() -> None:
    inputs, coded, config, result = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    table = result.policy_table.copy(deep=True)
    table.loc[table.index[0], "rationale"] = "Coordinated but false rationale."
    coordinated = module._result_with_hashes(replace(result, policy_table=table))
    with pytest.raises(BessPlanningFeaturePolicyError, match="table|rebuilt"):
        validate_bess_planning_feature_policy_result(
            *inputs, coded, config, coordinated
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_persisted_parquet_and_json_readback_is_source_complete`

**Purpose:** Regression invariant: persisted parquet and json readback is source complete. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_persisted_parquet_and_json_readback_is_source_complete(
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
  - `assert pd.isna(row["official_legal_reference"])`
  - `assert pd.isna(row["official_regulation_reference"])`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `_write_artifacts` | `tests.unit.test_bess_planning_feature_policy._write_artifacts` |
| `importlib.import_module` | `importlib.import_module` |
| `module.load_bess_planning_feature_policy_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `pd.isna` | `pandas.isna` |
| `validate_bess_planning_feature_policy_result` | `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result` |

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
def test_persisted_parquet_and_json_readback_is_source_complete(
    tmp_path: Path,
) -> None:
    inputs, coded, config, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    persisted = module.load_bess_planning_feature_policy_artifacts(
        parquet, manifest_path
    )
    assert_frame_equal(result.policy_table, persisted.policy_table, check_dtype=True)
    row = persisted.policy_table.loc[
        (persisted.policy_table["feature_family"] == "INFORMATION")
        & (persisted.policy_table["type_code"] == "99")
        & (persisted.policy_table["subtype_code"] == "00")
    ].iloc[0]
    assert pd.isna(row["official_legal_reference"])
    assert pd.isna(row["official_regulation_reference"])
    validate_bess_planning_feature_policy_result(*inputs, coded, config, persisted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_manifest_model_is_strict_and_frozen`

**Purpose:** Regression invariant: artifact manifest model is strict and frozen. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_artifact_manifest_model_is_strict_and_frozen(tmp_path: Path) -> None:
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
  - `pytest.raises(ValidationError)`
- Exact assertions:
  - `assert validated.schema_version == 2`
  - `assert validated.artifact_kind == ARTIFACT_KIND`
  - `assert validated.cnig_profile_schema_version == 2`
  - `assert validated.cnig_result_hash_schema_version == 5`
  - `assert validated.parquet_filename == parquet.name`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `_write_artifacts` | `tests.unit.test_bess_planning_feature_policy._write_artifacts` |
| `importlib.import_module` | `importlib.import_module` |
| `module.BessPlanningFeaturePolicyArtifactManifest.model_validate` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |

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
| In-memory mutation | `validated.parquet_row_count = 0` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_artifact_manifest_model_is_strict_and_frozen(tmp_path: Path) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, _, manifest = _write_artifacts(tmp_path, result)
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    validated = module.BessPlanningFeaturePolicyArtifactManifest.model_validate(
        manifest
    )
    assert validated.schema_version == 2
    assert validated.artifact_kind == ARTIFACT_KIND
    assert validated.cnig_profile_schema_version == 2
    assert validated.cnig_result_hash_schema_version == 5
    assert validated.parquet_filename == parquet.name
    with pytest.raises(ValidationError):
        validated.parquet_row_count = 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_loader_rejects_manifest_mismatch`

**Purpose:** Regression invariant: artifact loader rejects manifest mismatch. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_artifact_loader_rejects_manifest_mismatch(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda value: value.update(schema_version=1), "schema"),
        (lambda value: value.update(unknown_field=True), "manifest|artifact"),
        (lambda value: value.update(parquet_filename="other.parquet"), "filename"),
        (lambda value: value.update(parquet_row_count=999), "row"),
        (lambda value: value.update(parquet_size_bytes=999), "size"),
        (lambda value: value.update(parquet_sha256="f" * 64), "SHA|hash"),
        (
            lambda value: value["policy_table_schema_signature"].update(
                index_names=["changed"]
            ),
            "schema",
        ),
        (lambda value: value.update(policy_table_content_sha256="f" * 64), "hash"),
        (lambda value: value.update(complete_result_content_sha256="f" * 64), "hash"),
        (lambda value: value.pop("policy_profile"), "manifest|artifact"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `mutation` | positional-or-keyword | `object` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match=message)`
- Exact assertions:
  - `assert callable(mutation)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `_write_artifacts` | `tests.unit.test_bess_planning_feature_policy._write_artifacts` |
| `callable` | `unresolved local/third-party receiver; no ownership inferred` |
| `mutation` | `unresolved local/third-party receiver; no ownership inferred` |
| `manifest_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `importlib.import_module` | `importlib.import_module` |
| `pytest.raises` | `pytest.raises` |
| `module.load_bess_planning_feature_policy_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_artifact_loader_rejects_manifest_mismatch(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, manifest = _write_artifacts(tmp_path, result)
    assert callable(mutation)
    mutation(manifest)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError, match=message):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_loader_uses_strict_json_before_parquet_read`

**Purpose:** Regression invariant: artifact loader uses strict json before parquet read. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_artifact_loader_uses_strict_json_before_parquet_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "document",
    [
        '{"schema_version": 2, "schema_version": 2}\n',
        '{"schema_version": NaN}\n',
        '{"schema_version": Infinity}\n',
        "[]\n",
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
  - `pytest.raises(<br>        BessPlanningFeaturePolicyError,<br>        match="Duplicate JSON\|finite\|top-level\|invalid",<br>    )`
- Exact assertions:
  - `assert parquet_reads == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `_write_artifacts` | `tests.unit.test_bess_planning_feature_policy._write_artifacts` |
| `manifest_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.load_bess_planning_feature_policy_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_artifact_loader_uses_strict_json_before_parquet_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    manifest_path.write_text(document, encoding="utf-8")
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    parquet_reads = 0

    def counted(*args: object, **kwargs: object) -> object:
        nonlocal parquet_reads
        parquet_reads += 1
        raise AssertionError("Parquet read preceded strict manifest validation")

    monkeypatch.setattr(module.pd, "read_parquet", counted)
    with pytest.raises(
        BessPlanningFeaturePolicyError,
        match="Duplicate JSON|finite|top-level|invalid",
    ):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
    assert parquet_reads == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_loader_uses_strict_json_before_parquet_read.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

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
  - `AssertionError("Parquet read preceded strict manifest validation")`.

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
        nonlocal parquet_reads
        parquet_reads += 1
        raise AssertionError("Parquet read preceded strict manifest validation")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_loader_rejects_parquet_replacement`

**Purpose:** Regression invariant: artifact loader rejects parquet replacement. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_artifact_loader_rejects_parquet_replacement(tmp_path: Path) -> None:
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
  - `pytest.raises(BessPlanningFeaturePolicyError, match="size\|SHA\|hash")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `_write_artifacts` | `tests.unit.test_bess_planning_feature_policy._write_artifacts` |
| `parquet.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `parquet.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `importlib.import_module` | `importlib.import_module` |
| `pytest.raises` | `pytest.raises` |
| `module.load_bess_planning_feature_policy_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `parquet.read_bytes` |
| Filesystem/archive write or publication | `parquet.write_bytes` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_artifact_loader_rejects_parquet_replacement(tmp_path: Path) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    parquet.write_bytes(parquet.read_bytes() + b"changed-after-manifest")
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError, match="size|SHA|hash"):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_loader_parses_the_exact_verified_parquet_bytes`

**Purpose:** Regression invariant: artifact loader parses the exact verified parquet bytes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_artifact_loader_parses_the_exact_verified_parquet_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
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
  - `assert replacement_bytes != verified_bytes`
  - `assert replacement_performed`
  - `assert parsed_payloads == [("buffer", verified_bytes)]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `_write_artifacts` | `tests.unit.test_bess_planning_feature_policy._write_artifacts` |
| `result.policy_table.to_parquet` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `module.load_bess_planning_feature_policy_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
| `assert_frame_equal` | `pandas.testing.assert_frame_equal` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `original_read_bytes` |
| Filesystem/archive write or publication | `result.policy_table.to_parquet` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_artifact_loader_parses_the_exact_verified_parquet_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    replacement = tmp_path / "replacement.parquet"
    result.policy_table.to_parquet(replacement, index=True, compression="gzip")
    original_read_bytes = Path.read_bytes
    verified_bytes = original_read_bytes(parquet)
    replacement_bytes = original_read_bytes(replacement)
    assert replacement_bytes != verified_bytes
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    original_read_parquet = module.pd.read_parquet
    replacement_performed = False
    parsed_payloads: list[tuple[str, bytes]] = []

    def replace_after_byte_read(path: Path) -> bytes:
        nonlocal replacement_performed
        payload = original_read_bytes(path)
        if path == parquet and not replacement_performed:
            path.write_bytes(replacement_bytes)
            replacement_performed = True
        return payload

    def old_hash_then_replace(path: Path) -> str:
        nonlocal replacement_performed
        payload = original_read_bytes(path)
        if path == parquet and not replacement_performed:
            path.write_bytes(replacement_bytes)
            replacement_performed = True
        return sha256(payload).hexdigest()

    def observed_read_parquet(
        source: object, *args: object, **kwargs: object
    ) -> object:
        if isinstance(source, BytesIO):
            parsed_payloads.append(("buffer", source.getvalue()))
        else:
            path = Path(source)
            parsed_payloads.append(("path", original_read_bytes(path)))
        return original_read_parquet(source, *args, **kwargs)

    monkeypatch.setattr(Path, "read_bytes", replace_after_byte_read)
    monkeypatch.setattr(module, "_file_sha256", old_hash_then_replace, raising=False)
    monkeypatch.setattr(module.pd, "read_parquet", observed_read_parquet)
    loaded = module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
    assert replacement_performed
    assert parsed_payloads == [("buffer", verified_bytes)]
    assert_frame_equal(result.policy_table, loaded.policy_table, check_dtype=True)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_loader_parses_the_exact_verified_parquet_bytes.replace_after_byte_read`

**Purpose:** Implements `replace after byte read` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def replace_after_byte_read(path: Path) -> bytes:
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
def replace_after_byte_read(path: Path) -> bytes:
        nonlocal replacement_performed
        payload = original_read_bytes(path)
        if path == parquet and not replacement_performed:
            path.write_bytes(replacement_bytes)
            replacement_performed = True
        return payload
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_loader_parses_the_exact_verified_parquet_bytes.old_hash_then_replace`

**Purpose:** Implements `old hash then replace` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def old_hash_then_replace(path: Path) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `sha256(payload).hexdigest()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `original_read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.write_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `original_read_bytes` |
| Filesystem/archive write or publication | `path.write_bytes` |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def old_hash_then_replace(path: Path) -> str:
        nonlocal replacement_performed
        payload = original_read_bytes(path)
        if path == parquet and not replacement_performed:
            path.write_bytes(replacement_bytes)
            replacement_performed = True
        return sha256(payload).hexdigest()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_artifact_loader_parses_the_exact_verified_parquet_bytes.observed_read_parquet`

**Purpose:** Implements `observed read parquet` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def observed_read_parquet(
        source: object, *args: object, **kwargs: object
    ) -> object:
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
  - `original_read_parquet(source, *args, **kwargs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `parsed_payloads.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `source.getvalue` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `original_read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `original_read_parquet` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `original_read_bytes`<br>`original_read_parquet` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `parsed_payloads.append(("buffer", source.getvalue()))`<br>`parsed_payloads.append(("path", original_read_bytes(path)))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def observed_read_parquet(
        source: object, *args: object, **kwargs: object
    ) -> object:
        if isinstance(source, BytesIO):
            parsed_payloads.append(("buffer", source.getvalue()))
        else:
            path = Path(source)
            parsed_payloads.append(("path", original_read_bytes(path)))
        return original_read_parquet(source, *args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_locally_invalid_result_fast_fails_before_source_validation`

**Purpose:** Regression invariant: locally invalid result fast fails before source validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_locally_invalid_result_fast_fails_before_source_validation(
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
  - `pytest.raises(<br>            BessPlanningFeaturePolicyError, match="type\|schema\|hash\|result"<br>        )`
- Exact assertions:
  - `assert calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.policy_table.drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_bess_planning_feature_policy_result` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `result.policy_table.drop(columns="confidence")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_locally_invalid_result_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, result = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    wrong_table = result.policy_table.drop(columns="confidence")
    invalid_results = (
        object(),
        replace(result, policy_schema_version=2),
        replace(result, policy_table=wrong_table),
        replace(result, policy_table_content_sha256="f" * 64),
        replace(result, complete_result_content_sha256="f" * 64),
    )
    for invalid in invalid_results:
        with pytest.raises(
            BessPlanningFeaturePolicyError, match="type|schema|hash|result"
        ):
            module.validate_bess_planning_feature_policy_result(
                *inputs, coded, config, invalid
            )
    assert calls == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_locally_invalid_result_fast_fails_before_source_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

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

### `test_compiler_wrong_source_lock_fast_fails_before_source_validation`

**Purpose:** Regression invariant: compiler wrong source lock fast fails before source validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_compiler_wrong_source_lock_fast_fails_before_source_validation(
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
  - `pytest.raises(BessPlanningFeaturePolicyError, match="lock\|document")`
- Exact assertions:
  - `assert calls == 0`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `config.source_lock.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `config.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.compile_bess_planning_feature_policy` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_compiler_wrong_source_lock_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, _ = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    wrong_lock = config.source_lock.model_copy(
        update={"document_id": "another-document"}
    )
    wrong_config = config.model_copy(update={"source_lock": wrong_lock})
    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    with pytest.raises(BessPlanningFeaturePolicyError, match="lock|document"):
        module.compile_bess_planning_feature_policy(*inputs, coded, wrong_config)
    assert calls == 0
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_compiler_wrong_source_lock_fast_fails_before_source_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

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

### `test_forged_matching_lock_still_runs_source_complete_validation`

**Purpose:** Regression invariant: forged matching lock still runs source complete validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_forged_matching_lock_still_runs_source_complete_validation(
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
  - `pytest.raises(BessPlanningFeaturePolicyError, match="Source-complete\|source")`
- Exact assertions:
  - `assert calls == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `importlib.import_module` | `importlib.import_module` |
| `replace` | `dataclasses.replace` |
| `config.source_lock.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `config.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.compile_bess_planning_feature_policy` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_forged_matching_lock_still_runs_source_complete_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, _ = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    actual = module.validate_planning_feature_code_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    forged_coded = replace(coded, source_document_id="forged-document")
    forged_lock = config.source_lock.model_copy(
        update={"document_id": "forged-document"}
    )
    forged_config = config.model_copy(update={"source_lock": forged_lock})
    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    with pytest.raises(BessPlanningFeaturePolicyError, match="Source-complete|source"):
        module.compile_bess_planning_feature_policy(
            *inputs, forged_coded, forged_config
        )
    assert calls == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_forged_matching_lock_still_runs_source_complete_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

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

### `test_compiler_and_public_validator_invoke_source_complete_coding_validation`

**Purpose:** Regression invariant: compiler and public validator invoke source complete coding validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_compiler_and_public_validator_invoke_source_complete_coding_validation(
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
| `_integration_inputs` | `test_resolve_planning_feature_codes._integration_inputs` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `BessPlanningFeaturePolicyConfig.model_validate` | `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.model_validate` |
| `_policy_payload` | `tests.unit.test_bess_planning_feature_policy._policy_payload` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `module.compile_bess_planning_feature_policy` | `unresolved local/third-party receiver; no ownership inferred` |
| `module.validate_bess_planning_feature_policy_result` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_compiler_and_public_validator_invoke_source_complete_coding_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    config = BessPlanningFeaturePolicyConfig.model_validate(
        _policy_payload(inputs, coded)
    )
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    actual = module.validate_planning_feature_code_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    result = module.compile_bess_planning_feature_policy(*inputs, coded, config)
    assert calls == 1
    module.validate_bess_planning_feature_policy_result(*inputs, coded, config, result)
    assert calls == 2
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_compiler_and_public_validator_invoke_source_complete_coding_validation.counted`

**Purpose:** Implements `counted` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

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

### `test_public_policy_api_exports_only_stable_symbols`

**Purpose:** Regression invariant: public policy api exports only stable symbols. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_public_policy_api_exports_only_stable_symbols() -> None:
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
  - `assert all(getattr(stages, name) is getattr(module, name) for name in required)`
  - `assert not any(name in module.__all__ for name in ("_canonical_sha256", "_lookup"))`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `required.issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_public_policy_api_exports_only_stable_symbols() -> None:
    required = {
        "BessPlanningFeaturePolicyArtifactManifest",
        "BessPlanningFeaturePolicyConfig",
        "BessPlanningFeaturePolicyError",
        "BessPlanningFeaturePolicyResult",
        "load_bess_planning_feature_policy_artifacts",
        "load_bess_planning_feature_policy_config",
        "compile_bess_planning_feature_policy",
        "validate_bess_planning_feature_policy_result",
        "validate_bess_planning_feature_policy_result_envelope",
    }
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    assert set(module.__all__) == required
    assert required.issubset(set(stages.__all__))
    assert all(getattr(stages, name) is getattr(module, name) for name in required)
    assert not any(name in module.__all__ for name in ("_canonical_sha256", "_lookup"))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator`

**Purpose:** Regression invariant: step 7d 5b 2b 5 exposes lightweight policy result validator. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match="hash")`
- Exact assertions:
  - `assert hasattr(module, "validate_bess_planning_feature_policy_result_envelope")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `hasattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `module.validate_bess_planning_feature_policy_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
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
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    assert hasattr(module, "validate_bess_planning_feature_policy_result_envelope")
    _, _, _, result = _compiled_fixture()
    module.validate_bess_planning_feature_policy_result_envelope(result)
    with pytest.raises(BessPlanningFeaturePolicyError, match="hash"):
        module.validate_bess_planning_feature_policy_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_manifest_rejects_nonportable_parquet_filename`

**Purpose:** Regression invariant: policy manifest rejects nonportable parquet filename. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_manifest_rejects_nonportable_parquet_filename(
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
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `_write_artifacts` | `tests.unit.test_bess_planning_feature_policy._write_artifacts` |
| `importlib.import_module` | `importlib.import_module` |
| `pytest.raises` | `pytest.raises` |
| `module.BessPlanningFeaturePolicyArtifactManifest.model_validate` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `manifest["parquet_filename"] = filename` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_policy_manifest_rejects_nonportable_parquet_filename(
    tmp_path: Path, filename: str
) -> None:
    _, _, _, result = _compiled_fixture()
    _, _, manifest = _write_artifacts(tmp_path, result)
    manifest["parquet_filename"] = filename
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(ValueError, match="filename|basename|portable"):
        module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_shared_filename_contract_rejects_superscript_windows_devices`

**Purpose:** Regression invariant: shared filename contract rejects superscript windows devices. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_shared_filename_contract_rejects_superscript_windows_devices(
    filename: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "filename",
    [
        "com¹.parquet",
        "CoM².parquet",
        "cOm³.parquet",
        "lpt¹.parquet",
        "LpT².parquet",
        "lPt³.parquet",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `filename` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="reserved\|basename\|portable")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pytest.raises` | `pytest.raises` |
| `validate_portable_parquet_filename` | `landscout.common.artifact_paths.validate_portable_parquet_filename` |
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
def test_shared_filename_contract_rejects_superscript_windows_devices(
    filename: str,
) -> None:
    with pytest.raises(ValueError, match="reserved|basename|portable"):
        validate_portable_parquet_filename(filename, "artifact filename")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_manifest_rejects_unsupported_cnig_source_schema`

**Purpose:** Regression invariant: policy manifest rejects unsupported cnig source schema. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_manifest_rejects_unsupported_cnig_source_schema(
    tmp_path: Path,
    field: str,
    version: int,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "version"),
    [
        ("cnig_profile_schema_version", 0),
        ("cnig_profile_schema_version", 1),
        ("cnig_profile_schema_version", 3),
        ("cnig_profile_schema_version", 999),
        ("cnig_result_hash_schema_version", 0),
        ("cnig_result_hash_schema_version", 1),
        ("cnig_result_hash_schema_version", 4),
        ("cnig_result_hash_schema_version", 6),
        ("cnig_result_hash_schema_version", 999),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `version` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValidationError, match="CNIG\|cnig\|schema\|version")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `_write_artifacts` | `tests.unit.test_bess_planning_feature_policy._write_artifacts` |
| `importlib.import_module` | `importlib.import_module` |
| `pytest.raises` | `pytest.raises` |
| `module.BessPlanningFeaturePolicyArtifactManifest.model_validate` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `manifest[field] = version` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_policy_manifest_rejects_unsupported_cnig_source_schema(
    tmp_path: Path,
    field: str,
    version: int,
) -> None:
    _, _, _, result = _compiled_fixture()
    _, _, manifest = _write_artifacts(tmp_path, result)
    manifest[field] = version
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(ValidationError, match="CNIG|cnig|schema|version"):
        module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_artifact_loader_rejects_source_schema_before_parquet_read`

**Purpose:** Regression invariant: policy artifact loader rejects source schema before parquet read. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_artifact_loader_rejects_source_schema_before_parquet_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    version: int,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "version"),
    [
        ("cnig_profile_schema_version", 0),
        ("cnig_profile_schema_version", 1),
        ("cnig_profile_schema_version", 3),
        ("cnig_profile_schema_version", 999),
        ("cnig_result_hash_schema_version", 0),
        ("cnig_result_hash_schema_version", 1),
        ("cnig_result_hash_schema_version", 4),
        ("cnig_result_hash_schema_version", 6),
        ("cnig_result_hash_schema_version", 999),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |
| `field` | positional-or-keyword | `str` | `required` |
| `version` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeaturePolicyError, match="CNIG\|cnig\|schema\|version"<br>    )`
- Exact assertions:
  - `assert calls == {"bytes": 0, "parse": 0}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `_write_artifacts` | `tests.unit.test_bess_planning_feature_policy._write_artifacts` |
| `manifest_path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `importlib.import_module` | `importlib.import_module` |
| `pytest.raises` | `pytest.raises` |
| `module.load_bess_planning_feature_policy_artifacts` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `manifest[field] = version` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_policy_artifact_loader_rejects_source_schema_before_parquet_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    version: int,
) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, manifest = _write_artifacts(tmp_path, result)
    manifest[field] = version
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    calls = {"bytes": 0, "parse": 0}
    original_read_bytes = Path.read_bytes

    def byte_read(path: Path, *args: object, **kwargs: object) -> bytes:
        if path == parquet:
            calls["bytes"] += 1
            raise AssertionError("Parquet bytes must not be read")
        return original_read_bytes(path)

    def parse(*args: object, **kwargs: object) -> pd.DataFrame:
        calls["parse"] += 1
        raise AssertionError("Parquet must not be parsed")

    monkeypatch.setattr(Path, "read_bytes", byte_read)
    monkeypatch.setattr(pd, "read_parquet", parse)
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(
        BessPlanningFeaturePolicyError, match="CNIG|cnig|schema|version"
    ):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
    assert calls == {"bytes": 0, "parse": 0}
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_artifact_loader_rejects_source_schema_before_parquet_read.byte_read`

**Purpose:** Implements `byte read` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def byte_read(path: Path, *args: object, **kwargs: object) -> bytes:
```

- Exact decorators: none.
- Declared return annotation: `bytes`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `Path` | `required` |
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `original_read_bytes(path)`
- Explicit raise paths:
  - `AssertionError("Parquet bytes must not be read")` under lexical guard `path == parquet`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `AssertionError` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `calls["bytes"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def byte_read(path: Path, *args: object, **kwargs: object) -> bytes:
        if path == parquet:
            calls["bytes"] += 1
            raise AssertionError("Parquet bytes must not be read")
        return original_read_bytes(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_artifact_loader_rejects_source_schema_before_parquet_read.parse`

**Purpose:** Implements `parse` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def parse(*args: object, **kwargs: object) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `AssertionError("Parquet must not be parsed")`.

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
| In-memory mutation | `calls["parse"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def parse(*args: object, **kwargs: object) -> pd.DataFrame:
        calls["parse"] += 1
        raise AssertionError("Parquet must not be parsed")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_rehash_policy_table`

**Purpose:** Implements `rehash policy table` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _rehash_policy_table(
    result: BessPlanningFeaturePolicyResult, table: pd.DataFrame
) -> BessPlanningFeaturePolicyResult:
```

- Exact decorators: none.
- Declared return annotation: `BessPlanningFeaturePolicyResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessPlanningFeaturePolicyResult` | `required` |
| `table` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `module._result_with_hashes(replace(result, policy_table=table))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_bess_planning_feature_policy::_canonical_empty_policy_result` via `_rehash_policy_table`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_canonical_empty_policy_result` via `_rehash_policy_table`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_accepts_one_exact_policy_row` via `_rehash_policy_table`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_accepts_one_exact_policy_row` via `_rehash_policy_table`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_validates_every_intrinsic_row_contract` via `_rehash_policy_table`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_validates_every_intrinsic_row_contract` via `_rehash_policy_table`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |

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
def _rehash_policy_table(
    result: BessPlanningFeaturePolicyResult, table: pd.DataFrame
) -> BessPlanningFeaturePolicyResult:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    return module._result_with_hashes(replace(result, policy_table=table))
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_canonical_empty_policy_result`

**Purpose:** Implements `canonical empty policy result` within the file role: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

**Exact signature**

```python
def _canonical_empty_policy_result(
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
  - `_rehash_policy_table(result, table)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_rejects_canonical_empty_policy_table` via `_canonical_empty_policy_result`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_envelope_rejects_canonical_empty_policy_table` via `_canonical_empty_policy_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `result.policy_table.iloc[0:0].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Index` | `pandas.Index` |
| `_rehash_policy_table` | `tests.unit.test_bess_planning_feature_policy._rehash_policy_table` |

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
| In-memory mutation | `table.index = pd.Index([], dtype="int64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _canonical_empty_policy_result(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
    table = result.policy_table.iloc[0:0].copy(deep=True)
    table.index = pd.Index([], dtype="int64")
    return _rehash_policy_table(result, table)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_envelope_rejects_canonical_empty_policy_table`

**Purpose:** Regression invariant: policy envelope rejects canonical empty policy table. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_envelope_rejects_canonical_empty_policy_table() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeaturePolicyError, match="policy\|table\|empty\|entry"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `_canonical_empty_policy_result` | `tests.unit.test_bess_planning_feature_policy._canonical_empty_policy_result` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_bess_planning_feature_policy_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_policy_envelope_rejects_canonical_empty_policy_table() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    empty = _canonical_empty_policy_result(result)
    with pytest.raises(
        BessPlanningFeaturePolicyError, match="policy|table|empty|entry"
    ):
        module.validate_bess_planning_feature_policy_result_envelope(empty)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_envelope_accepts_one_exact_policy_row`

**Purpose:** Regression invariant: policy envelope accepts one exact policy row. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_envelope_accepts_one_exact_policy_row() -> None:
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
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `result.policy_table.iloc[[0]].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Index` | `pandas.Index` |
| `_rehash_policy_table` | `tests.unit.test_bess_planning_feature_policy._rehash_policy_table` |
| `module.validate_bess_planning_feature_policy_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `table.index = pd.Index([0], dtype="int64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_policy_envelope_accepts_one_exact_policy_row() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    table = result.policy_table.iloc[[0]].copy(deep=True)
    table.index = pd.Index([0], dtype="int64")
    one_row = _rehash_policy_table(result, table)
    module.validate_bess_planning_feature_policy_result_envelope(one_row)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_envelope_accepts_current_twelve_row_snapshot`

**Purpose:** Regression invariant: policy envelope accepts current twelve row snapshot. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_envelope_accepts_current_twelve_row_snapshot() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(result.policy_table) == 12`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_checked_in_policy_result` | `tests.unit.test_bess_planning_feature_policy._checked_in_policy_result` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `module.validate_bess_planning_feature_policy_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_policy_envelope_accepts_current_twelve_row_snapshot() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    result = _checked_in_policy_result()
    assert len(result.policy_table) == 12
    module.validate_bess_planning_feature_policy_result_envelope(result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_envelope_requires_cnig_profile_schema_two`

**Purpose:** Regression invariant: policy envelope requires cnig profile schema two. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_envelope_requires_cnig_profile_schema_two(version: int) -> None:
```

- Exact decorators: `pytest.mark.parametrize("version", [0, 1, 3, 999])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `version` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match="profile schema\|schema")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_bess_planning_feature_policy_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_policy_envelope_requires_cnig_profile_schema_two(version: int) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    changed = module._result_with_hashes(
        replace(result, cnig_profile_schema_version=version)
    )
    with pytest.raises(BessPlanningFeaturePolicyError, match="profile schema|schema"):
        module.validate_bess_planning_feature_policy_result_envelope(changed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_envelope_requires_cnig_result_schema_five`

**Purpose:** Regression invariant: policy envelope requires cnig result schema five. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_envelope_requires_cnig_result_schema_five(version: int) -> None:
```

- Exact decorators: `pytest.mark.parametrize("version", [0, 1, 2, 4, 6, 999])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `version` | positional-or-keyword | `int` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match="CNIG result\|schema")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `module._result_with_hashes` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_bess_planning_feature_policy_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
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
def test_policy_envelope_requires_cnig_result_schema_five(version: int) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    changed = module._result_with_hashes(
        replace(result, cnig_result_hash_schema_version=version)
    )
    with pytest.raises(BessPlanningFeaturePolicyError, match="CNIG result|schema"):
        module.validate_bess_planning_feature_policy_result_envelope(changed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_envelope_validates_every_intrinsic_row_contract`

**Purpose:** Regression invariant: policy envelope validates every intrinsic row contract. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_envelope_validates_every_intrinsic_row_contract(
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "mutation",
    [
        "duplicate-pair",
        "reordered-pairs",
        "malformed-code",
        "invalid-status",
        "invalid-confidence",
        "zero-priority",
        "negative-priority",
        "bool-priority",
        "status-two-priorities",
        "priority-two-statuses",
        "row-scope",
        "row-flag",
        "row-policy-sha",
        "row-cnig-profile",
        "row-cnig-sha",
        "row-cnig-result-sha",
        "literal-null-reference",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        BessPlanningFeaturePolicyError,<br>        match="policy\|pair\|order\|code\|status\|confidence\|priority\|scope\|flag\|CNIG\|null\|schema",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `result.policy_table.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.loc[<br>            first, ["feature_family", "type_code", "subtype_code"]<br>        ].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `table.iloc[::-1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `table["status_priority"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `_rehash_policy_table` | `tests.unit.test_bess_planning_feature_policy._rehash_policy_table` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_bess_planning_feature_policy_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
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
| In-memory mutation | `table.loc[second, ["feature_family", "type_code", "subtype_code"]] = table.loc[<br>            first, ["feature_family", "type_code", "subtype_code"]<br>        ].tolist()`<br>`table.loc[first, "type_code"] = "1"`<br>`table.loc[first, "precheck_status"] = "AUTHORIZED"`<br>`table.loc[first, "confidence"] = "CERTAIN"`<br>`table.loc[first, "status_priority"] = 0`<br>`table.loc[first, "status_priority"] = -1`<br>`values.loc[first] = True`<br>`table["status_priority"] = values`<br>`table.loc[second, "precheck_status"] = table.loc[first, "precheck_status"]`<br>`table.loc[second, "status_priority"] = table.loc[first, "status_priority"] + 1`<br>`table.loc[different, "status_priority"] = table.loc[first, "status_priority"]`<br>`table.loc[first, "policy_scope"] = "OTHER_SCOPE"`<br>`table.loc[first, "local_feature_text_interpreted"] = True`<br>`table.loc[first, "policy_sha256"] = "a" * 64`<br>`table.loc[first, "cnig_profile"] = "other-cnig-profile"`<br>`table.loc[first, "cnig_profile_sha256"] = "a" * 64`<br>`table.loc[first, "cnig_complete_result_content_sha256"] = "a" * 64`<br>`table.loc[first, "official_legal_reference"] = "None"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_policy_envelope_validates_every_intrinsic_row_contract(
    mutation: str,
) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    table = result.policy_table.copy(deep=True)
    first, second = table.index[:2]
    if mutation == "duplicate-pair":
        table.loc[second, ["feature_family", "type_code", "subtype_code"]] = table.loc[
            first, ["feature_family", "type_code", "subtype_code"]
        ].tolist()
    elif mutation == "reordered-pairs":
        table = table.iloc[::-1].copy(deep=True)
    elif mutation == "malformed-code":
        table.loc[first, "type_code"] = "1"
    elif mutation == "invalid-status":
        table.loc[first, "precheck_status"] = "AUTHORIZED"
    elif mutation == "invalid-confidence":
        table.loc[first, "confidence"] = "CERTAIN"
    elif mutation == "zero-priority":
        table.loc[first, "status_priority"] = 0
    elif mutation == "negative-priority":
        table.loc[first, "status_priority"] = -1
    elif mutation == "bool-priority":
        values = table["status_priority"].astype("object")
        values.loc[first] = True
        table["status_priority"] = values
    elif mutation == "status-two-priorities":
        table.loc[second, "precheck_status"] = table.loc[first, "precheck_status"]
        table.loc[second, "status_priority"] = table.loc[first, "status_priority"] + 1
    elif mutation == "priority-two-statuses":
        different = table.index[
            table["precheck_status"] != table.loc[first, "precheck_status"]
        ][0]
        table.loc[different, "status_priority"] = table.loc[first, "status_priority"]
    elif mutation == "row-scope":
        table.loc[first, "policy_scope"] = "OTHER_SCOPE"
    elif mutation == "row-flag":
        table.loc[first, "local_feature_text_interpreted"] = True
    elif mutation == "row-policy-sha":
        table.loc[first, "policy_sha256"] = "a" * 64
    elif mutation == "row-cnig-profile":
        table.loc[first, "cnig_profile"] = "other-cnig-profile"
    elif mutation == "row-cnig-sha":
        table.loc[first, "cnig_profile_sha256"] = "a" * 64
    elif mutation == "row-cnig-result-sha":
        table.loc[first, "cnig_complete_result_content_sha256"] = "a" * 64
    else:
        table.loc[first, "official_legal_reference"] = "None"
    changed = _rehash_policy_table(result, table)
    with pytest.raises(
        BessPlanningFeaturePolicyError,
        match="policy|pair|order|code|status|confidence|priority|scope|flag|CNIG|null|schema",
    ):
        module.validate_bess_planning_feature_policy_result_envelope(changed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1`

**Purpose:** Regression invariant: policy envelope requires exact type and accepts valid schema v1. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError, match="type\|result")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_compiled_fixture` | `tests.unit.test_bess_planning_feature_policy._compiled_fixture` |
| `DerivedPolicyResult` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_bess_planning_feature_policy_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()

    class DerivedPolicyResult(BessPlanningFeaturePolicyResult):
        pass

    derived = DerivedPolicyResult(**result.__dict__)
    with pytest.raises(BessPlanningFeaturePolicyError, match="type|result"):
        module.validate_bess_planning_feature_policy_result_envelope(derived)
    module.validate_bess_planning_feature_policy_result_envelope(result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_policy_envelope_controls_malformed_result_type`

**Purpose:** Regression invariant: policy envelope controls malformed result type. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_policy_envelope_controls_malformed_result_type(malformed: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("malformed", [None, object()])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `malformed` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(BessPlanningFeaturePolicyError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_bess_planning_feature_policy_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `object` | `unresolved local/third-party receiver; no ownership inferred` |

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
def test_policy_envelope_controls_malformed_result_type(malformed: object) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError):
        module.validate_bess_planning_feature_policy_result_envelope(malformed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **52**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status` | none | none | 8 | Proves valid exact policy compiles without applying feature or parcel status using the exact source reproduced in section 7. |
| `test_checked_in_policy_pins_all_twelve_exact_muret_decisions` | none | none | 10 | Proves checked in policy pins all twelve exact muret decisions using the exact source reproduced in section 7. |
| `test_checked_in_policy_complete_snapshot_is_immutable` | none | none | 11 | Proves checked in policy complete snapshot is immutable using the exact source reproduced in section 7. |
| `test_checked_in_compiled_policy_result_hashes_are_pinned` | none | none | 2 | Proves checked in compiled policy result hashes are pinned using the exact source reproduced in section 7. |
| `test_profile_v1_snapshot_detects_policy_text_drift` | pytest.mark.parametrize(<br>    "field",<br>    ["rationale", "required_human_action", "limitations"],<br>) | none | 3 | Proves profile v1 snapshot detects policy text drift using the exact source reproduced in section 7. |
| `test_profile_v1_snapshot_detects_source_lock_drift` | none | none | 3 | Proves profile v1 snapshot detects source lock drift using the exact source reproduced in section 7. |
| `test_pandas_is_a_direct_bounded_runtime_dependency` | none | none | 1 | Proves pandas is a direct bounded runtime dependency using the exact source reproduced in section 7. |
| `test_information_9900_official_references_remain_missing` | none | none | 2 | Proves information 9900 official references remain missing using the exact source reproduced in section 7. |
| `test_null_reference_literal_is_rejected_by_local_envelope` | pytest.mark.parametrize(<br>    ("column", "literal"),<br>    [<br>        (column, literal)<br>        for column in (<br>            "official_legal_reference",<br>            "official_regulation_reference",<br>        )<br>        for literal in ("None", "nan", "<NA>")<br>    ],<br>) | pytest.raises(BessPlanningFeaturePolicyError, match="reference\|null\|missing") | 0 | Proves null reference literal is rejected by local envelope using the exact source reproduced in section 7. |
| `test_source_lock_mismatch_is_rejected` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("document_id", "another-document"),<br>        ("archive_sha256", "f" * 64),<br>        ("cnig_profile", "another-profile"),<br>        ("cnig_profile_schema_version", 1),<br>        ("cnig_profile_sha256", "f" * 64),<br>        ("cnig_result_hash_schema_version", 4),<br>        ("cnig_complete_result_content_sha256", "f" * 64),<br>    ],<br>) | pytest.raises(BessPlanningFeaturePolicyError, match="lock\|source\|CNIG") | 0 | Proves source lock mismatch is rejected using the exact source reproduced in section 7. |
| `test_missing_policy_pair_is_rejected` | none | pytest.raises(BessPlanningFeaturePolicyError, match="missing\|pair") | 1 | Proves missing policy pair is rejected using the exact source reproduced in section 7. |
| `test_extra_policy_pair_is_rejected_without_type_fallback` | none | pytest.raises(BessPlanningFeaturePolicyError, match="extra\|pair") | 1 | Proves extra policy pair is rejected without type fallback using the exact source reproduced in section 7. |
| `test_duplicate_policy_pair_is_rejected` | none | pytest.raises(ValidationError, match="duplicate\|pair") | 1 | Proves duplicate policy pair is rejected using the exact source reproduced in section 7. |
| `test_prescription_information_code_spaces_remain_separate` | none | pytest.raises(BessPlanningFeaturePolicyError, match="missing\|extra\|pair") | 1 | Proves prescription information code spaces remain separate using the exact source reproduced in section 7. |
| `test_official_meaning_mismatch_is_rejected` | pytest.mark.parametrize(<br>    ("field", "value", "message"),<br>    [<br>        ("expected_official_label", "Wrong official label", "label"),<br>        ("expected_legal_reference", "Wrong legal reference", "legal"),<br>        ("expected_regulation_reference", "Wrong regulation reference", "regulation"),<br>    ],<br>) | pytest.raises(BessPlanningFeaturePolicyError, match=message) | 1 | Proves official meaning mismatch is rejected using the exact source reproduced in section 7. |
| `test_invalid_or_legal_conclusion_status_is_rejected` | pytest.mark.parametrize("status", ["ALLOWED", "FORBIDDEN", "PROHIBITED"]) | pytest.raises(ValidationError) | 1 | Proves invalid or legal conclusion status is rejected using the exact source reproduced in section 7. |
| `test_invalid_confidence_is_rejected` | none | pytest.raises(ValidationError) | 1 | Proves invalid confidence is rejected using the exact source reproduced in section 7. |
| `test_status_priority_contract_is_strict` | pytest.mark.parametrize("mutation", ["duplicate", "missing", "zero", "bool", "string"]) | pytest.raises(ValidationError, match="priority\|integer") | 1 | Proves status priority contract is strict using the exact source reproduced in section 7. |
| `test_status_priority_mapping_is_deeply_immutable` | none | pytest.raises(TypeError, match="frozen mapping") | 1 | Proves status priority mapping is deeply immutable using the exact source reproduced in section 7. |
| `test_duplicate_yaml_key_is_rejected` | none | pytest.raises(BessPlanningFeaturePolicyError, match="Duplicate YAML") | 0 | Proves duplicate yaml key is rejected using the exact source reproduced in section 7. |
| `test_unknown_yaml_field_is_rejected` | none | pytest.raises(ValidationError) | 0 | Proves unknown yaml field is rejected using the exact source reproduced in section 7. |
| `test_noncanonical_whitespace_is_rejected` | none | pytest.raises(ValidationError, match="whitespace\|exact") | 1 | Proves noncanonical whitespace is rejected using the exact source reproduced in section 7. |
| `test_malformed_sha256_is_rejected` | none | pytest.raises(ValidationError, match="SHA256") | 0 | Proves malformed sha256 is rejected using the exact source reproduced in section 7. |
| `test_in_memory_config_is_revalidated_before_compilation` | none | pytest.raises(BessPlanningFeaturePolicyError, match="in-memory\|canonical") | 0 | Proves in memory config is revalidated before compilation using the exact source reproduced in section 7. |
| `test_policy_entries_require_deterministic_order` | none | pytest.raises(ValidationError, match="order") | 1 | Proves policy entries require deterministic order using the exact source reproduced in section 7. |
| `test_policy_table_is_sorted_and_preserves_leading_zero_codes` | none | none | 2 | Proves policy table is sorted and preserves leading zero codes using the exact source reproduced in section 7. |
| `test_policy_table_mutation_is_rejected` | none | pytest.raises(BessPlanningFeaturePolicyError, match="hash\|table\|rebuilt") | 0 | Proves policy table mutation is rejected using the exact source reproduced in section 7. |
| `test_coordinated_policy_table_and_hash_mutation_is_rejected` | none | pytest.raises(BessPlanningFeaturePolicyError, match="table\|rebuilt") | 0 | Proves coordinated policy table and hash mutation is rejected using the exact source reproduced in section 7. |
| `test_persisted_parquet_and_json_readback_is_source_complete` | none | none | 2 | Proves persisted parquet and json readback is source complete using the exact source reproduced in section 7. |
| `test_artifact_manifest_model_is_strict_and_frozen` | none | pytest.raises(ValidationError) | 5 | Proves artifact manifest model is strict and frozen using the exact source reproduced in section 7. |
| `test_artifact_loader_rejects_manifest_mismatch` | pytest.mark.parametrize(<br>    ("mutation", "message"),<br>    [<br>        (lambda value: value.update(schema_version=1), "schema"),<br>        (lambda value: value.update(unknown_field=True), "manifest\|artifact"),<br>        (lambda value: value.update(parquet_filename="other.parquet"), "filename"),<br>        (lambda value: value.update(parquet_row_count=999), "row"),<br>        (lambda value: value.update(parquet_size_bytes=999), "size"),<br>        (lambda value: value.update(parquet_sha256="f" * 64), "SHA\|hash"),<br>        (<br>            lambda value: value["policy_table_schema_signature"].update(<br>                index_names=["changed"]<br>            ),<br>            "schema",<br>        ),<br>        (lambda value: value.update(policy_table_content_sha256="f" * 64), "hash"),<br>        (lambda value: value.update(complete_result_content_sha256="f" * 64), "hash"),<br>        (lambda value: value.pop("policy_profile"), "manifest\|artifact"),<br>    ],<br>) | pytest.raises(BessPlanningFeaturePolicyError, match=message) | 1 | Proves artifact loader rejects manifest mismatch using the exact source reproduced in section 7. |
| `test_artifact_loader_uses_strict_json_before_parquet_read` | pytest.mark.parametrize(<br>    "document",<br>    [<br>        '{"schema_version": 2, "schema_version": 2}\n',<br>        '{"schema_version": NaN}\n',<br>        '{"schema_version": Infinity}\n',<br>        "[]\n",<br>    ],<br>    ids=["duplicate-key", "nan", "infinity", "non-object"],<br>) | pytest.raises(<br>        BessPlanningFeaturePolicyError,<br>        match="Duplicate JSON\|finite\|top-level\|invalid",<br>    ) | 1 | Proves artifact loader uses strict json before parquet read using the exact source reproduced in section 7. |
| `test_artifact_loader_rejects_parquet_replacement` | none | pytest.raises(BessPlanningFeaturePolicyError, match="size\|SHA\|hash") | 0 | Proves artifact loader rejects parquet replacement using the exact source reproduced in section 7. |
| `test_artifact_loader_parses_the_exact_verified_parquet_bytes` | none | none | 3 | Proves artifact loader parses the exact verified parquet bytes using the exact source reproduced in section 7. |
| `test_locally_invalid_result_fast_fails_before_source_validation` | none | pytest.raises(<br>            BessPlanningFeaturePolicyError, match="type\|schema\|hash\|result"<br>        ) | 1 | Proves locally invalid result fast fails before source validation using the exact source reproduced in section 7. |
| `test_compiler_wrong_source_lock_fast_fails_before_source_validation` | none | pytest.raises(BessPlanningFeaturePolicyError, match="lock\|document") | 1 | Proves compiler wrong source lock fast fails before source validation using the exact source reproduced in section 7. |
| `test_forged_matching_lock_still_runs_source_complete_validation` | none | pytest.raises(BessPlanningFeaturePolicyError, match="Source-complete\|source") | 1 | Proves forged matching lock still runs source complete validation using the exact source reproduced in section 7. |
| `test_compiler_and_public_validator_invoke_source_complete_coding_validation` | none | none | 2 | Proves compiler and public validator invoke source complete coding validation using the exact source reproduced in section 7. |
| `test_public_policy_api_exports_only_stable_symbols` | none | none | 4 | Proves public policy api exports only stable symbols using the exact source reproduced in section 7. |
| `test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator` | none | pytest.raises(BessPlanningFeaturePolicyError, match="hash") | 1 | Proves step 7d 5b 2b 5 exposes lightweight policy result validator using the exact source reproduced in section 7. |
| `test_policy_manifest_rejects_nonportable_parquet_filename` | pytest.mark.parametrize(<br>    "filename",<br>    [<br>        "/tmp/file.parquet",<br>        "../file.parquet",<br>        "subdir/file.parquet",<br>        r"C:\absolute\file.parquet",<br>        "C:/absolute/file.parquet",<br>        r"\\server\share\file.parquet",<br>        r"subdir\file.parquet",<br>        "CON.parquet",<br>        "con.PARQUET",<br>        "NUL.parquet",<br>        "PRN.parquet",<br>        "AUX.parquet",<br>        "CLOCK$.parquet",<br>        "COM1.parquet",<br>        "COM9.parquet",<br>        "LPT1.parquet",<br>        "LPT9.parquet",<br>        "COM¹.parquet",<br>        "COM².parquet",<br>        "COM³.parquet",<br>        "LPT¹.parquet",<br>        "LPT².parquet",<br>        "LPT³.parquet",<br>        "file:name.parquet",<br>        "base.parquet:stream.parquet",<br>        "file?.parquet",<br>        "file*.parquet",<br>        "file<.parquet",<br>        "file>.parquet",<br>        "file\|.parquet",<br>        'file".parquet',<br>        "nul\x00.parquet",<br>        "line\nbreak.parquet",<br>        "del\x7f.parquet",<br>    ],<br>) | pytest.raises(ValueError, match="filename\|basename\|portable") | 0 | Proves policy manifest rejects nonportable parquet filename using the exact source reproduced in section 7. |
| `test_shared_filename_contract_rejects_superscript_windows_devices` | pytest.mark.parametrize(<br>    "filename",<br>    [<br>        "com¹.parquet",<br>        "CoM².parquet",<br>        "cOm³.parquet",<br>        "lpt¹.parquet",<br>        "LpT².parquet",<br>        "lPt³.parquet",<br>    ],<br>) | pytest.raises(ValueError, match="reserved\|basename\|portable") | 0 | Proves shared filename contract rejects superscript windows devices using the exact source reproduced in section 7. |
| `test_policy_manifest_rejects_unsupported_cnig_source_schema` | pytest.mark.parametrize(<br>    ("field", "version"),<br>    [<br>        ("cnig_profile_schema_version", 0),<br>        ("cnig_profile_schema_version", 1),<br>        ("cnig_profile_schema_version", 3),<br>        ("cnig_profile_schema_version", 999),<br>        ("cnig_result_hash_schema_version", 0),<br>        ("cnig_result_hash_schema_version", 1),<br>        ("cnig_result_hash_schema_version", 4),<br>        ("cnig_result_hash_schema_version", 6),<br>        ("cnig_result_hash_schema_version", 999),<br>    ],<br>) | pytest.raises(ValidationError, match="CNIG\|cnig\|schema\|version") | 0 | Proves policy manifest rejects unsupported cnig source schema using the exact source reproduced in section 7. |
| `test_policy_artifact_loader_rejects_source_schema_before_parquet_read` | pytest.mark.parametrize(<br>    ("field", "version"),<br>    [<br>        ("cnig_profile_schema_version", 0),<br>        ("cnig_profile_schema_version", 1),<br>        ("cnig_profile_schema_version", 3),<br>        ("cnig_profile_schema_version", 999),<br>        ("cnig_result_hash_schema_version", 0),<br>        ("cnig_result_hash_schema_version", 1),<br>        ("cnig_result_hash_schema_version", 4),<br>        ("cnig_result_hash_schema_version", 6),<br>        ("cnig_result_hash_schema_version", 999),<br>    ],<br>) | pytest.raises(<br>        BessPlanningFeaturePolicyError, match="CNIG\|cnig\|schema\|version"<br>    ) | 1 | Proves policy artifact loader rejects source schema before parquet read using the exact source reproduced in section 7. |
| `test_policy_envelope_rejects_canonical_empty_policy_table` | none | pytest.raises(<br>        BessPlanningFeaturePolicyError, match="policy\|table\|empty\|entry"<br>    ) | 0 | Proves policy envelope rejects canonical empty policy table using the exact source reproduced in section 7. |
| `test_policy_envelope_accepts_one_exact_policy_row` | none | none | 0 | Proves policy envelope accepts one exact policy row using the exact source reproduced in section 7. |
| `test_policy_envelope_accepts_current_twelve_row_snapshot` | none | none | 1 | Proves policy envelope accepts current twelve row snapshot using the exact source reproduced in section 7. |
| `test_policy_envelope_requires_cnig_profile_schema_two` | pytest.mark.parametrize("version", [0, 1, 3, 999]) | pytest.raises(BessPlanningFeaturePolicyError, match="profile schema\|schema") | 0 | Proves policy envelope requires cnig profile schema two using the exact source reproduced in section 7. |
| `test_policy_envelope_requires_cnig_result_schema_five` | pytest.mark.parametrize("version", [0, 1, 2, 4, 6, 999]) | pytest.raises(BessPlanningFeaturePolicyError, match="CNIG result\|schema") | 0 | Proves policy envelope requires cnig result schema five using the exact source reproduced in section 7. |
| `test_policy_envelope_validates_every_intrinsic_row_contract` | pytest.mark.parametrize(<br>    "mutation",<br>    [<br>        "duplicate-pair",<br>        "reordered-pairs",<br>        "malformed-code",<br>        "invalid-status",<br>        "invalid-confidence",<br>        "zero-priority",<br>        "negative-priority",<br>        "bool-priority",<br>        "status-two-priorities",<br>        "priority-two-statuses",<br>        "row-scope",<br>        "row-flag",<br>        "row-policy-sha",<br>        "row-cnig-profile",<br>        "row-cnig-sha",<br>        "row-cnig-result-sha",<br>        "literal-null-reference",<br>    ],<br>) | pytest.raises(<br>        BessPlanningFeaturePolicyError,<br>        match="policy\|pair\|order\|code\|status\|confidence\|priority\|scope\|flag\|CNIG\|null\|schema",<br>    ) | 0 | Proves policy envelope validates every intrinsic row contract using the exact source reproduced in section 7. |
| `test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1` | none | pytest.raises(BessPlanningFeaturePolicyError, match="type\|result") | 0 | Proves policy envelope requires exact type and accepts valid schema v1 using the exact source reproduced in section 7. |
| `test_policy_envelope_controls_malformed_result_type` | pytest.mark.parametrize("malformed", [None, object()]) | pytest.raises(BessPlanningFeaturePolicyError) | 0 | Proves policy envelope controls malformed result type using the exact source reproduced in section 7. |

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
import json
import tomllib
from dataclasses import fields, replace
from hashlib import sha256
from io import BytesIO
from pathlib import Path

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from pydantic import ValidationError
from test_resolve_planning_feature_codes import _integration_inputs

from landscout import stages
from landscout.common.artifact_paths import validate_portable_parquet_filename
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)
from landscout.stages.resolve_planning_feature_codes import (
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
)

POLICY_PATH = Path("configs/planning/muret_bess_cnig_feature_policy.yaml")
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"
STATUS_PRIORITIES = {
    "LIKELY_MATERIAL_CONSTRAINT": 50,
    "UNKNOWN": 40,
    "MATERIAL_REVIEW_REQUIRED": 30,
    "DESIGN_REVIEW_REQUIRED": 20,
    "CONTEXT_REVIEW_REQUIRED": 10,
}
EXPECTED_MURET_DECISIONS = {
    ("INFORMATION", "02", "00"): ("CONTEXT_REVIEW_REQUIRED", "HIGH"),
    ("INFORMATION", "14", "00"): ("CONTEXT_REVIEW_REQUIRED", "HIGH"),
    ("INFORMATION", "27", "00"): ("CONTEXT_REVIEW_REQUIRED", "HIGH"),
    ("INFORMATION", "99", "00"): ("UNKNOWN", "LOW"),
    ("PRESCRIPTION", "01", "00"): ("LIKELY_MATERIAL_CONSTRAINT", "HIGH"),
    ("PRESCRIPTION", "05", "00"): ("MATERIAL_REVIEW_REQUIRED", "HIGH"),
    ("PRESCRIPTION", "07", "00"): ("LIKELY_MATERIAL_CONSTRAINT", "MEDIUM"),
    ("PRESCRIPTION", "07", "04"): ("LIKELY_MATERIAL_CONSTRAINT", "HIGH"),
    ("PRESCRIPTION", "15", "00"): ("DESIGN_REVIEW_REQUIRED", "MEDIUM"),
    ("PRESCRIPTION", "15", "01"): ("DESIGN_REVIEW_REQUIRED", "HIGH"),
    ("PRESCRIPTION", "17", "00"): ("MATERIAL_REVIEW_REQUIRED", "MEDIUM"),
    ("PRESCRIPTION", "18", "00"): ("MATERIAL_REVIEW_REQUIRED", "HIGH"),
}
EXPECTED_POLICY_ENTRIES_SHA256 = (
    "1d3e63f1123000402065b74402cb1e2295db2ac5655209ce410aaf36bfc2be91"
)
EXPECTED_POLICY_SHA256 = (
    "1cfca0eb3d777e9b6604748e8a81609abe7b728de8d0695711cd569180df6489"
)
EXPECTED_POLICY_TABLE_SHA256 = (
    "225105fe488e21f8aa080751812dde1671340c26620cae1d8372c2e59488ed41"
)
EXPECTED_COMPLETE_RESULT_SHA256 = (
    "84a59b418f5a53bc61df73296964b2847cc5d3529c10d0c6912c96222edba09c"
)
EXPECTED_SOURCE_LOCK = {
    "document_id": "33edb4c9f6943c88d8d92518bff20bec",
    "archive_sha256": (
        "9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93"
    ),
    "cnig_profile": "cnig_plu_2017_muret_observed_pairs_v2",
    "cnig_profile_schema_version": 2,
    "cnig_profile_sha256": (
        "5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"
    ),
    "cnig_result_hash_schema_version": 5,
    "cnig_complete_result_content_sha256": (
        "b56b195b32914583e6599fe96b3d29977c52450c9755228d89ce7e192903ab3e"
    ),
}
ARTIFACT_KIND = "BESS_CNIG_FEATURE_POLICY_RESULT"


def _canonical_sha256(value: object) -> str:
    return sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def _policy_entry(row: object, position: int) -> dict[str, object]:
    statuses = tuple(STATUS_PRIORITIES)
    status = statuses[position % len(statuses)]
    legal_reference = row.legal_reference
    regulation_reference = row.regulation_or_annex_reference
    return {
        "feature_family": row.feature_family,
        "type_code": row.type_code,
        "subtype_code": row.subtype_code,
        "expected_official_label": row.official_label,
        "expected_legal_reference": (
            None if pd.isna(legal_reference) else legal_reference
        ),
        "expected_regulation_reference": (
            None if pd.isna(regulation_reference) else regulation_reference
        ),
        "precheck_status": status,
        "confidence": ("HIGH", "MEDIUM", "LOW")[position % 3],
        "rationale": f"Official pair {row.feature_family} {row.type_code}/{row.subtype_code} requires conservative review.",
        "required_human_action": "Review the official code meaning and the separate local planning material.",
        "limitations": "This entry does not interpret local text or establish authorization or prohibition.",
    }


def _compiled_fixture() -> tuple[
    tuple[object, ...],
    object,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
]:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    config = BessPlanningFeaturePolicyConfig.model_validate(
        _policy_payload(inputs, coded)
    )
    result = compile_bess_planning_feature_policy(*inputs, coded, config)
    return inputs, coded, config, result


def _policy_payload(inputs: tuple[object, ...], coded: object) -> dict[str, object]:
    entries = [
        _policy_entry(row, position)
        for position, row in enumerate(
            coded.code_dictionary.itertuples(index=False),
        )
    ]
    return {
        "schema_version": 1,
        "profile": "synthetic_bess_cnig_feature_policy_v1",
        "policy_scope": POLICY_SCOPE,
        "local_feature_text_interpreted": False,
        "local_regulation_content_interpreted": False,
        "legal_conclusion_produced": False,
        "source_lock": {
            "document_id": coded.source_document_id,
            "archive_sha256": coded.source_archive_sha256,
            "cnig_profile": coded.profile,
            "cnig_profile_schema_version": coded.profile_schema_version,
            "cnig_profile_sha256": coded.profile_sha256,
            "cnig_result_hash_schema_version": coded.result_hash_schema_version,
            "cnig_complete_result_content_sha256": (
                coded.complete_result_content_sha256
            ),
        },
        "status_priority": dict(STATUS_PRIORITIES),
        "canonical_policy_entries_sha256": _canonical_sha256(entries),
        "entries": entries,
    }


def _validated_config(payload: dict[str, object]) -> BessPlanningFeaturePolicyConfig:
    entries = payload["entries"]
    assert isinstance(entries, list)
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    return BessPlanningFeaturePolicyConfig.model_validate(payload)


def _artifact_manifest(
    result: BessPlanningFeaturePolicyResult,
    parquet: Path,
) -> dict[str, object]:
    scalar_names = tuple(
        field.name
        for field in fields(BessPlanningFeaturePolicyResult)
        if field.name != "policy_table"
    )
    return {
        "schema_version": 2,
        "artifact_kind": ARTIFACT_KIND,
        **{name: getattr(result, name) for name in scalar_names},
        "parquet_filename": parquet.name,
        "parquet_row_count": len(result.policy_table),
        "parquet_size_bytes": parquet.stat().st_size,
        "parquet_sha256": sha256(parquet.read_bytes()).hexdigest(),
        "policy_table_schema_signature": deterministic_frame_schema_signature(
            result.policy_table
        ),
    }


def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeaturePolicyResult,
) -> tuple[Path, Path, dict[str, object]]:
    parquet = tmp_path / "policy.parquet"
    manifest_path = tmp_path / "policy.json"
    result.policy_table.to_parquet(parquet, index=True)
    manifest = _artifact_manifest(result, parquet)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return parquet, manifest_path, manifest


def _checked_in_policy_result() -> BessPlanningFeaturePolicyResult:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    cnig_profile = load_cnig_feature_code_profile(
        Path("configs/planning/cnig_plu_2017_feature_codes.yaml")
    )
    cnig_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    policy_module = importlib.import_module(
        "landscout.stages.bess_planning_feature_policy"
    )
    locked_coded = replace(
        coded,
        profile=config.source_lock.cnig_profile,
        profile_schema_version=config.source_lock.cnig_profile_schema_version,
        profile_sha256=config.source_lock.cnig_profile_sha256,
        source_document_id=config.source_lock.document_id,
        source_archive_sha256=config.source_lock.archive_sha256,
        result_hash_schema_version=(config.source_lock.cnig_result_hash_schema_version),
        complete_result_content_sha256=(
            config.source_lock.cnig_complete_result_content_sha256
        ),
        code_dictionary=cnig_module._dictionary(
            cnig_profile, config.source_lock.cnig_profile_sha256
        ),
    )
    return policy_module._build_result(config, locked_coded)


def test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status() -> (
    None
):
    inputs, coded, config, result = _compiled_fixture()
    validate_bess_planning_feature_policy_result(*inputs, coded, config, result)
    assert result.policy_schema_version == 1
    assert result.result_hash_schema_version == 1
    assert result.policy_scope == POLICY_SCOPE
    assert len(result.policy_table) == len(coded.code_dictionary)
    assert not any(
        column in result.policy_table.columns
        for column in ("parcel_id", "planning_feature_id", "relation_type")
    )
    assert result.policy_table["local_feature_text_interpreted"].eq(False).all()
    assert result.policy_table["local_regulation_content_interpreted"].eq(False).all()
    assert result.policy_table["legal_conclusion_produced"].eq(False).all()


def test_checked_in_policy_pins_all_twelve_exact_muret_decisions() -> None:
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    actual = {
        (entry.feature_family, entry.type_code, entry.subtype_code): (
            entry.precheck_status,
            entry.confidence,
        )
        for entry in config.entries
    }
    assert actual == EXPECTED_MURET_DECISIONS
    assert config.status_priority == STATUS_PRIORITIES
    assert config.policy_scope == POLICY_SCOPE
    assert config.local_feature_text_interpreted is False
    assert config.local_regulation_content_interpreted is False
    assert config.legal_conclusion_produced is False
    assert len(config.entries) == 12
    assert ("PRESCRIPTION", "15", "00") in actual
    assert ("PRESCRIPTION", "15", "01") in actual
    assert all(len(key[1]) == len(key[2]) == 2 for key in actual)


def test_checked_in_policy_complete_snapshot_is_immutable() -> None:
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    assert config.schema_version == 1
    assert config.profile == "muret_bess_cnig_feature_policy_v1"
    assert config.policy_scope == POLICY_SCOPE
    assert config.local_feature_text_interpreted is False
    assert config.local_regulation_content_interpreted is False
    assert config.legal_conclusion_produced is False
    assert config.source_lock.model_dump(mode="json") == EXPECTED_SOURCE_LOCK
    assert config.status_priority == STATUS_PRIORITIES
    assert config.canonical_policy_entries_sha256 == EXPECTED_POLICY_ENTRIES_SHA256
    assert (
        _canonical_sha256([entry.model_dump(mode="json") for entry in config.entries])
        == EXPECTED_POLICY_ENTRIES_SHA256
    )
    assert _canonical_sha256(config.model_dump(mode="json")) == EXPECTED_POLICY_SHA256


def test_checked_in_compiled_policy_result_hashes_are_pinned() -> None:
    result = _checked_in_policy_result()
    assert result.policy_table_content_sha256 == EXPECTED_POLICY_TABLE_SHA256
    assert result.complete_result_content_sha256 == EXPECTED_COMPLETE_RESULT_SHA256


@pytest.mark.parametrize(
    "field",
    ["rationale", "required_human_action", "limitations"],
)
def test_profile_v1_snapshot_detects_policy_text_drift(field: str) -> None:
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    payload = config.model_dump(mode="json")
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0][field] = f"{entries[0][field]} Changed."
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    changed = BessPlanningFeaturePolicyConfig.model_validate(payload)
    assert changed.profile == "muret_bess_cnig_feature_policy_v1"
    assert _canonical_sha256(changed.model_dump(mode="json")) != EXPECTED_POLICY_SHA256


def test_profile_v1_snapshot_detects_source_lock_drift() -> None:
    config = load_bess_planning_feature_policy_config(POLICY_PATH)
    payload = config.model_dump(mode="json")
    source_lock = payload["source_lock"]
    assert isinstance(source_lock, dict)
    source_lock["document_id"] = "another-document"
    changed = BessPlanningFeaturePolicyConfig.model_validate(payload)
    assert changed.profile == "muret_bess_cnig_feature_policy_v1"
    assert _canonical_sha256(changed.model_dump(mode="json")) != EXPECTED_POLICY_SHA256


def test_pandas_is_a_direct_bounded_runtime_dependency() -> None:
    project = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))[
        "project"
    ]
    assert "pandas>=3.0,<4" in project["dependencies"]


def test_information_9900_official_references_remain_missing() -> None:
    _, _, _, result = _compiled_fixture()
    row = result.policy_table.loc[
        (result.policy_table["feature_family"] == "INFORMATION")
        & (result.policy_table["type_code"] == "99")
        & (result.policy_table["subtype_code"] == "00")
    ].iloc[0]
    assert pd.isna(row["official_legal_reference"])
    assert pd.isna(row["official_regulation_reference"])


@pytest.mark.parametrize(
    ("column", "literal"),
    [
        (column, literal)
        for column in (
            "official_legal_reference",
            "official_regulation_reference",
        )
        for literal in ("None", "nan", "<NA>")
    ],
)
def test_null_reference_literal_is_rejected_by_local_envelope(
    column: str,
    literal: str,
) -> None:
    _, _, _, result = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    table = result.policy_table.copy(deep=True)
    row = table.index[
        (table["feature_family"] == "INFORMATION")
        & (table["type_code"] == "99")
        & (table["subtype_code"] == "00")
    ][0]
    table.loc[row, column] = literal
    coordinated = module._result_with_hashes(replace(result, policy_table=table))
    with pytest.raises(BessPlanningFeaturePolicyError, match="reference|null|missing"):
        module._validate_result_envelope(coordinated)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("document_id", "another-document"),
        ("archive_sha256", "f" * 64),
        ("cnig_profile", "another-profile"),
        ("cnig_profile_schema_version", 1),
        ("cnig_profile_sha256", "f" * 64),
        ("cnig_result_hash_schema_version", 4),
        ("cnig_complete_result_content_sha256", "f" * 64),
    ],
)
def test_source_lock_mismatch_is_rejected(field: str, value: object) -> None:
    inputs, coded, config, _ = _compiled_fixture()
    changed_lock = config.source_lock.model_copy(update={field: value})
    changed = config.model_copy(update={"source_lock": changed_lock})
    with pytest.raises(BessPlanningFeaturePolicyError, match="lock|source|CNIG"):
        compile_bess_planning_feature_policy(*inputs, coded, changed)


def test_missing_policy_pair_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries.pop()
    config = _validated_config(payload)
    with pytest.raises(BessPlanningFeaturePolicyError, match="missing|pair"):
        compile_bess_planning_feature_policy(*inputs, coded, config)


def test_extra_policy_pair_is_rejected_without_type_fallback() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    extra = dict(entries[-1])
    extra.update(
        {
            "feature_family": "INFORMATION",
            "type_code": "98",
            "subtype_code": "00",
            "expected_official_label": "Synthetic extra official pair",
            "expected_legal_reference": None,
            "expected_regulation_reference": None,
        }
    )
    entries.append(extra)
    entries.sort(
        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"])
    )
    config = _validated_config(payload)
    with pytest.raises(BessPlanningFeaturePolicyError, match="extra|pair"):
        compile_bess_planning_feature_policy(*inputs, coded, config)


def test_duplicate_policy_pair_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries.append(dict(entries[0]))
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError, match="duplicate|pair"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_prescription_information_code_spaces_remain_separate() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0]["feature_family"] = "PRESCRIPTION"
    entries.sort(
        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"])
    )
    config = _validated_config(payload)
    with pytest.raises(BessPlanningFeaturePolicyError, match="missing|extra|pair"):
        compile_bess_planning_feature_policy(*inputs, coded, config)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("expected_official_label", "Wrong official label", "label"),
        ("expected_legal_reference", "Wrong legal reference", "legal"),
        ("expected_regulation_reference", "Wrong regulation reference", "regulation"),
    ],
)
def test_official_meaning_mismatch_is_rejected(
    field: str,
    value: object,
    message: str,
) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0][field] = value
    config = _validated_config(payload)
    with pytest.raises(BessPlanningFeaturePolicyError, match=message):
        compile_bess_planning_feature_policy(*inputs, coded, config)


@pytest.mark.parametrize("status", ["ALLOWED", "FORBIDDEN", "PROHIBITED"])
def test_invalid_or_legal_conclusion_status_is_rejected(status: str) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0]["precheck_status"] = status
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_invalid_confidence_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0]["confidence"] = "CERTAIN"
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


@pytest.mark.parametrize("mutation", ["duplicate", "missing", "zero", "bool", "string"])
def test_status_priority_contract_is_strict(mutation: str) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    priorities = payload["status_priority"]
    assert isinstance(priorities, dict)
    if mutation == "duplicate":
        priorities["UNKNOWN"] = priorities["LIKELY_MATERIAL_CONSTRAINT"]
    elif mutation == "missing":
        priorities.pop("UNKNOWN")
    elif mutation == "zero":
        priorities["UNKNOWN"] = 0
    elif mutation == "bool":
        priorities["UNKNOWN"] = True
    else:
        priorities["UNKNOWN"] = "40"
    with pytest.raises(ValidationError, match="priority|integer"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_status_priority_mapping_is_deeply_immutable() -> None:
    _, _, config, _ = _compiled_fixture()
    snapshot = config.model_dump(mode="python")

    with pytest.raises(TypeError, match="frozen mapping"):
        config.status_priority["UNKNOWN"] = 999

    assert config.model_dump(mode="python") == snapshot


def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.yaml"
    path.write_text("schema_version: 1\nschema_version: 1\n", encoding="utf-8")
    with pytest.raises(BessPlanningFeaturePolicyError, match="Duplicate YAML"):
        load_bess_planning_feature_policy_config(path)


def test_unknown_yaml_field_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    payload["unknown_field"] = "not allowed"
    with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_noncanonical_whitespace_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries[0]["rationale"] = " leading whitespace"
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError, match="whitespace|exact"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_malformed_sha256_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    payload["canonical_policy_entries_sha256"] = "NOT-A-SHA"
    with pytest.raises(ValidationError, match="SHA256"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_in_memory_config_is_revalidated_before_compilation() -> None:
    inputs, coded, config, _ = _compiled_fixture()
    corrupted = config.model_copy(update={"canonical_policy_entries_sha256": "f" * 64})
    with pytest.raises(BessPlanningFeaturePolicyError, match="in-memory|canonical"):
        compile_bess_planning_feature_policy(*inputs, coded, corrupted)


def test_policy_entries_require_deterministic_order() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    entries = payload["entries"]
    assert isinstance(entries, list)
    entries.reverse()
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    with pytest.raises(ValidationError, match="order"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)


def test_policy_table_is_sorted_and_preserves_leading_zero_codes() -> None:
    _, _, _, result = _compiled_fixture()
    keys = list(
        result.policy_table[["feature_family", "type_code", "subtype_code"]].itertuples(
            index=False, name=None
        )
    )
    assert keys == sorted(keys)
    assert all(
        len(type_code) == len(subtype_code) == 2 for _, type_code, subtype_code in keys
    )


def test_policy_table_mutation_is_rejected() -> None:
    inputs, coded, config, result = _compiled_fixture()
    table = result.policy_table.copy(deep=True)
    table.loc[table.index[0], "precheck_status"] = "UNKNOWN"
    with pytest.raises(BessPlanningFeaturePolicyError, match="hash|table|rebuilt"):
        validate_bess_planning_feature_policy_result(
            *inputs, coded, config, replace(result, policy_table=table)
        )


def test_coordinated_policy_table_and_hash_mutation_is_rejected() -> None:
    inputs, coded, config, result = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    table = result.policy_table.copy(deep=True)
    table.loc[table.index[0], "rationale"] = "Coordinated but false rationale."
    coordinated = module._result_with_hashes(replace(result, policy_table=table))
    with pytest.raises(BessPlanningFeaturePolicyError, match="table|rebuilt"):
        validate_bess_planning_feature_policy_result(
            *inputs, coded, config, coordinated
        )


def test_persisted_parquet_and_json_readback_is_source_complete(
    tmp_path: Path,
) -> None:
    inputs, coded, config, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    persisted = module.load_bess_planning_feature_policy_artifacts(
        parquet, manifest_path
    )
    assert_frame_equal(result.policy_table, persisted.policy_table, check_dtype=True)
    row = persisted.policy_table.loc[
        (persisted.policy_table["feature_family"] == "INFORMATION")
        & (persisted.policy_table["type_code"] == "99")
        & (persisted.policy_table["subtype_code"] == "00")
    ].iloc[0]
    assert pd.isna(row["official_legal_reference"])
    assert pd.isna(row["official_regulation_reference"])
    validate_bess_planning_feature_policy_result(*inputs, coded, config, persisted)


def test_artifact_manifest_model_is_strict_and_frozen(tmp_path: Path) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, _, manifest = _write_artifacts(tmp_path, result)
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    validated = module.BessPlanningFeaturePolicyArtifactManifest.model_validate(
        manifest
    )
    assert validated.schema_version == 2
    assert validated.artifact_kind == ARTIFACT_KIND
    assert validated.cnig_profile_schema_version == 2
    assert validated.cnig_result_hash_schema_version == 5
    assert validated.parquet_filename == parquet.name
    with pytest.raises(ValidationError):
        validated.parquet_row_count = 0


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda value: value.update(schema_version=1), "schema"),
        (lambda value: value.update(unknown_field=True), "manifest|artifact"),
        (lambda value: value.update(parquet_filename="other.parquet"), "filename"),
        (lambda value: value.update(parquet_row_count=999), "row"),
        (lambda value: value.update(parquet_size_bytes=999), "size"),
        (lambda value: value.update(parquet_sha256="f" * 64), "SHA|hash"),
        (
            lambda value: value["policy_table_schema_signature"].update(
                index_names=["changed"]
            ),
            "schema",
        ),
        (lambda value: value.update(policy_table_content_sha256="f" * 64), "hash"),
        (lambda value: value.update(complete_result_content_sha256="f" * 64), "hash"),
        (lambda value: value.pop("policy_profile"), "manifest|artifact"),
    ],
)
def test_artifact_loader_rejects_manifest_mismatch(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, manifest = _write_artifacts(tmp_path, result)
    assert callable(mutation)
    mutation(manifest)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError, match=message):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)


@pytest.mark.parametrize(
    "document",
    [
        '{"schema_version": 2, "schema_version": 2}\n',
        '{"schema_version": NaN}\n',
        '{"schema_version": Infinity}\n',
        "[]\n",
    ],
    ids=["duplicate-key", "nan", "infinity", "non-object"],
)
def test_artifact_loader_uses_strict_json_before_parquet_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    manifest_path.write_text(document, encoding="utf-8")
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    parquet_reads = 0

    def counted(*args: object, **kwargs: object) -> object:
        nonlocal parquet_reads
        parquet_reads += 1
        raise AssertionError("Parquet read preceded strict manifest validation")

    monkeypatch.setattr(module.pd, "read_parquet", counted)
    with pytest.raises(
        BessPlanningFeaturePolicyError,
        match="Duplicate JSON|finite|top-level|invalid",
    ):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
    assert parquet_reads == 0


def test_artifact_loader_rejects_parquet_replacement(tmp_path: Path) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    parquet.write_bytes(parquet.read_bytes() + b"changed-after-manifest")
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError, match="size|SHA|hash"):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)


def test_artifact_loader_parses_the_exact_verified_parquet_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    replacement = tmp_path / "replacement.parquet"
    result.policy_table.to_parquet(replacement, index=True, compression="gzip")
    original_read_bytes = Path.read_bytes
    verified_bytes = original_read_bytes(parquet)
    replacement_bytes = original_read_bytes(replacement)
    assert replacement_bytes != verified_bytes
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    original_read_parquet = module.pd.read_parquet
    replacement_performed = False
    parsed_payloads: list[tuple[str, bytes]] = []

    def replace_after_byte_read(path: Path) -> bytes:
        nonlocal replacement_performed
        payload = original_read_bytes(path)
        if path == parquet and not replacement_performed:
            path.write_bytes(replacement_bytes)
            replacement_performed = True
        return payload

    def old_hash_then_replace(path: Path) -> str:
        nonlocal replacement_performed
        payload = original_read_bytes(path)
        if path == parquet and not replacement_performed:
            path.write_bytes(replacement_bytes)
            replacement_performed = True
        return sha256(payload).hexdigest()

    def observed_read_parquet(
        source: object, *args: object, **kwargs: object
    ) -> object:
        if isinstance(source, BytesIO):
            parsed_payloads.append(("buffer", source.getvalue()))
        else:
            path = Path(source)
            parsed_payloads.append(("path", original_read_bytes(path)))
        return original_read_parquet(source, *args, **kwargs)

    monkeypatch.setattr(Path, "read_bytes", replace_after_byte_read)
    monkeypatch.setattr(module, "_file_sha256", old_hash_then_replace, raising=False)
    monkeypatch.setattr(module.pd, "read_parquet", observed_read_parquet)
    loaded = module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
    assert replacement_performed
    assert parsed_payloads == [("buffer", verified_bytes)]
    assert_frame_equal(result.policy_table, loaded.policy_table, check_dtype=True)


def test_locally_invalid_result_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, result = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    wrong_table = result.policy_table.drop(columns="confidence")
    invalid_results = (
        object(),
        replace(result, policy_schema_version=2),
        replace(result, policy_table=wrong_table),
        replace(result, policy_table_content_sha256="f" * 64),
        replace(result, complete_result_content_sha256="f" * 64),
    )
    for invalid in invalid_results:
        with pytest.raises(
            BessPlanningFeaturePolicyError, match="type|schema|hash|result"
        ):
            module.validate_bess_planning_feature_policy_result(
                *inputs, coded, config, invalid
            )
    assert calls == 0


def test_compiler_wrong_source_lock_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, _ = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    wrong_lock = config.source_lock.model_copy(
        update={"document_id": "another-document"}
    )
    wrong_config = config.model_copy(update={"source_lock": wrong_lock})
    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    with pytest.raises(BessPlanningFeaturePolicyError, match="lock|document"):
        module.compile_bess_planning_feature_policy(*inputs, coded, wrong_config)
    assert calls == 0


def test_forged_matching_lock_still_runs_source_complete_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, _ = _compiled_fixture()
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    actual = module.validate_planning_feature_code_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    forged_coded = replace(coded, source_document_id="forged-document")
    forged_lock = config.source_lock.model_copy(
        update={"document_id": "forged-document"}
    )
    forged_config = config.model_copy(update={"source_lock": forged_lock})
    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    with pytest.raises(BessPlanningFeaturePolicyError, match="Source-complete|source"):
        module.compile_bess_planning_feature_policy(
            *inputs, forged_coded, forged_config
        )
    assert calls == 1


def test_compiler_and_public_validator_invoke_source_complete_coding_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    config = BessPlanningFeaturePolicyConfig.model_validate(
        _policy_payload(inputs, coded)
    )
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    actual = module.validate_planning_feature_code_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    monkeypatch.setattr(module, "validate_planning_feature_code_result", counted)
    result = module.compile_bess_planning_feature_policy(*inputs, coded, config)
    assert calls == 1
    module.validate_bess_planning_feature_policy_result(*inputs, coded, config, result)
    assert calls == 2


def test_public_policy_api_exports_only_stable_symbols() -> None:
    required = {
        "BessPlanningFeaturePolicyArtifactManifest",
        "BessPlanningFeaturePolicyConfig",
        "BessPlanningFeaturePolicyError",
        "BessPlanningFeaturePolicyResult",
        "load_bess_planning_feature_policy_artifacts",
        "load_bess_planning_feature_policy_config",
        "compile_bess_planning_feature_policy",
        "validate_bess_planning_feature_policy_result",
        "validate_bess_planning_feature_policy_result_envelope",
    }
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    assert set(module.__all__) == required
    assert required.issubset(set(stages.__all__))
    assert all(getattr(stages, name) is getattr(module, name) for name in required)
    assert not any(name in module.__all__ for name in ("_canonical_sha256", "_lookup"))


def test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    assert hasattr(module, "validate_bess_planning_feature_policy_result_envelope")
    _, _, _, result = _compiled_fixture()
    module.validate_bess_planning_feature_policy_result_envelope(result)
    with pytest.raises(BessPlanningFeaturePolicyError, match="hash"):
        module.validate_bess_planning_feature_policy_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )


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
def test_policy_manifest_rejects_nonportable_parquet_filename(
    tmp_path: Path, filename: str
) -> None:
    _, _, _, result = _compiled_fixture()
    _, _, manifest = _write_artifacts(tmp_path, result)
    manifest["parquet_filename"] = filename
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(ValueError, match="filename|basename|portable"):
        module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)


@pytest.mark.parametrize(
    "filename",
    [
        "com¹.parquet",
        "CoM².parquet",
        "cOm³.parquet",
        "lpt¹.parquet",
        "LpT².parquet",
        "lPt³.parquet",
    ],
)
def test_shared_filename_contract_rejects_superscript_windows_devices(
    filename: str,
) -> None:
    with pytest.raises(ValueError, match="reserved|basename|portable"):
        validate_portable_parquet_filename(filename, "artifact filename")


@pytest.mark.parametrize(
    ("field", "version"),
    [
        ("cnig_profile_schema_version", 0),
        ("cnig_profile_schema_version", 1),
        ("cnig_profile_schema_version", 3),
        ("cnig_profile_schema_version", 999),
        ("cnig_result_hash_schema_version", 0),
        ("cnig_result_hash_schema_version", 1),
        ("cnig_result_hash_schema_version", 4),
        ("cnig_result_hash_schema_version", 6),
        ("cnig_result_hash_schema_version", 999),
    ],
)
def test_policy_manifest_rejects_unsupported_cnig_source_schema(
    tmp_path: Path,
    field: str,
    version: int,
) -> None:
    _, _, _, result = _compiled_fixture()
    _, _, manifest = _write_artifacts(tmp_path, result)
    manifest[field] = version
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(ValidationError, match="CNIG|cnig|schema|version"):
        module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)


@pytest.mark.parametrize(
    ("field", "version"),
    [
        ("cnig_profile_schema_version", 0),
        ("cnig_profile_schema_version", 1),
        ("cnig_profile_schema_version", 3),
        ("cnig_profile_schema_version", 999),
        ("cnig_result_hash_schema_version", 0),
        ("cnig_result_hash_schema_version", 1),
        ("cnig_result_hash_schema_version", 4),
        ("cnig_result_hash_schema_version", 6),
        ("cnig_result_hash_schema_version", 999),
    ],
)
def test_policy_artifact_loader_rejects_source_schema_before_parquet_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    version: int,
) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, manifest = _write_artifacts(tmp_path, result)
    manifest[field] = version
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    calls = {"bytes": 0, "parse": 0}
    original_read_bytes = Path.read_bytes

    def byte_read(path: Path, *args: object, **kwargs: object) -> bytes:
        if path == parquet:
            calls["bytes"] += 1
            raise AssertionError("Parquet bytes must not be read")
        return original_read_bytes(path)

    def parse(*args: object, **kwargs: object) -> pd.DataFrame:
        calls["parse"] += 1
        raise AssertionError("Parquet must not be parsed")

    monkeypatch.setattr(Path, "read_bytes", byte_read)
    monkeypatch.setattr(pd, "read_parquet", parse)
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(
        BessPlanningFeaturePolicyError, match="CNIG|cnig|schema|version"
    ):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
    assert calls == {"bytes": 0, "parse": 0}


def _rehash_policy_table(
    result: BessPlanningFeaturePolicyResult, table: pd.DataFrame
) -> BessPlanningFeaturePolicyResult:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    return module._result_with_hashes(replace(result, policy_table=table))


def _canonical_empty_policy_result(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
    table = result.policy_table.iloc[0:0].copy(deep=True)
    table.index = pd.Index([], dtype="int64")
    return _rehash_policy_table(result, table)


def test_policy_envelope_rejects_canonical_empty_policy_table() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    empty = _canonical_empty_policy_result(result)
    with pytest.raises(
        BessPlanningFeaturePolicyError, match="policy|table|empty|entry"
    ):
        module.validate_bess_planning_feature_policy_result_envelope(empty)


def test_policy_envelope_accepts_one_exact_policy_row() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    table = result.policy_table.iloc[[0]].copy(deep=True)
    table.index = pd.Index([0], dtype="int64")
    one_row = _rehash_policy_table(result, table)
    module.validate_bess_planning_feature_policy_result_envelope(one_row)


def test_policy_envelope_accepts_current_twelve_row_snapshot() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    result = _checked_in_policy_result()
    assert len(result.policy_table) == 12
    module.validate_bess_planning_feature_policy_result_envelope(result)


@pytest.mark.parametrize("version", [0, 1, 3, 999])
def test_policy_envelope_requires_cnig_profile_schema_two(version: int) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    changed = module._result_with_hashes(
        replace(result, cnig_profile_schema_version=version)
    )
    with pytest.raises(BessPlanningFeaturePolicyError, match="profile schema|schema"):
        module.validate_bess_planning_feature_policy_result_envelope(changed)


@pytest.mark.parametrize("version", [0, 1, 2, 4, 6, 999])
def test_policy_envelope_requires_cnig_result_schema_five(version: int) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    changed = module._result_with_hashes(
        replace(result, cnig_result_hash_schema_version=version)
    )
    with pytest.raises(BessPlanningFeaturePolicyError, match="CNIG result|schema"):
        module.validate_bess_planning_feature_policy_result_envelope(changed)


@pytest.mark.parametrize(
    "mutation",
    [
        "duplicate-pair",
        "reordered-pairs",
        "malformed-code",
        "invalid-status",
        "invalid-confidence",
        "zero-priority",
        "negative-priority",
        "bool-priority",
        "status-two-priorities",
        "priority-two-statuses",
        "row-scope",
        "row-flag",
        "row-policy-sha",
        "row-cnig-profile",
        "row-cnig-sha",
        "row-cnig-result-sha",
        "literal-null-reference",
    ],
)
def test_policy_envelope_validates_every_intrinsic_row_contract(
    mutation: str,
) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    table = result.policy_table.copy(deep=True)
    first, second = table.index[:2]
    if mutation == "duplicate-pair":
        table.loc[second, ["feature_family", "type_code", "subtype_code"]] = table.loc[
            first, ["feature_family", "type_code", "subtype_code"]
        ].tolist()
    elif mutation == "reordered-pairs":
        table = table.iloc[::-1].copy(deep=True)
    elif mutation == "malformed-code":
        table.loc[first, "type_code"] = "1"
    elif mutation == "invalid-status":
        table.loc[first, "precheck_status"] = "AUTHORIZED"
    elif mutation == "invalid-confidence":
        table.loc[first, "confidence"] = "CERTAIN"
    elif mutation == "zero-priority":
        table.loc[first, "status_priority"] = 0
    elif mutation == "negative-priority":
        table.loc[first, "status_priority"] = -1
    elif mutation == "bool-priority":
        values = table["status_priority"].astype("object")
        values.loc[first] = True
        table["status_priority"] = values
    elif mutation == "status-two-priorities":
        table.loc[second, "precheck_status"] = table.loc[first, "precheck_status"]
        table.loc[second, "status_priority"] = table.loc[first, "status_priority"] + 1
    elif mutation == "priority-two-statuses":
        different = table.index[
            table["precheck_status"] != table.loc[first, "precheck_status"]
        ][0]
        table.loc[different, "status_priority"] = table.loc[first, "status_priority"]
    elif mutation == "row-scope":
        table.loc[first, "policy_scope"] = "OTHER_SCOPE"
    elif mutation == "row-flag":
        table.loc[first, "local_feature_text_interpreted"] = True
    elif mutation == "row-policy-sha":
        table.loc[first, "policy_sha256"] = "a" * 64
    elif mutation == "row-cnig-profile":
        table.loc[first, "cnig_profile"] = "other-cnig-profile"
    elif mutation == "row-cnig-sha":
        table.loc[first, "cnig_profile_sha256"] = "a" * 64
    elif mutation == "row-cnig-result-sha":
        table.loc[first, "cnig_complete_result_content_sha256"] = "a" * 64
    else:
        table.loc[first, "official_legal_reference"] = "None"
    changed = _rehash_policy_table(result, table)
    with pytest.raises(
        BessPlanningFeaturePolicyError,
        match="policy|pair|order|code|status|confidence|priority|scope|flag|CNIG|null|schema",
    ):
        module.validate_bess_planning_feature_policy_result_envelope(changed)


def test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()

    class DerivedPolicyResult(BessPlanningFeaturePolicyResult):
        pass

    derived = DerivedPolicyResult(**result.__dict__)
    with pytest.raises(BessPlanningFeaturePolicyError, match="type|result"):
        module.validate_bess_planning_feature_policy_result_envelope(derived)
    module.validate_bess_planning_feature_policy_result_envelope(result)


@pytest.mark.parametrize("malformed", [None, object()])
def test_policy_envelope_controls_malformed_result_type(malformed: object) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError):
        module.validate_bess_planning_feature_policy_result_envelope(malformed)
```
