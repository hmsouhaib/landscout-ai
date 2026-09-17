# DOCS.CONTINUITY.1.R2 — auditor diagnostics and scoped receipt

Status: tool correction implemented; candidate execution/publication gates below;
independent review **PENDING**, global semantic audit **PARTIAL**. This is not final
DOCS.CONTINUITY.1 closure, a visual audit, or a new functional step.

## Authority and supplied review provenance

The [exact R2 ticket](../../project/tickets/DOCS.CONTINUITY.1.R2.txt) is the supplied
authority and contains the scoped independent review receipt in section 1.
Attachment identifier: `dcfc38bc-0987-4174-b788-0564cc424a40/pasted-text.txt`.
Raw attachment/archive SHA256:
`61d04a721ba6a48b94937cd6da60b879e0a1c75a5dee43bb62d396f11d140d31`.
No separate signed/full review message was supplied or invented.

That receipt accepts R1 only as preservation/publication. Its Linux/Python 3.13.5/
Git 2.47.3 synthetic inspection applies to tool blob
`71799192aa840ba3ce07bac27ed65fb323511bdb`, raw SHA256
`8eca12abc2b9a93faab1c33ab21deddd2fe01b58ac1eba50778ad5b83236510f`.
It does not approve the R2 implementation or the unfinished global documentation.

## Readiness, scope and preservation

Starting recovery HEAD and local/actual remote recovery:
`a413ee01072ed1c0ba2c4efb32a0f4c978c63aff` on
`recovery/docs-continuity-1-partial`. Local/actual remote main:
`aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`. Clean worktree, no unmerged entries or
Git-operation markers. Normal network query failed at GitHub connection; native
explicit-root query reproduced the exact R1 ownership mismatch. Only then the
ticket-authorized command-scoped `-c safe.directory=C:/souhaib/landscout-ai`
prefix established actual remote refs. No persistent trust/config/security change.
The auditor itself runs in the repository-owning normal context, without that
exception and without network; the outer Git prefix is not inherited by Python.

The complete 106-path original protected manifest passed base Git / index /
recorded initial raw-checkout SHA comparisons. All 270 unchanged R1 paths outside
the R2 allowlist passed raw-checkout comparisons. Original fragments, initial
coverage, matrix, recovery reports, cold-start answers and research pair remain
untouched. The two retained raw/index EOL representations are the original Muret
zoning YAML and prior resume ticket; neither was rewritten. Original coverage
SHA256 remains `5ae2a994effb59947b0dbe4af97b777bc17fb13998a8ba5b8110f2c42052036c`.

Exact eight-path allowlist:

- `tools/audit_documentation.py`
- `tests/unit/test_audit_documentation.py`
- `docs/code/files/tools/audit_documentation.py.md`
- `docs/code/files/tests/unit/test_audit_documentation.py.md`
- `docs/code/audit/R2_DIAGNOSTICS.md`
- `docs/code/audit/DOCUMENTATION_AUDIT.md`
- `docs/project/CURRENT_STATE.md`
- `docs/project/tickets/DOCS.CONTINUITY.1.R2.txt`

## First instrumented diagnostic, before correction

One current-phase probe was added before optimization. The index remained the
276-file R1 candidate: 29,129,416 per-path content bytes; manifest
`97bb469f415448c1f269f6d0ae2e7c9a1138e4f019f5a6ba24affca65e72418b` under the R2
sorted `(path, mode, blob-ID)` compact-JSON manifest definition. Only the executing
worktree tool had temporary flushed phase probes. No candidate scope was narrowed.

Diagnostic command: `.venv\Scripts\python.exe -u -X utf8 -c` with runpy executing
the tool as `__main__ --check`, cProfile enabled, stdout/stderr redirected to
`C:\souhaib\r2-before.stdout.txt` / `C:\souhaib\r2-before.stderr.txt`, and
`faulthandler.dump_traceback_later(30, repeat=True)` writing to the latter.
Logs stay outside Git. No finished cProfile report is claimed.

Observed phase deltas from flushed perf_counter timestamps:

| Phase | Observed seconds / scope |
|---|---|
| Index enumeration plus per-file reads | 7.506; 277 successful Git processes (ls-files + 276 show), history not reached |
| Coverage loading before Python | 0.012 |
| Python namespaces | 4.175; 94 file progress records |
| Checkout / Markdown | 1.416 |
| Coverage rows | 3.107; all 245 original rows visited |
| References | First stalled document reached after 0.104; no completion |

The 30-second stack dump locates the running loop in `resolves_reference`, called
from the reference scan of the apply-BESS-policy companion. A bounded standalone
inspection identified the growing rewrite: module prefix
`landscout.stages.apply_bess_planning_feature_policy` maps to the same prefix plus
`.apply_bess_planning_feature_policy`, while trying to resolve the documented
manifest's dynamic `model_validate` member. Every whole string differs, so the old
whole-reference cycle set never terminates. The new per-alias-prefix set does.

The diagnostic was deliberately stopped after capturing this evidence; native
process exit 1, not a completed audit. Ctrl-C did not end the redirected worker;
identity-scoped native process inspection found launcher 7356 / worker 1628, but
native Stop-Process failed. Owner-context termination succeeded; subsequent process
checks found neither remaining. No child Git was active in the sampled Python loop.
This reproduces a current stall, not proof of the exact cause of R1's historical
630.254-second interruption. Per-file Git/AST work was additional cost, not the
observed infinite loop. Old AST call sites reparsed namespace and covered-file
inventories/exports; no measured old AST-call counter is claimed.

## Correction and permanent scope

Five read-only Git subprocesses per complete stable-index audit, independent of
file count: stage enumeration, raw blob batch, local history, shallow-history
query, final index equality. Finite default 30-second child timeout; errors carry
phase/role and bounded redacted stderr; timeout/cancellation kills and reaps the
child. No lazy fetch, shell, filters or production imports. Batch framing is by
declared byte length, never content lines; unsupported/conflicted index entries
fail closed. The manifest binds captured object IDs; later index changes abort.

One AST/inventory per indexed Python file is reused for namespaces and exports.
The annotation extraction/signature contract is unchanged, including tested
Unicode and LF/CRLF ranges. No persistent cache or offset-algorithm rewrite.
Phase starts/file progress flush on stderr; metrics remain outside fingerprints.

Strict consumed JSON shapes, duplicate keys and non-finite values fail with
contextual exit 2. Missing required ledgers also mean incomplete exit 2. Missing
history is unfinished, never CHECKED. Approved/partial review records require
exact strings, known local commit and canonical indexed receipt file/Markdown
anchor; structural provenance is not independent semantic approval. Heading
collision sequence a/a/a-1 now yields a/a-1/a-1-1. The Markdown subset is not full
GFM or a visual renderer. Alias expansion cycles report unresolved references.

## Focused tests and quality commands actually run

Initial sandbox formatting/test command failed before collection because uv could
not open its existing cache `.git`; no environment alteration. Native retries used
explicit repository location and fresh short bases. First native focused run:
112 passed in 32.28 s; expanded intermediate run 126 passed in 36.79 s; both exit 0
including cleanup, no warnings/skips/xfails reported.
First Ruff check found two import-order/style findings; corrected, not suppressed.

Final focused command:

```text
uv run pytest -q tests/unit/test_audit_documentation.py --basetemp C:\Users\souha\AppData\Local\LandScout\pytest-runs\r2d168
```

**131 passed in 36.01 s; native exit 0 including cleanup; zero reported warnings,
skips or xfails.** All 23 historical cases remain, with the read-only assertion
strengthened to compare the full before/after file set. 108 additional cases cover
review provenance, history, JSON, process errors/redaction/reaping/progress, bounded
Git cost, exact bytes, conflicts/modes, index drift, AST reuse, growing aliases,
heading collisions and read-only refs/config. The tool-specific inventory is
35 symbols; test-specific inventory 50 symbols, including nested helpers. These
are not additions to the original semantic closure totals.

All following commands succeeded with native exit 0, stopping the command sequence
on any failure:

```text
uv run ruff check tools/audit_documentation.py tests/unit/test_audit_documentation.py
uv run ruff format --check tools/audit_documentation.py tests/unit/test_audit_documentation.py
uv run mypy tools/audit_documentation.py
uv run mypy src
uv lock --check
uv pip check
uv run python -m compileall -q tools tests/unit/test_audit_documentation.py
```

Ruff: all checks passed, two files formatted. mypy: one tool / 52 source files.
Lock: 48 packages. Installed dependency check: 45 compatible packages.
No full application pytest or EP operation; 3,939 remains a prior reported
baseline, not a newly executed full-suite result.

## Full index candidate check

The full explicitly staged candidate completed operationally: **native exit 1**,
ordinary findings, not an interruption or exit 2. Exact command in the owner
context, with PowerShell stdout redirection:

```text
.venv\Scripts\python.exe -X utf8 tools/audit_documentation.py --check --progress > C:\souhaib\r2-candidate.stdout.txt
```

Root `C:\souhaib\landscout-ai`; basis `SHA256_OF_EXACT_GIT_CONTENT_BYTES`.
Captured manifest SHA256:
`07659c10e9bfd947e20d02c39d0dbf7605e2e41a09572424d3b69c9ead5a969a`.
278 indexed files / 275 distinct blobs / 29,254,124 per-path content bytes;
94 Python files / **94 AST parses** / 4,854 enumerated symbols (the original 4,769
plus 85 tool/test symbols, not semantic closure). Five Git processes; non-shallow
local history; final stage enumeration identical; `completed=true`.
Native command tool wall time 2.0487741 s; this includes launcher/output overhead.
The earlier probe had cProfile enabled, so these observations are not a controlled
benchmark ratio. Observed complete-run phase seconds:

| Phase | Seconds |
|---|---:|
| index | 0.194617 |
| coverage-input | 0.010944 |
| python | 0.797795 |
| checkout-markdown | 0.272122 |
| coverage | 0.113803 |
| references | 0.123766 |
| history | 0.071924 |
| index-postcondition | 0.026853 |

**10,266 sorted unique findings**, categorized without promoting any record:

| Category / diagnostic | Count |
|---|---:|
| Coverage/staleness: inventory mismatch | 1 |
| Coverage/staleness: stale file fingerprint | 108 |
| Coverage/staleness: missing companion exception | 131 |
| Coverage/staleness: export inventory mismatch | 24 |
| Coverage/staleness: missing recorded documented anchor | 4,769 |
| Mechanical: ambiguous companion line-ending basis | 104 |
| Mechanical: bad local link | 3 |
| Mechanical: DEV_LOG companion fence errors | 2 |
| Mechanical: missing exact source snapshot | 9 |
| Mechanical: stale companion hash | 1 |
| Mechanical: unresolved qualified reference | 97 |
| Mechanical: undeclared checkout EOL difference | 1 |
| Pending recorded acceptance: semantic ledger not COMPLETE | 1 |
| Pending recorded acceptance: unresolved file review | 245 |
| Pending recorded acceptance: unresolved symbol review | 4,769 |
| Pending recorded acceptance: unfinished history audit | 1 |

Group totals: coverage/staleness 5,033; mechanical 217; pending recorded acceptance
5,016. The initial global ledger remains unmerged NOT_READ; missing symbol anchors
are absent evidence in that ledger, not a claim that every companion has no anchor.
The one checkout difference is the previously preserved CRLF resume ticket, which
the initial coverage does not declare. No new exception was invented to hide it.
Accessible review provenance is structural only; independent acceptance stays
pending irrespective of these counts.

Detailed sorted stdout stays outside Git: `C:\souhaib\r2-candidate.stdout.txt`,
2,314,936 bytes (PowerShell UTF-16 representation), SHA256
`bd39fdbc46cb41bfa8432752644c6301749800f4fc98109c51a6d09d90686518`.
The exact captured path/mode/ID list is retained outside Git at
`C:\souhaib\r2-candidate.manifest.json`; decode its PowerShell UTF-16 wrapper,
serialize compact ASCII-safe JSON without terminal newline, and SHA256 reproduces
the manifest above. No huge second ledger is committed.

The checked candidate contained this receipt's **pre-result preparation version**.
Only this receipt changes afterward to append actual outcomes, then is explicitly
restaged. Its later bytes are not claimed to have been included in the preceding
full run. Subsequent scoped checks verify this changed receipt's links/fences and
the final index allowlist/protected bytes. No self hash or future commit SHA.

Both changed companions have exact indexed source SHA, git-content basis, full
source snapshots and anchors for all 35/50 symbols; their local links pass.
Tool SHA256 `5b5aae765c6c32225496d7830e17e83a9bfac89e007949b032b75b13eda3029f`;
test SHA256 `1a77c16a8b357ac6481682a649a9af0729d3eb54f66d9827967757d381c9fe29`.

## Whitespace and publication boundary

`git diff --check` and `git diff --cached --check` for the **new R2 delta** both
returned native exit 0. Cumulative `git diff --cached --check aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`
returned native exit 2 with exactly the inherited 13 findings: twelve original
cold-start Markdown hard breaks and the original ticket's final blank line.
No archival byte rewrite, whitespace suppression or hook bypass.

The authorized WIP message is `wip: make continuity auditor diagnostic and reliable`;
only the recovery branch may be pushed. Final commit SHA, remote equality and
unchanged actual main are verified after publication in the user-facing report,
not invented here. The scoped tool implementation is ready for independent review;
the global audit is not complete.

## Preserved acceptance boundaries

Original closure remains **67/245 files and 1,388/4,769 symbols**, leaving 178 files
and 3,381 symbols open. No global coverage regeneration, fragment merge or status
promotion. A-001/A-002/A-003 and five test-evidence limitations remain open.
Cold start remains **REPORTED_EXECUTED_PENDING_REVIEW**; no repeat exercise or
visual audit. Last approved functional boundary remains 7F.1B.4; 7F.1C.1 remains
a research draft pending exhaustive independent semantic review.

The first deferred semantic item remains the two enrich_planning_features
companions against unchanged source/tests. R2 does not review or close them.
After the authorized recovery-branch publication, stop for independent review;
no main push, PR, merge, next feature or final DOCS.CONTINUITY.1 DEV_LOG entry.
