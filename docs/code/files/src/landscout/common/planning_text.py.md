# `src/landscout/common/planning_text.py`

## File identity

- Repository path: `src/landscout/common/planning_text.py`
- File type: Python source
- Layer: internal common contract
- Domain: planning
- Responsibility: Normalizes planning text for deterministic matching while retaining mappings back to raw source spans.
- Source SHA256: `1e4d6ec3de5914174eaa053c2c6afdf700ab00bfd6d96db98281a1991f7eae80`

## 1. Purpose

Normalizes planning text for deterministic matching while retaining mappings back to raw source spans.

## 2. Position in LandScout architecture

This file belongs to the **internal common contract** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import unicodedata`

### Third-party packages

- `None.`

### Internal LandScout imports

- `None.`

## 4. Contract taxonomy

### A. Python constants

#### `SEARCH_NORMALIZATION_PROFILE`

```python
SEARCH_NORMALIZATION_PROFILE = "fr_literal_v1"
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_APOSTROPHES`

```python
_APOSTROPHES = frozenset("'’‘ʼ‛＇ꞌ")
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/common/planning_text.py::normalize_planning_search_text_with_mapping` (value reference).

#### `_DASHES`

```python
_DASHES = frozenset("-‐‑‒–—―−﹘﹣－")
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/common/planning_text.py::normalize_planning_search_text_with_mapping` (value reference).

#### `_SPECIAL_EXPANSIONS`

```python
_SPECIAL_EXPANSIONS = {"œ": "oe", "Œ": "oe", "æ": "ae", "Æ": "ae"}
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/common/planning_text.py::normalize_planning_search_text_with_mapping` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `normalize_planning_search_text_with_mapping`

**Exact signature**

```python
def normalize_planning_search_text_with_mapping(
    value: str,
) -> tuple[str, tuple[tuple[int, int], ...]]:
```

**Purpose**

Normalize literal-search text and map each output character to a raw span.

**Return contract**

- Declared return annotation: `tuple[str, tuple[tuple[int, int], ...]]`.
- Every observed return expression is reproduced without truncation:
```python
(''.join(output), tuple(raw_spans))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `emitted`, `output`, `raw_spans`, `raw_spans[-1]`.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `src/landscout/stages/structure_planning_regulation.py::<module>` via `from landscout.common.planning_text import (
    normalize_planning_search_text,
    normalize_planning_search_text_with_mapping,
    raw_context_from_spans,
)`.
- direct call: `src/landscout/common/planning_text.py::normalize_planning_search_text` via `normalize_planning_search_text_with_mapping`.

**Complete source-ordered implementation**

```python
def normalize_planning_search_text_with_mapping(
    value: str,
) -> tuple[str, tuple[tuple[int, int], ...]]:
    """Normalize literal-search text and map each output character to a raw span."""

    output: list[str] = []
    raw_spans: list[tuple[int, int]] = []
    pending_space_span: tuple[int, int] | None = None
    pending_ignored_start: int | None = None
    raw_position = 0
    while raw_position < len(value):
        raw_character = value[raw_position]
        if raw_character == "\u00ad":
            if raw_spans:
                previous_start, _ = raw_spans[-1]
                raw_spans[-1] = (previous_start, raw_position + 1)
            if pending_ignored_start is None:
                pending_ignored_start = raw_position
            raw_position += 1
            continue
        raw_end = raw_position + 1
        while raw_end < len(value) and unicodedata.combining(value[raw_end]):
            raw_end += 1
        cluster = value[raw_position:raw_end]
        expanded = _SPECIAL_EXPANSIONS.get(raw_character, raw_character)
        emitted: list[str] = []
        for character in unicodedata.normalize("NFKD", expanded + cluster[1:]):
            if unicodedata.combining(character):
                continue
            if character in _APOSTROPHES:
                folded = "'"
            elif character in _DASHES:
                folded = "-"
            else:
                folded = character.casefold()
            emitted.extend(folded)
        if not emitted:
            raw_position = raw_end
            continue
        if all(character.isspace() for character in emitted):
            if output:
                if pending_space_span is None:
                    pending_space_span = (raw_position, raw_end)
                else:
                    pending_space_span = (pending_space_span[0], raw_end)
            raw_position = raw_end
            continue
        if pending_space_span is not None:
            output.append(" ")
            raw_spans.append(pending_space_span)
            pending_space_span = None
        for normalized_character in emitted:
            output.append(normalized_character)
            raw_spans.append(
                (
                    pending_ignored_start
                    if pending_ignored_start is not None
                    else raw_position,
                    raw_end,
                )
            )
        pending_ignored_start = None
        raw_position = raw_end
    return "".join(output), tuple(raw_spans)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `normalize_planning_search_text`

**Exact signature**

```python
def normalize_planning_search_text(value: str) -> str:
```

**Purpose**

Normalize text using the stable ``fr_literal_v1`` search profile.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
normalize_planning_search_text_with_mapping(value)[0]
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `src/landscout/stages/structure_planning_regulation.py::<module>` via `from landscout.common.planning_text import (
    normalize_planning_search_text,
    normalize_planning_search_text_with_mapping,
    raw_context_from_spans,
)`.
- import: `tests/unit/test_index_planning_regulation.py::<module>` via `from landscout.common.planning_text import (
    normalize_planning_search_text as _normalize_search_text,
)`.
- import: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.common.planning_text import normalize_planning_search_text`.
- direct call: `tests/unit/test_index_planning_regulation.py::test_french_literal_normalization` via `_normalize_search_text`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `normalize_planning_search_text`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_token_boundary_and_longest_match_policy` via `normalize_planning_search_text`.

**Complete source-ordered implementation**

```python
def normalize_planning_search_text(value: str) -> str:
    """Normalize text using the stable ``fr_literal_v1`` search profile."""

    return normalize_planning_search_text_with_mapping(value)[0]
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `raw_context_from_spans`

**Exact signature**

```python
def raw_context_from_spans(
    raw_text: str,
    raw_spans: tuple[tuple[int, int], ...],
    normalized_start: int,
    normalized_end: int,
) -> str:
```

**Purpose**

Return the exact raw substring covering a normalized-text range.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
raw_text[raw_start:raw_end]

''
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `src/landscout/stages/structure_planning_regulation.py::<module>` via `from landscout.common.planning_text import (
    normalize_planning_search_text,
    normalize_planning_search_text_with_mapping,
    raw_context_from_spans,
)`.

**Complete source-ordered implementation**

```python
def raw_context_from_spans(
    raw_text: str,
    raw_spans: tuple[tuple[int, int], ...],
    normalized_start: int,
    normalized_end: int,
) -> str:
    """Return the exact raw substring covering a normalized-text range."""

    if normalized_start >= normalized_end:
        return ""
    raw_start = raw_spans[normalized_start][0]
    raw_end = raw_spans[normalized_end - 1][1]
    return raw_text[raw_start:raw_end]
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module does not define `__all__`; no package-export guarantee is inferred from its absence. Symbols can still be imported directly or re-exported by a separate package initializer, as shown by the reference lists.

## 9. Error handling

Controlled exceptions, local raise guards, delegated validators, and framework assertions are documented per exact function implementation. No broader error guarantee is inferred.

## 10. Side effects

Network I/O, filesystem reads/writes, in-memory mutation, input mutation, geometry/CRS calculations, hashing, and process/environment effects are listed separately for every function.

## 11. Security / trust boundaries

Textual URL/provider/hash fields are provenance claims, not physical proof. Physical proof exists only where the reproduced implementation revalidates transport, bytes, archive structure, source layers, geometry, or result hashes.


## 12. GIS / CRS rules

Only the explicit CRS/geometry validators and calculation copies in this module establish GIS behavior. No geometry repair, reprojection, or metric meaning is inferred from a field name alone.

## 13. Provenance rules

Configured identity, row lineage, byte identity, cache metadata, and source-complete revalidation are separate levels. This companion claims only the levels implemented above.

## 14. Business meaning

The module contributes to the planning flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
