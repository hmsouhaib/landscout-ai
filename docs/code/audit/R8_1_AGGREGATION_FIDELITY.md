# DOCS.CONTINUITY.1.R8.1 — aggregation documentation fidelity

Local correction of R8-D01..17; global audit **PARTIAL**, independent R8.1 review **PENDING**. A local CHECKED label is not independent approval. No production defect or A-005 is established by these documentary contradictions.

## Authority and bounded method

Exact supplied [R8.1 ticket](../../project/tickets/DOCS.CONTINUITY.1.R8.1.txt), section 1, archives the read-only ChatGPT reviewer statement: **CORRECTION_REQUIRED — R8 documentation only** at `e5279b1a7486afb973f4404d94a4bd3dd4f56483`, parent `fcf618ca6f569db35dd0f5b55cbca986393451ea`. It is not a Codex execution or cryptographic signature. The reviewer read the full two Python files and necessary dependency passages, not all upstream modules; did not run pytest, INDEX, application loaders, GPU/EP or rendering; and did not reattest all mappings/snapshots/preservation. [CURRENT_STATE](../../project/CURRENT_STATE.md) records that successor verdict without rewriting the [historical R8 receipt](R8_BESS_CNIG_AGGREGATION.md).

Starting local/tracking/server recovery HEAD: `e5279b1a7486afb973f4404d94a4bd3dd4f56483`. Repository `C:\souhaib\landscout-ai`, branch `recovery/docs-continuity-1-partial`. Main/local tracking/actual server: `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`. Clean index/worktree and no merge/rebase/cherry-pick/revert/bisect/index-lock operation at entry. Initial remote attempt failed; an escalated repository inspection then explicitly reported dubious ownership. Only after that error, the exact per-command `-c safe.directory=C:/souhaib/landscout-ai` permitted actual `ls-remote`; no persistent security setting changed.

Only seven authorized documentary paths change: the two companions below, `reviews/planning.json`, this receipt, `DOCUMENTATION_AUDIT.md`, `docs/project/CURRENT_STATE.md`, and the exact-byte ticket archive. No application/test/config bytes, hash algorithms, snapshots, previous tickets/receipts, coverage, original matrix or other fragments change. Temporary standard-library scripts stay outside Git under `C:\souhaib`; they read Git bytes/AST/Markdown/JSON without importing application modules. The unchanged auditor's parsing functions are used for bounded structural checks, not to infer semantic fidelity from AST.

Relevant bodies, effective call sites and assertions were reread in full; unchanged parts reuse the R8 reading. Changes are local paragraphs, not regenerated companions. Source and test snapshots/signatures are retained. The 21 concerned symbol notes (10 production, 11 test) are synchronized with prose in the sole planning owner, plus declaration R8-D16 at row provenance level: 22 corrected companion paragraphs in total. Unchanged notes and complete r8_prior_evidence remain. Each four-row resolution record points to the prior commit and this receipt rather than duplicating old rows again.

## Source identity and correction evidence

P = [unchanged production source](../../../src/landscout/stages/aggregate_bess_planning_feature_policy.py), 1495 lines; [production companion](../files/src/landscout/stages/aggregate_bess_planning_feature_policy.py.md).

T = [unchanged test source](../../../tests/unit/test_aggregate_bess_planning_feature_policy.py), 2211 lines; [test companion](../files/tests/unit/test_aggregate_bess_planning_feature_policy.py.md).

All line ranges below refer to Python, not Markdown. Owner names are relative to P or T as marked; every listed function/field has its own existing qualified section and symbol note in [planning.json](reviews/planning.json). D16 is a module declaration and has no original AST symbol row.

| Finding | Corrected notice and concerned owner note | Body, call or assertion evidence |
| --- | --- | --- |
| R8-D01 | P `_aggregate_frames`: `(parcels, assessments)`, GeoDataFrame then non-geospatial DataFrame. | P909–965 return order; `_build_result` P1021 and `_validate_result_envelope` P1211 unpack parcels first. |
| R8-D02 | T `_write_artifacts`: `(manifest_path, paths, manifest)`, not three Path values. | T382–431: Path, `dict[str, Path]` by PARCELS/RELATION_ASSESSMENTS, `dict[str, object]`; caller T1701 unpacks all three. |
| R8-D03 | P `_exact_string`: built-in ValueError, original untrimmed value. Related error-class note qualified. | P206–209 tests isinstance(str), nonempty and equality with strip; returns value. `_sha256_string` calls it at P213; envelope P1087–1100 catches ValueError. ID helper uses its own inline checks. |
| R8-D04 | P `_sha256_string`: no local translation to aggregation error. Related error-class note qualified. | P212–216 exact-string call then SHA_PATTERN.fullmatch; malformed syntax raises ValueError. Record P244 / manifest P360 use it in model validators; envelope wraps ValueError separately. |
| R8-D05 | P `_read_verified_artifact`: explicit mismatch guards versus unwrapped I/O/decode/library failures. Related error-class note qualified. | P1398–1443 has no enclosing catch around read_bytes, Parquet/schema/CRS operations. Public loader P1490–1495 preserves owned errors and wraps other Exception values. Captured bytes, not a post-read path seal. |
| R8-D06 | P `BessPlanningFeatureParcelAggregationArtifactRecord._validate_record`: local freeze, checks, then assignments. | P237–238 frozen locals; P239–254 filename/count/size/SHA/role/CRS guards; P255–260 object.__setattr__ of signature and non-null CRS; return self P261. |
| R8-D07 | P `_ApplicationLineage.complete_result_content_sha256`: upstream application digest directly. Related result/ArtifactManifest same-name notes separated. | Field P199; constructor P1208 copies result.application_complete_result_content_sha256. Aggregation result P289 / ArtifactManifest P328 instead hold aggregation complete digest. |
| R8-D08 | T `test_aggregation_manifest_uses_strict_json_before_artifact_read.counted`: forbidden-read sentinel. Parent and counted_bytes notes use one shared counter. | T1741–1744 increments artifact_reads then raises AssertionError; no delegated reader. counted_bytes T1735–1739 delegates original Path.read_bytes and increments only artifact paths. Parent T1755 asserts one counter == 0. Separate inspect_read T1793–1796 really delegates. |
| R8-D09 | T `test_aggregation_artifact_record_is_deeply_immutable_without_aliases`: actual input aliases and fresh expected payload. | T114–142 appends caller_mutation to columns, adds caller_mutation=True to CRS; checks geometry tuple/key absence and JSON dump against fresh helper payload. No saved dump/CRS-name edit. Four immediate mutation failures retained. |
| R8-D10 | T `test_valid_repeated_status_and_priority_mapping_selects_every_exact_match`: selected count and both roles only. | T947–960 count 2 and two SELECTED_CONTROLLING roles; no selected-ID JSON assertion. Named other test `test_exact_relations_select_configured_max_priority_and_lowest_confidence` T546–584 asserts `["HIGH-A","HIGH-B"]`. |
| R8-D11 | T `test_document_wide_repeated_mapping_and_unresolved_rows_are_valid`: three relations, two parcels, no aggregation envelope call. | T1138–1154 PARCEL-1/A and PARCEL-2/B,U; `_build_from_relations` T226–284 calls private builder. Sole explicit assert: relation count 3. |
| R8-D12 | T `test_policy_unknown_is_exact_but_unresolved_controlling_overrides`: builder/internal guards, not aggregation envelope. | T587–611 calls `_build_from_relations`; asserts exact UNKNOWN then unresolved state, three null decision fields, unresolved JSON and deferred/unresolved roles. |
| R8-D13 | T `test_artifact_manifest_corruption_is_rejected`: nineteen real mutations, no direct valid-record permutation case. | T1667–1696 versions (four cases), remove/append EXTRA/append duplicate (three), filenames (three), size, two SHA cases, row count, index_names, two CRS cases, geospatial, extra key; T1697–1708 adapter raises. First-guard limitations preserved. |
| R8-D14 | T `test_step_7d_5b_2b_5_aggregation_loader_requires_exact_upstreams`: ordered names and validator existence, not defaults. | T1935–1950 checks list(signature.parameters) and hasattr. Requiredness is visible in P1446–1452, not a separate test assertion. |
| R8-D15 | T `_relation`: exact default MATERIAL_REVIEW_REQUIRED / HIGH / 30. | T287–379 signature/body: APPLIED_EXACT_POLICY, AREA_OVERLAP, area 1e-6. Not LIKELY_MATERIAL_CONSTRAINT. |
| R8-D16 | T `PARCEL_COLUMNS`: real external column-dictionary link; no nonexistent local table. Companion-row resolution provenance, no new symbol. | T45–75 ordered test declaration; link resolves to production companion's Appended column dictionary. |
| R8-D17 | P `_validate_feature_id`: checks one supplied value; callers' broader coverage attributed separately. | P463–475 single value; `_json_ids` P478–480 checks selected/unresolved/context members, `_validate_json_ids` P483–504 checks readback members. P558–580 delegates all relation identities to common `validate_bess_application_relation_frame` (common/bess_application_contract.py508–553), including lower-priority/deferred rows. |

Classification: D01/D02 are interface errors; D03/D04/D05 local-error-boundary errors; D06 initialization-order and D07 lineage-ownership errors; D08–D14 test-evidence/call-path errors. D15 exact default terminology, D16 table navigation and D17 helper-versus-caller scope are smaller precision corrections, not equivalent to an inverted return or invented assertion. All seventeen concern documentation; none licenses changing production to match prose. Related copied error/hash/counter explanations were corrected in place, not treated as additional closure units.

Preserved R8 facts: no surface-weighted selection; exact UNKNOWN differs from unresolved code pairs; confidence uses selected relations only; three distinct validation paths; loader uses supplied upstream objects without new physical GPU validation; captured-byte Parquet reads do not guarantee a post-read path state; test adapter/global/first-guard limits remain explicit.

| Source | Git blob | Git-content SHA256 |
| --- | --- | --- |
| P | affad41097bbe253b002158c35537160d3846029 | 27bc7dcc9c67fead2c6f0638b033aab6e98282cfd2d865aec37dbf11b681c598 |
| T | 4a07d0f7f9a856dd8820cce917e7b9011e5c8ad4 | 52f53bc0808d49b0a50f4b09b2383af9b473308824472bfc3f6a3faf99479d83 |

## Validation boundary and historical results

No new pytest, application import/loader/pipeline, physical GPU/EP operation, Python linter/compiler, uv sync, install or environment change. **Historical R8 only:** 182 passed in 463.30 seconds, process exit 0. No independent reexecution is claimed. Visual Markdown rendering remains **PENDING**; no usable renderer is exercised or installed. Static links/fences/tables/Unicode checks are not visual approval.

The final bounded control reads the staged documentary lot: all 198 original mappings/qualified headings/signatures/ranges, snapshots against unchanged Git bytes, strict JSON, IDs/links/Unicode/tables/fences, old-formulation search limited to current notices, four owner-row boundaries, untouched prior evidence, 106 protected paths and all recalculated out-of-scope paths. It compares the new clean diff separately with the 13 inherited whitespace observations and preserves both known Git/checkout EOL exceptions. Semantic statements above result from reading bodies/calls/assertions, not AST generation.

## Candidate evidence and exact final delta

After explicit staging of exactly seven authorized paths, the single bounded control `.venv\Scripts\python.exe -B -X utf8 C:\souhaib\r81_check.py` passed, process exit 0. Its retained output is `C:\souhaib\r8-1-bounded-check.json`. It verifies 198/198 existing symbol mappings and signatures/ranges, complete unchanged fenced snapshots, 225 explicit IDs, 263 heading IDs, 59 local links, two incoming companion links, 228 qualified references, 73 table lines and 13 strict JSON files in that candidate. These are structural counts, not independent semantic approval. All 21 replaced symbol notices are absent from current companion prose and replaced owner notes; historical prior evidence is deliberately excluded from that absence claim. D16's old table claim is absent from the test companion. Four owner rows only change; no status, original symbol identity or prior-evidence payload changes.

All 106 protected files match the authority's Git OIDs/content SHA256/checkout SHA256 and main. Of 294 starting tracked paths, **289 initial paths outside the seven-path write set are unchanged** (five existing allowed paths, two new). The two Python identities match the table above; all companion signature/snapshot blocks equal those at the starting commit. The two historical EOL exceptions remain exactly as recorded, not normalized: structure-policy YAML checkout `879d50627c063bb10096950d004cf4d4e446ff04ef9a1178b3e3fb28e2ffdae3` versus Git `c736ea8901997f4852fd1f72a3f6f34282452f18dcd9abc0ccbce8255adaad45`; original RESUME ticket checkout `9e18c25d571c5cfe34391d1f35833634bb4c3672087781360752fa0fba7243ed` versus Git `b5a0fa80569fbc0b11d28718c0037f9e8ba23caac5dadca6fd60c05c7cc64a5b`. New staged diff is whitespace-clean; main-to-candidate `diff --check` retains exactly the same 13 historical observations, including output text and exit 2, as main-to-start. None is repaired in this ticket.

Companion Git-content SHA256 bindings updated only in their existing owner rows:

| Companion | SHA256 |
| --- | --- |
| Production P | 1cec06e3f60561dc6001586b72d96a03e104d886371618446309f2eecd524e88 |
| Test T | 4433a8a5bebd603dd7fa9afb1a74dcbc5c8ea105062ae72c56eb2677ba57e85e |
| Exact-byte R8.1 ticket archive | 601d30151074cd5d3234f7818f54f6519081de4866774ce970039dfa9247f502 |

Exactly one complete unchanged INDEX-auditor invocation followed staging:

```text
.venv\Scripts\python.exe -B -X utf8 tools/audit_documentation.py --check --progress > C:\souhaib\r8-1-candidate.stdout.txt
```

Progress/stderr was also retained as `C:\souhaib\r8-1-candidate.stderr.txt`; full sorted path/mode/OID manifest is `C:\souhaib\r8-1-candidate.manifest.json`. Completion: **completed=true, process exit 1, 10,267 findings**, not exit 2/timeout/interruption and not a global clean audit. Metrics: 296 files, 293 unique blobs, 28,753,040 indexed bytes, 94 Python files / 94 AST parses, 4,863 enumerated symbols, original coverage 245 files / 4,769 symbols, five Git processes, non-shallow history. Phase times in seconds: index 0.192692; coverage-input 0.010851; python 0.747395; references 0.110206; coverage 0.105701; checkout-markdown 0.267219; history 0.069213; index-postcondition 0.026325. These timings are not a new pytest result.

Candidate manifest SHA256 (sorted triples, compact ASCII JSON): `8d504302ebacbc12c80c92de80ac2c926c5df2e938885d136de762570b46b3b8`. Complete captured UTF-16 stdout: 2,316,024 bytes, SHA256 `aa1948d6678a06dd9005fc61a51acef8f57eaedfe512ec831b8fda73eae271e8`. The read-only comparison script `C:\souhaib\r81_compare.py` retained full metrics and exact removed/added finding lines in `C:\souhaib\r8-1-candidate.comparison.json`; it verified the existing R8 stdout digest before comparing all lines as multisets, not sampling or subtracting totals alone.

Compared with R8's 10,267-finding candidate: **10,266 unchanged finding occurrences, one removed line, one added line**. The replaced inventory-mismatch line adds only `docs/project/tickets/DOCS.CONTINUITY.1.R8.1.txt` to its missing list; all other list entries and empty extra list stay the same. The relevant-path subset (aggregation, planning owner, state/ledger/new receipt/ticket) remains 406 occurrences, with only that same inventory-line replacement. No new companion-reference failure appears. The unchanged total is observed, not a target or semantic certification. Global coverage is intentionally not merged to hide existing findings.

After this audit, **only this receipt** replaces its single pending-result token with the evidence above; all other indexed paths/modes/OIDs remain those of the audited candidate. The targeted final-delta control verifies exact prefix/suffix preservation, the sole receipt change, its new links/tables/fences/Unicode, index/worktree equality and clean incremental diff. It reports actual final manifest/receipt digests and byte delta externally, avoiding a self-referential receipt hash. No second complete INDEX run or repeat full bounded audit is performed; the final tree is not claimed byte-identical to the audited candidate. Final Git/remote checks are reported externally after publication.

## Unchanged progression and stop boundary

Four existing R8 units only; zero additional closure credit. Local recorded totals remain **83/245 files and 1,792/4,769 symbols**, with **162 files / 2,977 symbols** unfinished. CHECKED/CORRECTED labels are not an independent approval of all those units. Original matrix/coverage and all r8_prior_evidence remain unchanged. R8 successor verdict is documentary CORRECTION_REQUIRED; R8.1 independent review is PENDING after publication.

A-001..A-004, five historical test-evidence limits, R3-T01..04, OPEN R5-D01, cold-start/render/global acceptance and 7F.1C.1 semantic review remain open/pending. Last approved functional boundary remains 7F.1B.4, `ca0ec73de37137b5515c1dfea14e2ea8a2a1ba3d`, with its original full-review-receipt gap preserved. No next application group, R9 or functional step is authorized.

Publication is recovery-only with `docs: correct aggregation reference fidelity`; final commit/server identity and clean-tree checks are reported after Git resolves them, never invented as this receipt's own future SHA. Stop after publication for review.
