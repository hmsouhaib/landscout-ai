# `src/landscout/stages/interpret_bess_zoning.py`

## File identity

- Repository path: `src/landscout/stages/interpret_bess_zoning.py`
- File type: Python source
- Primary responsibility: Applies the checked-in written-zoning evidence policy to structured regulation evidence and parcel zoning facts.
- Layer / domain: `stage` / `project`
- Public or internal role: Contains an explicit module/package export surface; helpers prefixed with `_` remain internal unless re-exported elsewhere.
- Source SHA256: `f230e39abedb5c61a7f51b227800c3a185df9689611f3526aa49cf362ffc99c9`

## 1. Purpose

Applies the checked-in written-zoning evidence policy to structured regulation evidence and parcel zoning facts.

## 2. Position in LandScout architecture

This file is a `stage` artifact in the `project` domain. Its actual upstream inputs and downstream calls are enumerated at symbol level below. It participates only in implemented portions of SCAN, FILTER, or ANALYZE where the documented public functions show that flow; it does not imply implemented SCORE, IDENTIFY, or EXPORT phases.

## 3. Imports and dependencies

### Python standard library

- `from __future__ import annotations` — required by the implementation paths and symbols documented below.
- `import json` — required by the implementation paths and symbols documented below.
- `import math` — required by the implementation paths and symbols documented below.
- `import re` — required by the implementation paths and symbols documented below.
- `from collections.abc import Mapping, Sequence` — required by the implementation paths and symbols documented below.
- `from dataclasses import dataclass, replace` — required by the implementation paths and symbols documented below.
- `from datetime import date, datetime` — required by the implementation paths and symbols documented below.
- `from hashlib import sha256` — required by the implementation paths and symbols documented below.
- `from numbers import Integral, Real` — required by the implementation paths and symbols documented below.
- `from pathlib import Path` — required by the implementation paths and symbols documented below.
- `from typing import Literal` — required by the implementation paths and symbols documented below.

### Third-party

- `import geopandas as gpd` — required by the implementation paths and symbols documented below.
- `import numpy as np` — required by the implementation paths and symbols documented below.
- `import pandas as pd` — required by the implementation paths and symbols documented below.
- `import yaml` — required by the implementation paths and symbols documented below.
- `from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, model_validator` — required by the implementation paths and symbols documented below.
- `from pyproj import CRS` — required by the implementation paths and symbols documented below.
- `from shapely import to_wkb` — required by the implementation paths and symbols documented below.
- `from shapely.geometry.base import BaseGeometry` — required by the implementation paths and symbols documented below.

### Internal LandScout

- `from landscout.sources.gpu_fr import GpuPlanningDocument` — required by the implementation paths and symbols documented below.
- `from landscout.stages.enrich_planning_zoning import ( PlanningZoningError, validate_normalized_planning_zoning_inputs, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.index_planning_regulation import ( PlanningRegulationIndex, validate_planning_regulation_index, )` — required by the implementation paths and symbols documented below.
- `from landscout.stages.planning_overlay import technical_overlay_tolerance` — required by the implementation paths and symbols documented below.
- `from landscout.stages.structure_planning_regulation import ( PlanningRegulationStructureConfig, PlanningRegulationStructureError, PlanningRegulationStructureResult, validate_planning_regulation_structure_with_fragments, )` — required by the implementation paths and symbols documented below.

## 4. Constants and domains

| Constant | Exact value/domain | Meaning and consumers |
|---|---|---|
| `POLICY_SCHEMA_VERSION` | `5` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `RESULT_HASH_SCHEMA_VERSION` | `5` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PLANNING_PRECHECK_SCOPE` | `"WRITTEN_ZONING_REGULATION_ONLY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `REVIEW_SCOPE` | `"CONFIGURED_USE_CONTROL_ARTICLES_ONLY"` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_CHAPTER_STATUSES` | `frozenset( {"POTENTIALLY_COMPATIBLE", "CONDITIONAL_REVIEW", "LIKELY_DIFFICULT", "UNKNOWN"} )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_PARCEL_STATUSES` | `_CHAPTER_STATUSES &#124; {"MIXED_REVIEW_REQUIRED"}` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_CONFIDENCES` | `frozenset({"HIGH", "MEDIUM", "LOW"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_RESOLVED_MAPPING_STATUSES` | `frozenset({"EXACT", "CONFIG_ALIAS"})` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `CHAPTER_POLICY_COLUMNS` | `( "resolved_zone_chapter_label", "chapter_section_id", "review_completeness", "review_scope", "reviewed_section_ids", "missing_required_section_ids", "review_note", "zoning_precheck_status", "zoning_precheck_confidence", "evidence_count", "evidence_ids", "decision_evidence_ids", "context_evidence_ids", "rationale", "missing_information", "planning_precheck_scope", "policy_profile", "policy_sha256", "document_id", "archive_sha256", "pdf_sha256", "index_content_sha256", "structure_result_content_sha256", "structure_profile", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EVIDENCE_CATALOG_COLUMNS` | `( "evidence_id", "resolved_zone_chapter_label", "section_id", "page_number", "evidence_kind", "evidence_direction", "linked_route_ids", "linked_route_roles", "decision_linked", "exact_raw_excerpt", "excerpt_sha256", "section_page_fragment_sha256", "excerpt_start", "excerpt_end", "source_rule_id", "source_rule_excerpt", "source_rule_sha256", "source_rule_start", "source_rule_end", "interpretation_note", "review_completeness", "review_scope", "policy_profile", "policy_sha256", "document_id", "archive_sha256", "pdf_sha256", "index_content_sha256", "structure_result_content_sha256", "structure_profile", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `_EVIDENCE_OCCURRENCE_COLUMNS` | `( "resolved_zone_chapter_label", "section_id", "page_number", "section_page_fragment_sha256", "excerpt_start", "excerpt_end", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `ROUTE_ASSESSMENT_COLUMNS` | `( "route_id", "resolved_zone_chapter_label", "route_kind", "derived_route_status", "positive_evidence_ids", "condition_evidence_ids", "difficulty_evidence_ids", "applicability_note", "review_completeness", "review_scope", "policy_profile", "policy_sha256", "document_id", "archive_sha256", "pdf_sha256", "index_content_sha256", "structure_result_content_sha256", "structure_profile", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `EVIDENCE_ROUTE_LINK_COLUMNS` | `( "route_id", "resolved_zone_chapter_label", "route_kind", "evidence_id", "route_role", "evidence_direction", "review_completeness", "review_scope", "policy_profile", "policy_sha256", "document_id", "archive_sha256", "pdf_sha256", "index_content_sha256", "structure_result_content_sha256", "structure_profile", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `SOURCE_ZONE_POLICY_COLUMNS` | `( "source_zone_label_raw", "resolved_zone_chapter_label", "mapping_status", "matched_section_id", "source_layer", "zoning_precheck_status", "zoning_precheck_confidence", "evidence_ids", "decision_evidence_ids", "context_evidence_ids", "review_scope", "planning_precheck_scope", "policy_profile", "policy_sha256", "document_id", "archive_sha256", "pdf_sha256", "index_content_sha256", "structure_result_content_sha256", "structure_profile", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_ZONE_POLICY_COLUMNS` | `( "parcel_id", "planning_zone_id", "source_zone_id", "source_zone_label_raw", "resolved_zone_chapter_label", "intersection_area_m2", "parcel_share_pct", "zoning_precheck_status", "zoning_precheck_confidence", "evidence_ids", "decision_evidence_ids", "context_evidence_ids", "review_scope", "planning_precheck_scope", "policy_profile", "policy_sha256", "document_id", "archive_sha256", "pdf_sha256", "index_content_sha256", "structure_result_content_sha256", "structure_profile", "source_layer", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |
| `PARCEL_PRECHECK_COLUMNS` | `( "zoning_precheck_status", "dominant_zone_precheck_status", "dominant_zone_precheck_confidence", "positive_area_zone_count", "distinct_zone_status_count", "non_dominant_different_status_count", "touch_only_zone_count", "zoning_precheck_evidence_ids", "zoning_precheck_context_evidence_ids", "zoning_precheck_requires_formal_review", "planning_precheck_scope", "review_scope", "non_zoning_planning_features_interpreted", "zoning_precheck_policy_profile", "zoning_precheck_policy_sha256", )` | Defines an implementation domain, schema, unit, role, version, or technical bound consumed by symbols in this module and its static callers. |

## 5. Classes / models / dataclasses

### `BessZoningPrecheckError`

**Purpose:** Raised when the preliminary zoning interpretation cannot be proven.

**Inheritance:** `ValueError`.

**Model form and mutability:** class inheriting from `ValueError`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `_StrictConfigModel`

**Purpose:** Represents checked-in or resolved configuration fields and validates their exact domain before use.

**Inheritance:** `BaseModel`.

**Model form and mutability:** Pydantic model; `model_config` and validators below define strictness, mutation, and extra-field behavior. Decorators: `none`.

**Validation configuration:** `model_config = ConfigDict(extra="forbid", frozen=True)`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

### `PolicySourceLock`

**Purpose:** Represents a validated policy configuration or compiled policy evidence envelope.

**Inheritance:** `_StrictConfigModel`.

**Model form and mutability:** class inheriting from `_StrictConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `document_id` | `StrictStr` | `Field(min_length=1)` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `archive_sha256` | `StrictStr` | `Field(pattern='^[0-9a-f]{64}$')` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `pdf_sha256` | `StrictStr` | `Field(pattern='^[0-9a-f]{64}$')` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `index_content_sha256` | `StrictStr` | `Field(pattern='^[0-9a-f]{64}$')` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `structure_result_content_sha256` | `StrictStr` | `Field(pattern='^[0-9a-f]{64}$')` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `structure_profile` | `StrictStr` | `Field(min_length=1)` | `StrictStr` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- None.

### `PolicyEvidence`

**Purpose:** Represents a validated policy configuration or compiled policy evidence envelope.

**Inheritance:** `_StrictConfigModel`.

**Model form and mutability:** class inheriting from `_StrictConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `evidence_id` | `StrictStr` | `Field(min_length=1)` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `section_id` | `StrictStr` | `Field(min_length=1)` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `page_number` | `StrictInt` | `Field(ge=1)` | `StrictInt` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `evidence_kind` | `EvidenceKind` | `required` | `EvidenceKind` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `evidence_direction` | `EvidenceDirection` | `required` | `EvidenceDirection` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `exact_raw_excerpt` | `StrictStr` | `Field(min_length=1, max_length=600)` | `StrictStr` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `excerpt_sha256` | `StrictStr` | `Field(pattern='^[0-9a-f]{64}$')` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `section_page_fragment_sha256` | `StrictStr` | `Field(pattern='^[0-9a-f]{64}$')` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `excerpt_start` | `StrictInt` | `Field(ge=0)` | `StrictInt` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `excerpt_end` | `StrictInt` | `Field(ge=1)` | `StrictInt` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_rule_id` | `StrictStr` | `Field(min_length=1)` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `source_rule_excerpt` | `StrictStr` | `Field(min_length=1)` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `source_rule_sha256` | `StrictStr` | `Field(pattern='^[0-9a-f]{64}$')` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_rule_start` | `StrictInt` | `Field(ge=0)` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `source_rule_end` | `StrictInt` | `Field(ge=1)` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `interpretation_note` | `StrictStr` | `Field(min_length=1)` | `StrictStr` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_exact_strings` — `def _validate_exact_strings(self) -> PolicyEvidence:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `RouteAssessment`

**Purpose:** Groups the `RouteAssessment` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `_StrictConfigModel`.

**Model form and mutability:** class inheriting from `_StrictConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `route_id` | `StrictStr` | `Field(min_length=1)` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `route_kind` | `RouteKind` | `required` | `RouteKind` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `positive_evidence_ids` | `tuple[StrictStr, ...]` | `()` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `condition_evidence_ids` | `tuple[StrictStr, ...]` | `()` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `difficulty_evidence_ids` | `tuple[StrictStr, ...]` | `()` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `applicability_note` | `StrictStr` | `Field(min_length=1)` | `StrictStr` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_route_shape` — `def _validate_route_shape(self) -> RouteAssessment:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `ChapterPolicy`

**Purpose:** Represents a validated policy configuration or compiled policy evidence envelope.

**Inheritance:** `_StrictConfigModel`.

**Model form and mutability:** class inheriting from `_StrictConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `resolved_zone_chapter_label` | `StrictStr` | `Field(min_length=1)` | `StrictStr` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `review_completeness` | `ReviewCompleteness` | `required` | `ReviewCompleteness` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `reviewed_section_ids` | `tuple[StrictStr, ...]` | `()` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `review_note` | `StrictStr` | `Field(min_length=1)` | `StrictStr` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `zoning_precheck_status` | `ChapterStatus` | `required` | Categorical factual, technical, policy, or diagnostic status; the owning constants/validators define the closed vocabulary. |
| `zoning_precheck_confidence` | `Confidence` | `required` | `Confidence` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `rationale` | `StrictStr` | `Field(min_length=1)` | `StrictStr` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `missing_information` | `StrictStr` | `Field(min_length=1)` | `StrictStr` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `evidence` | `tuple[PolicyEvidence, ...]` | `()` | `tuple[PolicyEvidence, ...]` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `route_assessments` | `tuple[RouteAssessment, ...]` | `()` | `tuple[RouteAssessment, ...]` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_evidence_semantics` — `def _validate_evidence_semantics(self) -> ChapterPolicy:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `BessZoningPolicyConfig`

**Purpose:** Strict source-locked interpretation policy.

**Inheritance:** `_StrictConfigModel`.

**Model form and mutability:** class inheriting from `_StrictConfigModel`. Decorators: `none`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `StrictInt` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_profile` | `StrictStr` | `Field(min_length=1)` | `StrictStr` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `planning_precheck_scope` | `Literal['WRITTEN_ZONING_REGULATION_ONLY']` | `required` | `Literal['WRITTEN_ZONING_REGULATION_ONLY']` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `review_scope` | `Literal['CONFIGURED_USE_CONTROL_ARTICLES_ONLY']` | `required` | `Literal['CONFIGURED_USE_CONTROL_ARTICLES_ONLY']` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_lock` | `PolicySourceLock` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `required_zone_article_numbers` | `tuple[StrictStr, ...]` | `Field(min_length=1)` | `tuple[StrictStr, ...]` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `chapters` | `tuple[ChapterPolicy, ...]` | `Field(min_length=1)` | `tuple[ChapterPolicy, ...]` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |

**Validators and methods:**

- `_validate_policy` — `def _validate_policy(self) -> BessZoningPolicyConfig:`; decorators `model_validator(mode='after')`. The complete method algorithm appears in the function/method section.

### `BessZoningPrecheckResult`

**Purpose:** Immutable envelope around the conservative written-zoning precheck.

**Inheritance:** `object`.

**Model form and mutability:** dataclass (frozen/immutable). Decorators: `dataclass(frozen=True)`.

**Fields:**

| Field | Type | Required/default | Meaning / source / consumers |
|---|---|---|---|
| `result_hash_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `policy_schema_version` | `int` | `required` | Strict integer schema version controlling compatibility; unsupported versions are rejected, not coerced. |
| `policy_profile` | `str` | `required` | `str` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `planning_precheck_scope` | `str` | `required` | `str` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `review_scope` | `str` | `required` | `str` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `document_id` | `str` | `required` | Exact portable identity used to join lineage or evidence across frames and result envelopes. |
| `archive_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `pdf_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `index_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `structure_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `structure_profile` | `str` | `required` | `str` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `policy_config_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `factual_structure_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `zone_mapping_input_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `zoning_relation_hash_columns` | `tuple[str, ...]` | `required` | `tuple[str, ...]` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `zoning_relations_input_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `evidence_catalog_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `evidence_route_links_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `route_assessments_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `chapter_policy_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `source_zone_policy_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `parcel_zone_policy_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `parcel_output_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `complete_result_content_sha256` | `str` | `required` | Lowercase SHA256 lineage/content digest; the prefix names the exact byte or canonical-content component bound by it. |
| `touch_only_relation_count` | `int` | `required` | Strict count; Boolean coercion is rejected where the model/validator requires an exact integer. |
| `evidence_catalog` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `evidence_route_links` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `route_assessments` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `chapter_policy` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `source_zone_policy` | `pd.DataFrame` | `required` | Source lineage or source-bound object whose exact identity is checked before downstream use. |
| `parcel_zone_interpretations` | `pd.DataFrame` | `required` | `pd.DataFrame` state used by `src/landscout/stages/interpret_bess_zoning.py`; allowed values and consumers are fixed by constructors, validators, and algorithms below. |
| `parcels` | `gpd.GeoDataFrame` | `required` | Tabular/spatial evidence carried with the schema, dtype, index, geometry, and preservation contract documented in this module. |

**Validators and methods:**

- None.

### `_UniqueKeyLoader`

**Purpose:** Groups the `UniqueKeyLoader` state and behavior shown by its fields, inheritance, validators, and methods.

**Inheritance:** `yaml.SafeLoader`.

**Model form and mutability:** class inheriting from `yaml.SafeLoader`. Decorators: `none`.

**Fields:**

- No annotated instance fields are declared directly on this class.

**Validators and methods:**

- None.

## 6. Functions and methods

### `PolicyEvidence._validate_exact_strings`

**Signature**

```python
def _validate_exact_strings(self) -> PolicyEvidence:
```

**Purpose**

Validates and rejects malformed exact strings according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `PolicyEvidence`. Observed return expression(s): `self`.

**Algorithm**

1. Iterates `(value, label)` over `((self.evidence_id, 'evidence ID'), (self.section_id, 'evidence section ID'), (self.exact_raw_excerpt, 'exact raw excerpt'), (self.source_rule_id, 'source rule ID'), (self.source_rule_excerpt, 'source rule excerpt'), (self.interpretation_note, 'interpretation note'))`. For each value: Calls `_config_string(value, label)` for its validation or side effect.
2. Checks `sha256(self.exact_raw_excerpt.encode('utf-8')).hexdigest() != self.excerpt_sha256`. When true: Raises `ValueError('evidence excerpt SHA256 differs from exact_raw_excerpt')`.
3. Checks `self.excerpt_end <= self.excerpt_start`. When true: Raises `ValueError('evidence excerpt offsets must be ordered')`.
4. Checks `sha256(self.source_rule_excerpt.encode('utf-8')).hexdigest() != self.source_rule_sha256`. When true: Raises `ValueError('source rule SHA256 differs from source_rule_excerpt')`.
5. Checks `self.source_rule_end <= self.source_rule_start`. When true: Raises `ValueError('source rule offsets must be ordered')`.
6. Checks `not (self.source_rule_start <= self.excerpt_start and self.excerpt_end <= self.source_rule_end)`. When true: Raises `ValueError('evidence excerpt must lie inside its source rule')`.
7. Defines `allowed_directions` with annotation `dict[str, frozenset[str]]` from `{'USE_PERMISSION': frozenset({'SUPPORTS_POTENTIAL_COMPATIBILITY', 'CONTEXT_ONLY'}), 'USE_RESTRICTION': frozenset({'SUPPORTS_DIFFICULTY', 'CONTEXT_ONLY'}), 'PUBLIC_INTEREST_EXCEPTION': frozenset({'SUPPORTS_POTENTIAL_COMPATIBILITY', 'CONDITION', 'CONTEXT_ONLY'}), 'TECHNICAL_EQUIPMENT_RULE': frozenset({'SUPPORTS_POTENTIA…`.
8. Computes `allowed` from `allowed_directions[self.evidence_kind]`.
9. Checks `self.evidence_direction not in allowed`. When true: Raises `ValueError('evidence kind and direction are incompatible')`.
10. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `sha256(self.exact_raw_excerpt.encode('utf-8')).hexdigest() != self.excerpt_sha256` is true.
- Rejects or diverts the path when `self.excerpt_end <= self.excerpt_start` is true.
- Rejects or diverts the path when `sha256(self.source_rule_excerpt.encode('utf-8')).hexdigest() != self.source_rule_sha256` is true.
- Rejects or diverts the path when `self.source_rule_end <= self.source_rule_start` is true.
- Rejects or diverts the path when `not (self.source_rule_start <= self.excerpt_start and self.excerpt_end <= self.source_rule_end)` is true.
- Rejects or diverts the path when `self.evidence_direction not in allowed` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_config_string`, `frozenset`, `model_validator`, `self.exact_raw_excerpt.encode`, `self.source_rule_excerpt.encode`, `sha256`, `sha256(self.exact_raw_excerpt.encode('utf-8')).hexdigest`, `sha256(self.source_rule_excerpt.encode('utf-8')).hexdigest`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `RouteAssessment._validate_route_shape`

**Signature**

```python
def _validate_route_shape(self) -> RouteAssessment:
```

**Purpose**

Validates and rejects malformed route shape according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `RouteAssessment`. Observed return expression(s): `self`.

**Algorithm**

1. Calls `_config_string(self.route_id, 'route ID')` for its validation or side effect.
2. Calls `_config_string(self.applicability_note, 'route applicability note')` for its validation or side effect.
3. Computes `roles` from `{'positive': self.positive_evidence_ids, 'condition': self.condition_evidence_ids, 'difficulty': self.difficulty_evidence_ids}`.
4. Defines `combined` with annotation `list[str]` from `[]`.
5. Iterates `(role, values)` over `roles.items()`. For each value: Computes `normalized` from `[_config_string(value, f'{role} evidence ID') for value in values]`. Checks `len(set(normalized)) != len(normalized)`. When true: Raises `ValueError(f'{role} evidence IDs must be unique within a route')`. Calls `combined.extend(normalized)` for its validation or side effect.
6. Checks `len(set(combined)) != len(combined)`. When true: Raises `ValueError('one evidence ID cannot occupy incompatible route roles')`.
7. Computes `positive` from `bool(self.positive_evidence_ids)`.
8. Computes `condition` from `bool(self.condition_evidence_ids)`.
9. Computes `difficulty` from `bool(self.difficulty_evidence_ids)`.
10. Computes `expected` from `{'DIRECT_ROUTE': (True, False, False), 'CONDITIONAL_ROUTE': (True, True, False), 'RESTRICTION_EXCEPTION_ROUTE': (True, False, True), 'DIFFICULTY_ONLY': (False, False, True)}[self.route_kind]`.
11. Checks `(positive, condition, difficulty) != expected`. When true: Raises `ValueError(f'{self.route_kind} has incompatible evidence-role membership')`.
12. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `len(set(combined)) != len(combined)` is true.
- Rejects or diverts the path when `(positive, condition, difficulty) != expected` is true.
- Rejects or diverts the path when `len(set(normalized)) != len(normalized)` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_config_string`, `bool`, `combined.extend`, `len`, `model_validator`, `roles.items`, `set`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_derived_chapter_status`

**Signature**

```python
def _derived_chapter_status(
    review_completeness: ReviewCompleteness,
    routes: Sequence[RouteAssessment],
) -> ChapterStatus:
```

**Purpose**

Implements derived chapter status according to the exact implementation and guards in this file.

**Inputs**

- `review_completeness` (`ReviewCompleteness`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `routes` (`Sequence[RouteAssessment]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ChapterStatus`. Observed return expression(s): `'UNKNOWN'`; `'CONDITIONAL_REVIEW'`; `'UNKNOWN' if 'DIFFICULTY_ONLY' in kinds else 'POTENTIALLY_COMPATIBLE'`; `'LIKELY_DIFFICULT'`.

**Algorithm**

1. Checks `review_completeness == 'INCOMPLETE'`. When true: Returns `'UNKNOWN'`.
2. Computes `kinds` from `{route.route_kind for route in routes}`.
3. Checks `kinds.intersection({'CONDITIONAL_ROUTE', 'RESTRICTION_EXCEPTION_ROUTE'})`. When true: Returns `'CONDITIONAL_REVIEW'`.
4. Checks `'DIRECT_ROUTE' in kinds`. When true: Returns `'UNKNOWN' if 'DIFFICULTY_ONLY' in kinds else 'POTENTIALLY_COMPATIBLE'`.
5. Checks `'DIFFICULTY_ONLY' in kinds`. When true: Returns `'LIKELY_DIFFICULT'`.
6. Returns `'UNKNOWN'`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `kinds.intersection`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `ChapterPolicy._validate_evidence_semantics`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `ChapterPolicy._validate_evidence_semantics`

**Signature**

```python
def _validate_evidence_semantics(self) -> ChapterPolicy:
```

**Purpose**

Validates and rejects malformed evidence semantics according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ChapterPolicy`. Observed return expression(s): `self`.

**Algorithm**

1. Calls `_config_string(self.resolved_zone_chapter_label, 'chapter label')` for its validation or side effect.
2. Calls `_config_string(self.review_note, 'chapter review note')` for its validation or side effect.
3. Calls `_config_string(self.rationale, 'chapter rationale')` for its validation or side effect.
4. Calls `_config_string(self.missing_information, 'chapter missing information')` for its validation or side effect.
5. Computes `reviewed` from `[_config_string(value, 'reviewed section ID') for value in self.reviewed_section_ids]`.
6. Checks `len(set(reviewed)) != len(reviewed)`. When true: Raises `ValueError('reviewed section IDs must be unique')`.
7. Checks `self.review_completeness == 'INCOMPLETE' and (self.zoning_precheck_status != 'UNKNOWN' or self.zoning_precheck_confidence != 'LOW')`. When true: Raises `ValueError('incomplete review requires UNKNOWN / LOW')`.
8. Computes `route_ids` from `[route.route_id for route in self.route_assessments]`.
9. Checks `len(set(route_ids)) != len(route_ids)`. When true: Raises `ValueError('route IDs must be unique within a chapter')`.
10. Computes `expected_status` from `_derived_chapter_status(self.review_completeness, self.route_assessments)`.
11. Checks `self.zoning_precheck_status != expected_status`. When true: Raises `ValueError('declared chapter status differs from coherent linked route assessments')`.
12. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `len(set(reviewed)) != len(reviewed)` is true.
- Rejects or diverts the path when `self.review_completeness == 'INCOMPLETE' and (self.zoning_precheck_status != 'UNKNOWN' or self.zoning_precheck_confidence != 'LOW')` is true.
- Rejects or diverts the path when `len(set(route_ids)) != len(route_ids)` is true.
- Rejects or diverts the path when `self.zoning_precheck_status != expected_status` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_config_string`, `_derived_chapter_status`, `len`, `model_validator`, `set`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `BessZoningPolicyConfig._validate_policy`

**Signature**

```python
def _validate_policy(self) -> BessZoningPolicyConfig:
```

**Purpose**

Validates and rejects malformed policy according to the exact implementation and guards in this file.

**Inputs**

- `self` (`unannotated`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessZoningPolicyConfig`. Observed return expression(s): `self`.

**Algorithm**

1. Checks `self.schema_version != POLICY_SCHEMA_VERSION`. When true: Raises `ValueError(f'unsupported BESS zoning policy schema: {self.schema_version}')`.
2. Calls `_config_string(self.policy_profile, 'policy profile')` for its validation or side effect.
3. Calls `_config_string(self.source_lock.document_id, 'policy document ID')` for its validation or side effect.
4. Calls `_config_string(self.source_lock.structure_profile, 'policy structure profile')` for its validation or side effect.
5. Computes `article_numbers` from `[_config_string(value, 'required zone article number') for value in self.required_zone_article_numbers]`.
6. Checks `len(set(article_numbers)) != len(article_numbers)`. When true: Raises `ValueError('required zone article numbers must be unique')`.
7. Computes `labels` from `[chapter.resolved_zone_chapter_label for chapter in self.chapters]`.
8. Checks `len(set(labels)) != len(labels)`. When true: Raises `ValueError('chapter policy labels must be unique')`.
9. Defines `evidence_ids` with annotation `set[str]` from `set()`.
10. Defines `route_ids` with annotation `set[str]` from `set()`.
11. Defines `chapter_occurrences` with annotation `dict[tuple[str, str, int, str, int, int], tuple[str, str, str]]` from `{}`.
12. Defines `source_rules` with annotation `dict[str, tuple[object, ...]]` from `{}`.
13. Defines `source_rule_occurrences` with annotation `dict[tuple[object, ...], str]` from `{}`.
14. Defines `source_rule_ranges` with annotation `dict[tuple[str, int, str], list[tuple[int, int, str]]]` from `{}`.
15. Iterates `chapter` over `self.chapters`. For each value: Computes `chapter_evidence` from `{evidence.evidence_id: evidence for evidence in chapter.evidence}`. Defines `linked_evidence_ids` with annotation `set[str]` from `set()`. Iterates `evidence` over `chapter.evidence`. For each value: Checks `evidence.evidence_id in evidence_ids`. When true: Raises `ValueError('evidence IDs must be globally unique')`. Calls `evidence_ids.add(evidence.evidence_id)` for its validation or side effect. Computes `key` from `(chapter.resolved_zone_chapter_label, evidence.section_id, evidence.page_number, evidence.section_page_fragment_sha256, evidence.excerpt_start, evidence.excerpt_end)`. Executes 16 additional source-ordered statement(s). Executes 2 additional source-ordered statement(s).
16. Returns `self`.

**Validation and invariants**

- Rejects or diverts the path when `self.schema_version != POLICY_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `len(set(article_numbers)) != len(article_numbers)` is true.
- Rejects or diverts the path when `len(set(labels)) != len(labels)` is true.
- Rejects or diverts the path when `evidence.evidence_id in evidence_ids` is true.
- Rejects or diverts the path when `previous is not None` is true.
- Rejects or diverts the path when `prior_rule is not None and prior_rule != rule_identity` is true.
- Rejects or diverts the path when `prior_rule_id is not None and prior_rule_id != evidence.source_rule_id` is true.
- Rejects or diverts the path when `route.route_id in route_ids` is true.
- Rejects or diverts the path when `evidence.evidence_direction == 'CONTEXT_ONLY' and is_linked` is true.
- Rejects or diverts the path when `evidence.evidence_direction != 'CONTEXT_ONLY' and (not is_linked)` is true.
- Rejects or diverts the path when `overlaps and (not identical)` is true.
- Rejects or diverts the path when `referenced_evidence is None` is true.
- Rejects or diverts the path when `referenced_evidence.evidence_direction != expected_direction` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `_config_string`, `chapter_evidence.get`, `chapter_occurrences.get`, `evidence_ids.add`, `len`, `linked_evidence_ids.add`, `max`, `min`, `model_validator`, `ranges.append`, `route_ids.add`, `set`, `source_rule_occurrences.get`, `source_rule_ranges.setdefault`, `source_rules.get`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

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
2. Iterates `(key_node, value_node)` over `node.value`. For each value: Computes `key` from `loader.construct_object(key_node, deep=deep)`. Checks `key in result`. When true: Raises `BessZoningPrecheckError(f'Duplicate YAML policy key: {key!r}')`. Computes `result[key]` from `loader.construct_object(value_node, deep=deep)`.
3. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `key in result` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `loader.construct_object`.

**Known repository callers**

No direct repository caller found.

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_config_string`

**Signature**

```python
def _config_string(value: str, label: str) -> str:
```

**Purpose**

Implements config string according to the exact implementation and guards in this file.

**Inputs**

- `value` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not value or value != value.strip()`. When true: Raises `ValueError(f'{label} must be a non-empty exact string')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not value or value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `ValueError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `ValueError`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `BessZoningPolicyConfig._validate_policy`
- `src/landscout/stages/interpret_bess_zoning.py` — `ChapterPolicy._validate_evidence_semantics`
- `src/landscout/stages/interpret_bess_zoning.py` — `PolicyEvidence._validate_exact_strings`
- `src/landscout/stages/interpret_bess_zoning.py` — `RouteAssessment._validate_route_shape`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `load_bess_zoning_policy_config`

**Signature**

```python
def load_bess_zoning_policy_config(path: str | Path) -> BessZoningPolicyConfig:
```

**Purpose**

Load a strict policy while rejecting duplicate YAML keys.

**Inputs**

- `path` (`str | Path`; required) — filesystem location participating in the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessZoningPolicyConfig`. Observed return expression(s): `BessZoningPolicyConfig.model_validate(payload)`.

**Algorithm**

1. Runs guarded operation: Computes `payload` from `yaml.load(Path(path).read_text(encoding='utf-8'), Loader=_UniqueKeyLoader)`. Checks `not isinstance(payload, Mapping)`. When true: Raises `BessZoningPrecheckError('BESS zoning policy must be a mapping')`. Returns `BessZoningPolicyConfig.model_validate(payload)`. Handles `BessZoningPrecheckError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(payload, Mapping)` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `Path(path).read_text`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `BessZoningPrecheckError`, `Path`, `Path(path).read_text`, `isinstance`, `yaml.load`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_resolved_policy`
- `tests/unit/test_interpret_bess_zoning.py` — `test_duplicate_yaml_key_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_policy_yaml_roundtrip_is_strict`
- `tests/unit/test_interpret_bess_zoning.py` — `test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite`
- `tests/unit/test_interpret_bess_zoning.py` — `test_real_muret_source_rules_preserve_conditional_and_exception_frames`
- `tests/unit/test_interpret_bess_zoning.py` — `test_real_muret_up_and_aup_keep_icpe_applicability_as_context`
- `tests/unit/test_interpret_bess_zoning.py` — `test_real_muret_up_route_does_not_use_the_separate_icpe_condition`

**Tests**

- `tests/unit/test_interpret_bess_zoning.py::test_duplicate_yaml_key_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_policy_yaml_roundtrip_is_strict`
- `tests/unit/test_interpret_bess_zoning.py::test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite`
- `tests/unit/test_interpret_bess_zoning.py::test_real_muret_source_rules_preserve_conditional_and_exception_frames`
- `tests/unit/test_interpret_bess_zoning.py::test_real_muret_up_and_aup_keep_icpe_applicability_as_context`
- `tests/unit/test_interpret_bess_zoning.py::test_real_muret_up_route_does_not_use_the_separate_icpe_condition`

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

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

- Declared return type: `str`. Observed return expression(s): `value`.

**Algorithm**

1. Checks `not isinstance(value, str) or not value or value != value.strip()`. When true: Raises `BessZoningPrecheckError(f'{label} must be a non-empty exact string')`.
2. Returns `value`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(value, str) or not value or value != value.strip()` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `isinstance`, `value.strip`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_chapter_policy`
- `src/landscout/stages/interpret_bess_zoning.py` — `_build_parcel_output`
- `src/landscout/stages/interpret_bess_zoning.py` — `_build_source_zone_policy`
- `src/landscout/stages/interpret_bess_zoning.py` — `_exact_id_series`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_mapping`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_policy_evidence`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_relations`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_zones`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validated_sha256`
- `src/landscout/stages/interpret_bess_zoning.py` — `_zone_chapter_rows`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_strict_nonnegative_integer`

**Signature**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

**Purpose**

Implements strict nonnegative integer according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `int`. Observed return expression(s): `result`.

**Algorithm**

1. Checks `isinstance(value, bool) or not isinstance(value, Integral)`. When true: Raises `BessZoningPrecheckError(f'{label} must be an integer')`.
2. Computes `result` from `int(value)`.
3. Checks `result < 0`. When true: Raises `BessZoningPrecheckError(f'{label} must be non-negative')`.
4. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Integral)` is true.
- Rejects or diverts the path when `result < 0` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `int`, `isinstance`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_compare_results`
- `src/landscout/stages/interpret_bess_zoning.py` — `_strict_positive_integer`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_parcels`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_strict_positive_integer`

**Signature**

```python
def _strict_positive_integer(value: object, label: str) -> int:
```

**Purpose**

Implements strict positive integer according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `int`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `result` from `_strict_nonnegative_integer(value, label)`.
2. Checks `result < 1`. When true: Raises `BessZoningPrecheckError(f'{label} must be positive')`.
3. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `result < 1` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_strict_nonnegative_integer`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_compare_results`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_policy_evidence`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_validated_sha256`

**Signature**

```python
def _validated_sha256(value: object, label: str) -> str:
```

**Purpose**

Validates and returns canonical sha256 according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `checksum`.

**Algorithm**

1. Computes `checksum` from `_strict_string(value, label)`.
2. Checks `re.fullmatch('[0-9a-f]{64}', checksum) is None`. When true: Raises `BessZoningPrecheckError(f'{label} must be exactly 64 lowercase hexadecimal characters')`.
3. Returns `checksum`.

**Validation and invariants**

- Rejects or diverts the path when `re.fullmatch('[0-9a-f]{64}', checksum) is None` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_strict_string`, `re.fullmatch`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_compare_results`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_strict_nonnegative_number`

**Signature**

```python
def _strict_nonnegative_number(value: object, label: str) -> float:
```

**Purpose**

Implements strict nonnegative number according to the exact implementation and guards in this file.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `float`. Observed return expression(s): `result`.

**Algorithm**

1. Checks `isinstance(value, bool) or not isinstance(value, Real)`. When true: Raises `BessZoningPrecheckError(f'{label} must be numeric')`.
2. Runs guarded operation: Computes `result` from `float(value)`. Handles `(TypeError, ValueError, OverflowError)`.
3. Checks `not math.isfinite(result) or result < 0`. When true: Raises `BessZoningPrecheckError(f'{label} must be finite and non-negative')`.
4. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(value, bool) or not isinstance(value, Real)` is true.
- Rejects or diverts the path when `not math.isfinite(result) or result < 0` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `float`, `isinstance`, `math.isfinite`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_relations`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

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

- Declared return type: `object`. Observed return expression(s): `None`; `_canonical_value(value.item())`; `to_wkb(value, hex=True, include_srid=False)`; `value.isoformat()`; `value.hex()`; `[_canonical_value(item) for item in value]`; `{str(key): _canonical_value(item) for key, item in value.items()}`; `value`.

**Algorithm**

1. Checks `value is None or value is pd.NA`. When true: Returns `None`.
2. Checks `isinstance(value, np.generic)`. When true: Returns `_canonical_value(value.item())`.
3. Checks `isinstance(value, BaseGeometry)`. When true: Returns `to_wkb(value, hex=True, include_srid=False)`.
4. Checks `isinstance(value, (pd.Timestamp, datetime, date))`. When true: Returns `value.isoformat()`.
5. Checks `isinstance(value, bytes)`. When true: Returns `value.hex()`.
6. Checks `isinstance(value, (tuple, list, np.ndarray))`. When true: Returns `[_canonical_value(item) for item in value]`.
7. Checks `isinstance(value, Mapping)`. When true: Returns `{str(key): _canonical_value(item) for key, item in value.items()}`.
8. Checks `isinstance(value, float) and math.isnan(value)`. When true: Returns `None`.
9. Checks `isinstance(value, (str, int, float, bool))`. When true: Returns `value`.
10. Raises `BessZoningPrecheckError(f'Value of type {type(value).__name__} cannot be canonically serialized')`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_canonical_value`, `isinstance`, `math.isnan`, `str`, `to_wkb`, `type`, `value.hex`, `value.isoformat`, `value.item`, `value.items`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_canonical_sha256`
- `src/landscout/stages/interpret_bess_zoning.py` — `_compare_frames`
- `src/landscout/stages/interpret_bess_zoning.py` — `_compare_results`
- `src/landscout/stages/interpret_bess_zoning.py` — `_frame_payload`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

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

- Declared return type: `str`. Observed return expression(s): `sha256(serialized).hexdigest()`.

**Algorithm**

1. Runs guarded operation: Computes `serialized` from `json.dumps(_canonical_value(value), ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')`. Handles `BessZoningPrecheckError`, `Exception`.
2. Returns `sha256(serialized).hexdigest()`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_canonical_value`, `json.dumps`, `json.dumps(_canonical_value(value), ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode`, `sha256`, `sha256(serialized).hexdigest`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_complete_result_sha256`
- `src/landscout/stages/interpret_bess_zoning.py` — `_factual_structure_sha256`
- `src/landscout/stages/interpret_bess_zoning.py` — `_frame_sha256`
- `src/landscout/stages/interpret_bess_zoning.py` — `_policy_sha256`
- `src/landscout/stages/interpret_bess_zoning.py` — `_result_frame_sha256`
- `src/landscout/stages/interpret_bess_zoning.py` — `_zone_mapping_input_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_frame_payload`

**Signature**

```python
def _frame_payload(frame: pd.DataFrame, columns: Sequence[str]) -> dict[str, object]:
```

**Purpose**

Implements frame payload according to the exact implementation and guards in this file.

**Inputs**

- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`Sequence[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `payload`.

**Algorithm**

1. Runs guarded operation: Checks `frame.columns.has_duplicates`. When true: Raises `BessZoningPrecheckError('DataFrame columns must be unique')`. Computes `missing` from `[column for column in columns if column not in frame.columns]`. Checks `missing`. When true: Raises `BessZoningPrecheckError(f'DataFrame is missing columns: {missing}')`. Defines `payload` with annotation `dict[str, object]` from `{'columns': list(columns), 'index_names': list(frame.index.names), 'index': [_canonical_value(value) for value in frame.index.tolist()], 'rows': frame.loc[:, columns].to_dict('records')}`. Executes 2 additional source-ordered statement(s). Handles `BessZoningPrecheckError`, `Exception`.

**Validation and invariants**

- Rejects or diverts the path when `frame.columns.has_duplicates` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `isinstance(frame, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `frame.crs is None` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `CRS.from_user_input`, `CRS.from_user_input(frame.crs).to_json_dict`, `_canonical_value`, `frame.index.tolist`, `frame.loc[:, columns].to_dict`, `isinstance`, `list`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_compare_frames`
- `src/landscout/stages/interpret_bess_zoning.py` — `_compare_results`
- `src/landscout/stages/interpret_bess_zoning.py` — `_frame_sha256`
- `src/landscout/stages/interpret_bess_zoning.py` — `_result_frame_sha256`
- `src/landscout/stages/interpret_bess_zoning.py` — `_zone_mapping_input_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_frame_sha256`

**Signature**

```python
def _frame_sha256(domain: str, frame: pd.DataFrame, columns: Sequence[str]) -> str:
```

**Purpose**

Implements frame sha256 according to the exact implementation and guards in this file.

**Inputs**

- `domain` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`Sequence[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': domain, **_frame_payload(frame, columns)})`.

**Algorithm**

1. Returns `_canonical_sha256({'domain': domain, **_frame_payload(frame, columns)})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `_frame_payload`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_policy_sha256`

**Signature**

```python
def _policy_sha256(config: BessZoningPolicyConfig) -> str:
```

**Purpose**

Implements policy sha256 according to the exact implementation and guards in this file.

**Inputs**

- `config` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': 'landscout.bess_zoning.policy_config', 'config': config.model_dump(mode='json')})`.

**Algorithm**

1. Returns `_canonical_sha256({'domain': 'landscout.bess_zoning.policy_config', 'config': config.model_dump(mode='json')})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `config.model_dump`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_factual_structure_sha256`

**Signature**

```python
def _factual_structure_sha256(
    structure: PlanningRegulationStructureResult,
) -> str:
```

**Purpose**

Implements factual structure sha256 according to the exact implementation and guards in this file.

**Inputs**

- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': 'landscout.bess_zoning.factual_structure_input', 'structure_result_content_sha256': structure.structure_result_content_sha256, 'section_hash_schema_version': structure.section_hash_schema_version, 'structure_config_sha256': structure.structure_config_sha256, 'sections_content_sha256': structure.sections_content_sha256, 'zone_map_content_sha256': structure.zone_map_con…`.

**Algorithm**

1. Returns `_canonical_sha256({'domain': 'landscout.bess_zoning.factual_structure_input', 'structure_result_content_sha256': structure.structure_result_content_sha256, 'section_hash_schema_version': structure.section_hash_schema_version, 'structure_config_sha256': structure.structure_config_sha256, 'sections_content_sha256': structure.sections_content_sha256, 'zone_map…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_resolved_policy`

**Signature**

```python
def _resolved_policy(
    policy: BessZoningPolicyConfig | str | Path,
) -> BessZoningPolicyConfig:
```

**Purpose**

Implements resolved policy according to the exact implementation and guards in this file.

**Inputs**

- `policy` (`BessZoningPolicyConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessZoningPolicyConfig`. Observed return expression(s): `load_bess_zoning_policy_config(policy)`; `BessZoningPolicyConfig.model_validate(policy.model_dump(mode='python'))`.

**Algorithm**

1. Checks `isinstance(policy, BessZoningPolicyConfig)`. When true: Runs guarded operation: Returns `BessZoningPolicyConfig.model_validate(policy.model_dump(mode='python'))`. Handles `Exception`.
2. Returns `load_bess_zoning_policy_config(policy)`.

**Validation and invariants**

- Rejects or diverts the path when `isinstance(policy, BessZoningPolicyConfig)` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `load_bess_zoning_policy_config`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessZoningPolicyConfig.model_validate`, `BessZoningPrecheckError`, `isinstance`, `load_bess_zoning_policy_config`, `policy.model_dump`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `interpret_bess_zoning`
- `src/landscout/stages/interpret_bess_zoning.py` — `validate_bess_zoning_precheck`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_validate_policy_lock`

**Signature**

```python
def _validate_policy_lock(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> None:
```

**Purpose**

Validates and rejects malformed policy lock according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `lock` from `policy.source_lock`.
2. Computes `comparisons` from `((lock.document_id, index.document_id, 'document ID'), (lock.archive_sha256, index.archive_sha256, 'archive SHA256'), (lock.pdf_sha256, index.pdf_sha256, 'PDF SHA256'), (lock.index_content_sha256, index.index_content_sha256, 'index SHA256'), (lock.structure_result_content_sha256, structure.structure_result_content_sha…`.
3. Iterates `(actual, expected, label)` over `comparisons`. For each value: Checks `actual != expected`. When true: Raises `BessZoningPrecheckError(f'BESS zoning policy {label} differs from factual source')`.

**Validation and invariants**

- Rejects or diverts the path when `actual != expected` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_exact_id_series`

**Signature**

```python
def _exact_id_series(series: pd.Series, label: str, *, unique: bool) -> tuple[str, ...]:
```

**Purpose**

Implements exact id series according to the exact implementation and guards in this file.

**Inputs**

- `series` (`pd.Series`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `unique` (`bool`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[str, ...]`. Observed return expression(s): `tuple(values)`.

**Algorithm**

1. Defines `values` with annotation `list[str]` from `[]`.
2. Iterates `value` over `series.tolist()`. For each value: Calls `values.append(_strict_string(value, label))` for its validation or side effect.
3. Checks `unique and len(set(values)) != len(values)`. When true: Raises `BessZoningPrecheckError(f'{label} values must be unique')`.
4. Returns `tuple(values)`.

**Validation and invariants**

- Rejects or diverts the path when `unique and len(set(values)) != len(values)` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_strict_string`, `len`, `series.tolist`, `set`, `tuple`, `values.append`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_compare_results`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_mapping`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_parcels`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_relations`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_zones`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_validate_parcels`

**Signature**

```python
def _validate_parcels(
    index: PlanningRegulationIndex,
    parcels: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
```

**Purpose**

Validates and rejects malformed parcels according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `parcels.copy(deep=True)`.

**Algorithm**

1. Checks `not isinstance(parcels, gpd.GeoDataFrame)`. When true: Raises `BessZoningPrecheckError('parcels must be a GeoDataFrame')`.
2. Checks `parcels.columns.has_duplicates`. When true: Raises `BessZoningPrecheckError('Parcel columns must be unique')`.
3. Computes `required` from `{'parcel_id', 'geometry', 'dominant_planning_zone_id', 'planning_surface_relation_count', 'prescription_surface_relation_count', 'information_surface_relation_count', 'planning_line_relation_count', 'planning_point_relation_count', 'planning_feature_document_id', 'planning_feature_archive_sha256', 'planning_document_i…`.
4. Computes `missing` from `sorted(required.difference(parcels.columns))`.
5. Checks `missing`. When true: Raises `BessZoningPrecheckError(f'Parcel input is missing columns: {missing}')`.
6. Computes `collisions` from `sorted(set(PARCEL_PRECHECK_COLUMNS).intersection(parcels.columns))`.
7. Checks `collisions`. When true: Raises `BessZoningPrecheckError(f'Parcel input already contains precheck columns: {collisions}')`.
8. Checks `parcels.crs is None`. When true: Raises `BessZoningPrecheckError('Parcel CRS is required')`.
9. Runs guarded operation: Calls `CRS.from_user_input(parcels.crs)` for its validation or side effect. Checks `parcels.geometry.name != 'geometry'`. When true: Raises `BessZoningPrecheckError('Parcel geometry must be active')`. Handles `BessZoningPrecheckError`, `Exception`.
10. Calls `_exact_id_series(parcels['parcel_id'], 'parcel ID', unique=True)` for its validation or side effect.
11. Computes `geometry` from `parcels.geometry`.
12. Checks `geometry.isna().any() or geometry.is_empty.any() or (~geometry.is_valid).any()`. When true: Raises `BessZoningPrecheckError('Parcel geometry must be non-null, non-empty, and valid')`.
13. Checks `not geometry.geom_type.isin({'Polygon', 'MultiPolygon'}).all()`. When true: Raises `BessZoningPrecheckError('Parcel geometry must be Polygon or MultiPolygon')`.
14. Iterates `column` over `('planning_surface_relation_count', 'prescription_surface_relation_count', 'information_surface_relation_count', 'planning_line_relation_count', 'planning_point_relation_count')`. For each value: Iterates `value` over `parcels[column].tolist()`. For each value: Calls `_strict_nonnegative_integer(value, column)` for its validation or side effect.
15. Iterates `document_column` over `('planning_document_id', 'planning_feature_document_id')`. For each value: Checks `not parcels[document_column].eq(index.document_id).all()`. When true: Raises `BessZoningPrecheckError(f'Parcel {document_column} lineage differs from the regulation')`.
16. Iterates `archive_column` over `('planning_archive_sha256', 'planning_feature_archive_sha256')`. For each value: Checks `not parcels[archive_column].eq(index.archive_sha256).all()`. When true: Raises `BessZoningPrecheckError(f'Parcel {archive_column} lineage differs from the regulation')`.
17. Returns `parcels.copy(deep=True)`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(parcels, gpd.GeoDataFrame)` is true.
- Rejects or diverts the path when `parcels.columns.has_duplicates` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `collisions` is true.
- Rejects or diverts the path when `parcels.crs is None` is true.
- Rejects or diverts the path when `geometry.isna().any() or geometry.is_empty.any() or (~geometry.is_valid).any()` is true.
- Rejects or diverts the path when `not geometry.geom_type.isin({'Polygon', 'MultiPolygon'}).all()` is true.
- Rejects or diverts the path when `parcels.geometry.name != 'geometry'` is true.
- Rejects or diverts the path when `not parcels[document_column].eq(index.document_id).all()` is true.
- Rejects or diverts the path when `not parcels[archive_column].eq(index.archive_sha256).all()` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `parcels.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(~geometry.is_valid).any`, `BessZoningPrecheckError`, `CRS.from_user_input`, `_exact_id_series`, `_strict_nonnegative_integer`, `geometry.geom_type.isin`, `geometry.geom_type.isin({'Polygon', 'MultiPolygon'}).all`, `geometry.is_empty.any`, `geometry.isna`, `geometry.isna().any`, `isinstance`, `parcels.copy`, `parcels[archive_column].eq`, `parcels[archive_column].eq(index.archive_sha256).all`, `parcels[column].tolist`, `parcels[document_column].eq`, `parcels[document_column].eq(index.document_id).all`, `required.difference`, `set`, `set(PARCEL_PRECHECK_COLUMNS).intersection`, `sorted`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_validate_zones`

**Signature**

```python
def _validate_zones(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
) -> pd.DataFrame:
```

**Purpose**

Validates and rejects malformed zones according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `result`.

**Algorithm**

1. Checks `not isinstance(zones, pd.DataFrame) or zones.columns.has_duplicates`. When true: Raises `BessZoningPrecheckError('zones must be a DataFrame with unique columns')`.
2. Computes `required` from `('planning_zone_id', 'source_zone_id', 'zone_label_raw', 'source_document_id', 'source_archive_sha256', 'source_layer')`.
3. Computes `missing` from `[column for column in required if column not in zones.columns]`.
4. Checks `missing`. When true: Raises `BessZoningPrecheckError(f'Zone catalog is missing columns: {missing}')`.
5. Computes `result` from `zones.copy(deep=True)`.
6. Calls `_exact_id_series(result['planning_zone_id'], 'planning zone ID', unique=True)` for its validation or side effect.
7. Calls `_exact_id_series(result['source_zone_id'], 'source zone ID', unique=True)` for its validation or side effect.
8. Calls `_exact_id_series(result['zone_label_raw'], 'raw zone label', unique=False)` for its validation or side effect.
9. Checks `not result['source_document_id'].eq(index.document_id).all()`. When true: Raises `BessZoningPrecheckError('Zone catalog document lineage differs')`.
10. Checks `not result['source_archive_sha256'].eq(index.archive_sha256).all()`. When true: Raises `BessZoningPrecheckError('Zone catalog archive lineage differs')`.
11. Iterates `value` over `result['source_layer'].tolist()`. For each value: Calls `_strict_string(value, 'zone source layer')` for its validation or side effect.
12. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(zones, pd.DataFrame) or zones.columns.has_duplicates` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `not result['source_document_id'].eq(index.document_id).all()` is true.
- Rejects or diverts the path when `not result['source_archive_sha256'].eq(index.archive_sha256).all()` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `zones.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessZoningPrecheckError`, `_exact_id_series`, `_strict_string`, `isinstance`, `result['source_archive_sha256'].eq`, `result['source_archive_sha256'].eq(index.archive_sha256).all`, `result['source_document_id'].eq`, `result['source_document_id'].eq(index.document_id).all`, `result['source_layer'].tolist`, `zones.copy`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_validate_relations`

**Signature**

```python
def _validate_relations(
    index: PlanningRegulationIndex,
    parcels: gpd.GeoDataFrame,
    zones: pd.DataFrame,
    relations: pd.DataFrame,
) -> pd.DataFrame:
```

**Purpose**

Validates and rejects malformed relations according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `result`.

**Algorithm**

1. Checks `not isinstance(relations, pd.DataFrame) or relations.columns.has_duplicates`. When true: Raises `BessZoningPrecheckError('zoning_intersections must be a DataFrame with unique columns')`.
2. Computes `required` from `('parcel_id', 'planning_zone_id', 'source_zone_id', 'zone_label_raw', 'relation_type', 'intersection_area_m2', 'parcel_metric_area_m2', 'zone_area_m2', 'parcel_share_pct', 'zone_share_pct', 'source_document_id', 'source_archive_sha256', 'source_layer')`.
3. Computes `missing` from `[column for column in required if column not in relations.columns]`.
4. Checks `missing`. When true: Raises `BessZoningPrecheckError(f'Zoning relations are missing columns: {missing}')`.
5. Computes `result` from `relations.copy(deep=True)`.
6. Checks `result.duplicated(['parcel_id', 'planning_zone_id']).any()`. When true: Raises `BessZoningPrecheckError('Parcel/zone relations must be unique')`.
7. Computes `parcel_ids` from `set(_exact_id_series(parcels['parcel_id'], 'parcel ID', unique=True))`.
8. Checks `not set(_exact_id_series(result['parcel_id'], 'relation parcel ID', unique=False)).issubset(parcel_ids)`. When true: Raises `BessZoningPrecheckError('Zoning relation references an unknown parcel')`.
9. Computes `zone_records` from `zones.set_index('planning_zone_id')[['source_zone_id', 'zone_label_raw', 'source_layer']].to_dict('index')`.
10. Iterates `row` over `result.to_dict('records')`. For each value: Computes `planning_id` from `_strict_string(row['planning_zone_id'], 'relation planning zone ID')`. Computes `source_id` from `_strict_string(row['source_zone_id'], 'relation source zone ID')`. Computes `label` from `_strict_string(row['zone_label_raw'], 'relation raw zone label')`. Executes 15 additional source-ordered statement(s).
11. Returns `result`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(relations, pd.DataFrame) or relations.columns.has_duplicates` is true.
- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `result.duplicated(['parcel_id', 'planning_zone_id']).any()` is true.
- Rejects or diverts the path when `not set(_exact_id_series(result['parcel_id'], 'relation parcel ID', unique=False)).issubset(parcel_ids)` is true.
- Rejects or diverts the path when `expected_zone is None` is true.
- Rejects or diverts the path when `source_id != expected_zone['source_zone_id'] or label != expected_zone['zone_label_raw']` is true.
- Rejects or diverts the path when `row['source_layer'] != expected_zone['source_layer']` is true.
- Rejects or diverts the path when `relation_type == 'AREA_OVERLAP' and area <= 0` is true.
- Rejects or diverts the path when `relation_type == 'TOUCH_ONLY' and area != 0` is true.
- Rejects or diverts the path when `relation_type not in {'AREA_OVERLAP', 'TOUCH_ONLY'}` is true.
- Rejects or diverts the path when `row['source_document_id'] != index.document_id` is true.
- Rejects or diverts the path when `row['source_archive_sha256'] != index.archive_sha256` is true.
- Rejects or diverts the path when `upper <= 0` is true.
- Rejects or diverts the path when `area - upper > technical_overlay_tolerance(upper)` is true.
- Rejects or diverts the path when `reference_area <= 0` is true.
- Rejects or diverts the path when `abs(percentage_area - area) > technical_overlay_tolerance(reference_area)` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `relations.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessZoningPrecheckError`, `_exact_id_series`, `_strict_nonnegative_number`, `_strict_string`, `abs`, `isinstance`, `relations.copy`, `result.duplicated`, `result.duplicated(['parcel_id', 'planning_zone_id']).any`, `result.to_dict`, `set`, `set(_exact_id_series(result['parcel_id'], 'relation parcel ID', unique=False)).issubset`, `technical_overlay_tolerance`, `zone_records.get`, `zones.set_index`, `zones.set_index('planning_zone_id')[['source_zone_id', 'zone_label_raw', 'source_layer']].to_dict`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_zone_mapping_input_sha256`

**Signature**

```python
def _zone_mapping_input_sha256(
    zones: pd.DataFrame,
    structure: PlanningRegulationStructureResult,
) -> str:
```

**Purpose**

Implements zone mapping input sha256 according to the exact implementation and guards in this file.

**Inputs**

- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': 'landscout.bess_zoning.zone_mapping_input', 'zones': _frame_payload(zones, zone_columns), 'mapping': _frame_payload(structure.zone_mapping, tuple((str(column) for column in structure.zone_mapping.columns)))})`.

**Algorithm**

1. Computes `zone_columns` from `('planning_zone_id', 'source_zone_id', 'zone_label_raw', 'source_document_id', 'source_archive_sha256', 'source_layer')`.
2. Returns `_canonical_sha256({'domain': 'landscout.bess_zoning.zone_mapping_input', 'zones': _frame_payload(zones, zone_columns), 'mapping': _frame_payload(structure.zone_mapping, tuple((str(column) for column in structure.zone_mapping.columns)))})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `_frame_payload`, `str`, `tuple`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_zone_chapter_rows`

**Signature**

```python
def _zone_chapter_rows(
    structure: PlanningRegulationStructureResult,
) -> list[dict[str, object]]:
```

**Purpose**

Implements zone chapter rows according to the exact implementation and guards in this file.

**Inputs**

- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `list[dict[str, object]]`. Observed return expression(s): `rows`.

**Algorithm**

1. Computes `rows` from `structure.sections.loc[structure.sections['section_type'].eq('ZONE_CHAPTER')].to_dict('records')`.
2. Computes `labels` from `[_strict_string(row['zone_chapter_label'], 'zone chapter label') for row in rows]`.
3. Computes `section_ids` from `[_strict_string(row['section_id'], 'zone chapter section ID') for row in rows]`.
4. Checks `len(set(labels)) != len(labels)`. When true: Raises `BessZoningPrecheckError('Regulation zone chapter labels must be unique')`.
5. Checks `len(set(section_ids)) != len(section_ids)`. When true: Raises `BessZoningPrecheckError('Regulation zone chapter section IDs must be unique')`.
6. Returns `rows`.

**Validation and invariants**

- Rejects or diverts the path when `len(set(labels)) != len(labels)` is true.
- Rejects or diverts the path when `len(set(section_ids)) != len(section_ids)` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_strict_string`, `len`, `set`, `structure.sections.loc[structure.sections['section_type'].eq('ZONE_CHAPTER')].to_dict`, `structure.sections['section_type'].eq`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_chapter_policy`
- `src/landscout/stages/interpret_bess_zoning.py` — `_required_section_ids_by_chapter`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_mapping`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_policy_evidence`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_required_section_ids_by_chapter`

**Signature**

```python
def _required_section_ids_by_chapter(
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> dict[str, tuple[str, ...]]:
```

**Purpose**

Implements required section ids by chapter according to the exact implementation and guards in this file.

**Inputs**

- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, tuple[str, ...]]`. Observed return expression(s): `result`.

**Algorithm**

1. Computes `required_numbers` from `set(policy.required_zone_article_numbers)`.
2. Computes `chapter_ids` from `{row['zone_chapter_label']: row['section_id'] for row in _zone_chapter_rows(structure)}`.
3. Defines `result` with annotation `dict[str, tuple[str, ...]]` from `{}`.
4. Computes `section_rows` from `structure.sections.to_dict('records')`.
5. Iterates `(label, chapter_id)` over `chapter_ids.items()`. For each value: Computes `result[str(label)]` from `tuple((str(row['section_id']) for row in section_rows if row['section_type'] == 'ARTICLE' and row['parent_section_id'] == chapter_id and (row['article_number_raw'] in required_numbers)))`.
6. Returns `result`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_zone_chapter_rows`, `chapter_ids.items`, `set`, `str`, `structure.sections.to_dict`, `tuple`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_chapter_policy`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_policy_evidence`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_validate_evidence_occurrence_uniqueness`

**Signature**

```python
def _validate_evidence_occurrence_uniqueness(catalog: pd.DataFrame) -> None:
```

**Purpose**

Validates and rejects malformed evidence occurrence uniqueness according to the exact implementation and guards in this file.

**Inputs**

- `catalog` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Computes `missing` from `set(_EVIDENCE_OCCURRENCE_COLUMNS).difference(catalog.columns)`.
2. Checks `missing`. When true: Raises `BessZoningPrecheckError(f'Evidence catalog lacks occurrence fields: {sorted(missing)}')`.
3. Checks `catalog.duplicated(list(_EVIDENCE_OCCURRENCE_COLUMNS)).any()`. When true: Raises `BessZoningPrecheckError('Evidence catalog contains a duplicate chapter-scoped evidence occurrence')`.

**Validation and invariants**

- Rejects or diverts the path when `missing` is true.
- Rejects or diverts the path when `catalog.duplicated(list(_EVIDENCE_OCCURRENCE_COLUMNS)).any()` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `catalog.duplicated`, `catalog.duplicated(list(_EVIDENCE_OCCURRENCE_COLUMNS)).any`, `list`, `set`, `set(_EVIDENCE_OCCURRENCE_COLUMNS).difference`, `sorted`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_compare_results`
- `src/landscout/stages/interpret_bess_zoning.py` — `_validate_policy_evidence`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_validate_policy_evidence`

**Signature**

```python
def _validate_policy_evidence(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    fragments: pd.DataFrame,
    policy_hash: str,
    evidence_route_links: pd.DataFrame,
) -> tuple[dict[str, dict[str, object]], pd.DataFrame]:
```

**Purpose**

Validates and rejects malformed policy evidence according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `fragments` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_hash` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `evidence_route_links` (`pd.DataFrame`; required) — exact identifier/code used by the contract. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `tuple[dict[str, dict[str, object]], pd.DataFrame]`. Observed return expression(s): `(chapters, catalog)`.

**Algorithm**

1. Computes `sections` from `{_strict_string(row['section_id'], 'section ID'): row for row in structure.sections.to_dict('records')}`.
2. Computes `fragment_records` from `{(_strict_string(row['section_id'], 'fragment section ID'), _strict_positive_integer(row['page_number'], 'fragment page number')): row for row in fragments.to_dict('records')}`.
3. Computes `chapters` from `{_strict_string(row['zone_chapter_label'], 'zone chapter label'): row for row in _zone_chapter_rows(structure)}`.
4. Computes `policy_labels` from `{chapter.resolved_zone_chapter_label for chapter in policy.chapters}`.
5. Checks `policy_labels != set(chapters)`. When true: Computes `missing` from `sorted(set(chapters).difference(policy_labels))`. Computes `extra` from `sorted(policy_labels.difference(chapters))`. Raises `BessZoningPrecheckError(f'Chapter policy completeness differs; missing={missing}, extra={extra}')`.
6. Defines `catalog_rows` with annotation `list[dict[str, object]]` from `[]`.
7. Defines `links_by_evidence` with annotation `dict[str, list[tuple[str, str]]]` from `{}`.
8. Iterates `link` over `evidence_route_links.to_dict('records')`. For each value: Computes `evidence_id` from `_strict_string(link['evidence_id'], 'linked evidence ID')`. Calls `links_by_evidence.setdefault(evidence_id, []).append((_strict_string(link['route_id'], 'linked route ID'), _strict_string(link['route_role'], 'route role')))` for its validation or side effect.
9. Computes `required_by_chapter` from `_required_section_ids_by_chapter(structure, policy)`.
10. Iterates `chapter` over `policy.chapters`. For each value: Computes `chapter_row` from `chapters[chapter.resolved_zone_chapter_label]`. Computes `chapter_id` from `chapter_row['section_id']`. Computes `reviewed_ids` from `set(chapter.reviewed_section_ids)`. Executes 5 additional source-ordered statement(s).
11. Computes `catalog` from `pd.DataFrame(catalog_rows, columns=EVIDENCE_CATALOG_COLUMNS)`.
12. Iterates `column` over `('page_number', 'excerpt_start', 'excerpt_end', 'source_rule_start', 'source_rule_end')`. For each value: Computes `catalog[column]` from `catalog[column].astype('int64')`.
13. Computes `catalog['decision_linked']` from `catalog['decision_linked'].astype('bool')`.
14. Checks `catalog['evidence_id'].duplicated().any()`. When true: Raises `BessZoningPrecheckError('Evidence catalog IDs must be unique')`.
15. Calls `_validate_evidence_occurrence_uniqueness(catalog)` for its validation or side effect.
16. Returns `(chapters, catalog)`.

**Validation and invariants**

- Rejects or diverts the path when `policy_labels != set(chapters)` is true.
- Rejects or diverts the path when `catalog['evidence_id'].duplicated().any()` is true.
- Rejects or diverts the path when `chapter.review_completeness == 'COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES' and missing_required` is true.
- Rejects or diverts the path when `reviewed is None` is true.
- Rejects or diverts the path when `reviewed['section_type'] not in {'ZONE_CHAPTER', 'ARTICLE'}` is true.
- Rejects or diverts the path when `reviewed['zone_chapter_label'] != chapter.resolved_zone_chapter_label` is true.
- Rejects or diverts the path when `reviewed['section_type'] == 'ARTICLE' and reviewed['parent_section_id'] != chapter_id` is true.
- Rejects or diverts the path when `section is None` is true.
- Rejects or diverts the path when `section_type == 'ARTICLE' and section['parent_section_id'] != chapter_id` is true.
- Rejects or diverts the path when `evidence.section_id not in reviewed_ids` is true.
- Rejects or diverts the path when `fragment is None` is true.
- Rejects or diverts the path when `not isinstance(raw_fragment, str)` is true.
- Rejects or diverts the path when `fragment['section_page_fragment_sha256'] != evidence.section_page_fragment_sha256` is true.
- Rejects or diverts the path when `evidence.excerpt_end > len(raw_fragment) or raw_fragment[evidence.excerpt_start:evidence.excerpt_end] != excerpt` is true.
- Rejects or diverts the path when `sha256(excerpt.encode('utf-8')).hexdigest() != evidence.excerpt_sha256` is true.
- Rejects or diverts the path when `evidence.source_rule_end > len(raw_fragment) or raw_fragment[evidence.source_rule_start:evidence.source_rule_end] != rule` is true.
- Rejects or diverts the path when `sha256(rule.encode('utf-8')).hexdigest() != evidence.source_rule_sha256` is true.
- Rejects or diverts the path when `rule[relative_start:relative_end] != excerpt` is true.
- Rejects or diverts the path when `section['zone_chapter_label'] != chapter.resolved_zone_chapter_label` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_required_section_ids_by_chapter`, `_strict_positive_integer`, `_strict_string`, `_validate_evidence_occurrence_uniqueness`, `_zone_chapter_rows`, `bool`, `catalog['decision_linked'].astype`, `catalog['evidence_id'].duplicated`, `catalog['evidence_id'].duplicated().any`, `catalog[column].astype`, `catalog_rows.append`, `evidence_route_links.to_dict`, `excerpt.encode`, `fragment_records.get`, `fragments.to_dict`, `isinstance`, `len`, `links_by_evidence.get`, `links_by_evidence.setdefault`, `links_by_evidence.setdefault(evidence_id, []).append`, `pd.DataFrame`, `policy_labels.difference`, `required_ids.difference`, `rule.encode`, `sections.get`, `set`, `set(chapters).difference`, `sha256`, `sha256(excerpt.encode('utf-8')).hexdigest`, `sha256(rule.encode('utf-8')).hexdigest`, `sorted`, `structure.sections.to_dict`, `tuple`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_validate_mapping`

**Signature**

```python
def _validate_mapping(
    structure: PlanningRegulationStructureResult,
    zones: pd.DataFrame,
) -> pd.DataFrame:
```

**Purpose**

Validates and rejects malformed mapping according to the exact implementation and guards in this file.

**Inputs**

- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `mapping`.

**Algorithm**

1. Computes `mapping` from `structure.zone_mapping.copy(deep=True)`.
2. Computes `source_labels` from `set(_exact_id_series(zones['zone_label_raw'], 'raw zone label', unique=False))`.
3. Computes `mapped_labels` from `set(_exact_id_series(mapping['source_zone_label_raw'], 'mapped source zone label', unique=True))`.
4. Checks `mapped_labels != source_labels`. When true: Raises `BessZoningPrecheckError('Factual zone mapping is incomplete or has extras')`.
5. Computes `chapters` from `{row['zone_chapter_label']: row['section_id'] for row in _zone_chapter_rows(structure)}`.
6. Iterates `row` over `mapping.to_dict('records')`. For each value: Calls `_strict_string(row['source_zone_label_raw'], 'mapped source zone label')` for its validation or side effect. Computes `status` from `_strict_string(row['mapping_status'], 'mapping status')`. Checks `status not in _RESOLVED_MAPPING_STATUSES`. When true: Raises `BessZoningPrecheckError(f"Source zone {row['source_zone_label_raw']!r} is not resolved")`. Executes 2 additional source-ordered statement(s).
7. Returns `mapping`.

**Validation and invariants**

- Rejects or diverts the path when `mapped_labels != source_labels` is true.
- Rejects or diverts the path when `status not in _RESOLVED_MAPPING_STATUSES` is true.
- Rejects or diverts the path when `chapters.get(resolved) != row['matched_section_id']` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `structure.zone_mapping.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessZoningPrecheckError`, `_exact_id_series`, `_strict_string`, `_zone_chapter_rows`, `chapters.get`, `mapping.to_dict`, `set`, `structure.zone_mapping.copy`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_lineage`

**Signature**

```python
def _lineage(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> dict[str, object]:
```

**Purpose**

Implements lineage according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_hash` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'planning_precheck_scope': PLANNING_PRECHECK_SCOPE, 'review_scope': REVIEW_SCOPE, 'policy_profile': policy.policy_profile, 'policy_sha256': policy_hash, 'document_id': index.document_id, 'archive_sha256': index.archive_sha256, 'pdf_sha256': index.pdf_sha256, 'index_content_sha256': index.index_content_sha256, 'structure_result_content_sha256': structure.structure_result_content_sha256, 'structur…`.

**Algorithm**

1. Returns `{'planning_precheck_scope': PLANNING_PRECHECK_SCOPE, 'review_scope': REVIEW_SCOPE, 'policy_profile': policy.policy_profile, 'policy_sha256': policy_hash, 'document_id': index.document_id, 'archive_sha256': index.archive_sha256, 'pdf_sha256': index.pdf_sha256, 'index_content_sha256': index.index_content_sha256, 'structure_result_content_sha256': structure.st…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_chapter_policy`
- `src/landscout/stages/interpret_bess_zoning.py` — `_build_evidence_route_links`
- `src/landscout/stages/interpret_bess_zoning.py` — `_build_parcel_zone_interpretations`
- `src/landscout/stages/interpret_bess_zoning.py` — `_build_route_assessments`
- `src/landscout/stages/interpret_bess_zoning.py` — `_build_source_zone_policy`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_build_chapter_policy`

**Signature**

```python
def _build_chapter_policy(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
```

**Purpose**

Builds chapter policy according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_hash` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Computes `by_label` from `{chapter.resolved_zone_chapter_label: chapter for chapter in policy.chapters}`.
2. Defines `rows` with annotation `list[dict[str, object]]` from `[]`.
3. Computes `lineage` from `_lineage(index, structure, policy, policy_hash)`.
4. Computes `chapters` from `_zone_chapter_rows(structure)`.
5. Computes `required_by_chapter` from `_required_section_ids_by_chapter(structure, policy)`.
6. Iterates `source` over `chapters`. For each value: Computes `label` from `_strict_string(source['zone_chapter_label'], 'zone chapter label')`. Computes `chapter_section_id` from `_strict_string(source['section_id'], 'zone chapter section ID')`. Computes `chapter` from `by_label[label]`. Executes 4 additional source-ordered statement(s).
7. Computes `frame` from `pd.DataFrame(rows, columns=CHAPTER_POLICY_COLUMNS)`.
8. Computes `frame['evidence_count']` from `frame['evidence_count'].astype('int64')`.
9. Returns `frame`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_lineage`, `_required_section_ids_by_chapter`, `_strict_string`, `_zone_chapter_rows`, `frame['evidence_count'].astype`, `len`, `pd.DataFrame`, `rows.append`, `set`, `tuple`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_route_status`

**Signature**

```python
def _route_status(route_kind: RouteKind) -> ChapterStatus:
```

**Purpose**

Implements route status according to the exact implementation and guards in this file.

**Inputs**

- `route_kind` (`RouteKind`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `ChapterStatus`. Observed return expression(s): `statuses[route_kind]`.

**Algorithm**

1. Defines `statuses` with annotation `dict[RouteKind, ChapterStatus]` from `{'DIRECT_ROUTE': 'POTENTIALLY_COMPATIBLE', 'CONDITIONAL_ROUTE': 'CONDITIONAL_REVIEW', 'RESTRICTION_EXCEPTION_ROUTE': 'CONDITIONAL_REVIEW', 'DIFFICULTY_ONLY': 'LIKELY_DIFFICULT'}`.
2. Returns `statuses[route_kind]`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- No function calls.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_route_assessments`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_build_route_assessments`

**Signature**

```python
def _build_route_assessments(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
```

**Purpose**

Builds route assessments according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_hash` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Computes `lineage` from `_lineage(index, structure, policy, policy_hash)`.
2. Computes `rows` from `[{'route_id': route.route_id, 'resolved_zone_chapter_label': chapter.resolved_zone_chapter_label, 'route_kind': route.route_kind, 'derived_route_status': _route_status(route.route_kind), 'positive_evidence_ids': tuple(route.positive_evidence_ids), 'condition_evidence_ids': tuple(route.condition_evidence_ids), 'difficu…`.
3. Computes `frame` from `pd.DataFrame(rows, columns=ROUTE_ASSESSMENT_COLUMNS)`.
4. Checks `frame['route_id'].duplicated().any()`. When true: Raises `BessZoningPrecheckError('Normalized route IDs must be unique')`.
5. Returns `frame`.

**Validation and invariants**

- Rejects or diverts the path when `frame['route_id'].duplicated().any()` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_lineage`, `_route_status`, `frame['route_id'].duplicated`, `frame['route_id'].duplicated().any`, `pd.DataFrame`, `tuple`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_build_evidence_route_links`

**Signature**

```python
def _build_evidence_route_links(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
```

**Purpose**

Builds evidence route links according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_hash` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Computes `lineage` from `_lineage(index, structure, policy, policy_hash)`.
2. Defines `rows` with annotation `list[dict[str, object]]` from `[]`.
3. Computes `role_fields` from `(('positive_evidence_ids', 'POSITIVE', 'SUPPORTS_POTENTIAL_COMPATIBILITY'), ('condition_evidence_ids', 'CONDITION', 'CONDITION'), ('difficulty_evidence_ids', 'DIFFICULTY', 'SUPPORTS_DIFFICULTY'))`.
4. Iterates `chapter` over `policy.chapters`. For each value: Iterates `route` over `chapter.route_assessments`. For each value: Iterates `(field, role, direction)` over `role_fields`. For each value: Iterates `evidence_id` over `getattr(route, field)`. For each value: Calls `rows.append({'route_id': route.route_id, 'resolved_zone_chapter_label': chapter.resolved_zone_chapter_label, 'route_kind': route.route_kind, 'evidence_id': evidence_id, 'route_role': role, 'evidence_direction': direction, 'review_completeness': chapter.review_completeness, 'review_scope': policy.review_scope, **lineage})` for its validation or side effect.
5. Computes `frame` from `pd.DataFrame(rows, columns=EVIDENCE_ROUTE_LINK_COLUMNS)`.
6. Checks `not frame.empty`. When true: Computes `frame` from `frame.sort_values(['route_id', 'evidence_id'], kind='mergesort').reset_index(drop=True)`.
7. Checks `frame.duplicated(['route_id', 'evidence_id']).any()`. When true: Raises `BessZoningPrecheckError('Evidence-route links must be unique by route and evidence')`.
8. Returns `frame`.

**Validation and invariants**

- Rejects or diverts the path when `frame.duplicated(['route_id', 'evidence_id']).any()` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_lineage`, `frame.duplicated`, `frame.duplicated(['route_id', 'evidence_id']).any`, `frame.sort_values`, `frame.sort_values(['route_id', 'evidence_id'], kind='mergesort').reset_index`, `getattr`, `pd.DataFrame`, `rows.append`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_build_source_zone_policy`

**Signature**

```python
def _build_source_zone_policy(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
    zones: pd.DataFrame,
    mapping: pd.DataFrame,
    chapter_policy: pd.DataFrame,
) -> pd.DataFrame:
```

**Purpose**

Builds source zone policy according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_hash` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `mapping` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `chapter_policy` (`pd.DataFrame`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `pd.DataFrame(rows, columns=SOURCE_ZONE_POLICY_COLUMNS)`.

**Algorithm**

1. Computes `policies` from `chapter_policy.set_index('resolved_zone_chapter_label').to_dict('index')`.
2. Computes `lineage` from `_lineage(index, structure, policy, policy_hash)`.
3. Defines `layers_by_label` with annotation `dict[str, str]` from `{}`.
4. Iterates `(label, group)` over `zones.groupby('zone_label_raw', sort=False)`. For each value: Computes `layers` from `tuple(dict.fromkeys(group['source_layer'].tolist()))`. Checks `len(layers) != 1`. When true: Raises `BessZoningPrecheckError(f'Source zone label {label!r} has ambiguous source-layer lineage')`. Computes `layers_by_label[str(label)]` from `_strict_string(layers[0], 'zone source layer')`.
5. Defines `rows` with annotation `list[dict[str, object]]` from `[]`.
6. Iterates `source` over `mapping.to_dict('records')`. For each value: Computes `chapter` from `policies[source['resolved_zone_chapter_label']]`. Calls `rows.append({'source_zone_label_raw': source['source_zone_label_raw'], 'resolved_zone_chapter_label': source['resolved_zone_chapter_label'], 'mapping_status': source['mapping_status'], 'matched_section_id': source['matched_section_id'], 'source_layer': layers_by_label[source['source_zone_label_raw']], 'zoning_precheck_status': chapter['zoning_precheck_statu…` for its validation or side effect.
7. Returns `pd.DataFrame(rows, columns=SOURCE_ZONE_POLICY_COLUMNS)`.

**Validation and invariants**

- Rejects or diverts the path when `len(layers) != 1` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_lineage`, `_strict_string`, `chapter_policy.set_index`, `chapter_policy.set_index('resolved_zone_chapter_label').to_dict`, `dict.fromkeys`, `group['source_layer'].tolist`, `len`, `mapping.to_dict`, `pd.DataFrame`, `rows.append`, `str`, `tuple`, `zones.groupby`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_build_parcel_zone_interpretations`

**Signature**

```python
def _build_parcel_zone_interpretations(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
    relations: pd.DataFrame,
    source_policy: pd.DataFrame,
) -> pd.DataFrame:
```

**Purpose**

Builds parcel zone interpretations according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_hash` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `source_policy` (`pd.DataFrame`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `pd.DataFrame`. Observed return expression(s): `frame`.

**Algorithm**

1. Computes `policies` from `source_policy.set_index('source_zone_label_raw').to_dict('index')`.
2. Computes `lineage` from `_lineage(index, structure, policy, policy_hash)`.
3. Defines `rows` with annotation `list[dict[str, object]]` from `[]`.
4. Computes `positive` from `relations.loc[relations['relation_type'].eq('AREA_OVERLAP')]`.
5. Iterates `source` over `positive.to_dict('records')`. For each value: Computes `item` from `policies[source['zone_label_raw']]`. Calls `rows.append({'parcel_id': source['parcel_id'], 'planning_zone_id': source['planning_zone_id'], 'source_zone_id': source['source_zone_id'], 'source_zone_label_raw': source['zone_label_raw'], 'resolved_zone_chapter_label': item['resolved_zone_chapter_label'], 'intersection_area_m2': float(source['intersection_area_m2']), 'parcel_share_pct': float(source['parc…` for its validation or side effect.
6. Computes `frame` from `pd.DataFrame(rows, columns=PARCEL_ZONE_POLICY_COLUMNS)`.
7. Checks `frame.empty`. When true: Computes `frame` from `pd.DataFrame({column: pd.Series(dtype='float64' if column in {'intersection_area_m2', 'parcel_share_pct'} else 'object') for column in PARCEL_ZONE_POLICY_COLUMNS})`.
8. Returns `frame`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_lineage`, `float`, `pd.DataFrame`, `pd.Series`, `positive.to_dict`, `relations['relation_type'].eq`, `rows.append`, `source_policy.set_index`, `source_policy.set_index('source_zone_label_raw').to_dict`, `tuple`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_is_null`

**Signature**

```python
def _is_null(value: object) -> bool:
```

**Purpose**

Returns whether `null` satisfies the exact predicates and branches listed below.

**Inputs**

- `value` (`object`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `bool`. Observed return expression(s): `isinstance(null, (bool, np.bool_)) and bool(null)`; `True`; `False`.

**Algorithm**

1. Checks `value is None or value is pd.NA`. When true: Returns `True`.
2. Runs guarded operation: Computes `null` from `pd.isna(value)`. Handles `(TypeError, ValueError)`.
3. Returns `isinstance(null, (bool, np.bool_)) and bool(null)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `bool`, `isinstance`, `pd.isna`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_parcel_output`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_build_parcel_output`

**Signature**

```python
def _build_parcel_output(
    parcels: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    interpretations: pd.DataFrame,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> gpd.GeoDataFrame:
```

**Purpose**

Builds parcel output according to the exact implementation and guards in this file.

**Inputs**

- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `relations` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `interpretations` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy_hash` (`str`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `gpd.GeoDataFrame`. Observed return expression(s): `output`.

**Algorithm**

1. Computes `output` from `parcels.copy(deep=True)`.
2. Computes `positive_by_parcel` from `{parcel_id: group.copy() for parcel_id, group in interpretations.groupby('parcel_id', sort=False)}`.
3. Computes `touch_counts` from `relations.loc[relations['relation_type'].eq('TOUCH_ONLY')].groupby('parcel_id', sort=False).size().to_dict()`.
4. Defines `summary` with annotation `dict[str, list[object]]` from `{column: [] for column in PARCEL_PRECHECK_COLUMNS}`.
5. Iterates `parcel` over `parcels.to_dict('records')`. For each value: Computes `parcel_id` from `parcel['parcel_id']`. Computes `group` from `positive_by_parcel.get(parcel_id)`. Computes `dominant_id` from `parcel['dominant_planning_zone_id']`. Executes 16 additional source-ordered statement(s).
6. Iterates `column` over `PARCEL_PRECHECK_COLUMNS`. For each value: Computes `values` from `np.empty(len(summary[column]), dtype=object)`. Computes `values[:]` from `summary[column]`. Computes `output[column]` from `values`.
7. Iterates `column` over `('positive_area_zone_count', 'distinct_zone_status_count', 'non_dominant_different_status_count', 'touch_only_zone_count')`. For each value: Computes `output[column]` from `output[column].astype('int64')`.
8. Iterates `column` over `('zoning_precheck_requires_formal_review', 'non_zoning_planning_features_interpreted')`. For each value: Computes `output[column]` from `output[column].astype('bool')`.
9. Returns `output`.

**Validation and invariants**

- Rejects or diverts the path when `group is None or group.empty` is true.
- Rejects or diverts the path when `not _is_null(dominant_id)` is true.
- Rejects or diverts the path when `dominant_id != expected_dominant` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `group.copy`, `parcels.copy`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `(group.loc[~group['planning_zone_id'].eq(expected_dominant), 'zoning_precheck_status'] != dominant_status).sum`, `BessZoningPrecheckError`, `_is_null`, `_strict_string`, `group.copy`, `group.sort_values`, `group['context_evidence_ids'].tolist`, `group['decision_evidence_ids'].tolist`, `group['planning_zone_id'].eq`, `group['zoning_precheck_status'].tolist`, `int`, `interpretations.groupby`, `len`, `np.empty`, `output[column].astype`, `parcels.copy`, `parcels.to_dict`, `positive_by_parcel.get`, `relations.loc[relations['relation_type'].eq('TOUCH_ONLY')].groupby`, `relations.loc[relations['relation_type'].eq('TOUCH_ONLY')].groupby('parcel_id', sort=False).size`, `relations.loc[relations['relation_type'].eq('TOUCH_ONLY')].groupby('parcel_id', sort=False).size().to_dict`, `relations['relation_type'].eq`, `set`, `sorted`, `summary['distinct_zone_status_count'].append`, `summary['dominant_zone_precheck_confidence'].append`, `summary['dominant_zone_precheck_status'].append`, `summary['non_dominant_different_status_count'].append`, `summary['non_zoning_planning_features_interpreted'].append`, `summary['planning_precheck_scope'].append`, `summary['positive_area_zone_count'].append`, `summary['review_scope'].append`, `summary['touch_only_zone_count'].append`, `summary['zoning_precheck_context_evidence_ids'].append`, `summary['zoning_precheck_evidence_ids'].append`, `summary['zoning_precheck_policy_profile'].append`, `summary['zoning_precheck_policy_sha256'].append`, `summary['zoning_precheck_requires_formal_review'].append`, `summary['zoning_precheck_status'].append`, `touch_counts.get`, `tuple`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_result_component_metadata`

**Signature**

```python
def _result_component_metadata(result: BessZoningPrecheckResult) -> dict[str, object]:
```

**Purpose**

Implements result component metadata according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessZoningPrecheckResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `dict[str, object]`. Observed return expression(s): `{'result_hash_schema_version': result.result_hash_schema_version, 'policy_schema_version': result.policy_schema_version, 'policy_profile': result.policy_profile, 'planning_precheck_scope': result.planning_precheck_scope, 'review_scope': result.review_scope, 'document_id': result.document_id, 'archive_sha256': result.archive_sha256, 'pdf_sha256': result.pdf_sha256, 'index_content_sha256': result.i…`.

**Algorithm**

1. Returns `{'result_hash_schema_version': result.result_hash_schema_version, 'policy_schema_version': result.policy_schema_version, 'policy_profile': result.policy_profile, 'planning_precheck_scope': result.planning_precheck_scope, 'review_scope': result.review_scope, 'document_id': result.document_id, 'archive_sha256': result.archive_sha256, 'pdf_sha256': result.pdf_…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `list`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_complete_result_sha256`
- `src/landscout/stages/interpret_bess_zoning.py` — `_result_frame_sha256`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_result_frame_sha256`

**Signature**

```python
def _result_frame_sha256(
    domain: str,
    result: BessZoningPrecheckResult,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
```

**Purpose**

Implements result frame sha256 according to the exact implementation and guards in this file.

**Inputs**

- `domain` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`BessZoningPrecheckResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `frame` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`Sequence[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': domain, **_result_component_metadata(result), 'frame': _frame_payload(frame, columns)})`.

**Algorithm**

1. Returns `_canonical_sha256({'domain': domain, **_result_component_metadata(result), 'frame': _frame_payload(frame, columns)})`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `_frame_payload`, `_result_component_metadata`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_result_with_hashes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_complete_result_sha256`

**Signature**

```python
def _complete_result_sha256(result: BessZoningPrecheckResult) -> str:
```

**Purpose**

Implements complete result sha256 according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessZoningPrecheckResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `str`. Observed return expression(s): `_canonical_sha256({'domain': 'landscout.bess_zoning.precheck_result', **_result_component_metadata(result), 'evidence_catalog_content_sha256': result.evidence_catalog_content_sha256, 'evidence_route_links_content_sha256': result.evidence_route_links_content_sha256, 'route_assessments_content_sha256': result.route_assessments_content_sha256, 'chapter_policy_content_sha256': result.chapter_policy_c…`.

**Algorithm**

1. Returns `_canonical_sha256({'domain': 'landscout.bess_zoning.precheck_result', **_result_component_metadata(result), 'evidence_catalog_content_sha256': result.evidence_catalog_content_sha256, 'evidence_route_links_content_sha256': result.evidence_route_links_content_sha256, 'route_assessments_content_sha256': result.route_assessments_content_sha256, 'chapter_policy_…`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `_canonical_sha256`, `_result_component_metadata`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_result_with_hashes`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_result_with_hashes`

**Signature**

```python
def _result_with_hashes(
    result: BessZoningPrecheckResult,
) -> BessZoningPrecheckResult:
```

**Purpose**

Implements result with hashes according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessZoningPrecheckResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessZoningPrecheckResult`. Observed return expression(s): `replace(component, complete_result_content_sha256=_complete_result_sha256(component))`.

**Algorithm**

1. Computes `component` from `replace(result, evidence_catalog_content_sha256=_result_frame_sha256('landscout.bess_zoning.evidence_catalog', result, result.evidence_catalog, EVIDENCE_CATALOG_COLUMNS), evidence_route_links_content_sha256=_result_frame_sha256('landscout.bess_zoning.evidence_route_links', result, result.evidence_route_links, EVIDENCE…`.
2. Returns `replace(component, complete_result_content_sha256=_complete_result_sha256(component))`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `replace`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `_complete_result_sha256`, `_result_frame_sha256`, `replace`, `tuple`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_build_result`
- `tests/unit/test_interpret_bess_zoning.py` — `test_coordinated_catalog_occurrence_duplicate_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_coordinated_evidence_catalog_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_coordinated_evidence_route_link_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_coordinated_result_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_coordinated_reverse_link_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_coordinated_route_table_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_repeated_excerpt_occurrence_is_bound_to_policy`

**Tests**

- `tests/unit/test_interpret_bess_zoning.py::test_coordinated_catalog_occurrence_duplicate_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_coordinated_evidence_catalog_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_coordinated_evidence_route_link_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_coordinated_result_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_coordinated_reverse_link_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_coordinated_route_table_mutation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_repeated_excerpt_occurrence_is_bound_to_policy`

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_build_result`

**Signature**

```python
def _build_result(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    structure_config: PlanningRegulationStructureConfig | str | Path,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    policy: BessZoningPolicyConfig,
) -> BessZoningPrecheckResult:
```

**Purpose**

Builds result according to the exact implementation and guards in this file.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure_config` (`PlanningRegulationStructureConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning_intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessZoningPrecheckResult`. Observed return expression(s): `_result_with_hashes(result)`.

**Algorithm**

1. Calls `validate_planning_regulation_index(index)` for its validation or side effect.
2. Computes `fragments` from `validate_planning_regulation_structure_with_fragments(index, zones, zoning_intersections, structure_config, structure)`.
3. Calls `_validate_policy_lock(index, structure, policy)` for its validation or side effect.
4. Computes `parcel_copy` from `_validate_parcels(index, parcels)`.
5. Computes `zone_copy` from `_validate_zones(index, zones)`.
6. Computes `relation_copy` from `_validate_relations(index, parcel_copy, zone_copy, zoning_intersections)`.
7. Computes `mapping` from `_validate_mapping(structure, zone_copy)`.
8. Computes `policy_hash` from `_policy_sha256(policy)`.
9. Computes `route_assessments` from `_build_route_assessments(index, structure, policy, policy_hash)`.
10. Computes `evidence_route_links` from `_build_evidence_route_links(index, structure, policy, policy_hash)`.
11. Computes `(_, evidence_catalog)` from `_validate_policy_evidence(index, structure, policy, fragments, policy_hash, evidence_route_links)`.
12. Computes `chapter_policy` from `_build_chapter_policy(index, structure, policy, policy_hash)`.
13. Computes `source_policy` from `_build_source_zone_policy(index, structure, policy, policy_hash, zone_copy, mapping, chapter_policy)`.
14. Computes `interpretations` from `_build_parcel_zone_interpretations(index, structure, policy, policy_hash, relation_copy, source_policy)`.
15. Computes `parcel_output` from `_build_parcel_output(parcel_copy, relation_copy, interpretations, policy, policy_hash)`.
16. Computes `relation_columns` from `tuple((str(column) for column in relation_copy.columns))`.
17. Computes `result` from `BessZoningPrecheckResult(result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION, policy_schema_version=policy.schema_version, policy_profile=policy.policy_profile, planning_precheck_scope=PLANNING_PRECHECK_SCOPE, review_scope=REVIEW_SCOPE, document_id=index.document_id, archive_sha256=index.archive_sha256, pdf_sha256=i…`.
18. Returns `_result_with_hashes(result)`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- No explicit raise expression; failures originate from called contracts or assertions where applicable.

**Side effects**

- Potentially relevant filesystem/network/calculation calls visible in the body: `relation_copy['relation_type'].eq`, `relation_copy['relation_type'].eq('TOUCH_ONLY').sum`. The exact effect occurs only on the guarded branch shown by the algorithm.

**Calls**

- `BessZoningPrecheckResult`, `_build_chapter_policy`, `_build_evidence_route_links`, `_build_parcel_output`, `_build_parcel_zone_interpretations`, `_build_route_assessments`, `_build_source_zone_policy`, `_factual_structure_sha256`, `_frame_sha256`, `_policy_sha256`, `_result_with_hashes`, `_validate_mapping`, `_validate_parcels`, `_validate_policy_evidence`, `_validate_policy_lock`, `_validate_relations`, `_validate_zones`, `_zone_mapping_input_sha256`, `int`, `relation_copy['relation_type'].eq`, `relation_copy['relation_type'].eq('TOUCH_ONLY').sum`, `str`, `tuple`, `validate_planning_regulation_index`, `validate_planning_regulation_structure_with_fragments`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `interpret_bess_zoning`
- `src/landscout/stages/interpret_bess_zoning.py` — `validate_bess_zoning_precheck`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_compare_frames`

**Signature**

```python
def _compare_frames(
    actual: pd.DataFrame,
    expected: pd.DataFrame,
    columns: Sequence[str],
    label: str,
) -> None:
```

**Purpose**

Compares frames according to the exact implementation and guards in this file.

**Inputs**

- `actual` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `columns` (`Sequence[str]`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `label` (`str`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `tuple(actual.columns) != tuple(expected.columns) or tuple(actual.columns) != tuple(columns)`. When true: Raises `BessZoningPrecheckError(f'{label} schema differs from rebuilt result')`.
2. Checks `_canonical_value(_frame_payload(actual, columns)) != _canonical_value(_frame_payload(expected, columns))`. When true: Raises `BessZoningPrecheckError(f'{label} differs from rebuilt source evidence')`.

**Validation and invariants**

- Rejects or diverts the path when `tuple(actual.columns) != tuple(expected.columns) or tuple(actual.columns) != tuple(columns)` is true.
- Rejects or diverts the path when `_canonical_value(_frame_payload(actual, columns)) != _canonical_value(_frame_payload(expected, columns))` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_canonical_value`, `_frame_payload`, `tuple`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `_compare_results`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `_compare_results`

**Signature**

```python
def _compare_results(
    result: BessZoningPrecheckResult,
    expected: BessZoningPrecheckResult,
    original_parcels: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Compares results according to the exact implementation and guards in this file.

**Inputs**

- `result` (`BessZoningPrecheckResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `expected` (`BessZoningPrecheckResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `original_parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Checks `not isinstance(result, BessZoningPrecheckResult)`. When true: Raises `BessZoningPrecheckError('result must be a BessZoningPrecheckResult')`.
2. Calls `_validate_evidence_occurrence_uniqueness(result.evidence_catalog)` for its validation or side effect.
3. Computes `scalar_fields` from `('result_hash_schema_version', 'policy_schema_version', 'policy_profile', 'planning_precheck_scope', 'review_scope', 'document_id', 'archive_sha256', 'pdf_sha256', 'index_content_sha256', 'structure_result_content_sha256', 'structure_profile', 'policy_config_sha256', 'factual_structure_content_sha256', 'zone_mapping_i…`.
4. Iterates `field` over `scalar_fields`. For each value: Checks `getattr(result, field) != getattr(expected, field)`. When true: Raises `BessZoningPrecheckError(f'BESS zoning result {field} differs from rebuilt source evidence')`.
5. Checks `_strict_positive_integer(result.result_hash_schema_version, 'precheck result hash schema version') != RESULT_HASH_SCHEMA_VERSION`. When true: Raises `BessZoningPrecheckError('Unsupported precheck result hash schema')`.
6. Checks `_strict_positive_integer(result.policy_schema_version, 'precheck policy schema version') != POLICY_SCHEMA_VERSION`. When true: Raises `BessZoningPrecheckError('Unsupported precheck policy schema')`.
7. Calls `_strict_nonnegative_integer(result.touch_only_relation_count, 'touch-only relation count')` for its validation or side effect.
8. Checks `type(result.zoning_relation_hash_columns) is not tuple or not all((isinstance(column, str) and column and (column == column.strip()) for column in result.zoning_relation_hash_columns))`. When true: Raises `BessZoningPrecheckError('Zoning relation hash columns must be an exact string tuple')`.
9. Iterates `field` over `('archive_sha256', 'pdf_sha256', 'index_content_sha256', 'structure_result_content_sha256', 'policy_config_sha256', 'factual_structure_content_sha256', 'zone_mapping_input_sha256', 'zoning_relations_input_sha256', 'evidence_catalog_content_sha256', 'evidence_route_links_content_sha256', 'route_assessments_content_sha2…`. For each value: Calls `_validated_sha256(getattr(result, field), field)` for its validation or side effect.
10. Calls `_compare_frames(result.evidence_catalog, expected.evidence_catalog, EVIDENCE_CATALOG_COLUMNS, 'evidence catalog')` for its validation or side effect.
11. Calls `_compare_frames(result.evidence_route_links, expected.evidence_route_links, EVIDENCE_ROUTE_LINK_COLUMNS, 'evidence-route links')` for its validation or side effect.
12. Calls `_compare_frames(result.route_assessments, expected.route_assessments, ROUTE_ASSESSMENT_COLUMNS, 'route assessments')` for its validation or side effect.
13. Calls `_compare_frames(result.chapter_policy, expected.chapter_policy, CHAPTER_POLICY_COLUMNS, 'chapter policy')` for its validation or side effect.
14. Calls `_compare_frames(result.source_zone_policy, expected.source_zone_policy, SOURCE_ZONE_POLICY_COLUMNS, 'source-zone policy')` for its validation or side effect.
15. Calls `_compare_frames(result.parcel_zone_interpretations, expected.parcel_zone_interpretations, PARCEL_ZONE_POLICY_COLUMNS, 'parcel/zone policy')` for its validation or side effect.
16. Calls `_compare_frames(result.parcels, expected.parcels, tuple(expected.parcels.columns), 'parcel precheck')` for its validation or side effect.
17. Computes `original_columns` from `tuple(original_parcels.columns)`.
18. Checks `tuple(result.parcels.columns[:len(original_columns)]) != original_columns`. When true: Raises `BessZoningPrecheckError('Existing parcel columns are not preserved')`.
19. Checks `_canonical_value(_frame_payload(result.parcels, original_columns)) != _canonical_value(_frame_payload(original_parcels, original_columns))`. When true: Raises `BessZoningPrecheckError('Parcel count, IDs, order, index, geometry, CRS, or prior fields changed')`.
20. Computes `statuses` from `set(result.chapter_policy['zoning_precheck_status'].tolist())`.
21. Computes `parcel_statuses` from `set(result.parcels['zoning_precheck_status'].tolist())`.
22. Computes `confidences` from `set(result.chapter_policy['zoning_precheck_confidence'].tolist())`.
23. Checks `not statuses.issubset(_CHAPTER_STATUSES)`. When true: Raises `BessZoningPrecheckError('Chapter policy status is invalid')`.
24. Checks `not parcel_statuses.issubset(_PARCEL_STATUSES)`. When true: Raises `BessZoningPrecheckError('Parcel precheck status is invalid')`.
25. Checks `not confidences.issubset(_CONFIDENCES)`. When true: Raises `BessZoningPrecheckError('Chapter policy confidence is invalid')`.
26. Computes `evidence_ids` from `set(_exact_id_series(result.evidence_catalog['evidence_id'], 'catalog evidence ID', unique=True))`.
27. Computes `catalog_by_id` from `result.evidence_catalog.set_index('evidence_id').to_dict('index')`.
28. Defines `expected_links` with annotation `set[tuple[str, str, str, str]]` from `set()`.
29. Computes `role_fields` from `(('positive_evidence_ids', 'POSITIVE', 'SUPPORTS_POTENTIAL_COMPATIBILITY'), ('condition_evidence_ids', 'CONDITION', 'CONDITION'), ('difficulty_evidence_ids', 'DIFFICULTY', 'SUPPORTS_DIFFICULTY'))`.
30. Iterates `route` over `result.route_assessments.to_dict('records')`. For each value: Iterates `(field, role, direction)` over `role_fields`. For each value: Computes `values` from `route[field]`. Checks `not isinstance(values, (tuple, list, np.ndarray))`. When true: Raises `BessZoningPrecheckError('Route evidence IDs must be arrays')`. Iterates `evidence_id` over `values`. For each value: Calls `expected_links.add((route['route_id'], evidence_id, role, direction))` for its validation or side effect.
31. Computes `actual_links` from `{(row['route_id'], row['evidence_id'], row['route_role'], row['evidence_direction']) for row in result.evidence_route_links.to_dict('records')}`.
32. Checks `len(actual_links) != len(result.evidence_route_links) or actual_links != expected_links`. When true: Raises `BessZoningPrecheckError('Evidence-route links do not exactly reproduce route evidence arrays')`.
33. Defines `reverse_links` with annotation `dict[str, list[tuple[str, str]]]` from `{}`.
34. Iterates `(route_id, evidence_id, role, _)` over `actual_links`. For each value: Checks `evidence_id not in catalog_by_id`. When true: Raises `BessZoningPrecheckError('Evidence-route link references unknown evidence')`. Calls `reverse_links.setdefault(evidence_id, []).append((route_id, role))` for its validation or side effect.
35. Defines `decision_ids` with annotation `set[str]` from `set()`.
36. Defines `context_ids` with annotation `set[str]` from `set()`.
37. Iterates `(evidence_id, row)` over `catalog_by_id.items()`. For each value: Computes `links` from `tuple(sorted(reverse_links.get(evidence_id, [])))`. Checks `tuple(row['linked_route_ids']) != tuple((item[0] for item in links))`. When true: Raises `BessZoningPrecheckError('Evidence reverse route IDs are inconsistent')`. Checks `tuple(row['linked_route_roles']) != tuple((item[1] for item in links))`. When true: Raises `BessZoningPrecheckError('Evidence reverse route roles are inconsistent')`. Executes 2 additional source-ordered statement(s).
38. Iterates `(frame, column)` over `((result.chapter_policy, 'evidence_ids'), (result.source_zone_policy, 'evidence_ids'), (result.parcel_zone_interpretations, 'evidence_ids'), (result.parcels, 'zoning_precheck_evidence_ids'))`. For each value: Iterates `values` over `frame[column].tolist()`. For each value: Checks `not isinstance(values, (tuple, list, np.ndarray))`. When true: Raises `BessZoningPrecheckError('Evidence references must be arrays')`. Checks `not set(values).issubset(evidence_ids)`. When true: Raises `BessZoningPrecheckError('An output evidence ID is absent from the evidence catalog')`.
39. Iterates `frame` over `(result.chapter_policy, result.source_zone_policy, result.parcel_zone_interpretations)`. For each value: Iterates `row` over `frame.to_dict('records')`. For each value: Computes `retained` from `set(row['evidence_ids'])`. Checks `set(row['decision_evidence_ids']) != retained.intersection(decision_ids)`. When true: Raises `BessZoningPrecheckError('Decision evidence output is inconsistent')`. Checks `set(row['context_evidence_ids']) != retained.intersection(context_ids)`. When true: Raises `BessZoningPrecheckError('Context evidence output is inconsistent')`.
40. Iterates `row` over `result.parcels.to_dict('records')`. For each value: Checks `not set(row['zoning_precheck_evidence_ids']).issubset(decision_ids)`. When true: Raises `BessZoningPrecheckError('Parcel decision evidence includes context')`. Checks `not set(row['zoning_precheck_context_evidence_ids']).issubset(context_ids)`. When true: Raises `BessZoningPrecheckError('Parcel context evidence includes a decision')`.
41. Checks `not result.parcels['zoning_precheck_requires_formal_review'].eq(True).all()`. When true: Raises `BessZoningPrecheckError('Every parcel must require formal review')`.
42. Checks `not result.parcels['non_zoning_planning_features_interpreted'].eq(False).all()`. When true: Raises `BessZoningPrecheckError('Non-zoning planning features must remain uninterpreted')`.
43. Checks `not result.parcels['review_scope'].eq(REVIEW_SCOPE).all()`. When true: Raises `BessZoningPrecheckError('Parcel review scope is invalid')`.

**Validation and invariants**

- Rejects or diverts the path when `not isinstance(result, BessZoningPrecheckResult)` is true.
- Rejects or diverts the path when `_strict_positive_integer(result.result_hash_schema_version, 'precheck result hash schema version') != RESULT_HASH_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `_strict_positive_integer(result.policy_schema_version, 'precheck policy schema version') != POLICY_SCHEMA_VERSION` is true.
- Rejects or diverts the path when `type(result.zoning_relation_hash_columns) is not tuple or not all((isinstance(column, str) and column and (column == column.strip()) for column in result.zoning_relation_hash_columns))` is true.
- Rejects or diverts the path when `tuple(result.parcels.columns[:len(original_columns)]) != original_columns` is true.
- Rejects or diverts the path when `_canonical_value(_frame_payload(result.parcels, original_columns)) != _canonical_value(_frame_payload(original_parcels, original_columns))` is true.
- Rejects or diverts the path when `not statuses.issubset(_CHAPTER_STATUSES)` is true.
- Rejects or diverts the path when `not parcel_statuses.issubset(_PARCEL_STATUSES)` is true.
- Rejects or diverts the path when `not confidences.issubset(_CONFIDENCES)` is true.
- Rejects or diverts the path when `len(actual_links) != len(result.evidence_route_links) or actual_links != expected_links` is true.
- Rejects or diverts the path when `not result.parcels['zoning_precheck_requires_formal_review'].eq(True).all()` is true.
- Rejects or diverts the path when `not result.parcels['non_zoning_planning_features_interpreted'].eq(False).all()` is true.
- Rejects or diverts the path when `not result.parcels['review_scope'].eq(REVIEW_SCOPE).all()` is true.
- Rejects or diverts the path when `getattr(result, field) != getattr(expected, field)` is true.
- Rejects or diverts the path when `evidence_id not in catalog_by_id` is true.
- Rejects or diverts the path when `tuple(row['linked_route_ids']) != tuple((item[0] for item in links))` is true.
- Rejects or diverts the path when `tuple(row['linked_route_roles']) != tuple((item[1] for item in links))` is true.
- Rejects or diverts the path when `bool(row['decision_linked']) != bool(links)` is true.
- Rejects or diverts the path when `row['evidence_direction'] == 'CONTEXT_ONLY'` is true.
- Rejects or diverts the path when `not set(row['zoning_precheck_evidence_ids']).issubset(decision_ids)` is true.
- Rejects or diverts the path when `not set(row['zoning_precheck_context_evidence_ids']).issubset(context_ids)` is true.
- Rejects or diverts the path when `not isinstance(values, (tuple, list, np.ndarray))` is true.
- Rejects or diverts the path when `links` is true.
- Rejects or diverts the path when `not links` is true.
- Rejects or diverts the path when `not set(values).issubset(evidence_ids)` is true.
- Rejects or diverts the path when `set(row['decision_evidence_ids']) != retained.intersection(decision_ids)` is true.
- Rejects or diverts the path when `set(row['context_evidence_ids']) != retained.intersection(context_ids)` is true.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_canonical_value`, `_compare_frames`, `_exact_id_series`, `_frame_payload`, `_strict_nonnegative_integer`, `_strict_positive_integer`, `_validate_evidence_occurrence_uniqueness`, `_validated_sha256`, `all`, `bool`, `catalog_by_id.items`, `column.strip`, `confidences.issubset`, `context_ids.add`, `decision_ids.add`, `expected_links.add`, `frame.to_dict`, `frame[column].tolist`, `getattr`, `isinstance`, `len`, `parcel_statuses.issubset`, `result.chapter_policy['zoning_precheck_confidence'].tolist`, `result.chapter_policy['zoning_precheck_status'].tolist`, `result.evidence_catalog.set_index`, `result.evidence_catalog.set_index('evidence_id').to_dict`, `result.evidence_route_links.to_dict`, `result.parcels.to_dict`, `result.parcels['non_zoning_planning_features_interpreted'].eq`, `result.parcels['non_zoning_planning_features_interpreted'].eq(False).all`, `result.parcels['review_scope'].eq`, `result.parcels['review_scope'].eq(REVIEW_SCOPE).all`, `result.parcels['zoning_precheck_requires_formal_review'].eq`, `result.parcels['zoning_precheck_requires_formal_review'].eq(True).all`, `result.parcels['zoning_precheck_status'].tolist`, `result.route_assessments.to_dict`, `retained.intersection`, `reverse_links.get`, `reverse_links.setdefault`, `reverse_links.setdefault(evidence_id, []).append`, `set`, `set(row['zoning_precheck_context_evidence_ids']).issubset`, `set(row['zoning_precheck_evidence_ids']).issubset`, `set(values).issubset`, `sorted`, `statuses.issubset`, `tuple`, `type`.

**Known repository callers**

- `src/landscout/stages/interpret_bess_zoning.py` — `interpret_bess_zoning`
- `src/landscout/stages/interpret_bess_zoning.py` — `validate_bess_zoning_precheck`

**Tests**

- No direct name-resolved test call found; module-level or higher-level tests may exercise it through a public entry point.

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `validate_bess_zoning_precheck`

**Signature**

```python
def validate_bess_zoning_precheck(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    structure_config: PlanningRegulationStructureConfig | str | Path,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
    policy: BessZoningPolicyConfig | str | Path,
    result: BessZoningPrecheckResult,
) -> None:
```

**Purpose**

Rebuild and validate the precheck from every factual and policy input.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure_config` (`PlanningRegulationStructureConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning_intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `result` (`BessZoningPrecheckResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `None`. No explicit `return` expression is present; normal completion returns `None`.

**Algorithm**

1. Runs guarded operation: Calls `validate_normalized_planning_zoning_inputs(planning_document, parcels, zones, zoning_intersections)` for its validation or side effect. Computes `resolved_policy` from `_resolved_policy(policy)`. Computes `expected` from `_build_result(index, structure, structure_config, zones, zoning_intersections, parcels, resolved_policy)`. Calls `_compare_results(result, expected, parcels)` for its validation or side effect. Handles `BessZoningPrecheckError`, `PlanningRegulationStructureError`, `PlanningZoningError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_build_result`, `_compare_results`, `_resolved_policy`, `validate_normalized_planning_zoning_inputs`.

**Known repository callers**

- `tests/unit/test_interpret_bess_zoning.py` — `_validate`
- `tests/unit/test_interpret_bess_zoning.py` — `test_evidence_change_after_result_creation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_factual_zone_mapping_counts_are_recomputed`
- `tests/unit/test_interpret_bess_zoning.py` — `test_policy_change_after_result_creation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_source_complete_validator_rejects_later_duplicate_chapter`
- `tests/unit/test_interpret_bess_zoning.py` — `test_zoning_relation_and_zone_mapping_changes_are_rejected`

**Tests**

- `tests/unit/test_interpret_bess_zoning.py::test_evidence_change_after_result_creation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_factual_zone_mapping_counts_are_recomputed`
- `tests/unit/test_interpret_bess_zoning.py::test_policy_change_after_result_creation_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_source_complete_validator_rejects_later_duplicate_chapter`
- `tests/unit/test_interpret_bess_zoning.py::test_zoning_relation_and_zone_mapping_changes_are_rejected`

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

### `interpret_bess_zoning`

**Signature**

```python
def interpret_bess_zoning(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    structure_config: PlanningRegulationStructureConfig | str | Path,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    parcels: gpd.GeoDataFrame,
    planning_document: GpuPlanningDocument,
    policy: BessZoningPolicyConfig | str | Path,
) -> BessZoningPrecheckResult:
```

**Purpose**

Build a conservative written-zoning precheck without rejecting parcels.

**Inputs**

- `index` (`PlanningRegulationIndex`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure` (`PlanningRegulationStructureResult`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `structure_config` (`PlanningRegulationStructureConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zones` (`pd.DataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `zoning_intersections` (`pd.DataFrame`; required) — input consumed according to its annotation and the implementation's explicit guards. Nullability and accepted values are exactly those enforced by the guards listed below.
- `parcels` (`gpd.GeoDataFrame`; required) — tabular or spatial input whose schema and values are validated by the function. Nullability and accepted values are exactly those enforced by the guards listed below.
- `planning_document` (`GpuPlanningDocument`; required) — upstream source-bound object and its lineage. Nullability and accepted values are exactly those enforced by the guards listed below.
- `policy` (`BessZoningPolicyConfig | str | Path`; required) — validated configuration or policy identity that controls the operation. Nullability and accepted values are exactly those enforced by the guards listed below.

**Returns**

- Declared return type: `BessZoningPrecheckResult`. Observed return expression(s): `result`.

**Algorithm**

1. Runs guarded operation: Calls `validate_normalized_planning_zoning_inputs(planning_document, parcels, zones, zoning_intersections)` for its validation or side effect. Computes `resolved_policy` from `_resolved_policy(policy)`. Computes `result` from `_build_result(index, structure, structure_config, zones, zoning_intersections, parcels, resolved_policy)`. Calls `_compare_results(result, result, parcels)` for its validation or side effect. Executes 1 additional source-ordered statement(s). Handles `BessZoningPrecheckError`, `PlanningRegulationStructureError`, `PlanningZoningError`, `Exception`.

**Validation and invariants**

- No direct `if`-guarded raise is present; invariants may be delegated to called validators listed below.

**Exceptions**

- Explicitly raises: `BessZoningPrecheckError`. Called functions may raise their documented controlled errors.

**Side effects**

- No direct network or filesystem mutation call is visible. In-memory mutation, if any, is determined by the exact assignments and called functions above.

**Calls**

- `BessZoningPrecheckError`, `_build_result`, `_compare_results`, `_resolved_policy`, `validate_normalized_planning_zoning_inputs`.

**Known repository callers**

- `tests/unit/test_interpret_bess_zoning.py` — `test_absent_excerpt_and_section_page_mismatch_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_context_evidence_is_separate_from_decision_outputs`
- `tests/unit/test_interpret_bess_zoning.py` — `test_evidence_must_be_inside_reviewed_sections`
- `tests/unit/test_interpret_bess_zoning.py` — `test_factual_zone_mapping_counts_are_recomputed`
- `tests/unit/test_interpret_bess_zoning.py` — `test_general_section_review_is_explicit_and_valid`
- `tests/unit/test_interpret_bess_zoning.py` — `test_incomplete_review_persists_exact_missing_required_sections`
- `tests/unit/test_interpret_bess_zoning.py` — `test_inputs_are_not_mutated`
- `tests/unit/test_interpret_bess_zoning.py` — `test_invalid_physical_zoning_fails_before_policy_interpretation`
- `tests/unit/test_interpret_bess_zoning.py` — `test_missing_and_extra_chapter_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_one_evidence_may_link_to_multiple_compatible_routes`
- `tests/unit/test_interpret_bess_zoning.py` — `test_one_precheck_build_performs_one_zoning_source_complete_validation`
- `tests/unit/test_interpret_bess_zoning.py` — `test_public_source_complete_validator_is_invoked`
- `tests/unit/test_interpret_bess_zoning.py` — `test_relation_area_denominators_are_required`
- `tests/unit/test_interpret_bess_zoning.py` — `test_relation_identity_change_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_relation_percentages_must_match_denominators`
- `tests/unit/test_interpret_bess_zoning.py` — `test_review_cannot_claim_another_chapter_section`
- `tests/unit/test_interpret_bess_zoning.py` — `test_reviewed_sections_cover_required_articles`
- `tests/unit/test_interpret_bess_zoning.py` — `test_same_general_occurrence_may_be_scoped_to_different_chapters`
- `tests/unit/test_interpret_bess_zoning.py` — `test_source_lock_mismatch_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_source_rule_identity_and_containment_are_strict`
- `tests/unit/test_interpret_bess_zoning.py` — `test_structure_config_and_hierarchy_changes_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_unknown_is_accepted_when_evidence_is_insufficient`
- `tests/unit/test_interpret_bess_zoning.py` — `test_unmapped_dominant_zone_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `test_wrong_occurrence_identity_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py` — `valid_result`

**Tests**

- `tests/unit/test_interpret_bess_zoning.py::test_absent_excerpt_and_section_page_mismatch_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_context_evidence_is_separate_from_decision_outputs`
- `tests/unit/test_interpret_bess_zoning.py::test_evidence_must_be_inside_reviewed_sections`
- `tests/unit/test_interpret_bess_zoning.py::test_factual_zone_mapping_counts_are_recomputed`
- `tests/unit/test_interpret_bess_zoning.py::test_general_section_review_is_explicit_and_valid`
- `tests/unit/test_interpret_bess_zoning.py::test_incomplete_review_persists_exact_missing_required_sections`
- `tests/unit/test_interpret_bess_zoning.py::test_inputs_are_not_mutated`
- `tests/unit/test_interpret_bess_zoning.py::test_invalid_physical_zoning_fails_before_policy_interpretation`
- `tests/unit/test_interpret_bess_zoning.py::test_missing_and_extra_chapter_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_one_evidence_may_link_to_multiple_compatible_routes`
- `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation`
- `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked`
- `tests/unit/test_interpret_bess_zoning.py::test_relation_area_denominators_are_required`
- `tests/unit/test_interpret_bess_zoning.py::test_relation_identity_change_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_relation_percentages_must_match_denominators`
- `tests/unit/test_interpret_bess_zoning.py::test_review_cannot_claim_another_chapter_section`
- `tests/unit/test_interpret_bess_zoning.py::test_reviewed_sections_cover_required_articles`
- `tests/unit/test_interpret_bess_zoning.py::test_same_general_occurrence_may_be_scoped_to_different_chapters`
- `tests/unit/test_interpret_bess_zoning.py::test_source_lock_mismatch_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_source_rule_identity_and_containment_are_strict`
- `tests/unit/test_interpret_bess_zoning.py::test_structure_config_and_hierarchy_changes_are_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_unknown_is_accepted_when_evidence_is_insufficient`
- `tests/unit/test_interpret_bess_zoning.py::test_unmapped_dominant_zone_is_rejected`
- `tests/unit/test_interpret_bess_zoning.py::test_wrong_occurrence_identity_is_rejected`

**Business interpretation**

This symbol contributes to the `project` layer only through the exact factual, proxy, diagnostic, policy, or validation role described above.

**Does NOT prove**

- This project file does not implement a business algorithm.

## 7. Data contracts

The following exact strings are used as frame columns, constructor/schema keys, or keyed domain labels. Rows explicitly marked as mapping/domain keys are not claimed to be DataFrame columns. Central ordered column and dtype constants in the Constants section remain authoritative.

| Column or keyed label | Contract observed here | Semantic boundary |
|---|---|---|
| `ACCESS_OR_NETWORK_CONDITION` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `CONDITION` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `CONDITIONAL_REVIEW` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `CONDITIONAL_ROUTE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `CONFIGURED_USE_CONTROL_ARTICLES_ONLY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `CONTEXT_ONLY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `DIFFICULTY_ONLY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `DIRECT_ROUTE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `HIGH` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `ICPE_RULE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `INCOMPLETE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LIKELY_DIFFICULT` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `LOW` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `MEDIUM` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `OTHER_RELEVANT_RULE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `POTENTIALLY_COMPATIBLE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `PUBLIC_INTEREST_EXCEPTION` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `RESTRICTION_EXCEPTION_ROUTE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `RISK_OR_NUISANCE_CONDITION` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `SUPPORTS_DIFFICULTY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `SUPPORTS_POTENTIAL_COMPATIBILITY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `TECHNICAL_EQUIPMENT_RULE` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `UNKNOWN` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `USE_PERMISSION` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `USE_RESTRICTION` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `WRITTEN_ZONING_REGULATION_ONLY` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `applicability_note` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `article_number_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `ascending` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `chapter_section_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `condition_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `context_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `crs` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `decision_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `decision_linked` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `derived_route_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `difficulty_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `distinct_zone_status_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_planning_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_precheck_confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `dominant_zone_precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `evidence_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `evidence_direction` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `evidence_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `evidence_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `exact_raw_excerpt` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `excerpt_end` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `excerpt_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `excerpt_start` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `geometry_column` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `index_content_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `interpretation_note` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `intersection_area_m2` | Logical dtype: float64 or strict numeric scalar as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | area in square metres computed on an EPSG:2154 calculation copy or copied from validated factual relations. Consumers and exact calculations are the functions that reference this column above. |
| `kind` | Logical dtype: mapping/domain key (not asserted as a DataFrame column). Nullability: not applicable as a column. | exact lookup/domain label used by an implementation mapping; it is intentionally not presented as a contractual frame column. Consumers and exact calculations are the functions that reference this column above. |
| `linked_route_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `linked_route_roles` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `mapping_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |
| `matched_section_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `missing_information` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `missing_required_section_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `non_dominant_different_status_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `non_zoning_planning_features_interpreted` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `page_number` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `parcel_share_pct` | Logical dtype: float64. Nullability: determined by the owning schema/dtype map and explicit null guards. | percentage derived from the exact numerator/denominator named by its stage. Consumers and exact calculations are the functions that reference this column above. |
| `parent_section_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `pdf_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `planning_precheck_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `planning_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `policy_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `policy_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `positive_area_zone_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `positive_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `rationale` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `raw_text` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `relation_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `resolved_zone_chapter_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `review_completeness` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `review_note` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `review_scope` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `reviewed_section_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `route_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `route_kind` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `route_role` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `section_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `section_page_fragment_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `section_type` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed source, geometry, feature, relation, or lineage domain enforced by validators. Consumers and exact calculations are the functions that reference this column above. |
| `source_archive_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_document_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_layer` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_rule_end` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_rule_excerpt` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_rule_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_rule_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `source_rule_start` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `source_zone_id` | Logical dtype: nullable-string/string dtype as declared. Nullability: normally non-null for portable identity; exact validator is authoritative. | portable identity used for deterministic joins and source/relation agreement. Consumers and exact calculations are the functions that reference this column above. |
| `source_zone_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `structure_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `structure_result_content_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `touch_only_zone_count` | Logical dtype: Int64 or strict integer as declared. Nullability: determined by the owning schema/dtype map and explicit null guards. | count of the entities named by the field. Consumers and exact calculations are the functions that reference this column above. |
| `zone_chapter_label` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zone_label_raw` | Logical dtype: source-preserving dtype. Nullability: source nulls preserved. | uninterpreted factual source value; normalization does not map it to suitability. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_precheck_confidence` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_precheck_context_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_precheck_evidence_ids` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_precheck_policy_profile` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_precheck_policy_sha256` | Logical dtype: nullable string or exact string as declared by the schema. Nullability: normally non-null for required lineage; exact validator is authoritative. | lowercase SHA256 binding the component named by the prefix. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_precheck_requires_formal_review` | Logical dtype: schema-defined Pandas dtype. Nullability: determined by the owning schema/dtype map and explicit null guards. | exact named field; factual/proxy/policy/diagnostic role follows the introducing function; introduced or consumed by the functions and ordered schemas in this module. Consumers and exact calculations are the functions that reference this column above. |
| `zoning_precheck_status` | Logical dtype: nullable string/string categorical value. Nullability: determined by the owning schema/dtype map and explicit null guards. | closed factual, technical, official, policy, or diagnostic vocabulary enforced by module constants. Consumers and exact calculations are the functions that reference this column above. |

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

This file contributes to LandScout's `project` evidence flow as described by its purpose and public symbols. It preserves the distinction among fact, proxy evidence, policy interpretation, diagnostic status, and parcel precheck.

## 15. Explicit non-goals

- This project file does not implement a business algorithm.

## 16. Tests

Direct name-resolved tests appear under each symbol. Higher-level tests may exercise private helpers through a public source-complete function; companion documents for all test files describe their fixtures, actions, assertions, and boundaries.

## 17. Change impact

Changing this file requires reviewing its static callers, package exports, directly mapped tests, relevant schema/hash/version constants, source locks, persisted artifact contracts, and the corresponding pipeline/cross-cutting documents. Any byte change makes the SHA256 above stale and requires regenerating this companion.
