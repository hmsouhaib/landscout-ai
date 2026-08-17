# `src/landscout/common/frame_integrity.py`

## File identity

- Repository path: `src/landscout/common/frame_integrity.py`
- File type: Python source
- Primary responsibility: Builds deterministic structural signatures for Pandas and GeoPandas frames.
- Layer / domain: `internal common contract/utility` / `common`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `dc5adb54d47e31171fa95c36c98d6e73bddfa109b65f26f5d5dc8f1a6183f861`

## 1. Purpose

Builds deterministic structural signatures for Pandas and GeoPandas frames.

## 2. Position in LandScout architecture

This file is a `internal common contract/utility` artifact in the `common` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.

### Internal LandScout

- None.

## 4. Constants and domains

No module-level meaningful constant is defined. Literal domains enforced inside functions are documented with those functions.

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `deterministic_frame_schema_signature`

**Signature**

```python
def deterministic_frame_schema_signature(
    frame: pd.DataFrame,
) -> dict[str, object]:
```

**Purpose**

Return the complete ordered schema identity used by integrity envelopes.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `signature`.

**Algorithm**

1. Checks `not isinstance(frame, pd.DataFrame)`. When true: Raises `TypeError('Frame schema signature requires a pandas DataFrame')`.
2. Computes `index` from `frame.index`.
3. Checks `isinstance(index, pd.MultiIndex)`. When true: Computes `index_dtypes` from `[str(dtype) for dtype in index.dtypes]`. Otherwise: Computes `index_dtypes` from `[str(index.dtype)]`.
4. Defines `signature` with annotation `dict[str, object]` from `{'columns': [str(column) for column in frame.columns], 'dtypes': [str(dtype) for dtype in frame.dtypes], 'index_class': f'{type(index).__module__}.{type(index).__qualname__}', 'index_names': [None if name is None else str(name) for name in index.names], 'index_level_dtypes': index_dtypes}`.
5. Checks `isinstance(frame, gpd.GeoDataFrame)`. When true: Computes `geometry_column` from `frame.geometry.name`. Checks `geometry_column not in frame.columns`. When true: Raises `ValueError('GeoDataFrame active geometry column is missing')`. Computes `signature['geometry_column']` from `str(geometry_column)`. Executes 2 additional source-ordered statement(s).
6. Returns `signature`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, pd.DataFrame)` is true.
- Rejects or diverts the path when `isinstance(frame, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `geometry_column not in frame.columns` is true.
- Rejects or diverts the path when `frame.crs is None` is true.

**Exceptions**

- Explicitly raises: `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_user_input`, `CRS.from_user_input(frame.crs).to_json_dict`, `TypeError`, `ValueError`, `isinstance`, `str`, `type`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_frame_payload`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_read_verified_artifact`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_frame_payload`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_read_verified_artifact`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_validate_result_envelope`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_frame_payload`
- `src/landscout/stages/bess_planning_feature_policy.py` — `_validate_result_envelope`
- `src/landscout/stages/bess_planning_feature_policy.py` — `load_bess_planning_feature_policy_artifacts`
- `src/landscout/stages/enrich_planning_features.py` — `_compare_normalized_catalog`
- `src/landscout/stages/enrich_planning_features.py` — `_compare_rebuilt_parcel_output`
- `src/landscout/stages/enrich_planning_features.py` — `_compare_rebuilt_relations`
- `src/landscout/stages/enrich_planning_features.py` — `_expected_relations_content_sha256`
- `src/landscout/stages/enrich_planning_zoning.py` — `_compare_exact_frame`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_frame_payload`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_code_dictionary`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_write_artifacts`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_no_relation_parcel_rejects_textual_null_identity`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_self_consistent_parcel_area_artifact_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `_write_application_artifacts`
- `tests/unit/test_bess_planning_feature_policy.py` — `_artifact_manifest`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected`

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `crs` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_column` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |

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
