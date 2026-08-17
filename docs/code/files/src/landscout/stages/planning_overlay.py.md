# `src/landscout/stages/planning_overlay.py`

## File identity

- Repository path: `src/landscout/stages/planning_overlay.py`
- File type: Python source
- Layer: processing stage
- Domain: planning
- Responsibility: Preserves the historical stage import path by re-exporting the shared common-layer technical overlay tolerance constants and function without adding behavior.
- Source SHA256: `7ba1e577956408550871aa0e817472e9b9443f900b48ed0fa28f09351951cf0b`

## 1. Purpose

Preserves the historical stage import path by re-exporting the shared common-layer technical overlay tolerance constants and function without adding behavior.

## 2. Position in LandScout architecture

This file belongs to the **processing stage** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`

### Third-party packages

- `None.`

### Internal LandScout imports

- `from landscout.common.planning_overlay import (
    ABSOLUTE_OVERLAY_TOLERANCE,
    RELATIVE_OVERLAY_TOLERANCE,
    technical_overlay_tolerance,
)`

## 4. Contract taxonomy

### A. Python constants

No meaningful module constant is declared.

### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "ABSOLUTE_OVERLAY_TOLERANCE",
    "RELATIVE_OVERLAY_TOLERANCE",
    "technical_overlay_tolerance",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

No function or method is declared.

## 7. Data contracts

No module-level canonical frame schema, mapping, or dtype declaration is present. Any frame interaction is recoverable from the complete function implementations below; no string literal is promoted to a column merely because it appears in code.

No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `ABSOLUTE_OVERLAY_TOLERANCE` | public re-export imported from its declaring module | `landscout.common.planning_overlay.ABSOLUTE_OVERLAY_TOLERANCE` | yes |
| `RELATIVE_OVERLAY_TOLERANCE` | public re-export imported from its declaring module | `landscout.common.planning_overlay.RELATIVE_OVERLAY_TOLERANCE` | yes |
| `technical_overlay_tolerance` | public re-export imported from its declaring module | `landscout.common.planning_overlay.technical_overlay_tolerance` | yes |

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
