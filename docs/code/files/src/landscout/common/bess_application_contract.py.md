# `src/landscout/common/bess_application_contract.py`

## File identity

- Repository path: `src/landscout/common/bess_application_contract.py`
- File type: Python source
- Layer: internal common contract
- Domain: common contract
- Responsibility: Enforces intrinsic BESS planning feature-catalog and factual-relation contracts shared by application and aggregation stages.
- Source SHA256: `710ddf6051636362585071089a566d8386844767b0cd8a00c1e6e877a2ca1d6b`

## 1. Purpose

Enforces intrinsic BESS planning feature-catalog and factual-relation contracts shared by application and aggregation stages.

## 2. Position in LandScout architecture

This file belongs to the **internal common contract** layer and the **common contract** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import math`
- `import re`
- `from numbers import Integral, Real`
- `from pathlib import PurePosixPath, PureWindowsPath`
- `from typing import Literal, cast`
- `from urllib.parse import urlsplit`

### Third-party packages

- `import geopandas as gpd`
- `import pandas as pd`
- `from pyproj import CRS`
- `from shapely import get_coordinate_dimension, get_parts`
- `from shapely.geometry.base import BaseGeometry`

### Internal LandScout imports

- `from landscout.common.planning_feature_contract import (
    validate_intrinsic_planning_feature_relations,
)`
- `from landscout.common.planning_feature_schema import (
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
- `from landscout.common.planning_overlay import technical_overlay_tolerance`

## 4. Contract taxonomy

### A. Python constants

#### `APPLICATION_SCOPE`

```python
APPLICATION_SCOPE = "FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` (import), `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::_policy_values` (value reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::_build_result` (value reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` (value reference).

#### `POLICY_SCOPE`

```python
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` (import), `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` (import), `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_parcel_summary` (value reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_build_result` (value reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` (value reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` (value reference).

#### `POLICY_COLUMNS`

```python
POLICY_COLUMNS = (
    "bess_cnig_policy_application_status",
    "bess_cnig_precheck_status",
    "bess_cnig_precheck_confidence",
    "bess_cnig_status_priority",
    "bess_cnig_rationale",
    "bess_cnig_required_human_action",
    "bess_cnig_limitations",
    "bess_cnig_application_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` (import), `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` (import), `src/landscout/common/bess_application_contract.py::<module>` (value reference), `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value reference), `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` (value reference), `src/landscout/common/bess_application_contract.py::validate_bess_application_relation_frame` (value reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::_assign_policy_columns` (value reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_feature_catalog` (value reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_relations` (value reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` (value reference), `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` (value reference).

#### `DECISION_COLUMNS`

```python
DECISION_COLUMNS = (
    "bess_cnig_precheck_status",
    "bess_cnig_precheck_confidence",
    "bess_cnig_status_priority",
    "bess_cnig_rationale",
    "bess_cnig_required_human_action",
    "bess_cnig_limitations",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value reference).

#### `FLAG_COLUMNS`

```python
FLAG_COLUMNS = (
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` (import), `src/landscout/common/bess_application_contract.py::<module>` (value reference), `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::_assign_policy_columns` (value reference).

#### `STRING_POLICY_COLUMNS`

```python
STRING_POLICY_COLUMNS = tuple(
    column
    for column in POLICY_COLUMNS
    if column not in {"bess_cnig_status_priority", *FLAG_COLUMNS}
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` (import), `src/landscout/common/bess_application_contract.py::<module>` (value reference), `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::_assign_policy_columns` (value reference).

#### `POLICY_SUFFIX_DTYPES`

```python
POLICY_SUFFIX_DTYPES = {
    **{column: "str" for column in STRING_POLICY_COLUMNS},
    "bess_cnig_status_priority": "Int64",
    **{column: "bool" for column in FLAG_COLUMNS},
}
```

Canonical Pandas/GeoPandas dtype contract aligned with the named schema. Consumers include `tests/unit/test_aggregate_bess_planning_feature_policy.py::<module>` (import), `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value reference), `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` (value reference), `src/landscout/common/bess_application_contract.py::validate_bess_application_relation_frame` (value reference), `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` (value reference).

#### `ALLOWED_PRECHECK_STATUSES`

```python
ALLOWED_PRECHECK_STATUSES = frozenset(
    {
        "LIKELY_MATERIAL_CONSTRAINT",
        "MATERIAL_REVIEW_REQUIRED",
        "DESIGN_REVIEW_REQUIRED",
        "CONTEXT_REVIEW_REQUIRED",
        "UNKNOWN",
    }
)
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` (import), `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_local_domains` (value reference).

#### `ALLOWED_CONFIDENCES`

```python
ALLOWED_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` (import), `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_local_domains` (value reference).

#### `ALLOWED_FEATURE_FAMILIES`

```python
ALLOWED_FEATURE_FAMILIES = frozenset({"PRESCRIPTION", "INFORMATION"})
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value reference).

#### `NULL_LITERALS`

```python
NULL_LITERALS = frozenset({"None", "nan", "<NA>"})
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` (import), `src/landscout/common/bess_application_contract.py::_optional_official_string` (value reference), `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value reference), `src/landscout/common/bess_application_contract.py::_relation_identity_string` (value reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_feature_id` (value reference), `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_parcel_frame` (value reference).

#### `CODE_PATTERN`

```python
CODE_PATTERN = re.compile(r"[0-9]{2}")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly. Consumers include `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` (value reference).

#### `SHA_PATTERN`

```python
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly. Consumers include `src/landscout/common/bess_application_contract.py::_sha256` (value reference).

#### `_FEATURE_SPECS`

```python
_FEATURE_SPECS = {
    "SURFACE": (
        frozenset({"prescription_surface", "information_surface"}),
        frozenset({"Polygon", "MultiPolygon"}),
        "feature_area_m2",
    ),
    "LINE": (
        frozenset({"prescription_line", "information_line"}),
        frozenset({"LineString", "MultiLineString"}),
        "feature_length_m",
    ),
    "POINT": (
        frozenset({"prescription_point", "information_point"}),
        frozenset({"Point", "MultiPoint"}),
        "point_member_count",
    ),
}
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` (value reference).


### B. Type aliases and closed domains

#### `ApplicationStatus`

```python
ApplicationStatus = Literal["APPLIED_EXACT_POLICY", "UNRESOLVED_CODE_PAIR"]
```

BESS CNIG application state: exact policy applied or unresolved code pair. Enforced/consumed by `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` (import), `src/landscout/stages/apply_bess_planning_feature_policy.py::_policy_values` (type annotation), `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_feature_catalog` (type annotation).


### C. Meaningful dunder contracts

No meaningful module-level dunder contract is declared.

### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

No class/model/dataclass is declared.

## 6. Functions and methods

### `_null_value`

**Exact signature**

```python
def _null_value(value: object) -> object:
```

**Purpose**

Return `None` for Python `None`, the singleton `pandas.NA`, or a NaN recognized by `isinstance(value, float)` and `math.isnan`; return every other object unchanged. This is not a general `pandas.isna` conversion and does not rewrite textual sentinels.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
value

None

None
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

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

- direct call: `src/landscout/common/bess_application_contract.py::_optional_official_string` via `_null_value`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` via `_null_value`.

**Complete source-ordered implementation**

```python
def _null_value(value: object) -> object:
    if value is None or value is pd.NA:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    return value
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_exact_string`

**Exact signature**

```python
def _exact_string(value: object, label: str) -> str:
```

**Purpose**

Require a string instance that is nonempty and already equal to its stripped form, then return it unchanged. There is no trimming, case conversion or exact-built-in-type requirement; `label` only provides error context.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip()`.
- Explicit raise expressions: `ValueError(f'{label} must be an exact non-empty string')`.

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

- direct call: `src/landscout/common/bess_application_contract.py::_sha256` via `_exact_string`.
- direct call: `src/landscout/common/bess_application_contract.py::_optional_official_string` via `_exact_string`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` via `_exact_string`.
- direct call: `src/landscout/common/bess_application_contract.py::_relation_identity_string` via `_exact_string`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` via `_exact_string`.

**Complete source-ordered implementation**

```python
def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be an exact non-empty string")
    return value
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_sha256`

**Exact signature**

```python
def _sha256(value: object, label: str) -> str:
```

**Purpose**

Apply `_exact_string`, then require exactly 64 lowercase hexadecimal characters through `SHA_PATTERN.fullmatch`. Return the textual digest unchanged. No bytes are read or hashed, and no digest authenticity is established.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
exact
```

**Validation and exceptions**

- Guard with a raise path: `SHA_PATTERN.fullmatch(exact) is None`.
- Explicit raise expressions: `ValueError(f'{label} must be a lowercase SHA256')`.

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

- direct call: `src/landscout/common/bess_application_contract.py::_validate_official_row` via `_sha256`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` via `_sha256`.

**Complete source-ordered implementation**

```python
def _sha256(value: object, label: str) -> str:
    exact = _exact_string(value, label)
    if SHA_PATTERN.fullmatch(exact) is None:
        raise ValueError(f"{label} must be a lowercase SHA256")
    return exact
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_optional_official_string`

**Exact signature**

```python
def _optional_official_string(value: object, label: str) -> str | None:
```

**Purpose**

Return `None` only for the null cases recognized by `_null_value`; otherwise require an exact nonempty string and reject the three literal missing-value spellings in `NULL_LITERALS`. Optionality does not authorize empty/trimmed strings or invented meaning.

**Return contract**

- Declared return annotation: `str | None`.
- Every observed return expression is reproduced without truncation:
```python
exact

None
```

**Validation and exceptions**

- Guard with a raise path: `exact in NULL_LITERALS`.
- Explicit raise expressions: `ValueError(f'{label} must not be a textual null sentinel')`.

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

- direct call: `src/landscout/common/bess_application_contract.py::_validate_official_row` via `_optional_official_string`.

**Complete source-ordered implementation**

```python
def _optional_official_string(value: object, label: str) -> str | None:
    if _null_value(value) is None:
        return None
    exact = _exact_string(value, label)
    if exact in NULL_LITERALS:
        raise ValueError(f"{label} must not be a textual null sentinel")
    return exact
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_validate_official_row`

**Exact signature**

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

Compare document/archive and CNIG profile/hash lineage with the supplied envelope, then validate both textual digests. Parse the four optional meaning cells. RESOLVED_OFFICIAL requires a label and source URL, while legal/regulation references may remain truly null; its URL is checked only for HTTPS scheme and a nonempty authority. UNKNOWN_CODE_PAIR requires all four meaning cells to remain null. Any other status is rejected. This helper does not fetch the URL, apply safe-transport DNS rules, consult an official dictionary, or prove the upstream meaning.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `row['source_document_id'] != source_document_id`.
- Guard with a raise path: `row['source_archive_sha256'] != source_archive_sha256`.
- Guard with a raise path: `row['official_code_profile'] != cnig_profile`.
- Guard with a raise path: `row['official_code_profile_sha256'] != cnig_profile_sha256`.
- Guard with a raise path: `official_status == 'RESOLVED_OFFICIAL'`.
- Guard with a raise path: `label_value is None or source_url is None`.
- Guard with a raise path: `parsed_url.scheme != 'https' or not parsed_url.netloc`.
- Guard with a raise path: `official_status == 'UNKNOWN_CODE_PAIR'`.
- Guard with a raise path: `any((value is not None for value in (label_value, legal, regulation, source_url)))`.
- Explicit raise expressions: `ValueError(f'{label} official profile SHA256 lineage differs')`, `ValueError(f'{label} official profile lineage differs from envelope')`, `ValueError(f'{label} official source URL must be exact HTTPS')`, `ValueError(f'{label} official-code status is invalid')`, `ValueError(f'{label} resolved official meaning is incomplete')`, `ValueError(f'{label} source archive lineage differs from envelope')`, `ValueError(f'{label} source document lineage differs from envelope')`, `ValueError(f'{label} unknown official meaning must remain null')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none; `_sha256` validates a digest string without computing a hash.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` via `_validate_official_row`.

**Complete source-ordered implementation**

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
    if row["source_document_id"] != source_document_id:
        raise ValueError(f"{label} source document lineage differs from envelope")
    if row["source_archive_sha256"] != source_archive_sha256:
        raise ValueError(f"{label} source archive lineage differs from envelope")
    _sha256(row["source_archive_sha256"], f"{label} source archive SHA256")
    if row["official_code_profile"] != cnig_profile:
        raise ValueError(f"{label} official profile lineage differs from envelope")
    if row["official_code_profile_sha256"] != cnig_profile_sha256:
        raise ValueError(f"{label} official profile SHA256 lineage differs")
    _sha256(row["official_code_profile_sha256"], f"{label} official profile SHA256")
    official_status = row["official_code_status"]
    label_value = _optional_official_string(
        row["official_code_label"], f"{label} official label"
    )
    legal = _optional_official_string(
        row["official_legal_reference"], f"{label} official legal reference"
    )
    regulation = _optional_official_string(
        row["official_regulation_reference"],
        f"{label} official regulation reference",
    )
    source_url = _optional_official_string(
        row["official_code_source_url"], f"{label} official source URL"
    )
    if official_status == "RESOLVED_OFFICIAL":
        if label_value is None or source_url is None:
            raise ValueError(f"{label} resolved official meaning is incomplete")
        parsed_url = urlsplit(source_url)
        if parsed_url.scheme != "https" or not parsed_url.netloc:
            raise ValueError(f"{label} official source URL must be exact HTTPS")
    elif official_status == "UNKNOWN_CODE_PAIR":
        if any(
            value is not None for value in (label_value, legal, regulation, source_url)
        ):
            raise ValueError(f"{label} unknown official meaning must remain null")
    else:
        raise ValueError(f"{label} official-code status is invalid")
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `validate_bess_application_policy_frame`

**Exact signature**

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

Validate the source document/archive and CNIG profile/hash arguments first. Require a DataFrame without duplicate columns, the exact 18-column policy suffix in order, its exact dtypes, and all needed identity/official columns. Each row then passes `_validate_official_row`, the feature-family domain, and two-digit code checks. APPLIED_EXACT_POLICY requires RESOLVED_OFFICIAL and six populated decision fields: allowed status/confidence, positive integral priority, and exact rationale/action/limitations strings. UNRESOLVED_CODE_PAIR requires UNKNOWN_CODE_PAIR and six true-null decision fields. Textual missing-value sentinels are rejected, both scopes must match, all six boundary flags must be the Python value `False`, and policy lineage must equal the supplied expectations.

Empty frames still receive envelope-argument and structural checks, but have no row-level checks. The policy-profile/hash expectations are compared with rows here; their independent validation and compiled-policy authority belong to the upstream caller. This helper does not establish the full factual prefix schema, global IDs, geometry, row-to-policy equality or physical source trust.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(frame, pd.DataFrame)`.
- Guard with a raise path: `frame.columns.duplicated().any()`.
- Guard with a raise path: `tuple(frame.columns[-len(POLICY_COLUMNS):]) != POLICY_COLUMNS`.
- Guard with a raise path: `not required.issubset(frame.columns)`.
- Guard with a raise path: `str(frame[column].dtype) != expected_dtype`.
- Guard with a raise path: `row['feature_family'] not in ALLOWED_FEATURE_FAMILIES`.
- Guard with a raise path: `application_status == 'APPLIED_EXACT_POLICY'`.
- Guard with a raise path: `row['bess_cnig_application_scope'] != APPLICATION_SCOPE`.
- Guard with a raise path: `row['bess_cnig_policy_scope'] != POLICY_SCOPE`.
- Guard with a raise path: `any((row[column] is not False for column in FLAG_COLUMNS))`.
- Guard with a raise path: `not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None`.
- Guard with a raise path: `official_status != 'RESOLVED_OFFICIAL'`.
- Guard with a raise path: `any((_null_value(row[column]) is None for column in DECISION_COLUMNS))`.
- Guard with a raise path: `row['bess_cnig_precheck_status'] not in ALLOWED_PRECHECK_STATUSES`.
- Guard with a raise path: `row['bess_cnig_precheck_confidence'] not in ALLOWED_CONFIDENCES`.
- Guard with a raise path: `isinstance(priority, bool) or not isinstance(priority, Integral) or int(priority) <= 0`.
- Guard with a raise path: `application_status == 'UNRESOLVED_CODE_PAIR'`.
- Guard with a raise path: `isinstance(value, str) and value in NULL_LITERALS`.
- Guard with a raise path: `actual != expected`.
- Guard with a raise path: `official_status != 'UNKNOWN_CODE_PAIR'`.
- Guard with a raise path: `any((_null_value(row[column]) is not None for column in DECISION_COLUMNS))`.
- Explicit raise expressions: `TypeError(f'{label} must be a DataFrame')`, `ValueError(f'{label} application identity schema is incomplete')`, `ValueError(f'{label} application scope is invalid')`, `ValueError(f'{label} application status is invalid')`, `ValueError(f'{label} applied policy row has a missing decision')`, `ValueError(f'{label} boundary flags must be false')`, `ValueError(f'{label} confidence is outside the domain')`, `ValueError(f'{label} contains a literal missing-value replacement')`, `ValueError(f'{label} contains duplicate columns')`, `ValueError(f'{label} feature family is invalid')`, `ValueError(f'{label} official status contradicts its application status')`, `ValueError(f'{label} policy dtype is invalid for {column}')`, `ValueError(f'{label} policy schema is invalid')`, `ValueError(f'{label} policy scope is invalid')`, `ValueError(f'{label} precheck status is outside the domain')`, `ValueError(f'{label} priority must be a positive integer')`, `ValueError(f'{label} unresolved row has an invented decision')`, `ValueError(f'{label} {column} is not an exact two-digit code')`, `ValueError(f'{label} {lineage_label} lineage is invalid')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none; `_sha256` validates a digest string without computing a hash.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` via `validate_bess_application_policy_frame`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_relation_frame` via `validate_bess_application_policy_frame`.

**Complete source-ordered implementation**

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
    """Validate the complete canonical application suffix and every row."""

    _exact_string(source_document_id, f"{label} source document identity")
    _sha256(source_archive_sha256, f"{label} source archive SHA256")
    _exact_string(cnig_profile, f"{label} CNIG profile")
    _sha256(cnig_profile_sha256, f"{label} CNIG profile SHA256")
    if not isinstance(frame, pd.DataFrame):
        raise TypeError(f"{label} must be a DataFrame")
    if frame.columns.duplicated().any():
        raise ValueError(f"{label} contains duplicate columns")
    if tuple(frame.columns[-len(POLICY_COLUMNS) :]) != POLICY_COLUMNS:
        raise ValueError(f"{label} policy schema is invalid")
    for column, expected_dtype in POLICY_SUFFIX_DTYPES.items():
        if str(frame[column].dtype) != expected_dtype:
            raise ValueError(f"{label} policy dtype is invalid for {column}")
    required = {
        "feature_family",
        "type_code_raw",
        "subtype_code_raw",
        "official_code_status",
        "official_code_label",
        "official_legal_reference",
        "official_regulation_reference",
        "official_code_source_url",
        "official_code_profile",
        "official_code_profile_sha256",
        "source_document_id",
        "source_archive_sha256",
        *POLICY_COLUMNS,
    }
    if not required.issubset(frame.columns):
        raise ValueError(f"{label} application identity schema is incomplete")
    for row in frame.to_dict("records"):
        _validate_official_row(
            row,
            label=label,
            source_document_id=source_document_id,
            source_archive_sha256=source_archive_sha256,
            cnig_profile=cnig_profile,
            cnig_profile_sha256=cnig_profile_sha256,
        )
        if row["feature_family"] not in ALLOWED_FEATURE_FAMILIES:
            raise ValueError(f"{label} feature family is invalid")
        for column in ("type_code_raw", "subtype_code_raw"):
            value = row[column]
            if not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None:
                raise ValueError(f"{label} {column} is not an exact two-digit code")
        application_status = row["bess_cnig_policy_application_status"]
        official_status = row["official_code_status"]
        if application_status == "APPLIED_EXACT_POLICY":
            if official_status != "RESOLVED_OFFICIAL":
                raise ValueError(
                    f"{label} official status contradicts its application status"
                )
            if any(_null_value(row[column]) is None for column in DECISION_COLUMNS):
                raise ValueError(f"{label} applied policy row has a missing decision")
            if row["bess_cnig_precheck_status"] not in ALLOWED_PRECHECK_STATUSES:
                raise ValueError(f"{label} precheck status is outside the domain")
            if row["bess_cnig_precheck_confidence"] not in ALLOWED_CONFIDENCES:
                raise ValueError(f"{label} confidence is outside the domain")
            priority = row["bess_cnig_status_priority"]
            if (
                isinstance(priority, bool)
                or not isinstance(priority, Integral)
                or int(priority) <= 0
            ):
                raise ValueError(f"{label} priority must be a positive integer")
            for column in (
                "bess_cnig_rationale",
                "bess_cnig_required_human_action",
                "bess_cnig_limitations",
            ):
                _exact_string(row[column], f"{label} {column}")
        elif application_status == "UNRESOLVED_CODE_PAIR":
            if official_status != "UNKNOWN_CODE_PAIR":
                raise ValueError(
                    f"{label} official status contradicts its application status"
                )
            if any(_null_value(row[column]) is not None for column in DECISION_COLUMNS):
                raise ValueError(f"{label} unresolved row has an invented decision")
        else:
            raise ValueError(f"{label} application status is invalid")
        for column in STRING_POLICY_COLUMNS:
            value = row[column]
            if isinstance(value, str) and value in NULL_LITERALS:
                raise ValueError(
                    f"{label} contains a literal missing-value replacement"
                )
        if row["bess_cnig_application_scope"] != APPLICATION_SCOPE:
            raise ValueError(f"{label} application scope is invalid")
        if row["bess_cnig_policy_scope"] != POLICY_SCOPE:
            raise ValueError(f"{label} policy scope is invalid")
        if any(row[column] is not False for column in FLAG_COLUMNS):
            raise ValueError(f"{label} boundary flags must be false")
        for actual, expected, lineage_label in (
            (row["bess_cnig_policy_profile"], policy_profile, "policy profile"),
            (row["bess_cnig_policy_sha256"], policy_sha256, "policy SHA256"),
            (
                row["bess_cnig_policy_result_sha256"],
                policy_result_sha256,
                "policy result SHA256",
            ),
        ):
            if actual != expected:
                raise ValueError(f"{label} {lineage_label} lineage is invalid")
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_relation_identity_string`

**Exact signature**

```python
def _relation_identity_string(value: object, label: str) -> str:
```

**Purpose**

Require an exact nonempty string and reject the three textual null sentinels. Return the original identifier without normalization; namespace/source equality is a separate caller check.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
exact
```

**Validation and exceptions**

- Guard with a raise path: `exact in NULL_LITERALS`.
- Explicit raise expressions: `ValueError(f'{label} must not be a textual null sentinel')`.

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

- direct call: `src/landscout/common/bess_application_contract.py::_portable_feature_id` via `_relation_identity_string`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` via `_relation_identity_string`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_relation_frame` via `_relation_identity_string`.

**Complete source-ordered implementation**

```python
def _relation_identity_string(value: object, label: str) -> str:
    exact = _exact_string(value, label)
    if exact in NULL_LITERALS:
        raise ValueError(f"{label} must not be a textual null sentinel")
    return exact
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_portable_feature_id`

**Exact signature**

```python
def _portable_feature_id(value: object, label: str) -> str:
```

**Purpose**

Validate the identity string, then reject paths considered absolute by either POSIX or Windows syntax. This is an identifier guard, not the portable Parquet-basename validator: it does not validate every relative path component or access the filesystem. The catalog validator additionally reconstructs the exact GPU namespace.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
feature_id
```

**Validation and exceptions**

- Guard with a raise path: `PurePosixPath(feature_id).is_absolute() or PureWindowsPath(feature_id).is_absolute()`.
- Explicit raise expressions: `ValueError(f'{label} must not be an absolute path')`.

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

- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` via `_portable_feature_id`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_relation_frame` via `_portable_feature_id`.

**Complete source-ordered implementation**

```python
def _portable_feature_id(value: object, label: str) -> str:
    feature_id = _relation_identity_string(value, label)
    if (
        PurePosixPath(feature_id).is_absolute()
        or PureWindowsPath(feature_id).is_absolute()
    ):
        raise ValueError(f"{label} must not be an absolute path")
    return feature_id
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_status_priority_mapping`

**Exact signature**

```python
def _status_priority_mapping(
    frame: pd.DataFrame, label: str
) -> tuple[dict[int, str], dict[str, int]]:
```

**Purpose**

Select APPLIED_EXACT_POLICY rows only, accumulate a set of statuses for each priority and a set of priorities for each status, then reject either direction with more than one member. Return two new mutable dictionaries representing the observed bijection. No applied rows yield two empty dictionaries. This checks consistency of observed rows, not completeness against the configured policy, and assumes scalar rows were already validated.

**Return contract**

- Declared return annotation: `tuple[dict[int, str], dict[str, int]]`.
- Every observed return expression is reproduced without truncation:
```python
({priority: next(iter(statuses)) for priority, statuses in priority_to_statuses.items()}, {status: next(iter(priorities)) for status, priorities in status_to_priorities.items()})
```

**Validation and exceptions**

- Guard with a raise path: `any((len(statuses) != 1 for statuses in priority_to_statuses.values())) or any((len(priorities) != 1 for priorities in status_to_priorities.values()))`.
- Explicit raise expressions: `ValueError(f'{label} status/priority mapping is not one-to-one')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `priority_to_statuses`, `priority_to_statuses.setdefault(priority, set())`, `status_to_priorities`, `status_to_priorities.setdefault(status, set())`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` via `_status_priority_mapping`.
- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_relation_frame` via `_status_priority_mapping`.

**Complete source-ordered implementation**

```python
def _status_priority_mapping(
    frame: pd.DataFrame, label: str
) -> tuple[dict[int, str], dict[str, int]]:
    priority_to_statuses: dict[int, set[str]] = {}
    status_to_priorities: dict[str, set[int]] = {}
    applied = frame[
        frame["bess_cnig_policy_application_status"] == "APPLIED_EXACT_POLICY"
    ]
    for row in applied.to_dict("records"):
        priority = int(row["bess_cnig_status_priority"])
        status = str(row["bess_cnig_precheck_status"])
        priority_to_statuses.setdefault(priority, set()).add(status)
        status_to_priorities.setdefault(status, set()).add(priority)
    if any(len(statuses) != 1 for statuses in priority_to_statuses.values()) or any(
        len(priorities) != 1 for priorities in status_to_priorities.values()
    ):
        raise ValueError(f"{label} status/priority mapping is not one-to-one")
    return (
        {
            priority: next(iter(statuses))
            for priority, statuses in priority_to_statuses.items()
        },
        {
            status: next(iter(priorities))
            for status, priorities in status_to_priorities.items()
        },
    )
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `_feature_metric`

**Exact signature**

```python
def _feature_metric(value: object, expected: float, label: str) -> None:
```

**Purpose**

Require a non-boolean real number, convert to float, and reject non-finite or non-positive values. Compare it with the geometry-derived expectation using the shared tolerance at the larger absolute magnitude. Return `None` on agreement; this helper compares numbers but does not itself measure geometry.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Real)`.
- Guard with a raise path: `not math.isfinite(number) or number <= 0`.
- Guard with a raise path: `abs(number - expected) > technical_overlay_tolerance(max(abs(number), abs(expected)))`.
- Explicit raise expressions: `TypeError(f'{label} must be numeric')`, `ValueError(f'{label} is inconsistent with feature geometry')`, `ValueError(f'{label} must be finite and positive')`.

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

- direct call: `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` via `_feature_metric`.

**Complete source-ordered implementation**

```python
def _feature_metric(value: object, expected: float, label: str) -> None:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{label} must be numeric")
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise ValueError(f"{label} must be finite and positive")
    if abs(number - expected) > technical_overlay_tolerance(
        max(abs(number), abs(expected))
    ):
        raise ValueError(f"{label} is inconsistent with feature geometry")
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `validate_bess_application_feature_catalogs`

**Exact signature**

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

For SURFACE, LINE and POINT in order, validate the exact coded-plus-policy schema and policy rows. Check active geometry/CRS and each row's source CRS against Lambert-93 (row source-CRS equivalence ignores axis order). Require the logical layer to belong to its geometry family, derive PRESCRIPTION/INFORMATION from that layer, and reconstruct `GPU:{document_id}:{logical_layer}:{source_id}` exactly. Require a valid nonempty Shapely geometry of the allowed single/multi family with coordinate dimension exactly two. Recompute area/length from that geometry and compare the stored metric; for points compare the positive integral count with `len(get_parts(geometry))`.

Collect every feature ID, including unreferenced features, reject duplicates across all three catalogs, concatenate the frames only for document-wide status/priority consistency, and return the observed bijection. No disk read, reprojection, geometry repair, GPU reconstruction or relation-to-catalog join occurs here. The input frames are not mutated; temporary lists/concatenated frames are newly allocated.

**Return contract**

- Declared return annotation: `tuple[dict[int, str], dict[str, int]]`.
- Every observed return expression is reproduced without truncation:
```python
_status_priority_mapping(combined, 'feature document-wide')
```

**Validation and exceptions**

- Guard with a raise path: `len(feature_ids) != len(set(feature_ids))`.
- Guard with a raise path: `not required.issubset(frame.columns)`.
- Guard with a raise path: `frame.geometry.name != 'geometry' or frame.crs is None`.
- Guard with a raise path: `not CRS.from_user_input(frame.crs).equals(CRS.from_epsg(2154))`.
- Guard with a raise path: `document_id != source_document_id`.
- Guard with a raise path: `not equivalent_source_crs`.
- Guard with a raise path: `logical_layer not in allowed_layers`.
- Guard with a raise path: `row['feature_family'] != expected_family`.
- Guard with a raise path: `row['geometry_kind'] != kind`.
- Guard with a raise path: `feature_id != expected_id`.
- Guard with a raise path: `not isinstance(geometry, BaseGeometry) or geometry.is_empty or (not geometry.is_valid) or (geometry.geom_type not in geometry_types)`.
- Guard with a raise path: `int(get_coordinate_dimension(geometry)) != 2`.
- Guard with a raise path: `isinstance(count, bool) or not isinstance(count, Integral) or int(count) <= 0 or (int(count) != len(get_parts(geometry)))`.
- Explicit raise expressions: `ValueError('CRS is not EPSG:2154')`, `ValueError('active geometry or CRS is missing')`, `ValueError('planning feature identity must be globally unique')`, `ValueError('point member count is inconsistent with feature geometry')`, `ValueError(f'{label} factual schema is incomplete')`, `ValueError(f'{label} family and logical layer are inconsistent')`, `ValueError(f'{label} geometry is invalid for {kind}')`, `ValueError(f'{label} geometry kind is invalid')`, `ValueError(f'{label} geometry must be canonical 2D')`, `ValueError(f'{label} logical layer is invalid')`, `ValueError(f'{label} must use active geometry and EPSG:2154')`, `ValueError(f'{label} planning feature identity differs from GPU namespace')`, `ValueError(f'{label} source CRS is invalid')`, `ValueError(f'{label} source CRS is not canonical Lambert-93')`, `ValueError(f'{label} source document lineage differs')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: CRS equivalence, Shapely validity/type/dimension checks, area/length measurement and point-part counting; no reprojection or repair.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `applied_frames`, `feature_ids`.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.common.bess_application_contract import (
    APPLICATION_SCOPE,
    FLAG_COLUMNS,
    POLICY_COLUMNS,
    POLICY_SCOPE,
    STRING_POLICY_COLUMNS,
    ApplicationStatus,
    validate_bess_application_feature_catalogs,
    validate_bess_application_relation_frame,
)`.
- direct call: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `validate_bess_application_feature_catalogs`.

**Complete source-ordered implementation**

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
    """Validate all intrinsic feature facts, identities, geometry, and mappings."""

    feature_ids: list[str] = []
    applied_frames: list[pd.DataFrame] = []
    for frame, kind, label in (
        (surface, "SURFACE", "surface features"),
        (line, "LINE", "line features"),
        (point, "POINT", "point features"),
    ):
        geometry_kind = cast(GeometryKind, kind)
        suffix_dtypes = tuple(POLICY_SUFFIX_DTYPES[column] for column in POLICY_COLUMNS)
        validate_canonical_frame_schema(
            frame,
            columns=feature_columns(geometry_kind, POLICY_COLUMNS),
            dtypes=feature_dtypes(geometry_kind, suffix_dtypes, frame),
            label=label,
            geospatial=True,
        )
        validate_bess_application_policy_frame(
            frame,
            label=label,
            policy_profile=policy_profile,
            policy_sha256=policy_sha256,
            policy_result_sha256=policy_result_sha256,
            source_document_id=source_document_id,
            source_archive_sha256=source_archive_sha256,
            cnig_profile=cnig_profile,
            cnig_profile_sha256=cnig_profile_sha256,
        )
        required = {
            "planning_feature_id",
            "source_feature_id",
            "source_document_id",
            "logical_layer",
            "feature_family",
            "geometry_kind",
            "source_crs",
            "geometry",
            _FEATURE_SPECS[kind][2],
        }
        if not required.issubset(frame.columns):
            raise ValueError(f"{label} factual schema is incomplete")
        try:
            if frame.geometry.name != "geometry" or frame.crs is None:
                raise ValueError("active geometry or CRS is missing")
            if not CRS.from_user_input(frame.crs).equals(CRS.from_epsg(2154)):
                raise ValueError("CRS is not EPSG:2154")
        except Exception as error:
            raise ValueError(
                f"{label} must use active geometry and EPSG:2154"
            ) from error
        allowed_layers, geometry_types, metric_column = _FEATURE_SPECS[kind]
        for row in frame.to_dict("records"):
            feature_id = _portable_feature_id(
                row["planning_feature_id"], f"{label} planning feature identity"
            )
            source_id = _relation_identity_string(
                row["source_feature_id"], f"{label} source feature identity"
            )
            document_id = _relation_identity_string(
                row["source_document_id"], f"{label} source document identity"
            )
            if document_id != source_document_id:
                raise ValueError(f"{label} source document lineage differs")
            source_crs = _exact_string(row["source_crs"], f"{label} source CRS")
            try:
                equivalent_source_crs = CRS.from_user_input(source_crs).equals(
                    CRS.from_epsg(2154), ignore_axis_order=True
                )
            except Exception as error:
                raise ValueError(f"{label} source CRS is invalid") from error
            if not equivalent_source_crs:
                raise ValueError(f"{label} source CRS is not canonical Lambert-93")
            logical_layer = row["logical_layer"]
            if logical_layer not in allowed_layers:
                raise ValueError(f"{label} logical layer is invalid")
            expected_family = (
                "PRESCRIPTION"
                if str(logical_layer).startswith("prescription_")
                else "INFORMATION"
            )
            if row["feature_family"] != expected_family:
                raise ValueError(f"{label} family and logical layer are inconsistent")
            if row["geometry_kind"] != kind:
                raise ValueError(f"{label} geometry kind is invalid")
            expected_id = f"GPU:{document_id}:{logical_layer}:{source_id}"
            if feature_id != expected_id:
                raise ValueError(
                    f"{label} planning feature identity differs from GPU namespace"
                )
            geometry = row["geometry"]
            if (
                not isinstance(geometry, BaseGeometry)
                or geometry.is_empty
                or not geometry.is_valid
                or geometry.geom_type not in geometry_types
            ):
                raise ValueError(f"{label} geometry is invalid for {kind}")
            if int(get_coordinate_dimension(geometry)) != 2:
                raise ValueError(f"{label} geometry must be canonical 2D")
            if kind == "SURFACE":
                _feature_metric(row[metric_column], float(geometry.area), metric_column)
            elif kind == "LINE":
                _feature_metric(
                    row[metric_column], float(geometry.length), metric_column
                )
            else:
                count = row[metric_column]
                if (
                    isinstance(count, bool)
                    or not isinstance(count, Integral)
                    or int(count) <= 0
                    or int(count) != len(get_parts(geometry))
                ):
                    raise ValueError(
                        "point member count is inconsistent with feature geometry"
                    )
            feature_ids.append(feature_id)
        applied_frames.append(frame)
    if len(feature_ids) != len(set(feature_ids)):
        raise ValueError("planning feature identity must be globally unique")
    combined = pd.concat(applied_frames, ignore_index=True)
    return _status_priority_mapping(combined, "feature document-wide")
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.

### `validate_bess_application_relation_frame`

**Exact signature**

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

Validate the exact non-geospatial coded-plus-policy schema, then the policy/official row contract. Require nonempty non-sentinel parcel and feature IDs, reject duplicate `(parcel_id, planning_feature_id)` pairs, delegate family-specific metrics/null/count rules to `validate_intrinsic_planning_feature_relations`, and return the observed status/priority bijection. A relation-only frame does not prove that its feature exists in a catalog, that the parcel exists, or that geometry actually intersects; the application/aggregation caller checks its additional upstream relationships.

**Return contract**

- Declared return annotation: `tuple[dict[int, str], dict[str, int]]`.
- Every observed return expression is reproduced without truncation:
```python
_status_priority_mapping(frame, f'{label} document-wide')
```

**Validation and exceptions**

- Guard with a raise path: `not required.issubset(frame.columns)`.
- Guard with a raise path: `frame.duplicated(['parcel_id', 'planning_feature_id']).any()`.
- Explicit raise expressions: `ValueError(f'{label} contains a duplicate parcel/feature relation pair')`, `ValueError(f'{label} relation identity schema is incomplete')`.

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

- import: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.common.bess_application_contract import (
    ALLOWED_CONFIDENCES,
    ALLOWED_PRECHECK_STATUSES,
    NULL_LITERALS,
    POLICY_SCOPE,
    validate_bess_application_relation_frame,
)`.
- import: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.common.bess_application_contract import (
    APPLICATION_SCOPE,
    FLAG_COLUMNS,
    POLICY_COLUMNS,
    POLICY_SCOPE,
    STRING_POLICY_COLUMNS,
    ApplicationStatus,
    validate_bess_application_feature_catalogs,
    validate_bess_application_relation_frame,
)`.
- direct call: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_application_relations` via `validate_bess_application_relation_frame`.
- direct call: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_relation_rows` via `validate_bess_application_relation_frame`.

**Complete source-ordered implementation**

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
    """Validate canonical application rows and the complete relation identity."""

    suffix_dtypes = tuple(POLICY_SUFFIX_DTYPES[column] for column in POLICY_COLUMNS)
    validate_canonical_frame_schema(
        frame,
        columns=relation_columns(POLICY_COLUMNS),
        dtypes=relation_dtypes(suffix_dtypes),
        label=label,
        geospatial=False,
    )
    validate_bess_application_policy_frame(
        frame,
        label=label,
        policy_profile=policy_profile,
        policy_sha256=policy_sha256,
        policy_result_sha256=policy_result_sha256,
        source_document_id=source_document_id,
        source_archive_sha256=source_archive_sha256,
        cnig_profile=cnig_profile,
        cnig_profile_sha256=cnig_profile_sha256,
    )
    required = {"parcel_id", "planning_feature_id", "relation_type"}
    if not required.issubset(frame.columns):
        raise ValueError(f"{label} relation identity schema is incomplete")
    for row in frame.to_dict("records"):
        _relation_identity_string(row["parcel_id"], f"{label} parcel identity")
        feature_id = _portable_feature_id(
            row["planning_feature_id"], f"{label} Feature ID identity"
        )
        assert feature_id
    if frame.duplicated(["parcel_id", "planning_feature_id"]).any():
        raise ValueError(f"{label} contains a duplicate parcel/feature relation pair")
    validate_intrinsic_planning_feature_relations(frame)
    return _status_priority_mapping(frame, f"{label} document-wide")
```

**Business boundary**

- This internal contract or utility does not make a parcel decision or independently establish source authority beyond its explicit checks.


## 7. Data contracts

The exact ordered `POLICY_COLUMNS` suffix has 18 fields. `DECISION_COLUMNS` selects the six decision fields; `FLAG_COLUMNS` selects six mandatory-false boundary flags; `STRING_POLICY_COLUMNS` is the remaining string-typed subset. These are DataFrame schemas, not fields of a frozen model. String dtype identity is checked by `str(dtype) == "str"`, priority by `"Int64"`, and flags by `"bool"`.

| Exact field | Runtime column contract and meaning |
|---|---|
| `bess_cnig_policy_application_status` | Non-null APPLIED_EXACT_POLICY or UNRESOLVED_CODE_PAIR; must agree with official-code resolution. |
| `bess_cnig_precheck_status` | Applied: one allowed precheck status; unresolved: true null. |
| `bess_cnig_precheck_confidence` | Applied: HIGH, MEDIUM or LOW; unresolved: true null. |
| `bess_cnig_status_priority` | Applied: positive non-boolean integer; unresolved: nullable-Int64 null. Observed status/priority must be one-to-one. |
| `bess_cnig_rationale` | Applied: exact nonempty rationale string; unresolved: true null. |
| `bess_cnig_required_human_action` | Applied: exact nonempty action string; unresolved: true null. |
| `bess_cnig_limitations` | Applied: exact nonempty limitation string; unresolved: true null. |
| `bess_cnig_application_scope` | Exactly FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY. |
| `bess_cnig_policy_scope` | Exactly OFFICIAL_CNIG_CODE_MEANING_ONLY. |
| `bess_cnig_local_feature_text_interpreted` | Boolean false: the application does not interpret local feature text. |
| `bess_cnig_local_regulation_content_interpreted` | Boolean false: local regulation content is not interpreted here. |
| `bess_cnig_legal_conclusion_produced` | Boolean false: no legal conclusion is produced. |
| `bess_cnig_parcel_status_aggregated` | Boolean false: this is not the later parcel-aggregation result. |
| `bess_cnig_parcel_rejection_performed` | Boolean false: no parcel rejection. |
| `bess_cnig_score_calculated` | Boolean false: no score. |
| `bess_cnig_policy_profile` | String equal to the caller's policy-profile expectation. |
| `bess_cnig_policy_sha256` | String equal to the caller's policy-config digest expectation; not independently recomputed here. |
| `bess_cnig_policy_result_sha256` | String equal to the caller's compiled-result digest expectation; not independently recomputed here. |

Allowed applied precheck statuses are LIKELY_MATERIAL_CONSTRAINT, MATERIAL_REVIEW_REQUIRED, DESIGN_REVIEW_REQUIRED, CONTEXT_REVIEW_REQUIRED and UNKNOWN. They are preliminary policy states, not permissions or prohibitions.

The policy-row validator additionally consumes the source document/archive, feature family and type/subtype codes, and the seven official-code fields declared by `planning_feature_schema`. Optional official legal/regulation references may be null on a resolved row; an unresolved official code requires label, legal reference, regulation reference and source URL all to be true null. Exact upstream dictionary meaning is validated elsewhere.

`_FEATURE_SPECS` couples each family to its two permitted logical layers, allowed single/multi geometry types and metric column: surface → Polygon/MultiPolygon/area; line → LineString/MultiLineString/length; point → Point/MultiPoint/member count. Neither a geometry-family label nor a textual digest alone is physical proof.

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
