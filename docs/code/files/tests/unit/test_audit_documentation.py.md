# `tests/unit/test_audit_documentation.py`

## File identity

- Repository path: `tests/unit/test_audit_documentation.py`
- Source SHA256: `16af752cb12f1ca603151d2d4e69f4d52e09c5212b75292bdf1630c79589d346`
- Source SHA256 basis: `git-content`
- Role: Narrow synthetic regression suite for the offline documentation checker.

## Scope and contracts

Seven test definitions expand to 23 collected cases: one 17-case attack test plus six single-case tests. Helpers write only temporary synthetic repositories; the checker they exercise is read-only. No EP cache, production import, DNS or HTTP is needed. The tests execute the new tool via runpy under a non-main name and directly call its returned functions. Test counts here describe this source; actual executions are recorded separately in the audit report.

<a id="_sha"></a>

### `_sha`

```python
def _sha(text: str) -> str:
```

SHA256 of UTF-8 fixture text; independent helper for expected source headers.

<a id="_write"></a>

### `_write`

```python
def _write(root: Path, path: str, text: str) -> None:
```

Creates parent directories and writes UTF-8 LF fixture text under the supplied temporary root. Used only by synthetic tests; not the read-only checker.

<a id="_stage"></a>

### `_stage`

```python
def _stage(root: Path) -> None:
```

Enumerates existing/indexed fixture paths, excludes .git internals, then stages the explicit resulting path list in the temporary Git repository, including tracked deletions. Does not operate on the LandScout index.

<a id="_companion"></a>

### `_companion`

```python
def _companion(source: str = SOURCE) -> str:
```

Returns a minimal source-bound companion with hash, explicit Git-content basis, work anchor/export and complete Python snapshot; a supplied alternative source updates the header/snapshot for coherent attacks.

<a id="_coverage"></a>

### `_coverage`

```python
def _coverage(root: Path) -> dict[str, Any]:
```

Reads and JSON-decodes the temporary fixture coverage ledger. No production model or real cache is loaded.

<a id="_publish_coverage"></a>

### `_publish_coverage`

```python
def _publish_coverage(root: Path, ledger: dict[str, Any]) -> None:
```

Rehashes existing fixture files in each ledger row, writes sorted JSON, then stages the fixture. Attack tests therefore do not accidentally fail only because of unrelated stale whole-file fingerprints.

<a id="repository"></a>

### `repository`

```python
def repository(tmp_path: Path) -> Path:
```

Creates a temporary repository with autocrlf=false, simple api.py, companion and empty step ledger. Uses the auditor's AST inventory to seed exact symbols, marks fixture review facts, declares original-doc exceptions, computes hashes and stages. It makes no commit and changes no global Git configuration.

<a id="test_small_fixture_is_accepted_read_only"></a>

### `test_small_fixture_is_accepted_read_only`

```python
def test_small_fixture_is_accepted_read_only(repository: Path) -> None:
```

Snapshots all existing temporary repository bytes, calls audit expecting no findings, then compares every snapshotted file's bytes. It proves no modifications to those files; it is not a sentinel against every possible new file or subprocess side effect.

<a id="test_documentation_attack_fails"></a>

### `test_documentation_attack_fails`

```python
def test_documentation_attack_fails(
    repository: Path, attack: str, expected: str
) -> None:
```

Seventeen parametrized mutations target missing companion/anchor, stale header, changed signature, missing export prose, missing local file/anchor, unclosed fence, ambiguous basis, missing review provenance, unfinished review, missing inventory, invented qualified reference, absent export owner, unknown dependency, missing step evidence and unfinished history. Each updates unrelated fingerprints coherently before asserting a targeted diagnostic substring; additional diagnostics may coexist. The entire test runs only against synthetic Git fixtures.

<a id="test_unstaged_change_is_not_hidden_by_index"></a>

### `test_unstaged_change_is_not_hidden_by_index`

```python
def test_unstaged_change_is_not_hidden_by_index(repository: Path) -> None:
```

Adds an unstaged source comment while retaining staged source/ledger bytes, then requires an unstaged-content diagnostic.

<a id="test_declared_exact_checkout_eol_exception"></a>

### `test_declared_exact_checkout_eol_exception`

```python
def test_declared_exact_checkout_eol_exception(repository: Path) -> None:
```

Locks the CRLF checkout SHA in the ledger while keeping LF Git source bytes, changes only checkout EOLs, and requires acceptance. It tests one explicit EOL-only exception, not arbitrary normalization.

<a id="test_malformed_ledger_has_controlled_cli_exit"></a>

### `test_malformed_ledger_has_controlled_cli_exit`

```python
def test_malformed_ledger_has_controlled_cli_exit(
    repository: Path, capsys: Any
) -> None:
```

Stages invalid JSON, invokes main with explicit --check/--root and asserts return code 2 plus the stderr input-error prefix.

<a id="test_nested_fences_preserve_snapshot"></a>

### `test_nested_fences_preserve_snapshot`

```python
def test_nested_fences_preserve_snapshot() -> None:
```

Passes a four-backtick Markdown wrapper containing a three-backtick Python block and asserts no errors, one page anchor, exact captured block bytes and no source statement in prose.

<a id="test_static_owner_resolution_handles_aliases_without_importing"></a>

### `test_static_owner_resolution_handles_aliases_without_importing`

```python
def test_static_owner_resolution_handles_aliases_without_importing() -> None:
```

Inventories three in-memory Python files; verifies a relative reexport alias with an annotated field and a module alias. Rejects a missing field, wrong module owner and a two-node alias cycle. No production module is imported.

## Effects, limits and change impact

Writes/deletes fixture files and invokes Git init/config/add only in tmp_path. These test setup effects must not be attributed to the checker. Retain coherent attacks, zero network and isolated short pytest basetemp behavior. Update this companion and the tool's companion together after changes; do not count passing synthetic mechanics as a semantic review of LandScout.

## Complete exact source snapshot

````python
"""Synthetic Git-only regressions for the offline documentation checker."""

from __future__ import annotations

import hashlib
import json
import runpy
import subprocess
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
    after = {relative: (repository / relative).read_bytes() for relative in before}
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
````
