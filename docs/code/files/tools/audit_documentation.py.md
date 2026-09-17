# `tools/audit_documentation.py`

## File identity

- Repository path: `tools/audit_documentation.py`
- Source SHA256: `8eca12abc2b9a93faab1c33ab21deddd2fe01b58ac1eba50778ad5b83236510f`
- Source SHA256 basis: `git-content`
- Role: Offline read-only documentation mechanics checker; not a LandScout business pipeline or semantic reviewer.

## Scope and contracts

Uses only argparse, ast, hashlib, json, re, subprocess, sys, pathlib, typing and urllib.parse from the standard library. Inputs are Git index bytes plus current checkout bytes and explicit JSON review ledgers. `BASIS` is SHA256_OF_EXACT_GIT_CONTENT_BYTES; complete review statuses are CHECKED/CORRECTED, with NOT_READ/READ/BLOCKED retained as unresolved. `COVERAGE`, `STEP_LEDGER` and `SELF_OUTPUTS` name the versioned ledger paths and self-referential audit-output exclusion. No configuration or runtime application artifact is created.

Run `uv run python tools/audit_documentation.py --check` after explicit-path staging of the reviewed candidate. Exit 0 means mechanically consistent records, not independent approval; 1 means findings; 2 means an input/argument failure. Existing source and test companions plus project history are read, never rewritten. Current qualified-reference scanning covers backticked landscout/tests/tools names; shorter aliases and dynamic call ownership still need manual review or a documented exception.

<a id="sha256"></a>

### `sha256`

```python
def sha256(raw: bytes) -> str:
```

Hashes the supplied bytes once with SHA256 and returns the lowercase hexadecimal digest. No normalization, Git blob prefix, object repr, I/O or mutation. Used for candidate and signature identities.

<a id="git"></a>

### `git`

```python
def git(root: Path, *args: str) -> bytes:
```

Invokes Git with the explicit root, forwards the caller's arguments and captures stdout bytes/stderr. Current call sites use ls-files, show and rev-list only. It does not itself enforce a read-only verb allowlist; callers own that restriction. OS/process failures propagate to main's controlled input-error boundary.

<a id="symbol_inventory"></a>

### `symbol_inventory`

```python
def symbol_inventory(raw: bytes) -> list[dict[str, Any]]:
```

Decodes UTF-8, keeps source lines, then parses AST and walks definitions in source order. Records qualified lexical names, definition ranges and exact source signature hashes; records annotated Name fields directly inside classes. No import/execution, inferred runtime fields, decorator expansion or dynamic member discovery. Returns ordinary mutable audit records, not a trust-bearing application model.

<a id="symbol_inventory-visitor"></a>

### `symbol_inventory.Visitor`

```python
    class Visitor(ast.NodeVisitor):
```

Local AST traversal helper, not a public configuration model. It owns a mutable lexical scope stack and closes over source lines and the output list. The mutable stack is implementation state, not an application integrity artifact.

<a id="symbol_inventory-visitor-__init__"></a>

### `symbol_inventory.Visitor.__init__`

```python
        def __init__(self) -> None:
```

Initializes an empty lexical scope list. The enclosing traversal creates one visitor per inventory call; no shared or retained caller alias.

<a id="symbol_inventory-visitor-definition"></a>

### `symbol_inventory.Visitor.definition`

```python
        def definition(
            self, node: ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef, kind: str
        ) -> None:
```

Slices the exact source header up to the first body statement, appends its name/kind/range/signature record, pushes the scope, and for classes records direct annotated Name fields using their exact AST source segment. Recurses with generic_visit, then pops scope. Nested definitions keep their lexical path. Syntax/parser errors are not silently skipped.

<a id="symbol_inventory-visitor-visit_functiondef"></a>

### `symbol_inventory.Visitor.visit_FunctionDef`

```python
        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
```

Delegates a synchronous function node to definition with kind function. Does not execute or infer return behavior.

<a id="symbol_inventory-visitor-visit_asyncfunctiondef"></a>

### `symbol_inventory.Visitor.visit_AsyncFunctionDef`

```python
        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
```

Delegates an asynchronous function node to the same function inventory path; no event loop or coroutine execution.

<a id="symbol_inventory-visitor-visit_classdef"></a>

### `symbol_inventory.Visitor.visit_ClassDef`

```python
        def visit_ClassDef(self, node: ast.ClassDef) -> None:
```

Delegates a class node to definition with kind class, enabling direct annotated-field inventory as well as nested traversal.

<a id="exports"></a>

### `exports`

```python
def exports(raw: bytes) -> list[str] | None:
```

Parses only top-level Assign nodes whose target includes __all__. Evaluates the assigned literal, requires a list/tuple of exact strings and returns a new list; returns None if absent. Dynamic expressions fail instead of being guessed. Annotated __all__ assignments and runtime export changes are outside this bounded implementation.

<a id="python_namespaces"></a>

### `python_namespaces`

```python
def python_namespaces(raw_files: dict[str, bytes]) -> tuple[set[str], dict[str, str]]:
```

For each indexed Python path, derives its module (removing src and __init__), adds parent namespaces and inventoried definitions/fields, then records top-level assignment names and import aliases including relative imports. Returns a name set and alias map. It does not import modules, resolve wildcard imports, infer instance types or evaluate conditional/dynamic definitions.

<a id="resolves_reference"></a>

### `resolves_reference`

```python
def resolves_reference(
    reference: str, names: set[str], aliases: dict[str, str]
) -> bool:
```

Checks the full name, then repeatedly rewrites the longest matching import-alias prefix. A seen-name set terminates alias cycles; an absent rewrite returns False. Repository-static ownership may resolve while dynamic/external leaves remain explicitly unproven.

<a id="markdown"></a>

### `markdown`

```python
def markdown(text: str) -> tuple[str, set[str], list[str], list[str]]:
```

Walks lines, collecting prose separately from fenced blocks. Opening fences use backticks or tildes (at least three); same-character closing runs must be at least as long and have no trailing text. Unclosed/malformed closing fences become diagnostics. Extracts explicit HTML ids/names and simplified GitHub-style ATX heading slugs with duplicate suffixes. It is not a full Markdown renderer: no semantic interpretation of table cells, Mermaid, reference-style links or all CommonMark constructs.

<a id="local_links"></a>

### `local_links`

```python
def local_links(path: str, prose: str) -> list[tuple[str, str]]:
```

Extracts simple inline Markdown and HTML href targets from prose, ignores HTTP/HTTPS/mailto provenance, rejects other schemes/netlocs, backslashes and absolute local paths as nonportable, URL-decodes local paths/anchors and resolves parent components without escaping repository scope. Returns targets, not filesystem reads; malformed URL/angle syntax can raise a controlled input error through main.

<a id="audit"></a>

### `audit`

```python
def audit(root: Path) -> list[str]:
```

Reads indexed paths and exact index bytes, requires the coverage ledger, checks its declared basis and exact non-self-output inventory, then checks checkout drift (only an explicit byte-locked EOL exception passes). Parses Markdown and static Python namespaces. For every covered path, checks fingerprint/read/status, companion or explicit exception, exact single SHA/basis headers and full snapshot. Python companions additionally require exact symbol ranges/signatures/status/anchors and literal exports/owners. Finally checks qualified prose references, local links/anchors and step/provenance/review consistency. Returns sorted unique diagnostics, including recorded semantic-review incompleteness; it never manufactures semantic approval from those records. It does not write reports or update the index.

<a id="main"></a>

### `main`

```python
def main(argv: list[str] | None = None) -> int:
```

Requires --check, accepts optional --root (default repository parent of this tool), resolves it and invokes audit. Prints sorted findings and returns 1; catches the listed filesystem/process/value/key/type/syntax errors and returns 2 on stderr; returns 0 only when mechanics agree. argparse handles argument errors itself. The __main__ guard raises SystemExit with that result; importing/run_path under another name does not run the CLI.

## Effects, limits and change impact

Git query subprocesses and filesystem reads are the only checker effects, besides stdout/stderr and its exit status. No repository writes, staging, cache access, network, hosted renderer, daemon or CI integration. Mechanical checks do not certify prose algorithm accuracy, real-source validity, legal semantics, full dynamic imports/calls or visual Markdown rendering. After changes, update synthetic tests, this companion, coverage's AST/signature/anchor records, testing/maintenance routes and the actual audit report. A complete source snapshot is an identity aid, not a replacement for the explanations above.

## Complete exact source snapshot

````python
"""Offline, read-only checks of Git-index documentation evidence, not semantic approval."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import unquote, urlsplit

BASIS = "SHA256_OF_EXACT_GIT_CONTENT_BYTES"
COMPLETE = {"CHECKED", "CORRECTED"}
STATUSES = COMPLETE | {"NOT_READ", "READ", "BLOCKED"}
COVERAGE = "docs/code/audit/coverage.json"
STEP_LEDGER = "docs/project/STEP_LEDGER.json"
SELF_OUTPUTS = "docs/code/audit/"


def sha256(raw: bytes) -> str:
    """Hash content bytes, never Git's blob envelope or a Python representation."""
    return hashlib.sha256(raw).hexdigest()


def git(root: Path, *args: str) -> bytes:
    """Run a read-only Git query; callers supply only fixed query verbs."""
    return subprocess.check_output(
        ["git", "-C", str(root), *args], stderr=subprocess.PIPE
    )


def symbol_inventory(raw: bytes) -> list[dict[str, Any]]:
    """Enumerate definitions and annotated class fields without importing code."""
    source = raw.decode("utf-8")
    lines = source.splitlines(keepends=True)
    found: list[dict[str, Any]] = []

    class Visitor(ast.NodeVisitor):
        def __init__(self) -> None:
            self.scope: list[str] = []

        def definition(
            self, node: ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef, kind: str
        ) -> None:
            end = node.body[0].lineno - 1
            signature = (
                "".join(lines[node.lineno - 1 : end])
                + lines[end][: node.body[0].col_offset]
            ).rstrip()
            name = ".".join([*self.scope, node.name])
            found.append(
                {
                    "qualified_name": name,
                    "kind": kind,
                    "range": [node.lineno, node.end_lineno],
                    "signature_sha256": sha256(signature.encode("utf-8")),
                    "signature": signature,
                }
            )
            self.scope.append(node.name)
            if kind == "class":
                for field in node.body:
                    if isinstance(field, ast.AnnAssign) and isinstance(
                        field.target, ast.Name
                    ):
                        field_source = ast.get_source_segment(source, field) or ""
                        found.append(
                            {
                                "qualified_name": name + "." + field.target.id,
                                "kind": "field",
                                "range": [field.lineno, field.end_lineno],
                                "signature_sha256": sha256(
                                    field_source.encode("utf-8")
                                ),
                                "signature": field_source,
                            }
                        )
            self.generic_visit(node)
            self.scope.pop()

        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            self.definition(node, "function")

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
            self.definition(node, "function")

        def visit_ClassDef(self, node: ast.ClassDef) -> None:
            self.definition(node, "class")

    Visitor().visit(ast.parse(source))
    return found


def exports(raw: bytes) -> list[str] | None:
    """Return a literal module-level __all__, rejecting dynamic declarations."""
    for node in ast.parse(raw.decode("utf-8")).body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "__all__"
            for target in node.targets
        ):
            value = ast.literal_eval(node.value)
            if not isinstance(value, (list, tuple)) or any(
                type(name) is not str for name in value
            ):
                raise ValueError("nonliteral string export inventory")
            return list(value)
    return None


def python_namespaces(raw_files: dict[str, bytes]) -> tuple[set[str], dict[str, str]]:
    """Inventory static Python ownership and import aliases, without execution."""
    names: set[str] = set()
    aliases: dict[str, str] = {}
    for path, raw in raw_files.items():
        if not path.endswith(".py"):
            continue
        parts = list(PurePosixPath(path).with_suffix("").parts)
        if parts[0] == "src":
            parts.pop(0)
        package = parts[-1] == "__init__"
        if package:
            parts.pop()
        module = ".".join(parts)
        names.update(".".join(parts[:end]) for end in range(1, len(parts) + 1))
        for symbol in symbol_inventory(raw):
            names.add(module + "." + symbol["qualified_name"])
        tree = ast.parse(raw.decode("utf-8"))
        for node in tree.body:
            if isinstance(node, (ast.Assign, ast.AnnAssign)):
                targets = (
                    node.targets if isinstance(node, ast.Assign) else [node.target]
                )
                for target in targets:
                    for item in ast.walk(target):
                        if isinstance(item, ast.Name):
                            names.add(module + "." + item.id)
            elif isinstance(node, ast.Import):
                for item in node.names:
                    local = item.asname or item.name.split(".")[0]
                    aliases[module + "." + local] = item.name if item.asname else local
            elif isinstance(node, ast.ImportFrom):
                parent = parts if package else parts[:-1]
                prefix = (
                    ".".join(parent[: len(parent) - node.level + 1])
                    if node.level
                    else ""
                )
                owner = ".".join(piece for piece in (prefix, node.module) if piece)
                for item in node.names:
                    if item.name != "*":
                        aliases[module + "." + (item.asname or item.name)] = (
                            owner + "." + item.name
                        )
    return names, aliases


def resolves_reference(
    reference: str, names: set[str], aliases: dict[str, str]
) -> bool:
    """Resolve static repository references; dynamic/external leaves remain unproven."""
    seen: set[str] = set()
    while reference not in seen:
        seen.add(reference)
        if reference in names:
            return True
        parts = reference.split(".")
        for end in range(len(parts), 0, -1):
            prefix = ".".join(parts[:end])
            if prefix in aliases:
                reference = ".".join([aliases[prefix], *parts[end:]])
                break
        else:
            return False
    return False


def markdown(text: str) -> tuple[str, set[str], list[str], list[str]]:
    """Separate fenced bytes/prose and derive explicit/GFM-style heading anchors."""
    prose: list[str] = []
    blocks: list[str] = []
    errors: list[str] = []
    current: list[str] = []
    fence = ""
    start = 0
    for number, line in enumerate(text.splitlines(keepends=True), 1):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*?)(?:\r?\n)?$", line)
        if not fence:
            if match:
                fence, start = match[1], number
                current = []
            else:
                prose.append(line)
        elif match and match[1][0] == fence[0] and len(match[1]) >= len(fence):
            if match[2].strip():
                errors.append(f"malformed closing fence at line {number}")
            else:
                blocks.append("".join(current))
                fence = ""
        else:
            current.append(line)
    if fence:
        errors.append(f"unclosed fence at line {start}")
    outside = "".join(prose)
    anchors = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', outside))
    seen: dict[str, int] = {}
    for line in outside.splitlines():
        heading = re.match(r"^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?$", line)
        if heading:
            label = re.sub(r"<[^>]*>", "", heading[1]).lower()
            slug = re.sub(r"[^\w\- ]", "", label, flags=re.UNICODE).replace(" ", "-")
            ordinal = seen.get(slug, 0)
            anchors.add(slug + (f"-{ordinal}" if ordinal else ""))
            seen[slug] = ordinal + 1
    return outside, anchors, blocks, errors


def local_links(path: str, prose: str) -> list[tuple[str, str]]:
    """Resolve simple Markdown/HTML local targets; external provenance is not crawled."""
    targets = re.findall(r"\]\(([^\n]+?)\)", prose)
    targets += re.findall(r'href=["\']([^"\']+)["\']', prose)
    result: list[tuple[str, str]] = []
    for target in targets:
        target = target.strip()
        if target.startswith("<"):
            target = target[1 : target.index(">")]
        else:
            target = target.split(' "', 1)[0]
        parsed = urlsplit(target)
        if parsed.scheme in {"http", "https", "mailto"}:
            continue
        if parsed.scheme or parsed.netloc or "\\" in parsed.path:
            result.append(("!nonportable:" + target, ""))
            continue
        relative = unquote(parsed.path)
        if relative.startswith("/"):
            result.append(("!nonportable:" + target, ""))
            continue
        parts = list(PurePosixPath(path).parent.parts) if relative else []
        for part in PurePosixPath(relative).parts:
            if part == "..":
                if not parts:
                    parts = ["!outside-repository"]
                    break
                parts.pop()
            elif part != ".":
                parts.append(part)
        result.append(("/".join(parts) if relative else path, unquote(parsed.fragment)))
    return result


def audit(root: Path) -> list[str]:
    """Check the indexed candidate plus unstaged drift; return sorted diagnostics."""
    paths = git(root, "ls-files", "-z").decode("utf-8").rstrip("\0").split("\0")
    raw_files = {path: git(root, "show", ":" + path) for path in paths if path}
    errors: list[str] = []
    if COVERAGE not in raw_files:
        return [f"missing coverage ledger: {COVERAGE}"]
    ledger = json.loads(raw_files[COVERAGE])
    if ledger.get("source_binding_basis") != BASIS:
        errors.append("ambiguous source binding basis; exact Git content required")
    rows = ledger["files"]
    indexed = {row["path"]: row for row in rows}
    if len(indexed) != len(rows):
        errors.append("duplicate file coverage rows")
    expected = {path for path in paths if not path.startswith(SELF_OUTPUTS)}
    if set(indexed) != expected:
        errors.append(
            f"inventory mismatch missing={sorted(expected - set(indexed))} "
            f"extra={sorted(set(indexed) - expected)}"
        )
    if ledger.get("audit_status") != "COMPLETE":
        errors.append("semantic audit ledger is not COMPLETE (not a tool verdict)")
    parsed_docs: dict[str, tuple[str, set[str], list[str], list[str]]] = {}
    names, aliases = python_namespaces(raw_files)
    for path, raw in raw_files.items():
        checkout = root.joinpath(*PurePosixPath(path).parts)
        if not checkout.is_file():
            errors.append(f"missing checkout file: {path}")
            continue
        current = checkout.read_bytes()
        if current != raw:
            row = indexed.get(path, {})
            if not (
                row.get("eol_only_difference") is True
                and current.replace(b"\r\n", b"\n") == raw
                and row.get("checkout_sha256") == sha256(current)
            ):
                errors.append(f"unstaged content or undeclared EOL difference: {path}")
        if path.endswith(".md"):
            parsed_docs[path] = markdown(raw.decode("utf-8"))
            errors.extend(f"{path}: {error}" for error in parsed_docs[path][3])
    for path, row in indexed.items():
        if path not in raw_files:
            continue
        raw = raw_files[path]
        if row.get("basis_sha256") != sha256(raw):
            errors.append(f"stale file fingerprint: {path}")
        status = row.get("status")
        if (
            status not in STATUSES
            or status not in COMPLETE
            or not row.get("read_complete")
        ):
            errors.append(f"unresolved semantic review row: {path} ({status})")
        companion = row.get("documentation_path")
        if not companion:
            if not row.get("companion_exception"):
                errors.append(f"missing companion exception: {path}")
            continue
        if companion not in parsed_docs:
            errors.append(f"missing companion: {path} -> {companion}")
            continue
        prose, anchors, blocks, _ = parsed_docs[companion]
        hashes = re.findall(r"^- Source SHA256: `([0-9a-f]{64})`$", prose, re.MULTILINE)
        if hashes != [sha256(raw)]:
            errors.append(f"stale companion hash: {path}")
        bases = re.findall(r"^- Source SHA256 basis: `([^`]+)`$", prose, re.MULTILINE)
        if bases != ["git-content"]:
            errors.append(f"ambiguous companion line-ending basis: {path}")
        if raw.decode("utf-8") not in blocks:
            errors.append(f"missing exact source snapshot: {path}")
        if not path.endswith(".py"):
            continue
        actual = symbol_inventory(raw)
        symbols = row.get("symbols", [])
        wanted = {(item["qualified_name"], item["kind"]): item for item in actual}
        recorded = {(item["qualified_name"], item["kind"]): item for item in symbols}
        if set(wanted) != set(recorded) or len(recorded) != len(symbols):
            errors.append(f"symbol inventory mismatch: {path}")
        for key in sorted(set(wanted) & set(recorded)):
            item, evidence = wanted[key], recorded[key]
            for field in ("range", "signature_sha256"):
                if item[field] != evidence.get(field):
                    errors.append(f"stale symbol {field}: {path}:{key[0]}")
            if evidence.get("status") not in COMPLETE:
                errors.append(f"unresolved symbol review: {path}:{key[0]}")
            if evidence.get("documentation_anchor") not in anchors:
                errors.append(f"missing documented anchor: {path}:{key[0]}")
        declared = exports(raw)
        if declared != row.get("exports"):
            errors.append(f"export inventory mismatch: {path}")
        for name in declared or []:
            if f"`{name}`" not in prose:
                errors.append(f"missing documented export: {path}:{name}")
            module = path.removeprefix("src/").removesuffix(".py").replace("/", ".")
            module = module.removesuffix(".__init__")
            if not resolves_reference(module + "." + name, names, aliases):
                errors.append(f"unresolved export owner: {path}:{name}")
    for path, (prose, _, _, _) in parsed_docs.items():
        exceptions = ledger.get("dynamic_reference_exceptions", [])
        for literal in re.findall(r"`([^`\n]+)`", prose):
            for reference in re.findall(
                r"(?<![\w./])(?:landscout|tests|tools)\.(?:[A-Za-z_]\w*\.)*[A-Za-z_]\w*",
                literal,
            ):
                if not resolves_reference(reference, names, aliases) and not any(
                    item.get("documentation_path") == path
                    and item.get("reference") == reference
                    and item.get("reason")
                    for item in exceptions
                ):
                    errors.append(f"unresolved qualified reference: {path}:{reference}")
        for target, anchor in local_links(path, prose):
            if target not in raw_files and not any(
                name.startswith(target.rstrip("/") + "/") for name in raw_files
            ):
                errors.append(f"bad local link: {path} -> {target}")
            elif (
                anchor
                and target in parsed_docs
                and anchor not in parsed_docs[target][1]
            ):
                errors.append(f"bad local anchor: {path} -> {target}#{anchor}")
    if STEP_LEDGER not in raw_files:
        errors.append("missing step ledger")
    else:
        steps = json.loads(raw_files[STEP_LEDGER])
        step_ids = [step["step_id"] for step in steps["steps"]]
        if len(step_ids) != len(set(step_ids)):
            errors.append("duplicate step IDs")
        known_commits = set(git(root, "rev-list", "--all").decode("ascii").splitlines())
        for step in steps["steps"]:
            for kind in ("dependencies", "corrections", "superseded_by"):
                for target in step.get(kind, []):
                    if target not in step_ids or target == step["step_id"]:
                        errors.append(
                            f"invalid step {kind}: {step['step_id']} -> {target}"
                        )
            for commit in step.get("implementation", {}).get("commits", []):
                if commit not in known_commits:
                    errors.append(
                        f"unknown publication commit: {step['step_id']}:{commit}"
                    )
            if step.get("history_audit_status", "CHECKED") not in COMPLETE:
                errors.append(f"unfinished history audit: {step['step_id']}")
            for evidence in step.get("provenance", []):
                if evidence.startswith("git:"):
                    commit = evidence.split(":")[1]
                    if commit not in known_commits:
                        errors.append(
                            f"unknown history provenance: {step['step_id']}:{commit}"
                        )
                    continue
                target, _, anchor = evidence.partition("#")
                if target not in raw_files:
                    errors.append(f"missing step evidence: {step['step_id']}:{target}")
                elif (
                    anchor
                    and target in parsed_docs
                    and anchor not in parsed_docs[target][1]
                ):
                    errors.append(
                        f"bad step evidence anchor: {step['step_id']}:{evidence}"
                    )
            review = step["review"]
            if review["status"].startswith(("APPROVED", "PARTIAL_REVIEW")):
                if not all(
                    review.get(key) for key in ("source", "commit", "scope", "reviewer")
                ):
                    errors.append(f"missing review provenance: {step['step_id']}")
                elif review["source"].split("#", 1)[0] not in raw_files:
                    errors.append(f"missing review source: {step['step_id']}")
    return sorted(set(errors))


def main(argv: list[str] | None = None) -> int:
    """Print deterministic diagnostics; return zero only for mechanical consistency."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", required=True)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args(argv)
    try:
        errors = audit(args.root.resolve())
    except (
        OSError,
        subprocess.CalledProcessError,
        ValueError,
        KeyError,
        TypeError,
        SyntaxError,
    ) as exc:
        print(f"documentation audit input error: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("\n".join(errors))
        return 1
    print(
        "Documentation mechanics consistent; recorded semantic review is not independent approval."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
````
