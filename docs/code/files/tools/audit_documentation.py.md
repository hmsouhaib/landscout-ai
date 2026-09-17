# `tools/audit_documentation.py`

## File identity

- Repository path: `tools/audit_documentation.py`
- Source SHA256: `5b5aae765c6c32225496d7830e17e83a9bfac89e007949b032b75b13eda3029f`
- Source SHA256 basis: `git-content`
- Scope: DOCS.CONTINUITY.1.R2 tooling only; independent review pending.

## Scope and contracts

Offline, standard-library, read-only Git-index checker, not a LandScout pipeline or semantic reviewer. Run `uv run python tools/audit_documentation.py --check --progress`; `--root` selects the repository. The complete stable-index path uses five Git processes, one AST per Python file and no production imports. Metrics are separate from deterministic findings and manifest identity. The captured manifest is compact JSON of sorted `(path, mode, blob-ID)` triples, not a filesystem/index-file timestamp hash.

The R2 [diagnostic receipt](../../audit/R2_DIAGNOSTICS.md) records the real candidate, observed growing-alias stall and execution limits. Whole-file batches are buffered in memory; there is a finite child deadline, not a universal wall-clock limit for every CPU/file operation. Supported Markdown is intentionally partial; no rendering or global semantic approval follows. Coverage/step records stay authoritative inputs and are never rewritten.

Protocol references: [Git raw batch framing](https://git-scm.com/docs/git-cat-file#_batch_output), [stage entries](https://git-scm.com/docs/git-ls-files#_output), [Python child cleanup](https://docs.python.org/3.12/library/subprocess.html#subprocess.Popen.communicate).

<a id="auditinputerror"></a>

### `AuditInputError`

```python
class AuditInputError(ValueError):
```

ValueError subclass for malformed ledgers/index protocol and invalid timeout. The CLI reports incomplete execution (2), not ordinary findings.

<a id="auditexecutionerror"></a>

### `AuditExecutionError`

```python
class AuditExecutionError(RuntimeError):
```

RuntimeError subclass for Git timeout, cancellation, nonzero exit, launch failure or a changed index. No completed report is fabricated.

<a id="redacted"></a>

### `redacted`

```python
def redacted(text: str) -> str:
```

Replaces URL user-info, token/password/secret/authorization values and URL query/fragment strings, then limits text to 2,000 characters. This is bounded defensive stderr redaction, not a universal secret detector. No environment dump is produced.

<a id="auditrun"></a>

### `AuditRun`

```python
class AuditRun:
```

Single-audit mutable bookkeeping, not an application trust model. Owns root, progress switch, finite timeout, current phase and metrics. It retains no persistent cache and changes no Git configuration.

<a id="auditrun-__init__"></a>

### `AuditRun.__init__`

```python
    def __init__(self, root: Path, progress: bool, timeout: float) -> None:
```

Stores the resolved root supplied by audit, checks a finite timeout strictly greater than zero and at most 300 seconds, and initializes process/phase metrics. Invalid bounds fail before a child is started.

<a id="auditrun-note"></a>

### `AuditRun.note`

```python
    def note(self, message: str) -> None:
```

When progress is enabled, prints a phase-tagged message to stderr with flush=True. Disabled progress does not change evidence or findings.

<a id="auditrun-phase"></a>

### `AuditRun.phase`

```python
    def phase(self, name: str) -> Iterator[None]:
```

Context manager: sets the phase and announces start before yielding; finally records elapsed perf_counter seconds and prints elapsed time even on failure. Timings are metrics only, never manifest inputs.

<a id="auditrun-git"></a>

### `AuditRun.git`

```python
    def git(self, role: str, *args: str, input_bytes: bytes | None = None) -> bytes:
```

Runs explicit argument-vector Git queries with piped input/output, no shell, and a copied environment disabling lazy object fetching, replacement objects and optional locks. communicate has the configured deadline. On timeout or KeyboardInterrupt, kills and drains/reaps the child before raising AuditExecutionError; nonzero exits retain phase/role/return code and redacted stderr. OS launch errors are translated. Call sites are read-only ls-files, cat-file, rev-list and rev-parse; this helper is not a general Git command allowlist. The process counter counts launch attempts; successful-run tests additionally count actual Popen calls.

<a id="sha256"></a>

### `sha256`

```python
def sha256(raw: bytes) -> str:
```

Hashes exact bytes with SHA256, with no Git envelope or Python repr. Returns a lowercase hexadecimal digest.

<a id="canonical_path"></a>

### `canonical_path`

```python
def canonical_path(path: str) -> bool:
```

Accepts nonempty portable relative paths, including spaces/Unicode. Rejects control characters, backslashes, colon, fragment/query/percent syntax, leading slash and empty/dot/parent/.git components. Deliberately narrower than all possible Git filenames; unsupported candidates fail explicitly.

<a id="read_index"></a>

### `read_index`

```python
def read_index(run: AuditRun) -> tuple[dict[str, bytes], bytes]:
```

Captures ls-files --stage -z entries; requires unique canonical UTF-8 stage-zero paths and regular modes 100644/100755. Conflicts, symlinks, submodules and malformed records fail before checkout-content reads. Sorts (path, mode, blob-ID) triples and hashes their ensure_ascii=True compact JSON UTF-8 representation. Deduplicates/sorts IDs, sends them to one raw cat-file --batch process, then parses each header and declared BYTE length plus terminator. Rejects missing objects, wrong IDs/types/sizes, truncation and trailing data. Empty, binary/multiline, space and Unicode inputs are preserved. Returns exact per-path bytes plus the captured enumeration for the final postcondition. No textconv/smudge or symlink-following option is used.

<a id="symbol_inventory"></a>

### `symbol_inventory`

```python
def symbol_inventory(
    raw: bytes, tree: ast.Module | None = None
) -> list[dict[str, Any]]:
```

Decodes UTF-8 and walks a supplied AST, or parses once for a standalone call. Records lexical qualified names, kinds, line ranges and exact signature SHA256 without importing production. Definition header extraction and ast.get_source_segment for annotated fields retain their previous meaning. No offset rewrite was necessary: profiling localized the stall to alias resolution, not annotation extraction.

<a id="symbol_inventory-visitor"></a>

### `symbol_inventory.Visitor`

```python
    class Visitor(ast.NodeVisitor):
```

Lexical AST traversal local to one inventory call. Its mutable scope stack and output list are transient audit implementation state.

<a id="symbol_inventory-visitor-__init__"></a>

### `symbol_inventory.Visitor.__init__`

```python
        def __init__(self) -> None:
```

Starts the empty lexical scope stack; it is not shared across files.

<a id="symbol_inventory-visitor-definition"></a>

### `symbol_inventory.Visitor.definition`

```python
        def definition(
            self, node: ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef, kind: str
        ) -> None:
```

Records the definition header up to the first body statement and its full AST range, then pushes the name. For a class, records each direct AnnAssign with a Name target using the exact source segment; recursively visits nested definitions and finally pops scope. Dynamic fields, decorators and inherited members are not inferred.

<a id="symbol_inventory-visitor-visit_functiondef"></a>

### `symbol_inventory.Visitor.visit_FunctionDef`

```python
        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
```

Delegates synchronous functions to definition with kind function.

<a id="symbol_inventory-visitor-visit_asyncfunctiondef"></a>

### `symbol_inventory.Visitor.visit_AsyncFunctionDef`

```python
        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
```

Delegates asynchronous functions to definition with kind function; never executes a coroutine.

<a id="symbol_inventory-visitor-visit_classdef"></a>

### `symbol_inventory.Visitor.visit_ClassDef`

```python
        def visit_ClassDef(self, node: ast.ClassDef) -> None:
```

Delegates classes to definition with kind class, enabling direct annotated-field records.

<a id="exports"></a>

### `exports`

```python
def exports(raw: bytes, tree: ast.Module | None = None) -> list[str] | None:
```

Uses a supplied AST (or parses for a standalone call), inspects module-level Assign to __all__, literal-evaluates and requires a list/tuple of exact strings. Returns a copied list or None when absent. Dynamic declarations fail; annotated/runtime-changing exports are outside this limited inventory.

<a id="python_namespaces"></a>

### `python_namespaces`

```python
def python_namespaces(
    raw_files: dict[str, bytes],
    facts: dict[str, tuple[ast.Module, list[dict[str, Any]]]] | None = None,
) -> tuple[set[str], dict[str, str]]:
```

Derives module/package names from Python paths, removes src/__init__, includes lexical symbols and top-level assigned names, and records normal/relative import aliases. During audit it reuses each file's (AST, inventory) pair; standalone use parses each file once. Does not execute imports, infer instance types or resolve wildcard/dynamic members.

<a id="resolves_reference"></a>

### `resolves_reference`

```python
def resolves_reference(
    reference: str, names: set[str], aliases: dict[str, str]
) -> bool:
```

Checks static names, then rewrites the longest matching alias prefix. Tracks both entire references and already-applied alias prefixes, so growing cycles terminate False rather than allocating ever-longer names indefinitely. A same-name module/function reexport can leave dynamic members unresolved; the checker reports that limitation, not inferred ownership. Successful resolution is static structural evidence only.

<a id="markdown"></a>

### `markdown`

```python
def markdown(text: str) -> tuple[str, set[str], list[str], list[str]]:
```

Separates supported fenced blocks from prose; backtick/tilde closing runs must match character, meet opening length and have no trailing text. Reports malformed/unclosed fences. Collects explicit HTML id/name anchors and simplified ATX heading slugs. All generated IDs are tracked: a/a/a-1 yields a, a-1, a-1-1. Explicit anchor handling is retained separately; this is not a full DOM uniqueness validator, renderer or GFM implementation.

<a id="local_links"></a>

### `local_links`

```python
def local_links(path: str, prose: str) -> list[tuple[str, str]]:
```

Extracts simple inline Markdown/HTML href links outside fences; skips HTTP/HTTPS/mailto without crawling. Rejects schemes/netlocs, absolute paths and literal/decoded backslashes, then resolves relative parent components without escaping the repository. Returns decoded path/anchor targets. Reference-style links, dynamic constructs and complete CommonMark syntax remain outside scope.

<a id="load_ledger"></a>

### `load_ledger`

```python
def load_ledger(raw: bytes, path: str) -> dict[str, Any]:
```

Strict JSON decoder for coverage/step records. Rejects duplicate object keys at any nesting, NaN/Infinity and finite-literal overflow; requires an object root. Syntax, Unicode and recursion failures become contextual AuditInputError. Unknown unconsumed documentary fields are not treated as semantic proof.

<a id="load_ledger-pairs"></a>

### `load_ledger.pairs`

```python
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
```

Builds each decoded object once, rejecting a repeated key instead of accepting the later value.

<a id="load_ledger-constant"></a>

### `load_ledger.constant`

```python
    def constant(value: str) -> Any:
```

Rejects JSON non-finite constants with the ledger path and value.

<a id="load_ledger-floating"></a>

### `load_ledger.floating`

```python
    def floating(value: str) -> float:
```

Parses floating literals and rejects nonfinite overflow such as 1e999.

<a id="require"></a>

### `require`

```python
def require(value: Any, expected: type, context: str) -> None:
```

Checks exact JSON types before operations; bool does not pass as int. Wrong or absent required members produce contextual input errors rather than incidental AttributeError/TypeError.

<a id="string_list"></a>

### `string_list`

```python
def string_list(value: Any, context: str) -> None:
```

Requires a list and validates each element as an exact string, with element index in errors.

<a id="validate_coverage"></a>

### `validate_coverage`

```python
def validate_coverage(ledger: dict[str, Any]) -> None:
```

Validates consumed root/file/symbol/exception fields. Requires basis/status strings, files list, canonical row paths, hashes/status strings and exact read_complete bool; validates nullable documentary strings, optional EOL bool and string exports. Python rows require symbol lists; symbols require names/kind/hash/status and positive ordered two-int line ranges. Missing anchors/companion claims remain review findings, not invented facts. Dynamic-reference exceptions require string path/reference/reason fields.

<a id="validate_steps"></a>

### `validate_steps`

```python
def validate_steps(ledger: dict[str, Any]) -> None:
```

Requires a steps list, object records, string IDs and review-status strings. Checks dependency/correction/supersession/provenance string lists, implementation object/commit list, optional history-status string, and nullable review source/commit/scope/reviewer strings. Missing history is deliberately not defaulted to CHECKED; missing approval evidence is diagnosed later.

<a id="evidence_problem"></a>

### `evidence_problem`

```python
def evidence_problem(
    evidence: str,
    raw_files: dict[str, bytes],
    parsed_docs: dict[str, tuple[str, set[str], list[str], list[str]]],
) -> str | None:
```

Validates a canonical root-relative receipt file against indexed bytes and any supplied nonempty Markdown anchor against parsed indexed prose. Rejects malformed paths, missing files, empty/multiple fragment syntax and anchors on non-Markdown files. Returns a problem label or None; no filesystem/network receipt lookup or semantic approval.

<a id="audit"></a>

### `audit`

```python
def audit(
    root: Path,
    *,
    progress: bool = False,
    git_timeout: float = 30,
    metrics: dict[str, Any] | None = None,
) -> list[str]:
```

Creates per-call state and announces root/basis under --progress. Reads one captured index, runs candidate checks, then re-enumerates the index and rejects any changed stage entries. Only after this postcondition sets completed=True and returns sorted findings. Optional metrics receives observations even on failure. A stable captured manifest identifies the candidate; no whole-worktree atomic snapshot or transient index ABA detection is claimed.

<a id="audit_candidate"></a>

### `audit_candidate`

```python
def audit_candidate(run: AuditRun, raw_files: dict[str, bytes]) -> list[str]:
```

Runs named coverage-input, python, checkout-markdown, coverage, references and history phases. Parses each Python file once for inventories, namespaces and exports. Checks indexed Markdown even if checkout is missing; reports checkout drift except an explicitly SHA-locked CRLF-only exception and avoids external checkout links. Verifies file/symbol fingerprint/status/read evidence, companions/basis/snapshots/anchors, exports/owners, simple local links and static qualified references. Strictly validates steps, checks local reachable commit IDs and offline shallow-history limits, and diagnoses absent/incomplete history. APPROVED*/PARTIAL_REVIEW* require exact nonempty reviewer/source/scope/commit, a known commit and a valid file/anchor. Pending records are never rewritten. Missing required ledgers abort with input error rather than a completed audit.

<a id="main"></a>

### `main`

```python
def main(argv: list[str] | None = None) -> int:
```

Retains required --check and optional --root; adds --progress and --git-timeout (default 30 s, finite 0<value<=300). Prints sorted findings to stdout and final metrics to stderr (including failure observations). Exit 0 means no required mechanical/recorded findings, not independent approval; 1 means a finished audit with findings; 2 means input/operational failure or interruption. argparse retains its own argument-error exit. __main__ returns the native process code.

## Effects, limits and maintenance

Only local Git queries, filesystem reads and stdout/stderr are intended auditor effects. The helper does not enforce all future caller command verbs; review its call sites when changing it. Local reachable history and accessible files/anchors prove structural provenance, not that a named reviewer approved every claim. Source-byte identity does not establish explanatory fidelity, legal/business meaning, dynamic ownership, full GFM conformance or a visual audit. Refresh this companion and the paired test companion after edits; global coverage integration remains deferred under R2.

## Complete exact source snapshot

````python
"""Offline, read-only checks of Git-index documentation evidence, not semantic approval."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import time
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import unquote, urlsplit

BASIS = "SHA256_OF_EXACT_GIT_CONTENT_BYTES"
COMPLETE = {"CHECKED", "CORRECTED"}
STATUSES = COMPLETE | {"NOT_READ", "READ", "BLOCKED"}
COVERAGE = "docs/code/audit/coverage.json"
STEP_LEDGER = "docs/project/STEP_LEDGER.json"
SELF_OUTPUTS = "docs/code/audit/"


class AuditInputError(ValueError):
    """Malformed evidence prevents a complete trustworthy audit."""


class AuditExecutionError(RuntimeError):
    """An operational failure prevents a complete trustworthy audit."""


def redacted(text: str) -> str:
    """Bound stderr and remove URL credentials, query secrets and auth tokens."""
    text = re.sub(r"(?i)\b(Bearer|Basic)\s+[^\s]+", r"\1 [REDACTED]", text)
    text = re.sub(r"(https?://)[^\s/@]+@", r"\1[REDACTED]@", text)
    text = re.sub(
        r"(?i)(token|password|secret|authorization)([=: ]+)[^\s]+",
        r"\1\2[REDACTED]",
        text,
    )
    text = re.sub(r"(https?://[^\s?#]+)[?#][^\s]+", r"\1?[REDACTED]", text)
    return text[:2000]


class AuditRun:
    """Per-call progress, timings and bounded read-only Git operations."""

    def __init__(self, root: Path, progress: bool, timeout: float) -> None:
        if not math.isfinite(timeout) or timeout <= 0 or timeout > 300:
            raise AuditInputError("Git timeout must be finite, > 0 and <= 300 seconds")
        self.root = root
        self.progress = progress
        self.timeout = timeout
        self.phase_name = "initialization"
        self.metrics: dict[str, Any] = {
            "root": str(root),
            "basis": BASIS,
            "git_processes": 0,
            "phase_seconds": {},
        }

    def note(self, message: str) -> None:
        if self.progress:
            print(f"[{self.phase_name}] {message}", file=sys.stderr, flush=True)

    @contextmanager
    def phase(self, name: str) -> Iterator[None]:
        self.phase_name = name
        self.note("start")
        started = time.perf_counter()
        try:
            yield
        finally:
            elapsed = time.perf_counter() - started
            self.metrics["phase_seconds"][name] = elapsed
            self.note(f"elapsed={elapsed:.6f}s")

    def git(self, role: str, *args: str, input_bytes: bytes | None = None) -> bytes:
        self.note(f"Git {role}")
        self.metrics["git_processes"] += 1
        env = dict(
            os.environ,
            GIT_NO_LAZY_FETCH="1",
            GIT_NO_REPLACE_OBJECTS="1",
            GIT_OPTIONAL_LOCKS="0",
        )
        try:
            with subprocess.Popen(
                ["git", "-C", str(self.root), *args],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=env,
            ) as child:
                try:
                    output, stderr = child.communicate(
                        input_bytes, timeout=self.timeout
                    )
                except (subprocess.TimeoutExpired, KeyboardInterrupt) as exc:
                    child.kill()
                    _, stderr = child.communicate()
                    reason = (
                        "timeout"
                        if isinstance(exc, subprocess.TimeoutExpired)
                        else "cancelled"
                    )
                    raise AuditExecutionError(
                        f"{self.phase_name}: Git {role} {reason}; {redacted(stderr.decode('utf-8', errors='replace'))}"
                    ) from exc
                if child.returncode:
                    raise AuditExecutionError(
                        f"{self.phase_name}: Git {role} exit {child.returncode}; {redacted(stderr.decode('utf-8', errors='replace'))}"
                    )
                return output
        except OSError as exc:
            raise AuditExecutionError(
                f"{self.phase_name}: Git {role}: {redacted(str(exc))}"
            ) from exc


def sha256(raw: bytes) -> str:
    """Hash content bytes, never Git's blob envelope or a Python representation."""
    return hashlib.sha256(raw).hexdigest()


def canonical_path(path: str) -> bool:
    """Require an exact repository-relative portable file path, not a URL."""
    return (
        bool(path)
        and not any(ord(c) < 32 for c in path)
        and not any(c in path for c in "\\:#?%")
        and not path.startswith("/")
        and all(part not in {"", ".", "..", ".git"} for part in path.split("/"))
    )


def read_index(run: AuditRun) -> tuple[dict[str, bytes], bytes]:
    """Capture stage-0 IDs, then read raw blobs in one length-framed batch."""
    snapshot = run.git("index enumeration", "ls-files", "--stage", "-z")
    entries: list[tuple[str, str, str]] = []
    for entry in snapshot.split(b"\0"):
        if not entry:
            continue
        match = re.fullmatch(
            rb"(\d{6}) ([0-9a-f]{40}|[0-9a-f]{64}) ([0-3])\t(.+)", entry, re.DOTALL
        )
        if not match:
            raise AuditInputError("index: malformed stage entry")
        mode, oid, stage, raw_path = match.groups()
        path = raw_path.decode("utf-8")
        if stage != b"0":
            raise AuditInputError(f"index: unmerged stage {stage.decode()}: {path}")
        if mode not in {b"100644", b"100755"}:
            raise AuditInputError(f"index: unsupported mode {mode.decode()}: {path}")
        if not canonical_path(path):
            raise AuditInputError(f"index: noncanonical path: {path!r}")
        entries.append((path, mode.decode(), oid.decode()))
    if len({entry[0] for entry in entries}) != len(entries):
        raise AuditInputError("index: duplicate paths")
    entries.sort()
    run.metrics["manifest_sha256"] = sha256(
        json.dumps(entries, ensure_ascii=True, separators=(",", ":")).encode()
    )
    oids = sorted({entry[2] for entry in entries})
    batch = run.git(
        "raw blob batch",
        "cat-file",
        "--batch",
        input_bytes="".join(oid + "\n" for oid in oids).encode("ascii"),
    )
    blobs: dict[str, bytes] = {}
    offset = 0
    for oid in oids:
        end = batch.find(b"\n", offset)
        header = batch[offset:end] if end >= 0 else b""
        match = re.fullmatch(oid.encode() + rb" blob (0|[1-9][0-9]*)", header)
        if not match:
            raise AuditInputError(f"blob batch: missing/malformed header for {oid}")
        size = int(match[1])
        start = end + 1
        offset = start + size
        if batch[offset : offset + 1] != b"\n":
            raise AuditInputError(f"blob batch: truncated content for {oid}")
        blobs[oid] = batch[start:offset]
        offset += 1
    if offset != len(batch):
        raise AuditInputError("blob batch: unexpected trailing bytes")
    files = {path: blobs[oid] for path, _, oid in entries}
    run.metrics.update(
        files=len(files), bytes=sum(map(len, files.values())), unique_blobs=len(blobs)
    )
    return files, snapshot


def symbol_inventory(
    raw: bytes, tree: ast.Module | None = None
) -> list[dict[str, Any]]:
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

    Visitor().visit(tree if tree is not None else ast.parse(source))
    return found


def exports(raw: bytes, tree: ast.Module | None = None) -> list[str] | None:
    """Return a literal module-level __all__, rejecting dynamic declarations."""
    for node in (tree if tree is not None else ast.parse(raw.decode("utf-8"))).body:
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


def python_namespaces(
    raw_files: dict[str, bytes],
    facts: dict[str, tuple[ast.Module, list[dict[str, Any]]]] | None = None,
) -> tuple[set[str], dict[str, str]]:
    """Inventory static Python ownership and import aliases, without execution."""
    names: set[str] = set()
    aliases: dict[str, str] = {}
    for path, raw in raw_files.items():
        if not path.endswith(".py"):
            continue
        if facts is None:
            tree = ast.parse(raw.decode("utf-8"))
            symbols = symbol_inventory(raw, tree)
        else:
            tree, symbols = facts[path]
        parts = list(PurePosixPath(path).with_suffix("").parts)
        if parts[0] == "src":
            parts.pop(0)
        package = parts[-1] == "__init__"
        if package:
            parts.pop()
        module = ".".join(parts)
        names.update(".".join(parts[:end]) for end in range(1, len(parts) + 1))
        for symbol in symbols:
            names.add(module + "." + symbol["qualified_name"])
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
    rewritten: set[str] = set()
    while reference not in seen:
        seen.add(reference)
        if reference in names:
            return True
        parts = reference.split(".")
        for end in range(len(parts), 0, -1):
            prefix = ".".join(parts[:end])
            if prefix in aliases:
                if prefix in rewritten:
                    return False
                rewritten.add(prefix)
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
    generated: set[str] = set()
    for line in outside.splitlines():
        heading = re.match(r"^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?$", line)
        if heading:
            label = re.sub(r"<[^>]*>", "", heading[1]).lower()
            slug = re.sub(r"[^\w\- ]", "", label, flags=re.UNICODE).replace(" ", "-")
            candidate = slug
            ordinal = 0
            while candidate in generated:
                ordinal += 1
                candidate = f"{slug}-{ordinal}"
            generated.add(candidate)
            anchors.add(candidate)
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
        if relative.startswith("/") or "\\" in relative:
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


def load_ledger(raw: bytes, path: str) -> dict[str, Any]:
    """Decode strict JSON; reject duplicate keys and all non-finite numbers."""

    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            if key in result:
                raise AuditInputError(f"{path}: duplicate JSON key {key!r}")
            result[key] = value
        return result

    def constant(value: str) -> Any:
        raise AuditInputError(f"{path}: non-finite JSON value {value}")

    def floating(value: str) -> float:
        parsed = float(value)
        if not math.isfinite(parsed):
            constant(value)
        return parsed

    try:
        value = json.loads(
            raw, object_pairs_hook=pairs, parse_constant=constant, parse_float=floating
        )
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise AuditInputError(f"{path}: {exc}") from exc
    require(value, dict, path)
    return value  # type: ignore[no-any-return]


def require(value: Any, expected: type, context: str) -> None:
    """Check exact JSON shapes before using mappings, iterables or scalars."""
    if type(value) is not expected:
        raise AuditInputError(
            f"{context}: expected {expected.__name__}, got {type(value).__name__}"
        )


def string_list(value: Any, context: str) -> None:
    require(value, list, context)
    for i, item in enumerate(value):
        require(item, str, f"{context}[{i}]")


def validate_coverage(ledger: dict[str, Any]) -> None:
    """Validate consumed coverage shapes; missing review evidence stays a finding."""
    for key in ("source_binding_basis", "audit_status"):
        require(ledger.get(key), str, f"{COVERAGE}.{key}")
    require(ledger.get("files"), list, f"{COVERAGE}.files")
    for i, row in enumerate(ledger["files"]):
        context = f"{COVERAGE}.files[{i}]"
        require(row, dict, context)
        for key in ("path", "basis_sha256", "status"):
            require(row.get(key), str, f"{context}.{key}")
        if not canonical_path(row["path"]):
            raise AuditInputError(f"{context}.path: noncanonical path")
        require(row.get("read_complete"), bool, f"{context}.read_complete")
        for key in ("documentation_path", "companion_exception", "checkout_sha256"):
            if row.get(key) is not None:
                require(row[key], str, f"{context}.{key}")
        if row.get("documentation_path") and not canonical_path(
            row["documentation_path"]
        ):
            raise AuditInputError(f"{context}.documentation_path: noncanonical path")
        if "eol_only_difference" in row:
            require(row["eol_only_difference"], bool, f"{context}.eol_only_difference")
        if row.get("exports") is not None:
            string_list(row["exports"], f"{context}.exports")
        symbols = row.get("symbols", [] if not row["path"].endswith(".py") else None)
        require(symbols, list, f"{context}.symbols")
        for j, item in enumerate(symbols):
            location = f"{context}.symbols[{j}]"
            require(item, dict, location)
            for key in ("qualified_name", "kind", "signature_sha256", "status"):
                require(item.get(key), str, f"{location}.{key}")
            require(item.get("range"), list, f"{location}.range")
            if (
                len(item["range"]) != 2
                or any(type(n) is not int or n < 1 for n in item["range"])
                or item["range"][1] < item["range"][0]
            ):
                raise AuditInputError(
                    f"{location}.range: expected positive ordered line pair"
                )
            if item.get("documentation_anchor") is not None:
                require(
                    item["documentation_anchor"],
                    str,
                    f"{location}.documentation_anchor",
                )
    exceptions = ledger.get("dynamic_reference_exceptions", [])
    require(exceptions, list, f"{COVERAGE}.dynamic_reference_exceptions")
    for i, item in enumerate(exceptions):
        context = f"{COVERAGE}.dynamic_reference_exceptions[{i}]"
        require(item, dict, context)
        for key in ("documentation_path", "reference", "reason"):
            require(item.get(key), str, f"{context}.{key}")


def validate_steps(ledger: dict[str, Any]) -> None:
    """Validate consumed step/review/provenance shapes without inventing approval."""
    require(ledger.get("steps"), list, f"{STEP_LEDGER}.steps")
    for i, step in enumerate(ledger["steps"]):
        context = f"{STEP_LEDGER}.steps[{i}]"
        require(step, dict, context)
        require(step.get("step_id"), str, f"{context}.step_id")
        for key in ("dependencies", "corrections", "superseded_by", "provenance"):
            string_list(step.get(key, []), f"{context}.{key}")
        implementation = step.get("implementation", {})
        require(implementation, dict, f"{context}.implementation")
        string_list(
            implementation.get("commits", []), f"{context}.implementation.commits"
        )
        if "history_audit_status" in step:
            require(
                step["history_audit_status"], str, f"{context}.history_audit_status"
            )
        review = step.get("review")
        require(review, dict, f"{context}.review")
        require(review.get("status"), str, f"{context}.review.status")
        for key in ("reviewer", "source", "scope", "commit"):
            if review.get(key) is not None:
                require(review[key], str, f"{context}.review.{key}")


def evidence_problem(
    evidence: str,
    raw_files: dict[str, bytes],
    parsed_docs: dict[str, tuple[str, set[str], list[str], list[str]]],
) -> str | None:
    """Check canonical root-relative receipt path and an optional Markdown anchor."""
    target, separator, anchor = evidence.partition("#")
    if not canonical_path(target) or (separator and (not anchor or "#" in anchor)):
        return "noncanonical evidence path"
    if target not in raw_files:
        return "missing evidence file"
    if separator and (
        target not in parsed_docs or anchor not in parsed_docs[target][1]
    ):
        return "bad evidence anchor"
    return None


def audit(
    root: Path,
    *,
    progress: bool = False,
    git_timeout: float = 30,
    metrics: dict[str, Any] | None = None,
) -> list[str]:
    """Check a captured index plus checkout drift; incomplete execution raises."""
    run = AuditRun(root.resolve(), progress, git_timeout)
    run.note(f"root={run.root} basis={BASIS}")
    try:
        with run.phase("index"):
            raw_files, snapshot = read_index(run)
        errors = audit_candidate(run, raw_files)
        with run.phase("index-postcondition"):
            if run.git("index postcondition", "ls-files", "--stage", "-z") != snapshot:
                raise AuditExecutionError(
                    "index-postcondition: index changed during audit; rerun on a stable candidate"
                )
        run.metrics["findings"] = len(errors)
        run.metrics["completed"] = True
        return errors
    finally:
        if metrics is not None:
            metrics.update(run.metrics)


def audit_candidate(run: AuditRun, raw_files: dict[str, bytes]) -> list[str]:
    """Check one captured index candidate; never promote or rewrite its ledgers."""
    root = run.root
    paths = list(raw_files)
    errors: list[str] = []
    if COVERAGE not in raw_files:
        raise AuditInputError(f"missing coverage ledger: {COVERAGE}")
    with run.phase("coverage-input"):
        ledger = load_ledger(raw_files[COVERAGE], COVERAGE)
        validate_coverage(ledger)
        run.metrics["coverage_files"] = len(ledger["files"])
        run.metrics["coverage_symbols"] = sum(
            len(row.get("symbols", [])) for row in ledger["files"]
        )
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
    facts: dict[str, tuple[ast.Module, list[dict[str, Any]]]] = {}
    with run.phase("python"):
        for path, raw in raw_files.items():
            if path.endswith(".py"):
                run.note(path)
                try:
                    tree = ast.parse(raw.decode("utf-8"), filename=path)
                    facts[path] = (tree, symbol_inventory(raw, tree))
                except (SyntaxError, ValueError) as exc:
                    raise AuditInputError(f"{path}: {exc}") from exc
        names, aliases = python_namespaces(raw_files, facts)
        run.metrics["python_files"] = len(facts)
        run.metrics["ast_parses"] = len(facts)
        run.metrics["symbols"] = sum(len(items) for _, items in facts.values())
    with run.phase("checkout-markdown"):
        for path, raw in raw_files.items():
            if path.endswith(".md"):
                parsed_docs[path] = markdown(raw.decode("utf-8"))
                errors.extend(f"{path}: {error}" for error in parsed_docs[path][3])
            checkout = root.joinpath(*PurePosixPath(path).parts)
            if not checkout.is_file():
                errors.append(f"missing checkout file: {path}")
                continue
            if checkout.is_symlink() or not checkout.resolve().is_relative_to(root):
                errors.append(f"unsafe checkout link: {path}")
                continue
            current = checkout.read_bytes()
            if current != raw:
                row = indexed.get(path, {})
                if not (
                    row.get("eol_only_difference") is True
                    and current.replace(b"\r\n", b"\n") == raw
                    and row.get("checkout_sha256") == sha256(current)
                ):
                    errors.append(
                        f"unstaged content or undeclared EOL difference: {path}"
                    )
    with run.phase("coverage"):
        for path, row in indexed.items():
            run.note(path)
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
            hashes = re.findall(
                r"^- Source SHA256: `([0-9a-f]{64})`$", prose, re.MULTILINE
            )
            if hashes != [sha256(raw)]:
                errors.append(f"stale companion hash: {path}")
            bases = re.findall(
                r"^- Source SHA256 basis: `([^`]+)`$", prose, re.MULTILINE
            )
            if bases != ["git-content"]:
                errors.append(f"ambiguous companion line-ending basis: {path}")
            if raw.decode("utf-8") not in blocks:
                errors.append(f"missing exact source snapshot: {path}")
            if not path.endswith(".py"):
                continue
            actual = facts[path][1]
            symbols = row.get("symbols", [])
            wanted = {(item["qualified_name"], item["kind"]): item for item in actual}
            recorded = {
                (item["qualified_name"], item["kind"]): item for item in symbols
            }
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
            declared = exports(raw, facts[path][0])
            if declared != row.get("exports"):
                errors.append(f"export inventory mismatch: {path}")
            for name in declared or []:
                if f"`{name}`" not in prose:
                    errors.append(f"missing documented export: {path}:{name}")
                module = path.removeprefix("src/").removesuffix(".py").replace("/", ".")
                module = module.removesuffix(".__init__")
                if not resolves_reference(module + "." + name, names, aliases):
                    errors.append(f"unresolved export owner: {path}:{name}")
    with run.phase("references"):
        for path, (prose, _, _, _) in parsed_docs.items():
            run.note(path)
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
                        errors.append(
                            f"unresolved qualified reference: {path}:{reference}"
                        )
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
    with run.phase("history"):
        if STEP_LEDGER not in raw_files:
            raise AuditInputError(f"missing step ledger: {STEP_LEDGER}")
        else:
            steps = load_ledger(raw_files[STEP_LEDGER], STEP_LEDGER)
            validate_steps(steps)
            step_ids = [step["step_id"] for step in steps["steps"]]
            if len(step_ids) != len(set(step_ids)):
                errors.append("duplicate step IDs")
            known_commits = set(
                run.git("available history", "rev-list", "--all")
                .decode("ascii")
                .splitlines()
            )
            shallow = (
                run.git("history scope", "rev-parse", "--is-shallow-repository").strip()
                == b"true"
            )
            run.metrics["shallow_history"] = shallow
            history_limit = (
                "unavailable in local history (shallow repository)"
                if shallow
                else "unavailable in local reachable history"
            )
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
                            f"unknown publication commit: {step['step_id']}:{commit} ({history_limit})"
                        )
                if step.get("history_audit_status") not in COMPLETE:
                    errors.append(f"unfinished history audit: {step['step_id']}")
                for evidence in step.get("provenance", []):
                    if evidence.startswith("git:"):
                        commit = evidence.split(":")[1]
                        if commit not in known_commits:
                            errors.append(
                                f"unknown history provenance: {step['step_id']}:{commit} ({history_limit})"
                            )
                        continue
                    problem = evidence_problem(evidence, raw_files, parsed_docs)
                    if problem:
                        errors.append(
                            f"missing step evidence: {step['step_id']}:{evidence} ({problem})"
                        )
                review = step["review"]
                if review["status"].startswith(("APPROVED", "PARTIAL_REVIEW")):
                    if not all(
                        type(review.get(key)) is str
                        and bool(review[key])
                        and review[key] == review[key].strip()
                        for key in ("source", "commit", "scope", "reviewer")
                    ):
                        errors.append(f"missing review provenance: {step['step_id']}")
                    else:
                        if review["commit"] not in known_commits:
                            errors.append(
                                f"unknown review commit: {step['step_id']}:{review['commit']} ({history_limit})"
                            )
                        problem = evidence_problem(
                            review["source"], raw_files, parsed_docs
                        )
                        if problem:
                            errors.append(
                                f"invalid review source: {step['step_id']}:{review['source']} ({problem})"
                            )
    return sorted(set(errors))


def main(argv: list[str] | None = None) -> int:
    """Print deterministic diagnostics; return zero only for mechanical consistency."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", required=True)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument(
        "--progress", action="store_true", help="flush phase/file progress to stderr"
    )
    parser.add_argument(
        "--git-timeout",
        type=float,
        default=30,
        help="Git operation timeout in seconds (0 < value <= 300)",
    )
    args = parser.parse_args(argv)
    metrics: dict[str, Any] = {}
    try:
        errors = audit(
            args.root.resolve(),
            progress=args.progress,
            git_timeout=args.git_timeout,
            metrics=metrics,
        )
    except (
        OSError,
        AuditExecutionError,
        KeyboardInterrupt,
        ValueError,
        SyntaxError,
    ) as exc:
        print(
            f"documentation audit input error/execution failure: {redacted(str(exc))}",
            file=sys.stderr,
            flush=True,
        )
        return 2
    finally:
        print(
            "audit metrics: " + json.dumps(metrics, sort_keys=True),
            file=sys.stderr,
            flush=True,
        )
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
