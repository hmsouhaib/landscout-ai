# LandScout — repository entry point

Read this file explicitly; do not assume a client loaded it automatically.

## Roles and authority

- Souhaib is product decision-maker.
- ChatGPT reviewer/architect: read-only review and ticket authoring; no Git writes.
- Codex implementer: scoped edits, validation and authorized commit/push.
- Codex cannot grant independent approval to its own work.

## Mandatory entry route

1. Inspect live repository identity, branch, HEAD, remote ref and worktree.
2. Read [working rules](docs/project/WORKING_RULES.md).
3. Read [current state](docs/project/CURRENT_STATE.md).
4. Read [step index](docs/project/STEP_INDEX.md), relevant
   [decisions](docs/project/DECISIONS.md) and [backlog/gaps](docs/project/BACKLOG_AND_GAPS.md).
5. Return the context receipt in [RESUME](docs/project/RESUME.md) before acting.
6. Load relevant [technical documentation](docs/code/README.md), source and tests.
7. For unfinished work, read the [audit ledger](docs/code/audit/DOCUMENTATION_AUDIT.md)
   and inspect the diff before applying any original clean-tree prerequisite.

## Non-negotiable boundaries

One explicitly authorized Codex ticket at a time. Independent review precedes
the next functional increment. Publication, test execution and review approval
are distinct evidence. Preserve unavailable history as a gap, not invented memory.

Preserve user changes and recovery material. No automatic reset, restore, stash,
clean, rebase, amend, merge, force-push or security-setting change.

Keep facts, proxies, preliminary policy evidence and eventual human decisions
separate. Unknown remains unknown. No inferred legal/heavy-truck road access,
grid capacity, BESS authorization or owner/contact facts.

Current continuity bootstrap is documentation/tooling only. EP semantic research
remains a draft with independent semantic review pending; no executable mapping.

Follow the active ticket's exact tests and scope. For Windows pytest use a fresh
short unique basetemp under `%LOCALAPPDATA%\LandScout\pytest-runs`; full process
exit status, including cleanup, is evidence. Do not redownload snapshots for docs.

Update affected companions, state, step/decision/gap records and local audit
evidence. Archive supplied tickets/review receipts with provenance. Stage only
explicit reviewed paths, and leave independent review pending until received.

This entry point is navigation, not a substitute for source, user-approved intent,
the active ticket, or a scoped independent review. See [provenance](docs/project/CONTEXT_PROVENANCE.md).
