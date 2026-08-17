# `tests/unit/test_bess_planning_feature_policy.py`

## File identity

- Repository path: `tests/unit/test_bess_planning_feature_policy.py`
- File type: Python test
- Layer: unit/regression test
- Domain: test
- Responsibility: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.
- Source SHA256: `3f7bc1a603948f9de88b87aeac65b89eb5532cd30ef777780692b3ea6bffe981`

## 1. Purpose

Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

## 2. Position in LandScout architecture

This file belongs to the **unit/regression test** layer and the **test** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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

### A. Python constants

#### `POLICY_PATH`

```python
POLICY_PATH = Path("configs/planning/muret_bess_cnig_feature_policy.yaml")
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_apply_road_vehicle_proxy_policy.py::test_policy_path_must_be_path_or_none` (value argument/reference), `tests/unit/test_bess_planning_feature_policy.py::_checked_in_policy_result` (value argument/reference), `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_policy_pins_all_twelve_exact_muret_decisions` (value argument/reference), `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_policy_complete_snapshot_is_immutable` (value argument/reference), `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_policy_text_drift` (value argument/reference), `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_source_lock_drift` (value argument/reference), `tests/unit/test_road_vehicle_proxy_policy.py::test_checked_in_policy_hash_binds_exact_file_bytes` (value argument/reference).

#### `POLICY_SCOPE`

```python
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_build_result` (value argument/reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` (import/re-export), `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` (import/re-export).

#### `STATUS_PRIORITIES`

```python
STATUS_PRIORITIES = {
    "LIKELY_MATERIAL_CONSTRAINT": 50,
    "UNKNOWN": 40,
    "MATERIAL_REVIEW_REQUIRED": 30,
    "DESIGN_REVIEW_REQUIRED": 20,
    "CONTEXT_REVIEW_REQUIRED": 10,
}
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `tests/unit/test_bess_planning_feature_policy.py::_policy_entry` (value argument/reference), `tests/unit/test_bess_planning_feature_policy.py::_policy_payload` (value argument/reference).

#### `EXPECTED_MURET_DECISIONS`

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

Module-level technical/source/policy constant consumed by the exact references below.

#### `EXPECTED_POLICY_ENTRIES_SHA256`

```python
EXPECTED_POLICY_ENTRIES_SHA256 = (
    "1d3e63f1123000402065b74402cb1e2295db2ac5655209ce410aaf36bfc2be91"
)
```

Hash identity, algorithm, or canonical-content field used by the named integrity contract.

#### `EXPECTED_POLICY_SHA256`

```python
EXPECTED_POLICY_SHA256 = (
    "1cfca0eb3d777e9b6604748e8a81609abe7b728de8d0695711cd569180df6489"
)
```

Hash identity, algorithm, or canonical-content field used by the named integrity contract.

#### `EXPECTED_POLICY_TABLE_SHA256`

```python
EXPECTED_POLICY_TABLE_SHA256 = (
    "225105fe488e21f8aa080751812dde1671340c26620cae1d8372c2e59488ed41"
)
```

Hash identity, algorithm, or canonical-content field used by the named integrity contract.

#### `EXPECTED_COMPLETE_RESULT_SHA256`

```python
EXPECTED_COMPLETE_RESULT_SHA256 = (
    "84a59b418f5a53bc61df73296964b2847cc5d3529c10d0c6912c96222edba09c"
)
```

Hash identity, algorithm, or canonical-content field used by the named integrity contract.

#### `EXPECTED_SOURCE_LOCK`

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

Module-level technical/source/policy constant consumed by the exact references below.

#### `ARTIFACT_KIND`

```python
ARTIFACT_KIND = "BESS_CNIG_FEATURE_POLICY_RESULT"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1.DerivedPolicyResult`

**Purpose:** Encapsulates the test behavior implemented by its exact methods and attributes below.

**Kind:** class.

**Inheritance:** `BessPlanningFeaturePolicyResult`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1` via `DerivedPolicyResult`.

**Exact class source**

```python
class DerivedPolicyResult(BessPlanningFeaturePolicyResult):
        pass
```


## 6. Functions and methods

### `_canonical_sha256`

**Exact signature**

```python
def _canonical_sha256(value: object) -> str:
```

**Purpose**

Private `test` helper for canonical sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
sha256(json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest`.
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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_policy_entry`

**Exact signature**

```python
def _policy_entry(row: object, position: int) -> dict[str, object]:
```

**Purpose**

Private `test` helper for policy entry; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'feature_family': row.feature_family, 'type_code': row.type_code, 'subtype_code': row.subtype_code, 'expected_official_label': row.official_label, 'expected_legal_reference': None if pd.isna(legal_reference) else legal_reference, 'expected_regulation_reference': None if pd.isna(regulation_reference) else regulation_reference, 'precheck_status': status, 'confidence': ('HIGH', 'MEDIUM', 'LOW')[position % 3], 'rationale': f'Official pair {row.feature_family} {row.type_code}/{row.subtype_code} requires conservative review.', 'required_human_action': 'Review the official code meaning and the separate local planning material.', 'limitations': 'This entry does not interpret local text or establish authorization or prohibition.'}
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

- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::_policy_payload` via `_policy_entry`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_compiled_fixture`

**Exact signature**

```python
def _compiled_fixture() -> tuple[
    tuple[object, ...],
    object,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
]:
```

**Purpose**

Private `test` helper for compiled fixture; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[tuple[object, ...], object, BessPlanningFeaturePolicyConfig, BessPlanningFeaturePolicyResult]`.
- Every observed return expression is reproduced without truncation:
```python
(inputs, coded, config, result)
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

- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_application_fixture` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_and_relation_inputs_are_preserved_and_not_mutated` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `_compiled_fixture`.
- import/re-export: `tests/unit/test_apply_bess_planning_feature_policy.py::<module>` via `from test_bess_planning_feature_policy import (
    _canonical_empty_policy_result,
    _checked_in_policy_result,
    _compiled_fixture,
)`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_information_9900_official_references_remain_missing` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_null_reference_literal_is_rejected_by_local_envelope` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_source_lock_mismatch_is_rejected` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_in_memory_config_is_revalidated_before_compilation` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_table_is_sorted_and_preserves_leading_zero_codes` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_table_mutation_is_rejected` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_coordinated_policy_table_and_hash_mutation_is_rejected` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_persisted_parquet_and_json_readback_is_source_complete` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_manifest_model_is_strict_and_frozen` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_manifest_mismatch` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_duplicate_json_key` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_parquet_replacement` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_parses_the_exact_verified_parquet_bytes` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_manifest_rejects_nonportable_parquet_filename` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_manifest_rejects_unsupported_cnig_source_schema` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_artifact_loader_rejects_source_schema_before_parquet_read` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_rejects_canonical_empty_policy_table` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_accepts_one_exact_policy_row` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_requires_cnig_profile_schema_two` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_requires_cnig_result_schema_five` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_validates_every_intrinsic_row_contract` via `_compiled_fixture`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1` via `_compiled_fixture`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_policy_payload`

**Exact signature**

```python
def _policy_payload(inputs: tuple[object, ...], coded: object) -> dict[str, object]:
```

**Purpose**

Private `test` helper for policy payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'schema_version': 1, 'profile': 'synthetic_bess_cnig_feature_policy_v1', 'policy_scope': POLICY_SCOPE, 'local_feature_text_interpreted': False, 'local_regulation_content_interpreted': False, 'legal_conclusion_produced': False, 'source_lock': {'document_id': coded.source_document_id, 'archive_sha256': coded.source_archive_sha256, 'cnig_profile': coded.profile, 'cnig_profile_schema_version': coded.profile_schema_version, 'cnig_profile_sha256': coded.profile_sha256, 'cnig_result_hash_schema_version': coded.result_hash_schema_version, 'cnig_complete_result_content_sha256': coded.complete_result_content_sha256}, 'status_priority': dict(STATUS_PRIORITIES), 'canonical_policy_entries_sha256': _canonical_sha256(entries), 'entries': entries}
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

- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::_compiled_fixture` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_missing_policy_pair_is_rejected` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_extra_policy_pair_is_rejected_without_type_fallback` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_duplicate_policy_pair_is_rejected` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_prescription_information_code_spaces_remain_separate` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_official_meaning_mismatch_is_rejected` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_invalid_or_legal_conclusion_status_is_rejected` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_invalid_confidence_is_rejected` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_status_priority_contract_is_strict` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_unknown_yaml_field_is_rejected` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_noncanonical_whitespace_is_rejected` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_malformed_sha256_is_rejected` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_entries_require_deterministic_order` via `_policy_payload`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `_policy_payload`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_validated_config`

**Exact signature**

```python
def _validated_config(payload: dict[str, object]) -> BessPlanningFeaturePolicyConfig:
```

**Purpose**

Checks and returns canonical config; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessPlanningFeaturePolicyConfig`.
- Every observed return expression is reproduced without truncation:
```python
BessPlanningFeaturePolicyConfig.model_validate(payload)
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
- In-memory mutation: `payload['canonical_policy_entries_sha256']`.
- Input mutation: `payload['canonical_policy_entries_sha256']`.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::download_inpn_protected_areas_archive` via `_validated_config`.
- direct call or construction: `src/landscout/sources/inpn_protected_areas_fr.py::extract_inpn_protected_areas_archive` via `_validated_config`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_missing_policy_pair_is_rejected` via `_validated_config`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_extra_policy_pair_is_rejected_without_type_fallback` via `_validated_config`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_prescription_information_code_spaces_remain_separate` via `_validated_config`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_official_meaning_mismatch_is_rejected` via `_validated_config`.

**Complete source-ordered implementation**

```python
def _validated_config(payload: dict[str, object]) -> BessPlanningFeaturePolicyConfig:
    entries = payload["entries"]
    assert isinstance(entries, list)
    payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
    return BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_artifact_manifest`

**Exact signature**

```python
def _artifact_manifest(
    result: BessPlanningFeaturePolicyResult,
    parquet: Path,
) -> dict[str, object]:
```

**Purpose**

Private `test` helper for artifact manifest; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'schema_version': 2, 'artifact_kind': ARTIFACT_KIND, **{name: getattr(result, name) for name in scalar_names}, 'parquet_filename': parquet.name, 'parquet_row_count': len(result.policy_table), 'parquet_size_bytes': parquet.stat().st_size, 'parquet_sha256': sha256(parquet.read_bytes()).hexdigest(), 'policy_table_schema_signature': deterministic_frame_schema_signature(result.policy_table)}
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `parquet.read_bytes`, `parquet.stat`, `sha256(parquet.read_bytes()).hexdigest`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(parquet.read_bytes()).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::_write_artifacts` via `_artifact_manifest`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_artifacts`

**Exact signature**

```python
def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeaturePolicyResult,
) -> tuple[Path, Path, dict[str, object]]:
```

**Purpose**

Serializes artifacts; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[Path, Path, dict[str, object]]`.
- Every observed return expression is reproduced without truncation:
```python
(parquet, manifest_path, manifest)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: `manifest_path.write_text`, `result.policy_table.to_parquet`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_relation_identity_artifact_corruption_fails_locally` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_controlling_relation_cannot_be_relabelled_contextual_in_artifact` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_two_file_verified_byte_artifacts_and_source_readback` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_artifact_manifest_corruption_is_rejected` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_json_and_physical_replacement_are_rejected` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_verified_bytes_are_the_bytes_parsed` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_accepts_only_supplied_upstreams` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_manifest_filenames_are_casefold_unique` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_manifest_rejects_nonportable_filename` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_persisted_parquet_and_json_readback_is_source_complete` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_manifest_model_is_strict_and_frozen` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_manifest_mismatch` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_duplicate_json_key` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_parquet_replacement` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_parses_the_exact_verified_parquet_bytes` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_manifest_rejects_nonportable_parquet_filename` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_manifest_rejects_unsupported_cnig_source_schema` via `_write_artifacts`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_artifact_loader_rejects_source_schema_before_parquet_read` via `_write_artifacts`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_checked_in_policy_result`

**Exact signature**

```python
def _checked_in_policy_result() -> BessPlanningFeaturePolicyResult:
```

**Purpose**

Private `test` helper for checked in policy result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeaturePolicyResult`.
- Every observed return expression is reproduced without truncation:
```python
policy_module._build_result(config, locked_coded)
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

- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct` via `_checked_in_policy_result`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_pair_remains_present_with_true_null_decision_fields` via `_checked_in_policy_result`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_inconsistent_official_status_and_policy_match_is_rejected` via `_checked_in_policy_result`.
- import/re-export: `tests/unit/test_apply_bess_planning_feature_policy.py::<module>` via `from test_bess_planning_feature_policy import (
    _canonical_empty_policy_result,
    _checked_in_policy_result,
    _compiled_fixture,
)`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_compiled_policy_result_hashes_are_pinned` via `_checked_in_policy_result`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_accepts_current_twelve_row_snapshot` via `_checked_in_policy_result`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, result = _compiled_fixture()
```

**Action**

```python
validate_bess_planning_feature_policy_result(*inputs, coded, config, result)
```

**Expected result**

```python
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

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_checked_in_policy_pins_all_twelve_exact_muret_decisions`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
actual = {
        (entry.feature_family, entry.type_code, entry.subtype_code): (
            entry.precheck_status,
            entry.confidence,
        )
        for entry in config.entries
    }
```

**Action**

```python
config = load_bess_planning_feature_policy_config(POLICY_PATH)
```

**Expected result**

```python
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

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_checked_in_policy_complete_snapshot_is_immutable`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
# No separate setup statement.
```

**Action**

```python
config = load_bess_planning_feature_policy_config(POLICY_PATH)
```

**Expected result**

```python
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

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_checked_in_compiled_policy_result_hashes_are_pinned`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
result = _checked_in_policy_result()
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert result.policy_table_content_sha256 == EXPECTED_POLICY_TABLE_SHA256
assert result.complete_result_content_sha256 == EXPECTED_COMPLETE_RESULT_SHA256
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_checked_in_compiled_policy_result_hashes_are_pinned() -> None:
    result = _checked_in_policy_result()
    assert result.policy_table_content_sha256 == EXPECTED_POLICY_TABLE_SHA256
    assert result.complete_result_content_sha256 == EXPECTED_COMPLETE_RESULT_SHA256
```

### `test_profile_v1_snapshot_detects_policy_text_drift`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`.

**Setup**

```python
payload = config.model_dump(mode="json")
entries = payload["entries"]
entries[0][field] = f"{entries[0][field]} Changed."
payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
changed = BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Action**

```python
config = load_bess_planning_feature_policy_config(POLICY_PATH)
```

**Expected result**

```python
assert isinstance(entries, list)
assert changed.profile == "muret_bess_cnig_feature_policy_v1"
assert _canonical_sha256(changed.model_dump(mode="json")) != EXPECTED_POLICY_SHA256
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_profile_v1_snapshot_detects_source_lock_drift`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
payload = config.model_dump(mode="json")
source_lock = payload["source_lock"]
source_lock["document_id"] = "another-document"
changed = BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Action**

```python
config = load_bess_planning_feature_policy_config(POLICY_PATH)
```

**Expected result**

```python
assert isinstance(source_lock, dict)
assert changed.profile == "muret_bess_cnig_feature_policy_v1"
assert _canonical_sha256(changed.model_dump(mode="json")) != EXPECTED_POLICY_SHA256
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_pandas_is_a_direct_bounded_runtime_dependency`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
project = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))[
        "project"
    ]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert "pandas>=3.0,<4" in project["dependencies"]
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_pandas_is_a_direct_bounded_runtime_dependency() -> None:
    project = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))[
        "project"
    ]
    assert "pandas>=3.0,<4" in project["dependencies"]
```

### `test_information_9900_official_references_remain_missing`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, result = _compiled_fixture()
row = result.policy_table.loc[
        (result.policy_table["feature_family"] == "INFORMATION")
        & (result.policy_table["type_code"] == "99")
        & (result.policy_table["subtype_code"] == "00")
    ].iloc[0]
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert pd.isna(row["official_legal_reference"])
assert pd.isna(row["official_regulation_reference"])
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_null_reference_literal_is_rejected_by_local_envelope`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `column`, `literal`.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="reference|null|missing"):
        module._validate_result_envelope(coordinated)
```

**Regression protected**

Pins true-null handling and prevents textual or malformed null-like values from changing the contract.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_source_lock_mismatch_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `value`.

**Setup**

```python
inputs, coded, config, _ = _compiled_fixture()
changed_lock = config.source_lock.model_copy(update={field: value})
changed = config.model_copy(update={"source_lock": changed_lock})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="lock|source|CNIG"):
        compile_bess_planning_feature_policy(*inputs, coded, changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_source_lock_mismatch_is_rejected(field: str, value: object) -> None:
    inputs, coded, config, _ = _compiled_fixture()
    changed_lock = config.source_lock.model_copy(update={field: value})
    changed = config.model_copy(update={"source_lock": changed_lock})
    with pytest.raises(BessPlanningFeaturePolicyError, match="lock|source|CNIG"):
        compile_bess_planning_feature_policy(*inputs, coded, changed)
```

### `test_missing_policy_pair_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
payload = _policy_payload(inputs, coded)
entries = payload["entries"]
entries.pop()
config = _validated_config(payload)
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
assert isinstance(entries, list)
with pytest.raises(BessPlanningFeaturePolicyError, match="missing|pair"):
        compile_bess_planning_feature_policy(*inputs, coded, config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_extra_policy_pair_is_rejected_without_type_fallback`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
payload = _policy_payload(inputs, coded)
entries = payload["entries"]
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
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
assert isinstance(entries, list)
with pytest.raises(BessPlanningFeaturePolicyError, match="extra|pair"):
        compile_bess_planning_feature_policy(*inputs, coded, config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_duplicate_policy_pair_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
payload = _policy_payload(inputs, coded)
entries = payload["entries"]
entries.append(dict(entries[0]))
payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
assert isinstance(entries, list)
with pytest.raises(ValidationError, match="duplicate|pair"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_prescription_information_code_spaces_remain_separate`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
payload = _policy_payload(inputs, coded)
entries = payload["entries"]
entries[0]["feature_family"] = "PRESCRIPTION"
entries.sort(
        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"])
    )
config = _validated_config(payload)
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
assert isinstance(entries, list)
with pytest.raises(BessPlanningFeaturePolicyError, match="missing|extra|pair"):
        compile_bess_planning_feature_policy(*inputs, coded, config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_official_meaning_mismatch_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `field`, `message`, `value`.

**Setup**

```python
inputs = _integration_inputs()
payload = _policy_payload(inputs, coded)
entries = payload["entries"]
entries[0][field] = value
config = _validated_config(payload)
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
assert isinstance(entries, list)
with pytest.raises(BessPlanningFeaturePolicyError, match=message):
        compile_bess_planning_feature_policy(*inputs, coded, config)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_invalid_or_legal_conclusion_status_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `status`.

**Setup**

```python
inputs = _integration_inputs()
payload = _policy_payload(inputs, coded)
entries = payload["entries"]
entries[0]["precheck_status"] = status
payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
assert isinstance(entries, list)
with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_invalid_confidence_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
payload = _policy_payload(inputs, coded)
entries = payload["entries"]
entries[0]["confidence"] = "CERTAIN"
payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
assert isinstance(entries, list)
with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_status_priority_contract_is_strict`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
inputs = _integration_inputs()
payload = _policy_payload(inputs, coded)
priorities = payload["status_priority"]
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
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
assert isinstance(priorities, dict)
with pytest.raises(ValidationError, match="priority|integer"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_duplicate_yaml_key_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
path = tmp_path / "duplicate.yaml"
path.write_text("schema_version: 1\nschema_version: 1\n", encoding="utf-8")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="Duplicate YAML"):
        load_bess_planning_feature_policy_config(path)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.yaml"
    path.write_text("schema_version: 1\nschema_version: 1\n", encoding="utf-8")
    with pytest.raises(BessPlanningFeaturePolicyError, match="Duplicate YAML"):
        load_bess_planning_feature_policy_config(path)
```

### `test_unknown_yaml_field_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
payload = _policy_payload(inputs, coded)
payload["unknown_field"] = "not allowed"
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_unknown_yaml_field_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    payload["unknown_field"] = "not allowed"
    with pytest.raises(ValidationError):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

### `test_noncanonical_whitespace_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
payload = _policy_payload(inputs, coded)
entries = payload["entries"]
entries[0]["rationale"] = " leading whitespace"
payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
assert isinstance(entries, list)
with pytest.raises(ValidationError, match="whitespace|exact"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_malformed_sha256_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
payload = _policy_payload(inputs, coded)
payload["canonical_policy_entries_sha256"] = "NOT-A-SHA"
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
with pytest.raises(ValidationError, match="SHA256"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_malformed_sha256_is_rejected() -> None:
    inputs = _integration_inputs()
    coded = resolve_planning_feature_codes(*inputs)
    payload = _policy_payload(inputs, coded)
    payload["canonical_policy_entries_sha256"] = "NOT-A-SHA"
    with pytest.raises(ValidationError, match="SHA256"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

### `test_in_memory_config_is_revalidated_before_compilation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, _ = _compiled_fixture()
corrupted = config.model_copy(update={"canonical_policy_entries_sha256": "f" * 64})
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="in-memory|canonical"):
        compile_bess_planning_feature_policy(*inputs, coded, corrupted)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_in_memory_config_is_revalidated_before_compilation() -> None:
    inputs, coded, config, _ = _compiled_fixture()
    corrupted = config.model_copy(update={"canonical_policy_entries_sha256": "f" * 64})
    with pytest.raises(BessPlanningFeaturePolicyError, match="in-memory|canonical"):
        compile_bess_planning_feature_policy(*inputs, coded, corrupted)
```

### `test_policy_entries_require_deterministic_order`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
payload = _policy_payload(inputs, coded)
entries = payload["entries"]
entries.reverse()
payload["canonical_policy_entries_sha256"] = _canonical_sha256(entries)
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
```

**Expected result**

```python
assert isinstance(entries, list)
with pytest.raises(ValidationError, match="order"):
        BessPlanningFeaturePolicyConfig.model_validate(payload)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_policy_table_is_sorted_and_preserves_leading_zero_codes`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, result = _compiled_fixture()
keys = list(
        result.policy_table[["feature_family", "type_code", "subtype_code"]].itertuples(
            index=False, name=None
        )
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert keys == sorted(keys)
assert all(
        len(type_code) == len(subtype_code) == 2 for _, type_code, subtype_code in keys
    )
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_policy_table_mutation_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, result = _compiled_fixture()
table = result.policy_table.copy(deep=True)
table.loc[table.index[0], "precheck_status"] = "UNKNOWN"
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="hash|table|rebuilt"):
        validate_bess_planning_feature_policy_result(
            *inputs, coded, config, replace(result, policy_table=table)
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_coordinated_policy_table_and_hash_mutation_is_rejected`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs, coded, config, result = _compiled_fixture()
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
table = result.policy_table.copy(deep=True)
table.loc[table.index[0], "rationale"] = "Coordinated but false rationale."
coordinated = module._result_with_hashes(replace(result, policy_table=table))
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="table|rebuilt"):
        validate_bess_planning_feature_policy_result(
            *inputs, coded, config, coordinated
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_persisted_parquet_and_json_readback_is_source_complete`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
validate_bess_planning_feature_policy_result(*inputs, coded, config, persisted)
```

**Expected result**

```python
assert pd.isna(row["official_legal_reference"])
assert pd.isna(row["official_regulation_reference"])
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_artifact_manifest_model_is_strict_and_frozen`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, result = _compiled_fixture()
parquet, _, manifest = _write_artifacts(tmp_path, result)
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
validated = module.BessPlanningFeaturePolicyArtifactManifest.model_validate(
        manifest
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert validated.schema_version == 2
assert validated.artifact_kind == ARTIFACT_KIND
assert validated.cnig_profile_schema_version == 2
assert validated.cnig_result_hash_schema_version == 5
assert validated.parquet_filename == parquet.name
with pytest.raises(ValidationError):
        validated.parquet_row_count = 0
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_artifact_loader_rejects_manifest_mismatch`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `message`, `mutation`.

**Setup**

```python
_, _, _, result = _compiled_fixture()
parquet, manifest_path, manifest = _write_artifacts(tmp_path, result)
mutation(manifest)
manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert callable(mutation)
with pytest.raises(BessPlanningFeaturePolicyError, match=message):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_artifact_loader_rejects_duplicate_json_key`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, result = _compiled_fixture()
parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
manifest_path.write_text(
        '{"schema_version": 2, "schema_version": 2}\n', encoding="utf-8"
    )
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="Duplicate JSON"):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_artifact_loader_rejects_duplicate_json_key(tmp_path: Path) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    manifest_path.write_text(
        '{"schema_version": 2, "schema_version": 2}\n', encoding="utf-8"
    )
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError, match="Duplicate JSON"):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
```

### `test_artifact_loader_rejects_parquet_replacement`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, result = _compiled_fixture()
parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
parquet.write_bytes(parquet.read_bytes() + b"changed-after-manifest")
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="size|SHA|hash"):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

```python
def test_artifact_loader_rejects_parquet_replacement(tmp_path: Path) -> None:
    _, _, _, result = _compiled_fixture()
    parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
    parquet.write_bytes(parquet.read_bytes() + b"changed-after-manifest")
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError, match="size|SHA|hash"):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
```

### `test_artifact_loader_parses_the_exact_verified_parquet_bytes`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
_, _, _, result = _compiled_fixture()
parquet, manifest_path, _ = _write_artifacts(tmp_path, result)
replacement = tmp_path / "replacement.parquet"
result.policy_table.to_parquet(replacement, index=True, compression="gzip")
original_read_bytes = Path.read_bytes
verified_bytes = original_read_bytes(parquet)
replacement_bytes = original_read_bytes(replacement)
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
assert_frame_equal(result.policy_table, loaded.policy_table, check_dtype=True)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert replacement_bytes != verified_bytes
assert replacement_performed
assert parsed_payloads == [("buffer", verified_bytes)]
```

**Regression protected**

Prevents a schema-compatible-looking frame from replacing the canonical dtype contract with an object/category/other representation.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_artifact_loader_parses_the_exact_verified_parquet_bytes.replace_after_byte_read`

**Exact signature**

```python
def replace_after_byte_read(path: Path) -> bytes:
```

**Purpose**

Private `test` helper for replace after byte read; its complete implementation below is the authoritative behavioral contract.

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

- Network I/O: none directly visible.
- Filesystem read: `original_read_bytes`.
- Filesystem write: `path.write_bytes`.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_parses_the_exact_verified_parquet_bytes` via `monkeypatch.setattr(Path, 'read_bytes', replace_after_byte_read)`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_parses_the_exact_verified_parquet_bytes.old_hash_then_replace`

**Exact signature**

```python
def old_hash_then_replace(path: Path) -> str:
```

**Purpose**

Private `test` helper for old hash then replace; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
sha256(payload).hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `original_read_bytes`.
- Filesystem write: `path.write_bytes`.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(payload).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_parses_the_exact_verified_parquet_bytes` via `monkeypatch.setattr(module, '_file_sha256', old_hash_then_replace, raising=False)`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_parses_the_exact_verified_parquet_bytes.observed_read_parquet`

**Exact signature**

```python
def observed_read_parquet(
        source: object, *args: object, **kwargs: object
    ) -> object:
```

**Purpose**

Private `test` helper for observed read parquet; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
original_read_parquet(source, *args, **kwargs)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `original_read_bytes`, `original_read_parquet`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_parses_the_exact_verified_parquet_bytes` via `monkeypatch.setattr(module.pd, 'read_parquet', observed_read_parquet)`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_locally_invalid_result_fast_fails_before_source_validation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
for invalid in invalid_results:
        with pytest.raises(
            BessPlanningFeaturePolicyError, match="type|schema|hash|result"
        ):
            module.validate_bess_planning_feature_policy_result(
                *inputs, coded, config, invalid
            )
assert calls == 0
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

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

### `test_locally_invalid_result_fast_fails_before_source_validation.counted`

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_compiler_wrong_source_lock_fast_fails_before_source_validation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="lock|document"):
        module.compile_bess_planning_feature_policy(*inputs, coded, wrong_config)
assert calls == 0
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

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

### `test_compiler_wrong_source_lock_fast_fails_before_source_validation.counted`

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_forged_matching_lock_still_runs_source_complete_validation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="Source-complete|source"):
        module.compile_bess_planning_feature_policy(
            *inputs, forged_coded, forged_config
        )
assert calls == 1
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

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

### `test_forged_matching_lock_still_runs_source_complete_validation.counted`

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_compiler_and_public_validator_invoke_source_complete_coding_validation`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
inputs = _integration_inputs()
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
```

**Action**

```python
coded = resolve_planning_feature_codes(*inputs)
result = module.compile_bess_planning_feature_policy(*inputs, coded, config)
module.validate_bess_planning_feature_policy_result(*inputs, coded, config, result)
```

**Expected result**

```python
assert calls == 1
assert calls == 2
```

**Regression protected**

Prevents a self-consistent but forged local object from bypassing the independent source-complete revalidation boundary.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.

**Complete test implementation**

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

### `test_compiler_and_public_validator_invoke_source_complete_coding_validation.counted`

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_application_result', counted)`.
- callback/function object: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `monkeypatch.setattr(module, 'validate_bess_planning_feature_policy_result', counted)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads` via `monkeypatch.setattr(Path, 'read_bytes', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `monkeypatch.setattr(module, 'validate_planning_feature_code_result', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `monkeypatch.setattr(interpret_module, 'validate_normalized_planning_zoning_inputs', counted)`.
- callback/function object: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `monkeypatch.setattr(interpret_module, 'validate_planning_regulation_structure_with_fragments', counted)`.

**Complete source-ordered implementation**

```python
def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_policy_api_exports_only_stable_symbols`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert set(module.__all__) == required
assert required.issubset(set(stages.__all__))
assert all(getattr(stages, name) is getattr(module, name) for name in required)
assert not any(name in module.__all__ for name in ("_canonical_sha256", "_lookup"))
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
_, _, _, result = _compiled_fixture()
module.validate_bess_planning_feature_policy_result_envelope(result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert hasattr(module, "validate_bess_planning_feature_policy_result_envelope")
with pytest.raises(BessPlanningFeaturePolicyError, match="hash"):
        module.validate_bess_planning_feature_policy_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_policy_manifest_rejects_nonportable_parquet_filename`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `filename`.

**Setup**

```python
_, _, _, result = _compiled_fixture()
_, _, manifest = _write_artifacts(tmp_path, result)
manifest["parquet_filename"] = filename
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValueError, match="filename|basename|portable"):
        module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_shared_filename_contract_rejects_superscript_windows_devices`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `filename`.

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
with pytest.raises(ValueError, match="reserved|basename|portable"):
        validate_portable_parquet_filename(filename, "artifact filename")
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_shared_filename_contract_rejects_superscript_windows_devices(
    filename: str,
) -> None:
    with pytest.raises(ValueError, match="reserved|basename|portable"):
        validate_portable_parquet_filename(filename, "artifact filename")
```

### `test_policy_manifest_rejects_unsupported_cnig_source_schema`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`, `version`.

**Setup**

```python
_, _, _, result = _compiled_fixture()
_, _, manifest = _write_artifacts(tmp_path, result)
manifest[field] = version
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(ValidationError, match="CNIG|cnig|schema|version"):
        module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

### `test_policy_artifact_loader_rejects_source_schema_before_parquet_read`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: `tmp_path` (pytest/plugin or imported fixture), `monkeypatch` (pytest/plugin or imported fixture).
- `pytest.mark.parametrize` arguments: `field`, `version`.

**Setup**

```python
_, _, _, result = _compiled_fixture()
parquet, manifest_path, manifest = _write_artifacts(tmp_path, result)
manifest[field] = version
manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
calls = {"bytes": 0, "parse": 0}
def byte_read(*args: object, **kwargs: object) -> bytes:
        calls["bytes"] += 1
        raise AssertionError("Parquet bytes must not be read")
def parse(*args: object, **kwargs: object) -> pd.DataFrame:
        calls["parse"] += 1
        raise AssertionError("Parquet must not be parsed")
monkeypatch.setattr(Path, "read_bytes", byte_read)
monkeypatch.setattr(pd, "read_parquet", parse)
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeaturePolicyError, match="CNIG|cnig|schema|version"
    ):
        module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)
assert calls == {"bytes": 0, "parse": 0}
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- Mocks/monkeypatches replace the exact callbacks visible in the source; no unshown production path is implied.
- Uses a temporary synthetic filesystem/source.

**Complete test implementation**

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

    def byte_read(*args: object, **kwargs: object) -> bytes:
        calls["bytes"] += 1
        raise AssertionError("Parquet bytes must not be read")

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

### `test_policy_artifact_loader_rejects_source_schema_before_parquet_read.byte_read`

**Exact signature**

```python
def byte_read(*args: object, **kwargs: object) -> bytes:
```

**Purpose**

Private `test` helper for byte read; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bytes`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('Parquet bytes must not be read')`.

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

- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_policy_artifact_loader_rejects_source_schema_before_parquet_read` via `monkeypatch.setattr(Path, 'read_bytes', byte_read)`.

**Complete source-ordered implementation**

```python
def byte_read(*args: object, **kwargs: object) -> bytes:
        calls["bytes"] += 1
        raise AssertionError("Parquet bytes must not be read")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_artifact_loader_rejects_source_schema_before_parquet_read.parse`

**Exact signature**

```python
def parse(*args: object, **kwargs: object) -> pd.DataFrame:
```

**Purpose**

Parses parse; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `AssertionError('Parquet must not be parsed')`.

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

- direct call or construction: `src/landscout/sources/gpu_fr.py::_discover_standard_models` via `ElementTree.parse`.
- property/attribute access: `src/landscout/sources/gpu_fr.py::_discover_standard_models` via `ElementTree.parse`.
- callback/function object: `tests/unit/test_bess_planning_feature_policy.py::test_policy_artifact_loader_rejects_source_schema_before_parquet_read` via `monkeypatch.setattr(pd, 'read_parquet', parse)`.

**Complete source-ordered implementation**

```python
def parse(*args: object, **kwargs: object) -> pd.DataFrame:
        calls["parse"] += 1
        raise AssertionError("Parquet must not be parsed")
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_rehash_policy_table`

**Exact signature**

```python
def _rehash_policy_table(
    result: BessPlanningFeaturePolicyResult, table: pd.DataFrame
) -> BessPlanningFeaturePolicyResult:
```

**Purpose**

Private `test` helper for rehash policy table; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeaturePolicyResult`.
- Every observed return expression is reproduced without truncation:
```python
module._result_with_hashes(replace(result, policy_table=table))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `module._result_with_hashes`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::_canonical_empty_policy_result` via `_rehash_policy_table`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_accepts_one_exact_policy_row` via `_rehash_policy_table`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_validates_every_intrinsic_row_contract` via `_rehash_policy_table`.

**Complete source-ordered implementation**

```python
def _rehash_policy_table(
    result: BessPlanningFeaturePolicyResult, table: pd.DataFrame
) -> BessPlanningFeaturePolicyResult:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    return module._result_with_hashes(replace(result, policy_table=table))
```

**Business boundary**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_canonical_empty_policy_result`

**Exact signature**

```python
def _canonical_empty_policy_result(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
```

**Purpose**

Private `test` helper for canonical empty policy result; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeaturePolicyResult`.
- Every observed return expression is reproduced without truncation:
```python
_rehash_policy_table(result, table)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_rehash_policy_table`.
- Environment/process effects: none directly visible.
- In-memory mutation: `table.index`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `_canonical_empty_policy_result`.
- import/re-export: `tests/unit/test_apply_bess_planning_feature_policy.py::<module>` via `from test_bess_planning_feature_policy import (
    _canonical_empty_policy_result,
    _checked_in_policy_result,
    _compiled_fixture,
)`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_rejects_canonical_empty_policy_table` via `_canonical_empty_policy_result`.

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

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_envelope_rejects_canonical_empty_policy_table`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
_, _, _, result = _compiled_fixture()
empty = _canonical_empty_policy_result(result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeaturePolicyError, match="policy|table|empty|entry"
    ):
        module.validate_bess_planning_feature_policy_result_envelope(empty)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_policy_envelope_accepts_one_exact_policy_row`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
_, _, _, result = _compiled_fixture()
table = result.policy_table.iloc[[0]].copy(deep=True)
table.index = pd.Index([0], dtype="int64")
one_row = _rehash_policy_table(result, table)
module.validate_bess_planning_feature_policy_result_envelope(one_row)
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

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_policy_envelope_accepts_one_exact_policy_row() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    _, _, _, result = _compiled_fixture()
    table = result.policy_table.iloc[[0]].copy(deep=True)
    table.index = pd.Index([0], dtype="int64")
    one_row = _rehash_policy_table(result, table)
    module.validate_bess_planning_feature_policy_result_envelope(one_row)
```

### `test_policy_envelope_accepts_current_twelve_row_snapshot`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
result = _checked_in_policy_result()
module.validate_bess_planning_feature_policy_result_envelope(result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
assert len(result.policy_table) == 12
```

**Regression protected**

Pins the exact output, preservation, call-count, or lineage invariant expressed by the reproduced assertions; changing that invariant requires an intentional contract update.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_policy_envelope_accepts_current_twelve_row_snapshot() -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    result = _checked_in_policy_result()
    assert len(result.policy_table) == 12
    module.validate_bess_planning_feature_policy_result_envelope(result)
```

### `test_policy_envelope_requires_cnig_profile_schema_two`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `version`.

**Setup**

```python
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
_, _, _, result = _compiled_fixture()
changed = module._result_with_hashes(
        replace(result, cnig_profile_schema_version=version)
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="profile schema|schema"):
        module.validate_bess_planning_feature_policy_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_policy_envelope_requires_cnig_result_schema_five`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `version`.

**Setup**

```python
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
_, _, _, result = _compiled_fixture()
changed = module._result_with_hashes(
        replace(result, cnig_result_hash_schema_version=version)
    )
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="CNIG result|schema"):
        module.validate_bess_planning_feature_policy_result_envelope(changed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_policy_envelope_validates_every_intrinsic_row_contract`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `mutation`.

**Setup**

```python
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
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(
        BessPlanningFeaturePolicyError,
        match="policy|pair|order|code|status|confidence|priority|scope|flag|CNIG|null|schema",
    ):
        module.validate_bess_planning_feature_policy_result_envelope(changed)
```

**Regression protected**

Prevents coordinated metadata/content mutation from being accepted without agreement with the authoritative byte or result envelope.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: none.

**Setup**

```python
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
_, _, _, result = _compiled_fixture()
class DerivedPolicyResult(BessPlanningFeaturePolicyResult):
        pass
derived = DerivedPolicyResult(**result.__dict__)
module.validate_bess_planning_feature_policy_result_envelope(result)
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError, match="type|result"):
        module.validate_bess_planning_feature_policy_result_envelope(derived)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

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

### `test_policy_envelope_controls_malformed_result_type`

**Purpose**

Exercises the concrete setup, action, and assertions reproduced below; the protected regression is derived from those operations rather than the test name alone.

**Pytest argument classification**

- Fixture-injected arguments: none.
- `pytest.mark.parametrize` arguments: `malformed`.

**Setup**

```python
module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
```

**Action**

```python
# Action is embedded in the assertion/raises context below.
```

**Expected result**

```python
with pytest.raises(BessPlanningFeaturePolicyError):
        module.validate_bess_planning_feature_policy_result_envelope(malformed)
```

**Regression protected**

Prevents the malformed/adversarial setup reproduced below from reaching a success path; the public boundary must raise the asserted controlled error.

**Test boundary**

- In-memory/local unit boundary defined entirely by the reproduced setup.

**Complete test implementation**

```python
def test_policy_envelope_controls_malformed_result_type(malformed: object) -> None:
    module = importlib.import_module("landscout.stages.bess_planning_feature_policy")
    with pytest.raises(BessPlanningFeaturePolicyError):
        module.validate_bess_planning_feature_policy_result_envelope(malformed)
```


## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

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
