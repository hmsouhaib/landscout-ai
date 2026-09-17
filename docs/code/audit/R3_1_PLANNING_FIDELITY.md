# DOCS.CONTINUITY.1.R3.1 — planning companion fidelity correction

Status: bounded documentary correction; independent acceptance **PENDING**.
Global DOCS.CONTINUITY.1 remains **PARTIAL**. No application change or approval.

## Authority, review scope and readiness

Authority: [exact supplied R3.1 ticket](../../project/tickets/DOCS.CONTINUITY.1.R3.1.txt),
attachment `5507b64e-9192-4745-af9b-00d4a12d4a00/pasted-text.txt`.
Attachment/archive: 17,473 exact UTF-8 bytes, SHA256
`8a003524859b7ba22c6a1687028d00358f4fcd54dc5c467ca19816b5e4fd378b`.

Clean starting branch `recovery/docs-continuity-1-partial`; HEAD, local tracking
and actual remote recovery: `aad641420c0b0d2c8c503815854ae9c17f4d09f4`.
Local tracking and actual remote main: `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`.
No unmerged entries or Git operation. Sandbox remote access failed; the native
explicit-root check reproduced the ownership mismatch (repository owner
Hammami/CodexSandboxOffline, execution HAMMAMI/souha), then the authorized
command-only `-c safe.directory=C:/souhaib/landscout-ai` remote query succeeded.
No persistent trust, ACL, security, hook, dependency or history change; no fetch.

The supplied independent read-only review covers the entire published planning
source/test and both companions' unique explanatory prose at that starting SHA.
Verified reviewed Git blobs:

- Source: `e19525566471a99743aa6c3d36ac3096a78eeb5e` (1–2057).
- Test: `085c5bc7838159598656675e945aa8d54491c0d8` (1–2287).
- Source companion: `d5e9e6bcaf3ec9675e11807941d3fb7c68db2eaa`.
- Test companion: `399875f8fe5a9515381e385cf1cdf65f0be8d5cc`.

Verdict: **CORRECTION_REQUIRED for specific documentary findings**, not rejection
of the whole R3 implementation. The reviewer did not newly execute the 183 cases,
byte-check complete snapshots, visually render Markdown, independently scan all
206 owner records or rerun A-003. Those activities are not attributed to it here.
The unchanged [R3 receipt](R3_PLANNING_FEATURES.md) retains its historical evidence.

Read the entry/rules/state/step/decision/gap/resume route, technical index, audit
ledger, original continuity/R3/recovery instructions and R3 receipt. Read both
existing companions' unique prose and all 122 test/helper notices against the
complete unchanged test bodies and referenced fixture helpers; inspected the
private/public source boundary in context (1649–1814). Existing complete-source
reading evidence is retained, not replaced by an AST inventory. No unrelated
configuration review, new application execution or broad audit was started.

## D-ANCHOR — exact public/private ownership

Before correction, the source companion had two explicit occurrences of
`r3-validate-normalized-planning-feature-inputs`, and two distinct symbol records
used it. An anchor set could not detect that defect; the old R3 presence-check
statement is historical and insufficient, not fresh uniqueness evidence.

- Public [validate_normalized_planning_feature_inputs](../files/src/landscout/stages/enrich_planning_features.py.md#r3-validate-normalized-planning-feature-inputs),
  source 1790–1814, retains `r3-validate-normalized-planning-feature-inputs`.
- Private [_validate_normalized_planning_feature_inputs](../files/src/landscout/stages/enrich_planning_features.py.md#r3-private-validate-normalized-planning-feature-inputs),
  source 1649–1787, uses `r3-private-validate-normalized-planning-feature-inputs`.

The repository-wide pre-edit search found only the two definitions and two owner
mapping values, no incoming Markdown link or historical receipt using that ID.
Only the private mapping is redirected; no duplicate alias is added. The two new
links above explicitly name their intended targets. Historical receipts are unchanged.

The bounded checker counts explicit IDs outside fences and associates each with
the immediately following exact qualified heading, preserving leading underscore
and enclosing scope. It checks displayed signature/range/hash against unchanged
Python, one distinct destination per record, and exact matching owner notes.
It is not a visual/DOM renderer and does not change the global auditor.

## D-FACTS / D-SCOPE — body-level corrections

These are targeted paragraph changes in the
[test companion](../files/tests/unit/test_enrich_planning_features.py.md) and the
same first review note in [the owner fragment](reviews/inpn_roads_extension.json).
No fixture, assertion, signature, line range or Python byte changes.

| Test/helper (unchanged test lines) | Corrected evidence |
|---|---|
| test_polygon_and_multipolygon_surfaces (479–488; decorators 472–478) | information_surface, INFORMATION / SURFACE, not prescription. One relation and positive intersection area only; no exact MultiPolygon area assertion. |
| test_line_boundary_touch_is_zero_length (510–519) | prescription_line from (10,5) to (15,5), starts at the 0..10 parcel boundary and extends outside. TOUCH_ONLY, zero clipped length, one line touch. |
| test_points_inside_boundary_outside_and_multipoint (540–564) | prescription_point for IN/BOUNDARY/OUT/MULTI, not information. Only IN/BOUNDARY/MULTI relate; MULTI full count 3, inside/boundary 1 each; three pairs, parcel member totals 2/2. |
| test_duplicate_parcel_ids_are_rejected (617–622) | IDs ["P","P"], squares (0,0)–(2,2) and (3,3)–(4,4), different sizes. Initial duplicate-ID rejection, not equal-shape/DUP fixtures. |
| test_duplicate_source_ids_are_rejected (625–632) | information_surface and ["SAME","SAME"], not prescription/DUP; per-role uniqueness after physical read, not cross-role uniqueness. |
| test_same_source_id_is_allowed_in_distinct_logical_layers (1411–1429) | SHARED in prescription_line and prescription_point. Two relations and two distinct planning_feature_id values. |
| test_source_complete_contract_accepts_epsg4326_parcels (1704–1708) | Discards earlier result via _, reprojects parcels, calls builder again, validates the newly built result with those geographic parcels. No old-result reuse claim. |
| test_source_complete_contract_rejects_tampered_gpkg_inventory_hash (1916–1931) | Envelope SHA replacement is "f" * 64, not b; physical GPKG and marker unchanged. |
| _shapefile_source_complete_contract (2085–2107) | Physical prescription-surface Shapefile, CNIG ID SHAPE-1, code pair 07/04, not PSC-SHP. |
| test_source_complete_contract_rejects_changed_shapefile_sidecar_bytes (2196–2207) | Exact call is cpg.write_text("UTF-8\n", encoding="utf-8"); UTF-8 text plus newline, platform text-mode newline translation, stale inventory/marker. Not an ISO-8859-1 family change. |
| test_present_empty_optional_layer_is_valid (875–905) | Empty catalog/relations, catalog CRS, one parcel and document lineage assertions are common to all three kinds. CNIG-ID drop, reader spy and fid_reads == 1 are surface-only; no measured line/point reader-call count. |
| test_epsg4326_parcels_are_measured_in_lambert93_but_preserved (594–608; helper 71–89) | Synthetic 0..10 square assigned EPSG:2154 then transformed, not “realistic” geography. Output CRS/WKB preservation and approximately 100 m2 remain the actual assertions. |

Two nested notices are also synchronized with their owner notes:

- `test_present_empty_optional_layer_is_valid.unexpected_fid_read` (886–890):
  defined/installed only in the surface branch, delegating real reads and counting
  fid_as_index; this extends the requested D-SCOPE qualification to its helper.
- `test_source_complete_contract_rejects_linked_spatial_dataset.synthetic_link`
  (2073–2074): true for the selected dataset without delegation; otherwise returns
  the real detector's result, which can also be true. Removes the ambiguous
  “true only for selected dataset” claim. No OS link creation is tested.

All other notices were cross-checked for concrete values, logical roles, mutation
sites, helper behavior, call order and actual assertions; no additional mismatch
was identified in that bounded comparison. Good R3 distinctions are retained:
frozen envelopes/mutable frames, real local data/fabricated ZIP lineage, full versus
clipped metrics, raw sums versus unions, early rejection and unvisited branches.
No branch instrumentation, fresh pytest, official-source or A-003 run is claimed.

## Owner reconciliation and preserved authority

Exactly the same four rows remain: source/test CHECKED (84/122 symbols), both
companions CORRECTED. Changes are 14 test/helper first notes, one private anchor,
two companion fingerprints and scoped R3.1 provenance on those rows. Original
R3 fields/r3_prior_evidence/receipt and all other symbol fields are retained.
R3 review findings and R3.1 pending acceptance are explicit; CHECKED is not an
independent approval. No unrelated row/status promotion or global-ledger merge.

Totals stay **71/245 files; 1,594/4,769 symbols**; **174 files / 3,175 symbols**
unfinished, based on the unchanged historical matrix plus the same R3 delta.
Next configuration stays queued, not started:
`configs/planning/cnig_plu_2017_feature_codes.yaml`.

A-001/A-002/A-003 remain OPEN. The original five evidence limitations,
R3-T01..R3-T04, cold-start REPORTED_EXECUTED_PENDING_REVIEW, visual-rendering
acceptance and final full-suite validation stay pending. Last independently
approved functional boundary remains 7F.1B.4; exhaustive independent 7F.1C.1
semantic review remains pending. No semantic mapping, scoring or new feature.

## Byte bindings and actual scoped validation

Unchanged source SHA256:
`01a56b482a3c956d1f8a7069b94c69518758ea3937c3d98ef8ae5d74615d6148`.
Unchanged test SHA256:
`f742a30c7921e83fd28114c7419ba0d4c2ca36aa0aed5d04c8881cad1feaef57`.
Unchanged auditor SHA256:
`5b5aae765c6c32225496d7830e17e83a9bfac89e007949b032b75b13eda3029f`.
Unchanged auditor-test SHA256:
`0c6ce4167f33c56ad09c3ea7cbe8ebeb039cda7ed013c38022a29d5cc98b0665`.

Final companion Git-content SHA256 bindings:

- Source companion: `6014d59a08f557ebeab6672e33d25d917d50db11fab52b9ee5e3b5a452b394a8`.
- Test companion: `73f4f2c6647a3bb643457b698ab063fdc8eb7dd5bda5ecafeb126a4173c58fbf`.

The worktree scoped check completed with exit 0: all **106 protected paths** match
recorded base/main Git blobs, indexed SHA256 and original checkout SHA256. All
**277 starting tracked paths outside the five existing allowed edits** retain
their bytes, including the separately verified historical raw/Git EOL distinctions
for Muret YAML and the old resume ticket. Auditor and auditor tests are unchanged.
Both complete snapshots match exact Git content (77,266/85,646 bytes); their source
headers, all **84/122 unique explicit IDs**, exact qualified headings, displayed
signatures/ranges and 206 owner notes/bindings pass. Strict JSON duplicate-key and
non-finite-constant rejection checks pass. Exactly 14 first notes and one private
mapping differ; all other symbol fields/statuses and original aggregate totals
are unchanged. Checked 200 local links, balanced fences and 48 table rows across
changed Markdown; no visual rendering is implied. New-delta diff whitespace is clean.

The first temporary-check attempt explicitly stopped because its initial scope
comparison counted the two already-recorded raw/Git EOL differences as edits.
The corrected check verifies their exact raw fingerprints separately; it does not
normalize/rewrite those files or silently treat their bytes as Git-identical.
The same scoped check passed against the explicitly staged index before the one
full checker execution recorded below; final receipt-only checks repeat that
bounded preservation/navigation check, not the full auditor.
Temporary read-only script: `C:\souhaib\r31_check.py`, outside Git. No new permanent
test/tool or visual rendering. Initial patch preparation stopped twice on explicit
context/order and duplicate-target checks without edits; corrected targeted patches
then applied. No companion regeneration or protected-file rewrite.

Historical only: R3's unchanged-file run was 183 passed, two warnings, 64.14 s,
native exit 0 including cleanup. **No pytest suite is rerun in R3.1**; no new
application cases, full suite, GPU/EP data operation or redownload is required.

## One full staged INDEX execution

Exactly seven approved paths were explicitly staged. New-delta `git diff --check`
and `git diff --cached --check` exited 0. The unchanged auditor ran **once**:

```text
.venv\Scripts\python.exe -X utf8 tools/audit_documentation.py --check --progress > C:\souhaib\r31-candidate.stdout.txt
```

Completed normally: **native exit 1, completed=true, 10,266 findings**, not timeout,
traceback or operational exit 2. Candidate manifest SHA256:
`57d2a18e4f0adbd3c9f85e88ec1bbcd30f08cb7b617f07d53cb78d2b13cfc3b7`.
284 paths, 281 unique blobs, 29,087,722 per-path content bytes; 94 Python files,
94 AST parses, 4,863 symbols, five Git processes, non-shallow history. Index
postcondition completed. Native command wall time 2.6086573 s includes launcher
and manifest-capture overhead, not an auditor benchmark.

The observed diagnostic breakdown remains partial: 5,033 coverage/staleness,
217 mechanical and 5,016 pending-review/history/semantic-status findings. No count
was forced. Global coverage is still unmerged, so its old missing-anchor and
NOT_READ diagnostics do not consume the four-row owner correction.

Compared with the retained R3 candidate output, the inventory line gains the new
ticket; there are exactly two additional qualified-reference diagnostics, both in
the **unchanged historical R3 receipt**. They describe the same two literal
hash-domain strings already reported against the source companion. That receipt
was extended after R3's full candidate run, as its own boundary states. There are
therefore four occurrences across two documents of those two known hash-domain
false positives in this run. They remain reported, not suppressed: no tool,
exception, history, coverage or source edit to obtain exit 0. No claim that every
mechanical check passes, that the whole audit is complete, or that rendering ran.

Detailed output stays outside Git: `C:\souhaib\r31-candidate.stdout.txt`,
PowerShell UTF-16, 2,315,530 bytes, SHA256
`9c7ccef063cc0ef8dbe0463c9b23a19b5f010b2c0cd7056e0731cc2a7a091a7b`.
The exact sorted path/mode/blob list is
`C:\souhaib\r31-candidate.manifest.json` (PowerShell UTF-16 JSON). Decoding and
compact ASCII-safe JSON serialization without terminal newline reproduces the
candidate manifest digest. No source/data operation accompanied this check.

**Only this receipt changes after that full run** to record its outcomes. Its
later bytes are not retroactively in the checked candidate. Final scoped checks
verify exactly that one-path manifest delta, seven-path total scope, all protected
bytes, links/fences/tables, both companion bindings and the 206 ownership mappings.
The final publication manifest is reported externally after those checks; no
self-hash or own future commit SHA is embedded here. No second full checker run.

Cumulative main-to-candidate whitespace exits 2 with exactly the **same 13 inherited
observations** as main-to-start, byte-identical stdout/stderr: twelve original
cold-start Markdown hard breaks (29,32,39,42,47,50,53,56,59,73,97,102) and original
continuity ticket blank EOF (1036). The new delta is clean; these archives were
neither rewritten nor suppressed.

## Publication boundary and stop

Only these seven paths may be staged/published:

- docs/code/files/src/landscout/stages/enrich_planning_features.py.md
- docs/code/files/tests/unit/test_enrich_planning_features.py.md
- docs/code/audit/reviews/inpn_roads_extension.json
- docs/code/audit/R3_1_PLANNING_FIDELITY.md
- docs/code/audit/DOCUMENTATION_AUDIT.md
- docs/project/CURRENT_STATE.md
- docs/project/tickets/DOCS.CONTINUITY.1.R3.1.txt

Commit message: `docs: correct planning companion evidence and anchors`.
Recovery-only push after gates; resolve final SHA through Git, not a self-reference
inside this receipt. Require clean tree, HEAD/local tracking/actual remote recovery
equality and actual main unchanged, then stop for independent R3.1 review.
