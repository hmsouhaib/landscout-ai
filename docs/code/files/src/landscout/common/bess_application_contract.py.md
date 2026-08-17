# `src/landscout/common/bess_application_contract.py`

## File identity

- Repository path: `src/landscout/common/bess_application_contract.py`
- File type: Python source
- Primary responsibility: Enforces intrinsic BESS planning feature-catalog and factual-relation contracts shared by application and aggregation stages.
- Layer / domain: `internal common contract/utility` / `common`
- Public or internal role: Module symbols without a package re-export are internal unless imported directly by repository code.
- Source SHA256: `710ddf6051636362585071089a566d8386844767b0cd8a00c1e6e877a2ca1d6b`

## 1. Purpose

Enforces intrinsic BESS planning feature-catalog and factual-relation contracts shared by application and aggregation stages.

## 2. Position in LandScout architecture

This file is a `internal common contract/utility` artifact in the `common` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import math` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `from numbers import Integral, Real` — required by the implementation paths and symbols documented below.
- `from pathlib import PurePosixPath, PureWindowsPath` — required by the implementation paths and symbols documented below.
- `from typing import Literal, cast` — required by the implementation paths and symbols documented below.
- `from urllib.parse import urlsplit` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.
- `from shapely import get_coordinate_dimension, get_parts` — required by the implementation paths and symbols documented below.
- `from shapely.geometry.base import BaseGeometry` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.planning_feature_contract import ( validate_intrinsic_planning_feature_relations, )` — required by the implementation paths and symbols documented below.
- `from landscout.common.planning_feature_schema import ( GeometryKind, feature_columns, feature_dtypes, relation_columns, relation_dtypes, validate_canonical_frame_schema, )` — required by the implementation paths and symbols documented below.
- `from landscout.common.planning_overlay import technical_overlay_tolerance` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `APPLICATION_SCOPE` | `"FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_SCOPE` | `"OFFICIAL_CNIG_CODE_MEANING_ONLY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_COLUMNS` | `( "bess_cnig_policy_application_status", "bess_cnig_precheck_status", "bess_cnig_precheck_confidence", "bess_cnig_status_priority", "bess_cnig_rationale", "bess_cnig_required_human_action", "bess_cnig_limitations", "bess_cnig_application_scope", "bess_cnig_policy_scope", "bess_cnig_local_feature_text_interpreted", "bess_cnig_local_regulation_content_interpreted", "bess_cnig_legal_conclusion_produced", "bess_cnig_parcel_status_aggregated", "bess_cnig_parcel_rejection_performed", "bess_cnig_score_calculated", "bess_cnig_policy_profile", "bess_cnig_policy_sha256", "bess_cnig_policy_result_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `DECISION_COLUMNS` | `( "bess_cnig_precheck_status", "bess_cnig_precheck_confidence", "bess_cnig_status_priority", "bess_cnig_rationale", "bess_cnig_required_human_action", "bess_cnig_limitations", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `FLAG_COLUMNS` | `( "bess_cnig_local_feature_text_interpreted", "bess_cnig_local_regulation_content_interpreted", "bess_cnig_legal_conclusion_produced", "bess_cnig_parcel_status_aggregated", "bess_cnig_parcel_rejection_performed", "bess_cnig_score_calculated", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `STRING_POLICY_COLUMNS` | `tuple( column for column in POLICY_COLUMNS if column not in {"bess_cnig_status_priority", *FLAG_COLUMNS} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `POLICY_SUFFIX_DTYPES` | `{ **{column: "str" for column in STRING_POLICY_COLUMNS}, "bess_cnig_status_priority": "Int64", **{column: "bool" for column in FLAG_COLUMNS}, }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ALLOWED_PRECHECK_STATUSES` | `frozenset( { "LIKELY_MATERIAL_CONSTRAINT", "MATERIAL_REVIEW_REQUIRED", "DESIGN_REVIEW_REQUIRED", "CONTEXT_REVIEW_REQUIRED", "UNKNOWN", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ALLOWED_CONFIDENCES` | `frozenset({"HIGH", "MEDIUM", "LOW"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ALLOWED_FEATURE_FAMILIES` | `frozenset({"PRESCRIPTION", "INFORMATION"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `NULL_LITERALS` | `frozenset({"None", "nan", "<NA>"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CODE_PATTERN` | `re.compile(r"[0-9]{2}")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SHA_PATTERN` | `re.compile(r"[0-9a-f]{64}")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_FEATURE_SPECS` | `{ "SURFACE": ( frozenset({"prescription_surface", "information_surface"}), frozenset({"Polygon", "MultiPolygon"}), "feature_area_m2", ), "LINE": ( frozenset({"prescription_line", "information_line"}), frozenset({"LineString", "MultiLineString"}), "feature_length_m", ), "POINT": ( frozenset({"prescription_point", "information_point"}), frozenset({"Point", "MultiPoint"}), "point_member_count", ), }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

No class, model, or dataclass is declared in this file.

## 6. Functions and methods

### `_null_value`

**Signature**

```python
def _null_value(value: object) -> object:
```

**Purpose**

Implements null value according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `value`; `None`.

**Algorithm**

1. Checks `value is None or value is pd.NA`. When true: Returns `None`.
2. Checks `isinstance(value, float) and math.isnan(value)`. When true: Returns `None`.
3. Returns `value`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `isinstance`, `math.isnan`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `_optional_official_string`
- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_policy_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_exact_string`

**Signature**

```python
def _exact_string(value: object, label: str) -> str:
```

**Purpose**

Implements exact string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `ValueError(f'{label} must be an exact non-empty string')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `isinstance`, `value.strip`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `_optional_official_string`
- `src/landscout/common/bess_application_contract.py` — `_relation_identity_string`
- `src/landscout/common/bess_application_contract.py` — `_sha256`
- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_feature_catalogs`
- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_policy_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_sha256`

**Signature**

```python
def _sha256(value: object, label: str) -> str:
```

**Purpose**

Implements sha256 according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `exact`.

**Algorithm**

1. Computes `exact` from `_exact_string(value, label)`.
2. Checks `SHA_PATTERN.fullmatch(exact) is None`. When true: Raises `ValueError(f'{label} must be a lowercase SHA256')`.
3. Returns `exact`.

**Validation and invariants**

- Rejects or diverts the path when `SHA_PATTERN.fullmatch(exact) is None` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SHA_PATTERN.fullmatch`, `ValueError`, `_exact_string`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `_validate_official_row`
- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_policy_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_optional_official_string`

**Signature**

```python
def _optional_official_string(value: object, label: str) -> str | None:
```

**Purpose**

Implements optional official string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str | None`. Observed return expression(s): `exact`; `None`.

**Algorithm**

1. Checks `_null_value(value) is None`. When true: Returns `None`.
2. Computes `exact` from `_exact_string(value, label)`.
3. Checks `exact in NULL_LITERALS`. When true: Raises `ValueError(f'{label} must not be a textual null sentinel')`.
4. Returns `exact`.

**Validation and invariants**

- Rejects or diverts the path when `exact in NULL_LITERALS` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_exact_string`, `_null_value`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `_validate_official_row`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_validate_official_row`

**Signature**

```python
def _validate_official_row(
    row: dict[str, object],
    *,
    label: str,
    source_document_id: str,
    source_archive_sha256: str,
    cnig_profile: str,
    cnig_profile_sha256: str,
) -> None:
```

**Purpose**

Validates and rejects malformed official row according to the exact implementation and guards in this file.

**Inputs**

- `row` (`dict[str, object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_document_id` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_archive_sha256` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cnig_profile` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cnig_profile_sha256` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `row['source_document_id'] != source_document_id`. When true: Raises `ValueError(f'{label} source document lineage differs from envelope')`.
2. Checks `row['source_archive_sha256'] != source_archive_sha256`. When true: Raises `ValueError(f'{label} source archive lineage differs from envelope')`.
3. Calls `_sha256(row['source_archive_sha256'], f'{label} source archive SHA256')` for its validation or side effect.
4. Checks `row['official_code_profile'] != cnig_profile`. When true: Raises `ValueError(f'{label} official profile lineage differs from envelope')`.
5. Checks `row['official_code_profile_sha256'] != cnig_profile_sha256`. When true: Raises `ValueError(f'{label} official profile SHA256 lineage differs')`.
6. Calls `_sha256(row['official_code_profile_sha256'], f'{label} official profile SHA256')` for its validation or side effect.
7. Computes `official_status` from `row['official_code_status']`.
8. Computes `label_value` from `_optional_official_string(row['official_code_label'], f'{label} official label')`.
9. Computes `legal` from `_optional_official_string(row['official_legal_reference'], f'{label} official legal reference')`.
10. Computes `regulation` from `_optional_official_string(row['official_regulation_reference'], f'{label} official regulation reference')`.
11. Computes `source_url` from `_optional_official_string(row['official_code_source_url'], f'{label} official source URL')`.
12. Checks `official_status == 'RESOLVED_OFFICIAL'`. When true: Checks `label_value is None or source_url is None`. When true: Raises `ValueError(f'{label} resolved official meaning is incomplete')`. Computes `parsed_url` from `urlsplit(source_url)`. Checks `parsed_url.scheme != 'https' or not parsed_url.netloc`. When true: Raises `ValueError(f'{label} official source URL must be exact HTTPS')`. Otherwise: Checks `official_status == 'UNKNOWN_CODE_PAIR'`. When true: Checks `any((value is not None for value in (label_value, legal, regulation, source_url)))`. When true: Raises `ValueError(f'{label} unknown official meaning must remain null')`. Otherwise: Raises `ValueError(f'{label} official-code status is invalid')`.

**Validation and invariants**

- Rejects or diverts the path when `row['source_document_id'] != source_document_id` is true.
- Rejects or diverts the path when `row['source_archive_sha256'] != source_archive_sha256` is true.
- Rejects or diverts the path when `row['official_code_profile'] != cnig_profile` is true.
- Rejects or diverts the path when `row['official_code_profile_sha256'] != cnig_profile_sha256` is true.
- Rejects or diverts the path when `official_status == 'RESOLVED_OFFICIAL'` is true.
- Rejects or diverts the path when `label_value is None or source_url is None` is true.
- Rejects or diverts the path when `parsed_url.scheme != 'https' or not parsed_url.netloc` is true.
- Rejects or diverts the path when `official_status == 'UNKNOWN_CODE_PAIR'` is true.
- Rejects or diverts the path when `any((value is not None for value in (label_value, legal, regulation, source_url)))` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_optional_official_string`, `_sha256`, `any`, `urlsplit`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_policy_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `validate_bess_application_policy_frame`

**Signature**

```python
def validate_bess_application_policy_frame(
    frame: pd.DataFrame,
    *,
    label: str,
    policy_profile: str,
    policy_sha256: str,
    policy_result_sha256: str,
    source_document_id: str,
    source_archive_sha256: str,
    cnig_profile: str,
    cnig_profile_sha256: str,
) -> None:
```

**Purpose**

Validate the complete canonical application suffix and every row.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_profile` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_sha256` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_result_sha256` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_document_id` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_archive_sha256` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cnig_profile` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cnig_profile_sha256` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `_exact_string(source_document_id, f'{label} source document identity')` for its validation or side effect.
2. Calls `_sha256(source_archive_sha256, f'{label} source archive SHA256')` for its validation or side effect.
3. Calls `_exact_string(cnig_profile, f'{label} CNIG profile')` for its validation or side effect.
4. Calls `_sha256(cnig_profile_sha256, f'{label} CNIG profile SHA256')` for its validation or side effect.
5. Checks `not isinstance(frame, pd.DataFrame)`. When true: Raises `TypeError(f'{label} must be a DataFrame')`.
6. Checks `frame.columns.duplicated().any()`. When true: Raises `ValueError(f'{label} contains duplicate columns')`.
7. Checks `tuple(frame.columns[-len(POLICY_COLUMNS):]) != POLICY_COLUMNS`. When true: Raises `ValueError(f'{label} policy schema is invalid')`.
8. Iterates `(column, expected_dtype)` over `POLICY_SUFFIX_DTYPES.items()`. For each value: Checks `str(frame[column].dtype) != expected_dtype`. When true: Raises `ValueError(f'{label} policy dtype is invalid for {column}')`.
9. Computes `required` from `{'feature_family', 'type_code_raw', 'subtype_code_raw', 'official_code_status', 'official_code_label', 'official_legal_reference', 'official_regulation_reference', 'official_code_source_url', 'official_code_profile', 'official_code_profile_sha256', 'source_document_id', 'source_archive_sha256', *POLICY_COLUMNS}`.
10. Checks `not required.issubset(frame.columns)`. When true: Raises `ValueError(f'{label} application identity schema is incomplete')`.
11. Iterates `row` over `frame.to_dict('records')`. For each value: Calls `_validate_official_row(row, label=label, source_document_id=source_document_id, source_archive_sha256=source_archive_sha256, cnig_profile=cnig_profile, cnig_profile_sha256=cnig_profile_sha256)` for its validation or side effect. Checks `row['feature_family'] not in ALLOWED_FEATURE_FAMILIES`. When true: Raises `ValueError(f'{label} feature family is invalid')`. Iterates `column` over `('type_code_raw', 'subtype_code_raw')`. For each value: Computes `value` from `row[column]`. Checks `not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None`. When true: Raises `ValueError(f'{label} {column} is not an exact two-digit code')`. Executes 8 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, pd.DataFrame)` is true.
- Rejects or diverts the path when `frame.columns.duplicated().any()` is true.
- Rejects or diverts the path when `tuple(frame.columns[-len(POLICY_COLUMNS):]) != POLICY_COLUMNS` is true.
- Rejects or diverts the path when `not required.issubset(frame.columns)` is true.
- Rejects or diverts the path when `str(frame[column].dtype) != expected_dtype` is true.
- Rejects or diverts the path when `row['feature_family'] not in ALLOWED_FEATURE_FAMILIES` is true.
- Rejects or diverts the path when `application_status == 'APPLIED_EXACT_POLICY'` is true.
- Rejects or diverts the path when `row['bess_cnig_application_scope'] != APPLICATION_SCOPE` is true.
- Rejects or diverts the path when `row['bess_cnig_policy_scope'] != POLICY_SCOPE` is true.
- Rejects or diverts the path when `any((row[column] is not False for column in FLAG_COLUMNS))` is true.
- Rejects or diverts the path when `not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None` is true.
- Rejects or diverts the path when `official_status != 'RESOLVED_OFFICIAL'` is true.
- Rejects or diverts the path when `any((_null_value(row[column]) is None for column in DECISION_COLUMNS))` is true.
- Rejects or diverts the path when `row['bess_cnig_precheck_status'] not in ALLOWED_PRECHECK_STATUSES` is true.
- Rejects or diverts the path when `row['bess_cnig_precheck_confidence'] not in ALLOWED_CONFIDENCES` is true.
- Rejects or diverts the path when `isinstance(priority, bool) or not isinstance(priority, Integral) or int(priority) <= 0` is true.
- Rejects or diverts the path when `application_status == 'UNRESOLVED_CODE_PAIR'` is true.
- Rejects or diverts the path when `isinstance(value, str) and value in NULL_LITERALS` is true.
- Rejects or diverts the path when `actual != expected` is true.
- Rejects or diverts the path when `official_status != 'UNKNOWN_CODE_PAIR'` is true.
- Rejects or diverts the path when `any((_null_value(row[column]) is not None for column in DECISION_COLUMNS))` is true.

**Exceptions**

- Explicitly raises: `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CODE_PATTERN.fullmatch`, `POLICY_SUFFIX_DTYPES.items`, `TypeError`, `ValueError`, `_exact_string`, `_null_value`, `_sha256`, `_validate_official_row`, `any`, `frame.columns.duplicated`, `frame.columns.duplicated().any`, `frame.to_dict`, `int`, `isinstance`, `len`, `required.issubset`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_feature_catalogs`
- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_relation_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_relation_identity_string`

**Signature**

```python
def _relation_identity_string(value: object, label: str) -> str:
```

**Purpose**

Implements relation identity string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `exact`.

**Algorithm**

1. Computes `exact` from `_exact_string(value, label)`.
2. Checks `exact in NULL_LITERALS`. When true: Raises `ValueError(f'{label} must not be a textual null sentinel')`.
3. Returns `exact`.

**Validation and invariants**

- Rejects or diverts the path when `exact in NULL_LITERALS` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_exact_string`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `_portable_feature_id`
- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_feature_catalogs`
- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_relation_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_portable_feature_id`

**Signature**

```python
def _portable_feature_id(value: object, label: str) -> str:
```

**Purpose**

Implements portable feature id according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `feature_id`.

**Algorithm**

1. Computes `feature_id` from `_relation_identity_string(value, label)`.
2. Checks `PurePosixPath(feature_id).is_absolute() or PureWindowsPath(feature_id).is_absolute()`. When true: Raises `ValueError(f'{label} must not be an absolute path')`.
3. Returns `feature_id`.

**Validation and invariants**

- Rejects or diverts the path when `PurePosixPath(feature_id).is_absolute() or PureWindowsPath(feature_id).is_absolute()` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PurePosixPath`, `PurePosixPath(feature_id).is_absolute`, `PureWindowsPath`, `PureWindowsPath(feature_id).is_absolute`, `ValueError`, `_relation_identity_string`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_feature_catalogs`
- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_relation_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_status_priority_mapping`

**Signature**

```python
def _status_priority_mapping(
    frame: pd.DataFrame, label: str
) -> tuple[dict[int, str], dict[str, int]]:
```

**Purpose**

Implements status priority mapping according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[dict[int, str], dict[str, int]]`. Observed return expression(s): `({priority: next(iter(statuses)) for priority, statuses in priority_to_statuses.items()}, {status: next(iter(priorities)) for status, priorities in status_to_priorities.items()})`.

**Algorithm**

1. Defines `priority_to_statuses` with annotation `dict[int, set[str]]` from `{}`.
2. Defines `status_to_priorities` with annotation `dict[str, set[int]]` from `{}`.
3. Computes `applied` from `frame[frame['bess_cnig_policy_application_status'] == 'APPLIED_EXACT_POLICY']`.
4. Iterates `row` over `applied.to_dict('records')`. For each value: Computes `priority` from `int(row['bess_cnig_status_priority'])`. Computes `status` from `str(row['bess_cnig_precheck_status'])`. Calls `priority_to_statuses.setdefault(priority, set()).add(status)` for its validation or side effect. Executes 1 additional source-ordered statement(s).
5. Checks `any((len(statuses) != 1 for statuses in priority_to_statuses.values())) or any((len(priorities) != 1 for priorities in status_to_priorities.values()))`. When true: Raises `ValueError(f'{label} status/priority mapping is not one-to-one')`.
6. Returns `({priority: next(iter(statuses)) for priority, statuses in priority_to_statuses.items()}, {status: next(iter(priorities)) for status, priorities in status_to_priorities.items()})`.

**Validation and invariants**

- Rejects or diverts the path when `any((len(statuses) != 1 for statuses in priority_to_statuses.values())) or any((len(priorities) != 1 for priorities in status_to_priorities.values()))` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `any`, `applied.to_dict`, `int`, `iter`, `len`, `next`, `priority_to_statuses.items`, `priority_to_statuses.setdefault`, `priority_to_statuses.setdefault(priority, set()).add`, `priority_to_statuses.values`, `set`, `status_to_priorities.items`, `status_to_priorities.setdefault`, `status_to_priorities.setdefault(status, set()).add`, `status_to_priorities.values`, `str`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_feature_catalogs`
- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_relation_frame`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_feature_metric`

**Signature**

```python
def _feature_metric(value: object, expected: float, label: str) -> None:
```

**Purpose**

Implements feature metric according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`float`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `isinstance(value, bool) or not isinstance(value, Real)`. When true: Raises `TypeError(f'{label} must be numeric')`.
2. Computes `number` from `float(value)`.
3. Checks `not math.isfinite(number) or number <= 0`. When true: Raises `ValueError(f'{label} must be finite and positive')`.
4. Checks `abs(number - expected) > technical_overlay_tolerance(max(abs(number), abs(expected)))`. When true: Raises `ValueError(f'{label} is inconsistent with feature geometry')`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Real)` is true.
- Rejects or diverts the path when `not math.isfinite(number) or number <= 0` is true.
- Rejects or diverts the path when `abs(number - expected) > technical_overlay_tolerance(max(abs(number), abs(expected)))` is true.

**Exceptions**

- Explicitly raises: `TypeError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `TypeError`, `ValueError`, `abs`, `float`, `isinstance`, `math.isfinite`, `max`, `technical_overlay_tolerance`.

**Known repository callers**

- `src/landscout/common/bess_application_contract.py` — `validate_bess_application_feature_catalogs`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `validate_bess_application_feature_catalogs`

**Signature**

```python
def validate_bess_application_feature_catalogs(
    surface: gpd.GeoDataFrame,
    line: gpd.GeoDataFrame,
    point: gpd.GeoDataFrame,
    *,
    policy_profile: str,
    policy_sha256: str,
    policy_result_sha256: str,
    source_document_id: str,
    source_archive_sha256: str,
    cnig_profile: str,
    cnig_profile_sha256: str,
) -> tuple[dict[int, str], dict[str, int]]:
```

**Purpose**

Validate all intrinsic feature facts, identities, geometry, and mappings.

**Inputs**

- `surface` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_profile` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_sha256` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_result_sha256` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_document_id` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_archive_sha256` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cnig_profile` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cnig_profile_sha256` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[dict[int, str], dict[str, int]]`. Observed return expression(s): `_status_priority_mapping(combined, 'feature document-wide')`.

**Algorithm**

1. Defines `feature_ids` with annotation `list[str]` from `[]`.
2. Defines `applied_frames` with annotation `list[pd.DataFrame]` from `[]`.
3. Iterates `(frame, kind, label)` over `((surface, 'SURFACE', 'surface features'), (line, 'LINE', 'line features'), (point, 'POINT', 'point features'))`. For each value: Computes `geometry_kind` from `cast(GeometryKind, kind)`. Computes `suffix_dtypes` from `tuple((POLICY_SUFFIX_DTYPES[column] for column in POLICY_COLUMNS))`. Calls `validate_canonical_frame_schema(frame, columns=feature_columns(geometry_kind, POLICY_COLUMNS), dtypes=feature_dtypes(geometry_kind, suffix_dtypes, frame), label=label, geospatial=True)` for its validation or side effect. Executes 7 additional source-ordered statement(s).
4. Checks `len(feature_ids) != len(set(feature_ids))`. When true: Raises `ValueError('planning feature identity must be globally unique')`.
5. Computes `combined` from `pd.concat(applied_frames, ignore_index=True)`.
6. Returns `_status_priority_mapping(combined, 'feature document-wide')`.

**Validation and invariants**

- Rejects or diverts the path when `len(feature_ids) != len(set(feature_ids))` is true.
- Rejects or diverts the path when `not required.issubset(frame.columns)` is true.
- Rejects or diverts the path when `frame.geometry.name != 'geometry' or frame.crs is None` is true.
- Rejects or diverts the path when `not CRS.from_user_input(frame.crs).equals(CRS.from_epsg(2154))` is true.
- Rejects or diverts the path when `document_id != source_document_id` is true.
- Rejects or diverts the path when `not equivalent_source_crs` is true.
- Rejects or diverts the path when `logical_layer not in allowed_layers` is true.
- Rejects or diverts the path when `row['feature_family'] != expected_family` is true.
- Rejects or diverts the path when `row['geometry_kind'] != kind` is true.
- Rejects or diverts the path when `feature_id != expected_id` is true.
- Rejects or diverts the path when `not isinstance(geometry, BaseGeometry) or geometry.is_empty or (not geometry.is_valid) or (geometry.geom_type not in geometry_types)` is true.
- Rejects or diverts the path when `int(get_coordinate_dimension(geometry)) != 2` is true.
- Rejects or diverts the path when `isinstance(count, bool) or not isinstance(count, Integral) or int(count) <= 0 or (int(count) != len(get_parts(geometry)))` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `CRS.from_epsg`, `CRS.from_user_input`, `CRS.from_user_input(frame.crs).equals`, `CRS.from_user_input(source_crs).equals`, `ValueError`, `_exact_string`, `_feature_metric`, `_portable_feature_id`, `_relation_identity_string`, `_status_priority_mapping`, `applied_frames.append`, `cast`, `feature_columns`, `feature_dtypes`, `feature_ids.append`, `float`, `frame.to_dict`, `get_coordinate_dimension`, `get_parts`, `int`, `isinstance`, `len`, `pd.concat`, `required.issubset`, `set`, `str`, `str(logical_layer).startswith`, `tuple`, `validate_bess_application_policy_frame`, `validate_canonical_frame_schema`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `validate_bess_application_relation_frame`

**Signature**

```python
def validate_bess_application_relation_frame(
    frame: pd.DataFrame,
    *,
    label: str,
    policy_profile: str,
    policy_sha256: str,
    policy_result_sha256: str,
    source_document_id: str,
    source_archive_sha256: str,
    cnig_profile: str,
    cnig_profile_sha256: str,
) -> tuple[dict[int, str], dict[str, int]]:
```

**Purpose**

Validate canonical application rows and the complete relation identity.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_profile` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_sha256` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_result_sha256` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_document_id` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_archive_sha256` (`str`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cnig_profile` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `cnig_profile_sha256` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[dict[int, str], dict[str, int]]`. Observed return expression(s): `_status_priority_mapping(frame, f'{label} document-wide')`.

**Algorithm**

1. Computes `suffix_dtypes` from `tuple((POLICY_SUFFIX_DTYPES[column] for column in POLICY_COLUMNS))`.
2. Calls `validate_canonical_frame_schema(frame, columns=relation_columns(POLICY_COLUMNS), dtypes=relation_dtypes(suffix_dtypes), label=label, geospatial=False)` for its validation or side effect.
3. Calls `validate_bess_application_policy_frame(frame, label=label, policy_profile=policy_profile, policy_sha256=policy_sha256, policy_result_sha256=policy_result_sha256, source_document_id=source_document_id, source_archive_sha256=source_archive_sha256, cnig_profile=cnig_profile, cnig_profile_sha256=cnig_profile_sha256)` for its validation or side effect.
4. Computes `required` from `{'parcel_id', 'planning_feature_id', 'relation_type'}`.
5. Checks `not required.issubset(frame.columns)`. When true: Raises `ValueError(f'{label} relation identity schema is incomplete')`.
6. Iterates `row` over `frame.to_dict('records')`. For each value: Calls `_relation_identity_string(row['parcel_id'], f'{label} parcel identity')` for its validation or side effect. Computes `feature_id` from `_portable_feature_id(row['planning_feature_id'], f'{label} Feature ID identity')`. Asserts `feature_id`.
7. Checks `frame.duplicated(['parcel_id', 'planning_feature_id']).any()`. When true: Raises `ValueError(f'{label} contains a duplicate parcel/feature relation pair')`.
8. Calls `validate_intrinsic_planning_feature_relations(frame)` for its validation or side effect.
9. Returns `_status_priority_mapping(frame, f'{label} document-wide')`.

**Validation and invariants**

- Rejects or diverts the path when `not required.issubset(frame.columns)` is true.
- Rejects or diverts the path when `frame.duplicated(['parcel_id', 'planning_feature_id']).any()` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_portable_feature_id`, `_relation_identity_string`, `_status_priority_mapping`, `frame.duplicated`, `frame.duplicated(['parcel_id', 'planning_feature_id']).any`, `frame.to_dict`, `relation_columns`, `relation_dtypes`, `required.issubset`, `tuple`, `validate_bess_application_policy_frame`, `validate_canonical_frame_schema`, `validate_intrinsic_planning_feature_relations`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_application_relations`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_validate_relation_rows`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `common` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `APPLIED_EXACT_POLICY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `UNRESOLVED_CODE_PAIR` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_application_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_legal_conclusion_produced` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_limitations` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_local_feature_text_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_local_regulation_content_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_rejection_performed` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_status_aggregated` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_application_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_result_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_precheck_confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_rationale` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_required_human_action` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_score_calculated` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_status_priority` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_family` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `logical_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_profile_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `official_legal_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_regulation_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_crs` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |

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
