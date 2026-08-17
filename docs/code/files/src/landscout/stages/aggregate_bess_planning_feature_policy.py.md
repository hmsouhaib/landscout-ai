# `src/landscout/stages/aggregate_bess_planning_feature_policy.py`

## File identity

- Repository path: `src/landscout/stages/aggregate_bess_planning_feature_policy.py`
- File type: Python source
- Primary responsibility: Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.
- Layer / domain: `stage` / `planning`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `d715ed2a3127c6b7e2d5c87158f7719a1f5ff0365930e465efab3e8e9b184a3a`

## 1. Purpose

Aggregates source-bound planning feature-policy relation evidence into parcel-level precheck summaries.

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
- `from pathlib import Path, PurePosixPath, PureWindowsPath` — required by the implementation paths and symbols documented below.
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
- `from landscout.common.bess_application_contract import ( ALLOWED_CONFIDENCES, ALLOWED_PRECHECK_STATUSES, NULL_LITERALS, POLICY_SCOPE, validate_bess_application_relation_frame, )` — required by the implementation paths and symbols documented below.
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature` — required by the implementation paths and symbols documented below.
- `from landscout.common.planning_overlay import technical_overlay_tolerance` — required by the implementation paths and symbols documented below.
- `from landscout.sources.gpu_fr import GpuPlanningDocument` — required by the implementation paths and symbols documented below.
- `from landscout.stages.apply_bess_planning_feature_policy import ( BessPlanningFeatureApplicationResult, validate_bess_planning_feature_application_result, validate_bess_planning_feature_application_result_envelope, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.bess_planning_feature_policy import ( BessPlanningFeaturePolicyConfig, BessPlanningFeaturePolicyResult, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.resolve_planning_feature_codes import ( CnigFeatureCodeProfile, PlanningFeatureCodeResult, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `RESULT_HASH_SCHEMA_VERSION` | `1` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARTIFACT_MANIFEST_SCHEMA_VERSION` | `1` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `APPLICATION_RESULT_HASH_SCHEMA_VERSION` | `2` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `AGGREGATION_SCOPE` | `"PARCEL_POLICY_AGGREGATION_ONLY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CONFIDENCE_METHOD` | `"LOWEST_CONFIDENCE_FOR_SELECTED_STATUS"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARTIFACT_KIND` | `"BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CONTROLLING_RELATION_TYPES` | `frozenset({"AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CONTEXT_RELATION_TYPES` | `frozenset({"TOUCH_ONLY", "BOUNDARY_TOUCH"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `AGGREGATION_STATUSES` | `frozenset( { "AGGREGATED_EXACT_POLICY", "UNRESOLVED_CONTROLLING_CODE_PAIR", "TOUCH_ONLY_RELATIONS_ONLY", "NO_PLANNING_FEATURE_RELATION", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATION_ROLES` | `frozenset( { "SELECTED_CONTROLLING", "LOWER_PRIORITY_CONTROLLING", "DEFERRED_BY_UNRESOLVED_CONTROLLING", "UNRESOLVED_CONTROLLING", "TOUCH_ONLY_CONTEXT", } )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CONFIDENCE_RANK` | `{"LOW": 0, "MEDIUM": 1, "HIGH": 2}` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SHA_PATTERN` | `re.compile(r"[0-9a-f]{64}")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_COLUMNS` | `( "bess_cnig_parcel_aggregation_status", "bess_cnig_parcel_precheck_status", "bess_cnig_parcel_precheck_confidence", "bess_cnig_parcel_status_priority", "bess_cnig_controlling_relation_count", "bess_cnig_exact_controlling_relation_count", "bess_cnig_unresolved_controlling_relation_count", "bess_cnig_touch_only_relation_count", "bess_cnig_selected_relation_count", "bess_cnig_lower_priority_controlling_relation_count", "bess_cnig_distinct_exact_status_count", "bess_cnig_multiple_exact_statuses", "bess_cnig_selected_feature_ids_json", "bess_cnig_unresolved_feature_ids_json", "bess_cnig_touch_only_feature_ids_json", "bess_cnig_confidence_aggregation_method", "bess_cnig_formal_review_required", "bess_cnig_aggregation_scope", "bess_cnig_policy_scope", "bess_cnig_local_feature_text_interpreted", "bess_cnig_local_regulation_content_interpreted", "bess_cnig_legal_conclusion_produced", "bess_cnig_parcel_status_aggregated", "bess_cnig_parcel_rejection_performed", "bess_cnig_score_calculated", "bess_cnig_policy_profile", "bess_cnig_policy_sha256", "bess_cnig_policy_result_sha256", "bess_cnig_application_result_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATION_COLUMNS` | `( "bess_cnig_parcel_relation_role", "bess_cnig_selected_for_parcel_status", "bess_cnig_resulting_parcel_aggregation_status", "bess_cnig_resulting_parcel_precheck_status", "bess_cnig_resulting_parcel_precheck_confidence", "bess_cnig_resulting_parcel_status_priority", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_STRING_COLUMNS` | `( "bess_cnig_parcel_aggregation_status", "bess_cnig_parcel_precheck_status", "bess_cnig_parcel_precheck_confidence", "bess_cnig_selected_feature_ids_json", "bess_cnig_unresolved_feature_ids_json", "bess_cnig_touch_only_feature_ids_json", "bess_cnig_confidence_aggregation_method", "bess_cnig_aggregation_scope", "bess_cnig_policy_scope", "bess_cnig_policy_profile", "bess_cnig_policy_sha256", "bess_cnig_policy_result_sha256", "bess_cnig_application_result_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_INTEGER_COLUMNS` | `( "bess_cnig_parcel_status_priority", "bess_cnig_controlling_relation_count", "bess_cnig_exact_controlling_relation_count", "bess_cnig_unresolved_controlling_relation_count", "bess_cnig_touch_only_relation_count", "bess_cnig_selected_relation_count", "bess_cnig_lower_priority_controlling_relation_count", "bess_cnig_distinct_exact_status_count", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_BOOL_COLUMNS` | `( "bess_cnig_multiple_exact_statuses", "bess_cnig_formal_review_required", "bess_cnig_local_feature_text_interpreted", "bess_cnig_local_regulation_content_interpreted", "bess_cnig_legal_conclusion_produced", "bess_cnig_parcel_status_aggregated", "bess_cnig_parcel_rejection_performed", "bess_cnig_score_calculated", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RELATION_STRING_COLUMNS` | `( "bess_cnig_parcel_relation_role", "bess_cnig_resulting_parcel_aggregation_status", "bess_cnig_resulting_parcel_precheck_status", "bess_cnig_resulting_parcel_precheck_confidence", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ARTIFACT_ROLES` | `("PARCELS", "RELATION_ASSESSMENTS")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RESULT_FRAME_FIELDS` | `("relation_assessments", "parcels")` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RESULT_SCALAR_FIELDS` | `tuple( field for field in BessPlanningFeatureParcelAggregationResult.__dataclass_fields__ if field not in RESULT_FRAME_FIELDS )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `BessPlanningFeatureParcelAggregationError`

**Purpose:** Raised when parcel aggregation integrity cannot be proven.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `_ApplicationLineage`

**Purpose:** Groups the `ApplicationLineage` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `source_document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `source_archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_profile` | `str` | `required` | `str` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cnig_profile_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `policy_profile` | `str` | `required` | `str` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `policy_complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |

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

### `BessPlanningFeatureParcelAggregationArtifactRecord`

**Purpose:** Groups the `BessPlanningFeatureParcelAggregationArtifactRecord` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `_StrictModel`.

**Model form and mutability:** class inheriting from `_StrictModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `artifact_role` | `ArtifactRole` | `required` | `ArtifactRole` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `filename` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `row_count` | `StrictInt` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `size_bytes` | `StrictInt` | `required` | `StrictInt` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `sha256` | `StrictStr` | `required` | Lowercase SHA256 binding the exact relevant bytes. |
| `frame_schema_signature` | `dict[StrictStr, object]` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |
| `geospatial` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `crs` | `dict[StrictStr, object] | None` | `required` | `dict[StrictStr, object] | None` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_record` — `def _validate_record(self) -> BessPlanningFeatureParcelAggregationArtifactRecord:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `BessPlanningFeatureParcelAggregationResult`

**Purpose:** Carries an immutable stage/result envelope whose fields and hashes are consumed by downstream validation.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `result_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `aggregation_scope` | `str` | `required` | `str` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_scope` | `str` | `required` | `str` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `local_feature_text_interpreted` | `bool` | `required` | `bool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `local_regulation_content_interpreted` | `bool` | `required` | `bool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `legal_conclusion_produced` | `bool` | `required` | `bool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parcel_status_aggregated` | `bool` | `required` | `bool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parcel_rejection_performed` | `bool` | `required` | `bool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `score_calculated` | `bool` | `required` | `bool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `source_archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_profile` | `str` | `required` | `str` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cnig_profile_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `policy_profile` | `str` | `required` | `str` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `policy_complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `application_result_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `application_complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_parcels_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_application_relations_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `relation_assessments_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `parcels_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `relation_assessments` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parcels` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |

**Validators and methods:**

- None.

### `BessPlanningFeatureParcelAggregationArtifactManifest`

**Purpose:** Groups the `BessPlanningFeatureParcelAggregationArtifactManifest` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `_StrictModel`.

**Model form and mutability:** class inheriting from `_StrictModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `StrictInt` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `artifact_kind` | `Literal['BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT']` | `required` | `Literal['BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT']` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `result_hash_schema_version` | `StrictInt` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `aggregation_scope` | `Literal['PARCEL_POLICY_AGGREGATION_ONLY']` | `required` | `Literal['PARCEL_POLICY_AGGREGATION_ONLY']` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_scope` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` | `required` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `local_feature_text_interpreted` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `local_regulation_content_interpreted` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `legal_conclusion_produced` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parcel_status_aggregated` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parcel_rejection_performed` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `score_calculated` | `StrictBool` | `required` | `StrictBool` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_document_id` | `StrictStr` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `source_archive_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_profile` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `cnig_profile_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `cnig_complete_result_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `policy_profile` | `StrictStr` | `required` | `StrictStr` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `policy_complete_result_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `application_result_hash_schema_version` | `StrictInt` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `application_complete_result_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_parcels_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_application_relations_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `relation_assessments_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `parcels_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `complete_result_content_sha256` | `StrictStr` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `artifacts` | `tuple[BessPlanningFeatureParcelAggregationArtifactRecord, ...]` | `required` | `tuple[BessPlanningFeatureParcelAggregationArtifactRecord, ...]` state used by `src/landscout/stages/aggregate_bess_planning_feature_policy.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_manifest` — `def _validate_manifest(         self,     ) -> BessPlanningFeatureParcelAggregationArtifactManifest:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

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

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_sha256_string`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_result_envelope`

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

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `BessPlanningFeatureParcelAggregationArtifactManifest._validate_manifest`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `BessPlanningFeatureParcelAggregationArtifactRecord._validate_record`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessPlanningFeatureParcelAggregationArtifactRecord._validate_record`

**Signature**

```python
def _validate_record(self) -> BessPlanningFeatureParcelAggregationArtifactRecord:
```

**Purpose**

Validates and rejects malformed record according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationArtifactRecord`. Observed return expression(s): `self`.

**Algorithm**

1. Calls `validate_portable_parquet_filename(self.filename, 'artifact filename')` for its validation or side effect.
2. Checks `type(self.row_count) is not int or self.row_count < 0`. When true: Raises `ValueError('artifact row_count must be non-negative')`.
3. Checks `type(self.size_bytes) is not int or self.size_bytes < 1`. When true: Raises `ValueError('artifact size_bytes must be positive')`.
4. Calls `_sha256_string(self.sha256, 'artifact SHA256')` for its validation or side effect.
5. Computes `expected_geo` from `self.artifact_role == 'PARCELS'`.
6. Checks `self.geospatial is not expected_geo`. When true: Raises `ValueError('artifact geospatial flag differs from its role')`.
7. Computes `signature_crs` from `self.frame_schema_signature.get('crs')`.
8. Checks `expected_geo`. When true: Checks `self.crs is None or signature_crs != self.crs`. When true: Raises `ValueError('parcel artifact CRS is missing or inconsistent')`. Otherwise: Checks `self.crs is not None or signature_crs is not None`. When true: Raises `ValueError('relation artifact must not declare CRS')`.
9. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `type(self.row_count) is not int or self.row_count < 0` is true.
- Rejects or diverts the path when `type(self.size_bytes) is not int or self.size_bytes < 1` is true.
- Rejects or diverts the path when `self.geospatial is not expected_geo` is true.
- Rejects or diverts the path when `expected_geo` is true.
- Rejects or diverts the path when `self.crs is None or signature_crs != self.crs` is true.
- Rejects or diverts the path when `self.crs is not None or signature_crs is not None` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_sha256_string`, `model_validator`, `self.frame_schema_signature.get`, `type`, `validate_portable_parquet_filename`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessPlanningFeatureParcelAggregationArtifactManifest._validate_manifest`

**Signature**

```python
def _validate_manifest(
        self,
    ) -> BessPlanningFeatureParcelAggregationArtifactManifest:
```

**Purpose**

Validates and rejects malformed manifest according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationArtifactManifest`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `type(self.schema_version) is not int or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION`. When true: Raises `ValueError('unsupported parcel aggregation artifact schema')`.
2. Checks `type(self.result_hash_schema_version) is not int or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`. When true: Raises `ValueError('unsupported parcel aggregation result schema')`.
3. Checks `any((value is not expected for value, expected in ((self.local_feature_text_interpreted, False), (self.local_regulation_content_interpreted, False), (self.legal_conclusion_produced, False), (self.parcel_status_aggregated, True), (self.parcel_rejection_performed, False), (self.score_calculated, False))))`. When true: Raises `ValueError('parcel aggregation boundary flags are invalid')`.
4. Iterates `field` over `RESULT_SCALAR_FIELDS`. For each value: Computes `value` from `getattr(self, field)`. Checks `field.endswith('sha256')`. When true: Calls `_sha256_string(value, field)` for its validation or side effect.
5. Checks `type(self.application_result_hash_schema_version) is not int or self.application_result_hash_schema_version != APPLICATION_RESULT_HASH_SCHEMA_VERSION`. When true: Raises `ValueError('application result schema must be exactly 2')`.
6. Computes `roles` from `tuple((record.artifact_role for record in self.artifacts))`.
7. Checks `roles != ARTIFACT_ROLES`. When true: Raises `ValueError('parcel aggregation artifact roles differ')`.
8. Computes `filenames` from `tuple((record.filename.casefold() for record in self.artifacts))`.
9. Checks `len(filenames) != len(set(filenames))`. When true: Raises `ValueError('parcel aggregation artifact filename is duplicated')`.
10. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `type(self.schema_version) is not int or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `type(self.result_hash_schema_version) is not int or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `any((value is not expected for value, expected in ((self.local_feature_text_interpreted, False), (self.local_regulation_content_interpreted, False), (self.legal_conclusion_produced, False), (self.parcel_status_aggregated, True), (self.parcel_rejection_performed, False), (self.score_calculated, False))))` is true.
- Rejects or diverts the path when `type(self.application_result_hash_schema_version) is not int or self.application_result_hash_schema_version != APPLICATION_RESULT_HASH_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `roles != ARTIFACT_ROLES` is true.
- Rejects or diverts the path when `len(filenames) != len(set(filenames))` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_sha256_string`, `any`, `field.endswith`, `getattr`, `len`, `model_validator`, `record.filename.casefold`, `set`, `tuple`, `type`.

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

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_canonical_value`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_local_domains`

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

- Declared return type: `object`. Observed return expression(s): `None`; `{'coordinate_dimension': dimension, 'wkb_hex': to_wkb(value, hex=True, output_dimension=2, byte_order=1, include_srid=False)}`; `value.isoformat()`; `_canonical_value(value.item())`; `value`; `int(value)`; `number`.

**Algorithm**

1. Computes `value` from `_null_value(value)`.
2. Checks `value is None`. When true: Returns `None`.
3. Checks `isinstance(value, BaseGeometry)`. When true: Computes `dimension` from `int(get_coordinate_dimension(value))`. Checks `dimension != 2`. When true: Raises `BessPlanningFeatureParcelAggregationError('Parcel aggregation geometry must be canonical 2D')`. Returns `{'coordinate_dimension': dimension, 'wkb_hex': to_wkb(value, hex=True, output_dimension=2, byte_order=1, include_srid=False)}`.
4. Checks `isinstance(value, (datetime, date, pd.Timestamp))`. When true: Returns `value.isoformat()`.
5. Checks `isinstance(value, np.generic)`. When true: Returns `_canonical_value(value.item())`.
6. Checks `isinstance(value, bool)`. When true: Returns `value`.
7. Checks `isinstance(value, Integral)`. When true: Returns `int(value)`.
8. Checks `isinstance(value, Real)`. When true: Computes `number` from `float(value)`. Checks `not math.isfinite(number)`. When true: Raises `BessPlanningFeatureParcelAggregationError('Aggregation payload contains non-finite data')`. Returns `number`.
9. Checks `isinstance(value, str)`. When true: Returns `value`.
10. Raises `BessPlanningFeatureParcelAggregationError(f'Unsupported aggregation integrity value {type(value).__name__}')`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, BaseGeometry)` is true.
- Rejects or diverts the path when `isinstance(value, Real)` is true.
- Rejects or diverts the path when `dimension != 2` is true.
- Rejects or diverts the path when `not math.isfinite(number)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `_canonical_value`, `_null_value`, `float`, `get_coordinate_dimension`, `int`, `isinstance`, `math.isfinite`, `to_wkb`, `type`, `value.isoformat`, `value.item`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_frame_payload`

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

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_compare_frame`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_frame_sha256`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_result_with_hashes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_sha256`

**Signature**

```python
def _canonical_sha256(value: object) -> str:
```

**Purpose**

Implements canonical sha256 according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `sha256(payload).hexdigest()`.

**Algorithm**

1. Runs guarded operation: Computes `payload` from `json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')`. Handles `(TypeError, ValueError)`.
2. Returns `sha256(payload).hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `json.dumps`, `json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode`, `sha256`, `sha256(payload).hexdigest`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_frame_sha256`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_result_with_hashes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_frame_sha256`

**Signature**

```python
def _frame_sha256(frame: pd.DataFrame, domain: str) -> str:
```

**Purpose**

Implements frame sha256 according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `domain` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': domain, 'result_hash_schema_version': RESULT_HASH_SCHEMA_VERSION, 'frame': _frame_payload(frame)})`.

**Algorithm**

1. Returns `_canonical_sha256({'domain': domain, 'result_hash_schema_version': RESULT_HASH_SCHEMA_VERSION, 'frame': _frame_payload(frame)})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `_frame_payload`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_build_result`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_result_envelope`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_source_locks`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_feature_id`

**Signature**

```python
def _validate_feature_id(value: object) -> str:
```

**Purpose**

Validates and rejects malformed feature id according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip() or (value in NULL_LITERALS) or PurePosixPath(value).is_absolute() or PureWindowsPath(value).is_absolute()`. When true: Raises `BessPlanningFeatureParcelAggregationError('Feature ID is not an exact portable string')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip() or (value in NULL_LITERALS) or PurePosixPath(value).is_absolute() or PureWindowsPath(value).is_absolute()` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `PurePosixPath`, `PurePosixPath(value).is_absolute`, `PureWindowsPath`, `PureWindowsPath(value).is_absolute`, `isinstance`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_json_ids`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_json_ids`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_json_ids`

**Signature**

```python
def _json_ids(values: list[object]) -> str:
```

**Purpose**

Implements json ids according to the exact implementation and guards in this file.

**Inputs**

- `values` (`list[object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `json.dumps(ids, ensure_ascii=False, allow_nan=False, separators=(',', ':'))`.

**Algorithm**

1. Computes `ids` from `sorted({_validate_feature_id(value) for value in values})`.
2. Returns `json.dumps(ids, ensure_ascii=False, allow_nan=False, separators=(',', ':'))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_validate_feature_id`, `json.dumps`, `sorted`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_parcel_summary`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_json_ids`

**Signature**

```python
def _validate_json_ids(value: object, label: str) -> None:
```

**Purpose**

Validates and rejects malformed json ids according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `not isinstance(value, str)`. When true: Raises `BessPlanningFeatureParcelAggregationError(f'{label} must be canonical JSON')`.
2. Runs guarded operation: Computes `parsed` from `json.loads(value)`. Handles `(TypeError, ValueError)`.
3. Checks `not isinstance(parsed, list)`. When true: Raises `BessPlanningFeatureParcelAggregationError(f'{label} must be a JSON array')`.
4. Computes `ids` from `[_validate_feature_id(item) for item in parsed]`.
5. Computes `canonical` from `json.dumps(sorted(set(ids)), ensure_ascii=False, allow_nan=False, separators=(',', ':'))`.
6. Checks `len(ids) != len(set(ids)) or ids != sorted(ids) or value != canonical`. When true: Raises `BessPlanningFeatureParcelAggregationError(f'{label} is not canonical')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str)` is true.
- Rejects or diverts the path when `not isinstance(parsed, list)` is true.
- Rejects or diverts the path when `len(ids) != len(set(ids)) or ids != sorted(ids) or value != canonical` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `_validate_feature_id`, `isinstance`, `json.dumps`, `json.loads`, `len`, `set`, `sorted`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_local_domains`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_parcel_frame`

**Signature**

```python
def _validate_parcel_frame(frame: object, label: str) -> gpd.GeoDataFrame:
```

**Purpose**

Validates and rejects malformed parcel frame according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`object`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Checks `not isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `BessPlanningFeatureParcelAggregationError(f'{label} must be a GeoDataFrame')`.
2. Checks `frame.columns.duplicated().any()`. When true: Raises `BessPlanningFeatureParcelAggregationError(f'{label} contains duplicate columns')`.
3. Checks `'parcel_id' not in frame.columns`. When true: Raises `BessPlanningFeatureParcelAggregationError(f'{label} lacks parcel_id')`.
4. Runs guarded operation: Computes `geometry_name` from `frame.geometry.name`. Checks `geometry_name not in frame.columns`. When true: Raises `ValueError('active geometry column is absent')`. Checks `frame.crs is None`. When true: Raises `ValueError('CRS is absent')`. Calls `CRS.from_user_input(frame.crs)` for its validation or side effect. Handles `Exception`.
5. Computes `parcel_ids` from `frame['parcel_id']`.
6. Checks `parcel_ids.isna().any() or parcel_ids.duplicated().any() or any((not isinstance(value, str) or not value or value != value.strip() or (value in NULL_LITERALS) for value in parcel_ids))`. When true: Raises `BessPlanningFeatureParcelAggregationError(f'{label} parcel IDs must be unique exact strings')`.
7. Iterates `geometry` over `frame.geometry.array`. For each value: Checks `geometry is None or geometry.is_empty or (not geometry.is_valid) or (geometry.geom_type not in {'Polygon', 'MultiPolygon'}) or (int(get_coordinate_dimension(geometry)) != 2)`. When true: Raises `BessPlanningFeatureParcelAggregationError(f'{label} requires valid canonical 2D polygon geometry')`.
8. Returns `frame`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `frame.columns.duplicated().any()` is true.
- Rejects or diverts the path when `'parcel_id' not in frame.columns` is true.
- Rejects or diverts the path when `parcel_ids.isna().any() or parcel_ids.duplicated().any() or any((not isinstance(value, str) or not value or value != value.strip() or (value in NULL_LITERALS) for value in parcel_ids))` is true.
- Rejects or diverts the path when `geometry_name not in frame.columns` is true.
- Rejects or diverts the path when `frame.crs is None` is true.
- Rejects or diverts the path when `geometry is None or geometry.is_empty or (not geometry.is_valid) or (geometry.geom_type not in {'Polygon', 'MultiPolygon'}) or (int(get_coordinate_dimension(geometry)) != 2)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`, `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `CRS.from_user_input`, `ValueError`, `any`, `frame.columns.duplicated`, `frame.columns.duplicated().any`, `get_coordinate_dimension`, `int`, `isinstance`, `parcel_ids.duplicated`, `parcel_ids.duplicated().any`, `parcel_ids.isna`, `parcel_ids.isna().any`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_aggregate_frames`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_result_envelope`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `load_bess_planning_feature_parcel_aggregation_artifacts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_application_relations`

**Signature**

```python
def _validate_application_relations(
    frame: object,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> pd.DataFrame:
```

**Purpose**

Validates and rejects malformed application relations according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`object`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `application` (`BessPlanningFeatureApplicationResult | _ApplicationLineage`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Checks `not isinstance(frame, pd.DataFrame) or isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `BessPlanningFeatureParcelAggregationError('Application relations must be a DataFrame')`.
2. Runs guarded operation: Calls `validate_bess_application_relation_frame(frame, label='application relations', policy_profile=application.policy_profile, policy_sha256=application.policy_sha256, policy_result_sha256=application.policy_complete_result_content_sha256, source_document_id=application.source_document_id, source_archive_sha256=application.source_archive_sha256, cnig_profile=app…` for its validation or side effect. Handles `(TypeError, ValueError)`.
3. Returns `frame`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(frame, pd.DataFrame) or isinstance(frame, gpd.GeoDataFrame)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `isinstance`, `str`, `validate_bess_application_relation_frame`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_aggregate_frames`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_relation_parcel_areas`

**Signature**

```python
def _validate_relation_parcel_areas(
    parcels: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> None:
```

**Purpose**

Validates and rejects malformed relation parcel areas according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `geometry_name` from `parcels.geometry.name`.
2. Computes `calculation` from `gpd.GeoDataFrame({'parcel_id': parcels['parcel_id'].copy(deep=True)}, geometry=parcels.geometry.copy(deep=True), crs=parcels.crs, index=parcels.index.copy(deep=True))`.
3. Runs guarded operation: Checks `not CRS.from_user_input(calculation.crs).equals(CRS.from_epsg(2154))`. When true: Computes `calculation` from `calculation.to_crs('EPSG:2154')`. Computes `areas` from `calculation.geometry.area.to_numpy(dtype='float64')`. Handles `Exception`.
4. Checks `not np.isfinite(areas).all() or (areas <= 0).any()`. When true: Raises `BessPlanningFeatureParcelAggregationError('parcel metric areas must be finite and positive')`.
5. Computes `expected` from `dict(zip(calculation['parcel_id'].tolist(), areas.tolist(), strict=True))`.
6. Iterates `(parcel_id, stored)` over `relations[['parcel_id', 'parcel_metric_area_m2']].itertuples(index=False, name=None)`. For each value: Computes `measured` from `expected.get(parcel_id)`. Checks `measured is None`. When true: Raises `BessPlanningFeatureParcelAggregationError('relation references an unknown parcel for metric area')`. Checks `isinstance(stored, bool) or not isinstance(stored, Real)`. When true: Raises `BessPlanningFeatureParcelAggregationError('relation parcel metric area must be numeric')`. Executes 4 additional source-ordered statement(s).
7. Checks `parcels.geometry.name != geometry_name`. When true: Raises `BessPlanningFeatureParcelAggregationError('parcel active geometry changed during metric validation')`.

**Validation and invariants**

- Rejects or diverts the path when `not np.isfinite(areas).all() or (areas <= 0).any()` is true.
- Rejects or diverts the path when `parcels.geometry.name != geometry_name` is true.
- Rejects or diverts the path when `measured is None` is true.
- Rejects or diverts the path when `isinstance(stored, bool) or not isinstance(stored, Real)` is true.
- Rejects or diverts the path when `not math.isfinite(actual)` is true.
- Rejects or diverts the path when `abs(actual - measured) > tolerance` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `calculation.to_crs`, `parcels.geometry.copy`, `parcels.index.copy`, `parcels['parcel_id'].copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(areas <= 0).any`, `BessPlanningFeatureParcelAggregationError`, `CRS.from_epsg`, `CRS.from_user_input`, `CRS.from_user_input(calculation.crs).equals`, `abs`, `areas.tolist`, `calculation.geometry.area.to_numpy`, `calculation.to_crs`, `calculation['parcel_id'].tolist`, `dict`, `expected.get`, `float`, `gpd.GeoDataFrame`, `isinstance`, `math.isfinite`, `max`, `np.isfinite`, `np.isfinite(areas).all`, `parcels.geometry.copy`, `parcels.index.copy`, `parcels['parcel_id'].copy`, `relations[['parcel_id', 'parcel_metric_area_m2']].itertuples`, `technical_overlay_tolerance`, `zip`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_aggregate_frames`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_local_domains`

**Signature**

```python
def _validate_local_domains(parcels: gpd.GeoDataFrame, relations: pd.DataFrame) -> None:
```

**Purpose**

Validates and rejects malformed local domains according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Iterates `row` over `parcels.to_dict('records')`. For each value: Computes `aggregation_status` from `row['bess_cnig_parcel_aggregation_status']`. Checks `aggregation_status not in AGGREGATION_STATUSES`. When true: Raises `BessPlanningFeatureParcelAggregationError('parcel aggregation status is outside the allowed domain')`. Computes `status` from `_null_value(row['bess_cnig_parcel_precheck_status'])`. Executes 4 additional source-ordered statement(s).
2. Iterates `row` over `relations.to_dict('records')`. For each value: Computes `role` from `row['bess_cnig_parcel_relation_role']`. Checks `role not in RELATION_ROLES`. When true: Raises `BessPlanningFeatureParcelAggregationError('parcel relation role is outside the allowed domain')`. Computes `selected` from `row['bess_cnig_selected_for_parcel_status']`. Executes 7 additional source-ordered statement(s).

**Validation and invariants**

- Rejects or diverts the path when `aggregation_status not in AGGREGATION_STATUSES` is true.
- Rejects or diverts the path when `aggregation_status == 'AGGREGATED_EXACT_POLICY'` is true.
- Rejects or diverts the path when `role not in RELATION_ROLES` is true.
- Rejects or diverts the path when `selected is not (role == 'SELECTED_CONTROLLING')` is true.
- Rejects or diverts the path when `status not in ALLOWED_PRECHECK_STATUSES` is true.
- Rejects or diverts the path when `confidence not in ALLOWED_CONFIDENCES` is true.
- Rejects or diverts the path when `isinstance(priority, bool) or not isinstance(priority, Integral) or int(priority) <= 0` is true.
- Rejects or diverts the path when `any((value is not None for value in (status, confidence, priority)))` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `_null_value`, `_validate_json_ids`, `any`, `int`, `isinstance`, `parcels.to_dict`, `relations.to_dict`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_result_envelope`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_relation_priority`

**Signature**

```python
def _relation_priority(row: dict[str, object]) -> int:
```

**Purpose**

Implements relation priority according to the exact implementation and guards in this file.

**Inputs**

- `row` (`dict[str, object]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `int`. Observed return expression(s): `int(value)`.

**Algorithm**

1. Computes `value` from `row['bess_cnig_status_priority']`.
2. Checks `isinstance(value, bool) or not isinstance(value, Integral) or int(value) <= 0`. When true: Raises `BessPlanningFeatureParcelAggregationError('Applied relation priority must be a positive integer')`.
3. Returns `int(value)`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Integral) or int(value) <= 0` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `int`, `isinstance`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_parcel_summary`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_parcel_summary`

**Signature**

```python
def _parcel_summary(
    parcel_relations: list[dict[str, object]],
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[dict[str, object], list[dict[str, object]]]:
```

**Purpose**

Implements parcel summary according to the exact implementation and guards in this file.

**Inputs**

- `parcel_relations` (`list[dict[str, object]]`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `application` (`BessPlanningFeatureApplicationResult | _ApplicationLineage`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[dict[str, object], list[dict[str, object]]]`. Observed return expression(s): `(summary, assessed)`.

**Algorithm**

1. Computes `controlling` from `[row for row in parcel_relations if row['relation_type'] in CONTROLLING_RELATION_TYPES]`.
2. Computes `contextual` from `[row for row in parcel_relations if row['relation_type'] in CONTEXT_RELATION_TYPES]`.
3. Checks `len(controlling) + len(contextual) != len(parcel_relations)`. When true: Raises `BessPlanningFeatureParcelAggregationError('Relation type is outside the aggregation contract')`.
4. Computes `exact` from `[row for row in controlling if row['bess_cnig_policy_application_status'] == 'APPLIED_EXACT_POLICY']`.
5. Computes `unresolved` from `[row for row in controlling if row['bess_cnig_policy_application_status'] == 'UNRESOLVED_CODE_PAIR']`.
6. Checks `len(exact) + len(unresolved) != len(controlling)`. When true: Raises `BessPlanningFeatureParcelAggregationError('Controlling application status is invalid')`.
7. Defines `selected_status` with annotation `str | None` from `None`.
8. Defines `selected_confidence` with annotation `str | None` from `None`.
9. Defines `selected_priority` with annotation `int | None` from `None`.
10. Defines `priorities` with annotation `list[int]` from `[]`.
11. Defines `priority_statuses` with annotation `dict[int, set[str]]` from `{}`.
12. Defines `status_priorities` with annotation `dict[str, set[int]]` from `{}`.
13. Iterates `row` over `exact`. For each value: Computes `priority` from `row['bess_cnig_status_priority']`. Computes `status` from `row['bess_cnig_precheck_status']`. Checks `isinstance(priority, bool) or not isinstance(priority, Integral) or int(priority) <= 0 or (not isinstance(status, str))`. When true: Raises `BessPlanningFeatureParcelAggregationError('Applied relation status and priority are invalid')`. Executes 4 additional source-ordered statement(s).
14. Checks `any((len(statuses) != 1 for statuses in priority_statuses.values())) or any((len(priority_values) != 1 for priority_values in status_priorities.values()))`. When true: Raises `BessPlanningFeatureParcelAggregationError('Applied relation status and priority mapping is not one-to-one')`.
15. Checks `unresolved`. When true: Computes `aggregation_status` from `'UNRESOLVED_CONTROLLING_CODE_PAIR'`. Otherwise: Checks `controlling`. When true: Computes `aggregation_status` from `'AGGREGATED_EXACT_POLICY'`. Computes `selected_priority` from `max(priorities)`. Computes `selected_status` from `next(iter(priority_statuses[selected_priority]))`. Executes 3 additional source-ordered statement(s). Otherwise: Checks `parcel_relations`. When true: Computes `aggregation_status` from `'TOUCH_ONLY_RELATIONS_ONLY'`. Otherwise: Computes `aggregation_status` from `'NO_PLANNING_FEATURE_RELATION'`.
16. Defines `assessed` with annotation `list[dict[str, object]]` from `[]`.
17. Iterates `row` over `parcel_relations`. For each value: Checks `row['relation_type'] in CONTEXT_RELATION_TYPES`. When true: Computes `role` from `'TOUCH_ONLY_CONTEXT'`. Otherwise: Checks `aggregation_status == 'UNRESOLVED_CONTROLLING_CODE_PAIR'`. When true: Computes `role` from `'UNRESOLVED_CONTROLLING' if row['bess_cnig_policy_application_status'] == 'UNRESOLVED_CODE_PAIR' else 'DEFERRED_BY_UNRESOLVED_CONTROLLING'`. Otherwise: Computes `role` from `'SELECTED_CONTROLLING' if row['bess_cnig_precheck_status'] == selected_status and _relation_priority(row) == selected_priority else 'LOWER_PRIORITY_CONTROLLING'`. Calls `assessed.append({**row, 'bess_cnig_parcel_relation_role': role, 'bess_cnig_selected_for_parcel_status': role == 'SELECTED_CONTROLLING', 'bess_cnig_resulting_parcel_aggregation_status': aggregation_status, 'bess_cnig_resulting_parcel_precheck_status': selected_status, 'bess_cnig_resulting_parcel_precheck_confidence': selected_confidence, 'bess_cnig_resulting…` for its validation or side effect.
18. Computes `roles` from `[row['bess_cnig_parcel_relation_role'] for row in assessed]`.
19. Computes `exact_statuses` from `{str(row['bess_cnig_precheck_status']) for row in exact}`.
20. Defines `summary` with annotation `dict[str, object]` from `{'bess_cnig_parcel_aggregation_status': aggregation_status, 'bess_cnig_parcel_precheck_status': selected_status, 'bess_cnig_parcel_precheck_confidence': selected_confidence, 'bess_cnig_parcel_status_priority': selected_priority, 'bess_cnig_controlling_relation_count': len(controlling), 'bess_cnig_exact_controlling_rel…`.
21. Returns `(summary, assessed)`.

**Validation and invariants**

- Rejects or diverts the path when `len(controlling) + len(contextual) != len(parcel_relations)` is true.
- Rejects or diverts the path when `len(exact) + len(unresolved) != len(controlling)` is true.
- Rejects or diverts the path when `any((len(statuses) != 1 for statuses in priority_statuses.values())) or any((len(priority_values) != 1 for priority_values in status_priorities.values()))` is true.
- Rejects or diverts the path when `isinstance(priority, bool) or not isinstance(priority, Integral) or int(priority) <= 0 or (not isinstance(status, str))` is true.
- Rejects or diverts the path when `controlling` is true.
- Rejects or diverts the path when `any((value not in CONFIDENCE_RANK for value in confidences))` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `_json_ids`, `_relation_priority`, `any`, `assessed.append`, `int`, `isinstance`, `iter`, `len`, `max`, `min`, `next`, `priorities.append`, `priority_statuses.setdefault`, `priority_statuses.setdefault(normalized_priority, set()).add`, `priority_statuses.values`, `roles.count`, `set`, `status_priorities.setdefault`, `status_priorities.setdefault(status, set()).add`, `status_priorities.values`, `str`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_aggregate_frames`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_assign_columns`

**Signature**

```python
def _assign_columns(
    frame: pd.DataFrame, rows: list[dict[str, object]], columns: tuple[str, ...]
) -> pd.DataFrame:
```

**Purpose**

Implements assign columns according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `rows` (`list[dict[str, object]]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`tuple[str, ...]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Iterates `column` over `columns`. For each value: Computes `values` from `[row[column] for row in rows]`. Checks `column in PARCEL_INTEGER_COLUMNS or column == 'bess_cnig_resulting_parcel_status_priority'`. When true: Computes `frame[column]` from `pd.array(values, dtype='Int64')`. Otherwise: Checks `column in PARCEL_BOOL_COLUMNS or column == 'bess_cnig_selected_for_parcel_status'`. When true: Computes `frame[column]` from `pd.array(values, dtype='bool')`. Otherwise: Computes `frame[column]` from `pd.array(values, dtype='str')`.
2. Returns `frame`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `pd.array`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_aggregate_frames`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_aggregate_frames`

**Signature**

```python
def _aggregate_frames(
    source_parcels: gpd.GeoDataFrame,
    source_relations: pd.DataFrame,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[gpd.GeoDataFrame, pd.DataFrame]:
```

**Purpose**

Aggregates frames according to the exact implementation and guards in this file.

**Inputs**

- `source_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `application` (`BessPlanningFeatureApplicationResult | _ApplicationLineage`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[gpd.GeoDataFrame, pd.DataFrame]`. Observed return expression(s): `(parcels, assessments)`.

**Algorithm**

1. Calls `_validate_parcel_frame(source_parcels, 'source parcels')` for its validation or side effect.
2. Calls `_validate_application_relations(source_relations, application)` for its validation or side effect.
3. Calls `_validate_relation_parcel_areas(source_parcels, source_relations)` for its validation or side effect.
4. Checks `any((column in source_parcels.columns for column in PARCEL_COLUMNS)) or any((column in source_relations.columns for column in RELATION_COLUMNS))`. When true: Raises `BessPlanningFeatureParcelAggregationError('Aggregation columns already exist on source inputs')`.
5. Checks `'parcel_id' not in source_parcels or 'parcel_id' not in source_relations`. When true: Raises `BessPlanningFeatureParcelAggregationError('Aggregation inputs lack parcel_id')`.
6. Computes `parcel_ids` from `source_parcels['parcel_id']`.
7. Computes `known` from `set(parcel_ids.tolist())`.
8. Checks `any((value not in known for value in source_relations['parcel_id']))`. When true: Raises `BessPlanningFeatureParcelAggregationError('Relation references an unknown parcel')`.
9. Computes `relation_rows` from `source_relations.to_dict('records')`.
10. Defines `grouped` with annotation `dict[str, list[dict[str, object]]]` from `{value: [] for value in parcel_ids.tolist()}`.
11. Iterates `row` over `relation_rows`. For each value: Calls `grouped[str(row['parcel_id'])].append(row)` for its validation or side effect.
12. Defines `summaries` with annotation `list[dict[str, object]]` from `[]`.
13. Defines `assessment_rows` with annotation `list[dict[str, object]]` from `[]`.
14. Iterates `parcel_id` over `parcel_ids.tolist()`. For each value: Computes `(summary, assessed)` from `_parcel_summary(grouped[parcel_id], application)`. Calls `summaries.append(summary)` for its validation or side effect. Calls `assessment_rows.extend(assessed)` for its validation or side effect.
15. Computes `parcels` from `source_parcels.copy(deep=True)`.
16. Calls `_assign_columns(parcels, summaries, PARCEL_COLUMNS)` for its validation or side effect.
17. Computes `parcels` from `gpd.GeoDataFrame(parcels, geometry=source_parcels.geometry.name, crs=source_parcels.crs)`.
18. Computes `assessments` from `source_relations.copy(deep=True)`.
19. Defines `cursor` with annotation `dict[str, int]` from `{parcel_id: 0 for parcel_id in grouped}`.
20. Defines `assessed_by_parcel` with annotation `dict[str, list[dict[str, object]]]` from `{parcel_id: [] for parcel_id in grouped}`.
21. Iterates `row` over `assessment_rows`. For each value: Calls `assessed_by_parcel[str(row['parcel_id'])].append(row)` for its validation or side effect.
22. Defines `ordered_assessed` with annotation `list[dict[str, object]]` from `[]`.
23. Iterates `source_row` over `relation_rows`. For each value: Computes `parcel_id` from `str(source_row['parcel_id'])`. Computes `item` from `assessed_by_parcel[parcel_id][cursor[parcel_id]]`. Updates `cursor[parcel_id]` using `` and `1`. Executes 1 additional source-ordered statement(s).
24. Calls `_assign_columns(assessments, ordered_assessed, RELATION_COLUMNS)` for its validation or side effect.
25. Returns `(parcels, assessments)`.

**Validation and invariants**

- Rejects or diverts the path when `any((column in source_parcels.columns for column in PARCEL_COLUMNS)) or any((column in source_relations.columns for column in RELATION_COLUMNS))` is true.
- Rejects or diverts the path when `'parcel_id' not in source_parcels or 'parcel_id' not in source_relations` is true.
- Rejects or diverts the path when `any((value not in known for value in source_relations['parcel_id']))` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `source_parcels.copy`, `source_relations.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `_assign_columns`, `_parcel_summary`, `_validate_application_relations`, `_validate_parcel_frame`, `_validate_relation_parcel_areas`, `any`, `assessed_by_parcel[str(row['parcel_id'])].append`, `assessment_rows.extend`, `gpd.GeoDataFrame`, `grouped[str(row['parcel_id'])].append`, `ordered_assessed.append`, `parcel_ids.tolist`, `set`, `source_parcels.copy`, `source_relations.copy`, `source_relations.to_dict`, `str`, `summaries.append`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_build_result`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_result_envelope`

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
    result: BessPlanningFeatureParcelAggregationResult,
) -> dict[str, object]:
```

**Purpose**

Implements component metadata according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureParcelAggregationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{field: getattr(result, field) for field in RESULT_SCALAR_FIELDS if field not in {'relation_assessments_content_sha256', 'parcels_content_sha256', 'complete_result_content_sha256'}}`.

**Algorithm**

1. Returns `{field: getattr(result, field) for field in RESULT_SCALAR_FIELDS if field not in {'relation_assessments_content_sha256', 'parcels_content_sha256', 'complete_result_content_sha256'}}`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `getattr`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_result_with_hashes`

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
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Implements result with hashes according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureParcelAggregationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `replace(components, complete_result_content_sha256=complete)`.

**Algorithm**

1. Computes `metadata` from `_component_metadata(result)`.
2. Computes `relations_hash` from `_canonical_sha256({'domain': 'landscout.bess_cnig_parcel_aggregation.relation_assessments', **metadata, 'frame': _frame_payload(result.relation_assessments)})`.
3. Computes `parcels_hash` from `_canonical_sha256({'domain': 'landscout.bess_cnig_parcel_aggregation.parcels', **metadata, 'frame': _frame_payload(result.parcels)})`.
4. Computes `components` from `replace(result, relation_assessments_content_sha256=relations_hash, parcels_content_sha256=parcels_hash)`.
5. Computes `complete` from `_canonical_sha256({'domain': 'landscout.bess_cnig_parcel_aggregation.result', **metadata, 'relation_assessments_content_sha256': relations_hash, 'parcels_content_sha256': parcels_hash})`.
6. Returns `replace(components, complete_result_content_sha256=complete)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_canonical_sha256`, `_component_metadata`, `_frame_payload`, `replace`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_build_result`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_result_envelope`

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
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Builds result according to the exact implementation and guards in this file.

**Inputs**

- `source_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `application` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `_result_with_hashes(result)`.

**Algorithm**

1. Computes `(parcels, assessments)` from `_aggregate_frames(source_parcels, application.relations, application)`.
2. Computes `result` from `BessPlanningFeatureParcelAggregationResult(result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION, aggregation_scope=AGGREGATION_SCOPE, policy_scope=POLICY_SCOPE, local_feature_text_interpreted=False, local_regulation_content_interpreted=False, legal_conclusion_produced=False, parcel_status_aggregated=True, parcel_reje…`.
3. Returns `_result_with_hashes(result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationResult`, `_aggregate_frames`, `_frame_sha256`, `_result_with_hashes`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `aggregate_bess_planning_feature_policy_to_parcels`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `load_bess_planning_feature_parcel_aggregation_artifacts`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `validate_bess_planning_feature_parcel_aggregation_result`

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

1. Checks `_frame_payload(actual) != _frame_payload(expected)`. When true: Raises `BessPlanningFeatureParcelAggregationError(f'{label} differs from deterministic aggregation')`.

**Validation and invariants**

- Rejects or diverts the path when `_frame_payload(actual) != _frame_payload(expected)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `_frame_payload`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `_validate_result_envelope`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `load_bess_planning_feature_parcel_aggregation_artifacts`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `validate_bess_planning_feature_parcel_aggregation_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result_envelope`

**Signature**

```python
def _validate_result_envelope(
    result: BessPlanningFeatureParcelAggregationResult,
) -> None:
```

**Purpose**

Validates and rejects malformed result envelope according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureParcelAggregationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `not isinstance(result, BessPlanningFeatureParcelAggregationResult)`. When true: Raises `BessPlanningFeatureParcelAggregationError('result has the wrong type')`.
2. Checks `type(result.result_hash_schema_version) is not int or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`. When true: Raises `BessPlanningFeatureParcelAggregationError('unsupported parcel aggregation result schema')`.
3. Checks `result.aggregation_scope != AGGREGATION_SCOPE or result.policy_scope != POLICY_SCOPE`. When true: Raises `BessPlanningFeatureParcelAggregationError('parcel aggregation scope is invalid')`.
4. Iterates `field` over `RESULT_SCALAR_FIELDS`. For each value: Checks `field.endswith('sha256')`. When true: Runs guarded operation: Calls `_sha256_string(getattr(result, field), field)` for its validation or side effect. Handles `ValueError`.
5. Iterates `(value, label)` over `((result.source_document_id, 'source_document_id'), (result.cnig_profile, 'cnig_profile'), (result.policy_profile, 'policy_profile'))`. For each value: Runs guarded operation: Calls `_exact_string(value, label)` for its validation or side effect. Handles `ValueError`.
6. Checks `type(result.application_result_hash_schema_version) is not int or result.application_result_hash_schema_version != APPLICATION_RESULT_HASH_SCHEMA_VERSION`. When true: Raises `BessPlanningFeatureParcelAggregationError('application result schema must be exactly 2')`.
7. Checks `any((value is not expected for value, expected in ((result.local_feature_text_interpreted, False), (result.local_regulation_content_interpreted, False), (result.legal_conclusion_produced, False), (result.parcel_status_aggregated, True), (result.parcel_rejection_performed, False), (result.score_calculated, False))))`. When true: Raises `BessPlanningFeatureParcelAggregationError('parcel aggregation flags are invalid')`.
8. Checks `not isinstance(result.parcels, gpd.GeoDataFrame) or not isinstance(result.relation_assessments, pd.DataFrame) or isinstance(result.relation_assessments, gpd.GeoDataFrame)`. When true: Raises `BessPlanningFeatureParcelAggregationError('aggregation output frame types are invalid')`.
9. Checks `result.parcels.columns.duplicated().any()`. When true: Raises `BessPlanningFeatureParcelAggregationError('parcel output contains duplicate columns')`.
10. Checks `result.relation_assessments.columns.duplicated().any()`. When true: Raises `BessPlanningFeatureParcelAggregationError('relation assessments contain duplicate columns')`.
11. Checks `tuple(result.parcels.columns[-len(PARCEL_COLUMNS):]) != PARCEL_COLUMNS or tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS):]) != RELATION_COLUMNS`. When true: Raises `BessPlanningFeatureParcelAggregationError('aggregation output suffix schema is invalid')`.
12. Iterates `column` over `PARCEL_STRING_COLUMNS`. For each value: Checks `str(result.parcels[column].dtype) != 'str'`. When true: Raises `BessPlanningFeatureParcelAggregationError('parcel aggregation string dtype is invalid')`.
13. Iterates `column` over `PARCEL_INTEGER_COLUMNS`. For each value: Checks `str(result.parcels[column].dtype) != 'Int64'`. When true: Raises `BessPlanningFeatureParcelAggregationError('parcel aggregation integer dtype is invalid')`.
14. Iterates `column` over `PARCEL_BOOL_COLUMNS`. For each value: Checks `str(result.parcels[column].dtype) != 'bool'`. When true: Raises `BessPlanningFeatureParcelAggregationError('parcel aggregation bool dtype is invalid')`.
15. Iterates `column` over `RELATION_STRING_COLUMNS`. For each value: Checks `str(result.relation_assessments[column].dtype) != 'str'`. When true: Raises `BessPlanningFeatureParcelAggregationError('relation assessment string dtype is invalid')`.
16. Checks `str(result.relation_assessments['bess_cnig_selected_for_parcel_status'].dtype) != 'bool' or str(result.relation_assessments['bess_cnig_resulting_parcel_status_priority'].dtype) != 'Int64'`. When true: Raises `BessPlanningFeatureParcelAggregationError('relation assessment dtype is invalid')`.
17. Calls `_validate_parcel_frame(result.parcels, 'parcel output')` for its validation or side effect.
18. Calls `_validate_local_domains(result.parcels, result.relation_assessments)` for its validation or side effect.
19. Computes `source_parcels` from `result.parcels.drop(columns=list(PARCEL_COLUMNS))`.
20. Computes `source_parcels` from `gpd.GeoDataFrame(source_parcels, geometry=result.parcels.geometry.name, crs=result.parcels.crs)`.
21. Computes `source_relations` from `result.relation_assessments.drop(columns=list(RELATION_COLUMNS))`.
22. Checks `result.source_parcels_content_sha256 != _frame_sha256(source_parcels, 'landscout.bess_cnig_parcel_aggregation.source_parcels')`. When true: Raises `BessPlanningFeatureParcelAggregationError('source parcel content SHA256 is invalid')`.
23. Checks `result.source_application_relations_content_sha256 != _frame_sha256(source_relations, 'landscout.bess_cnig_parcel_aggregation.source_application_relations')`. When true: Raises `BessPlanningFeatureParcelAggregationError('source application relation content SHA256 is invalid')`.
24. Computes `lineage` from `_ApplicationLineage(source_document_id=result.source_document_id, source_archive_sha256=result.source_archive_sha256, cnig_profile=result.cnig_profile, cnig_profile_sha256=result.cnig_profile_sha256, policy_profile=result.policy_profile, policy_sha256=result.policy_sha256, policy_complete_result_content_sha256=result.…`.
25. Calls `_validate_application_relations(source_relations, lineage)` for its validation or side effect.
26. Computes `(expected_parcels, expected_relations)` from `_aggregate_frames(source_parcels, source_relations, lineage)`.
27. Calls `_compare_frame(result.parcels, expected_parcels, 'parcel output')` for its validation or side effect.
28. Calls `_compare_frame(result.relation_assessments, expected_relations, 'relation assessments')` for its validation or side effect.
29. Computes `rebuilt` from `_result_with_hashes(result)`.
30. Iterates `field` over `('relation_assessments_content_sha256', 'parcels_content_sha256', 'complete_result_content_sha256')`. For each value: Checks `getattr(result, field) != getattr(rebuilt, field)`. When true: Raises `BessPlanningFeatureParcelAggregationError(f'{field} is invalid')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(result, BessPlanningFeatureParcelAggregationResult)` is true.
- Rejects or diverts the path when `type(result.result_hash_schema_version) is not int or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `result.aggregation_scope != AGGREGATION_SCOPE or result.policy_scope != POLICY_SCOPE` is true.
- Rejects or diverts the path when `type(result.application_result_hash_schema_version) is not int or result.application_result_hash_schema_version != APPLICATION_RESULT_HASH_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `any((value is not expected for value, expected in ((result.local_feature_text_interpreted, False), (result.local_regulation_content_interpreted, False), (result.legal_conclusion_produced, False), (result.parcel_status_aggregated, True), (result.parcel_rejection_performed, False), (result.score_calculated, False))))` is true.
- Rejects or diverts the path when `not isinstance(result.parcels, gpd.GeoDataFrame) or not isinstance(result.relation_assessments, pd.DataFrame) or isinstance(result.relation_assessments, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `result.parcels.columns.duplicated().any()` is true.
- Rejects or diverts the path when `result.relation_assessments.columns.duplicated().any()` is true.
- Rejects or diverts the path when `tuple(result.parcels.columns[-len(PARCEL_COLUMNS):]) != PARCEL_COLUMNS or tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS):]) != RELATION_COLUMNS` is true.
- Rejects or diverts the path when `str(result.relation_assessments['bess_cnig_selected_for_parcel_status'].dtype) != 'bool' or str(result.relation_assessments['bess_cnig_resulting_parcel_status_priority'].dtype) != 'Int64'` is true.
- Rejects or diverts the path when `result.source_parcels_content_sha256 != _frame_sha256(source_parcels, 'landscout.bess_cnig_parcel_aggregation.source_parcels')` is true.
- Rejects or diverts the path when `result.source_application_relations_content_sha256 != _frame_sha256(source_relations, 'landscout.bess_cnig_parcel_aggregation.source_application_relations')` is true.
- Rejects or diverts the path when `field.endswith('sha256')` is true.
- Rejects or diverts the path when `str(result.parcels[column].dtype) != 'str'` is true.
- Rejects or diverts the path when `str(result.parcels[column].dtype) != 'Int64'` is true.
- Rejects or diverts the path when `str(result.parcels[column].dtype) != 'bool'` is true.
- Rejects or diverts the path when `str(result.relation_assessments[column].dtype) != 'str'` is true.
- Rejects or diverts the path when `getattr(result, field) != getattr(rebuilt, field)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `_ApplicationLineage`, `_aggregate_frames`, `_compare_frame`, `_exact_string`, `_frame_sha256`, `_result_with_hashes`, `_sha256_string`, `_validate_application_relations`, `_validate_local_domains`, `_validate_parcel_frame`, `any`, `field.endswith`, `getattr`, `gpd.GeoDataFrame`, `isinstance`, `len`, `list`, `result.parcels.columns.duplicated`, `result.parcels.columns.duplicated().any`, `result.parcels.drop`, `result.relation_assessments.columns.duplicated`, `result.relation_assessments.columns.duplicated().any`, `result.relation_assessments.drop`, `str`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `aggregate_bess_planning_feature_policy_to_parcels`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `load_bess_planning_feature_parcel_aggregation_artifacts`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `validate_bess_planning_feature_parcel_aggregation_result`

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
    result: BessPlanningFeatureParcelAggregationResult
    | BessPlanningFeatureParcelAggregationArtifactManifest,
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> None:
```

**Purpose**

Validates and rejects malformed source locks according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessPlanningFeatureParcelAggregationResult | BessPlanningFeatureParcelAggregationArtifactManifest`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `application` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `comparisons` from `((result.source_document_id, application.source_document_id), (result.source_archive_sha256, application.source_archive_sha256), (result.cnig_profile, application.cnig_profile), (result.cnig_profile_sha256, application.cnig_profile_sha256), (result.cnig_complete_result_content_sha256, application.cnig_complete_result_…`.
2. Checks `any((actual != expected for actual, expected in comparisons))`. When true: Raises `BessPlanningFeatureParcelAggregationError('parcel aggregation source lock differs')`.

**Validation and invariants**

- Rejects or diverts the path when `any((actual != expected for actual, expected in comparisons))` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `_frame_sha256`, `any`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `load_bess_planning_feature_parcel_aggregation_artifacts`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `validate_bess_planning_feature_parcel_aggregation_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_application_source`

**Signature**

```python
def _validate_application_source(
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
    application_result: BessPlanningFeatureApplicationResult,
) -> None:
```

**Purpose**

Validates and rejects malformed application source according to the exact implementation and guards in this file.

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
- `application_result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `validate_bess_planning_feature_application_result(planning_document, parcels, surface_features, line_features, point_features, relations, code_profile, coded_result, policy_config, policy_result, application_result)` for its validation or side effect. Handles `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `validate_bess_planning_feature_application_result`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `aggregate_bess_planning_feature_policy_to_parcels`
- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `validate_bess_planning_feature_parcel_aggregation_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `aggregate_bess_planning_feature_policy_to_parcels`

**Signature**

```python
def aggregate_bess_planning_feature_policy_to_parcels(
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
    application_result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Validate the application once and aggregate its relations to every parcel.

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
- `application_result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `result`.

**Algorithm**

1. Runs guarded operation: Calls `_validate_application_source(planning_document, parcels, surface_features, line_features, point_features, relations, code_profile, coded_result, policy_config, policy_result, application_result)` for its validation or side effect. Computes `result` from `_build_result(parcels, application_result)`. Calls `_validate_result_envelope(result)` for its validation or side effect. Returns `result`. Handles `BessPlanningFeatureParcelAggregationError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `_build_result`, `_validate_application_source`, `_validate_result_envelope`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `_aggregation_fixture`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_parcel_and_relation_prefixes_order_and_inputs_are_preserved`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_and_relation_prefixes_order_and_inputs_are_preserved`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_bess_planning_feature_parcel_aggregation_result`

**Signature**

```python
def validate_bess_planning_feature_parcel_aggregation_result(
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
    application_result: BessPlanningFeatureApplicationResult,
    result: BessPlanningFeatureParcelAggregationResult,
) -> None:
```

**Purpose**

Independently validate and rebuild one persisted parcel aggregation result.

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
- `application_result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`BessPlanningFeatureParcelAggregationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `_validate_result_envelope(result)` for its validation or side effect. Calls `_validate_source_locks(result, parcels, application_result)` for its validation or side effect. Calls `_validate_application_source(planning_document, parcels, surface_features, line_features, point_features, relations, code_profile, coded_result, policy_config, policy_result, application_result)` for its validation or side effect. Computes `expected` from `_build_result(parcels, application_result)`. Executes 3 additional source-ordered statement(s). Handles `BessPlanningFeatureParcelAggregationError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `getattr(result, field) != getattr(expected, field)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `_build_result`, `_compare_frame`, `_validate_application_source`, `_validate_result_envelope`, `_validate_source_locks`, `getattr`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_local_corruption_fast_fails_before_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_parcel_area_defect_fast_fails_before_application_source_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_relation_identity_and_global_mapping_fail_before_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_relation_semantic_failure_fast_fails_before_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_representative_intrinsic_failures_all_precede_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_valid_two_file_verified_byte_artifacts_and_source_readback`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_defect_fast_fails_before_application_source_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_identity_and_global_mapping_fail_before_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_semantic_failure_fast_fails_before_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_valid_two_file_verified_byte_artifacts_and_source_readback`

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
2. Iterates `(key, value)` over `pairs`. For each value: Checks `key in output`. When true: Raises `BessPlanningFeatureParcelAggregationError(f'Duplicate JSON aggregation artifact key: {key!r}')`. Computes `output[key]` from `value`.
3. Returns `output`.

**Validation and invariants**

- Rejects or diverts the path when `key in output` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessPlanningFeatureParcelAggregationError`.

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
    path: Path, record: BessPlanningFeatureParcelAggregationArtifactRecord
) -> pd.DataFrame:
```

**Purpose**

Reads and validates verified artifact according to the exact implementation and guards in this file.

**Inputs**

- `path` (`Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `record` (`BessPlanningFeatureParcelAggregationArtifactRecord`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Checks `path.name != record.filename`. When true: Raises `BessPlanningFeatureParcelAggregationError('Aggregation artifact filename differs')`.
2. Computes `payload` from `path.read_bytes()`.
3. Checks `len(payload) != record.size_bytes`. When true: Raises `BessPlanningFeatureParcelAggregationError('Aggregation artifact byte size differs')`.
4. Checks `sha256(payload).hexdigest() != record.sha256`. When true: Raises `BessPlanningFeatureParcelAggregationError('Aggregation artifact SHA256 differs')`.
5. Computes `buffer` from `BytesIO(payload)`.
6. Defines `frame` with annotation `pd.DataFrame` from `gpd.read_parquet(buffer) if record.geospatial else pd.read_parquet(buffer)`.
7. Checks `len(frame) != record.row_count`. When true: Raises `BessPlanningFeatureParcelAggregationError('Aggregation artifact row count differs')`.
8. Checks `deterministic_frame_schema_signature(frame) != record.frame_schema_signature`. When true: Raises `BessPlanningFeatureParcelAggregationError('Aggregation artifact frame schema differs')`.
9. Checks `record.geospatial`. When true: Checks `not isinstance(frame, gpd.GeoDataFrame) or frame.crs is None or CRS.from_user_input(frame.crs).to_json_dict() != record.crs`. When true: Raises `BessPlanningFeatureParcelAggregationError('Aggregation parcel artifact CRS differs')`. Otherwise: Checks `isinstance(frame, gpd.GeoDataFrame)`. When true: Raises `BessPlanningFeatureParcelAggregationError('Relation assessment artifact is unexpectedly geospatial')`.
10. Returns `frame`.

**Validation and invariants**

- Rejects or diverts the path when `path.name != record.filename` is true.
- Rejects or diverts the path when `len(payload) != record.size_bytes` is true.
- Rejects or diverts the path when `sha256(payload).hexdigest() != record.sha256` is true.
- Rejects or diverts the path when `len(frame) != record.row_count` is true.
- Rejects or diverts the path when `deterministic_frame_schema_signature(frame) != record.frame_schema_signature` is true.
- Rejects or diverts the path when `record.geospatial` is true.
- Rejects or diverts the path when `not isinstance(frame, gpd.GeoDataFrame) or frame.crs is None or CRS.from_user_input(frame.crs).to_json_dict() != record.crs` is true.
- Rejects or diverts the path when `isinstance(frame, gpd.GeoDataFrame)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `gpd.read_parquet`, `path.read_bytes`, `pd.read_parquet`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessPlanningFeatureParcelAggregationError`, `BytesIO`, `CRS.from_user_input`, `CRS.from_user_input(frame.crs).to_json_dict`, `deterministic_frame_schema_signature`, `gpd.read_parquet`, `isinstance`, `len`, `path.read_bytes`, `pd.read_parquet`, `sha256`, `sha256(payload).hexdigest`.

**Known repository callers**

- `src/landscout/stages/aggregate_bess_planning_feature_policy.py` — `load_bess_planning_feature_parcel_aggregation_artifacts`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_bess_planning_feature_parcel_aggregation_artifacts`

**Signature**

```python
def load_bess_planning_feature_parcel_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
    source_parcels: gpd.GeoDataFrame,
    application_result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

**Purpose**

Load byte-sealed outputs and bind them to exact lightweight upstreams.

**Inputs**

- `manifest_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relation_assessments_path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `application_result` (`BessPlanningFeatureApplicationResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessPlanningFeatureParcelAggregationResult`. Observed return expression(s): `result`.

**Algorithm**

1. Runs guarded operation: Calls `validate_bess_planning_feature_application_result_envelope(application_result)` for its validation or side effect. Calls `_validate_parcel_frame(source_parcels, 'source parcels')` for its validation or side effect. Computes `payload` from `json.loads(Path(manifest_path).read_text(encoding='utf-8'), object_pairs_hook=_unique_json_object)`. Computes `manifest` from `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(payload)`. Executes 11 additional source-ordered statement(s). Handles `BessPlanningFeatureParcelAggregationError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(loaded_parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `getattr(result, field) != getattr(expected, field)` is true.

**Exceptions**

- Explicitly raises: `BessPlanningFeatureParcelAggregationError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `Path(manifest_path).read_text`, `_read_verified_artifact`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessPlanningFeatureParcelAggregationArtifactManifest.model_validate`, `BessPlanningFeatureParcelAggregationError`, `BessPlanningFeatureParcelAggregationResult`, `Path`, `Path(manifest_path).read_text`, `_build_result`, `_compare_frame`, `_read_verified_artifact`, `_validate_parcel_frame`, `_validate_result_envelope`, `_validate_source_locks`, `getattr`, `isinstance`, `json.loads`, `validate_bess_planning_feature_application_result_envelope`.

**Known repository callers**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `load_bess_planning_feature_parcel_aggregation_artifacts`
- `tests/unit/test_aggregate_bess_planning_feature_policy.py` — `test_aggregation_loader_rejects_bad_application_before_artifact_reads`

**Tests**

- `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_aggregation_loader_rejects_bad_application_before_artifact_reads`

**Business interpretation**

This symbol contributes to the `planning` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `OFFICIAL_CNIG_CODE_MEANING_ONLY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `PARCELS` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `PARCEL_POLICY_AGGREGATION_ONLY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `RELATION_ASSESSMENTS` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_aggregation_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_application_result_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_confidence_aggregation_method` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_controlling_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_distinct_exact_status_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_exact_controlling_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_formal_review_required` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_legal_conclusion_produced` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_local_feature_text_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_local_regulation_content_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_lower_priority_controlling_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_multiple_exact_statuses` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_aggregation_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_precheck_confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_rejection_performed` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_relation_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_status_aggregated` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_parcel_status_priority` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_application_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_result_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_policy_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_precheck_confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_resulting_parcel_aggregation_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_resulting_parcel_precheck_confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_resulting_parcel_precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_resulting_parcel_status_priority` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_score_calculated` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_selected_feature_ids_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_selected_for_parcel_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_selected_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_status_priority` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_touch_only_feature_ids_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_touch_only_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_unresolved_controlling_relation_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `bess_cnig_unresolved_feature_ids_json` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `columns` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_metric_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `planning_feature_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `relation_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |

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
