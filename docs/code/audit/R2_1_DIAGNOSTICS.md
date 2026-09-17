# DOCS.CONTINUITY.1.R2.1 — subprocess-test correction receipt

Status: scoped correction implemented; independent review **PENDING**, global
DOCS.CONTINUITY.1 **PARTIAL**. No global code, semantic or visual audit is claimed.

## Authority, starting identity and supplied review

Authority: [exact supplied R2.1 ticket](../../project/tickets/DOCS.CONTINUITY.1.R2.1.txt),
attachment `3b9db51f-2356-4c23-a4ea-9c16d701d6d9/pasted-text.txt`.
Raw attachment/archive SHA256:
`a84c605da5eb1f0e8a6c1a3cfa90a917991d3dab4301948e6235fbea9a16e9b9`.
Its section 1 is the supplied independent receipt, not a new Codex reproduction.

Clean starting recovery branch `recovery/docs-continuity-1-partial`, HEAD/local
and actual remote recovery `64787a28bd5801dcc88f8e2107cd230fe263d476`;
local/actual remote main `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`.
No unmerged entries or Git-operation markers. Native remote inspection reproduced
the known repository ownership mismatch; only then the authorized exact command
prefix `-c safe.directory=C:/souhaib/landscout-ai` was used. No persistent trust,
environment or security setting changed.

The reviewer accepts the principal R2 auditor corrections in the stated scope:
bounded aliases, commit/file/anchor provenance, incomplete history, ledger shapes,
heading IDs, batched index reads/postcondition, progress and child cleanup. This
does not approve the unfinished global corpus or this new test correction.

The original [R2 receipt](R2_DIAGNOSTICS.md) remains unchanged: its Windows
131-pass run is historical, not contradicted by the supplied Linux observations.
The reviewer verified complete GitHub-retrieved tool/test bytes and reported:

- Tool blob `fe552a4c4eeadb0da10acaa00b2329693ff34a59`, SHA256
  `5b5aae765c6c32225496d7830e17e83a9bfac89e007949b032b75b13eda3029f`.
- Starting test blob `f138ca77fde5b4baa9f88c4259bad815891a4ac8`, SHA256
  `1a77c16a8b357ac6481682a649a9af0729d3eb54f66d9827967757d381c9fe29`.
- Linux Python 3.13.5 / Git 2.47.3, unmodified suite: **129 passed, 2 failed,
  3.92 s, exit 1**. Timeout killed/reaped before required stderr was emitted;
  intended exit 7 instead timed out. Auditor diagnostics were correct.
- Observed startup READY approximately 0.522 s, exit approximately 0.726 s;
  earlier whole command approximately 0.677 s, not universal timings.
- Diagnostic-only child `-I -S` copy: **131 passed, 3.20 s**; not a pass of the
  unchanged test and not proof of scheduling independence by flags alone.

## Correction and assertion boundaries

Only executable change: `tests/unit/test_audit_documentation.py`. The approved
auditor and its companion remain byte-identical. Stdlib-only real children use
`sys.executable -I -S -c`; parent imports/environment/dependencies are unchanged.

The former three-case shared 0.5-second test is replaced by five behavior cases:

- `test_git_nonzero_exit_reaps_child_and_is_controlled[normal/slow-start]`:
  0/0.75-second startup delays, independent 30-second startup/completion budget,
  actual exit 7, auditor 2, READY and redacted phase/role/exit diagnostics.
- `test_git_timeout_after_ready_reaps_child_and_is_controlled[normal/slow-start]`:
  0/0.75-second startup delays, a new tmp_path sentinel written after stdout and
  stderr flush, finite 30-second monotonic READY guard with 0.01-second polling,
  then the deliberately short 0.1-second auditor communicate timeout. The ready
  child sleeps 60 seconds; actual timeout, kill/drain/reap and stderr are required.
- `test_git_cancellation_reaps_ready_child_and_is_controlled`: same READY guard,
  real child, one injected KeyboardInterrupt restoring real communicate before
  the auditor drains/reaps; auditor 2 and redacted cancellation diagnostics.

Each substitute checks progress before handing the owned child to the auditor.
No readiness check consumes/fabricates pipes. No tight elapsed-time assertion,
skip, xfail, global timeout increase, or auditor function patch. Delayed cases
exceed the old 0.5-second assumption; exit 7 cannot pass as timeout.

`_managed_subprocess_child` owns cleanup through setup and auditor execution:
kill if running, wait with a separate 30-second guard, close all three pipes.
Auditor reaping is asserted inside this context, before fallback cleanup.
`test_subprocess_fixture_reaps_child_on_setup_failure[startup-guard/assertion/interrupt]`
forces zero-budget bootstrap expiry, assertion failure or KeyboardInterrupt;
each requires its real child reaped and pipes closed afterward. No unrelated
process or temp-tree deletion. These three cases raise the total to **136**:
128 other cases unchanged + five replacement behaviors + three cleanup cases.
The test inventory is 59 symbols (was 50); this is not semantic closure.

## Executed focused validation

Initial sandbox uv formatter/test attempts failed at cache access before collection
(exit 1). Native execution used the existing environment and explicit repo root.
First focused run: 8 passed / 128 deselected, 2.80 s, base `r21b62`, exit 0.
First full file: 136 passed, 40.65 s, base `r21c79`, exit 0. Ruff then found SIM117;
the new nested contexts were combined. Format check requested a line wrap; Ruff
formatted only this test. These style failures were corrected, not suppressed.

Final commands, each pytest base new beneath
`C:\Users\souha\AppData\Local\LandScout\pytest-runs`:

```text
uv run pytest -q tests/unit/test_audit_documentation.py -k "git_nonzero_exit or git_timeout_after_ready or git_cancellation or subprocess_fixture" --basetemp C:\Users\souha\AppData\Local\LandScout\pytest-runs\r21d83
uv run pytest -q tests/unit/test_audit_documentation.py --basetemp C:\Users\souha\AppData\Local\LandScout\pytest-runs\r21e96
uv run ruff check tests/unit/test_audit_documentation.py
uv run ruff format --check tests/unit/test_audit_documentation.py
uv run mypy tools/audit_documentation.py
uv run python -m compileall -q tests/unit/test_audit_documentation.py
```

Final selected run: **136 collected, 8 selected/passed, 128 deselected, 2.80 s**.
Final whole file: **136 collected/passed, 41.06 s**. Both native exits 0 including
cleanup; zero failures/skips/xfails/warnings reported. The earlier passing runs
also reported none. Ruff all checks passed; format one file already formatted;
mypy no issues in one unchanged source file; compileall exit 0. All final quality
commands exit 0. No full application pytest, dependency update or source operation.
Corrected Linux execution is not claimed; supplied Linux evidence is historical.

## Preservation, companions and candidate integration

Pre-staging verification passed all **106** original protected paths against base
Git identities, current index hashes and recorded raw-checkout hashes. All **274**
starting tracked paths outside the four existing allowed edits retain exact bytes,
including the original R2 receipt, tool companion, coverage, fragments, matrices,
archives and EP research. The original Muret YAML and prior resume-ticket raw/Git
EOL distinctions remain untouched; no new exception or normalization is introduced.
Original coverage SHA256:
`5ae2a994effb59947b0dbe4af97b777bc17fb13998a8ba5b8110f2c42052036c`.

Unchanged tool SHA256:
`5b5aae765c6c32225496d7830e17e83a9bfac89e007949b032b75b13eda3029f`.
Corrected test SHA256:
`0c6ce4167f33c56ad09c3ea7cbe8ebeb039cda7ed013c38022a29d5cc98b0665`.
The [test companion](../files/tests/unit/test_audit_documentation.py.md) documents
every new helper/nested substitute, deadlines, parametrization and cleanup boundary,
with updated exact Git-content fingerprint, complete snapshot and symbol anchors.

Only six paths are allowed: the test, its companion, this receipt, CURRENT_STATE,
DOCUMENTATION_AUDIT and the exact R2.1 ticket archive. The single full INDEX check
below used the explicitly staged preparation version of this receipt. Only this
receipt changes afterward to record outcomes; its later bytes are not retroactively
part of that candidate. No visual/GFM validation is claimed.

### Actual full INDEX check and later receipt boundary

Owner-context command, stdout redirected outside Git:

```text
.venv\Scripts\python.exe -X utf8 tools/audit_documentation.py --check --progress > C:\souhaib\r21-candidate.stdout.txt
```

**Native exit 1**, normal PARTIAL/stale findings, `completed=true`; no hang or exit 2.
Root `C:\souhaib\landscout-ai`, basis `SHA256_OF_EXACT_GIT_CONTENT_BYTES`.
Candidate manifest SHA256:
`fb8f795c5a966e5eec06621b6801698d3aa5f7db1b86554e2d04503bae8499d9`.
280 paths / 277 unique blobs / 29,296,428 per-path content bytes; 94 Python files,
94 AST parses, 4,863 enumerated symbols (4,769 original + 35 tool + 59 test).
Five Git processes, non-shallow local history, unchanged final index enumeration.
Native wrapper wall time 2.114839 s includes manifest capture/launcher overhead,
not a controlled performance benchmark. Phase seconds: index 0.186987,
coverage-input 0.010809, python 0.753744, checkout-markdown 0.280907,
coverage 0.115327, references 0.117096, history 0.080685,
index-postcondition 0.026432.

**10,266 sorted unique findings**, observed rather than targeted. Comparison with
the retained R2 stdout differs only in the inventory-mismatch line adding this
ticket archive. The prior diagnostic groups remain: coverage/staleness 5,033,
mechanical 217, pending recorded acceptance 5,016. The unchanged original ledger
does not declare the historical resume-ticket checkout EOL exception; that finding
is preserved, not hidden. No new source/test companion mechanical finding.

Detailed stdout: `C:\souhaib\r21-candidate.stdout.txt`, PowerShell UTF-16,
2,315,038 bytes, SHA256
`f589e036640f9a56b0bd645d1b5d98508d0860b3363a55743f20147df4500d67`.
The captured path/mode/blob list stays outside Git at
`C:\souhaib\r21-candidate.manifest.json`; decode UTF-16, then compact ASCII-safe
JSON without terminal newline reproduces the manifest above. The later receipt
update is checked separately for links/fences and staged scope/protected bytes;
no second full audit or global ledger regeneration is performed.

New-delta `git diff --check` and `git diff --cached --check` both exit 0.
Cumulative `git diff --cached --check aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`
returns native exit 2 with the original 13 observations: twelve preserved
cold-start Markdown hard breaks and the original ticket's final blank line.
No archive rewrite, whitespace suppression or hook bypass.

## Pending acceptance and publication boundary

Global closure stays **67/245 files, 1,388/4,769 symbols**; 178 files and 3,381
symbols remain open. A-001/A-002/A-003, five test-evidence limitations, cold-start
acceptance (`REPORTED_EXECUTED_PENDING_REVIEW`) and full 7F.1C.1 semantic review
remain pending. No fragment or coverage status is promoted. The two
enrich_planning_features companions remain the deferred next semantic item.

Only recovery-branch publication is authorized, with scoped message
`test: stabilize continuity auditor subprocess regressions`. Final SHA and actual
remote equality/main preservation are verified after publication, not predicted
here. Stop afterward for independent review; no main push, PR, merge or next step.
