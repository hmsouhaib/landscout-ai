# `src/landscout/stages/apply_bess_planning_feature_policy.py`

## File identity

- Repository path: `src/landscout/stages/apply_bess_planning_feature_policy.py`
- File type: Python source
- Primary responsibility: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.
- Layer / domain: `stage` / `planning`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `35c40953ec24f8ce27c8de89f3f2ff8538b48c9e594407e7ce2a877f0375b174`

## 1. Purpose

Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `planning` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import math` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass, replace` — required by the implementation paths and symbols documented below.
- `from datetime import date, datetime` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from io import BytesIO` — required by the implementation paths and symbols documented below.
- `from numbers import Integral, Real` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Literal` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `from pydantic import ( BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr, model_validator, )` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.
- `from shapely import get_coordinate_dimension, to_wkb` — required by the implementation paths and symbols documented below.
- `from shapely.geometry.base import BaseGeometry` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.common.artifact_paths import validate_portable_parquet_filename` — required by the implementation paths and symbols documented below.
- `from landscout.common.bess_application_contract import ( APPLICATION_SCOPE, FLAG_COLUMNS, POLICY_COLUMNS, POLICY_SCOPE, STRING_POLICY_COLUMNS, ApplicationStatus, validate_bess_application_feature_catalogs, validate_bess_application_relation_frame, )` — required by the implementation paths and symbols documented below.
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature` — required by the implementation paths and symbols documented below.
- `from landscout.common.planning_overlay import technical_overlay_tolerance` — required by the implementation paths and symbols documented below.
- `from landscout.sources.gpu_fr import GpuPlanningDocument` — required by the implementation paths and symbols documented below.
- `from landscout.stages.bess_planning_feature_policy import ( BessPlanningFeaturePolicyConfig, BessPlanningFeaturePolicyResult, validate_bess_planning_feature_policy_result, validate_bess_planning_feature_policy_result_envelope, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.resolve_planning_feature_codes import ( CnigFeatureCodeProfile, PlanningFeatureCodeResult, validate_planning_feature_code_result_envelope, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `RESULT_HASH_SCHEMA_VERSION` | `2` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARTIFACT_MANIFEST_SCHEMA_VERSION` | `2` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARTIFACT_KIND` | `"BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARTIFACT_ROLES` | `( "SURFACE_FEATURES", "LINE_FEATURES", "POINT_FEATURES", "RELATIONS", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATION_FEATURE_AGREEMENT_COLUMNS` | `( "source_feature_id", "source_identity_kind", "source_identity_field", "logical_layer", "feature_family", "geometry_kind", "type_code_raw", "subtype_code_raw", "label_raw", "text_raw", "source_document_id", "source_archive_sha256", "source_layer", "source_validity_date_raw", "regulation_filename_raw", "official_code_status", "official_code_label", "official_legal_reference", "official_regulation_reference", "official_code_source_url", "official_code_profile", "official_code_profile_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SHA_PATTERN` | `re.compile(r"[0-9a-f]{64}")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CODE_PATTERN` | `re.compile(r"[0-9]{2}")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RESULT_FRAME_FIELDS` | `( "surface_features", "line_features", "point_features", "relations", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RESULT_SCALAR_FIELDS` | `tuple( field for field in BessPlanningFeatureApplicationResult.__dataclass_fields__ if field not in RESULT_FRAME_FIELDS )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `BessPlanningFeatureApplicationError`

**Purpose:** Raised when exact feature-policy propagation cannot be proven.

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

### `BessPlanningFeatureApplicationArtifactRecord`

**Purpose:** One physical output record within the application manifest.

**Inheritance:** `_StrictModel`.

**Model form and mutability:** class inheriting from `_StrictModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `artifact_role` | `ArtifactRole` | `required` | `ArtifactRole` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `filename` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `row_count` | `StrictInt` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `size_bytes` | `StrictInt` | `required` | `StrictInt` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `sha256` | `StrictStr` | `required` | Lowercase SHA256 binding the exact relevant bytes. |
| `frame_schema_signature` | `dict[StrictStr, object]` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `geospatial` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `crs` | `dict[StrictStr, object] | None` | `required` | `dict[StrictStr, object] | None` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_record` — `def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `BessPlanningFeatureApplicationResult`

**Purpose:** Immutable exact policy propagation over coded features and relations.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `result_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `application_scope` | `str` | `required` | `str` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_scope` | `str` | `required` | `str` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `local_feature_text_interpreted` | `bool` | `required` | `bool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `local_regulation_content_interpreted` | `bool` | `required` | `bool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `legal_conclusion_produced` | `bool` | `required` | `bool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parcel_status_aggregated` | `bool` | `required` | `bool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parcel_rejection_performed` | `bool` | `required` | `bool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `score_calculated` | `bool` | `required` | `bool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_profile` | `str` | `required` | `str` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `policy_result_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `policy_complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_profile` | `str` | `required` | `str` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cnig_profile_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_result_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `cnig_complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `source_archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_surface_features_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_line_features_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_point_features_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_relations_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `surface_features_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `line_features_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `point_features_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `relations_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `surface_features` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `line_features` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `point_features` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `relations` | `pd.DataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |

**Validators and methods:**

- None.

### `BessPlanningFeatureApplicationArtifactManifest`

**Purpose:** Strict four-file physical artifact envelope.

**Inheritance:** `_StrictModel`.

**Model form and mutability:** class inheriting from `_StrictModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `StrictInt` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `artifact_kind` | `Literal['BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT']` | `required` | `Literal['BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT']` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `result_hash_schema_version` | `StrictInt` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `application_scope` | `Literal['FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY']` | `required` | `Literal['FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY']` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_scope` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` | `required` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `local_feature_text_interpreted` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `local_regulation_content_interpreted` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `legal_conclusion_produced` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parcel_status_aggregated` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parcel_rejection_performed` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `score_calculated` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_profile` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `policy_result_hash_schema_version` | `StrictInt` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `policy_complete_result_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_profile` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cnig_profile_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_result_hash_schema_version` | `StrictInt` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `cnig_complete_result_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_document_id` | `StrictStr` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `source_archive_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_surface_features_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_line_features_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_point_features_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_relations_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `surface_features_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `line_features_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `point_features_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `relations_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `complete_result_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `artifacts` | `tuple[BessPlanningFeatureApplicationArtifactRecord, ...]` | `required` | `tuple[BessPlanningFeatureApplicationArtifactRecord, ...]` state used by `src/landscout/stages/apply_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_manifest` — `def _validate_manifest(self) -> BessPlanningFeatureApplicationArtifactManifest:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

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

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `BessPlanningFeatureApplicationArtifactManifest._validate_manifest`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_sha256_string`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_sha256_string`

**Signature**

```python
def _sha256_string(value: object, label: str) -> str:
```

**Purpose**

Implements sha256 string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `text`.

**Algorithm**

1. Computes `text` from `_exact_string(value, label)`.
2. Checks `SHA_PATTERN.fullmatch(text) is None`. When true: Raises `ValueError(f'{label} must be a lowercase SHA256')`.
3. Returns `text`.

**Validation and invariants**

- Rejects or diverts the path when `SHA_PATTERN.fullmatch(text) is None` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `SHA_PATTERN.fullmatch`, `ValueError`, `_exact_string`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `BessPlanningFeatureApplicationArtifactManifest._validate_manifest`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `BessPlanningFeatureApplicationArtifactRecord._validate_record`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessPlanningFeatureApplicationArtifactRecord._validate_record`

**Signature**

```python
def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:
```

**Purpose**

Validates and rejects malformed record according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationArtifactRecord`. Observed return expression(s): `self`.

**Algorithm**

1. Calls `validate_portable_parquet_filename(self.filename, 'artifact filename')` for its validation or side effect.
2. Checks `type(self.row_count) is not int or self.row_count < 0`. When true: Raises `ValueError('artifact row_count must be a non-negative integer')`.
3. Checks `type(self.size_bytes) is not int or self.size_bytes < 1`. When true: Raises `ValueError('artifact size_bytes must be a positive integer')`.
4. Calls `_sha256_string(self.sha256, 'artifact SHA256')` for its validation or side effect.
5. Computes `expected_geospatial` from `self.artifact_role != 'RELATIONS'`.
6. Checks `self.geospatial is not expected_geospatial`. When true: Raises `ValueError('artifact geospatial flag differs from its role')`.
7. Computes `signature_crs` from `self.frame_schema_signature.get('crs')`.
8. Computes `signature_geometry` from `self.frame_schema_signature.get('geometry_column')`.
9. Checks `expected_geospatial`. When true: Checks `self.crs is None or signature_crs != self.crs`. When true: Raises `ValueError('geospatial artifact CRS is missing or inconsistent')`. Checks `not isinstance(signature_geometry, str) or not signature_geometry`. When true: Raises `ValueError('geospatial artifact geometry column is missing')`. Otherwise: Checks `self.crs is not None or signature_crs is not None`. When true: Raises `ValueError('non-geospatial artifact must not declare a CRS')`.
10. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `type(self.row_count) is not int or self.row_count < 0` is true.
- Rejects or diverts the path when `type(self.size_bytes) is not int or self.size_bytes < 1` is true.
- Rejects or diverts the path when `self.geospatial is not expected_geospatial` is true.
- Rejects or diverts the path when `expected_geospatial` is true.
- Rejects or diverts the path when `self.crs is None or signature_crs != self.crs` is true.
- Rejects or diverts the path when `not isinstance(signature_geometry, str) or not signature_geometry` is true.
- Rejects or diverts the path when `self.crs is not None or signature_crs is not None` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_sha256_string`, `isinstance`, `model_validator`, `self.frame_schema_signature.get`, `type`, `validate_portable_parquet_filename`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessPlanningFeatureApplicationArtifactManifest._validate_manifest`

**Signature**

```python
def _validate_manifest(self) -> BessPlanningFeatureApplicationArtifactManifest:
```

**Purpose**

Validates and rejects malformed manifest according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationArtifactManifest`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `type(self.schema_version) is not int or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION`. When true: Raises `ValueError('unsupported application artifact manifest schema')`.
2. Checks `type(self.result_hash_schema_version) is not int or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`. When true: Raises `ValueError('unsupported application result hash schema')`.
3. Checks `any((value is not False for value in (self.local_feature_text_interpreted, self.local_regulation_content_interpreted, self.legal_conclusion_produced, self.parcel_status_aggregated, self.parcel_rejection_performed, self.score_calculated)))`. When true: Raises `ValueError('application boundary flags must all be false')`.
4. Iterates `(exact_value, label)` over `((self.policy_profile, 'policy_profile'), (self.cnig_profile, 'cnig_profile'), (self.source_document_id, 'source_document_id'))`. For each value: Calls `_exact_string(exact_value, label)` for its validation or side effect.
5. Checks `self.policy_result_hash_schema_version != 1`. When true: Raises `ValueError('policy result hash schema must be exactly 1')`.
6. Checks `self.cnig_result_hash_schema_version != 5`. When true: Raises `ValueError('CNIG result hash schema must be exactly 5')`.
7. Iterates `field` over `RESULT_SCALAR_FIELDS`. For each value: Checks `field.endswith('sha256')`. When true: Calls `_sha256_string(getattr(self, field), field)` for its validation or side effect.
8. Computes `roles` from `tuple((record.artifact_role for record in self.artifacts))`.
9. Checks `roles != ARTIFACT_ROLES`. When true: Raises `ValueError('application artifact roles are missing, extra, or unordered')`.
10. Computes `filenames` from `tuple((record.filename.casefold() for record in self.artifacts))`.
11. Checks `len(filenames) != len(set(filenames))`. When true: Raises `ValueError('application artifact filenames contain a duplicate')`.
12. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `type(self.schema_version) is not int or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `type(self.result_hash_schema_version) is not int or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `any((value is not False for value in (self.local_feature_text_interpreted, self.local_regulation_content_interpreted, self.legal_conclusion_produced, self.parcel_status_aggregated, self.parcel_rejection_performed, self.score_calculated)))` is true.
- Rejects or diverts the path when `self.policy_result_hash_schema_version != 1` is true.
- Rejects or diverts the path when `self.cnig_result_hash_schema_version != 5` is true.
- Rejects or diverts the path when `roles != ARTIFACT_ROLES` is true.
- Rejects or diverts the path when `len(filenames) != len(set(filenames))` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_exact_string`, `_sha256_string`, `any`, `field.endswith`, `getattr`, `len`, `model_validator`, `record.filename.casefold`, `set`, `tuple`, `type`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

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
2. Runs guarded operation: Computes `missing` from `pd.isna(value)`. Handles `(TypeError, ValueError)`.
3. Checks `isinstance(missing, (bool, np.bool_)) and bool(missing)`. When true: Returns `None`.
4. Returns `value`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `bool`, `isinstance`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_canonical_value`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_null_safe_equal`

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

- Declared return type: `object`. Observed return expression(s): `None`; `{'coordinate_dimension': coordinate_dimension, 'wkb_hex': to_wkb(value, hex=True, output_dimension=2, byte_order=1, include_srid=False)}`; `value.isoformat()`; `_canonical_value(value.item())`; `value`; `int(value)`; `number`.

**Algorithm**

1. Computes `value` from `_null_value(value)`.
2. Checks `value is None`. When true: Returns `None`.
3. Checks `isinstance(value, BaseGeometry)`. When true: Computes `coordinate_dimension` from `int(get_coordinate_dimension(value))`. Checks `coordinate_dimension != 2`. When true: Raises `BessPlanningFeatureApplicationError('Application geometry coordinate dimension must be exactly 2D')`. Returns `{'coordinate_dimension': coordinate_dimension, 'wkb_hex': to_wkb(value, hex=True, output_dimension=2, byte_order=1, include_srid=False)}`.
4. Checks `isinstance(value, (datetime, date, pd.Timestamp))`. When true: Returns `value.isoformat()`.
5. Checks `isinstance(value, np.generic)`. When true: Returns `_canonical_value(value.item())`.
6. Checks `isinstance(value, bool)`. When true: Returns `value`.
7. Checks `isinstance(value, Integral)`. When true: Returns `int(value)`.
8. Checks `isinstance(value, Real)`. When true: Computes `number` from `float(value)`. Checks `not math.isfinite(number)`. When true: Raises `BessPlanningFeatureApplicationError('Application integrity payload contains non-finite data')`. Returns `number`.
9. Checks `isinstance(value, str)`. When true: Returns `value`.
10. Raises `BessPlanningFeatureApplicationError(f'Unsupported application integrity value {type(value).__name__}')`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, BaseGeometry)` is true.
- Rejects or diverts the path when `isinstance(value, Real)` is true.
- Rejects or diverts the path when `coordinate_dimension != 2` is true.
- Rejects or diverts the path when `not math.isfinite(number)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`, `_canonical_value`, `_null_value`, `float`, `get_coordinate_dimension`, `int`, `isinstance`, `math.isfinite`, `to_wkb`, `type`, `value.isoformat`, `value.item`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_frame_payload`

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

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'schema': deterministic_frame_schema_signature(frame), 'index': [_canonical_value(value) for value in frame.index.tolist()], 'rows': [[_canonical_value(value) for value in row] for row in frame.itertuples(index=False, name=None)]}`.

**Algorithm**

1. Returns `{'schema': deterministic_frame_schema_signature(frame), 'index': [_canonical_value(value) for value in frame.index.tolist()], 'rows': [[_canonical_value(value) for value in row] for row in frame.itertuples(index=False, name=None)]}`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_value`, `deterministic_frame_schema_signature`, `frame.index.tolist`, `frame.itertuples`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_compare_frame`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_component_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_application_geometry`

**Signature**

```python
def _validate_application_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
```

**Purpose**

Require supplied application geometry to remain canonical two-dimensional.

**Inputs**

- `frame` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Computes `geometry_name` from `frame.geometry.name`. Checks `geometry_name not in frame.columns`. When true: Raises `BessPlanningFeatureApplicationError(f'{label} active geometry column is missing')`. Iterates `(position, geometry)` over `enumerate(frame.geometry.array)`. For each value: Checks `not isinstance(geometry, BaseGeometry)`. When true: Raises `BessPlanningFeatureApplicationError(f'{label} geometry at row {position} is missing or invalid')`. Checks `int(get_coordinate_dimension(geometry)) != 2`. When true: Raises `BessPlanningFeatureApplicationError(f'{label} geometry at row {position} must be canonical 2D')`. Handles `BessPlanningFeatureApplicationError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `geometry_name not in frame.columns` is true.
- Rejects or diverts the path when `not isinstance(geometry, BaseGeometry)` is true.
- Rejects or diverts the path when `int(get_coordinate_dimension(geometry)) != 2` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`, `enumerate`, `get_coordinate_dimension`, `int`, `isinstance`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_apply_feature_catalog`

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

1. Runs guarded operation: Computes `encoded` from `json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')`. Handles `(TypeError, ValueError)`.
2. Returns `sha256(encoded).hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`, `json.dumps`, `json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode`, `sha256`, `sha256(encoded).hexdigest`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_complete_result_sha256`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_component_sha256`

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

- Declared return type: `bool`. Observed return expression(s): `left is None and right is None`; `bool(left == right)`; `False`.

**Algorithm**

1. Computes `left` from `_null_value(left)`.
2. Computes `right` from `_null_value(right)`.
3. Checks `left is None or right is None`. When true: Returns `left is None and right is None`.
4. Runs guarded operation: Returns `bool(left == right)`. Handles `(TypeError, ValueError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_null_value`, `bool`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_apply_relations`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_validate_coded_policy_compatibility`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_lookup`

**Signature**

```python
def _policy_lookup(
    policy: BessPlanningFeaturePolicyResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

**Purpose**

Implements policy lookup according to the exact implementation and guards in this file.

**Inputs**

- `policy` (`BessPlanningFeaturePolicyResult`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[tuple[str, str, str], dict[str, object]]`. Observed return expression(s): `lookup`.

**Algorithm**

1. Defines `lookup` with annotation `dict[tuple[str, str, str], dict[str, object]]` from `{}`.
2. Iterates `row` over `policy.policy_table.to_dict('records')`. For each value: Computes `key` from `(str(row['feature_family']), str(row['type_code']), str(row['subtype_code']))`. Checks `key in lookup`. When true: Raises `BessPlanningFeatureApplicationError('Compiled policy contains a duplicate exact code pair')`. Computes `lookup[key]` from `row`.
3. Returns `lookup`.

**Validation and invariants**

- Rejects or diverts the path when `key in lookup` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`, `policy.policy_table.to_dict`, `str`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_apply_feature_catalog`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_values`

**Signature**

```python
def _policy_values(
    row: dict[str, object] | None,
    application_status: ApplicationStatus,
    policy: BessPlanningFeaturePolicyResult,
) -> dict[str, object]:
```

**Purpose**

Implements policy values according to the exact implementation and guards in this file.

**Inputs**

- `row` (`dict[str, object] | None`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `application_status` (`ApplicationStatus`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessPlanningFeaturePolicyResult`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'bess_cnig_policy_application_status': application_status, 'bess_cnig_precheck_status': None if row is None else row['precheck_status'], 'bess_cnig_precheck_confidence': None if row is None else row['confidence'], 'bess_cnig_status_priority': None if row is None else row['status_priority'], 'bess_cnig_rationale': None if row is None else row['rationale'], 'bess_cnig_required_human_action': None …`.

**Algorithm**

1. Returns `{'bess_cnig_policy_application_status': application_status, 'bess_cnig_precheck_status': None if row is None else row['precheck_status'], 'bess_cnig_precheck_confidence': None if row is None else row['confidence'], 'bess_cnig_status_priority': None if row is None else row['status_priority'], 'bess_cnig_rationale': None if row is None else row['rationale'], …`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_apply_feature_catalog`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_assign_policy_columns`

**Signature**

```python
def _assign_policy_columns(
    frame: pd.DataFrame,
    rows: list[dict[str, object]],
) -> pd.DataFrame:
```

**Purpose**

Implements assign policy columns according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `rows` (`list[dict[str, object]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Defines `values` with annotation `dict[str, object]` from `{}`.
2. Iterates `column` over `STRING_POLICY_COLUMNS`. For each value: Computes `values[column]` from `pd.array([row[column] for row in rows], dtype='str')`.
3. Computes `values['bess_cnig_status_priority']` from `pd.array([row['bess_cnig_status_priority'] for row in rows], dtype='Int64')`.
4. Iterates `column` over `FLAG_COLUMNS`. For each value: Computes `values[column]` from `pd.array([row[column] for row in rows], dtype='bool')`.
5. Iterates `column` over `POLICY_COLUMNS`. For each value: Computes `frame[column]` from `values[column]`.
6. Returns `frame`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `pd.array`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_apply_feature_catalog`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_apply_relations`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_apply_feature_catalog`

**Signature**

```python
def _apply_feature_catalog(
    catalog: gpd.GeoDataFrame,
    policy: BessPlanningFeaturePolicyResult,
) -> gpd.GeoDataFrame:
```

**Purpose**

Apply exact family/type/subtype policy to one already-coded catalog.

**Inputs**

- `catalog` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessPlanningFeaturePolicyResult`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `applied`.

**Algorithm**

1. Checks `not isinstance(catalog, gpd.GeoDataFrame)`. When true: Raises `BessPlanningFeatureApplicationError('Coded feature catalog is not geospatial')`.
2. Checks `any((column in catalog.columns for column in POLICY_COLUMNS))`. When true: Raises `BessPlanningFeatureApplicationError('Coded feature catalog already contains BESS policy columns')`.
3. Computes `required` from `{'planning_feature_id', 'feature_family', 'type_code_raw', 'subtype_code_raw', 'official_code_status'}`.
4. Checks `not required.issubset(catalog.columns)`. When true: Raises `BessPlanningFeatureApplicationError('Coded feature catalog lacks exact policy lookup fields')`.
5. Computes `lookup` from `_policy_lookup(policy)`.
6. Defines `policy_rows` with annotation `list[dict[str, object]]` from `[]`.
7. Iterates `row` over `catalog.to_dict('records')`. For each value: Computes `type_code` from `row['type_code_raw']`. Computes `subtype_code` from `row['subtype_code_raw']`. Checks `not isinstance(type_code, str) or CODE_PATTERN.fullmatch(type_code) is None`. When true: Raises `BessPlanningFeatureApplicationError('Feature type code is not an exact two-character string')`. Executes 6 additional source-ordered statement(s).
8. Computes `output` from `catalog.copy(deep=True)`.
9. Calls `_assign_policy_columns(output, policy_rows)` for its validation or side effect.
10. Computes `applied` from `gpd.GeoDataFrame(output, geometry=catalog.geometry.name, crs=catalog.crs)`.
11. Calls `_validate_application_geometry(applied, 'applied feature catalog')` for its validation or side effect.
12. Returns `applied`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(catalog, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `any((column in catalog.columns for column in POLICY_COLUMNS))` is true.
- Rejects or diverts the path when `not required.issubset(catalog.columns)` is true.
- Rejects or diverts the path when `not isinstance(type_code, str) or CODE_PATTERN.fullmatch(type_code) is None` is true.
- Rejects or diverts the path when `not isinstance(subtype_code, str) or CODE_PATTERN.fullmatch(subtype_code) is None` is true.
- Rejects or diverts the path when `official_status == 'RESOLVED_OFFICIAL'` is true.
- Rejects or diverts the path when `policy_row is None` is true.
- Rejects or diverts the path when `official_status == 'UNKNOWN_CODE_PAIR'` is true.
- Rejects or diverts the path when `policy_row is not None` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `catalog.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessPlanningFeatureApplicationError`, `CODE_PATTERN.fullmatch`, `_assign_policy_columns`, `_policy_lookup`, `_policy_values`, `_validate_application_geometry`, `any`, `catalog.copy`, `catalog.to_dict`, `gpd.GeoDataFrame`, `isinstance`, `lookup.get`, `policy_rows.append`, `required.issubset`, `str`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_feature_rows_by_id`

**Signature**

```python
def _feature_rows_by_id(
    *catalogs: gpd.GeoDataFrame,
) -> dict[str, dict[str, object]]:
```

**Purpose**

Implements feature rows by id according to the exact implementation and guards in this file.

**Inputs**

- `*catalogs` (`gpd.GeoDataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, dict[str, object]]`. Observed return expression(s): `indexed`.

**Algorithm**

1. Defines `indexed` with annotation `dict[str, dict[str, object]]` from `{}`.
2. Iterates `catalog` over `catalogs`. For each value: Iterates `row` over `catalog.to_dict('records')`. For each value: Computes `feature_id` from `row['planning_feature_id']`. Checks `not isinstance(feature_id, str) or not feature_id`. When true: Raises `BessPlanningFeatureApplicationError('Enriched feature ID must be an exact string')`. Checks `feature_id in indexed`. When true: Raises `BessPlanningFeatureApplicationError('Enriched planning feature ID is not globally unique')`. Executes 1 additional source-ordered statement(s).
3. Returns `indexed`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(feature_id, str) or not feature_id` is true.
- Rejects or diverts the path when `feature_id in indexed` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`, `catalog.to_dict`, `isinstance`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_apply_relations`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_apply_relations`

**Signature**

```python
def _apply_relations(
    relations: pd.DataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

**Purpose**

Propagate feature policy to relations only through planning_feature_id.

**Inputs**

- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `_assign_policy_columns(output, policy_rows)`.

**Algorithm**

1. Checks `not isinstance(relations, pd.DataFrame) or isinstance(relations, gpd.GeoDataFrame)`. When true: Raises `BessPlanningFeatureApplicationError('Coded relations must be a DataFrame')`.
2. Checks `any((column in relations.columns for column in POLICY_COLUMNS))`. When true: Raises `BessPlanningFeatureApplicationError('Coded relations already contain BESS policy columns')`.
3. Computes `required` from `{'planning_feature_id', *RELATION_FEATURE_AGREEMENT_COLUMNS}`.
4. Checks `not required.issubset(relations.columns)`. When true: Raises `BessPlanningFeatureApplicationError('Coded relations lack feature-policy agreement fields')`.
5. Computes `features` from `_feature_rows_by_id(surface_features, line_features, point_features)`.
6. Defines `policy_rows` with annotation `list[dict[str, object]]` from `[]`.
7. Iterates `relation` over `relations.to_dict('records')`. For each value: Computes `feature_id` from `relation['planning_feature_id']`. Computes `feature` from `features.get(str(feature_id))`. Checks `feature is None`. When true: Raises `BessPlanningFeatureApplicationError(f'Relation references unknown planning feature ID: {feature_id!r}')`. Executes 2 additional source-ordered statement(s).
8. Computes `output` from `relations.copy(deep=True)`.
9. Returns `_assign_policy_columns(output, policy_rows)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(relations, pd.DataFrame) or isinstance(relations, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `any((column in relations.columns for column in POLICY_COLUMNS))` is true.
- Rejects or diverts the path when `not required.issubset(relations.columns)` is true.
- Rejects or diverts the path when `feature is None` is true.
- Rejects or diverts the path when `not _null_safe_equal(relation[column], feature[column])` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `relations.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessPlanningFeatureApplicationError`, `_assign_policy_columns`, `_feature_rows_by_id`, `_null_safe_equal`, `any`, `features.get`, `isinstance`, `policy_rows.append`, `relations.copy`, `relations.to_dict`, `required.issubset`, `str`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_component_metadata`

**Signature**

```python
def _component_metadata(
    result: BessPlanningFeatureApplicationResult,
) -> dict[str, object]:
```

**Purpose**

Implements component metadata according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'result_hash_schema_version': result.result_hash_schema_version, 'application_scope': result.application_scope, 'policy_scope': result.policy_scope, 'local_feature_text_interpreted': result.local_feature_text_interpreted, 'local_regulation_content_interpreted': result.local_regulation_content_interpreted, 'legal_conclusion_produced': result.legal_conclusion_produced, 'parcel_status_aggregated': …`.

**Algorithm**

1. Returns `{'result_hash_schema_version': result.result_hash_schema_version, 'application_scope': result.application_scope, 'policy_scope': result.policy_scope, 'local_feature_text_interpreted': result.local_feature_text_interpreted, 'local_regulation_content_interpreted': result.local_regulation_content_interpreted, 'legal_conclusion_produced': result.legal_conclusio…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_complete_result_sha256`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_component_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_component_sha256`

**Signature**

```python
def _component_sha256(
    result: BessPlanningFeatureApplicationResult,
    frame: pd.DataFrame,
    role: str,
) -> str:
```

**Purpose**

Implements component sha256 according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `role` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256({'domain': f'landscout.bess_planning_feature_application.{role}', **_component_metadata(result), 'frame': _frame_payload(frame)})`.

**Algorithm**

1. Returns `_canonical_json_sha256({'domain': f'landscout.bess_planning_feature_application.{role}', **_component_metadata(result), 'frame': _frame_payload(frame)})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_json_sha256`, `_component_metadata`, `_frame_payload`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_result_with_hashes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_complete_result_sha256`

**Signature**

```python
def _complete_result_sha256(result: BessPlanningFeatureApplicationResult) -> str:
```

**Purpose**

Implements complete result sha256 according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_json_sha256({'domain': 'landscout.bess_planning_feature_application.result', **_component_metadata(result), 'surface_features_content_sha256': result.surface_features_content_sha256, 'line_features_content_sha256': result.line_features_content_sha256, 'point_features_content_sha256': result.point_features_content_sha256, 'relations_content_sha256': result.relations_content_sha256})`.

**Algorithm**

1. Returns `_canonical_json_sha256({'domain': 'landscout.bess_planning_feature_application.result', **_component_metadata(result), 'surface_features_content_sha256': result.surface_features_content_sha256, 'line_features_content_sha256': result.line_features_content_sha256, 'point_features_content_sha256': result.point_features_content_sha256, 'relations_content_sha256…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_json_sha256`, `_component_metadata`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_result_with_hashes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_result_with_hashes`

**Signature**

```python
def _result_with_hashes(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Implements result with hashes according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationResult`. Observed return expression(s): `replace(components, complete_result_content_sha256=_complete_result_sha256(components))`.

**Algorithm**

1. Computes `components` from `replace(result, surface_features_content_sha256=_component_sha256(result, result.surface_features, 'surface_features'), line_features_content_sha256=_component_sha256(result, result.line_features, 'line_features'), point_features_content_sha256=_component_sha256(result, result.point_features, 'point_features'), relati…`.
2. Returns `replace(components, complete_result_content_sha256=_complete_result_sha256(components))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_complete_result_sha256`, `_component_sha256`, `replace`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_build_result`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_result`

**Signature**

```python
def _build_result(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Builds result according to the exact implementation and guards in this file.

**Inputs**

- `coded` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessPlanningFeaturePolicyResult`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationResult`. Observed return expression(s): `_result_with_hashes(result)`.

**Algorithm**

1. Computes `surface` from `_apply_feature_catalog(coded.surface_features, policy)`.
2. Computes `line` from `_apply_feature_catalog(coded.line_features, policy)`.
3. Computes `point` from `_apply_feature_catalog(coded.point_features, policy)`.
4. Computes `relations` from `_apply_relations(coded.relations, surface, line, point)`.
5. Computes `result` from `BessPlanningFeatureApplicationResult(result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION, application_scope=APPLICATION_SCOPE, policy_scope=policy.policy_scope, local_feature_text_interpreted=False, local_regulation_content_interpreted=False, legal_conclusion_produced=False, parcel_status_aggregated=False, parcel_re…`.
6. Returns `_result_with_hashes(result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationResult`, `_apply_feature_catalog`, `_apply_relations`, `_result_with_hashes`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `apply_bess_planning_feature_policy`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `load_bess_planning_feature_application_artifacts`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `validate_bess_planning_feature_application_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_relation_rows`

**Signature**

```python
def _validate_relation_rows(
    frame: pd.DataFrame,
    label: str,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[dict[int, str], dict[str, int]]:
```

**Purpose**

Validates and rejects malformed relation rows according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[dict[int, str], dict[str, int]]`. Observed return expression(s): `validate_bess_application_relation_frame(frame, label=label, policy_profile=result.policy_profile, policy_sha256=result.policy_sha256, policy_result_sha256=result.policy_complete_result_content_sha256, source_document_id=result.source_document_id, source_archive_sha256=result.source_archive_sha256, cnig_profile=result.cnig_profile, cnig_profile_sha256=result.cnig_profile_sha256)`.

**Algorithm**

1. Runs guarded operation: Returns `validate_bess_application_relation_frame(frame, label=label, policy_profile=result.policy_profile, policy_sha256=result.policy_sha256, policy_result_sha256=result.policy_complete_result_content_sha256, source_document_id=result.source_document_id, source_archive_sha256=result.source_archive_sha256, cnig_profile=result.cnig_profile, cnig_profile_sha256=resul…`. Handles `(TypeError, ValueError)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`, `str`, `validate_bess_application_relation_frame`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result_envelope`

**Signature**

```python
def _validate_result_envelope(result: BessPlanningFeatureApplicationResult) -> None:
```

**Purpose**

Validates and rejects malformed result envelope according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `not isinstance(result, BessPlanningFeatureApplicationResult)`. When true: Raises `BessPlanningFeatureApplicationError('result must be a BessPlanningFeatureApplicationResult')`.
2. Checks `type(result.result_hash_schema_version) is not int or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`. When true: Raises `BessPlanningFeatureApplicationError('unsupported result hash schema')`.
3. Checks `result.application_scope != APPLICATION_SCOPE or result.policy_scope != POLICY_SCOPE`. When true: Raises `BessPlanningFeatureApplicationError('application result scope is invalid')`.
4. Iterates `(exact_value, label)` over `((result.policy_profile, 'policy_profile'), (result.cnig_profile, 'cnig_profile'), (result.source_document_id, 'source_document_id'))`. For each value: Runs guarded operation: Calls `_exact_string(exact_value, label)` for its validation or side effect. Handles `ValueError`.
5. Checks `result.policy_result_hash_schema_version != 1`. When true: Raises `BessPlanningFeatureApplicationError('policy result hash schema must be exactly 1')`.
6. Checks `result.cnig_result_hash_schema_version != 5`. When true: Raises `BessPlanningFeatureApplicationError('CNIG result hash schema must be exactly 5')`.
7. Checks `any((value is not False for value in (result.local_feature_text_interpreted, result.local_regulation_content_interpreted, result.legal_conclusion_produced, result.parcel_status_aggregated, result.parcel_rejection_performed, result.score_calculated)))`. When true: Raises `BessPlanningFeatureApplicationError('application result boundary flags must all be false')`.
8. Iterates `(frame, label)` over `((result.surface_features, 'surface features'), (result.line_features, 'line features'), (result.point_features, 'point features'))`. For each value: Checks `not isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `BessPlanningFeatureApplicationError(f'{label} must be geospatial')`. Checks `frame.columns.duplicated().any()`. When true: Raises `BessPlanningFeatureApplicationError(f'{label} policy schema is invalid')`. Calls `deterministic_frame_schema_signature(frame)` for its validation or side effect.
9. Runs guarded operation: Computes `feature_mapping` from `validate_bess_application_feature_catalogs(result.surface_features, result.line_features, result.point_features, policy_profile=result.policy_profile, policy_sha256=result.policy_sha256, policy_result_sha256=result.policy_complete_result_content_sha256, source_document_id=result.source_document_id, source_archive_sha2…`. Handles `(TypeError, ValueError)`.
10. Checks `not isinstance(result.relations, pd.DataFrame) or isinstance(result.relations, gpd.GeoDataFrame)`. When true: Raises `BessPlanningFeatureApplicationError('relations must be a DataFrame')`.
11. Checks `result.relations.columns.duplicated().any()`. When true: Raises `BessPlanningFeatureApplicationError('relations policy schema is invalid')`.
12. Computes `relation_mapping` from `_validate_relation_rows(result.relations, 'relations', result)`.
13. Checks `any((feature_mapping[0].get(priority) != status for priority, status in relation_mapping[0].items())) or any((feature_mapping[1].get(status) != priority for status, priority in relation_mapping[1].items()))`. When true: Raises `BessPlanningFeatureApplicationError('relation policy mapping differs from the feature mapping')`.
14. Computes `feature_rows` from `_feature_rows_by_id(result.surface_features, result.line_features, result.point_features)`.
15. Iterates `relation` over `result.relations.to_dict('records')`. For each value: Computes `feature` from `feature_rows.get(str(relation['planning_feature_id']))`. Checks `feature is None`. When true: Raises `BessPlanningFeatureApplicationError('Application relation references an unknown feature')`. Iterates `column` over `(*RELATION_FEATURE_AGREEMENT_COLUMNS, *POLICY_COLUMNS)`. For each value: Checks `not _null_safe_equal(relation[column], feature[column])`. When true: Raises `BessPlanningFeatureApplicationError(f'Application relation {column} differs from its feature')`. Executes 4 additional source-ordered statement(s).
16. Iterates `field` over `RESULT_SCALAR_FIELDS`. For each value: Checks `field.endswith('sha256')`. When true: Runs guarded operation: Calls `_sha256_string(getattr(result, field), field)` for its validation or side effect. Handles `ValueError`.
17. Computes `rebuilt` from `_result_with_hashes(result)`.
18. Iterates `field` over `('surface_features_content_sha256', 'line_features_content_sha256', 'point_features_content_sha256', 'relations_content_sha256', 'complete_result_content_sha256')`. For each value: Checks `getattr(result, field) != getattr(rebuilt, field)`. When true: Raises `BessPlanningFeatureApplicationError(f'{field} is invalid')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(result, BessPlanningFeatureApplicationResult)` is true.
- Rejects or diverts the path when `type(result.result_hash_schema_version) is not int or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `result.application_scope != APPLICATION_SCOPE or result.policy_scope != POLICY_SCOPE` is true.
- Rejects or diverts the path when `result.policy_result_hash_schema_version != 1` is true.
- Rejects or diverts the path when `result.cnig_result_hash_schema_version != 5` is true.
- Rejects or diverts the path when `any((value is not False for value in (result.local_feature_text_interpreted, result.local_regulation_content_interpreted, result.legal_conclusion_produced, result.parcel_status_aggregated, result.parcel_rejection_performed, result.score_calculated)))` is true.
- Rejects or diverts the path when `not isinstance(result.relations, pd.DataFrame) or isinstance(result.relations, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `result.relations.columns.duplicated().any()` is true.
- Rejects or diverts the path when `any((feature_mapping[0].get(priority) != status for priority, status in relation_mapping[0].items())) or any((feature_mapping[1].get(status) != priority for status, priority in relation_mapping[1].items()))` is true.
- Rejects or diverts the path when `not isinstance(frame, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `frame.columns.duplicated().any()` is true.
- Rejects or diverts the path when `feature is None` is true.
- Rejects or diverts the path when `not metric_equal` is true.
- Rejects or diverts the path when `field.endswith('sha256')` is true.
- Rejects or diverts the path when `getattr(result, field) != getattr(rebuilt, field)` is true.
- Rejects or diverts the path when `not _null_safe_equal(relation[column], feature[column])` is true.
- Rejects or diverts the path when `isinstance(actual_value, bool) or not isinstance(actual_value, Real) or isinstance(expected_value, bool) or (not isinstance(expected_value, Real))` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`, `_exact_string`, `_feature_rows_by_id`, `_null_safe_equal`, `_result_with_hashes`, `_sha256_string`, `_validate_relation_rows`, `abs`, `any`, `deterministic_frame_schema_signature`, `feature_mapping[0].get`, `feature_mapping[1].get`, `feature_rows.get`, `field.endswith`, `float`, `frame.columns.duplicated`, `frame.columns.duplicated().any`, `getattr`, `isinstance`, `max`, `relation_mapping[0].items`, `relation_mapping[1].items`, `result.relations.columns.duplicated`, `result.relations.columns.duplicated().any`, `result.relations.to_dict`, `str`, `technical_overlay_tolerance`, `type`, `validate_bess_application_feature_catalogs`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `apply_bess_planning_feature_policy`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `load_bess_planning_feature_application_artifacts`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `validate_bess_planning_feature_application_result_envelope`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `validate_bess_planning_feature_application_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_bess_planning_feature_application_result_envelope`

**Signature**

```python
def validate_bess_planning_feature_application_result_envelope(
    result: BessPlanningFeatureApplicationResult,
) -> None:
```

**Purpose**

Validate one application envelope without reconstructing source inputs.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Calls `_validate_result_envelope(result)` for its validation or side effect.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_validate_result_envelope`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `load_bess_planning_feature_parcel_aggregation_artifacts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_coded_policy_compatibility`

**Signature**

```python
def _validate_coded_policy_compatibility(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
```

**Purpose**

Validates and rejects malformed coded policy compatibility according to the exact implementation and guards in this file.

**Inputs**

- `coded` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessPlanningFeaturePolicyResult`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `comparisons` from `((policy.source_document_id, coded.source_document_id, 'document ID'), (policy.source_archive_sha256, coded.source_archive_sha256, 'archive SHA256'), (policy.cnig_profile, coded.profile, 'CNIG profile'), (policy.cnig_profile_schema_version, coded.profile_schema_version, 'CNIG profile schema'), (policy.cnig_profile_sha…`.
2. Iterates `(actual, expected, label)` over `comparisons`. For each value: Checks `actual != expected`. When true: Raises `BessPlanningFeatureApplicationError(f'Policy and coded result differ for {label}')`.
3. Computes `coded_rows` from `{(row['feature_family'], row['type_code'], row['subtype_code']): row for row in coded.code_dictionary.to_dict('records')}`.
4. Computes `policy_rows` from `{(row['feature_family'], row['type_code'], row['subtype_code']): row for row in policy.policy_table.to_dict('records')}`.
5. Checks `not coded_rows or not policy_rows`. When true: Raises `BessPlanningFeatureApplicationError('Policy and code dictionary pair sets must be non-empty')`.
6. Checks `set(policy_rows) != set(coded_rows)`. When true: Raises `BessPlanningFeatureApplicationError('Policy and code dictionary pair sets differ')`.
7. Iterates `(key, coded_row)` over `coded_rows.items()`. For each value: Computes `policy_row` from `policy_rows[key]`. Computes `meaning_comparisons` from `((policy_row['official_label'], coded_row['official_label']), (policy_row['official_legal_reference'], coded_row['legal_reference']), (policy_row['official_regulation_reference'], coded_row['regulation_or_annex_reference']))`. Checks `any((not _null_safe_equal(actual, expected) for actual, expected in meaning_comparisons))`. When true: Raises `BessPlanningFeatureApplicationError(f'Policy official meaning differs from code dictionary for pair {key}')`.

**Validation and invariants**

- Rejects or diverts the path when `not coded_rows or not policy_rows` is true.
- Rejects or diverts the path when `set(policy_rows) != set(coded_rows)` is true.
- Rejects or diverts the path when `actual != expected` is true.
- Rejects or diverts the path when `any((not _null_safe_equal(actual, expected) for actual, expected in meaning_comparisons))` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`, `_null_safe_equal`, `any`, `coded.code_dictionary.to_dict`, `coded_rows.items`, `policy.policy_table.to_dict`, `set`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `load_bess_planning_feature_application_artifacts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_source_locks`

**Signature**

```python
def _validate_source_locks(
    result: BessPlanningFeatureApplicationResult
    | BessPlanningFeatureApplicationArtifactManifest,
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
```

**Purpose**

Validates and rejects malformed source locks according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureApplicationResult | BessPlanningFeatureApplicationArtifactManifest`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessPlanningFeaturePolicyResult`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `comparisons` from `((result.policy_profile, policy.policy_profile, 'policy profile'), (result.policy_sha256, policy.policy_sha256, 'policy SHA256'), (result.policy_result_hash_schema_version, policy.result_hash_schema_version, 'policy result hash schema'), (result.policy_complete_result_content_sha256, policy.complete_result_content_sha…`.
2. Iterates `(actual, expected, label)` over `comparisons`. For each value: Checks `actual != expected`. When true: Raises `BessPlanningFeatureApplicationError(f'Application source lock differs for {label}')`.
3. Computes `policy_coded_comparisons` from `((policy.source_document_id, coded.source_document_id, 'policy document ID'), (policy.source_archive_sha256, coded.source_archive_sha256, 'policy archive SHA256'), (policy.cnig_profile, coded.profile, 'policy CNIG profile'), (policy.cnig_profile_schema_version, coded.profile_schema_version, 'policy CNIG profile schema…`.
4. Iterates `(actual, expected, label)` over `policy_coded_comparisons`. For each value: Checks `actual != expected`. When true: Raises `BessPlanningFeatureApplicationError(f'Application source lock differs for {label}')`.

**Validation and invariants**

- Rejects or diverts the path when `actual != expected` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `load_bess_planning_feature_application_artifacts`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `validate_bess_planning_feature_application_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_policy_source`

**Signature**

```python
def _validate_policy_source(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    policy_result: BessPlanningFeaturePolicyResult,
) -> None:
```

**Purpose**

Validates and rejects malformed policy source according to the exact implementation and guards in this file.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `code_profile` (`CnigFeatureCodeProfile | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded_result` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_config` (`BessPlanningFeaturePolicyConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_result` (`BessPlanningFeaturePolicyResult`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `validate_bess_planning_feature_policy_result(planning_document, parcels, surface_features, line_features, point_features, relations, code_profile, coded_result, policy_config, policy_result)` for its validation or side effect. Handles `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`, `validate_bess_planning_feature_policy_result`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `apply_bess_planning_feature_policy`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `validate_bess_planning_feature_application_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `apply_bess_planning_feature_policy`

**Signature**

```python
def apply_bess_planning_feature_policy(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    policy_result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Validate once, then propagate exact compiled policy to features and relations.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `code_profile` (`CnigFeatureCodeProfile | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded_result` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_config` (`BessPlanningFeaturePolicyConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_result` (`BessPlanningFeaturePolicyResult`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationResult`. Observed return expression(s): `result`.

**Algorithm**

1. Runs guarded operation: Calls `_validate_policy_source(planning_document, parcels, surface_features, line_features, point_features, relations, code_profile, coded_result, policy_config, policy_result)` for its validation or side effect. Computes `result` from `_build_result(coded_result, policy_result)`. Calls `_validate_result_envelope(result)` for its validation or side effect. Returns `result`. Handles `BessPlanningFeatureApplicationError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`, `_build_result`, `_validate_policy_source`, `_validate_result_envelope`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `_application_fixture`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_feature_and_relation_inputs_are_preserved_and_not_mutated`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_and_relation_inputs_are_preserved_and_not_mutated`

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

1. Checks `_frame_payload(actual) != _frame_payload(expected)`. When true: Raises `BessPlanningFeatureApplicationError(f'Application {label} differs from rebuilt result')`.

**Validation and invariants**

- Rejects or diverts the path when `_frame_payload(actual) != _frame_payload(expected)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`, `_frame_payload`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `load_bess_planning_feature_application_artifacts`
- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `validate_bess_planning_feature_application_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_bess_planning_feature_application_result`

**Signature**

```python
def validate_bess_planning_feature_application_result(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    policy_result: BessPlanningFeaturePolicyResult,
    result: BessPlanningFeatureApplicationResult,
) -> None:
```

**Purpose**

Independently rebuild exact policy propagation from every source input.

**Inputs**

- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `code_profile` (`CnigFeatureCodeProfile | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded_result` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_config` (`BessPlanningFeaturePolicyConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_result` (`BessPlanningFeaturePolicyResult`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `_validate_result_envelope(result)` for its validation or side effect. Calls `_validate_source_locks(result, coded_result, policy_result)` for its validation or side effect. Calls `_validate_policy_source(planning_document, parcels, surface_features, line_features, point_features, relations, code_profile, coded_result, policy_config, policy_result)` for its validation or side effect. Computes `expected` from `_build_result(coded_result, policy_result)`. Executes 2 additional source-ordered statement(s). Handles `BessPlanningFeatureApplicationError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `getattr(result, field) != getattr(expected, field)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`, `_build_result`, `_compare_frame`, `_validate_policy_source`, `_validate_result_envelope`, `_validate_source_locks`, `getattr`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_application_source`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_coordinated_feature_or_relation_policy_mutation_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_lineage_defect_fast_fails_before_policy_source_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_valid_four_file_manifest_and_verified_byte_readback`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_feature_or_relation_policy_mutation_is_rejected`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation`
- `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_four_file_manifest_and_verified_byte_readback`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_unique_json_object`

**Signature**

```python
def _unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
```

**Purpose**

Implements unique json object according to the exact implementation and guards in this file.

**Inputs**

- `pairs` (`list[tuple[str, object]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `output`.

**Algorithm**

1. Defines `output` with annotation `dict[str, object]` from `{}`.
2. Iterates `(key, value)` over `pairs`. For each value: Checks `key in output`. When true: Raises `BessPlanningFeatureApplicationError(f'Duplicate JSON application artifact key: {key!r}')`. Computes `output[key]` from `value`.
3. Returns `output`.

**Validation and invariants**

- Rejects or diverts the path when `key in output` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureApplicationError`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_read_verified_artifact`

**Signature**

```python
def _read_verified_artifact(
    path: Path,
    record: BessPlanningFeatureApplicationArtifactRecord,
) -> pd.DataFrame:
```

**Purpose**

Reads and validates verified artifact according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `record` (`BessPlanningFeatureApplicationArtifactRecord`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Checks `path.name != record.filename`. When true: Raises `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} filename differs')`.
2. Computes `payload` from `path.read_bytes()`.
3. Checks `len(payload) != record.size_bytes`. When true: Raises `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} byte size differs')`.
4. Checks `sha256(payload).hexdigest() != record.sha256`. When true: Raises `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} SHA256 differs')`.
5. Computes `buffer` from `BytesIO(payload)`.
6. Defines `frame` with annotation `pd.DataFrame` without an initial value.
7. Checks `record.geospatial`. When true: Computes `frame` from `gpd.read_parquet(buffer)`. Otherwise: Computes `frame` from `pd.read_parquet(buffer)`.
8. Checks `len(frame) != record.row_count`. When true: Raises `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} row count differs')`.
9. Computes `signature` from `deterministic_frame_schema_signature(frame)`.
10. Checks `signature != record.frame_schema_signature`. When true: Raises `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} frame schema differs')`.
11. Checks `record.geospatial`. When true: Checks `not isinstance(frame, gpd.GeoDataFrame) or frame.crs is None`. When true: Raises `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} geospatial contract differs')`. Checks `CRS.from_user_input(frame.crs).to_json_dict() != record.crs`. When true: Raises `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} CRS differs')`. Otherwise: Checks `isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `BessPlanningFeatureApplicationError('Relations artifact unexpectedly loaded as geospatial')`.
12. Returns `frame`.

**Validation and invariants**

- Rejects or diverts the path when `path.name != record.filename` is true.
- Rejects or diverts the path when `len(payload) != record.size_bytes` is true.
- Rejects or diverts the path when `sha256(payload).hexdigest() != record.sha256` is true.
- Rejects or diverts the path when `len(frame) != record.row_count` is true.
- Rejects or diverts the path when `signature != record.frame_schema_signature` is true.
- Rejects or diverts the path when `record.geospatial` is true.
- Rejects or diverts the path when `not isinstance(frame, gpd.GeoDataFrame) or frame.crs is None` is true.
- Rejects or diverts the path when `CRS.from_user_input(frame.crs).to_json_dict() != record.crs` is true.
- Rejects or diverts the path when `isinstance(frame, gpd.GeoDataFrame)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `gpd.read_parquet`, `path.read_bytes`, `pd.read_parquet`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessPlanningFeatureApplicationError`, `BytesIO`, `CRS.from_user_input`, `CRS.from_user_input(frame.crs).to_json_dict`, `deterministic_frame_schema_signature`, `gpd.read_parquet`, `isinstance`, `len`, `path.read_bytes`, `pd.read_parquet`, `sha256`, `sha256(payload).hexdigest`.

**Known repository callers**

- `src/landscout/stages/apply_bess_planning_feature_policy.py` — `load_bess_planning_feature_application_artifacts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_bess_planning_feature_application_artifacts`

**Signature**

```python
def load_bess_planning_feature_application_artifacts(
    manifest_path: str | Path,
    surface_features_path: str | Path,
    line_features_path: str | Path,
    point_features_path: str | Path,
    relations_path: str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Load byte-sealed outputs and bind them to exact validated upstream results.

**Inputs**

- `manifest_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `surface_features_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `line_features_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `point_features_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `coded_result` (`PlanningFeatureCodeResult`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_result` (`BessPlanningFeaturePolicyResult`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureApplicationResult`. Observed return expression(s): `result`.

**Algorithm**

1. Runs guarded operation: Calls `validate_planning_feature_code_result_envelope(coded_result)` for its validation or side effect. Calls `validate_bess_planning_feature_policy_result_envelope(policy_result)` for its validation or side effect. Calls `_validate_coded_policy_compatibility(coded_result, policy_result)` for its validation or side effect. Computes `payload` from `json.loads(Path(manifest_path).read_text(encoding='utf-8'), object_pairs_hook=_unique_json_object)`. Executes 11 additional source-ordered statement(s). Handles `BessPlanningFeatureApplicationError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `getattr(result, field) != getattr(expected, field)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureApplicationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `Path(manifest_path).read_text`, `_read_verified_artifact`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessPlanningFeatureApplicationArtifactManifest.model_validate`, `BessPlanningFeatureApplicationError`, `BessPlanningFeatureApplicationResult`, `Path`, `Path(manifest_path).read_text`, `_build_result`, `_compare_frame`, `_read_verified_artifact`, `_validate_coded_policy_compatibility`, `_validate_result_envelope`, `_validate_source_locks`, `getattr`, `json.loads`, `validate_bess_planning_feature_policy_result_envelope`, `validate_planning_feature_code_result_envelope`.

**Known repository callers**

- `tests/unit/test_apply_bess_planning_feature_policy.py` — `load_bess_planning_feature_application_artifacts`
- `tests/unit/test_apply_bess_planning_feature_policy.py` — `test_application_loader_rejects_bad_upstream_before_artifact_reads`

**Tests**

- `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_bad_upstream_before_artifact_reads`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LINE_FEATURES` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `OFFICIAL_CNIG_CODE_MEANING_ONLY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `POINT_FEATURES` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `RELATIONS` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `SURFACE_FEATURES` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_status_priority` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `feature_family` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `legal_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `limitations` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `logical_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_profile_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_source_url` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_code_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `official_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_legal_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `official_regulation_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `rationale` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `regulation_filename_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `regulation_or_annex_reference` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `required_human_action` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_identity_field` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_identity_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_validity_date_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `status_priority` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `subtype_code` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `subtype_code_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `text_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
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
