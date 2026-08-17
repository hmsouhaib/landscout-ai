# `src/landscout/common/artifact_paths.py`

## File identity

- Repository path: `src/landscout/common/artifact_paths.py`
- File type: Python source
- Primary responsibility: Validates portable local Parquet artifact basenames across POSIX and Windows rules.
- Layer / domain: `internal common contract/utility` / `common`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `729fb042286323d6417e14690c70094d293c9a3905b2ca640b640c7e64397975`

## 1. Purpose

Validates portable local Parquet artifact basenames across POSIX and Windows rules.

## 2. Position in LandScout architecture

This file is a `internal common contract/utility` artifact in the `common` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `from pathlib import PurePosixPath, PureWindowsPath` — required by the implementation paths and symbols documented below.

### Third-party

- None.

### Internal LandScout

- None.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `_WINDOWS_FORBIDDEN_CHARACTERS` | `frozenset('<>:"/\\&#124;?*')` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_WINDOWS_RESERVED_BASENAMES` | `frozenset( {"con", "prn", "aux", "nul", "clock$"} &#124; {f"com{number}" for number in range(1, 10)} &#124; {f"lpt{number}" for number in range(1, 10)} &#124; {f"com{number}" for number in "¹²³"} &#124; {f"lpt{number}" for number in "¹²³"} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `validate_portable_parquet_filename`

**Signature**

```python
def validate_portable_parquet_filename(value: object, label: str) -> str:
```

**Purpose**

Return one portable local Parquet basename or raise ``ValueError``.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `ValueError(f'{label} must be an exact non-empty string')`.
2. Checks `any((ord(character) <= 31 or ord(character) == 127 for character in value))`. When true: Raises `ValueError(f'{label} contains a control character')`.
3. Checks `any((character in _WINDOWS_FORBIDDEN_CHARACTERS for character in value))`. When true: Raises `ValueError(f'{label} contains a Windows-forbidden character')`.
4. Checks `value.endswith(('.', ' '))`. When true: Raises `ValueError(f'{label} must not end in a dot or space')`.
5. Computes `posix` from `PurePosixPath(value)`.
6. Computes `windows` from `PureWindowsPath(value)`.
7. Checks `posix.is_absolute() or windows.is_absolute() or posix.name != value or (windows.name != value) or (posix.suffix.lower() != '.parquet') or (windows.suffix.lower() != '.parquet')`. When true: Raises `ValueError(f'{label} must be one portable local Parquet basename')`.
8. Computes `reserved_stem` from `value.split('.', 1)[0].casefold()`.
9. Checks `reserved_stem in _WINDOWS_RESERVED_BASENAMES`. When true: Raises `ValueError(f'{label} uses a Windows-reserved basename')`.
10. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.
- Rejects or diverts the path when `any((ord(character) <= 31 or ord(character) == 127 for character in value))` is true.
- Rejects or diverts the path when `any((character in _WINDOWS_FORBIDDEN_CHARACTERS for character in value))` is true.
- Rejects or diverts the path when `value.endswith(('.', ' '))` is true.
- Rejects or diverts the path when `posix.is_absolute() or windows.is_absolute() or posix.name != value or (windows.name != value) or (posix.suffix.lower() != '.parquet') or (windows.suffix.lower() != '.parquet')` is true.
- Rejects or diverts the path when `reserved_stem in _WINDOWS_RESERVED_BASENAMES` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PurePosixPath`, `PureWindowsPath`, `ValueError`, `any`, `isinstance`, `ord`, `posix.is_absolute`, `posix.suffix.lower`, `value.endswith`, `value.split`, `value.split('.', 1)[0].casefold`, `value.strip`, `windows.is_absolute`, `windows.suffix.lower`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `BessPlanningFeatureParcelAggregationArtifactRecord._validate_record`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `BessPlanningFeatureApplicationArtifactRecord._validate_record`
- `src/landscout/stages/bess_planning_feature_policy.py` — `BessPlanningFeaturePolicyArtifactManifest._validate_manifest`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_shared_filename_contract_rejects_superscript_windows_devices`

**Tests**

- `tests/unit/test_bess_planning_feature_policy.py::test_shared_filename_contract_rejects_superscript_windows_devices`

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

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

This file contributes to LandScout's `common` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
