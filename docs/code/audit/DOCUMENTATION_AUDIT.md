# DOCS.CONTINUITY.1 — documentation audit progress

Status: **IN_PROGRESS / PARTIAL**. No completion or independent approval is claimed.

Current bounded continuation: [DOCS.CONTINUITY.1.R9](../../project/tickets/DOCS.CONTINUITY.1.R9.txt), application of compiled BESS/CNIG policy to coded objects/relations, from `05d6ffce1726774be5b956080323e92f43aef825`. [R9 receipt](R9_BESS_CNIG_APPLICATION.md) records source/test and unique-prose reads, 219 qualified semantic notices, source/manifest schemas2/2, seven exports, four distinct trust paths, exact propagation/nulls/metrics, immutable metadata, canonical/raw-byte hashes and test-evidence limits. Section1 of the exact ticket supplies documentary-only R8.1 APPROVED (no R8.2); [CURRENT_STATE](../../project/CURRENT_STATE.md) preserves that successor verdict and limits without rewriting old PENDING receipts. R9 independent review **PENDING**, global audit **PARTIAL**. Four formerly NOT_READ rows in sole [planning owner](reviews/planning.json) close: two protected Python CHECKED and two companions CORRECTED; 109/110 original symbols CHECKED. The historic extension transfer was never materialized; compact prior metadata and exact prior-symbol fingerprint/commit remain. Deduplicated totals **87/245 files and 2,011/4,769 symbols**, remaining **158 files / 2,758 symbols**. File totals CHECKED34/CORRECTED53/READ141/NOT_READ17; symbol totals CHECKED2,010/CORRECTED1/READ2,078/NOT_READ680. Gain4files/219symbols; no credit for declarations/dependencies/new receipts/approval. Original coverage/matrix remain unmerged. R9 allows one focused existing test and one full INDEX candidate; exact execution/results/final receipt delta are in its receipt, not invented from R8.1's10,267 findings. Source/tests/configs/snapshots/old history unchanged. A-001..A-004, five historical limits, R3-T01..04, OPEN R5-D01, cold-start/render/global final acceptance and exhaustive7F.1C.1 semantic review remain open/pending. R9-T01..04 are bounded test-proof reservations, not production fixes/new findings. Stop after recovery-only publication for independent review; no next lot begins. All execution reports below retain their historical scope.

Current checkpoint authority: [DOCS.CONTINUITY.1.R1](../../project/tickets/DOCS.CONTINUITY.1.R1.txt). The [appended R1 record](RECOVERY_STATUS_2026-09-17.md#r1-recovery-checkpoint-preparation) preserves this partial state on a dedicated recovery branch only. Earlier no-stage/no-push statements below describe their historical execution, not the later explicit recovery authorization. No semantic status or original fragment is promoted by R1.

Starting identity was fetched and checked on clean `main` at `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`. The original Git inventory has 245 files. The [coverage ledger](coverage.json) begins with every file and qualified Python symbol explicitly `NOT_READ`; AST enumeration is not semantic review. The [protected-file manifest](protected_files.json) records exact Git-content and starting-checkout SHA256 separately.

## Recovery checkpoint

Read this report, coverage and the six `reviews/` fragments, then inspect `git status --short` and the diff before resuming. Preserve unfinished edits. Do not reset, stash, clean or publish a partial audit as complete. Root owns global tooling, history/continuity documents, exports, dependencies, remaining cross-cutting documents and final DEV_LOG synchronization. Domain reviewers own only their allocated companions and pipeline prose.

The [2026-09-17 recovery report](RECOVERY_STATUS_2026-09-17.md) supersedes stale aggregate progress statements, without rewriting original evidence. Its [245-path reconciliation](recovery_file_matrix_2026-09-17.json) records 24 CHECKED, 43 CORRECTED, 141 READ and 37 NOT_READ files; 1,388/4,769 symbols have closure labels. `coverage.json` is still the unmerged initial inventory, not a completed audit. The fresh 23-case checker run and static gates passed; full pytest and final audit acceptance remain pending. No work was staged or published.

## Active work allocation

- `reviews/foundations.json`: configuration/common serialization/HTTP/immutability, cadastre, geometry, grid, shape and related tests/configs/companions.
- `reviews/planning.json`: GPU, common planning/artifact contracts, spatial/written planning, CNIG, policy/application/aggregation and related tests/configs/companions.
- `reviews/inpn_roads.json`: five INPN evidence components, road normalization/policy/proximity/coverage and related tests/configs/companions.
- Root: all remaining original tracked files, durable project history/rules, checker/self-tests and final cross-domain verification.

Required read method (not a claim that all reads are finished): read every source/test completely and every unique companion explanation/table/interface in its symbol context. Exact repeated source snapshots may be byte-compared to source content already fully read. Repeated generic explanatory paragraphs/import blocks may be displayed once with occurrence locations recorded; per-symbol purposes, guards, caller and side-effect rows still require contextual checking. This duplicate-content method does not treat a matching hash or snapshot as proof of explanation accuracy.

## Not yet completed

Global semantic coverage, portable-binding migration, final checker integration, final cold-start acceptance, full-suite finalization, final findings/provenance/state reports and publication are pending. An interim fresh-context exercise has now been executed and separately checked within a bounded scope; see the dated recovery report. Existing EP research remains `RESEARCH_DRAFT_NOT_RUNTIME_POLICY`; no functional progression is authorized. No existing production/config/test behavior may be changed in this audit.

## Actual interim executions

The new `tools/audit_documentation.py` is an offline standard-library checker of the Git-index candidate. It is not yet integrated with the final coverage records. Its new synthetic suite currently has 23 passing cases (`uv run pytest -q tests/unit/test_audit_documentation.py --basetemp C:\Users\souha\AppData\Local\LandScout\pytest-runs\da5714`), process exit 0 including cleanup, 8.93 seconds. Ruff check and mypy pass for the new tool (Ruff also checks its test). The preceding 17-case run passed in 5.85 seconds; an earlier collection attempt failed with exit 1 because the new test's tool path went one directory too high, then that new-test path was corrected. No existing assertion or fixture was modified. The complete repository has **not** been run during this audit yet.

Ruff formatted only the new tool and new tests. The initial sandboxed uv invocation could not read the user uv cache; the same installed environment succeeded with an authorized escalation. No environment/dependency/security setting was changed.

## Open application findings, no production fix

The foundations review has reproduced two in-memory findings and records exact symbols/commands/limits in [its fragment](reviews/foundations.json): `A-001`, canonical Cadastre validation admits an XYM polygon despite its exactly-2D contract; `A-002`, malformed RTE geometry `type` list/dict values leak `TypeError`. These are respectively a contract-integrity gap and a controlled-error gap, not new end-to-end source acquisitions or a demonstrated network bypass. No production correction is authorized by this documentation ticket. See the [classified backlog](../../project/BACKLOG_AND_GAPS.md#application-findings).

Recovery reproduced `A-003`: a synthetic physical GPU feature label with surrounding whitespace is preserved by the public builder but rejected by its public result validator. The [dated recovery report](RECOVERY_STATUS_2026-09-17.md#application-findings) retains the exact command, output and limits. This is a separate contract-consistency finding, not permission to strip raw source text or repair production here.

## Completed bounded subreviews

The original INPN/roads allocation has all 46 files freshly read and 1,387 symbols checked: 22 file rows CHECKED, 24 CORRECTED, eleven corrected documentation findings and five explicit test-evidence limitations. This does not close the whole-repository audit. Foundations/planning/root progress remains in the per-owner fragments; global coverage will only be merged to COMPLETE after all allocations and final checks close.

Root has read all 802 lockfile lines, verified all 1,591 passive TOML leaf values/types/order against its companion and verified exact Git snapshot equality (48 packages). All 99 DEV_LOG narratives and 101 publication records have been reviewed. The 1,749-line historical EP domain dump is preserved mechanically, not reinterpreted or reprofiled as a fresh source run. The complete historical snapshot matches 600,865 Git bytes. The recovery and publication commits for 7F.1B.1.2 resolve to the same tree `602363f11ab63b6e0f031e3332aed33d3f735dda`.

The [semantic-pair continuity review](reviews/semantic_reference.json) records complete Markdown reading and exhaustive internal profile/key/frequency/source-reference checks: 45 profiles, 64 entries, 960 layer frequencies, 42 source records and 7,584 JSON leaves. Of 1,223 section-local narrative-string comparisons, 1,221 match literally; the two remaining cases are an excluded heading and an explicit equivalent documentary-only qualification. No pair bytes, external-source research status or runtime semantics changed. This check does not close the pending full independent source/semantic review of STEP 7F.1C.1.

## Rendering discovery, not a visual pass

No Markdown document has yet been visually rendered in this audit. `pandoc`, `markdown`, `marked` and standalone `node` were not available on PATH; the installed Python environment lacks markdown/markdown-it/mistune/docutils. A versioned VS Code installation and bundled Markdown extension were found; there is no standalone renderer entry among the inspected paths, and native-app UI control is unavailable in this session. No extension, dependency or security setting was installed/changed, and no repository content was sent to a public renderer. Static fence/link/table review is not visual rendering. This remains an explicit acceptance limitation unless a usable local preview is actually exercised later.
