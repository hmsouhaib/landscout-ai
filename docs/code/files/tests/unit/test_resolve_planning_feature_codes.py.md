# `tests/unit/test_resolve_planning_feature_codes.py`

## File identity

- Repository path: `tests/unit/test_resolve_planning_feature_codes.py`
- File type: Python source
- Layer: unit/regression test
- Domain: isolated contract test evidence
- Responsibility: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.
- Source SHA256: `f089c7cf174ecf5fa745d5909f817884a6c9df6d52f0e53f8702a639106e574c`

## 1. STEP 7F.1A.4 contract delta

- Refreshes permanent STEP 7F.1A.4 regression coverage for resolve planning feature codes; the exact fixtures, mutations, calls, controlled failures, and assertions are inventoried below.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

The file belongs to the **unit/regression test** layer and **isolated contract test evidence** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import importlib`
- `import inspect`
- `import json`
- `import shutil`
- `import tempfile`
- `from dataclasses import replace`
- `from hashlib import sha256`
- `from pathlib import Path`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `import pytest`
- `import yaml`
- `from geopandas.testing import assert_geodataframe_equal`
- `from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)`

### Internal LandScout imports

- `from landscout.common.planning_feature_schema import (
    NORMALIZED_RELATION_DTYPES,
    feature_dtypes,
    relation_dtypes,
)`
- `from landscout.sources import gpu_fr as gpu_source_module`
- `from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)`
- `from landscout.stages.enrich_planning_features import (
    RELATION_COLUMNS,
    intersect_parcels_with_gpu_planning_features,
)`
- `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`
- `from landscout.stages.resolve_planning_feature_codes import (
    resolve_planning_feature_codes as _public_resolve_planning_feature_codes,
)`
- `from landscout.stages.resolve_planning_feature_codes import (
    validate_planning_feature_code_result as _public_validate_planning_feature_code_result,
)`
- `from landscout import stages`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `P_URL`

- Category: module constant or closed domain.
- Exact declaration:

```python
P_URL = "https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `I_URL`

- Category: module constant or closed domain.
- Exact declaration:

```python
I_URL = "https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `TEXT_NORMALIZATION`

- Category: module constant or closed domain.
- Exact declaration:

```python
TEXT_NORMALIZATION = "GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result.DerivedPlanningFeatureCodeResult`

**Source purpose:** Defines `test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result.DerivedPlanningFeatureCodeResult`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `PlanningFeatureCodeResult`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class DerivedPlanningFeatureCodeResult(PlanningFeatureCodeResult):
        pass
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_canonical_relation_schema`

**Purpose:** Implements `canonical relation schema` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _canonical_relation_schema(frame: pd.DataFrame) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_parcel_feature_relation_is_rejected` via `_canonical_relation_schema`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_parcel_feature_relation_is_rejected` via `_canonical_relation_schema`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_relation_type_must_match_catalog_geometry_kind` via `_canonical_relation_schema`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_relation_type_must_match_catalog_geometry_kind` via `_canonical_relation_schema`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `frame.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Series` | `pandas.Series` |
| `output[column].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.RangeIndex` | `pandas.RangeIndex` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `output[column] = pd.Series(<br>            output[column].tolist(), index=output.index, dtype=dtype<br>        )`<br>`output.index = pd.RangeIndex(len(output))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _canonical_relation_schema(frame: pd.DataFrame) -> pd.DataFrame:
    output = frame.copy(deep=True)
    for column, dtype in zip(RELATION_COLUMNS, NORMALIZED_RELATION_DTYPES, strict=True):
        output[column] = pd.Series(
            output[column].tolist(), index=output.index, dtype=dtype
        )
    output.index = pd.RangeIndex(len(output))
    return output
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_records_hash`

**Purpose:** Implements `records hash` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _records_hash(records: list[dict[str, object]]) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `records` | positional-or-keyword | `list[dict[str, object]]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `sha256(payload).hexdigest()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_profile_payload` via `_records_hash`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_profile_payload` via `_records_hash`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `_records_hash`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `_records_hash`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_official_family_endpoints_require_exact_identity` via `_records_hash`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_official_family_endpoints_require_exact_identity` via `_records_hash`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_official_text_must_already_be_canonical` via `_records_hash`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_official_text_must_already_be_canonical` via `_records_hash`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps(<br>        ordered,<br>        ensure_ascii=False,<br>        allow_nan=False,<br>        sort_keys=True,<br>        separators=(",", ":"),<br>    ).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `sha256(payload).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(payload).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _records_hash(records: list[dict[str, object]]) -> str:
    ordered = sorted(
        records,
        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"]),
    )
    payload = json.dumps(
        ordered,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return sha256(payload).hexdigest()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_payload_hash`

**Purpose:** Implements `payload hash` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _payload_hash(payload: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `payload` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `sha256(encoded).hexdigest()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs` via `_payload_hash`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs` via `_payload_hash`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.dumps(<br>        payload,<br>        ensure_ascii=False,<br>        allow_nan=False,<br>        sort_keys=True,<br>        separators=(",", ":"),<br>        default=str,<br>    ).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `sha256(encoded).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(encoded).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _payload_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return sha256(encoded).hexdigest()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_record`

**Purpose:** Implements `record` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _record(
    family: str,
    type_code: str,
    subtype_code: str,
    label: str,
) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `family` | positional-or-keyword | `str` | `required` |
| `type_code` | positional-or-keyword | `str` | `required` |
| `subtype_code` | positional-or-keyword | `str` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "feature_family": family,<br>        "type_code": type_code,<br>        "subtype_code": subtype_code,<br>        "official_label": label,<br>        "legal_reference": None,<br>        "regulation_or_annex_reference": None,<br>        "official_source_url": P_URL if family == "PRESCRIPTION" else I_URL,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_profile_payload` via `_record`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_profile_payload` via `_record`

Outbound call expressions and conservative ownership:
- No calls.

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _record(
    family: str,
    type_code: str,
    subtype_code: str,
    label: str,
) -> dict[str, object]:
    return {
        "feature_family": family,
        "type_code": type_code,
        "subtype_code": subtype_code,
        "official_label": label,
        "legal_reference": None,
        "regulation_or_annex_reference": None,
        "official_source_url": P_URL if family == "PRESCRIPTION" else I_URL,
    }
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_profile_payload`

**Purpose:** Implements `profile payload` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _profile_payload() -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "schema_version": 2,<br>        "profile": "synthetic_cnig_plu_2017",<br>        "standard_model": "CNIG PLU v2017",<br>        "official_text_normalization": TEXT_NORMALIZATION,<br>        "official_sources": {<br>            "prescription": P_URL,<br>            "information": I_URL,<br>        },<br>        "retrieval_date": "2026-08-12",<br>        "canonical_records_sha256": _records_hash(records),<br>        "records": records,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_profile` via `_profile_payload`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_profile` via `_profile_payload`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `_profile_payload`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `_profile_payload`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_official_family_endpoints_require_exact_identity` via `_profile_payload`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_official_family_endpoints_require_exact_identity` via `_profile_payload`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_official_text_must_already_be_canonical` via `_profile_payload`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_official_text_must_already_be_canonical` via `_profile_payload`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_malformed_code_is_rejected` via `_profile_payload`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_malformed_code_is_rejected` via `_profile_payload`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_pair_and_profile_hash_mutation_are_rejected` via `_profile_payload`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_pair_and_profile_hash_mutation_are_rejected` via `_profile_payload`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_wrong_official_host_and_unknown_field_are_rejected` via `_profile_payload`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_wrong_official_host_and_unknown_field_are_rejected` via `_profile_payload`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_record_order_must_be_deterministic` via `_profile_payload`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_record_order_must_be_deterministic` via `_profile_payload`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_yaml_snapshot_loads_strictly` via `_profile_payload`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_yaml_snapshot_loads_strictly` via `_profile_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_record` | `tests.unit.test_resolve_planning_feature_codes._record` |
| `_records_hash` | `tests.unit.test_resolve_planning_feature_codes._records_hash` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_records_hash` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _profile_payload() -> dict[str, object]:
    records = [
        _record("INFORMATION", "02", "00", "Information two"),
        _record("INFORMATION", "99", "00", "Other information"),
        _record("PRESCRIPTION", "07", "00", "Prescription seven"),
        _record("PRESCRIPTION", "07", "04", "Prescription seven subtype four"),
    ]
    return {
        "schema_version": 2,
        "profile": "synthetic_cnig_plu_2017",
        "standard_model": "CNIG PLU v2017",
        "official_text_normalization": TEXT_NORMALIZATION,
        "official_sources": {
            "prescription": P_URL,
            "information": I_URL,
        },
        "retrieval_date": "2026-08-12",
        "canonical_records_sha256": _records_hash(records),
        "records": records,
    }
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_profile`

**Purpose:** Implements `profile` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _profile() -> CnigFeatureCodeProfile:
```

- Exact decorators: none.
- Declared return annotation: `CnigFeatureCodeProfile`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `CnigFeatureCodeProfile.model_validate(_profile_payload())`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_legacy_inputs` via `_profile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_legacy_inputs` via `_profile`
- direct call: `tests.unit.test_resolve_planning_feature_codes::_mutated_profile` via `_profile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_mutated_profile` via `_profile`
- direct call: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `_profile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `_profile`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `_profile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `_profile`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `_profile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `_profile`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_relation_types_are_retained` via `_profile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_relation_types_are_retained` via `_profile`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_yaml_snapshot_loads_strictly` via `_profile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_yaml_snapshot_loads_strictly` via `_profile`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `CnigFeatureCodeProfile.model_validate` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.model_validate` |
| `_profile_payload` | `tests.unit.test_resolve_planning_feature_codes._profile_payload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _profile() -> CnigFeatureCodeProfile:
    return CnigFeatureCodeProfile.model_validate(_profile_payload())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_physical_inventory`

**Purpose:** Implements `physical inventory` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuExtractedFile, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(<br>        GpuExtractedFile(<br>            relative_path=path.relative_to(root).as_posix(),<br>            file_type=path.suffix.casefold().lstrip(".") or "none",<br>            size_bytes=path.stat().st_size,<br>            sha256=sha256(path.read_bytes()).hexdigest(),<br>            category="SPATIAL_DATA",<br>        )<br>        for path in sorted(<br>            (item for item in root.rglob("*") if item.is_file()), key=str<br>        )<br>        if not (path.parent == root and path.name == EXTRACTION_MANIFEST_NAME)<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `_physical_inventory`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `_physical_inventory`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuExtractedFile` | `landscout.sources.gpu_fr.GpuExtractedFile` |
| `path.relative_to(root).as_posix` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.suffix.casefold().lstrip` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.suffix.casefold` | `unresolved local/third-party receiver; no ownership inferred` |
| `path.stat` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(path.read_bytes()).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `path.read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `root.rglob` | `unresolved local/third-party receiver; no ownership inferred` |
| `item.is_file` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `path.stat`<br>`sha256(path.read_bytes()).hexdigest`<br>`path.read_bytes`<br>`item.is_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(path.read_bytes()).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    return tuple(
        GpuExtractedFile(
            relative_path=path.relative_to(root).as_posix(),
            file_type=path.suffix.casefold().lstrip(".") or "none",
            size_bytes=path.stat().st_size,
            sha256=sha256(path.read_bytes()).hexdigest(),
            category="SPATIAL_DATA",
        )
        for path in sorted(
            (item for item in root.rglob("*") if item.is_file()), key=str
        )
        if not (path.parent == root and path.name == EXTRACTION_MANIFEST_NAME)
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_write_extraction_manifest`

**Purpose:** Implements `write extraction manifest` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `root` | positional-or-keyword | `Path` | `required` |
| `archive_sha256` | positional-or-keyword | `str` | `required` |
| `files` | positional-or-keyword | `tuple[GpuExtractedFile, ...]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `_write_extraction_manifest`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `_write_extraction_manifest`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `(root / EXTRACTION_MANIFEST_NAME).write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `(root / EXTRACTION_MANIFEST_NAME).write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
    (root / EXTRACTION_MANIFEST_NAME).write_text(
        json.dumps(
            {
                "schema_version": 2,
                "archive_sha256": archive_sha256,
                "files": [
                    {
                        "relative_path": item.relative_path,
                        "size_bytes": item.size_bytes,
                        "sha256": item.sha256,
                    }
                    for item in files
                ],
            },
            sort_keys=True,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_layer_summary`

**Purpose:** Implements `layer summary` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _layer_summary(frame: gpd.GeoDataFrame, source_layer: str) -> GpuLayerSummary:
```

- Exact decorators: none.
- Declared return annotation: `GpuLayerSummary`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `source_layer` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuLayerSummary(<br>        source_document_id="doc-1",<br>        source_archive_sha256="a" * 64,<br>        source_layer=source_layer,<br>        crs=frame.crs.to_string(),<br>        feature_count=len(frame),<br>        columns=tuple(str(column) for column in frame.columns),<br>        dtypes=tuple(<br>            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()<br>        ),<br>        null_counts=tuple(<br>            (str(column), int(frame[column].isna().sum())) for column in frame.columns<br>        ),<br>        geometry_types=tuple(<br>            (str(name), int(count))<br>            for name, count in geometry.geom_type.value_counts().sort_index().items()<br>        ),<br>        null_geometry_count=int((~non_null).sum()),<br>        empty_geometry_count=int((non_null & geometry.is_empty).sum()),<br>        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `_layer_summary`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_planning_document` via `_layer_summary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuLayerSummary` | `landscout.sources.gpu_fr.GpuLayerSummary` |
| `frame.crs.to_string` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna().sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.value_counts().sort_index().items` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.value_counts().sort_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.value_counts` | `unresolved local/third-party receiver; no ownership inferred` |
| `(~non_null).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_null & geometry.is_empty).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_empty & ~geometry.is_valid).sum` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna`<br>`geometry.geom_type.value_counts().sort_index().items`<br>`geometry.geom_type.value_counts().sort_index`<br>`geometry.geom_type.value_counts`<br>`(non_null & geometry.is_empty).sum`<br>`(non_empty & ~geometry.is_valid).sum` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _layer_summary(frame: gpd.GeoDataFrame, source_layer: str) -> GpuLayerSummary:
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    return GpuLayerSummary(
        source_document_id="doc-1",
        source_archive_sha256="a" * 64,
        source_layer=source_layer,
        crs=frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(name), int(count))
            for name, count in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_planning_document`

**Purpose:** Implements `planning document` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _planning_document(
    standard: str = "CNIG PLU v2017",
    related_layers: tuple[GpuInspectedLayer, ...] = (),
) -> GpuPlanningDocument:
```

- Exact decorators: none.
- Declared return annotation: `GpuPlanningDocument`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `standard` | positional-or-keyword | `str` | `'CNIG PLU v2017'` |
| `related_layers` | positional-or-keyword | `tuple[GpuInspectedLayer, ...]` | `()` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuPlanningDocument(<br>        source_config=source_config,<br>        source_config_sha256=gpu_source_module._source_config_sha256(source_config),<br>        extraction=extraction,<br>        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(extraction),<br>        zoning=zoning,<br>        related_layers=related_layers,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_legacy_inputs` via `_planning_document`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_legacy_inputs` via `_planning_document`
- direct call: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `_planning_document`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `_planning_document`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_wrong_planning_standard_is_rejected` via `_planning_document`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_wrong_planning_standard_is_rejected` via `_planning_document`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_multi_geometries_are_accepted` via `_planning_document`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_multi_geometries_are_accepted` via `_planning_document`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_empty_optional_catalogs_preserve_schema_and_crs` via `_planning_document`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_empty_optional_catalogs_preserve_schema_and_crs` via `_planning_document`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_relation_types_are_retained` via `_planning_document`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_relation_types_are_retained` via `_planning_document`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Path` | `pathlib.Path` |
| `tempfile.mkdtemp` | `tempfile.mkdtemp` |
| `layer.data.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.read_file` | `geopandas.read_file` |
| `replace` | `dataclasses.replace` |
| `physical_layers.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_layer_summary` | `tests.unit.test_resolve_planning_feature_codes._layer_summary` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuDocumentMetadata` | `landscout.sources.gpu_fr.GpuDocumentMetadata` |
| `GpuArchiveDownload` | `landscout.sources.gpu_fr.GpuArchiveDownload` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `Polygon` | `shapely.geometry.Polygon` |
| `zoning_data.to_file` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialLayerReference` | `landscout.sources.gpu_fr.GpuSpatialLayerReference` |
| `GpuInspectedLayer` | `landscout.sources.gpu_fr.GpuInspectedLayer` |
| `_physical_inventory` | `tests.unit.test_resolve_planning_feature_codes._physical_inventory` |
| `_write_extraction_manifest` | `tests.unit.test_resolve_planning_feature_codes._write_extraction_manifest` |
| `GpuExtraction` | `landscout.sources.gpu_fr.GpuExtraction` |
| `load_gpu_source_config(<br>        Path("configs/sources/gpu_fr.yaml")<br>    ).model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_gpu_source_config` | `landscout.sources.gpu_fr.load_gpu_source_config` |
| `GpuSourceConfig.model_validate` | `landscout.sources.gpu_fr.GpuSourceConfig.model_validate` |
| `GpuPlanningDocument` | `landscout.sources.gpu_fr.GpuPlanningDocument` |
| `gpu_source_module._source_config_sha256` | `landscout.sources.gpu_fr._source_config_sha256` |
| `gpu_source_module.discover_gpu_spatial_layers` | `landscout.sources.gpu_fr.discover_gpu_spatial_layers` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `gpd.read_file` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `gpu_source_module._source_config_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `physical_layers.append(<br>            replace(<br>                layer,<br>                reference=reference,<br>                data=reread,<br>                summary=_layer_summary(reread, reference.source_layer),<br>            )<br>        )`<br>`config_payload["spatial_layers"][role]["match_tokens"] = [f"unused_{role}"]`<br>`config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONE"]`<br>`config_payload["spatial_layers"][layer.logical_name]["match_tokens"] = [<br>            layer.reference.source_layer<br>        ]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _planning_document(
    standard: str = "CNIG PLU v2017",
    related_layers: tuple[GpuInspectedLayer, ...] = (),
) -> GpuPlanningDocument:
    extraction_root = Path(tempfile.mkdtemp(prefix="landscout-code-source-"))
    physical_layers: list[GpuInspectedLayer] = []
    for layer in related_layers:
        path = extraction_root / f"{layer.logical_name}.gpkg"
        layer.data.to_file(
            path,
            layer=layer.reference.source_layer,
            driver="GPKG",
            engine="pyogrio",
            index=False,
        )
        reread = gpd.read_file(
            path, layer=layer.reference.source_layer, engine="pyogrio"
        )
        reference = replace(
            layer.reference,
            dataset_path=path,
            driver="GPKG",
        )
        physical_layers.append(
            replace(
                layer,
                reference=reference,
                data=reread,
                summary=_layer_summary(reread, reference.source_layer),
            )
        )
    related_layers = tuple(physical_layers)
    document = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="G\u00e9oportail de l'Urbanisme",
        commune_code="31395",
        partition="DU_31395",
        document_id="doc-1",
        document_family="DU",
        document_type="PLU",
        document_title=None,
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name="31395_PLU_20240215",
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=None,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395",
        written_files=(),
    )
    archive = GpuArchiveDownload(
        document=document,
        download_timestamp="2026-08-12T00:00:00Z",
        filename="31395_PLU_20240215.zip",
        archive_format="zip",
        file_size=1,
        sha256="a" * 64,
        path=Path("synthetic.zip"),
        cache_hit=True,
    )
    zoning_data = gpd.GeoDataFrame(
        {"LIB_IDZONE": ["Z1"]},
        geometry=[Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])],
        crs="EPSG:2154",
    )
    zoning_path = extraction_root / "zones.gpkg"
    zoning_data.to_file(
        zoning_path,
        layer="ZONE",
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    zoning_data = gpd.read_file(zoning_path, layer="ZONE", engine="pyogrio")
    reference = GpuSpatialLayerReference(zoning_path, "ZONE", "GPKG")
    summary = _layer_summary(zoning_data, "ZONE")
    zoning = GpuInspectedLayer("zoning", reference, zoning_data, summary)
    inventory = _physical_inventory(extraction_root)
    _write_extraction_manifest(extraction_root, archive.sha256, inventory)
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=extraction_root,
        files=inventory,
        standard_models=(standard,),
        cache_hit=True,
    )
    config_payload = load_gpu_source_config(
        Path("configs/sources/gpu_fr.yaml")
    ).model_dump(mode="python")
    for role in config_payload["spatial_layers"]:
        config_payload["spatial_layers"][role]["match_tokens"] = [f"unused_{role}"]
    config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONE"]
    for layer in related_layers:
        config_payload["spatial_layers"][layer.logical_name]["match_tokens"] = [
            layer.reference.source_layer
        ]
    source_config = GpuSourceConfig.model_validate(config_payload)
    related_by_logical_name = {layer.logical_name: layer for layer in related_layers}
    related_layers = tuple(
        related_by_logical_name[logical_name]
        for logical_name in gpu_source_module._GPU_LOGICAL_LAYER_NAMES
        if logical_name != "zoning" and logical_name in related_by_logical_name
    )
    return GpuPlanningDocument(
        source_config=source_config,
        source_config_sha256=gpu_source_module._source_config_sha256(source_config),
        extraction=extraction,
        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(extraction),
        zoning=zoning,
        related_layers=related_layers,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_base_row`

**Purpose:** Implements `base row` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _base_row(
    feature_id: str,
    source_id: str,
    family: str,
    layer: str,
    kind: str,
    type_code: str,
    subtype_code: str,
) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `feature_id` | positional-or-keyword | `str` | `required` |
| `source_id` | positional-or-keyword | `str` | `required` |
| `family` | positional-or-keyword | `str` | `required` |
| `layer` | positional-or-keyword | `str` | `required` |
| `kind` | positional-or-keyword | `str` | `required` |
| `type_code` | positional-or-keyword | `str` | `required` |
| `subtype_code` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "planning_feature_id": feature_id,<br>        "source_feature_id": source_id,<br>        "source_identity_kind": "CNIG_ATTRIBUTE",<br>        "source_identity_field": "LIB_IDPSC"<br>        if family == "PRESCRIPTION"<br>        else "LIB_IDINFO",<br>        "logical_layer": layer,<br>        "feature_family": family,<br>        "geometry_kind": kind,<br>        "type_code_raw": type_code,<br>        "subtype_code_raw": subtype_code,<br>        "label_raw": None,<br>        "text_raw": None,<br>        "regulation_filename_raw": None,<br>        "regulation_url_raw": None,<br>        "source_document_reference_raw": "31395_PLU_20240215",<br>        "source_validity_date_raw": "20240215",<br>        "source_provider": "Géoportail de l'Urbanisme",<br>        "source_portal": "https://www.geoportail-urbanisme.gouv.fr",<br>        "source_commune_code": "31395",<br>        "source_document_id": "doc-1",<br>        "source_document_type": "PLU",<br>        "source_archive_name": "31395_PLU_20240215",<br>        "source_archive_sha256": "a" * 64,<br>        "source_layer": layer.upper(),<br>        "source_standard_model": "CNIG PLU v2017",<br>        "source_crs": "EPSG:2154",<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_legacy_inputs` via `_base_row`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_legacy_inputs` via `_base_row`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `layer.upper` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _base_row(
    feature_id: str,
    source_id: str,
    family: str,
    layer: str,
    kind: str,
    type_code: str,
    subtype_code: str,
) -> dict[str, object]:
    return {
        "planning_feature_id": feature_id,
        "source_feature_id": source_id,
        "source_identity_kind": "CNIG_ATTRIBUTE",
        "source_identity_field": "LIB_IDPSC"
        if family == "PRESCRIPTION"
        else "LIB_IDINFO",
        "logical_layer": layer,
        "feature_family": family,
        "geometry_kind": kind,
        "type_code_raw": type_code,
        "subtype_code_raw": subtype_code,
        "label_raw": None,
        "text_raw": None,
        "regulation_filename_raw": None,
        "regulation_url_raw": None,
        "source_document_reference_raw": "31395_PLU_20240215",
        "source_validity_date_raw": "20240215",
        "source_provider": "Géoportail de l'Urbanisme",
        "source_portal": "https://www.geoportail-urbanisme.gouv.fr",
        "source_commune_code": "31395",
        "source_document_id": "doc-1",
        "source_document_type": "PLU",
        "source_archive_name": "31395_PLU_20240215",
        "source_archive_sha256": "a" * 64,
        "source_layer": layer.upper(),
        "source_standard_model": "CNIG PLU v2017",
        "source_crs": "EPSG:2154",
    }
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_legacy_inputs`

**Purpose:** Implements `legacy inputs` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _legacy_inputs():
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `_planning_document(), surface, line, point, relations, _profile()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_base_row` | `tests.unit.test_resolve_planning_feature_codes._base_row` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `Polygon` | `shapely.geometry.Polygon` |
| `pd.Index` | `pandas.Index` |
| `LineString` | `shapely.geometry.LineString` |
| `Point` | `shapely.geometry.Point` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_planning_document` | `tests.unit.test_resolve_planning_feature_codes._planning_document` |
| `_profile` | `tests.unit.test_resolve_planning_feature_codes._profile` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface["feature_area_m2"] = [4.0, 4.0]`<br>`line["feature_length_m"] = [2.0]`<br>`point["point_member_count"] = [1]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _legacy_inputs():
    surface_rows = [
        _base_row(
            "F-P-0700",
            "P-1",
            "PRESCRIPTION",
            "prescription_surface",
            "SURFACE",
            "07",
            "00",
        ),
        _base_row(
            "F-I-0200",
            "I-1",
            "INFORMATION",
            "information_surface",
            "SURFACE",
            "02",
            "00",
        ),
    ]
    surface = gpd.GeoDataFrame(
        surface_rows,
        geometry=[
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),
            Polygon([(3, 0), (5, 0), (5, 2), (3, 2)]),
        ],
        crs="EPSG:2154",
        index=pd.Index([11, 22], name="source_row"),
    )
    surface["feature_area_m2"] = [4.0, 4.0]
    line = gpd.GeoDataFrame(
        [
            _base_row(
                "F-P-0704",
                "P-2",
                "PRESCRIPTION",
                "prescription_line",
                "LINE",
                "07",
                "04",
            )
        ],
        geometry=[LineString([(0, 0), (2, 0)])],
        crs="EPSG:2154",
        index=pd.Index([33], name="source_row"),
    )
    line["feature_length_m"] = [2.0]
    point = gpd.GeoDataFrame(
        [
            _base_row(
                "F-I-9900",
                "I-2",
                "INFORMATION",
                "information_point",
                "POINT",
                "99",
                "00",
            )
        ],
        geometry=[Point(1, 1)],
        crs="EPSG:2154",
        index=pd.Index([44], name="source_row"),
    )
    point["point_member_count"] = [1]
    relations = pd.DataFrame(
        [
            {
                "parcel_id": "PARCEL-1",
                **{
                    key: surface.iloc[0][key]
                    for key in (
                        "planning_feature_id",
                        "source_feature_id",
                        "source_identity_kind",
                        "source_identity_field",
                        "logical_layer",
                        "feature_family",
                        "geometry_kind",
                        "type_code_raw",
                        "subtype_code_raw",
                        "label_raw",
                        "text_raw",
                        "source_document_id",
                        "source_archive_sha256",
                        "source_layer",
                        "source_validity_date_raw",
                        "regulation_filename_raw",
                    )
                },
                "relation_type": "AREA_OVERLAP",
                "parcel_metric_area_m2": 4.0,
                "feature_area_m2": 4.0,
                "source_line_length_m": None,
                "intersection_area_m2": 4.0,
                "intersection_length_m": None,
                "parcel_share_pct": 100.0,
                "feature_share_pct": 100.0,
                "point_member_count": None,
                "point_members_inside_count": None,
                "point_members_boundary_count": None,
            },
            {
                "parcel_id": "PARCEL-1",
                **{
                    key: line.iloc[0][key]
                    for key in (
                        "planning_feature_id",
                        "source_feature_id",
                        "source_identity_kind",
                        "source_identity_field",
                        "logical_layer",
                        "feature_family",
                        "geometry_kind",
                        "type_code_raw",
                        "subtype_code_raw",
                        "label_raw",
                        "text_raw",
                        "source_document_id",
                        "source_archive_sha256",
                        "source_layer",
                        "source_validity_date_raw",
                        "regulation_filename_raw",
                    )
                },
                "relation_type": "LENGTH_OVERLAP",
                "parcel_metric_area_m2": 4.0,
                "feature_area_m2": None,
                "source_line_length_m": 2.0,
                "intersection_area_m2": None,
                "intersection_length_m": 2.0,
                "parcel_share_pct": None,
                "feature_share_pct": None,
                "point_member_count": None,
                "point_members_inside_count": None,
                "point_members_boundary_count": None,
            },
        ],
        index=pd.Index([101, 102], name="relation_row"),
    )
    relations = relations.loc[:, list(RELATION_COLUMNS)]
    return _planning_document(), surface, line, point, relations, _profile()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_mutated_profile`

**Purpose:** Build a deliberately unvalidated frozen profile for boundary tests.

**Exact signature**

```python
def _mutated_profile(**updates: object) -> CnigFeatureCodeProfile:
```

- Exact decorators: none.
- Declared return annotation: `CnigFeatureCodeProfile`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `**updates` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `profile.model_copy(update=updates)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated` via `_mutated_profile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated` via `_mutated_profile`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_profile` | `tests.unit.test_resolve_planning_feature_codes._profile` |
| `profile.model_copy` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _mutated_profile(**updates: object) -> CnigFeatureCodeProfile:
    """Build a deliberately unvalidated frozen profile for boundary tests."""

    profile = _profile()
    return profile.model_copy(update=updates)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_empty_catalog`

**Purpose:** Return an optional empty catalog with the deterministic source schema.

**Exact signature**

```python
def _empty_catalog(kind: str) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `kind` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `template.iloc[0:0].copy()`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `template.iloc[0:0].copy` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _empty_catalog(kind: str) -> gpd.GeoDataFrame:
    """Return an optional empty catalog with the deterministic source schema."""

    _, surface, line, point, _, _ = _inputs()
    template = {"SURFACE": surface, "LINE": line, "POINT": point}[kind]
    return template.iloc[0:0].copy()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_integration_source_frame`

**Purpose:** Implements `integration source frame` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _integration_source_frame(
    logical_layer: str,
    geometries: list[object],
    source_ids: list[str],
    type_codes: list[str],
    subtype_codes: list[str],
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `logical_layer` | positional-or-keyword | `str` | `required` |
| `geometries` | positional-or-keyword | `list[object]` | `required` |
| `source_ids` | positional-or-keyword | `list[str]` | `required` |
| `type_codes` | positional-or-keyword | `list[str]` | `required` |
| `subtype_codes` | positional-or-keyword | `list[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {<br>            "LIBELLE": [f"Label {identifier}" for identifier in source_ids],<br>            "TXT": [None] * len(source_ids),<br>            ("TYPEPSC" if prescription else "TYPEINF"): type_codes,<br>            ("STYPEPSC" if prescription else "STYPEINF"): subtype_codes,<br>            "NOMFIC": [None] * len(source_ids),<br>            "URLFIC": [None] * len(source_ids),<br>            "IDURBA": ["31395_PLU_20240215"] * len(source_ids),<br>            "DATVALID": ["20240215"] * len(source_ids),<br>            ("LIB_IDPSC" if prescription else "LIB_IDINFO"): source_ids,<br>        },<br>        geometry=geometries,<br>        crs="EPSG:2154",<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `_integration_source_frame`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `_integration_source_frame`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_relation_types_are_retained` via `_integration_source_frame`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_relation_types_are_retained` via `_integration_source_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `logical_layer.startswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _integration_source_frame(
    logical_layer: str,
    geometries: list[object],
    source_ids: list[str],
    type_codes: list[str],
    subtype_codes: list[str],
) -> gpd.GeoDataFrame:
    prescription = logical_layer.startswith("prescription")
    return gpd.GeoDataFrame(
        {
            "LIBELLE": [f"Label {identifier}" for identifier in source_ids],
            "TXT": [None] * len(source_ids),
            ("TYPEPSC" if prescription else "TYPEINF"): type_codes,
            ("STYPEPSC" if prescription else "STYPEINF"): subtype_codes,
            "NOMFIC": [None] * len(source_ids),
            "URLFIC": [None] * len(source_ids),
            "IDURBA": ["31395_PLU_20240215"] * len(source_ids),
            "DATVALID": ["20240215"] * len(source_ids),
            ("LIB_IDPSC" if prescription else "LIB_IDINFO"): source_ids,
        },
        geometry=geometries,
        crs="EPSG:2154",
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_integration_layer`

**Purpose:** Implements `integration layer` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _integration_layer(
    logical_layer: str,
    frame: gpd.GeoDataFrame,
) -> GpuInspectedLayer:
```

- Exact decorators: none.
- Declared return annotation: `GpuInspectedLayer`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `logical_layer` | positional-or-keyword | `str` | `required` |
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `GpuInspectedLayer(logical_layer, reference, frame, summary)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `_integration_layer`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `_integration_layer`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_multi_geometries_are_accepted` via `_integration_layer`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_multi_geometries_are_accepted` via `_integration_layer`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_relation_types_are_retained` via `_integration_layer`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_relation_types_are_retained` via `_integration_layer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `logical_layer.upper` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuSpatialLayerReference` | `landscout.sources.gpu_fr.GpuSpatialLayerReference` |
| `Path` | `pathlib.Path` |
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuLayerSummary` | `landscout.sources.gpu_fr.GpuLayerSummary` |
| `frame.crs.to_string` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.dtypes.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna().sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.value_counts().sort_index().items` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.value_counts().sort_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.value_counts` | `unresolved local/third-party receiver; no ownership inferred` |
| `(~non_null).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_null & geometry.is_empty).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `(non_empty & ~geometry.is_valid).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `GpuInspectedLayer` | `landscout.sources.gpu_fr.GpuInspectedLayer` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `geometry.isna`<br>`geometry.geom_type.value_counts().sort_index().items`<br>`geometry.geom_type.value_counts().sort_index`<br>`geometry.geom_type.value_counts`<br>`(non_null & geometry.is_empty).sum`<br>`(non_empty & ~geometry.is_valid).sum` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _integration_layer(
    logical_layer: str,
    frame: gpd.GeoDataFrame,
) -> GpuInspectedLayer:
    source_layer = logical_layer.upper()
    reference = GpuSpatialLayerReference(
        Path(f"{logical_layer}.gpkg"), source_layer, "GPKG"
    )
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    summary = GpuLayerSummary(
        source_document_id="doc-1",
        source_archive_sha256="a" * 64,
        source_layer=source_layer,
        crs=frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(name), int(count))
            for name, count in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )
    return GpuInspectedLayer(logical_layer, reference, frame, summary)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_integration_inputs`

**Purpose:** Implements `integration inputs` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _integration_inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, pd.DataFrame, CnigFeatureCodeProfile]`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `(<br>        planning_document,<br>        parcels,<br>        normalized.surface_features,<br>        normalized.line_features,<br>        normalized.point_features,<br>        normalized.relations,<br>        _profile(),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_inputs` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_inputs` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_multi_geometries_are_accepted` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_multi_geometries_are_accepted` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_empty_optional_catalogs_preserve_schema_and_crs` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_empty_optional_catalogs_preserve_schema_and_crs` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_step_7d_3_1_output_integrates_with_public_coding_api` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_step_7d_3_1_output_integrates_with_public_coding_api` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_coded_result_persists_all_source_input_hashes` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_coded_result_persists_all_source_input_hashes` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_source_input_hash_mutation_is_rejected` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_source_input_hash_mutation_is_rejected` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_gpu_related_source_hash_is_deterministic_across_cache_roots` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_gpu_related_source_hash_is_deterministic_across_cache_roots` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_source_binding_hashes_bind_every_component_hash` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_source_binding_hashes_bind_every_component_hash` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_parcel_source_change_invalidates_coded_result` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_parcel_source_change_invalidates_coded_result` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_gpu_document_context_change_invalidates_coded_result` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_gpu_document_context_change_invalidates_coded_result` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_normalized_relation_change_invalidates_coded_result` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_normalized_relation_change_invalidates_coded_result` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_coding_api_rejects_relation_set_not_rebuilt_from_geometry` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_coding_api_rejects_relation_set_not_rebuilt_from_geometry` via `_integration_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_parquet_readback_preserves_source_hash_envelope` via `_integration_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_parquet_readback_preserves_source_hash_envelope` via `_integration_inputs`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_layer` | `tests.unit.test_resolve_planning_feature_codes._integration_layer` |
| `_integration_source_frame` | `tests.unit.test_resolve_planning_feature_codes._integration_source_frame` |
| `Polygon` | `shapely.geometry.Polygon` |
| `LineString` | `shapely.geometry.LineString` |
| `Point` | `shapely.geometry.Point` |
| `_planning_document` | `tests.unit.test_resolve_planning_feature_codes._planning_document` |
| `_integration_parcels` | `tests.unit.test_resolve_planning_feature_codes._integration_parcels` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |
| `_profile` | `tests.unit.test_resolve_planning_feature_codes._profile` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _integration_inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
    layers = (
        _integration_layer(
            "prescription_surface",
            _integration_source_frame(
                "prescription_surface",
                [Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])],
                ["P-1"],
                ["07"],
                ["00"],
            ),
        ),
        _integration_layer(
            "information_surface",
            _integration_source_frame(
                "information_surface",
                [Polygon([(3, 0), (5, 0), (5, 2), (3, 2)])],
                ["I-1"],
                ["02"],
                ["00"],
            ),
        ),
        _integration_layer(
            "prescription_line",
            _integration_source_frame(
                "prescription_line",
                [LineString([(0, 1), (2, 1)])],
                ["P-2"],
                ["07"],
                ["04"],
            ),
        ),
        _integration_layer(
            "information_point",
            _integration_source_frame(
                "information_point",
                [Point(10, 10)],
                ["I-2"],
                ["99"],
                ["00"],
            ),
        ),
    )
    planning_document = _planning_document(related_layers=layers)
    parcels = _integration_parcels()
    normalized = intersect_parcels_with_gpu_planning_features(
        parcels, planning_document
    )
    return (
        planning_document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        _profile(),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_integration_parcels`

**Purpose:** Implements `integration parcels` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _integration_parcels() -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `gpd.GeoDataFrame(<br>        {"parcel_id": ["PARCEL-1"], "existing_fact": [7]},<br>        geometry=[Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])],<br>        crs="EPSG:2154",<br>        index=pd.Index([91], name="parcel_row"),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `_integration_parcels`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `_integration_parcels`
- direct call: `tests.unit.test_resolve_planning_feature_codes::resolve_planning_feature_codes` via `_integration_parcels`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::resolve_planning_feature_codes` via `_integration_parcels`
- direct call: `tests.unit.test_resolve_planning_feature_codes::validate_planning_feature_code_result` via `_integration_parcels`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::validate_planning_feature_code_result` via `_integration_parcels`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_relation_types_are_retained` via `_integration_parcels`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_relation_types_are_retained` via `_integration_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `Polygon` | `shapely.geometry.Polygon` |
| `pd.Index` | `pandas.Index` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _integration_parcels() -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {"parcel_id": ["PARCEL-1"], "existing_fact": [7]},
        geometry=[Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])],
        crs="EPSG:2154",
        index=pd.Index([91], name="parcel_row"),
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_inputs`

**Purpose:** Implements `inputs` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[GpuPlanningDocument, gpd.GeoDataFrame, gpd.GeoDataFrame, gpd.GeoDataFrame, pd.DataFrame, CnigFeatureCodeProfile]`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `document, surface, line, point, relations, profile`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::_empty_catalog` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_empty_catalog` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_exact_family_pair_resolution_and_leading_zeros` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_exact_family_pair_resolution_and_leading_zeros` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_wrong_planning_standard_is_rejected` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_wrong_planning_standard_is_rejected` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_catalogs_and_relations_are_preserved_and_inputs_immutable` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_catalogs_and_relations_are_preserved_and_inputs_immutable` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_complete_normalized_catalog_schema_is_required` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_complete_normalized_catalog_schema_is_required` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_unexpected_factual_catalog_column_is_rejected` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_unexpected_factual_catalog_column_is_rejected` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_cnig_identity_provenance_is_exact` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_cnig_identity_provenance_is_exact` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_ogr_fid_provenance_is_restricted` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_ogr_fid_provenance_is_restricted` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_source_feature_id_is_unique_inside_logical_layer` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_source_feature_id_is_unique_inside_logical_layer` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_catalog_crs_must_be_canonical_epsg_2154` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_catalog_crs_must_be_canonical_epsg_2154` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_catalog_geometry_metrics_are_revalidated` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_catalog_geometry_metrics_are_revalidated` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_complete_relation_schema_is_required` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_complete_relation_schema_is_required` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_unexpected_factual_relation_column_is_rejected` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_unexpected_factual_relation_column_is_rejected` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_cnig_resolver_invokes_shared_factual_contract` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_cnig_resolver_invokes_shared_factual_contract` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_complete_relation_catalog_agreement_is_required` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_complete_relation_catalog_agreement_is_required` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_surface_relation_metrics_are_revalidated` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_surface_relation_metrics_are_revalidated` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_line_relation_metrics_are_revalidated` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_line_relation_metrics_are_revalidated` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_catalog_columns_are_rejected` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_catalog_columns_are_rejected` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_missing_catalog_crs_is_rejected` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_missing_catalog_crs_is_rejected` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_unparseable_catalog_crs_is_rejected` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_unparseable_catalog_crs_is_rejected` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_inactive_or_wrong_geometry_column_is_rejected` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_inactive_or_wrong_geometry_column_is_rejected` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_surface_geometry_contract_is_enforced` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_surface_geometry_contract_is_enforced` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_catalog_semantic_and_string_contracts_are_enforced` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_catalog_semantic_and_string_contracts_are_enforced` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_every_required_catalog_identity_is_an_exact_non_null_string` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_every_required_catalog_identity_is_an_exact_non_null_string` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_line_and_point_geometry_types_are_enforced` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_line_and_point_geometry_types_are_enforced` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_planning_feature_ids_are_globally_unique_across_catalogs` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_planning_feature_ids_are_globally_unique_across_catalogs` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_relation_catalog_code_mismatch_is_rejected` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_relation_catalog_code_mismatch_is_rejected` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_relation_columns_are_rejected` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_relation_columns_are_rejected` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_relation_identity_must_be_an_exact_non_null_string` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_relation_identity_must_be_an_exact_non_null_string` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_parcel_feature_relation_is_rejected` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_parcel_feature_relation_is_rejected` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_unknown_relation_feature_id_is_rejected` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_unknown_relation_feature_id_is_rejected` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_relation_type_must_match_catalog_geometry_kind` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_relation_type_must_match_catalog_geometry_kind` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_coordinated_output_hash_mutation_is_rejected` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_coordinated_output_hash_mutation_is_rejected` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_parquet_readback_passes_source_complete_validation` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_parquet_readback_passes_source_complete_validation` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_result_schema_versions_are_strict` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_result_schema_versions_are_strict` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator` via `_inputs`
- direct call: `tests.unit.test_resolve_planning_feature_codes::_schema_v5_envelope_result` via `_inputs`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_schema_v5_envelope_result` via `_inputs`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
    document, _, surface, line, point, relations, profile = _integration_inputs()
    return document, surface, line, point, relations, profile
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `resolve_planning_feature_codes`

**Purpose:** Exercise the new bound API while keeping legacy unit call sites compact.

**Exact signature**

```python
def resolve_planning_feature_codes(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
) -> PlanningFeatureCodeResult:
```

- Exact decorators: none.
- Declared return annotation: `PlanningFeatureCodeResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `surface_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `line_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `point_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `code_profile` | positional-or-keyword | `CnigFeatureCodeProfile \| str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_public_resolve_planning_feature_codes(<br>        planning_document,<br>        _integration_parcels(),<br>        surface_features,<br>        line_features,<br>        point_features,<br>        relations,<br>        code_profile,<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_exact_family_pair_resolution_and_leading_zeros` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_exact_family_pair_resolution_and_leading_zeros` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_wrong_planning_standard_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_wrong_planning_standard_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_catalogs_and_relations_are_preserved_and_inputs_immutable` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_catalogs_and_relations_are_preserved_and_inputs_immutable` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_complete_normalized_catalog_schema_is_required` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_complete_normalized_catalog_schema_is_required` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_unexpected_factual_catalog_column_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_unexpected_factual_catalog_column_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_cnig_identity_provenance_is_exact` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_cnig_identity_provenance_is_exact` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_ogr_fid_provenance_is_restricted` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_ogr_fid_provenance_is_restricted` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_source_feature_id_is_unique_inside_logical_layer` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_source_feature_id_is_unique_inside_logical_layer` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_catalog_crs_must_be_canonical_epsg_2154` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_catalog_crs_must_be_canonical_epsg_2154` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_catalog_geometry_metrics_are_revalidated` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_catalog_geometry_metrics_are_revalidated` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_complete_relation_schema_is_required` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_complete_relation_schema_is_required` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_unexpected_factual_relation_column_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_unexpected_factual_relation_column_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_cnig_resolver_invokes_shared_factual_contract` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_cnig_resolver_invokes_shared_factual_contract` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_complete_relation_catalog_agreement_is_required` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_complete_relation_catalog_agreement_is_required` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_surface_relation_metrics_are_revalidated` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_surface_relation_metrics_are_revalidated` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_line_relation_metrics_are_revalidated` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_line_relation_metrics_are_revalidated` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_catalog_columns_are_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_catalog_columns_are_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_missing_catalog_crs_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_missing_catalog_crs_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_unparseable_catalog_crs_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_unparseable_catalog_crs_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_inactive_or_wrong_geometry_column_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_inactive_or_wrong_geometry_column_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_surface_geometry_contract_is_enforced` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_surface_geometry_contract_is_enforced` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_catalog_semantic_and_string_contracts_are_enforced` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_catalog_semantic_and_string_contracts_are_enforced` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_every_required_catalog_identity_is_an_exact_non_null_string` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_every_required_catalog_identity_is_an_exact_non_null_string` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_line_and_point_geometry_types_are_enforced` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_line_and_point_geometry_types_are_enforced` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_planning_feature_ids_are_globally_unique_across_catalogs` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_planning_feature_ids_are_globally_unique_across_catalogs` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_relation_catalog_code_mismatch_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_relation_catalog_code_mismatch_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_relation_columns_are_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_relation_columns_are_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_relation_identity_must_be_an_exact_non_null_string` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_relation_identity_must_be_an_exact_non_null_string` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_parcel_feature_relation_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_parcel_feature_relation_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_unknown_relation_feature_id_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_unknown_relation_feature_id_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_relation_type_must_match_catalog_geometry_kind` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_relation_type_must_match_catalog_geometry_kind` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_coordinated_output_hash_mutation_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_coordinated_output_hash_mutation_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_parquet_readback_passes_source_complete_validation` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_parquet_readback_passes_source_complete_validation` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_result_schema_versions_are_strict` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_result_schema_versions_are_strict` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::_schema_v5_envelope_result` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_schema_v5_envelope_result` via `resolve_planning_feature_codes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_integration_parcels` | `tests.unit.test_resolve_planning_feature_codes._integration_parcels` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def resolve_planning_feature_codes(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
) -> PlanningFeatureCodeResult:
    """Exercise the new bound API while keeping legacy unit call sites compact."""

    return _public_resolve_planning_feature_codes(
        planning_document,
        _integration_parcels(),
        surface_features,
        line_features,
        point_features,
        relations,
        code_profile,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `validate_planning_feature_code_result`

**Purpose:** Implements `validate planning feature code result` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def validate_planning_feature_code_result(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    result: PlanningFeatureCodeResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `surface_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `line_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `point_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `code_profile` | positional-or-keyword | `CnigFeatureCodeProfile \| str \| Path` | `required` |
| `result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_coordinated_output_hash_mutation_is_rejected` via `validate_planning_feature_code_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_coordinated_output_hash_mutation_is_rejected` via `validate_planning_feature_code_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_parquet_readback_passes_source_complete_validation` via `validate_planning_feature_code_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_parquet_readback_passes_source_complete_validation` via `validate_planning_feature_code_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_result_schema_versions_are_strict` via `validate_planning_feature_code_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_result_schema_versions_are_strict` via `validate_planning_feature_code_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_public_validate_planning_feature_code_result` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result` |
| `_integration_parcels` | `tests.unit.test_resolve_planning_feature_codes._integration_parcels` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def validate_planning_feature_code_result(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    result: PlanningFeatureCodeResult,
) -> None:
    _public_validate_planning_feature_code_result(
        planning_document,
        _integration_parcels(),
        surface_features,
        line_features,
        point_features,
        relations,
        code_profile,
        result,
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_exact_family_pair_resolution_and_leading_zeros`

**Purpose:** Regression invariant: exact family pair resolution and leading zeros. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_exact_family_pair_resolution_and_leading_zeros() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        surface.loc["GPU:doc-1:prescription_surface:P-1", "official_code_label"]<br>        == "Prescription seven"<br>    )`
  - `assert (<br>        surface.loc["GPU:doc-1:information_surface:I-1", "official_code_label"]<br>        == "Information two"<br>    )`
  - `assert (<br>        result.line_features.iloc[0]["official_code_label"]<br>        == "Prescription seven subtype four"<br>    )`
  - `assert result.line_features.iloc[0]["type_code_raw"] == "07"`
  - `assert result.line_features.iloc[0]["subtype_code_raw"] == "04"`
  - `assert set(surface["official_code_status"]) == {"RESOLVED_OFFICIAL"}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `result.surface_features.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_exact_family_pair_resolution_and_leading_zeros() -> None:
    result = resolve_planning_feature_codes(*_inputs())
    surface = result.surface_features.set_index("planning_feature_id")
    assert (
        surface.loc["GPU:doc-1:prescription_surface:P-1", "official_code_label"]
        == "Prescription seven"
    )
    assert (
        surface.loc["GPU:doc-1:information_surface:I-1", "official_code_label"]
        == "Information two"
    )
    assert (
        result.line_features.iloc[0]["official_code_label"]
        == "Prescription seven subtype four"
    )
    assert result.line_features.iloc[0]["type_code_raw"] == "07"
    assert result.line_features.iloc[0]["subtype_code_raw"] == "04"
    assert set(surface["official_code_status"]) == {"RESOLVED_OFFICIAL"}
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_no_type_only_or_cross_family_fallback_and_unknown_is_retained`

**Purpose:** Regression invariant: no type only or cross family fallback and unknown is retained. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_no_type_only_or_cross_family_fallback_and_unknown_is_retained() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.line_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"`
  - `assert pd.isna(result.line_features.iloc[0]["official_code_label"])`
  - `assert result.point_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"`
  - `assert len(result.line_features) == 1`
  - `assert len(result.point_features) == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `_profile_payload` | `tests.unit.test_resolve_planning_feature_codes._profile_payload` |
| `_records_hash` | `tests.unit.test_resolve_planning_feature_codes._records_hash` |
| `CnigFeatureCodeProfile.model_validate` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.model_validate` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pd.isna` | `pandas.isna` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_records_hash` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["records"] = [<br>        record<br>        for record in payload["records"]<br>        if not (<br>            (record["feature_family"], record["type_code"], record["subtype_code"])<br>            in {("PRESCRIPTION", "07", "04"), ("INFORMATION", "99", "00")}<br>        )<br>    ]`<br>`payload["canonical_records_sha256"] = _records_hash(payload["records"])` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_no_type_only_or_cross_family_fallback_and_unknown_is_retained() -> None:
    document, surface, line, point, relations, profile = _inputs()
    payload = _profile_payload()
    payload["records"] = [
        record
        for record in payload["records"]
        if not (
            (record["feature_family"], record["type_code"], record["subtype_code"])
            in {("PRESCRIPTION", "07", "04"), ("INFORMATION", "99", "00")}
        )
    ]
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    profile = CnigFeatureCodeProfile.model_validate(payload)
    result = resolve_planning_feature_codes(
        document, surface, line, point, relations, profile
    )
    assert result.line_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"
    assert pd.isna(result.line_features.iloc[0]["official_code_label"])
    assert result.point_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"
    assert len(result.line_features) == 1
    assert len(result.point_features) == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated`

**Purpose:** Regression invariant: in memory profile model copy with wrong hash is revalidated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="profile\|canonical")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `_mutated_profile` | `tests.unit.test_resolve_planning_feature_codes._mutated_profile` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `inputs[-1] = _mutated_profile(canonical_records_sha256="f" * 64)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated() -> None:
    inputs = list(_inputs())
    inputs[-1] = _mutated_profile(canonical_records_sha256="f" * 64)
    with pytest.raises(PlanningFeatureCodeError, match="profile|canonical"):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated`

**Purpose:** Regression invariant: in memory profile model construct with invalid schema is revalidated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="schema\|profile")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_profile` | `tests.unit.test_resolve_planning_feature_codes._profile` |
| `CnigFeatureCodeProfile.model_construct` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.model_construct` |
| `profile.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `inputs[-1] = invalid` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated() -> None:
    profile = _profile()
    invalid = CnigFeatureCodeProfile.model_construct(
        **{**profile.model_dump(mode="python"), "schema_version": 1}
    )
    inputs = list(_inputs())
    inputs[-1] = invalid
    with pytest.raises(PlanningFeatureCodeError, match="schema|profile"):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated`

**Purpose:** Regression invariant: in memory profile model construct with duplicate pair is revalidated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="duplicate\|profile")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_profile` | `tests.unit.test_resolve_planning_feature_codes._profile` |
| `CnigFeatureCodeProfile.model_construct` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.model_construct` |
| `profile.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `inputs[-1] = invalid` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated() -> None:
    profile = _profile()
    invalid = CnigFeatureCodeProfile.model_construct(
        **{
            **profile.model_dump(mode="python"),
            "records": (*profile.records, profile.records[0]),
        }
    )
    inputs = list(_inputs())
    inputs[-1] = invalid
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|profile"):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_official_family_endpoints_require_exact_identity`

**Purpose:** Regression invariant: official family endpoints require exact identity. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_official_family_endpoints_require_exact_identity(
    family: str, url: str
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("family", "url"),
    [
        ("prescription", "https://www.geoportail-urbanisme.gouv.fr/another/path"),
        ("prescription", f"{P_URL}?format=json"),
        (
            "prescription",
            "https://www.geoportail-urbanisme.gouv.fr:444/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        (
            "prescription",
            "https://user@www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        (
            "prescription",
            "https://geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        ("prescription", I_URL),
        ("information", P_URL),
        ("information", f"{I_URL}#codes"),
        ("information", f"{I_URL}/"),
        ("information", I_URL.replace("https://", "http://")),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `family` | positional-or-keyword | `str` | `required` |
| `url` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="official\|source\|URL")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_profile_payload` | `tests.unit.test_resolve_planning_feature_codes._profile_payload` |
| `family.upper` | `unresolved local/third-party receiver; no ownership inferred` |
| `_records_hash` | `tests.unit.test_resolve_planning_feature_codes._records_hash` |
| `pytest.raises` | `pytest.raises` |
| `CnigFeatureCodeProfile.model_validate` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.model_validate` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `I_URL.replace` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `I_URL.replace` |
| Hashing/byte identity | `_records_hash` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["official_sources"][family] = url`<br>`record["official_source_url"] = url`<br>`payload["canonical_records_sha256"] = _records_hash(payload["records"])` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_official_family_endpoints_require_exact_identity(
    family: str, url: str
) -> None:
    payload = _profile_payload()
    payload["official_sources"][family] = url
    family_name = family.upper()
    for record in payload["records"]:
        if record["feature_family"] == family_name:
            record["official_source_url"] = url
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    with pytest.raises(ValueError, match="official|source|URL"):
        CnigFeatureCodeProfile.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_official_text_must_already_be_canonical`

**Purpose:** Regression invariant: official text must already be canonical. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_official_text_must_already_be_canonical(field: str, value: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("official_label", "Repeated  whitespace"),
        ("official_label", "Decomposed e\u0301"),
        ("legal_reference", "L151-1\n  L151-2"),
        ("regulation_or_annex_reference", " R151-1"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        ValueError,<br>        match="GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1\|canonical\|normalization\|exact",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_profile_payload` | `tests.unit.test_resolve_planning_feature_codes._profile_payload` |
| `_records_hash` | `tests.unit.test_resolve_planning_feature_codes._records_hash` |
| `pytest.raises` | `pytest.raises` |
| `CnigFeatureCodeProfile.model_validate` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.model_validate` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_records_hash` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["records"][0][field] = value`<br>`payload["canonical_records_sha256"] = _records_hash(payload["records"])` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_official_text_must_already_be_canonical(field: str, value: str) -> None:
    payload = _profile_payload()
    payload["records"][0][field] = value
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    with pytest.raises(
        ValueError,
        match="GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1|canonical|normalization|exact",
    ):
        CnigFeatureCodeProfile.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_malformed_code_is_rejected`

**Purpose:** Regression invariant: malformed code is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_malformed_code_is_rejected(code: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize("code", ["1", "001", "A1", " 01", "01 ", 1])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `code` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_profile_payload` | `tests.unit.test_resolve_planning_feature_codes._profile_payload` |
| `pytest.raises` | `pytest.raises` |
| `CnigFeatureCodeProfile.model_validate` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.model_validate` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["records"][0]["type_code"] = code` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_malformed_code_is_rejected(code: object) -> None:
    payload = _profile_payload()
    payload["records"][0]["type_code"] = code
    with pytest.raises(ValueError):
        CnigFeatureCodeProfile.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_pair_and_profile_hash_mutation_are_rejected`

**Purpose:** Regression invariant: duplicate pair and profile hash mutation are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_pair_and_profile_hash_mutation_are_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="duplicate")`
  - `pytest.raises(ValueError, match="canonical")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_profile_payload` | `tests.unit.test_resolve_planning_feature_codes._profile_payload` |
| `payload["records"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `CnigFeatureCodeProfile.model_validate` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.model_validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["records"].append(dict(payload["records"][0]))`<br>`payload["canonical_records_sha256"] = "f" * 64` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_pair_and_profile_hash_mutation_are_rejected() -> None:
    payload = _profile_payload()
    payload["records"].append(dict(payload["records"][0]))
    with pytest.raises(ValueError, match="duplicate"):
        CnigFeatureCodeProfile.model_validate(payload)
    payload = _profile_payload()
    payload["canonical_records_sha256"] = "f" * 64
    with pytest.raises(ValueError, match="canonical"):
        CnigFeatureCodeProfile.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_official_host_and_unknown_field_are_rejected`

**Purpose:** Regression invariant: wrong official host and unknown field are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_official_host_and_unknown_field_are_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="official\|exact")`
  - `pytest.raises(ValueError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_profile_payload` | `tests.unit.test_resolve_planning_feature_codes._profile_payload` |
| `pytest.raises` | `pytest.raises` |
| `CnigFeatureCodeProfile.model_validate` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.model_validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["official_sources"]["prescription"] = "https://example.com/codes"`<br>`payload["semantic_policy"] = "BLOCK"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_wrong_official_host_and_unknown_field_are_rejected() -> None:
    payload = _profile_payload()
    payload["official_sources"]["prescription"] = "https://example.com/codes"
    with pytest.raises(ValueError, match="official|exact"):
        CnigFeatureCodeProfile.model_validate(payload)
    payload = _profile_payload()
    payload["semantic_policy"] = "BLOCK"
    with pytest.raises(ValueError):
        CnigFeatureCodeProfile.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_yaml_key_is_rejected`

**Purpose:** Regression invariant: duplicate yaml key is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="Duplicate YAML")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `load_cnig_feature_code_profile` | `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "codes.yaml"
    path.write_text("schema_version: 1\nschema_version: 1\n", encoding="utf-8")
    with pytest.raises(PlanningFeatureCodeError, match="Duplicate YAML"):
        load_cnig_feature_code_profile(path)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_wrong_planning_standard_is_rejected`

**Purpose:** Regression invariant: wrong planning standard is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_wrong_planning_standard_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="standard")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `_planning_document` | `tests.unit.test_resolve_planning_feature_codes._planning_document` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `inputs[0] = _planning_document("CNIG PLU v2022")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_wrong_planning_standard_is_rejected() -> None:
    inputs = list(_inputs())
    inputs[0] = _planning_document("CNIG PLU v2022")
    with pytest.raises(PlanningFeatureCodeError, match="standard"):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_catalogs_and_relations_are_preserved_and_inputs_immutable`

**Purpose:** Regression invariant: catalogs and relations are preserved and inputs immutable. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_catalogs_and_relations_are_preserved_and_inputs_immutable() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS<br>        )`
  - `assert tuple(result.code_dictionary.columns) == CODE_DICTIONARY_COLUMNS`
  - `assert result.relations.index.equals(inputs[4].index)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `frame.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `assert_geodataframe_equal` | `geopandas.testing.assert_geodataframe_equal` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.testing.assert_frame_equal` | `pandas.testing.assert_frame_equal` |
| `result.relations.index.equals` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_catalogs_and_relations_are_preserved_and_inputs_immutable() -> None:
    inputs = _inputs()
    snapshots = [frame.copy(deep=True) for frame in inputs[1:5]]
    result = resolve_planning_feature_codes(*inputs)
    for original, snapshot, coded in zip(
        inputs[1:4],
        snapshots[:3],
        (result.surface_features, result.line_features, result.point_features),
        strict=True,
    ):
        assert_geodataframe_equal(original, snapshot)
        assert_geodataframe_equal(coded.loc[:, original.columns], original)
        assert (
            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS
        )
    pd.testing.assert_frame_equal(inputs[4], snapshots[3])
    pd.testing.assert_frame_equal(result.relations.loc[:, inputs[4].columns], inputs[4])
    assert tuple(result.code_dictionary.columns) == CODE_DICTIONARY_COLUMNS
    assert result.relations.index.equals(inputs[4].index)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_complete_normalized_catalog_schema_is_required`

**Purpose:** Regression invariant: complete normalized catalog schema is required. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_complete_normalized_catalog_schema_is_required(
    catalog_position: int,
    column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("catalog_position", "column"),
    [
        (1, "feature_area_m2"),
        (2, "feature_length_m"),
        (3, "point_member_count"),
        (1, "label_raw"),
        (1, "source_crs"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `catalog_position` | positional-or-keyword | `int` | `required` |
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="normalized\|schema\|column")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `inputs[catalog_position].drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `inputs[catalog_position] = inputs[catalog_position].drop(columns=column)`<br>`inputs[catalog_position].drop(columns=column)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_complete_normalized_catalog_schema_is_required(
    catalog_position: int,
    column: str,
) -> None:
    inputs = list(_inputs())
    inputs[catalog_position] = inputs[catalog_position].drop(columns=column)
    with pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column"):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unexpected_factual_catalog_column_is_rejected`

**Purpose:** Regression invariant: unexpected factual catalog column is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unexpected_factual_catalog_column_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="normalized\|schema\|column")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `inputs[1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface["unexpected_fact"] = "not-produced-by-step-7d-3-1"`<br>`inputs[1] = surface` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unexpected_factual_catalog_column_is_rejected() -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface["unexpected_fact"] = "not-produced-by-step-7d-3-1"
    inputs[1] = surface
    with pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column"):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cnig_identity_provenance_is_exact`

**Purpose:** Regression invariant: cnig identity provenance is exact. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cnig_identity_provenance_is_exact(column: str, value: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_identity_kind", "UNKNOWN_KIND"),
        ("source_identity_field", "LIB_IDINFO"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeatureCodeError, match="identity\|provenance\|normalized"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `inputs[1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.loc[surface.index[0], column] = value`<br>`inputs[1] = surface` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_cnig_identity_provenance_is_exact(column: str, value: str) -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface.loc[surface.index[0], column] = value
    inputs[1] = surface
    with pytest.raises(
        PlanningFeatureCodeError, match="identity|provenance|normalized"
    ):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_ogr_fid_provenance_is_restricted`

**Purpose:** Regression invariant: ogr fid provenance is restricted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_ogr_fid_provenance_is_restricted(
    logical_layer: str,
    feature_family: str,
    source_feature_id: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("logical_layer", "feature_family", "source_feature_id"),
    [
        ("information_surface", "INFORMATION", "OGR_FID:1"),
        ("prescription_surface", "PRESCRIPTION", "1"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `logical_layer` | positional-or-keyword | `str` | `required` |
| `feature_family` | positional-or-keyword | `str` | `required` |
| `source_feature_id` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeatureCodeError, match="OGR\|identity\|provenance\|normalized"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `inputs[1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.loc[row_index, "logical_layer"] = logical_layer`<br>`surface.loc[row_index, "feature_family"] = feature_family`<br>`surface.loc[row_index, "source_identity_kind"] = "ARCHIVE_SCOPED_OGR_FID"`<br>`surface.loc[row_index, "source_identity_field"] = "OGR_FID"`<br>`surface.loc[row_index, "source_feature_id"] = source_feature_id`<br>`inputs[1] = surface` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_ogr_fid_provenance_is_restricted(
    logical_layer: str,
    feature_family: str,
    source_feature_id: str,
) -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    row_index = surface.index[0]
    surface.loc[row_index, "logical_layer"] = logical_layer
    surface.loc[row_index, "feature_family"] = feature_family
    surface.loc[row_index, "source_identity_kind"] = "ARCHIVE_SCOPED_OGR_FID"
    surface.loc[row_index, "source_identity_field"] = "OGR_FID"
    surface.loc[row_index, "source_feature_id"] = source_feature_id
    inputs[1] = surface
    with pytest.raises(
        PlanningFeatureCodeError, match="OGR|identity|provenance|normalized"
    ):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_feature_id_is_unique_inside_logical_layer`

**Purpose:** Regression invariant: source feature id is unique inside logical layer. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_feature_id_is_unique_inside_logical_layer() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="source_feature_id\|unique")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `inputs[1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.loc[surface.index[1], "logical_layer"] = surface.iloc[0]["logical_layer"]`<br>`surface.loc[surface.index[1], "feature_family"] = surface.iloc[0]["feature_family"]`<br>`surface.loc[surface.index[1], "source_identity_field"] = surface.iloc[0][<br>        "source_identity_field"<br>    ]`<br>`surface.loc[surface.index[1], "source_feature_id"] = surface.iloc[0][<br>        "source_feature_id"<br>    ]`<br>`inputs[1] = surface` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_feature_id_is_unique_inside_logical_layer() -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface.loc[surface.index[1], "logical_layer"] = surface.iloc[0]["logical_layer"]
    surface.loc[surface.index[1], "feature_family"] = surface.iloc[0]["feature_family"]
    surface.loc[surface.index[1], "source_identity_field"] = surface.iloc[0][
        "source_identity_field"
    ]
    surface.loc[surface.index[1], "source_feature_id"] = surface.iloc[0][
        "source_feature_id"
    ]
    inputs[1] = surface
    with pytest.raises(PlanningFeatureCodeError, match="source_feature_id|unique"):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_catalog_crs_must_be_canonical_epsg_2154`

**Purpose:** Regression invariant: catalog crs must be canonical epsg 2154. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_catalog_crs_must_be_canonical_epsg_2154() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="EPSG:2154\|CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `inputs[1].to_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `inputs[1].to_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `inputs[1] = inputs[1].to_crs("EPSG:4326")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_catalog_crs_must_be_canonical_epsg_2154() -> None:
    inputs = list(_inputs())
    inputs[1] = inputs[1].to_crs("EPSG:4326")
    with pytest.raises(PlanningFeatureCodeError, match="EPSG:2154|CRS"):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_catalog_geometry_metrics_are_revalidated`

**Purpose:** Regression invariant: catalog geometry metrics are revalidated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_catalog_geometry_metrics_are_revalidated(
    catalog_position: int,
    column: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("catalog_position", "column", "value"),
    [
        (1, "feature_area_m2", 99.0),
        (2, "feature_length_m", 99.0),
        (3, "point_member_count", 2),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `catalog_position` | positional-or-keyword | `int` | `required` |
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="metric\|area\|length\|member")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `inputs[catalog_position].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `catalog.loc[catalog.index[0], column] = value`<br>`inputs[catalog_position] = catalog` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_catalog_geometry_metrics_are_revalidated(
    catalog_position: int,
    column: str,
    value: object,
) -> None:
    inputs = list(_inputs())
    catalog = inputs[catalog_position].copy(deep=True)
    catalog.loc[catalog.index[0], column] = value
    inputs[catalog_position] = catalog
    with pytest.raises(PlanningFeatureCodeError, match="metric|area|length|member"):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_complete_relation_schema_is_required`

**Purpose:** Regression invariant: complete relation schema is required. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_complete_relation_schema_is_required() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="relation\|schema\|column")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `inputs[4].drop` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `inputs[4] = inputs[4].drop(columns="intersection_length_m")`<br>`inputs[4].drop(columns="intersection_length_m")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_complete_relation_schema_is_required() -> None:
    inputs = list(_inputs())
    inputs[4] = inputs[4].drop(columns="intersection_length_m")
    with pytest.raises(PlanningFeatureCodeError, match="relation|schema|column"):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unexpected_factual_relation_column_is_rejected`

**Purpose:** Regression invariant: unexpected factual relation column is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unexpected_factual_relation_column_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="relation\|schema")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `inputs[4].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `relations["unexpected_metric"] = 0.0`<br>`inputs[4] = relations` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unexpected_factual_relation_column_is_rejected() -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations["unexpected_metric"] = 0.0
    inputs[4] = relations
    with pytest.raises(PlanningFeatureCodeError, match="relation|schema"):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cnig_resolver_invokes_shared_factual_contract`

**Purpose:** Regression invariant: cnig resolver invokes shared factual contract. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_cnig_resolver_invokes_shared_factual_contract(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeatureCodeError, match="shared factual contract marker"<br>    )`
- Exact assertions:
  - `assert calls == 1`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_cnig_resolver_invokes_shared_factual_contract(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    calls = 0

    def reject_shared_contract(*args: object) -> None:
        nonlocal calls
        calls += 1
        raise ValueError("shared factual contract marker")

    monkeypatch.setattr(
        coding_module,
        "validate_normalized_planning_feature_inputs",
        reject_shared_contract,
    )
    with pytest.raises(
        PlanningFeatureCodeError, match="shared factual contract marker"
    ):
        resolve_planning_feature_codes(*_inputs())
    assert calls == 1
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_cnig_resolver_invokes_shared_factual_contract.reject_shared_contract`

**Purpose:** Implements `reject shared contract` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def reject_shared_contract(*args: object) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `ValueError("shared factual contract marker")`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def reject_shared_contract(*args: object) -> None:
        nonlocal calls
        calls += 1
        raise ValueError("shared factual contract marker")
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_complete_relation_catalog_agreement_is_required`

**Purpose:** Regression invariant: complete relation catalog agreement is required. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_complete_relation_catalog_agreement_is_required(
    column: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("label_raw", "mutated label"),
        ("source_validity_date_raw", "19990101"),
        ("regulation_filename_raw", "other.pdf"),
        ("feature_area_m2", 3.0),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeatureCodeError, match="catalog\|metric\|normalized\|feature share"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `inputs[4].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[relations.index[0], column] = value`<br>`inputs[4] = relations` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_complete_relation_catalog_agreement_is_required(
    column: str,
    value: object,
) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations.loc[relations.index[0], column] = value
    inputs[4] = relations
    with pytest.raises(
        PlanningFeatureCodeError, match="catalog|metric|normalized|feature share"
    ):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_surface_relation_metrics_are_revalidated`

**Purpose:** Regression invariant: surface relation metrics are revalidated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_surface_relation_metrics_are_revalidated(column: str, value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("intersection_area_m2", 0.0),
        ("intersection_area_m2", -1.0),
        ("intersection_area_m2", float("inf")),
        ("parcel_share_pct", 99.0),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeatureCodeError, match="relation\|metric\|finite\|percentage"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `inputs[4].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[relations.index[0], column] = value`<br>`inputs[4] = relations` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_surface_relation_metrics_are_revalidated(column: str, value: object) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations.loc[relations.index[0], column] = value
    inputs[4] = relations
    with pytest.raises(
        PlanningFeatureCodeError, match="relation|metric|finite|percentage"
    ):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_line_relation_metrics_are_revalidated`

**Purpose:** Regression invariant: line relation metrics are revalidated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_line_relation_metrics_are_revalidated(column: str, value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value"),
    [
        ("intersection_length_m", 0.0),
        ("relation_type", "TOUCH_ONLY"),
        ("source_line_length_m", 1.0),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="relation\|length\|catalog")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `inputs[4].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[line_index, column] = value`<br>`inputs[4] = relations` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_line_relation_metrics_are_revalidated(column: str, value: object) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    line_index = relations.index[relations["geometry_kind"].eq("LINE")][0]
    relations.loc[line_index, column] = value
    inputs[4] = relations
    with pytest.raises(PlanningFeatureCodeError, match="relation|length|catalog"):
        resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_catalog_columns_are_rejected`

**Purpose:** Regression invariant: duplicate catalog columns are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_catalog_columns_are_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="duplicate\|columns")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `pd.concat` | `pandas.concat` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_catalog_columns_are_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    duplicate = pd.concat([surface, surface[["planning_feature_id"]]], axis=1)
    duplicate = gpd.GeoDataFrame(duplicate, geometry="geometry", crs=surface.crs)
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|columns"):
        resolve_planning_feature_codes(
            document, duplicate, line, point, relations, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_missing_catalog_crs_is_rejected`

**Purpose:** Regression invariant: missing catalog crs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_missing_catalog_crs_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `surface.set_crs` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `surface.set_crs` |
| External process/environment | None directly present. |
| In-memory mutation | `surface.set_crs(None, allow_override=True)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_missing_catalog_crs_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.set_crs(None, allow_override=True)
    with pytest.raises(PlanningFeatureCodeError, match="CRS"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unparseable_catalog_crs_is_rejected`

**Purpose:** Regression invariant: unparseable catalog crs is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unparseable_catalog_crs_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="CRS")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `surface.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.geometry.array._crs = "definitely-not-a-crs"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unparseable_catalog_crs_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.geometry.array._crs = "definitely-not-a-crs"  # type: ignore[attr-defined]
    with pytest.raises(PlanningFeatureCodeError, match="CRS"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_inactive_or_wrong_geometry_column_is_rejected`

**Purpose:** Regression invariant: inactive or wrong geometry column is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_inactive_or_wrong_geometry_column_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="geometry")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `surface.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `surface.geometry.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `surface.set_geometry` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `surface.geometry.copy`<br>`surface.set_geometry` |
| External process/environment | None directly present. |
| In-memory mutation | `surface["alternate_geometry"] = surface.geometry.copy()`<br>`surface.set_geometry("alternate_geometry")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_inactive_or_wrong_geometry_column_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface["alternate_geometry"] = surface.geometry.copy()
    surface = surface.set_geometry("alternate_geometry")
    with pytest.raises(PlanningFeatureCodeError, match="geometry"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_surface_geometry_contract_is_enforced`

**Purpose:** Regression invariant: surface geometry contract is enforced. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_surface_geometry_contract_is_enforced(
    geometry: object,
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("geometry", "message"),
    [
        (None, "null|geometry"),
        (Polygon(), "empty|geometry"),
        (Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)]), "invalid|geometry"),
        (LineString([(0, 0), (1, 1)]), "type|geometry|SURFACE"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry` | positional-or-keyword | `object` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `surface.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `LineString` | `shapely.geometry.LineString` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.at[surface.index[0], "geometry"] = geometry` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_surface_geometry_contract_is_enforced(
    geometry: object,
    message: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.at[surface.index[0], "geometry"] = geometry
    with pytest.raises(PlanningFeatureCodeError, match=message):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_multi_geometries_are_accepted`

**Purpose:** Regression invariant: valid multi geometries are accepted. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_multi_geometries_are_accepted(
    catalog_name: str, geometry: object
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        ("surface", MultiPolygon([Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])])),
        ("line", MultiLineString([[(0, 0), (2, 0)]])),
        ("point", MultiPoint([(0, 0), (1, 1)])),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `catalog_name` | positional-or-keyword | `str` | `required` |
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert getattr(result, f"{catalog_name}_features").geometry.iloc[0].equals(geometry)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `changed_layers.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `layer.data.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_integration_layer` | `tests.unit.test_resolve_planning_feature_codes._integration_layer` |
| `_planning_document` | `tests.unit.test_resolve_planning_feature_codes._planning_document` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `getattr(result, f"{catalog_name}_features").geometry.iloc[0].equals` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `MultiPolygon` | `shapely.geometry.MultiPolygon` |
| `Polygon` | `shapely.geometry.Polygon` |
| `MultiLineString` | `shapely.geometry.MultiLineString` |
| `MultiPoint` | `shapely.geometry.MultiPoint` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `getattr(result, f"{catalog_name}_features").geometry.iloc[0].equals` |
| External process/environment | None directly present. |
| In-memory mutation | `changed_layers.append(layer)`<br>`source.at[source.index[0], "geometry"] = geometry`<br>`changed_layers.append(_integration_layer(target_logical, source))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_multi_geometries_are_accepted(
    catalog_name: str, geometry: object
) -> None:
    document, parcels, _, _, _, _, profile = _integration_inputs()
    target_logical = {
        "surface": "prescription_surface",
        "line": "prescription_line",
        "point": "information_point",
    }[catalog_name]
    changed_layers: list[GpuInspectedLayer] = []
    for layer in document.related_layers:
        if layer.logical_name != target_logical:
            changed_layers.append(layer)
            continue
        source = layer.data.copy(deep=True)
        source.at[source.index[0], "geometry"] = geometry
        changed_layers.append(_integration_layer(target_logical, source))
    changed_document = _planning_document(related_layers=tuple(changed_layers))
    normalized = intersect_parcels_with_gpu_planning_features(parcels, changed_document)
    result = _public_resolve_planning_feature_codes(
        changed_document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        profile,
    )
    assert getattr(result, f"{catalog_name}_features").geometry.iloc[0].equals(geometry)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_catalog_semantic_and_string_contracts_are_enforced`

**Purpose:** Regression invariant: catalog semantic and string contracts are enforced. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_catalog_semantic_and_string_contracts_are_enforced(
    column: str,
    value: object,
    message: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("geometry_kind", "LINE", "geometry kind|SURFACE"),
        ("logical_layer", "prescription_line", "logical layer|surface"),
        ("feature_family", "INFORMATION", "family|logical layer"),
        ("source_identity_kind", None, "source identity|exact string"),
        ("source_layer", " SOURCE ", "source layer|exact string"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |
| `message` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match=message)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `surface.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.loc[surface.index[0], column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_catalog_semantic_and_string_contracts_are_enforced(
    column: str,
    value: object,
    message: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.loc[surface.index[0], column] = value
    with pytest.raises(PlanningFeatureCodeError, match=message):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_every_required_catalog_identity_is_an_exact_non_null_string`

**Purpose:** Regression invariant: every required catalog identity is an exact non null string. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_every_required_catalog_identity_is_an_exact_non_null_string(
    column: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "column",
    [
        "planning_feature_id",
        "source_feature_id",
        "source_identity_kind",
        "source_identity_field",
        "logical_layer",
        "feature_family",
        "geometry_kind",
        "source_layer",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="exact string\|non-empty")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `surface.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.loc[surface.index[0], column] = " invalid "`<br>`relations.loc[relations["planning_feature_id"].eq(feature_id), column] = (<br>            " invalid "<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_every_required_catalog_identity_is_an_exact_non_null_string(
    column: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    relations = relations.copy(deep=True)
    feature_id = surface.iloc[0]["planning_feature_id"]
    surface.loc[surface.index[0], column] = " invalid "
    if column in relations.columns:
        relations.loc[relations["planning_feature_id"].eq(feature_id), column] = (
            " invalid "
        )
    with pytest.raises(PlanningFeatureCodeError, match="exact string|non-empty"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_line_and_point_geometry_types_are_enforced`

**Purpose:** Regression invariant: line and point geometry types are enforced. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_line_and_point_geometry_types_are_enforced(
    catalog_name: str,
    geometry: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        ("line", Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])),
        ("point", LineString([(0, 0), (1, 1)])),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `catalog_name` | positional-or-keyword | `str` | `required` |
| `geometry` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="geometry\|type")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `line.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `point.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |
| `Polygon` | `shapely.geometry.Polygon` |
| `LineString` | `shapely.geometry.LineString` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `catalog.at[catalog.index[0], "geometry"] = geometry`<br>`catalogs[catalog_name] = catalog` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_line_and_point_geometry_types_are_enforced(
    catalog_name: str,
    geometry: object,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    catalogs = {"line": line.copy(deep=True), "point": point.copy(deep=True)}
    catalog = catalogs[catalog_name]
    catalog.at[catalog.index[0], "geometry"] = geometry
    catalogs[catalog_name] = catalog
    with pytest.raises(PlanningFeatureCodeError, match="geometry|type"):
        resolve_planning_feature_codes(
            document,
            surface,
            catalogs["line"],
            catalogs["point"],
            relations,
            profile,
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_planning_feature_ids_are_globally_unique_across_catalogs`

**Purpose:** Regression invariant: planning feature ids are globally unique across catalogs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_planning_feature_ids_are_globally_unique_across_catalogs() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="unique\|catalog\|deterministic")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `line.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `line.loc[line.index[0], "planning_feature_id"] = surface.iloc[0][<br>        "planning_feature_id"<br>    ]` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_planning_feature_ids_are_globally_unique_across_catalogs() -> None:
    document, surface, line, point, relations, profile = _inputs()
    line = line.copy(deep=True)
    line.loc[line.index[0], "planning_feature_id"] = surface.iloc[0][
        "planning_feature_id"
    ]
    with pytest.raises(PlanningFeatureCodeError, match="unique|catalog|deterministic"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_empty_optional_catalogs_preserve_schema_and_crs`

**Purpose:** Regression invariant: valid empty optional catalogs preserve schema and crs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_empty_optional_catalogs_preserve_schema_and_crs() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert coded.empty`
  - `assert coded.crs == original.crs`
  - `assert tuple(coded.columns[: len(original.columns)]) == tuple(original.columns)`
  - `assert (<br>            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS<br>        )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_planning_document` | `tests.unit.test_resolve_planning_feature_codes._planning_document` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_empty_optional_catalogs_preserve_schema_and_crs() -> None:
    document, parcels, _, _, _, _, profile = _integration_inputs()
    surface_layers = tuple(
        layer
        for layer in document.related_layers
        if layer.logical_name in {"prescription_surface", "information_surface"}
    )
    document = _planning_document(related_layers=surface_layers)
    normalized = intersect_parcels_with_gpu_planning_features(parcels, document)
    result = _public_resolve_planning_feature_codes(
        document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        profile,
    )
    for original, coded in (
        (normalized.line_features, result.line_features),
        (normalized.point_features, result.point_features),
    ):
        assert coded.empty
        assert coded.crs == original.crs
        assert tuple(coded.columns[: len(original.columns)]) == tuple(original.columns)
        assert (
            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relation_catalog_code_mismatch_is_rejected`

**Purpose:** Regression invariant: relation catalog code mismatch is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_relation_catalog_code_mismatch_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="catalog")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[relation_index, "subtype_code_raw"] = (<br>        "04" if original != "04" else "00"<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_relation_catalog_code_mismatch_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relation_index = relations.index[0]
    original = relations.loc[relation_index, "subtype_code_raw"]
    relations.loc[relation_index, "subtype_code_raw"] = (
        "04" if original != "04" else "00"
    )
    with pytest.raises(PlanningFeatureCodeError, match="catalog"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_relation_columns_are_rejected`

**Purpose:** Regression invariant: duplicate relation columns are rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_relation_columns_are_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="duplicate\|columns")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `pd.concat` | `pandas.concat` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_relation_columns_are_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    duplicate = pd.concat([relations, relations[["parcel_id"]]], axis=1)
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|columns"):
        resolve_planning_feature_codes(
            document, surface, line, point, duplicate, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relation_identity_must_be_an_exact_non_null_string`

**Purpose:** Regression invariant: relation identity must be an exact non null string. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_relation_identity_must_be_an_exact_non_null_string(
    column: str,
    value: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("column", ["parcel_id", "planning_feature_id"])`, `pytest.mark.parametrize("value", [None, " invalid "])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `column` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="relation\|exact string")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[relations.index[0], column] = value` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_relation_identity_must_be_an_exact_non_null_string(
    column: str,
    value: object,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relations.loc[relations.index[0], column] = value
    with pytest.raises(PlanningFeatureCodeError, match="relation|exact string"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_duplicate_parcel_feature_relation_is_rejected`

**Purpose:** Regression invariant: duplicate parcel feature relation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_duplicate_parcel_feature_relation_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="unique\|duplicate")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `pd.concat` | `pandas.concat` |
| `_canonical_relation_schema` | `tests.unit.test_resolve_planning_feature_codes._canonical_relation_schema` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_duplicate_parcel_feature_relation_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = pd.concat([relations, relations.iloc[[0]]], ignore_index=True)
    relations = _canonical_relation_schema(relations)
    with pytest.raises(PlanningFeatureCodeError, match="unique|duplicate"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_unknown_relation_feature_id_is_rejected`

**Purpose:** Regression invariant: unknown relation feature id is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_unknown_relation_feature_id_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="unknown")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[relations.index[0], "planning_feature_id"] = "UNKNOWN"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_unknown_relation_feature_id_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relations.loc[relations.index[0], "planning_feature_id"] = "UNKNOWN"
    with pytest.raises(PlanningFeatureCodeError, match="unknown"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_relation_type_must_match_catalog_geometry_kind`

**Purpose:** Regression invariant: relation type must match catalog geometry kind. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_relation_type_must_match_catalog_geometry_kind(
    geometry_kind: str,
    relation_type: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "LENGTH_OVERLAP"),
        ("SURFACE", "NOT_A_RELATION"),
        ("LINE", "INSIDE"),
        ("POINT", "AREA_OVERLAP"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry_kind` | positional-or-keyword | `str` | `required` |
| `relation_type` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="[Rr]elation type\|geometry")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `relations.iloc[0].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `_canonical_relation_schema` | `tests.unit.test_resolve_planning_feature_codes._canonical_relation_schema` |
| `pytest.raises` | `pytest.raises` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `row[column] = feature[column]`<br>`row["relation_type"] = relation_type`<br>`row[column] = None`<br>`row["feature_area_m2"] = 4.0`<br>`row["intersection_area_m2"] = area`<br>`row["parcel_share_pct"] = 100.0 if area else 0.0`<br>`row["feature_share_pct"] = 100.0 if area else 0.0`<br>`row["source_line_length_m"] = 2.0`<br>`row["intersection_length_m"] = 2.0 if relation_type == "LENGTH_OVERLAP" else 0.0`<br>`row["point_member_count"] = 1`<br>`row["point_members_inside_count"] = 1 if relation_type == "INSIDE" else 0`<br>`row["point_members_boundary_count"] = (<br>            1 if relation_type == "BOUNDARY_TOUCH" else 0<br>        )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_relation_type_must_match_catalog_geometry_kind(
    geometry_kind: str,
    relation_type: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    catalogs = {"SURFACE": surface, "LINE": line, "POINT": point}
    feature = catalogs[geometry_kind].iloc[0]
    row = relations.iloc[0].copy()
    for column in (
        "planning_feature_id",
        "source_feature_id",
        "source_identity_kind",
        "source_identity_field",
        "logical_layer",
        "feature_family",
        "geometry_kind",
        "type_code_raw",
        "subtype_code_raw",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
        "label_raw",
        "text_raw",
        "source_validity_date_raw",
        "regulation_filename_raw",
    ):
        row[column] = feature[column]
    row["relation_type"] = relation_type
    metric_columns = (
        "feature_area_m2",
        "source_line_length_m",
        "intersection_area_m2",
        "intersection_length_m",
        "parcel_share_pct",
        "feature_share_pct",
        "point_member_count",
        "point_members_inside_count",
        "point_members_boundary_count",
    )
    for column in metric_columns:
        row[column] = None
    if geometry_kind == "SURFACE":
        area = 4.0 if relation_type == "AREA_OVERLAP" else 0.0
        row["feature_area_m2"] = 4.0
        row["intersection_area_m2"] = area
        row["parcel_share_pct"] = 100.0 if area else 0.0
        row["feature_share_pct"] = 100.0 if area else 0.0
    elif geometry_kind == "LINE":
        row["source_line_length_m"] = 2.0
        row["intersection_length_m"] = 2.0 if relation_type == "LENGTH_OVERLAP" else 0.0
    else:
        row["point_member_count"] = 1
        row["point_members_inside_count"] = 1 if relation_type == "INSIDE" else 0
        row["point_members_boundary_count"] = (
            1 if relation_type == "BOUNDARY_TOUCH" else 0
        )
    candidate = pd.DataFrame([row], columns=relations.columns)
    candidate = _canonical_relation_schema(candidate)
    with pytest.raises(PlanningFeatureCodeError, match="[Rr]elation type|geometry"):
        resolve_planning_feature_codes(
            document, surface, line, point, candidate, profile
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_valid_relation_types_are_retained`

**Purpose:** Regression invariant: valid relation types are retained. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_valid_relation_types_are_retained(
    geometry_kind: str,
    relation_type: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "AREA_OVERLAP"),
        ("SURFACE", "TOUCH_ONLY"),
        ("LINE", "LENGTH_OVERLAP"),
        ("LINE", "TOUCH_ONLY"),
        ("POINT", "INSIDE"),
        ("POINT", "BOUNDARY_TOUCH"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `geometry_kind` | positional-or-keyword | `str` | `required` |
| `relation_type` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.relations["relation_type"].tolist() == [relation_type]`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Polygon` | `shapely.geometry.Polygon` |
| `LineString` | `shapely.geometry.LineString` |
| `Point` | `shapely.geometry.Point` |
| `_integration_source_frame` | `tests.unit.test_resolve_planning_feature_codes._integration_source_frame` |
| `logical.startswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `_planning_document` | `tests.unit.test_resolve_planning_feature_codes._planning_document` |
| `_integration_layer` | `tests.unit.test_resolve_planning_feature_codes._integration_layer` |
| `_integration_parcels` | `tests.unit.test_resolve_planning_feature_codes._integration_parcels` |
| `intersect_parcels_with_gpu_planning_features` | `landscout.stages.enrich_planning_features.intersect_parcels_with_gpu_planning_features` |
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_profile` | `tests.unit.test_resolve_planning_feature_codes._profile` |
| `result.relations["relation_type"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_valid_relation_types_are_retained(
    geometry_kind: str,
    relation_type: str,
) -> None:
    geometry: object
    if geometry_kind == "SURFACE":
        logical = "prescription_surface"
        geometry = (
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
            if relation_type == "AREA_OVERLAP"
            else Polygon([(2, 0), (4, 0), (4, 2), (2, 2)])
        )
    elif geometry_kind == "LINE":
        logical = "prescription_line"
        geometry = (
            LineString([(0, 1), (2, 1)])
            if relation_type == "LENGTH_OVERLAP"
            else LineString([(-1, 0), (0, 0)])
        )
    else:
        logical = "information_point"
        geometry = Point(1, 1) if relation_type == "INSIDE" else Point(0, 1)
    source = _integration_source_frame(
        logical,
        [geometry],
        ["FEATURE-1"],
        ["07" if logical.startswith("prescription") else "99"],
        ["00"],
    )
    document = _planning_document(related_layers=(_integration_layer(logical, source),))
    parcels = _integration_parcels()
    normalized = intersect_parcels_with_gpu_planning_features(parcels, document)
    result = _public_resolve_planning_feature_codes(
        document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        _profile(),
    )
    assert result.relations["relation_type"].tolist() == [relation_type]
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coordinated_output_hash_mutation_is_rejected`

**Purpose:** Regression invariant: coordinated output hash mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coordinated_output_hash_mutation_is_rejected() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="rebuilt\|meaning\|dictionary")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `result.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_result_with_hashes` | `landscout.stages.resolve_planning_feature_codes._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_feature_code_result` | `tests.unit.test_resolve_planning_feature_codes.validate_planning_feature_code_result` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.loc[surface.index[0], "official_code_label"] = "Mutated"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coordinated_output_hash_mutation_is_rejected() -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_label"] = "Mutated"
    mutated = _result_with_hashes(replace(result, surface_features=surface))
    with pytest.raises(PlanningFeatureCodeError, match="rebuilt|meaning|dictionary"):
        validate_planning_feature_code_result(*inputs, mutated)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parquet_readback_passes_source_complete_validation`

**Purpose:** Regression invariant: parquet readback passes source complete validation. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parquet_readback_passes_source_complete_validation(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `paths.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr(result, name).to_parquet` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pd.read_parquet` | `pandas.read_parquet` |
| `gpd.read_parquet` | `geopandas.read_parquet` |
| `validate_planning_feature_code_result` | `tests.unit.test_resolve_planning_feature_codes.validate_planning_feature_code_result` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `pd.read_parquet`<br>`gpd.read_parquet` |
| Filesystem/archive write or publication | `getattr(result, name).to_parquet` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_parquet_readback_passes_source_complete_validation(tmp_path: Path) -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    paths = {
        name: tmp_path / f"{name}.parquet"
        for name in (
            "code_dictionary",
            "surface_features",
            "line_features",
            "point_features",
            "relations",
        )
    }
    for name, path in paths.items():
        getattr(result, name).to_parquet(path, index=True)
    persisted = replace(
        result,
        code_dictionary=pd.read_parquet(paths["code_dictionary"]),
        surface_features=gpd.read_parquet(paths["surface_features"]),
        line_features=gpd.read_parquet(paths["line_features"]),
        point_features=gpd.read_parquet(paths["point_features"]),
        relations=pd.read_parquet(paths["relations"]),
    )
    validate_planning_feature_code_result(*inputs, persisted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_record_order_must_be_deterministic`

**Purpose:** Regression invariant: record order must be deterministic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_record_order_must_be_deterministic() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(ValueError, match="deterministic order")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_profile_payload` | `tests.unit.test_resolve_planning_feature_codes._profile_payload` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `reversed` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `CnigFeatureCodeProfile.model_validate` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.model_validate` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["records"] = list(reversed(payload["records"]))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_record_order_must_be_deterministic() -> None:
    payload = _profile_payload()
    payload["records"] = list(reversed(payload["records"]))
    with pytest.raises(ValueError, match="deterministic order"):
        CnigFeatureCodeProfile.model_validate(payload)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_yaml_snapshot_loads_strictly`

**Purpose:** Regression invariant: yaml snapshot loads strictly. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_yaml_snapshot_loads_strictly(tmp_path: Path) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert load_cnig_feature_code_profile(path) == _profile()`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_profile_payload` | `tests.unit.test_resolve_planning_feature_codes._profile_payload` |
| `path.write_text` | `unresolved local/third-party receiver; no ownership inferred` |
| `yaml.safe_dump` | `yaml.safe_dump` |
| `load_cnig_feature_code_profile` | `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile` |
| `_profile` | `tests.unit.test_resolve_planning_feature_codes._profile` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `path.write_text` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_yaml_snapshot_loads_strictly(tmp_path: Path) -> None:
    payload = _profile_payload()
    path = tmp_path / "profile.yaml"
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    assert load_cnig_feature_code_profile(path) == _profile()
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_stable_public_api_is_exported_from_module_and_stage_package`

**Purpose:** Regression invariant: stable public api is exported from module and stage package. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_stable_public_api_is_exported_from_module_and_stage_package() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert required.issubset(set(coding_module.__all__))`
  - `assert required.issubset(set(stages.__all__))`
  - `assert getattr(stages, name) is getattr(coding_module, name)`
  - `assert low_level.isdisjoint(coding_module.__all__)`
  - `assert low_level.isdisjoint(stages.__all__)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `required.issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `low_level.isdisjoint` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `low_level.isdisjoint` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_stable_public_api_is_exported_from_module_and_stage_package() -> None:
    from landscout import stages

    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )

    required = {
        "CnigFeatureCodeProfile",
        "PlanningFeatureCodeError",
        "PlanningFeatureCodeResult",
        "load_cnig_feature_code_profile",
        "resolve_planning_feature_codes",
        "validate_planning_feature_code_result",
        "validate_planning_feature_code_result_envelope",
    }
    low_level = {
        "_canonical_json_sha256",
        "_coded_catalog",
        "_lookup",
        "_profile_sha256",
        "_result_with_hashes",
    }
    assert required.issubset(set(coding_module.__all__))
    assert required.issubset(set(stages.__all__))
    for name in required:
        assert getattr(stages, name) is getattr(coding_module, name)
    assert low_level.isdisjoint(coding_module.__all__)
    assert low_level.isdisjoint(stages.__all__)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs`

**Purpose:** Regression invariant: checked in official snapshot is complete for observed muret pairs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert profile.schema_version == 2`
  - `assert profile.profile == "cnig_plu_2017_muret_observed_pairs_v2"`
  - `assert profile.standard_model == "CNIG PLU v2017"`
  - `assert profile.official_text_normalization == TEXT_NORMALIZATION`
  - `assert profile.retrieval_date.isoformat() == "2026-08-12"`
  - `assert profile.official_sources.prescription == P_URL`
  - `assert profile.official_sources.information == I_URL`
  - `assert (<br>        profile.canonical_records_sha256<br>        == "5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c"<br>    )`
  - `assert (<br>        _payload_hash(profile.model_dump(mode="json"))<br>        == "5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"<br>    )`
  - `assert actual_records == expected_records`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `Path` | `pathlib.Path` |
| `load_cnig_feature_code_profile` | `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `profile.retrieval_date.isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_payload_hash` | `tests.unit.test_resolve_planning_feature_codes._payload_hash` |
| `profile.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_payload_hash` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs() -> None:
    path = Path("configs/planning/cnig_plu_2017_feature_codes.yaml")
    profile = load_cnig_feature_code_profile(path)
    expected_records = (
        (
            "INFORMATION",
            "02",
            "00",
            "Zone d'aménagement concerté",
            "L311-1 code de l’urbanisme",
            "R151-52 8°",
            I_URL,
        ),
        (
            "INFORMATION",
            "14",
            "00",
            "Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)",
            "L571-10 code de l’environnement",
            "R151-53 5°",
            I_URL,
        ),
        (
            "INFORMATION",
            "27",
            "00",
            "Plan d'exposition au bruit des aérodromes",
            "L112-6 code de l’urbanisme",
            "R151-52 2°",
            I_URL,
        ),
        (
            "INFORMATION",
            "99",
            "00",
            "Autre périmètre, secteur, plan, document, site, projet, espace.",
            None,
            None,
            I_URL,
        ),
        (
            "PRESCRIPTION",
            "01",
            "00",
            "Espace boisé classé",
            "L113-1",
            "R151-31 1°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "05",
            "00",
            "Emplacement réservé",
            "L151-41 1° à 3°",
            "R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "07",
            "00",
            "Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique",
            "L151-19 et L151-23",
            "R151-41 3° Et R151-43",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "07",
            "04",
            "Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique",
            "L151-23",
            "R151-43 5°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "15",
            "00",
            "Règles d’implantation des constructions",
            "L151-17 et L151-18",
            "R151-39 dernier al.",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "15",
            "01",
            "Implantation des constructions par rapport aux voies et aux emprises publiques",
            "L151-17 et L151-18",
            "R151-39",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "17",
            "00",
            "Secteur à programme de logements mixité sociale en zone U et AU",
            "L151-15",
            "R151-38 3°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "18",
            "00",
            "Périmètre comportant des orientations d’aménagement et de programmation (OAP)",
            "L151-6 et L151-7",
            "R151-6 à R151-8-1",
            P_URL,
        ),
    )
    actual_records = tuple(
        (
            record.feature_family,
            record.type_code,
            record.subtype_code,
            record.official_label,
            record.legal_reference,
            record.regulation_or_annex_reference,
            record.official_source_url,
        )
        for record in profile.records
    )
    assert profile.schema_version == 2
    assert profile.profile == "cnig_plu_2017_muret_observed_pairs_v2"
    assert profile.standard_model == "CNIG PLU v2017"
    assert profile.official_text_normalization == TEXT_NORMALIZATION
    assert profile.retrieval_date.isoformat() == "2026-08-12"
    assert profile.official_sources.prescription == P_URL
    assert profile.official_sources.information == I_URL
    assert (
        profile.canonical_records_sha256
        == "5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c"
    )
    assert (
        _payload_hash(profile.model_dump(mode="json"))
        == "5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"
    )
    assert actual_records == expected_records
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_result_schema_versions_are_strict`

**Purpose:** Regression invariant: result schema versions are strict. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_result_schema_versions_are_strict(field: str, value: object) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    ("field", "value"),
    [
        ("result_hash_schema_version", True),
        ("result_hash_schema_version", 0),
        ("result_hash_schema_version", 1),
        ("result_hash_schema_version", 2),
        ("result_hash_schema_version", 3),
        ("result_hash_schema_version", 4),
        ("result_hash_schema_version", 6),
        ("result_hash_schema_version", 5.0),
        ("result_hash_schema_version", "5"),
        ("profile_schema_version", True),
        ("profile_schema_version", 0),
        ("profile_schema_version", 1),
        ("profile_schema_version", 3),
        ("profile_schema_version", 2.0),
        ("profile_schema_version", "2"),
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="schema version")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.raises` | `pytest.raises` |
| `validate_planning_feature_code_result` | `tests.unit.test_resolve_planning_feature_codes.validate_planning_feature_code_result` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_result_schema_versions_are_strict(field: str, value: object) -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    with pytest.raises(PlanningFeatureCodeError, match="schema version"):
        validate_planning_feature_code_result(
            *inputs, replace(result, **{field: value})
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_step_7d_3_1_output_integrates_with_public_coding_api`

**Purpose:** Regression invariant: step 7d 3 1 output integrates with public coding api. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_step_7d_3_1_output_integrates_with_public_coding_api() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert result.result_hash_schema_version == 5`
  - `assert result.profile_schema_version == 2`
  - `assert len(result.surface_features) == 2`
  - `assert len(result.line_features) == 1`
  - `assert len(result.point_features) == 1`
  - `assert len(result.relations) == 2`
  - `assert set(result.surface_features["official_code_status"]) == {"RESOLVED_OFFICIAL"}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `_public_validate_planning_feature_code_result` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_step_7d_3_1_output_integrates_with_public_coding_api() -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    assert result.result_hash_schema_version == 5
    assert result.profile_schema_version == 2
    assert len(result.surface_features) == 2
    assert len(result.line_features) == 1
    assert len(result.point_features) == 1
    assert len(result.relations) == 2
    assert set(result.surface_features["official_code_status"]) == {"RESOLVED_OFFICIAL"}
    _public_validate_planning_feature_code_result(*inputs, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats`

**Purpose:** Regression invariant: resolver runs heavy factual validation once and public validator repeats. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `monkeypatch` | positional-or-keyword | `pytest.MonkeyPatch` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert calls == {"physical": 1, "relations": 1}`
  - `assert calls == {"physical": 2, "relations": 2}`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `importlib.import_module` | `importlib.import_module` |
| `monkeypatch.setattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `coding_module.resolve_planning_feature_codes` | `unresolved local/third-party receiver; no ownership inferred` |
| `coding_module.validate_planning_feature_code_result` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs = _integration_inputs()
    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    enrich_module = importlib.import_module("landscout.stages.enrich_planning_features")
    actual_physical = enrich_module.revalidate_gpu_spatial_layer_sources
    actual_relations = enrich_module._build_relation_tables
    calls = {"physical": 0, "relations": 0}

    def counted_physical(*args: object, **kwargs: object) -> object:
        calls["physical"] += 1
        return actual_physical(*args, **kwargs)

    def counted_relations(*args: object, **kwargs: object) -> object:
        calls["relations"] += 1
        return actual_relations(*args, **kwargs)

    monkeypatch.setattr(
        enrich_module, "revalidate_gpu_spatial_layer_sources", counted_physical
    )
    monkeypatch.setattr(enrich_module, "_build_relation_tables", counted_relations)

    result = coding_module.resolve_planning_feature_codes(*inputs)
    assert calls == {"physical": 1, "relations": 1}

    coding_module.validate_planning_feature_code_result(*inputs, result)
    assert calls == {"physical": 2, "relations": 2}
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats.counted_physical`

**Purpose:** Implements `counted physical` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def counted_physical(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `actual_physical(*args, **kwargs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `actual_physical` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `calls["physical"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def counted_physical(*args: object, **kwargs: object) -> object:
        calls["physical"] += 1
        return actual_physical(*args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats.counted_relations`

**Purpose:** Implements `counted relations` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def counted_relations(*args: object, **kwargs: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `*args` | variadic positional | `object` | `variadic` |
| `**kwargs` | variadic keyword | `object` | `variadic` |

**Return and exception contract**

- Exact observed return expressions:
  - `actual_relations(*args, **kwargs)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `actual_relations` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `calls["relations"] += 1` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def counted_relations(*args: object, **kwargs: object) -> object:
        calls["relations"] += 1
        return actual_relations(*args, **kwargs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coded_result_persists_all_source_input_hashes`

**Purpose:** Regression invariant: coded result persists all source input hashes. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coded_result_persists_all_source_input_hashes() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert isinstance(value, str)`
  - `assert len(value) == 64`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coded_result_persists_all_source_input_hashes() -> None:
    result = _public_resolve_planning_feature_codes(*_integration_inputs())
    for hash_field in (
        "planning_document_context_sha256",
        "parcel_identity_input_sha256",
        "normalized_catalogs_input_sha256",
        "normalized_relations_input_sha256",
        "gpu_related_source_files_sha256",
        "expected_relations_content_sha256",
    ):
        value = getattr(result, hash_field)
        assert isinstance(value, str)
        assert len(value) == 64
        int(value, 16)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_input_hash_mutation_is_rejected`

**Purpose:** Regression invariant: source input hash mutation is rejected. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_input_hash_mutation_is_rejected(field: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "field",
    [
        "planning_document_context_sha256",
        "parcel_identity_input_sha256",
        "normalized_catalogs_input_sha256",
        "normalized_relations_input_sha256",
        "gpu_related_source_files_sha256",
        "expected_relations_content_sha256",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="hash\|rebuilt\|source")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.raises` | `pytest.raises` |
| `_public_validate_planning_feature_code_result` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_input_hash_mutation_is_rejected(field: str) -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    with pytest.raises(PlanningFeatureCodeError, match="hash|rebuilt|source"):
        _public_validate_planning_feature_code_result(
            *inputs, replace(result, **{field: "f" * 64})
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_gpu_related_source_hash_is_deterministic_across_cache_roots`

**Purpose:** Regression invariant: gpu related source hash is deterministic across cache roots. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_gpu_related_source_hash_is_deterministic_across_cache_roots(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert (<br>        first.gpu_related_source_files_sha256 == second.gpu_related_source_files_sha256<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `shutil.copytree` | `shutil.copytree` |
| `relocated_reference` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_gpu_related_source_hash_is_deterministic_across_cache_roots(
    tmp_path: Path,
) -> None:
    first_inputs = _integration_inputs()
    first_document = first_inputs[0]
    source_root = first_document.extraction.extraction_root
    relocated_root = tmp_path / "relocated-extraction"
    shutil.copytree(source_root, relocated_root)

    def relocated_reference(
        reference: GpuSpatialLayerReference,
    ) -> GpuSpatialLayerReference:
        relative = reference.dataset_path.relative_to(source_root)
        return replace(reference, dataset_path=relocated_root / relative)

    reference_map = {
        reference: relocated_reference(reference)
        for reference in first_document.all_spatial_layers
    }
    relocated_document = replace(
        first_document,
        extraction=replace(
            first_document.extraction,
            extraction_root=relocated_root,
        ),
        all_spatial_layers=tuple(
            reference_map[reference] for reference in first_document.all_spatial_layers
        ),
        zoning=replace(
            first_document.zoning,
            reference=reference_map[first_document.zoning.reference],
        ),
        related_layers=tuple(
            replace(layer, reference=reference_map[layer.reference])
            for layer in first_document.related_layers
        ),
    )
    second_inputs = (relocated_document, *first_inputs[1:])
    first = _public_resolve_planning_feature_codes(*first_inputs)
    second = _public_resolve_planning_feature_codes(*second_inputs)
    assert (
        first.gpu_related_source_files_sha256 == second.gpu_related_source_files_sha256
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_gpu_related_source_hash_is_deterministic_across_cache_roots.relocated_reference`

**Purpose:** Implements `relocated reference` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def relocated_reference(
        reference: GpuSpatialLayerReference,
    ) -> GpuSpatialLayerReference:
```

- Exact decorators: none.
- Declared return annotation: `GpuSpatialLayerReference`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `reference` | positional-or-keyword | `GpuSpatialLayerReference` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(reference, dataset_path=relocated_root / relative)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `reference.dataset_path.relative_to` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def relocated_reference(
        reference: GpuSpatialLayerReference,
    ) -> GpuSpatialLayerReference:
        relative = reference.dataset_path.relative_to(source_root)
        return replace(reference, dataset_path=relocated_root / relative)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_source_binding_hashes_bind_every_component_hash`

**Purpose:** Regression invariant: source binding hashes bind every component hash. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_source_binding_hashes_bind_every_component_hash(field: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "field",
    ["gpu_related_source_files_sha256", "expected_relations_content_sha256"],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `field` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert getattr(changed, hash_field) != getattr(result, hash_field)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `_result_with_hashes` | `landscout.stages.resolve_planning_feature_codes._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_source_binding_hashes_bind_every_component_hash(field: str) -> None:
    result = _public_resolve_planning_feature_codes(*_integration_inputs())
    changed = _result_with_hashes(replace(result, **{field: "f" * 64}))
    for hash_field in (
        "code_dictionary_content_sha256",
        "surface_features_content_sha256",
        "line_features_content_sha256",
        "point_features_content_sha256",
        "relations_content_sha256",
        "complete_result_content_sha256",
    ):
        assert getattr(changed, hash_field) != getattr(result, hash_field)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_parcel_source_change_invalidates_coded_result`

**Purpose:** Regression invariant: parcel source change invalidates coded result. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_parcel_source_change_invalidates_coded_result() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="parcel\|source\|rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `inputs[1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_public_validate_planning_feature_code_result` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `parcels.loc[parcels.index[0], "parcel_id"] = "CHANGED-PARCEL"`<br>`inputs[1] = parcels` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_parcel_source_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    parcels = inputs[1].copy(deep=True)
    parcels.loc[parcels.index[0], "parcel_id"] = "CHANGED-PARCEL"
    inputs[1] = parcels
    with pytest.raises(PlanningFeatureCodeError, match="parcel|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_gpu_document_context_change_invalidates_coded_result`

**Purpose:** Regression invariant: gpu document context change invalidates coded result. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_gpu_document_context_change_invalidates_coded_result() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="document\|source\|rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `_public_validate_planning_feature_code_result` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `inputs[0] = replace(<br>        planning_document,<br>        extraction=replace(<br>            planning_document.extraction,<br>            archive=replace(archive, document=changed_document),<br>        ),<br>    )` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_gpu_document_context_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    planning_document = inputs[0]
    archive = planning_document.extraction.archive
    changed_document = replace(archive.document, provider="Changed provider")
    inputs[0] = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=changed_document),
        ),
    )
    with pytest.raises(PlanningFeatureCodeError, match="document|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_normalized_catalog_change_invalidates_coded_result_even_when_coherent`

**Purpose:** Regression invariant: normalized catalog change invalidates coded result even when coherent. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_normalized_catalog_change_invalidates_coded_result_even_when_coherent() -> (
    None
):
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="normalized\|source\|rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `inputs[2].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `inputs[5].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["planning_feature_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_public_validate_planning_feature_code_result` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.loc[surface.index[0], "label_raw"] = "Coherently changed"`<br>`relations.loc[relations["planning_feature_id"].eq(feature_id), "label_raw"] = (<br>        "Coherently changed"<br>    )`<br>`inputs[2] = surface`<br>`inputs[5] = relations` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_normalized_catalog_change_invalidates_coded_result_even_when_coherent() -> (
    None
):
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    surface = inputs[2].copy(deep=True)
    relations = inputs[5].copy(deep=True)
    feature_id = surface.iloc[0]["planning_feature_id"]
    surface.loc[surface.index[0], "label_raw"] = "Coherently changed"
    relations.loc[relations["planning_feature_id"].eq(feature_id), "label_raw"] = (
        "Coherently changed"
    )
    inputs[2] = surface
    inputs[5] = relations
    with pytest.raises(PlanningFeatureCodeError, match="normalized|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_normalized_relation_change_invalidates_coded_result`

**Purpose:** Regression invariant: normalized relation change invalidates coded result. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_normalized_relation_change_invalidates_coded_result() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="[Rr]elation\|source\|rebuilt")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `inputs[5].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_public_validate_planning_feature_code_result` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `relations.loc[line_mask, "parcel_metric_area_m2"] = 8.0`<br>`inputs[5] = relations` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_normalized_relation_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    relations = inputs[5].copy(deep=True)
    line_mask = relations["geometry_kind"].eq("LINE")
    relations.loc[line_mask, "parcel_metric_area_m2"] = 8.0
    inputs[5] = relations
    with pytest.raises(PlanningFeatureCodeError, match="[Rr]elation|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_coding_api_rejects_relation_set_not_rebuilt_from_geometry`

**Purpose:** Regression invariant: coding api rejects relation set not rebuilt from geometry. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_coding_api_rejects_relation_set_not_rebuilt_from_geometry(
    mutation: str,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "metric"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeatureCodeError,<br>        match="relation\|parcel\|source\|rebuilt\|normalized",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `inputs[5].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.iloc[1:].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.iloc[[0]].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.concat` | `pandas.concat` |
| `relations.iloc[::-1].reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["geometry_kind"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `relations["geometry_kind"].eq` |
| External process/environment | None directly present. |
| In-memory mutation | `extra.loc[extra.index[0], "parcel_id"] = "PARCEL-OTHER"`<br>`relations.loc[line_mask, "intersection_length_m"] = 1.0`<br>`inputs[5] = relations` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_coding_api_rejects_relation_set_not_rebuilt_from_geometry(
    mutation: str,
) -> None:
    inputs = list(_integration_inputs())
    relations = inputs[5].copy(deep=True)
    if mutation == "missing":
        relations = relations.iloc[1:].copy()
    elif mutation == "extra":
        extra = relations.iloc[[0]].copy(deep=True)
        extra.loc[extra.index[0], "parcel_id"] = "PARCEL-OTHER"
        relations = pd.concat([relations, extra], ignore_index=True)
    elif mutation == "reordered":
        relations = relations.iloc[::-1].reset_index(drop=True)
    else:
        line_mask = relations["geometry_kind"].eq("LINE")
        relations.loc[line_mask, "intersection_length_m"] = 1.0
    inputs[5] = relations
    with pytest.raises(
        PlanningFeatureCodeError,
        match="relation|parcel|source|rebuilt|normalized",
    ):
        _public_resolve_planning_feature_codes(*inputs)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_schema_v5_parquet_readback_preserves_source_hash_envelope`

**Purpose:** Regression invariant: schema v5 parquet readback preserves source hash envelope. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_schema_v5_parquet_readback_preserves_source_hash_envelope(
    tmp_path: Path,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `tmp_path` | positional-or-keyword | `Path` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_integration_inputs` | `tests.unit.test_resolve_planning_feature_codes._integration_inputs` |
| `_public_resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `paths.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr(result, name).to_parquet` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pd.read_parquet` | `pandas.read_parquet` |
| `gpd.read_parquet` | `geopandas.read_parquet` |
| `_public_validate_planning_feature_code_result` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `pd.read_parquet`<br>`gpd.read_parquet` |
| Filesystem/archive write or publication | `getattr(result, name).to_parquet` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_schema_v5_parquet_readback_preserves_source_hash_envelope(
    tmp_path: Path,
) -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    paths = {
        name: tmp_path / f"integrated-{name}.parquet"
        for name in (
            "code_dictionary",
            "surface_features",
            "line_features",
            "point_features",
            "relations",
        )
    }
    for name, path in paths.items():
        getattr(result, name).to_parquet(path, index=True)
    persisted = replace(
        result,
        code_dictionary=pd.read_parquet(paths["code_dictionary"]),
        surface_features=gpd.read_parquet(paths["surface_features"]),
        line_features=gpd.read_parquet(paths["line_features"]),
        point_features=gpd.read_parquet(paths["point_features"]),
        relations=pd.read_parquet(paths["relations"]),
    )
    _public_validate_planning_feature_code_result(*inputs, persisted)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_schema_v5_public_api_signatures_remain_source_complete`

**Purpose:** Regression invariant: schema v5 public api signatures remain source complete. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_schema_v5_public_api_signatures_remain_source_complete() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert tuple(<br>        inspect.signature(_public_resolve_planning_feature_codes).parameters<br>    ) == (<br>        "planning_document",<br>        "parcels",<br>        "surface_features",<br>        "line_features",<br>        "point_features",<br>        "relations",<br>        "code_profile",<br>    )`
  - `assert tuple(<br>        inspect.signature(_public_validate_planning_feature_code_result).parameters<br>    ) == (<br>        "planning_document",<br>        "parcels",<br>        "surface_features",<br>        "line_features",<br>        "point_features",<br>        "relations",<br>        "code_profile",<br>        "result",<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `inspect.signature` | `inspect.signature` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_schema_v5_public_api_signatures_remain_source_complete() -> None:
    assert tuple(
        inspect.signature(_public_resolve_planning_feature_codes).parameters
    ) == (
        "planning_document",
        "parcels",
        "surface_features",
        "line_features",
        "point_features",
        "relations",
        "code_profile",
    )
    assert tuple(
        inspect.signature(_public_validate_planning_feature_code_result).parameters
    ) == (
        "planning_document",
        "parcels",
        "surface_features",
        "line_features",
        "point_features",
        "relations",
        "code_profile",
        "result",
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator`

**Purpose:** Regression invariant: step 7d 5b 2b 5 exposes lightweight coded result validator. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="hash\|invalid")`
- Exact assertions:
  - `assert hasattr(module, "validate_planning_feature_code_result_envelope")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `hasattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `module.validate_planning_feature_code_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `replace` | `dataclasses.replace` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    assert hasattr(module, "validate_planning_feature_code_result_envelope")
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    module.validate_planning_feature_code_result_envelope(result)
    with pytest.raises(PlanningFeatureCodeError, match="hash|invalid"):
        module.validate_planning_feature_code_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_schema_v5_envelope_result`

**Purpose:** Implements `schema v5 envelope result` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _schema_v5_envelope_result() -> PlanningFeatureCodeResult:
```

- Exact decorators: none.
- Declared return annotation: `PlanningFeatureCodeResult`.

**Inputs**

- No parameters.

**Return and exception contract**

- Exact observed return expressions:
  - `resolve_planning_feature_codes(*_inputs())`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_rejects_canonical_empty_code_dictionary` via `_schema_v5_envelope_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_rejects_canonical_empty_code_dictionary` via `_schema_v5_envelope_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs` via `_schema_v5_envelope_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs` via `_schema_v5_envelope_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_controls_malformed_dictionary_type` via `_schema_v5_envelope_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_controls_malformed_dictionary_type` via `_schema_v5_envelope_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_rejects_geospatial_code_dictionary` via `_schema_v5_envelope_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_rejects_geospatial_code_dictionary` via `_schema_v5_envelope_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_dictionary_schema_is_explicit` via `_schema_v5_envelope_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_dictionary_schema_is_explicit` via `_schema_v5_envelope_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_dictionary_rows_are_intrinsically_validated` via `_schema_v5_envelope_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_dictionary_rows_are_intrinsically_validated` via `_schema_v5_envelope_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_scalar_lineage_contracts_are_intrinsic` via `_schema_v5_envelope_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_scalar_lineage_contracts_are_intrinsic` via `_schema_v5_envelope_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic` via `_schema_v5_envelope_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic` via `_schema_v5_envelope_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result` via `_schema_v5_envelope_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result` via `_schema_v5_envelope_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `resolve_planning_feature_codes` | `tests.unit.test_resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `_inputs` | `tests.unit.test_resolve_planning_feature_codes._inputs` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _schema_v5_envelope_result() -> PlanningFeatureCodeResult:
    return resolve_planning_feature_codes(*_inputs())
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `_canonical_empty_coded_result`

**Purpose:** Implements `canonical empty coded result` within the file role: Provides complete unit and regression coverage for the `resolve_planning_feature_codes` contracts exercised in this file.

**Exact signature**

```python
def _canonical_empty_coded_result(
    result: PlanningFeatureCodeResult,
    *,
    empty_dictionary: bool,
) -> PlanningFeatureCodeResult:
```

- Exact decorators: none.
- Declared return annotation: `PlanningFeatureCodeResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |
| `empty_dictionary` | keyword-only | `bool` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_result_with_hashes(<br>        replace(<br>            result,<br>            code_dictionary=dictionary,<br>            relations=relations,<br>            **catalogs,<br>        )<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_rejects_canonical_empty_code_dictionary` via `_canonical_empty_coded_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_rejects_canonical_empty_code_dictionary` via `_canonical_empty_coded_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs` via `_canonical_empty_coded_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs` via `_canonical_empty_coded_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `getattr(result, field).iloc[0:0].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `zip` | `unresolved local/third-party receiver; no ownership inferred` |
| `feature_dtypes` | `landscout.common.planning_feature_schema.feature_dtypes` |
| `pd.Series` | `pandas.Series` |
| `pd.Index` | `pandas.Index` |
| `result.relations.iloc[0:0].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_dtypes` | `landscout.common.planning_feature_schema.relation_dtypes` |
| `result.code_dictionary.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `dictionary.iloc[0:0].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_result_with_hashes` | `landscout.stages.resolve_planning_feature_codes._result_with_hashes` |
| `replace` | `dataclasses.replace` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `output[column] = pd.Series(index=output.index, dtype=dtype)`<br>`output.index = pd.Index([], dtype="int64")`<br>`catalogs[field] = output`<br>`relations[column] = pd.Series(index=relations.index, dtype=dtype)`<br>`relations.index = pd.Index([], dtype="int64")`<br>`dictionary.index = pd.Index([], dtype="int64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _canonical_empty_coded_result(
    result: PlanningFeatureCodeResult,
    *,
    empty_dictionary: bool,
) -> PlanningFeatureCodeResult:
    catalogs: dict[str, gpd.GeoDataFrame] = {}
    for field, kind in (
        ("surface_features", "SURFACE"),
        ("line_features", "LINE"),
        ("point_features", "POINT"),
    ):
        output = getattr(result, field).iloc[0:0].copy(deep=True)
        for column, dtype in zip(output.columns, feature_dtypes(kind), strict=True):
            if dtype != "geometry":
                output[column] = pd.Series(index=output.index, dtype=dtype)
        output.index = pd.Index([], dtype="int64")
        catalogs[field] = output
    relations = result.relations.iloc[0:0].copy(deep=True)
    for column, dtype in zip(relations.columns, relation_dtypes(), strict=True):
        relations[column] = pd.Series(index=relations.index, dtype=dtype)
    relations.index = pd.Index([], dtype="int64")
    dictionary = result.code_dictionary.copy(deep=True)
    if empty_dictionary:
        dictionary = dictionary.iloc[0:0].copy(deep=True)
        dictionary.index = pd.Index([], dtype="int64")
    return _result_with_hashes(
        replace(
            result,
            code_dictionary=dictionary,
            relations=relations,
            **catalogs,
        )
    )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_schema_v5_envelope_rejects_canonical_empty_code_dictionary`

**Purpose:** Regression invariant: schema v5 envelope rejects canonical empty code dictionary. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_schema_v5_envelope_rejects_canonical_empty_code_dictionary() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="dictionary\|empty\|record")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_canonical_empty_coded_result` | `tests.unit.test_resolve_planning_feature_codes._canonical_empty_coded_result` |
| `_schema_v5_envelope_result` | `tests.unit.test_resolve_planning_feature_codes._schema_v5_envelope_result` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_planning_feature_code_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_schema_v5_envelope_rejects_canonical_empty_code_dictionary() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _canonical_empty_coded_result(
        _schema_v5_envelope_result(), empty_dictionary=True
    )
    with pytest.raises(PlanningFeatureCodeError, match="dictionary|empty|record"):
        module.validate_planning_feature_code_result_envelope(result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs`

**Purpose:** Regression invariant: schema v5 envelope accepts nonempty dictionary with empty outputs. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact assertions:
  - `assert len(result.code_dictionary) >= 1`
  - `assert (<br>        sum(<br>            len(frame)<br>            for frame in (<br>                result.surface_features,<br>                result.line_features,<br>                result.point_features,<br>                result.relations,<br>            )<br>        )<br>        == 0<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_canonical_empty_coded_result` | `tests.unit.test_resolve_planning_feature_codes._canonical_empty_coded_result` |
| `_schema_v5_envelope_result` | `tests.unit.test_resolve_planning_feature_codes._schema_v5_envelope_result` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `module.validate_planning_feature_code_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _canonical_empty_coded_result(
        _schema_v5_envelope_result(), empty_dictionary=False
    )
    assert len(result.code_dictionary) >= 1
    assert (
        sum(
            len(frame)
            for frame in (
                result.surface_features,
                result.line_features,
                result.point_features,
                result.relations,
            )
        )
        == 0
    )
    module.validate_planning_feature_code_result_envelope(result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_schema_v5_envelope_controls_malformed_dictionary_type`

**Purpose:** Regression invariant: schema v5 envelope controls malformed dictionary type. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_schema_v5_envelope_controls_malformed_dictionary_type(
    dictionary: object,
) -> None:
```

- Exact decorators: `pytest.mark.parametrize("dictionary", [None, "not-a-frame"])`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `dictionary` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError)`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_schema_v5_envelope_result` | `tests.unit.test_resolve_planning_feature_codes._schema_v5_envelope_result` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_planning_feature_code_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_schema_v5_envelope_controls_malformed_dictionary_type(
    dictionary: object,
) -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    with pytest.raises(PlanningFeatureCodeError):
        module.validate_planning_feature_code_result_envelope(
            replace(result, code_dictionary=dictionary)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_schema_v5_envelope_rejects_geospatial_code_dictionary`

**Purpose:** Regression invariant: schema v5 envelope rejects geospatial code dictionary. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_schema_v5_envelope_rejects_geospatial_code_dictionary() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="dictionary\|DataFrame")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_schema_v5_envelope_result` | `tests.unit.test_resolve_planning_feature_codes._schema_v5_envelope_result` |
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `result.code_dictionary.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_planning_feature_code_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `replace` | `dataclasses.replace` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_schema_v5_envelope_rejects_geospatial_code_dictionary() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    dictionary = gpd.GeoDataFrame(result.code_dictionary.copy(deep=True))
    with pytest.raises(PlanningFeatureCodeError, match="dictionary|DataFrame"):
        module.validate_planning_feature_code_result_envelope(
            replace(result, code_dictionary=dictionary)
        )
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_schema_v5_dictionary_schema_is_explicit`

**Purpose:** Regression invariant: schema v5 dictionary schema is explicit. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_schema_v5_dictionary_schema_is_explicit(mutation: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "mutation", ["dtype", "range-index", "index-name", "index-dtype"]
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="dictionary\|schema\|dtype\|index")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_schema_v5_envelope_result` | `tests.unit.test_resolve_planning_feature_codes._schema_v5_envelope_result` |
| `result.code_dictionary.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `dictionary["official_label"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.RangeIndex` | `pandas.RangeIndex` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `dictionary.index.rename` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Index` | `pandas.Index` |
| `dictionary.index.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_result_with_hashes` | `landscout.stages.resolve_planning_feature_codes._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_planning_feature_code_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `dictionary["official_label"] = dictionary["official_label"].astype("category")`<br>`dictionary.index = pd.RangeIndex(len(dictionary))`<br>`dictionary.index = dictionary.index.rename("changed")`<br>`dictionary.index.rename("changed")`<br>`dictionary.index = pd.Index(dictionary.index.to_numpy(), dtype="uint64")` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_schema_v5_dictionary_schema_is_explicit(mutation: str) -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    dictionary = result.code_dictionary.copy(deep=True)
    if mutation == "dtype":
        dictionary["official_label"] = dictionary["official_label"].astype("category")
    elif mutation == "range-index":
        dictionary.index = pd.RangeIndex(len(dictionary))
    elif mutation == "index-name":
        dictionary.index = dictionary.index.rename("changed")
    else:
        dictionary.index = pd.Index(dictionary.index.to_numpy(), dtype="uint64")
    changed = _result_with_hashes(replace(result, code_dictionary=dictionary))
    with pytest.raises(PlanningFeatureCodeError, match="dictionary|schema|dtype|index"):
        module.validate_planning_feature_code_result_envelope(changed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_schema_v5_dictionary_rows_are_intrinsically_validated`

**Purpose:** Regression invariant: schema v5 dictionary rows are intrinsically validated. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_schema_v5_dictionary_rows_are_intrinsically_validated(mutation: str) -> None:
```

- Exact decorators: `pytest.mark.parametrize(
    "mutation",
    [
        "duplicate-pair",
        "unsorted-pairs",
        "malformed-type",
        "malformed-subtype",
        "wrong-family",
        "wrong-url",
        "wrong-profile",
        "wrong-profile-sha",
        "literal-null-reference",
    ],
)`.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `mutation` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>        PlanningFeatureCodeError, match="dictionary\|pair\|code\|family\|URL\|profile\|order"<br>    )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_schema_v5_envelope_result` | `tests.unit.test_resolve_planning_feature_codes._schema_v5_envelope_result` |
| `result.code_dictionary.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `dictionary.loc[<br>            dictionary.index[0], ["feature_family", "type_code", "subtype_code"]<br>        ].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `dictionary.iloc[::-1].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_result_with_hashes` | `landscout.stages.resolve_planning_feature_codes._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_planning_feature_code_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.mark.parametrize` | `pytest.mark.parametrize` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `dictionary.loc[<br>            dictionary.index[1], ["feature_family", "type_code", "subtype_code"]<br>        ] = dictionary.loc[<br>            dictionary.index[0], ["feature_family", "type_code", "subtype_code"]<br>        ].tolist()`<br>`dictionary.loc[dictionary.index[0], "type_code"] = "1"`<br>`dictionary.loc[dictionary.index[0], "subtype_code"] = "000"`<br>`dictionary.loc[dictionary.index[0], "feature_family"] = "ZONING"`<br>`dictionary.loc[dictionary.index[0], "official_source_url"] = (<br>            "https://example.com/codes"<br>        )`<br>`dictionary.loc[dictionary.index[0], "profile"] = "other-profile"`<br>`dictionary.loc[dictionary.index[0], "profile_sha256"] = "a" * 64`<br>`dictionary.loc[dictionary.index[0], "legal_reference"] = "None"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_schema_v5_dictionary_rows_are_intrinsically_validated(mutation: str) -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    dictionary = result.code_dictionary.copy(deep=True)
    if mutation == "duplicate-pair":
        dictionary.loc[
            dictionary.index[1], ["feature_family", "type_code", "subtype_code"]
        ] = dictionary.loc[
            dictionary.index[0], ["feature_family", "type_code", "subtype_code"]
        ].tolist()
    elif mutation == "unsorted-pairs":
        dictionary = dictionary.iloc[::-1].copy(deep=True)
    elif mutation == "malformed-type":
        dictionary.loc[dictionary.index[0], "type_code"] = "1"
    elif mutation == "malformed-subtype":
        dictionary.loc[dictionary.index[0], "subtype_code"] = "000"
    elif mutation == "wrong-family":
        dictionary.loc[dictionary.index[0], "feature_family"] = "ZONING"
    elif mutation == "wrong-url":
        dictionary.loc[dictionary.index[0], "official_source_url"] = (
            "https://example.com/codes"
        )
    elif mutation == "wrong-profile":
        dictionary.loc[dictionary.index[0], "profile"] = "other-profile"
    elif mutation == "wrong-profile-sha":
        dictionary.loc[dictionary.index[0], "profile_sha256"] = "a" * 64
    else:
        dictionary.loc[dictionary.index[0], "legal_reference"] = "None"
    changed = _result_with_hashes(replace(result, code_dictionary=dictionary))
    with pytest.raises(
        PlanningFeatureCodeError, match="dictionary|pair|code|family|URL|profile|order"
    ):
        module.validate_planning_feature_code_result_envelope(changed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_schema_v5_scalar_lineage_contracts_are_intrinsic`

**Purpose:** Regression invariant: schema v5 scalar lineage contracts are intrinsic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_schema_v5_scalar_lineage_contracts_are_intrinsic() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="standard\|SHA\|sha\|lineage")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_schema_v5_envelope_result` | `tests.unit.test_resolve_planning_feature_codes._schema_v5_envelope_result` |
| `_result_with_hashes` | `landscout.stages.resolve_planning_feature_codes._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_planning_feature_code_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_schema_v5_scalar_lineage_contracts_are_intrinsic() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    changed_standard = _result_with_hashes(
        replace(result, standard_model="CNIG PLU v2099")
    )
    malformed_sha = _result_with_hashes(
        replace(result, planning_document_context_sha256="not-a-sha")
    )
    for changed in (changed_standard, malformed_sha):
        with pytest.raises(PlanningFeatureCodeError, match="standard|SHA|sha|lineage"):
            module.validate_planning_feature_code_result_envelope(changed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic`

**Purpose:** Regression invariant: schema v5 official rows and relation feature agreement are intrinsic. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic() -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(<br>            PlanningFeatureCodeError,<br>            match="official\|meaning\|UNKNOWN\|relation\|feature",<br>        )`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_schema_v5_envelope_result` | `tests.unit.test_resolve_planning_feature_codes._schema_v5_envelope_result` |
| `result.surface_features.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_result_with_hashes` | `landscout.stages.resolve_planning_feature_codes._result_with_hashes` |
| `replace` | `dataclasses.replace` |
| `result.relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_planning_feature_code_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `surface.loc[surface.index[0], "official_code_label"] = pd.NA`<br>`surface.loc[surface.index[0], "official_code_status"] = "UNKNOWN_CODE_PAIR"`<br>`relations.loc[relations.index[0], "official_code_label"] = "Other official meaning"` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_label"] = pd.NA
    missing_meaning = _result_with_hashes(replace(result, surface_features=surface))

    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_status"] = "UNKNOWN_CODE_PAIR"
    invented_unknown = _result_with_hashes(replace(result, surface_features=surface))

    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "official_code_label"] = "Other official meaning"
    mismatched_relation = _result_with_hashes(replace(result, relations=relations))

    for changed in (missing_meaning, invented_unknown, mismatched_relation):
        with pytest.raises(
            PlanningFeatureCodeError,
            match="official|meaning|UNKNOWN|relation|feature",
        ):
            module.validate_planning_feature_code_result_envelope(changed)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.

### `test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result`

**Purpose:** Regression invariant: schema v5 envelope requires exact result type and accepts valid result. Exact mutation, invocation, expected exception, and assertions are reproduced below.

**Exact signature**

```python
def test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result() -> (
    None
):
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

- No parameters.

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.
- Exact expected-exception contexts:
  - `pytest.raises(PlanningFeatureCodeError, match="type\|result")`

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `importlib.import_module` | `importlib.import_module` |
| `_schema_v5_envelope_result` | `tests.unit.test_resolve_planning_feature_codes._schema_v5_envelope_result` |
| `DerivedPlanningFeatureCodeResult` | `unresolved local/third-party receiver; no ownership inferred` |
| `pytest.raises` | `pytest.raises` |
| `module.validate_planning_feature_code_result_envelope` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result() -> (
    None
):
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()

    class DerivedPlanningFeatureCodeResult(PlanningFeatureCodeResult):
        pass

    derived = DerivedPlanningFeatureCodeResult(**result.__dict__)
    with pytest.raises(PlanningFeatureCodeError, match="type|result"):
        module.validate_planning_feature_code_result_envelope(derived)
    module.validate_planning_feature_code_result_envelope(result)
```

**Business boundary**

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.


## 7. Test-specific regression contract

- Test functions: **74**.
- Pytest fixtures (decorator-proven): **0**.

### Per-test regression index

| Test | Parametrization | Expected exception contexts | Assertion count | Exact regression purpose |
|---|---|---|---:|---|
| `test_exact_family_pair_resolution_and_leading_zeros` | none | none | 6 | Proves exact family pair resolution and leading zeros using the exact source reproduced in section 7. |
| `test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` | none | none | 5 | Proves no type only or cross family fallback and unknown is retained using the exact source reproduced in section 7. |
| `test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated` | none | pytest.raises(PlanningFeatureCodeError, match="profile\|canonical") | 0 | Proves in memory profile model copy with wrong hash is revalidated using the exact source reproduced in section 7. |
| `test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` | none | pytest.raises(PlanningFeatureCodeError, match="schema\|profile") | 0 | Proves in memory profile model construct with invalid schema is revalidated using the exact source reproduced in section 7. |
| `test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` | none | pytest.raises(PlanningFeatureCodeError, match="duplicate\|profile") | 0 | Proves in memory profile model construct with duplicate pair is revalidated using the exact source reproduced in section 7. |
| `test_official_family_endpoints_require_exact_identity` | pytest.mark.parametrize(<br>    ("family", "url"),<br>    [<br>        ("prescription", "https://www.geoportail-urbanisme.gouv.fr/another/path"),<br>        ("prescription", f"{P_URL}?format=json"),<br>        (<br>            "prescription",<br>            "https://www.geoportail-urbanisme.gouv.fr:444/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",<br>        ),<br>        (<br>            "prescription",<br>            "https://user@www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",<br>        ),<br>        (<br>            "prescription",<br>            "https://geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",<br>        ),<br>        ("prescription", I_URL),<br>        ("information", P_URL),<br>        ("information", f"{I_URL}#codes"),<br>        ("information", f"{I_URL}/"),<br>        ("information", I_URL.replace("https://", "http://")),<br>    ],<br>) | pytest.raises(ValueError, match="official\|source\|URL") | 0 | Proves official family endpoints require exact identity using the exact source reproduced in section 7. |
| `test_official_text_must_already_be_canonical` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("official_label", "Repeated  whitespace"),<br>        ("official_label", "Decomposed e\u0301"),<br>        ("legal_reference", "L151-1\n  L151-2"),<br>        ("regulation_or_annex_reference", " R151-1"),<br>    ],<br>) | pytest.raises(<br>        ValueError,<br>        match="GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1\|canonical\|normalization\|exact",<br>    ) | 0 | Proves official text must already be canonical using the exact source reproduced in section 7. |
| `test_malformed_code_is_rejected` | pytest.mark.parametrize("code", ["1", "001", "A1", " 01", "01 ", 1]) | pytest.raises(ValueError) | 0 | Proves malformed code is rejected using the exact source reproduced in section 7. |
| `test_duplicate_pair_and_profile_hash_mutation_are_rejected` | none | pytest.raises(ValueError, match="duplicate"); pytest.raises(ValueError, match="canonical") | 0 | Proves duplicate pair and profile hash mutation are rejected using the exact source reproduced in section 7. |
| `test_wrong_official_host_and_unknown_field_are_rejected` | none | pytest.raises(ValueError, match="official\|exact"); pytest.raises(ValueError) | 0 | Proves wrong official host and unknown field are rejected using the exact source reproduced in section 7. |
| `test_duplicate_yaml_key_is_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="Duplicate YAML") | 0 | Proves duplicate yaml key is rejected using the exact source reproduced in section 7. |
| `test_wrong_planning_standard_is_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="standard") | 0 | Proves wrong planning standard is rejected using the exact source reproduced in section 7. |
| `test_catalogs_and_relations_are_preserved_and_inputs_immutable` | none | none | 3 | Proves catalogs and relations are preserved and inputs immutable using the exact source reproduced in section 7. |
| `test_complete_normalized_catalog_schema_is_required` | pytest.mark.parametrize(<br>    ("catalog_position", "column"),<br>    [<br>        (1, "feature_area_m2"),<br>        (2, "feature_length_m"),<br>        (3, "point_member_count"),<br>        (1, "label_raw"),<br>        (1, "source_crs"),<br>    ],<br>) | pytest.raises(PlanningFeatureCodeError, match="normalized\|schema\|column") | 0 | Proves complete normalized catalog schema is required using the exact source reproduced in section 7. |
| `test_unexpected_factual_catalog_column_is_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="normalized\|schema\|column") | 0 | Proves unexpected factual catalog column is rejected using the exact source reproduced in section 7. |
| `test_cnig_identity_provenance_is_exact` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("source_identity_kind", "UNKNOWN_KIND"),<br>        ("source_identity_field", "LIB_IDINFO"),<br>    ],<br>) | pytest.raises(<br>        PlanningFeatureCodeError, match="identity\|provenance\|normalized"<br>    ) | 0 | Proves cnig identity provenance is exact using the exact source reproduced in section 7. |
| `test_ogr_fid_provenance_is_restricted` | pytest.mark.parametrize(<br>    ("logical_layer", "feature_family", "source_feature_id"),<br>    [<br>        ("information_surface", "INFORMATION", "OGR_FID:1"),<br>        ("prescription_surface", "PRESCRIPTION", "1"),<br>    ],<br>) | pytest.raises(<br>        PlanningFeatureCodeError, match="OGR\|identity\|provenance\|normalized"<br>    ) | 0 | Proves ogr fid provenance is restricted using the exact source reproduced in section 7. |
| `test_source_feature_id_is_unique_inside_logical_layer` | none | pytest.raises(PlanningFeatureCodeError, match="source_feature_id\|unique") | 0 | Proves source feature id is unique inside logical layer using the exact source reproduced in section 7. |
| `test_catalog_crs_must_be_canonical_epsg_2154` | none | pytest.raises(PlanningFeatureCodeError, match="EPSG:2154\|CRS") | 0 | Proves catalog crs must be canonical epsg 2154 using the exact source reproduced in section 7. |
| `test_catalog_geometry_metrics_are_revalidated` | pytest.mark.parametrize(<br>    ("catalog_position", "column", "value"),<br>    [<br>        (1, "feature_area_m2", 99.0),<br>        (2, "feature_length_m", 99.0),<br>        (3, "point_member_count", 2),<br>    ],<br>) | pytest.raises(PlanningFeatureCodeError, match="metric\|area\|length\|member") | 0 | Proves catalog geometry metrics are revalidated using the exact source reproduced in section 7. |
| `test_complete_relation_schema_is_required` | none | pytest.raises(PlanningFeatureCodeError, match="relation\|schema\|column") | 0 | Proves complete relation schema is required using the exact source reproduced in section 7. |
| `test_unexpected_factual_relation_column_is_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="relation\|schema") | 0 | Proves unexpected factual relation column is rejected using the exact source reproduced in section 7. |
| `test_cnig_resolver_invokes_shared_factual_contract` | none | pytest.raises(<br>        PlanningFeatureCodeError, match="shared factual contract marker"<br>    ) | 1 | Proves cnig resolver invokes shared factual contract using the exact source reproduced in section 7. |
| `test_complete_relation_catalog_agreement_is_required` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("label_raw", "mutated label"),<br>        ("source_validity_date_raw", "19990101"),<br>        ("regulation_filename_raw", "other.pdf"),<br>        ("feature_area_m2", 3.0),<br>    ],<br>) | pytest.raises(<br>        PlanningFeatureCodeError, match="catalog\|metric\|normalized\|feature share"<br>    ) | 0 | Proves complete relation catalog agreement is required using the exact source reproduced in section 7. |
| `test_surface_relation_metrics_are_revalidated` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("intersection_area_m2", 0.0),<br>        ("intersection_area_m2", -1.0),<br>        ("intersection_area_m2", float("inf")),<br>        ("parcel_share_pct", 99.0),<br>    ],<br>) | pytest.raises(<br>        PlanningFeatureCodeError, match="relation\|metric\|finite\|percentage"<br>    ) | 0 | Proves surface relation metrics are revalidated using the exact source reproduced in section 7. |
| `test_line_relation_metrics_are_revalidated` | pytest.mark.parametrize(<br>    ("column", "value"),<br>    [<br>        ("intersection_length_m", 0.0),<br>        ("relation_type", "TOUCH_ONLY"),<br>        ("source_line_length_m", 1.0),<br>    ],<br>) | pytest.raises(PlanningFeatureCodeError, match="relation\|length\|catalog") | 0 | Proves line relation metrics are revalidated using the exact source reproduced in section 7. |
| `test_duplicate_catalog_columns_are_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="duplicate\|columns") | 0 | Proves duplicate catalog columns are rejected using the exact source reproduced in section 7. |
| `test_missing_catalog_crs_is_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="CRS") | 0 | Proves missing catalog crs is rejected using the exact source reproduced in section 7. |
| `test_unparseable_catalog_crs_is_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="CRS") | 0 | Proves unparseable catalog crs is rejected using the exact source reproduced in section 7. |
| `test_inactive_or_wrong_geometry_column_is_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="geometry") | 0 | Proves inactive or wrong geometry column is rejected using the exact source reproduced in section 7. |
| `test_surface_geometry_contract_is_enforced` | pytest.mark.parametrize(<br>    ("geometry", "message"),<br>    [<br>        (None, "null\|geometry"),<br>        (Polygon(), "empty\|geometry"),<br>        (Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)]), "invalid\|geometry"),<br>        (LineString([(0, 0), (1, 1)]), "type\|geometry\|SURFACE"),<br>    ],<br>) | pytest.raises(PlanningFeatureCodeError, match=message) | 0 | Proves surface geometry contract is enforced using the exact source reproduced in section 7. |
| `test_valid_multi_geometries_are_accepted` | pytest.mark.parametrize(<br>    ("catalog_name", "geometry"),<br>    [<br>        ("surface", MultiPolygon([Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])])),<br>        ("line", MultiLineString([[(0, 0), (2, 0)]])),<br>        ("point", MultiPoint([(0, 0), (1, 1)])),<br>    ],<br>) | none | 1 | Proves valid multi geometries are accepted using the exact source reproduced in section 7. |
| `test_catalog_semantic_and_string_contracts_are_enforced` | pytest.mark.parametrize(<br>    ("column", "value", "message"),<br>    [<br>        ("geometry_kind", "LINE", "geometry kind\|SURFACE"),<br>        ("logical_layer", "prescription_line", "logical layer\|surface"),<br>        ("feature_family", "INFORMATION", "family\|logical layer"),<br>        ("source_identity_kind", None, "source identity\|exact string"),<br>        ("source_layer", " SOURCE ", "source layer\|exact string"),<br>    ],<br>) | pytest.raises(PlanningFeatureCodeError, match=message) | 0 | Proves catalog semantic and string contracts are enforced using the exact source reproduced in section 7. |
| `test_every_required_catalog_identity_is_an_exact_non_null_string` | pytest.mark.parametrize(<br>    "column",<br>    [<br>        "planning_feature_id",<br>        "source_feature_id",<br>        "source_identity_kind",<br>        "source_identity_field",<br>        "logical_layer",<br>        "feature_family",<br>        "geometry_kind",<br>        "source_layer",<br>    ],<br>) | pytest.raises(PlanningFeatureCodeError, match="exact string\|non-empty") | 0 | Proves every required catalog identity is an exact non null string using the exact source reproduced in section 7. |
| `test_line_and_point_geometry_types_are_enforced` | pytest.mark.parametrize(<br>    ("catalog_name", "geometry"),<br>    [<br>        ("line", Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])),<br>        ("point", LineString([(0, 0), (1, 1)])),<br>    ],<br>) | pytest.raises(PlanningFeatureCodeError, match="geometry\|type") | 0 | Proves line and point geometry types are enforced using the exact source reproduced in section 7. |
| `test_planning_feature_ids_are_globally_unique_across_catalogs` | none | pytest.raises(PlanningFeatureCodeError, match="unique\|catalog\|deterministic") | 0 | Proves planning feature ids are globally unique across catalogs using the exact source reproduced in section 7. |
| `test_valid_empty_optional_catalogs_preserve_schema_and_crs` | none | none | 4 | Proves valid empty optional catalogs preserve schema and crs using the exact source reproduced in section 7. |
| `test_relation_catalog_code_mismatch_is_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="catalog") | 0 | Proves relation catalog code mismatch is rejected using the exact source reproduced in section 7. |
| `test_duplicate_relation_columns_are_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="duplicate\|columns") | 0 | Proves duplicate relation columns are rejected using the exact source reproduced in section 7. |
| `test_relation_identity_must_be_an_exact_non_null_string` | pytest.mark.parametrize("column", ["parcel_id", "planning_feature_id"]); pytest.mark.parametrize("value", [None, " invalid "]) | pytest.raises(PlanningFeatureCodeError, match="relation\|exact string") | 0 | Proves relation identity must be an exact non null string using the exact source reproduced in section 7. |
| `test_duplicate_parcel_feature_relation_is_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="unique\|duplicate") | 0 | Proves duplicate parcel feature relation is rejected using the exact source reproduced in section 7. |
| `test_unknown_relation_feature_id_is_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="unknown") | 0 | Proves unknown relation feature id is rejected using the exact source reproduced in section 7. |
| `test_relation_type_must_match_catalog_geometry_kind` | pytest.mark.parametrize(<br>    ("geometry_kind", "relation_type"),<br>    [<br>        ("SURFACE", "LENGTH_OVERLAP"),<br>        ("SURFACE", "NOT_A_RELATION"),<br>        ("LINE", "INSIDE"),<br>        ("POINT", "AREA_OVERLAP"),<br>    ],<br>) | pytest.raises(PlanningFeatureCodeError, match="[Rr]elation type\|geometry") | 0 | Proves relation type must match catalog geometry kind using the exact source reproduced in section 7. |
| `test_valid_relation_types_are_retained` | pytest.mark.parametrize(<br>    ("geometry_kind", "relation_type"),<br>    [<br>        ("SURFACE", "AREA_OVERLAP"),<br>        ("SURFACE", "TOUCH_ONLY"),<br>        ("LINE", "LENGTH_OVERLAP"),<br>        ("LINE", "TOUCH_ONLY"),<br>        ("POINT", "INSIDE"),<br>        ("POINT", "BOUNDARY_TOUCH"),<br>    ],<br>) | none | 1 | Proves valid relation types are retained using the exact source reproduced in section 7. |
| `test_coordinated_output_hash_mutation_is_rejected` | none | pytest.raises(PlanningFeatureCodeError, match="rebuilt\|meaning\|dictionary") | 0 | Proves coordinated output hash mutation is rejected using the exact source reproduced in section 7. |
| `test_parquet_readback_passes_source_complete_validation` | none | none | 0 | Proves parquet readback passes source complete validation using the exact source reproduced in section 7. |
| `test_record_order_must_be_deterministic` | none | pytest.raises(ValueError, match="deterministic order") | 0 | Proves record order must be deterministic using the exact source reproduced in section 7. |
| `test_yaml_snapshot_loads_strictly` | none | none | 1 | Proves yaml snapshot loads strictly using the exact source reproduced in section 7. |
| `test_stable_public_api_is_exported_from_module_and_stage_package` | none | none | 5 | Proves stable public api is exported from module and stage package using the exact source reproduced in section 7. |
| `test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs` | none | none | 10 | Proves checked in official snapshot is complete for observed muret pairs using the exact source reproduced in section 7. |
| `test_result_schema_versions_are_strict` | pytest.mark.parametrize(<br>    ("field", "value"),<br>    [<br>        ("result_hash_schema_version", True),<br>        ("result_hash_schema_version", 0),<br>        ("result_hash_schema_version", 1),<br>        ("result_hash_schema_version", 2),<br>        ("result_hash_schema_version", 3),<br>        ("result_hash_schema_version", 4),<br>        ("result_hash_schema_version", 6),<br>        ("result_hash_schema_version", 5.0),<br>        ("result_hash_schema_version", "5"),<br>        ("profile_schema_version", True),<br>        ("profile_schema_version", 0),<br>        ("profile_schema_version", 1),<br>        ("profile_schema_version", 3),<br>        ("profile_schema_version", 2.0),<br>        ("profile_schema_version", "2"),<br>    ],<br>) | pytest.raises(PlanningFeatureCodeError, match="schema version") | 0 | Proves result schema versions are strict using the exact source reproduced in section 7. |
| `test_step_7d_3_1_output_integrates_with_public_coding_api` | none | none | 7 | Proves step 7d 3 1 output integrates with public coding api using the exact source reproduced in section 7. |
| `test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats` | none | none | 2 | Proves resolver runs heavy factual validation once and public validator repeats using the exact source reproduced in section 7. |
| `test_coded_result_persists_all_source_input_hashes` | none | none | 2 | Proves coded result persists all source input hashes using the exact source reproduced in section 7. |
| `test_source_input_hash_mutation_is_rejected` | pytest.mark.parametrize(<br>    "field",<br>    [<br>        "planning_document_context_sha256",<br>        "parcel_identity_input_sha256",<br>        "normalized_catalogs_input_sha256",<br>        "normalized_relations_input_sha256",<br>        "gpu_related_source_files_sha256",<br>        "expected_relations_content_sha256",<br>    ],<br>) | pytest.raises(PlanningFeatureCodeError, match="hash\|rebuilt\|source") | 0 | Proves source input hash mutation is rejected using the exact source reproduced in section 7. |
| `test_gpu_related_source_hash_is_deterministic_across_cache_roots` | none | none | 1 | Proves gpu related source hash is deterministic across cache roots using the exact source reproduced in section 7. |
| `test_source_binding_hashes_bind_every_component_hash` | pytest.mark.parametrize(<br>    "field",<br>    ["gpu_related_source_files_sha256", "expected_relations_content_sha256"],<br>) | none | 1 | Proves source binding hashes bind every component hash using the exact source reproduced in section 7. |
| `test_parcel_source_change_invalidates_coded_result` | none | pytest.raises(PlanningFeatureCodeError, match="parcel\|source\|rebuilt") | 0 | Proves parcel source change invalidates coded result using the exact source reproduced in section 7. |
| `test_gpu_document_context_change_invalidates_coded_result` | none | pytest.raises(PlanningFeatureCodeError, match="document\|source\|rebuilt") | 0 | Proves gpu document context change invalidates coded result using the exact source reproduced in section 7. |
| `test_normalized_catalog_change_invalidates_coded_result_even_when_coherent` | none | pytest.raises(PlanningFeatureCodeError, match="normalized\|source\|rebuilt") | 0 | Proves normalized catalog change invalidates coded result even when coherent using the exact source reproduced in section 7. |
| `test_normalized_relation_change_invalidates_coded_result` | none | pytest.raises(PlanningFeatureCodeError, match="[Rr]elation\|source\|rebuilt") | 0 | Proves normalized relation change invalidates coded result using the exact source reproduced in section 7. |
| `test_coding_api_rejects_relation_set_not_rebuilt_from_geometry` | pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "metric"]) | pytest.raises(<br>        PlanningFeatureCodeError,<br>        match="relation\|parcel\|source\|rebuilt\|normalized",<br>    ) | 0 | Proves coding api rejects relation set not rebuilt from geometry using the exact source reproduced in section 7. |
| `test_schema_v5_parquet_readback_preserves_source_hash_envelope` | none | none | 0 | Proves schema v5 parquet readback preserves source hash envelope using the exact source reproduced in section 7. |
| `test_schema_v5_public_api_signatures_remain_source_complete` | none | none | 2 | Proves schema v5 public api signatures remain source complete using the exact source reproduced in section 7. |
| `test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator` | none | pytest.raises(PlanningFeatureCodeError, match="hash\|invalid") | 1 | Proves step 7d 5b 2b 5 exposes lightweight coded result validator using the exact source reproduced in section 7. |
| `test_schema_v5_envelope_rejects_canonical_empty_code_dictionary` | none | pytest.raises(PlanningFeatureCodeError, match="dictionary\|empty\|record") | 0 | Proves schema v5 envelope rejects canonical empty code dictionary using the exact source reproduced in section 7. |
| `test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs` | none | none | 2 | Proves schema v5 envelope accepts nonempty dictionary with empty outputs using the exact source reproduced in section 7. |
| `test_schema_v5_envelope_controls_malformed_dictionary_type` | pytest.mark.parametrize("dictionary", [None, "not-a-frame"]) | pytest.raises(PlanningFeatureCodeError) | 0 | Proves schema v5 envelope controls malformed dictionary type using the exact source reproduced in section 7. |
| `test_schema_v5_envelope_rejects_geospatial_code_dictionary` | none | pytest.raises(PlanningFeatureCodeError, match="dictionary\|DataFrame") | 0 | Proves schema v5 envelope rejects geospatial code dictionary using the exact source reproduced in section 7. |
| `test_schema_v5_dictionary_schema_is_explicit` | pytest.mark.parametrize(<br>    "mutation", ["dtype", "range-index", "index-name", "index-dtype"]<br>) | pytest.raises(PlanningFeatureCodeError, match="dictionary\|schema\|dtype\|index") | 0 | Proves schema v5 dictionary schema is explicit using the exact source reproduced in section 7. |
| `test_schema_v5_dictionary_rows_are_intrinsically_validated` | pytest.mark.parametrize(<br>    "mutation",<br>    [<br>        "duplicate-pair",<br>        "unsorted-pairs",<br>        "malformed-type",<br>        "malformed-subtype",<br>        "wrong-family",<br>        "wrong-url",<br>        "wrong-profile",<br>        "wrong-profile-sha",<br>        "literal-null-reference",<br>    ],<br>) | pytest.raises(<br>        PlanningFeatureCodeError, match="dictionary\|pair\|code\|family\|URL\|profile\|order"<br>    ) | 0 | Proves schema v5 dictionary rows are intrinsically validated using the exact source reproduced in section 7. |
| `test_schema_v5_scalar_lineage_contracts_are_intrinsic` | none | pytest.raises(PlanningFeatureCodeError, match="standard\|SHA\|sha\|lineage") | 0 | Proves schema v5 scalar lineage contracts are intrinsic using the exact source reproduced in section 7. |
| `test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic` | none | pytest.raises(<br>            PlanningFeatureCodeError,<br>            match="official\|meaning\|UNKNOWN\|relation\|feature",<br>        ) | 0 | Proves schema v5 official rows and relation feature agreement are intrinsic using the exact source reproduced in section 7. |
| `test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result` | none | pytest.raises(PlanningFeatureCodeError, match="type\|result") | 0 | Proves schema v5 envelope requires exact result type and accepts valid result using the exact source reproduced in section 7. |

## 8. Public exports and package ownership

This module declares no `__all__`; no package-level public guarantee is inferred from direct importability alone.

## 9. Trust, provenance, side effects, and business boundary

- This file contributes test evidence only; it does not itself acquire production data, change policy meaning, or make parcel decisions.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
from __future__ import annotations

import importlib
import inspect
import json
import shutil
import tempfile
from dataclasses import replace
from hashlib import sha256
from pathlib import Path

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd
import pytest
import yaml  # type: ignore[import-untyped]
from geopandas.testing import assert_geodataframe_equal
from shapely.geometry import (
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)

from landscout.common.planning_feature_schema import (
    NORMALIZED_RELATION_DTYPES,
    feature_dtypes,
    relation_dtypes,
)
from landscout.sources import gpu_fr as gpu_source_module
from landscout.sources.gpu_fr import (
    EXTRACTION_MANIFEST_NAME,
    GpuArchiveDownload,
    GpuDocumentMetadata,
    GpuExtractedFile,
    GpuExtraction,
    GpuInspectedLayer,
    GpuLayerSummary,
    GpuPlanningDocument,
    GpuSourceConfig,
    GpuSpatialLayerReference,
    load_gpu_source_config,
)
from landscout.stages.enrich_planning_features import (
    RELATION_COLUMNS,
    intersect_parcels_with_gpu_planning_features,
)
from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)
from landscout.stages.resolve_planning_feature_codes import (
    resolve_planning_feature_codes as _public_resolve_planning_feature_codes,
)
from landscout.stages.resolve_planning_feature_codes import (
    validate_planning_feature_code_result as _public_validate_planning_feature_code_result,
)


def _canonical_relation_schema(frame: pd.DataFrame) -> pd.DataFrame:
    output = frame.copy(deep=True)
    for column, dtype in zip(RELATION_COLUMNS, NORMALIZED_RELATION_DTYPES, strict=True):
        output[column] = pd.Series(
            output[column].tolist(), index=output.index, dtype=dtype
        )
    output.index = pd.RangeIndex(len(output))
    return output


P_URL = "https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"
I_URL = "https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"
TEXT_NORMALIZATION = "GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"


def _records_hash(records: list[dict[str, object]]) -> str:
    ordered = sorted(
        records,
        key=lambda row: (row["feature_family"], row["type_code"], row["subtype_code"]),
    )
    payload = json.dumps(
        ordered,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return sha256(payload).hexdigest()


def _payload_hash(payload: object) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return sha256(encoded).hexdigest()


def _record(
    family: str,
    type_code: str,
    subtype_code: str,
    label: str,
) -> dict[str, object]:
    return {
        "feature_family": family,
        "type_code": type_code,
        "subtype_code": subtype_code,
        "official_label": label,
        "legal_reference": None,
        "regulation_or_annex_reference": None,
        "official_source_url": P_URL if family == "PRESCRIPTION" else I_URL,
    }


def _profile_payload() -> dict[str, object]:
    records = [
        _record("INFORMATION", "02", "00", "Information two"),
        _record("INFORMATION", "99", "00", "Other information"),
        _record("PRESCRIPTION", "07", "00", "Prescription seven"),
        _record("PRESCRIPTION", "07", "04", "Prescription seven subtype four"),
    ]
    return {
        "schema_version": 2,
        "profile": "synthetic_cnig_plu_2017",
        "standard_model": "CNIG PLU v2017",
        "official_text_normalization": TEXT_NORMALIZATION,
        "official_sources": {
            "prescription": P_URL,
            "information": I_URL,
        },
        "retrieval_date": "2026-08-12",
        "canonical_records_sha256": _records_hash(records),
        "records": records,
    }


def _profile() -> CnigFeatureCodeProfile:
    return CnigFeatureCodeProfile.model_validate(_profile_payload())


def _physical_inventory(root: Path) -> tuple[GpuExtractedFile, ...]:
    return tuple(
        GpuExtractedFile(
            relative_path=path.relative_to(root).as_posix(),
            file_type=path.suffix.casefold().lstrip(".") or "none",
            size_bytes=path.stat().st_size,
            sha256=sha256(path.read_bytes()).hexdigest(),
            category="SPATIAL_DATA",
        )
        for path in sorted(
            (item for item in root.rglob("*") if item.is_file()), key=str
        )
        if not (path.parent == root and path.name == EXTRACTION_MANIFEST_NAME)
    )


def _write_extraction_manifest(
    root: Path,
    archive_sha256: str,
    files: tuple[GpuExtractedFile, ...],
) -> None:
    (root / EXTRACTION_MANIFEST_NAME).write_text(
        json.dumps(
            {
                "schema_version": 2,
                "archive_sha256": archive_sha256,
                "files": [
                    {
                        "relative_path": item.relative_path,
                        "size_bytes": item.size_bytes,
                        "sha256": item.sha256,
                    }
                    for item in files
                ],
            },
            sort_keys=True,
            separators=(",", ":"),
        ),
        encoding="utf-8",
    )


def _layer_summary(frame: gpd.GeoDataFrame, source_layer: str) -> GpuLayerSummary:
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    return GpuLayerSummary(
        source_document_id="doc-1",
        source_archive_sha256="a" * 64,
        source_layer=source_layer,
        crs=frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(name), int(count))
            for name, count in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )


def _planning_document(
    standard: str = "CNIG PLU v2017",
    related_layers: tuple[GpuInspectedLayer, ...] = (),
) -> GpuPlanningDocument:
    extraction_root = Path(tempfile.mkdtemp(prefix="landscout-code-source-"))
    physical_layers: list[GpuInspectedLayer] = []
    for layer in related_layers:
        path = extraction_root / f"{layer.logical_name}.gpkg"
        layer.data.to_file(
            path,
            layer=layer.reference.source_layer,
            driver="GPKG",
            engine="pyogrio",
            index=False,
        )
        reread = gpd.read_file(
            path, layer=layer.reference.source_layer, engine="pyogrio"
        )
        reference = replace(
            layer.reference,
            dataset_path=path,
            driver="GPKG",
        )
        physical_layers.append(
            replace(
                layer,
                reference=reference,
                data=reread,
                summary=_layer_summary(reread, reference.source_layer),
            )
        )
    related_layers = tuple(physical_layers)
    document = GpuDocumentMetadata(
        provider="Géoportail de l'Urbanisme",
        portal="G\u00e9oportail de l'Urbanisme",
        commune_code="31395",
        partition="DU_31395",
        document_id="doc-1",
        document_family="DU",
        document_type="PLU",
        document_title=None,
        status="document.production",
        legal_status="APPROVED",
        effective_status="EN_VIGUEUR",
        version="10",
        archive_name="31395_PLU_20240215",
        publication_timestamp=None,
        update_timestamp=None,
        revision_date=None,
        producer=None,
        standard_model=None,
        projection="EPSG:2154",
        metadata_identifier=None,
        source_url="https://www.geoportail-urbanisme.gouv.fr/api/document/download-by-partition/DU_31395",
        written_files=(),
    )
    archive = GpuArchiveDownload(
        document=document,
        download_timestamp="2026-08-12T00:00:00Z",
        filename="31395_PLU_20240215.zip",
        archive_format="zip",
        file_size=1,
        sha256="a" * 64,
        path=Path("synthetic.zip"),
        cache_hit=True,
    )
    zoning_data = gpd.GeoDataFrame(
        {"LIB_IDZONE": ["Z1"]},
        geometry=[Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])],
        crs="EPSG:2154",
    )
    zoning_path = extraction_root / "zones.gpkg"
    zoning_data.to_file(
        zoning_path,
        layer="ZONE",
        driver="GPKG",
        engine="pyogrio",
        index=False,
    )
    zoning_data = gpd.read_file(zoning_path, layer="ZONE", engine="pyogrio")
    reference = GpuSpatialLayerReference(zoning_path, "ZONE", "GPKG")
    summary = _layer_summary(zoning_data, "ZONE")
    zoning = GpuInspectedLayer("zoning", reference, zoning_data, summary)
    inventory = _physical_inventory(extraction_root)
    _write_extraction_manifest(extraction_root, archive.sha256, inventory)
    extraction = GpuExtraction(
        archive=archive,
        extraction_root=extraction_root,
        files=inventory,
        standard_models=(standard,),
        cache_hit=True,
    )
    config_payload = load_gpu_source_config(
        Path("configs/sources/gpu_fr.yaml")
    ).model_dump(mode="python")
    for role in config_payload["spatial_layers"]:
        config_payload["spatial_layers"][role]["match_tokens"] = [f"unused_{role}"]
    config_payload["spatial_layers"]["zoning"]["match_tokens"] = ["ZONE"]
    for layer in related_layers:
        config_payload["spatial_layers"][layer.logical_name]["match_tokens"] = [
            layer.reference.source_layer
        ]
    source_config = GpuSourceConfig.model_validate(config_payload)
    related_by_logical_name = {layer.logical_name: layer for layer in related_layers}
    related_layers = tuple(
        related_by_logical_name[logical_name]
        for logical_name in gpu_source_module._GPU_LOGICAL_LAYER_NAMES
        if logical_name != "zoning" and logical_name in related_by_logical_name
    )
    return GpuPlanningDocument(
        source_config=source_config,
        source_config_sha256=gpu_source_module._source_config_sha256(source_config),
        extraction=extraction,
        all_spatial_layers=gpu_source_module.discover_gpu_spatial_layers(extraction),
        zoning=zoning,
        related_layers=related_layers,
    )


def _base_row(
    feature_id: str,
    source_id: str,
    family: str,
    layer: str,
    kind: str,
    type_code: str,
    subtype_code: str,
) -> dict[str, object]:
    return {
        "planning_feature_id": feature_id,
        "source_feature_id": source_id,
        "source_identity_kind": "CNIG_ATTRIBUTE",
        "source_identity_field": "LIB_IDPSC"
        if family == "PRESCRIPTION"
        else "LIB_IDINFO",
        "logical_layer": layer,
        "feature_family": family,
        "geometry_kind": kind,
        "type_code_raw": type_code,
        "subtype_code_raw": subtype_code,
        "label_raw": None,
        "text_raw": None,
        "regulation_filename_raw": None,
        "regulation_url_raw": None,
        "source_document_reference_raw": "31395_PLU_20240215",
        "source_validity_date_raw": "20240215",
        "source_provider": "Géoportail de l'Urbanisme",
        "source_portal": "https://www.geoportail-urbanisme.gouv.fr",
        "source_commune_code": "31395",
        "source_document_id": "doc-1",
        "source_document_type": "PLU",
        "source_archive_name": "31395_PLU_20240215",
        "source_archive_sha256": "a" * 64,
        "source_layer": layer.upper(),
        "source_standard_model": "CNIG PLU v2017",
        "source_crs": "EPSG:2154",
    }


def _legacy_inputs():
    surface_rows = [
        _base_row(
            "F-P-0700",
            "P-1",
            "PRESCRIPTION",
            "prescription_surface",
            "SURFACE",
            "07",
            "00",
        ),
        _base_row(
            "F-I-0200",
            "I-1",
            "INFORMATION",
            "information_surface",
            "SURFACE",
            "02",
            "00",
        ),
    ]
    surface = gpd.GeoDataFrame(
        surface_rows,
        geometry=[
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),
            Polygon([(3, 0), (5, 0), (5, 2), (3, 2)]),
        ],
        crs="EPSG:2154",
        index=pd.Index([11, 22], name="source_row"),
    )
    surface["feature_area_m2"] = [4.0, 4.0]
    line = gpd.GeoDataFrame(
        [
            _base_row(
                "F-P-0704",
                "P-2",
                "PRESCRIPTION",
                "prescription_line",
                "LINE",
                "07",
                "04",
            )
        ],
        geometry=[LineString([(0, 0), (2, 0)])],
        crs="EPSG:2154",
        index=pd.Index([33], name="source_row"),
    )
    line["feature_length_m"] = [2.0]
    point = gpd.GeoDataFrame(
        [
            _base_row(
                "F-I-9900",
                "I-2",
                "INFORMATION",
                "information_point",
                "POINT",
                "99",
                "00",
            )
        ],
        geometry=[Point(1, 1)],
        crs="EPSG:2154",
        index=pd.Index([44], name="source_row"),
    )
    point["point_member_count"] = [1]
    relations = pd.DataFrame(
        [
            {
                "parcel_id": "PARCEL-1",
                **{
                    key: surface.iloc[0][key]
                    for key in (
                        "planning_feature_id",
                        "source_feature_id",
                        "source_identity_kind",
                        "source_identity_field",
                        "logical_layer",
                        "feature_family",
                        "geometry_kind",
                        "type_code_raw",
                        "subtype_code_raw",
                        "label_raw",
                        "text_raw",
                        "source_document_id",
                        "source_archive_sha256",
                        "source_layer",
                        "source_validity_date_raw",
                        "regulation_filename_raw",
                    )
                },
                "relation_type": "AREA_OVERLAP",
                "parcel_metric_area_m2": 4.0,
                "feature_area_m2": 4.0,
                "source_line_length_m": None,
                "intersection_area_m2": 4.0,
                "intersection_length_m": None,
                "parcel_share_pct": 100.0,
                "feature_share_pct": 100.0,
                "point_member_count": None,
                "point_members_inside_count": None,
                "point_members_boundary_count": None,
            },
            {
                "parcel_id": "PARCEL-1",
                **{
                    key: line.iloc[0][key]
                    for key in (
                        "planning_feature_id",
                        "source_feature_id",
                        "source_identity_kind",
                        "source_identity_field",
                        "logical_layer",
                        "feature_family",
                        "geometry_kind",
                        "type_code_raw",
                        "subtype_code_raw",
                        "label_raw",
                        "text_raw",
                        "source_document_id",
                        "source_archive_sha256",
                        "source_layer",
                        "source_validity_date_raw",
                        "regulation_filename_raw",
                    )
                },
                "relation_type": "LENGTH_OVERLAP",
                "parcel_metric_area_m2": 4.0,
                "feature_area_m2": None,
                "source_line_length_m": 2.0,
                "intersection_area_m2": None,
                "intersection_length_m": 2.0,
                "parcel_share_pct": None,
                "feature_share_pct": None,
                "point_member_count": None,
                "point_members_inside_count": None,
                "point_members_boundary_count": None,
            },
        ],
        index=pd.Index([101, 102], name="relation_row"),
    )
    relations = relations.loc[:, list(RELATION_COLUMNS)]
    return _planning_document(), surface, line, point, relations, _profile()


def _mutated_profile(**updates: object) -> CnigFeatureCodeProfile:
    """Build a deliberately unvalidated frozen profile for boundary tests."""

    profile = _profile()
    return profile.model_copy(update=updates)


def _empty_catalog(kind: str) -> gpd.GeoDataFrame:
    """Return an optional empty catalog with the deterministic source schema."""

    _, surface, line, point, _, _ = _inputs()
    template = {"SURFACE": surface, "LINE": line, "POINT": point}[kind]
    return template.iloc[0:0].copy()


def _integration_source_frame(
    logical_layer: str,
    geometries: list[object],
    source_ids: list[str],
    type_codes: list[str],
    subtype_codes: list[str],
) -> gpd.GeoDataFrame:
    prescription = logical_layer.startswith("prescription")
    return gpd.GeoDataFrame(
        {
            "LIBELLE": [f"Label {identifier}" for identifier in source_ids],
            "TXT": [None] * len(source_ids),
            ("TYPEPSC" if prescription else "TYPEINF"): type_codes,
            ("STYPEPSC" if prescription else "STYPEINF"): subtype_codes,
            "NOMFIC": [None] * len(source_ids),
            "URLFIC": [None] * len(source_ids),
            "IDURBA": ["31395_PLU_20240215"] * len(source_ids),
            "DATVALID": ["20240215"] * len(source_ids),
            ("LIB_IDPSC" if prescription else "LIB_IDINFO"): source_ids,
        },
        geometry=geometries,
        crs="EPSG:2154",
    )


def _integration_layer(
    logical_layer: str,
    frame: gpd.GeoDataFrame,
) -> GpuInspectedLayer:
    source_layer = logical_layer.upper()
    reference = GpuSpatialLayerReference(
        Path(f"{logical_layer}.gpkg"), source_layer, "GPKG"
    )
    geometry = frame.geometry
    non_null = ~geometry.isna()
    non_empty = non_null & ~geometry.is_empty
    summary = GpuLayerSummary(
        source_document_id="doc-1",
        source_archive_sha256="a" * 64,
        source_layer=source_layer,
        crs=frame.crs.to_string(),
        feature_count=len(frame),
        columns=tuple(str(column) for column in frame.columns),
        dtypes=tuple(
            (str(column), str(dtype)) for column, dtype in frame.dtypes.items()
        ),
        null_counts=tuple(
            (str(column), int(frame[column].isna().sum())) for column in frame.columns
        ),
        geometry_types=tuple(
            (str(name), int(count))
            for name, count in geometry.geom_type.value_counts().sort_index().items()
        ),
        null_geometry_count=int((~non_null).sum()),
        empty_geometry_count=int((non_null & geometry.is_empty).sum()),
        invalid_geometry_count=int((non_empty & ~geometry.is_valid).sum()),
    )
    return GpuInspectedLayer(logical_layer, reference, frame, summary)  # type: ignore[arg-type]


def _integration_inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
    layers = (
        _integration_layer(
            "prescription_surface",
            _integration_source_frame(
                "prescription_surface",
                [Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])],
                ["P-1"],
                ["07"],
                ["00"],
            ),
        ),
        _integration_layer(
            "information_surface",
            _integration_source_frame(
                "information_surface",
                [Polygon([(3, 0), (5, 0), (5, 2), (3, 2)])],
                ["I-1"],
                ["02"],
                ["00"],
            ),
        ),
        _integration_layer(
            "prescription_line",
            _integration_source_frame(
                "prescription_line",
                [LineString([(0, 1), (2, 1)])],
                ["P-2"],
                ["07"],
                ["04"],
            ),
        ),
        _integration_layer(
            "information_point",
            _integration_source_frame(
                "information_point",
                [Point(10, 10)],
                ["I-2"],
                ["99"],
                ["00"],
            ),
        ),
    )
    planning_document = _planning_document(related_layers=layers)
    parcels = _integration_parcels()
    normalized = intersect_parcels_with_gpu_planning_features(
        parcels, planning_document
    )
    return (
        planning_document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        _profile(),
    )


def _integration_parcels() -> gpd.GeoDataFrame:
    return gpd.GeoDataFrame(
        {"parcel_id": ["PARCEL-1"], "existing_fact": [7]},
        geometry=[Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])],
        crs="EPSG:2154",
        index=pd.Index([91], name="parcel_row"),
    )


def _inputs() -> tuple[
    GpuPlanningDocument,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    gpd.GeoDataFrame,
    pd.DataFrame,
    CnigFeatureCodeProfile,
]:
    document, _, surface, line, point, relations, profile = _integration_inputs()
    return document, surface, line, point, relations, profile


def resolve_planning_feature_codes(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
) -> PlanningFeatureCodeResult:
    """Exercise the new bound API while keeping legacy unit call sites compact."""

    return _public_resolve_planning_feature_codes(
        planning_document,
        _integration_parcels(),
        surface_features,
        line_features,
        point_features,
        relations,
        code_profile,
    )


def validate_planning_feature_code_result(
    planning_document: GpuPlanningDocument,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    result: PlanningFeatureCodeResult,
) -> None:
    _public_validate_planning_feature_code_result(
        planning_document,
        _integration_parcels(),
        surface_features,
        line_features,
        point_features,
        relations,
        code_profile,
        result,
    )


def test_exact_family_pair_resolution_and_leading_zeros() -> None:
    result = resolve_planning_feature_codes(*_inputs())
    surface = result.surface_features.set_index("planning_feature_id")
    assert (
        surface.loc["GPU:doc-1:prescription_surface:P-1", "official_code_label"]
        == "Prescription seven"
    )
    assert (
        surface.loc["GPU:doc-1:information_surface:I-1", "official_code_label"]
        == "Information two"
    )
    assert (
        result.line_features.iloc[0]["official_code_label"]
        == "Prescription seven subtype four"
    )
    assert result.line_features.iloc[0]["type_code_raw"] == "07"
    assert result.line_features.iloc[0]["subtype_code_raw"] == "04"
    assert set(surface["official_code_status"]) == {"RESOLVED_OFFICIAL"}


def test_no_type_only_or_cross_family_fallback_and_unknown_is_retained() -> None:
    document, surface, line, point, relations, profile = _inputs()
    payload = _profile_payload()
    payload["records"] = [
        record
        for record in payload["records"]
        if not (
            (record["feature_family"], record["type_code"], record["subtype_code"])
            in {("PRESCRIPTION", "07", "04"), ("INFORMATION", "99", "00")}
        )
    ]
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    profile = CnigFeatureCodeProfile.model_validate(payload)
    result = resolve_planning_feature_codes(
        document, surface, line, point, relations, profile
    )
    assert result.line_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"
    assert pd.isna(result.line_features.iloc[0]["official_code_label"])
    assert result.point_features.iloc[0]["official_code_status"] == "UNKNOWN_CODE_PAIR"
    assert len(result.line_features) == 1
    assert len(result.point_features) == 1


def test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated() -> None:
    inputs = list(_inputs())
    inputs[-1] = _mutated_profile(canonical_records_sha256="f" * 64)
    with pytest.raises(PlanningFeatureCodeError, match="profile|canonical"):
        resolve_planning_feature_codes(*inputs)


def test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated() -> None:
    profile = _profile()
    invalid = CnigFeatureCodeProfile.model_construct(
        **{**profile.model_dump(mode="python"), "schema_version": 1}
    )
    inputs = list(_inputs())
    inputs[-1] = invalid
    with pytest.raises(PlanningFeatureCodeError, match="schema|profile"):
        resolve_planning_feature_codes(*inputs)


def test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated() -> None:
    profile = _profile()
    invalid = CnigFeatureCodeProfile.model_construct(
        **{
            **profile.model_dump(mode="python"),
            "records": (*profile.records, profile.records[0]),
        }
    )
    inputs = list(_inputs())
    inputs[-1] = invalid
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|profile"):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("family", "url"),
    [
        ("prescription", "https://www.geoportail-urbanisme.gouv.fr/another/path"),
        ("prescription", f"{P_URL}?format=json"),
        (
            "prescription",
            "https://www.geoportail-urbanisme.gouv.fr:444/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        (
            "prescription",
            "https://user@www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        (
            "prescription",
            "https://geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType",
        ),
        ("prescription", I_URL),
        ("information", P_URL),
        ("information", f"{I_URL}#codes"),
        ("information", f"{I_URL}/"),
        ("information", I_URL.replace("https://", "http://")),
    ],
)
def test_official_family_endpoints_require_exact_identity(
    family: str, url: str
) -> None:
    payload = _profile_payload()
    payload["official_sources"][family] = url
    family_name = family.upper()
    for record in payload["records"]:
        if record["feature_family"] == family_name:
            record["official_source_url"] = url
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    with pytest.raises(ValueError, match="official|source|URL"):
        CnigFeatureCodeProfile.model_validate(payload)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("official_label", "Repeated  whitespace"),
        ("official_label", "Decomposed e\u0301"),
        ("legal_reference", "L151-1\n  L151-2"),
        ("regulation_or_annex_reference", " R151-1"),
    ],
)
def test_official_text_must_already_be_canonical(field: str, value: str) -> None:
    payload = _profile_payload()
    payload["records"][0][field] = value
    payload["canonical_records_sha256"] = _records_hash(payload["records"])
    with pytest.raises(
        ValueError,
        match="GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1|canonical|normalization|exact",
    ):
        CnigFeatureCodeProfile.model_validate(payload)


@pytest.mark.parametrize("code", ["1", "001", "A1", " 01", "01 ", 1])
def test_malformed_code_is_rejected(code: object) -> None:
    payload = _profile_payload()
    payload["records"][0]["type_code"] = code
    with pytest.raises(ValueError):
        CnigFeatureCodeProfile.model_validate(payload)


def test_duplicate_pair_and_profile_hash_mutation_are_rejected() -> None:
    payload = _profile_payload()
    payload["records"].append(dict(payload["records"][0]))
    with pytest.raises(ValueError, match="duplicate"):
        CnigFeatureCodeProfile.model_validate(payload)
    payload = _profile_payload()
    payload["canonical_records_sha256"] = "f" * 64
    with pytest.raises(ValueError, match="canonical"):
        CnigFeatureCodeProfile.model_validate(payload)


def test_wrong_official_host_and_unknown_field_are_rejected() -> None:
    payload = _profile_payload()
    payload["official_sources"]["prescription"] = "https://example.com/codes"
    with pytest.raises(ValueError, match="official|exact"):
        CnigFeatureCodeProfile.model_validate(payload)
    payload = _profile_payload()
    payload["semantic_policy"] = "BLOCK"
    with pytest.raises(ValueError):
        CnigFeatureCodeProfile.model_validate(payload)


def test_duplicate_yaml_key_is_rejected(tmp_path: Path) -> None:
    path = tmp_path / "codes.yaml"
    path.write_text("schema_version: 1\nschema_version: 1\n", encoding="utf-8")
    with pytest.raises(PlanningFeatureCodeError, match="Duplicate YAML"):
        load_cnig_feature_code_profile(path)


def test_wrong_planning_standard_is_rejected() -> None:
    inputs = list(_inputs())
    inputs[0] = _planning_document("CNIG PLU v2022")
    with pytest.raises(PlanningFeatureCodeError, match="standard"):
        resolve_planning_feature_codes(*inputs)


def test_catalogs_and_relations_are_preserved_and_inputs_immutable() -> None:
    inputs = _inputs()
    snapshots = [frame.copy(deep=True) for frame in inputs[1:5]]
    result = resolve_planning_feature_codes(*inputs)
    for original, snapshot, coded in zip(
        inputs[1:4],
        snapshots[:3],
        (result.surface_features, result.line_features, result.point_features),
        strict=True,
    ):
        assert_geodataframe_equal(original, snapshot)
        assert_geodataframe_equal(coded.loc[:, original.columns], original)
        assert (
            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS
        )
    pd.testing.assert_frame_equal(inputs[4], snapshots[3])
    pd.testing.assert_frame_equal(result.relations.loc[:, inputs[4].columns], inputs[4])
    assert tuple(result.code_dictionary.columns) == CODE_DICTIONARY_COLUMNS
    assert result.relations.index.equals(inputs[4].index)


@pytest.mark.parametrize(
    ("catalog_position", "column"),
    [
        (1, "feature_area_m2"),
        (2, "feature_length_m"),
        (3, "point_member_count"),
        (1, "label_raw"),
        (1, "source_crs"),
    ],
)
def test_complete_normalized_catalog_schema_is_required(
    catalog_position: int,
    column: str,
) -> None:
    inputs = list(_inputs())
    inputs[catalog_position] = inputs[catalog_position].drop(columns=column)
    with pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column"):
        resolve_planning_feature_codes(*inputs)


def test_unexpected_factual_catalog_column_is_rejected() -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface["unexpected_fact"] = "not-produced-by-step-7d-3-1"
    inputs[1] = surface
    with pytest.raises(PlanningFeatureCodeError, match="normalized|schema|column"):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("source_identity_kind", "UNKNOWN_KIND"),
        ("source_identity_field", "LIB_IDINFO"),
    ],
)
def test_cnig_identity_provenance_is_exact(column: str, value: str) -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface.loc[surface.index[0], column] = value
    inputs[1] = surface
    with pytest.raises(
        PlanningFeatureCodeError, match="identity|provenance|normalized"
    ):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("logical_layer", "feature_family", "source_feature_id"),
    [
        ("information_surface", "INFORMATION", "OGR_FID:1"),
        ("prescription_surface", "PRESCRIPTION", "1"),
    ],
)
def test_ogr_fid_provenance_is_restricted(
    logical_layer: str,
    feature_family: str,
    source_feature_id: str,
) -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    row_index = surface.index[0]
    surface.loc[row_index, "logical_layer"] = logical_layer
    surface.loc[row_index, "feature_family"] = feature_family
    surface.loc[row_index, "source_identity_kind"] = "ARCHIVE_SCOPED_OGR_FID"
    surface.loc[row_index, "source_identity_field"] = "OGR_FID"
    surface.loc[row_index, "source_feature_id"] = source_feature_id
    inputs[1] = surface
    with pytest.raises(
        PlanningFeatureCodeError, match="OGR|identity|provenance|normalized"
    ):
        resolve_planning_feature_codes(*inputs)


def test_source_feature_id_is_unique_inside_logical_layer() -> None:
    inputs = list(_inputs())
    surface = inputs[1].copy(deep=True)
    surface.loc[surface.index[1], "logical_layer"] = surface.iloc[0]["logical_layer"]
    surface.loc[surface.index[1], "feature_family"] = surface.iloc[0]["feature_family"]
    surface.loc[surface.index[1], "source_identity_field"] = surface.iloc[0][
        "source_identity_field"
    ]
    surface.loc[surface.index[1], "source_feature_id"] = surface.iloc[0][
        "source_feature_id"
    ]
    inputs[1] = surface
    with pytest.raises(PlanningFeatureCodeError, match="source_feature_id|unique"):
        resolve_planning_feature_codes(*inputs)


def test_catalog_crs_must_be_canonical_epsg_2154() -> None:
    inputs = list(_inputs())
    inputs[1] = inputs[1].to_crs("EPSG:4326")
    with pytest.raises(PlanningFeatureCodeError, match="EPSG:2154|CRS"):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("catalog_position", "column", "value"),
    [
        (1, "feature_area_m2", 99.0),
        (2, "feature_length_m", 99.0),
        (3, "point_member_count", 2),
    ],
)
def test_catalog_geometry_metrics_are_revalidated(
    catalog_position: int,
    column: str,
    value: object,
) -> None:
    inputs = list(_inputs())
    catalog = inputs[catalog_position].copy(deep=True)
    catalog.loc[catalog.index[0], column] = value
    inputs[catalog_position] = catalog
    with pytest.raises(PlanningFeatureCodeError, match="metric|area|length|member"):
        resolve_planning_feature_codes(*inputs)


def test_complete_relation_schema_is_required() -> None:
    inputs = list(_inputs())
    inputs[4] = inputs[4].drop(columns="intersection_length_m")
    with pytest.raises(PlanningFeatureCodeError, match="relation|schema|column"):
        resolve_planning_feature_codes(*inputs)


def test_unexpected_factual_relation_column_is_rejected() -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations["unexpected_metric"] = 0.0
    inputs[4] = relations
    with pytest.raises(PlanningFeatureCodeError, match="relation|schema"):
        resolve_planning_feature_codes(*inputs)


def test_cnig_resolver_invokes_shared_factual_contract(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    calls = 0

    def reject_shared_contract(*args: object) -> None:
        nonlocal calls
        calls += 1
        raise ValueError("shared factual contract marker")

    monkeypatch.setattr(
        coding_module,
        "validate_normalized_planning_feature_inputs",
        reject_shared_contract,
    )
    with pytest.raises(
        PlanningFeatureCodeError, match="shared factual contract marker"
    ):
        resolve_planning_feature_codes(*_inputs())
    assert calls == 1


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("label_raw", "mutated label"),
        ("source_validity_date_raw", "19990101"),
        ("regulation_filename_raw", "other.pdf"),
        ("feature_area_m2", 3.0),
    ],
)
def test_complete_relation_catalog_agreement_is_required(
    column: str,
    value: object,
) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations.loc[relations.index[0], column] = value
    inputs[4] = relations
    with pytest.raises(
        PlanningFeatureCodeError, match="catalog|metric|normalized|feature share"
    ):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("intersection_area_m2", 0.0),
        ("intersection_area_m2", -1.0),
        ("intersection_area_m2", float("inf")),
        ("parcel_share_pct", 99.0),
    ],
)
def test_surface_relation_metrics_are_revalidated(column: str, value: object) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    relations.loc[relations.index[0], column] = value
    inputs[4] = relations
    with pytest.raises(
        PlanningFeatureCodeError, match="relation|metric|finite|percentage"
    ):
        resolve_planning_feature_codes(*inputs)


@pytest.mark.parametrize(
    ("column", "value"),
    [
        ("intersection_length_m", 0.0),
        ("relation_type", "TOUCH_ONLY"),
        ("source_line_length_m", 1.0),
    ],
)
def test_line_relation_metrics_are_revalidated(column: str, value: object) -> None:
    inputs = list(_inputs())
    relations = inputs[4].copy(deep=True)
    line_index = relations.index[relations["geometry_kind"].eq("LINE")][0]
    relations.loc[line_index, column] = value
    inputs[4] = relations
    with pytest.raises(PlanningFeatureCodeError, match="relation|length|catalog"):
        resolve_planning_feature_codes(*inputs)


def test_duplicate_catalog_columns_are_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    duplicate = pd.concat([surface, surface[["planning_feature_id"]]], axis=1)
    duplicate = gpd.GeoDataFrame(duplicate, geometry="geometry", crs=surface.crs)
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|columns"):
        resolve_planning_feature_codes(
            document, duplicate, line, point, relations, profile
        )


def test_missing_catalog_crs_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.set_crs(None, allow_override=True)
    with pytest.raises(PlanningFeatureCodeError, match="CRS"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_unparseable_catalog_crs_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.geometry.array._crs = "definitely-not-a-crs"  # type: ignore[attr-defined]
    with pytest.raises(PlanningFeatureCodeError, match="CRS"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_inactive_or_wrong_geometry_column_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface["alternate_geometry"] = surface.geometry.copy()
    surface = surface.set_geometry("alternate_geometry")
    with pytest.raises(PlanningFeatureCodeError, match="geometry"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    ("geometry", "message"),
    [
        (None, "null|geometry"),
        (Polygon(), "empty|geometry"),
        (Polygon([(0, 0), (2, 2), (2, 0), (0, 2), (0, 0)]), "invalid|geometry"),
        (LineString([(0, 0), (1, 1)]), "type|geometry|SURFACE"),
    ],
)
def test_surface_geometry_contract_is_enforced(
    geometry: object,
    message: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.at[surface.index[0], "geometry"] = geometry
    with pytest.raises(PlanningFeatureCodeError, match=message):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        ("surface", MultiPolygon([Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])])),
        ("line", MultiLineString([[(0, 0), (2, 0)]])),
        ("point", MultiPoint([(0, 0), (1, 1)])),
    ],
)
def test_valid_multi_geometries_are_accepted(
    catalog_name: str, geometry: object
) -> None:
    document, parcels, _, _, _, _, profile = _integration_inputs()
    target_logical = {
        "surface": "prescription_surface",
        "line": "prescription_line",
        "point": "information_point",
    }[catalog_name]
    changed_layers: list[GpuInspectedLayer] = []
    for layer in document.related_layers:
        if layer.logical_name != target_logical:
            changed_layers.append(layer)
            continue
        source = layer.data.copy(deep=True)
        source.at[source.index[0], "geometry"] = geometry
        changed_layers.append(_integration_layer(target_logical, source))
    changed_document = _planning_document(related_layers=tuple(changed_layers))
    normalized = intersect_parcels_with_gpu_planning_features(parcels, changed_document)
    result = _public_resolve_planning_feature_codes(
        changed_document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        profile,
    )
    assert getattr(result, f"{catalog_name}_features").geometry.iloc[0].equals(geometry)


@pytest.mark.parametrize(
    ("column", "value", "message"),
    [
        ("geometry_kind", "LINE", "geometry kind|SURFACE"),
        ("logical_layer", "prescription_line", "logical layer|surface"),
        ("feature_family", "INFORMATION", "family|logical layer"),
        ("source_identity_kind", None, "source identity|exact string"),
        ("source_layer", " SOURCE ", "source layer|exact string"),
    ],
)
def test_catalog_semantic_and_string_contracts_are_enforced(
    column: str,
    value: object,
    message: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    surface.loc[surface.index[0], column] = value
    with pytest.raises(PlanningFeatureCodeError, match=message):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    "column",
    [
        "planning_feature_id",
        "source_feature_id",
        "source_identity_kind",
        "source_identity_field",
        "logical_layer",
        "feature_family",
        "geometry_kind",
        "source_layer",
    ],
)
def test_every_required_catalog_identity_is_an_exact_non_null_string(
    column: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    surface = surface.copy(deep=True)
    relations = relations.copy(deep=True)
    feature_id = surface.iloc[0]["planning_feature_id"]
    surface.loc[surface.index[0], column] = " invalid "
    if column in relations.columns:
        relations.loc[relations["planning_feature_id"].eq(feature_id), column] = (
            " invalid "
        )
    with pytest.raises(PlanningFeatureCodeError, match="exact string|non-empty"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    ("catalog_name", "geometry"),
    [
        ("line", Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])),
        ("point", LineString([(0, 0), (1, 1)])),
    ],
)
def test_line_and_point_geometry_types_are_enforced(
    catalog_name: str,
    geometry: object,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    catalogs = {"line": line.copy(deep=True), "point": point.copy(deep=True)}
    catalog = catalogs[catalog_name]
    catalog.at[catalog.index[0], "geometry"] = geometry
    catalogs[catalog_name] = catalog
    with pytest.raises(PlanningFeatureCodeError, match="geometry|type"):
        resolve_planning_feature_codes(
            document,
            surface,
            catalogs["line"],
            catalogs["point"],
            relations,
            profile,
        )


def test_planning_feature_ids_are_globally_unique_across_catalogs() -> None:
    document, surface, line, point, relations, profile = _inputs()
    line = line.copy(deep=True)
    line.loc[line.index[0], "planning_feature_id"] = surface.iloc[0][
        "planning_feature_id"
    ]
    with pytest.raises(PlanningFeatureCodeError, match="unique|catalog|deterministic"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_valid_empty_optional_catalogs_preserve_schema_and_crs() -> None:
    document, parcels, _, _, _, _, profile = _integration_inputs()
    surface_layers = tuple(
        layer
        for layer in document.related_layers
        if layer.logical_name in {"prescription_surface", "information_surface"}
    )
    document = _planning_document(related_layers=surface_layers)
    normalized = intersect_parcels_with_gpu_planning_features(parcels, document)
    result = _public_resolve_planning_feature_codes(
        document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        profile,
    )
    for original, coded in (
        (normalized.line_features, result.line_features),
        (normalized.point_features, result.point_features),
    ):
        assert coded.empty
        assert coded.crs == original.crs
        assert tuple(coded.columns[: len(original.columns)]) == tuple(original.columns)
        assert (
            tuple(coded.columns[-len(OFFICIAL_CODE_COLUMNS) :]) == OFFICIAL_CODE_COLUMNS
        )


def test_relation_catalog_code_mismatch_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relation_index = relations.index[0]
    original = relations.loc[relation_index, "subtype_code_raw"]
    relations.loc[relation_index, "subtype_code_raw"] = (
        "04" if original != "04" else "00"
    )
    with pytest.raises(PlanningFeatureCodeError, match="catalog"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_duplicate_relation_columns_are_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    duplicate = pd.concat([relations, relations[["parcel_id"]]], axis=1)
    with pytest.raises(PlanningFeatureCodeError, match="duplicate|columns"):
        resolve_planning_feature_codes(
            document, surface, line, point, duplicate, profile
        )


@pytest.mark.parametrize("column", ["parcel_id", "planning_feature_id"])
@pytest.mark.parametrize("value", [None, " invalid "])
def test_relation_identity_must_be_an_exact_non_null_string(
    column: str,
    value: object,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relations.loc[relations.index[0], column] = value
    with pytest.raises(PlanningFeatureCodeError, match="relation|exact string"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_duplicate_parcel_feature_relation_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = pd.concat([relations, relations.iloc[[0]]], ignore_index=True)
    relations = _canonical_relation_schema(relations)
    with pytest.raises(PlanningFeatureCodeError, match="unique|duplicate"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


def test_unknown_relation_feature_id_is_rejected() -> None:
    document, surface, line, point, relations, profile = _inputs()
    relations = relations.copy(deep=True)
    relations.loc[relations.index[0], "planning_feature_id"] = "UNKNOWN"
    with pytest.raises(PlanningFeatureCodeError, match="unknown"):
        resolve_planning_feature_codes(
            document, surface, line, point, relations, profile
        )


@pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "LENGTH_OVERLAP"),
        ("SURFACE", "NOT_A_RELATION"),
        ("LINE", "INSIDE"),
        ("POINT", "AREA_OVERLAP"),
    ],
)
def test_relation_type_must_match_catalog_geometry_kind(
    geometry_kind: str,
    relation_type: str,
) -> None:
    document, surface, line, point, relations, profile = _inputs()
    catalogs = {"SURFACE": surface, "LINE": line, "POINT": point}
    feature = catalogs[geometry_kind].iloc[0]
    row = relations.iloc[0].copy()
    for column in (
        "planning_feature_id",
        "source_feature_id",
        "source_identity_kind",
        "source_identity_field",
        "logical_layer",
        "feature_family",
        "geometry_kind",
        "type_code_raw",
        "subtype_code_raw",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
        "label_raw",
        "text_raw",
        "source_validity_date_raw",
        "regulation_filename_raw",
    ):
        row[column] = feature[column]
    row["relation_type"] = relation_type
    metric_columns = (
        "feature_area_m2",
        "source_line_length_m",
        "intersection_area_m2",
        "intersection_length_m",
        "parcel_share_pct",
        "feature_share_pct",
        "point_member_count",
        "point_members_inside_count",
        "point_members_boundary_count",
    )
    for column in metric_columns:
        row[column] = None
    if geometry_kind == "SURFACE":
        area = 4.0 if relation_type == "AREA_OVERLAP" else 0.0
        row["feature_area_m2"] = 4.0
        row["intersection_area_m2"] = area
        row["parcel_share_pct"] = 100.0 if area else 0.0
        row["feature_share_pct"] = 100.0 if area else 0.0
    elif geometry_kind == "LINE":
        row["source_line_length_m"] = 2.0
        row["intersection_length_m"] = 2.0 if relation_type == "LENGTH_OVERLAP" else 0.0
    else:
        row["point_member_count"] = 1
        row["point_members_inside_count"] = 1 if relation_type == "INSIDE" else 0
        row["point_members_boundary_count"] = (
            1 if relation_type == "BOUNDARY_TOUCH" else 0
        )
    candidate = pd.DataFrame([row], columns=relations.columns)
    candidate = _canonical_relation_schema(candidate)
    with pytest.raises(PlanningFeatureCodeError, match="[Rr]elation type|geometry"):
        resolve_planning_feature_codes(
            document, surface, line, point, candidate, profile
        )


@pytest.mark.parametrize(
    ("geometry_kind", "relation_type"),
    [
        ("SURFACE", "AREA_OVERLAP"),
        ("SURFACE", "TOUCH_ONLY"),
        ("LINE", "LENGTH_OVERLAP"),
        ("LINE", "TOUCH_ONLY"),
        ("POINT", "INSIDE"),
        ("POINT", "BOUNDARY_TOUCH"),
    ],
)
def test_valid_relation_types_are_retained(
    geometry_kind: str,
    relation_type: str,
) -> None:
    geometry: object
    if geometry_kind == "SURFACE":
        logical = "prescription_surface"
        geometry = (
            Polygon([(0, 0), (2, 0), (2, 2), (0, 2)])
            if relation_type == "AREA_OVERLAP"
            else Polygon([(2, 0), (4, 0), (4, 2), (2, 2)])
        )
    elif geometry_kind == "LINE":
        logical = "prescription_line"
        geometry = (
            LineString([(0, 1), (2, 1)])
            if relation_type == "LENGTH_OVERLAP"
            else LineString([(-1, 0), (0, 0)])
        )
    else:
        logical = "information_point"
        geometry = Point(1, 1) if relation_type == "INSIDE" else Point(0, 1)
    source = _integration_source_frame(
        logical,
        [geometry],
        ["FEATURE-1"],
        ["07" if logical.startswith("prescription") else "99"],
        ["00"],
    )
    document = _planning_document(related_layers=(_integration_layer(logical, source),))
    parcels = _integration_parcels()
    normalized = intersect_parcels_with_gpu_planning_features(parcels, document)
    result = _public_resolve_planning_feature_codes(
        document,
        parcels,
        normalized.surface_features,
        normalized.line_features,
        normalized.point_features,
        normalized.relations,
        _profile(),
    )
    assert result.relations["relation_type"].tolist() == [relation_type]


def test_coordinated_output_hash_mutation_is_rejected() -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_label"] = "Mutated"
    mutated = _result_with_hashes(replace(result, surface_features=surface))
    with pytest.raises(PlanningFeatureCodeError, match="rebuilt|meaning|dictionary"):
        validate_planning_feature_code_result(*inputs, mutated)


def test_parquet_readback_passes_source_complete_validation(tmp_path: Path) -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    paths = {
        name: tmp_path / f"{name}.parquet"
        for name in (
            "code_dictionary",
            "surface_features",
            "line_features",
            "point_features",
            "relations",
        )
    }
    for name, path in paths.items():
        getattr(result, name).to_parquet(path, index=True)
    persisted = replace(
        result,
        code_dictionary=pd.read_parquet(paths["code_dictionary"]),
        surface_features=gpd.read_parquet(paths["surface_features"]),
        line_features=gpd.read_parquet(paths["line_features"]),
        point_features=gpd.read_parquet(paths["point_features"]),
        relations=pd.read_parquet(paths["relations"]),
    )
    validate_planning_feature_code_result(*inputs, persisted)


def test_record_order_must_be_deterministic() -> None:
    payload = _profile_payload()
    payload["records"] = list(reversed(payload["records"]))
    with pytest.raises(ValueError, match="deterministic order"):
        CnigFeatureCodeProfile.model_validate(payload)


def test_yaml_snapshot_loads_strictly(tmp_path: Path) -> None:
    payload = _profile_payload()
    path = tmp_path / "profile.yaml"
    path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
    assert load_cnig_feature_code_profile(path) == _profile()


def test_stable_public_api_is_exported_from_module_and_stage_package() -> None:
    from landscout import stages

    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )

    required = {
        "CnigFeatureCodeProfile",
        "PlanningFeatureCodeError",
        "PlanningFeatureCodeResult",
        "load_cnig_feature_code_profile",
        "resolve_planning_feature_codes",
        "validate_planning_feature_code_result",
        "validate_planning_feature_code_result_envelope",
    }
    low_level = {
        "_canonical_json_sha256",
        "_coded_catalog",
        "_lookup",
        "_profile_sha256",
        "_result_with_hashes",
    }
    assert required.issubset(set(coding_module.__all__))
    assert required.issubset(set(stages.__all__))
    for name in required:
        assert getattr(stages, name) is getattr(coding_module, name)
    assert low_level.isdisjoint(coding_module.__all__)
    assert low_level.isdisjoint(stages.__all__)


def test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs() -> None:
    path = Path("configs/planning/cnig_plu_2017_feature_codes.yaml")
    profile = load_cnig_feature_code_profile(path)
    expected_records = (
        (
            "INFORMATION",
            "02",
            "00",
            "Zone d'aménagement concerté",
            "L311-1 code de l’urbanisme",
            "R151-52 8°",
            I_URL,
        ),
        (
            "INFORMATION",
            "14",
            "00",
            "Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)",
            "L571-10 code de l’environnement",
            "R151-53 5°",
            I_URL,
        ),
        (
            "INFORMATION",
            "27",
            "00",
            "Plan d'exposition au bruit des aérodromes",
            "L112-6 code de l’urbanisme",
            "R151-52 2°",
            I_URL,
        ),
        (
            "INFORMATION",
            "99",
            "00",
            "Autre périmètre, secteur, plan, document, site, projet, espace.",
            None,
            None,
            I_URL,
        ),
        (
            "PRESCRIPTION",
            "01",
            "00",
            "Espace boisé classé",
            "L113-1",
            "R151-31 1°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "05",
            "00",
            "Emplacement réservé",
            "L151-41 1° à 3°",
            "R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "07",
            "00",
            "Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique",
            "L151-19 et L151-23",
            "R151-41 3° Et R151-43",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "07",
            "04",
            "Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique",
            "L151-23",
            "R151-43 5°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "15",
            "00",
            "Règles d’implantation des constructions",
            "L151-17 et L151-18",
            "R151-39 dernier al.",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "15",
            "01",
            "Implantation des constructions par rapport aux voies et aux emprises publiques",
            "L151-17 et L151-18",
            "R151-39",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "17",
            "00",
            "Secteur à programme de logements mixité sociale en zone U et AU",
            "L151-15",
            "R151-38 3°",
            P_URL,
        ),
        (
            "PRESCRIPTION",
            "18",
            "00",
            "Périmètre comportant des orientations d’aménagement et de programmation (OAP)",
            "L151-6 et L151-7",
            "R151-6 à R151-8-1",
            P_URL,
        ),
    )
    actual_records = tuple(
        (
            record.feature_family,
            record.type_code,
            record.subtype_code,
            record.official_label,
            record.legal_reference,
            record.regulation_or_annex_reference,
            record.official_source_url,
        )
        for record in profile.records
    )
    assert profile.schema_version == 2
    assert profile.profile == "cnig_plu_2017_muret_observed_pairs_v2"
    assert profile.standard_model == "CNIG PLU v2017"
    assert profile.official_text_normalization == TEXT_NORMALIZATION
    assert profile.retrieval_date.isoformat() == "2026-08-12"
    assert profile.official_sources.prescription == P_URL
    assert profile.official_sources.information == I_URL
    assert (
        profile.canonical_records_sha256
        == "5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c"
    )
    assert (
        _payload_hash(profile.model_dump(mode="json"))
        == "5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"
    )
    assert actual_records == expected_records


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("result_hash_schema_version", True),
        ("result_hash_schema_version", 0),
        ("result_hash_schema_version", 1),
        ("result_hash_schema_version", 2),
        ("result_hash_schema_version", 3),
        ("result_hash_schema_version", 4),
        ("result_hash_schema_version", 6),
        ("result_hash_schema_version", 5.0),
        ("result_hash_schema_version", "5"),
        ("profile_schema_version", True),
        ("profile_schema_version", 0),
        ("profile_schema_version", 1),
        ("profile_schema_version", 3),
        ("profile_schema_version", 2.0),
        ("profile_schema_version", "2"),
    ],
)
def test_result_schema_versions_are_strict(field: str, value: object) -> None:
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    with pytest.raises(PlanningFeatureCodeError, match="schema version"):
        validate_planning_feature_code_result(
            *inputs, replace(result, **{field: value})
        )


def test_step_7d_3_1_output_integrates_with_public_coding_api() -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    assert result.result_hash_schema_version == 5
    assert result.profile_schema_version == 2
    assert len(result.surface_features) == 2
    assert len(result.line_features) == 1
    assert len(result.point_features) == 1
    assert len(result.relations) == 2
    assert set(result.surface_features["official_code_status"]) == {"RESOLVED_OFFICIAL"}
    _public_validate_planning_feature_code_result(*inputs, result)


def test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inputs = _integration_inputs()
    coding_module = importlib.import_module(
        "landscout.stages.resolve_planning_feature_codes"
    )
    enrich_module = importlib.import_module("landscout.stages.enrich_planning_features")
    actual_physical = enrich_module.revalidate_gpu_spatial_layer_sources
    actual_relations = enrich_module._build_relation_tables
    calls = {"physical": 0, "relations": 0}

    def counted_physical(*args: object, **kwargs: object) -> object:
        calls["physical"] += 1
        return actual_physical(*args, **kwargs)

    def counted_relations(*args: object, **kwargs: object) -> object:
        calls["relations"] += 1
        return actual_relations(*args, **kwargs)

    monkeypatch.setattr(
        enrich_module, "revalidate_gpu_spatial_layer_sources", counted_physical
    )
    monkeypatch.setattr(enrich_module, "_build_relation_tables", counted_relations)

    result = coding_module.resolve_planning_feature_codes(*inputs)
    assert calls == {"physical": 1, "relations": 1}

    coding_module.validate_planning_feature_code_result(*inputs, result)
    assert calls == {"physical": 2, "relations": 2}


def test_coded_result_persists_all_source_input_hashes() -> None:
    result = _public_resolve_planning_feature_codes(*_integration_inputs())
    for hash_field in (
        "planning_document_context_sha256",
        "parcel_identity_input_sha256",
        "normalized_catalogs_input_sha256",
        "normalized_relations_input_sha256",
        "gpu_related_source_files_sha256",
        "expected_relations_content_sha256",
    ):
        value = getattr(result, hash_field)
        assert isinstance(value, str)
        assert len(value) == 64
        int(value, 16)


@pytest.mark.parametrize(
    "field",
    [
        "planning_document_context_sha256",
        "parcel_identity_input_sha256",
        "normalized_catalogs_input_sha256",
        "normalized_relations_input_sha256",
        "gpu_related_source_files_sha256",
        "expected_relations_content_sha256",
    ],
)
def test_source_input_hash_mutation_is_rejected(field: str) -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    with pytest.raises(PlanningFeatureCodeError, match="hash|rebuilt|source"):
        _public_validate_planning_feature_code_result(
            *inputs, replace(result, **{field: "f" * 64})
        )


def test_gpu_related_source_hash_is_deterministic_across_cache_roots(
    tmp_path: Path,
) -> None:
    first_inputs = _integration_inputs()
    first_document = first_inputs[0]
    source_root = first_document.extraction.extraction_root
    relocated_root = tmp_path / "relocated-extraction"
    shutil.copytree(source_root, relocated_root)

    def relocated_reference(
        reference: GpuSpatialLayerReference,
    ) -> GpuSpatialLayerReference:
        relative = reference.dataset_path.relative_to(source_root)
        return replace(reference, dataset_path=relocated_root / relative)

    reference_map = {
        reference: relocated_reference(reference)
        for reference in first_document.all_spatial_layers
    }
    relocated_document = replace(
        first_document,
        extraction=replace(
            first_document.extraction,
            extraction_root=relocated_root,
        ),
        all_spatial_layers=tuple(
            reference_map[reference] for reference in first_document.all_spatial_layers
        ),
        zoning=replace(
            first_document.zoning,
            reference=reference_map[first_document.zoning.reference],
        ),
        related_layers=tuple(
            replace(layer, reference=reference_map[layer.reference])
            for layer in first_document.related_layers
        ),
    )
    second_inputs = (relocated_document, *first_inputs[1:])
    first = _public_resolve_planning_feature_codes(*first_inputs)
    second = _public_resolve_planning_feature_codes(*second_inputs)
    assert (
        first.gpu_related_source_files_sha256 == second.gpu_related_source_files_sha256
    )


@pytest.mark.parametrize(
    "field",
    ["gpu_related_source_files_sha256", "expected_relations_content_sha256"],
)
def test_source_binding_hashes_bind_every_component_hash(field: str) -> None:
    result = _public_resolve_planning_feature_codes(*_integration_inputs())
    changed = _result_with_hashes(replace(result, **{field: "f" * 64}))
    for hash_field in (
        "code_dictionary_content_sha256",
        "surface_features_content_sha256",
        "line_features_content_sha256",
        "point_features_content_sha256",
        "relations_content_sha256",
        "complete_result_content_sha256",
    ):
        assert getattr(changed, hash_field) != getattr(result, hash_field)


def test_parcel_source_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    parcels = inputs[1].copy(deep=True)
    parcels.loc[parcels.index[0], "parcel_id"] = "CHANGED-PARCEL"
    inputs[1] = parcels
    with pytest.raises(PlanningFeatureCodeError, match="parcel|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)


def test_gpu_document_context_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    planning_document = inputs[0]
    archive = planning_document.extraction.archive
    changed_document = replace(archive.document, provider="Changed provider")
    inputs[0] = replace(
        planning_document,
        extraction=replace(
            planning_document.extraction,
            archive=replace(archive, document=changed_document),
        ),
    )
    with pytest.raises(PlanningFeatureCodeError, match="document|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)


def test_normalized_catalog_change_invalidates_coded_result_even_when_coherent() -> (
    None
):
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    surface = inputs[2].copy(deep=True)
    relations = inputs[5].copy(deep=True)
    feature_id = surface.iloc[0]["planning_feature_id"]
    surface.loc[surface.index[0], "label_raw"] = "Coherently changed"
    relations.loc[relations["planning_feature_id"].eq(feature_id), "label_raw"] = (
        "Coherently changed"
    )
    inputs[2] = surface
    inputs[5] = relations
    with pytest.raises(PlanningFeatureCodeError, match="normalized|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)


def test_normalized_relation_change_invalidates_coded_result() -> None:
    inputs = list(_integration_inputs())
    result = _public_resolve_planning_feature_codes(*inputs)
    relations = inputs[5].copy(deep=True)
    line_mask = relations["geometry_kind"].eq("LINE")
    relations.loc[line_mask, "parcel_metric_area_m2"] = 8.0
    inputs[5] = relations
    with pytest.raises(PlanningFeatureCodeError, match="[Rr]elation|source|rebuilt"):
        _public_validate_planning_feature_code_result(*inputs, result)


@pytest.mark.parametrize("mutation", ["missing", "extra", "reordered", "metric"])
def test_coding_api_rejects_relation_set_not_rebuilt_from_geometry(
    mutation: str,
) -> None:
    inputs = list(_integration_inputs())
    relations = inputs[5].copy(deep=True)
    if mutation == "missing":
        relations = relations.iloc[1:].copy()
    elif mutation == "extra":
        extra = relations.iloc[[0]].copy(deep=True)
        extra.loc[extra.index[0], "parcel_id"] = "PARCEL-OTHER"
        relations = pd.concat([relations, extra], ignore_index=True)
    elif mutation == "reordered":
        relations = relations.iloc[::-1].reset_index(drop=True)
    else:
        line_mask = relations["geometry_kind"].eq("LINE")
        relations.loc[line_mask, "intersection_length_m"] = 1.0
    inputs[5] = relations
    with pytest.raises(
        PlanningFeatureCodeError,
        match="relation|parcel|source|rebuilt|normalized",
    ):
        _public_resolve_planning_feature_codes(*inputs)


def test_schema_v5_parquet_readback_preserves_source_hash_envelope(
    tmp_path: Path,
) -> None:
    inputs = _integration_inputs()
    result = _public_resolve_planning_feature_codes(*inputs)
    paths = {
        name: tmp_path / f"integrated-{name}.parquet"
        for name in (
            "code_dictionary",
            "surface_features",
            "line_features",
            "point_features",
            "relations",
        )
    }
    for name, path in paths.items():
        getattr(result, name).to_parquet(path, index=True)
    persisted = replace(
        result,
        code_dictionary=pd.read_parquet(paths["code_dictionary"]),
        surface_features=gpd.read_parquet(paths["surface_features"]),
        line_features=gpd.read_parquet(paths["line_features"]),
        point_features=gpd.read_parquet(paths["point_features"]),
        relations=pd.read_parquet(paths["relations"]),
    )
    _public_validate_planning_feature_code_result(*inputs, persisted)


def test_schema_v5_public_api_signatures_remain_source_complete() -> None:
    assert tuple(
        inspect.signature(_public_resolve_planning_feature_codes).parameters
    ) == (
        "planning_document",
        "parcels",
        "surface_features",
        "line_features",
        "point_features",
        "relations",
        "code_profile",
    )
    assert tuple(
        inspect.signature(_public_validate_planning_feature_code_result).parameters
    ) == (
        "planning_document",
        "parcels",
        "surface_features",
        "line_features",
        "point_features",
        "relations",
        "code_profile",
        "result",
    )


def test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    assert hasattr(module, "validate_planning_feature_code_result_envelope")
    inputs = _inputs()
    result = resolve_planning_feature_codes(*inputs)
    module.validate_planning_feature_code_result_envelope(result)
    with pytest.raises(PlanningFeatureCodeError, match="hash|invalid"):
        module.validate_planning_feature_code_result_envelope(
            replace(result, complete_result_content_sha256="0" * 64)
        )


def _schema_v5_envelope_result() -> PlanningFeatureCodeResult:
    return resolve_planning_feature_codes(*_inputs())


def _canonical_empty_coded_result(
    result: PlanningFeatureCodeResult,
    *,
    empty_dictionary: bool,
) -> PlanningFeatureCodeResult:
    catalogs: dict[str, gpd.GeoDataFrame] = {}
    for field, kind in (
        ("surface_features", "SURFACE"),
        ("line_features", "LINE"),
        ("point_features", "POINT"),
    ):
        output = getattr(result, field).iloc[0:0].copy(deep=True)
        for column, dtype in zip(output.columns, feature_dtypes(kind), strict=True):
            if dtype != "geometry":
                output[column] = pd.Series(index=output.index, dtype=dtype)
        output.index = pd.Index([], dtype="int64")
        catalogs[field] = output
    relations = result.relations.iloc[0:0].copy(deep=True)
    for column, dtype in zip(relations.columns, relation_dtypes(), strict=True):
        relations[column] = pd.Series(index=relations.index, dtype=dtype)
    relations.index = pd.Index([], dtype="int64")
    dictionary = result.code_dictionary.copy(deep=True)
    if empty_dictionary:
        dictionary = dictionary.iloc[0:0].copy(deep=True)
        dictionary.index = pd.Index([], dtype="int64")
    return _result_with_hashes(
        replace(
            result,
            code_dictionary=dictionary,
            relations=relations,
            **catalogs,
        )
    )


def test_schema_v5_envelope_rejects_canonical_empty_code_dictionary() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _canonical_empty_coded_result(
        _schema_v5_envelope_result(), empty_dictionary=True
    )
    with pytest.raises(PlanningFeatureCodeError, match="dictionary|empty|record"):
        module.validate_planning_feature_code_result_envelope(result)


def test_schema_v5_envelope_accepts_nonempty_dictionary_with_empty_outputs() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _canonical_empty_coded_result(
        _schema_v5_envelope_result(), empty_dictionary=False
    )
    assert len(result.code_dictionary) >= 1
    assert (
        sum(
            len(frame)
            for frame in (
                result.surface_features,
                result.line_features,
                result.point_features,
                result.relations,
            )
        )
        == 0
    )
    module.validate_planning_feature_code_result_envelope(result)


@pytest.mark.parametrize("dictionary", [None, "not-a-frame"])
def test_schema_v5_envelope_controls_malformed_dictionary_type(
    dictionary: object,
) -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    with pytest.raises(PlanningFeatureCodeError):
        module.validate_planning_feature_code_result_envelope(
            replace(result, code_dictionary=dictionary)
        )


def test_schema_v5_envelope_rejects_geospatial_code_dictionary() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    dictionary = gpd.GeoDataFrame(result.code_dictionary.copy(deep=True))
    with pytest.raises(PlanningFeatureCodeError, match="dictionary|DataFrame"):
        module.validate_planning_feature_code_result_envelope(
            replace(result, code_dictionary=dictionary)
        )


@pytest.mark.parametrize(
    "mutation", ["dtype", "range-index", "index-name", "index-dtype"]
)
def test_schema_v5_dictionary_schema_is_explicit(mutation: str) -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    dictionary = result.code_dictionary.copy(deep=True)
    if mutation == "dtype":
        dictionary["official_label"] = dictionary["official_label"].astype("category")
    elif mutation == "range-index":
        dictionary.index = pd.RangeIndex(len(dictionary))
    elif mutation == "index-name":
        dictionary.index = dictionary.index.rename("changed")
    else:
        dictionary.index = pd.Index(dictionary.index.to_numpy(), dtype="uint64")
    changed = _result_with_hashes(replace(result, code_dictionary=dictionary))
    with pytest.raises(PlanningFeatureCodeError, match="dictionary|schema|dtype|index"):
        module.validate_planning_feature_code_result_envelope(changed)


@pytest.mark.parametrize(
    "mutation",
    [
        "duplicate-pair",
        "unsorted-pairs",
        "malformed-type",
        "malformed-subtype",
        "wrong-family",
        "wrong-url",
        "wrong-profile",
        "wrong-profile-sha",
        "literal-null-reference",
    ],
)
def test_schema_v5_dictionary_rows_are_intrinsically_validated(mutation: str) -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    dictionary = result.code_dictionary.copy(deep=True)
    if mutation == "duplicate-pair":
        dictionary.loc[
            dictionary.index[1], ["feature_family", "type_code", "subtype_code"]
        ] = dictionary.loc[
            dictionary.index[0], ["feature_family", "type_code", "subtype_code"]
        ].tolist()
    elif mutation == "unsorted-pairs":
        dictionary = dictionary.iloc[::-1].copy(deep=True)
    elif mutation == "malformed-type":
        dictionary.loc[dictionary.index[0], "type_code"] = "1"
    elif mutation == "malformed-subtype":
        dictionary.loc[dictionary.index[0], "subtype_code"] = "000"
    elif mutation == "wrong-family":
        dictionary.loc[dictionary.index[0], "feature_family"] = "ZONING"
    elif mutation == "wrong-url":
        dictionary.loc[dictionary.index[0], "official_source_url"] = (
            "https://example.com/codes"
        )
    elif mutation == "wrong-profile":
        dictionary.loc[dictionary.index[0], "profile"] = "other-profile"
    elif mutation == "wrong-profile-sha":
        dictionary.loc[dictionary.index[0], "profile_sha256"] = "a" * 64
    else:
        dictionary.loc[dictionary.index[0], "legal_reference"] = "None"
    changed = _result_with_hashes(replace(result, code_dictionary=dictionary))
    with pytest.raises(
        PlanningFeatureCodeError, match="dictionary|pair|code|family|URL|profile|order"
    ):
        module.validate_planning_feature_code_result_envelope(changed)


def test_schema_v5_scalar_lineage_contracts_are_intrinsic() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    changed_standard = _result_with_hashes(
        replace(result, standard_model="CNIG PLU v2099")
    )
    malformed_sha = _result_with_hashes(
        replace(result, planning_document_context_sha256="not-a-sha")
    )
    for changed in (changed_standard, malformed_sha):
        with pytest.raises(PlanningFeatureCodeError, match="standard|SHA|sha|lineage"):
            module.validate_planning_feature_code_result_envelope(changed)


def test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic() -> None:
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()
    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_label"] = pd.NA
    missing_meaning = _result_with_hashes(replace(result, surface_features=surface))

    surface = result.surface_features.copy(deep=True)
    surface.loc[surface.index[0], "official_code_status"] = "UNKNOWN_CODE_PAIR"
    invented_unknown = _result_with_hashes(replace(result, surface_features=surface))

    relations = result.relations.copy(deep=True)
    relations.loc[relations.index[0], "official_code_label"] = "Other official meaning"
    mismatched_relation = _result_with_hashes(replace(result, relations=relations))

    for changed in (missing_meaning, invented_unknown, mismatched_relation):
        with pytest.raises(
            PlanningFeatureCodeError,
            match="official|meaning|UNKNOWN|relation|feature",
        ):
            module.validate_planning_feature_code_result_envelope(changed)


def test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result() -> (
    None
):
    module = importlib.import_module("landscout.stages.resolve_planning_feature_codes")
    result = _schema_v5_envelope_result()

    class DerivedPlanningFeatureCodeResult(PlanningFeatureCodeResult):
        pass

    derived = DerivedPlanningFeatureCodeResult(**result.__dict__)
    with pytest.raises(PlanningFeatureCodeError, match="type|result"):
        module.validate_planning_feature_code_result_envelope(derived)
    module.validate_planning_feature_code_result_envelope(result)
```
