# R15.1 — IGN test companion side effects

Local documentary correction of [R15](R15_IGN_BDTOPO_SOURCE.md) at starting recovery commit `29732dd3f4f1b4f0f2351d18e1f9d2d96a503091`. The [exact supplied ticket and reviewer statement](../../project/tickets/DOCS.CONTINUITY.1.R15.1.md) says **CORRECTION_REQUIRED** for R15 documentation. Its two blocking reservations concern eight cells in [the IGN test companion](../files/tests/unit/test_ign_bdtopo_fr.py.md), not a newly demonstrated application defect. This local correction awaits independent review; the global audit remains **PARTIAL**. The statement's source readings and limits belong to the reviewer; they are not a new Codex execution or exhaustive owner/snapshot certification.

## Eight corrections against unchanged tests

The published `tests/unit/test_ign_bdtopo_fr.py` bodies and their companion notices were read for these eight functions. Each row below identifies the single changed cell; every other line of those notices, including purpose, assertions, signature, range, anchor and repeated code, is retained from R15.

| Reservation | Function | Previous cell | Corrected direct evidence |
|---|---|---|---|
| R15-REV01 | `test_ambiguous_electric_line_layers_fail` | Write: `None directly present.` | `pyogrio.write_dataframe(..., layer="LIGNE_ELECTRIQUE_SECONDAIRE", append=True)` writes a second layer to a synthetic GPKG. |
| R15-REV01 | `test_ambiguous_road_layer_fails_safely` | Write: `None directly present.` | `pyogrio.write_dataframe(..., layer="TRONCON_DE_ROUTE_SECONDAIRE", append=True)` writes a second layer to a synthetic GPKG. |
| R15-REV01 | `test_road_loader_rejects_changed_layer_inventory` | Write: `None directly present.` | `pyogrio.write_dataframe(..., layer="ADDED_AFTER_EXTRACTION", append=True)` changes the extracted synthetic GPKG. Its stale size/SHA can reject before isolated layer-inventory comparison. |
| R15-REV01 | `test_department_coverage_layer_discovery_must_be_unambiguous` | Write: `None directly present.` | `pyogrio.write_dataframe(..., layer="DEPARTEMENT_SECONDAIRE", append=True)` writes a second layer to a synthetic GPKG. |
| R15-REV02 | `test_download_revalidates_a_tampered_config_before_network` | Mutation: `None directly present.` | `object.__setattr__(tampered, "provider", "UNTRUSTED")` changes the local deep model copy. |
| R15-REV02 | `test_non_electric_layer_loaders_revalidate_mutated_role_config_before_read` | Mutation: `None directly present.` | Road branch changes copied nested `match_tokens` to `()`; coverage branch changes copied nested `department_code_field` to `" "`, both via `object.__setattr__`. |
| R15-REV02 | `test_missing_required_source_field_fails` | Mutation: `None directly present.` | `del content[field]` removes `source_url` or `edition` from a local `_config_data()` dictionary. |
| R15-REV02 | `test_invalid_department_coverage_config_fails` | Mutation: two assignments only. | Adds `del content["coverage"]` in the `missing` branch; retains the blank-field and empty-token assignments in their own branches. |

The two `Direct parameter mutation` rows in those model/dictionary tests stay unchanged: copying the model or building a local dictionary does not mutate the original fixture argument or the YAML on disk. The four GeoPackage writes are direct calls inside the test bodies, distinct from delegated fixture writes or official acquisition. Existing `gpd.read_file` and transport sentinels and their assertions remain as published.

## Ownership, history and scope

`docs/code/audit/reviews/foundations.json` remains the sole owner of the IGN test unit; the companion has embedded documentation state, without a new row. All eight targeted R15 purpose notes were already accurate against the bodies. Their R14 predecessor notes were generic READ notices, preserved through `r15_prior_evidence`; all eight R15 notes and all other symbols remain unchanged. Only this row's companion SHA256 binding and compact `r15_1_provenance` are added/updated. Its `r15_provenance` remains historical PENDING, while the new provenance separately records the supplied correction request and local correction pending review.

Starting test source Git OID `560c3ec1774ec514e77f58e1f9a63ec6599de2db`, source Git SHA256 `39d0e303aec55a24866a2c41b32bdb215203b4280fb748421454120eae24f078`; source adapter OID `876207e3b1b0ac4c1a245c01fdad91e72e5bb4d3`. The companion binding moves from `f4ac55a98498fcac75098f9cb05116ffd57068a854145e7d2979d6aa18613f83` to `dcb9da1a08dcb30f8a2196c3a5535e46fd1dbd416f117f910df02239ae6b6964`, SHA256 of its new exact Git content. Source/test bytes, the source companion and both R14 retouches stay unchanged. The supplied R15 reviewer accepted those R14 retouches within their stated scope.

Coverage gain **0 files / 0 symbols**: locally recorded totals stay **111/245 files and 3,330/4,769 symbols**, leaving **134 files / 1,439 symbols**. The original global coverage ledger and matrix remain unmerged. Preserve A-001..A-004, OPEN R5-D01, R15-T01..05, earlier limits, visual/cold-start/global acceptance gaps, incomplete EP 7F.1C.1 semantic review and the original 7F.1B.4 review-receipt gap. Last approved functional boundary stays 7F.1B.4. No new functional action follows from this receipt.

## Bounded verification and candidate audit

The bounded static check compares all eight exact cells to the unchanged Python bodies, preserves all other companion lines and code fences, checks strict owner JSON and the single fingerprint/provenance delta, exact ticket archive, links/table/Unicode structure, the 106 protected files and all initial paths outside the six allowed outputs. It separately compares Git content, index and checkout bytes, retaining the two historical EOL exceptions and thirteen inherited whitespace observations. `git diff --check` is required on the new delta. Temporary scripts and logs live outside Git. No pytest or application import is authorized for this prose correction; R15's 125 passes and R14's 174 passes remain historical results. Visual rendering remains unexecuted and **PENDING**.

Only six named documentary paths form the staged candidate. One unchanged full INDEX auditor run is required; native exit, `completed`, actual findings, sorted path/mode/OID manifest and comparison to available R15 candidate logs are recorded below. Exit 1 with `completed=true` leaves the global audit **PARTIAL**. Only this receipt's placeholder is filled after the run, with the receipt-only delta and unchanged other candidate OIDs checked separately. No final-tree finding total is inferred from the pre-completion candidate.

The single unchanged INDEX auditor finished with **native exit 1 / completed=true / 10,209 findings**, wrapper elapsed **1.9434015 seconds**. The global audit remains **PARTIAL**; this is a completed run, not a green result. Candidate manifest (sorted path/mode/OID compact JSON SHA256) is `94b04614ab97276512a95b08957a648a19a287ac00d7b29c58421f9bdd5c6f0d`: 316 paths, 313 unique blobs, 27,822,840 bytes, 94 Python files / 94 AST parses / 4863 actual symbols, historical denominator 245 files / 4769 symbols, 5 Git processes. The index and auditor remained unchanged during this run.

Compared by exact finding-line multiplicity with the actual R15 *candidate* logs (manifest `a54db5d82f6b18bbee8bc0254ab4be173405fad0077feb5de8fc21306df2ebe6`, exit 1, completed=true, 10,209 findings): **10,208 occurrences shared, one removed and one added**; count **10,209 → 10,209**. Both changed lines are the inventory-mismatch diagnostic: the new one includes the R15.1 ticket path. No diagnostic was removed because the eight prose cells were repaired. The unchanged `stale file fingerprint: docs/code/files/tests/unit/test_ign_bdtopo_fr.py.md` refers to the deliberately unmerged global coverage ledger; the active foundations owner has the correct new companion SHA. There is no unresolved qualified-reference finding for the changed companion. The other 10,208 common findings are not thereby classified as harmless or repaired; global missing anchors, unresolved review rows/symbols, links, exports, exceptions, snapshots and earlier reserves remain. The R15 comparator is its pre-receipt candidate, not R15's committed final tree.

Staged bounded static verification passed: exactly eight source-matched cell substitutions and unchanged test bodies/companion code blocks; one owner row changed only in companion SHA and successor provenance, with **all 105 symbol notes and states unchanged**. Six allowed paths, 310 initial outside-scope paths, 106 protected files, two unchanged historical EOL exceptions, exact ticket archive and thirteen inherited whitespace observations were checked. Strict JSON, Markdown fences/tables, Unicode, local links and `git diff --check` passed. This is static proof, not an executed visual renderer or independent acceptance. No pytest, application import, acquisition or official GPKG read occurred for R15.1.

Local evidence retained outside Git:

- `C:/souhaib/r15-1-candidate.stdout.txt`: 2,297,970 bytes; SHA256 `6a8d6f0cc4a70b64c91c6f0a9d57e8eef6723e21dde9500d518796b2b23fa4cd`.
- `C:/souhaib/r15-1-candidate.stderr.txt`: 64,462 bytes; SHA256 `b57f64e466a08380981e9fbab15fe7e6946f60dcba3a1b3d2cf0ffca9e6b4f3e`.
- `C:/souhaib/r15-1-candidate.manifest.json`: 81,262 bytes; SHA256 `2fa54429c1ba78b7a7127b86b79b7e79a64514ed44e22c93bcb16a06d5f185ed`.
- `C:/souhaib/r15-1-compare.json`: 10,242 bytes; SHA256 `b250e8a7d4b2da29724ff780c3027540e5953967e05954cf662ab1135d535741`.
- `C:/souhaib/r15-1-static-index.json`: 4,340 bytes; SHA256 `0f409b35c7447b76c14b3460efb98faa87c889c189a4a4c8dc8db26ea7da14dd`.
- `C:/souhaib/r15-candidate.stdout.txt`: 2,297,868 bytes; SHA256 `f5b60b351bde41de756bc10331c441e2d5a56366ddd6ecf5208f589061542d10`.
- `C:/souhaib/r15-candidate.stderr.txt`: 64,204 bytes; SHA256 `709b60b5242dd0e6de11e1c5589290aa0b64876a3495ea8dcea40044e629bffa`.
- `C:/souhaib/r15-candidate.manifest.json`: 80,742 bytes; SHA256 `ad2009f26a26d91e38ced7afe03bebd18bb5f03dbc5750ee97c73727226bb0a9`.

Candidate receipt before completion: OID `46082edd88452d57a0d7b349c581628e60e23331`, 6,863 bytes, SHA256 `5d70e3575aa7d31bda47990e0f4f65b8e54b6179737cff527ea0e3e806c01432`. Only the dedicated auditor-result placeholder is replaced afterward. The exact receipt-only path/mode/OID delta and final manifest are checked and kept outside the receipt to avoid self-hashing circularity. No second full auditor or final-tree finding count is asserted. Publication SHA, clean index/worktree and remote/main identities must be read from Git after commit/push.

After publication, resolve the real recovery SHA and verify clean index/worktree, tracking/server recovery equality and unchanged local/tracking/server main. Independent R15.1 acceptance remains pending.
