# `src/landscout/common/artifact_paths.py`

## File identity

- Repository path: `src/landscout/common/artifact_paths.py`
- File type: Python source
- Layer: internal common contract
- Domain: common contract
- Responsibility: Validates portable local Parquet artifact basenames across POSIX and Windows rules.
- Source SHA256: `729fb042286323d6417e14690c70094d293c9a3905b2ca640b640c7e64397975`

## 1. Purpose

Validates portable local Parquet artifact basenames across POSIX and Windows rules.

## 2. Position in LandScout architecture

This file belongs to the **internal common contract** layer and the **common contract** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `from pathlib import PurePosixPath, PureWindowsPath`

### Third-party packages

- `None.`

### Internal LandScout imports

- `None.`

## 4. Contract taxonomy

### A. Python constants

#### `_WINDOWS_FORBIDDEN_CHARACTERS`

```python
_WINDOWS_FORBIDDEN_CHARACTERS = frozenset('<>:"/\\|?*')
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `_WINDOWS_RESERVED_BASENAMES`

```python
_WINDOWS_RESERVED_BASENAMES = frozenset(
    {"con", "prn", "aux", "nul", "clock$"}
    | {f"com{number}" for number in range(1, 10)}
    | {f"lpt{number}" for number in range(1, 10)}
    | {f"com{number}" for number in "¹²³"}
    | {f"lpt{number}" for number in "¹²³"}
)
```

Module-level technical/source/policy constant consumed by the exact references below.


### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `validate_portable_parquet_filename`

**Exact signature**

```python
def validate_portable_parquet_filename(value: object, label: str) -> str:
```

**Purpose**

Return one portable local Parquet basename or raise ``ValueError``.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip()`.
- Guard with a raise path: `any((ord(character) <= 31 or ord(character) == 127 for character in value))`.
- Guard with a raise path: `any((character in _WINDOWS_FORBIDDEN_CHARACTERS for character in value))`.
- Guard with a raise path: `value.endswith(('.', ' '))`.
- Guard with a raise path: `posix.is_absolute() or windows.is_absolute() or posix.name != value or (windows.name != value) or (posix.suffix.lower() != '.parquet') or (windows.suffix.lower() != '.parquet')`.
- Guard with a raise path: `reserved_stem in _WINDOWS_RESERVED_BASENAMES`.
- Explicit raise expressions: `ValueError(f'{label} contains a Windows-forbidden character')`, `ValueError(f'{label} contains a control character')`, `ValueError(f'{label} must be an exact non-empty string')`, `ValueError(f'{label} must be one portable local Parquet basename')`, `ValueError(f'{label} must not end in a dot or space')`, `ValueError(f'{label} uses a Windows-reserved basename')`.

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

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::BessPlanningFeatureParcelAggregationArtifactRecord._validate_record` via `validate_portable_parquet_filename`.
- import/re-export: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.common.artifact_paths import validate_portable_parquet_filename`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::BessPlanningFeatureApplicationArtifactRecord._validate_record` via `validate_portable_parquet_filename`.
- import/re-export: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.common.artifact_paths import validate_portable_parquet_filename`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `validate_portable_parquet_filename`.
- import/re-export: `src/landscout/stages/bess_planning_feature_policy.py::<module>` via `from landscout.common.artifact_paths import validate_portable_parquet_filename`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::test_shared_filename_contract_rejects_superscript_windows_devices` via `validate_portable_parquet_filename`.
- import/re-export: `tests/unit/test_bess_planning_feature_policy.py::<module>` via `from landscout.common.artifact_paths import validate_portable_parquet_filename`.

**Complete source-ordered implementation**

```python
def validate_portable_parquet_filename(value: object, label: str) -> str:
    """Return one portable local Parquet basename or raise ``ValueError``."""

    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be an exact non-empty string")
    if any(ord(character) <= 0x1F or ord(character) == 0x7F for character in value):
        raise ValueError(f"{label} contains a control character")
    if any(character in _WINDOWS_FORBIDDEN_CHARACTERS for character in value):
        raise ValueError(f"{label} contains a Windows-forbidden character")
    if value.endswith((".", " ")):
        raise ValueError(f"{label} must not end in a dot or space")
    posix = PurePosixPath(value)
    windows = PureWindowsPath(value)
    if (
        posix.is_absolute()
        or windows.is_absolute()
        or posix.name != value
        or windows.name != value
        or posix.suffix.lower() != ".parquet"
        or windows.suffix.lower() != ".parquet"
    ):
        raise ValueError(f"{label} must be one portable local Parquet basename")
    reserved_stem = value.split(".", 1)[0].casefold()
    if reserved_stem in _WINDOWS_RESERVED_BASENAMES:
        raise ValueError(f"{label} uses a Windows-reserved basename")
    return value
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.


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

The module contributes to the common contract flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
