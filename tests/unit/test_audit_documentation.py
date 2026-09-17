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
