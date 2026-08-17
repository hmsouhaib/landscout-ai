# `tests/unit/test_bess_planning_feature_policy.py`

## File identity

- Repository path: `tests/unit/test_bess_planning_feature_policy.py`
- File type: Python test
- Primary responsibility: Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.
- Layer / domain: `unit/regression test` / `test`
- Public or internal role: Internal test support; not a production API.
- Source SHA256: `3f7bc1a603948f9de88b87aeac65b89eb5532cd30ef777780692b3ea6bffe981`

## 1. Purpose

Provides complete unit and regression coverage for the `bess_planning_feature_policy` contracts exercised in this file.

## 2. Position in LandScout architecture

This file is a `unit/regression test` artifact in the `test` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `from dataclasses import fields, replace` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from io import BytesIO` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.

### Third-party

- `import importlib` — required by the implementation paths and symbols documented below.
- `import tomllib` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import pytest` — required by the implementation paths and symbols documented below.
- `from pandas.testing import assert_frame_equal` — required by the implementation paths and symbols documented below.
- `from pydantic import ValidationError` — required by the implementation paths and symbols documented below.
- `from test_resolve_planning_feature_codes import _integration_inputs` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout import stages` — required by the implementation paths and symbols documented below.
- `from landscout.common.artifact_paths import validate_portable_parquet_filename` — required by the implementation paths and symbols documented below.
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature` — required by the implementation paths and symbols documented below.
- `from landscout.stages.bess_planning_feature_policy import ( BessPlanningFeaturePolicyConfig, BessPlanningFeaturePolicyError, BessPlanningFeaturePolicyResult, compile_bess_planning_feature_policy, load_bess_planning_feature_policy_config, validate_bess_planning_feature_policy_result, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.resolve_planning_feature_codes import ( load_cnig_feature_code_profile, resolve_planning_feature_codes, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `POLICY_PATH` | `Path("configs/planning/muret_bess_cnig_feature_policy.yaml")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_SCOPE` | `"OFFICIAL_CNIG_CODE_MEANING_ONLY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `STATUS_PRIORITIES` | `{ "LIKELY_MATERIAL_CONSTRAINT": 50, "UNKNOWN": 40, "MATERIAL_REVIEW_REQUIRED": 30, "DESIGN_REVIEW_REQUIRED": 20, "CONTEXT_REVIEW_REQUIRED": 10, }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXPECTED_MURET_DECISIONS` | `{ ("INFORMATION", "02", "00"): ("CONTEXT_REVIEW_REQUIRED", "HIGH"), ("INFORMATION", "14", "00"): ("CONTEXT_REVIEW_REQUIRED", "HIGH"), ("INFORMATION", "27", "00"): ("CONTEXT_REVIEW_REQUIRED", "HIGH"), ("INFORMATION", "99", "00"): ("UNKNOWN", "LOW"), ("PRESCRIPTION", "01", "00"): ("LIKELY_MATERIAL_CONSTRAINT", "HIGH"), ("PRESCRIPTION", "05", "00"): ("MATERIAL_REVIEW_REQUIRED", "HIGH"), ("PRESCRIPTION", "07", "00"): ("LIKELY_MATERIAL_CONSTRAINT", "MEDIUM"), ("PRESCRIPTION", "07", "04"): ("LIKELY_MATERIAL_CONSTRAINT", "HIGH"), ("PRESCRIPTION", "15", "00"): ("DESIGN_REVIEW_REQUIRED", "MEDIUM"), ("PRESCRIPTION", "15", "01"): ("DESIGN_REVIEW_REQUIRED", "HIGH"), ("PRESCRIPTION", "17", "00"): ("MATERIAL_REVIEW_REQUIRED", "MEDIUM"), ("PRESCRIPTION", "18", "00"): ("MATERIAL_REVIEW_REQUIRED", "HIGH"), }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXPECTED_POLICY_ENTRIES_SHA256` | `"1d3e63f1123000402065b74402cb1e2295db2ac5655209ce410aaf36bfc2be91"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXPECTED_POLICY_SHA256` | `"1cfca0eb3d777e9b6604748e8a81609abe7b728de8d0695711cd569180df6489"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXPECTED_POLICY_TABLE_SHA256` | `"225105fe488e21f8aa080751812dde1671340c26620cae1d8372c2e59488ed41"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXPECTED_COMPLETE_RESULT_SHA256` | `"84a59b418f5a53bc61df73296964b2847cc5d3529c10d0c6912c96222edba09c"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EXPECTED_SOURCE_LOCK` | `{ "document_id": "33edb4c9f6943c88d8d92518bff20bec", "archive_sha256": ( "9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93" ), "cnig_profile": "cnig_plu_2017_muret_observed_pairs_v2", "cnig_profile_schema_version": 2, "cnig_profile_sha256": ( "5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee" ), "cnig_result_hash_schema_version": 5, "cnig_complete_result_content_sha256": ( "b56b195b32914583e6599fe96b3d29977c52450c9755228d89ce7e192903ab3e" ), }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARTIFACT_KIND` | `"BESS_CNIG_FEATURE_POLICY_RESULT"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1.DerivedPolicyResult`

**Purpose:** Carries an immutable stage/result envelope whose fields and hashes are consumed by downstream validation.

**Inheritance:** `BessPlanningFeaturePolicyResult`.

**Model form and mutability:** class inheriting from `BessPlanningFeaturePolicyResult`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

## 6. Functions and methods

### `_canonical_sha256`

**Signature**

```python
def _canonical_sha256(value: object) -> str:
```

**Purpose**

Implements canonical sha256 according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `sha256(json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()`.

**Algorithm**

1. Returns `sha256(json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `json.dumps`, `json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode`, `sha256`, `sha256(json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest`.

**Known repository callers**

- `tests/unit/test_bess_planning_feature_policy.py` — `_policy_payload`
- `tests/unit/test_bess_planning_feature_policy.py` — `_validated_config`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_checked_in_policy_complete_snapshot_is_immutable`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_duplicate_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_invalid_confidence_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_invalid_or_legal_conclusion_status_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_noncanonical_whitespace_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_entries_require_deterministic_order`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_profile_v1_snapshot_detects_policy_text_drift`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_profile_v1_snapshot_detects_source_lock_drift`

**Tests**

- `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_policy_complete_snapshot_is_immutable`
- `tests/unit/test_bess_planning_feature_policy.py::test_duplicate_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_invalid_confidence_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_invalid_or_legal_conclusion_status_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_noncanonical_whitespace_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_entries_require_deterministic_order`
- `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_policy_text_drift`
- `tests/unit/test_bess_planning_feature_policy.py::test_profile_v1_snapshot_detects_source_lock_drift`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_policy_entry`

**Signature**

```python
def _policy_entry(row: object, position: int) -> dict[str, object]:
```

**Purpose**

Implements policy entry according to the exact implementation and guards in this file.

**Inputs**

- `row` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `position` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'feature_family': row.feature_family, 'type_code': row.type_code, 'subtype_code': row.subtype_code, 'expected_official_label': row.official_label, 'expected_legal_reference': None if pd.isna(legal_reference) else legal_reference, 'expected_regulation_reference': None if pd.isna(regulation_reference) else regulation_reference, 'precheck_status': status, 'confidence': ('HIGH', 'MEDIUM', 'LOW')[pos…`.

**Algorithm**

1. Computes `statuses` from `tuple(STATUS_PRIORITIES)`.
2. Computes `status` from `statuses[position % len(statuses)]`.
3. Computes `legal_reference` from `row.legal_reference`.
4. Computes `regulation_reference` from `row.regulation_or_annex_reference`.
5. Returns `{'feature_family': row.feature_family, 'type_code': row.type_code, 'subtype_code': row.subtype_code, 'expected_official_label': row.official_label, 'expected_legal_reference': None if pd.isna(legal_reference) else legal_reference, 'expected_regulation_reference': None if pd.isna(regulation_reference) else regulation_reference, 'precheck_status': status, 'co…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `len`, `pd.isna`, `tuple`.

**Known repository callers**

- `tests/unit/test_bess_planning_feature_policy.py` — `_policy_payload`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_compiled_fixture`

**Signature**

```python
def _compiled_fixture() -> tuple[
    tuple[object, ...],
    object,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
]:
```

**Purpose**

Implements compiled fixture according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `tuple[tuple[object, ...], object, BessPlanningFeaturePolicyConfig, BessPlanningFeaturePolicyResult]`. Observed return expression(s): `(inputs, coded, config, result)`.

**Algorithm**

1. Computes `inputs` from `_integration_inputs()`.
2. Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
3. Computes `config` from `BessPlanningFeaturePolicyConfig.model_validate(_policy_payload(inputs, coded))`.
4. Computes `result` from `compile_bess_planning_feature_policy(*inputs, coded, config)`.
5. Returns `(inputs, coded, config, result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_integration_inputs`, `_policy_payload`, `compile_bess_planning_feature_policy`, `resolve_planning_feature_codes`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `_application_fixture`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_and_public_validator_heavy_validation_counts`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_feature_and_relation_inputs_are_preserved_and_not_mutated`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_artifact_loader_parses_the_exact_verified_parquet_bytes`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_artifact_loader_rejects_duplicate_json_key`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_artifact_loader_rejects_manifest_mismatch`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_artifact_loader_rejects_parquet_replacement`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_artifact_manifest_model_is_strict_and_frozen`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_compiler_wrong_source_lock_fast_fails_before_source_validation`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_coordinated_policy_table_and_hash_mutation_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_forged_matching_lock_still_runs_source_complete_validation`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_in_memory_config_is_revalidated_before_compilation`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_information_9900_official_references_remain_missing`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_locally_invalid_result_fast_fails_before_source_validation`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_null_reference_literal_is_rejected_by_local_envelope`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_persisted_parquet_and_json_readback_is_source_complete`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_artifact_loader_rejects_source_schema_before_parquet_read`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_envelope_accepts_one_exact_policy_row`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_envelope_rejects_canonical_empty_policy_table`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_envelope_requires_cnig_profile_schema_two`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_envelope_requires_cnig_result_schema_five`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_envelope_validates_every_intrinsic_row_contract`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_manifest_rejects_nonportable_parquet_filename`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_manifest_rejects_unsupported_cnig_source_schema`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_table_is_sorted_and_preserves_leading_zero_codes`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_table_mutation_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_source_lock_mismatch_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_and_relation_inputs_are_preserved_and_not_mutated`
- `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_parses_the_exact_verified_parquet_bytes`
- `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_duplicate_json_key`
- `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_manifest_mismatch`
- `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_parquet_replacement`
- `tests/unit/test_bess_planning_feature_policy.py::test_artifact_manifest_model_is_strict_and_frozen`
- `tests/unit/test_bess_planning_feature_policy.py::test_compiler_wrong_source_lock_fast_fails_before_source_validation`
- `tests/unit/test_bess_planning_feature_policy.py::test_coordinated_policy_table_and_hash_mutation_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_forged_matching_lock_still_runs_source_complete_validation`
- `tests/unit/test_bess_planning_feature_policy.py::test_in_memory_config_is_revalidated_before_compilation`
- `tests/unit/test_bess_planning_feature_policy.py::test_information_9900_official_references_remain_missing`
- `tests/unit/test_bess_planning_feature_policy.py::test_locally_invalid_result_fast_fails_before_source_validation`
- `tests/unit/test_bess_planning_feature_policy.py::test_null_reference_literal_is_rejected_by_local_envelope`
- `tests/unit/test_bess_planning_feature_policy.py::test_persisted_parquet_and_json_readback_is_source_complete`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_artifact_loader_rejects_source_schema_before_parquet_read`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_accepts_one_exact_policy_row`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_rejects_canonical_empty_policy_table`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_requires_cnig_profile_schema_two`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_requires_cnig_result_schema_five`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_validates_every_intrinsic_row_contract`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_manifest_rejects_nonportable_parquet_filename`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_manifest_rejects_unsupported_cnig_source_schema`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_table_is_sorted_and_preserves_leading_zero_codes`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_table_mutation_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_source_lock_mismatch_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator`
- `tests/unit/test_bess_planning_feature_policy.py::test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_policy_payload`

**Signature**

```python
def _policy_payload(inputs: tuple[object, ...], coded: object) -> dict[str, object]:
```

**Purpose**

Implements policy payload according to the exact implementation and guards in this file.

**Inputs**

- `inputs` (`tuple[object, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded` (`object`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'schema_version': 1, 'profile': 'synthetic_bess_cnig_feature_policy_v1', 'policy_scope': POLICY_SCOPE, 'local_feature_text_interpreted': False, 'local_regulation_content_interpreted': False, 'legal_conclusion_produced': False, 'source_lock': {'document_id': coded.source_document_id, 'archive_sha256': coded.source_archive_sha256, 'cnig_profile': coded.profile, 'cnig_profile_schema_version': coded…`.

**Algorithm**

1. Computes `entries` from `[_policy_entry(row, position) for position, row in enumerate(coded.code_dictionary.itertuples(index=False))]`.
2. Returns `{'schema_version': 1, 'profile': 'synthetic_bess_cnig_feature_policy_v1', 'policy_scope': POLICY_SCOPE, 'local_feature_text_interpreted': False, 'local_regulation_content_interpreted': False, 'legal_conclusion_produced': False, 'source_lock': {'document_id': coded.source_document_id, 'archive_sha256': coded.source_archive_sha256, 'cnig_profile': coded.profi…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `_policy_entry`, `coded.code_dictionary.itertuples`, `dict`, `enumerate`.

**Known repository callers**

- `tests/unit/test_bess_planning_feature_policy.py` — `_compiled_fixture`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_compiler_and_public_validator_invoke_source_complete_coding_validation`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_duplicate_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_extra_policy_pair_is_rejected_without_type_fallback`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_invalid_confidence_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_invalid_or_legal_conclusion_status_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_malformed_sha256_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_missing_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_noncanonical_whitespace_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_official_meaning_mismatch_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_entries_require_deterministic_order`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_prescription_information_code_spaces_remain_separate`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_status_priority_contract_is_strict`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_unknown_yaml_field_is_rejected`

**Tests**

- `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation`
- `tests/unit/test_bess_planning_feature_policy.py::test_duplicate_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_extra_policy_pair_is_rejected_without_type_fallback`
- `tests/unit/test_bess_planning_feature_policy.py::test_invalid_confidence_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_invalid_or_legal_conclusion_status_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_malformed_sha256_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_missing_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_noncanonical_whitespace_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_official_meaning_mismatch_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_entries_require_deterministic_order`
- `tests/unit/test_bess_planning_feature_policy.py::test_prescription_information_code_spaces_remain_separate`
- `tests/unit/test_bess_planning_feature_policy.py::test_status_priority_contract_is_strict`
- `tests/unit/test_bess_planning_feature_policy.py::test_unknown_yaml_field_is_rejected`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_validated_config`

**Signature**

```python
def _validated_config(payload: dict[str, object]) -> BessPlanningFeaturePolicyConfig:
```

**Purpose**

Validates and returns canonical config according to the exact implementation and guards in this file.

**Inputs**

- `payload` (`dict[str, object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeaturePolicyConfig`. Observed return expression(s): `BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Algorithm**

1. Computes `entries` from `payload['entries']`.
2. Asserts `isinstance(entries, list)`.
3. Computes `payload['canonical_policy_entries_sha256']` from `_canonical_sha256(entries)`.
4. Returns `BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `isinstance`.

**Known repository callers**

- `tests/unit/test_bess_planning_feature_policy.py` — `test_extra_policy_pair_is_rejected_without_type_fallback`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_missing_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_official_meaning_mismatch_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_prescription_information_code_spaces_remain_separate`

**Tests**

- `tests/unit/test_bess_planning_feature_policy.py::test_extra_policy_pair_is_rejected_without_type_fallback`
- `tests/unit/test_bess_planning_feature_policy.py::test_missing_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_official_meaning_mismatch_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_prescription_information_code_spaces_remain_separate`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_artifact_manifest`

**Signature**

```python
def _artifact_manifest(
    result: BessPlanningFeaturePolicyResult,
    parquet: Path,
) -> dict[str, object]:
```

**Purpose**

Implements artifact manifest according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeaturePolicyResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parquet` (`Path`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'schema_version': 2, 'artifact_kind': ARTIFACT_KIND, **{name: getattr(result, name) for name in scalar_names}, 'parquet_filename': parquet.name, 'parquet_row_count': len(result.policy_table), 'parquet_size_bytes': parquet.stat().st_size, 'parquet_sha256': sha256(parquet.read_bytes()).hexdigest(), 'policy_table_schema_signature': deterministic_frame_schema_signature(result.policy_table)}`.

**Algorithm**

1. Computes `scalar_names` from `tuple((field.name for field in fields(BessPlanningFeaturePolicyResult) if field.name != 'policy_table'))`.
2. Returns `{'schema_version': 2, 'artifact_kind': ARTIFACT_KIND, **{name: getattr(result, name) for name in scalar_names}, 'parquet_filename': parquet.name, 'parquet_row_count': len(result.policy_table), 'parquet_size_bytes': parquet.stat().st_size, 'parquet_sha256': sha256(parquet.read_bytes()).hexdigest(), 'policy_table_schema_signature': deterministic_frame_schema_…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `parquet.read_bytes`, `sha256(parquet.read_bytes()).hexdigest`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `deterministic_frame_schema_signature`, `fields`, `getattr`, `len`, `parquet.read_bytes`, `parquet.stat`, `sha256`, `sha256(parquet.read_bytes()).hexdigest`, `tuple`.

**Known repository callers**

- `tests/unit/test_bess_planning_feature_policy.py` — `_write_artifacts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_write_artifacts`

**Signature**

```python
def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeaturePolicyResult,
) -> tuple[Path, Path, dict[str, object]]:
```

**Purpose**

Writes artifacts according to the exact implementation and guards in this file.

**Inputs**

- `tmp_path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`BessPlanningFeaturePolicyResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[Path, Path, dict[str, object]]`. Observed return expression(s): `(parquet, manifest_path, manifest)`.

**Algorithm**

1. Computes `parquet` from `tmp_path / 'policy.parquet'`.
2. Computes `manifest_path` from `tmp_path / 'policy.json'`.
3. Calls `result.policy_table.to_parquet(parquet, index=True)` for its validation or side effect.
4. Computes `manifest` from `_artifact_manifest(result, parquet)`.
5. Calls `manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + '\n', encoding='utf-8')` for its validation or side effect.
6. Returns `(parquet, manifest_path, manifest)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `manifest_path.write_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_artifact_manifest`, `json.dumps`, `manifest_path.write_text`, `result.policy_table.to_parquet`.

**Known repository callers**

- `tests/unit/test_bess_planning_feature_policy.py` — `test_artifact_loader_parses_the_exact_verified_parquet_bytes`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_artifact_loader_rejects_duplicate_json_key`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_artifact_loader_rejects_manifest_mismatch`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_artifact_loader_rejects_parquet_replacement`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_artifact_manifest_model_is_strict_and_frozen`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_persisted_parquet_and_json_readback_is_source_complete`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_artifact_loader_rejects_source_schema_before_parquet_read`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_manifest_rejects_nonportable_parquet_filename`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_manifest_rejects_unsupported_cnig_source_schema`

**Tests**

- `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_parses_the_exact_verified_parquet_bytes`
- `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_duplicate_json_key`
- `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_manifest_mismatch`
- `tests/unit/test_bess_planning_feature_policy.py::test_artifact_loader_rejects_parquet_replacement`
- `tests/unit/test_bess_planning_feature_policy.py::test_artifact_manifest_model_is_strict_and_frozen`
- `tests/unit/test_bess_planning_feature_policy.py::test_persisted_parquet_and_json_readback_is_source_complete`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_artifact_loader_rejects_source_schema_before_parquet_read`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_manifest_rejects_nonportable_parquet_filename`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_manifest_rejects_unsupported_cnig_source_schema`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_checked_in_policy_result`

**Signature**

```python
def _checked_in_policy_result() -> BessPlanningFeaturePolicyResult:
```

**Purpose**

Implements checked in policy result according to the exact implementation and guards in this file.

**Inputs**

- No parameters.

**Returns**

- Declared return type: `BessPlanningFeaturePolicyResult`. Observed return expression(s): `policy_module._build_result(config, locked_coded)`.

**Algorithm**

1. Computes `inputs` from `_integration_inputs()`.
2. Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
3. Computes `config` from `load_bess_planning_feature_policy_config(POLICY_PATH)`.
4. Computes `cnig_profile` from `load_cnig_feature_code_profile(Path('configs/planning/cnig_plu_2017_feature_codes.yaml'))`.
5. Computes `cnig_module` from `importlib.import_module('landscout.stages.resolve_planning_feature_codes')`.
6. Computes `policy_module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
7. Computes `locked_coded` from `replace(coded, profile=config.source_lock.cnig_profile, profile_schema_version=config.source_lock.cnig_profile_schema_version, profile_sha256=config.source_lock.cnig_profile_sha256, source_document_id=config.source_lock.document_id, source_archive_sha256=config.source_lock.archive_sha256, result_hash_schema_version=co…`.
8. Returns `policy_module._build_result(config, locked_coded)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_bess_planning_feature_policy_config`, `load_cnig_feature_code_profile`, `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `Path`, `_integration_inputs`, `cnig_module._dictionary`, `importlib.import_module`, `load_bess_planning_feature_policy_config`, `load_cnig_feature_code_profile`, `policy_module._build_result`, `replace`, `resolve_planning_feature_codes`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_inconsistent_official_status_and_policy_match_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_unknown_pair_remains_present_with_true_null_decision_fields`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_checked_in_compiled_policy_result_hashes_are_pinned`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_envelope_accepts_current_twelve_row_snapshot`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_inconsistent_official_status_and_policy_match_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_pair_remains_present_with_true_null_decision_fields`
- `tests/unit/test_bess_planning_feature_policy.py::test_checked_in_compiled_policy_result_hashes_are_pinned`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_accepts_current_twelve_row_snapshot`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_parses_the_exact_verified_parquet_bytes.replace_after_byte_read`

**Signature**

```python
def replace_after_byte_read(path: Path) -> bytes:
```

**Purpose**

Implements replace after byte read according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. Observed return expression(s): `payload`.

**Algorithm**

1. Executes `nonlocal replacement_performed`.
2. Computes `payload` from `original_read_bytes(path)`.
3. Checks `path == parquet and (not replacement_performed)`. When true: Calls `path.write_bytes(replacement_bytes)` for its validation or side effect. Computes `replacement_performed` from `True`.
4. Returns `payload`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_read_bytes`, `path.write_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `original_read_bytes`, `path.write_bytes`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_parses_the_exact_verified_parquet_bytes.old_hash_then_replace`

**Signature**

```python
def old_hash_then_replace(path: Path) -> str:
```

**Purpose**

Implements old hash then replace according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `sha256(payload).hexdigest()`.

**Algorithm**

1. Executes `nonlocal replacement_performed`.
2. Computes `payload` from `original_read_bytes(path)`.
3. Checks `path == parquet and (not replacement_performed)`. When true: Calls `path.write_bytes(replacement_bytes)` for its validation or side effect. Computes `replacement_performed` from `True`.
4. Returns `sha256(payload).hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_read_bytes`, `path.write_bytes`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `original_read_bytes`, `path.write_bytes`, `sha256`, `sha256(payload).hexdigest`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_parses_the_exact_verified_parquet_bytes.observed_read_parquet`

**Signature**

```python
def observed_read_parquet(
        source: object, *args: object, **kwargs: object
    ) -> object:
```

**Purpose**

Implements observed read parquet according to the exact implementation and guards in this file.

**Inputs**

- `source` (`object`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `original_read_parquet(source, *args, **kwargs)`.

**Algorithm**

1. Checks `isinstance(source, BytesIO)`. When true: Calls `parsed_payloads.append(('buffer', source.getvalue()))` for its validation or side effect. Otherwise: Computes `path` from `Path(source)`. Calls `parsed_payloads.append(('path', original_read_bytes(path)))` for its validation or side effect.
2. Returns `original_read_parquet(source, *args, **kwargs)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `original_read_bytes`, `original_read_parquet`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `Path`, `isinstance`, `original_read_bytes`, `original_read_parquet`, `parsed_payloads.append`, `source.getvalue`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_locally_invalid_result_fast_fails_before_source_validation.counted`

**Signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_compiler_wrong_source_lock_fast_fails_before_source_validation.counted`

**Signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_forged_matching_lock_still_runs_source_complete_validation.counted`

**Signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.
3. Calls `actual(*args, **kwargs)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `actual`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_compiler_and_public_validator_invoke_source_complete_coding_validation.counted`

**Signature**

```python
def counted(*args: object, **kwargs: object) -> None:
```

**Purpose**

Implements counted according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Executes `nonlocal calls`.
2. Updates `calls` using `` and `1`.
3. Calls `actual(*args, **kwargs)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `actual`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_artifact_loader_rejects_source_schema_before_parquet_read.byte_read`

**Signature**

```python
def byte_read(*args: object, **kwargs: object) -> bytes:
```

**Purpose**

Implements byte read according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bytes`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['bytes']` using `` and `1`.
2. Raises `AssertionError('Parquet bytes must not be read')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_artifact_loader_rejects_source_schema_before_parquet_read.parse`

**Signature**

```python
def parse(*args: object, **kwargs: object) -> pd.DataFrame:
```

**Purpose**

Parses parse according to the exact implementation and guards in this file.

**Inputs**

- `*args` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `**kwargs` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Updates `calls['parse']` using `` and `1`.
2. Raises `AssertionError('Parquet must not be parsed')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `AssertionError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `AssertionError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_rehash_policy_table`

**Signature**

```python
def _rehash_policy_table(
    result: BessPlanningFeaturePolicyResult, table: pd.DataFrame
) -> BessPlanningFeaturePolicyResult:
```

**Purpose**

Implements rehash policy table according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeaturePolicyResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `table` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeaturePolicyResult`. Observed return expression(s): `module._result_with_hashes(replace(result, policy_table=table))`.

**Algorithm**

1. Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
2. Returns `module._result_with_hashes(replace(result, policy_table=table))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `importlib.import_module`, `module._result_with_hashes`, `replace`.

**Known repository callers**

- `tests/unit/test_bess_planning_feature_policy.py` — `_canonical_empty_policy_result`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_envelope_accepts_one_exact_policy_row`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_envelope_validates_every_intrinsic_row_contract`

**Tests**

- `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_accepts_one_exact_policy_row`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_validates_every_intrinsic_row_contract`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `_canonical_empty_policy_result`

**Signature**

```python
def _canonical_empty_policy_result(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
```

**Purpose**

Implements canonical empty policy result according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeaturePolicyResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeaturePolicyResult`. Observed return expression(s): `_rehash_policy_table(result, table)`.

**Algorithm**

1. Computes `table` from `result.policy_table.iloc[0:0].copy(deep=True)`.
2. Computes `table.index` from `pd.Index([], dtype='int64')`.
3. Returns `_rehash_policy_table(result, table)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `result.policy_table.iloc[0:0].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_rehash_policy_table`, `pd.Index`, `result.policy_table.iloc[0:0].copy`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_envelope_rejects_canonical_empty_policy_table`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_envelope_rejects_canonical_empty_policy_table`

**Business interpretation**

This symbol contributes to the `test` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status`

**Signature**

```python
def test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status() -> (
    None
):
```

**Purpose**

Protects the `valid exact policy compiles without applying feature or parcel status` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `(inputs, coded, config, result)` from `_compiled_fixture()`.

**Action**

- Calls `_compiled_fixture`, `any`, `result.policy_table['legal_conclusion_produced'].eq`, `result.policy_table['legal_conclusion_produced'].eq(False).all`, `result.policy_table['local_feature_text_interpreted'].eq`, `result.policy_table['local_feature_text_interpreted'].eq(False).all`, `result.policy_table['local_regulation_content_interpreted'].eq`, `result.policy_table['local_regulation_content_interpreted'].eq(False).all`, `validate_bess_planning_feature_policy_result`.

**Expected result**

- Direct assertions: `assert result.policy_schema_version == 1`; `assert result.result_hash_schema_version == 1`; `assert result.policy_scope == POLICY_SCOPE`; `assert len(result.policy_table) == len(coded.code_dictionary)`; `assert not any((column in result.policy_table.columns for column in ('parcel_id', 'planning_feature_id', 'relation_type')))`; `assert result.policy_table['local_feature_text_interpreted'].eq(False).all()`; `assert result.policy_table['local_regulation_content_interpreted'].eq(False).all()`; `assert result.policy_table['legal_conclusion_produced'].eq(False).all()`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `valid exact policy compiles without applying feature or parcel status` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `any`, `len`, `result.policy_table['legal_conclusion_produced'].eq`, `result.policy_table['legal_conclusion_produced'].eq(False).all`, `result.policy_table['local_feature_text_interpreted'].eq`, `result.policy_table['local_feature_text_interpreted'].eq(False).all`, `result.policy_table['local_regulation_content_interpreted'].eq`, `result.policy_table['local_regulation_content_interpreted'].eq(False).all`, `validate_bess_planning_feature_policy_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_checked_in_policy_pins_all_twelve_exact_muret_decisions`

**Signature**

```python
def test_checked_in_policy_pins_all_twelve_exact_muret_decisions() -> None:
```

**Purpose**

Protects the `checked in policy pins all twelve exact muret decisions` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `config` from `load_bess_planning_feature_policy_config(POLICY_PATH)`.
- Computes `actual` from `{(entry.feature_family, entry.type_code, entry.subtype_code): (entry.precheck_status, entry.confidence) for entry in config.entries}`.

**Action**

- Calls `all`, `load_bess_planning_feature_policy_config`.

**Expected result**

- Direct assertions: `assert actual == EXPECTED_MURET_DECISIONS`; `assert config.status_priority == STATUS_PRIORITIES`; `assert config.policy_scope == POLICY_SCOPE`; `assert config.local_feature_text_interpreted is False`; `assert config.local_regulation_content_interpreted is False`; `assert config.legal_conclusion_produced is False`; `assert len(config.entries) == 12`; `assert ('PRESCRIPTION', '15', '00') in actual`; `assert ('PRESCRIPTION', '15', '01') in actual`; `assert all((len(key[1]) == len(key[2]) == 2 for key in actual))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `checked in policy pins all twelve exact muret decisions` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `all`, `len`, `load_bess_planning_feature_policy_config`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_checked_in_policy_complete_snapshot_is_immutable`

**Signature**

```python
def test_checked_in_policy_complete_snapshot_is_immutable() -> None:
```

**Purpose**

Protects the `checked in policy complete snapshot is immutable` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `config` from `load_bess_planning_feature_policy_config(POLICY_PATH)`.

**Action**

- Calls `_canonical_sha256`, `config.model_dump`, `config.source_lock.model_dump`, `entry.model_dump`, `load_bess_planning_feature_policy_config`.

**Expected result**

- Direct assertions: `assert config.schema_version == 1`; `assert config.profile == 'muret_bess_cnig_feature_policy_v1'`; `assert config.policy_scope == POLICY_SCOPE`; `assert config.local_feature_text_interpreted is False`; `assert config.local_regulation_content_interpreted is False`; `assert config.legal_conclusion_produced is False`; `assert config.source_lock.model_dump(mode='json') == EXPECTED_SOURCE_LOCK`; `assert config.status_priority == STATUS_PRIORITIES`; `assert config.canonical_policy_entries_sha256 == EXPECTED_POLICY_ENTRIES_SHA256`; `assert _canonical_sha256([entry.model_dump(mode='json') for entry in config.entries]) == EXPECTED_POLICY_ENTRIES_SHA256`; `assert _canonical_sha256(config.model_dump(mode='json')) == EXPECTED_POLICY_SHA256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `checked in policy complete snapshot is immutable` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_canonical_sha256`, `config.model_dump`, `config.source_lock.model_dump`, `entry.model_dump`, `load_bess_planning_feature_policy_config`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_checked_in_compiled_policy_result_hashes_are_pinned`

**Signature**

```python
def test_checked_in_compiled_policy_result_hashes_are_pinned() -> None:
```

**Purpose**

Protects the `checked in compiled policy result hashes are pinned` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `result` from `_checked_in_policy_result()`.

**Action**

- Calls `_checked_in_policy_result`.

**Expected result**

- Direct assertions: `assert result.policy_table_content_sha256 == EXPECTED_POLICY_TABLE_SHA256`; `assert result.complete_result_content_sha256 == EXPECTED_COMPLETE_RESULT_SHA256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `checked in compiled policy result hashes are pinned` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_checked_in_policy_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_v1_snapshot_detects_policy_text_drift`

**Signature**

```python
def test_profile_v1_snapshot_detects_policy_text_drift(field: str) -> None:
```

**Purpose**

Protects the `profile v1 snapshot detects policy text drift` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`.
- Contains 6 explicit setup/context statement(s).
- Computes `config` from `load_bess_planning_feature_policy_config(POLICY_PATH)`.
- Computes `payload` from `config.model_dump(mode='json')`.
- Computes `entries` from `payload['entries']`.
- Computes `entries[0][field]` from `f'{entries[0][field]} Changed.'`.
- Computes `payload['canonical_policy_entries_sha256']` from `_canonical_sha256(entries)`.
- Computes `changed` from `BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Action**

- Calls `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `changed.model_dump`, `config.model_dump`, `isinstance`, `load_bess_planning_feature_policy_config`.

**Expected result**

- Direct assertions: `assert isinstance(entries, list)`; `assert changed.profile == 'muret_bess_cnig_feature_policy_v1'`; `assert _canonical_sha256(changed.model_dump(mode='json')) != EXPECTED_POLICY_SHA256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `profile v1 snapshot detects policy text drift` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `changed.model_dump`, `config.model_dump`, `isinstance`, `load_bess_planning_feature_policy_config`, `pytest.mark.parametrize`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_profile_v1_snapshot_detects_source_lock_drift`

**Signature**

```python
def test_profile_v1_snapshot_detects_source_lock_drift() -> None:
```

**Purpose**

Protects the `profile v1 snapshot detects source lock drift` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `config` from `load_bess_planning_feature_policy_config(POLICY_PATH)`.
- Computes `payload` from `config.model_dump(mode='json')`.
- Computes `source_lock` from `payload['source_lock']`.
- Computes `source_lock['document_id']` from `'another-document'`.
- Computes `changed` from `BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Action**

- Calls `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `changed.model_dump`, `config.model_dump`, `isinstance`, `load_bess_planning_feature_policy_config`.

**Expected result**

- Direct assertions: `assert isinstance(source_lock, dict)`; `assert changed.profile == 'muret_bess_cnig_feature_policy_v1'`; `assert _canonical_sha256(changed.model_dump(mode='json')) != EXPECTED_POLICY_SHA256`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `profile v1 snapshot detects source lock drift` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `changed.model_dump`, `config.model_dump`, `isinstance`, `load_bess_planning_feature_policy_config`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_pandas_is_a_direct_bounded_runtime_dependency`

**Signature**

```python
def test_pandas_is_a_direct_bounded_runtime_dependency() -> None:
```

**Purpose**

Protects the `pandas is a direct bounded runtime dependency` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 1 explicit setup/context statement(s).
- Computes `project` from `tomllib.loads(Path('pyproject.toml').read_text(encoding='utf-8'))['project']`.

**Action**

- Calls `Path`, `Path('pyproject.toml').read_text`, `tomllib.loads`.

**Expected result**

- Direct assertions: `assert 'pandas>=3.0,<4' in project['dependencies']`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `pandas is a direct bounded runtime dependency` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `Path('pyproject.toml').read_text`, `tomllib.loads`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_information_9900_official_references_remain_missing`

**Signature**

```python
def test_information_9900_official_references_remain_missing() -> None:
```

**Purpose**

Protects the `information 9900 official references remain missing` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `row` from `result.policy_table.loc[(result.policy_table['feature_family'] == 'INFORMATION') & (result.policy_table['type_code'] == '99') & (result.policy_table['subtype_code'] == '00')].iloc[0]`.

**Action**

- Calls `_compiled_fixture`, `pd.isna`.

**Expected result**

- Direct assertions: `assert pd.isna(row['official_legal_reference'])`; `assert pd.isna(row['official_regulation_reference'])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `information 9900 official references remain missing` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `pd.isna`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_null_reference_literal_is_rejected_by_local_envelope`

**Signature**

```python
def test_null_reference_literal_is_rejected_by_local_envelope(
    column: str,
    literal: str,
) -> None:
```

**Purpose**

Protects the `null reference literal is rejected by local envelope` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `column`, `literal`.
- Contains 7 explicit setup/context statement(s).
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `table` from `result.policy_table.copy(deep=True)`.
- Computes `row` from `table.index[(table['feature_family'] == 'INFORMATION') & (table['type_code'] == '99') & (table['subtype_code'] == '00')][0]`.
- Computes `table.loc[row, column]` from `literal`.
- Computes `coordinated` from `module._result_with_hashes(replace(result, policy_table=table))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='reference|null|missing')` and executes: Calls `module._validate_result_envelope(coordinated)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `replace`, `result.policy_table.copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='reference|null|missing'): module._validate_result_envelope(coordinated)`.

**Regression protected**

- Protects the exact `null reference literal is rejected by local envelope` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module._validate_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`, `result.policy_table.copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_source_lock_mismatch_is_rejected`

**Signature**

```python
def test_source_lock_mismatch_is_rejected(field: str, value: object) -> None:
```

**Purpose**

Protects the `source lock mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`.
- Contains 4 explicit setup/context statement(s).
- Computes `(inputs, coded, config, _)` from `_compiled_fixture()`.
- Computes `changed_lock` from `config.source_lock.model_copy(update={field: value})`.
- Computes `changed` from `config.model_copy(update={'source_lock': changed_lock})`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='lock|source|CNIG')` and executes: Calls `compile_bess_planning_feature_policy(*inputs, coded, changed)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `compile_bess_planning_feature_policy`, `config.model_copy`, `config.source_lock.model_copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='lock|source|CNIG'): compile_bess_planning_feature_policy(*inputs, coded, changed)`.

**Regression protected**

- Protects the exact `source lock mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `compile_bess_planning_feature_policy`, `config.model_copy`, `config.source_lock.model_copy`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_missing_policy_pair_is_rejected`

**Signature**

```python
def test_missing_policy_pair_is_rejected() -> None:
```

**Purpose**

Protects the `missing policy pair is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `payload` from `_policy_payload(inputs, coded)`.
- Computes `entries` from `payload['entries']`.
- Computes `config` from `_validated_config(payload)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='missing|pair')` and executes: Calls `compile_bess_planning_feature_policy(*inputs, coded, config)` for its validation or side effect.

**Action**

- Calls `_integration_inputs`, `_policy_payload`, `_validated_config`, `compile_bess_planning_feature_policy`, `entries.pop`, `isinstance`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert isinstance(entries, list)`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='missing|pair'): compile_bess_planning_feature_policy(*inputs, coded, config)`.

**Regression protected**

- Protects the exact `missing policy pair is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_policy_payload`, `_validated_config`, `compile_bess_planning_feature_policy`, `entries.pop`, `isinstance`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_extra_policy_pair_is_rejected_without_type_fallback`

**Signature**

```python
def test_extra_policy_pair_is_rejected_without_type_fallback() -> None:
```

**Purpose**

Protects the `extra policy pair is rejected without type fallback` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `payload` from `_policy_payload(inputs, coded)`.
- Computes `entries` from `payload['entries']`.
- Computes `extra` from `dict(entries[-1])`.
- Computes `config` from `_validated_config(payload)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='extra|pair')` and executes: Calls `compile_bess_planning_feature_policy(*inputs, coded, config)` for its validation or side effect.

**Action**

- Calls `_integration_inputs`, `_policy_payload`, `_validated_config`, `compile_bess_planning_feature_policy`, `entries.append`, `entries.sort`, `extra.update`, `isinstance`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert isinstance(entries, list)`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='extra|pair'): compile_bess_planning_feature_policy(*inputs, coded, config)`.

**Regression protected**

- Protects the exact `extra policy pair is rejected without type fallback` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_policy_payload`, `_validated_config`, `compile_bess_planning_feature_policy`, `dict`, `entries.append`, `entries.sort`, `extra.update`, `isinstance`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_policy_pair_is_rejected`

**Signature**

```python
def test_duplicate_policy_pair_is_rejected() -> None:
```

**Purpose**

Protects the `duplicate policy pair is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `payload` from `_policy_payload(inputs, coded)`.
- Computes `entries` from `payload['entries']`.
- Computes `payload['canonical_policy_entries_sha256']` from `_canonical_sha256(entries)`.
- Enters managed context(s) `pytest.raises(ValidationError, match='duplicate|pair')` and executes: Calls `BessPlanningFeaturePolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `_integration_inputs`, `_policy_payload`, `entries.append`, `isinstance`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert isinstance(entries, list)`.
- Expected exception contexts: `with pytest.raises(ValidationError, match='duplicate|pair'): BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `duplicate policy pair is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `_integration_inputs`, `_policy_payload`, `dict`, `entries.append`, `isinstance`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_prescription_information_code_spaces_remain_separate`

**Signature**

```python
def test_prescription_information_code_spaces_remain_separate() -> None:
```

**Purpose**

Protects the `prescription information code spaces remain separate` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `payload` from `_policy_payload(inputs, coded)`.
- Computes `entries` from `payload['entries']`.
- Computes `entries[0]['feature_family']` from `'PRESCRIPTION'`.
- Computes `config` from `_validated_config(payload)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='missing|extra|pair')` and executes: Calls `compile_bess_planning_feature_policy(*inputs, coded, config)` for its validation or side effect.

**Action**

- Calls `_integration_inputs`, `_policy_payload`, `_validated_config`, `compile_bess_planning_feature_policy`, `entries.sort`, `isinstance`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert isinstance(entries, list)`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='missing|extra|pair'): compile_bess_planning_feature_policy(*inputs, coded, config)`.

**Regression protected**

- Protects the exact `prescription information code spaces remain separate` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_policy_payload`, `_validated_config`, `compile_bess_planning_feature_policy`, `entries.sort`, `isinstance`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_official_meaning_mismatch_is_rejected`

**Signature**

```python
def test_official_meaning_mismatch_is_rejected(
    field: str,
    value: object,
    message: str,
) -> None:
```

**Purpose**

Protects the `official meaning mismatch is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `field`, `value`, `message`.
- Contains 7 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `payload` from `_policy_payload(inputs, coded)`.
- Computes `entries` from `payload['entries']`.
- Computes `entries[0][field]` from `value`.
- Computes `config` from `_validated_config(payload)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match=message)` and executes: Calls `compile_bess_planning_feature_policy(*inputs, coded, config)` for its validation or side effect.

**Action**

- Calls `_integration_inputs`, `_policy_payload`, `_validated_config`, `compile_bess_planning_feature_policy`, `isinstance`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert isinstance(entries, list)`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match=message): compile_bess_planning_feature_policy(*inputs, coded, config)`.

**Regression protected**

- Protects the exact `official meaning mismatch is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_integration_inputs`, `_policy_payload`, `_validated_config`, `compile_bess_planning_feature_policy`, `isinstance`, `pytest.mark.parametrize`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_or_legal_conclusion_status_is_rejected`

**Signature**

```python
def test_invalid_or_legal_conclusion_status_is_rejected(status: str) -> None:
```

**Purpose**

Protects the `invalid or legal conclusion status is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `status`.
- Contains 7 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `payload` from `_policy_payload(inputs, coded)`.
- Computes `entries` from `payload['entries']`.
- Computes `entries[0]['precheck_status']` from `status`.
- Computes `payload['canonical_policy_entries_sha256']` from `_canonical_sha256(entries)`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `BessPlanningFeaturePolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `_integration_inputs`, `_policy_payload`, `isinstance`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert isinstance(entries, list)`.
- Expected exception contexts: `with pytest.raises(ValidationError): BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `invalid or legal conclusion status is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `_integration_inputs`, `_policy_payload`, `isinstance`, `pytest.mark.parametrize`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_invalid_confidence_is_rejected`

**Signature**

```python
def test_invalid_confidence_is_rejected() -> None:
```

**Purpose**

Protects the `invalid confidence is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `payload` from `_policy_payload(inputs, coded)`.
- Computes `entries` from `payload['entries']`.
- Computes `entries[0]['confidence']` from `'CERTAIN'`.
- Computes `payload['canonical_policy_entries_sha256']` from `_canonical_sha256(entries)`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `BessPlanningFeaturePolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `_integration_inputs`, `_policy_payload`, `isinstance`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert isinstance(entries, list)`.
- Expected exception contexts: `with pytest.raises(ValidationError): BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `invalid confidence is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `_integration_inputs`, `_policy_payload`, `isinstance`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_status_priority_contract_is_strict`

**Signature**

```python
def test_status_priority_contract_is_strict(mutation: str) -> None:
```

**Purpose**

Protects the `status priority contract is strict` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 5 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `payload` from `_policy_payload(inputs, coded)`.
- Computes `priorities` from `payload['status_priority']`.
- Enters managed context(s) `pytest.raises(ValidationError, match='priority|integer')` and executes: Calls `BessPlanningFeaturePolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessPlanningFeaturePolicyConfig.model_validate`, `_integration_inputs`, `_policy_payload`, `isinstance`, `priorities.pop`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert isinstance(priorities, dict)`.
- Expected exception contexts: `with pytest.raises(ValidationError, match='priority|integer'): BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `status priority contract is strict` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_integration_inputs`, `_policy_payload`, `isinstance`, `priorities.pop`, `pytest.mark.parametrize`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_duplicate_yaml_key_is_rejected`

**Signature**

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
```

**Purpose**

Protects the `duplicate yaml key is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 2 explicit setup/context statement(s).
- Computes `path` from `tmp_path / 'duplicate.yaml'`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='Duplicate YAML')` and executes: Calls `load_bess_planning_feature_policy_config(path)` for its validation or side effect.

**Action**

- Calls `load_bess_planning_feature_policy_config`, `path.write_text`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='Duplicate YAML'): load_bess_planning_feature_policy_config(path)`.

**Regression protected**

- Protects the exact `duplicate yaml key is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `load_bess_planning_feature_policy_config`, `path.write_text`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_unknown_yaml_field_is_rejected`

**Signature**

```python
def test_unknown_yaml_field_is_rejected() -> None:
```

**Purpose**

Protects the `unknown yaml field is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `payload` from `_policy_payload(inputs, coded)`.
- Computes `payload['unknown_field']` from `'not allowed'`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Calls `BessPlanningFeaturePolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessPlanningFeaturePolicyConfig.model_validate`, `_integration_inputs`, `_policy_payload`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError): BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `unknown yaml field is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_integration_inputs`, `_policy_payload`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_noncanonical_whitespace_is_rejected`

**Signature**

```python
def test_noncanonical_whitespace_is_rejected() -> None:
```

**Purpose**

Protects the `noncanonical whitespace is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 7 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `payload` from `_policy_payload(inputs, coded)`.
- Computes `entries` from `payload['entries']`.
- Computes `entries[0]['rationale']` from `' leading whitespace'`.
- Computes `payload['canonical_policy_entries_sha256']` from `_canonical_sha256(entries)`.
- Enters managed context(s) `pytest.raises(ValidationError, match='whitespace|exact')` and executes: Calls `BessPlanningFeaturePolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `_integration_inputs`, `_policy_payload`, `isinstance`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert isinstance(entries, list)`.
- Expected exception contexts: `with pytest.raises(ValidationError, match='whitespace|exact'): BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `noncanonical whitespace is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `_integration_inputs`, `_policy_payload`, `isinstance`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_malformed_sha256_is_rejected`

**Signature**

```python
def test_malformed_sha256_is_rejected() -> None:
```

**Purpose**

Protects the `malformed sha256 is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `payload` from `_policy_payload(inputs, coded)`.
- Computes `payload['canonical_policy_entries_sha256']` from `'NOT-A-SHA'`.
- Enters managed context(s) `pytest.raises(ValidationError, match='SHA256')` and executes: Calls `BessPlanningFeaturePolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessPlanningFeaturePolicyConfig.model_validate`, `_integration_inputs`, `_policy_payload`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError, match='SHA256'): BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `malformed sha256 is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_integration_inputs`, `_policy_payload`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_in_memory_config_is_revalidated_before_compilation`

**Signature**

```python
def test_in_memory_config_is_revalidated_before_compilation() -> None:
```

**Purpose**

Protects the `in memory config is revalidated before compilation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `(inputs, coded, config, _)` from `_compiled_fixture()`.
- Computes `corrupted` from `config.model_copy(update={'canonical_policy_entries_sha256': 'f' * 64})`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='in-memory|canonical')` and executes: Calls `compile_bess_planning_feature_policy(*inputs, coded, corrupted)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `compile_bess_planning_feature_policy`, `config.model_copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='in-memory|canonical'): compile_bess_planning_feature_policy(*inputs, coded, corrupted)`.

**Regression protected**

- Protects the exact `in memory config is revalidated before compilation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `compile_bess_planning_feature_policy`, `config.model_copy`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_entries_require_deterministic_order`

**Signature**

```python
def test_policy_entries_require_deterministic_order() -> None:
```

**Purpose**

Protects the `policy entries require deterministic order` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `payload` from `_policy_payload(inputs, coded)`.
- Computes `entries` from `payload['entries']`.
- Computes `payload['canonical_policy_entries_sha256']` from `_canonical_sha256(entries)`.
- Enters managed context(s) `pytest.raises(ValidationError, match='order')` and executes: Calls `BessPlanningFeaturePolicyConfig.model_validate(payload)` for its validation or side effect.

**Action**

- Calls `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `_integration_inputs`, `_policy_payload`, `entries.reverse`, `isinstance`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert isinstance(entries, list)`.
- Expected exception contexts: `with pytest.raises(ValidationError, match='order'): BessPlanningFeaturePolicyConfig.model_validate(payload)`.

**Regression protected**

- Protects the exact `policy entries require deterministic order` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_canonical_sha256`, `_integration_inputs`, `_policy_payload`, `entries.reverse`, `isinstance`, `pytest.raises`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_table_is_sorted_and_preserves_leading_zero_codes`

**Signature**

```python
def test_policy_table_is_sorted_and_preserves_leading_zero_codes() -> None:
```

**Purpose**

Protects the `policy table is sorted and preserves leading zero codes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `keys` from `list(result.policy_table[['feature_family', 'type_code', 'subtype_code']].itertuples(index=False, name=None))`.

**Action**

- Calls `_compiled_fixture`, `all`, `result.policy_table[['feature_family', 'type_code', 'subtype_code']].itertuples`, `sorted`.

**Expected result**

- Direct assertions: `assert keys == sorted(keys)`; `assert all((len(type_code) == len(subtype_code) == 2 for _, type_code, subtype_code in keys))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `policy table is sorted and preserves leading zero codes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `all`, `len`, `list`, `result.policy_table[['feature_family', 'type_code', 'subtype_code']].itertuples`, `sorted`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_table_mutation_is_rejected`

**Signature**

```python
def test_policy_table_mutation_is_rejected() -> None:
```

**Purpose**

Protects the `policy table mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `(inputs, coded, config, result)` from `_compiled_fixture()`.
- Computes `table` from `result.policy_table.copy(deep=True)`.
- Computes `table.loc[table.index[0], 'precheck_status']` from `'UNKNOWN'`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='hash|table|rebuilt')` and executes: Calls `validate_bess_planning_feature_policy_result(*inputs, coded, config, replace(result, policy_table=table))` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `replace`, `result.policy_table.copy`, `validate_bess_planning_feature_policy_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='hash|table|rebuilt'): validate_bess_planning_feature_policy_result(*inputs, coded, config, replace(result, policy_table=table))`.

**Regression protected**

- Protects the exact `policy table mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `pytest.raises`, `replace`, `result.policy_table.copy`, `validate_bess_planning_feature_policy_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_coordinated_policy_table_and_hash_mutation_is_rejected`

**Signature**

```python
def test_coordinated_policy_table_and_hash_mutation_is_rejected() -> None:
```

**Purpose**

Protects the `coordinated policy table and hash mutation is rejected` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 6 explicit setup/context statement(s).
- Computes `(inputs, coded, config, result)` from `_compiled_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `table` from `result.policy_table.copy(deep=True)`.
- Computes `table.loc[table.index[0], 'rationale']` from `'Coordinated but false rationale.'`.
- Computes `coordinated` from `module._result_with_hashes(replace(result, policy_table=table))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='table|rebuilt')` and executes: Calls `validate_bess_planning_feature_policy_result(*inputs, coded, config, coordinated)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `importlib.import_module`, `module._result_with_hashes`, `replace`, `result.policy_table.copy`, `validate_bess_planning_feature_policy_result`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='table|rebuilt'): validate_bess_planning_feature_policy_result(*inputs, coded, config, coordinated)`.

**Regression protected**

- Protects the exact `coordinated policy table and hash mutation is rejected` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `importlib.import_module`, `module._result_with_hashes`, `pytest.raises`, `replace`, `result.policy_table.copy`, `validate_bess_planning_feature_policy_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_persisted_parquet_and_json_readback_is_source_complete`

**Signature**

```python
def test_persisted_parquet_and_json_readback_is_source_complete(
    tmp_path: Path,
) -> None:
```

**Purpose**

Protects the `persisted parquet and json readback is source complete` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `(inputs, coded, config, result)` from `_compiled_fixture()`.
- Computes `(parquet, manifest_path, _)` from `_write_artifacts(tmp_path, result)`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `persisted` from `module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)`.
- Computes `row` from `persisted.policy_table.loc[(persisted.policy_table['feature_family'] == 'INFORMATION') & (persisted.policy_table['type_code'] == '99') & (persisted.policy_table['subtype_code'] == '00')].iloc[0]`.

**Action**

- Calls `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `module.load_bess_planning_feature_policy_artifacts`, `pd.isna`, `validate_bess_planning_feature_policy_result`.

**Expected result**

- Direct assertions: `assert pd.isna(row['official_legal_reference'])`; `assert pd.isna(row['official_regulation_reference'])`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `persisted parquet and json readback is source complete` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `_write_artifacts`, `assert_frame_equal`, `importlib.import_module`, `module.load_bess_planning_feature_policy_artifacts`, `pd.isna`, `validate_bess_planning_feature_policy_result`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_manifest_model_is_strict_and_frozen`

**Signature**

```python
def test_artifact_manifest_model_is_strict_and_frozen(tmp_path: Path) -> None:
```

**Purpose**

Protects the `artifact manifest model is strict and frozen` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 5 explicit setup/context statement(s).
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `(parquet, _, manifest)` from `_write_artifacts(tmp_path, result)`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `validated` from `module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)`.
- Enters managed context(s) `pytest.raises(ValidationError)` and executes: Computes `validated.parquet_row_count` from `0`.

**Action**

- Calls `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `module.BessPlanningFeaturePolicyArtifactManifest.model_validate`.

**Expected result**

- Direct assertions: `assert validated.schema_version == 2`; `assert validated.artifact_kind == ARTIFACT_KIND`; `assert validated.cnig_profile_schema_version == 2`; `assert validated.cnig_result_hash_schema_version == 5`; `assert validated.parquet_filename == parquet.name`.
- Expected exception contexts: `with pytest.raises(ValidationError): validated.parquet_row_count = 0`.

**Regression protected**

- Protects the exact `artifact manifest model is strict and frozen` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `module.BessPlanningFeaturePolicyArtifactManifest.model_validate`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_rejects_manifest_mismatch`

**Signature**

```python
def test_artifact_loader_rejects_manifest_mismatch(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
```

**Purpose**

Protects the `artifact loader rejects manifest mismatch` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `mutation`, `message`.
- Contains 4 explicit setup/context statement(s).
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `(parquet, manifest_path, manifest)` from `_write_artifacts(tmp_path, result)`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match=message)` and executes: Calls `module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `_write_artifacts`, `callable`, `importlib.import_module`, `json.dumps`, `manifest_path.write_text`, `module.load_bess_planning_feature_policy_artifacts`, `mutation`, `value.pop`, `value.update`, `value['policy_table_schema_signature'].update`.

**Expected result**

- Direct assertions: `assert callable(mutation)`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match=message): module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)`.

**Regression protected**

- Protects the exact `artifact loader rejects manifest mismatch` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `_write_artifacts`, `callable`, `importlib.import_module`, `json.dumps`, `manifest_path.write_text`, `module.load_bess_planning_feature_policy_artifacts`, `mutation`, `pytest.mark.parametrize`, `pytest.raises`, `value.pop`, `value.update`, `value['policy_table_schema_signature'].update`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_rejects_duplicate_json_key`

**Signature**

```python
def test_artifact_loader_rejects_duplicate_json_key(tmp_path: Path) -> None:
```

**Purpose**

Protects the `artifact loader rejects duplicate json key` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `(parquet, manifest_path, _)` from `_write_artifacts(tmp_path, result)`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='Duplicate JSON')` and executes: Calls `module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `manifest_path.write_text`, `module.load_bess_planning_feature_policy_artifacts`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='Duplicate JSON'): module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)`.

**Regression protected**

- Protects the exact `artifact loader rejects duplicate json key` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `manifest_path.write_text`, `module.load_bess_planning_feature_policy_artifacts`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_rejects_parquet_replacement`

**Signature**

```python
def test_artifact_loader_rejects_parquet_replacement(tmp_path: Path) -> None:
```

**Purpose**

Protects the `artifact loader rejects parquet replacement` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`.
- Contains 4 explicit setup/context statement(s).
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `(parquet, manifest_path, _)` from `_write_artifacts(tmp_path, result)`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='size|SHA|hash')` and executes: Calls `module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `module.load_bess_planning_feature_policy_artifacts`, `parquet.read_bytes`, `parquet.write_bytes`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='size|SHA|hash'): module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)`.

**Regression protected**

- Protects the exact `artifact loader rejects parquet replacement` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `module.load_bess_planning_feature_policy_artifacts`, `parquet.read_bytes`, `parquet.write_bytes`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_artifact_loader_parses_the_exact_verified_parquet_bytes`

**Signature**

```python
def test_artifact_loader_parses_the_exact_verified_parquet_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `artifact loader parses the exact verified parquet bytes` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`.
- Contains 11 explicit setup/context statement(s).
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `(parquet, manifest_path, _)` from `_write_artifacts(tmp_path, result)`.
- Computes `replacement` from `tmp_path / 'replacement.parquet'`.
- Computes `original_read_bytes` from `Path.read_bytes`.
- Computes `verified_bytes` from `original_read_bytes(parquet)`.
- Computes `replacement_bytes` from `original_read_bytes(replacement)`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `original_read_parquet` from `module.pd.read_parquet`.
- Computes `replacement_performed` from `False`.
- Defines `parsed_payloads` with annotation `list[tuple[str, bytes]]` from `[]`.
- Computes `loaded` from `module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)`.

**Action**

- Calls `Path`, `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `isinstance`, `module.load_bess_planning_feature_policy_artifacts`, `monkeypatch.setattr`, `original_read_bytes`, `original_read_parquet`, `parsed_payloads.append`, `path.write_bytes`, `result.policy_table.to_parquet`, `sha256`, `sha256(payload).hexdigest`, `source.getvalue`.

**Expected result**

- Direct assertions: `assert replacement_bytes != verified_bytes`; `assert replacement_performed`; `assert parsed_payloads == [('buffer', verified_bytes)]`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `artifact loader parses the exact verified parquet bytes` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `Path`, `_compiled_fixture`, `_write_artifacts`, `assert_frame_equal`, `importlib.import_module`, `isinstance`, `module.load_bess_planning_feature_policy_artifacts`, `monkeypatch.setattr`, `original_read_bytes`, `original_read_parquet`, `parsed_payloads.append`, `path.write_bytes`, `result.policy_table.to_parquet`, `sha256`, `sha256(payload).hexdigest`, `source.getvalue`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_locally_invalid_result_fast_fails_before_source_validation`

**Signature**

```python
def test_locally_invalid_result_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `locally invalid result fast fails before source validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 5 explicit setup/context statement(s).
- Computes `(inputs, coded, config, result)` from `_compiled_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `calls` from `0`.
- Computes `wrong_table` from `result.policy_table.drop(columns='confidence')`.
- Computes `invalid_results` from `(object(), replace(result, policy_schema_version=2), replace(result, policy_table=wrong_table), replace(result, policy_table_content_sha256='f' * 64), replace(result, complete_result_content_sha256='f' * 64))`.

**Action**

- Calls `_compiled_fixture`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result`, `monkeypatch.setattr`, `object`, `replace`, `result.policy_table.drop`.

**Expected result**

- Direct assertions: `assert calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='type|schema|hash|result'): module.validate_bess_planning_feature_policy_result(*inputs, coded, config, invalid)`.

**Regression protected**

- Protects the exact `locally invalid result fast fails before source validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result`, `monkeypatch.setattr`, `object`, `pytest.raises`, `replace`, `result.policy_table.drop`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_compiler_wrong_source_lock_fast_fails_before_source_validation`

**Signature**

```python
def test_compiler_wrong_source_lock_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `compiler wrong source lock fast fails before source validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 6 explicit setup/context statement(s).
- Computes `(inputs, coded, config, _)` from `_compiled_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `calls` from `0`.
- Computes `wrong_lock` from `config.source_lock.model_copy(update={'document_id': 'another-document'})`.
- Computes `wrong_config` from `config.model_copy(update={'source_lock': wrong_lock})`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='lock|document')` and executes: Calls `module.compile_bess_planning_feature_policy(*inputs, coded, wrong_config)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `config.model_copy`, `config.source_lock.model_copy`, `importlib.import_module`, `module.compile_bess_planning_feature_policy`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert calls == 0`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='lock|document'): module.compile_bess_planning_feature_policy(*inputs, coded, wrong_config)`.

**Regression protected**

- Protects the exact `compiler wrong source lock fast fails before source validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `config.model_copy`, `config.source_lock.model_copy`, `importlib.import_module`, `module.compile_bess_planning_feature_policy`, `monkeypatch.setattr`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_forged_matching_lock_still_runs_source_complete_validation`

**Signature**

```python
def test_forged_matching_lock_still_runs_source_complete_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `forged matching lock still runs source complete validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 8 explicit setup/context statement(s).
- Computes `(inputs, coded, config, _)` from `_compiled_fixture()`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `actual` from `module.validate_planning_feature_code_result`.
- Computes `calls` from `0`.
- Computes `forged_coded` from `replace(coded, source_document_id='forged-document')`.
- Computes `forged_lock` from `config.source_lock.model_copy(update={'document_id': 'forged-document'})`.
- Computes `forged_config` from `config.model_copy(update={'source_lock': forged_lock})`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='Source-complete|source')` and executes: Calls `module.compile_bess_planning_feature_policy(*inputs, forged_coded, forged_config)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `actual`, `config.model_copy`, `config.source_lock.model_copy`, `importlib.import_module`, `module.compile_bess_planning_feature_policy`, `monkeypatch.setattr`, `replace`.

**Expected result**

- Direct assertions: `assert calls == 1`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='Source-complete|source'): module.compile_bess_planning_feature_policy(*inputs, forged_coded, forged_config)`.

**Regression protected**

- Protects the exact `forged matching lock still runs source complete validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `actual`, `config.model_copy`, `config.source_lock.model_copy`, `importlib.import_module`, `module.compile_bess_planning_feature_policy`, `monkeypatch.setattr`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_compiler_and_public_validator_invoke_source_complete_coding_validation`

**Signature**

```python
def test_compiler_and_public_validator_invoke_source_complete_coding_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

**Purpose**

Protects the `compiler and public validator invoke source complete coding validation` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `monkeypatch`.
- Contains 7 explicit setup/context statement(s).
- Computes `inputs` from `_integration_inputs()`.
- Computes `coded` from `resolve_planning_feature_codes(*inputs)`.
- Computes `config` from `BessPlanningFeaturePolicyConfig.model_validate(_policy_payload(inputs, coded))`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `actual` from `module.validate_planning_feature_code_result`.
- Computes `calls` from `0`.
- Computes `result` from `module.compile_bess_planning_feature_policy(*inputs, coded, config)`.

**Action**

- Calls `BessPlanningFeaturePolicyConfig.model_validate`, `_integration_inputs`, `_policy_payload`, `actual`, `importlib.import_module`, `module.compile_bess_planning_feature_policy`, `module.validate_bess_planning_feature_policy_result`, `monkeypatch.setattr`, `resolve_planning_feature_codes`.

**Expected result**

- Direct assertions: `assert calls == 1`; `assert calls == 2`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `compiler and public validator invoke source complete coding validation` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `BessPlanningFeaturePolicyConfig.model_validate`, `_integration_inputs`, `_policy_payload`, `actual`, `importlib.import_module`, `module.compile_bess_planning_feature_policy`, `module.validate_bess_planning_feature_policy_result`, `monkeypatch.setattr`, `resolve_planning_feature_codes`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_public_policy_api_exports_only_stable_symbols`

**Signature**

```python
def test_public_policy_api_exports_only_stable_symbols() -> None:
```

**Purpose**

Protects the `public policy api exports only stable symbols` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `required` from `{'BessPlanningFeaturePolicyArtifactManifest', 'BessPlanningFeaturePolicyConfig', 'BessPlanningFeaturePolicyError', 'BessPlanningFeaturePolicyResult', 'load_bess_planning_feature_policy_artifacts', 'load_bess_planning_feature_policy_config', 'compile_bess_planning_feature_policy', 'validate_bess_planning_feature_policy…`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.

**Action**

- Calls `all`, `any`, `getattr`, `importlib.import_module`, `required.issubset`.

**Expected result**

- Direct assertions: `assert set(module.__all__) == required`; `assert required.issubset(set(stages.__all__))`; `assert all((getattr(stages, name) is getattr(module, name) for name in required))`; `assert not any((name in module.__all__ for name in ('_canonical_sha256', '_lookup')))`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `public policy api exports only stable symbols` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `all`, `any`, `getattr`, `importlib.import_module`, `required.issubset`, `set`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator`

**Signature**

```python
def test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator() -> None:
```

**Purpose**

Protects the `step 7d 5b 2b 5 exposes lightweight policy result validator` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 3 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='hash')` and executes: Calls `module.validate_bess_planning_feature_policy_result_envelope(replace(result, complete_result_content_sha256='0' * 64))` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `hasattr`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`, `replace`.

**Expected result**

- Direct assertions: `assert hasattr(module, 'validate_bess_planning_feature_policy_result_envelope')`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='hash'): module.validate_bess_planning_feature_policy_result_envelope(replace(result, complete_result_content_sha256='0' * 64))`.

**Regression protected**

- Protects the exact `step 7d 5b 2b 5 exposes lightweight policy result validator` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `hasattr`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_manifest_rejects_nonportable_parquet_filename`

**Signature**

```python
def test_policy_manifest_rejects_nonportable_parquet_filename(
    tmp_path: Path, filename: str
) -> None:
```

**Purpose**

Protects the `policy manifest rejects nonportable parquet filename` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `filename`.
- Contains 5 explicit setup/context statement(s).
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `(_, _, manifest)` from `_write_artifacts(tmp_path, result)`.
- Computes `manifest['parquet_filename']` from `filename`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Enters managed context(s) `pytest.raises(ValueError, match='filename|basename|portable')` and executes: Calls `module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `module.BessPlanningFeaturePolicyArtifactManifest.model_validate`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='filename|basename|portable'): module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)`.

**Regression protected**

- Protects the exact `policy manifest rejects nonportable parquet filename` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `module.BessPlanningFeaturePolicyArtifactManifest.model_validate`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_shared_filename_contract_rejects_superscript_windows_devices`

**Signature**

```python
def test_shared_filename_contract_rejects_superscript_windows_devices(
    filename: str,
) -> None:
```

**Purpose**

Protects the `shared filename contract rejects superscript windows devices` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `filename`.
- Contains 1 explicit setup/context statement(s).
- Enters managed context(s) `pytest.raises(ValueError, match='reserved|basename|portable')` and executes: Calls `validate_portable_parquet_filename(filename, 'artifact filename')` for its validation or side effect.

**Action**

- Calls `validate_portable_parquet_filename`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValueError, match='reserved|basename|portable'): validate_portable_parquet_filename(filename, 'artifact filename')`.

**Regression protected**

- Protects the exact `shared filename contract rejects superscript windows devices` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `pytest.mark.parametrize`, `pytest.raises`, `validate_portable_parquet_filename`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_manifest_rejects_unsupported_cnig_source_schema`

**Signature**

```python
def test_policy_manifest_rejects_unsupported_cnig_source_schema(
    tmp_path: Path,
    field: str,
    version: int,
) -> None:
```

**Purpose**

Protects the `policy manifest rejects unsupported cnig source schema` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `field`, `version`.
- Contains 5 explicit setup/context statement(s).
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `(_, _, manifest)` from `_write_artifacts(tmp_path, result)`.
- Computes `manifest[field]` from `version`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Enters managed context(s) `pytest.raises(ValidationError, match='CNIG|cnig|schema|version')` and executes: Calls `module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `module.BessPlanningFeaturePolicyArtifactManifest.model_validate`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(ValidationError, match='CNIG|cnig|schema|version'): module.BessPlanningFeaturePolicyArtifactManifest.model_validate(manifest)`.

**Regression protected**

- Protects the exact `policy manifest rejects unsupported cnig source schema` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `module.BessPlanningFeaturePolicyArtifactManifest.model_validate`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_artifact_loader_rejects_source_schema_before_parquet_read`

**Signature**

```python
def test_policy_artifact_loader_rejects_source_schema_before_parquet_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    version: int,
) -> None:
```

**Purpose**

Protects the `policy artifact loader rejects source schema before parquet read` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `tmp_path`, `monkeypatch`, `field`, `version`.
- Contains 6 explicit setup/context statement(s).
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `(parquet, manifest_path, manifest)` from `_write_artifacts(tmp_path, result)`.
- Computes `manifest[field]` from `version`.
- Computes `calls` from `{'bytes': 0, 'parse': 0}`.
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='CNIG|cnig|schema|version')` and executes: Calls `module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)` for its validation or side effect.

**Action**

- Calls `AssertionError`, `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `json.dumps`, `manifest_path.write_text`, `module.load_bess_planning_feature_policy_artifacts`, `monkeypatch.setattr`.

**Expected result**

- Direct assertions: `assert calls == {'bytes': 0, 'parse': 0}`.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='CNIG|cnig|schema|version'): module.load_bess_planning_feature_policy_artifacts(parquet, manifest_path)`.

**Regression protected**

- Protects the exact `policy artifact loader rejects source schema before parquet read` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- synthetic filesystem; monkeypatches/mocks. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `AssertionError`, `_compiled_fixture`, `_write_artifacts`, `importlib.import_module`, `json.dumps`, `manifest_path.write_text`, `module.load_bess_planning_feature_policy_artifacts`, `monkeypatch.setattr`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_envelope_rejects_canonical_empty_policy_table`

**Signature**

```python
def test_policy_envelope_rejects_canonical_empty_policy_table() -> None:
```

**Purpose**

Protects the `policy envelope rejects canonical empty policy table` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `empty` from `_canonical_empty_policy_result(result)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='policy|table|empty|entry')` and executes: Calls `module.validate_bess_planning_feature_policy_result_envelope(empty)` for its validation or side effect.

**Action**

- Calls `_canonical_empty_policy_result`, `_compiled_fixture`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='policy|table|empty|entry'): module.validate_bess_planning_feature_policy_result_envelope(empty)`.

**Regression protected**

- Protects the exact `policy envelope rejects canonical empty policy table` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_canonical_empty_policy_result`, `_compiled_fixture`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_envelope_accepts_one_exact_policy_row`

**Signature**

```python
def test_policy_envelope_accepts_one_exact_policy_row() -> None:
```

**Purpose**

Protects the `policy envelope accepts one exact policy row` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 5 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `table` from `result.policy_table.iloc[[0]].copy(deep=True)`.
- Computes `table.index` from `pd.Index([0], dtype='int64')`.
- Computes `one_row` from `_rehash_policy_table(result, table)`.

**Action**

- Calls `_compiled_fixture`, `_rehash_policy_table`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`, `pd.Index`, `result.policy_table.iloc[[0]].copy`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `policy envelope accepts one exact policy row` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `_rehash_policy_table`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`, `pd.Index`, `result.policy_table.iloc[[0]].copy`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_envelope_accepts_current_twelve_row_snapshot`

**Signature**

```python
def test_policy_envelope_accepts_current_twelve_row_snapshot() -> None:
```

**Purpose**

Protects the `policy envelope accepts current twelve row snapshot` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 2 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `result` from `_checked_in_policy_result()`.

**Action**

- Calls `_checked_in_policy_result`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`.

**Expected result**

- Direct assertions: `assert len(result.policy_table) == 12`.
- Expected exception contexts: none.

**Regression protected**

- Protects the exact `policy envelope accepts current twelve row snapshot` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_checked_in_policy_result`, `importlib.import_module`, `len`, `module.validate_bess_planning_feature_policy_result_envelope`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_envelope_requires_cnig_profile_schema_two`

**Signature**

```python
def test_policy_envelope_requires_cnig_profile_schema_two(version: int) -> None:
```

**Purpose**

Protects the `policy envelope requires cnig profile schema two` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `version`.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `changed` from `module._result_with_hashes(replace(result, cnig_profile_schema_version=version))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='profile schema|schema')` and executes: Calls `module.validate_bess_planning_feature_policy_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module.validate_bess_planning_feature_policy_result_envelope`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='profile schema|schema'): module.validate_bess_planning_feature_policy_result_envelope(changed)`.

**Regression protected**

- Protects the exact `policy envelope requires cnig profile schema two` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module.validate_bess_planning_feature_policy_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_envelope_requires_cnig_result_schema_five`

**Signature**

```python
def test_policy_envelope_requires_cnig_result_schema_five(version: int) -> None:
```

**Purpose**

Protects the `policy envelope requires cnig result schema five` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `version`.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `changed` from `module._result_with_hashes(replace(result, cnig_result_hash_schema_version=version))`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='CNIG result|schema')` and executes: Calls `module.validate_bess_planning_feature_policy_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module.validate_bess_planning_feature_policy_result_envelope`, `replace`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='CNIG result|schema'): module.validate_bess_planning_feature_policy_result_envelope(changed)`.

**Regression protected**

- Protects the exact `policy envelope requires cnig result schema five` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `importlib.import_module`, `module._result_with_hashes`, `module.validate_bess_planning_feature_policy_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `replace`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_envelope_validates_every_intrinsic_row_contract`

**Signature**

```python
def test_policy_envelope_validates_every_intrinsic_row_contract(
    mutation: str,
) -> None:
```

**Purpose**

Protects the `policy envelope validates every intrinsic row contract` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `mutation`.
- Contains 6 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `table` from `result.policy_table.copy(deep=True)`.
- Computes `(first, second)` from `table.index[:2]`.
- Computes `changed` from `_rehash_policy_table(result, table)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='policy|pair|order|code|status|confidence|priority|scope|flag|CNIG|null|schema')` and executes: Calls `module.validate_bess_planning_feature_policy_result_envelope(changed)` for its validation or side effect.

**Action**

- Calls `_compiled_fixture`, `_rehash_policy_table`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`, `result.policy_table.copy`, `table.iloc[::-1].copy`, `table.loc[first, ['feature_family', 'type_code', 'subtype_code']].tolist`, `table['status_priority'].astype`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='policy|pair|order|code|status|confidence|priority|scope|flag|CNIG|null|schema'): module.validate_bess_planning_feature_policy_result_envelope(changed)`.

**Regression protected**

- Protects the exact `policy envelope validates every intrinsic row contract` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `_compiled_fixture`, `_rehash_policy_table`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`, `pytest.mark.parametrize`, `pytest.raises`, `result.policy_table.copy`, `table.iloc[::-1].copy`, `table.loc[first, ['feature_family', 'type_code', 'subtype_code']].tolist`, `table['status_priority'].astype`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1`

**Signature**

```python
def test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1() -> None:
```

**Purpose**

Protects the `policy envelope requires exact type and accepts valid schema v1` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: none.
- Contains 4 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Computes `(_, _, _, result)` from `_compiled_fixture()`.
- Computes `derived` from `DerivedPolicyResult(**result.__dict__)`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError, match='type|result')` and executes: Calls `module.validate_bess_planning_feature_policy_result_envelope(derived)` for its validation or side effect.

**Action**

- Calls `DerivedPolicyResult`, `_compiled_fixture`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError, match='type|result'): module.validate_bess_planning_feature_policy_result_envelope(derived)`.

**Regression protected**

- Protects the exact `policy envelope requires exact type and accepts valid schema v1` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `DerivedPolicyResult`, `_compiled_fixture`, `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

### `test_policy_envelope_controls_malformed_result_type`

**Signature**

```python
def test_policy_envelope_controls_malformed_result_type(malformed: object) -> None:
```

**Purpose**

Protects the `policy envelope controls malformed result type` behavior encoded by this regression's setup, action, and assertions.

**Setup**

- Uses parameters/fixtures: `malformed`.
- Contains 2 explicit setup/context statement(s).
- Computes `module` from `importlib.import_module('landscout.stages.bess_planning_feature_policy')`.
- Enters managed context(s) `pytest.raises(BessPlanningFeaturePolicyError)` and executes: Calls `module.validate_bess_planning_feature_policy_result_envelope(malformed)` for its validation or side effect.

**Action**

- Calls `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`, `object`.

**Expected result**

- Direct assertions: none; the expected failure is expressed through a context manager.
- Expected exception contexts: `with pytest.raises(BessPlanningFeaturePolicyError): module.validate_bess_planning_feature_policy_result_envelope(malformed)`.

**Regression protected**

- Protects the exact `policy envelope controls malformed result type` contract against a future change that would violate these assertions or controlled-failure expectations.

**Test boundary**

- in-memory synthetic data and local calls only. No live external source is implied unless the setup explicitly opens one.

**Calls**

- `importlib.import_module`, `module.validate_bess_planning_feature_policy_result_envelope`, `object`, `pytest.mark.parametrize`, `pytest.raises`.

**Does NOT prove**

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `LIKELY_MATERIAL_CONSTRAINT` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `UNKNOWN` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bytes` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `canonical_policy_entries_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `cnig_complete_result_content_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `cnig_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `cnig_profile_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `dependencies` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `entries` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_family` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `legal_conclusion_produced` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `local_feature_text_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `local_regulation_content_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_legal_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_regulation_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parquet_filename` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parse` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `policy_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `policy_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `policy_table_schema_signature` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `project` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `rationale` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_lock` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `status_priority` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `subtype_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `type_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `unknown_field` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `test` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- The test proves only the exercised synthetic or mocked contract; it does not substitute for live-source or legal validation.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
