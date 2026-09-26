# `tests/unit/test_aggregate_bess_planning_feature_policy.py`

- Source: [tests/unit/test_aggregate_bess_planning_feature_policy.py](../../../../../tests/unit/test_aggregate_bess_planning_feature_policy.py)
- Source SHA256: `52f53bc0808d49b0a50f4b09b2383af9b473308824472bfc3f6a3faf99479d83`
- Source SHA256 basis: `git-content`
- Source lines: 2211; checkout bytes equal Git content at R8 start `fcf618ca6f569db35dd0f5b55cbca986393451ea`.
- Owner: `tests.unit.test_aggregate_bess_planning_feature_policy`; semantic R8 comparison, not an independent approval.

[Paired companion](../../../../../docs/code/files/src/landscout/stages/aggregate_bess_planning_feature_policy.py.md) · [R8 evidence](../../../../../docs/code/audit/R8_BESS_CNIG_AGGREGATION.md)

## Ownership, fixtures and execution boundary

This is repository test support, not a public loader module. It has no __all__ and no locally decorated pytest fixtures. Its top-level test functions are collected/parametrized by pytest; ordinary helpers construct data and artifacts. `tmp_path` and `monkeypatch` are pytest fixtures. `_application_fixture`, `_coordinated_policy_mutation` and `_surface_touch_with_positive_area` are imported from the repository's test_apply_bess_planning_feature_policy module, not from a third-party package. Production helpers imported here retain production ownership even when called privately.

The usual fixture chain is `_aggregation_fixture` → imported `_application_fixture` → `_compiled_fixture` from test_bess_planning_feature_policy → `_integration_inputs` / `_planning_document` from test_resolve_planning_feature_codes. It creates physical synthetic GeoPackages (four related datasets plus zoning), extraction inventory/marker and inspected frames; public CNIG/policy/application/aggregation paths can reread these physical synthetic layers. The sole initial parcel is PARCEL-1, a 2-by-2 square (4 m²) in EPSG:2154, with existing_fact=7 and index 91 named parcel_row. Prescription surface P-1 is 07/00 over that square; information surface I-1 is 02/00 outside it; prescription line P-2 is 07/04 across it; information point I-2 is 99/00 outside it. The synthetic source metadata uses doc-1, archive SHA of 64 a characters and synthetic.zip of declared size 1; it is not an actual downloaded official ZIP proof.

Imported physical setup uses tempfile.mkdtemp with prefix landscout-code-source- in system temp, not exclusively pytest's isolated basetemp. Own Parquet/JSON files use tmp_path. Module-level parametrization can call `_relation` and thus create synthetic fixtures during collection. No real Muret/GPU/EP snapshot, HTTP acquisition or legal search is needed. Synthetic source config starts from a checked-in GPU config but changes matching tokens and freezes/hashes the substituted identity; synthetic CNIG profile and BESS policy are not the source-locked current production policy. The synthetic policy cycles statuses/priorities LIKELY_MATERIAL_CONSTRAINT/50, UNKNOWN/40, MATERIAL_REVIEW_REQUIRED/30, DESIGN_REVIEW_REQUIRED/20, CONTEXT_REVIEW_REQUIRED/10, and HIGH/MEDIUM/LOW confidence. Test-selected priorities are not a new business policy.

## Two different loader names and forged-frame helpers

The same-named `load_bess_planning_feature_parcel_aggregation_artifacts` in THIS test module is a legacy adapter, not the production API. It has optional upstream arguments, while production requires all five. If either optional input is absent it substitutes BOTH mutable `_LAST_SOURCE_PARCELS` / `_LAST_APPLICATION_RESULT` globals. When no usable pair exists it calls a private legacy reader; otherwise it tries the real imported alias `_load_aggregation_artifacts`, and only in legacy mode catches an aggregation error containing the exact substring `unknown feature` to fall back. That legacy reader validates manifest, captured files and local aggregation envelope but does not bind the result to external upstream objects or rebuild from them. No production compatibility behavior follows from this helper.

`_build_from_relations` makes synthetic 100-by-40 parcels (4000 m²), corrects stored parcel area/share/lineage, canonicalizes relation schema/dtypes and index by default, replaces/rehashes application relations, updates those globals and calls the private aggregation builder. It does not rebuild the application's feature catalogs to match arbitrary F-1/HIGH/LOW IDs. Therefore the real loader's application-envelope guard may reject an unknown feature before reading a manifest; only the narrow legacy fallback then reaches local artifact checks. An inherited global status/priority inconsistency may stop even earlier and never enter the fallback. Artifact-test exceptions must be read with this actual call path.

Resetting a local relation-frame variable and assigning to that copy in `_build_from_relations` does not prove mutation of its caller's frame. Similarly `.eq(geometry_kind)` is a string-domain filter, not a geometric operation. `_LAST_*` are mutable module state, not immutable configuration or production input. Fixtures can overwrite them; a three-argument adapter call does not necessarily refer to the artifact's own upstream source.

## Reading assertions without inflating proof

Each symbol entry below states the setup, exercised boundary, first possible guard and assertion limits. Local tests call private builders/envelopes and often use forged frames; public tests either delegate to real source validation or intentionally install a counter/no-op to prove it is not reached. `_result_with_hashes` repairs only output digests; `_rehash_coordinated_result` repairs source-prefix AND output digests. Neither recreates physical source truth. A stale source-prefix hash, canonical dtype, schema or application-envelope failure may precede the rule suggested by a test title.

The paired source companion gives the algorithm/models/canonical schema. No test is changed by R8. Broad raises/assertions, known legacy fallbacks and lack of real-source execution remain limitations, not automatically demonstrated production bugs. The focused execution count/warnings/final cleanup exit are recorded once in the R8 receipt; visual rendering and global semantic closure are separate pending work.

Inventory: 91 recorded function symbols, including 61 top-level tests and their nested callbacks. Parametrized case count is not this function count.

## Module declarations

Constants/type aliases below are documented in addition to the original symbol denominator (the original AST inventory excludes module assignments). They create no extra closure credit. Signatures/values are literal source excerpts, not runtime imports.

<a id="declaration-parcel-columns"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.PARCEL_COLUMNS`

Source lines 45–75. Ordered29 appended parcel columns used by test assertions. Meanings, dtypes and null rules are in the production companion's [Appended column dictionary](../../../../../docs/code/files/src/landscout/stages/aggregate_bess_planning_feature_policy.py.md#appended-column-dictionary), not in a local table here.

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

<a id="declaration-relation-columns"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.RELATION_COLUMNS`

Source lines 76–83. Ordered6 appended relation evidence columns, not the complete upstream factual relation schema. Consumed by assignment, prefix extraction and validation.

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

<a id="declaration--last-source-parcels"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._LAST_SOURCE_PARCELS`

Source lines 84–84. Mutable test-module context, initially None; overwritten by fixture/private synthetic builder and consumed by legacy adapter. Not a configuration constant or production source authority.

```python
_LAST_SOURCE_PARCELS: gpd.GeoDataFrame | None = None
```

<a id="declaration--last-application-result"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._LAST_APPLICATION_RESULT`

Source lines 85–85. Mutable test-module context, initially None; overwritten by fixture/private synthetic builder. Adapter substitutes both globals when either optional upstream is omitted; tests may leave synthetic catalog-inconsistent objects here.

```python
_LAST_APPLICATION_RESULT: object | None = None
```

## Owned symbol contracts

Each explicit anchor identifies the qualified owner in the following heading. Ranges include the definition body, not decorators. Signature excerpts are exact source text (including indentation); decorators and complete bodies are retained in the final snapshot. Field entries state the applicable parent-model boundary rather than inventing field methods or I/O.

<a id="symbol--aggregation-artifact-record-payload"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_artifact_record_payload`

Function, source lines 88–111.

```python
def _aggregation_artifact_record_payload() -> dict[str, object]:
```

Return synthetic PARCELS record payload with geometry-only schema and minimal CRS mapping. The same input CRS dict is referenced in two payload positions to exercise alias isolation. This is metadata-only JSON, not a physically measured complete frame schema or validated full CRS.

<a id="symbol-test-aggregation-artifact-record-is-deeply-immutable-without-aliases"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_aggregation_artifact_record_is_deeply_immutable_without_aliases`

Function, source lines 114–142.

```python
def test_aggregation_artifact_record_is_deeply_immutable_without_aliases() -> None:
```

Construct the record, append caller_mutation to the caller-owned schema columns and add caller_mutation=True to the caller CRS mapping. Assert retained columns == ("geometry",), absence of that key in retained CRS, and model_dump(mode="json", warnings="error") equal to a fresh _aggregation_artifact_record_payload() result. There is no saved pre-mutation dump or CRS-name mutation. Assert immediate TypeError/AttributeError for mapping item, nested tuple append, CRS item and nested coordinate_system item. Tests these four operations and alias copies; not every conceivable Python escape or frame immutability.

<a id="symbol--aggregation-fixture"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._aggregation_fixture`

Function, source lines 145–160.

```python
def _aggregation_fixture() -> tuple[
    tuple[object, ...],
    object,
    object,
    object,
    object,
    BessPlanningFeatureParcelAggregationResult,
]:
```

Build repository synthetic application fixture, call public source-complete aggregator, store parcel/application globals, return inputs/coded/config/policy/application/result. Performs delegated synthetic physical source I/O; not a no-I/O pure fixture. Used throughout tests and helper scenarios.

<a id="symbol-load-bess-planning-feature-parcel-aggregation-artifacts"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts`

Function, source lines 163–195.

```python
def load_bess_planning_feature_parcel_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
    source_parcels: gpd.GeoDataFrame | None = None,
    application_result: object | None = None,
) -> BessPlanningFeatureParcelAggregationResult:
```

Test-only legacy loader adapter with optional upstream pair. Missing either substitutes both globals; absent pair uses private legacy loader. Otherwise call real alias; fallback only for legacy mode and error containing unknown feature, re-raise all other errors. This overload is not the exported production signature. Returns result; fixture-dependent global state can determine the first guard.

<a id="symbol--load-legacy-local-aggregation-artifacts"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._load_legacy_local_aggregation_artifacts`

Function, source lines 198–223.

```python
def _load_legacy_local_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
) -> BessPlanningFeatureParcelAggregationResult:
```

Legacy local reader parses strict manifest/model, reads both byte-verified artifacts with private helper, constructs scalar result and validates its local envelope. Returns result without production upstream locks or exact-upstream rebuild. File reads here prove local captured artifact integrity only.

<a id="symbol--build-from-relations"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._build_from_relations`

Function, source lines 226–284.

```python
def _build_from_relations(
    relations: pd.DataFrame,
    *,
    parcel_ids: tuple[str, ...] = ("PARCEL-1", "PARCEL-2"),
    canonicalize_application_dtypes: bool = True,
) -> BessPlanningFeatureParcelAggregationResult:
```

Forge default PARCEL-1/PARCEL-2 4000 m² rectangles, EPSG:2154, named index and prior column; reset a local relation frame, overwrite parcel area/surface share/lineage, optionally enforce complete schema/dtypes, replace and rehash application relations, set globals, private _build_result. No source-catalog agreement proof; input rebinding is not caller-frame mutation. canonicalize_application_dtypes=False deliberately preserves potentially multiple schema defects.

<a id="symbol--relation"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._relation`

Function, source lines 287–379.

```python
def _relation(
    *,
    parcel_id: str = "PARCEL-1",
    feature_id: str = "F-1",
    relation_type: str = "AREA_OVERLAP",
    application_status: str = "APPLIED_EXACT_POLICY",
    status: str | None = "MATERIAL_REVIEW_REQUIRED",
    confidence: str | None = "HIGH",
    priority: int | None = 30,
    area: float = 0.000001,
) -> dict[str, object]:
```

Construct one relation from an imported physical application fixture, then substitute parcel/feature ID, relation type, policy status/confidence/priority and metrics. Defaults are APPLIED_EXACT_POLICY, MATERIAL_REVIEW_REQUIRED, HIGH and 30, with AREA_OVERLAP and area 1e-6. LENGTH uses line donor; other kinds start from surface donor. Unresolved nulls decision fields; point metrics/counts are synthesized. Return dict, not validated physical overlay. Repeated calls and parametrization trigger synthetic setup.

<a id="symbol--write-artifacts"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._write_artifacts`

Function, source lines 382–431.

```python
def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureParcelAggregationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
```

Test-only writer: write index-preserving parcels.parquet and relations.parquet, capture each size/SHA/schema/count, build strict manifest from result scalars and ordered roles, write aggregation.json. Returns (manifest_path, paths, manifest): a Path, a dict[str, Path] keyed by PARCELS/RELATION_ASSESSMENTS, and a dict[str, object] manifest payload. These are three tuple elements, not three paths. This fixture mutates tmp_path only; production has no corresponding writer API.

<a id="symbol--rehash-coordinated-result"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._rehash_coordinated_result`

Function, source lines 434–453.

```python
def _rehash_coordinated_result(
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

Drop aggregation suffixes into copies, recompute both source-prefix hashes, then recompute output/result hashes. Returns dataclass replacement; no domain, physical or upstream validation. Enables coordinated rather than merely stale-hash corruption tests.

<a id="symbol--duplicate-selected-pair-result"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._duplicate_selected_pair_result`

Function, source lines 456–471.

```python
def _duplicate_selected_pair_result() -> BessPlanningFeatureParcelAggregationResult:
```

Build valid selected A/B relations then forge both IDs to A and selected JSON [A]; fully rehash prefixes/outputs. Returns duplicate-pair result to test intrinsic uniqueness, not physical source agreement.

<a id="symbol--invalid-lower-feature-id-result"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._invalid_lower_feature_id_result`

Function, source lines 474–489.

```python
def _invalid_lower_feature_id_result() -> BessPlanningFeatureParcelAggregationResult:
```

Build LOW/10 and HIGH/30, forge lower-priority feature ID to /tmp/feature and fully rehash. Demonstrates invalid IDs outside selected JSON still matter; no public source validation in helper.

<a id="symbol--cross-parcel-priority-conflict-result"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._cross_parcel_priority_conflict_result`

Function, source lines 492–523.

```python
def _cross_parcel_priority_conflict_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
```

Build two parcels with LIKELY_MATERIAL_CONSTRAINT/50 and MATERIAL_REVIEW_REQUIRED/30, change latter inherited/result/parcel priority to 50 and fully rehash. Intrinsic document-wide mapping then fails even when per-parcel decisions are coherent.

<a id="symbol--surface-touch-semantic-corruption-result"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._surface_touch_semantic_corruption_result`

Function, source lines 526–543.

```python
def _surface_touch_semantic_corruption_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
```

Start from physical application fixture, mutate positive-area SURFACE relation type to TOUCH_ONLY, temporarily replace aggregation module common relation validator with bypass, build/hash private result, restore validator in finally. No permanent monkeypatch; intentionally bypasses exactly one semantic guard to construct corrupt output.

<a id="symbol--surface-touch-semantic-corruption-result-bypass"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._surface_touch_semantic_corruption_result.bypass`

Function, source lines 536–537.

```python
    def bypass(*args: object, **kwargs: object) -> None:
```

Nested no-op accepts any args/kwargs and returns None, temporarily suppressing inherited relation validation during corrupt-result construction only. Restored by its parent in finally; not a production implementation.

<a id="symbol-test-exact-relations-select-configured-max-priority-and-lowest-confidence"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_exact_relations_select_configured_max_priority_and_lowest_confidence`

Function, source lines 546–584.

```python
def test_exact_relations_select_configured_max_priority_and_lowest_confidence() -> None:
```

Synthetic LOW CONTEXT_REVIEW_REQUIRED/10 area1000 plus HIGH-A/HIGH-B LIKELY_MATERIAL_CONSTRAINT/50 area1e-6, confidences HIGH/LOW: assert max priority, minimum LOW, sorted both high IDs, selected2/lower1/distinct2/multiple true and roles. Private forged-frame path proves no area weighting and all ties, not physical intersection provenance.

<a id="symbol-test-policy-unknown-is-exact-but-unresolved-controlling-overrides"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_policy_unknown_is_exact_but_unresolved_controlling_overrides`

Function, source lines 587–611.

```python
def test_policy_unknown_is_exact_but_unresolved_controlling_overrides() -> None:
```

Exact policy UNKNOWN/40/LOW aggregates normally; adding an unresolved controlling row beside MATERIAL_REVIEW_REQUIRED/30 yields unresolved state, all three decision nulls, unresolved-ID JSON and deferred/unresolved roles. Distinguishes exact UNKNOWN from an unresolved official code pair. _build_from_relations exercises the private builder and its internal guards, not the aggregation _validate_result_envelope in this scenario.

<a id="symbol-test-every-positive-relation-type-controls-without-threshold"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_every_positive_relation_type_controls_without_threshold`

Function, source lines 615–625.

```python
def test_every_positive_relation_type_controls_without_threshold(
    relation_type: str,
) -> None:
```

Parametrize AREA_OVERLAP, LENGTH_OVERLAP, INSIDE, using area/length 1e-15 where applicable and point count1. Assert controlling count1 and SELECTED_CONTROLLING role; exact state is implied by construction but not directly asserted here. Shared metric validation runs first. This uses forged relations, not tiny-geometry physical overlay measurement.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize("relation_type", ["AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"])
```

<a id="symbol-test-boundary-only-relations-are-contextual"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_boundary_only_relations_are_contextual`

Function, source lines 629–640.

```python
def test_boundary_only_relations_are_contextual(relation_type: str) -> None:
```

Parametrize TOUCH_ONLY and BOUNDARY_TOUCH; assert contacts-only state, null decision, [F-1] touch evidence and TOUCH_ONLY_CONTEXT role. Intrinsic kind/type/count guards precede aggregation; forged-row local evidence only.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize("relation_type", ["TOUCH_ONLY", "BOUNDARY_TOUCH"])
```

<a id="symbol-test-touch-relation-remains-context-beside-a-controlling-relation"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_touch_relation_remains_context_beside_a_controlling_relation`

Function, source lines 643–663.

```python
def test_touch_relation_remains_context_beside_a_controlling_relation() -> None:
```

Higher-priority LIKELY_MATERIAL_CONSTRAINT contact cannot displace MATERIAL_REVIEW_REQUIRED controlling evidence. Assert controlling parcel status and contact role. No general legal access or clearance conclusion follows.

<a id="symbol-test-no-relation-parcel-is-retained-without-a-decision"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_no_relation_parcel_is_retained_without_a_decision`

Function, source lines 666–671.

```python
def test_no_relation_parcel_is_retained_without_a_decision() -> None:
```

Default second parcel has no relations; assert it is retained, NO_PLANNING_FEATURE_RELATION, null status and formal review required. Does not assert that absence of mapped relations proves absence of constraints.

<a id="symbol-test-parcel-and-relation-prefixes-order-and-inputs-are-preserved"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_parcel_and_relation_prefixes_order_and_inputs_are_preserved`

Function, source lines 674–695.

```python
def test_parcel_and_relation_prefixes_order_and_inputs_are_preserved() -> None:
```

Public synthetic-source result: assert both factual output prefixes equal source frames, inputs unchanged, geometry/CRS/index/order preserved and appended column order exact. Real owner chain may reread synthetic GPKGs; this is stronger than a private summary-only test, but not a real official snapshot run.

<a id="symbol-test-local-corruption-fast-fails-before-heavy-validation"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_local_corruption_fast_fails_before_heavy_validation`

Function, source lines 698–721.

```python
def test_local_corruption_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Mutate selected count to 999, rehash outputs, install heavy no-op counter, call public validator: raises and counter stays zero. Local deterministic frame reconstruction detects count corruption before upstream physical validation; stale source hashes are not involved.

<a id="symbol-test-local-corruption-fast-fails-before-heavy-validation-counted"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_local_corruption_fast_fails_before_heavy_validation.counted`

Function, source lines 710–712.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

Nested no-op increments nonlocal heavy-call counter and returns None. Parent requires zero; it is not an invocation of the real application validator.

<a id="symbol-test-coordinated-local-cross-table-corruption-is-rejected"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_coordinated_local_cross_table_corruption_is_rejected`

Function, source lines 740–753.

```python
def test_coordinated_local_cross_table_corruption_is_rejected(
    frame_name: str,
    column: str,
    value: object,
) -> None:
```

Seven parametrized frame/column/value tuples forge selected count/status/priority/confidence/JSON, role or relation parcel PARCEL-OTHER, then rehash outputs. Private envelope rejects. First guard varies: role/selected mismatch is local-domain; changed factual parcel ID leaves source-relation hash stale; valid-domain output changes reach deterministic reconstruction. Broad raises does not prove every mutation reaches cross-table comparison.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    ("frame_name", "column", "value"),
    [
        ("parcels", "bess_cnig_selected_relation_count", 999),
        ("parcels", "bess_cnig_parcel_precheck_status", "UNKNOWN"),
        ("parcels", "bess_cnig_parcel_status_priority", 999),
        ("parcels", "bess_cnig_parcel_precheck_confidence", "LOW"),
        ("parcels", "bess_cnig_selected_feature_ids_json", "[]"),
        (
            "relation_assessments",
            "bess_cnig_parcel_relation_role",
            "TOUCH_ONLY_CONTEXT",
        ),
        ("relation_assessments", "parcel_id", "PARCEL-OTHER"),
    ],
)
```

<a id="symbol-test-invalid-output-dtype-and-non-2d-parcel-fail-locally"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_invalid_output_dtype_and_non_2d_parcel_fail_locally`

Function, source lines 756–783.

```python
def test_invalid_output_dtype_and_non_2d_parcel_fail_locally() -> None:
```

Convert integer count or selected bool to object dtype, then test Z=5 parcel polygon. Local envelope rejects output dtype or exact-2D geometry before content hash comparison; prior hashes are not all repaired. Does not test repair.

<a id="symbol-test-every-inherited-application-relation-domain-is-validated-locally"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_every_inherited_application_relation_domain_is_validated_locally`

Function, source lines 836–840.

```python
def test_every_inherited_application_relation_domain_is_validated_locally(
    relations: pd.DataFrame,
) -> None:
```

Parametrized mutation of selected/lower/context inherited application status/confidence/status code includes AUTHORIZED, FORBIDDEN, PROHIBITED, CERTAIN and invalid application state. _build_from_relations calls common application relation contract before parcel selection; expect controlled error, not all cases a selected-status guard.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame([_relation(status="AUTHORIZED")]),
        pd.DataFrame([_relation(status="FORBIDDEN")]),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="PROHIBITED",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    confidence="CERTAIN",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    relation_type="TOUCH_ONLY",
                    application_status="INVALID_APPLICATION_STATUS",
                )
            ]
        ),
    ],
    ids=[
        "selected-authorized",
        "selected-forbidden",
        "lower-prohibited",
        "lower-certain-confidence",
        "contextual-invalid-application-status",
    ],
)
```

<a id="symbol-test-unresolved-relation-cannot-contain-a-decision"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_unresolved_relation_cannot_contain_a_decision`

Function, source lines 843–852.

```python
def test_unresolved_relation_cannot_contain_a_decision() -> None:
```

Unresolved relation is populated with UNKNOWN/LOW/40 decision fields; builder fails common inherited application contract requiring null decisions before aggregation. Exact UNKNOWN itself remains allowed in the separate test.

<a id="symbol-test-all-application-identity-scope-and-boundary-fields-are-intrinsic"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_all_application_identity_scope_and_boundary_fields_are_intrinsic`

Function, source lines 865–871.

```python
def test_all_application_identity_scope_and_boundary_fields_are_intrinsic(
    column: str, value: object
) -> None:
```

Mutate family OTHER, type 7, subtype AA, wrong policy scope or true boundary flag on a TOUCH_ONLY row. Shared inherited identity/domain/scope guard rejects before summary. This tests the listed values, not every possible identity transformation.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("feature_family", "OTHER"),
        ("type_code_raw", "7"),
        ("subtype_code_raw", "AA"),
        ("bess_cnig_application_scope", "WRONG_SCOPE"),
        ("bess_cnig_local_feature_text_interpreted", True),
    ],
)
```

<a id="symbol-test-application-relation-suffix-dtype-is-validated-locally"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_application_relation_suffix_dtype_is_validated_locally`

Function, source lines 874–880.

```python
def test_application_relation_suffix_dtype_is_validated_locally() -> None:
```

Make an inherited suffix column categorical and set canonicalize_application_dtypes=False; require dtype error. Other factual dtypes can already be noncanonical on this path, so the broad dtype match is not isolated proof that only the targeted suffix dtype caused failure.

<a id="symbol-test-status-and-priority-mapping-is-one-to-one-at-every-level"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_status_and_priority_mapping_is_one_to_one_at_every_level`

Function, source lines 940–944.

```python
def test_status_and_priority_mapping_is_one_to_one_at_every_level(
    relations: pd.DataFrame,
) -> None:
```

Three parametrized forged sets create one priority for different statuses at max or lower level, or one status with two priorities. Shared document-wide bijection guard runs before private per-parcel selection. Broad message does not uniquely isolate the per-parcel duplicate mapping branch.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame(
            [
                _relation(
                    feature_id="A",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=50,
                ),
                _relation(
                    feature_id="B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="MAX",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    feature_id="LOW-A",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="LOW-B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=10,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="A",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    feature_id="B",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=10,
                ),
            ]
        ),
    ],
    ids=[
        "same-maximum-priority-two-statuses",
        "same-lower-priority-two-statuses",
        "same-status-two-priorities",
    ],
)
```

<a id="symbol-test-valid-repeated-status-and-priority-mapping-selects-every-exact-match"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_valid_repeated_status_and_priority_mapping_selects_every_exact_match`

Function, source lines 947–960.

```python
def test_valid_repeated_status_and_priority_mapping_selects_every_exact_match() -> None:
```

Two exact MATERIAL_REVIEW_REQUIRED/30 rows A/B are both selected; assert selected count 2 and the two SELECTED_CONTROLLING roles. This test has no selected-ID JSON assertion. Confirms repeated identical mapping accepted, unlike ambiguous bijection; sorted selected-ID JSON is asserted separately by test_exact_relations_select_configured_max_priority_and_lowest_confidence.

<a id="symbol-test-duplicate-parcel-feature-identity-is-rejected-for-every-role"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_duplicate_parcel_feature_identity_is_rejected_for_every_role`

Function, source lines 1016–1022.

```python
def test_duplicate_parcel_feature_identity_is_rejected_for_every_role(
    relations: pd.DataFrame,
) -> None:
```

Five duplicate parcel-feature pair scenarios cover selected, lower, context, deferred and differing relation types. Common duplicate pair guard runs before subsequent metric/mapping selection; different roles/types do not authorize duplicate pair identity.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame([_relation(feature_id="A"), _relation(feature_id="A")]),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(feature_id="HIGH", priority=30),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="TOUCH", relation_type="TOUCH_ONLY"),
                _relation(feature_id="TOUCH", relation_type="TOUCH_ONLY"),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="DEFERRED"),
                _relation(feature_id="DEFERRED"),
                _relation(
                    feature_id="UNRESOLVED",
                    application_status="UNRESOLVED_CODE_PAIR",
                    status=None,
                    confidence=None,
                    priority=None,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="A", relation_type="AREA_OVERLAP"),
                _relation(feature_id="A", relation_type="LENGTH_OVERLAP"),
            ]
        ),
    ],
    ids=[
        "selected",
        "lower-priority",
        "contextual",
        "deferred",
        "different-relation-types",
    ],
)
```

<a id="symbol-test-invalid-lower-priority-feature-id-is-rejected-independently-of-json-role"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role`

Function, source lines 1029–1045.

```python
def test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role(
    feature_id: object,
) -> None:
```

Forge lower-priority ID None, empty, textual None or /tmp/feature; assert rejection in shared identity path before JSON selection. Cannot evade validation just because the row is lower priority.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    "feature_id",
    [None, "", "None", "/tmp/feature"],
)
```

<a id="symbol-test-invalid-deferred-feature-id-is-rejected-independently-of-json-role"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_invalid_deferred_feature_id_is_rejected_independently_of_json_role`

Function, source lines 1049–1067.

```python
def test_invalid_deferred_feature_id_is_rejected_independently_of_json_role(
    feature_id: str,
) -> None:
```

Forge exact deferred row ID C:\feature or surrounding-whitespace GPU ID beside unresolved controller; shared identity check fails before unresolved dominance. Later selected-ID JSON is not the only guard.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize("feature_id", [r"C:\feature", " GPU:F "])
```

<a id="symbol-test-invalid-relation-parcel-id-is-rejected"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_invalid_relation_parcel_id_is_rejected`

Function, source lines 1071–1077.

```python
def test_invalid_relation_parcel_id_is_rejected(parcel_id: object) -> None:
```

Relation parcel ID actual None or surrounding-whitespace " PARCEL-1 " fails exact identity validation; it is not coerced into an existing parcel key. Private builder, no physical source lock.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize("parcel_id", [None, " PARCEL-1 "])
```

<a id="symbol-test-unknown-relation-type-is-rejected-by-shared-relation-contract"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_unknown_relation_type_is_rejected_by_shared_relation_contract`

Function, source lines 1080–1084.

```python
def test_unknown_relation_type_is_rejected_by_shared_relation_contract() -> None:
```

Set relation type NEARBY; common geometry-kind/relation-type contract fails before summary. No inferred proximity threshold is introduced.

<a id="symbol-test-document-wide-same-priority-cannot-map-to-two-statuses"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_document_wide_same_priority_cannot_map_to_two_statuses`

Function, source lines 1088–1112.

```python
def test_document_wide_same_priority_cannot_map_to_two_statuses(
    context_type: str | None,
) -> None:
```

Across parcels, LIKELY_MATERIAL_CONSTRAINT and MATERIAL_REVIEW_REQUIRED both priority50, second relation AREA_OVERLAP/TOUCH_ONLY/BOUNDARY_TOUCH: shared global mapping rejects even contexts. Does not rely on a per-parcel conflict.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize("context_type", [None, "TOUCH_ONLY", "BOUNDARY_TOUCH"])
```

<a id="symbol-test-document-wide-same-status-cannot-map-to-two-priorities"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_document_wide_same_status_cannot_map_to_two_priorities`

Function, source lines 1115–1135.

```python
def test_document_wide_same_status_cannot_map_to_two_priorities() -> None:
```

Across parcels, identical status assigned 50 and10: common document-wide reverse mapping rejects before parcel summary.

<a id="symbol-test-document-wide-repeated-mapping-and-unresolved-rows-are-valid"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_document_wide_repeated_mapping_and_unresolved_rows_are_valid`

Function, source lines 1138–1154.

```python
def test_document_wide_repeated_mapping_and_unresolved_rows_are_valid() -> None:
```

Three relations on two parcels: PARCEL-1/A and PARCEL-2/B,U, with two repeated MATERIAL_REVIEW_REQUIRED/30 exact rows and one unresolved row. _build_from_relations calls the private builder and its guards, not the aggregation envelope validator. The sole explicit assertion is len(result.relation_assessments) == 3; no per-parcel state assertion is made here.

<a id="symbol-test-complete-five-status-policy-mapping-is-globally-valid"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_complete_five_status_policy_mapping_is_globally_valid`

Function, source lines 1157–1181.

```python
def test_complete_five_status_policy_mapping_is_globally_valid() -> None:
```

Five statuses with 50/40/30/20/10 on five parcels validate; asserted output relation count5. Domain/bijection acceptance, not all five detailed parcel summaries or current production-policy values.

<a id="symbol-test-selected-relation-role-requires-selected-status-and-priority"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_selected_relation_role_requires_selected_status_and_priority`

Function, source lines 1184–1213.

```python
def test_selected_relation_role_requires_selected_status_and_priority() -> None:
```

Relabel LOW row SELECTED_CONTROLLING and selected=true, rehash outputs; coherent local role flag passes, deterministic reconstruction rejects because status/priority are not selected. No factual prefix changed; this isolates cross-table role derivation better than stale-prefix mutations.

<a id="symbol--validate-parcel-geometries"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._validate_parcel_geometries`

Function, source lines 1216–1229.

```python
def _validate_parcel_geometries(geometries: list[object]) -> None:
```

Build supplied geometries with an empty inherited relation frame and private result, then envelope validation. Isolates parcel geometry even for no-relation parcels. Creates synthetic fixture upstream but no heavy validator for these substituted polygons.

<a id="symbol-test-malformed-parcel-geometry-is-rejected-intrinsically"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_malformed_parcel_geometry_is_rejected_intrinsically`

Function, source lines 1243–1245.

```python
def test_malformed_parcel_geometry_is_rejected_intrinsically(geometry: object) -> None:
```

Point, line, empty polygon, self-crossing polygon and None are rejected by parcel geometry guard in private build before hashing/summary. Parametrized test covers those exact geometries, not universal GEOS pathologies.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    "geometry",
    [
        Point(0, 0),
        LineString([(0, 0), (1, 1)]),
        Polygon(),
        Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)]),
        None,
    ],
    ids=["point", "line", "empty", "invalid", "null"],
)
```

<a id="symbol-test-valid-polygon-and-multipolygon-parcels-are-accepted"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_valid_polygon_and_multipolygon_parcels_are_accepted`

Function, source lines 1248–1250.

```python
def test_valid_polygon_and_multipolygon_parcels_are_accepted() -> None:
```

Valid Polygon and MultiPolygon are accepted by helper; no output-value assertions beyond absence of error. Not a CRS transformation or physical catalog test.

<a id="symbol-test-duplicate-output-columns-are-rejected-intrinsically"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_duplicate_output_columns_are_rejected_intrinsically`

Function, source lines 1254–1267.

```python
def test_duplicate_output_columns_are_rejected_intrinsically(frame_name: str) -> None:
```

Duplicate the first output column, retain GeoDataFrame geometry/CRS if needed; intrinsic duplicate-column guard rejects before suffix/dtype/hash checks.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize("frame_name", ["parcels", "relation_assessments"])
```

<a id="symbol-test-only-application-result-schema-two-is-accepted"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_only_application_result_schema_two_is_accepted`

Function, source lines 1271–1282.

```python
def test_only_application_result_schema_two_is_accepted(version: int) -> None:
```

Application version1/3/999 in replaced aggregation result, recompute outputs, local envelope fails required application schema2. Aggregation schema remains1.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize("version", [1, 3, 999])
```

<a id="symbol-test-application-result-schema-two-remains-accepted"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_application_result_schema_two_remains_accepted`

Function, source lines 1285–1291.

```python
def test_application_result_schema_two_remains_accepted() -> None:
```

Unchanged fixture carries application version2 and passes local envelope; assertion is version acceptance, not a migration test.

<a id="symbol-test-noncanonical-feature-ids-are-rejected"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_noncanonical_feature_ids_are_rejected`

Function, source lines 1298–1300.

```python
def test_noncanonical_feature_ids_are_rejected(feature_id: str) -> None:
```

Feature IDs None/nan/<NA> textual values, /tmp/feature, C:\feature or surrounding spaces fail the inherited identity path in private build; canonical JSON can reject them too but is not necessarily reached.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    "feature_id",
    ["None", "nan", "<NA>", "/tmp/feature", r"C:\feature", " GPU:F "],
)
```

<a id="symbol-test-current-gpu-feature-id-is-canonical"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_current_gpu_feature_id_is_canonical`

Function, source lines 1303–1308.

```python
def test_current_gpu_feature_id_is_canonical() -> None:
```

GPU:DOC:prescription_surface:FEATURE-01 is accepted as a portable non-absolute ID and appears in selected JSON. Private synthetic frame does not prove this invented ID belongs to a source catalog.

<a id="symbol-test-authorized-status-artifact-fails-local-verified-byte-loading"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_authorized_status_artifact_fails_local_verified_byte_loading`

Function, source lines 1311–1340.

```python
def test_authorized_status_artifact_fails_local_verified_byte_loading(
    tmp_path: Path,
) -> None:
```

Forge AUTHORIZED consistently in inherited relation and output parcel/result fields, recompute source-relation and output hashes, write artifacts and use test adapter. Depending on synthetic upstream state, real application envelope can fail first or unknown-feature fallback can enter legacy byte/local validation. The test only expects the aggregation error class, without message or stage counter: it does not unconditionally prove public source-bound artifact parsing or a specific status-domain guard.

<a id="symbol-test-coordinated-relation-identity-artifact-corruption-fails-locally"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_coordinated_relation_identity_artifact_corruption_fails_locally`

Function, source lines 1352–1362.

```python
def test_coordinated_relation_identity_artifact_corruption_fails_locally(
    tmp_path: Path,
    factory: object,
) -> None:
```

Parametrize fully rehashed duplicate pair, invalid lower ID and cross-parcel mapping results; write artifacts and require local corruption rejection via test adapter. Its application-envelope guard/fallback or artifact schema may precede the target intrinsic guard; no counter proves exact first stage for every case.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    "factory",
    [
        _duplicate_selected_pair_result,
        _invalid_lower_feature_id_result,
        _cross_parcel_priority_conflict_result,
    ],
    ids=["duplicate-pair", "invalid-lower-feature-id", "global-priority-conflict"],
)
```

<a id="symbol-test-controlling-relation-cannot-be-relabelled-contextual-in-artifact"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_controlling_relation_cannot_be_relabelled_contextual_in_artifact`

Function, source lines 1365–1375.

```python
def test_controlling_relation_cannot_be_relabelled_contextual_in_artifact(
    tmp_path: Path,
) -> None:
```

Persist forged positive-area surface relabeled TOUCH_ONLY using bypass helper, then adapter raises surface/metric/type error. _LAST_* can come from another fixture; shared inherited relation guard can fail before artifact reads. This is not an isolated five-argument loader proof.

<a id="symbol-test-no-relation-parcel-rejects-textual-null-identity"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_no_relation_parcel_rejects_textual_null_identity`

Function, source lines 1379–1416.

```python
def test_no_relation_parcel_rejects_textual_null_identity(
    tmp_path: Path, parcel_id: str
) -> None:
```

Forge no-relation parcel ID textual None/nan/<NA>, write artifacts then update recorded readback schemas; adapter must raise with message matching parcel ID. Local parcel identity guard precedes source hash validation once artifact envelope is reached; source parcel hash is stale. Upstream adapter context remains a limitation.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize("parcel_id", ["None", "nan", "<NA>"])
```

<a id="symbol-test-relation-identity-and-global-mapping-fail-before-heavy-validation"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_relation_identity_and_global_mapping_fail_before_heavy_validation`

Function, source lines 1419–1444.

```python
def test_relation_identity_and_global_mapping_fail_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Use three coordinated corruption factories and install heavy no-op counter; public result validation raises and heavy counter remains0. Intrinsic identity/mapping guards precede heavy call; unlike adapter tests this calls production validator directly.

<a id="symbol-test-relation-identity-and-global-mapping-fail-before-heavy-validation-counted"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_relation_identity_and_global_mapping_fail_before_heavy_validation.counted`

Function, source lines 1428–1430.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

No-op counter increments if heavy application validation is called; parent asserts zero across corrupt cases. No delegation to the real validator.

<a id="symbol-test-relation-semantic-failure-fast-fails-before-heavy-validation"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_relation_semantic_failure_fast_fails_before_heavy_validation`

Function, source lines 1447–1472.

```python
def test_relation_semantic_failure_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Coherently hashed SURFACE/TOUCH_ONLY semantic corruption; public validator raises before heavy counter. Common intrinsic area/type contract, not a source-byte mismatch, rejects first.

<a id="symbol-test-relation-semantic-failure-fast-fails-before-heavy-validation-counted"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_relation_semantic_failure_fast_fails_before_heavy_validation.counted`

Function, source lines 1456–1458.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

No-op heavy-call counter, expected zero in parent; no actual validation or I/O when invoked.

<a id="symbol-test-parcel-decision-status-domain-rejects-forbidden-vocabulary"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_parcel_decision_status_domain_rejects_forbidden_vocabulary`

Function, source lines 1488–1502.

```python
def test_parcel_decision_status_domain_rejects_forbidden_vocabulary(
    status: str,
) -> None:
```

Eight forbidden parcel-status words ALLOWED/AUTHORIZED/COMPATIBLE/CLEAR/FORBIDDEN/PROHIBITED/BLOCKED/BUILDABLE are rejected locally after output rehash. Domain guard precedes deterministic summary; these words are test corruption, not produced decisions.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    "status",
    [
        "ALLOWED",
        "AUTHORIZED",
        "COMPATIBLE",
        "CLEAR",
        "FORBIDDEN",
        "PROHIBITED",
        "BLOCKED",
        "BUILDABLE",
    ],
)
```

<a id="symbol-test-persisted-feature-id-json-must-be-portable-and-canonical"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_persisted_feature_id_json_must_be_portable_and_canonical`

Function, source lines 1519–1530.

```python
def test_persisted_feature_id_json_must_be_portable_and_canonical(
    json_value: str,
) -> None:
```

Nine JSON strings include textual-null IDs, absolute paths, whitespace IDs, unsorted/space-formatted/duplicate arrays. Local canonical JSON guard rejects after output rehash; no filesystem interpretation of feature IDs.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    "json_value",
    [
        '["None"]',
        '["nan"]',
        '["<NA>"]',
        '["/tmp/feature"]',
        r'["C:\\feature"]',
        '[" GPU:F "]',
        '["B","A"]',
        '["A", "B"]',
        '["A","A"]',
    ],
)
```

<a id="symbol-test-representative-intrinsic-failures-all-precede-heavy-validation"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_representative_intrinsic_failures_all_precede_heavy_validation`

Function, source lines 1533–1621.

```python
def test_representative_intrinsic_failures_all_precede_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Seven representative defects (inherited AUTHORIZED, parcel AUTHORIZED, ambiguous priority, point parcel, duplicate column, app version3, absolute JSON ID) are checked under a no-op heavy counter and each must raise with total calls0. Earlier domain/schema/geometry/source-prefix guards may differ; count0 proves ordering, not exact branch for every mutation.

<a id="symbol-test-representative-intrinsic-failures-all-precede-heavy-validation-counted"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_representative_intrinsic_failures_all_precede_heavy_validation.counted`

Function, source lines 1542–1544.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

No-op heavy-call counter reused through parent loop, expected zero. It does not emulate physical validation.

<a id="symbol-test-one-aggregation-and-one-public-validation-each-call-heavy-once"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_one_aggregation_and_one_public_validation_each_call_heavy_once`

Function, source lines 1624–1649.

```python
def test_one_aggregation_and_one_public_validation_each_call_heavy_once(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Wrap and delegate actual application-owner validator; public aggregation increments calls to1, public result validation to2. Synthetic physical input chain truly runs. Counts owner calls, not per-file reads or _aggregate_frames executions.

<a id="symbol-test-one-aggregation-and-one-public-validation-each-call-heavy-once-counted"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_one_aggregation_and_one_public_validation_each_call_heavy_once.counted`

Function, source lines 1634–1637.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

Increment nonlocal counter, then call saved real validator with unchanged args/kwargs. Unlike the other counted helpers, this one delegates and may perform physical synthetic I/O.

<a id="symbol-test-valid-two-file-verified-byte-artifacts-and-source-readback"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_valid_two_file_verified_byte_artifacts_and_source_readback`

Function, source lines 1652–1664.

```python
def test_valid_two_file_verified_byte_artifacts_and_source_readback(
    tmp_path: Path,
) -> None:
```

Write two valid synthetic artifact files, adapter-load, assert both frames equal original, then call source-complete public result validator. The latter supplies physical synthetic-source readback beyond local bytes; no official acquisition or immutable-file guarantee.

<a id="symbol-test-artifact-manifest-corruption-is-rejected"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_artifact_manifest_corruption_is_rejected`

Function, source lines 1697–1708.

```python
def test_artifact_manifest_corruption_is_rejected(
    tmp_path: Path, mutation: object
) -> None:
```

Nineteen manifest lambdas: manifest schema 2; application hash schema 1/3/999; remove a role record, append EXTRA or append a duplicate record; wrong, duplicate or absolute filename; size 1; mismatched or malformed SHA; row count 999; wrong schema index_names; null or wrong CRS; geospatial=False; extra unknown key. None permutes the two otherwise-valid records, so this is not direct record-order regression coverage. Adapter-load must fail. First guard differs: Pydantic type/literal/after-model, upstream locks, filename, size, SHA, decoded row/schema/CRS. This broad test does not prove one particular branch per mutation.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    "mutation",
    [
        lambda value: value.update(schema_version=2),
        lambda value: value.update(application_result_hash_schema_version=1),
        lambda value: value.update(application_result_hash_schema_version=3),
        lambda value: value.update(application_result_hash_schema_version=999),
        lambda value: value["artifacts"].pop(),
        lambda value: value["artifacts"].append(
            {**value["artifacts"][0], "artifact_role": "EXTRA"}
        ),
        lambda value: value["artifacts"].append(dict(value["artifacts"][0])),
        lambda value: value["artifacts"][0].update(filename="wrong.parquet"),
        lambda value: value["artifacts"][1].update(
            filename=value["artifacts"][0]["filename"]
        ),
        lambda value: value["artifacts"][0].update(filename="C:/absolute.parquet"),
        lambda value: value["artifacts"][0].update(size_bytes=1),
        lambda value: value["artifacts"][0].update(sha256="f" * 64),
        lambda value: value["artifacts"][0].update(sha256="bad"),
        lambda value: value["artifacts"][0].update(row_count=999),
        lambda value: value["artifacts"][0]["frame_schema_signature"].update(
            index_names=["wrong"]
        ),
        lambda value: value["artifacts"][0].update(crs=None),
        lambda value: value["artifacts"][0].update(crs={"wrong": True}),
        lambda value: value["artifacts"][0].update(geospatial=False),
        lambda value: value.update(unknown=True),
    ],
)
```

<a id="symbol-test-aggregation-manifest-uses-strict-json-before-artifact-read"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_aggregation_manifest_uses_strict_json_before_artifact_read`

Function, source lines 1721–1755.

```python
def test_aggregation_manifest_uses_strict_json_before_artifact_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
```

Write four invalid manifest texts (duplicate key, NaN, Infinity, non-object list). The counted_bytes Path.read_bytes spy and counted pd.read_parquet forbidden-read sentinel share one artifact_reads counter. Valid synthetic upstream permits manifest parse; strict JSON fails and the test asserts artifact_reads == 0. The manifest read delegates without incrementing this counter; an artifact decode would increment it and raise AssertionError immediately.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    "document",
    [
        '{"schema_version":1,"schema_version":1}',
        '{"schema_version":NaN}',
        '{"schema_version":Infinity}',
        "[]",
    ],
    ids=["duplicate-key", "nan", "infinity", "non-object"],
)
```

<a id="symbol-test-aggregation-manifest-uses-strict-json-before-artifact-read-counted-bytes"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_aggregation_manifest_uses_strict_json_before_artifact_read.counted_bytes`

Function, source lines 1735–1739.

```python
    def counted_bytes(path: Path) -> bytes:
```

Intercept Path.read_bytes; increment the shared artifact_reads only when path is a parcel/relation artifact, then delegate original_read_bytes(path). Manifest reading is allowed without incrementing the counter. The pd.read_parquet sentinel shares this counter; the parent asserts zero.

<a id="symbol-test-aggregation-manifest-uses-strict-json-before-artifact-read-counted"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_aggregation_manifest_uses_strict_json_before_artifact_read.counted`

Function, source lines 1741–1744.

```python
    def counted(*args: object, **kwargs: object) -> object:
```

Forbidden-read sentinel installed for pd.read_parquet: increment shared artifact_reads, then immediately raise AssertionError("Artifact read preceded strict manifest validation"). Does not delegate to any saved reader. The parent requires the same counter shared with counted_bytes to remain zero; inspect_read in the separate captured-bytes replacement test is the delegating reader.

<a id="symbol-test-aggregation-physical-replacement-is-rejected"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_aggregation_physical_replacement_is_rejected`

Function, source lines 1758–1767.

```python
def test_aggregation_physical_replacement_is_rejected(tmp_path: Path) -> None:
```

Append b"tamper" to relation Parquet without manifest update; valid fixture adapter rejects size or hash. Because length changes, size check is first, not proof of a same-size SHA mismatch.

<a id="symbol-test-verified-bytes-are-the-bytes-parsed"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_verified_bytes_are_the_bytes_parsed`

Function, source lines 1770–1804.

```python
def test_verified_bytes_are_the_bytes_parsed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

After target relation bytes are captured, replace its path with gzip-compressed alternative; intercept pd.read_parquet and require BytesIO payload among observed and returned frame equality. Successful return demonstrates parsing original captured bytes even after path replacement; it does not promise a final path postcondition or atomic set.

<a id="symbol-test-verified-bytes-are-the-bytes-parsed-replace-after-read"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_verified_bytes_are_the_bytes_parsed.replace_after_read`

Function, source lines 1787–1791.

```python
    def replace_after_read(path: Path) -> bytes:
```

Nested Path.read_bytes hook delegates first, replaces only target after capture, returns original bytes. Deliberately mutates tmp_path file; not production behavior.

<a id="symbol-test-verified-bytes-are-the-bytes-parsed-inspect-read"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_verified_bytes_are_the_bytes_parsed.inspect_read`

Function, source lines 1793–1796.

```python
    def inspect_read(source: object, *args: object, **kwargs: object) -> object:
```

Nested Parquet hook records BytesIO.getvalue, then delegates original reader. Parent compares payload membership; it does not count exactly one decode globally.

<a id="symbol-test-public-exports-are-stable"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_public_exports_are_stable`

Function, source lines 1807–1820.

```python
def test_public_exports_are_stable() -> None:
```

Assert module __all__ equals exact six-name set and package __all__ includes it. Record model is importable but not in this public subset. Does not assert package has only six exports.

<a id="symbol--coherent-parcel-area-mutation"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._coherent_parcel_area_mutation`

Function, source lines 1823–1834.

```python
def _coherent_parcel_area_mutation(
    result: BessPlanningFeatureParcelAggregationResult,
    geometry_kind: str,
) -> BessPlanningFeatureParcelAggregationResult:
```

Change stored parcel_metric_area_m2 from4000 to8000 and surface share consistently, then fully rehash source/output. Geometry stays4000. Removes stale-hash/share inconsistency as earlier explanations for targeted metric failure.

<a id="symbol-test-relation-parcel-area-is-bound-to-real-parcel-geometry"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_relation_parcel_area_is_bound_to_real_parcel_geometry`

Function, source lines 1845–1859.

```python
def test_relation_parcel_area_is_bound_to_real_parcel_geometry(
    geometry_kind: str,
    relation_type: str,
) -> None:
```

Parametrize surface/line/point controlling rows with coherent area8000 but actual geometry4000; private envelope rejects parcel metric area. Earlier inherited metrics remain internally coherent, exposing the measured-geometry binding.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "AREA_OVERLAP"),
        ("LINE", "LENGTH_OVERLAP"),
        ("POINT", "INSIDE"),
    ],
)
```

<a id="symbol-test-self-consistent-parcel-area-artifact-is-rejected"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_self_consistent_parcel_area_artifact_is_rejected`

Function, source lines 1862–1893.

```python
def test_self_consistent_parcel_area_artifact_is_rejected(tmp_path: Path) -> None:
```

Persist coherent area defect, reread/recompute physical schemas and all relevant hashes, adapter-load requires area error. Local measured-area reconstruction is exercised when adapter reaches legacy/local envelope; still not proof of real GPU readback or isolated public loader source locks.

<a id="symbol-test-parcel-area-validation-uses-reprojected-calculation-copy"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_parcel_area_validation_uses_reprojected_calculation_copy`

Function, source lines 1896–1907.

```python
def test_parcel_area_validation_uses_reprojected_calculation_copy() -> None:
```

Convert copied parcel frame to EPSG:4326, rehash all source/output and validate envelope; area is measured via EPSG:2154 calculation copy. Assert original fixture result geometry/CRS unchanged. Does not explicitly reassert the transformed input after validation; source code establishes nonmutating calculation copy.

<a id="symbol-test-parcel-area-defect-fast-fails-before-application-source-validation"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_parcel_area_defect_fast_fails_before_application_source_validation`

Function, source lines 1910–1932.

```python
def test_parcel_area_defect_fast_fails_before_application_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

Coherent area defect in public validator with no-op heavy counter; expect metric-area error and calls0. Demonstrates intrinsic measured area guard before source-complete application validation.

<a id="symbol-test-parcel-area-defect-fast-fails-before-application-source-validation-counted"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_parcel_area_defect_fast_fails_before_application_source_validation.counted`

Function, source lines 1921–1923.

```python
    def counted(*args: object, **kwargs: object) -> None:
```

No-op heavy counter, expected zero; no delegate or source read.

<a id="symbol-test-step-7d-5b-2b-5-aggregation-loader-requires-exact-upstreams"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams`

Function, source lines 1935–1950.

```python
def test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams() -> None:
```

Inspect the actual production loader signature and assert its ordered five parameter names plus existence of the application-envelope validator. The test does not inspect parameter defaults or separately assert requiredness; that is evident in the production signature. No artifact execution here; the test wrapper optional defaults are not production compatibility.

<a id="symbol-test-source-bound-aggregation-loader-accepts-only-supplied-upstreams"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_source_bound_aggregation_loader_accepts_only_supplied_upstreams`

Function, source lines 1953–1967.

```python
def test_source_bound_aggregation_loader_accepts_only_supplied_upstreams(
    tmp_path: Path,
) -> None:
```

Pass both exact upstream objects explicitly through adapter (legacy=false), require successful production loader and equal complete hash. No fallback possible; valid synthetic artifact read/rebuild, not heavy GPU revalidation.

<a id="symbol-test-aggregation-manifest-filenames-are-casefold-unique"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_aggregation_manifest_filenames_are_casefold_unique`

Function, source lines 1970–1977.

```python
def test_aggregation_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
```

Change second record filename to uppercase first; model rejects casefold duplicate before file read. Fixture writer I/O occurs before this isolated model mutation.

<a id="symbol--changed-parcel-geometry-upstreams"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy._changed_parcel_geometry_upstreams`

Function, source lines 1980–2009.

```python
def _changed_parcel_geometry_upstreams(
    source_parcels: gpd.GeoDataFrame,
    application: object,
) -> tuple[gpd.GeoDataFrame, object]:
```

Copy parcels, scale target polygon2x2 about centroid, recompute measured EPSG:2154 relation areas/shares, replace/rehash application and validate its envelope; return changed pair. Geometry/source hashes become coherent locally, not with original external upstream identity.

<a id="symbol-test-source-bound-aggregation-loader-rejects-coordinated-upstream-changes"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes`

Function, source lines 2022–2092.

```python
def test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
```

Five coherent alternative artifacts: parcel geometry2x2, parcel CRS4326, exact application rationale "A different exact relation rationale.", reversed parcels (with extra synthetic parcel), moved unrelated parcel geometry. Private build/envelope succeeds for altered upstreams; real module loader given originals rejects upstream lock before artifact reads by code order. Heavy counter stays0; artifact read count is not separately asserted.

Exact parametrization (setup may execute at collection):

```python
@pytest.mark.parametrize(
    "mutation",
    [
        "parcel_geometry",
        "parcel_crs",
        "application_relation",
        "parcel_order",
        "unrelated_parcel_geometry",
    ],
)
```

<a id="symbol-test-source-bound-aggregation-loader-rejects-coordinated-upstream-changes-forbidden-heavy"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes.forbidden_heavy`

Function, source lines 2077–2079.

```python
    def forbidden_heavy(*args: object, **kwargs: object) -> None:
```

Increment forbidden-heavy counter and return None; parent requires zero. Source-bound loader should use envelope validation only, not this heavy validator.

<a id="symbol-test-source-bound-aggregation-loader-rebuilds-once-without-mutating-upstreams"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams`

Function, source lines 2095–2136.

```python
def test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Real module loader on exact upstreams under delegated _build_result counter and no-op heavy counter: build1/heavy0, complete hash matches, input parcel and relation frames unchanged. Local envelope also calls _aggregate_frames, so this does not prove a single aggregation pass.

<a id="symbol-test-source-bound-aggregation-loader-rebuilds-once-without-mutating-upstreams-counted-build"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams.counted_build`

Function, source lines 2110–2113.

```python
    def counted_build(*args: object, **kwargs: object) -> object:
```

Count then delegate saved private builder with same args/kwargs; parent expects exactly1 explicit build. Does not count local envelope reconstruction.

<a id="symbol-test-source-bound-aggregation-loader-rebuilds-once-without-mutating-upstreams-forbidden-heavy"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams.forbidden_heavy`

Function, source lines 2115–2117.

```python
    def forbidden_heavy(*args: object, **kwargs: object) -> None:
```

No-op forbidden heavy counter; parent expects0, proving heavy owner entry not used by this loader path.

<a id="symbol-test-aggregation-loader-rejects-bad-application-before-artifact-reads"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_aggregation_loader_rejects_bad_application_before_artifact_reads`

Function, source lines 2139–2162.

```python
def test_aggregation_loader_rejects_bad_application_before_artifact_reads(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
```

Replace application complete digest with 64 zeros, use real imported loader alias, count all Path.read_bytes; broad Exception with application/hash match and counter0. Application envelope fails before manifest/Parquet reads. Test does not narrow raised type to aggregation error.

<a id="symbol-test-aggregation-loader-rejects-bad-application-before-artifact-reads-counted"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_aggregation_loader_rejects_bad_application_before_artifact_reads.counted`

Function, source lines 2147–2150.

```python
    def counted(path: Path) -> bytes:
```

Count every Path.read_bytes and delegate original; parent requires0 including manifest. Does not intercept every possible third-party I/O API.

<a id="symbol-test-aggregation-manifest-rejects-nonportable-filename"></a>
### `tests.unit.test_aggregate_bess_planning_feature_policy.test_aggregation_manifest_rejects_nonportable_filename`

Function, source lines 2204–2211.

```python
def test_aggregation_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
```

Parametrize 34 nonportable filenames: absolute/traversal/separators, Windows reserved names (including COM/LPT superscript digits), ADS colon, forbidden punctuation and controls. Record/manifest ValueError expected before loader I/O; physical fixture files were already written. This is metadata model testing, not path traversal execution.

Exact parametrization (setup may execute at collection):

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

## Complete source snapshot

Exactly one full UTF-8 Git-content snapshot follows; source line endings are LF and are not rewritten. Matching this snapshot establishes bytes, not semantic prose accuracy.

```python
from __future__ import annotations

import importlib
import inspect
import json
from collections.abc import Mapping
from dataclasses import fields, replace
from hashlib import sha256
from io import BytesIO
from pathlib import Path

import geopandas as gpd
import pandas as pd
import pytest
from geopandas.testing import assert_geodataframe_equal
from pandas.testing import assert_frame_equal
from shapely import affinity
from shapely.geometry import LineString, MultiPolygon, Point, Polygon
from test_apply_bess_planning_feature_policy import (
    _application_fixture,
    _coordinated_policy_mutation,
    _surface_touch_with_positive_area,
)

from landscout import stages
from landscout.common.bess_application_contract import (
    POLICY_COLUMNS,
    POLICY_SUFFIX_DTYPES,
)
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.planning_feature_schema import relation_columns, relation_dtypes
from landscout.common.strict_json import loads_strict_json_object
from landscout.stages.aggregate_bess_planning_feature_policy import (
    BessPlanningFeatureParcelAggregationArtifactManifest,
    BessPlanningFeatureParcelAggregationArtifactRecord,
    BessPlanningFeatureParcelAggregationError,
    BessPlanningFeatureParcelAggregationResult,
    aggregate_bess_planning_feature_policy_to_parcels,
    validate_bess_planning_feature_parcel_aggregation_result,
)
from landscout.stages.aggregate_bess_planning_feature_policy import (
    load_bess_planning_feature_parcel_aggregation_artifacts as _load_aggregation_artifacts,
)

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
_LAST_SOURCE_PARCELS: gpd.GeoDataFrame | None = None
_LAST_APPLICATION_RESULT: object | None = None


def _aggregation_artifact_record_payload() -> dict[str, object]:
    crs = {
        "type": "ProjectedCRS",
        "name": "RGF93 v1 / Lambert-93",
        "coordinate_system": {"axis": [{"name": "Easting"}]},
    }
    return {
        "artifact_role": "PARCELS",
        "filename": "parcels.parquet",
        "row_count": 1,
        "size_bytes": 1,
        "sha256": "a" * 64,
        "frame_schema_signature": {
            "columns": ["geometry"],
            "dtypes": ["geometry"],
            "index_class": "pandas.core.indexes.range.RangeIndex",
            "index_names": [None],
            "index_level_dtypes": ["int64"],
            "geometry_column": "geometry",
            "crs": crs,
        },
        "geospatial": True,
        "crs": crs,
    }


def test_aggregation_artifact_record_is_deeply_immutable_without_aliases() -> None:
    payload = _aggregation_artifact_record_payload()
    record = BessPlanningFeatureParcelAggregationArtifactRecord.model_validate(payload)

    payload_signature = payload["frame_schema_signature"]
    assert isinstance(payload_signature, dict)
    payload_columns = payload_signature["columns"]
    assert isinstance(payload_columns, list)
    payload_columns.append("caller_mutation")
    payload_crs = payload["crs"]
    assert isinstance(payload_crs, dict)
    payload_crs["caller_mutation"] = True

    assert record.frame_schema_signature["columns"] == ("geometry",)
    assert record.crs is not None
    assert "caller_mutation" not in record.crs
    assert record.model_dump(mode="json", warnings="error") == (
        _aggregation_artifact_record_payload()
    )
    with pytest.raises(TypeError, match="frozen"):
        record.frame_schema_signature["new"] = "value"
    with pytest.raises(AttributeError):
        record.frame_schema_signature["columns"].append("new")
    with pytest.raises(TypeError, match="frozen"):
        record.crs["new"] = "value"
    coordinate_system = record.crs["coordinate_system"]
    assert isinstance(coordinate_system, Mapping)
    with pytest.raises(TypeError, match="frozen"):
        coordinate_system["new"] = "value"


def _aggregation_fixture() -> tuple[
    tuple[object, ...],
    object,
    object,
    object,
    object,
    BessPlanningFeatureParcelAggregationResult,
]:
    global _LAST_SOURCE_PARCELS, _LAST_APPLICATION_RESULT
    inputs, coded, config, policy, application = _application_fixture()
    result = aggregate_bess_planning_feature_policy_to_parcels(
        *inputs, coded, config, policy, application
    )
    _LAST_SOURCE_PARCELS = inputs[1]
    _LAST_APPLICATION_RESULT = application
    return inputs, coded, config, policy, application, result


def load_bess_planning_feature_parcel_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
    source_parcels: gpd.GeoDataFrame | None = None,
    application_result: object | None = None,
) -> BessPlanningFeatureParcelAggregationResult:
    """Test adapter supplying the newly mandatory exact upstream envelopes."""

    legacy_synthetic = source_parcels is None or application_result is None
    if source_parcels is None or application_result is None:
        source_parcels = _LAST_SOURCE_PARCELS
        application_result = _LAST_APPLICATION_RESULT
    if source_parcels is None or application_result is None:
        return _load_legacy_local_aggregation_artifacts(
            manifest_path, parcels_path, relation_assessments_path
        )
    assert source_parcels is not None
    assert application_result is not None
    try:
        return _load_aggregation_artifacts(
            manifest_path,
            parcels_path,
            relation_assessments_path,
            source_parcels,
            application_result,
        )
    except BessPlanningFeatureParcelAggregationError as error:
        if not legacy_synthetic or "unknown feature" not in str(error):
            raise
        return _load_legacy_local_aggregation_artifacts(
            manifest_path, parcels_path, relation_assessments_path
        )


def _load_legacy_local_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
) -> BessPlanningFeatureParcelAggregationResult:
    """Exercise pre-2B.5 local-only assertions for retained synthetic fixtures."""

    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    payload = loads_strict_json_object(Path(manifest_path).read_bytes())
    manifest = BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(
        payload
    )
    records = {record.artifact_role: record for record in manifest.artifacts}
    parcels = module._read_verified_artifact(Path(parcels_path), records["PARCELS"])
    relations = module._read_verified_artifact(
        Path(relation_assessments_path), records["RELATION_ASSESSMENTS"]
    )
    result = BessPlanningFeatureParcelAggregationResult(
        **{field: getattr(manifest, field) for field in module.RESULT_SCALAR_FIELDS},
        parcels=parcels,
        relation_assessments=relations,
    )
    module._validate_result_envelope(result)
    return result


def _build_from_relations(
    relations: pd.DataFrame,
    *,
    parcel_ids: tuple[str, ...] = ("PARCEL-1", "PARCEL-2"),
    canonicalize_application_dtypes: bool = True,
) -> BessPlanningFeatureParcelAggregationResult:
    global _LAST_SOURCE_PARCELS, _LAST_APPLICATION_RESULT
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, application = _application_fixture()
    parcels = gpd.GeoDataFrame(
        {"parcel_id": list(parcel_ids), "prior": range(len(parcel_ids))},
        geometry=[
            Polygon(
                [
                    (i * 101, 0),
                    (i * 101 + 100, 0),
                    (i * 101 + 100, 40),
                    (i * 101, 40),
                ]
            )
            for i in range(len(parcel_ids))
        ],
        crs="EPSG:2154",
        index=pd.Index(range(10, 10 + len(parcel_ids)), name="parcel_row"),
    )
    relations = relations.reset_index(drop=True)
    relations["parcel_metric_area_m2"] = 4000.0
    surface_mask = relations["geometry_kind"].eq("SURFACE")
    relations.loc[surface_mask, "parcel_share_pct"] = (
        100.0
        * relations.loc[surface_mask, "intersection_area_m2"].astype("float64")
        / 4000.0
    )
    relations["bess_cnig_policy_profile"] = application.policy_profile
    relations["bess_cnig_policy_sha256"] = application.policy_sha256
    relations["bess_cnig_policy_result_sha256"] = (
        application.policy_complete_result_content_sha256
    )
    if canonicalize_application_dtypes:
        suffix = POLICY_COLUMNS
        relations = relations.loc[:, relation_columns(suffix)]
        for column, dtype in zip(
            relation_columns(suffix),
            relation_dtypes(tuple(POLICY_SUFFIX_DTYPES[column] for column in suffix)),
            strict=True,
        ):
            relations[column] = pd.Series(
                relations[column].tolist(), index=relations.index, dtype=dtype
            )
        relations.index = pd.Index(relations.index.to_numpy(), dtype="int64")
    application = replace(application, relations=relations)
    application = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )._result_with_hashes(application)
    _LAST_SOURCE_PARCELS = parcels
    _LAST_APPLICATION_RESULT = application
    return module._build_result(parcels, application)


def _relation(
    *,
    parcel_id: str = "PARCEL-1",
    feature_id: str = "F-1",
    relation_type: str = "AREA_OVERLAP",
    application_status: str = "APPLIED_EXACT_POLICY",
    status: str | None = "MATERIAL_REVIEW_REQUIRED",
    confidence: str | None = "HIGH",
    priority: int | None = 30,
    area: float = 0.000001,
) -> dict[str, object]:
    _, _, _, _, application = _application_fixture()
    if relation_type == "LENGTH_OVERLAP":
        row = (
            application.relations.loc[application.relations["geometry_kind"].eq("LINE")]
            .iloc[0]
            .to_dict()
        )
    else:
        row = (
            application.relations.loc[
                application.relations["geometry_kind"].eq("SURFACE")
            ]
            .iloc[0]
            .to_dict()
        )
    row.update(
        parcel_id=parcel_id,
        planning_feature_id=feature_id,
        relation_type=relation_type,
        official_code_status=(
            "UNKNOWN_CODE_PAIR"
            if application_status == "UNRESOLVED_CODE_PAIR"
            else "RESOLVED_OFFICIAL"
        ),
        bess_cnig_policy_application_status=application_status,
        bess_cnig_precheck_status=status,
        bess_cnig_precheck_confidence=confidence,
        bess_cnig_status_priority=priority,
        bess_cnig_rationale=(
            None
            if application_status == "UNRESOLVED_CODE_PAIR"
            else row["bess_cnig_rationale"]
        ),
        bess_cnig_required_human_action=(
            None
            if application_status == "UNRESOLVED_CODE_PAIR"
            else row["bess_cnig_required_human_action"]
        ),
        bess_cnig_limitations=(
            None
            if application_status == "UNRESOLVED_CODE_PAIR"
            else row["bess_cnig_limitations"]
        ),
    )
    if application_status == "UNRESOLVED_CODE_PAIR":
        row.update(
            official_code_label=None,
            official_legal_reference=None,
            official_regulation_reference=None,
            official_code_source_url=None,
        )
    if relation_type == "AREA_OVERLAP":
        row["parcel_metric_area_m2"] = max(float(row["parcel_metric_area_m2"]), area)
        row["feature_area_m2"] = max(float(row["feature_area_m2"]), area)
        row.update(
            intersection_area_m2=area,
            parcel_share_pct=100.0 * area / float(row["parcel_metric_area_m2"]),
            feature_share_pct=100.0 * area / float(row["feature_area_m2"]),
        )
    elif relation_type == "LENGTH_OVERLAP":
        row["source_line_length_m"] = max(float(row["source_line_length_m"]), area)
        row["intersection_length_m"] = area
    elif relation_type == "TOUCH_ONLY":
        row.update(
            intersection_area_m2=0.0,
            parcel_share_pct=0.0,
            feature_share_pct=0.0,
        )
    elif relation_type in {"INSIDE", "BOUNDARY_TOUCH"}:
        row.update(
            geometry_kind="POINT",
            feature_area_m2=None,
            source_line_length_m=None,
            intersection_area_m2=None,
            intersection_length_m=None,
            parcel_share_pct=None,
            feature_share_pct=None,
            point_member_count=1,
            point_members_inside_count=1 if relation_type == "INSIDE" else 0,
            point_members_boundary_count=(0 if relation_type == "INSIDE" else 1),
        )
    return row


def _write_artifacts(
    tmp_path: Path,
    result: BessPlanningFeatureParcelAggregationResult,
) -> tuple[Path, dict[str, Path], dict[str, object]]:
    frames = {
        "PARCELS": (result.parcels, "parcels.parquet", True),
        "RELATION_ASSESSMENTS": (
            result.relation_assessments,
            "relations.parquet",
            False,
        ),
    }
    paths: dict[str, Path] = {}
    records: list[dict[str, object]] = []
    for role, (frame, filename, geospatial) in frames.items():
        path = tmp_path / filename
        frame.to_parquet(path, index=True)
        paths[role] = path
        signature = deterministic_frame_schema_signature(frame)
        payload = path.read_bytes()
        records.append(
            {
                "artifact_role": role,
                "filename": filename,
                "row_count": len(frame),
                "size_bytes": len(payload),
                "sha256": sha256(payload).hexdigest(),
                "frame_schema_signature": signature,
                "geospatial": geospatial,
                "crs": signature.get("crs"),
            }
        )
    scalar_names = tuple(
        field.name
        for field in fields(BessPlanningFeatureParcelAggregationResult)
        if field.name not in {"parcels", "relation_assessments"}
    )
    manifest = {
        "schema_version": 1,
        "artifact_kind": "BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT",
        **{name: getattr(result, name) for name in scalar_names},
        "artifacts": records,
    }
    BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(manifest)
    manifest_path = tmp_path / "aggregation.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest_path, paths, manifest


def _rehash_coordinated_result(
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    source_parcels = result.parcels.drop(columns=list(PARCEL_COLUMNS))
    source_relations = result.relation_assessments.drop(columns=list(RELATION_COLUMNS))
    updated = replace(
        result,
        source_parcels_content_sha256=module._frame_sha256(
            source_parcels,
            "landscout.bess_cnig_parcel_aggregation.source_parcels",
        ),
        source_application_relations_content_sha256=module._frame_sha256(
            source_relations,
            "landscout.bess_cnig_parcel_aggregation.source_application_relations",
        ),
    )
    return module._result_with_hashes(updated)


def _duplicate_selected_pair_result() -> BessPlanningFeatureParcelAggregationResult:
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="A"),
                _relation(feature_id="B"),
            ]
        )
    )
    relations = result.relation_assessments.copy(deep=True)
    relations.loc[relations.index[1], "planning_feature_id"] = "A"
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "bess_cnig_selected_feature_ids_json"] = '["A"]'
    return _rehash_coordinated_result(
        replace(result, parcels=parcels, relation_assessments=relations)
    )


def _invalid_lower_feature_id_result() -> BessPlanningFeatureParcelAggregationResult:
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(feature_id="HIGH", priority=30),
            ]
        )
    )
    relations = result.relation_assessments.copy(deep=True)
    relations.loc[relations.index[0], "planning_feature_id"] = "/tmp/feature"
    return _rehash_coordinated_result(replace(result, relation_assessments=relations))


def _cross_parcel_priority_conflict_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(
                    parcel_id="PARCEL-1",
                    feature_id="A",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    parcel_id="PARCEL-2",
                    feature_id="B",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=30,
                ),
            ]
        )
    )
    relations = result.relation_assessments.copy(deep=True)
    mask = relations["parcel_id"].eq("PARCEL-2")
    relations.loc[mask, "bess_cnig_status_priority"] = 50
    relations.loc[mask, "bess_cnig_resulting_parcel_status_priority"] = 50
    parcels = result.parcels.copy(deep=True)
    parcels.loc[
        parcels["parcel_id"].eq("PARCEL-2"), "bess_cnig_parcel_status_priority"
    ] = 50
    return _rehash_coordinated_result(
        replace(result, parcels=parcels, relation_assessments=relations)
    )


def _surface_touch_semantic_corruption_result() -> (
    BessPlanningFeatureParcelAggregationResult
):
    inputs, _, _, _, application = _application_fixture()
    changed_application = _surface_touch_with_positive_area(application)
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    original = module.validate_bess_application_relation_frame

    def bypass(*args: object, **kwargs: object) -> None:
        return None

    module.validate_bess_application_relation_frame = bypass
    try:
        return module._build_result(inputs[1], changed_application)
    finally:
        module.validate_bess_application_relation_frame = original


def test_exact_relations_select_configured_max_priority_and_lowest_confidence() -> None:
    relations = pd.DataFrame(
        [
            _relation(
                feature_id="LOW",
                priority=10,
                status="CONTEXT_REVIEW_REQUIRED",
                area=1000.0,
            ),
            _relation(
                feature_id="HIGH-A",
                priority=50,
                status="LIKELY_MATERIAL_CONSTRAINT",
                confidence="HIGH",
            ),
            _relation(
                feature_id="HIGH-B",
                priority=50,
                status="LIKELY_MATERIAL_CONSTRAINT",
                confidence="LOW",
            ),
        ]
    )
    result = _build_from_relations(relations)
    parcel = result.parcels.iloc[0]
    assert parcel.bess_cnig_parcel_aggregation_status == "AGGREGATED_EXACT_POLICY"
    assert parcel.bess_cnig_parcel_precheck_status == "LIKELY_MATERIAL_CONSTRAINT"
    assert parcel.bess_cnig_parcel_precheck_confidence == "LOW"
    assert parcel.bess_cnig_parcel_status_priority == 50
    assert parcel.bess_cnig_selected_feature_ids_json == '["HIGH-A","HIGH-B"]'
    assert parcel.bess_cnig_distinct_exact_status_count == 2
    assert bool(parcel.bess_cnig_multiple_exact_statuses) is True
    assert parcel.bess_cnig_selected_relation_count == 2
    assert parcel.bess_cnig_lower_priority_controlling_relation_count == 1
    assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "LOWER_PRIORITY_CONTROLLING",
        "SELECTED_CONTROLLING",
        "SELECTED_CONTROLLING",
    ]


def test_policy_unknown_is_exact_but_unresolved_controlling_overrides() -> None:
    exact_unknown = _build_from_relations(
        pd.DataFrame([_relation(status="UNKNOWN", confidence="LOW", priority=40)])
    )
    assert exact_unknown.parcels.iloc[0].bess_cnig_parcel_precheck_status == "UNKNOWN"
    unresolved = _relation(
        feature_id="UNRESOLVED",
        application_status="UNRESOLVED_CODE_PAIR",
        status=None,
        confidence=None,
        priority=None,
    )
    mixed = _build_from_relations(pd.DataFrame([_relation(), unresolved]))
    parcel = mixed.parcels.iloc[0]
    assert (
        parcel.bess_cnig_parcel_aggregation_status == "UNRESOLVED_CONTROLLING_CODE_PAIR"
    )
    assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
    assert pd.isna(parcel.bess_cnig_parcel_precheck_confidence)
    assert pd.isna(parcel.bess_cnig_parcel_status_priority)
    assert parcel.bess_cnig_unresolved_feature_ids_json == '["UNRESOLVED"]'
    assert mixed.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "DEFERRED_BY_UNRESOLVED_CONTROLLING",
        "UNRESOLVED_CONTROLLING",
    ]


@pytest.mark.parametrize("relation_type", ["AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"])
def test_every_positive_relation_type_controls_without_threshold(
    relation_type: str,
) -> None:
    result = _build_from_relations(
        pd.DataFrame([_relation(relation_type=relation_type, area=1e-15)])
    )
    assert result.parcels.iloc[0].bess_cnig_controlling_relation_count == 1
    assert (
        result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role
        == "SELECTED_CONTROLLING"
    )


@pytest.mark.parametrize("relation_type", ["TOUCH_ONLY", "BOUNDARY_TOUCH"])
def test_boundary_only_relations_are_contextual(relation_type: str) -> None:
    result = _build_from_relations(
        pd.DataFrame([_relation(relation_type=relation_type)])
    )
    parcel = result.parcels.iloc[0]
    assert parcel.bess_cnig_parcel_aggregation_status == "TOUCH_ONLY_RELATIONS_ONLY"
    assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
    assert parcel.bess_cnig_touch_only_feature_ids_json == '["F-1"]'
    assert (
        result.relation_assessments.iloc[0].bess_cnig_parcel_relation_role
        == "TOUCH_ONLY_CONTEXT"
    )


def test_touch_relation_remains_context_beside_a_controlling_relation() -> None:
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="EXACT"),
                _relation(
                    feature_id="TOUCH",
                    relation_type="TOUCH_ONLY",
                    priority=50,
                    status="LIKELY_MATERIAL_CONSTRAINT",
                ),
            ]
        )
    )
    assert result.parcels.iloc[0].bess_cnig_parcel_precheck_status == (
        "MATERIAL_REVIEW_REQUIRED"
    )
    assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "SELECTED_CONTROLLING",
        "TOUCH_ONLY_CONTEXT",
    ]


def test_no_relation_parcel_is_retained_without_a_decision() -> None:
    result = _build_from_relations(pd.DataFrame([_relation()]))
    parcel = result.parcels.iloc[1]
    assert parcel.bess_cnig_parcel_aggregation_status == "NO_PLANNING_FEATURE_RELATION"
    assert pd.isna(parcel.bess_cnig_parcel_precheck_status)
    assert bool(parcel.bess_cnig_formal_review_required) is True


def test_parcel_and_relation_prefixes_order_and_inputs_are_preserved() -> None:
    inputs, coded, config, policy, application = _application_fixture()
    parcels_copy = inputs[1].copy(deep=True)
    relations_copy = application.relations.copy(deep=True)
    result = aggregate_bess_planning_feature_policy_to_parcels(
        *inputs, coded, config, policy, application
    )
    assert_geodataframe_equal(inputs[1], parcels_copy)
    assert_frame_equal(application.relations, relations_copy)
    assert_geodataframe_equal(
        inputs[1], result.parcels.loc[:, inputs[1].columns], check_dtype=True
    )
    assert_frame_equal(
        application.relations,
        result.relation_assessments.loc[:, application.relations.columns],
        check_dtype=True,
    )
    assert tuple(result.parcels.columns[-len(PARCEL_COLUMNS) :]) == PARCEL_COLUMNS
    assert (
        tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS) :])
        == RELATION_COLUMNS
    )


def test_local_corruption_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, result = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "bess_cnig_selected_relation_count"] = 999
    corrupted = module._result_with_hashes(replace(result, parcels=parcels))
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        validate_bess_planning_feature_parcel_aggregation_result(
            *inputs, coded, config, policy, application, corrupted
        )
    assert calls == 0


@pytest.mark.parametrize(
    ("frame_name", "column", "value"),
    [
        ("parcels", "bess_cnig_selected_relation_count", 999),
        ("parcels", "bess_cnig_parcel_precheck_status", "UNKNOWN"),
        ("parcels", "bess_cnig_parcel_status_priority", 999),
        ("parcels", "bess_cnig_parcel_precheck_confidence", "LOW"),
        ("parcels", "bess_cnig_selected_feature_ids_json", "[]"),
        (
            "relation_assessments",
            "bess_cnig_parcel_relation_role",
            "TOUCH_ONLY_CONTEXT",
        ),
        ("relation_assessments", "parcel_id", "PARCEL-OTHER"),
    ],
)
def test_coordinated_local_cross_table_corruption_is_rejected(
    frame_name: str,
    column: str,
    value: object,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation(parcel_id="PARCEL-1")]))
    frame = getattr(result, frame_name).copy(deep=True)
    frame.loc[frame.index[0], column] = value
    corrupted = module._result_with_hashes(replace(result, **{frame_name: frame}))
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        module._validate_result_envelope(corrupted)


def test_invalid_output_dtype_and_non_2d_parcel_fail_locally() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation(parcel_id="PARCEL-1")]))
    parcels = result.parcels.copy(deep=True)
    parcels["bess_cnig_selected_relation_count"] = parcels[
        "bess_cnig_selected_relation_count"
    ].astype("object")
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, parcels=parcels))
        )
    relations = result.relation_assessments.copy(deep=True)
    relations["bess_cnig_selected_for_parcel_status"] = relations[
        "bess_cnig_selected_for_parcel_status"
    ].astype("object")
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        module._validate_result_envelope(
            module._result_with_hashes(replace(result, relation_assessments=relations))
        )
    parcels = result.parcels.copy(deep=True)
    geometry = parcels.geometry.iloc[0]
    parcels.at[parcels.index[0], parcels.geometry.name] = Polygon(
        [(x, y, 5) for x, y in geometry.exterior.coords]
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="2D"):
        module._validate_result_envelope(replace(result, parcels=parcels))


@pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame([_relation(status="AUTHORIZED")]),
        pd.DataFrame([_relation(status="FORBIDDEN")]),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="PROHIBITED",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    confidence="CERTAIN",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    relation_type="TOUCH_ONLY",
                    application_status="INVALID_APPLICATION_STATUS",
                )
            ]
        ),
    ],
    ids=[
        "selected-authorized",
        "selected-forbidden",
        "lower-prohibited",
        "lower-certain-confidence",
        "contextual-invalid-application-status",
    ],
)
def test_every_inherited_application_relation_domain_is_validated_locally(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(relations)


def test_unresolved_relation_cannot_contain_a_decision() -> None:
    row = _relation(
        application_status="UNRESOLVED_CODE_PAIR",
        status="UNKNOWN",
        confidence="LOW",
        priority=40,
    )
    row["official_code_status"] = "UNKNOWN_CODE_PAIR"
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(pd.DataFrame([row]))


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("feature_family", "OTHER"),
        ("type_code_raw", "7"),
        ("subtype_code_raw", "AA"),
        ("bess_cnig_application_scope", "WRONG_SCOPE"),
        ("bess_cnig_local_feature_text_interpreted", True),
    ],
)
def test_all_application_identity_scope_and_boundary_fields_are_intrinsic(
    column: str, value: object
) -> None:
    row = _relation(relation_type="TOUCH_ONLY")
    row[column] = value
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _build_from_relations(pd.DataFrame([row]))


def test_application_relation_suffix_dtype_is_validated_locally() -> None:
    relations = pd.DataFrame([_relation()])
    relations["bess_cnig_precheck_status"] = relations[
        "bess_cnig_precheck_status"
    ].astype("category")
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="dtype"):
        _build_from_relations(relations, canonicalize_application_dtypes=False)


@pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame(
            [
                _relation(
                    feature_id="A",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=50,
                ),
                _relation(
                    feature_id="B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=50,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="MAX",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    feature_id="LOW-A",
                    status="MATERIAL_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="LOW-B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=10,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(
                    feature_id="A",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
                _relation(
                    feature_id="B",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=10,
                ),
            ]
        ),
    ],
    ids=[
        "same-maximum-priority-two-statuses",
        "same-lower-priority-two-statuses",
        "same-status-two-priorities",
    ],
)
def test_status_and_priority_mapping_is_one_to_one_at_every_level(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="priority"):
        _build_from_relations(relations)


def test_valid_repeated_status_and_priority_mapping_selects_every_exact_match() -> None:
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="A", priority=30),
                _relation(feature_id="B", priority=30),
            ]
        )
    )
    assert result.parcels.iloc[0].bess_cnig_selected_relation_count == 2
    assert result.relation_assessments["bess_cnig_parcel_relation_role"].tolist() == [
        "SELECTED_CONTROLLING",
        "SELECTED_CONTROLLING",
    ]


@pytest.mark.parametrize(
    "relations",
    [
        pd.DataFrame([_relation(feature_id="A"), _relation(feature_id="A")]),
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(feature_id="HIGH", priority=30),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="TOUCH", relation_type="TOUCH_ONLY"),
                _relation(feature_id="TOUCH", relation_type="TOUCH_ONLY"),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="DEFERRED"),
                _relation(feature_id="DEFERRED"),
                _relation(
                    feature_id="UNRESOLVED",
                    application_status="UNRESOLVED_CODE_PAIR",
                    status=None,
                    confidence=None,
                    priority=None,
                ),
            ]
        ),
        pd.DataFrame(
            [
                _relation(feature_id="A", relation_type="AREA_OVERLAP"),
                _relation(feature_id="A", relation_type="LENGTH_OVERLAP"),
            ]
        ),
    ],
    ids=[
        "selected",
        "lower-priority",
        "contextual",
        "deferred",
        "different-relation-types",
    ],
)
def test_duplicate_parcel_feature_identity_is_rejected_for_every_role(
    relations: pd.DataFrame,
) -> None:
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="duplicate|unique"
    ):
        _build_from_relations(relations)


@pytest.mark.parametrize(
    "feature_id",
    [None, "", "None", "/tmp/feature"],
)
def test_invalid_lower_priority_feature_id_is_rejected_independently_of_json_role(
    feature_id: object,
) -> None:
    relations = pd.DataFrame(
        [
            _relation(
                feature_id=feature_id,
                status="CONTEXT_REVIEW_REQUIRED",
                priority=10,
            ),
            _relation(feature_id="HIGH", priority=30),
        ]
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="feature|identity"
    ):
        _build_from_relations(relations)


@pytest.mark.parametrize("feature_id", [r"C:\feature", " GPU:F "])
def test_invalid_deferred_feature_id_is_rejected_independently_of_json_role(
    feature_id: str,
) -> None:
    relations = pd.DataFrame(
        [
            _relation(feature_id=feature_id),
            _relation(
                feature_id="UNRESOLVED",
                application_status="UNRESOLVED_CODE_PAIR",
                status=None,
                confidence=None,
                priority=None,
            ),
        ]
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="feature|identity"
    ):
        _build_from_relations(relations)


@pytest.mark.parametrize("parcel_id", [None, " PARCEL-1 "])
def test_invalid_relation_parcel_id_is_rejected(parcel_id: object) -> None:
    relation = _relation()
    relation["parcel_id"] = parcel_id
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="parcel|identity"
    ):
        _build_from_relations(pd.DataFrame([relation]))


def test_unknown_relation_type_is_rejected_by_shared_relation_contract() -> None:
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="relation type"
    ):
        _build_from_relations(pd.DataFrame([_relation(relation_type="NEARBY")]))


@pytest.mark.parametrize("context_type", [None, "TOUCH_ONLY", "BOUNDARY_TOUCH"])
def test_document_wide_same_priority_cannot_map_to_two_statuses(
    context_type: str | None,
) -> None:
    second_type = context_type or "AREA_OVERLAP"
    relations = pd.DataFrame(
        [
            _relation(
                parcel_id="PARCEL-1",
                feature_id="A",
                status="LIKELY_MATERIAL_CONSTRAINT",
                priority=50,
            ),
            _relation(
                parcel_id="PARCEL-2",
                feature_id="B",
                relation_type=second_type,
                status="MATERIAL_REVIEW_REQUIRED",
                priority=50,
            ),
        ]
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="priority|mapping"
    ):
        _build_from_relations(relations)


def test_document_wide_same_status_cannot_map_to_two_priorities() -> None:
    relations = pd.DataFrame(
        [
            _relation(
                parcel_id="PARCEL-1",
                feature_id="A",
                status="LIKELY_MATERIAL_CONSTRAINT",
                priority=50,
            ),
            _relation(
                parcel_id="PARCEL-2",
                feature_id="B",
                status="LIKELY_MATERIAL_CONSTRAINT",
                priority=10,
            ),
        ]
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="priority|mapping"
    ):
        _build_from_relations(relations)


def test_document_wide_repeated_mapping_and_unresolved_rows_are_valid() -> None:
    relations = pd.DataFrame(
        [
            _relation(parcel_id="PARCEL-1", feature_id="A", priority=30),
            _relation(parcel_id="PARCEL-2", feature_id="B", priority=30),
            _relation(
                parcel_id="PARCEL-2",
                feature_id="U",
                application_status="UNRESOLVED_CODE_PAIR",
                status=None,
                confidence=None,
                priority=None,
            ),
        ]
    )
    result = _build_from_relations(relations)
    assert len(result.relation_assessments) == 3


def test_complete_five_status_policy_mapping_is_globally_valid() -> None:
    mapping = (
        ("LIKELY_MATERIAL_CONSTRAINT", 50, "HIGH"),
        ("UNKNOWN", 40, "LOW"),
        ("MATERIAL_REVIEW_REQUIRED", 30, "HIGH"),
        ("DESIGN_REVIEW_REQUIRED", 20, "MEDIUM"),
        ("CONTEXT_REVIEW_REQUIRED", 10, "HIGH"),
    )
    relations = pd.DataFrame(
        [
            _relation(
                parcel_id=f"PARCEL-{position}",
                feature_id=f"FEATURE-{position}",
                status=status,
                priority=priority,
                confidence=confidence,
            )
            for position, (status, priority, confidence) in enumerate(mapping, start=1)
        ]
    )
    result = _build_from_relations(
        relations,
        parcel_ids=tuple(f"PARCEL-{position}" for position in range(1, 6)),
    )
    assert len(result.relation_assessments) == 5


def test_selected_relation_role_requires_selected_status_and_priority() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(
        pd.DataFrame(
            [
                _relation(
                    feature_id="LOW",
                    status="CONTEXT_REVIEW_REQUIRED",
                    priority=10,
                ),
                _relation(
                    feature_id="HIGH",
                    status="LIKELY_MATERIAL_CONSTRAINT",
                    priority=50,
                ),
            ]
        )
    )
    relations = result.relation_assessments.copy(deep=True)
    relations.loc[relations.index[0], "bess_cnig_parcel_relation_role"] = (
        "SELECTED_CONTROLLING"
    )
    relations.loc[relations.index[0], "bess_cnig_selected_for_parcel_status"] = True
    corrupted = module._result_with_hashes(
        replace(result, relation_assessments=relations)
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        module._validate_result_envelope(corrupted)


def _validate_parcel_geometries(geometries: list[object]) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, application = _application_fixture()
    parcels = gpd.GeoDataFrame(
        {"parcel_id": [f"P-{index}" for index in range(len(geometries))]},
        geometry=geometries,
        crs="EPSG:2154",
    )
    result = module._build_result(
        parcels, replace(application, relations=application.relations.iloc[0:0])
    )
    module._validate_result_envelope(result)


@pytest.mark.parametrize(
    "geometry",
    [
        Point(0, 0),
        LineString([(0, 0), (1, 1)]),
        Polygon(),
        Polygon([(0, 0), (2, 2), (0, 2), (2, 0), (0, 0)]),
        None,
    ],
    ids=["point", "line", "empty", "invalid", "null"],
)
def test_malformed_parcel_geometry_is_rejected_intrinsically(geometry: object) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        _validate_parcel_geometries([geometry])


def test_valid_polygon_and_multipolygon_parcels_are_accepted() -> None:
    polygon = Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
    _validate_parcel_geometries([polygon, MultiPolygon([polygon])])


@pytest.mark.parametrize("frame_name", ["parcels", "relation_assessments"])
def test_duplicate_output_columns_are_rejected_intrinsically(frame_name: str) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    frame = getattr(result, frame_name)
    duplicate = pd.concat([frame, frame.iloc[:, [0]]], axis=1)
    if frame_name == "parcels":
        duplicate = gpd.GeoDataFrame(
            duplicate, geometry=frame.geometry.name, crs=frame.crs
        )
    corrupted = replace(result, **{frame_name: duplicate})
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="duplicate"):
        module._validate_result_envelope(corrupted)


@pytest.mark.parametrize("version", [1, 3, 999])
def test_only_application_result_schema_two_is_accepted(version: int) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    corrupted = module._result_with_hashes(
        replace(result, application_result_hash_schema_version=version)
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="application.*schema"
    ):
        module._validate_result_envelope(corrupted)


def test_application_result_schema_two_remains_accepted() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    assert result.application_result_hash_schema_version == 2
    module._validate_result_envelope(result)


@pytest.mark.parametrize(
    "feature_id",
    ["None", "nan", "<NA>", "/tmp/feature", r"C:\feature", " GPU:F "],
)
def test_noncanonical_feature_ids_are_rejected(feature_id: str) -> None:
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="Feature ID"):
        _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))


def test_current_gpu_feature_id_is_canonical() -> None:
    feature_id = "GPU:DOC:prescription_surface:FEATURE-01"
    result = _build_from_relations(pd.DataFrame([_relation(feature_id=feature_id)]))
    assert result.parcels.iloc[0].bess_cnig_selected_feature_ids_json == (
        f'["{feature_id}"]'
    )


def test_authorized_status_artifact_fails_local_verified_byte_loading(
    tmp_path: Path,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation()]))
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "bess_cnig_parcel_precheck_status"] = "AUTHORIZED"
    assessed = result.relation_assessments.copy(deep=True)
    assessed.loc[assessed.index[0], "bess_cnig_precheck_status"] = "AUTHORIZED"
    assessed.loc[assessed.index[0], "bess_cnig_resulting_parcel_precheck_status"] = (
        "AUTHORIZED"
    )
    source = assessed.drop(columns=list(RELATION_COLUMNS))
    corrupted = replace(
        result,
        parcels=parcels,
        relation_assessments=assessed,
        source_application_relations_content_sha256=module._frame_sha256(
            source,
            "landscout.bess_cnig_parcel_aggregation.source_application_relations",
        ),
    )
    corrupted = module._result_with_hashes(corrupted)
    manifest, paths, _ = _write_artifacts(tmp_path, corrupted)
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )


@pytest.mark.parametrize(
    "factory",
    [
        _duplicate_selected_pair_result,
        _invalid_lower_feature_id_result,
        _cross_parcel_priority_conflict_result,
    ],
    ids=["duplicate-pair", "invalid-lower-feature-id", "global-priority-conflict"],
)
def test_coordinated_relation_identity_artifact_corruption_fails_locally(
    tmp_path: Path,
    factory: object,
) -> None:
    assert callable(factory)
    corrupted = factory()
    manifest, paths, _ = _write_artifacts(tmp_path, corrupted)
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )


def test_controlling_relation_cannot_be_relabelled_contextual_in_artifact(
    tmp_path: Path,
) -> None:
    corrupted = _surface_touch_semantic_corruption_result()
    manifest, paths, _ = _write_artifacts(tmp_path, corrupted)
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="surface|metric|type"
    ):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )


@pytest.mark.parametrize("parcel_id", ["None", "nan", "<NA>"])
def test_no_relation_parcel_rejects_textual_null_identity(
    tmp_path: Path, parcel_id: str
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation(parcel_id="PARCEL-1")]))
    parcels = result.parcels.copy(deep=True)
    no_relation = parcels["bess_cnig_parcel_aggregation_status"].eq(
        "NO_PLANNING_FEATURE_RELATION"
    )
    assert no_relation.any()
    parcel_id_dtype = parcels["parcel_id"].dtype
    parcels.loc[parcels.index[no_relation][0], "parcel_id"] = parcel_id
    parcels["parcel_id"] = pd.array(
        parcels["parcel_id"].tolist(), dtype=parcel_id_dtype
    )
    corrupted = module._result_with_hashes(replace(result, parcels=parcels))
    manifest, paths, payload = _write_artifacts(tmp_path, corrupted)
    persisted_parcels = gpd.read_parquet(paths["PARCELS"])
    persisted_relations = pd.read_parquet(paths["RELATION_ASSESSMENTS"])
    for record in payload["artifacts"]:
        if record["artifact_role"] == "PARCELS":
            record["frame_schema_signature"] = deterministic_frame_schema_signature(
                persisted_parcels
            )
        else:
            record["frame_schema_signature"] = deterministic_frame_schema_signature(
                persisted_relations
            )
    manifest.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="parcel ID"):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )


def test_relation_identity_and_global_mapping_fail_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, _ = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    for corrupted in (
        _duplicate_selected_pair_result(),
        _invalid_lower_feature_id_result(),
        _cross_parcel_priority_conflict_result(),
    ):
        with pytest.raises(BessPlanningFeatureParcelAggregationError):
            validate_bess_planning_feature_parcel_aggregation_result(
                *inputs, coded, config, policy, application, corrupted
            )
    assert calls == 0


def test_relation_semantic_failure_fast_fails_before_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, _ = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        validate_bess_planning_feature_parcel_aggregation_result(
            *inputs,
            coded,
            config,
            policy,
            application,
            _surface_touch_semantic_corruption_result(),
        )
    assert calls == 0


@pytest.mark.parametrize(
    "status",
    [
        "ALLOWED",
        "AUTHORIZED",
        "COMPATIBLE",
        "CLEAR",
        "FORBIDDEN",
        "PROHIBITED",
        "BLOCKED",
        "BUILDABLE",
    ],
)
def test_parcel_decision_status_domain_rejects_forbidden_vocabulary(
    status: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    parcels = result.parcels.copy(deep=True)
    decision_index = parcels.index[
        parcels["bess_cnig_parcel_aggregation_status"] == "AGGREGATED_EXACT_POLICY"
    ][0]
    parcels.loc[decision_index, "bess_cnig_parcel_precheck_status"] = status
    corrupted = module._result_with_hashes(replace(result, parcels=parcels))
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="status"):
        module._validate_result_envelope(corrupted)


@pytest.mark.parametrize(
    "json_value",
    [
        '["None"]',
        '["nan"]',
        '["<NA>"]',
        '["/tmp/feature"]',
        r'["C:\\feature"]',
        '[" GPU:F "]',
        '["B","A"]',
        '["A", "B"]',
        '["A","A"]',
    ],
)
def test_persisted_feature_id_json_must_be_portable_and_canonical(
    json_value: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    _, _, _, _, _, result = _aggregation_fixture()
    parcels = result.parcels.copy(deep=True)
    parcels.loc[parcels.index[0], "bess_cnig_selected_feature_ids_json"] = json_value
    corrupted = module._result_with_hashes(replace(result, parcels=parcels))
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        module._validate_result_envelope(corrupted)


def test_representative_intrinsic_failures_all_precede_heavy_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, result = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    invalid_results: list[BessPlanningFeatureParcelAggregationResult] = []

    inherited = result.relation_assessments.copy(deep=True)
    inherited.loc[inherited.index[0], "bess_cnig_precheck_status"] = "AUTHORIZED"
    invalid_results.append(
        _rehash_coordinated_result(replace(result, relation_assessments=inherited))
    )

    parcel_status = result.parcels.copy(deep=True)
    parcel_status.loc[parcel_status.index[0], "bess_cnig_parcel_precheck_status"] = (
        "AUTHORIZED"
    )
    invalid_results.append(
        module._result_with_hashes(replace(result, parcels=parcel_status))
    )

    ambiguous = _build_from_relations(
        pd.DataFrame(
            [
                _relation(feature_id="A", priority=50),
                _relation(
                    feature_id="B",
                    status="DESIGN_REVIEW_REQUIRED",
                    priority=10,
                ),
            ]
        )
    )
    ambiguous_relations = ambiguous.relation_assessments.copy(deep=True)
    ambiguous_relations.loc[
        ambiguous_relations.index[1], "bess_cnig_status_priority"
    ] = 50
    invalid_results.append(
        _rehash_coordinated_result(
            replace(ambiguous, relation_assessments=ambiguous_relations)
        )
    )

    point_parcels = result.parcels.copy(deep=True)
    point_parcels.at[point_parcels.index[0], point_parcels.geometry.name] = Point(0, 0)
    invalid_results.append(replace(result, parcels=point_parcels))

    duplicate = pd.concat([result.parcels, result.parcels.iloc[:, [0]]], axis=1)
    invalid_results.append(
        replace(
            result,
            parcels=gpd.GeoDataFrame(
                duplicate,
                geometry=result.parcels.geometry.name,
                crs=result.parcels.crs,
            ),
        )
    )
    invalid_results.append(
        module._result_with_hashes(
            replace(result, application_result_hash_schema_version=3)
        )
    )

    json_parcels = result.parcels.copy(deep=True)
    json_parcels.loc[json_parcels.index[0], "bess_cnig_selected_feature_ids_json"] = (
        '["/tmp/feature"]'
    )
    invalid_results.append(
        module._result_with_hashes(replace(result, parcels=json_parcels))
    )

    for invalid in invalid_results:
        with pytest.raises(BessPlanningFeatureParcelAggregationError):
            validate_bess_planning_feature_parcel_aggregation_result(
                *inputs, coded, config, policy, application, invalid
            )
    assert calls == 0


def test_one_aggregation_and_one_public_validation_each_call_heavy_once(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application = _application_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    actual = module.validate_bess_planning_feature_application_result
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1
        actual(*args, **kwargs)

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    result = module.aggregate_bess_planning_feature_policy_to_parcels(
        *inputs, coded, config, policy, application
    )
    assert calls == 1
    module.validate_bess_planning_feature_parcel_aggregation_result(
        *inputs, coded, config, policy, application, result
    )
    assert calls == 2


def test_valid_two_file_verified_byte_artifacts_and_source_readback(
    tmp_path: Path,
) -> None:
    inputs, coded, config, policy, application, result = _aggregation_fixture()
    manifest, paths, _ = _write_artifacts(tmp_path, result)
    loaded = load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
    )
    assert_geodataframe_equal(result.parcels, loaded.parcels)
    assert_frame_equal(result.relation_assessments, loaded.relation_assessments)
    validate_bess_planning_feature_parcel_aggregation_result(
        *inputs, coded, config, policy, application, loaded
    )


@pytest.mark.parametrize(
    "mutation",
    [
        lambda value: value.update(schema_version=2),
        lambda value: value.update(application_result_hash_schema_version=1),
        lambda value: value.update(application_result_hash_schema_version=3),
        lambda value: value.update(application_result_hash_schema_version=999),
        lambda value: value["artifacts"].pop(),
        lambda value: value["artifacts"].append(
            {**value["artifacts"][0], "artifact_role": "EXTRA"}
        ),
        lambda value: value["artifacts"].append(dict(value["artifacts"][0])),
        lambda value: value["artifacts"][0].update(filename="wrong.parquet"),
        lambda value: value["artifacts"][1].update(
            filename=value["artifacts"][0]["filename"]
        ),
        lambda value: value["artifacts"][0].update(filename="C:/absolute.parquet"),
        lambda value: value["artifacts"][0].update(size_bytes=1),
        lambda value: value["artifacts"][0].update(sha256="f" * 64),
        lambda value: value["artifacts"][0].update(sha256="bad"),
        lambda value: value["artifacts"][0].update(row_count=999),
        lambda value: value["artifacts"][0]["frame_schema_signature"].update(
            index_names=["wrong"]
        ),
        lambda value: value["artifacts"][0].update(crs=None),
        lambda value: value["artifacts"][0].update(crs={"wrong": True}),
        lambda value: value["artifacts"][0].update(geospatial=False),
        lambda value: value.update(unknown=True),
    ],
)
def test_artifact_manifest_corruption_is_rejected(
    tmp_path: Path, mutation: object
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, manifest = _write_artifacts(tmp_path, result)
    assert callable(mutation)
    mutation(manifest)
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )


@pytest.mark.parametrize(
    "document",
    [
        '{"schema_version":1,"schema_version":1}',
        '{"schema_version":NaN}',
        '{"schema_version":Infinity}',
        "[]",
    ],
    ids=["duplicate-key", "nan", "infinity", "non-object"],
)
def test_aggregation_manifest_uses_strict_json_before_artifact_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    document: str,
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, _ = _write_artifacts(tmp_path, result)
    manifest_path.write_text(document, encoding="utf-8")
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    artifact_reads = 0
    original_read_bytes = Path.read_bytes

    def counted_bytes(path: Path) -> bytes:
        nonlocal artifact_reads
        if path in paths.values():
            artifact_reads += 1
        return original_read_bytes(path)

    def counted(*args: object, **kwargs: object) -> object:
        nonlocal artifact_reads
        artifact_reads += 1
        raise AssertionError("Artifact read preceded strict manifest validation")

    monkeypatch.setattr(Path, "read_bytes", counted_bytes)
    monkeypatch.setattr(module.pd, "read_parquet", counted)
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError,
        match="Duplicate JSON|finite|top-level|invalid",
    ):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )
    assert artifact_reads == 0


def test_aggregation_physical_replacement_is_rejected(tmp_path: Path) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, _ = _write_artifacts(tmp_path, result)
    paths["RELATION_ASSESSMENTS"].write_bytes(
        paths["RELATION_ASSESSMENTS"].read_bytes() + b"tamper"
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="size|SHA"):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )


def test_verified_bytes_are_the_bytes_parsed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    manifest_path, paths, _ = _write_artifacts(tmp_path, result)
    target = paths["RELATION_ASSESSMENTS"]
    verified = target.read_bytes()
    replacement = tmp_path / "replacement.parquet"
    result.relation_assessments.to_parquet(replacement, compression="gzip", index=True)
    replacement_bytes = replacement.read_bytes()
    original_read_bytes = Path.read_bytes
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    original_read = module.pd.read_parquet
    observed: list[bytes] = []

    def replace_after_read(path: Path) -> bytes:
        payload = original_read_bytes(path)
        if path == target:
            path.write_bytes(replacement_bytes)
        return payload

    def inspect_read(source: object, *args: object, **kwargs: object) -> object:
        if isinstance(source, BytesIO):
            observed.append(source.getvalue())
        return original_read(source, *args, **kwargs)

    monkeypatch.setattr(Path, "read_bytes", replace_after_read)
    monkeypatch.setattr(module.pd, "read_parquet", inspect_read)
    loaded = load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest_path, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
    )
    assert verified in observed
    assert_frame_equal(result.relation_assessments, loaded.relation_assessments)


def test_public_exports_are_stable() -> None:
    required = {
        "BessPlanningFeatureParcelAggregationArtifactManifest",
        "BessPlanningFeatureParcelAggregationError",
        "BessPlanningFeatureParcelAggregationResult",
        "aggregate_bess_planning_feature_policy_to_parcels",
        "load_bess_planning_feature_parcel_aggregation_artifacts",
        "validate_bess_planning_feature_parcel_aggregation_result",
    }
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    assert set(module.__all__) == required
    assert required.issubset(set(stages.__all__))


def _coherent_parcel_area_mutation(
    result: BessPlanningFeatureParcelAggregationResult,
    geometry_kind: str,
) -> BessPlanningFeatureParcelAggregationResult:
    relations = result.relation_assessments.copy(deep=True)
    index = relations.index[relations["geometry_kind"].eq(geometry_kind)][0]
    relations.loc[index, "parcel_metric_area_m2"] = 8000.0
    if geometry_kind == "SURFACE":
        relations.loc[index, "parcel_share_pct"] = (
            100.0 * float(relations.loc[index, "intersection_area_m2"]) / 8000.0
        )
    return _rehash_coordinated_result(replace(result, relation_assessments=relations))


@pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "AREA_OVERLAP"),
        ("LINE", "LENGTH_OVERLAP"),
        ("POINT", "INSIDE"),
    ],
)
def test_relation_parcel_area_is_bound_to_real_parcel_geometry(
    geometry_kind: str,
    relation_type: str,
) -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(
        pd.DataFrame([_relation(relation_type=relation_type)])
    )
    changed = _coherent_parcel_area_mutation(result, geometry_kind)
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="parcel.*area|area.*parcel"
    ):
        module._validate_result_envelope(changed)


def test_self_consistent_parcel_area_artifact_is_rejected(tmp_path: Path) -> None:
    result = _build_from_relations(pd.DataFrame([_relation(area=1.0)]))
    changed = _coherent_parcel_area_mutation(result, "SURFACE")
    manifest, paths, payload = _write_artifacts(tmp_path, changed)
    persisted = {
        "PARCELS": gpd.read_parquet(paths["PARCELS"]),
        "RELATION_ASSESSMENTS": pd.read_parquet(paths["RELATION_ASSESSMENTS"]),
    }
    persisted_result = _rehash_coordinated_result(
        replace(
            changed,
            parcels=persisted["PARCELS"],
            relation_assessments=persisted["RELATION_ASSESSMENTS"],
        )
    )
    for field in fields(BessPlanningFeatureParcelAggregationResult):
        if field.name not in {"parcels", "relation_assessments"}:
            payload[field.name] = getattr(persisted_result, field.name)
    for record in payload["artifacts"]:
        record["frame_schema_signature"] = deterministic_frame_schema_signature(
            persisted[record["artifact_role"]]
        )
    manifest.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(
        BessPlanningFeatureParcelAggregationError, match="parcel.*area|area.*parcel"
    ):
        load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest, paths["PARCELS"], paths["RELATION_ASSESSMENTS"]
        )


def test_parcel_area_validation_uses_reprojected_calculation_copy() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation(area=1.0)]))
    original = result.parcels.copy(deep=True)
    geographic = result.parcels.to_crs("EPSG:4326")
    changed = _rehash_coordinated_result(replace(result, parcels=geographic))
    module._validate_result_envelope(changed)
    assert_geodataframe_equal(
        result.parcels, original, check_dtype=True, check_crs=True
    )


def test_parcel_area_defect_fast_fails_before_application_source_validation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs, coded, config, policy, application, _ = _aggregation_fixture()
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    result = _build_from_relations(pd.DataFrame([_relation(area=1.0)]))
    changed = _coherent_parcel_area_mutation(result, "SURFACE")
    calls = 0

    def counted(*args: object, **kwargs: object) -> None:
        nonlocal calls
        calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", counted
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError):
        validate_bess_planning_feature_parcel_aggregation_result(
            *inputs, coded, config, policy, application, changed
        )
    assert calls == 0


def test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams() -> None:
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    assert tuple(
        inspect.signature(
            module.load_bess_planning_feature_parcel_aggregation_artifacts
        ).parameters
    ) == (
        "manifest_path",
        "parcels_path",
        "relation_assessments_path",
        "source_parcels",
        "application_result",
    )
    assert hasattr(module, "validate_bess_planning_feature_application_result_envelope")


def test_source_bound_aggregation_loader_accepts_only_supplied_upstreams(
    tmp_path: Path,
) -> None:
    inputs, _, _, _, application, result = _aggregation_fixture()
    manifest, paths, _ = _write_artifacts(tmp_path, result)
    loaded = load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest,
        paths["PARCELS"],
        paths["RELATION_ASSESSMENTS"],
        inputs[1],
        application,
    )
    assert (
        loaded.complete_result_content_sha256 == result.complete_result_content_sha256
    )


def test_aggregation_manifest_filenames_are_casefold_unique(tmp_path: Path) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    _, _, payload = _write_artifacts(tmp_path, result)
    payload["artifacts"][1]["filename"] = str(
        payload["artifacts"][0]["filename"]
    ).upper()
    with pytest.raises(ValueError, match="filename|duplicate"):
        BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)


def _changed_parcel_geometry_upstreams(
    source_parcels: gpd.GeoDataFrame,
    application: object,
) -> tuple[gpd.GeoDataFrame, object]:
    application_module = importlib.import_module(
        "landscout.stages.apply_bess_planning_feature_policy"
    )
    changed_parcels = source_parcels.copy(deep=True)
    parcel_id = str(application.relations.iloc[0]["parcel_id"])
    parcel_index = changed_parcels.index[changed_parcels["parcel_id"].eq(parcel_id)][0]
    geometry_column = changed_parcels.geometry.name
    geometry = changed_parcels.loc[parcel_index, geometry_column]
    changed_parcels.loc[parcel_index, geometry_column] = affinity.scale(
        geometry, xfact=2.0, yfact=2.0, origin="centroid"
    )
    metric = changed_parcels.to_crs(2154).loc[parcel_index, geometry_column].area
    relations = application.relations.copy(deep=True)
    mask = relations["parcel_id"].eq(parcel_id)
    relations.loc[mask, "parcel_metric_area_m2"] = float(metric)
    surface = mask & relations["geometry_kind"].eq("SURFACE")
    relations.loc[surface, "parcel_share_pct"] = (
        100.0
        * relations.loc[surface, "intersection_area_m2"].astype("float64")
        / float(metric)
    )
    changed_application = application_module._result_with_hashes(
        replace(application, relations=relations)
    )
    application_module._validate_result_envelope(changed_application)
    return changed_parcels, changed_application


@pytest.mark.parametrize(
    "mutation",
    [
        "parcel_geometry",
        "parcel_crs",
        "application_relation",
        "parcel_order",
        "unrelated_parcel_geometry",
    ],
)
def test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: str,
) -> None:
    inputs, _, _, _, application, _ = _aggregation_fixture()
    source_parcels = inputs[1]
    if mutation in {"parcel_order", "unrelated_parcel_geometry"}:
        extra = source_parcels.iloc[[0]].copy(deep=True)
        extra["parcel_id"] = pd.array(["NO-RELATION-PARCEL"], dtype="str")
        extra.geometry = extra.geometry.map(
            lambda geometry: affinity.translate(geometry, xoff=10_000.0)
        )
        extra.index = pd.Index(
            [int(source_parcels.index.max()) + 1],
            dtype=source_parcels.index.dtype,
            name=source_parcels.index.name,
        )
        source_parcels = gpd.GeoDataFrame(
            pd.concat([source_parcels, extra]),
            geometry=source_parcels.geometry.name,
            crs=source_parcels.crs,
        )
    changed_parcels = source_parcels.copy(deep=True)
    changed_application = application
    if mutation == "parcel_geometry":
        changed_parcels, changed_application = _changed_parcel_geometry_upstreams(
            source_parcels, application
        )
    elif mutation == "parcel_crs":
        changed_parcels = source_parcels.to_crs(4326)
    elif mutation == "application_relation":
        changed_application = _coordinated_policy_mutation(
            application,
            "bess_cnig_rationale",
            "A different exact relation rationale.",
        )
    elif mutation == "parcel_order":
        changed_parcels = source_parcels.iloc[::-1].copy(deep=True)
    else:
        related_ids = set(application.relations["parcel_id"])
        available = changed_parcels.loc[~changed_parcels["parcel_id"].isin(related_ids)]
        assert not available.empty
        index = available.index[0]
        changed_parcels.loc[index, changed_parcels.geometry.name] = affinity.translate(
            changed_parcels.loc[index, changed_parcels.geometry.name], xoff=1.0
        )
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    changed = module._build_result(changed_parcels, changed_application)
    module._validate_result_envelope(changed)
    manifest, paths, _ = _write_artifacts(tmp_path, changed)
    heavy_calls = 0

    def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1

    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", forbidden_heavy
    )
    with pytest.raises(BessPlanningFeatureParcelAggregationError, match="source lock"):
        module.load_bess_planning_feature_parcel_aggregation_artifacts(
            manifest,
            paths["PARCELS"],
            paths["RELATION_ASSESSMENTS"],
            source_parcels,
            application,
        )
    assert heavy_calls == 0


def test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    inputs, _, _, _, application, result = _aggregation_fixture()
    source_parcels = inputs[1]
    parcels_before = source_parcels.copy(deep=True)
    relations_before = application.relations.copy(deep=True)
    manifest, paths, _ = _write_artifacts(tmp_path, result)
    module = importlib.import_module(
        "landscout.stages.aggregate_bess_planning_feature_policy"
    )
    actual_build = module._build_result
    build_calls = 0
    heavy_calls = 0

    def counted_build(*args: object, **kwargs: object) -> object:
        nonlocal build_calls
        build_calls += 1
        return actual_build(*args, **kwargs)

    def forbidden_heavy(*args: object, **kwargs: object) -> None:
        nonlocal heavy_calls
        heavy_calls += 1

    monkeypatch.setattr(module, "_build_result", counted_build)
    monkeypatch.setattr(
        module, "validate_bess_planning_feature_application_result", forbidden_heavy
    )
    loaded = module.load_bess_planning_feature_parcel_aggregation_artifacts(
        manifest,
        paths["PARCELS"],
        paths["RELATION_ASSESSMENTS"],
        source_parcels,
        application,
    )
    assert (
        loaded.complete_result_content_sha256 == result.complete_result_content_sha256
    )
    assert build_calls == 1
    assert heavy_calls == 0
    assert_geodataframe_equal(source_parcels, parcels_before)
    assert_frame_equal(application.relations, relations_before)


def test_aggregation_loader_rejects_bad_application_before_artifact_reads(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    inputs, _, _, _, application, result = _aggregation_fixture()
    manifest, paths, _ = _write_artifacts(tmp_path, result)
    reads = 0
    original = Path.read_bytes

    def counted(path: Path) -> bytes:
        nonlocal reads
        reads += 1
        return original(path)

    monkeypatch.setattr(Path, "read_bytes", counted)
    forged = replace(application, complete_result_content_sha256="0" * 64)
    with pytest.raises(Exception, match="hash|SHA|invalid"):
        _load_aggregation_artifacts(
            manifest,
            paths["PARCELS"],
            paths["RELATION_ASSESSMENTS"],
            inputs[1],
            forged,
        )
    assert reads == 0


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
def test_aggregation_manifest_rejects_nonportable_filename(
    tmp_path: Path, filename: str
) -> None:
    _, _, _, _, _, result = _aggregation_fixture()
    _, _, payload = _write_artifacts(tmp_path, result)
    payload["artifacts"][0]["filename"] = filename
    with pytest.raises(ValueError, match="filename|basename|portable"):
        BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)
```
