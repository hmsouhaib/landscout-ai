# Current evidenced project state

This file is a state summary, not a live Git oracle or chronological history. Check the actual repository, branch, worktree, local HEAD and remote ref; reconcile differences explicitly rather than resetting or assuming these words are current.

## Publication versus independent approval

Latest implementation publication at bootstrap: `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`, STEP 7F.1C.1, seven documentation-only paths. Its direct parent is `ca0ec73de37137b5515c1dfea14e2ea8a2a1ba3d`. The [French semantic reference](../reference/inpn_ep_2026_07_semantic_reference.md) remains `RESEARCH_DRAFT_NOT_RUNTIME_POLICY`; no production consumer exists.

Last independently approved implemented functional boundary: STEP 7F.1B.4, commit `ca0ec73de37137b5515c1dfea14e2ea8a2a1ba3d`, source-bound EP bundle assembly and complete physical FID alignment. Status: `APPROVED_RECORDED_IN_CONVERSATION`, provenance [bootstrap ticket Appendix A4](tickets/DOCS.CONTINUITY.1.txt). The complete original review receipt is unavailable in the versioned record; do not invent one.

The supplied 7F.1C.1 review inspected publication/parent/seven-file scope, frozen bindings, draft status, summary counts/nulls, field-mapping limits and the documentary-version conflict. It did NOT fully audit all 64 meanings, 42 sources, every JSON line or all MD/JSON equivalences. Independent semantic review remains **PENDING**. Codex's earlier reported checks are not an expanded independent verdict.

## Active ticket and next action

DOCS.CONTINUITY.1 is **IN_PROGRESS**: documentation-content audit and durable continuity bootstrap. [Coverage/progress](../code/audit/DOCUMENTATION_AUDIT.md) is partial; do not publish it as complete. The ticket's known input SHA is the bootstrap publication above. The eventual publication SHA must be resolved through Git after commit, never embedded as its own future SHA here.

Current bounded instruction: [DOCS.CONTINUITY.1.R3.1](tickets/DOCS.CONTINUITY.1.R3.1.txt), from recovery HEAD `aad641420c0b0d2c8c503815854ae9c17f4d09f4` on `recovery/docs-continuity-1-partial`, corrects only the two planning companions and matching four-row owner evidence. Independent read-only review of published R3 found fixture/call-order/scope contradictions and a duplicated private/public anchor: **CORRECTION_REQUIRED for those documentary findings**, not rejection of the whole implementation. The [R3.1 receipt](../code/audit/R3_1_PLANNING_FIDELITY.md) records the correction; independent acceptance is **PENDING**. The unchanged [R3 receipt](../code/audit/R3_PLANNING_FEATURES.md) retains the prior 183-pass/two-warning execution, not an R3.1 rerun. R3's supplied receipt still approves R2.1 within subprocess-test stabilization only; historical [R2](../code/audit/R2_DIAGNOSTICS.md) and [R2.1](../code/audit/R2_1_DIAGNOSTICS.md) evidence stays untouched. R1 remains preservation only. No application approval or A-003 closure follows. Resolve final publication/remote refs through Git; publish recovery only, then stop for independent review. No next batch or main publication is authorized.

Historical recovery report, 2026-09-17 before R1: **PARTIAL — work preserved**, then no commit or push. Its [recovery evidence](../code/audit/RECOVERY_STATUS_2026-09-17.md) remains the original 67/245 files and 1,388/4,769 symbols, with 178 unfinished files. R3 now applies exactly four previously NOT_READ rows: unchanged source/test CHECKED (84/122 symbols), their two companions CORRECTED. Updated [operational owner](../code/audit/reviews/inpn_roads_extension.json) plus the unchanged historical matrix reconcile to **71/245 files and 1,594/4,769 symbols closed; 174 files and 3,175 symbols unfinished**. Global coverage.json is still unmerged. Prior planning-fragment transfer duplicates are not counted twice; no unrelated row is promoted. The next preserved sorted NOT_READ path is `configs/planning/cnig_plu_2017_feature_codes.yaml`, not authorization to begin it.

Cold-start status for independent review: **REPORTED_EXECUTED_PENDING_REVIEW**. Preserve the [twelve-answer execution record](../code/audit/cold_start_resume_2026-09-17.md) and the parent-recorded bounded verification in the recovery report. Neither is an accepted independent verdict. Application findings A-001/A-002/A-003 and the five prior test-evidence limitations remain open; R3 separately records planning test-evidence limits, not repairs. No visual Markdown rendering or fresh full application pytest is claimed; both remain final global-audit acceptance work.

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
