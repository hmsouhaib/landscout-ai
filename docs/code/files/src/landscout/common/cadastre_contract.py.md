# `src/landscout/common/cadastre_contract.py`

## File identity

- Repository path: `src/landscout/common/cadastre_contract.py`
- File type: Python source
- Layer: internal common contract
- Domain: cadastre
- Responsibility: Provides the internal exact geometry-status vocabulary guard shared by cadastral filtering stages.
- Source SHA256: `d7dc15892f65fbf8935051af26e519b82c98b74defa2e1b2f09c298427903971`

## 1. Purpose

Provides the internal exact geometry-status vocabulary guard shared by cadastral filtering stages.

## 2. Position in LandScout architecture

This file belongs to the **internal common contract** layer and the **cadastre** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from collections.abc import Iterable`

### Third-party packages

- `None.`

### Internal LandScout imports

- `None.`

## 4. Contract taxonomy

### A. Python constants

#### `CADASTRE_GEOMETRY_STATUSES`

```python
CADASTRE_GEOMETRY_STATUSES = frozenset({"VALID", "INVALID"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `validate_cadastre_geometry_statuses`

**Exact signature**

```python
def validate_cadastre_geometry_statuses(values: Iterable[object]) -> None:
```

**Purpose**

Require the exact geometry-status vocabulary emitted by normalization.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `any((type(value) is not str or value not in CADASTRE_GEOMETRY_STATUSES for value in values))`.
- Explicit raise expressions: `ValueError('geometry_status must contain only exact VALID or INVALID strings')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/enrich_shape.py::enrich_parcel_shapes` via `validate_cadastre_geometry_statuses`.
- import/re-export: `src/landscout/stages/enrich_shape.py::<module>` via `from landscout.common.cadastre_contract import validate_cadastre_geometry_statuses`.
- direct call or construction: `src/landscout/stages/filter_parcels.py::filter_parcels_by_area` via `validate_cadastre_geometry_statuses`.
- import/re-export: `src/landscout/stages/filter_parcels.py::<module>` via `from landscout.common.cadastre_contract import validate_cadastre_geometry_statuses`.

**Complete source-ordered implementation**

```python
def validate_cadastre_geometry_statuses(values: Iterable[object]) -> None:
    """Require the exact geometry-status vocabulary emitted by normalization."""

    if any(
        type(value) is not str or value not in CADASTRE_GEOMETRY_STATUSES
        for value in values
    ):
        raise ValueError(
            "geometry_status must contain only exact VALID or INVALID strings"
        )
```

**Business boundary**

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.


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

The module contributes to the cadastre flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- It does not establish ownership contacts, developability, planning authorization, ranking, or a BESS score.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
