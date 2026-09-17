# Working rules and collaboration authority

Authority: user-supplied [DOCS.CONTINUITY.1](tickets/DOCS.CONTINUITY.1.txt), especially Appendix A1–A3 and sections 1–3, 10–12. The appendix is a selected conversation summary, not a complete transcript. These rules preserve user decisions; they are not a new independent code approval.

## Permanent collaboration rules

Souhaib owns product decisions. ChatGPT acts as read-only architect, technical/product reviewer and ticket author. Codex performs authorized local implementation, validation and publication. A Codex completion report cannot stand in for the reviewer's verdict. The reviewer need not secretly write to the repository: Codex may archive an exact supplied receipt during the next authorized update.

One Codex ticket at a time: explicit objective, repository/branch, starting SHA, bounded changes, non-goals, readiness/done criteria and validation commands. Keep functional increments small; consolidated correction tickets are possible when justified. Do not infer authority for a next functional step from a previous completion. Independent review comes first.

LandScout is BESS-first land origination and preliminary analysis, with Muret (31395) as pilot rather than permanent geography. `SCAN -> FILTER -> ANALYZE -> SCORE -> IDENTIFY -> EXPORT -> HUMAN` is the intended product sequence, not a claim of complete orchestration or a permanent overnight schedule.

## Evidence and reporting

Distinguish implemented bytes, published commits, historic Codex/DEV_LOG reports, commands actually rerun now, exact independent-review scope, user decisions, proposals, superseded instructions and unavailable history. A commit proves publication; a test proves only exercised assertions; a source SHA proves byte identity, not prose accuracy or business soundness.

Current source/tests describe observed behavior. User-approved intent and exact source contracts remain normative inputs: record a mismatch as a finding, rather than rewriting the intended rule to legitimize a defect. Never invent full prompts, reviewed SHAs, dates, rejected alternatives or rationale.

Prefer official/open evidence. Preserve unknowns and original attribute TEXT. Distinguish acquisition, normalization, physical/spatial facts, proxies, policy/precheck, diagnostics, later scoring and human decisions. In particular:

- Road evidence does not prove legal, heavy-truck or construction access.
- Grid proximity does not prove an RTE connection point, capacity, cost or feasibility.
- Planning prechecks are not permits; ICPE applicability cannot be assumed, and ICPE-only evidence is not an unconditional UP/AUp prerequisite.
- Hashes, inventories and FID alignment do not prove environmental meaning or correct georeferencing.
- EP, Natura 2000 and ZNIEFF remain distinct sources. No fabricated owner/contact data.

## Safe work and interruption recovery

Check live state before work. If readiness fails, preserve and report it. Never erase local changes to make a clean-tree precondition true. No automatic reset/restore/stash/clean/rebase/amend/merge/force-push or deletion of recovery history. Explicitly scoped future recovery instructions may authorize a different operation; routine work does not.

During long work, maintain file-level progress and findings. On resumption read the current diff and ledger first. Unfinished work is neither complete nor independently approved. Request a recovery instruction if a checkpoint needs publication; do not silently push partial work on main.

Keep the existing Windows/native environment. The user reported past Smart App Control and pytest-cleanup problems, but those do not prove a current block. Do not change security settings, reinstall dependencies, assume a corporate PC or request corporate IT on that basis. Run native checks normally. Every pytest invocation uses a fresh SHORT unique directory under `%LOCALAPPDATA%\LandScout\pytest-runs`; report the final native exit code including cleanup. No broad temp deletion.

Do not redownload large verified sources merely for documentation or unit-level changes. Byte-verified caches should remain offline; recovery material is preserved. Distinguish offline source access from separately authorized online documentation/Git access.

## Maintenance after every ticket

Update affected companions and impact maps, current state, backlog, step ledger and decisions. Retain exact supplied tickets/review receipts once, link their provenance, and preserve reversals. Record actual commands/results/limitations. Run local documentation checks in addition to ticket-specific gates. Finalize DEV_LOG after other evidence, then its source-bound companion last.

Stage explicit reviewed paths only. Publish only when the authorized checks succeed and open items are classified truthfully. A failed production suite prevents publication. Verify clean tree and HEAD == origin/main after the authorized push.

Approval attaches to a commit and scope. A documentation-only successor may preserve previously approved code through exact source-tree evidence; its new prose is not thereby independently approved.

## Ticket-specific restrictions, not universal product bans

DOCS.CONTINUITY.1 permits documentation, continuity records, a narrow local offline checker and new checker tests. It forbids production/config/dependency changes, existing-test weakening, source redownloads and functional environmental work. Those scope limits belong to this ticket; future changes require explicit authorization and review.

CI/PR/pipeline implementation is deferred by user decision, not implemented by the local checker. The EP semantic mapping is not authorized. See [current state](CURRENT_STATE.md) and [backlog](BACKLOG_AND_GAPS.md).
