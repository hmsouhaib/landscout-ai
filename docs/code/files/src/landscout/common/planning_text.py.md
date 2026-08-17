# `src/landscout/common/planning_text.py`

## File identity

- Repository path: `src/landscout/common/planning_text.py`
- File type: Python source
- Primary responsibility: Normalizes planning text for deterministic matching while retaining mappings back to raw source spans.
- Layer / domain: `internal common contract/utility` / `planning`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `1e4d6ec3de5914174eaa053c2c6afdf700ab00bfd6d96db98281a1991f7eae80`

## 1. Purpose

Normalizes planning text for deterministic matching while retaining mappings back to raw source spans.

## 2. Position in LandScout architecture

This file is a `internal common contract/utility` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import unicodedata` — required by the implementation paths and symbols documented below.

### Third-party

- None.

### Internal LandScout

- None.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `SEARCH_NORMALIZATION_PROFILE` | `"fr_literal_v1"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_APOSTROPHES` | `frozenset("'’‘ʼ‛＇ꞌ")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_DASHES` | `frozenset("-‐‑‒–—―−﹘﹣－")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SPECIAL_EXPANSIONS` | `{"œ": "oe", "Œ": "oe", "æ": "ae", "Æ": "ae"}` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `normalize_planning_search_text_with_mapping`

**Signature**

```python
def normalize_planning_search_text_with_mapping(
    value: str,
) -> tuple[str, tuple[tuple[int, int], ...]]:
```

**Purpose**

Normalize literal-search text and map each output character to a raw span.

**Inputs**

- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, tuple[tuple[int, int], ...]]`. Observed return expression(s): `(''.join(output), tuple(raw_spans))`.

**Algorithm**

1. Defines `output` with annotation `list[str]` from `[]`.
2. Defines `raw_spans` with annotation `list[tuple[int, int]]` from `[]`.
3. Defines `pending_space_span` with annotation `tuple[int, int] | None` from `None`.
4. Defines `pending_ignored_start` with annotation `int | None` from `None`.
5. Computes `raw_position` from `0`.
6. Repeats the guarded body while `raw_position < len(value)` remains true.
7. Returns `(''.join(output), tuple(raw_spans))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `''.join`, `_SPECIAL_EXPANSIONS.get`, `all`, `character.casefold`, `character.isspace`, `emitted.extend`, `len`, `output.append`, `raw_spans.append`, `tuple`, `unicodedata.combining`, `unicodedata.normalize`.

**Known repository callers**

- `src/landscout/common/planning_text.py` — `normalize_planning_search_text`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `normalize_planning_search_text`

**Signature**

```python
def normalize_planning_search_text(value: str) -> str:
```

**Purpose**

Normalize text using the stable ``fr_literal_v1`` search profile.

**Inputs**

- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `normalize_planning_search_text_with_mapping(value)[0]`.

**Algorithm**

1. Returns `normalize_planning_search_text_with_mapping(value)[0]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `normalize_planning_search_text_with_mapping`.

**Known repository callers**

- `tests/unit/test_index_planning_regulation.py` — `test_french_literal_normalization`
- `tests/unit/test_structure_planning_regulation.py` — `test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py` — `test_token_boundary_and_longest_match_policy`

**Tests**

- `tests/unit/test_index_planning_regulation.py::test_french_literal_normalization`
- `tests/unit/test_structure_planning_regulation.py::test_equal_length_overlap_uses_configured_term_order_as_tie_break`
- `tests/unit/test_structure_planning_regulation.py::test_token_boundary_and_longest_match_policy`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `raw_context_from_spans`

**Signature**

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

**Inputs**

- `raw_text` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `raw_spans` (`tuple[tuple[int, int], ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `normalized_start` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `normalized_end` (`int`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `raw_text[raw_start:raw_end]`; `''`.

**Algorithm**

1. Checks `normalized_start >= normalized_end`. When true: Returns `''`.
2. Computes `raw_start` from `raw_spans[normalized_start][0]`.
3. Computes `raw_end` from `raw_spans[normalized_end - 1][1]`.
4. Returns `raw_text[raw_start:raw_end]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 7. Data contracts

No DataFrame/GeoDataFrame column is referenced directly. Object and scalar contracts are documented through classes, parameters, returns, constants, and validators.

## 8. Interfaces

Known static callers, internal calls, and tests are listed for every symbol. Package-level availability is controlled by this module's `__all__` and the relevant package `__init__.py`; private helpers are not a stable public API.

## 9. Error handling

Every explicit raise and guarded condition is listed with its function. Public boundaries translate malformed source/configuration/input conditions into the controlled exception classes shown by those functions and tests; raw implementation errors are not promised as API.

## 10. Side effects

Per-function side effects are derived from actual calls. Source adapters may perform guarded network, cache, archive, or filesystem operations; stages normally operate on copies unless their preservation validators state otherwise; tests use the boundaries stated per test.

## 11. Security / trust boundaries

Trust claims are limited to the explicit byte, schema, lineage, source-complete, path, URL, geometry, or policy checks implemented by this file and its callees. Textual lineage is not treated as physical proof unless the function revalidates the physical source.

## 12. GIS / CRS rules

GIS rules apply only where geometry/CRS calls or columns are listed above. Storage geometry is not silently repaired; metric work uses the explicit CRS transformations and calculation copies visible in the algorithm. Files without GIS calls impose no CRS contract.

## 13. Provenance rules

Provenance is carried only through exact source/configuration/hash fields shown by the models, constants, and frame columns. Consult `docs/code/SOURCE_TRUST_MODEL.md` for the cross-adapter chain.

## 14. Business meaning

This file contributes to LandScout's `planning` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
