# `src/landscout/common/frame_integrity.py`

## File identity

- Repository path: `src/landscout/common/frame_integrity.py`
- File type: Python source
- Layer: internal common contract
- Domain: common contract
- Responsibility: Builds deterministic structural signatures for Pandas and GeoPandas frames.
- Source SHA256: `dc5adb54d47e31171fa95c36c98d6e73bddfa109b65f26f5d5dc8f1a6183f861`

## 1. Purpose

Builds deterministic structural signatures for Pandas and GeoPandas frames.

## 2. Position in LandScout architecture

This file belongs to the **internal common contract** layer and the **common contract** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `from pyproj import CRS`

### Internal LandScout imports

- `None.`

## 4. Contract taxonomy

### A. Python constants

No meaningful module constant is declared.

### B. Type aliases and closed domains

No module-level Literal/Annotated/TypeAlias declaration is present.

### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `deterministic_frame_schema_signature`

**Exact signature**

```python
def deterministic_frame_schema_signature(
    frame: pd.DataFrame,
) -> dict[str, object]:
```

**Purpose**

Return the complete ordered schema identity used by integrity envelopes.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
signature
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, pd.DataFrame)`.
- Guard with a raise path: `isinstance(frame, gpd.GeoDataFrame)`.
- Guard with a raise path: `geometry_column not in frame.columns`.
- Guard with a raise path: `frame.crs is None`.
- Explicit raise expressions: `TypeError('Frame schema signature requires a pandas DataFrame')`, `ValueError('GeoDataFrame CRS is missing')`, `ValueError('GeoDataFrame active geometry column is missing')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `signature['crs']`, `signature['geometry_column']`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_frame_payload` via `deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_read_verified_artifact` via `deterministic_frame_schema_signature`.
- import/re-export: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.common.frame_integrity import deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_frame_payload` via `deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_read_verified_artifact` via `deterministic_frame_schema_signature`.
- import/re-export: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.common.frame_integrity import deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_frame_payload` via `deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_artifacts` via `deterministic_frame_schema_signature`.
- import/re-export: `src/landscout/stages/bess_planning_feature_policy.py::<module>` via `from landscout.common.frame_integrity import deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_expected_relations_content_sha256` via `deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_compare_normalized_catalog` via `deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_relations` via `deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_parcel_output` via `deterministic_frame_schema_signature`.
- import/re-export: `src/landscout/stages/enrich_planning_features.py::<module>` via `from landscout.common.frame_integrity import deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/enrich_planning_zoning.py::_compare_exact_frame` via `deterministic_frame_schema_signature`.
- import/re-export: `src/landscout/stages/enrich_planning_zoning.py::<module>` via `from landscout.common.frame_integrity import deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_code_dictionary` via `deterministic_frame_schema_signature`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_payload` via `deterministic_frame_schema_signature`.
- import/re-export: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `from landscout.common.frame_integrity import deterministic_frame_schema_signature`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_write_artifacts` via `deterministic_frame_schema_signature`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `deterministic_frame_schema_signature`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_self_consistent_parcel_area_artifact_is_rejected` via `deterministic_frame_schema_signature`.
- import/re-export: `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.common.frame_integrity import deterministic_frame_schema_signature`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_write_application_artifacts` via `deterministic_frame_schema_signature`.
- import/re-export: `tests/unit/test_apply_bess_planning_feature_policy.py::<module>` via `from landscout.common.frame_integrity import deterministic_frame_schema_signature`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::_artifact_manifest` via `deterministic_frame_schema_signature`.
- import/re-export: `tests/unit/test_bess_planning_feature_policy.py::<module>` via `from landscout.common.frame_integrity import deterministic_frame_schema_signature`.

**Complete source-ordered implementation**

```python
def deterministic_frame_schema_signature(
    frame: pd.DataFrame,
) -> dict[str, object]:
    """Return the complete ordered schema identity used by integrity envelopes."""

    if not isinstance(frame, pd.DataFrame):
        raise TypeError("Frame schema signature requires a pandas DataFrame")
    index = frame.index
    if isinstance(index, pd.MultiIndex):
        index_dtypes = [str(dtype) for dtype in index.dtypes]
    else:
        index_dtypes = [str(index.dtype)]
    signature: dict[str, object] = {
        "columns": [str(column) for column in frame.columns],
        "dtypes": [str(dtype) for dtype in frame.dtypes],
        "index_class": f"{type(index).__module__}.{type(index).__qualname__}",
        "index_names": [None if name is None else str(name) for name in index.names],
        "index_level_dtypes": index_dtypes,
    }
    if isinstance(frame, gpd.GeoDataFrame):
        geometry_column = frame.geometry.name
        if geometry_column not in frame.columns:
            raise ValueError("GeoDataFrame active geometry column is missing")
        signature["geometry_column"] = str(geometry_column)
        if frame.crs is None:
            raise ValueError("GeoDataFrame CRS is missing")
        signature["crs"] = CRS.from_user_input(frame.crs).to_json_dict()
    return signature
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.


## 7. Data contracts

### Frame-preservation and semantic notes

- `crs` and `geometry_column` are keys in the returned structural-signature mapping; they are not asserted as columns of the inspected frame.

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
