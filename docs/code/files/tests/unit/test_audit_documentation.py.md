# `tests/unit/test_audit_documentation.py`

## File identity

- Repository path: `tests/unit/test_audit_documentation.py`
- Source SHA256: `1a77c16a8b357ac6481682a649a9af0729d3eb54f66d9827967757d381c9fe29`
- Source SHA256 basis: `git-content`
- Scope: DOCS.CONTINUITY.1.R2 tooling only; independent review pending.

## Scope and contracts

Offline synthetic tests for the existing documentation checker. 131 collected cases, including all 23 original cases, plus 108 R2 regressions. `runpy` loads the checker under a non-main name; fixture files/commits/config mutations are confined to temporary repositories. No application import, real EP cache, DNS/HTTP or remote Git is needed. Use a fresh short pytest `--basetemp` under the established LandScout pytest-runs directory and retain the final process exit including cleanup.

Actual executions and independent-review limits are in the [R2 diagnostic receipt](../../../audit/R2_DIAGNOSTICS.md). Tests use counters and controlled processes, not strict performance thresholds. Mocked shallow history/index mutations prove diagnostic behavior, not a real concurrent filesystem race. No global ledger/status promotion is performed.

<a id="_sha"></a>

### `_sha`

```python
def _sha(text: str) -> str:
```

Hashes UTF-8 fixture text independently for expected headers.

<a id="_write"></a>

### `_write`

```python
def _write(root: Path, path: str, text: str) -> None:
```

Creates fixture parents and writes explicit UTF-8 LF text, only in temporary repositories.

<a id="_stage"></a>

### `_stage`

```python
def _stage(root: Path) -> None:
```

Enumerates temporary fixture files/index paths and stages their exact union, excluding .git. These test setup mutations are not auditor effects.

<a id="_companion"></a>

### `_companion`

```python
def _companion(source: str = SOURCE) -> str:
```

Constructs a coherent minimal source companion with hash, Git-content basis, work anchor/export and full source snapshot.

<a id="_coverage"></a>

### `_coverage`

```python
def _coverage(root: Path) -> dict[str, Any]:
```

Reads the temporary coverage JSON for a targeted fixture mutation.

<a id="_publish_coverage"></a>

### `_publish_coverage`

```python
def _publish_coverage(root: Path, ledger: dict[str, Any]) -> None:
```

Refreshes unrelated fixture file hashes, writes sorted JSON and stages the fixture, isolating the intended attack.

<a id="repository"></a>

### `repository`

```python
def repository(tmp_path: Path) -> Path:
```

Initializes an offline temporary Git repo with local autocrlf=false, api.py, its companion, empty steps and coherent coverage. AST fixture records are CHECKED only as synthetic controls; no real review is granted.

<a id="test_small_fixture_is_accepted_read_only"></a>

### `test_small_fixture_is_accepted_read_only`

```python
def test_small_fixture_is_accepted_read_only(repository: Path) -> None:
```

Requires no findings and compares the complete before/after file set and bytes, including .git, so additions as well as modifications are detected.

<a id="test_documentation_attack_fails"></a>

### `test_documentation_attack_fails`

```python
def test_documentation_attack_fails(
    repository: Path, attack: str, expected: str
) -> None:
```

Preserves all seventeen original attacks: companion/anchor/header/signature/export/link/fence/basis/review/inventory/reference/owner/dependency/provenance/history errors. Requires targeted substrings after coherent unrelated hashes are updated; other diagnostics may coexist.

<a id="test_unstaged_change_is_not_hidden_by_index"></a>

### `test_unstaged_change_is_not_hidden_by_index`

```python
def test_unstaged_change_is_not_hidden_by_index(repository: Path) -> None:
```

Adds only an unstaged source comment and requires a drift finding.

<a id="test_declared_exact_checkout_eol_exception"></a>

### `test_declared_exact_checkout_eol_exception`

```python
def test_declared_exact_checkout_eol_exception(repository: Path) -> None:
```

Keeps LF index source, declares the exact expected CRLF checkout SHA, then writes CRLF checkout bytes and requires no findings.

<a id="test_malformed_ledger_has_controlled_cli_exit"></a>

### `test_malformed_ledger_has_controlled_cli_exit`

```python
def test_malformed_ledger_has_controlled_cli_exit(
    repository: Path, capsys: Any
) -> None:
```

Stages syntactically invalid JSON; requires CLI return 2 and contextual stderr prefix.

<a id="test_nested_fences_preserve_snapshot"></a>

### `test_nested_fences_preserve_snapshot`

```python
def test_nested_fences_preserve_snapshot() -> None:
```

Asserts exact inner Python fence bytes survive a longer Markdown fence; no source content leaks into prose.

<a id="test_static_owner_resolution_handles_aliases_without_importing"></a>

### `test_static_owner_resolution_handles_aliases_without_importing`

```python
def test_static_owner_resolution_handles_aliases_without_importing() -> None:
```

Checks relative reexport field/module aliases, missing field, wrong owner and a fixed two-node cycle using only in-memory source bytes.

<a id="_commit"></a>

### `_commit`

```python
def _commit(root: Path) -> str:
```

Creates a local synthetic commit with command-scoped fixture author identity and returns its SHA; does not set global user config.

<a id="_step"></a>

### `_step`

```python
def _step(root: Path, **overrides: Any) -> dict[str, Any]:
```

Creates a synthetic approved-record control tied to a real temporary commit and companion #work anchor. Overrides only caller-specified fields.

<a id="_publish_step"></a>

### `_publish_step`

```python
def _publish_step(root: Path, step: dict[str, Any]) -> None:
```

Writes the synthetic step ledger and refreshes coverage hashes/staging.

<a id="test_review_provenance_is_structural_not_approval"></a>

### `test_review_provenance_is_structural_not_approval`

```python
def test_review_provenance_is_structural_not_approval(
    repository: Path, status: str, attack: str
) -> None:
```

22 cases: APPROVED and PARTIAL_REVIEW_RECORDED crossed with a valid control and ten malformed/missing commit, anchor, file, path or exact-string attacks. Valid controls have no findings; attacks require a review diagnostic. A structural control is not an actual reviewer verdict.

<a id="test_missing_or_pending_history_never_defaults_checked"></a>

### `test_missing_or_pending_history_never_defaults_checked`

```python
def test_missing_or_pending_history_never_defaults_checked(
    repository: Path, status: str | None, capsys: Any
) -> None:
```

Four absent/READ/NOT_READ/BLOCKED history cases retain PENDING review, require CLI exit 1 plus unfinished-history finding, and compare unchanged step bytes.

<a id="test_wrong_json_shapes_are_controlled"></a>

### `test_wrong_json_shapes_are_controlled`

```python
def test_wrong_json_shapes_are_controlled(
    repository: Path, path: str, payload: str, capsys: Any
) -> None:
```

18 wrong-root/list/step/review and duplicate/nonfinite JSON cases require exit 2, ledger context and no traceback.

<a id="test_nested_ledger_types_are_controlled"></a>

### `test_nested_ledger_types_are_controlled`

```python
def test_nested_ledger_types_are_controlled(
    repository: Path, target: str, key: str, value: Any, capsys: Any
) -> None:
```

22 malformed consumed file/symbol/step/review fields require controlled exit 2. Includes bool-as-line-number, wrong ranges, iterable/scalar confusion and malformed dynamic-reference exceptions.

<a id="test_heading_ids_do_not_collide"></a>

### `test_heading_ids_do_not_collide`

```python
def test_heading_ids_do_not_collide(text: str, expected: set[str]) -> None:
```

Three literal expected sets cover a/a/a-1, repeated and pre-existing suffix slugs, with retained explicit anchor. Expected IDs are not computed by production.

<a id="test_expanding_import_alias_terminates_without_claiming_owner"></a>

### `test_expanding_import_alias_terminates_without_claiming_owner`

```python
def test_expanding_import_alias_terminates_without_claiming_owner() -> None:
```

Direct regressions for self-expanding and mutually growing prefix aliases, plus a resolvable alias control. Exercises the stall found by profiling; no timing threshold.

<a id="test_progress_does_not_change_findings"></a>

### `test_progress_does_not_change_findings`

```python
def test_progress_does_not_change_findings(repository: Path, capsys: Any) -> None:
```

Compares quiet/progress sorted findings for identical unstaged drift, requires root/basis and start/postcondition stderr messages, and checks completion metrics.

<a id="test_git_failure_reaps_child_and_is_controlled"></a>

### `test_git_failure_reaps_child_and_is_controlled`

```python
def test_git_failure_reaps_child_and_is_controlled(
    repository: Path, monkeypatch: Any, capsys: Any, failure: str
) -> None:
```

Three controlled child scenarios: nonzero 7, finite timeout, and injected KeyboardInterrupt. The substitute asserts phase/role progress is already visible before launching/stalling, then the test requires exit 2, useful redacted stderr where available and reaped child. No strict elapsed-time assertion or live Git network.

<a id="test_git_failure_reaps_child_and_is_controlled-substitute"></a>

### `test_git_failure_reaps_child_and_is_controlled.substitute`

```python
    def substitute(*args: Any, **kwargs: Any) -> Any:
```

Replaces only auditor Popen calls with an actual Python child printing a fake credential URL and exiting or sleeping. Captures the child for termination assertions.

<a id="test_git_failure_reaps_child_and_is_controlled-substitute-interrupted"></a>

### `test_git_failure_reaps_child_and_is_controlled.substitute.interrupted`

```python
            def interrupted(*a: Any, **k: Any) -> Any:
```

Restores the real communicate method then raises KeyboardInterrupt once, allowing the auditor's kill/drain path to be exercised.

<a id="test_git_timeout_must_be_finite_and_bounded"></a>

### `test_git_timeout_must_be_finite_and_bounded`

```python
def test_git_timeout_must_be_finite_and_bounded(
    repository: Path, value: str, capsys: Any
) -> None:
```

Five nan/inf/zero/negative/over-300 settings fail with controlled CLI exit 2 before Git.

<a id="test_git_process_count_is_bounded"></a>

### `test_git_process_count_is_bounded`

```python
def test_git_process_count_is_bounded(
    repository: Path, extra: int, monkeypatch: Any
) -> None:
```

Audits fixtures with zero or forty extra files; actual intercepted Popen calls and reported count both equal five. Asserts no shell, lazy fetching disabled and no per-file show.

<a id="test_git_process_count_is_bounded-counted"></a>

### `test_git_process_count_is_bounded.counted`

```python
    def counted(*args: Any, **kwargs: Any) -> Any:
```

Records real process argument vectors, checks readonly execution options, and delegates to the original Popen.

<a id="test_batch_reads_exact_empty_multiline_unicode_and_space_bytes"></a>

### `test_batch_reads_exact_empty_multiline_unicode_and_space_bytes`

```python
def test_batch_reads_exact_empty_multiline_unicode_and_space_bytes(
    repository: Path,
) -> None:
```

Tests zero-byte, NUL/header-like multiline and UTF-8 data with space/Unicode paths, then modifies checkout and confirms read_index still returns exact staged bytes in two processes.

<a id="test_unsupported_index_modes_fail_before_checkout_read"></a>

### `test_unsupported_index_modes_fail_before_checkout_read`

```python
def test_unsupported_index_modes_fail_before_checkout_read(
    repository: Path, mode: str, capsys: Any
) -> None:
```

Creates synthetic 120000 symlink/160000 gitlink index entries and requires controlled unsupported-mode failure without needing external targets.

<a id="test_unmerged_index_fails_closed"></a>

### `test_unmerged_index_fails_closed`

```python
def test_unmerged_index_fails_closed(repository: Path, capsys: Any) -> None:
```

Injects stages 1 and 2 through Git index-info; requires exit 2 and an unmerged-stage diagnostic, not silently dropped rows.

<a id="test_index_change_during_audit_is_operational_failure"></a>

### `test_index_change_during_audit_is_operational_failure`

```python
def test_index_change_during_audit_is_operational_failure(
    repository: Path, monkeypatch: Any, capsys: Any
) -> None:
```

Injects a changed final enumeration and requires controlled exit 2, not ordinary findings.

<a id="test_index_change_during_audit_is_operational_failure-changed"></a>

### `test_index_change_during_audit_is_operational_failure.changed`

```python
    def changed(self: Any, role: str, *args: str, **kwargs: Any) -> bytes:
```

Delegates all queries, altering only index-postcondition bytes to simulate concurrent staging.

<a id="test_ast_is_parsed_once_per_file_without_execution"></a>

### `test_ast_is_parsed_once_per_file_without_execution`

```python
def test_ast_is_parsed_once_per_file_without_execution(
    repository: Path, monkeypatch: Any
) -> None:
```

Adds a Python file that would raise if executed, wraps ast.parse and requires exactly api.py/never_import.py once each; verifies metric count two.

<a id="test_ast_is_parsed_once_per_file_without_execution-counted"></a>

### `test_ast_is_parsed_once_per_file_without_execution.counted`

```python
    def counted(
        source: Any, filename: str = "<unknown>", *args: Any, **kwargs: Any
    ) -> Any:
```

Records parse filenames and delegates to the real parser, without importing candidate modules.

<a id="test_inventory_reuse_keeps_unicode_signature_and_ranges"></a>

### `test_inventory_reuse_keeps_unicode_signature_and_ranges`

```python
def test_inventory_reuse_keeps_unicode_signature_and_ranges(ending: str) -> None:
```

LF/CRLF cases compare standalone/cached inventory and independently assert exact accented multiline field text, SHA and line pair [2,4].

<a id="test_bad_batch_protocol_is_not_silently_skipped"></a>

### `test_bad_batch_protocol_is_not_silently_skipped`

```python
def test_bad_batch_protocol_is_not_silently_skipped(
    repository: Path, monkeypatch: Any, capsys: Any, attack: str
) -> None:
```

Five injected missing/header-size/truncation/trailing/wrong-ID responses require exit 2 and batch-context diagnostics.

<a id="test_bad_batch_protocol_is_not_silently_skipped-malformed"></a>

### `test_bad_batch_protocol_is_not_silently_skipped.malformed`

```python
    def malformed(self: Any, role: str, *args: str, **kwargs: Any) -> bytes:
```

Delegates real queries and mutates only the raw-batch protocol for the selected case.

<a id="test_bad_or_missing_index_object_fails_closed"></a>

### `test_bad_or_missing_index_object_fails_closed`

```python
def test_bad_or_missing_index_object_fails_closed(
    repository: Path, monkeypatch: Any, capsys: Any, payload: bytes
) -> None:
```

Three malformed entry, parent-path and nonexistent-object cases require controlled failure.

<a id="test_bad_or_missing_index_object_fails_closed-malformed"></a>

### `test_bad_or_missing_index_object_fails_closed.malformed`

```python
    def malformed(self: Any, role: str, *args: str, **kwargs: Any) -> bytes:
```

Replaces enumeration bytes only; nonexistent blob lookup still exercises actual offline cat-file.

<a id="test_shallow_history_limit_is_explicit_offline"></a>

### `test_shallow_history_limit_is_explicit_offline`

```python
def test_shallow_history_limit_is_explicit_offline(
    repository: Path, monkeypatch: Any
) -> None:
```

Uses a real synthetic commit with a nonexistent review SHA, injects shallow=true and requires the explicit local-history limitation. No clone or fetch.

<a id="test_shallow_history_limit_is_explicit_offline-shallow"></a>

### `test_shallow_history_limit_is_explicit_offline.shallow`

```python
    def shallow(self: Any, role: str, *args: str, **kwargs: Any) -> bytes:
```

Replaces only the history-scope answer, delegating all other local queries.

<a id="test_read_only_with_real_local_commit_refs_and_config"></a>

### `test_read_only_with_real_local_commit_refs_and_config`

```python
def test_read_only_with_real_local_commit_refs_and_config(repository: Path) -> None:
```

Snapshots full fixture checkout and .git bytes after commit; a successful audit preserves every path and byte including index, refs and config.

<a id="test_missing_required_ledger_is_incomplete_exit_two"></a>

### `test_missing_required_ledger_is_incomplete_exit_two`

```python
def test_missing_required_ledger_is_incomplete_exit_two(
    repository: Path, path: str, capsys: Any
) -> None:
```

Two missing coverage/step-ledger cases require incomplete exit 2; absence is not manufactured into a completed audit.

<a id="test_missing_checkout_does_not_replace_index_markdown"></a>

### `test_missing_checkout_does_not_replace_index_markdown`

```python
def test_missing_checkout_does_not_replace_index_markdown(repository: Path) -> None:
```

Deletes only the companion checkout and requires exactly that checkout finding, proving indexed Markdown still drives companion checks.

<a id="test_duplicate_nested_json_key_is_rejected"></a>

### `test_duplicate_nested_json_key_is_rejected`

```python
def test_duplicate_nested_json_key_is_rejected(repository: Path, capsys: Any) -> None:
```

Stages a nested PENDING/APPROVED duplicate status and requires controlled rejection rather than last-value approval.

<a id="test_redaction_retains_context_without_common_credentials"></a>

### `test_redaction_retains_context_without_common_credentials`

```python
def test_redaction_retains_context_without_common_credentials(text: str) -> None:
```

Four direct cases remove fake Bearer/Basic, URL user-info/query and key-value secrets while retaining useful failure context.

<a id="test_partial_coverage_remains_exit_one_without_promotion"></a>

### `test_partial_coverage_remains_exit_one_without_promotion`

```python
def test_partial_coverage_remains_exit_one_without_promotion(
    repository: Path, capsys: Any
) -> None:
```

Marks only the coverage aggregate PARTIAL and requires completed exit 1, the explicit incomplete-semantic finding, and unchanged ledger bytes.

## Effects, limits and maintenance

Tests create and modify only synthetic fixtures and spawn controlled children; these are not production/auditor writes. The complete file-set comparisons cover normal checkout/index/ref/config behavior, not every possible hostile platform/hook configuration. Preserve targeted assertions when private helpers change. Update the source-bound tool and test companions together; passing mechanics must not increase original semantic closure totals.

## Complete exact source snapshot

````python
"""Synthetic Git-only regressions for the offline documentation checker."""

from __future__ import annotations

import hashlib
import json
import runpy
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

AUDITOR = runpy.run_path(
    str(Path(__file__).resolve().parents[2] / "tools" / "audit_documentation.py")
)
SOURCE = 'def work(value: int = 1) -> int:\n    return value\n\n\n__all__ = ["work"]\n'
DOC = "docs/code/files/api.py.md"
COVERAGE = "docs/code/audit/coverage.json"
STEPS = "docs/project/STEP_LEDGER.json"


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _write(root: Path, path: str, text: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8", newline="\n")


def _stage(root: Path) -> None:
    tracked = (
        subprocess.check_output(["git", "-C", str(root), "ls-files", "-z"])
        .decode()
        .split("\0")
    )
    present = [
        file.relative_to(root).as_posix()
        for file in root.rglob("*")
        if file.is_file() and ".git" not in file.relative_to(root).parts
    ]
    subprocess.run(
        ["git", "-C", str(root), "add", "--", *sorted(set(present + tracked) - {""})],
        check=True,
        capture_output=True,
    )


def _companion(source: str = SOURCE) -> str:
    return (
        "# API\n\n"
        f"- Source SHA256: `{_sha(source)}`\n"
        "- Source SHA256 basis: `git-content`\n\n"
        "## work\n\nReturns the supplied integer; default is one.\n\n"
        "Export: `work`.\n\n"
        f"```python\n{source}```\n"
    )


def _coverage(root: Path) -> dict[str, Any]:
    return json.loads((root / COVERAGE).read_text(encoding="utf-8"))


def _publish_coverage(root: Path, ledger: dict[str, Any]) -> None:
    for row in ledger["files"]:
        file = root / row["path"]
        if file.is_file():
            row["basis_sha256"] = hashlib.sha256(file.read_bytes()).hexdigest()
    _write(root, COVERAGE, json.dumps(ledger, sort_keys=True) + "\n")
    _stage(root)


@pytest.fixture
def repository(tmp_path: Path) -> Path:
    root = tmp_path / "r"
    root.mkdir()
    subprocess.run(["git", "init", str(root)], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(root), "config", "core.autocrlf", "false"],
        check=True,
        capture_output=True,
    )
    _write(root, "api.py", SOURCE)
    _write(root, DOC, _companion())
    _write(root, STEPS, json.dumps({"steps": []}) + "\n")
    symbols = AUDITOR["symbol_inventory"](SOURCE.encode())
    for symbol in symbols:
        symbol["status"] = "CHECKED"
        symbol["documentation_anchor"] = "work"
    ledger = {
        "source_binding_basis": AUDITOR["BASIS"],
        "audit_status": "COMPLETE",
        "files": [
            {
                "path": "api.py",
                "status": "CHECKED",
                "read_complete": True,
                "documentation_path": DOC,
                "symbols": symbols,
                "exports": ["work"],
            },
            {
                "path": DOC,
                "status": "CHECKED",
                "read_complete": True,
                "companion_exception": "original companion; no recursive companion",
            },
            {
                "path": STEPS,
                "status": "CHECKED",
                "read_complete": True,
                "companion_exception": "original continuity record",
            },
        ],
    }
    _publish_coverage(root, ledger)
    return root


def test_small_fixture_is_accepted_read_only(repository: Path) -> None:
    before = {
        file.relative_to(repository): file.read_bytes()
        for file in repository.rglob("*")
        if file.is_file()
    }
    assert AUDITOR["audit"](repository) == []
    after = {
        file.relative_to(repository): file.read_bytes()
        for file in repository.rglob("*")
        if file.is_file()
    }
    assert after == before


@pytest.mark.parametrize(
    ("attack", "expected"),
    [
        ("missing_companion", "missing companion:"),
        ("missing_anchor", "missing documented anchor:"),
        ("stale_hash", "stale companion hash:"),
        ("changed_signature", "stale symbol signature_sha256:"),
        ("missing_export", "missing documented export:"),
        ("bad_link", "bad local link:"),
        ("bad_anchor_link", "bad local anchor:"),
        ("malformed_fence", "unclosed fence"),
        ("ambiguous_eol_basis", "ambiguous companion line-ending basis:"),
        ("missing_review_provenance", "missing review provenance:"),
        ("unresolved_review", "unresolved semantic review row:"),
        ("missing_inventory", "inventory mismatch"),
        ("qualified_reference", "unresolved qualified reference:"),
        ("export_owner", "unresolved export owner:"),
        ("step_reference", "invalid step dependencies:"),
        ("step_provenance", "missing step evidence:"),
        ("history_pending", "unfinished history audit:"),
    ],
)
def test_documentation_attack_fails(
    repository: Path, attack: str, expected: str
) -> None:
    ledger = _coverage(repository)
    doc = (repository / DOC).read_text(encoding="utf-8")
    if attack == "missing_companion":
        (repository / DOC).unlink()
        ledger["files"] = [row for row in ledger["files"] if row["path"] != DOC]
    elif attack == "missing_anchor":
        _write(repository, DOC, doc.replace("## work", "## renamed"))
    elif attack == "stale_hash":
        _write(repository, DOC, doc.replace(_sha(SOURCE), "0" * 64))
    elif attack == "changed_signature":
        source = SOURCE.replace("value: int = 1", "value: int = 2")
        _write(repository, "api.py", source)
        _write(repository, DOC, _companion(source))
    elif attack == "missing_export":
        _write(repository, DOC, doc.replace("Export: `work`.\n", ""))
    elif attack == "bad_link":
        _write(repository, DOC, doc + "\n[missing](missing.md)\n")
    elif attack == "bad_anchor_link":
        _write(repository, DOC, doc + "\n[missing](#absent)\n")
    elif attack == "malformed_fence":
        _write(repository, DOC, doc + "\n```text\nnever closed\n")
    elif attack == "ambiguous_eol_basis":
        _write(
            repository, DOC, doc.replace("basis: `git-content`", "basis: `checkout`")
        )
    elif attack == "missing_review_provenance":
        _write(
            repository,
            STEPS,
            json.dumps({"steps": [{"step_id": "X", "review": {"status": "APPROVED"}}]}),
        )
    elif attack == "unresolved_review":
        ledger["files"][0]["status"] = "READ"
    elif attack == "missing_inventory":
        _write(repository, "unaccounted.txt", "new file\n")
    elif attack == "qualified_reference":
        _write(repository, DOC, doc + "\nCall `landscout.invented.missing`.\n")
    elif attack == "export_owner":
        source = SOURCE.replace('["work"]', '["missing"]')
        _write(repository, "api.py", source)
        _write(repository, DOC, _companion(source) + "\nExport: `missing`.\n")
        ledger["files"][0]["exports"] = ["missing"]
    elif attack in {"step_reference", "step_provenance", "history_pending"}:
        step = {
            "step_id": "X",
            "review": {"status": "PENDING"},
            "dependencies": ["missing"] if attack == "step_reference" else [],
            "provenance": ["missing.md"] if attack == "step_provenance" else [],
            "history_audit_status": "NOT_READ"
            if attack == "history_pending"
            else "CHECKED",
        }
        _write(repository, STEPS, json.dumps({"steps": [step]}))
    else:
        raise AssertionError(attack)
    _publish_coverage(repository, ledger)
    assert any(expected in error for error in AUDITOR["audit"](repository))


def test_unstaged_change_is_not_hidden_by_index(repository: Path) -> None:
    _write(repository, "api.py", SOURCE + "# unstaged\n")
    assert any("unstaged content" in error for error in AUDITOR["audit"](repository))


def test_declared_exact_checkout_eol_exception(repository: Path) -> None:
    ledger = _coverage(repository)
    raw = SOURCE.replace("\n", "\r\n").encode()
    ledger["files"][0]["eol_only_difference"] = True
    ledger["files"][0]["checkout_sha256"] = hashlib.sha256(raw).hexdigest()
    _publish_coverage(repository, ledger)
    (repository / "api.py").write_bytes(raw)
    assert AUDITOR["audit"](repository) == []


def test_malformed_ledger_has_controlled_cli_exit(
    repository: Path, capsys: Any
) -> None:
    _write(repository, COVERAGE, "{")
    _stage(repository)
    assert AUDITOR["main"](["--check", "--root", str(repository)]) == 2
    assert "documentation audit input error" in capsys.readouterr().err


def test_nested_fences_preserve_snapshot() -> None:
    prose, anchors, blocks, errors = AUDITOR["markdown"](
        "# Page\n\n````markdown\n```python\nvalue = 1\n```\n````\n"
    )
    assert errors == []
    assert anchors == {"page"}
    assert blocks == ["```python\nvalue = 1\n```\n"]
    assert "value" not in prose


def test_static_owner_resolution_handles_aliases_without_importing() -> None:
    names, aliases = AUDITOR["python_namespaces"](
        {
            "src/landscout/api.py": b"class Result:\n    value: int\n",
            "src/landscout/__init__.py": b"from .api import Result as PublicResult\n",
            "src/landscout/consumer.py": b"import landscout.api as owner\n",
        }
    )
    resolve = AUDITOR["resolves_reference"]
    assert resolve("landscout.PublicResult.value", names, aliases)
    assert resolve("landscout.consumer.owner.Result", names, aliases)
    assert not resolve("landscout.PublicResult.missing", names, aliases)
    assert not resolve("landscout.consumer.Result", names, aliases)
    assert not resolve("a", set(), {"a": "b", "b": "a"})


def _commit(root: Path) -> str:
    subprocess.run(
        [
            "git",
            "-C",
            str(root),
            "-c",
            "user.name=Synthetic",
            "-c",
            "user.email=synthetic@example.test",
            "commit",
            "-m",
            "fixture",
        ],
        check=True,
        capture_output=True,
    )
    return (
        subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"])
        .decode()
        .strip()
    )


def _step(root: Path, **overrides: Any) -> dict[str, Any]:
    step: dict[str, Any] = {
        "step_id": "X",
        "history_audit_status": "CHECKED",
        "review": {
            "status": "APPROVED",
            "reviewer": "Synthetic reviewer",
            "scope": "Synthetic structural control only",
            "source": DOC + "#work",
            "commit": _commit(root),
        },
    }
    step.update(overrides)
    return step


def _publish_step(root: Path, step: dict[str, Any]) -> None:
    _write(root, STEPS, json.dumps({"steps": [step]}))
    _publish_coverage(root, _coverage(root))


@pytest.mark.parametrize("status", ["APPROVED", "PARTIAL_REVIEW_RECORDED"])
@pytest.mark.parametrize(
    "attack",
    [
        "valid",
        "commit",
        "anchor",
        "nonmarkdown_anchor",
        "missing_file",
        "absolute",
        "parent",
        "backslash",
        "encoded",
        "whitespace",
        "empty",
    ],
)
def test_review_provenance_is_structural_not_approval(
    repository: Path, status: str, attack: str
) -> None:
    step = _step(repository)
    review = step["review"]
    review["status"] = status
    if attack == "commit":
        review["commit"] = "0" * 40
    elif attack == "anchor":
        review["source"] = DOC + "#absent"
    elif attack == "nonmarkdown_anchor":
        review["source"] = "api.py#work"
    elif attack == "missing_file":
        review["source"] = "missing.md"
    elif attack == "absolute":
        review["source"] = "/" + DOC
    elif attack == "parent":
        review["source"] = "docs/../" + DOC
    elif attack == "backslash":
        review["source"] = DOC.replace("/", "\\")
    elif attack == "encoded":
        review["source"] = "%64ocs/code/files/api.py.md"
    elif attack == "whitespace":
        review["reviewer"] = " Reviewer "
    elif attack == "empty":
        review["scope"] = ""
    _publish_step(repository, step)
    errors = AUDITOR["audit"](repository)
    if attack == "valid":
        assert errors == []
    else:
        assert any("review" in error for error in errors)


@pytest.mark.parametrize("status", [None, "READ", "NOT_READ", "BLOCKED"])
def test_missing_or_pending_history_never_defaults_checked(
    repository: Path, status: str | None, capsys: Any
) -> None:
    step = _step(repository, review={"status": "PENDING"})
    if status is None:
        del step["history_audit_status"]
    else:
        step["history_audit_status"] = status
    _publish_step(repository, step)
    before = (repository / STEPS).read_bytes()
    assert AUDITOR["main"](["--check", "--root", str(repository)]) == 1
    assert "unfinished history audit: X" in capsys.readouterr().out
    assert (repository / STEPS).read_bytes() == before


@pytest.mark.parametrize(
    ("path", "payload"),
    [
        (COVERAGE, "[]"),
        (COVERAGE, "null"),
        (COVERAGE, '"text"'),
        (COVERAGE, "{}"),
        (COVERAGE, '{"files":{},"audit_status":"COMPLETE","source_binding_basis":"x"}'),
        (STEPS, "[]"),
        (STEPS, "null"),
        (STEPS, "{}"),
        (STEPS, '{"steps":{}}'),
        (STEPS, '{"steps":[null]}'),
        (STEPS, '{"steps":[{"step_id":[],"review":{}}]}'),
        (STEPS, '{"steps":[{"step_id":"X","review":[]}]}'),
        (STEPS, '{"steps":[{"step_id":"X","review":{"status":5}}]}'),
        (STEPS, '{"steps":[],"steps":[]}'),
        (STEPS, '{"steps":[],"number":NaN}'),
        (COVERAGE, '{"number":Infinity}'),
        (STEPS, '{"steps":[],"number":-Infinity}'),
        (STEPS, '{"steps":[],"number":1e999}'),
    ],
)
def test_wrong_json_shapes_are_controlled(
    repository: Path, path: str, payload: str, capsys: Any
) -> None:
    _write(repository, path, payload)
    _stage(repository)
    assert AUDITOR["main"](["--check", "--root", str(repository)]) == 2
    error = capsys.readouterr().err
    assert path in error
    assert "Traceback" not in error


@pytest.mark.parametrize(
    ("target", "key", "value"),
    [
        ("ledger", "files", [None]),
        ("ledger", "dynamic_reference_exceptions", [None]),
        (
            "ledger",
            "dynamic_reference_exceptions",
            [{"documentation_path": DOC, "reference": [], "reason": "x"}],
        ),
        ("file", "path", []),
        ("file", "status", []),
        ("file", "read_complete", 1),
        ("file", "documentation_path", {}),
        ("file", "symbols", {}),
        ("file", "symbols", [None]),
        ("file", "exports", [1]),
        ("symbol", "kind", []),
        ("symbol", "range", [True, 2]),
        ("symbol", "range", [2]),
        ("symbol", "documentation_anchor", []),
        ("step", "implementation", []),
        ("step", "provenance", [None]),
        ("step", "dependencies", "X"),
        ("step", "history_audit_status", []),
        ("review", "reviewer", []),
        ("review", "source", {}),
        ("review", "scope", False),
        ("review", "commit", 123),
    ],
)
def test_nested_ledger_types_are_controlled(
    repository: Path, target: str, key: str, value: Any, capsys: Any
) -> None:
    if target in {"step", "review"}:
        step = _step(repository)
        (step["review"] if target == "review" else step)[key] = value
        _publish_step(repository, step)
        path = STEPS
    else:
        ledger = _coverage(repository)
        record = ledger if target == "ledger" else ledger["files"][0]
        if target == "symbol":
            record = record["symbols"][0]
        record[key] = value
        _write(repository, COVERAGE, json.dumps(ledger))
        _stage(repository)
        path = COVERAGE
    assert AUDITOR["main"](["--check", "--root", str(repository)]) == 2
    error = capsys.readouterr().err
    assert path in error and "Traceback" not in error


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("# a\n# a\n# a-1\n", {"a", "a-1", "a-1-1"}),
        ("# a\n# a\n# a\n# a-1\n# a-1\n", {"a", "a-1", "a-2", "a-1-1", "a-1-2"}),
        ('<a id="explicit"></a>\n# a-1\n# a\n# a\n', {"explicit", "a-1", "a", "a-2"}),
    ],
)
def test_heading_ids_do_not_collide(text: str, expected: set[str]) -> None:
    assert AUDITOR["markdown"](text)[1] == expected


def test_expanding_import_alias_terminates_without_claiming_owner() -> None:
    resolve = AUDITOR["resolves_reference"]
    assert not resolve("pkg.api.Model.dynamic", set(), {"pkg.api": "pkg.api.api"})
    assert not resolve("a.x", set(), {"a": "b.more", "b": "a.more"})
    assert resolve("alias.value", {"owner.value"}, {"alias": "owner"})


def test_progress_does_not_change_findings(repository: Path, capsys: Any) -> None:
    _write(repository, "api.py", SOURCE + "# unstaged\n")
    quiet = AUDITOR["audit"](repository)
    capsys.readouterr()
    metrics: dict[str, Any] = {}
    visible = AUDITOR["audit"](repository, progress=True, metrics=metrics)
    assert quiet == visible == sorted(set(visible))
    error = capsys.readouterr().err
    assert "root=" in error and AUDITOR["BASIS"] in error
    assert "[index] start" in error and "[index-postcondition]" in error
    assert metrics["completed"] is True


@pytest.mark.parametrize("failure", ["timeout", "nonzero", "cancelled"])
def test_git_failure_reaps_child_and_is_controlled(
    repository: Path, monkeypatch: Any, capsys: Any, failure: str
) -> None:
    popen = subprocess.Popen
    children: list[Any] = []

    def substitute(*args: Any, **kwargs: Any) -> Any:
        observed = capsys.readouterr().err
        assert "[index] start" in observed
        assert "Git index enumeration" in observed
        script = "import sys,time; print('failure https://user:secret@example.test/x?token=abc',file=sys.stderr,flush=True); "
        script += "sys.exit(7)" if failure == "nonzero" else "time.sleep(60)"
        child = popen([sys.executable, "-c", script], **kwargs)
        children.append(child)
        if failure == "cancelled":
            communicate = child.communicate

            def interrupted(*a: Any, **k: Any) -> Any:
                child.communicate = communicate
                raise KeyboardInterrupt

            child.communicate = interrupted
        return child

    monkeypatch.setattr(subprocess, "Popen", substitute)
    result = AUDITOR["main"](
        ["--check", "--root", str(repository), "--progress", "--git-timeout", "0.5"]
    )
    assert result == 2
    assert children and all(child.poll() is not None for child in children)
    error = capsys.readouterr().err
    assert "index" in error and "index enumeration" in error
    assert ("exit 7" if failure == "nonzero" else failure) in error
    if failure != "cancelled":
        assert "failure" in error and "example.test" in error and "[REDACTED]" in error
    assert "user:secret" not in error and "token=abc" not in error


@pytest.mark.parametrize("value", ["nan", "inf", "0", "-1", "301"])
def test_git_timeout_must_be_finite_and_bounded(
    repository: Path, value: str, capsys: Any
) -> None:
    assert (
        AUDITOR["main"](["--check", "--root", str(repository), "--git-timeout", value])
        == 2
    )
    assert "timeout must be finite" in capsys.readouterr().err


@pytest.mark.parametrize("extra", [0, 40])
def test_git_process_count_is_bounded(
    repository: Path, extra: int, monkeypatch: Any
) -> None:
    for i in range(extra):
        _write(repository, f"extra {i}.txt", f"{i}\n")
    _stage(repository)
    popen = subprocess.Popen
    processes: list[Any] = []

    def counted(*args: Any, **kwargs: Any) -> Any:
        processes.append(args[0])
        assert kwargs.get("shell", False) is False
        assert kwargs["env"]["GIT_NO_LAZY_FETCH"] == "1"
        return popen(*args, **kwargs)

    monkeypatch.setattr(subprocess, "Popen", counted)
    metrics: dict[str, Any] = {}
    AUDITOR["audit"](repository, metrics=metrics)
    assert metrics["git_processes"] == len(processes) == 5
    assert all("show" not in command for command in processes)
    assert metrics["files"] == 4 + extra


def test_batch_reads_exact_empty_multiline_unicode_and_space_bytes(
    repository: Path,
) -> None:
    payloads = {
        "empty file.dat": b"",
        "espace é.dat": "é\n汉字\n".encode(),
        "multiline.dat": b"\x00\n123 blob 4\ndata\nlast",
    }
    for path, raw in payloads.items():
        (repository / path).write_bytes(raw)
    _stage(repository)
    (repository / "espace é.dat").write_bytes(b"unstaged")
    run = AUDITOR["AuditRun"](repository, False, 30)
    files, _ = AUDITOR["read_index"](run)
    assert {path: files[path] for path in payloads} == payloads
    assert run.metrics["git_processes"] == 2


@pytest.mark.parametrize("mode", ["120000", "160000"])
def test_unsupported_index_modes_fail_before_checkout_read(
    repository: Path, mode: str, capsys: Any
) -> None:
    oid = (
        _commit(repository)
        if mode == "160000"
        else subprocess.check_output(
            ["git", "-C", str(repository), "rev-parse", ":api.py"]
        )
        .decode()
        .strip()
    )
    subprocess.run(
        [
            "git",
            "-C",
            str(repository),
            "update-index",
            "--add",
            "--cacheinfo",
            f"{mode},{oid},external",
        ],
        check=True,
    )
    assert AUDITOR["main"](["--check", "--root", str(repository)]) == 2
    assert f"unsupported mode {mode}" in capsys.readouterr().err


def test_unmerged_index_fails_closed(repository: Path, capsys: Any) -> None:
    oid = (
        subprocess.check_output(["git", "-C", str(repository), "rev-parse", ":api.py"])
        .decode()
        .strip()
    )
    lines = f"0 {'0' * 40}\tapi.py\n100644 {oid} 1\tapi.py\n100644 {oid} 2\tapi.py\n"
    subprocess.run(
        ["git", "-C", str(repository), "update-index", "--index-info"],
        input=lines.encode(),
        check=True,
    )
    assert AUDITOR["main"](["--check", "--root", str(repository)]) == 2
    assert "unmerged stage" in capsys.readouterr().err


def test_index_change_during_audit_is_operational_failure(
    repository: Path, monkeypatch: Any, capsys: Any
) -> None:
    cls = AUDITOR["AuditRun"]
    original = cls.git

    def changed(self: Any, role: str, *args: str, **kwargs: Any) -> bytes:
        result: bytes = original(self, role, *args, **kwargs)
        return result + b"changed" if role == "index postcondition" else result

    monkeypatch.setattr(cls, "git", changed)
    assert AUDITOR["main"](["--check", "--root", str(repository)]) == 2
    assert "index changed during audit" in capsys.readouterr().err


def test_ast_is_parsed_once_per_file_without_execution(
    repository: Path, monkeypatch: Any
) -> None:
    import ast

    _write(
        repository,
        "never_import.py",
        "raise RuntimeError('must not execute')\nclass É:\n    café: tuple[str, ...] = ('é',)\n",
    )
    _stage(repository)
    parse = ast.parse
    calls: list[str] = []

    def counted(
        source: Any, filename: str = "<unknown>", *args: Any, **kwargs: Any
    ) -> Any:
        calls.append(filename)
        return parse(source, filename, *args, **kwargs)

    monkeypatch.setattr(ast, "parse", counted)
    metrics: dict[str, Any] = {}
    AUDITOR["audit"](repository, metrics=metrics)
    assert calls == ["api.py", "never_import.py"]
    assert metrics["ast_parses"] == 2


@pytest.mark.parametrize("ending", ["\n", "\r\n"])
def test_inventory_reuse_keeps_unicode_signature_and_ranges(ending: str) -> None:
    import ast

    source = "class É:\n    café: tuple[str, ...] = (\n        'é',\n    )\n".replace(
        "\n", ending
    )
    raw = source.encode()
    tree = ast.parse(source)
    expected_field = (
        "café: tuple[str, ...] = (" + ending + "        'é'," + ending + "    )"
    )
    reused = AUDITOR["symbol_inventory"](raw, tree)
    assert reused == AUDITOR["symbol_inventory"](raw)
    assert reused[1]["signature"] == expected_field
    assert reused[1]["signature_sha256"] == _sha(expected_field)
    assert reused[1]["range"] == [2, 4]


@pytest.mark.parametrize(
    "attack", ["missing", "size", "truncated", "trailing", "wrong_oid"]
)
def test_bad_batch_protocol_is_not_silently_skipped(
    repository: Path, monkeypatch: Any, capsys: Any, attack: str
) -> None:
    cls = AUDITOR["AuditRun"]
    original = cls.git

    def malformed(self: Any, role: str, *args: str, **kwargs: Any) -> bytes:
        result: bytes = original(self, role, *args, **kwargs)
        if role != "raw blob batch":
            return result
        if attack == "missing":
            return b"0" * 40 + b" missing\n"
        if attack == "size":
            header, _, body = result.partition(b"\n")
            return header.rsplit(b" ", 1)[0] + b" -1\n" + body
        if attack == "truncated":
            return result[:-1]
        if attack == "wrong_oid":
            return b"0" * 40 + result[40:]
        return result + b"extra"

    monkeypatch.setattr(cls, "git", malformed)
    assert AUDITOR["main"](["--check", "--root", str(repository)]) == 2
    assert "blob batch:" in capsys.readouterr().err


@pytest.mark.parametrize(
    "payload",
    [
        b"broken\0",
        b"100644 " + b"0" * 40 + b" 0\t../outside\0",
        b"100644 " + b"0" * 40 + b" 0\tapi.py\0",
    ],
)
def test_bad_or_missing_index_object_fails_closed(
    repository: Path, monkeypatch: Any, capsys: Any, payload: bytes
) -> None:
    cls = AUDITOR["AuditRun"]
    original = cls.git

    def malformed(self: Any, role: str, *args: str, **kwargs: Any) -> bytes:
        return (
            payload
            if role == "index enumeration"
            else original(self, role, *args, **kwargs)
        )

    monkeypatch.setattr(cls, "git", malformed)
    assert AUDITOR["main"](["--check", "--root", str(repository)]) == 2
    assert "documentation audit input error" in capsys.readouterr().err


def test_shallow_history_limit_is_explicit_offline(
    repository: Path, monkeypatch: Any
) -> None:
    step = _step(repository)
    step["review"]["commit"] = "0" * 40
    _publish_step(repository, step)
    cls = AUDITOR["AuditRun"]
    original = cls.git

    def shallow(self: Any, role: str, *args: str, **kwargs: Any) -> bytes:
        return (
            b"true\n"
            if role == "history scope"
            else original(self, role, *args, **kwargs)
        )

    monkeypatch.setattr(cls, "git", shallow)
    errors = AUDITOR["audit"](repository)
    assert any(
        "unknown review commit" in item and "shallow repository" in item
        for item in errors
    )


def test_read_only_with_real_local_commit_refs_and_config(repository: Path) -> None:
    _commit(repository)
    before = {
        file.relative_to(repository): file.read_bytes()
        for file in repository.rglob("*")
        if file.is_file()
    }
    assert AUDITOR["audit"](repository) == []
    after = {
        file.relative_to(repository): file.read_bytes()
        for file in repository.rglob("*")
        if file.is_file()
    }
    assert after == before


@pytest.mark.parametrize("path", [COVERAGE, STEPS])
def test_missing_required_ledger_is_incomplete_exit_two(
    repository: Path, path: str, capsys: Any
) -> None:
    (repository / path).unlink()
    _stage(repository)
    assert AUDITOR["main"](["--check", "--root", str(repository)]) == 2
    assert "missing" in capsys.readouterr().err


def test_missing_checkout_does_not_replace_index_markdown(repository: Path) -> None:
    (repository / DOC).unlink()
    findings = AUDITOR["audit"](repository)
    assert findings == [f"missing checkout file: {DOC}"]


def test_duplicate_nested_json_key_is_rejected(repository: Path, capsys: Any) -> None:
    _write(
        repository,
        STEPS,
        '{"steps":[{"step_id":"X","review":{"status":"PENDING","status":"APPROVED"}}]}',
    )
    _stage(repository)
    assert AUDITOR["main"](["--check", "--root", str(repository)]) == 2
    assert "duplicate JSON key 'status'" in capsys.readouterr().err


@pytest.mark.parametrize(
    "text",
    [
        "Authorization: Bearer sensitive-value",
        "Authorization: Basic sensitive-value",
        "https://user:sensitive-value@example.test/path?key=sensitive-value",
        "password=sensitive-value token=sensitive-value secret=sensitive-value",
    ],
)
def test_redaction_retains_context_without_common_credentials(text: str) -> None:
    result = AUDITOR["redacted"]("useful Git failure: " + text)
    assert "sensitive-value" not in result
    assert "useful Git failure" in result and "[REDACTED]" in result


def test_partial_coverage_remains_exit_one_without_promotion(
    repository: Path, capsys: Any
) -> None:
    ledger = _coverage(repository)
    ledger["audit_status"] = "PARTIAL"
    _publish_coverage(repository, ledger)
    before = (repository / COVERAGE).read_bytes()
    assert AUDITOR["main"](["--check", "--root", str(repository)]) == 1
    assert "semantic audit ledger is not COMPLETE" in capsys.readouterr().out
    assert (repository / COVERAGE).read_bytes() == before
````
