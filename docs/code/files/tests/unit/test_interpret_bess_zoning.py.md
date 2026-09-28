# `tests/unit/test_interpret_bess_zoning.py`

- Source: [tests/unit/test_interpret_bess_zoning.py](../../../../../tests/unit/test_interpret_bess_zoning.py)
- Source SHA256: `e5ad284bb61a67a348377ad4d68092c4425c16eb13519c6440a0c52de70b70d3`
- Source SHA256 basis: `git-content`
- Source lines: 2164; Git blob at R11 start: `657b77322a3b110fba8559d8f556212bcaaf6e69`

Git/index/checkout Python bytes remain unchanged. Local semantic closure is not independent approval. [R11 receipt](../../../../../docs/code/audit/R11_BESS_WRITTEN_ZONING.md).

## Evidence scope and fixture ownership

This suite has 79 top-level tests, two pytest fixtures and 96 original inventoried symbols including helpers and five nested callbacks. Executed case count belongs to the R11 receipt, not these static counts. Tests return None on success; assertions/pytest.raises fail otherwise. Literal signatures distinguish missing annotation from -> None. No test-module __all__ or public production API is declared.

The module-level importlib.import_module assignment actually imports the interpreter for monkeypatch access. Standard library also supplies replace/SHA/Path. Pandas/GeoPandas construct frames and read/write synthetic Parquet; Shapely builds polygons; pytest provides fixtures/parameters/errors; YAML is imported locally in roundtrip test. The _structure_with_hashes alias belongs to structure_planning_regulation, not the similarly named interpreter helper. Both private helpers reseal in-memory outputs without proving them authoritative.

_index constructs three literal synthetic pages with repeated text; it does not extract a PDF. _zones is a plain DataFrame, _relations six declared rows, _parcels four polygons. inputs replaces the interpreter's GPU gate by a no-op and uses object() for planning_document. Structure/fragments are genuinely rebuilt from those in-memory texts. valid_result returns a result object, not None. Tests repatching gates are described individually. There is no physical GPU integration fixture in this file; no integration suite was run/read for R11.

Four tests named real_muret load checked-in YAML and assert configured words/IDs/offsets/hashes; none reopen the original PDF/GPU cache. Temporary YAML writes and seven-Parquet roundtrip are real local I/O over synthetic fixtures, not production artifacts or a module writer/manifest API. [Interpreter](../../src/landscout/stages/interpret_bess_zoning.py.md) describes the actual public source gate and reconstruction separately.

Proof limits retained without repairing source/tests:

- R11-T01: no-op/counter GPU gate and raising sentinel prove invocation/order, not physical validation or disk-read counts. Delegating structure spies prove their own call bounds.
- R11-T02: distinct-offset model test only model-validates; later exact-occurrence tests separately exercise synthetic fragment slices.
- R11-T03: several negative cases can fail earlier structure hashes/chapter coherence or component-hash comparisons before a named later guard. Notices identify the actual message/absence of message constraints. Rehashed outputs are not necessarily validated through every semantic subguard.
- R11-T04: test_zoning_relation_and_zone_mapping_changes_are_rejected changes relation values only, not mapping.
- R11-T05: test_factual_zone_mapping_counts_are_recomputed receives only inputs. Its second call passes the global valid_result fixture function, not a fixture-created result; earlier bad-structure rejection and broad raises limit that arm's evidence.

These are bounded proof limitations, not automatically new application backlog defects. No claim of exhaustive malformed-input/immutability/physical-source/legal coverage is made. Existing A-001..A-004 and other historical reservations remain as recorded in current state. Every notice below follows the exact scenario, not the words of its title; full source/decorators preserve precise literals and expected exceptions.

## Module declarations

Exact imports are preserved in the full snapshot. These constants/aliases add no extra closure units.

<a id="declaration-interpret-module"></a>
### `tests.unit.test_interpret_bess_zoning.interpret_module`

Source lines 14–14. Module object obtained by actual importlib.import_module call; used to patch/call interpreter attributes. Not an inert constant or additional export.

```python
interpret_module = importlib.import_module("landscout.stages.interpret_bess_zoning")
```

## Qualified symbol contracts

Every original symbol has one notice and a matching owner note. Exact signatures specify all parameters/types/defaults; missing annotations are not None annotations. For fields, Field constraints without a supplied value do not create defaults. Private lookup/third-party exceptions propagate unless an explicit wrapper is described. Full implementations and imports appear once below.

<a id="symbol--index"></a>
### `tests.unit.test_interpret_bess_zoning._index`

Source lines 51–98. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def _index() -> PlanningRegulationIndex:
```

Construct three synthetic raw-text pages, including a repeated conditional sentence on page 2; normalize search text and compute page/pages/index hashes with index-owner helpers. Return replaced PlanningRegulationIndex, no PDF extraction/read. Archive a*64, PDF c*64 and metadata are synthetic.

<a id="symbol--zones"></a>
### `tests.unit.test_interpret_bess_zoning._zones`

Source lines 101–111. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def _zones(index: PlanningRegulationIndex) -> pd.DataFrame:
```

Return plain six-column DataFrame of ZONE-U/ZONE-UA/ZONE-N and SRC-U/SRC-UA/SRC-N, raw labels U/Ua/N and index lineage, layer ZONE. No geometry or physical source.

<a id="symbol--relations"></a>
### `tests.unit.test_interpret_bess_zoning._relations`

Source lines 114–150. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def _relations(index: PlanningRegulationIndex) -> pd.DataFrame:
```

Return six synthetic relation rows: five positive and P-4/N touch; area/share values 100,60,40,60,40,0 with 100 m2 parcel and 1000 m2 zone denominators, zone percent area/10. No overlay is run.

<a id="symbol--structure-config"></a>
### `tests.unit.test_interpret_bess_zoning._structure_config`

Source lines 153–190. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def _structure_config(
    index: PlanningRegulationIndex,
) -> PlanningRegulationStructureConfig:
```

Return schema-2 synthetic frozen structure config locked to index, body page 1/no TOC, explicit heading regexes, Ua->U alias, technical-equipment token and 20-character context. No checked-in Muret source used.

<a id="symbol--parcels"></a>
### `tests.unit.test_interpret_bess_zoning._parcels`

Source lines 193–216. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def _parcels(index: PlanningRegulationIndex) -> gpd.GeoDataFrame:
```

Return four 10-by-10 synthetic polygons in EPSG:2154 with named source_row index 10/20/30/40, dominant U/U/U/None, five feature counts, document/archive pairs and prior_fact. These are inputs, not results of a physical GPU overlay.

<a id="symbol--policy"></a>
### `tests.unit.test_interpret_bess_zoning._policy`

Source lines 219–367. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def _policy(index, structure, config, zones, relations) -> BessZoningPolicyConfig:
```

Use validated synthetic section/page fragments and first U/N article 1; declare required articles 1 and 2, U conditional positive+condition route and N difficulty-only route with configured confidence MEDIUM/HIGH. Return schema-5 policy with synthetic six-field lock. Invokes nested evidence helper; no PDF read.

<a id="symbol--policy-evidence"></a>
### `tests.unit.test_interpret_bess_zoning._policy.evidence`

Source lines 236–268. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
    def evidence(
        evidence_id: str,
        section_id: str,
        page_number: int,
        kind: str,
        direction: str,
        excerpt: str,
        source_rule_id: str,
        source_rule: str,
        note: str,
    ) -> dict[str, object]:
```

Closure over fragments; locate full rule via raw.index then quote via raw.index within its bounds. Return mutable dict with supplied IDs/kind/direction/note, zero-based half-open offsets and UTF-8 quote/rule hashes plus fragment hash. Lookup/index exceptions unwrapped. Called only by _policy, not a production owner.

<a id="symbol-inputs"></a>
### `tests.unit.test_interpret_bess_zoning.inputs`

Source lines 371–394. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def inputs(monkeypatch):
```

Pytest fixture monkeypatches interpreter validate_normalized_planning_zoning_inputs to lambda *args: None. Builds synthetic index/zones/relations/config/structure/parcels/policy, planning_document=object(), returns EIGHT-item tuple in public API order. No return annotation, not a None-returning fixture; physical GPU guard bypassed throughout dependent tests unless explicitly repatched.

Exact decorators (not extra units):

```python
@pytest.fixture
```

<a id="symbol-valid-result"></a>
### `tests.unit.test_interpret_bess_zoning.valid_result`

Source lines 398–399. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def valid_result(inputs):
```

Pytest fixture returns interpret_bess_zoning(*inputs), a BessZoningPrecheckResult. Unannotated, not None. Uses inputs GPU bypass.

Exact decorators (not extra units):

```python
@pytest.fixture
```

<a id="symbol--payload"></a>
### `tests.unit.test_interpret_bess_zoning._payload`

Source lines 402–403. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def _payload(policy: BessZoningPolicyConfig) -> dict[str, object]:
```

Return fresh policy.model_dump(mode="python") dict for test editing; tuple containers remain tuples, nested model dictionaries can be changed without modifying frozen original policy.

<a id="symbol--policy-with-context-only-evidence"></a>
### `tests.unit.test_interpret_bess_zoning._policy_with_context_only_evidence`

Source lines 406–416. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def _policy_with_context_only_evidence(
    policy: BessZoningPolicyConfig,
) -> BessZoningPolicyConfig:
```

On dumped payload make U condition CONTEXT_ONLY, route DIRECT_ROUTE with empty condition IDs, status POTENTIALLY_COMPATIBLE; return revalidated policy. Does not mutate retained input model.

<a id="symbol--validate"></a>
### `tests.unit.test_interpret_bess_zoning._validate`

Source lines 419–420. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def _validate(inputs, result) -> None:
```

Call public nine-input validator with *inputs then result; return None, exceptions propagate to test.

<a id="symbol-test-package-exports-precheck-api"></a>
### `tests.unit.test_interpret_bess_zoning.test_package_exports_precheck_api`

Source lines 423–434. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_package_exports_precheck_api() -> None:
```

Assert eight listed names occur in stages.__all__: six interpreter exports plus two structure-fragment functions. Does not call any API or prove behavioral identity.

<a id="symbol-test-valid-locked-policy-builds-complete-outputs"></a>
### `tests.unit.test_interpret_bess_zoning.test_valid_locked_policy_builds_complete_outputs`

Source lines 437–470. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_valid_locked_policy_builds_complete_outputs(inputs, valid_result) -> None:
```

Build and publicly validate synthetic result; assert the six ordered non-parcel table schemas, including evidence_catalog, chapter/source/positive/parcel counts 2/3/5/4, versions 5/5, scopes, two routes/three links, touch count 1, selected lineage/profile, relation column tuple and source-label set. GPU gate bypassed; not a real-source run.

<a id="symbol-test-source-lock-mismatch-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_source_lock_mismatch_is_rejected`

Source lines 484–490. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_source_lock_mismatch_is_rejected(inputs, field: str) -> None:
```

Six parametrized lock fields changed to f*64 or wrong; model remains valid, interpreter must raise message differs from factual source. Physical guard bypassed; this isolates lock mismatch after structure validation.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    "field",
    [
        "document_id",
        "archive_sha256",
        "pdf_sha256",
        "index_content_sha256",
        "structure_result_content_sha256",
        "structure_profile",
    ],
)
```

<a id="symbol-test-missing-and-extra-chapter-are-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_missing_and_extra_chapter_are_rejected`

Source lines 493–511. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_missing_and_extra_chapter_are_rejected(inputs) -> None:
```

Remove last chapter; separately append EXTRA with empty evidence/routes and UNKNOWN; interpreter rejects completeness or extra EXTRA against synthetic structure. No policy hashes resealed manually.

<a id="symbol-test-regulation-zone-chapter-labels-and-ids-must-be-unique"></a>
### `tests.unit.test_interpret_bess_zoning.test_regulation_zone_chapter_labels_and_ids_must_be_unique`

Source lines 514–565. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_regulation_zone_chapter_labels_and_ids_must_be_unique(inputs) -> None:
```

Direct _zone_chapter_rows call: baseline two; duplicate used U label with new ID, two unused X labels, then new X label reusing N section ID. Assert corresponding uniqueness messages. No full public or physical validation.

<a id="symbol-test-source-complete-validator-rejects-later-duplicate-chapter"></a>
### `tests.unit.test_interpret_bess_zoning.test_source_complete_validator_rejects_later_duplicate_chapter`

Source lines 568–597. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_source_complete_validator_rejects_later_duplicate_chapter(
    inputs, valid_result
) -> None:
```

Append first chapter section with new SECTION-LATE-DUPLICATE ID to result structure without resealing its hashes; public validation raises BessZoningPrecheckError (no match). Upstream structure checks can reject first; not isolation of the interpreter duplicate-label guard.

<a id="symbol-test-duplicate-chapter-and-evidence-id-are-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_duplicate_chapter_and_evidence_id_are_rejected`

Source lines 600–612. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_duplicate_chapter_and_evidence_id_are_rejected(inputs) -> None:
```

Append same chapter to policy payload then independently reuse E-U-POSITIVE as N evidence ID; model_validate rejects chapter-label and global-evidence-ID duplicates by message.

<a id="symbol-test-one-excerpt-cannot-be-reused-with-contradictory-directions"></a>
### `tests.unit.test_interpret_bess_zoning.test_one_excerpt_cannot_be_reused_with_contradictory_directions`

Source lines 615–624. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_one_excerpt_cannot_be_reused_with_contradictory_directions(inputs) -> None:
```

Duplicate the U condition occurrence with new evidence ID and positive/difficulty directions; root model rejects chapter-scoped occurrence. This is occurrence identity, not a general prohibition on identical text at distinct offsets.

<a id="symbol-test-duplicate-chapter-scoped-occurrence-in-one-route-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected`

Source lines 627–641. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected(inputs) -> None:
```

Clone U positive under E-U-POSITIVE-DUPLICATE and reference both positive IDs in same route; expect chapter-scoped occurrence error during model validation.

<a id="symbol-test-duplicate-occurrence-in-different-compatible-routes-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_duplicate_occurrence_in_different_compatible_routes_is_rejected`

Source lines 644–667. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_duplicate_occurrence_in_different_compatible_routes_is_rejected(
    inputs,
) -> None:
```

Clone N occurrence under new evidence ID, add second difficulty route referring to clone; root occurrence guard rejects despite compatible routes.

<a id="symbol-test-forbidden-or-invalid-final-status-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_forbidden_or_invalid_final_status_is_rejected`

Source lines 671–675. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_forbidden_or_invalid_final_status_is_rejected(inputs, status: str) -> None:
```

Parametrize ALLOWED/FORBIDDEN/PROHIBITED in U chapter status; model_validate must raise ValueError. Literal-domain rejection, not legal adjudication.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize("status", ["ALLOWED", "FORBIDDEN", "PROHIBITED"])
```

<a id="symbol-test-invalid-confidence-and-unknown-field-are-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_invalid_confidence_and_unknown_field_are_rejected`

Source lines 678–686. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_invalid_confidence_and_unknown_field_are_rejected(inputs) -> None:
```

Separate payloads set confidence CERTAIN and add automatic_classifier=True at root; both model_validate calls raise ValueError, proving these domain/extra-field cases.

<a id="symbol-test-duplicate-yaml-key-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_duplicate_yaml_key_is_rejected`

Source lines 689–696. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
```

Write temporary UTF-8 YAML with schema_version: 2 twice; loader raises duplicate-key message before unsupported schema handling. No official file changed.

<a id="symbol-test-old-policy-schema-versions-are-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_old_policy_schema_versions_are_rejected`

Source lines 700–704. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_old_policy_schema_versions_are_rejected(inputs, version: int) -> None:
```

Set schema to each 1,2,3,4; model_validate raises unsupported BESS zoning policy schema. Does not test every non-integer input.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize("version", [1, 2, 3, 4])
```

<a id="symbol-test-every-evidence-kind-has-an-explicit-direction-matrix"></a>
### `tests.unit.test_interpret_bess_zoning.test_every_evidence_kind_has_an_explicit_direction_matrix`

Source lines 707–766. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_every_evidence_kind_has_an_explicit_direction_matrix(inputs) -> None:
```

For all eight kinds by four directions, validate one standalone PolicyEvidence: allowed pairs succeed, others raise kind/direction message. This tests 32 pairs inside one test, not routes or source fragments.

<a id="symbol-test-valid-exact-evidence-is-preserved"></a>
### `tests.unit.test_interpret_bess_zoning.test_valid_exact_evidence_is_preserved`

Source lines 769–785. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_valid_exact_evidence_is_preserved(inputs, valid_result) -> None:
```

Assert U positive exact text and SHA, two ordered chapter evidence IDs; catalog full rule contains only when and its relative slice equals quote. Synthetic retained text, not external PDF verification.

<a id="symbol-test-source-rule-identity-and-containment-are-strict"></a>
### `tests.unit.test_interpret_bess_zoning.test_source_rule_identity_and_containment_are_strict`

Source lines 789–812. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_source_rule_identity_and_containment_are_strict(inputs, mutation: str) -> None:
```

Four cases: f*64 rule hash and start beyond quote fail model hash/containment; changing both related U rule starts -1 or ends +1 keeps declaration identity coherent but interpreter rejects actual source-rule offsets. Branch-specific messages separate model and fragment checks.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize("mutation", ["hash", "start", "end", "outside"])
```

<a id="symbol-test-same-rule-text-at-distinct-offsets-has-distinct-identity"></a>
### `tests.unit.test_interpret_bess_zoning.test_same_rule_text_at_distinct_offsets_has_distinct_identity`

Source lines 815–843. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_same_rule_text_at_distinct_offsets_has_distinct_identity(inputs) -> None:
```

Clone positive text to second rule occurrence with new IDs, shifted four offsets, technical/difficulty direction and extra difficulty route; model_validate succeeds and last direction asserted. No interpret call proving that second fragment slice; boundary is model coherence only (R11-T02).

<a id="symbol-test-real-muret-source-rules-preserve-conditional-and-exception-frames"></a>
### `tests.unit.test_interpret_bess_zoning.test_real_muret_source_rules_preserve_conditional_and_exception_frames`

Source lines 846–884. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_real_muret_source_rules_preserve_conditional_and_exception_frames() -> None:
```

Load checked-in YAML only. Assert conditional wording for UA/UB/UC/UD/UF/AU/AUf; exclusion wording UP/AUp; prohibition frame AU0/AUf0/A/N; A/N difficulty and positive share rule ID/text. Does not reopen PDF or validate GPU/Muret cache.

<a id="symbol-test-real-muret-up-route-does-not-use-the-separate-icpe-condition"></a>
### `tests.unit.test_interpret_bess_zoning.test_real_muret_up_route_does_not_use_the_separate_icpe_condition`

Source lines 887–929. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_real_muret_up_route_does_not_use_the_separate_icpe_condition() -> None:
```

Load YAML; assert version5/profile v6, UP restriction-exception route with exact positive/difficulty IDs and empty condition tuple. Pin restriction kind/direction SECTION-0080 page71, exact quote, [68:124], quote/fragment SHA, rule ID/[68:236]/SHA. No independent source text extraction.

<a id="symbol-test-real-muret-aup-route-uses-the-general-infrastructure-prerequisite"></a>
### `tests.unit.test_interpret_bess_zoning.test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite`

Source lines 932–975. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite() -> None:
```

Load YAML; assert AUp conditional route positive/infrastructure-condition IDs and empty difficulty. Pin prerequisite ACCESS_OR_NETWORK_CONDITION/CONDITION, SECTION-0111 page93, exact multiline infrastructure rule, [98:325], quote/fragment SHA, rule ID/text/range and rule SHA=quote SHA. Not a physical source read or BESS permission.

<a id="symbol-test-real-muret-up-and-aup-keep-icpe-applicability-as-context"></a>
### `tests.unit.test_interpret_bess_zoning.test_real_muret_up_and_aup_keep_icpe_applicability_as_context`

Source lines 978–1004. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_real_muret_up_and_aup_keep_icpe_applicability_as_context() -> None:
```

Load YAML; for UP/AUp ICPE IDs assert ICPE_RULE/CONTEXT_ONLY, ICPE in missing_information and absence from all route role tuples. Does not prove BESS is or is not ICPE.

<a id="symbol-test-absent-excerpt-and-section-page-mismatch-are-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_absent_excerpt_and_section_page_mismatch_are_rejected`

Source lines 1007–1021. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_absent_excerpt_and_section_page_mismatch_are_rejected(inputs) -> None:
```

Replace U quote with absent text and recompute quote SHA (offsets unchanged); interpreter rejects offsets. Separate payload changes both U evidence pages to3; rejects missing section/page fragment. No source-rule hash modification.

<a id="symbol-test-excerpt-hash-and-length-are-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_excerpt_hash_and_length_are_rejected`

Source lines 1024–1036. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_excerpt_hash_and_length_are_rejected(inputs) -> None:
```

Set quote SHA f*64, expect excerpt SHA mismatch; separately set 601-character quote and its correct SHA, expect ValueError from model. Not a long full-rule rejection.

<a id="symbol-test-declared-status-must-equal-derived-route-status"></a>
### `tests.unit.test_interpret_bess_zoning.test_declared_status_must_equal_derived_route_status`

Source lines 1042–1046. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_declared_status_must_equal_derived_route_status(inputs, status: str) -> None:
```

For potential/difficult/unknown declared U statuses leave conditional route intact; require model error differs from coherent linked route.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    "status", ["POTENTIALLY_COMPATIBLE", "LIKELY_DIFFICULT", "UNKNOWN"]
)
```

<a id="symbol-test-condition-alone-cannot-create-conditional-review"></a>
### `tests.unit.test_interpret_bess_zoning.test_condition_alone_cannot_create_conditional_review`

Source lines 1049–1055. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_condition_alone_cannot_create_conditional_review(inputs) -> None:
```

Keep only condition evidence, remove routes but retain CONDITIONAL_REVIEW; model fails chapter derived-status check. Does not isolate later root orphan-evidence guard (R11-T03).

<a id="symbol-test-unrelated-positive-and-condition-do-not-create-conditional-review"></a>
### `tests.unit.test_interpret_bess_zoning.test_unrelated_positive_and_condition_do_not_create_conditional_review`

Source lines 1058–1075. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_unrelated_positive_and_condition_do_not_create_conditional_review(
    inputs,
) -> None:
```

Replace U route with direct positive-only route but leave condition unlinked and status conditional; coherent|linked route error can arise at chapter status before orphan check. No proof of natural-language relationship detection (R11-T03).

<a id="symbol-test-unlinked-context-only-unknown-succeeds"></a>
### `tests.unit.test_interpret_bess_zoning.test_unlinked_context_only_unknown_succeeds`

Source lines 1078–1087. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_unlinked_context_only_unknown_succeeds(inputs) -> None:
```

Keep only U condition as CONTEXT_ONLY, empty routes, UNKNOWN/LOW; model succeeds and UNKNOWN asserted. No result tables built.

<a id="symbol-test-positive-condition-and-conflict-status-routes"></a>
### `tests.unit.test_interpret_bess_zoning.test_positive_condition_and_conflict_status_routes`

Source lines 1090–1105. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_positive_condition_and_conflict_status_routes(inputs) -> None:
```

Assert baseline conditional model, then convert U condition to difficulty and same route to restriction-exception with no condition IDs; status remains conditional. Coherent explicit linked routes, not arbitrary independent evidence union.

<a id="symbol-test-route-references-must-be-same-chapter-and-role-compatible"></a>
### `tests.unit.test_interpret_bess_zoning.test_route_references_must_be_same_chapter_and_role_compatible`

Source lines 1108–1126. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_route_references_must_be_same_chapter_and_role_compatible(inputs) -> None:
```

Loop unknown condition ID, other-chapter N ID, wrong positive role using E-U-CONDITION; adjust route/status coherently for last case. Model must match unknown/another-chapter or incompatible positive-role messages.

<a id="symbol-test-route-ids-are-globally-unique"></a>
### `tests.unit.test_interpret_bess_zoning.test_route_ids_are_globally_unique`

Source lines 1129–1135. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_route_ids_are_globally_unique(inputs) -> None:
```

Copy U route ID into N route; model_validate fails global route-ID uniqueness.

<a id="symbol-test-unlinked-difficulty-evidence-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_unlinked_difficulty_evidence_is_rejected`

Source lines 1138–1156. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_unlinked_difficulty_evidence_is_rejected(inputs) -> None:
```

Append N difficulty clone with new evidence/rule IDs and all four offsets +100, without route link. Model rejects orphan decision evidence; it does not validate invented fragment offsets.

<a id="symbol-test-unlinked-positive-and-condition-evidence-are-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_unlinked_positive_and_condition_evidence_are_rejected`

Source lines 1159–1180. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_unlinked_positive_and_condition_evidence_are_rejected(inputs) -> None:
```

For both U positive/condition clones use new IDs and four offsets +100 without links; root decision-evidence message required. Not source occurrence validity tests.

<a id="symbol-test-context-only-evidence-must-be-unlinked"></a>
### `tests.unit.test_interpret_bess_zoning.test_context_only_evidence_must_be_unlinked`

Source lines 1183–1194. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_context_only_evidence_must_be_unlinked(inputs) -> None:
```

Helper gives valid context-only model; assert direction, then reattach it as condition and restore conditional kind/status; model raises ValueError. Role/direction incompatibility may reject before explicit context-unlinked guard (R11-T03).

<a id="symbol-test-one-evidence-may-link-to-multiple-compatible-routes"></a>
### `tests.unit.test_interpret_bess_zoning.test_one_evidence_may_link_to_multiple_compatible_routes`

Source lines 1197–1213. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_one_evidence_may_link_to_multiple_compatible_routes(inputs) -> None:
```

Append second N difficulty route using SAME evidence ID (no duplicate evidence occurrence); interpret and assert sorted two route IDs and two DIFFICULTY reverse roles.

<a id="symbol-test-difficulty-and-positive-only-status-routes"></a>
### `tests.unit.test_interpret_bess_zoning.test_difficulty_and_positive_only_status_routes`

Source lines 1216–1257. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_difficulty_and_positive_only_status_routes(inputs) -> None:
```

Two independent payloads keep U difficulty-only or positive-only evidence, coherent route kind/IDs and declared difficult/potential status. Model validation and status assertions only.

<a id="symbol-test-incomplete-review-requires-unknown-low"></a>
### `tests.unit.test_interpret_bess_zoning.test_incomplete_review_requires_unknown_low`

Source lines 1260–1287. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_incomplete_review_requires_unknown_low(inputs) -> None:
```

Make U incomplete, empty reviewed/evidence/routes and UNKNOWN/LOW; assert completeness accepted. Independently change status conditional or confidence medium and expect incomplete-review error.

<a id="symbol-test-incomplete-review-persists-exact-missing-required-sections"></a>
### `tests.unit.test_interpret_bess_zoning.test_incomplete_review_persists_exact_missing_required_sections`

Source lines 1290–1315. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_incomplete_review_persists_exact_missing_required_sections(inputs) -> None:
```

Build incomplete U with empty reviewed/evidence/routes UNKNOWN/LOW; assert empty reviewed tuple, exact U article-ID tuple in missing_required_section_ids and status/confidence. Physical required articles still exist in synthetic structure.

<a id="symbol-test-unknown-is-accepted-when-evidence-is-insufficient"></a>
### `tests.unit.test_interpret_bess_zoning.test_unknown_is_accepted_when_evidence_is_insufficient`

Source lines 1318–1327. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_unknown_is_accepted_when_evidence_is_insufficient(inputs) -> None:
```

Remove U evidence/routes and set UNKNOWN, keeping COMPLETE review and configured MEDIUM confidence; interpreter returns UNKNOWN. Does not impose LOW on every unknown status.

<a id="symbol-test-reviewed-sections-cover-required-articles"></a>
### `tests.unit.test_interpret_bess_zoning.test_reviewed_sections_cover_required_articles`

Source lines 1330–1342. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_reviewed_sections_cover_required_articles(inputs) -> None:
```

Set reviewed IDs only to U chapter header while required articles remain1/2; interpreter must reject omits required reviewed. Additional doc-1 assert is synthetic identity only.

<a id="symbol-test-every-configured-article-must-exist-once-in-every-chapter"></a>
### `tests.unit.test_interpret_bess_zoning.test_every_configured_article_must_exist_once_in_every_chapter`

Source lines 1346–1363. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_every_configured_article_must_exist_once_in_every_chapter(
    inputs,
    article_number: str,
) -> None:
```

For article1 and2 remove matching U ARTICLE from copied sections; directly call _required_section_ids_by_chapter and require exactly-one-article error. Not full public reconstruction or all-chapter parametrization.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize("article_number", ["1", "2"])
```

<a id="symbol-test-duplicate-configured-article-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_duplicate_configured_article_is_rejected`

Source lines 1366–1386. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_duplicate_configured_article_is_rejected(inputs) -> None:
```

Append U article2 under new section ID; direct required-section helper rejects exactly-one-article count.

<a id="symbol-test-configured-article-with-wrong-chapter-parent-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_configured_article_with_wrong_chapter_parent_is_rejected`

Source lines 1389–1406. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_configured_article_with_wrong_chapter_parent_is_rejected(inputs) -> None:
```

Change U article2 parent to N chapter ID on copy; direct required-section helper finds zero correctly parented matches and rejects.

<a id="symbol-test-evidence-must-be-inside-reviewed-sections"></a>
### `tests.unit.test_interpret_bess_zoning.test_evidence_must_be_inside_reviewed_sections`

Source lines 1409–1427. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_evidence_must_be_inside_reviewed_sections(inputs) -> None:
```

Require only article2, review U chapter plus U article2, retain article1 evidence; interpreter rejects outside reviewed sections, so completeness no longer masks this guard.

<a id="symbol-test-review-cannot-claim-another-chapter-section"></a>
### `tests.unit.test_interpret_bess_zoning.test_review_cannot_claim_another_chapter_section`

Source lines 1430–1441. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_review_cannot_claim_another_chapter_section(inputs) -> None:
```

Append N article ID to U reviewed tuple; interpreter raises another chapter.

<a id="symbol-test-general-section-review-is-explicit-and-valid"></a>
### `tests.unit.test_interpret_bess_zoning.test_general_section_review_is_explicit_and_valid`

Source lines 1444–1458. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_general_section_review_is_explicit_and_valid(inputs) -> None:
```

Append GENERAL ID to U reviewed tuple; interpret and assert ID retained. No new evidence occurrence in this case.

<a id="symbol-test-same-general-occurrence-may-be-scoped-to-different-chapters"></a>
### `tests.unit.test_interpret_bess_zoning.test_same_general_occurrence_may_be_scoped_to_different_chapters`

Source lines 1461–1524. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_same_general_occurrence_may_be_scoped_to_different_chapters(inputs) -> None:
```

Construct same GENERAL quote/rule/offset/hash as context in both chapters with different evidence IDs and shared rule ID, add GENERAL to both reviews; interpret, select occurrence and assert exactly two rows with U/N labels.

<a id="symbol-test-exact-section-page-occurrence-is-auditable"></a>
### `tests.unit.test_interpret_bess_zoning.test_exact_section_page_occurrence_is_auditable`

Source lines 1527–1541. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_exact_section_page_occurrence_is_auditable(inputs, valid_result) -> None:
```

For every catalog row rebuild synthetic fragments and assert fragment SHA equality and exact [start:end] quote. Does not recompute PDF byte SHA or independently interpret full rule.

<a id="symbol-test-repeated-excerpt-occurrence-is-bound-to-policy"></a>
### `tests.unit.test_interpret_bess_zoning.test_repeated_excerpt_occurrence_is_bound_to_policy`

Source lines 1544–1563. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_repeated_excerpt_occurrence_is_bound_to_policy(inputs, valid_result) -> None:
```

Find second identical synthetic quote (assert second>first); change catalog quote offsets only, reseal all result component/complete hashes; public validation rejects differs from rebuilt. Can fail scalar component hash comparison before semantic table checks.

<a id="symbol-test-wrong-occurrence-identity-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_wrong_occurrence_identity_is_rejected`

Source lines 1567–1582. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_wrong_occurrence_identity_is_rejected(inputs, mutation: str) -> None:
```

Four mutations: both related evidence pages to1, both fragment hashes f*64, quote start+1 or end-1. Revalidate policy then interpret; require fragment|offset message. Distinct from same-text second occurrence test.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize("mutation", ["page", "fragment_hash", "start", "end"])
```

<a id="symbol-test-exact-and-alias-mappings-are-inherited-without-prefix-logic"></a>
### `tests.unit.test_interpret_bess_zoning.test_exact_and_alias_mappings_are_inherited_without_prefix_logic`

Source lines 1585–1595. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_exact_and_alias_mappings_are_inherited_without_prefix_logic(
    valid_result,
) -> None:
```

Assert U EXACT, Ua CONFIG_ALIAS resolved U and same status in valid synthetic result. Explicit configured alias, not a general test that all prefix matching is impossible.

<a id="symbol-test-unmapped-dominant-zone-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_unmapped_dominant_zone_is_rejected`

Source lines 1598–1634. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_unmapped_dominant_zone_is_rejected(inputs) -> None:
```

Copy structure mapping, set U resolved label/section null, status UNMAPPED/method NONE; reseal structure and update lock. Interpreter must raise factual-structure wrapper before local _validate_mapping. Not isolation of unresolved-mapping fallback.

<a id="symbol-test-link-table-exactly-reproduces-routes-and-reverse-links"></a>
### `tests.unit.test_interpret_bess_zoning.test_link_table_exactly_reproduces_routes_and_reverse_links`

Source lines 1637–1651. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_link_table_exactly_reproduces_routes_and_reverse_links(valid_result) -> None:
```

Compare three expected route/evidence/role triples; assert U positive reverse route/role and all catalog decision_linked true. Does not cover context in this fixture.

<a id="symbol-test-context-evidence-is-separate-from-decision-outputs"></a>
### `tests.unit.test_interpret_bess_zoning.test_context_evidence_is_separate_from_decision_outputs`

Source lines 1654–1677. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_context_evidence_is_separate_from_decision_outputs(inputs) -> None:
```

Use context helper, interpret; assert no reverse links/decision flag for U condition and exact all/decision/context tuples at chapter, source, positive relation and P-1 parcel outputs.

<a id="symbol-test-parcel-aggregation-preserves-conflicts-and-touch-only"></a>
### `tests.unit.test_interpret_bess_zoning.test_parcel_aggregation_preserves_conflicts_and_touch_only`

Source lines 1680–1695. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_parcel_aggregation_preserves_conflicts_and_touch_only(valid_result) -> None:
```

Assert P-1 conditional one zone; P-2 conditional two same-status zones; P-3 mixed with conditional dominant and one differing nondominant; P-4 unknown/no positive/one touch/null dominant, global touch1 and no P-4 positive interpretation. No majority vote or area-coverage test.

<a id="symbol-test-prior-parcel-fields-geometry-order-index-and-crs-are-preserved"></a>
### `tests.unit.test_interpret_bess_zoning.test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved`

Source lines 1698–1712. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved(
    inputs, valid_result
) -> None:
```

Compare output original-column slice by assert_geodataframe_equal, index/CRS equality and prior surface count; assert non-zoning False/formal-review True. Scope is this synthetic fixture, no dimension-preservation torture test.

<a id="symbol-test-inputs-are-not-mutated"></a>
### `tests.unit.test_interpret_bess_zoning.test_inputs_are_not_mutated`

Source lines 1715–1725. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_inputs_are_not_mutated(inputs) -> None:
```

Copy zones, relations, parcels, structure.sections; run interpreter then pandas/geopandas equality assertions. Does not snapshot every structure table or every policy object.

<a id="symbol-test-policy-change-after-result-creation-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_policy_change_after_result_creation_is_rejected`

Source lines 1728–1733. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_policy_change_after_result_creation_is_rejected(inputs, valid_result) -> None:
```

Change dumped U rationale, revalidate model, validate old result; require policy_config_sha256 mismatch. This is a replacement policy, not in-place frozen-model mutation.

<a id="symbol-test-evidence-change-after-result-creation-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_evidence_change_after_result_creation_is_rejected`

Source lines 1736–1747. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_evidence_change_after_result_creation_is_rejected(
    inputs, valid_result
) -> None:
```

Shorten U quote by removing Technical prefix, update SHA/start, revalidate new policy; old result validation raises controlled error without message constraint. Could reject changed policy hash first.

<a id="symbol-test-zoning-relation-and-zone-mapping-changes-are-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_zoning_relation_and_zone_mapping_changes_are_rejected`

Source lines 1750–1771. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_zoning_relation_and_zone_mapping_changes_are_rejected(
    inputs, valid_result
) -> None:
```

Despite name, changes only relation row0 area/share/zone-share to99/99/9.9; old structure retained; public validator must raise factual-structure wrapper. No mapping mutation in this test (R11-T04).

<a id="symbol-test-structure-config-and-hierarchy-changes-are-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_structure_config_and_hierarchy_changes_are_rejected`

Source lines 1774–1817. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_structure_config_and_hierarchy_changes_are_rejected(inputs) -> None:
```

First model_copy changes structure profile; second copied sections change first ARTICLE parent to SECTION-UNKNOWN, reseal structure and update policy lock. Interpreter rejects both with factual-structure wrapper; GPU bypass remains.

<a id="symbol-test-public-source-complete-validator-is-invoked"></a>
### `tests.unit.test_interpret_bess_zoning.test_public_source_complete_validator_is_invoked`

Source lines 1820–1835. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_public_source_complete_validator_is_invoked(inputs, monkeypatch) -> None:
```

Spy on structure-with-fragments validator delegates to captured original; interpret, assert calls>=1. Invocation lower bound, not exact rebuild count or physical reads.

<a id="symbol-test-public-source-complete-validator-is-invoked-counted"></a>
### `tests.unit.test_interpret_bess_zoning.test_public_source_complete_validator_is_invoked.counted`

Source lines 1824–1827. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
    def counted(*args, **kwargs):
```

Closure increments nonlocal calls and returns original(*args, **kwargs). Delegating structure-validator spy, unannotated; no own exception translation.

<a id="symbol-test-one-precheck-build-performs-one-zoning-source-complete-validation"></a>
### `tests.unit.test_interpret_bess_zoning.test_one_precheck_build_performs_one_zoning_source_complete_validation`

Source lines 1838–1856. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_one_precheck_build_performs_one_zoning_source_complete_validation(
    inputs,
    monkeypatch,
) -> None:
```

Replace bypass with counter-only GPU callback; interpret then assert calls==1. Proves one gate invocation, no validation work or physical read (R11-T01).

<a id="symbol-test-one-precheck-build-performs-one-zoning-source-complete-validation-counted"></a>
### `tests.unit.test_interpret_bess_zoning.test_one_precheck_build_performs_one_zoning_source_complete_validation.counted`

Source lines 1844–1846. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
    def counted(*args) -> None:
```

Increment nonlocal calls, implicit None; DOES NOT delegate. *args only, annotation None, no physical or geometric work.

<a id="symbol-test-invalid-physical-zoning-fails-before-policy-interpretation"></a>
### `tests.unit.test_interpret_bess_zoning.test_invalid_physical_zoning_fails_before_policy_interpretation`

Source lines 1859–1883. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_invalid_physical_zoning_fails_before_policy_interpretation(
    inputs,
    monkeypatch,
) -> None:
```

Replace GPU gate with raising sentinel and policy resolver with counter; expect wrapped physical source invalid and policy_calls==0. Proves ordering with synthetic failure, not a corrupted actual GPU file.

<a id="symbol-test-invalid-physical-zoning-fails-before-policy-interpretation-invalid-source"></a>
### `tests.unit.test_interpret_bess_zoning.test_invalid_physical_zoning_fails_before_policy_interpretation.invalid_source`

Source lines 1865–1866. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
    def invalid_source(*args) -> None:
```

Always raise interpreter-imported PlanningZoningError("physical source invalid"); annotation None but never returns. No physical source examined.

<a id="symbol-test-invalid-physical-zoning-fails-before-policy-interpretation-counted-policy"></a>
### `tests.unit.test_interpret_bess_zoning.test_invalid_physical_zoning_fails_before_policy_interpretation.counted_policy`

Source lines 1868–1871. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
    def counted_policy(*args):
```

Increment nonlocal policy_calls and return inputs[-1] if invoked; test expects never reached, so no resolution/revalidation occurs.

<a id="symbol-test-one-build-result-performs-one-factual-structure-rebuild"></a>
### `tests.unit.test_interpret_bess_zoning.test_one_build_result_performs_one_factual_structure_rebuild`

Source lines 1886–1903. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_one_build_result_performs_one_factual_structure_rebuild(
    inputs, monkeypatch
) -> None:
```

Patch structure-with-fragments to delegating spy, call private _build_result(*inputs[:6], inputs[-1]); assert calls==1. Exact owner invocation count, not PDF/GPU read count; private path has no physical GPU gate.

<a id="symbol-test-one-build-result-performs-one-factual-structure-rebuild-counted"></a>
### `tests.unit.test_interpret_bess_zoning.test_one_build_result_performs_one_factual_structure_rebuild.counted`

Source lines 1892–1895. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
    def counted(*args, **kwargs):
```

Increment nonlocal calls then return captured original(*args, **kwargs). Delegates real in-memory structure rebuild over synthetic index.

<a id="symbol-test-relation-area-denominators-are-required"></a>
### `tests.unit.test_interpret_bess_zoning.test_relation_area_denominators_are_required`

Source lines 1910–1924. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_relation_area_denominators_are_required(inputs, column: str) -> None:
```

Drop parcel_metric_area_m2 or zone_area_m2, call interpreter and require BessZoningPrecheckError without message. Earlier structure/input checks may reject; does not isolate local relation helper (R11-T03).

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    "column",
    ["parcel_metric_area_m2", "zone_area_m2"],
)
```

<a id="symbol-test-relation-percentages-must-match-denominators"></a>
### `tests.unit.test_interpret_bess_zoning.test_relation_percentages_must_match_denominators`

Source lines 1931–1947. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_relation_percentages_must_match_denominators(inputs, column: str) -> None:
```

Add1 to row0 parcel_share_pct or zone_share_pct, leave old structure unchanged; expect any BessZoningPrecheckError. Structure input hash can reject before local percentage tolerance (R11-T03).

Exact decorators (not extra units):

```python
@pytest.mark.parametrize(
    "column",
    ["parcel_share_pct", "zone_share_pct"],
)
```

<a id="symbol-test-factual-zone-mapping-counts-are-recomputed"></a>
### `tests.unit.test_interpret_bess_zoning.test_factual_zone_mapping_counts_are_recomputed`

Source lines 1950–2008. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_factual_zone_mapping_counts_are_recomputed(inputs) -> None:
```

First increment candidate_intersection_count, reseal structure and update lock; interpreter rejects factual structure. Then change raw mapping label to CHANGED, reseal/update lock and call public validator with bare global valid_result: fixture is NOT a parameter here. That argument is a fixture function object, not built result; any controlled failure suffices and structure may reject first. This second arm is not a valid-result comparison proof (R11-T05).

<a id="symbol-test-coordinated-result-mutation-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_coordinated_result_mutation_is_rejected`

Source lines 2011–2016. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_coordinated_result_mutation_is_rejected(inputs, valid_result) -> None:
```

Change copied chapter row0 confidence to HIGH, reseal result hashes, validate against original inputs; require differs from rebuilt. Scalar component-hash mismatch can precede frame comparison.

<a id="symbol-test-coordinated-evidence-catalog-mutation-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_coordinated_evidence_catalog_mutation_is_rejected`

Source lines 2019–2026. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_coordinated_evidence_catalog_mutation_is_rejected(
    inputs, valid_result
) -> None:
```

Change copied catalog interpretation_note to Coordinated mutation., reseal and validate; expect differs from rebuilt. Not proof later reference guards are reached.

<a id="symbol-test-coordinated-catalog-occurrence-duplicate-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_coordinated_catalog_occurrence_duplicate_is_rejected`

Source lines 2029–2049. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_coordinated_catalog_occurrence_duplicate_is_rejected(
    inputs, valid_result
) -> None:
```

Copy first catalog six occurrence fields into second row, reseal hashes; require duplicate chapter-scoped occurrence message. _compare_results checks duplicate occurrence before scalar hash comparison, isolating that guard.

<a id="symbol-test-coordinated-route-table-mutation-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_coordinated_route_table_mutation_is_rejected`

Source lines 2052–2057. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_coordinated_route_table_mutation_is_rejected(inputs, valid_result) -> None:
```

Change copied first route applicability_note, reseal hashes; validation requires differs from rebuilt, possibly at scalar hash comparison.

<a id="symbol-test-coordinated-evidence-route-link-mutation-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_coordinated_evidence_route_link_mutation_is_rejected`

Source lines 2060–2067. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_coordinated_evidence_route_link_mutation_is_rejected(
    inputs, valid_result
) -> None:
```

Change copied first link route_role to BROKEN, reseal; require differs from rebuilt, not necessarily later link-set guard.

<a id="symbol-test-coordinated-reverse-link-mutation-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_coordinated_reverse_link_mutation_is_rejected`

Source lines 2070–2075. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_coordinated_reverse_link_mutation_is_rejected(inputs, valid_result) -> None:
```

Set copied first catalog linked_route_roles to (DIFFICULTY,), reseal; require differs from rebuilt, possibly before reverse-link guard.

<a id="symbol-test-evidence-route-link-hash-mutation-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_evidence_route_link_hash_mutation_is_rejected`

Source lines 2078–2084. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_evidence_route_link_hash_mutation_is_rejected(inputs, valid_result) -> None:
```

Replace only evidence_route_links_content_sha256 by f*64 without resealing complete result; validation rejects differs from rebuilt scalar.

<a id="symbol-test-old-result-hash-schemas-are-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_old_result_hash_schemas_are_rejected`

Source lines 2088–2092. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_old_result_hash_schemas_are_rejected(
    inputs, valid_result, version: int
) -> None:
```

Replace result_hash_schema_version with1..4 without rehash; validator rejects named scalar mismatch. Not direct isolation of supported-version branch after scalar comparison.

Exact decorators (not extra units):

```python
@pytest.mark.parametrize("version", [1, 2, 3, 4])
```

<a id="symbol-test-relation-identity-change-is-rejected"></a>
### `tests.unit.test_interpret_bess_zoning.test_relation_identity_change_is_rejected`

Source lines 2095–2111. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_relation_identity_change_is_rejected(inputs) -> None:
```

Change first relation source_zone_id to SRC-N; old structure retained; interpreter raises factual-structure wrapper. Not a fresh physical-source attack.

<a id="symbol-test-readback-result-validates"></a>
### `tests.unit.test_interpret_bess_zoning.test_readback_result_validates`

Source lines 2114–2148. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_readback_result_validates(tmp_path: Path, inputs, valid_result) -> None:
```

Write seven synthetic Parquets: six plain frames index=False, parcels with index retained. Read with pandas/geopandas, replace frame fields without rehash, publicly validate against same bypassed inputs, assert no duplicate occurrence. Proves this serialization roundtrip, not manifest byte capture, writer API, real GPU or PDF.

<a id="symbol-test-policy-yaml-roundtrip-is-strict"></a>
### `tests.unit.test_interpret_bess_zoning.test_policy_yaml_roundtrip_is_strict`

Source lines 2151–2164. Kind: function. Owner: `tests.unit.test_interpret_bess_zoning`.

```python
def test_policy_yaml_roundtrip_is_strict(tmp_path: Path, inputs) -> None:
```

Write temporary safe_dump of model_dump(mode="json"), allow_unicode=True/sort_keys=False; loader equality to original policy. Scoped roundtrip, not every malformed YAML or mutation operation.

## Complete source snapshot

Exact full Git-content UTF-8 source. Byte identity supports provenance, not semantic correctness of prose by itself.

```python
from __future__ import annotations

import importlib
from dataclasses import replace
from hashlib import sha256
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import Polygon

interpret_module = importlib.import_module("landscout.stages.interpret_bess_zoning")

from landscout import stages
from landscout.stages.index_planning_regulation import (
    INDEX_HASH_SCHEMA_VERSION,
    PAGE_HASH_SCHEMA_VERSION,
    SEARCH_NORMALIZATION_PROFILE,
    PlanningRegulationIndex,
    _index_content_sha256,
    _normalize_search_text,
    _page_content_sha256,
    _pages_content_sha256,
)
from landscout.stages.interpret_bess_zoning import (
    CHAPTER_POLICY_COLUMNS,
    EVIDENCE_CATALOG_COLUMNS,
    EVIDENCE_ROUTE_LINK_COLUMNS,
    PARCEL_ZONE_POLICY_COLUMNS,
    ROUTE_ASSESSMENT_COLUMNS,
    SOURCE_ZONE_POLICY_COLUMNS,
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    _result_with_hashes,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)
from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
)
from landscout.stages.structure_planning_regulation import (
    _result_with_hashes as _structure_with_hashes,
)


def _index() -> PlanningRegulationIndex:
    raw_pages = (
        "ARTICLE 1 - GENERAL\nGeneral factual text.",
        (
            "ZONE U\nARTICLE U 1 - USES\nTechnical equipment is permitted only when "
            "formal review is required.\nTechnical equipment is permitted only when "
            "formal review is required.\nARTICLE U 2 - OTHER\nOther factual text."
        ),
        (
            "ZONE N\nARTICLE N 1 - USES\nBattery facilities are restricted.\n"
            "Technical equipment is permitted only when formal review is required.\n"
            "ARTICLE N 2 - OTHER\nOther factual text."
        ),
    )
    rows: list[dict[str, object]] = []
    for number, raw_text in enumerate(raw_pages, start=1):
        row: dict[str, object] = {
            "page_number": number,
            "extraction_status": "TEXT",
            "raw_text": raw_text,
            "normalized_search_text": _normalize_search_text(raw_text),
            "character_count": len(raw_text),
            "extraction_error": None,
            "page_content_sha256": "",
        }
        row["page_content_sha256"] = _page_content_sha256(row)
        rows.append(row)
    pages = pd.DataFrame(rows)
    index = PlanningRegulationIndex(
        document_id="doc-1",
        archive_sha256="a" * 64,
        regulation_filename="commune_reglement.pdf",
        source_selection_method="ZONING_NOMFIC",
        source_selection_sha256="b" * 64,
        pdf_relative_path="package/commune_reglement.pdf",
        pdf_size_bytes=100,
        pdf_sha256="c" * 64,
        extraction_library="pypdf",
        extraction_library_version="test-version",
        search_normalization_profile=SEARCH_NORMALIZATION_PROFILE,
        page_hash_schema_version=PAGE_HASH_SCHEMA_VERSION,
        index_hash_schema_version=INDEX_HASH_SCHEMA_VERSION,
        total_page_count=len(pages),
        pages_content_sha256=_pages_content_sha256(pages),
        index_content_sha256="d" * 64,
        pages=pages,
    )
    return replace(index, index_content_sha256=_index_content_sha256(index))


def _zones(index: PlanningRegulationIndex) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "planning_zone_id": ["ZONE-U", "ZONE-UA", "ZONE-N"],
            "source_zone_id": ["SRC-U", "SRC-UA", "SRC-N"],
            "zone_label_raw": ["U", "Ua", "N"],
            "source_document_id": index.document_id,
            "source_archive_sha256": index.archive_sha256,
            "source_layer": "ZONE",
        }
    )


def _relations(index: PlanningRegulationIndex) -> pd.DataFrame:
    rows = (
        ("P-1", "ZONE-U", "SRC-U", "U", "AREA_OVERLAP", 100.0, 100.0),
        ("P-2", "ZONE-U", "SRC-U", "U", "AREA_OVERLAP", 60.0, 60.0),
        ("P-2", "ZONE-UA", "SRC-UA", "Ua", "AREA_OVERLAP", 40.0, 40.0),
        ("P-3", "ZONE-U", "SRC-U", "U", "AREA_OVERLAP", 60.0, 60.0),
        ("P-3", "ZONE-N", "SRC-N", "N", "AREA_OVERLAP", 40.0, 40.0),
        ("P-4", "ZONE-N", "SRC-N", "N", "TOUCH_ONLY", 0.0, 0.0),
    )
    return pd.DataFrame(
        [
            {
                "parcel_id": parcel_id,
                "planning_zone_id": planning_zone_id,
                "source_zone_id": source_zone_id,
                "zone_label_raw": label,
                "relation_type": relation_type,
                "intersection_area_m2": area,
                "parcel_share_pct": share,
                "zone_share_pct": area / 10.0,
                "source_document_id": index.document_id,
                "source_archive_sha256": index.archive_sha256,
                "source_layer": "ZONE",
                "parcel_metric_area_m2": 100.0,
                "zone_area_m2": 1000.0,
            }
            for (
                parcel_id,
                planning_zone_id,
                source_zone_id,
                label,
                relation_type,
                area,
                share,
            ) in rows
        ]
    )


def _structure_config(
    index: PlanningRegulationIndex,
) -> PlanningRegulationStructureConfig:
    return PlanningRegulationStructureConfig.model_validate(
        {
            "schema_version": 2,
            "structure_profile": "synthetic_v1",
            "document_lock": {
                "document_id": index.document_id,
                "pdf_sha256": index.pdf_sha256,
                "pages_content_sha256": index.pages_content_sha256,
                "index_content_sha256": index.index_content_sha256,
                "normalization_profile": index.search_normalization_profile,
            },
            "document_layout": {
                "body_start_page": 1,
                "table_of_contents_pages": [],
                "max_heading_continuation_lines": 0,
                "include_table_of_contents_in_topic_evidence": False,
            },
            "heading_patterns": {
                "zone_chapter": [r"^ZONE\s+(?P<label>[A-Za-z0-9]+)$"],
                "article": [
                    r"^ARTICLE\s+(?P<zone>[A-Za-z0-9]+)\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"
                ],
                "general_section": [r"^ARTICLE\s+(?P<number>\d+)\s*-\s*(?P<title>.*)$"],
                "continuation": [],
            },
            "ignored_patterns": {"page_headers": [], "page_footers": []},
            "zone_aliases": {"Ua": "U"},
            "topics": {"technical": ["technical equipment"]},
            "topic_match_policy": {
                "boundary_mode": "token",
                "overlap_resolution": "longest_match",
            },
            "topic_context_characters": 20,
        }
    )


def _parcels(index: PlanningRegulationIndex) -> gpd.GeoDataFrame:
    frame = gpd.GeoDataFrame(
        {
            "parcel_id": ["P-1", "P-2", "P-3", "P-4"],
            "dominant_planning_zone_id": ["ZONE-U", "ZONE-U", "ZONE-U", None],
            "planning_surface_relation_count": [0, 1, 2, 0],
            "prescription_surface_relation_count": [0, 1, 1, 0],
            "information_surface_relation_count": [0, 0, 1, 0],
            "planning_line_relation_count": [0, 0, 0, 0],
            "planning_point_relation_count": [0, 0, 0, 0],
            "planning_document_id": index.document_id,
            "planning_archive_sha256": index.archive_sha256,
            "planning_feature_document_id": index.document_id,
            "planning_feature_archive_sha256": index.archive_sha256,
            "prior_fact": ["one", "two", "three", "four"],
        },
        geometry=[
            Polygon([(x, 0), (x + 10, 0), (x + 10, 10), (x, 10), (x, 0)])
            for x in (0, 20, 40, 60)
        ],
        crs="EPSG:2154",
        index=pd.Index([10, 20, 30, 40], name="source_row"),
    )
    return frame


def _policy(index, structure, config, zones, relations) -> BessZoningPolicyConfig:
    sections = structure.sections
    u_articles = sections.loc[
        sections["section_type"].eq("ARTICLE") & sections["zone_chapter_label"].eq("U")
    ]
    n_articles = sections.loc[
        sections["section_type"].eq("ARTICLE") & sections["zone_chapter_label"].eq("N")
    ]
    u_article = u_articles.loc[u_articles["article_number_raw"].eq("1")].iloc[0]
    n_article = n_articles.loc[n_articles["article_number_raw"].eq("1")].iloc[0]
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    u_positive = "Technical equipment is permitted"
    u_condition = "only when formal review is required"
    n_excerpt = "Battery facilities are restricted."

    def evidence(
        evidence_id: str,
        section_id: str,
        page_number: int,
        kind: str,
        direction: str,
        excerpt: str,
        source_rule_id: str,
        source_rule: str,
        note: str,
    ) -> dict[str, object]:
        fragment = fragments.loc[(section_id, page_number)]
        raw = fragment["raw_text"]
        rule_start = raw.index(source_rule)
        start = raw.index(excerpt, rule_start, rule_start + len(source_rule))
        return {
            "evidence_id": evidence_id,
            "section_id": section_id,
            "page_number": page_number,
            "evidence_kind": kind,
            "evidence_direction": direction,
            "exact_raw_excerpt": excerpt,
            "excerpt_sha256": sha256(excerpt.encode()).hexdigest(),
            "section_page_fragment_sha256": fragment["section_page_fragment_sha256"],
            "excerpt_start": start,
            "excerpt_end": start + len(excerpt),
            "source_rule_id": source_rule_id,
            "source_rule_excerpt": source_rule,
            "source_rule_sha256": sha256(source_rule.encode()).hexdigest(),
            "source_rule_start": rule_start,
            "source_rule_end": rule_start + len(source_rule),
            "interpretation_note": note,
        }

    return BessZoningPolicyConfig.model_validate(
        {
            "schema_version": 5,
            "policy_profile": "synthetic_policy_v5",
            "planning_precheck_scope": "WRITTEN_ZONING_REGULATION_ONLY",
            "review_scope": "CONFIGURED_USE_CONTROL_ARTICLES_ONLY",
            "source_lock": {
                "document_id": index.document_id,
                "archive_sha256": index.archive_sha256,
                "pdf_sha256": index.pdf_sha256,
                "index_content_sha256": index.index_content_sha256,
                "structure_result_content_sha256": (
                    structure.structure_result_content_sha256
                ),
                "structure_profile": structure.structure_profile,
            },
            "required_zone_article_numbers": ["1", "2"],
            "chapters": [
                {
                    "resolved_zone_chapter_label": "U",
                    "review_completeness": "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES",
                    "reviewed_section_ids": u_articles["section_id"].tolist(),
                    "review_note": "The required use-control article was reviewed.",
                    "zoning_precheck_status": "CONDITIONAL_REVIEW",
                    "zoning_precheck_confidence": "MEDIUM",
                    "rationale": "The source states a review condition.",
                    "missing_information": "Formal classification and review.",
                    "evidence": [
                        evidence(
                            "E-U-POSITIVE",
                            u_article["section_id"],
                            2,
                            "USE_PERMISSION",
                            "SUPPORTS_POTENTIAL_COMPATIBILITY",
                            u_positive,
                            "RULE-U-CONDITIONAL",
                            "Technical equipment is permitted only when formal review is required.",
                            "This is positive route evidence only.",
                        ),
                        evidence(
                            "E-U-CONDITION",
                            u_article["section_id"],
                            2,
                            "TECHNICAL_EQUIPMENT_RULE",
                            "CONDITION",
                            u_condition,
                            "RULE-U-CONDITIONAL",
                            "Technical equipment is permitted only when formal review is required.",
                            "This is a condition only.",
                        ),
                    ],
                    "route_assessments": [
                        {
                            "route_id": "ROUTE-U-CONDITIONAL",
                            "route_kind": "CONDITIONAL_ROUTE",
                            "positive_evidence_ids": ["E-U-POSITIVE"],
                            "condition_evidence_ids": ["E-U-CONDITION"],
                            "difficulty_evidence_ids": [],
                            "applicability_note": "The positive route and its condition are assessed together.",
                        }
                    ],
                },
                {
                    "resolved_zone_chapter_label": "N",
                    "review_completeness": "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES",
                    "reviewed_section_ids": n_articles["section_id"].tolist(),
                    "review_note": "The required use-control article was reviewed.",
                    "zoning_precheck_status": "LIKELY_DIFFICULT",
                    "zoning_precheck_confidence": "HIGH",
                    "rationale": "The source states a relevant restriction.",
                    "missing_information": "Formal classification and review.",
                    "evidence": [
                        evidence(
                            "E-N-1",
                            n_article["section_id"],
                            3,
                            "USE_RESTRICTION",
                            "SUPPORTS_DIFFICULTY",
                            n_excerpt,
                            "RULE-N-RESTRICTION",
                            n_excerpt,
                            "This is difficulty evidence only.",
                        )
                    ],
                    "route_assessments": [
                        {
                            "route_id": "ROUTE-N-DIFFICULT",
                            "route_kind": "DIFFICULTY_ONLY",
                            "positive_evidence_ids": [],
                            "condition_evidence_ids": [],
                            "difficulty_evidence_ids": ["E-N-1"],
                            "applicability_note": "The restriction is assessed without a positive route.",
                        }
                    ],
                },
            ],
        }
    )


@pytest.fixture
def inputs(monkeypatch):
    monkeypatch.setattr(
        interpret_module,
        "validate_normalized_planning_zoning_inputs",
        lambda *args: None,
    )
    index = _index()
    zones = _zones(index)
    relations = _relations(index)
    config = _structure_config(index)
    structure = structure_planning_regulation(index, zones, relations, config)
    parcels = _parcels(index)
    policy = _policy(index, structure, config, zones, relations)
    planning_document = object()
    return (
        index,
        structure,
        config,
        zones,
        relations,
        parcels,
        planning_document,
        policy,
    )


@pytest.fixture
def valid_result(inputs):
    return interpret_bess_zoning(*inputs)


def _payload(policy: BessZoningPolicyConfig) -> dict[str, object]:
    return policy.model_dump(mode="python")


def _policy_with_context_only_evidence(
    policy: BessZoningPolicyConfig,
) -> BessZoningPolicyConfig:
    payload = _payload(policy)
    chapter = payload["chapters"][0]
    chapter["evidence"][1]["evidence_direction"] = "CONTEXT_ONLY"
    route = chapter["route_assessments"][0]
    route["route_kind"] = "DIRECT_ROUTE"
    route["condition_evidence_ids"] = []
    chapter["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"
    return BessZoningPolicyConfig.model_validate(payload)


def _validate(inputs, result) -> None:
    validate_bess_zoning_precheck(*inputs, result)


def test_package_exports_precheck_api() -> None:
    for name in (
        "BessZoningPolicyConfig",
        "BessZoningPrecheckError",
        "BessZoningPrecheckResult",
        "interpret_bess_zoning",
        "load_bess_zoning_policy_config",
        "planning_regulation_section_page_fragments",
        "validate_bess_zoning_precheck",
        "validate_planning_regulation_structure_with_fragments",
    ):
        assert name in stages.__all__


def test_valid_locked_policy_builds_complete_outputs(inputs, valid_result) -> None:
    index, structure, _, zones, relations, parcels, _, policy = inputs
    result = valid_result
    _validate(inputs, result)
    assert tuple(result.chapter_policy.columns) == CHAPTER_POLICY_COLUMNS
    assert tuple(result.route_assessments.columns) == ROUTE_ASSESSMENT_COLUMNS
    assert tuple(result.evidence_route_links.columns) == EVIDENCE_ROUTE_LINK_COLUMNS
    assert tuple(result.source_zone_policy.columns) == SOURCE_ZONE_POLICY_COLUMNS
    assert (
        tuple(result.parcel_zone_interpretations.columns) == PARCEL_ZONE_POLICY_COLUMNS
    )
    assert len(result.chapter_policy) == 2
    assert len(result.source_zone_policy) == 3
    assert len(result.parcel_zone_interpretations) == 5
    assert len(result.parcels) == len(parcels)
    assert result.policy_schema_version == 5
    assert result.result_hash_schema_version == 5
    assert tuple(result.evidence_catalog.columns) == EVIDENCE_CATALOG_COLUMNS
    assert result.planning_precheck_scope == "WRITTEN_ZONING_REGULATION_ONLY"
    assert result.review_scope == "CONFIGURED_USE_CONTROL_ARTICLES_ONLY"
    assert result.parcels["review_scope"].eq(result.review_scope).all()
    assert len(result.route_assessments) == 2
    assert len(result.evidence_route_links) == 3
    assert result.touch_only_relation_count == 1
    assert result.document_id == index.document_id
    assert (
        result.structure_result_content_sha256
        == structure.structure_result_content_sha256
    )
    assert result.zoning_relation_hash_columns == tuple(relations.columns)
    assert set(result.source_zone_policy["source_zone_label_raw"]) == set(
        zones["zone_label_raw"]
    )
    assert result.policy_profile == policy.policy_profile


@pytest.mark.parametrize(
    "field",
    [
        "document_id",
        "archive_sha256",
        "pdf_sha256",
        "index_content_sha256",
        "structure_result_content_sha256",
        "structure_profile",
    ],
)
def test_source_lock_mismatch_is_rejected(inputs, field: str) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    payload["source_lock"][field] = "f" * 64 if "sha256" in field else "wrong"
    bad = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError, match="differs from factual source"):
        interpret_bess_zoning(*sources, bad)


def test_missing_and_extra_chapter_are_rejected(inputs) -> None:
    *sources, policy = inputs
    missing_payload = _payload(policy)
    missing_payload["chapters"] = missing_payload["chapters"][:-1]
    with pytest.raises(BessZoningPrecheckError, match="completeness differs"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(missing_payload)
        )
    extra_payload = _payload(policy)
    extra = dict(extra_payload["chapters"][0])
    extra["resolved_zone_chapter_label"] = "EXTRA"
    extra["evidence"] = []
    extra["route_assessments"] = []
    extra["zoning_precheck_status"] = "UNKNOWN"
    extra_payload["chapters"] = (*extra_payload["chapters"], extra)
    with pytest.raises(BessZoningPrecheckError, match="extra=.*EXTRA"):
        interpret_bess_zoning(
            *sources, BessZoningPolicyConfig.model_validate(extra_payload)
        )


def test_regulation_zone_chapter_labels_and_ids_must_be_unique(inputs) -> None:
    structure = inputs[1]
    assert len(interpret_module._zone_chapter_rows(structure)) == 2

    used = (
        structure.sections.loc[
            structure.sections["section_type"].eq("ZONE_CHAPTER")
            & structure.sections["zone_chapter_label"].eq("U")
        ]
        .iloc[0]
        .copy()
    )
    used["section_id"] = "SECTION-DUPLICATE-U"
    duplicated_used = replace(
        structure,
        sections=pd.concat([structure.sections, used.to_frame().T], ignore_index=True),
    )
    with pytest.raises(BessZoningPrecheckError, match="labels must be unique"):
        interpret_module._zone_chapter_rows(duplicated_used)

    unused_one = used.copy()
    unused_one["section_id"] = "SECTION-UNUSED-X-1"
    unused_one["zone_chapter_label"] = "X"
    unused_two = unused_one.copy()
    unused_two["section_id"] = "SECTION-UNUSED-X-2"
    duplicated_unused = replace(
        structure,
        sections=pd.concat(
            [
                structure.sections,
                unused_one.to_frame().T,
                unused_two.to_frame().T,
            ],
            ignore_index=True,
        ),
    )
    with pytest.raises(BessZoningPrecheckError, match="labels must be unique"):
        interpret_module._zone_chapter_rows(duplicated_unused)

    duplicate_id = used.copy()
    duplicate_id["section_id"] = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER"), "section_id"
    ].iloc[1]
    duplicate_id["zone_chapter_label"] = "X"
    duplicated_section_id = replace(
        structure,
        sections=pd.concat(
            [structure.sections, duplicate_id.to_frame().T], ignore_index=True
        ),
    )
    with pytest.raises(BessZoningPrecheckError, match="section IDs must be unique"):
        interpret_module._zone_chapter_rows(duplicated_section_id)


def test_source_complete_validator_rejects_later_duplicate_chapter(
    inputs, valid_result
) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    duplicate = (
        structure.sections.loc[structure.sections["section_type"].eq("ZONE_CHAPTER")]
        .iloc[0]
        .copy()
    )
    duplicate["section_id"] = "SECTION-LATE-DUPLICATE"
    changed = replace(
        structure,
        sections=pd.concat(
            [structure.sections, duplicate.to_frame().T], ignore_index=True
        ),
    )
    with pytest.raises(BessZoningPrecheckError):
        validate_bess_zoning_precheck(
            index,
            changed,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            policy,
            valid_result,
        )


def test_duplicate_chapter_and_evidence_id_are_rejected(inputs) -> None:
    policy = inputs[-1]
    chapter_payload = _payload(policy)
    chapter_payload["chapters"] = (
        *chapter_payload["chapters"],
        chapter_payload["chapters"][0],
    )
    with pytest.raises(ValueError, match="chapter policy labels must be unique"):
        BessZoningPolicyConfig.model_validate(chapter_payload)
    evidence_payload = _payload(policy)
    evidence_payload["chapters"][1]["evidence"][0]["evidence_id"] = "E-U-POSITIVE"
    with pytest.raises(ValueError, match="evidence IDs must be globally unique"):
        BessZoningPolicyConfig.model_validate(evidence_payload)


def test_one_excerpt_cannot_be_reused_with_contradictory_directions(inputs) -> None:
    payload = _payload(inputs[-1])
    first = dict(payload["chapters"][0]["evidence"][1])
    second = dict(first)
    first["evidence_direction"] = "SUPPORTS_POTENTIAL_COMPATIBILITY"
    second["evidence_id"] = "E-U-2"
    second["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    payload["chapters"][0]["evidence"] = (first, second)
    with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)


def test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    duplicate = dict(payload["chapters"][0]["evidence"][0])
    duplicate["evidence_id"] = "E-U-POSITIVE-DUPLICATE"
    payload["chapters"][0]["evidence"] = (
        *payload["chapters"][0]["evidence"],
        duplicate,
    )
    payload["chapters"][0]["route_assessments"][0]["positive_evidence_ids"] = [
        "E-U-POSITIVE",
        "E-U-POSITIVE-DUPLICATE",
    ]

    with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)


def test_duplicate_occurrence_in_different_compatible_routes_is_rejected(
    inputs,
) -> None:
    payload = _payload(inputs[-1])
    duplicate = dict(payload["chapters"][1]["evidence"][0])
    duplicate["evidence_id"] = "E-N-DUPLICATE-ROUTE"
    payload["chapters"][1]["evidence"] = (
        *payload["chapters"][1]["evidence"],
        duplicate,
    )
    payload["chapters"][1]["route_assessments"] = (
        *payload["chapters"][1]["route_assessments"],
        {
            "route_id": "ROUTE-N-DUPLICATE-OCCURRENCE",
            "route_kind": "DIFFICULTY_ONLY",
            "positive_evidence_ids": [],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": ["E-N-DUPLICATE-ROUTE"],
            "applicability_note": "A second route must not duplicate the occurrence.",
        },
    )

    with pytest.raises(ValueError, match="chapter-scoped evidence occurrence"):
        BessZoningPolicyConfig.model_validate(payload)


@pytest.mark.parametrize("status", ["ALLOWED", "FORBIDDEN", "PROHIBITED"])
def test_forbidden_or_invalid_final_status_is_rejected(inputs, status: str) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = status
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)


def test_invalid_confidence_and_unknown_field_are_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_confidence"] = "CERTAIN"
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)
    payload = _payload(inputs[-1])
    payload["automatic_classifier"] = True
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)


def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.yaml"
    path.write_text(
        "schema_version: 2\nschema_version: 2\n",
        encoding="utf-8",
    )
    with pytest.raises(BessZoningPrecheckError, match="Duplicate YAML.*key"):
        load_bess_zoning_policy_config(path)


@pytest.mark.parametrize("version", [1, 2, 3, 4])
def test_old_policy_schema_versions_are_rejected(inputs, version: int) -> None:
    payload = _payload(inputs[-1])
    payload["schema_version"] = version
    with pytest.raises(ValueError, match="unsupported BESS zoning policy schema"):
        BessZoningPolicyConfig.model_validate(payload)


def test_every_evidence_kind_has_an_explicit_direction_matrix(inputs) -> None:
    allowed = {
        "USE_PERMISSION": {
            "SUPPORTS_POTENTIAL_COMPATIBILITY",
            "CONTEXT_ONLY",
        },
        "USE_RESTRICTION": {"SUPPORTS_DIFFICULTY", "CONTEXT_ONLY"},
        "PUBLIC_INTEREST_EXCEPTION": {
            "SUPPORTS_POTENTIAL_COMPATIBILITY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "TECHNICAL_EQUIPMENT_RULE": {
            "SUPPORTS_POTENTIAL_COMPATIBILITY",
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "ICPE_RULE": {
            "SUPPORTS_POTENTIAL_COMPATIBILITY",
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "RISK_OR_NUISANCE_CONDITION": {
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "ACCESS_OR_NETWORK_CONDITION": {
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
        "OTHER_RELEVANT_RULE": {
            "SUPPORTS_DIFFICULTY",
            "CONDITION",
            "CONTEXT_ONLY",
        },
    }
    directions = {
        "SUPPORTS_POTENTIAL_COMPATIBILITY",
        "SUPPORTS_DIFFICULTY",
        "CONDITION",
        "CONTEXT_ONLY",
    }
    base = _payload(inputs[-1])["chapters"][0]["evidence"][0]
    for kind, permitted in allowed.items():
        for direction in directions:
            evidence = dict(base)
            evidence["evidence_kind"] = kind
            evidence["evidence_direction"] = direction
            if direction in permitted:
                interpret_module.PolicyEvidence.model_validate(evidence)
            else:
                with pytest.raises(
                    ValueError,
                    match="kind and direction are incompatible",
                ):
                    interpret_module.PolicyEvidence.model_validate(evidence)


def test_valid_exact_evidence_is_preserved(inputs, valid_result) -> None:
    policy = inputs[-1]
    excerpt = policy.chapters[0].evidence[0].exact_raw_excerpt
    assert excerpt == "Technical equipment is permitted"
    assert (
        policy.chapters[0].evidence[0].excerpt_sha256
        == sha256(excerpt.encode()).hexdigest()
    )
    assert valid_result.chapter_policy.iloc[0]["evidence_ids"] == (
        "E-U-POSITIVE",
        "E-U-CONDITION",
    )
    row = valid_result.evidence_catalog.set_index("evidence_id").loc["E-U-POSITIVE"]
    assert "only when" in row["source_rule_excerpt"]
    relative_start = row["excerpt_start"] - row["source_rule_start"]
    relative_end = row["excerpt_end"] - row["source_rule_start"]
    assert row["source_rule_excerpt"][relative_start:relative_end] == excerpt


@pytest.mark.parametrize("mutation", ["hash", "start", "end", "outside"])
def test_source_rule_identity_and_containment_are_strict(inputs, mutation: str) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    evidence = payload["chapters"][0]["evidence"][0]
    if mutation == "hash":
        evidence["source_rule_sha256"] = "f" * 64
        with pytest.raises(ValueError, match="source rule SHA256"):
            BessZoningPolicyConfig.model_validate(payload)
        return
    if mutation == "outside":
        evidence["source_rule_start"] = evidence["excerpt_start"] + 1
        with pytest.raises(ValueError, match="inside its source rule"):
            BessZoningPolicyConfig.model_validate(payload)
        return
    for related in payload["chapters"][0]["evidence"]:
        if mutation == "start":
            related["source_rule_start"] -= 1
        else:
            related["source_rule_end"] += 1
    with pytest.raises(BessZoningPrecheckError, match="source-rule offsets"):
        interpret_bess_zoning(
            *sources,
            BessZoningPolicyConfig.model_validate(payload),
        )


def test_same_rule_text_at_distinct_offsets_has_distinct_identity(inputs) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    first = chapter["evidence"][0]
    second = dict(first)
    rule_length = len(first["source_rule_excerpt"])
    second_rule_start = first["source_rule_end"] + 1
    second["evidence_id"] = "E-U-SECOND-OCCURRENCE"
    second["evidence_kind"] = "TECHNICAL_EQUIPMENT_RULE"
    second["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    second["source_rule_id"] = "RULE-U-SECOND-OCCURRENCE"
    second["source_rule_start"] = second_rule_start
    second["source_rule_end"] = second_rule_start + rule_length
    second["excerpt_start"] = second_rule_start
    second["excerpt_end"] = second_rule_start + len(first["exact_raw_excerpt"])
    chapter["evidence"] = (*chapter["evidence"], second)
    chapter["route_assessments"] = (
        *chapter["route_assessments"],
        {
            "route_id": "ROUTE-U-SECOND-DIFFICULTY",
            "route_kind": "DIFFICULTY_ONLY",
            "positive_evidence_ids": [],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": ["E-U-SECOND-OCCURRENCE"],
            "applicability_note": "The distinct occurrence is linked explicitly.",
        },
    )
    policy = BessZoningPolicyConfig.model_validate(payload)
    assert policy.chapters[0].evidence[-1].evidence_direction == "SUPPORTS_DIFFICULTY"


def test_real_muret_source_rules_preserve_conditional_and_exception_frames() -> None:
    policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
    by_label = {
        chapter.resolved_zone_chapter_label: chapter for chapter in policy.chapters
    }
    for label in ("UA", "UB", "UC", "UD", "UF", "AU", "AUf"):
        positive = next(
            evidence
            for evidence in by_label[label].evidence
            if evidence.evidence_direction == "SUPPORTS_POTENTIAL_COMPATIBILITY"
        )
        assert "ne sont autorisées qu’à" in positive.source_rule_excerpt
        assert "condition" in positive.source_rule_excerpt
    for label in ("UP", "AUp"):
        positive = next(
            evidence
            for evidence in by_label[label].evidence
            if evidence.evidence_direction == "SUPPORTS_POTENTIAL_COMPATIBILITY"
        )
        assert positive.source_rule_excerpt.startswith("Toutes constructions")
        assert "autres que celles" in positive.source_rule_excerpt
    for label in ("AU0", "AUf0", "A", "N"):
        chapter = by_label[label]
        positive = next(
            evidence
            for evidence in chapter.evidence
            if evidence.evidence_direction == "SUPPORTS_POTENTIAL_COMPATIBILITY"
        )
        assert positive.source_rule_excerpt.startswith("Sont interdites")
        if label in {"A", "N"}:
            difficulty = next(
                evidence
                for evidence in chapter.evidence
                if evidence.evidence_direction == "SUPPORTS_DIFFICULTY"
            )
            assert difficulty.source_rule_id == positive.source_rule_id
            assert difficulty.source_rule_excerpt == positive.source_rule_excerpt


def test_real_muret_up_route_does_not_use_the_separate_icpe_condition() -> None:
    policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
    assert policy.schema_version == 5
    assert policy.policy_profile == "muret_bess_written_zoning_v6"
    chapter = next(
        item for item in policy.chapters if item.resolved_zone_chapter_label == "UP"
    )
    route = chapter.route_assessments[0]

    assert route.route_kind == "RESTRICTION_EXCEPTION_ROUTE"
    assert route.positive_evidence_ids == ("MURET-UP-PUBLIC-ROUTE-01",)
    assert route.condition_evidence_ids == ()
    assert route.difficulty_evidence_ids == ("MURET-UP-RESTRICTION-01",)

    restriction = next(
        evidence
        for evidence in chapter.evidence
        if evidence.evidence_id == "MURET-UP-RESTRICTION-01"
    )
    assert restriction.evidence_kind == "USE_RESTRICTION"
    assert restriction.evidence_direction == "SUPPORTS_DIFFICULTY"
    assert restriction.section_id == "SECTION-0080"
    assert restriction.page_number == 71
    assert (
        restriction.exact_raw_excerpt
        == "Toutes constructions ou  installations autres que celles"
    )
    assert restriction.excerpt_start == 68
    assert restriction.excerpt_end == 124
    assert restriction.excerpt_sha256 == (
        "edfbe54799b8a6c0e74d86b0e9596e8c68471f11105783b3e4e93825f8308462"
    )
    assert restriction.section_page_fragment_sha256 == (
        "06f8ea334a2fa8ce62337d6a3c59d24e03f9d8b9d8cc9e936c92e97b771babbb"
    )
    assert restriction.source_rule_id == "MURET-UP-ROUTE-RULE-01"
    assert restriction.source_rule_start == 68
    assert restriction.source_rule_end == 236
    assert restriction.source_rule_sha256 == (
        "de2615e25b83708c84e9ff9313060dca708ca0a8bc693777b627951bc2de394c"
    )


def test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite() -> None:
    policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
    chapter = next(
        item for item in policy.chapters if item.resolved_zone_chapter_label == "AUp"
    )
    route = chapter.route_assessments[0]

    assert route.route_kind == "CONDITIONAL_ROUTE"
    assert route.positive_evidence_ids == ("MURET-AUP-PUBLIC-ROUTE-01",)
    assert route.condition_evidence_ids == ("MURET-AUP-INFRASTRUCTURE-CONDITION-01",)
    assert route.difficulty_evidence_ids == ()

    prerequisite = next(
        evidence
        for evidence in chapter.evidence
        if evidence.evidence_id == "MURET-AUP-INFRASTRUCTURE-CONDITION-01"
    )
    exact_rule = (
        "Les constructions et opérations ne pourront être autorisées qu’après "
        "réalisation des  \n"
        "équipements d’infrastructure indispensable à leur fonctionnement "
        "(accès, voirie et  \n"
        "réseaux divers) conformément aux articles AUp3 et AUp4."
    )
    assert prerequisite.evidence_kind == "ACCESS_OR_NETWORK_CONDITION"
    assert prerequisite.evidence_direction == "CONDITION"
    assert prerequisite.section_id == "SECTION-0111"
    assert prerequisite.page_number == 93
    assert prerequisite.exact_raw_excerpt == exact_rule
    assert prerequisite.excerpt_start == 98
    assert prerequisite.excerpt_end == 325
    assert prerequisite.excerpt_sha256 == (
        "b2be9b1f7e3597802d5ed2c301a7e34bb7a9eecaeab55898e55306719b1b315b"
    )
    assert prerequisite.section_page_fragment_sha256 == (
        "57540d28148aefc320fcc8baa9a92df7e382d72299da6e804a3ebfaf52408b44"
    )
    assert prerequisite.source_rule_id == "MURET-AUp-INFRASTRUCTURE-RULE-01"
    assert prerequisite.source_rule_excerpt == exact_rule
    assert prerequisite.source_rule_start == 98
    assert prerequisite.source_rule_end == 325
    assert prerequisite.source_rule_sha256 == prerequisite.excerpt_sha256


def test_real_muret_up_and_aup_keep_icpe_applicability_as_context() -> None:
    policy = load_bess_zoning_policy_config(
        Path("configs/planning/muret_bess_zoning_policy.yaml")
    )
    chapters = {
        chapter.resolved_zone_chapter_label: chapter for chapter in policy.chapters
    }
    identities = {
        "UP": "MURET-UP-ICPE-CONDITION-01",
        "AUp": "MURET-AUP-ICPE-CONDITION-01",
    }

    for label, evidence_id in identities.items():
        chapter = chapters[label]
        evidence = next(
            item for item in chapter.evidence if item.evidence_id == evidence_id
        )
        assert evidence.evidence_kind == "ICPE_RULE"
        assert evidence.evidence_direction == "CONTEXT_ONLY"
        assert "ICPE" in chapter.missing_information
        for route in chapter.route_assessments:
            linked_ids = (
                route.positive_evidence_ids
                + route.condition_evidence_ids
                + route.difficulty_evidence_ids
            )
            assert evidence_id not in linked_ids


def test_absent_excerpt_and_section_page_mismatch_are_rejected(inputs) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    excerpt = "Not present in the indexed source."
    payload["chapters"][0]["evidence"][0]["exact_raw_excerpt"] = excerpt
    payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = sha256(
        excerpt.encode()
    ).hexdigest()
    with pytest.raises(BessZoningPrecheckError, match="offsets"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
    payload = _payload(policy)
    for evidence in payload["chapters"][0]["evidence"]:
        evidence["page_number"] = 3
    with pytest.raises(BessZoningPrecheckError, match="section/page fragment"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))


def test_excerpt_hash_and_length_are_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = "f" * 64
    with pytest.raises(ValueError, match="excerpt SHA256 differs"):
        BessZoningPolicyConfig.model_validate(payload)
    payload = _payload(inputs[-1])
    excerpt = "x" * 601
    payload["chapters"][0]["evidence"][0]["exact_raw_excerpt"] = excerpt
    payload["chapters"][0]["evidence"][0]["excerpt_sha256"] = sha256(
        excerpt.encode()
    ).hexdigest()
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)


@pytest.mark.parametrize(
    "status", ["POTENTIALLY_COMPATIBLE", "LIKELY_DIFFICULT", "UNKNOWN"]
)
def test_declared_status_must_equal_derived_route_status(inputs, status: str) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = status
    with pytest.raises(ValueError, match="differs from coherent linked route"):
        BessZoningPolicyConfig.model_validate(payload)


def test_condition_alone_cannot_create_conditional_review(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
    payload["chapters"][0]["evidence"] = [payload["chapters"][0]["evidence"][1]]
    payload["chapters"][0]["route_assessments"] = []
    with pytest.raises(ValueError, match="coherent linked route"):
        BessZoningPolicyConfig.model_validate(payload)


def test_unrelated_positive_and_condition_do_not_create_conditional_review(
    inputs,
) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    chapter["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
    chapter["route_assessments"] = [
        {
            "route_id": "ROUTE-U-DIRECT-ONLY",
            "route_kind": "DIRECT_ROUTE",
            "positive_evidence_ids": ["E-U-POSITIVE"],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": [],
            "applicability_note": "The separate condition is deliberately unlinked.",
        }
    ]
    with pytest.raises(ValueError, match="coherent|linked route"):
        BessZoningPolicyConfig.model_validate(payload)


def test_unlinked_context_only_unknown_succeeds(inputs) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    chapter["zoning_precheck_status"] = "UNKNOWN"
    chapter["zoning_precheck_confidence"] = "LOW"
    chapter["evidence"] = [chapter["evidence"][1]]
    chapter["evidence"][0]["evidence_direction"] = "CONTEXT_ONLY"
    chapter["route_assessments"] = []
    policy = BessZoningPolicyConfig.model_validate(payload)
    assert policy.chapters[0].zoning_precheck_status == "UNKNOWN"


def test_positive_condition_and_conflict_status_routes(inputs) -> None:
    payload = _payload(inputs[-1])
    assert (
        BessZoningPolicyConfig.model_validate(payload)
        .chapters[0]
        .zoning_precheck_status
        == "CONDITIONAL_REVIEW"
    )
    conflict = _payload(inputs[-1])
    conflict["chapters"][0]["evidence"][1]["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    route = conflict["chapters"][0]["route_assessments"][0]
    route["route_kind"] = "RESTRICTION_EXCEPTION_ROUTE"
    route["condition_evidence_ids"] = []
    route["difficulty_evidence_ids"] = ["E-U-CONDITION"]
    policy = BessZoningPolicyConfig.model_validate(conflict)
    assert policy.chapters[0].zoning_precheck_status == "CONDITIONAL_REVIEW"


def test_route_references_must_be_same_chapter_and_role_compatible(inputs) -> None:
    for mutation, message in (
        ("unknown", "unknown or another-chapter"),
        ("another_chapter", "unknown or another-chapter"),
        ("wrong_role", "incompatible positive role"),
    ):
        payload = _payload(inputs[-1])
        route = payload["chapters"][0]["route_assessments"][0]
        if mutation == "unknown":
            route["condition_evidence_ids"] = ["E-UNKNOWN"]
        elif mutation == "another_chapter":
            route["condition_evidence_ids"] = ["E-N-1"]
        else:
            route["route_kind"] = "DIRECT_ROUTE"
            route["positive_evidence_ids"] = ["E-U-CONDITION"]
            route["condition_evidence_ids"] = []
            payload["chapters"][0]["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"
        with pytest.raises(ValueError, match=message):
            BessZoningPolicyConfig.model_validate(payload)


def test_route_ids_are_globally_unique(inputs) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][1]["route_assessments"][0]["route_id"] = payload["chapters"][0][
        "route_assessments"
    ][0]["route_id"]
    with pytest.raises(ValueError, match="route IDs must be globally unique"):
        BessZoningPolicyConfig.model_validate(payload)


def test_unlinked_difficulty_evidence_is_rejected(inputs) -> None:
    payload = _payload(inputs[-1])
    unlinked = dict(payload["chapters"][1]["evidence"][0])
    unlinked["evidence_id"] = "E-N-UNLINKED"
    unlinked["source_rule_id"] = "RULE-N-UNLINKED"
    for field in (
        "excerpt_start",
        "excerpt_end",
        "source_rule_start",
        "source_rule_end",
    ):
        unlinked[field] += 100
    payload["chapters"][1]["evidence"] = (
        *payload["chapters"][1]["evidence"],
        unlinked,
    )

    with pytest.raises(ValueError, match="decision evidence must be linked"):
        BessZoningPolicyConfig.model_validate(payload)


def test_unlinked_positive_and_condition_evidence_are_rejected(inputs) -> None:
    for direction, evidence_index in (
        ("SUPPORTS_POTENTIAL_COMPATIBILITY", 0),
        ("CONDITION", 1),
    ):
        payload = _payload(inputs[-1])
        unlinked = dict(payload["chapters"][0]["evidence"][evidence_index])
        unlinked["evidence_id"] = f"E-U-UNLINKED-{direction}"
        unlinked["source_rule_id"] = f"RULE-U-UNLINKED-{direction}"
        for field in (
            "excerpt_start",
            "excerpt_end",
            "source_rule_start",
            "source_rule_end",
        ):
            unlinked[field] += 100
        payload["chapters"][0]["evidence"] = (
            *payload["chapters"][0]["evidence"],
            unlinked,
        )
        with pytest.raises(ValueError, match="decision evidence must be linked"):
            BessZoningPolicyConfig.model_validate(payload)


def test_context_only_evidence_must_be_unlinked(inputs) -> None:
    policy = _policy_with_context_only_evidence(inputs[-1])
    assert policy.chapters[0].evidence[1].evidence_direction == "CONTEXT_ONLY"

    payload = _payload(policy)
    payload["chapters"][0]["route_assessments"][0]["condition_evidence_ids"] = [
        "E-U-CONDITION"
    ]
    payload["chapters"][0]["route_assessments"][0]["route_kind"] = "CONDITIONAL_ROUTE"
    payload["chapters"][0]["zoning_precheck_status"] = "CONDITIONAL_REVIEW"
    with pytest.raises(ValueError):
        BessZoningPolicyConfig.model_validate(payload)


def test_one_evidence_may_link_to_multiple_compatible_routes(inputs) -> None:
    payload = _payload(inputs[-1])
    route = dict(payload["chapters"][1]["route_assessments"][0])
    route["route_id"] = "ROUTE-N-DIFFICULT-SECOND"
    payload["chapters"][1]["route_assessments"] = (
        *payload["chapters"][1]["route_assessments"],
        route,
    )
    policy = BessZoningPolicyConfig.model_validate(payload)
    *sources, _ = inputs
    result = interpret_bess_zoning(*sources, policy)
    evidence = result.evidence_catalog.set_index("evidence_id").loc["E-N-1"]
    assert evidence["linked_route_ids"] == (
        "ROUTE-N-DIFFICULT",
        "ROUTE-N-DIFFICULT-SECOND",
    )
    assert evidence["linked_route_roles"] == ("DIFFICULTY", "DIFFICULTY")


def test_difficulty_and_positive_only_status_routes(inputs) -> None:
    difficult = _payload(inputs[-1])
    chapter = difficult["chapters"][0]
    chapter["zoning_precheck_status"] = "LIKELY_DIFFICULT"
    chapter["evidence"] = [chapter["evidence"][1]]
    chapter["evidence"][0]["evidence_direction"] = "SUPPORTS_DIFFICULTY"
    chapter["route_assessments"] = [
        {
            "route_id": "ROUTE-U-DIFFICULT",
            "route_kind": "DIFFICULTY_ONLY",
            "positive_evidence_ids": [],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": ["E-U-CONDITION"],
            "applicability_note": "Only the linked difficulty is assessed.",
        }
    ]
    assert (
        BessZoningPolicyConfig.model_validate(difficult)
        .chapters[0]
        .zoning_precheck_status
        == "LIKELY_DIFFICULT"
    )
    potential = _payload(inputs[-1])
    chapter = potential["chapters"][0]
    chapter["zoning_precheck_status"] = "POTENTIALLY_COMPATIBLE"
    chapter["evidence"] = [chapter["evidence"][0]]
    chapter["route_assessments"] = [
        {
            "route_id": "ROUTE-U-DIRECT",
            "route_kind": "DIRECT_ROUTE",
            "positive_evidence_ids": ["E-U-POSITIVE"],
            "condition_evidence_ids": [],
            "difficulty_evidence_ids": [],
            "applicability_note": "Only the direct linked route is assessed.",
        }
    ]
    assert (
        BessZoningPolicyConfig.model_validate(potential)
        .chapters[0]
        .zoning_precheck_status
        == "POTENTIALLY_COMPATIBLE"
    )


def test_incomplete_review_requires_unknown_low(inputs) -> None:
    payload = _payload(inputs[-1])
    chapter = payload["chapters"][0]
    chapter["review_completeness"] = "INCOMPLETE"
    chapter["zoning_precheck_status"] = "UNKNOWN"
    chapter["zoning_precheck_confidence"] = "LOW"
    chapter["evidence"] = []
    chapter["route_assessments"] = []
    chapter["reviewed_section_ids"] = []
    assert (
        BessZoningPolicyConfig.model_validate(payload).chapters[0].review_completeness
        == "INCOMPLETE"
    )
    for field, value in (
        ("zoning_precheck_status", "CONDITIONAL_REVIEW"),
        ("zoning_precheck_confidence", "MEDIUM"),
    ):
        invalid = _payload(inputs[-1])
        candidate = invalid["chapters"][0]
        candidate["review_completeness"] = "INCOMPLETE"
        candidate["zoning_precheck_status"] = "UNKNOWN"
        candidate["zoning_precheck_confidence"] = "LOW"
        candidate["evidence"] = []
        candidate["route_assessments"] = []
        candidate["reviewed_section_ids"] = []
        candidate[field] = value
        with pytest.raises(ValueError, match="incomplete review"):
            BessZoningPolicyConfig.model_validate(invalid)


def test_incomplete_review_persists_exact_missing_required_sections(inputs) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    chapter = payload["chapters"][0]
    chapter["review_completeness"] = "INCOMPLETE"
    chapter["reviewed_section_ids"] = []
    chapter["zoning_precheck_status"] = "UNKNOWN"
    chapter["zoning_precheck_confidence"] = "LOW"
    chapter["evidence"] = []
    chapter["route_assessments"] = []
    result = interpret_bess_zoning(
        *sources,
        BessZoningPolicyConfig.model_validate(payload),
    )
    row = result.chapter_policy.set_index("resolved_zone_chapter_label").loc["U"]
    assert row["reviewed_section_ids"] == ()
    expected_missing = tuple(
        inputs[1].sections.loc[
            inputs[1].sections["section_type"].eq("ARTICLE")
            & inputs[1].sections["zone_chapter_label"].eq("U"),
            "section_id",
        ]
    )
    assert row["missing_required_section_ids"] == expected_missing
    assert row["zoning_precheck_status"] == "UNKNOWN"
    assert row["zoning_precheck_confidence"] == "LOW"


def test_unknown_is_accepted_when_evidence_is_insufficient(inputs) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    payload["chapters"][0]["zoning_precheck_status"] = "UNKNOWN"
    payload["chapters"][0]["evidence"] = []
    payload["chapters"][0]["route_assessments"] = []
    result = interpret_bess_zoning(
        *sources, BessZoningPolicyConfig.model_validate(payload)
    )
    assert result.chapter_policy.iloc[0]["zoning_precheck_status"] == "UNKNOWN"


def test_reviewed_sections_cover_required_articles(inputs) -> None:
    *sources, policy = inputs
    index, structure = inputs[:2]
    payload = _payload(policy)
    chapter_id = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
        & structure.sections["zone_chapter_label"].eq("U"),
        "section_id",
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] = [chapter_id]
    with pytest.raises(BessZoningPrecheckError, match="omits required reviewed"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))
    assert index.document_id == "doc-1"


@pytest.mark.parametrize("article_number", ["1", "2"])
def test_every_configured_article_must_exist_once_in_every_chapter(
    inputs,
    article_number: str,
) -> None:
    structure = inputs[1]
    policy = inputs[-1]
    keep = ~(
        structure.sections["section_type"].eq("ARTICLE")
        & structure.sections["zone_chapter_label"].eq("U")
        & structure.sections["article_number_raw"].eq(article_number)
    )
    changed = replace(
        structure,
        sections=structure.sections.loc[keep].reset_index(drop=True),
    )

    with pytest.raises(BessZoningPrecheckError, match="exactly one.*article"):
        interpret_module._required_section_ids_by_chapter(changed, policy)


def test_duplicate_configured_article_is_rejected(inputs) -> None:
    structure = inputs[1]
    duplicate = (
        structure.sections.loc[
            structure.sections["section_type"].eq("ARTICLE")
            & structure.sections["zone_chapter_label"].eq("U")
            & structure.sections["article_number_raw"].eq("2")
        ]
        .iloc[0]
        .copy()
    )
    duplicate["section_id"] = "SECTION-DUPLICATE-U-2"
    changed = replace(
        structure,
        sections=pd.concat(
            [structure.sections, duplicate.to_frame().T], ignore_index=True
        ),
    )

    with pytest.raises(BessZoningPrecheckError, match="exactly one.*article"):
        interpret_module._required_section_ids_by_chapter(changed, inputs[-1])


def test_configured_article_with_wrong_chapter_parent_is_rejected(inputs) -> None:
    structure = inputs[1]
    sections = structure.sections.copy(deep=True)
    n_chapter_id = sections.loc[
        sections["section_type"].eq("ZONE_CHAPTER")
        & sections["zone_chapter_label"].eq("N"),
        "section_id",
    ].iloc[0]
    target = (
        sections["section_type"].eq("ARTICLE")
        & sections["zone_chapter_label"].eq("U")
        & sections["article_number_raw"].eq("2")
    )
    sections.loc[target, "parent_section_id"] = n_chapter_id
    changed = replace(structure, sections=sections)

    with pytest.raises(BessZoningPrecheckError, match="exactly one.*article"):
        interpret_module._required_section_ids_by_chapter(changed, inputs[-1])


def test_evidence_must_be_inside_reviewed_sections(inputs) -> None:
    *sources, policy = inputs
    structure = inputs[1]
    payload = _payload(policy)
    payload["required_zone_article_numbers"] = ["2"]
    chapter_id = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
        & structure.sections["zone_chapter_label"].eq("U"),
        "section_id",
    ].iloc[0]
    article_2_id = structure.sections.loc[
        structure.sections["section_type"].eq("ARTICLE")
        & structure.sections["zone_chapter_label"].eq("U")
        & structure.sections["article_number_raw"].eq("2"),
        "section_id",
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] = [chapter_id, article_2_id]
    with pytest.raises(BessZoningPrecheckError, match="outside reviewed sections"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))


def test_review_cannot_claim_another_chapter_section(inputs) -> None:
    *sources, policy = inputs
    structure = inputs[1]
    payload = _payload(policy)
    n_article = structure.sections.loc[
        structure.sections["section_type"].eq("ARTICLE")
        & structure.sections["zone_chapter_label"].eq("N"),
        "section_id",
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] += (n_article,)
    with pytest.raises(BessZoningPrecheckError, match="another chapter"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))


def test_general_section_review_is_explicit_and_valid(inputs) -> None:
    *sources, policy = inputs
    structure = inputs[1]
    payload = _payload(policy)
    general_id = structure.sections.loc[
        structure.sections["section_type"].eq("GENERAL"), "section_id"
    ].iloc[0]
    payload["chapters"][0]["reviewed_section_ids"] += (general_id,)
    result = interpret_bess_zoning(
        *sources, BessZoningPolicyConfig.model_validate(payload)
    )
    reviewed = result.chapter_policy.set_index("resolved_zone_chapter_label").loc[
        "U", "reviewed_section_ids"
    ]
    assert general_id in reviewed


def test_same_general_occurrence_may_be_scoped_to_different_chapters(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    general = structure.sections.loc[
        structure.sections["section_type"].eq("GENERAL")
    ].iloc[0]
    fragment = (
        planning_regulation_section_page_fragments(
            index, zones, relations, config, structure
        )
        .set_index(["section_id", "page_number"])
        .loc[(general["section_id"], 1)]
    )
    excerpt = "General factual text."
    start = fragment["raw_text"].index(excerpt)
    base = {
        "section_id": general["section_id"],
        "page_number": 1,
        "evidence_kind": "TECHNICAL_EQUIPMENT_RULE",
        "evidence_direction": "CONTEXT_ONLY",
        "exact_raw_excerpt": excerpt,
        "excerpt_sha256": sha256(excerpt.encode()).hexdigest(),
        "section_page_fragment_sha256": fragment["section_page_fragment_sha256"],
        "excerpt_start": start,
        "excerpt_end": start + len(excerpt),
        "source_rule_id": "RULE-GENERAL-CONTEXT",
        "source_rule_excerpt": excerpt,
        "source_rule_sha256": sha256(excerpt.encode()).hexdigest(),
        "source_rule_start": start,
        "source_rule_end": start + len(excerpt),
        "interpretation_note": "The same factual GENERAL occurrence is chapter-scoped.",
    }
    payload = _payload(policy)
    for chapter, evidence_id in zip(
        payload["chapters"],
        ("E-U-GENERAL-CONTEXT", "E-N-GENERAL-CONTEXT"),
        strict=True,
    ):
        chapter["reviewed_section_ids"] = (
            *chapter["reviewed_section_ids"],
            general["section_id"],
        )
        chapter["evidence"] = (
            *chapter["evidence"],
            {**base, "evidence_id": evidence_id},
        )
    scoped_policy = BessZoningPolicyConfig.model_validate(payload)
    result = interpret_bess_zoning(
        index,
        structure,
        config,
        zones,
        relations,
        parcels,
        planning_document,
        scoped_policy,
    )
    scoped = result.evidence_catalog.loc[
        result.evidence_catalog["section_id"].eq(general["section_id"])
        & result.evidence_catalog["excerpt_start"].eq(start)
    ]
    assert set(scoped["resolved_zone_chapter_label"]) == {"U", "N"}
    assert len(scoped) == 2


def test_exact_section_page_occurrence_is_auditable(inputs, valid_result) -> None:
    index, structure, config, zones, relations, *_ = inputs
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    for row in valid_result.evidence_catalog.to_dict("records"):
        fragment = fragments.loc[(row["section_id"], row["page_number"])]
        assert (
            row["section_page_fragment_sha256"]
            == fragment["section_page_fragment_sha256"]
        )
        assert (
            fragment["raw_text"][row["excerpt_start"] : row["excerpt_end"]]
            == row["exact_raw_excerpt"]
        )


def test_repeated_excerpt_occurrence_is_bound_to_policy(inputs, valid_result) -> None:
    index, structure, config, zones, relations, *_ = inputs
    row_index = valid_result.evidence_catalog.index[
        valid_result.evidence_catalog["evidence_id"].eq("E-U-POSITIVE")
    ][0]
    row = valid_result.evidence_catalog.loc[row_index]
    fragments = planning_regulation_section_page_fragments(
        index, zones, relations, config, structure
    ).set_index(["section_id", "page_number"])
    raw = fragments.loc[(row["section_id"], row["page_number"]), "raw_text"]
    first = raw.index(row["exact_raw_excerpt"])
    second = raw.index(row["exact_raw_excerpt"], first + 1)
    assert second > first

    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.loc[row_index, "excerpt_start"] = second
    catalog.loc[row_index, "excerpt_end"] = second + len(row["exact_raw_excerpt"])
    coordinated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, coordinated)


@pytest.mark.parametrize("mutation", ["page", "fragment_hash", "start", "end"])
def test_wrong_occurrence_identity_is_rejected(inputs, mutation: str) -> None:
    *sources, policy = inputs
    payload = _payload(policy)
    evidence = payload["chapters"][0]["evidence"][0]
    if mutation == "page":
        for related in payload["chapters"][0]["evidence"]:
            related["page_number"] = 1
    elif mutation == "fragment_hash":
        for related in payload["chapters"][0]["evidence"]:
            related["section_page_fragment_sha256"] = "f" * 64
    elif mutation == "start":
        evidence["excerpt_start"] += 1
    else:
        evidence["excerpt_end"] -= 1
    with pytest.raises(BessZoningPrecheckError, match="fragment|offset"):
        interpret_bess_zoning(*sources, BessZoningPolicyConfig.model_validate(payload))


def test_exact_and_alias_mappings_are_inherited_without_prefix_logic(
    valid_result,
) -> None:
    policies = valid_result.source_zone_policy.set_index("source_zone_label_raw")
    assert policies.loc["U", "mapping_status"] == "EXACT"
    assert policies.loc["Ua", "mapping_status"] == "CONFIG_ALIAS"
    assert policies.loc["Ua", "resolved_zone_chapter_label"] == "U"
    assert (
        policies.loc["Ua", "zoning_precheck_status"]
        == policies.loc["U", "zoning_precheck_status"]
    )


def test_unmapped_dominant_zone_is_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    mapping = structure.zone_mapping.copy()
    mapping.loc[
        mapping["source_zone_label_raw"].eq("U"),
        [
            "resolved_zone_chapter_label",
            "matched_section_id",
        ],
    ] = None
    mapping.loc[mapping["source_zone_label_raw"].eq("U"), "mapping_status"] = "UNMAPPED"
    mapping.loc[mapping["source_zone_label_raw"].eq("U"), "mapping_method"] = "NONE"
    mutated = _structure_with_hashes(replace(structure, zone_mapping=mapping))
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        mutated.structure_result_content_sha256
                    )
                }
            )
        },
    )
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            mutated,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            changed_policy,
        )


def test_link_table_exactly_reproduces_routes_and_reverse_links(valid_result) -> None:
    expected = {
        ("ROUTE-U-CONDITIONAL", "E-U-POSITIVE", "POSITIVE"),
        ("ROUTE-U-CONDITIONAL", "E-U-CONDITION", "CONDITION"),
        ("ROUTE-N-DIFFICULT", "E-N-1", "DIFFICULTY"),
    }
    actual = {
        (row.route_id, row.evidence_id, row.route_role)
        for row in valid_result.evidence_route_links.itertuples(index=False)
    }
    assert actual == expected
    catalog = valid_result.evidence_catalog.set_index("evidence_id")
    assert catalog.loc["E-U-POSITIVE", "linked_route_ids"] == ("ROUTE-U-CONDITIONAL",)
    assert catalog.loc["E-U-POSITIVE", "linked_route_roles"] == ("POSITIVE",)
    assert bool(catalog["decision_linked"].all())


def test_context_evidence_is_separate_from_decision_outputs(inputs) -> None:
    *sources, policy = inputs
    context_policy = _policy_with_context_only_evidence(policy)
    result = interpret_bess_zoning(*sources, context_policy)
    catalog = result.evidence_catalog.set_index("evidence_id")
    context = catalog.loc["E-U-CONDITION"]
    assert context["linked_route_ids"] == ()
    assert context["linked_route_roles"] == ()
    assert not bool(context["decision_linked"])
    chapter = result.chapter_policy.set_index("resolved_zone_chapter_label").loc["U"]
    assert chapter["evidence_ids"] == ("E-U-POSITIVE", "E-U-CONDITION")
    assert chapter["decision_evidence_ids"] == ("E-U-POSITIVE",)
    assert chapter["context_evidence_ids"] == ("E-U-CONDITION",)
    source = result.source_zone_policy.set_index("source_zone_label_raw").loc["U"]
    assert source["decision_evidence_ids"] == ("E-U-POSITIVE",)
    assert source["context_evidence_ids"] == ("E-U-CONDITION",)
    relation = result.parcel_zone_interpretations.loc[
        result.parcel_zone_interpretations["resolved_zone_chapter_label"].eq("U")
    ].iloc[0]
    assert relation["decision_evidence_ids"] == ("E-U-POSITIVE",)
    assert relation["context_evidence_ids"] == ("E-U-CONDITION",)
    parcel = result.parcels.loc[result.parcels["parcel_id"].eq("P-1")].iloc[0]
    assert parcel["zoning_precheck_evidence_ids"] == ("E-U-POSITIVE",)
    assert parcel["zoning_precheck_context_evidence_ids"] == ("E-U-CONDITION",)


def test_parcel_aggregation_preserves_conflicts_and_touch_only(valid_result) -> None:
    parcels = valid_result.parcels.set_index("parcel_id")
    assert parcels.loc["P-1", "zoning_precheck_status"] == "CONDITIONAL_REVIEW"
    assert parcels.loc["P-1", "positive_area_zone_count"] == 1
    assert parcels.loc["P-2", "zoning_precheck_status"] == "CONDITIONAL_REVIEW"
    assert parcels.loc["P-2", "positive_area_zone_count"] == 2
    assert parcels.loc["P-2", "distinct_zone_status_count"] == 1
    assert parcels.loc["P-3", "zoning_precheck_status"] == "MIXED_REVIEW_REQUIRED"
    assert parcels.loc["P-3", "dominant_zone_precheck_status"] == "CONDITIONAL_REVIEW"
    assert parcels.loc["P-3", "non_dominant_different_status_count"] == 1
    assert parcels.loc["P-4", "zoning_precheck_status"] == "UNKNOWN"
    assert parcels.loc["P-4", "positive_area_zone_count"] == 0
    assert parcels.loc["P-4", "touch_only_zone_count"] == 1
    assert pd.isna(parcels.loc["P-4", "dominant_zone_precheck_status"])
    assert valid_result.touch_only_relation_count == 1
    assert "P-4" not in set(valid_result.parcel_zone_interpretations["parcel_id"])


def test_prior_parcel_fields_geometry_order_index_and_crs_are_preserved(
    inputs, valid_result
) -> None:
    original = inputs[5]
    prior = valid_result.parcels.loc[:, original.columns]
    assert_geodataframe_equal(prior, original)
    assert valid_result.parcels.index.equals(original.index)
    assert valid_result.parcels.crs == original.crs
    assert valid_result.parcels["planning_surface_relation_count"].equals(
        original["planning_surface_relation_count"]
    )
    assert (
        valid_result.parcels["non_zoning_planning_features_interpreted"].eq(False).all()
    )
    assert valid_result.parcels["zoning_precheck_requires_formal_review"].eq(True).all()


def test_inputs_are_not_mutated(inputs) -> None:
    _, structure, _, zones, relations, parcels, _, _ = inputs
    zone_snapshot = zones.copy(deep=True)
    relation_snapshot = relations.copy(deep=True)
    parcel_snapshot = parcels.copy(deep=True)
    section_snapshot = structure.sections.copy(deep=True)
    interpret_bess_zoning(*inputs)
    pd.testing.assert_frame_equal(zones, zone_snapshot)
    pd.testing.assert_frame_equal(relations, relation_snapshot)
    assert_geodataframe_equal(parcels, parcel_snapshot)
    pd.testing.assert_frame_equal(structure.sections, section_snapshot)


def test_policy_change_after_result_creation_is_rejected(inputs, valid_result) -> None:
    payload = _payload(inputs[-1])
    payload["chapters"][0]["rationale"] = "Changed checked-in rationale."
    changed = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError, match="policy_config_sha256"):
        validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)


def test_evidence_change_after_result_creation_is_rejected(
    inputs, valid_result
) -> None:
    payload = _payload(inputs[-1])
    excerpt = "equipment is permitted"
    evidence = payload["chapters"][0]["evidence"][0]
    evidence["exact_raw_excerpt"] = excerpt
    evidence["excerpt_sha256"] = sha256(excerpt.encode()).hexdigest()
    evidence["excerpt_start"] += len("Technical ")
    changed = BessZoningPolicyConfig.model_validate(payload)
    with pytest.raises(BessZoningPrecheckError):
        validate_bess_zoning_precheck(*inputs[:-1], changed, valid_result)


def test_zoning_relation_and_zone_mapping_changes_are_rejected(
    inputs, valid_result
) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed_relations = relations.copy()
    changed_relations.loc[0, "intersection_area_m2"] = 99.0
    changed_relations.loc[0, "parcel_share_pct"] = 99.0
    changed_relations.loc[0, "zone_share_pct"] = 9.9
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        validate_bess_zoning_precheck(
            index,
            structure,
            config,
            zones,
            changed_relations,
            parcels,
            planning_document,
            policy,
            valid_result,
        )


def test_structure_config_and_hierarchy_changes_are_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed_config = config.model_copy(update={"structure_profile": "changed"})
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            structure,
            changed_config,
            zones,
            relations,
            parcels,
            planning_document,
            policy,
        )
    changed_sections = structure.sections.copy(deep=True)
    article = changed_sections["section_type"].eq("ARTICLE")
    changed_sections.loc[article.idxmax(), "parent_section_id"] = "SECTION-UNKNOWN"
    changed_structure = _structure_with_hashes(
        replace(structure, sections=changed_sections)
    )
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        changed_structure.structure_result_content_sha256
                    )
                }
            )
        }
    )
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            changed_structure,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            changed_policy,
        )


def test_public_source_complete_validator_is_invoked(inputs, monkeypatch) -> None:
    calls = 0
    original = interpret_module.validate_planning_regulation_structure_with_fragments

    def counted(*args, **kwargs):
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)

    monkeypatch.setattr(
        interpret_module,
        "validate_planning_regulation_structure_with_fragments",
        counted,
    )
    interpret_bess_zoning(*inputs)
    assert calls >= 1


def test_one_precheck_build_performs_one_zoning_source_complete_validation(
    inputs,
    monkeypatch,
) -> None:
    calls = 0

    def counted(*args) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        interpret_module,
        "validate_normalized_planning_zoning_inputs",
        counted,
    )

    interpret_bess_zoning(*inputs)

    assert calls == 1


def test_invalid_physical_zoning_fails_before_policy_interpretation(
    inputs,
    monkeypatch,
) -> None:
    policy_calls = 0

    def invalid_source(*args) -> None:
        raise interpret_module.PlanningZoningError("physical source invalid")

    def counted_policy(*args):
        nonlocal policy_calls
        policy_calls += 1
        return inputs[-1]

    monkeypatch.setattr(
        interpret_module,
        "validate_normalized_planning_zoning_inputs",
        invalid_source,
    )
    monkeypatch.setattr(interpret_module, "_resolved_policy", counted_policy)

    with pytest.raises(BessZoningPrecheckError, match="physical source invalid"):
        interpret_bess_zoning(*inputs)

    assert policy_calls == 0


def test_one_build_result_performs_one_factual_structure_rebuild(
    inputs, monkeypatch
) -> None:
    calls = 0
    original = interpret_module.validate_planning_regulation_structure_with_fragments

    def counted(*args, **kwargs):
        nonlocal calls
        calls += 1
        return original(*args, **kwargs)

    monkeypatch.setattr(
        interpret_module,
        "validate_planning_regulation_structure_with_fragments",
        counted,
    )
    interpret_module._build_result(*inputs[:6], inputs[-1])
    assert calls == 1


@pytest.mark.parametrize(
    "column",
    ["parcel_metric_area_m2", "zone_area_m2"],
)
def test_relation_area_denominators_are_required(inputs, column: str) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    with pytest.raises(BessZoningPrecheckError):
        interpret_bess_zoning(
            index,
            structure,
            config,
            zones,
            relations.drop(columns=column),
            parcels,
            planning_document,
            policy,
        )


@pytest.mark.parametrize(
    "column",
    ["parcel_share_pct", "zone_share_pct"],
)
def test_relation_percentages_must_match_denominators(inputs, column: str) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed = relations.copy(deep=True)
    changed.loc[0, column] += 1.0
    with pytest.raises(BessZoningPrecheckError):
        interpret_bess_zoning(
            index,
            structure,
            config,
            zones,
            changed,
            parcels,
            planning_document,
            policy,
        )


def test_factual_zone_mapping_counts_are_recomputed(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed_mapping = structure.zone_mapping.copy(deep=True)
    changed_mapping.loc[0, "candidate_intersection_count"] += 1
    changed_structure = _structure_with_hashes(
        replace(structure, zone_mapping=changed_mapping)
    )
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        changed_structure.structure_result_content_sha256
                    )
                }
            )
        }
    )
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            changed_structure,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            changed_policy,
        )
    changed_mapping = structure.zone_mapping.copy()
    changed_mapping.loc[0, "source_zone_label_raw"] = "CHANGED"
    changed_structure = _structure_with_hashes(
        replace(structure, zone_mapping=changed_mapping)
    )
    changed_policy = policy.model_copy(
        update={
            "source_lock": policy.source_lock.model_copy(
                update={
                    "structure_result_content_sha256": (
                        changed_structure.structure_result_content_sha256
                    )
                }
            )
        },
    )
    with pytest.raises(BessZoningPrecheckError):
        validate_bess_zoning_precheck(
            index,
            changed_structure,
            config,
            zones,
            relations,
            parcels,
            planning_document,
            changed_policy,
            valid_result,
        )


def test_coordinated_result_mutation_is_rejected(inputs, valid_result) -> None:
    chapter = valid_result.chapter_policy.copy(deep=True)
    chapter.loc[0, "zoning_precheck_confidence"] = "HIGH"
    mutated = _result_with_hashes(replace(valid_result, chapter_policy=chapter))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


def test_coordinated_evidence_catalog_mutation_is_rejected(
    inputs, valid_result
) -> None:
    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.loc[0, "interpretation_note"] = "Coordinated mutation."
    mutated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


def test_coordinated_catalog_occurrence_duplicate_is_rejected(
    inputs, valid_result
) -> None:
    catalog = valid_result.evidence_catalog.copy(deep=True)
    occurrence_columns = [
        "resolved_zone_chapter_label",
        "section_id",
        "page_number",
        "section_page_fragment_sha256",
        "excerpt_start",
        "excerpt_end",
    ]
    catalog.loc[catalog.index[1], occurrence_columns] = catalog.loc[
        catalog.index[0], occurrence_columns
    ].to_numpy()
    mutated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(
        BessZoningPrecheckError,
        match="duplicate chapter-scoped evidence occurrence",
    ):
        _validate(inputs, mutated)


def test_coordinated_route_table_mutation_is_rejected(inputs, valid_result) -> None:
    routes = valid_result.route_assessments.copy(deep=True)
    routes.loc[0, "applicability_note"] = "Coordinated route mutation."
    mutated = _result_with_hashes(replace(valid_result, route_assessments=routes))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


def test_coordinated_evidence_route_link_mutation_is_rejected(
    inputs, valid_result
) -> None:
    links = valid_result.evidence_route_links.copy(deep=True)
    links.loc[0, "route_role"] = "BROKEN"
    mutated = _result_with_hashes(replace(valid_result, evidence_route_links=links))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


def test_coordinated_reverse_link_mutation_is_rejected(inputs, valid_result) -> None:
    catalog = valid_result.evidence_catalog.copy(deep=True)
    catalog.at[0, "linked_route_roles"] = ("DIFFICULTY",)
    mutated = _result_with_hashes(replace(valid_result, evidence_catalog=catalog))
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


def test_evidence_route_link_hash_mutation_is_rejected(inputs, valid_result) -> None:
    mutated = replace(
        valid_result,
        evidence_route_links_content_sha256="f" * 64,
    )
    with pytest.raises(BessZoningPrecheckError, match="differs from rebuilt"):
        _validate(inputs, mutated)


@pytest.mark.parametrize("version", [1, 2, 3, 4])
def test_old_result_hash_schemas_are_rejected(
    inputs, valid_result, version: int
) -> None:
    with pytest.raises(BessZoningPrecheckError, match="result_hash_schema_version"):
        _validate(inputs, replace(valid_result, result_hash_schema_version=version))


def test_relation_identity_change_is_rejected(inputs) -> None:
    index, structure, config, zones, relations, parcels, planning_document, policy = (
        inputs
    )
    changed = relations.copy()
    changed.loc[0, "source_zone_id"] = "SRC-N"
    with pytest.raises(BessZoningPrecheckError, match="Factual regulation structure"):
        interpret_bess_zoning(
            index,
            structure,
            config,
            zones,
            changed,
            parcels,
            planning_document,
            policy,
        )


def test_readback_result_validates(tmp_path: Path, inputs, valid_result) -> None:
    chapter_path = tmp_path / "chapter.parquet"
    evidence_path = tmp_path / "evidence.parquet"
    route_path = tmp_path / "routes.parquet"
    link_path = tmp_path / "links.parquet"
    source_path = tmp_path / "source.parquet"
    relation_path = tmp_path / "relations.parquet"
    parcel_path = tmp_path / "parcels.parquet"
    valid_result.evidence_catalog.to_parquet(evidence_path, index=False)
    valid_result.route_assessments.to_parquet(route_path, index=False)
    valid_result.evidence_route_links.to_parquet(link_path, index=False)
    valid_result.chapter_policy.to_parquet(chapter_path, index=False)
    valid_result.source_zone_policy.to_parquet(source_path, index=False)
    valid_result.parcel_zone_interpretations.to_parquet(relation_path, index=False)
    valid_result.parcels.to_parquet(parcel_path)
    persisted = replace(
        valid_result,
        evidence_catalog=pd.read_parquet(evidence_path),
        route_assessments=pd.read_parquet(route_path),
        evidence_route_links=pd.read_parquet(link_path),
        chapter_policy=pd.read_parquet(chapter_path),
        source_zone_policy=pd.read_parquet(source_path),
        parcel_zone_interpretations=pd.read_parquet(relation_path),
        parcels=gpd.read_parquet(parcel_path),
    )
    _validate(inputs, persisted)
    occurrence_columns = [
        "resolved_zone_chapter_label",
        "section_id",
        "page_number",
        "section_page_fragment_sha256",
        "excerpt_start",
        "excerpt_end",
    ]
    assert not persisted.evidence_catalog.duplicated(occurrence_columns).any()


def test_policy_yaml_roundtrip_is_strict(tmp_path: Path, inputs) -> None:
    policy = inputs[-1]
    path = tmp_path / "policy.yaml"
    import yaml  # type: ignore[import-untyped]

    path.write_text(
        yaml.safe_dump(
            policy.model_dump(mode="json"),
            allow_unicode=True,
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    assert load_bess_zoning_policy_config(path) == policy
```
