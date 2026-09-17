# Repository-only cold-start comprehension exercise

Current review status: **REPORTED_EXECUTED_PENDING_REVIEW**, as required by [R1](tickets/DOCS.CONTINUITY.1.R1.txt). The preserved 2026-09-17 execution record reports **EXECUTED_INTERIM_FRESH_CONTEXT**; it is not replaced with NOT_EXECUTED. Documentation audit completion and cold-start acceptance are separate. The exercise ran against unfinished entry records; it must not be reported as completed acceptance. No same-context claim of forgetting is used.

## Exact exercise prompt

> You are a fresh read-only LandScout comprehension reviewer. Repository: `C:\souhaib\landscout-ai`. Start only from `AGENTS.md`, then use repository documents and read-only Git queries. Do not use prior conversation, account memory, external audit scripts, network source data or application caches. Do not edit files, commit, push, run source acquisitions or propose the next functional ticket. Follow the mandatory reading route and return the required context receipt. Answer the questions in `docs/project/COLD_START_EXERCISE.md`, citing repository file/section references and distinguishing publication, reported execution and independent review. Disclose every inaccessible source or unresolved contradiction. Do not infer approval from a “complete” log entry.

## Questions

1. What is LandScout's final purpose, and why is Muret not the permanent scope?
2. What is implemented versus explicitly absent?
3. What is live HEAD, the last independently approved step, and current pending work?
4. Who may modify/push the repository, and how are tickets sequenced?
5. How do source bytes become trusted results; where are hashes insufficient alone?
6. Why are EP geometry rows read with SQLite rather than Pyogrio?
7. What does FID alignment prove, and what does it not prove?
8. Why is `sig_tadl` unresolved despite matching catalog/observed bounds?
9. Why does the STEP 7F.1C.1 draft not authorize executable category rules?
10. Which functions, APIs, configurations and tests would be affected by an INPN acquisition or alignment change?
11. What exact local validation routine and short basetemp convention applies?
12. What must be preserved after an interrupted session, and what work is deferred?

## Execution record to complete, never prefill as success

Record the executor/task identity, genuinely fresh context configuration, exact prompt supplied, allowed access, actual HEAD/worktree, full answers and citations. If no fresh context can actually be created, record `NOT_EXECUTED_FRESH_CONTEXT` and leave acceptance pending for independent review.

A separate verifier must compare each answer with current source/tests and provenance, not merely another summary. Record its identity/context, checked paths/symbols, omissions, ambiguities, contradictions, corrections and residual limits. Neither participant may modify production or authorize a next feature. A successful Codex exercise is not ChatGPT's independent approval of this ticket or of the EP semantic draft.

## Current result

Executor: `/root/continuity_cold_start`, spawned with `fork_turns="none"`; no previous conversation supplied. [Full prompt, twelve answers, citations, access list and limits](../code/audit/cold_start_resume_2026-09-17.md) are archived unchanged. The parent authorized that sole archival write after the read-only exercise.

Separate verifier: `/root/resume_checker_review`, a different task also spawned with `fork_turns="none"`. [Bounded source/test and provenance verification](../code/audit/RECOVERY_STATUS_2026-09-17.md#cold-start-and-separate-verification) found no substantive contradiction in the core INPN trust/reader claims. It confirmed one broken current-state anchor, corrected during recovery. It did not audit every domain implementation, historical record or external semantic source.

Acceptance: **PENDING**. Neither the exercise nor its bounded verification is final global acceptance or independent ChatGPT approval. Do not replace these statuses with old source-suite or documentation-checker results.
