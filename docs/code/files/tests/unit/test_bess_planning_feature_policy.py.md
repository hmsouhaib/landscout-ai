# `tests/unit/test_bess_planning_feature_policy.py`

- Source: [tests/unit/test_bess_planning_feature_policy.py](../../../../../tests/unit/test_bess_planning_feature_policy.py)
- Source SHA256: `49d02758c7dd407fe95e10340c0b80d7da71cb9d39b27aac18f5cfacca9888d8`
- Source SHA256 basis: `git-content`
- Source lines: 1242; Git blob at R10 start: `1cc0c9f48c17efcbf6d780dcd521ffe7d80d83da`

Git/index/checkout source bytes are unchanged. Local semantic closure is not independent approval. [R10 receipt](../../../../../docs/code/audit/R10_BESS_CNIG_COMPILER.md).

## Executable evidence, not inferred coverage

This existing suite exercises policy model/config boundaries, source-complete synthetic compilation, local result envelopes, manifests and captured-byte Parquet readback. Each test notice states its actual assertions. All tests return None on success; failed assertions/pytest.raises checks fail the test. Helpers/callback return annotations below do not override a body that only raises. Parameters named tmp_path/monkeypatch come from pytest; field/value/mutation/document/filename/version/malformed/status are supplied by the shown decorators. There are no locally declared pytest fixtures. A test title is not a universal coverage guarantee.

Imports from `tests.unit.test_resolve_planning_feature_codes` are repository helpers, not third-party APIs. `_integration_inputs` builds four source features (two polygons, one line, one point), one parcel, physical temporary GeoPackages, canonical normalized catalogs/relations and a synthetic CNIG profile. `_planning_document` writes and rereads those files, creates inventory/manifest and a validated synthetic GPU source config; archive metadata are synthetic. The ordinary fixture invokes public source validators. `_checked_in_policy_result` instead replaces identities and dictionary, then calls the private builder: its checked-in Muret hash assertions do not mean real Muret files were validated. Setup may create temporary files even when the subsequent tested guard performs no I/O.

Standard-library imports supply replace, SHA, JSON, Path, BytesIO, importlib and tomllib; Pandas and pandas.testing supply frame/Parquet behavior and equality assertions; pytest and Pydantic own test/error primitives. Imported compiler symbols are production owners. Test module has no __all__, no stable package API and no production writer. [Compiler contract](../../src/landscout/stages/bess_planning_feature_policy.py.md) distinguishes nine-input compiler, ten-input full validator, one-input envelope and two-path local artifact loader.

The 12 checked-in decisions and four pinned digests are reproduced literally below; no policy recalibration or hash-version migration occurs. Test counts are reported only from the authorized run in the R10 receipt, not inferred from parameter decorators. R10-T01: the snapshot “immutable” test asserts pinned values, while the separate priority test attempts one item assignment. R10-T02: strict-JSON instrumentation counts only the Parquet decoder; source-schema instrumentation counts both target raw reads and decoder. R10-T03: bool-priority changes dtype to object and can fail the schema guard first. R10-T04: verified-byte parsing permits path replacement after capture; historical _file_sha256 trap is unused by current production. These are proof limits, not automatic new application findings. Existing A-004 optional-reference mismatch and R5-D01 remain open, not repaired.

Inventory: 52 top-level tests; 73 original symbols including helpers, nested callbacks and one nested class.

## Module declarations

Literal source declarations below add no symbol closure credit.

<a id="declaration-policy-path"></a>
### `tests.unit.test_bess_planning_feature_policy.POLICY_PATH`

Source lines 33–33. Checked-in human-authored Muret YAML path, not a real source-cache location.

```python
POLICY_PATH = Path("configs/planning/muret_bess_cnig_feature_policy.yaml")
```

<a id="declaration-policy-scope"></a>
### `tests.unit.test_bess_planning_feature_policy.POLICY_SCOPE`

Source lines 34–34. Expected scope constant asserted by tests.

```python
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"
```

<a id="declaration-status-priorities"></a>
### `tests.unit.test_bess_planning_feature_policy.STATUS_PRIORITIES`

Source lines 35–41. Test mapping with order used by synthetic entry status cycling; values are pinned in checked-in assertions, not selected from geometry.

```python
STATUS_PRIORITIES = {
    "LIKELY_MATERIAL_CONSTRAINT": 50,
    "UNKNOWN": 40,
    "MATERIAL_REVIEW_REQUIRED": 30,
    "DESIGN_REVIEW_REQUIRED": 20,
    "CONTEXT_REVIEW_REQUIRED": 10,
}
```

<a id="declaration-expected-muret-decisions"></a>
### `tests.unit.test_bess_planning_feature_policy.EXPECTED_MURET_DECISIONS`

Source lines 42–55. Exact 12 checked-in triple-to-status/confidence expectations, not computed legal meanings.

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

<a id="declaration-expected-policy-entries-sha256"></a>
### `tests.unit.test_bess_planning_feature_policy.EXPECTED_POLICY_ENTRIES_SHA256`

Source lines 56–58. Pinned ordered canonical entry-list SHA, not YAML byte SHA.

```python
EXPECTED_POLICY_ENTRIES_SHA256 = (
    "1d3e63f1123000402065b74402cb1e2295db2ac5655209ce410aaf36bfc2be91"
)
```

<a id="declaration-expected-policy-sha256"></a>
### `tests.unit.test_bess_planning_feature_policy.EXPECTED_POLICY_SHA256`

Source lines 59–61. Pinned complete canonical config SHA.

```python
EXPECTED_POLICY_SHA256 = (
    "1cfca0eb3d777e9b6604748e8a81609abe7b728de8d0695711cd569180df6489"
)
```

<a id="declaration-expected-policy-table-sha256"></a>
### `tests.unit.test_bess_planning_feature_policy.EXPECTED_POLICY_TABLE_SHA256`

Source lines 62–64. Pinned private checked-in reconstruction table-content SHA.

```python
EXPECTED_POLICY_TABLE_SHA256 = (
    "225105fe488e21f8aa080751812dde1671340c26620cae1d8372c2e59488ed41"
)
```

<a id="declaration-expected-complete-result-sha256"></a>
### `tests.unit.test_bess_planning_feature_policy.EXPECTED_COMPLETE_RESULT_SHA256`

Source lines 65–67. Pinned private checked-in reconstruction complete-result SHA.

```python
EXPECTED_COMPLETE_RESULT_SHA256 = (
    "84a59b418f5a53bc61df73296964b2847cc5d3529c10d0c6912c96222edba09c"
)
```

<a id="declaration-expected-source-lock"></a>
### `tests.unit.test_bess_planning_feature_policy.EXPECTED_SOURCE_LOCK`

Source lines 68–82. Exact seven-field checked-in lock expectations. Fixture private replacement of these values does not validate physical Muret source files.

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

<a id="declaration-artifact-kind"></a>
### `tests.unit.test_bess_planning_feature_policy.ARTIFACT_KIND`

Source lines 83–83. Expected persisted manifest kind; test-only artifact writer inserts this value.

```python
ARTIFACT_KIND = "BESS_CNIG_FEATURE_POLICY_RESULT"
```

## Qualified symbol contracts

Each notice owns one original symbol. Literal signatures specify argument order, annotations and defaults; fields have no default unless shown. Full bodies/imports appear in the exact final snapshot. No physical units attach to codes/statuses/digests; counts and byte sizes are identified explicitly.

<a id="symbol--canonical-sha256"></a>
### `tests.unit.test_bess_planning_feature_policy._canonical_sha256`

Source lines 86–95. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def _canonical_sha256(value: object) -> str:
```

Test-only canonical JSON SHA helper: UTF-8, sorted keys, compact separators, non-ASCII retained and NaN disallowed. Returns digest; no controlled-error wrapper or disk I/O.

<a id="symbol--policy-entry"></a>
### `tests.unit.test_bess_planning_feature_policy._policy_entry`

Source lines 98–119. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def _policy_entry(row: object, position: int) -> dict[str, object]:
```

Convert one dictionary row object and integer position into a synthetic entry dict; cycle statuses by STATUS_PRIORITIES insertion order and confidence by position modulo 3. Missing official references become None using pd.isna. Copy official label/codes and add synthetic rationale/action/limitations. No source validation or file I/O.

<a id="symbol--compiled-fixture"></a>
### `tests.unit.test_bess_planning_feature_policy._compiled_fixture`

Source lines 122–134. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def _compiled_fixture() -> tuple[
    tuple[object, ...],
    object,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
]:
```

Obtain seven _integration_inputs values, publicly resolve CNIG, validate synthetic policy payload and publicly compile it. Return (inputs, coded, config, result). This transitively creates/reads synthetic GPKGs and factual intersections; not real Muret acquisition or a no-I/O fixture.

<a id="symbol--policy-payload"></a>
### `tests.unit.test_bess_planning_feature_policy._policy_payload`

Source lines 137–165. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def _policy_payload(inputs: tuple[object, ...], coded: object) -> dict[str, object]:
```

Return synthetic schema-1 config dict with seven locks from coded, copied priority dict, entries in dictionary iteration order, and canonical entry digest. inputs parameter is unused. Does not validate the dict or sort entries; no direct I/O.

<a id="symbol--validated-config"></a>
### `tests.unit.test_bess_planning_feature_policy._validated_config`

Source lines 168–172. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def _validated_config(payload: dict[str, object]) -> BessPlanningFeaturePolicyConfig:
```

Assert payload entries is list; MUTATE supplied payload canonical_policy_entries_sha256 to recomputed value, then model_validate and return config. Used after deliberate test changes; no file I/O.

<a id="symbol--artifact-manifest"></a>
### `tests.unit.test_bess_planning_feature_policy._artifact_manifest`

Source lines 175–195. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def _artifact_manifest(
    result: BessPlanningFeaturePolicyResult,
    parquet: Path,
) -> dict[str, object]:
```

Introspect result dataclass fields except table, combine with schema/kind, filename, row count, stat size, raw read_bytes SHA and deterministic schema signature. Returns mutable dict. stat/read are separate test operations, not atomic snapshot proof.

<a id="symbol--write-artifacts"></a>
### `tests.unit.test_bess_planning_feature_policy._write_artifacts`

Source lines 198–210. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeaturePolicyResult,
) -> tuple[Path, Path, dict[str, object]]:
```

Write result table to policy.parquet with index=True; construct manifest and write sorted indented UTF-8 JSON with final newline to policy.json. Return (Parquet Path, manifest Path, mutable manifest dict). Test-only writer, no production export promise.

<a id="symbol--checked-in-policy-result"></a>
### `tests.unit.test_bess_planning_feature_policy._checked_in_policy_result`

Source lines 213–241. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def _checked_in_policy_result() -> BessPlanningFeaturePolicyResult:
```

Create synthetic physical inputs and publicly resolve them; load checked-in Muret policy and CNIG profile. Replace coded profile/source/version/hash identities with policy lock values and code dictionary with private _dictionary output, then call private policy _build_result. It bypasses the public compiler’s source-lock/CNIG source validation for those forged identities; no physical Muret validation or rehash of complete coded result is asserted.

<a id="symbol-test-valid-exact-policy-compiles-without-applying-feature-or-parcel-status"></a>
### `tests.unit.test_bess_planning_feature_policy.test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status`

Source lines 244–259. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_valid_exact_policy_compiles_without_applying_feature_or_parcel_status() -> (
    None
):
```

Compile synthetic fixture and call full validator. Assert policy/result versions 1/1, scope, table row count equals dictionary length, no parcel_id/planning_feature_id/relation_type columns, and all three flags False. No parcel decision or production Muret source proof.

<a id="symbol-test-checked-in-policy-pins-all-twelve-exact-muret-decisions"></a>
### `tests.unit.test_bess_planning_feature_policy.test_checked_in_policy_pins_all_twelve_exact_muret_decisions`

Source lines 262–280. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_checked_in_policy_pins_all_twelve_exact_muret_decisions() -> None:
```

Load checked-in YAML and compare all 12 triple-to-(status,confidence) declarations with EXPECTED_MURET_DECISIONS, exact priority mapping, scope and False flags; specifically retain PRESCRIPTION 15/00 and 15/01, and assert both code lengths are 2 for every key. This reads policy only, not physical Muret data.

<a id="symbol-test-checked-in-policy-complete-snapshot-is-immutable"></a>
### `tests.unit.test_bess_planning_feature_policy.test_checked_in_policy_complete_snapshot_is_immutable`

Source lines 283–298. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_checked_in_policy_complete_snapshot_is_immutable() -> None:
```

Load checked-in YAML; assert schema 1, exact profile, scope, three False flags, complete source-lock dict, priorities, declared and independently test-helper-recomputed entry digest, and complete config hash. Despite title, no mutation is attempted: this pins values, not every in-place mutation operation.

<a id="symbol-test-checked-in-compiled-policy-result-hashes-are-pinned"></a>
### `tests.unit.test_bess_planning_feature_policy.test_checked_in_compiled_policy_result_hashes_are_pinned`

Source lines 301–304. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_checked_in_compiled_policy_result_hashes_are_pinned() -> None:
```

Use _checked_in_policy_result private reconstruction and assert exact table and complete hashes against constants. Proves deterministic private compilation of those identities, not public acceptance of physical Muret sources.

<a id="symbol-test-profile-v1-snapshot-detects-policy-text-drift"></a>
### `tests.unit.test_bess_planning_feature_policy.test_profile_v1_snapshot_detects_policy_text_drift`

Source lines 311–320. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_profile_v1_snapshot_detects_policy_text_drift(field: str) -> None:
```

For rationale, required_human_action or limitations, append " Changed." to first checked-in entry; recompute entry digest and validate. Assert profile unchanged but policy hash differs from the pinned hash. Modified config is accepted, not rejected by a profile-name pin.

Exact decorators/parameters (not extra closure units):

```python
@pytest.mark.parametrize(
    "field",
    ["rationale", "required_human_action", "limitations"],
)
```

<a id="symbol-test-profile-v1-snapshot-detects-source-lock-drift"></a>
### `tests.unit.test_bess_planning_feature_policy.test_profile_v1_snapshot_detects_source_lock_drift`

Source lines 323–331. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_profile_v1_snapshot_detects_source_lock_drift() -> None:
```

Change only checked-in payload source_lock.document_id to another-document, validate config, and assert same profile with different/unpinned full hash. No source-complete compiler call for this modified config.

<a id="symbol-test-pandas-is-a-direct-bounded-runtime-dependency"></a>
### `tests.unit.test_bess_planning_feature_policy.test_pandas_is_a_direct_bounded_runtime_dependency`

Source lines 334–338. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_pandas_is_a_direct_bounded_runtime_dependency() -> None:
```

Read pyproject.toml using tomllib and assert project dependencies contain pandas>=3.0,<4. This checks declaration, not installed Pandas version or resolver behavior.

<a id="symbol-test-information-9900-official-references-remain-missing"></a>
### `tests.unit.test_bess_planning_feature_policy.test_information_9900_official_references_remain_missing`

Source lines 341–349. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_information_9900_official_references_remain_missing() -> None:
```

Compile ordinary synthetic fixture; select INFORMATION 99/00 and assert both official reference cells are pd.isna. No string replacement and no full null-domain test here.

<a id="symbol-test-null-reference-literal-is-rejected-by-local-envelope"></a>
### `tests.unit.test_bess_planning_feature_policy.test_null_reference_literal_is_rejected_by_local_envelope`

Source lines 363–378. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_null_reference_literal_is_rejected_by_local_envelope(
    column: str,
    literal: str,
) -> None:
```

Six cases: change INFORMATION 99/00 legal or regulation reference to "None", "nan" or "<NA>" on a copied table, reseal table/complete hashes privately, then expect private local-envelope policy error matching reference/null/missing. This isolates intrinsic references from stale hashes; not model-level rejection.

Exact decorators/parameters (not extra closure units):

```python
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
```

<a id="symbol-test-source-lock-mismatch-is-rejected"></a>
### `tests.unit.test_bess_planning_feature_policy.test_source_lock_mismatch_is_rejected`

Source lines 393–398. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_source_lock_mismatch_is_rejected(field: str, value: object) -> None:
```

Seven cases forge one lock through model_copy (document, archive SHA, profile, profile schema, profile SHA, result schema, complete SHA), then model_copy config and call public compiler. Expect controlled error matching lock/source/CNIG; no counter asserts a physical-read total.

Exact decorators/parameters (not extra closure units):

```python
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
```

<a id="symbol-test-missing-policy-pair-is-rejected"></a>
### `tests.unit.test_bess_planning_feature_policy.test_missing_policy_pair_is_rejected`

Source lines 401–410. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_missing_policy_pair_is_rejected() -> None:
```

Pop last synthetic entry, recompute entry hash/model-validate, call public compiler and expect missing/pair error. This is incomplete dictionary coverage despite a coherent config hash.

<a id="symbol-test-extra-policy-pair-is-rejected-without-type-fallback"></a>
### `tests.unit.test_bess_planning_feature_policy.test_extra_policy_pair_is_rejected_without_type_fallback`

Source lines 413–436. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_extra_policy_pair_is_rejected_without_type_fallback() -> None:
```

Clone last entry as INFORMATION 98/00 with new label and None references, append and sort triples, reseal config, then public compile expects extra/pair. No fallback to an existing type is allowed; original input fixture is otherwise unchanged.

<a id="symbol-test-duplicate-policy-pair-is-rejected"></a>
### `tests.unit.test_bess_planning_feature_policy.test_duplicate_policy_pair_is_rejected`

Source lines 439–448. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_duplicate_policy_pair_is_rejected() -> None:
```

Append a copy of first entry, recompute digest and expect model ValidationError duplicate/pair. Duplicate guard precedes order checking; no compiler call for invalid config.

<a id="symbol-test-prescription-information-code-spaces-remain-separate"></a>
### `tests.unit.test_bess_planning_feature_policy.test_prescription_information_code_spaces_remain_separate`

Source lines 451–463. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_prescription_information_code_spaces_remain_separate() -> None:
```

Change first entry family to PRESCRIPTION, sort and reseal/validate config, then compiler expects missing/extra/pair. Exact family matters; missing check can reject before extra. Not an exhaustive proof over every cross-family combination.

<a id="symbol-test-official-meaning-mismatch-is-rejected"></a>
### `tests.unit.test_bess_planning_feature_policy.test_official_meaning_mismatch_is_rejected`

Source lines 474–487. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_official_meaning_mismatch_is_rejected(
    field: str,
    value: object,
    message: str,
) -> None:
```

Three cases alter first expected label, legal reference or regulation reference to stated wrong text; reseal config then public compiler expects corresponding label/legal/regulation error. Dictionary content is not mutated.

Exact decorators/parameters (not extra closure units):

```python
@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("expected_official_label", "Wrong official label", "label"),
        ("expected_legal_reference", "Wrong legal reference", "legal"),
        ("expected_regulation_reference", "Wrong regulation reference", "regulation"),
    ],
)
```

<a id="symbol-test-invalid-or-legal-conclusion-status-is-rejected"></a>
### `tests.unit.test_bess_planning_feature_policy.test_invalid_or_legal_conclusion_status_is_rejected`

Source lines 491–500. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_invalid_or_legal_conclusion_status_is_rejected(status: str) -> None:
```

ALLOWED, FORBIDDEN and PROHIBITED replace first entry status; entry hash updated; config model raises ValidationError. This validates literal vocabulary, not legal correctness of policy meanings.

Exact decorators/parameters (not extra closure units):

```python
@pytest.mark.parametrize("status", ["ALLOWED", "FORBIDDEN", "PROHIBITED"])
```

<a id="symbol-test-invalid-confidence-is-rejected"></a>
### `tests.unit.test_bess_planning_feature_policy.test_invalid_confidence_is_rejected`

Source lines 503–512. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_invalid_confidence_is_rejected() -> None:
```

Set first confidence to CERTAIN, update entry digest and expect config ValidationError. No policy compiler or source mutation is exercised after that failure.

<a id="symbol-test-status-priority-contract-is-strict"></a>
### `tests.unit.test_bess_planning_feature_policy.test_status_priority_contract_is_strict`

Source lines 516–533. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_status_priority_contract_is_strict(mutation: str) -> None:
```

Five payload changes to UNKNOWN priority: duplicate 50, missing key, zero, bool True or string "40". Config model must raise ValidationError matching priority/integer. Tests mapping domain/strict values, not all possible integers.

Exact decorators/parameters (not extra closure units):

```python
@pytest.mark.parametrize("mutation", ["duplicate", "missing", "zero", "bool", "string"])
```

<a id="symbol-test-status-priority-mapping-is-deeply-immutable"></a>
### `tests.unit.test_bess_planning_feature_policy.test_status_priority_mapping_is_deeply_immutable`

Source lines 536–543. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_status_priority_mapping_is_deeply_immutable() -> None:
```

Save model_dump(mode="python"), attempt status_priority["UNKNOWN"]=999, require immediate TypeError matching frozen mapping and unchanged dump. This single item-assignment regression is not a test of all mapping operations or caller-input aliases.

<a id="symbol-test-duplicate-yaml-key-is-rejected"></a>
### `tests.unit.test_bess_planning_feature_policy.test_duplicate_yaml_key_is_rejected`

Source lines 546–550. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
```

Write a temporary YAML file repeating schema_version: 1 and call config loader; expect policy error Duplicate YAML. Parsing fails before model completeness, with no real network/source input.

<a id="symbol-test-unknown-yaml-field-is-rejected"></a>
### `tests.unit.test_bess_planning_feature_policy.test_unknown_yaml_field_is_rejected`

Source lines 553–559. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_unknown_yaml_field_is_rejected() -> None:
```

Add unknown_field to synthetic payload then directly model_validate, expecting ValidationError. Despite title, no YAML file is loaded in this test.

<a id="symbol-test-noncanonical-whitespace-is-rejected"></a>
### `tests.unit.test_bess_planning_feature_policy.test_noncanonical_whitespace_is_rejected`

Source lines 562–571. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_noncanonical_whitespace_is_rejected() -> None:
```

Set first rationale to leading-whitespace text, update entry hash and require config ValidationError matching whitespace/exact. Guard rejects, does not strip.

<a id="symbol-test-malformed-sha256-is-rejected"></a>
### `tests.unit.test_bess_planning_feature_policy.test_malformed_sha256_is_rejected`

Source lines 574–580. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_malformed_sha256_is_rejected() -> None:
```

Replace canonical_policy_entries_sha256 with NOT-A-SHA in synthetic payload and expect model ValidationError SHA256. Tests syntax, not forged valid-format checksum.

<a id="symbol-test-in-memory-config-is-revalidated-before-compilation"></a>
### `tests.unit.test_bess_planning_feature_policy.test_in_memory_config_is_revalidated_before_compilation`

Source lines 583–587. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_in_memory_config_is_revalidated_before_compilation() -> None:
```

model_copy config with entry digest "f" * 64, then public compile must reject in-memory/canonical. This bypassed-model-validation fixture tests boundary reconstruction; no valid entry rehash is supplied.

<a id="symbol-test-policy-entries-require-deterministic-order"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_entries_require_deterministic_order`

Source lines 590–599. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_entries_require_deterministic_order() -> None:
```

Reverse entry list and recompute digest; model_validate rejects order. Hash consistency does not make noncanonical ordering acceptable.

<a id="symbol-test-policy-table-is-sorted-and-preserves-leading-zero-codes"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_table_is_sorted_and_preserves_leading_zero_codes`

Source lines 602–612. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_table_is_sorted_and_preserves_leading_zero_codes() -> None:
```

Extract compiled triple tuples, assert equality to sorted tuples and both code string lengths equal 2. It does not independently inspect every code’s digit syntax here.

<a id="symbol-test-policy-table-mutation-is-rejected"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_table_mutation_is_rejected`

Source lines 615–622. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_table_mutation_is_rejected() -> None:
```

Copy compiled table, set first precheck_status to UNKNOWN without changing priority or hashes, and call full validator expecting hash/table/rebuilt error. The local status-priority consistency guard can fail before hash comparison; broad regex does not identify only one guard.

<a id="symbol-test-coordinated-policy-table-and-hash-mutation-is-rejected"></a>
### `tests.unit.test_bess_planning_feature_policy.test_coordinated_policy_table_and_hash_mutation_is_rejected`

Source lines 625–634. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_coordinated_policy_table_and_hash_mutation_is_rejected() -> None:
```

Copy table, replace first rationale with "Coordinated but false rationale.", privately recompute both result hashes and call full validator; expect table/rebuilt mismatch. Source reconstruction, not stale digest alone, rejects this otherwise coherent altered text.

<a id="symbol-test-persisted-parquet-and-json-readback-is-source-complete"></a>
### `tests.unit.test_bess_planning_feature_policy.test_persisted_parquet_and_json_readback_is_source_complete`

Source lines 637–654. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_persisted_parquet_and_json_readback_is_source_complete(
    tmp_path: Path,
) -> None:
```

Write synthetic fixture artifacts, load through two-path LOCAL loader, assert_frame_equal including dtype and true missing INFORMATION 99/00 legal AND regulation references, THEN separately invoke full source validator with inputs/coded/config. The test’s combined path is source-complete; loader alone is not.

<a id="symbol-test-artifact-manifest-model-is-strict-and-frozen"></a>
### `tests.unit.test_bess_planning_feature_policy.test_artifact_manifest_model_is_strict_and_frozen`

Source lines 657–670. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_artifact_manifest_model_is_strict_and_frozen(tmp_path: Path) -> None:
```

Write synthetic artifacts, model_validate manifest, assert versions/kind/filename, then require ValidationError on assigning parquet_row_count=0. Does not attempt every field/nested mutation or input-alias operation.

<a id="symbol-test-artifact-loader-rejects-manifest-mismatch"></a>
### `tests.unit.test_bess_planning_feature_policy.test_artifact_loader_rejects_manifest_mismatch`

Source lines 693–708. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_artifact_loader_rejects_manifest_mismatch(
    tmp_path: Path,
    mutation: object,
    message: str,
) -> None:
```

Ten parametrized callbacks mutate the manifest dict: schema 1, extra field, other basename, row count 999, byte size 999, raw SHA f*64, index_names changed, table hash f*64, complete hash f*64, or missing policy_profile. Rewrite JSON and call local loader expecting case regex. Callbacks mutate, do not spy/delegate; first failing stage varies from model to schema/hash.

Exact decorators/parameters (not extra closure units):

```python
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
```

<a id="symbol-test-artifact-loader-uses-strict-json-before-parquet-read"></a>
### `tests.unit.test_bess_planning_feature_policy.test_artifact_loader_uses_strict_json_before_parquet_read`

Source lines 721–743. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_artifact_loader_uses_strict_json_before_parquet_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
```

Four invalid manifest texts: duplicate schema key, NaN, Infinity, array. Replace pd.read_parquet with raising counted sentinel; loader raises controlled strict-JSON error and parquet_reads stays 0. This instruments decoder calls, NOT raw Parquet Path.read_bytes.

Exact decorators/parameters (not extra closure units):

```python
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
```

<a id="symbol-test-artifact-loader-uses-strict-json-before-parquet-read-counted"></a>
### `tests.unit.test_bess_planning_feature_policy.test_artifact_loader_uses_strict_json_before_parquet_read.counted`

Source lines 732–735. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
    def counted(*args: object, **kwargs: object) -> object:
```

Nested sentinel increments parquet_reads then raises AssertionError if called; no delegation or successful return despite object annotation. Parent proves zero decoder calls after invalid JSON, not a file-read count.

<a id="symbol-test-artifact-loader-rejects-parquet-replacement"></a>
### `tests.unit.test_bess_planning_feature_policy.test_artifact_loader_rejects_parquet_replacement`

Source lines 746–752. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_artifact_loader_rejects_parquet_replacement(tmp_path: Path) -> None:
```

Append b"changed-after-manifest" to actual test Parquet while retaining old manifest; local loader must reject size/SHA/hash. Size mismatch can reject first; this is pre-load byte corruption, not a mid-read race.

<a id="symbol-test-artifact-loader-parses-the-exact-verified-parquet-bytes"></a>
### `tests.unit.test_bess_planning_feature_policy.test_artifact_loader_parses_the_exact_verified_parquet_bytes`

Source lines 755–804. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_artifact_loader_parses_the_exact_verified_parquet_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Capture verified bytes, produce a different gzip Parquet, then patch Path.read_bytes to replace the path AFTER capturing original bytes. Observe read_parquet input, require replacement occurred, parsed_payloads exactly [("buffer", verified_bytes)] and frame equality. Historical _file_sha256 trap is installed with raising=False but production has no such helper. Proves captured-byte parsing, not final live-path equality or atomic fileset.

<a id="symbol-test-artifact-loader-parses-the-exact-verified-parquet-bytes-replace-after-byte-read"></a>
### `tests.unit.test_bess_planning_feature_policy.test_artifact_loader_parses_the_exact_verified_parquet_bytes.replace_after_byte_read`

Source lines 772–778. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
    def replace_after_byte_read(path: Path) -> bytes:
```

Delegate original_read_bytes first, replace only the target path once with replacement bytes, then return the initially captured payload. Counter flag tracks replacement. No source validation or post-read path check.

<a id="symbol-test-artifact-loader-parses-the-exact-verified-parquet-bytes-old-hash-then-replace"></a>
### `tests.unit.test_bess_planning_feature_policy.test_artifact_loader_parses_the_exact_verified_parquet_bytes.old_hash_then_replace`

Source lines 780–786. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
    def old_hash_then_replace(path: Path) -> str:
```

Historical trap callback would read original bytes, replace target path once, and return SHA of captured payload. Installed on nonexistent _file_sha256 via raising=False; no assertion proves it is called and current loader never calls it.

<a id="symbol-test-artifact-loader-parses-the-exact-verified-parquet-bytes-observed-read-parquet"></a>
### `tests.unit.test_bess_planning_feature_policy.test_artifact_loader_parses_the_exact_verified_parquet_bytes.observed_read_parquet`

Source lines 788–796. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
    def observed_read_parquet(
        source: object, *args: object, **kwargs: object
    ) -> object:
```

Delegating spy records buffer.getvalue for BytesIO, otherwise original bytes from the path, then returns original_read_parquet(source,*args,**kwargs). Parent asserts exactly one buffer containing initially verified bytes.

<a id="symbol-test-locally-invalid-result-fast-fails-before-source-validation"></a>
### `tests.unit.test_bess_planning_feature_policy.test_locally_invalid_result_fast_fails_before_source_validation`

Source lines 807–834. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_locally_invalid_result_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

After valid fixture setup, replace CNIG owner with no-op counter. Full validator sees object(), policy schema 2, dropped confidence column, bad table hash or bad complete hash and raises type/schema/hash/result; cumulative calls remains 0. Does not count setup source work or internal I/O.

<a id="symbol-test-locally-invalid-result-fast-fails-before-source-validation-counted"></a>
### `tests.unit.test_bess_planning_feature_policy.test_locally_invalid_result_fast_fails_before_source_validation.counted`

Source lines 814–816. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

Nested no-op counter increments calls and implicitly returns None; does not delegate or raise. Parent’s invalid-envelope loop must never reach it.

<a id="symbol-test-compiler-wrong-source-lock-fast-fails-before-source-validation"></a>
### `tests.unit.test_bess_planning_feature_policy.test_compiler_wrong_source_lock_fast_fails_before_source_validation`

Source lines 837–855. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_compiler_wrong_source_lock_fast_fails_before_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

After fixture setup, forge config document lock only, patch CNIG owner with no-op counter, public compile rejects lock/document and calls == 0. This tests lock ordering, not every lock field’s I/O behavior.

<a id="symbol-test-compiler-wrong-source-lock-fast-fails-before-source-validation-counted"></a>
### `tests.unit.test_bess_planning_feature_policy.test_compiler_wrong_source_lock_fast_fails_before_source_validation.counted`

Source lines 844–846. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

Nested no-op CNIG counter increments calls and returns None implicitly. No delegation/rejection; parent asserts it was not reached.

<a id="symbol-test-forged-matching-lock-still-runs-source-complete-validation"></a>
### `tests.unit.test_bess_planning_feature_policy.test_forged_matching_lock_still_runs_source_complete_validation`

Source lines 858–881. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_forged_matching_lock_still_runs_source_complete_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Forge coded source_document_id AND config lock.document_id to "forged-document" without resealing coded hashes/rows. The delegating CNIG spy is reached once; compiler raises Source-complete/source. That owner can reject its local lineage/hash envelope before physical reconstruction; the test proves invocation, not a completed physical rebuild or a disk-read count.

<a id="symbol-test-forged-matching-lock-still-runs-source-complete-validation-counted"></a>
### `tests.unit.test_bess_planning_feature_policy.test_forged_matching_lock_still_runs_source_complete_validation.counted`

Source lines 866–869. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

Delegating spy increments calls then invokes saved actual CNIG validator; parent expects that real owner to reject. Count is owner invocations, not disk reads.

<a id="symbol-test-compiler-and-public-validator-invoke-source-complete-coding-validation"></a>
### `tests.unit.test_bess_planning_feature_policy.test_compiler_and_public_validator_invoke_source_complete_coding_validation`

Source lines 884–905. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_compiler_and_public_validator_invoke_source_complete_coding_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Build synthetic inputs/coded/config before patch; delegating CNIG spy sees calls == 1 after public compile and calls == 2 after full validator. This is one invocation per operation, not one internal physical pass.

<a id="symbol-test-compiler-and-public-validator-invoke-source-complete-coding-validation-counted"></a>
### `tests.unit.test_bess_planning_feature_policy.test_compiler_and_public_validator_invoke_source_complete_coding_validation.counted`

Source lines 896–899. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

Delegating spy increments shared calls and executes actual(*args,**kwargs), implicitly returning None. No exception suppression or fabricated source validity.

<a id="symbol-test-public-policy-api-exports-only-stable-symbols"></a>
### `tests.unit.test_bess_planning_feature_policy.test_public_policy_api_exports_only_stable_symbols`

Source lines 908–924. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_public_policy_api_exports_only_stable_symbols() -> None:
```

Assert module __all__ equals exact nine-name set, package includes those names with identical objects, and _canonical_sha256/_lookup are not in module exports. Does not test default arguments or prohibit every private importable name.

<a id="symbol-test-step-7d-5b-2b-5-exposes-lightweight-policy-result-validator"></a>
### `tests.unit.test_bess_planning_feature_policy.test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator`

Source lines 927–935. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_step_7d_5b_2b_5_exposes_lightweight_policy_result_validator() -> None:
```

Assert envelope API exists, accept valid fixture locally, replace complete hash with 64 zeroes and expect hash error. No source-owner call-count instrumentation in this test.

<a id="symbol-test-policy-manifest-rejects-nonportable-parquet-filename"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_manifest_rejects_nonportable_parquet_filename`

Source lines 977–985. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_manifest_rejects_nonportable_parquet_filename(
    tmp_path: Path, filename: str
) -> None:
```

34 parametrized absolute/traversal/separator/Windows-device/colon/forbidden/control-character names replace manifest basename. Model validation must raise ValueError filename/basename/portable; Pydantic ValidationError is a ValueError subclass. No loader containment or symlink test.

Exact decorators/parameters (not extra closure units):

```python
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
```

<a id="symbol-test-shared-filename-contract-rejects-superscript-windows-devices"></a>
### `tests.unit.test_bess_planning_feature_policy.test_shared_filename_contract_rejects_superscript_windows_devices`

Source lines 999–1003. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_shared_filename_contract_rejects_superscript_windows_devices(
    filename: str,
) -> None:
```

Six mixed-case COM/LPT superscript 1/2/3 basenames directly hit common portable-name guard and expect ValueError reserved/basename/portable. No artifact reads.

Exact decorators/parameters (not extra closure units):

```python
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
```

<a id="symbol-test-policy-manifest-rejects-unsupported-cnig-source-schema"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_manifest_rejects_unsupported_cnig_source_schema`

Source lines 1020–1030. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_manifest_rejects_unsupported_cnig_source_schema(
    tmp_path: Path,
    field: str,
    version: int,
) -> None:
```

Nine invalid CNIG profile/result version assignments to manifest dict; model_validate raises ValidationError CNIG/cnig/schema/version. Exact supported versions are 2/5; result version 2 is not among these nine cases.

Exact decorators/parameters (not extra closure units):

```python
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
```

<a id="symbol-test-policy-artifact-loader-rejects-source-schema-before-parquet-read"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_artifact_loader_rejects_source_schema_before_parquet_read`

Source lines 1047–1080. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_artifact_loader_rejects_source_schema_before_parquet_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    field: str,
    version: int,
) -> None:
```

Same nine unsupported source-version JSON mutations. Path.read_bytes spy permits manifest but counts/raises on Parquet, and pd.read_parquet sentinel counts/raises. Local loader rejects with controlled schema error and calls == {"bytes":0,"parse":0}. Unlike strict-JSON test, both raw read and parser are instrumented.

Exact decorators/parameters (not extra closure units):

```python
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
```

<a id="symbol-test-policy-artifact-loader-rejects-source-schema-before-parquet-read-byte-read"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_artifact_loader_rejects_source_schema_before_parquet_read.byte_read`

Source lines 1063–1067. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
    def byte_read(path: Path, *args: object, **kwargs: object) -> bytes:
```

For target Parquet increment calls["bytes"] and raise AssertionError; for other paths delegate original_read_bytes. Thus manifest reads remain real, target data read must not occur.

<a id="symbol-test-policy-artifact-loader-rejects-source-schema-before-parquet-read-parse"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_artifact_loader_rejects_source_schema_before_parquet_read.parse`

Source lines 1069–1071. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
    def parse(*args: object, **kwargs: object) -> pd.DataFrame:
```

Always increment calls["parse"] and raise AssertionError, no delegation or successful DataFrame return. Parent requires zero calls.

<a id="symbol--rehash-policy-table"></a>
### `tests.unit.test_bess_planning_feature_policy._rehash_policy_table`

Source lines 1083–1087. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def _rehash_policy_table(
    result: BessPlanningFeaturePolicyResult, table: pd.DataFrame
) -> BessPlanningFeaturePolicyResult:
```

Replace result table reference and call private _result_with_hashes; return newly sealed envelope, sharing supplied mutable table. No intrinsic or source validation, no I/O.

<a id="symbol--canonical-empty-policy-result"></a>
### `tests.unit.test_bess_planning_feature_policy._canonical_empty_policy_result`

Source lines 1090–1095. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def _canonical_empty_policy_result(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
```

Take copied zero-row slice preserving columns/dtypes, assign empty plain int64 Index, then privately reseal. Returns syntactically coherent empty table result for the nonempty regression, not a valid policy.

<a id="symbol-test-policy-envelope-rejects-canonical-empty-policy-table"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_envelope_rejects_canonical_empty_policy_table`

Source lines 1098–1105. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_envelope_rejects_canonical_empty_policy_table() -> None:
```

Build typed zero-row/resealed result using helper and require public envelope policy/table/empty/entry error. Empty guard, not stale hash or changed schema, is targeted.

<a id="symbol-test-policy-envelope-accepts-one-exact-policy-row"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_envelope_accepts_one_exact_policy_row`

Source lines 1108–1114. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_envelope_accepts_one_exact_policy_row() -> None:
```

Copy first row, assign plain int64 index [0], reseal hashes and require local public envelope success. Does not call full validator; acceptance proves local coherence, not dictionary completeness.

<a id="symbol-test-policy-envelope-accepts-current-twelve-row-snapshot"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_envelope_accepts_current_twelve_row_snapshot`

Source lines 1117–1121. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_envelope_accepts_current_twelve_row_snapshot() -> None:
```

Use private checked-in reconstruction, assert 12 rows and local envelope success. No source-complete physical Muret validation.

<a id="symbol-test-policy-envelope-requires-cnig-profile-schema-two"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_envelope_requires_cnig_profile_schema_two`

Source lines 1125–1132. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_envelope_requires_cnig_profile_schema_two(version: int) -> None:
```

For versions 0,1,3,999 replace CNIG profile version, reseal hashes and expect public envelope schema error. Coherent hashes cannot permit unsupported versions.

Exact decorators/parameters (not extra closure units):

```python
@pytest.mark.parametrize("version", [0, 1, 3, 999])
```

<a id="symbol-test-policy-envelope-requires-cnig-result-schema-five"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_envelope_requires_cnig_result_schema_five`

Source lines 1136–1143. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_envelope_requires_cnig_result_schema_five(version: int) -> None:
```

For versions 0,1,2,4,6,999 replace CNIG result version, reseal hashes and expect public envelope CNIG result/schema error.

Exact decorators/parameters (not extra closure units):

```python
@pytest.mark.parametrize("version", [0, 1, 2, 4, 6, 999])
```

<a id="symbol-test-policy-envelope-validates-every-intrinsic-row-contract"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_envelope_validates_every_intrinsic_row_contract`

Source lines 1168–1222. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_envelope_validates_every_intrinsic_row_contract(
    mutation: str,
) -> None:
```

Seventeen copied-table/resealed mutations: duplicate triple at distinct indices; reverse row order; type_code="1"; AUTHORIZED status; CERTAIN confidence; zero/negative priority; bool priority using object dtype; one status/two priorities; two statuses/one priority; OTHER_SCOPE; local_feature_text_interpreted=True; policy SHA a*64; other CNIG profile; CNIG profile SHA a*64; CNIG result SHA a*64; legal reference "None". Broad policy/pair/order/code/status/confidence/priority/scope/flag/CNIG/null/schema regex permits different first guards. The bool case fails schema before row priority type; name does not prove exhaustive intrinsic coverage.

Exact decorators/parameters (not extra closure units):

```python
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
```

<a id="symbol-test-policy-envelope-requires-exact-type-and-accepts-valid-schema-v1"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1`

Source lines 1225–1235. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1() -> None:
```

Construct a DerivedPolicyResult subclass using valid result.__dict__, require public envelope type/result rejection, then accept the exact base instance. Tests exact-type boundary, not runtime validation on dataclass construction.

<a id="symbol-test-policy-envelope-requires-exact-type-and-accepts-valid-schema-v1-derivedpolicyresult"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_envelope_requires_exact_type_and_accepts_valid_schema_v1.DerivedPolicyResult`

Source lines 1229–1230. Kind: class. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
    class DerivedPolicyResult(BessPlanningFeaturePolicyResult):
```

Empty nested subclass of result dataclass, constructed only to prove exact-type rejection. No methods, fields, I/O or independent validation.

<a id="symbol-test-policy-envelope-controls-malformed-result-type"></a>
### `tests.unit.test_bess_planning_feature_policy.test_policy_envelope_controls_malformed_result_type`

Source lines 1239–1242. Kind: function. Owner: `tests.unit.test_bess_planning_feature_policy`.

```python
def test_policy_envelope_controls_malformed_result_type(malformed: object) -> None:
```

Parametrized None and object() must raise controlled BessPlanningFeaturePolicyError at public envelope. No injected unexpected exception or broad-wrapper branch is independently instrumented.

Exact decorators/parameters (not extra closure units):

```python
@pytest.mark.parametrize("malformed", [None, object()])
```

## Complete source snapshot

Exact full Git-content UTF-8 snapshot, not evidence that the prose is correct by itself.

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
