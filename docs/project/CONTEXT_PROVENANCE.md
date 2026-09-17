# Context provenance and evidence classes

## Bootstrap authority

The user supplied [DOCS.CONTINUITY.1](tickets/DOCS.CONTINUITY.1.txt) in the active conversation. The archived UTF-8 bytes are exact, including its terminal newlines: SHA256 `ce2d79126feb5ac13075116217b0559241ec5b82499e6ceecb25ea034cdd42cb`, 38,843 bytes. Appendix A is explicitly a **selected conversation summary**, not a transcript, account-memory export or independently reconstructed history. No inaccessible conversation has been invented.

The archive supplies the collaboration roles, product boundaries, deferred CI decision, selected implementation decisions, exact latest-review scope and historic environment observations. Its commit anchors are checked against local Git history. Git supplies publication and ancestry, not approval. The [step ledger](STEP_LEDGER.json) preserves missing original prompts and receipts as unavailable rather than presenting commit summaries as their exact text.

The exact [2026-09-17 resume instruction](tickets/DOCS.CONTINUITY.1.RESUME.2026-09-17.txt) is also retained: 7,040 UTF-8 bytes, SHA256 `9e18c25d571c5cfe34391d1f35833634bb4c3672087781360752fa0fba7243ed`, including its original CRLF line endings. It preserves the original ticket's authority and explicitly requires a PARTIAL/no-publication handoff if semantic coverage is unfinished. The [recovery report](../code/audit/RECOVERY_STATUS_2026-09-17.md) records newly executed checks separately from historical results; it is not a completion or approval receipt.

## Evidence classification

| Class | What it establishes | What it does not establish |
|---|---|---|
| `GIT_PUBLICATION` | Exact reachable commit bytes, parentage and paths | Independent approval or a successful historical execution |
| `REPORTED_EXECUTION` | A retained Codex/DEV_LOG report of a command or observation | That this audit reran it, or that all business contracts hold |
| `AUDIT_EXECUTION` | Command, environment, actual result and scope recorded during this ticket | More than the exercised assertions/operations |
| `USER_DECISION` | Explicit direction in the supplied ticket/seed | An unrecorded rationale, date or rejected alternative |
| `APPROVED_RECORDED_IN_CONVERSATION` | The exact review boundary summarized in Appendix A4 | A verbatim original receipt or retroactive approval of every intermediate commit |
| `PARTIAL_REVIEW_RECORDED_IN_CONVERSATION` | Only the listed 7F.1C.1 inspection scope | Global semantic approval of all entries/sources/MD–JSON equivalence |
| `PROPOSAL` / `DEFERRED` | An explicitly classified possible or postponed action | Authorization to implement it |
| `SUPERSEDED` | A preserved earlier instruction corrected by later evidence | The current governing instruction |
| `UNAVAILABLE` | A disclosed evidence gap | A fact to reconstruct through plausible guesses |

## Known review boundary

STEP 7F.1B.4 at `ca0ec73de37137b5515c1dfea14e2ea8a2a1ba3d` is the last independently approved functional boundary **as recorded in Appendix A4**: EP bundle assembly and full physical FID alignment. The original complete review receipt is not retained in this repository.

STEP 7F.1C.1 at `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02` is a published research draft. The supplied reviewer summary covers publication/parent/seven-file documentation scope, frozen bindings, draft status, summaries, mapping limitations and documentary-version conflict. It expressly excludes a complete review of all 64 entries, 42 sources and every JSON/Markdown equivalence. Its independent semantic review remains pending. This audit may check inventory/link/serialization mechanics without enlarging that verdict.

Codex reviewers working on this documentation audit are implementation collaborators, not the independent ChatGPT reviewer. Their file/symbol findings and any cold-start exercise have their own executor/context records. Codex cannot grant itself independent approval.

## Runtime and source evidence

Appendix A6/A7 and the historical DEV_LOG retain the pinned EP hashes, `sig_tadl` observation and prior native/toolchain runs. This ticket does not redownload or reprofile the real snapshot. Newly executed native import/version checks belong in the audit execution record; old real-source results remain reported history even if executable bytes are unchanged.

The [protected manifest](../code/audit/protected_files.json) separately records Git blob IDs, SHA256 of Git content and initial checkout bytes. The one known CRLF-only configuration representation is not rewritten. Matching bytes support continuity of implementation, not semantic correctness of its documentation.

## Maintenance and privacy

Archive an exact future supplied ticket or review receipt once, reference its path/hash and scope from the ledger, and preserve reversals. Do not make a read-only reviewer secretly write to Git. Do not insert hidden reasoning, secrets, private unrelated biography or fabricated chat exports. A missing date, reviewed SHA or rationale stays null/unavailable until evidence arrives.
