# `src/landscout/stages/resolve_planning_feature_codes.py`

## File identity

- Repository path: `src/landscout/stages/resolve_planning_feature_codes.py`
- File type: Python source
- Primary responsibility: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.
- Layer / domain: `stage` / `planning`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `57907fd137407beeceaf0dee2cd1419a7746945032577782bcfa209711d5c2ae`

## 1. Purpose

Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import math` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `import unicodedata` — required by the implementation paths and symbols documented below.
- `from collections.abc import Mapping, Sequence` — required by the implementation paths and symbols documented below.
- `from dataclasses import asdict, dataclass, replace` — required by the implementation paths and symbols documented below.
- `from datetime import date, datetime` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from numbers import Integral, Real` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Literal, cast` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.
- `from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, model_validator` — required by the implementation paths and symbols documented below.
- `from shapely import to_wkb` — required by the implementation paths and symbols documented below.
- `from shapely.geometry.base import BaseGeometry` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.frame_integrity import deterministic_frame_schema_signature` — required by the implementation paths and symbols documented below.
- `from landscout.common.planning_feature_schema import ( OFFICIAL_CODE_COLUMNS, GeometryKind, feature_columns, feature_dtypes, relation_columns, relation_dtypes, validate_canonical_frame_schema, )` — required by the implementation paths and symbols documented below.
- `from landscout.sources.gpu_fr import GpuInspectedLayer, GpuPlanningDocument` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_planning_features import ( PlanningFeatureInputValidation, validate_normalized_planning_feature_inputs, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `PROFILE_SCHEMA_VERSION` | `2` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RESULT_HASH_SCHEMA_VERSION` | `5` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `STANDARD_MODEL` | `"CNIG PLU v2017"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `OFFICIAL_TEXT_NORMALIZATION` | `"GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PRESCRIPTION_OFFICIAL_SOURCE_URL` | `"https://www.geoportail-urbanisme.gouv.fr/standard/" "cnig_PLU_2017/codes/PrescriptionUrbaType"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `INFORMATION_OFFICIAL_SOURCE_URL` | `"https://www.geoportail-urbanisme.gouv.fr/standard/" "cnig_PLU_2017/codes/InformationUrbaType"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CODE_DICTIONARY_COLUMNS` | `( "feature_family", "type_code", "subtype_code", "official_label", "legal_reference", "regulation_or_annex_reference", "official_source_url", "profile", "profile_sha256", "standard_model", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CODE_DICTIONARY_DTYPES` | `tuple("str" for _ in CODE_DICTIONARY_COLUMNS)` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CODE_DICTIONARY_SCHEMA_SIGNATURE` | `{ "columns": list(CODE_DICTIONARY_COLUMNS), "dtypes": list(CODE_DICTIONARY_DTYPES), "index_class": "pandas.Index", "index_names": [None], "index_level_dtypes": ["int64"], }` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_CODE_PATTERN` | `re.compile(r"[0-9]{2}")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_SHA_PATTERN` | `re.compile(r"[0-9a-f]{64}")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_NULL_REFERENCE_LITERALS` | `frozenset({"None", "nan", "<NA>"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `PlanningFeatureCodeError`

**Purpose:** Raised when official code resolution integrity cannot be proven.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `_StrictModel`

**Purpose:** Groups the `StrictModel` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid", frozen=True)`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `OfficialSourceUrls`

**Purpose:** Groups the `OfficialSourceUrls` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `_StrictModel`.

**Model form and mutability:** class inheriting from `_StrictModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `prescription` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `information` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_urls` — `def _validate_urls(self) -> OfficialSourceUrls:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `CnigFeatureCodeRecord`

**Purpose:** Groups the `CnigFeatureCodeRecord` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `_StrictModel`.

**Model form and mutability:** class inheriting from `_StrictModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `feature_family` | `FeatureFamily` | `required` | `FeatureFamily` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `type_code` | `StrictStr` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `subtype_code` | `StrictStr` | `required` | Exact configured or source code whose vocabulary/format is enforced by the owning validator. |
| `official_label` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `legal_reference` | `StrictStr | None` | `required` | `StrictStr | None` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `regulation_or_annex_reference` | `StrictStr | None` | `required` | `StrictStr | None` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `official_source_url` | `StrictStr` | `required` | Exact source or evidence URL; host/path/HTTPS restrictions are enforced by configuration or source validators. |

**Validators and methods:**

- `_validate_record` — `def _validate_record(self) -> CnigFeatureCodeRecord:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `CnigFeatureCodeProfile`

**Purpose:** Strict offline snapshot of official CNIG feature code records.

**Inheritance:** `_StrictModel`.

**Model form and mutability:** class inheriting from `_StrictModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `StrictInt` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `profile` | `StrictStr` | `Field(min_length=1)` | `StrictStr` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `standard_model` | `Literal['CNIG PLU v2017']` | `required` | `Literal['CNIG PLU v2017']` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `official_text_normalization` | `Literal['GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1']` | `required` | `Literal['GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1']` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `official_sources` | `OfficialSourceUrls` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `retrieval_date` | `date` | `required` | `date` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `canonical_records_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `records` | `tuple[CnigFeatureCodeRecord, ...]` | `Field(min_length=1)` | `tuple[CnigFeatureCodeRecord, ...]` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_profile` — `def _validate_profile(self) -> CnigFeatureCodeProfile:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `_UniqueKeyLoader`

**Purpose:** Groups the `UniqueKeyLoader` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `yaml.SafeLoader`.

**Model form and mutability:** class inheriting from `yaml.SafeLoader`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `PlanningFeatureCodeResult`

**Purpose:** Immutable envelope around exact official code resolution outputs.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `result_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `profile_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `profile` | `str` | `required` | `str` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `standard_model` | `str` | `required` | `str` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `profile_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `source_archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `planning_document_context_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `parcel_identity_input_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `normalized_catalogs_input_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `normalized_relations_input_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `gpu_related_source_files_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `expected_relations_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `code_dictionary_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `surface_features_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `line_features_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `point_features_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `relations_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `code_dictionary` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/resolve_planning_feature_codes.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `surface_features` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `line_features` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `point_features` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `relations` | `pd.DataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |

**Validators and methods:**

- None.

## 6. Functions and methods

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

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `ValueError(f'{label} must be a non-empty exact string')`.
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

- `src/landscout/stages/resolve_planning_feature_codes.py` — `CnigFeatureCodeProfile._validate_profile`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_strict_string`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_official_text`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_official_text`

**Signature**

```python
def _canonical_official_text(value: str) -> str:
```

**Purpose**

Implements canonical official text according to the exact implementation and guards in this file.

**Inputs**

- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `' '.join(unicodedata.normalize('NFC', value).split())`.

**Algorithm**

1. Returns `' '.join(unicodedata.normalize('NFC', value).split())`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `' '.join`, `unicodedata.normalize`, `unicodedata.normalize('NFC', value).split`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_official_text`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_official_text`

**Signature**

```python
def _validate_official_text(value: object, label: str) -> str:
```

**Purpose**

Validates and rejects malformed official text according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `text`.

**Algorithm**

1. Computes `text` from `_exact_string(value, label)`.
2. Checks `text != _canonical_official_text(text)`. When true: Raises `ValueError(f'{label} must already use canonical {OFFICIAL_TEXT_NORMALIZATION} text')`.
3. Returns `text`.

**Validation and invariants**

- Rejects or diverts the path when `text != _canonical_official_text(text)` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_canonical_official_text`, `_exact_string`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `CnigFeatureCodeRecord._validate_record`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_code_dictionary`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_nullable_official_value`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_optional_official_text`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_optional_official_text`

**Signature**

```python
def _validate_optional_official_text(value: object, label: str) -> str | None:
```

**Purpose**

Validates and rejects malformed optional official text according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str | None`. Observed return expression(s): `_validate_official_text(value, label)`; `None`.

**Algorithm**

1. Checks `value is None`. When true: Returns `None`.
2. Returns `_validate_official_text(value, label)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_validate_official_text`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `CnigFeatureCodeRecord._validate_record`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `OfficialSourceUrls._validate_urls`

**Signature**

```python
def _validate_urls(self) -> OfficialSourceUrls:
```

**Purpose**

Validates and rejects malformed urls according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `OfficialSourceUrls`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `self.prescription != PRESCRIPTION_OFFICIAL_SOURCE_URL`. When true: Raises `ValueError('prescription source URL is not the exact official GPU host endpoint')`.
2. Checks `self.information != INFORMATION_OFFICIAL_SOURCE_URL`. When true: Raises `ValueError('information source URL is not the exact official GPU host endpoint')`.
3. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `self.prescription != PRESCRIPTION_OFFICIAL_SOURCE_URL` is true.
- Rejects or diverts the path when `self.information != INFORMATION_OFFICIAL_SOURCE_URL` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `model_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `CnigFeatureCodeRecord._validate_record`

**Signature**

```python
def _validate_record(self) -> CnigFeatureCodeRecord:
```

**Purpose**

Validates and rejects malformed record according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CnigFeatureCodeRecord`. Observed return expression(s): `self`.

**Algorithm**

1. Iterates `(code, label)` over `((self.type_code, 'type code'), (self.subtype_code, 'subtype code'))`. For each value: Checks `_CODE_PATTERN.fullmatch(code) is None`. When true: Raises `ValueError(f'{label} must contain exactly two digits')`.
2. Calls `_validate_official_text(self.official_label, 'official label')` for its validation or side effect.
3. Calls `_validate_optional_official_text(self.legal_reference, 'legal reference')` for its validation or side effect.
4. Calls `_validate_optional_official_text(self.regulation_or_annex_reference, 'regulation or annex reference')` for its validation or side effect.
5. Computes `expected_url` from `PRESCRIPTION_OFFICIAL_SOURCE_URL if self.feature_family == 'PRESCRIPTION' else INFORMATION_OFFICIAL_SOURCE_URL`.
6. Checks `self.official_source_url != expected_url`. When true: Raises `ValueError('record source URL is not the exact family endpoint')`.
7. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `self.official_source_url != expected_url` is true.
- Rejects or diverts the path when `_CODE_PATTERN.fullmatch(code) is None` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_CODE_PATTERN.fullmatch`, `_validate_official_text`, `_validate_optional_official_text`, `model_validator`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_record_payload`

**Signature**

```python
def _record_payload(record: CnigFeatureCodeRecord) -> dict[str, object]:
```

**Purpose**

Implements record payload according to the exact implementation and guards in this file.

**Inputs**

- `record` (`CnigFeatureCodeRecord`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'feature_family': record.feature_family, 'type_code': record.type_code, 'subtype_code': record.subtype_code, 'official_label': record.official_label, 'legal_reference': record.legal_reference, 'regulation_or_annex_reference': record.regulation_or_annex_reference, 'official_source_url': record.official_source_url}`.

**Algorithm**

1. Returns `{'feature_family': record.feature_family, 'type_code': record.type_code, 'subtype_code': record.subtype_code, 'official_label': record.official_label, 'legal_reference': record.legal_reference, 'regulation_or_annex_reference': record.regulation_or_annex_reference, 'official_source_url': record.official_source_url}`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_dictionary`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_records_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_json_sha256`

**Signature**

```python
def _canonical_json_sha256(value: object) -> str:
```

**Purpose**

Implements canonical json sha256 according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `sha256(encoded).hexdigest()`.

**Algorithm**

1. Runs guarded operation: Computes `encoded` from `json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')`. Handles `Exception`.
2. Returns `sha256(encoded).hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `json.dumps`, `json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode`, `sha256`, `sha256(encoded).hexdigest`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_complete_sha256`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_frame_sha256`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_normalized_catalogs_input_sha256`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_planning_document_context_sha256`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_profile_sha256`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_records_sha256`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_source_frame_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_records_sha256`

**Signature**

```python
def _records_sha256(records: Sequence[CnigFeatureCodeRecord]) -> str:
```

**Purpose**

Implements records sha256 according to the exact implementation and guards in this file.

**Inputs**

- `records` (`Sequence[CnigFeatureCodeRecord]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256([_record_payload(record) for record in records])`.

**Algorithm**

1. Returns `_canonical_json_sha256([_record_payload(record) for record in records])`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_json_sha256`, `_record_payload`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `CnigFeatureCodeProfile._validate_profile`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `CnigFeatureCodeProfile._validate_profile`

**Signature**

```python
def _validate_profile(self) -> CnigFeatureCodeProfile:
```

**Purpose**

Validates and rejects malformed profile according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CnigFeatureCodeProfile`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `self.schema_version != PROFILE_SCHEMA_VERSION`. When true: Raises `ValueError(f'unsupported CNIG feature-code profile schema: {self.schema_version}')`.
2. Calls `_exact_string(self.profile, 'code profile')` for its validation or side effect.
3. Checks `_SHA_PATTERN.fullmatch(self.canonical_records_sha256) is None`. When true: Raises `ValueError('canonical records SHA256 is invalid')`.
4. Computes `keys` from `[(record.feature_family, record.type_code, record.subtype_code) for record in self.records]`.
5. Checks `len(set(keys)) != len(keys)`. When true: Raises `ValueError('configured CNIG code pairs contain a duplicate')`.
6. Checks `keys != sorted(keys)`. When true: Raises `ValueError('configured CNIG records must use deterministic order')`.
7. Checks `_records_sha256(self.records) != self.canonical_records_sha256`. When true: Raises `ValueError('canonical records SHA256 differs from configured records')`.
8. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `self.schema_version != PROFILE_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `_SHA_PATTERN.fullmatch(self.canonical_records_sha256) is None` is true.
- Rejects or diverts the path when `len(set(keys)) != len(keys)` is true.
- Rejects or diverts the path when `keys != sorted(keys)` is true.
- Rejects or diverts the path when `_records_sha256(self.records) != self.canonical_records_sha256` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_SHA_PATTERN.fullmatch`, `_exact_string`, `_records_sha256`, `len`, `model_validator`, `set`, `sorted`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_construct_unique_mapping`

**Signature**

```python
def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
```

**Purpose**

Implements construct unique mapping according to the exact implementation and guards in this file.

**Inputs**

- `loader` (`yaml.SafeLoader`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `node` (`yaml.MappingNode`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `deep` (`bool`; optional/default `False`) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[object, object]`. Observed return expression(s): `result`.

**Algorithm**

1. Defines `result` with annotation `dict[object, object]` from `{}`.
2. Iterates `(key_node, value_node)` over `node.value`. For each value: Computes `key` from `loader.construct_object(key_node, deep=deep)`. Checks `key in result`. When true: Raises `PlanningFeatureCodeError(f'Duplicate YAML code-profile key: {key!r}')`. Computes `result[key]` from `loader.construct_object(value_node, deep=deep)`.
3. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `key in result` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `loader.construct_object`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_cnig_feature_code_profile`

**Signature**

```python
def load_cnig_feature_code_profile(path: str | Path) -> CnigFeatureCodeProfile:
```

**Purpose**

Load a strict offline CNIG feature-code profile.

**Inputs**

- `path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CnigFeatureCodeProfile`. Observed return expression(s): `CnigFeatureCodeProfile.model_validate(payload)`.

**Algorithm**

1. Runs guarded operation: Computes `payload` from `yaml.load(Path(path).read_text(encoding='utf-8'), Loader=_UniqueKeyLoader)`. Checks `not isinstance(payload, Mapping)`. When true: Raises `PlanningFeatureCodeError('CNIG feature-code profile must be a mapping')`. Returns `CnigFeatureCodeProfile.model_validate(payload)`. Handles `PlanningFeatureCodeError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(payload, Mapping)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `Path(path).read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CnigFeatureCodeProfile.model_validate`, `Path`, `Path(path).read_text`, `PlanningFeatureCodeError`, `isinstance`, `yaml.load`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_resolved_profile`
- `tests/unit/test_bess_planning_feature_policy.py` — `_checked_in_policy_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_duplicate_yaml_key_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_yaml_snapshot_loads_strictly`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs`
- `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_yaml_key_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_yaml_snapshot_loads_strictly`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_resolved_profile`

**Signature**

```python
def _resolved_profile(
    profile: CnigFeatureCodeProfile | str | Path,
) -> CnigFeatureCodeProfile:
```

**Purpose**

Implements resolved profile according to the exact implementation and guards in this file.

**Inputs**

- `profile` (`CnigFeatureCodeProfile | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `CnigFeatureCodeProfile`. Observed return expression(s): `load_cnig_feature_code_profile(profile)`; `CnigFeatureCodeProfile.model_validate(payload)`.

**Algorithm**

1. Checks `not isinstance(profile, CnigFeatureCodeProfile)`. When true: Returns `load_cnig_feature_code_profile(profile)`.
2. Runs guarded operation: Computes `payload` from `profile.model_dump(mode='python', warnings='error')`. Returns `CnigFeatureCodeProfile.model_validate(payload)`. Handles `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_cnig_feature_code_profile`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `CnigFeatureCodeProfile.model_validate`, `PlanningFeatureCodeError`, `isinstance`, `load_cnig_feature_code_profile`, `profile.model_dump`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `resolve_planning_feature_codes`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `validate_planning_feature_code_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_profile_sha256`

**Signature**

```python
def _profile_sha256(profile: CnigFeatureCodeProfile) -> str:
```

**Purpose**

Profiles sha256 according to the exact implementation and guards in this file.

**Inputs**

- `profile` (`CnigFeatureCodeProfile`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256(profile.model_dump(mode='json'))`.

**Algorithm**

1. Returns `_canonical_json_sha256(profile.model_dump(mode='json'))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_json_sha256`, `profile.model_dump`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_string`

**Signature**

```python
def _strict_string(value: object, label: str) -> str:
```

**Purpose**

Implements strict string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_exact_string(value, label)`.

**Algorithm**

1. Runs guarded operation: Returns `_exact_string(value, label)`. Handles `ValueError`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_exact_string`, `str`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_coded_relations`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_inspected_layer_payload`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_planning_document_context_sha256`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_planning_standard`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_planning_standard`

**Signature**

```python
def _planning_standard(document: GpuPlanningDocument) -> str:
```

**Purpose**

Implements planning standard according to the exact implementation and guards in this file.

**Inputs**

- `document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_strict_string(distinct[0], 'planning document standard')`.

**Algorithm**

1. Checks `not isinstance(document, GpuPlanningDocument)`. When true: Raises `PlanningFeatureCodeError('planning_document must be a GpuPlanningDocument')`.
2. Computes `metadata` from `document.extraction.archive.document`.
3. Computes `models` from `list(document.extraction.standard_models)`.
4. Checks `metadata.standard_model is not None`. When true: Calls `models.append(metadata.standard_model)` for its validation or side effect.
5. Computes `distinct` from `tuple(dict.fromkeys(models))`.
6. Checks `len(distinct) != 1`. When true: Raises `PlanningFeatureCodeError('Planning document standard lineage is ambiguous')`.
7. Returns `_strict_string(distinct[0], 'planning document standard')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(document, GpuPlanningDocument)` is true.
- Rejects or diverts the path when `len(distinct) != 1` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_strict_string`, `dict.fromkeys`, `isinstance`, `len`, `list`, `models.append`, `tuple`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_build_result`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `resolve_planning_feature_codes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_code_series`

**Signature**

```python
def _validated_code_series(series: pd.Series, label: str) -> None:
```

**Purpose**

Validates and returns canonical code series according to the exact implementation and guards in this file.

**Inputs**

- `series` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Iterates `value` over `series.tolist()`. For each value: Checks `not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None`. When true: Raises `PlanningFeatureCodeError(f'{label} must contain exact two-character digit strings')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_CODE_PATTERN.fullmatch`, `isinstance`, `series.tolist`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_catalog_document_lineage`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_is_true_null`

**Signature**

```python
def _is_true_null(value: object) -> bool:
```

**Purpose**

Returns whether `true null` satisfies the exact predicates and branches listed below.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `isinstance(missing, (bool, np.bool_)) and bool(missing)`; `True`; `False`.

**Algorithm**

1. Checks `value is None or value is pd.NA`. When true: Returns `True`.
2. Runs guarded operation: Computes `missing` from `pd.isna(value)`. Handles `(TypeError, ValueError)`.
3. Returns `isinstance(missing, (bool, np.bool_)) and bool(missing)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `bool`, `isinstance`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_null_safe_equal`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_coded_meaning_rows`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_nullable_official_value`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_null_safe_equal`

**Signature**

```python
def _null_safe_equal(left: object, right: object) -> bool:
```

**Purpose**

Implements null safe equal according to the exact implementation and guards in this file.

**Inputs**

- `left` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `right` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `type(left) is type(right) and left == right`; `left_null and right_null`.

**Algorithm**

1. Computes `left_null` from `_is_true_null(left)`.
2. Computes `right_null` from `_is_true_null(right)`.
3. Checks `left_null or right_null`. When true: Returns `left_null and right_null`.
4. Returns `type(left) is type(right) and left == right`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_is_true_null`, `type`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_coded_meaning_rows`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_nullable_official_value`

**Signature**

```python
def _validate_nullable_official_value(value: object, label: str) -> None:
```

**Purpose**

Validates and rejects malformed nullable official value according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. Observed return expression(s): `None`.

**Algorithm**

1. Checks `_is_true_null(value)`. When true: Returns `None`.
2. Checks `isinstance(value, str) and value in _NULL_REFERENCE_LITERALS`. When true: Raises `PlanningFeatureCodeError(f'{label} contains a literal null replacement')`.
3. Runs guarded operation: Calls `_validate_official_text(value, label)` for its validation or side effect. Handles `ValueError`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, str) and value in _NULL_REFERENCE_LITERALS` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_is_true_null`, `_validate_official_text`, `isinstance`, `str`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_code_dictionary`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_code_dictionary`

**Signature**

```python
def _validate_code_dictionary(
    result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

**Purpose**

Validates and rejects malformed code dictionary according to the exact implementation and guards in this file.

**Inputs**

- `result` (`PlanningFeatureCodeResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[tuple[str, str, str], dict[str, object]]`. Observed return expression(s): `records`.

**Algorithm**

1. Computes `frame` from `result.code_dictionary`.
2. Checks `type(frame) is not pd.DataFrame`. When true: Raises `PlanningFeatureCodeError('code dictionary must be a non-geospatial DataFrame')`.
3. Checks `frame.columns.duplicated().any() or deterministic_frame_schema_signature(frame) != CODE_DICTIONARY_SCHEMA_SIGNATURE`. When true: Raises `PlanningFeatureCodeError('code dictionary canonical schema is invalid')`.
4. Checks `frame.empty`. When true: Raises `PlanningFeatureCodeError('code dictionary must contain at least one official code record')`.
5. Defines `records` with annotation `dict[tuple[str, str, str], dict[str, object]]` from `{}`.
6. Defines `ordered_keys` with annotation `list[tuple[str, str, str]]` from `[]`.
7. Iterates `(position, row)` over `enumerate(frame.to_dict('records'))`. For each value: Computes `family` from `row['feature_family']`. Checks `family not in {'PRESCRIPTION', 'INFORMATION'}`. When true: Raises `PlanningFeatureCodeError(f'code dictionary row {position} feature family is invalid')`. Iterates `field` over `('type_code', 'subtype_code')`. For each value: Computes `value` from `row[field]`. Checks `not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None`. When true: Raises `PlanningFeatureCodeError(f'code dictionary row {position} {field} is invalid')`. Executes 10 additional source-ordered statement(s).
8. Checks `ordered_keys != sorted(ordered_keys)`. When true: Raises `PlanningFeatureCodeError('code dictionary pair order is not canonical')`.
9. Returns `records`.

**Validation and invariants**

- Rejects or diverts the path when `type(frame) is not pd.DataFrame` is true.
- Rejects or diverts the path when `frame.columns.duplicated().any() or deterministic_frame_schema_signature(frame) != CODE_DICTIONARY_SCHEMA_SIGNATURE` is true.
- Rejects or diverts the path when `frame.empty` is true.
- Rejects or diverts the path when `ordered_keys != sorted(ordered_keys)` is true.
- Rejects or diverts the path when `family not in {'PRESCRIPTION', 'INFORMATION'}` is true.
- Rejects or diverts the path when `key in records` is true.
- Rejects or diverts the path when `row['official_source_url'] != expected_url` is true.
- Rejects or diverts the path when `row['profile'] != result.profile or row['profile_sha256'] != result.profile_sha256 or row['standard_model'] != result.standard_model` is true.
- Rejects or diverts the path when `not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_CODE_PATTERN.fullmatch`, `_validate_nullable_official_value`, `_validate_official_text`, `deterministic_frame_schema_signature`, `enumerate`, `frame.columns.duplicated`, `frame.columns.duplicated().any`, `frame.to_dict`, `isinstance`, `ordered_keys.append`, `sorted`, `str`, `type`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_coded_meaning_rows`

**Signature**

```python
def _validate_coded_meaning_rows(
    result: PlanningFeatureCodeResult,
    dictionary: Mapping[tuple[str, str, str], Mapping[str, object]],
) -> None:
```

**Purpose**

Validates and rejects malformed coded meaning rows according to the exact implementation and guards in this file.

**Inputs**

- `result` (`PlanningFeatureCodeResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `dictionary` (`Mapping[tuple[str, str, str], Mapping[str, object]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `catalogs` from `(result.surface_features, result.line_features, result.point_features)`.
2. Defines `features` with annotation `dict[str, dict[str, object]]` from `{}`.
3. Iterates `frame` over `catalogs`. For each value: Iterates `(position, row)` over `enumerate(frame.to_dict('records'))`. For each value: Computes `family` from `row['feature_family']`. Computes `type_code` from `row['type_code_raw']`. Computes `subtype_code` from `row['subtype_code_raw']`. Executes 12 additional source-ordered statement(s).
4. Computes `compared_fields` from `('feature_family', 'type_code_raw', 'subtype_code_raw', *OFFICIAL_CODE_COLUMNS)`.
5. Iterates `row` over `result.relations.to_dict('records')`. For each value: Computes `identifier` from `row['planning_feature_id']`. Computes `feature` from `features.get(identifier)`. Checks `feature is None`. When true: Raises `PlanningFeatureCodeError('coded relation references an unknown feature ID')`. Executes 1 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `feature is None` is true.
- Rejects or diverts the path when `any((not _null_safe_equal(row[field], feature[field]) for field in compared_fields))` is true.
- Rejects or diverts the path when `family not in {'PRESCRIPTION', 'INFORMATION'}` is true.
- Rejects or diverts the path when `row['official_code_profile'] != result.profile or row['official_code_profile_sha256'] != result.profile_sha256` is true.
- Rejects or diverts the path when `status == 'RESOLVED_OFFICIAL'` is true.
- Rejects or diverts the path when `not isinstance(identifier, str) or not identifier` is true.
- Rejects or diverts the path when `identifier in features` is true.
- Rejects or diverts the path when `not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None` is true.
- Rejects or diverts the path when `record is None or any((not _null_safe_equal(row[field], record[dictionary_field]) for field, dictionary_field in meaning_fields))` is true.
- Rejects or diverts the path when `status == 'UNKNOWN_CODE_PAIR'` is true.
- Rejects or diverts the path when `record is not None or any((not _is_true_null(row[field]) for field, _ in meaning_fields))` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_CODE_PATTERN.fullmatch`, `_is_true_null`, `_null_safe_equal`, `any`, `dictionary.get`, `enumerate`, `features.get`, `frame.to_dict`, `isinstance`, `result.relations.to_dict`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_catalog_document_lineage`

**Signature**

```python
def _validate_catalog_document_lineage(
    frame: gpd.GeoDataFrame,
    label: str,
    document: GpuPlanningDocument,
    standard_model: str,
) -> gpd.GeoDataFrame:
```

**Purpose**

Validates and rejects malformed catalog document lineage according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `standard_model` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame.copy(deep=True)`.

**Algorithm**

1. Calls `_validated_code_series(frame['type_code_raw'], f'{label} type code')` for its validation or side effect.
2. Calls `_validated_code_series(frame['subtype_code_raw'], f'{label} subtype code')` for its validation or side effect.
3. Computes `metadata` from `document.extraction.archive.document`.
4. Checks `not frame['source_document_id'].eq(metadata.document_id).all()`. When true: Raises `PlanningFeatureCodeError(f'{label} document lineage differs')`.
5. Checks `not frame['source_archive_sha256'].eq(document.extraction.archive.sha256).all()`. When true: Raises `PlanningFeatureCodeError(f'{label} archive lineage differs')`.
6. Checks `not frame['source_standard_model'].eq(standard_model).all()`. When true: Raises `PlanningFeatureCodeError(f'{label} source standard lineage differs')`.
7. Returns `frame.copy(deep=True)`.

**Validation and invariants**

- Rejects or diverts the path when `not frame['source_document_id'].eq(metadata.document_id).all()` is true.
- Rejects or diverts the path when `not frame['source_archive_sha256'].eq(document.extraction.archive.sha256).all()` is true.
- Rejects or diverts the path when `not frame['source_standard_model'].eq(standard_model).all()` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningFeatureCodeError`, `_validated_code_series`, `frame.copy`, `frame['source_archive_sha256'].eq`, `frame['source_archive_sha256'].eq(document.extraction.archive.sha256).all`, `frame['source_document_id'].eq`, `frame['source_document_id'].eq(metadata.document_id).all`, `frame['source_standard_model'].eq`, `frame['source_standard_model'].eq(standard_model).all`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_dictionary`

**Signature**

```python
def _dictionary(
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> pd.DataFrame:
```

**Purpose**

Implements dictionary according to the exact implementation and guards in this file.

**Inputs**

- `profile` (`CnigFeatureCodeProfile`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `profile_hash` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `rows` from `[{**_record_payload(record), 'profile': profile.profile, 'profile_sha256': profile_hash, 'standard_model': profile.standard_model} for record in profile.records]`.
2. Computes `output` from `pd.DataFrame(rows, columns=CODE_DICTIONARY_COLUMNS)`.
3. Iterates `column` over `CODE_DICTIONARY_COLUMNS`. For each value: Computes `output[column]` from `pd.array(output[column].tolist(), dtype='str')`.
4. Computes `output.index` from `pd.Index(np.arange(len(output), dtype='int64'))`.
5. Returns `output`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_record_payload`, `len`, `np.arange`, `output[column].tolist`, `pd.DataFrame`, `pd.Index`, `pd.array`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_lookup`

**Signature**

```python
def _lookup(
    profile: CnigFeatureCodeProfile,
) -> dict[tuple[str, str, str], CnigFeatureCodeRecord]:
```

**Purpose**

Implements lookup according to the exact implementation and guards in this file.

**Inputs**

- `profile` (`CnigFeatureCodeProfile`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[tuple[str, str, str], CnigFeatureCodeRecord]`. Observed return expression(s): `{(record.feature_family, record.type_code, record.subtype_code): record for record in profile.records}`.

**Algorithm**

1. Returns `{(record.feature_family, record.type_code, record.subtype_code): record for record in profile.records}`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_coded_catalog`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_coded_catalog`

**Signature**

```python
def _coded_catalog(
    frame: gpd.GeoDataFrame,
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> gpd.GeoDataFrame:
```

**Purpose**

Implements coded catalog according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `profile` (`CnigFeatureCodeProfile`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `profile_hash` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `output` from `frame.copy(deep=True)`.
2. Computes `mapping` from `_lookup(profile)`.
3. Defines `columns` with annotation `dict[str, list[object]]` from `{column: [] for column in OFFICIAL_CODE_COLUMNS}`.
4. Iterates `row` over `frame.to_dict('records')`. For each value: Computes `key` from `(row['feature_family'], row['type_code_raw'], row['subtype_code_raw'])`. Computes `record` from `mapping.get(key)`. Calls `columns['official_code_status'].append('RESOLVED_OFFICIAL' if record is not None else 'UNKNOWN_CODE_PAIR')` for its validation or side effect. Executes 6 additional source-ordered statement(s).
5. Iterates `column` over `OFFICIAL_CODE_COLUMNS`. For each value: Computes `output[column]` from `pd.array(columns[column], dtype='str')`.
6. Computes `output.index` from `pd.Index(output.index.to_numpy(copy=True), name=output.index.name)`.
7. Returns `output`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `frame.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_lookup`, `columns['official_code_label'].append`, `columns['official_code_profile'].append`, `columns['official_code_profile_sha256'].append`, `columns['official_code_source_url'].append`, `columns['official_code_status'].append`, `columns['official_legal_reference'].append`, `columns['official_regulation_reference'].append`, `frame.copy`, `frame.to_dict`, `mapping.get`, `output.index.to_numpy`, `pd.Index`, `pd.array`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_catalog_by_id`

**Signature**

```python
def _catalog_by_id(
    catalogs: Sequence[gpd.GeoDataFrame],
) -> dict[str, dict[str, object]]:
```

**Purpose**

Implements catalog by id according to the exact implementation and guards in this file.

**Inputs**

- `catalogs` (`Sequence[gpd.GeoDataFrame]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, dict[str, object]]`. Observed return expression(s): `records`.

**Algorithm**

1. Defines `records` with annotation `dict[str, dict[str, object]]` from `{}`.
2. Iterates `catalog` over `catalogs`. For each value: Iterates `row` over `catalog.to_dict('records')`. For each value: Computes `identifier` from `str(row['planning_feature_id'])`. Checks `identifier in records`. When true: Raises `PlanningFeatureCodeError('Planning feature IDs must be unique across feature catalogs')`. Computes `records[identifier]` from `row`.
3. Returns `records`.

**Validation and invariants**

- Rejects or diverts the path when `identifier in records` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `catalog.to_dict`, `str`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_coded_relations`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_coded_relations`

**Signature**

```python
def _coded_relations(
    relations: pd.DataFrame,
    coded: Sequence[gpd.GeoDataFrame],
) -> pd.DataFrame:
```

**Purpose**

Implements coded relations according to the exact implementation and guards in this file.

**Inputs**

- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded` (`Sequence[gpd.GeoDataFrame]`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `meanings` from `_catalog_by_id(coded)`.
2. Computes `output` from `relations.copy(deep=True)`.
3. Defines `appended` with annotation `dict[str, list[object]]` from `{column: [] for column in OFFICIAL_CODE_COLUMNS}`.
4. Iterates `row` over `relations.to_dict('records')`. For each value: Computes `identifier` from `_strict_string(row['planning_feature_id'], 'relation feature ID')`. Computes `meaning` from `meanings.get(identifier)`. Checks `meaning is None`. When true: Raises `PlanningFeatureCodeError('Relation references an unknown feature catalog ID')`. Executes 1 additional source-ordered statement(s).
5. Iterates `column` over `OFFICIAL_CODE_COLUMNS`. For each value: Computes `output[column]` from `pd.array(appended[column], dtype='str')`.
6. Computes `output.index` from `pd.Index(output.index.to_numpy(copy=True), name=output.index.name)`.
7. Returns `output`.

**Validation and invariants**

- Rejects or diverts the path when `meaning is None` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `relations.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningFeatureCodeError`, `_catalog_by_id`, `_strict_string`, `appended[column].append`, `meanings.get`, `output.index.to_numpy`, `pd.Index`, `pd.array`, `relations.copy`, `relations.to_dict`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_value`

**Signature**

```python
def _canonical_value(value: object) -> object:
```

**Purpose**

Implements canonical value according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `object`. Observed return expression(s): `to_wkb(value, hex=True, include_srid=False)`; `value.isoformat()`; `_canonical_value(value.item())`; `{str(key): _canonical_value(item) for key, item in value.items()}`; `[_canonical_value(item) for item in value]`; `None`; `value`; `int(value)`; `number`.

**Algorithm**

1. Checks `isinstance(value, BaseGeometry)`. When true: Returns `to_wkb(value, hex=True, include_srid=False)`.
2. Checks `isinstance(value, (datetime, date, pd.Timestamp))`. When true: Returns `value.isoformat()`.
3. Checks `isinstance(value, np.generic)`. When true: Returns `_canonical_value(value.item())`.
4. Checks `isinstance(value, Mapping)`. When true: Returns `{str(key): _canonical_value(item) for key, item in value.items()}`.
5. Checks `isinstance(value, (tuple, list, np.ndarray))`. When true: Returns `[_canonical_value(item) for item in value]`.
6. Checks `value is None or value is pd.NA`. When true: Returns `None`.
7. Runs guarded operation: Computes `missing` from `pd.isna(value)`. Handles `(TypeError, ValueError)`.
8. Checks `isinstance(missing, (bool, np.bool_)) and bool(missing)`. When true: Returns `None`.
9. Checks `isinstance(value, bool)`. When true: Returns `value`.
10. Checks `isinstance(value, Integral)`. When true: Returns `int(value)`.
11. Checks `isinstance(value, Real)`. When true: Computes `number` from `float(value)`. Checks `not math.isfinite(number)`. When true: Raises `PlanningFeatureCodeError('Integrity payload contains non-finite numeric data')`. Returns `number`.
12. Checks `isinstance(value, str)`. When true: Returns `value`.
13. Raises `PlanningFeatureCodeError(f'Integrity payload contains unsupported value {type(value).__name__}')`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, Real)` is true.
- Rejects or diverts the path when `not math.isfinite(number)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_canonical_value`, `bool`, `float`, `int`, `isinstance`, `math.isfinite`, `pd.isna`, `str`, `to_wkb`, `type`, `value.isoformat`, `value.item`, `value.items`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_compare_frame`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_frame_payload`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_frame_payload`

**Signature**

```python
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
```

**Purpose**

Implements frame payload according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `payload`.

**Algorithm**

1. Defines `payload` with annotation `dict[str, object]` from `{'schema': deterministic_frame_schema_signature(frame), 'index': [_canonical_value(value) for value in frame.index.tolist()], 'rows': [[_canonical_value(value) for value in row] for row in frame.itertuples(index=False, name=None)]}`.
2. Returns `payload`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_value`, `deterministic_frame_schema_signature`, `frame.index.tolist`, `frame.itertuples`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_compare_frame`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_frame_sha256`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_normalized_catalogs_input_sha256`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_source_frame_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_source_frame_sha256`

**Signature**

```python
def _source_frame_sha256(domain: str, frame: pd.DataFrame) -> str:
```

**Purpose**

Implements source frame sha256 according to the exact implementation and guards in this file.

**Inputs**

- `domain` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256({'domain': domain, 'result_hash_schema_version': RESULT_HASH_SCHEMA_VERSION, 'frame': _frame_payload(frame)})`.

**Algorithm**

1. Returns `_canonical_json_sha256({'domain': domain, 'result_hash_schema_version': RESULT_HASH_SCHEMA_VERSION, 'frame': _frame_payload(frame)})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_json_sha256`, `_frame_payload`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_inspected_layer_payload`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_normalized_relations_input_sha256`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_parcel_identity_input_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_inspected_layer_payload`

**Signature**

```python
def _inspected_layer_payload(layer: GpuInspectedLayer) -> dict[str, object]:
```

**Purpose**

Implements inspected layer payload according to the exact implementation and guards in this file.

**Inputs**

- `layer` (`GpuInspectedLayer`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'logical_name': logical_name, 'source_layer': _strict_string(reference.source_layer, 'GPU source layer'), 'driver': _strict_string(reference.driver, 'GPU driver'), 'summary': asdict(summary), 'source_data_sha256': _source_frame_sha256('landscout.cnig_feature_codes.gpu_source_layer', data)}`.

**Algorithm**

1. Runs guarded operation: Computes `logical_name` from `_strict_string(layer.logical_name, 'GPU logical layer name')`. Computes `reference` from `layer.reference`. Computes `summary` from `layer.summary`. Computes `data` from `layer.data`. Executes 2 additional source-ordered statement(s). Handles `PlanningFeatureCodeError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(data, gpd.GeoDataFrame)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_source_frame_sha256`, `_strict_string`, `asdict`, `isinstance`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_planning_document_context_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_planning_document_context_sha256`

**Signature**

```python
def _planning_document_context_sha256(document: GpuPlanningDocument) -> str:
```

**Purpose**

Implements planning document context sha256 according to the exact implementation and guards in this file.

**Inputs**

- `document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256({'domain': 'landscout.cnig_feature_codes.planning_document_input', 'result_hash_schema_version': RESULT_HASH_SCHEMA_VERSION, 'document_metadata': asdict(archive.document), 'archive': {'filename': archive.filename, 'archive_format': archive.archive_format, 'file_size': archive.file_size, 'sha256': archive.sha256}, 'standard_models': sorted(document.extraction.standard_models…`.

**Algorithm**

1. Runs guarded operation: Computes `archive` from `document.extraction.archive`. Computes `related` from `sorted((_inspected_layer_payload(layer) for layer in document.related_layers), key=lambda item: str(item['logical_name']))`. Computes `spatial_references` from `sorted(({'source_layer': _strict_string(reference.source_layer, 'GPU spatial source layer'), 'driver': _strict_string(reference.driver, 'GPU spatial source driver')} for reference in document.all_spatial_layers), key=lambda item: (str(item['source_layer']), str(item['driver'])))`. Returns `_canonical_json_sha256({'domain': 'landscout.cnig_feature_codes.planning_document_input', 'result_hash_schema_version': RESULT_HASH_SCHEMA_VERSION, 'document_metadata': asdict(archive.document), 'archive': {'filename': archive.filename, 'archive_format': archive.archive_format, 'file_size': archive.file_size, 'sha256': archive.sha256}, 'standard_models': so…`. Handles `PlanningFeatureCodeError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_canonical_json_sha256`, `_inspected_layer_payload`, `_strict_string`, `asdict`, `sorted`, `str`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_parcel_identity_input_sha256`

**Signature**

```python
def _parcel_identity_input_sha256(parcels: gpd.GeoDataFrame) -> str:
```

**Purpose**

Implements parcel identity input sha256 according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_source_frame_sha256('landscout.cnig_feature_codes.parcel_identity_input', identity)`.

**Algorithm**

1. Runs guarded operation: Computes `identity` from `gpd.GeoDataFrame(parcels[['parcel_id', 'geometry']].copy(deep=True), geometry='geometry', crs=parcels.crs)`. Handles `Exception`.
2. Returns `_source_frame_sha256('landscout.cnig_feature_codes.parcel_identity_input', identity)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `parcels[['parcel_id', 'geometry']].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `PlanningFeatureCodeError`, `_source_frame_sha256`, `gpd.GeoDataFrame`, `parcels[['parcel_id', 'geometry']].copy`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalized_catalogs_input_sha256`

**Signature**

```python
def _normalized_catalogs_input_sha256(
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> str:
```

**Purpose**

Implements normalized catalogs input sha256 according to the exact implementation and guards in this file.

**Inputs**

- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256({'domain': 'landscout.cnig_feature_codes.normalized_catalogs_input', 'result_hash_schema_version': RESULT_HASH_SCHEMA_VERSION, 'surface': _frame_payload(surface_features), 'line': _frame_payload(line_features), 'point': _frame_payload(point_features)})`.

**Algorithm**

1. Returns `_canonical_json_sha256({'domain': 'landscout.cnig_feature_codes.normalized_catalogs_input', 'result_hash_schema_version': RESULT_HASH_SCHEMA_VERSION, 'surface': _frame_payload(surface_features), 'line': _frame_payload(line_features), 'point': _frame_payload(point_features)})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_json_sha256`, `_frame_payload`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalized_relations_input_sha256`

**Signature**

```python
def _normalized_relations_input_sha256(relations: pd.DataFrame) -> str:
```

**Purpose**

Implements normalized relations input sha256 according to the exact implementation and guards in this file.

**Inputs**

- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_source_frame_sha256('landscout.cnig_feature_codes.normalized_relations_input', relations)`.

**Algorithm**

1. Returns `_source_frame_sha256('landscout.cnig_feature_codes.normalized_relations_input', relations)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_source_frame_sha256`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_component_metadata`

**Signature**

```python
def _component_metadata(result: PlanningFeatureCodeResult) -> dict[str, object]:
```

**Purpose**

Implements component metadata according to the exact implementation and guards in this file.

**Inputs**

- `result` (`PlanningFeatureCodeResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'result_hash_schema_version': result.result_hash_schema_version, 'profile_schema_version': result.profile_schema_version, 'profile': result.profile, 'standard_model': result.standard_model, 'profile_sha256': result.profile_sha256, 'source_document_id': result.source_document_id, 'source_archive_sha256': result.source_archive_sha256, 'planning_document_context_sha256': result.planning_document_co…`.

**Algorithm**

1. Returns `{'result_hash_schema_version': result.result_hash_schema_version, 'profile_schema_version': result.profile_schema_version, 'profile': result.profile, 'standard_model': result.standard_model, 'profile_sha256': result.profile_sha256, 'source_document_id': result.source_document_id, 'source_archive_sha256': result.source_archive_sha256, 'planning_document_cont…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_complete_sha256`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_frame_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_frame_sha256`

**Signature**

```python
def _frame_sha256(
    domain: str,
    result: PlanningFeatureCodeResult,
    frame: pd.DataFrame,
) -> str:
```

**Purpose**

Implements frame sha256 according to the exact implementation and guards in this file.

**Inputs**

- `domain` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`PlanningFeatureCodeResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256({'domain': domain, **_component_metadata(result), 'frame': _frame_payload(frame)})`.

**Algorithm**

1. Returns `_canonical_json_sha256({'domain': domain, **_component_metadata(result), 'frame': _frame_payload(frame)})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_json_sha256`, `_component_metadata`, `_frame_payload`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_result_with_hashes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_complete_sha256`

**Signature**

```python
def _complete_sha256(result: PlanningFeatureCodeResult) -> str:
```

**Purpose**

Implements complete sha256 according to the exact implementation and guards in this file.

**Inputs**

- `result` (`PlanningFeatureCodeResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256({'domain': 'landscout.cnig_feature_codes.result', **_component_metadata(result), 'code_dictionary_content_sha256': result.code_dictionary_content_sha256, 'surface_features_content_sha256': result.surface_features_content_sha256, 'line_features_content_sha256': result.line_features_content_sha256, 'point_features_content_sha256': result.point_features_content_sha256, 'relati…`.

**Algorithm**

1. Returns `_canonical_json_sha256({'domain': 'landscout.cnig_feature_codes.result', **_component_metadata(result), 'code_dictionary_content_sha256': result.code_dictionary_content_sha256, 'surface_features_content_sha256': result.surface_features_content_sha256, 'line_features_content_sha256': result.line_features_content_sha256, 'point_features_content_sha256': resul…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_json_sha256`, `_component_metadata`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_result_with_hashes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_result_with_hashes`

**Signature**

```python
def _result_with_hashes(result: PlanningFeatureCodeResult) -> PlanningFeatureCodeResult:
```

**Purpose**

Implements result with hashes according to the exact implementation and guards in this file.

**Inputs**

- `result` (`PlanningFeatureCodeResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningFeatureCodeResult`. Observed return expression(s): `replace(component, complete_result_content_sha256=_complete_sha256(component))`.

**Algorithm**

1. Computes `component` from `replace(result, code_dictionary_content_sha256=_frame_sha256('landscout.cnig_feature_codes.dictionary', result, result.code_dictionary), surface_features_content_sha256=_frame_sha256('landscout.cnig_feature_codes.surface', result, result.surface_features), line_features_content_sha256=_frame_sha256('landscout.cnig_fea…`.
2. Returns `replace(component, complete_result_content_sha256=_complete_sha256(component))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_complete_sha256`, `_frame_sha256`, `replace`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `_build_result`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `_validate_result_envelope`
- `tests/unit/test_resolve_planning_feature_codes.py` — `_canonical_empty_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_coordinated_output_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_dictionary_rows_are_intrinsically_validated`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_dictionary_schema_is_explicit`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_scalar_lineage_contracts_are_intrinsic`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_source_binding_hashes_bind_every_component_hash`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_coordinated_output_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_dictionary_rows_are_intrinsically_validated`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_dictionary_schema_is_explicit`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_scalar_lineage_contracts_are_intrinsic`
- `tests/unit/test_resolve_planning_feature_codes.py::test_source_binding_hashes_bind_every_component_hash`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_result`

**Signature**

```python
def _build_result(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile,
    factual_validation: PlanningFeatureInputValidation | None = None,
) -> PlanningFeatureCodeResult:
```

**Purpose**

Builds result according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `code_profile` (`CnigFeatureCodeProfile`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `factual_validation` (`PlanningFeatureInputValidation | None`; optional/default `None`) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningFeatureCodeResult`. Observed return expression(s): `_result_with_hashes(result)`.

**Algorithm**

1. Computes `standard` from `_planning_standard(planning_document)`.
2. Checks `standard != code_profile.standard_model`. When true: Raises `PlanningFeatureCodeError(f'Planning document standard {standard!r} differs from code-profile standard')`.
3. Checks `factual_validation is None`. When true: Runs guarded operation: Computes `factual_validation` from `validate_normalized_planning_feature_inputs(planning_document, parcels, surface_features, line_features, point_features, relations)`. Handles `ValueError`.
4. Computes `surface` from `_validate_catalog_document_lineage(surface_features, 'surface feature catalog', planning_document, standard)`.
5. Computes `line` from `_validate_catalog_document_lineage(line_features, 'line feature catalog', planning_document, standard)`.
6. Computes `point` from `_validate_catalog_document_lineage(point_features, 'point feature catalog', planning_document, standard)`.
7. Computes `profile_hash` from `_profile_sha256(code_profile)`.
8. Computes `coded_surface` from `_coded_catalog(surface, code_profile, profile_hash)`.
9. Computes `coded_line` from `_coded_catalog(line, code_profile, profile_hash)`.
10. Computes `coded_point` from `_coded_catalog(point, code_profile, profile_hash)`.
11. Computes `coded_relations` from `_coded_relations(relations, (coded_surface, coded_line, coded_point))`.
12. Computes `archive` from `planning_document.extraction.archive`.
13. Computes `result` from `PlanningFeatureCodeResult(result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION, profile_schema_version=code_profile.schema_version, profile=code_profile.profile, standard_model=standard, profile_sha256=profile_hash, source_document_id=archive.document.document_id, source_archive_sha256=archive.sha256, planning_docume…`.
14. Returns `_result_with_hashes(result)`.

**Validation and invariants**

- Rejects or diverts the path when `standard != code_profile.standard_model` is true.
- Rejects or diverts the path when `factual_validation is None` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `PlanningFeatureCodeResult`, `_coded_catalog`, `_coded_relations`, `_dictionary`, `_normalized_catalogs_input_sha256`, `_normalized_relations_input_sha256`, `_parcel_identity_input_sha256`, `_planning_document_context_sha256`, `_planning_standard`, `_profile_sha256`, `_result_with_hashes`, `_validate_catalog_document_lineage`, `validate_normalized_planning_feature_inputs`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `resolve_planning_feature_codes`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `validate_planning_feature_code_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result_envelope`

**Signature**

```python
def _validate_result_envelope(result: PlanningFeatureCodeResult) -> None:
```

**Purpose**

Validates and rejects malformed result envelope according to the exact implementation and guards in this file.

**Inputs**

- `result` (`PlanningFeatureCodeResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `type(result) is not PlanningFeatureCodeResult`. When true: Raises `PlanningFeatureCodeError('result must be a PlanningFeatureCodeResult')`.
2. Iterates `(version, expected_version, label)` over `((result.result_hash_schema_version, RESULT_HASH_SCHEMA_VERSION, 'result hash schema version'), (result.profile_schema_version, PROFILE_SCHEMA_VERSION, 'profile schema version'))`. For each value: Checks `type(version) is not int or version != expected_version`. When true: Raises `PlanningFeatureCodeError(f'unsupported {label}: {version!r}')`.
3. Checks `result.standard_model != STANDARD_MODEL`. When true: Raises `PlanningFeatureCodeError('result standard model is invalid')`.
4. Iterates `(value, label)` over `((result.profile, 'result profile'), (result.source_document_id, 'result source document ID'))`. For each value: Calls `_strict_string(value, label)` for its validation or side effect.
5. Iterates `field` over `PlanningFeatureCodeResult.__dataclass_fields__`. For each value: Checks `not field.endswith('_sha256')`. When true: Executes `continue` control flow. Computes `value` from `getattr(result, field)`. Checks `not isinstance(value, str) or _SHA_PATTERN.fullmatch(value) is None`. When true: Raises `PlanningFeatureCodeError(f'{field} must be a lowercase SHA256')`.
6. Computes `dictionary` from `_validate_code_dictionary(result)`.
7. Iterates `(frame, label, kind)` over `((result.surface_features, 'surface features', 'SURFACE'), (result.line_features, 'line features', 'LINE'), (result.point_features, 'point features', 'POINT'))`. For each value: Computes `geometry_kind` from `cast(GeometryKind, kind)`. Runs guarded operation: Calls `validate_canonical_frame_schema(frame, columns=feature_columns(geometry_kind), dtypes=feature_dtypes(geometry_kind, frame=frame), label=label, geospatial=True)` for its validation or side effect. Handles `(TypeError, ValueError)`.
8. Runs guarded operation: Calls `validate_canonical_frame_schema(result.relations, columns=relation_columns(), dtypes=relation_dtypes(), label='coded relations', geospatial=False)` for its validation or side effect. Handles `(TypeError, ValueError)`.
9. Calls `_validate_coded_meaning_rows(result, dictionary)` for its validation or side effect.
10. Computes `rebuilt_hashes` from `_result_with_hashes(result)`.
11. Iterates `field` over `('code_dictionary_content_sha256', 'surface_features_content_sha256', 'line_features_content_sha256', 'point_features_content_sha256', 'relations_content_sha256', 'complete_result_content_sha256')`. For each value: Checks `getattr(result, field) != getattr(rebuilt_hashes, field)`. When true: Raises `PlanningFeatureCodeError(f'result hash {field} is invalid')`.

**Validation and invariants**

- Rejects or diverts the path when `type(result) is not PlanningFeatureCodeResult` is true.
- Rejects or diverts the path when `result.standard_model != STANDARD_MODEL` is true.
- Rejects or diverts the path when `type(version) is not int or version != expected_version` is true.
- Rejects or diverts the path when `not isinstance(value, str) or _SHA_PATTERN.fullmatch(value) is None` is true.
- Rejects or diverts the path when `getattr(result, field) != getattr(rebuilt_hashes, field)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_SHA_PATTERN.fullmatch`, `_result_with_hashes`, `_strict_string`, `_validate_code_dictionary`, `_validate_coded_meaning_rows`, `cast`, `feature_columns`, `feature_dtypes`, `field.endswith`, `getattr`, `isinstance`, `relation_columns`, `relation_dtypes`, `str`, `type`, `validate_canonical_frame_schema`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `resolve_planning_feature_codes`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `validate_planning_feature_code_result_envelope`
- `src/landscout/stages/resolve_planning_feature_codes.py` — `validate_planning_feature_code_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_planning_feature_code_result_envelope`

**Signature**

```python
def validate_planning_feature_code_result_envelope(
    result: PlanningFeatureCodeResult,
) -> None:
```

**Purpose**

Validate one coded-result envelope without rebuilding factual sources.

**Inputs**

- `result` (`PlanningFeatureCodeResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `_validate_result_envelope(result)` for its validation or side effect. Handles `PlanningFeatureCodeError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_validate_result_envelope`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `load_bess_planning_feature_application_artifacts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_frame`

**Signature**

```python
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
```

**Purpose**

Compares frame according to the exact implementation and guards in this file.

**Inputs**

- `actual` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `_canonical_value(_frame_payload(actual)) != _canonical_value(_frame_payload(expected))`. When true: Raises `PlanningFeatureCodeError(f'{label} differs from rebuilt source result')`.

**Validation and invariants**

- Rejects or diverts the path when `_canonical_value(_frame_payload(actual)) != _canonical_value(_frame_payload(expected))` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_canonical_value`, `_frame_payload`.

**Known repository callers**

- `src/landscout/stages/resolve_planning_feature_codes.py` — `validate_planning_feature_code_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_planning_feature_code_result`

**Signature**

```python
def validate_planning_feature_code_result(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    result: PlanningFeatureCodeResult,
) -> None:
```

**Purpose**

Rebuild and validate a coded result from every factual source input.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `code_profile` (`CnigFeatureCodeProfile | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`PlanningFeatureCodeResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `_validate_result_envelope(result)` for its validation or side effect. Computes `expected` from `_build_result(planning_document, parcels, surface_features, line_features, point_features, relations, _resolved_profile(code_profile))`. Computes `scalar_fields` from `('result_hash_schema_version', 'profile_schema_version', 'profile', 'standard_model', 'profile_sha256', 'source_document_id', 'source_archive_sha256', 'planning_document_context_sha256', 'parcel_identity_input_sha256', 'normalized_catalogs_input_sha256', 'normalized_relations_input_sha256', 'gpu_related_source_files_s…`. Iterates `field` over `scalar_fields`. For each value: Checks `getattr(result, field) != getattr(expected, field)`. When true: Raises `PlanningFeatureCodeError(f'result {field} differs from rebuilt source result')`. Executes 1 additional source-ordered statement(s). Handles `PlanningFeatureCodeError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `getattr(result, field) != getattr(expected, field)` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_build_result`, `_compare_frame`, `_resolved_profile`, `_validate_result_envelope`, `getattr`.

**Known repository callers**

- `src/landscout/stages/bess_planning_feature_policy.py` — `_validate_coded_source`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_gpu_document_context_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_normalized_catalog_change_invalidates_coded_result_even_when_coherent`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_normalized_relation_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_parcel_source_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_parquet_readback_preserves_source_hash_envelope`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_source_input_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_step_7d_3_1_output_integrates_with_public_coding_api`
- `tests/unit/test_resolve_planning_feature_codes.py` — `validate_planning_feature_code_result`

**Tests**

- `tests/unit/test_resolve_planning_feature_codes.py::test_gpu_document_context_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent`
- `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_relation_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py::test_parcel_source_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_parquet_readback_preserves_source_hash_envelope`
- `tests/unit/test_resolve_planning_feature_codes.py::test_source_input_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_step_7d_3_1_output_integrates_with_public_coding_api`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `resolve_planning_feature_codes`

**Signature**

```python
def resolve_planning_feature_codes(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
) -> PlanningFeatureCodeResult:
```

**Purpose**

Attach exact official CNIG meanings without interpreting their impact.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `code_profile` (`CnigFeatureCodeProfile | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PlanningFeatureCodeResult`. Observed return expression(s): `result`.

**Algorithm**

1. Runs guarded operation: Computes `profile` from `_resolved_profile(code_profile)`. Computes `standard` from `_planning_standard(planning_document)`. Checks `standard != profile.standard_model`. When true: Raises `PlanningFeatureCodeError(f'Planning document standard {standard!r} differs from code-profile standard')`. Computes `factual_validation` from `validate_normalized_planning_feature_inputs(planning_document, parcels, surface_features, line_features, point_features, relations)`. Executes 3 additional source-ordered statement(s). Handles `PlanningFeatureCodeError`, `ValueError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `standard != profile.standard_model` is true.

**Exceptions**

- Explicitly raises: `PlanningFeatureCodeError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `PlanningFeatureCodeError`, `_build_result`, `_planning_standard`, `_resolved_profile`, `_validate_result_envelope`, `validate_normalized_planning_feature_inputs`.

**Known repository callers**

- `tests/unit/test_bess_planning_feature_policy.py` — `_checked_in_policy_result`
- `tests/unit/test_bess_planning_feature_policy.py` — `_compiled_fixture`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_compiler_and_public_validator_invoke_source_complete_coding_validation`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_duplicate_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_extra_policy_pair_is_rejected_without_type_fallback`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_invalid_confidence_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_invalid_or_legal_conclusion_status_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_malformed_sha256_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_missing_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_noncanonical_whitespace_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_official_meaning_mismatch_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_policy_entries_require_deterministic_order`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_prescription_information_code_spaces_remain_separate`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_status_priority_contract_is_strict`
- `tests/unit/test_bess_planning_feature_policy.py` — `test_unknown_yaml_field_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `resolve_planning_feature_codes`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_coded_result_persists_all_source_input_hashes`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_coding_api_rejects_relation_set_not_rebuilt_from_geometry`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_gpu_document_context_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_gpu_related_source_hash_is_deterministic_across_cache_roots`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_normalized_catalog_change_invalidates_coded_result_even_when_coherent`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_normalized_relation_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_parcel_source_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_schema_v5_parquet_readback_preserves_source_hash_envelope`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_source_binding_hashes_bind_every_component_hash`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_source_input_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_step_7d_3_1_output_integrates_with_public_coding_api`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_empty_optional_catalogs_preserve_schema_and_crs`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_multi_geometries_are_accepted`
- `tests/unit/test_resolve_planning_feature_codes.py` — `test_valid_relation_types_are_retained`

**Tests**

- `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation`
- `tests/unit/test_bess_planning_feature_policy.py::test_duplicate_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_extra_policy_pair_is_rejected_without_type_fallback`
- `tests/unit/test_bess_planning_feature_policy.py::test_invalid_confidence_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_invalid_or_legal_conclusion_status_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_malformed_sha256_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_missing_policy_pair_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_noncanonical_whitespace_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_official_meaning_mismatch_is_rejected`
- `tests/unit/test_bess_planning_feature_policy.py::test_policy_entries_require_deterministic_order`
- `tests/unit/test_bess_planning_feature_policy.py::test_prescription_information_code_spaces_remain_separate`
- `tests/unit/test_bess_planning_feature_policy.py::test_status_priority_contract_is_strict`
- `tests/unit/test_bess_planning_feature_policy.py::test_unknown_yaml_field_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_coded_result_persists_all_source_input_hashes`
- `tests/unit/test_resolve_planning_feature_codes.py::test_coding_api_rejects_relation_set_not_rebuilt_from_geometry`
- `tests/unit/test_resolve_planning_feature_codes.py::test_gpu_document_context_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py::test_gpu_related_source_hash_is_deterministic_across_cache_roots`
- `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent`
- `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_relation_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py::test_parcel_source_change_invalidates_coded_result`
- `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_parquet_readback_preserves_source_hash_envelope`
- `tests/unit/test_resolve_planning_feature_codes.py::test_source_binding_hashes_bind_every_component_hash`
- `tests/unit/test_resolve_planning_feature_codes.py::test_source_input_hash_mutation_is_rejected`
- `tests/unit/test_resolve_planning_feature_codes.py::test_step_7d_3_1_output_integrates_with_public_coding_api`
- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_empty_optional_catalogs_preserve_schema_and_crs`
- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_multi_geometries_are_accepted`
- `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `CNIG PLU v2017` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `INFORMATION` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `PRESCRIPTION` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `RESOLVED_OFFICIAL` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `UNKNOWN_CODE_PAIR` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `driver` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_family` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry` | Logical dtype: GeoPandas active geometry dtype. Nullability: nullable only where the source-stage geometry-status contract explicitly preserves nulls. | source or preserved spatial geometry; never itself a suitability or legal conclusion. Consumers and exact calculations are the functions that reference this column above. |
| `legal_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `logical_name` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_profile_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `official_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_legal_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_regulation_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `profile_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `regulation_or_annex_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_standard_model` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `standard_model` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `subtype_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `subtype_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `type_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `type_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `planning` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
