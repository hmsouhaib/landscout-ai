# `src/landscout/common/planning_overlay.py`

## File identity

- Repository path: `src/landscout/common/planning_overlay.py`
- File type: Python source
- Layer: internal common contract
- Domain: planning
- Responsibility: Defines the technical floating-point tolerance used by factual planning overlay checks.
- Source SHA256: `f28349ab5f3f8223b537184ac28a98d6d6e328a724957dabb7089c3809351086`

## 1. Purpose

Defines the technical floating-point tolerance used by factual planning overlay checks.

## 2. Position in LandScout architecture

This file belongs to the **internal common contract** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from math import isfinite`

### Third-party packages

- `None.`

### Internal LandScout imports

- `None.`

## 4. Contract taxonomy

### A. Python constants

#### `ABSOLUTE_OVERLAY_TOLERANCE`

```python
ABSOLUTE_OVERLAY_TOLERANCE = 1e-6
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/planning_overlay.py::<module>` (re-export), `src/landscout/common/planning_overlay.py::technical_overlay_tolerance` (value reference).

#### `RELATIVE_OVERLAY_TOLERANCE`

```python
RELATIVE_OVERLAY_TOLERANCE = 1e-12
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/planning_overlay.py::<module>` (re-export), `src/landscout/common/planning_overlay.py::technical_overlay_tolerance` (value reference).


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `technical_overlay_tolerance`

**Exact signature**

```python
def technical_overlay_tolerance(reference_value: float) -> float:
```

**Purpose**

Return the shared floating-point overlay tolerance for a metric value.

**Return contract**

- Declared return annotation: `float`.
- Every observed return expression is reproduced without truncation:
```python
max(ABSOLUTE_OVERLAY_TOLERANCE, reference_value * RELATIVE_OVERLAY_TOLERANCE)
```

**Validation and exceptions**

- Guard with a raise path: `not isfinite(reference_value) or reference_value < 0`.
- Explicit raise expressions: `ValueError('Overlay tolerance reference must be finite and non-negative')`.

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

- import: `src/landscout/common/bess_application_contract.py::<module>` via `from landscout.common.planning_overlay import technical_overlay_tolerance`.
- import: `src/landscout/common/planning_feature_contract.py::<module>` via `from landscout.common.planning_overlay import technical_overlay_tolerance`.
- import: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.common.planning_overlay import technical_overlay_tolerance`.
- import: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.common.planning_overlay import technical_overlay_tolerance`.
- import: `src/landscout/stages/enrich_planning_features.py::<module>` via `from landscout.common.planning_overlay import technical_overlay_tolerance`.
- import: `src/landscout/stages/enrich_planning_zoning.py::<module>` via `from landscout.stages.planning_overlay import technical_overlay_tolerance`.
- import: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `from landscout.stages.planning_overlay import technical_overlay_tolerance`.
- re-export: `src/landscout/stages/planning_overlay.py::<module>` via `from landscout.common.planning_overlay import (
    ABSOLUTE_OVERLAY_TOLERANCE,
    RELATIVE_OVERLAY_TOLERANCE,
    technical_overlay_tolerance,
)`.
- import: `src/landscout/stages/structure_planning_regulation.py::<module>` via `from landscout.stages.planning_overlay import technical_overlay_tolerance`.
- import: `tests/unit/test_enrich_planning_zoning.py::<module>` via `from landscout.stages.planning_overlay import technical_overlay_tolerance`.
- import: `tests/unit/test_structure_planning_regulation.py::<module>` via `from landscout.stages.planning_overlay import technical_overlay_tolerance`.
- direct call: `src/landscout/common/bess_application_contract.py::_feature_metric` via `technical_overlay_tolerance`.
- direct call: `src/landscout/common/planning_feature_contract.py::validate_intrinsic_planning_feature_relations` via `technical_overlay_tolerance`.
- direct call: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_relation_parcel_areas` via `technical_overlay_tolerance`.
- direct call: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `technical_overlay_tolerance`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_technical_tolerance` via `technical_overlay_tolerance`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_require_close` via `technical_overlay_tolerance`.
- direct call: `src/landscout/stages/enrich_planning_features.py::_validate_parcel_summaries` via `technical_overlay_tolerance`.
- direct call: `src/landscout/stages/enrich_planning_zoning.py::_technical_area_tolerance` via `technical_overlay_tolerance`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_relations` via `technical_overlay_tolerance`.
- direct call: `src/landscout/stages/structure_planning_regulation.py::_validated_zoning_inputs` via `technical_overlay_tolerance`.
- direct call: `tests/unit/test_enrich_planning_zoning.py::test_shared_overlay_tolerance_preserves_zoning_numerical_behavior` via `technical_overlay_tolerance`.
- direct call: `tests/unit/test_structure_planning_regulation.py::test_intersection_upper_bound_uses_shared_relative_tolerance` via `technical_overlay_tolerance`.

**Complete source-ordered implementation**

```python
def technical_overlay_tolerance(reference_value: float) -> float:
    """Return the shared floating-point overlay tolerance for a metric value."""

    if not isfinite(reference_value) or reference_value < 0:
        raise ValueError("Overlay tolerance reference must be finite and non-negative")
    return max(
        ABSOLUTE_OVERLAY_TOLERANCE,
        reference_value * RELATIVE_OVERLAY_TOLERANCE,
    )
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
