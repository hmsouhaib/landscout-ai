# Current evidenced project state

This file is a state summary, not a live Git oracle or chronological history. Check the actual repository, branch, worktree, local HEAD and remote ref; reconcile differences explicitly rather than resetting or assuming these words are current.

## Publication versus independent approval

Latest implementation publication at bootstrap: `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`, STEP 7F.1C.1, seven documentation-only paths. Its direct parent is `ca0ec73de37137b5515c1dfea14e2ea8a2a1ba3d`. The [French semantic reference](../reference/inpn_ep_2026_07_semantic_reference.md) remains `RESEARCH_DRAFT_NOT_RUNTIME_POLICY`; no production consumer exists.

Last independently approved implemented functional boundary: STEP 7F.1B.4, commit `ca0ec73de37137b5515c1dfea14e2ea8a2a1ba3d`, source-bound EP bundle assembly and complete physical FID alignment. Status: `APPROVED_RECORDED_IN_CONVERSATION`, provenance [bootstrap ticket Appendix A4](tickets/DOCS.CONTINUITY.1.txt). The complete original review receipt is unavailable in the versioned record; do not invent one.

The supplied 7F.1C.1 review inspected publication/parent/seven-file scope, frozen bindings, draft status, summary counts/nulls, field-mapping limits and the documentary-version conflict. It did NOT fully audit all 64 meanings, 42 sources, every JSON line or all MD/JSON equivalences. Independent semantic review remains **PENDING**. Codex's earlier reported checks are not an expanded independent verdict.

## Active ticket and next action

DOCS.CONTINUITY.1 is **IN_PROGRESS**: documentation-content audit and durable continuity bootstrap. [Coverage/progress](../code/audit/DOCUMENTATION_AUDIT.md) is partial; do not publish it as complete. The ticket's known input SHA is the bootstrap publication above. The eventual publication SHA must be resolved through Git after commit, never embedded as its own future SHA here.

Current bounded instruction: [DOCS.CONTINUITY.1.R4](tickets/DOCS.CONTINUITY.1.R4.txt), from recovery HEAD `e89f7f176f7bc3369977055aceb6423b882d3429`, audits only the unchanged CNIG feature-code YAML and its companion, with bounded owner/continuity evidence. The [R4 receipt](../code/audit/R4_CNIG_CONFIGURATION.md) records implementation/checks; independent R4 review is **PENDING**. Publish recovery only, then stop. No next unit or main publication is authorized.

The exact R4 ticket section 1 supplies ChatGPT's independent read-only **APPROVED** verdict for R3.1 at `e89f7f176f7bc3369977055aceb6423b882d3429`, parent `aad641420c0b0d2c8c503815854ae9c17f4d09f4`: planning documentation-fidelity correction only. It checked the seven-path publication/diffs, corrected anchors/owner mapping and amended fixture/call-order/scope notices against source/tests, not a fresh 183-test run, full INDEX execution, all-206 automated mapping audit, visual rendering, A-003 rerun or official GPU/EP operation. The historical R3 **CORRECTION_REQUIRED** verdict remains in [R3.1's archived ticket](tickets/DOCS.CONTINUITY.1.R3.1.txt); the unchanged [R3](../code/audit/R3_PLANNING_FEATURES.md) and [R3.1](../code/audit/R3_1_PLANNING_FIDELITY.md) receipts retain their original execution/review state. This successor approval is not application/global approval and adds no closure count. Historical R2/R2.1 evidence likewise remains unchanged.

Historical recovery report, 2026-09-17 before R1: **PARTIAL — work preserved**, then no commit or push. Its [recovery evidence](../code/audit/RECOVERY_STATUS_2026-09-17.md) retains 67/245 files and 1,388/4,769 symbols. R3 closed four original rows through the [extension](../code/audit/reviews/inpn_roads_extension.json): 71/245 and 1,594/4,769. R4 closes two original NOT_READ rows in their actual [planning owner](../code/audit/reviews/planning.json): unchanged CNIG YAML CHECKED, companion CORRECTED. Both now read_complete=true; no duplicate extension row exists despite the historical transfer intention. Deduplicated closure is **73/245 files and 1,594/4,769 symbols; 172 files / 3,175 symbols unfinished**. YAML/Markdown add zero AST symbols. Global coverage and original matrix remain unchanged/unmerged. Next preserved sorted NOT_READ item is `configs/planning/muret_bess_cnig_feature_policy.yaml`, identified only, not started.

Cold-start status for independent review: **REPORTED_EXECUTED_PENDING_REVIEW**. Preserve the [twelve-answer execution record](../code/audit/cold_start_resume_2026-09-17.md) and the parent-recorded bounded verification in the recovery report. Neither is an accepted independent verdict. Application findings A-001/A-002/A-003 and the five prior test-evidence limitations remain open; R3 separately records planning test-evidence limits, not repairs. R4 preserves these limits and adds A-004 (record-model versus result literal-null-reference validation), reproduced only in memory; no application correction. No visual Markdown rendering or fresh full application pytest is claimed; both remain final global-audit acceptance work.

Forbidden next actions: executable EP mapping/category decisions, geometry normalization/reprojection, parcel environmental analysis, owner/contact work, scoring, CI/PR automation, source/config/application-test behavior changes or redownloads under this documentation ticket.

## Implemented components and missing product outcomes

Cadastre/parcel geometry and shape, RTE/IGN grid proxies/coverage, GPU spatial and written planning, CNIG meaning/policy/application/aggregation/artifact contracts, road proxies/proximity/coverage, shared strict serialization/immutability/HTTPS/recovery, and EP physical evidence exist as library components. See [architecture](../code/ARCHITECTURE.md), [data flow](../code/DATA_FLOW.md) and [file index](../code/FILE_INDEX.md).

An autonomous end-to-end product orchestrator, global score/ranking, owner identification, production delivery/human workflow and environmental executable category policy are not established by those components. Muret remains the pilot, not the product's fixed scope.

## Active questions and evidence

- Exact EP export edition/field/value dictionary, all `statut` NULLs, `Nature`/`nature`, raw delimiter grammar, draft chronology, local/seasonal/composite applicability: [research dossier](../reference/inpn_ep_2026_07_semantic_reference.md).
- `sig_tadl`: declared EPSG:32753 and coordinates near 140/−66 remain unresolved despite matching catalog/observed bounds; no inferred replacement CRS. [Environment evidence](../code/ENVIRONMENT_PIPELINE.md#recorded-factual-result-historical-source-verification-not-rerun-by-this-documentation-audit).
- Missing historical prompts/receipts and deferred CI/PR work: [backlog/gaps](BACKLOG_AND_GAPS.md).
- Exact archive/catalog/attribute/geometry/bundle hashes and recorded toolchain: [source bindings](../reference/inpn_ep_2026_07_semantic_reference.md#2-source-figée-et-chaîne-de-preuve). These are reported frozen-snapshot evidence, not new real-source executions during this audit.

## Reconcile live Git

If HEAD differs, inspect its ancestry and changed paths against the recorded input, then consult the step ledger and exact available review receipts. Distinguish a documentation successor with identical protected source bytes from a changed implementation. Do not infer approval from commit proximity or a DEV_LOG “complete” label. Report missing access or contradictory records before code/ticket action.
