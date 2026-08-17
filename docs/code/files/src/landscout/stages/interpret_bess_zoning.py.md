# `src/landscout/stages/interpret_bess_zoning.py`

## File identity

- Repository path: `src/landscout/stages/interpret_bess_zoning.py`
- File type: Python source
- Layer: policy application/precheck stage
- Domain: planning
- Responsibility: Applies the source-locked Muret written-zoning evidence policy to structured regulation and parcel-zone facts to produce deterministic planning precheck evidence.
- Source SHA256: `f230e39abedb5c61a7f51b227800c3a185df9689611f3526aa49cf362ffc99c9`

## 1. Purpose

Applies the source-locked Muret written-zoning evidence policy to structured regulation and parcel-zone facts to produce deterministic planning precheck evidence.

## 2. Position in LandScout architecture

This file belongs to the **policy application/precheck stage** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import math`
- `import re`
- `from collections.abc import Mapping, Sequence`
- `from dataclasses import dataclass, replace`
- `from datetime import date, datetime`
- `from hashlib import sha256`
- `from numbers import Integral, Real`
- `from pathlib import Path`
- `from typing import Literal`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `import yaml`
- `from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, model_validator`
- `from pyproj import CRS`
- `from shapely import to_wkb`
- `from shapely.geometry.base import BaseGeometry`

### Internal LandScout imports

- `from landscout.sources.gpu_fr import GpuPlanningDocument`
- `from landscout.stages.enrich_planning_zoning import (
    PlanningZoningError,
    validate_normalized_planning_zoning_inputs,
)`
- `from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)`
- `from landscout.stages.planning_overlay import technical_overlay_tolerance`
- `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    validate_planning_regulation_structure_with_fragments,
)`

## 4. Contract taxonomy

### A. Python constants

#### `POLICY_SCHEMA_VERSION`

```python
POLICY_SCHEMA_VERSION = 5
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/stages/interpret_bess_zoning.py::BessZoningPolicyConfig._validate_policy` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_compare_results` (value reference).

#### `RESULT_HASH_SCHEMA_VERSION`

```python
RESULT_HASH_SCHEMA_VERSION = 5
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/stages/interpret_bess_zoning.py::_build_result` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_compare_results` (value reference).

#### `PLANNING_PRECHECK_SCOPE`

```python
PLANNING_PRECHECK_SCOPE = "WRITTEN_ZONING_REGULATION_ONLY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/interpret_bess_zoning.py::_lineage` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_build_parcel_output` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_build_result` (value reference).

#### `REVIEW_SCOPE`

```python
REVIEW_SCOPE = "CONFIGURED_USE_CONTROL_ARTICLES_ONLY"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/interpret_bess_zoning.py::_lineage` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_build_parcel_output` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_build_result` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_compare_results` (value reference).

#### `_CHAPTER_STATUSES`

```python
_CHAPTER_STATUSES = frozenset(
    {"POTENTIALLY_COMPATIBLE", "CONDITIONAL_REVIEW", "LIKELY_DIFFICULT", "UNKNOWN"}
)
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/interpret_bess_zoning.py::<module>` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_compare_results` (value reference).

#### `_PARCEL_STATUSES`

```python
_PARCEL_STATUSES = _CHAPTER_STATUSES | {"MIXED_REVIEW_REQUIRED"}
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema. Consumers include `src/landscout/stages/interpret_bess_zoning.py::_compare_results` (value reference).

#### `_CONFIDENCES`

```python
_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/interpret_bess_zoning.py::_compare_results` (value reference).

#### `_RESOLVED_MAPPING_STATUSES`

```python
_RESOLVED_MAPPING_STATUSES = frozenset({"EXACT", "CONFIG_ALIAS"})
```

Explicit mapping between source/input and target/output fields; keys and values are documented separately. Consumers include `src/landscout/stages/interpret_bess_zoning.py::_validate_mapping` (value reference).

#### `CHAPTER_POLICY_COLUMNS`

```python
CHAPTER_POLICY_COLUMNS = (
    "resolved_zone_chapter_label",
    "chapter_section_id",
    "review_completeness",
    "review_scope",
    "reviewed_section_ids",
    "missing_required_section_ids",
    "review_note",
    "zoning_precheck_status",
    "zoning_precheck_confidence",
    "evidence_count",
    "evidence_ids",
    "decision_evidence_ids",
    "context_evidence_ids",
    "rationale",
    "missing_information",
    "planning_precheck_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_interpret_bess_zoning.py::<module>` (import), `src/landscout/stages/interpret_bess_zoning.py::_build_chapter_policy` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_result_with_hashes` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_compare_results` (value reference), `tests/unit/test_interpret_bess_zoning.py::test_valid_locked_policy_builds_complete_outputs` (value reference).

#### `EVIDENCE_CATALOG_COLUMNS`

```python
EVIDENCE_CATALOG_COLUMNS = (
    "evidence_id",
    "resolved_zone_chapter_label",
    "section_id",
    "page_number",
    "evidence_kind",
    "evidence_direction",
    "linked_route_ids",
    "linked_route_roles",
    "decision_linked",
    "exact_raw_excerpt",
    "excerpt_sha256",
    "section_page_fragment_sha256",
    "excerpt_start",
    "excerpt_end",
    "source_rule_id",
    "source_rule_excerpt",
    "source_rule_sha256",
    "source_rule_start",
    "source_rule_end",
    "interpretation_note",
    "review_completeness",
    "review_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_interpret_bess_zoning.py::<module>` (import), `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_evidence` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_result_with_hashes` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_compare_results` (value reference), `tests/unit/test_interpret_bess_zoning.py::test_valid_locked_policy_builds_complete_outputs` (value reference).

#### `_EVIDENCE_OCCURRENCE_COLUMNS`

```python
_EVIDENCE_OCCURRENCE_COLUMNS = (
    "resolved_zone_chapter_label",
    "section_id",
    "page_number",
    "section_page_fragment_sha256",
    "excerpt_start",
    "excerpt_end",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/interpret_bess_zoning.py::_validate_evidence_occurrence_uniqueness` (value reference).

#### `ROUTE_ASSESSMENT_COLUMNS`

```python
ROUTE_ASSESSMENT_COLUMNS = (
    "route_id",
    "resolved_zone_chapter_label",
    "route_kind",
    "derived_route_status",
    "positive_evidence_ids",
    "condition_evidence_ids",
    "difficulty_evidence_ids",
    "applicability_note",
    "review_completeness",
    "review_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_interpret_bess_zoning.py::<module>` (import), `src/landscout/stages/interpret_bess_zoning.py::_build_route_assessments` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_result_with_hashes` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_compare_results` (value reference), `tests/unit/test_interpret_bess_zoning.py::test_valid_locked_policy_builds_complete_outputs` (value reference).

#### `EVIDENCE_ROUTE_LINK_COLUMNS`

```python
EVIDENCE_ROUTE_LINK_COLUMNS = (
    "route_id",
    "resolved_zone_chapter_label",
    "route_kind",
    "evidence_id",
    "route_role",
    "evidence_direction",
    "review_completeness",
    "review_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_interpret_bess_zoning.py::<module>` (import), `src/landscout/stages/interpret_bess_zoning.py::_build_evidence_route_links` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_result_with_hashes` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_compare_results` (value reference), `tests/unit/test_interpret_bess_zoning.py::test_valid_locked_policy_builds_complete_outputs` (value reference).

#### `SOURCE_ZONE_POLICY_COLUMNS`

```python
SOURCE_ZONE_POLICY_COLUMNS = (
    "source_zone_label_raw",
    "resolved_zone_chapter_label",
    "mapping_status",
    "matched_section_id",
    "source_layer",
    "zoning_precheck_status",
    "zoning_precheck_confidence",
    "evidence_ids",
    "decision_evidence_ids",
    "context_evidence_ids",
    "review_scope",
    "planning_precheck_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_interpret_bess_zoning.py::<module>` (import), `src/landscout/stages/interpret_bess_zoning.py::_build_source_zone_policy` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_result_with_hashes` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_compare_results` (value reference), `tests/unit/test_interpret_bess_zoning.py::test_valid_locked_policy_builds_complete_outputs` (value reference).

#### `PARCEL_ZONE_POLICY_COLUMNS`

```python
PARCEL_ZONE_POLICY_COLUMNS = (
    "parcel_id",
    "planning_zone_id",
    "source_zone_id",
    "source_zone_label_raw",
    "resolved_zone_chapter_label",
    "intersection_area_m2",
    "parcel_share_pct",
    "zoning_precheck_status",
    "zoning_precheck_confidence",
    "evidence_ids",
    "decision_evidence_ids",
    "context_evidence_ids",
    "review_scope",
    "planning_precheck_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
    "source_layer",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_interpret_bess_zoning.py::<module>` (import), `src/landscout/stages/interpret_bess_zoning.py::_build_parcel_zone_interpretations` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_result_with_hashes` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_compare_results` (value reference), `tests/unit/test_interpret_bess_zoning.py::test_valid_locked_policy_builds_complete_outputs` (value reference).

#### `PARCEL_PRECHECK_COLUMNS`

```python
PARCEL_PRECHECK_COLUMNS = (
    "zoning_precheck_status",
    "dominant_zone_precheck_status",
    "dominant_zone_precheck_confidence",
    "positive_area_zone_count",
    "distinct_zone_status_count",
    "non_dominant_different_status_count",
    "touch_only_zone_count",
    "zoning_precheck_evidence_ids",
    "zoning_precheck_context_evidence_ids",
    "zoning_precheck_requires_formal_review",
    "planning_precheck_scope",
    "review_scope",
    "non_zoning_planning_features_interpreted",
    "zoning_precheck_policy_profile",
    "zoning_precheck_policy_sha256",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `src/landscout/stages/interpret_bess_zoning.py::_validate_parcels` (value reference), `src/landscout/stages/interpret_bess_zoning.py::_build_parcel_output` (value reference).


### B. Type aliases and closed domains

#### `ChapterStatus`

```python
ChapterStatus = Literal[
    "POTENTIALLY_COMPATIBLE",
    "CONDITIONAL_REVIEW",
    "LIKELY_DIFFICULT",
    "UNKNOWN",
]
```

Written-zoning precheck result domain: POTENTIALLY_COMPATIBLE, CONDITIONAL_REVIEW, LIKELY_DIFFICULT, or UNKNOWN. Enforced/consumed by `src/landscout/stages/interpret_bess_zoning.py::_derived_chapter_status` (type annotation), `src/landscout/stages/interpret_bess_zoning.py::ChapterPolicy` (type annotation), `src/landscout/stages/interpret_bess_zoning.py::_route_status` (type annotation).

#### `Confidence`

```python
Confidence = Literal["HIGH", "MEDIUM", "LOW"]
```

Written-zoning evidence confidence domain: HIGH, MEDIUM, or LOW. Enforced/consumed by `src/landscout/stages/interpret_bess_zoning.py::ChapterPolicy` (type annotation).

#### `ReviewCompleteness`

```python
ReviewCompleteness = Literal[
    "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES", "INCOMPLETE"
]
```

Whether configured use-control articles are complete or the review remains incomplete. Enforced/consumed by `src/landscout/stages/interpret_bess_zoning.py::_derived_chapter_status` (type annotation), `src/landscout/stages/interpret_bess_zoning.py::ChapterPolicy` (type annotation).

#### `RouteKind`

```python
RouteKind = Literal[
    "DIRECT_ROUTE",
    "CONDITIONAL_ROUTE",
    "RESTRICTION_EXCEPTION_ROUTE",
    "DIFFICULTY_ONLY",
]
```

Configured written-zoning evidence-route kind consumed by _route_status. Enforced/consumed by `src/landscout/stages/interpret_bess_zoning.py::RouteAssessment` (type annotation), `src/landscout/stages/interpret_bess_zoning.py::_route_status` (type annotation).

#### `EvidenceKind`

```python
EvidenceKind = Literal[
    "USE_PERMISSION",
    "USE_RESTRICTION",
    "PUBLIC_INTEREST_EXCEPTION",
    "TECHNICAL_EQUIPMENT_RULE",
    "ICPE_RULE",
    "RISK_OR_NUISANCE_CONDITION",
    "ACCESS_OR_NETWORK_CONDITION",
    "OTHER_RELEVANT_RULE",
]
```

Taxonomy of exact written-regulation evidence occurrences. Enforced/consumed by `src/landscout/stages/interpret_bess_zoning.py::PolicyEvidence` (type annotation).

#### `EvidenceDirection`

```python
EvidenceDirection = Literal[
    "SUPPORTS_POTENTIAL_COMPATIBILITY",
    "SUPPORTS_DIFFICULTY",
    "CONDITION",
    "CONTEXT_ONLY",
]
```

Decision relationship of evidence: supports compatibility/difficulty, condition, or contextual only. Enforced/consumed by `src/landscout/stages/interpret_bess_zoning.py::PolicyEvidence` (type annotation).


### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "BessZoningPolicyConfig",
    "BessZoningPrecheckError",
    "BessZoningPrecheckResult",
    "interpret_bess_zoning",
    "load_bess_zoning_policy_config",
    "validate_bess_zoning_precheck",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `BessZoningPrecheckError`

**Purpose:** Raised when the preliminary zoning interpretation cannot be proven.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`.
- import: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.interpret_bess_zoning import (
    CHAPTER_POLICY_COLUMNS,
    EVIDENCE_CATALOG_COLUMNS,
    EVIDENCE_ROUTE_LINK_COLUMNS,
    PARCEL_ZONE_POLICY_COLUMNS,
    ROUTE_ASSESSMENT_COLUMNS,
    SOURCE_ZONE_POLICY_COLUMNS,
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    _result_with_hashes,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_construct_unique_mapping` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::load_bess_zoning_policy_config` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_strict_string` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_strict_nonnegative_integer` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_strict_positive_integer` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_validated_sha256` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_strict_nonnegative_number` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_canonical_value` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_canonical_sha256` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_frame_payload` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_resolved_policy` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_lock` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_exact_id_series` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_validate_parcels` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_validate_zones` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_validate_relations` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_zone_chapter_rows` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_validate_evidence_occurrence_uniqueness` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_evidence` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_validate_mapping` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_build_route_assessments` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_build_evidence_route_links` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_build_source_zone_policy` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_build_parcel_output` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_compare_frames` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::validate_bess_zoning_precheck` via `BessZoningPrecheckError`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::interpret_bess_zoning` via `BessZoningPrecheckError`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_source_lock_mismatch_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='differs from factual source')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_missing_and_extra_chapter_are_rejected` via `pytest.raises(BessZoningPrecheckError, match='completeness differs')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_missing_and_extra_chapter_are_rejected` via `pytest.raises(BessZoningPrecheckError, match='extra=.*EXTRA')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_regulation_zone_chapter_labels_and_ids_must_be_unique` via `pytest.raises(BessZoningPrecheckError, match='labels must be unique')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_regulation_zone_chapter_labels_and_ids_must_be_unique` via `pytest.raises(BessZoningPrecheckError, match='section IDs must be unique')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_source_complete_validator_rejects_later_duplicate_chapter` via `pytest.raises(BessZoningPrecheckError)`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_duplicate_yaml_key_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='Duplicate YAML policy key')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_source_rule_identity_and_containment_are_strict` via `pytest.raises(BessZoningPrecheckError, match='source-rule offsets')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_absent_excerpt_and_section_page_mismatch_are_rejected` via `pytest.raises(BessZoningPrecheckError, match='offsets')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_absent_excerpt_and_section_page_mismatch_are_rejected` via `pytest.raises(BessZoningPrecheckError, match='section/page fragment')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_reviewed_sections_cover_required_articles` via `pytest.raises(BessZoningPrecheckError, match='omits required reviewed')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_evidence_must_be_inside_reviewed_sections` via `pytest.raises(BessZoningPrecheckError, match='outside reviewed sections')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_review_cannot_claim_another_chapter_section` via `pytest.raises(BessZoningPrecheckError, match='another chapter')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_repeated_excerpt_occurrence_is_bound_to_policy` via `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_wrong_occurrence_identity_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='fragment|offset')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_unmapped_dominant_zone_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='Factual regulation structure')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_policy_change_after_result_creation_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='policy_config_sha256')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_evidence_change_after_result_creation_is_rejected` via `pytest.raises(BessZoningPrecheckError)`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_zoning_relation_and_zone_mapping_changes_are_rejected` via `pytest.raises(BessZoningPrecheckError, match='Factual regulation structure')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_structure_config_and_hierarchy_changes_are_rejected` via `pytest.raises(BessZoningPrecheckError, match='Factual regulation structure')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_invalid_physical_zoning_fails_before_policy_interpretation` via `pytest.raises(BessZoningPrecheckError, match='physical source invalid')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_relation_area_denominators_are_required` via `pytest.raises(BessZoningPrecheckError)`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_relation_percentages_must_match_denominators` via `pytest.raises(BessZoningPrecheckError)`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_factual_zone_mapping_counts_are_recomputed` via `pytest.raises(BessZoningPrecheckError, match='Factual regulation structure')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_factual_zone_mapping_counts_are_recomputed` via `pytest.raises(BessZoningPrecheckError)`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_result_mutation_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_evidence_catalog_mutation_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_catalog_occurrence_duplicate_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='duplicate chapter-scoped evidence occurrence')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_route_table_mutation_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_evidence_route_link_mutation_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_reverse_link_mutation_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_evidence_route_link_hash_mutation_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='differs from rebuilt')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_old_result_hash_schemas_are_rejected` via `pytest.raises(BessZoningPrecheckError, match='result_hash_schema_version')`.
- expected exception type: `tests/unit/test_interpret_bess_zoning.py::test_relation_identity_change_is_rejected` via `pytest.raises(BessZoningPrecheckError, match='Factual regulation structure')`.

**Exact class source**

```python
class BessZoningPrecheckError(ValueError):
    """Raised when the preliminary zoning interpretation cannot be proven."""
```

### `_StrictConfigModel`

**Purpose:** Validates the planning contract carried by its explicit validators and inherited fields.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class _StrictConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `PolicySourceLock`

**Purpose:** Exact upstream document/archive/CNIG or planning-result identity that the owning policy must match before compilation/application.

**Kind:** Pydantic model.

**Inheritance:** `_StrictConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `document_id` | `document_id: StrictStr = Field(min_length=1)` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `archive_sha256` | `archive_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `pdf_sha256` | `pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `index_content_sha256` | `index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `structure_result_content_sha256` | `structure_result_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `structure_profile` | `structure_profile: StrictStr = Field(min_length=1)` | Document-specific planning-structure profile identity propagated through source locks and results. |

**Interface consumers**

- type annotation: `src/landscout/stages/interpret_bess_zoning.py::BessZoningPolicyConfig` via `PolicySourceLock`.

**Exact class source**

```python
class PolicySourceLock(_StrictConfigModel):
    document_id: StrictStr = Field(min_length=1)
    archive_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    structure_result_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    structure_profile: StrictStr = Field(min_length=1)
```

### `PolicyEvidence`

**Purpose:** One source-locked written-regulation evidence occurrence, including direction, kind, exact excerpt/span/hash, source rule, applicability note, and route links.

**Kind:** Pydantic model.

**Inheritance:** `_StrictConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `evidence_id` | `evidence_id: StrictStr = Field(min_length=1)` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `section_id` | `section_id: StrictStr = Field(min_length=1)` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `page_number` | `page_number: StrictInt = Field(ge=1)` | One-based source PDF page number owning this record/evidence occurrence. |
| `evidence_kind` | `evidence_kind: EvidenceKind` | `PolicyEvidence.evidence_kind` represents the `evidence_kind` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `evidence_direction` | `evidence_direction: EvidenceDirection` | `PolicyEvidence.evidence_direction` represents the `evidence_direction` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `exact_raw_excerpt` | `exact_raw_excerpt: StrictStr = Field(min_length=1, max_length=600)` | Exact source regulation substring bound to its page fragment, offsets, and SHA256. |
| `excerpt_sha256` | `excerpt_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `section_page_fragment_sha256` | `section_page_fragment_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `excerpt_start` | `excerpt_start: StrictInt = Field(ge=0)` | Inclusive source-fragment character offset for the exact regulation excerpt. |
| `excerpt_end` | `excerpt_end: StrictInt = Field(ge=1)` | Exclusive source-fragment character offset for the exact regulation excerpt. |
| `source_rule_id` | `source_rule_id: StrictStr = Field(min_length=1)` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `source_rule_excerpt` | `source_rule_excerpt: StrictStr = Field(min_length=1)` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |
| `source_rule_sha256` | `source_rule_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_rule_start` | `source_rule_start: StrictInt = Field(ge=0)` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |
| `source_rule_end` | `source_rule_end: StrictInt = Field(ge=1)` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |
| `interpretation_note` | `interpretation_note: StrictStr = Field(min_length=1)` | `PolicyEvidence.interpretation_note` carries the interpretation note used by the reproduced constructors and validators; its declared type is `StrictStr` and no legal meaning is inferred beyond that owner. |

**Validators (exact source)**

`_validate_exact_strings`:

```python
def _validate_exact_strings(self) -> PolicyEvidence:
        for value, label in (
            (self.evidence_id, "evidence ID"),
            (self.section_id, "evidence section ID"),
            (self.exact_raw_excerpt, "exact raw excerpt"),
            (self.source_rule_id, "source rule ID"),
            (self.source_rule_excerpt, "source rule excerpt"),
            (self.interpretation_note, "interpretation note"),
        ):
            _config_string(value, label)
        if sha256(self.exact_raw_excerpt.encode("utf-8")).hexdigest() != self.excerpt_sha256:
            raise ValueError("evidence excerpt SHA256 differs from exact_raw_excerpt")
        if self.excerpt_end <= self.excerpt_start:
            raise ValueError("evidence excerpt offsets must be ordered")
        if sha256(self.source_rule_excerpt.encode("utf-8")).hexdigest() != (
            self.source_rule_sha256
        ):
            raise ValueError("source rule SHA256 differs from source_rule_excerpt")
        if self.source_rule_end <= self.source_rule_start:
            raise ValueError("source rule offsets must be ordered")
        if not (
            self.source_rule_start <= self.excerpt_start
            and self.excerpt_end <= self.source_rule_end
        ):
            raise ValueError("evidence excerpt must lie inside its source rule")
        allowed_directions: dict[str, frozenset[str]] = {
            "USE_PERMISSION": frozenset(
                {"SUPPORTS_POTENTIAL_COMPATIBILITY", "CONTEXT_ONLY"}
            ),
            "USE_RESTRICTION": frozenset({"SUPPORTS_DIFFICULTY", "CONTEXT_ONLY"}),
            "PUBLIC_INTEREST_EXCEPTION": frozenset(
                {
                    "SUPPORTS_POTENTIAL_COMPATIBILITY",
                    "CONDITION",
                    "CONTEXT_ONLY",
                }
            ),
            "TECHNICAL_EQUIPMENT_RULE": frozenset(
                {
                    "SUPPORTS_POTENTIAL_COMPATIBILITY",
                    "SUPPORTS_DIFFICULTY",
                    "CONDITION",
                    "CONTEXT_ONLY",
                }
            ),
            "ICPE_RULE": frozenset(
                {
                    "SUPPORTS_POTENTIAL_COMPATIBILITY",
                    "SUPPORTS_DIFFICULTY",
                    "CONDITION",
                    "CONTEXT_ONLY",
                }
            ),
            "RISK_OR_NUISANCE_CONDITION": frozenset(
                {"SUPPORTS_DIFFICULTY", "CONDITION", "CONTEXT_ONLY"}
            ),
            "ACCESS_OR_NETWORK_CONDITION": frozenset(
                {"SUPPORTS_DIFFICULTY", "CONDITION", "CONTEXT_ONLY"}
            ),
            "OTHER_RELEVANT_RULE": frozenset(
                {"SUPPORTS_DIFFICULTY", "CONDITION", "CONTEXT_ONLY"}
            ),
        }
        allowed = allowed_directions[self.evidence_kind]
        if self.evidence_direction not in allowed:
            raise ValueError("evidence kind and direction are incompatible")
        return self
```

**Interface consumers**

- type annotation: `src/landscout/stages/interpret_bess_zoning.py::PolicyEvidence._validate_exact_strings` via `PolicyEvidence`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::ChapterPolicy` via `PolicyEvidence`.

**Exact class source**

```python
class PolicyEvidence(_StrictConfigModel):
    evidence_id: StrictStr = Field(min_length=1)
    section_id: StrictStr = Field(min_length=1)
    page_number: StrictInt = Field(ge=1)
    evidence_kind: EvidenceKind
    evidence_direction: EvidenceDirection
    exact_raw_excerpt: StrictStr = Field(min_length=1, max_length=600)
    excerpt_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    section_page_fragment_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    excerpt_start: StrictInt = Field(ge=0)
    excerpt_end: StrictInt = Field(ge=1)
    source_rule_id: StrictStr = Field(min_length=1)
    source_rule_excerpt: StrictStr = Field(min_length=1)
    source_rule_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    source_rule_start: StrictInt = Field(ge=0)
    source_rule_end: StrictInt = Field(ge=1)
    interpretation_note: StrictStr = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_exact_strings(self) -> PolicyEvidence:
        for value, label in (
            (self.evidence_id, "evidence ID"),
            (self.section_id, "evidence section ID"),
            (self.exact_raw_excerpt, "exact raw excerpt"),
            (self.source_rule_id, "source rule ID"),
            (self.source_rule_excerpt, "source rule excerpt"),
            (self.interpretation_note, "interpretation note"),
        ):
            _config_string(value, label)
        if sha256(self.exact_raw_excerpt.encode("utf-8")).hexdigest() != self.excerpt_sha256:
            raise ValueError("evidence excerpt SHA256 differs from exact_raw_excerpt")
        if self.excerpt_end <= self.excerpt_start:
            raise ValueError("evidence excerpt offsets must be ordered")
        if sha256(self.source_rule_excerpt.encode("utf-8")).hexdigest() != (
            self.source_rule_sha256
        ):
            raise ValueError("source rule SHA256 differs from source_rule_excerpt")
        if self.source_rule_end <= self.source_rule_start:
            raise ValueError("source rule offsets must be ordered")
        if not (
            self.source_rule_start <= self.excerpt_start
            and self.excerpt_end <= self.source_rule_end
        ):
            raise ValueError("evidence excerpt must lie inside its source rule")
        allowed_directions: dict[str, frozenset[str]] = {
            "USE_PERMISSION": frozenset(
                {"SUPPORTS_POTENTIAL_COMPATIBILITY", "CONTEXT_ONLY"}
            ),
            "USE_RESTRICTION": frozenset({"SUPPORTS_DIFFICULTY", "CONTEXT_ONLY"}),
            "PUBLIC_INTEREST_EXCEPTION": frozenset(
                {
                    "SUPPORTS_POTENTIAL_COMPATIBILITY",
                    "CONDITION",
                    "CONTEXT_ONLY",
                }
            ),
            "TECHNICAL_EQUIPMENT_RULE": frozenset(
                {
                    "SUPPORTS_POTENTIAL_COMPATIBILITY",
                    "SUPPORTS_DIFFICULTY",
                    "CONDITION",
                    "CONTEXT_ONLY",
                }
            ),
            "ICPE_RULE": frozenset(
                {
                    "SUPPORTS_POTENTIAL_COMPATIBILITY",
                    "SUPPORTS_DIFFICULTY",
                    "CONDITION",
                    "CONTEXT_ONLY",
                }
            ),
            "RISK_OR_NUISANCE_CONDITION": frozenset(
                {"SUPPORTS_DIFFICULTY", "CONDITION", "CONTEXT_ONLY"}
            ),
            "ACCESS_OR_NETWORK_CONDITION": frozenset(
                {"SUPPORTS_DIFFICULTY", "CONDITION", "CONTEXT_ONLY"}
            ),
            "OTHER_RELEVANT_RULE": frozenset(
                {"SUPPORTS_DIFFICULTY", "CONDITION", "CONTEXT_ONLY"}
            ),
        }
        allowed = allowed_directions[self.evidence_kind]
        if self.evidence_direction not in allowed:
            raise ValueError("evidence kind and direction are incompatible")
        return self
```

### `RouteAssessment`

**Purpose:** One configured written-zoning evidence route and its deterministic status, evidence-role lists, applicability, review, policy, and source lineage.

**Kind:** Pydantic model.

**Inheritance:** `_StrictConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `route_id` | `route_id: StrictStr = Field(min_length=1)` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `route_kind` | `route_kind: RouteKind` | `RouteAssessment.route_kind` represents the `route_kind` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `positive_evidence_ids` | `positive_evidence_ids: tuple[StrictStr, ...] = ()` | `RouteAssessment.positive_evidence_ids` carries the positive evidence ids used by the reproduced constructors and validators; its declared type is `tuple[StrictStr, ...]` and no legal meaning is inferred beyond that owner. |
| `condition_evidence_ids` | `condition_evidence_ids: tuple[StrictStr, ...] = ()` | `RouteAssessment.condition_evidence_ids` carries the condition evidence ids used by the reproduced constructors and validators; its declared type is `tuple[StrictStr, ...]` and no legal meaning is inferred beyond that owner. |
| `difficulty_evidence_ids` | `difficulty_evidence_ids: tuple[StrictStr, ...] = ()` | `RouteAssessment.difficulty_evidence_ids` carries the difficulty evidence ids used by the reproduced constructors and validators; its declared type is `tuple[StrictStr, ...]` and no legal meaning is inferred beyond that owner. |
| `applicability_note` | `applicability_note: StrictStr = Field(min_length=1)` | `RouteAssessment.applicability_note` carries the applicability note used by the reproduced constructors and validators; its declared type is `StrictStr` and no legal meaning is inferred beyond that owner. |

**Validators (exact source)**

`_validate_route_shape`:

```python
def _validate_route_shape(self) -> RouteAssessment:
        _config_string(self.route_id, "route ID")
        _config_string(self.applicability_note, "route applicability note")
        roles = {
            "positive": self.positive_evidence_ids,
            "condition": self.condition_evidence_ids,
            "difficulty": self.difficulty_evidence_ids,
        }
        combined: list[str] = []
        for role, values in roles.items():
            normalized = [_config_string(value, f"{role} evidence ID") for value in values]
            if len(set(normalized)) != len(normalized):
                raise ValueError(f"{role} evidence IDs must be unique within a route")
            combined.extend(normalized)
        if len(set(combined)) != len(combined):
            raise ValueError("one evidence ID cannot occupy incompatible route roles")
        positive = bool(self.positive_evidence_ids)
        condition = bool(self.condition_evidence_ids)
        difficulty = bool(self.difficulty_evidence_ids)
        expected = {
            "DIRECT_ROUTE": (True, False, False),
            "CONDITIONAL_ROUTE": (True, True, False),
            "RESTRICTION_EXCEPTION_ROUTE": (True, False, True),
            "DIFFICULTY_ONLY": (False, False, True),
        }[self.route_kind]
        if (positive, condition, difficulty) != expected:
            raise ValueError(
                f"{self.route_kind} has incompatible evidence-role membership"
            )
        return self
```

**Interface consumers**

- type annotation: `src/landscout/stages/interpret_bess_zoning.py::RouteAssessment._validate_route_shape` via `RouteAssessment`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_derived_chapter_status` via `RouteAssessment`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::ChapterPolicy` via `RouteAssessment`.

**Exact class source**

```python
class RouteAssessment(_StrictConfigModel):
    route_id: StrictStr = Field(min_length=1)
    route_kind: RouteKind
    positive_evidence_ids: tuple[StrictStr, ...] = ()
    condition_evidence_ids: tuple[StrictStr, ...] = ()
    difficulty_evidence_ids: tuple[StrictStr, ...] = ()
    applicability_note: StrictStr = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_route_shape(self) -> RouteAssessment:
        _config_string(self.route_id, "route ID")
        _config_string(self.applicability_note, "route applicability note")
        roles = {
            "positive": self.positive_evidence_ids,
            "condition": self.condition_evidence_ids,
            "difficulty": self.difficulty_evidence_ids,
        }
        combined: list[str] = []
        for role, values in roles.items():
            normalized = [_config_string(value, f"{role} evidence ID") for value in values]
            if len(set(normalized)) != len(normalized):
                raise ValueError(f"{role} evidence IDs must be unique within a route")
            combined.extend(normalized)
        if len(set(combined)) != len(combined):
            raise ValueError("one evidence ID cannot occupy incompatible route roles")
        positive = bool(self.positive_evidence_ids)
        condition = bool(self.condition_evidence_ids)
        difficulty = bool(self.difficulty_evidence_ids)
        expected = {
            "DIRECT_ROUTE": (True, False, False),
            "CONDITIONAL_ROUTE": (True, True, False),
            "RESTRICTION_EXCEPTION_ROUTE": (True, False, True),
            "DIFFICULTY_ONLY": (False, False, True),
        }[self.route_kind]
        if (positive, condition, difficulty) != expected:
            raise ValueError(
                f"{self.route_kind} has incompatible evidence-role membership"
            )
        return self
```

### `ChapterPolicy`

**Purpose:** One zone chapter's reviewed sections, completeness, evidence/routes, precheck status/confidence, rationale, missing information, and scope.

**Kind:** Pydantic model.

**Inheritance:** `_StrictConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `resolved_zone_chapter_label` | `resolved_zone_chapter_label: StrictStr = Field(min_length=1)` | `ChapterPolicy.resolved_zone_chapter_label` carries the resolved zone chapter label used by the reproduced constructors and validators; its declared type is `StrictStr` and no legal meaning is inferred beyond that owner. |
| `review_completeness` | `review_completeness: ReviewCompleteness` | Configured chapter review-completeness classification consumed by the written-zoning policy. |
| `reviewed_section_ids` | `reviewed_section_ids: tuple[StrictStr, ...] = ()` | Structured `reviewed section ids` collection owned by `ChapterPolicy`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `review_note` | `review_note: StrictStr = Field(min_length=1)` | `ChapterPolicy.review_note` carries the review note used by the reproduced constructors and validators; its declared type is `StrictStr` and no legal meaning is inferred beyond that owner. |
| `zoning_precheck_status` | `zoning_precheck_status: ChapterStatus` | `ChapterPolicy.zoning_precheck_status` represents the `zoning_precheck_status` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `zoning_precheck_confidence` | `zoning_precheck_confidence: Confidence` | Chapter-level zoning precheck confidence propagated to mapped zones/parcels. |
| `rationale` | `rationale: StrictStr = Field(min_length=1)` | `ChapterPolicy.rationale` carries the rationale used by the reproduced constructors and validators; its declared type is `StrictStr` and no legal meaning is inferred beyond that owner. |
| `missing_information` | `missing_information: StrictStr = Field(min_length=1)` | `ChapterPolicy.missing_information` represents the `missing_information` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `evidence` | `evidence: tuple[PolicyEvidence, ...] = ()` | `ChapterPolicy.evidence` carries the evidence used by the reproduced constructors and validators; its declared type is `tuple[PolicyEvidence, ...]` and no legal meaning is inferred beyond that owner. |
| `route_assessments` | `route_assessments: tuple[RouteAssessment, ...] = ()` | Deterministic written-zoning evidence-route assessment frame. |

**Validators (exact source)**

`_validate_evidence_semantics`:

```python
def _validate_evidence_semantics(self) -> ChapterPolicy:
        _config_string(self.resolved_zone_chapter_label, "chapter label")
        _config_string(self.review_note, "chapter review note")
        _config_string(self.rationale, "chapter rationale")
        _config_string(self.missing_information, "chapter missing information")
        reviewed = [
            _config_string(value, "reviewed section ID")
            for value in self.reviewed_section_ids
        ]
        if len(set(reviewed)) != len(reviewed):
            raise ValueError("reviewed section IDs must be unique")
        if self.review_completeness == "INCOMPLETE" and (
            self.zoning_precheck_status != "UNKNOWN"
            or self.zoning_precheck_confidence != "LOW"
        ):
            raise ValueError("incomplete review requires UNKNOWN / LOW")
        route_ids = [route.route_id for route in self.route_assessments]
        if len(set(route_ids)) != len(route_ids):
            raise ValueError("route IDs must be unique within a chapter")
        expected_status = _derived_chapter_status(
            self.review_completeness,
            self.route_assessments,
        )
        if self.zoning_precheck_status != expected_status:
            raise ValueError(
                "declared chapter status differs from coherent linked route assessments"
            )
        return self
```

**Interface consumers**

- type annotation: `src/landscout/stages/interpret_bess_zoning.py::ChapterPolicy._validate_evidence_semantics` via `ChapterPolicy`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::BessZoningPolicyConfig` via `ChapterPolicy`.

**Exact class source**

```python
class ChapterPolicy(_StrictConfigModel):
    resolved_zone_chapter_label: StrictStr = Field(min_length=1)
    review_completeness: ReviewCompleteness
    reviewed_section_ids: tuple[StrictStr, ...] = ()
    review_note: StrictStr = Field(min_length=1)
    zoning_precheck_status: ChapterStatus
    zoning_precheck_confidence: Confidence
    rationale: StrictStr = Field(min_length=1)
    missing_information: StrictStr = Field(min_length=1)
    evidence: tuple[PolicyEvidence, ...] = ()
    route_assessments: tuple[RouteAssessment, ...] = ()

    @model_validator(mode="after")
    def _validate_evidence_semantics(self) -> ChapterPolicy:
        _config_string(self.resolved_zone_chapter_label, "chapter label")
        _config_string(self.review_note, "chapter review note")
        _config_string(self.rationale, "chapter rationale")
        _config_string(self.missing_information, "chapter missing information")
        reviewed = [
            _config_string(value, "reviewed section ID")
            for value in self.reviewed_section_ids
        ]
        if len(set(reviewed)) != len(reviewed):
            raise ValueError("reviewed section IDs must be unique")
        if self.review_completeness == "INCOMPLETE" and (
            self.zoning_precheck_status != "UNKNOWN"
            or self.zoning_precheck_confidence != "LOW"
        ):
            raise ValueError("incomplete review requires UNKNOWN / LOW")
        route_ids = [route.route_id for route in self.route_assessments]
        if len(set(route_ids)) != len(route_ids):
            raise ValueError("route IDs must be unique within a chapter")
        expected_status = _derived_chapter_status(
            self.review_completeness,
            self.route_assessments,
        )
        if self.zoning_precheck_status != expected_status:
            raise ValueError(
                "declared chapter status differs from coherent linked route assessments"
            )
        return self
```

### `BessZoningPolicyConfig`

**Purpose:** Strict source-locked interpretation policy.

**Kind:** Pydantic model.

**Inheritance:** `_StrictConfigModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `schema_version` | `schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `policy_profile` | `policy_profile: StrictStr = Field(min_length=1)` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `planning_precheck_scope` | `planning_precheck_scope: Literal["WRITTEN_ZONING_REGULATION_ONLY"]` | `BessZoningPolicyConfig.planning_precheck_scope` represents the `planning_precheck_scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `review_scope` | `review_scope: Literal["CONFIGURED_USE_CONTROL_ARTICLES_ONLY"]` | `BessZoningPolicyConfig.review_scope` represents the `review_scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `source_lock` | `source_lock: PolicySourceLock` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |
| `required_zone_article_numbers` | `required_zone_article_numbers: tuple[StrictStr, ...] = Field(min_length=1)` | Structured `required zone article numbers` collection owned by `BessZoningPolicyConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `chapters` | `chapters: tuple[ChapterPolicy, ...] = Field(min_length=1)` | Structured `chapters` collection owned by `BessZoningPolicyConfig`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Validators (exact source)**

`_validate_policy`:

```python
def _validate_policy(self) -> BessZoningPolicyConfig:
        if self.schema_version != POLICY_SCHEMA_VERSION:
            raise ValueError(f"unsupported BESS zoning policy schema: {self.schema_version}")
        _config_string(self.policy_profile, "policy profile")
        _config_string(self.source_lock.document_id, "policy document ID")
        _config_string(self.source_lock.structure_profile, "policy structure profile")
        article_numbers = [
            _config_string(value, "required zone article number")
            for value in self.required_zone_article_numbers
        ]
        if len(set(article_numbers)) != len(article_numbers):
            raise ValueError("required zone article numbers must be unique")
        labels = [chapter.resolved_zone_chapter_label for chapter in self.chapters]
        if len(set(labels)) != len(labels):
            raise ValueError("chapter policy labels must be unique")
        evidence_ids: set[str] = set()
        route_ids: set[str] = set()
        chapter_occurrences: dict[
            tuple[str, str, int, str, int, int], tuple[str, str, str]
        ] = {}
        source_rules: dict[str, tuple[object, ...]] = {}
        source_rule_occurrences: dict[tuple[object, ...], str] = {}
        source_rule_ranges: dict[tuple[str, int, str], list[tuple[int, int, str]]] = {}
        for chapter in self.chapters:
            chapter_evidence = {
                evidence.evidence_id: evidence for evidence in chapter.evidence
            }
            linked_evidence_ids: set[str] = set()
            for evidence in chapter.evidence:
                if evidence.evidence_id in evidence_ids:
                    raise ValueError("evidence IDs must be globally unique")
                evidence_ids.add(evidence.evidence_id)
                key = (
                    chapter.resolved_zone_chapter_label,
                    evidence.section_id,
                    evidence.page_number,
                    evidence.section_page_fragment_sha256,
                    evidence.excerpt_start,
                    evidence.excerpt_end,
                )
                previous = chapter_occurrences.get(key)
                if previous is not None:
                    raise ValueError(
                        "one chapter-scoped evidence occurrence must resolve to exactly one evidence ID, kind, and direction"
                    )
                chapter_occurrences[key] = (
                    evidence.evidence_id,
                    evidence.evidence_kind,
                    evidence.evidence_direction,
                )
                rule_identity = (
                    evidence.section_id,
                    evidence.page_number,
                    evidence.section_page_fragment_sha256,
                    evidence.source_rule_start,
                    evidence.source_rule_end,
                    evidence.source_rule_sha256,
                    evidence.source_rule_excerpt,
                )
                prior_rule = source_rules.get(evidence.source_rule_id)
                if prior_rule is not None and prior_rule != rule_identity:
                    raise ValueError(
                        "one source rule ID must resolve to one exact occurrence"
                    )
                source_rules[evidence.source_rule_id] = rule_identity
                occurrence = rule_identity[:5]
                prior_rule_id = source_rule_occurrences.get(occurrence)
                if prior_rule_id is not None and prior_rule_id != evidence.source_rule_id:
                    raise ValueError(
                        "one exact source-rule occurrence must use one source rule ID"
                    )
                source_rule_occurrences[occurrence] = evidence.source_rule_id
                range_key = (
                    evidence.section_id,
                    evidence.page_number,
                    evidence.section_page_fragment_sha256,
                )
                ranges = source_rule_ranges.setdefault(range_key, [])
                current = (
                    evidence.source_rule_start,
                    evidence.source_rule_end,
                    evidence.source_rule_id,
                )
                for start, end, rule_id in ranges:
                    overlaps = max(start, current[0]) < min(end, current[1])
                    identical = start == current[0] and end == current[1]
                    if overlaps and not identical:
                        raise ValueError(
                            f"source rule {evidence.source_rule_id!r} partially overlaps {rule_id!r}"
                        )
                if current not in ranges:
                    ranges.append(current)
            for route in chapter.route_assessments:
                if route.route_id in route_ids:
                    raise ValueError("route IDs must be globally unique")
                route_ids.add(route.route_id)
                roles = (
                    (
                        route.positive_evidence_ids,
                        "SUPPORTS_POTENTIAL_COMPATIBILITY",
                        "positive",
                    ),
                    (route.condition_evidence_ids, "CONDITION", "condition"),
                    (
                        route.difficulty_evidence_ids,
                        "SUPPORTS_DIFFICULTY",
                        "difficulty",
                    ),
                )
                for identifiers, expected_direction, role in roles:
                    for evidence_id in identifiers:
                        referenced_evidence = chapter_evidence.get(evidence_id)
                        if referenced_evidence is None:
                            raise ValueError(
                                f"route references unknown or another-chapter evidence ID {evidence_id!r}"
                            )
                        if referenced_evidence.evidence_direction != expected_direction:
                            raise ValueError(
                                f"route assigns evidence ID {evidence_id!r} to an incompatible {role} role"
                            )
                        linked_evidence_ids.add(evidence_id)
            for evidence in chapter.evidence:
                is_linked = evidence.evidence_id in linked_evidence_ids
                if evidence.evidence_direction == "CONTEXT_ONLY" and is_linked:
                    raise ValueError("CONTEXT_ONLY evidence must not be linked to a route")
                if evidence.evidence_direction != "CONTEXT_ONLY" and not is_linked:
                    raise ValueError(
                        "decision evidence must be linked to at least one route"
                    )
        return self
```

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`.
- import: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.interpret_bess_zoning import (
    CHAPTER_POLICY_COLUMNS,
    EVIDENCE_CATALOG_COLUMNS,
    EVIDENCE_ROUTE_LINK_COLUMNS,
    PARCEL_ZONE_POLICY_COLUMNS,
    ROUTE_ASSESSMENT_COLUMNS,
    SOURCE_ZONE_POLICY_COLUMNS,
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    _result_with_hashes,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::BessZoningPolicyConfig._validate_policy` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::load_bess_zoning_policy_config` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_policy_sha256` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_resolved_policy` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_lock` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_required_section_ids_by_chapter` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_evidence` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_lineage` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_chapter_policy` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_route_assessments` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_evidence_route_links` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_source_zone_policy` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_parcel_zone_interpretations` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_parcel_output` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::validate_bess_zoning_precheck` via `BessZoningPolicyConfig`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::interpret_bess_zoning` via `BessZoningPolicyConfig`.
- type annotation: `tests/unit/test_interpret_bess_zoning.py::_policy` via `BessZoningPolicyConfig`.
- type annotation: `tests/unit/test_interpret_bess_zoning.py::_payload` via `BessZoningPolicyConfig`.
- type annotation: `tests/unit/test_interpret_bess_zoning.py::_policy_with_context_only_evidence` via `BessZoningPolicyConfig`.

**Exact class source**

```python
class BessZoningPolicyConfig(_StrictConfigModel):
    """Strict source-locked interpretation policy."""

    schema_version: StrictInt
    policy_profile: StrictStr = Field(min_length=1)
    planning_precheck_scope: Literal["WRITTEN_ZONING_REGULATION_ONLY"]
    review_scope: Literal["CONFIGURED_USE_CONTROL_ARTICLES_ONLY"]
    source_lock: PolicySourceLock
    required_zone_article_numbers: tuple[StrictStr, ...] = Field(min_length=1)
    chapters: tuple[ChapterPolicy, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_policy(self) -> BessZoningPolicyConfig:
        if self.schema_version != POLICY_SCHEMA_VERSION:
            raise ValueError(f"unsupported BESS zoning policy schema: {self.schema_version}")
        _config_string(self.policy_profile, "policy profile")
        _config_string(self.source_lock.document_id, "policy document ID")
        _config_string(self.source_lock.structure_profile, "policy structure profile")
        article_numbers = [
            _config_string(value, "required zone article number")
            for value in self.required_zone_article_numbers
        ]
        if len(set(article_numbers)) != len(article_numbers):
            raise ValueError("required zone article numbers must be unique")
        labels = [chapter.resolved_zone_chapter_label for chapter in self.chapters]
        if len(set(labels)) != len(labels):
            raise ValueError("chapter policy labels must be unique")
        evidence_ids: set[str] = set()
        route_ids: set[str] = set()
        chapter_occurrences: dict[
            tuple[str, str, int, str, int, int], tuple[str, str, str]
        ] = {}
        source_rules: dict[str, tuple[object, ...]] = {}
        source_rule_occurrences: dict[tuple[object, ...], str] = {}
        source_rule_ranges: dict[tuple[str, int, str], list[tuple[int, int, str]]] = {}
        for chapter in self.chapters:
            chapter_evidence = {
                evidence.evidence_id: evidence for evidence in chapter.evidence
            }
            linked_evidence_ids: set[str] = set()
            for evidence in chapter.evidence:
                if evidence.evidence_id in evidence_ids:
                    raise ValueError("evidence IDs must be globally unique")
                evidence_ids.add(evidence.evidence_id)
                key = (
                    chapter.resolved_zone_chapter_label,
                    evidence.section_id,
                    evidence.page_number,
                    evidence.section_page_fragment_sha256,
                    evidence.excerpt_start,
                    evidence.excerpt_end,
                )
                previous = chapter_occurrences.get(key)
                if previous is not None:
                    raise ValueError(
                        "one chapter-scoped evidence occurrence must resolve to exactly one evidence ID, kind, and direction"
                    )
                chapter_occurrences[key] = (
                    evidence.evidence_id,
                    evidence.evidence_kind,
                    evidence.evidence_direction,
                )
                rule_identity = (
                    evidence.section_id,
                    evidence.page_number,
                    evidence.section_page_fragment_sha256,
                    evidence.source_rule_start,
                    evidence.source_rule_end,
                    evidence.source_rule_sha256,
                    evidence.source_rule_excerpt,
                )
                prior_rule = source_rules.get(evidence.source_rule_id)
                if prior_rule is not None and prior_rule != rule_identity:
                    raise ValueError(
                        "one source rule ID must resolve to one exact occurrence"
                    )
                source_rules[evidence.source_rule_id] = rule_identity
                occurrence = rule_identity[:5]
                prior_rule_id = source_rule_occurrences.get(occurrence)
                if prior_rule_id is not None and prior_rule_id != evidence.source_rule_id:
                    raise ValueError(
                        "one exact source-rule occurrence must use one source rule ID"
                    )
                source_rule_occurrences[occurrence] = evidence.source_rule_id
                range_key = (
                    evidence.section_id,
                    evidence.page_number,
                    evidence.section_page_fragment_sha256,
                )
                ranges = source_rule_ranges.setdefault(range_key, [])
                current = (
                    evidence.source_rule_start,
                    evidence.source_rule_end,
                    evidence.source_rule_id,
                )
                for start, end, rule_id in ranges:
                    overlaps = max(start, current[0]) < min(end, current[1])
                    identical = start == current[0] and end == current[1]
                    if overlaps and not identical:
                        raise ValueError(
                            f"source rule {evidence.source_rule_id!r} partially overlaps {rule_id!r}"
                        )
                if current not in ranges:
                    ranges.append(current)
            for route in chapter.route_assessments:
                if route.route_id in route_ids:
                    raise ValueError("route IDs must be globally unique")
                route_ids.add(route.route_id)
                roles = (
                    (
                        route.positive_evidence_ids,
                        "SUPPORTS_POTENTIAL_COMPATIBILITY",
                        "positive",
                    ),
                    (route.condition_evidence_ids, "CONDITION", "condition"),
                    (
                        route.difficulty_evidence_ids,
                        "SUPPORTS_DIFFICULTY",
                        "difficulty",
                    ),
                )
                for identifiers, expected_direction, role in roles:
                    for evidence_id in identifiers:
                        referenced_evidence = chapter_evidence.get(evidence_id)
                        if referenced_evidence is None:
                            raise ValueError(
                                f"route references unknown or another-chapter evidence ID {evidence_id!r}"
                            )
                        if referenced_evidence.evidence_direction != expected_direction:
                            raise ValueError(
                                f"route assigns evidence ID {evidence_id!r} to an incompatible {role} role"
                            )
                        linked_evidence_ids.add(evidence_id)
            for evidence in chapter.evidence:
                is_linked = evidence.evidence_id in linked_evidence_ids
                if evidence.evidence_direction == "CONTEXT_ONLY" and is_linked:
                    raise ValueError("CONTEXT_ONLY evidence must not be linked to a route")
                if evidence.evidence_direction != "CONTEXT_ONLY" and not is_linked:
                    raise ValueError(
                        "decision evidence must be linked to at least one route"
                    )
        return self
```

### `BessZoningPrecheckResult`

**Purpose:** Immutable envelope around the conservative written-zoning precheck.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `result_hash_schema_version` | `result_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `policy_schema_version` | `policy_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `policy_profile` | `policy_profile: str` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `planning_precheck_scope` | `planning_precheck_scope: str` | `BessZoningPrecheckResult.planning_precheck_scope` represents the `planning_precheck_scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `review_scope` | `review_scope: str` | `BessZoningPrecheckResult.review_scope` represents the `review_scope` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `document_id` | `document_id: str` | Exact identity for the entity named by the field; uniqueness, portability, and lineage meaning are only those explicitly validated by the owner. |
| `archive_sha256` | `archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `pdf_sha256` | `pdf_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `index_content_sha256` | `index_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `structure_result_content_sha256` | `structure_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `structure_profile` | `structure_profile: str` | Document-specific planning-structure profile identity propagated through source locks and results. |
| `policy_config_sha256` | `policy_config_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `factual_structure_content_sha256` | `factual_structure_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `zone_mapping_input_sha256` | `zone_mapping_input_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `zoning_relation_hash_columns` | `zoning_relation_hash_columns: tuple[str, ...]` | Structured `zoning relation hash columns` collection owned by `BessZoningPrecheckResult`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `zoning_relations_input_sha256` | `zoning_relations_input_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `evidence_catalog_content_sha256` | `evidence_catalog_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `evidence_route_links_content_sha256` | `evidence_route_links_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `route_assessments_content_sha256` | `route_assessments_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `chapter_policy_content_sha256` | `chapter_policy_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_zone_policy_content_sha256` | `source_zone_policy_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `parcel_zone_policy_content_sha256` | `parcel_zone_policy_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `parcel_output_content_sha256` | `parcel_output_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `complete_result_content_sha256` | `complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `touch_only_relation_count` | `touch_only_relation_count: int` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `evidence_catalog` | `evidence_catalog: pd.DataFrame` | `BessZoningPrecheckResult.evidence_catalog` carries the evidence catalog used by the reproduced constructors and validators; its declared type is `pd.DataFrame` and no legal meaning is inferred beyond that owner. |
| `evidence_route_links` | `evidence_route_links: pd.DataFrame` | `BessZoningPrecheckResult.evidence_route_links` carries the evidence route links used by the reproduced constructors and validators; its declared type is `pd.DataFrame` and no legal meaning is inferred beyond that owner. |
| `route_assessments` | `route_assessments: pd.DataFrame` | Deterministic written-zoning evidence-route assessment frame. |
| `chapter_policy` | `chapter_policy: pd.DataFrame` | Deterministic chapter-level written-zoning policy frame. |
| `source_zone_policy` | `source_zone_policy: pd.DataFrame` | Source fact or textual lineage named by the suffix; it becomes physical proof only where a validator rechecks bytes/source content. |
| `parcel_zone_interpretations` | `parcel_zone_interpretations: pd.DataFrame` | Deterministic parcel-zone written-zoning interpretation frame. |
| `parcels` | `parcels: gpd.GeoDataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_result_component_metadata` via `BessZoningPrecheckResult`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_result_frame_sha256` via `BessZoningPrecheckResult`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_complete_result_sha256` via `BessZoningPrecheckResult`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_result_with_hashes` via `BessZoningPrecheckResult`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `BessZoningPrecheckResult`.
- constructor call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `BessZoningPrecheckResult`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `BessZoningPrecheckResult`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::validate_bess_zoning_precheck` via `BessZoningPrecheckResult`.
- type annotation: `src/landscout/stages/interpret_bess_zoning.py::interpret_bess_zoning` via `BessZoningPrecheckResult`.

**Exact class source**

```python
class BessZoningPrecheckResult:
    """Immutable envelope around the conservative written-zoning precheck."""

    result_hash_schema_version: int
    policy_schema_version: int
    policy_profile: str
    planning_precheck_scope: str
    review_scope: str
    document_id: str
    archive_sha256: str
    pdf_sha256: str
    index_content_sha256: str
    structure_result_content_sha256: str
    structure_profile: str
    policy_config_sha256: str
    factual_structure_content_sha256: str
    zone_mapping_input_sha256: str
    zoning_relation_hash_columns: tuple[str, ...]
    zoning_relations_input_sha256: str
    evidence_catalog_content_sha256: str
    evidence_route_links_content_sha256: str
    route_assessments_content_sha256: str
    chapter_policy_content_sha256: str
    source_zone_policy_content_sha256: str
    parcel_zone_policy_content_sha256: str
    parcel_output_content_sha256: str
    complete_result_content_sha256: str
    touch_only_relation_count: int
    evidence_catalog: pd.DataFrame
    evidence_route_links: pd.DataFrame
    route_assessments: pd.DataFrame
    chapter_policy: pd.DataFrame
    source_zone_policy: pd.DataFrame
    parcel_zone_interpretations: pd.DataFrame
    parcels: gpd.GeoDataFrame
```

### `_UniqueKeyLoader`

**Purpose:** Private PyYAML SafeLoader subclass whose mapping constructor is replaced to reject duplicate YAML keys.

**Kind:** PyYAML loader subclass.

**Inheritance:** `yaml.SafeLoader`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- No repository construction/import/property/decorator reference was found; the exact declaration is retained because it participates in the module's runtime/framework namespace.

**Exact class source**

```python
class _UniqueKeyLoader(yaml.SafeLoader):
    pass
```


## 6. Functions and methods

### `PolicyEvidence._validate_exact_strings`

**Exact signature**

```python
def _validate_exact_strings(self) -> PolicyEvidence:
```

**Purpose**

Rejects malformed or inconsistent exact strings; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `PolicyEvidence`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `sha256(self.exact_raw_excerpt.encode('utf-8')).hexdigest() != self.excerpt_sha256`.
- Guard with a raise path: `self.excerpt_end <= self.excerpt_start`.
- Guard with a raise path: `sha256(self.source_rule_excerpt.encode('utf-8')).hexdigest() != self.source_rule_sha256`.
- Guard with a raise path: `self.source_rule_end <= self.source_rule_start`.
- Guard with a raise path: `not (self.source_rule_start <= self.excerpt_start and self.excerpt_end <= self.source_rule_end)`.
- Guard with a raise path: `self.evidence_direction not in allowed`.
- Explicit raise expressions: `ValueError('evidence excerpt SHA256 differs from exact_raw_excerpt')`, `ValueError('evidence excerpt must lie inside its source rule')`, `ValueError('evidence excerpt offsets must be ordered')`, `ValueError('evidence kind and direction are incompatible')`, `ValueError('source rule SHA256 differs from source_rule_excerpt')`, `ValueError('source rule offsets must be ordered')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(self.exact_raw_excerpt.encode('utf-8')).hexdigest`, `sha256(self.source_rule_excerpt.encode('utf-8')).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _validate_exact_strings(self) -> PolicyEvidence:
        for value, label in (
            (self.evidence_id, "evidence ID"),
            (self.section_id, "evidence section ID"),
            (self.exact_raw_excerpt, "exact raw excerpt"),
            (self.source_rule_id, "source rule ID"),
            (self.source_rule_excerpt, "source rule excerpt"),
            (self.interpretation_note, "interpretation note"),
        ):
            _config_string(value, label)
        if sha256(self.exact_raw_excerpt.encode("utf-8")).hexdigest() != self.excerpt_sha256:
            raise ValueError("evidence excerpt SHA256 differs from exact_raw_excerpt")
        if self.excerpt_end <= self.excerpt_start:
            raise ValueError("evidence excerpt offsets must be ordered")
        if sha256(self.source_rule_excerpt.encode("utf-8")).hexdigest() != (
            self.source_rule_sha256
        ):
            raise ValueError("source rule SHA256 differs from source_rule_excerpt")
        if self.source_rule_end <= self.source_rule_start:
            raise ValueError("source rule offsets must be ordered")
        if not (
            self.source_rule_start <= self.excerpt_start
            and self.excerpt_end <= self.source_rule_end
        ):
            raise ValueError("evidence excerpt must lie inside its source rule")
        allowed_directions: dict[str, frozenset[str]] = {
            "USE_PERMISSION": frozenset(
                {"SUPPORTS_POTENTIAL_COMPATIBILITY", "CONTEXT_ONLY"}
            ),
            "USE_RESTRICTION": frozenset({"SUPPORTS_DIFFICULTY", "CONTEXT_ONLY"}),
            "PUBLIC_INTEREST_EXCEPTION": frozenset(
                {
                    "SUPPORTS_POTENTIAL_COMPATIBILITY",
                    "CONDITION",
                    "CONTEXT_ONLY",
                }
            ),
            "TECHNICAL_EQUIPMENT_RULE": frozenset(
                {
                    "SUPPORTS_POTENTIAL_COMPATIBILITY",
                    "SUPPORTS_DIFFICULTY",
                    "CONDITION",
                    "CONTEXT_ONLY",
                }
            ),
            "ICPE_RULE": frozenset(
                {
                    "SUPPORTS_POTENTIAL_COMPATIBILITY",
                    "SUPPORTS_DIFFICULTY",
                    "CONDITION",
                    "CONTEXT_ONLY",
                }
            ),
            "RISK_OR_NUISANCE_CONDITION": frozenset(
                {"SUPPORTS_DIFFICULTY", "CONDITION", "CONTEXT_ONLY"}
            ),
            "ACCESS_OR_NETWORK_CONDITION": frozenset(
                {"SUPPORTS_DIFFICULTY", "CONDITION", "CONTEXT_ONLY"}
            ),
            "OTHER_RELEVANT_RULE": frozenset(
                {"SUPPORTS_DIFFICULTY", "CONDITION", "CONTEXT_ONLY"}
            ),
        }
        allowed = allowed_directions[self.evidence_kind]
        if self.evidence_direction not in allowed:
            raise ValueError("evidence kind and direction are incompatible")
        return self
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `RouteAssessment._validate_route_shape`

**Exact signature**

```python
def _validate_route_shape(self) -> RouteAssessment:
```

**Purpose**

Rejects malformed or inconsistent route shape; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `RouteAssessment`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `len(set(combined)) != len(combined)`.
- Guard with a raise path: `(positive, condition, difficulty) != expected`.
- Guard with a raise path: `len(set(normalized)) != len(normalized)`.
- Explicit raise expressions: `ValueError('one evidence ID cannot occupy incompatible route roles')`, `ValueError(f'{role} evidence IDs must be unique within a route')`, `ValueError(f'{self.route_kind} has incompatible evidence-role membership')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `combined`.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _validate_route_shape(self) -> RouteAssessment:
        _config_string(self.route_id, "route ID")
        _config_string(self.applicability_note, "route applicability note")
        roles = {
            "positive": self.positive_evidence_ids,
            "condition": self.condition_evidence_ids,
            "difficulty": self.difficulty_evidence_ids,
        }
        combined: list[str] = []
        for role, values in roles.items():
            normalized = [_config_string(value, f"{role} evidence ID") for value in values]
            if len(set(normalized)) != len(normalized):
                raise ValueError(f"{role} evidence IDs must be unique within a route")
            combined.extend(normalized)
        if len(set(combined)) != len(combined):
            raise ValueError("one evidence ID cannot occupy incompatible route roles")
        positive = bool(self.positive_evidence_ids)
        condition = bool(self.condition_evidence_ids)
        difficulty = bool(self.difficulty_evidence_ids)
        expected = {
            "DIRECT_ROUTE": (True, False, False),
            "CONDITIONAL_ROUTE": (True, True, False),
            "RESTRICTION_EXCEPTION_ROUTE": (True, False, True),
            "DIFFICULTY_ONLY": (False, False, True),
        }[self.route_kind]
        if (positive, condition, difficulty) != expected:
            raise ValueError(
                f"{self.route_kind} has incompatible evidence-role membership"
            )
        return self
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_derived_chapter_status`

**Exact signature**

```python
def _derived_chapter_status(
    review_completeness: ReviewCompleteness,
    routes: Sequence[RouteAssessment],
) -> ChapterStatus:
```

**Purpose**

Private `planning` helper for derived chapter status; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `ChapterStatus`.
- Every observed return expression is reproduced without truncation:
```python
'UNKNOWN'

'UNKNOWN'

'CONDITIONAL_REVIEW'

'UNKNOWN' if 'DIFFICULTY_ONLY' in kinds else 'POTENTIALLY_COMPATIBLE'

'LIKELY_DIFFICULT'
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `kinds.intersection`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::ChapterPolicy._validate_evidence_semantics` via `_derived_chapter_status`.

**Complete source-ordered implementation**

```python
def _derived_chapter_status(
    review_completeness: ReviewCompleteness,
    routes: Sequence[RouteAssessment],
) -> ChapterStatus:
    if review_completeness == "INCOMPLETE":
        return "UNKNOWN"
    kinds = {route.route_kind for route in routes}
    if kinds.intersection({"CONDITIONAL_ROUTE", "RESTRICTION_EXCEPTION_ROUTE"}):
        return "CONDITIONAL_REVIEW"
    if "DIRECT_ROUTE" in kinds:
        return "UNKNOWN" if "DIFFICULTY_ONLY" in kinds else "POTENTIALLY_COMPATIBLE"
    if "DIFFICULTY_ONLY" in kinds:
        return "LIKELY_DIFFICULT"
    return "UNKNOWN"
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `ChapterPolicy._validate_evidence_semantics`

**Exact signature**

```python
def _validate_evidence_semantics(self) -> ChapterPolicy:
```

**Purpose**

Rejects malformed or inconsistent evidence semantics; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `ChapterPolicy`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `len(set(reviewed)) != len(reviewed)`.
- Guard with a raise path: `self.review_completeness == 'INCOMPLETE' and (self.zoning_precheck_status != 'UNKNOWN' or self.zoning_precheck_confidence != 'LOW')`.
- Guard with a raise path: `len(set(route_ids)) != len(route_ids)`.
- Guard with a raise path: `self.zoning_precheck_status != expected_status`.
- Explicit raise expressions: `ValueError('declared chapter status differs from coherent linked route assessments')`, `ValueError('incomplete review requires UNKNOWN / LOW')`, `ValueError('reviewed section IDs must be unique')`, `ValueError('route IDs must be unique within a chapter')`.

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

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _validate_evidence_semantics(self) -> ChapterPolicy:
        _config_string(self.resolved_zone_chapter_label, "chapter label")
        _config_string(self.review_note, "chapter review note")
        _config_string(self.rationale, "chapter rationale")
        _config_string(self.missing_information, "chapter missing information")
        reviewed = [
            _config_string(value, "reviewed section ID")
            for value in self.reviewed_section_ids
        ]
        if len(set(reviewed)) != len(reviewed):
            raise ValueError("reviewed section IDs must be unique")
        if self.review_completeness == "INCOMPLETE" and (
            self.zoning_precheck_status != "UNKNOWN"
            or self.zoning_precheck_confidence != "LOW"
        ):
            raise ValueError("incomplete review requires UNKNOWN / LOW")
        route_ids = [route.route_id for route in self.route_assessments]
        if len(set(route_ids)) != len(route_ids):
            raise ValueError("route IDs must be unique within a chapter")
        expected_status = _derived_chapter_status(
            self.review_completeness,
            self.route_assessments,
        )
        if self.zoning_precheck_status != expected_status:
            raise ValueError(
                "declared chapter status differs from coherent linked route assessments"
            )
        return self
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessZoningPolicyConfig._validate_policy`

**Exact signature**

```python
def _validate_policy(self) -> BessZoningPolicyConfig:
```

**Purpose**

Rejects malformed or inconsistent policy; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessZoningPolicyConfig`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `self.schema_version != POLICY_SCHEMA_VERSION`.
- Guard with a raise path: `len(set(article_numbers)) != len(article_numbers)`.
- Guard with a raise path: `len(set(labels)) != len(labels)`.
- Guard with a raise path: `evidence.evidence_id in evidence_ids`.
- Guard with a raise path: `previous is not None`.
- Guard with a raise path: `prior_rule is not None and prior_rule != rule_identity`.
- Guard with a raise path: `prior_rule_id is not None and prior_rule_id != evidence.source_rule_id`.
- Guard with a raise path: `route.route_id in route_ids`.
- Guard with a raise path: `evidence.evidence_direction == 'CONTEXT_ONLY' and is_linked`.
- Guard with a raise path: `evidence.evidence_direction != 'CONTEXT_ONLY' and (not is_linked)`.
- Guard with a raise path: `overlaps and (not identical)`.
- Guard with a raise path: `referenced_evidence is None`.
- Guard with a raise path: `referenced_evidence.evidence_direction != expected_direction`.
- Explicit raise expressions: `ValueError('CONTEXT_ONLY evidence must not be linked to a route')`, `ValueError('chapter policy labels must be unique')`, `ValueError('decision evidence must be linked to at least one route')`, `ValueError('evidence IDs must be globally unique')`, `ValueError('one chapter-scoped evidence occurrence must resolve to exactly one evidence ID, kind, and direction')`, `ValueError('one exact source-rule occurrence must use one source rule ID')`, `ValueError('one source rule ID must resolve to one exact occurrence')`, `ValueError('required zone article numbers must be unique')`, `ValueError('route IDs must be globally unique')`, `ValueError(f'route assigns evidence ID {evidence_id!r} to an incompatible {role} role')`, `ValueError(f'route references unknown or another-chapter evidence ID {evidence_id!r}')`, `ValueError(f'source rule {evidence.source_rule_id!r} partially overlaps {rule_id!r}')`, `ValueError(f'unsupported BESS zoning policy schema: {self.schema_version}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `chapter_occurrences[key]`, `evidence_ids`, `linked_evidence_ids`, `ranges`, `route_ids`, `source_rule_occurrences[occurrence]`, `source_rule_ranges`, `source_rules[evidence.source_rule_id]`.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _validate_policy(self) -> BessZoningPolicyConfig:
        if self.schema_version != POLICY_SCHEMA_VERSION:
            raise ValueError(f"unsupported BESS zoning policy schema: {self.schema_version}")
        _config_string(self.policy_profile, "policy profile")
        _config_string(self.source_lock.document_id, "policy document ID")
        _config_string(self.source_lock.structure_profile, "policy structure profile")
        article_numbers = [
            _config_string(value, "required zone article number")
            for value in self.required_zone_article_numbers
        ]
        if len(set(article_numbers)) != len(article_numbers):
            raise ValueError("required zone article numbers must be unique")
        labels = [chapter.resolved_zone_chapter_label for chapter in self.chapters]
        if len(set(labels)) != len(labels):
            raise ValueError("chapter policy labels must be unique")
        evidence_ids: set[str] = set()
        route_ids: set[str] = set()
        chapter_occurrences: dict[
            tuple[str, str, int, str, int, int], tuple[str, str, str]
        ] = {}
        source_rules: dict[str, tuple[object, ...]] = {}
        source_rule_occurrences: dict[tuple[object, ...], str] = {}
        source_rule_ranges: dict[tuple[str, int, str], list[tuple[int, int, str]]] = {}
        for chapter in self.chapters:
            chapter_evidence = {
                evidence.evidence_id: evidence for evidence in chapter.evidence
            }
            linked_evidence_ids: set[str] = set()
            for evidence in chapter.evidence:
                if evidence.evidence_id in evidence_ids:
                    raise ValueError("evidence IDs must be globally unique")
                evidence_ids.add(evidence.evidence_id)
                key = (
                    chapter.resolved_zone_chapter_label,
                    evidence.section_id,
                    evidence.page_number,
                    evidence.section_page_fragment_sha256,
                    evidence.excerpt_start,
                    evidence.excerpt_end,
                )
                previous = chapter_occurrences.get(key)
                if previous is not None:
                    raise ValueError(
                        "one chapter-scoped evidence occurrence must resolve to exactly one evidence ID, kind, and direction"
                    )
                chapter_occurrences[key] = (
                    evidence.evidence_id,
                    evidence.evidence_kind,
                    evidence.evidence_direction,
                )
                rule_identity = (
                    evidence.section_id,
                    evidence.page_number,
                    evidence.section_page_fragment_sha256,
                    evidence.source_rule_start,
                    evidence.source_rule_end,
                    evidence.source_rule_sha256,
                    evidence.source_rule_excerpt,
                )
                prior_rule = source_rules.get(evidence.source_rule_id)
                if prior_rule is not None and prior_rule != rule_identity:
                    raise ValueError(
                        "one source rule ID must resolve to one exact occurrence"
                    )
                source_rules[evidence.source_rule_id] = rule_identity
                occurrence = rule_identity[:5]
                prior_rule_id = source_rule_occurrences.get(occurrence)
                if prior_rule_id is not None and prior_rule_id != evidence.source_rule_id:
                    raise ValueError(
                        "one exact source-rule occurrence must use one source rule ID"
                    )
                source_rule_occurrences[occurrence] = evidence.source_rule_id
                range_key = (
                    evidence.section_id,
                    evidence.page_number,
                    evidence.section_page_fragment_sha256,
                )
                ranges = source_rule_ranges.setdefault(range_key, [])
                current = (
                    evidence.source_rule_start,
                    evidence.source_rule_end,
                    evidence.source_rule_id,
                )
                for start, end, rule_id in ranges:
                    overlaps = max(start, current[0]) < min(end, current[1])
                    identical = start == current[0] and end == current[1]
                    if overlaps and not identical:
                        raise ValueError(
                            f"source rule {evidence.source_rule_id!r} partially overlaps {rule_id!r}"
                        )
                if current not in ranges:
                    ranges.append(current)
            for route in chapter.route_assessments:
                if route.route_id in route_ids:
                    raise ValueError("route IDs must be globally unique")
                route_ids.add(route.route_id)
                roles = (
                    (
                        route.positive_evidence_ids,
                        "SUPPORTS_POTENTIAL_COMPATIBILITY",
                        "positive",
                    ),
                    (route.condition_evidence_ids, "CONDITION", "condition"),
                    (
                        route.difficulty_evidence_ids,
                        "SUPPORTS_DIFFICULTY",
                        "difficulty",
                    ),
                )
                for identifiers, expected_direction, role in roles:
                    for evidence_id in identifiers:
                        referenced_evidence = chapter_evidence.get(evidence_id)
                        if referenced_evidence is None:
                            raise ValueError(
                                f"route references unknown or another-chapter evidence ID {evidence_id!r}"
                            )
                        if referenced_evidence.evidence_direction != expected_direction:
                            raise ValueError(
                                f"route assigns evidence ID {evidence_id!r} to an incompatible {role} role"
                            )
                        linked_evidence_ids.add(evidence_id)
            for evidence in chapter.evidence:
                is_linked = evidence.evidence_id in linked_evidence_ids
                if evidence.evidence_direction == "CONTEXT_ONLY" and is_linked:
                    raise ValueError("CONTEXT_ONLY evidence must not be linked to a route")
                if evidence.evidence_direction != "CONTEXT_ONLY" and not is_linked:
                    raise ValueError(
                        "decision evidence must be linked to at least one route"
                    )
        return self
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_construct_unique_mapping`

**Exact signature**

```python
def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
```

**Purpose**

Private `planning` helper for construct unique mapping; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[object, object]`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `key in result`.
- Explicit raise expressions: `BessZoningPrecheckError(f'Duplicate YAML policy key: {key!r}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `result[key]`.
- Input mutation: none.

**Repository interfaces and consumers**

- function object argument: `src/landscout/stages/interpret_bess_zoning.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.

**Complete source-ordered implementation**

```python
def _construct_unique_mapping(
    loader: yaml.SafeLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
    result: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise BessZoningPrecheckError(f"Duplicate YAML policy key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_config_string`

**Exact signature**

```python
def _config_string(value: str, label: str) -> str:
```

**Purpose**

Private `planning` helper for config string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not value or value != value.strip()`.
- Explicit raise expressions: `ValueError(f'{label} must be a non-empty exact string')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::PolicyEvidence._validate_exact_strings` via `_config_string`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::RouteAssessment._validate_route_shape` via `_config_string`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::ChapterPolicy._validate_evidence_semantics` via `_config_string`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::BessZoningPolicyConfig._validate_policy` via `_config_string`.

**Complete source-ordered implementation**

```python
def _config_string(value: str, label: str) -> str:
    if not value or value != value.strip():
        raise ValueError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_bess_zoning_policy_config`

**Exact signature**

```python
def load_bess_zoning_policy_config(path: str | Path) -> BessZoningPolicyConfig:
```

**Purpose**

Load a strict policy while rejecting duplicate YAML keys.

**Return contract**

- Declared return annotation: `BessZoningPolicyConfig`.
- Every observed return expression is reproduced without truncation:
```python
BessZoningPolicyConfig.model_validate(payload)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(payload, Mapping)`.
- Explicit raise expressions: `BessZoningPrecheckError('BESS zoning policy is invalid')`, `BessZoningPrecheckError('BESS zoning policy must be a mapping')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: `Path(path).read_text`.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`.
- import: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.interpret_bess_zoning import (
    CHAPTER_POLICY_COLUMNS,
    EVIDENCE_CATALOG_COLUMNS,
    EVIDENCE_ROUTE_LINK_COLUMNS,
    PARCEL_ZONE_POLICY_COLUMNS,
    ROUTE_ASSESSMENT_COLUMNS,
    SOURCE_ZONE_POLICY_COLUMNS,
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    _result_with_hashes,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_resolved_policy` via `load_bess_zoning_policy_config`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_duplicate_yaml_key_is_rejected` via `load_bess_zoning_policy_config`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_real_muret_source_rules_preserve_conditional_and_exception_frames` via `load_bess_zoning_policy_config`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_real_muret_up_route_does_not_use_the_separate_icpe_condition` via `load_bess_zoning_policy_config`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite` via `load_bess_zoning_policy_config`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_real_muret_up_and_aup_keep_icpe_applicability_as_context` via `load_bess_zoning_policy_config`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_policy_yaml_roundtrip_is_strict` via `load_bess_zoning_policy_config`.

**Complete source-ordered implementation**

```python
def load_bess_zoning_policy_config(path: str | Path) -> BessZoningPolicyConfig:
    """Load a strict policy while rejecting duplicate YAML keys."""

    try:
        payload = yaml.load(Path(path).read_text(encoding="utf-8"), Loader=_UniqueKeyLoader)
        if not isinstance(payload, Mapping):
            raise BessZoningPrecheckError("BESS zoning policy must be a mapping")
        return BessZoningPolicyConfig.model_validate(payload)
    except BessZoningPrecheckError:
        raise
    except Exception as error:
        raise BessZoningPrecheckError("BESS zoning policy is invalid") from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_string`

**Exact signature**

```python
def _strict_string(value: object, label: str) -> str:
```

**Purpose**

Private `planning` helper for strict string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
value
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or not value or value != value.strip()`.
- Explicit raise expressions: `BessZoningPrecheckError(f'{label} must be a non-empty exact string')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validated_sha256` via `_strict_string`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_exact_id_series` via `_strict_string`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_zones` via `_strict_string`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_relations` via `_strict_string`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_zone_chapter_rows` via `_strict_string`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_evidence` via `_strict_string`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_mapping` via `_strict_string`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_chapter_policy` via `_strict_string`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_source_zone_policy` via `_strict_string`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_parcel_output` via `_strict_string`.

**Complete source-ordered implementation**

```python
def _strict_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise BessZoningPrecheckError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_nonnegative_integer`

**Exact signature**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

**Purpose**

Private `planning` helper for strict nonnegative integer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `int`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Integral)`.
- Guard with a raise path: `result < 0`.
- Explicit raise expressions: `BessZoningPrecheckError(f'{label} must be an integer')`, `BessZoningPrecheckError(f'{label} must be non-negative')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_strict_positive_integer` via `_strict_nonnegative_integer`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_parcels` via `_strict_nonnegative_integer`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_strict_nonnegative_integer`.

**Complete source-ordered implementation**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise BessZoningPrecheckError(f"{label} must be an integer")
    result = int(value)
    if result < 0:
        raise BessZoningPrecheckError(f"{label} must be non-negative")
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_positive_integer`

**Exact signature**

```python
def _strict_positive_integer(value: object, label: str) -> int:
```

**Purpose**

Private `planning` helper for strict positive integer; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `int`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `result < 1`.
- Explicit raise expressions: `BessZoningPrecheckError(f'{label} must be positive')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_evidence` via `_strict_positive_integer`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_strict_positive_integer`.

**Complete source-ordered implementation**

```python
def _strict_positive_integer(value: object, label: str) -> int:
    result = _strict_nonnegative_integer(value, label)
    if result < 1:
        raise BessZoningPrecheckError(f"{label} must be positive")
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_sha256`

**Exact signature**

```python
def _validated_sha256(value: object, label: str) -> str:
```

**Purpose**

Checks and returns canonical sha256; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
checksum
```

**Validation and exceptions**

- Guard with a raise path: `re.fullmatch('[0-9a-f]{64}', checksum) is None`.
- Explicit raise expressions: `BessZoningPrecheckError(f'{label} must be exactly 64 lowercase hexadecimal characters')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_validated_sha256`.

**Complete source-ordered implementation**

```python
def _validated_sha256(value: object, label: str) -> str:
    checksum = _strict_string(value, label)
    if re.fullmatch(r"[0-9a-f]{64}", checksum) is None:
        raise BessZoningPrecheckError(
            f"{label} must be exactly 64 lowercase hexadecimal characters"
        )
    return checksum
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_strict_nonnegative_number`

**Exact signature**

```python
def _strict_nonnegative_number(value: object, label: str) -> float:
```

**Purpose**

Private `planning` helper for strict nonnegative number; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `float`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, bool) or not isinstance(value, Real)`.
- Guard with a raise path: `not math.isfinite(result) or result < 0`.
- Explicit raise expressions: `BessZoningPrecheckError(f'{label} must be finite and non-negative')`, `BessZoningPrecheckError(f'{label} must be finite')`, `BessZoningPrecheckError(f'{label} must be numeric')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_relations` via `_strict_nonnegative_number`.

**Complete source-ordered implementation**

```python
def _strict_nonnegative_number(value: object, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise BessZoningPrecheckError(f"{label} must be numeric")
    try:
        result = float(value)
    except (TypeError, ValueError, OverflowError) as error:
        raise BessZoningPrecheckError(f"{label} must be finite") from error
    if not math.isfinite(result) or result < 0:
        raise BessZoningPrecheckError(f"{label} must be finite and non-negative")
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_value`

**Exact signature**

```python
def _canonical_value(value: object) -> object:
```

**Purpose**

Private `planning` helper for canonical value; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `object`.
- Every observed return expression is reproduced without truncation:
```python
None

_canonical_value(value.item())

to_wkb(value, hex=True, include_srid=False)

value.isoformat()

value.hex()

[_canonical_value(item) for item in value]

{str(key): _canonical_value(item) for key, item in value.items()}

None

value
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessZoningPrecheckError(f'Value of type {type(value).__name__} cannot be canonically serialized')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_canonical_sha256` via `_canonical_value`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_frame_payload` via `_canonical_value`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_compare_frames` via `_canonical_value`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_canonical_value`.

**Complete source-ordered implementation**

```python
def _canonical_value(value: object) -> object:
    if value is None or value is pd.NA:
        return None
    if isinstance(value, np.generic):
        return _canonical_value(value.item())
    if isinstance(value, BaseGeometry):
        return to_wkb(value, hex=True, include_srid=False)
    if isinstance(value, (pd.Timestamp, datetime, date)):
        return value.isoformat()
    if isinstance(value, bytes):
        return value.hex()
    if isinstance(value, (tuple, list, np.ndarray)):
        return [_canonical_value(item) for item in value]
    if isinstance(value, Mapping):
        return {str(key): _canonical_value(item) for key, item in value.items()}
    if isinstance(value, float) and math.isnan(value):
        return None
    if isinstance(value, (str, int, float, bool)):
        return value
    raise BessZoningPrecheckError(
        f"Value of type {type(value).__name__} cannot be canonically serialized"
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_sha256`

**Exact signature**

```python
def _canonical_sha256(value: object) -> str:
```

**Purpose**

Private `planning` helper for canonical sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
sha256(serialized).hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessZoningPrecheckError('Canonical integrity serialization failed')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(serialized).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_frame_sha256` via `_canonical_sha256`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_policy_sha256` via `_canonical_sha256`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_factual_structure_sha256` via `_canonical_sha256`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_zone_mapping_input_sha256` via `_canonical_sha256`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_result_frame_sha256` via `_canonical_sha256`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_complete_result_sha256` via `_canonical_sha256`.

**Complete source-ordered implementation**

```python
def _canonical_sha256(value: object) -> str:
    try:
        serialized = json.dumps(
            _canonical_value(value),
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except BessZoningPrecheckError:
        raise
    except Exception as error:
        raise BessZoningPrecheckError("Canonical integrity serialization failed") from error
    return sha256(serialized).hexdigest()
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_frame_payload`

**Exact signature**

```python
def _frame_payload(frame: pd.DataFrame, columns: Sequence[str]) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for frame payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
payload
```

**Validation and exceptions**

- Guard with a raise path: `frame.columns.has_duplicates`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `isinstance(frame, gpd.GeoDataFrame)`.
- Guard with a raise path: `frame.crs is None`.
- Explicit raise expressions: `BessZoningPrecheckError('DataFrame columns must be unique')`, `BessZoningPrecheckError('DataFrame integrity serialization failed')`, `BessZoningPrecheckError('GeoDataFrame CRS is required')`, `BessZoningPrecheckError(f'DataFrame is missing columns: {missing}')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `payload['crs']`, `payload['geometry_column']`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_frame_sha256` via `_frame_payload`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_zone_mapping_input_sha256` via `_frame_payload`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_result_frame_sha256` via `_frame_payload`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_compare_frames` via `_frame_payload`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_frame_payload`.

**Complete source-ordered implementation**

```python
def _frame_payload(frame: pd.DataFrame, columns: Sequence[str]) -> dict[str, object]:
    try:
        if frame.columns.has_duplicates:
            raise BessZoningPrecheckError("DataFrame columns must be unique")
        missing = [column for column in columns if column not in frame.columns]
        if missing:
            raise BessZoningPrecheckError(f"DataFrame is missing columns: {missing}")
        payload: dict[str, object] = {
            "columns": list(columns),
            "index_names": list(frame.index.names),
            "index": [_canonical_value(value) for value in frame.index.tolist()],
            "rows": frame.loc[:, columns].to_dict("records"),
        }
        if isinstance(frame, gpd.GeoDataFrame):
            if frame.crs is None:
                raise BessZoningPrecheckError("GeoDataFrame CRS is required")
            payload["crs"] = CRS.from_user_input(frame.crs).to_json_dict()
            payload["geometry_column"] = frame.geometry.name
        return payload
    except BessZoningPrecheckError:
        raise
    except Exception as error:
        raise BessZoningPrecheckError("DataFrame integrity serialization failed") from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_frame_sha256`

**Exact signature**

```python
def _frame_sha256(domain: str, frame: pd.DataFrame, columns: Sequence[str]) -> str:
```

**Purpose**

Private `planning` helper for frame sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': domain, **_frame_payload(frame, columns)})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_frame_sha256`.

**Complete source-ordered implementation**

```python
def _frame_sha256(domain: str, frame: pd.DataFrame, columns: Sequence[str]) -> str:
    return _canonical_sha256({"domain": domain, **_frame_payload(frame, columns)})
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_sha256`

**Exact signature**

```python
def _policy_sha256(config: BessZoningPolicyConfig) -> str:
```

**Purpose**

Private `planning` helper for policy sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': 'landscout.bess_zoning.policy_config', 'config': config.model_dump(mode='json')})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_policy_sha256`.

**Complete source-ordered implementation**

```python
def _policy_sha256(config: BessZoningPolicyConfig) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.bess_zoning.policy_config",
            "config": config.model_dump(mode="json"),
        }
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_factual_structure_sha256`

**Exact signature**

```python
def _factual_structure_sha256(
    structure: PlanningRegulationStructureResult,
) -> str:
```

**Purpose**

Private `planning` helper for factual structure sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': 'landscout.bess_zoning.factual_structure_input', 'structure_result_content_sha256': structure.structure_result_content_sha256, 'section_hash_schema_version': structure.section_hash_schema_version, 'structure_config_sha256': structure.structure_config_sha256, 'sections_content_sha256': structure.sections_content_sha256, 'zone_map_content_sha256': structure.zone_map_content_sha256, 'topic_evidence_content_sha256': structure.topic_evidence_content_sha256})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_factual_structure_sha256`.

**Complete source-ordered implementation**

```python
def _factual_structure_sha256(
    structure: PlanningRegulationStructureResult,
) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.bess_zoning.factual_structure_input",
            "structure_result_content_sha256": structure.structure_result_content_sha256,
            "section_hash_schema_version": structure.section_hash_schema_version,
            "structure_config_sha256": structure.structure_config_sha256,
            "sections_content_sha256": structure.sections_content_sha256,
            "zone_map_content_sha256": structure.zone_map_content_sha256,
            "topic_evidence_content_sha256": structure.topic_evidence_content_sha256,
        }
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_resolved_policy`

**Exact signature**

```python
def _resolved_policy(
    policy: BessZoningPolicyConfig | str | Path,
) -> BessZoningPolicyConfig:
```

**Purpose**

Private `planning` helper for resolved policy; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessZoningPolicyConfig`.
- Every observed return expression is reproduced without truncation:
```python
load_bess_zoning_policy_config(policy)

BessZoningPolicyConfig.model_validate(policy.model_dump(mode='python'))
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(policy, BessZoningPolicyConfig)`.
- Explicit raise expressions: `BessZoningPrecheckError('BESS zoning policy is invalid')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::validate_bess_zoning_precheck` via `_resolved_policy`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::interpret_bess_zoning` via `_resolved_policy`.

**Complete source-ordered implementation**

```python
def _resolved_policy(
    policy: BessZoningPolicyConfig | str | Path,
) -> BessZoningPolicyConfig:
    if isinstance(policy, BessZoningPolicyConfig):
        try:
            return BessZoningPolicyConfig.model_validate(
                policy.model_dump(mode="python")
            )
        except Exception as error:
            raise BessZoningPrecheckError("BESS zoning policy is invalid") from error
    return load_bess_zoning_policy_config(policy)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_policy_lock`

**Exact signature**

```python
def _validate_policy_lock(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent policy lock; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `actual != expected`.
- Explicit raise expressions: `BessZoningPrecheckError(f'BESS zoning policy {label} differs from factual source')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_validate_policy_lock`.

**Complete source-ordered implementation**

```python
def _validate_policy_lock(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> None:
    lock = policy.source_lock
    comparisons = (
        (lock.document_id, index.document_id, "document ID"),
        (lock.archive_sha256, index.archive_sha256, "archive SHA256"),
        (lock.pdf_sha256, index.pdf_sha256, "PDF SHA256"),
        (lock.index_content_sha256, index.index_content_sha256, "index SHA256"),
        (
            lock.structure_result_content_sha256,
            structure.structure_result_content_sha256,
            "structure result SHA256",
        ),
        (lock.structure_profile, structure.structure_profile, "structure profile"),
    )
    for actual, expected, label in comparisons:
        if actual != expected:
            raise BessZoningPrecheckError(
                f"BESS zoning policy {label} differs from factual source"
            )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_exact_id_series`

**Exact signature**

```python
def _exact_id_series(series: pd.Series, label: str, *, unique: bool) -> tuple[str, ...]:
```

**Purpose**

Private `planning` helper for exact id series; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `tuple[str, ...]`.
- Every observed return expression is reproduced without truncation:
```python
tuple(values)
```

**Validation and exceptions**

- Guard with a raise path: `unique and len(set(values)) != len(values)`.
- Explicit raise expressions: `BessZoningPrecheckError(f'{label} values must be unique')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `values`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_parcels` via `_exact_id_series`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_zones` via `_exact_id_series`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_relations` via `_exact_id_series`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_mapping` via `_exact_id_series`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_exact_id_series`.

**Complete source-ordered implementation**

```python
def _exact_id_series(series: pd.Series, label: str, *, unique: bool) -> tuple[str, ...]:
    values: list[str] = []
    for value in series.tolist():
        values.append(_strict_string(value, label))
    if unique and len(set(values)) != len(values):
        raise BessZoningPrecheckError(f"{label} values must be unique")
    return tuple(values)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_parcels`

**Exact signature**

```python
def _validate_parcels(
    index: PlanningRegulationIndex,
    parcels: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
```

**Purpose**

Rejects malformed or inconsistent parcels; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
parcels.copy(deep=True)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(parcels, gpd.GeoDataFrame)`.
- Guard with a raise path: `parcels.columns.has_duplicates`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `collisions`.
- Guard with a raise path: `parcels.crs is None`.
- Guard with a raise path: `geometry.isna().any() or geometry.is_empty.any() or (~geometry.is_valid).any()`.
- Guard with a raise path: `not geometry.geom_type.isin({'Polygon', 'MultiPolygon'}).all()`.
- Guard with a raise path: `parcels.geometry.name != 'geometry'`.
- Guard with a raise path: `not parcels[document_column].eq(index.document_id).all()`.
- Guard with a raise path: `not parcels[archive_column].eq(index.archive_sha256).all()`.
- Explicit raise expressions: `BessZoningPrecheckError('Parcel CRS is required')`, `BessZoningPrecheckError('Parcel CRS or geometry is invalid')`, `BessZoningPrecheckError('Parcel columns must be unique')`, `BessZoningPrecheckError('Parcel geometry must be Polygon or MultiPolygon')`, `BessZoningPrecheckError('Parcel geometry must be active')`, `BessZoningPrecheckError('Parcel geometry must be non-null, non-empty, and valid')`, `BessZoningPrecheckError('parcels must be a GeoDataFrame')`, `BessZoningPrecheckError(f'Parcel input already contains precheck columns: {collisions}')`, `BessZoningPrecheckError(f'Parcel input is missing columns: {missing}')`, `BessZoningPrecheckError(f'Parcel {archive_column} lineage differs from the regulation')`, `BessZoningPrecheckError(f'Parcel {document_column} lineage differs from the regulation')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `(~geometry.is_valid).any`, `geometry.geom_type.isin`, `geometry.geom_type.isin({'Polygon', 'MultiPolygon'}).all`, `geometry.is_empty.any`, `geometry.isna`, `geometry.isna().any`, `set(PARCEL_PRECHECK_COLUMNS).intersection`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_validate_parcels`.

**Complete source-ordered implementation**

```python
def _validate_parcels(
    index: PlanningRegulationIndex,
    parcels: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
    if not isinstance(parcels, gpd.GeoDataFrame):
        raise BessZoningPrecheckError("parcels must be a GeoDataFrame")
    if parcels.columns.has_duplicates:
        raise BessZoningPrecheckError("Parcel columns must be unique")
    required = {
        "parcel_id",
        "geometry",
        "dominant_planning_zone_id",
        "planning_surface_relation_count",
        "prescription_surface_relation_count",
        "information_surface_relation_count",
        "planning_line_relation_count",
        "planning_point_relation_count",
        "planning_feature_document_id",
        "planning_feature_archive_sha256",
        "planning_document_id",
        "planning_archive_sha256",
    }
    missing = sorted(required.difference(parcels.columns))
    if missing:
        raise BessZoningPrecheckError(f"Parcel input is missing columns: {missing}")
    collisions = sorted(set(PARCEL_PRECHECK_COLUMNS).intersection(parcels.columns))
    if collisions:
        raise BessZoningPrecheckError(
            f"Parcel input already contains precheck columns: {collisions}"
        )
    if parcels.crs is None:
        raise BessZoningPrecheckError("Parcel CRS is required")
    try:
        CRS.from_user_input(parcels.crs)
        if parcels.geometry.name != "geometry":
            raise BessZoningPrecheckError("Parcel geometry must be active")
    except BessZoningPrecheckError:
        raise
    except Exception as error:
        raise BessZoningPrecheckError("Parcel CRS or geometry is invalid") from error
    _exact_id_series(parcels["parcel_id"], "parcel ID", unique=True)
    geometry = parcels.geometry
    if geometry.isna().any() or geometry.is_empty.any() or (~geometry.is_valid).any():
        raise BessZoningPrecheckError(
            "Parcel geometry must be non-null, non-empty, and valid"
        )
    if not geometry.geom_type.isin({"Polygon", "MultiPolygon"}).all():
        raise BessZoningPrecheckError("Parcel geometry must be Polygon or MultiPolygon")
    for column in (
        "planning_surface_relation_count",
        "prescription_surface_relation_count",
        "information_surface_relation_count",
        "planning_line_relation_count",
        "planning_point_relation_count",
    ):
        for value in parcels[column].tolist():
            _strict_nonnegative_integer(value, column)
    for document_column in ("planning_document_id", "planning_feature_document_id"):
        if not parcels[document_column].eq(index.document_id).all():
            raise BessZoningPrecheckError(
                f"Parcel {document_column} lineage differs from the regulation"
            )
    for archive_column in (
        "planning_archive_sha256",
        "planning_feature_archive_sha256",
    ):
        if not parcels[archive_column].eq(index.archive_sha256).all():
            raise BessZoningPrecheckError(
                f"Parcel {archive_column} lineage differs from the regulation"
            )
    return parcels.copy(deep=True)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_zones`

**Exact signature**

```python
def _validate_zones(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
) -> pd.DataFrame:
```

**Purpose**

Rejects malformed or inconsistent zones; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(zones, pd.DataFrame) or zones.columns.has_duplicates`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `not result['source_document_id'].eq(index.document_id).all()`.
- Guard with a raise path: `not result['source_archive_sha256'].eq(index.archive_sha256).all()`.
- Explicit raise expressions: `BessZoningPrecheckError('Zone catalog archive lineage differs')`, `BessZoningPrecheckError('Zone catalog document lineage differs')`, `BessZoningPrecheckError('zones must be a DataFrame with unique columns')`, `BessZoningPrecheckError(f'Zone catalog is missing columns: {missing}')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_validate_zones`.

**Complete source-ordered implementation**

```python
def _validate_zones(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
) -> pd.DataFrame:
    if not isinstance(zones, pd.DataFrame) or zones.columns.has_duplicates:
        raise BessZoningPrecheckError("zones must be a DataFrame with unique columns")
    required = (
        "planning_zone_id",
        "source_zone_id",
        "zone_label_raw",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
    )
    missing = [column for column in required if column not in zones.columns]
    if missing:
        raise BessZoningPrecheckError(f"Zone catalog is missing columns: {missing}")
    result = zones.copy(deep=True)
    _exact_id_series(result["planning_zone_id"], "planning zone ID", unique=True)
    _exact_id_series(result["source_zone_id"], "source zone ID", unique=True)
    _exact_id_series(result["zone_label_raw"], "raw zone label", unique=False)
    if not result["source_document_id"].eq(index.document_id).all():
        raise BessZoningPrecheckError("Zone catalog document lineage differs")
    if not result["source_archive_sha256"].eq(index.archive_sha256).all():
        raise BessZoningPrecheckError("Zone catalog archive lineage differs")
    for value in result["source_layer"].tolist():
        _strict_string(value, "zone source layer")
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_relations`

**Exact signature**

```python
def _validate_relations(
    index: PlanningRegulationIndex,
    parcels: gpd.GeoDataFrame,
    zones: pd.DataFrame,
    relations: pd.DataFrame,
) -> pd.DataFrame:
```

**Purpose**

Rejects malformed or inconsistent relations; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(relations, pd.DataFrame) or relations.columns.has_duplicates`.
- Guard with a raise path: `missing`.
- Guard with a raise path: `result.duplicated(['parcel_id', 'planning_zone_id']).any()`.
- Guard with a raise path: `not set(_exact_id_series(result['parcel_id'], 'relation parcel ID', unique=False)).issubset(parcel_ids)`.
- Guard with a raise path: `expected_zone is None`.
- Guard with a raise path: `source_id != expected_zone['source_zone_id'] or label != expected_zone['zone_label_raw']`.
- Guard with a raise path: `row['source_layer'] != expected_zone['source_layer']`.
- Guard with a raise path: `relation_type == 'AREA_OVERLAP' and area <= 0`.
- Guard with a raise path: `relation_type == 'TOUCH_ONLY' and area != 0`.
- Guard with a raise path: `relation_type not in {'AREA_OVERLAP', 'TOUCH_ONLY'}`.
- Guard with a raise path: `row['source_document_id'] != index.document_id`.
- Guard with a raise path: `row['source_archive_sha256'] != index.archive_sha256`.
- Guard with a raise path: `upper <= 0`.
- Guard with a raise path: `area - upper > technical_overlay_tolerance(upper)`.
- Guard with a raise path: `reference_area <= 0`.
- Guard with a raise path: `abs(percentage_area - area) > technical_overlay_tolerance(reference_area)`.
- Explicit raise expressions: `BessZoningPrecheckError('AREA_OVERLAP requires positive area')`, `BessZoningPrecheckError('Parcel/zone relations must be unique')`, `BessZoningPrecheckError('TOUCH_ONLY requires zero area')`, `BessZoningPrecheckError('Zoning relation archive lineage differs')`, `BessZoningPrecheckError('Zoning relation document lineage differs')`, `BessZoningPrecheckError('Zoning relation references an unknown parcel')`, `BessZoningPrecheckError('Zoning relation references an unknown zone')`, `BessZoningPrecheckError('Zoning relation source layer is inconsistent')`, `BessZoningPrecheckError('Zoning relation type is invalid')`, `BessZoningPrecheckError('Zoning relation zone identity is inconsistent')`, `BessZoningPrecheckError('zoning_intersections must be a DataFrame with unique columns')`, `BessZoningPrecheckError(f'Intersection area exceeds {upper_column}')`, `BessZoningPrecheckError(f'Zoning relations are missing columns: {missing}')`, `BessZoningPrecheckError(f'{area_column} must be positive for a zoning relation')`, `BessZoningPrecheckError(f'{percentage_column} is inconsistent with factual areas')`, `BessZoningPrecheckError(f'{upper_column} must be positive for a zoning relation')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_validate_relations`.

**Complete source-ordered implementation**

```python
def _validate_relations(
    index: PlanningRegulationIndex,
    parcels: gpd.GeoDataFrame,
    zones: pd.DataFrame,
    relations: pd.DataFrame,
) -> pd.DataFrame:
    if not isinstance(relations, pd.DataFrame) or relations.columns.has_duplicates:
        raise BessZoningPrecheckError(
            "zoning_intersections must be a DataFrame with unique columns"
        )
    required = (
        "parcel_id",
        "planning_zone_id",
        "source_zone_id",
        "zone_label_raw",
        "relation_type",
        "intersection_area_m2",
        "parcel_metric_area_m2",
        "zone_area_m2",
        "parcel_share_pct",
        "zone_share_pct",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
    )
    missing = [column for column in required if column not in relations.columns]
    if missing:
        raise BessZoningPrecheckError(f"Zoning relations are missing columns: {missing}")
    result = relations.copy(deep=True)
    if result.duplicated(["parcel_id", "planning_zone_id"]).any():
        raise BessZoningPrecheckError("Parcel/zone relations must be unique")
    parcel_ids = set(_exact_id_series(parcels["parcel_id"], "parcel ID", unique=True))
    if not set(_exact_id_series(result["parcel_id"], "relation parcel ID", unique=False)).issubset(parcel_ids):
        raise BessZoningPrecheckError("Zoning relation references an unknown parcel")
    zone_records = zones.set_index("planning_zone_id")[
        ["source_zone_id", "zone_label_raw", "source_layer"]
    ].to_dict("index")
    for row in result.to_dict("records"):
        planning_id = _strict_string(row["planning_zone_id"], "relation planning zone ID")
        source_id = _strict_string(row["source_zone_id"], "relation source zone ID")
        label = _strict_string(row["zone_label_raw"], "relation raw zone label")
        expected_zone = zone_records.get(planning_id)
        if expected_zone is None:
            raise BessZoningPrecheckError("Zoning relation references an unknown zone")
        if source_id != expected_zone["source_zone_id"] or label != expected_zone["zone_label_raw"]:
            raise BessZoningPrecheckError("Zoning relation zone identity is inconsistent")
        if row["source_layer"] != expected_zone["source_layer"]:
            raise BessZoningPrecheckError("Zoning relation source layer is inconsistent")
        relation_type = _strict_string(row["relation_type"], "zoning relation type")
        area = _strict_nonnegative_number(row["intersection_area_m2"], "intersection area")
        if relation_type == "AREA_OVERLAP" and area <= 0:
            raise BessZoningPrecheckError("AREA_OVERLAP requires positive area")
        if relation_type == "TOUCH_ONLY" and area != 0:
            raise BessZoningPrecheckError("TOUCH_ONLY requires zero area")
        if relation_type not in {"AREA_OVERLAP", "TOUCH_ONLY"}:
            raise BessZoningPrecheckError("Zoning relation type is invalid")
        for upper_column in ("parcel_metric_area_m2", "zone_area_m2"):
            upper = _strict_nonnegative_number(row[upper_column], upper_column)
            if upper <= 0:
                raise BessZoningPrecheckError(
                    f"{upper_column} must be positive for a zoning relation"
                )
            if area - upper > technical_overlay_tolerance(upper):
                raise BessZoningPrecheckError(
                    f"Intersection area exceeds {upper_column}"
                )
        percentage_checks = (
            ("parcel_metric_area_m2", "parcel_share_pct"),
            ("zone_area_m2", "zone_share_pct"),
        )
        for area_column, percentage_column in percentage_checks:
            reference_area = _strict_nonnegative_number(
                row[area_column], area_column
            )
            observed_percentage = _strict_nonnegative_number(
                row[percentage_column], percentage_column
            )
            if reference_area <= 0:
                raise BessZoningPrecheckError(
                    f"{area_column} must be positive for a zoning relation"
                )
            percentage_area = observed_percentage * reference_area / 100.0
            if abs(percentage_area - area) > technical_overlay_tolerance(
                reference_area
            ):
                raise BessZoningPrecheckError(
                    f"{percentage_column} is inconsistent with factual areas"
                )
        if row["source_document_id"] != index.document_id:
            raise BessZoningPrecheckError("Zoning relation document lineage differs")
        if row["source_archive_sha256"] != index.archive_sha256:
            raise BessZoningPrecheckError("Zoning relation archive lineage differs")
        _strict_string(row["source_layer"], "zoning relation source layer")
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_zone_mapping_input_sha256`

**Exact signature**

```python
def _zone_mapping_input_sha256(
    zones: pd.DataFrame,
    structure: PlanningRegulationStructureResult,
) -> str:
```

**Purpose**

Private `planning` helper for zone mapping input sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': 'landscout.bess_zoning.zone_mapping_input', 'zones': _frame_payload(zones, zone_columns), 'mapping': _frame_payload(structure.zone_mapping, tuple((str(column) for column in structure.zone_mapping.columns)))})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_zone_mapping_input_sha256`.

**Complete source-ordered implementation**

```python
def _zone_mapping_input_sha256(
    zones: pd.DataFrame,
    structure: PlanningRegulationStructureResult,
) -> str:
    zone_columns = (
        "planning_zone_id",
        "source_zone_id",
        "zone_label_raw",
        "source_document_id",
        "source_archive_sha256",
        "source_layer",
    )
    return _canonical_sha256(
        {
            "domain": "landscout.bess_zoning.zone_mapping_input",
            "zones": _frame_payload(zones, zone_columns),
            "mapping": _frame_payload(
                structure.zone_mapping,
                tuple(str(column) for column in structure.zone_mapping.columns),
            ),
        }
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_zone_chapter_rows`

**Exact signature**

```python
def _zone_chapter_rows(
    structure: PlanningRegulationStructureResult,
) -> list[dict[str, object]]:
```

**Purpose**

Private `planning` helper for zone chapter rows; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `list[dict[str, object]]`.
- Every observed return expression is reproduced without truncation:
```python
rows
```

**Validation and exceptions**

- Guard with a raise path: `len(set(labels)) != len(labels)`.
- Guard with a raise path: `len(set(section_ids)) != len(section_ids)`.
- Explicit raise expressions: `BessZoningPrecheckError('Regulation zone chapter labels must be unique')`, `BessZoningPrecheckError('Regulation zone chapter section IDs must be unique')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_required_section_ids_by_chapter` via `_zone_chapter_rows`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_evidence` via `_zone_chapter_rows`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_mapping` via `_zone_chapter_rows`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_chapter_policy` via `_zone_chapter_rows`.

**Complete source-ordered implementation**

```python
def _zone_chapter_rows(
    structure: PlanningRegulationStructureResult,
) -> list[dict[str, object]]:
    rows = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
    ].to_dict("records")
    labels = [
        _strict_string(row["zone_chapter_label"], "zone chapter label")
        for row in rows
    ]
    section_ids = [
        _strict_string(row["section_id"], "zone chapter section ID") for row in rows
    ]
    if len(set(labels)) != len(labels):
        raise BessZoningPrecheckError(
            "Regulation zone chapter labels must be unique"
        )
    if len(set(section_ids)) != len(section_ids):
        raise BessZoningPrecheckError(
            "Regulation zone chapter section IDs must be unique"
        )
    return rows
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_required_section_ids_by_chapter`

**Exact signature**

```python
def _required_section_ids_by_chapter(
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> dict[str, tuple[str, ...]]:
```

**Purpose**

Private `planning` helper for required section ids by chapter; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, tuple[str, ...]]`.
- Every observed return expression is reproduced without truncation:
```python
result
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
- In-memory mutation: `result[str(label)]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_evidence` via `_required_section_ids_by_chapter`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_chapter_policy` via `_required_section_ids_by_chapter`.

**Complete source-ordered implementation**

```python
def _required_section_ids_by_chapter(
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> dict[str, tuple[str, ...]]:
    required_numbers = set(policy.required_zone_article_numbers)
    chapter_ids = {
        row["zone_chapter_label"]: row["section_id"]
        for row in _zone_chapter_rows(structure)
    }
    result: dict[str, tuple[str, ...]] = {}
    section_rows = structure.sections.to_dict("records")
    for label, chapter_id in chapter_ids.items():
        result[str(label)] = tuple(
            str(row["section_id"])
            for row in section_rows
            if row["section_type"] == "ARTICLE"
            and row["parent_section_id"] == chapter_id
            and row["article_number_raw"] in required_numbers
        )
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_evidence_occurrence_uniqueness`

**Exact signature**

```python
def _validate_evidence_occurrence_uniqueness(catalog: pd.DataFrame) -> None:
```

**Purpose**

Rejects malformed or inconsistent evidence occurrence uniqueness; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `missing`.
- Guard with a raise path: `catalog.duplicated(list(_EVIDENCE_OCCURRENCE_COLUMNS)).any()`.
- Explicit raise expressions: `BessZoningPrecheckError('Evidence catalog contains a duplicate chapter-scoped evidence occurrence')`, `BessZoningPrecheckError(f'Evidence catalog lacks occurrence fields: {sorted(missing)}')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_validate_policy_evidence` via `_validate_evidence_occurrence_uniqueness`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_validate_evidence_occurrence_uniqueness`.

**Complete source-ordered implementation**

```python
def _validate_evidence_occurrence_uniqueness(catalog: pd.DataFrame) -> None:
    missing = set(_EVIDENCE_OCCURRENCE_COLUMNS).difference(catalog.columns)
    if missing:
        raise BessZoningPrecheckError(
            f"Evidence catalog lacks occurrence fields: {sorted(missing)}"
        )
    if catalog.duplicated(list(_EVIDENCE_OCCURRENCE_COLUMNS)).any():
        raise BessZoningPrecheckError(
            "Evidence catalog contains a duplicate chapter-scoped evidence occurrence"
        )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_policy_evidence`

**Exact signature**

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

Rejects malformed or inconsistent policy evidence; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[dict[str, dict[str, object]], pd.DataFrame]`.
- Every observed return expression is reproduced without truncation:
```python
(chapters, catalog)
```

**Validation and exceptions**

- Guard with a raise path: `policy_labels != set(chapters)`.
- Guard with a raise path: `catalog['evidence_id'].duplicated().any()`.
- Guard with a raise path: `chapter.review_completeness == 'COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES' and missing_required`.
- Guard with a raise path: `reviewed is None`.
- Guard with a raise path: `reviewed['section_type'] not in {'ZONE_CHAPTER', 'ARTICLE'}`.
- Guard with a raise path: `reviewed['zone_chapter_label'] != chapter.resolved_zone_chapter_label`.
- Guard with a raise path: `reviewed['section_type'] == 'ARTICLE' and reviewed['parent_section_id'] != chapter_id`.
- Guard with a raise path: `section is None`.
- Guard with a raise path: `section_type == 'ARTICLE' and section['parent_section_id'] != chapter_id`.
- Guard with a raise path: `evidence.section_id not in reviewed_ids`.
- Guard with a raise path: `fragment is None`.
- Guard with a raise path: `not isinstance(raw_fragment, str)`.
- Guard with a raise path: `fragment['section_page_fragment_sha256'] != evidence.section_page_fragment_sha256`.
- Guard with a raise path: `evidence.excerpt_end > len(raw_fragment) or raw_fragment[evidence.excerpt_start:evidence.excerpt_end] != excerpt`.
- Guard with a raise path: `sha256(excerpt.encode('utf-8')).hexdigest() != evidence.excerpt_sha256`.
- Guard with a raise path: `evidence.source_rule_end > len(raw_fragment) or raw_fragment[evidence.source_rule_start:evidence.source_rule_end] != rule`.
- Guard with a raise path: `sha256(rule.encode('utf-8')).hexdigest() != evidence.source_rule_sha256`.
- Guard with a raise path: `rule[relative_start:relative_end] != excerpt`.
- Guard with a raise path: `section['zone_chapter_label'] != chapter.resolved_zone_chapter_label`.
- Explicit raise expressions: `BessZoningPrecheckError('Evidence catalog IDs must be unique')`, `BessZoningPrecheckError(f'Chapter policy completeness differs; missing={missing}, extra={extra}')`, `BessZoningPrecheckError(f'Chapter {chapter.resolved_zone_chapter_label} omits required reviewed articles: {missing_required}')`, `BessZoningPrecheckError(f'Evidence {evidence.evidence_id} belongs to another zone chapter')`, `BessZoningPrecheckError(f'Evidence {evidence.evidence_id} excerpt SHA256 differs')`, `BessZoningPrecheckError(f'Evidence {evidence.evidence_id} fragment SHA256 differs')`, `BessZoningPrecheckError(f'Evidence {evidence.evidence_id} fragment text is invalid')`, `BessZoningPrecheckError(f'Evidence {evidence.evidence_id} has no factual section/page fragment')`, `BessZoningPrecheckError(f'Evidence {evidence.evidence_id} has the wrong chapter parent')`, `BessZoningPrecheckError(f'Evidence {evidence.evidence_id} is outside its source rule')`, `BessZoningPrecheckError(f'Evidence {evidence.evidence_id} is outside reviewed sections')`, `BessZoningPrecheckError(f'Evidence {evidence.evidence_id} offsets do not identify its exact excerpt')`, `BessZoningPrecheckError(f'Evidence {evidence.evidence_id} references an unknown section')`, `BessZoningPrecheckError(f'Evidence {evidence.evidence_id} source-rule SHA256 differs')`, `BessZoningPrecheckError(f'Evidence {evidence.evidence_id} source-rule offsets differ')`, `BessZoningPrecheckError(f'Reviewed section {reviewed_id!r} belongs to another chapter')`, `BessZoningPrecheckError(f'Reviewed section {reviewed_id!r} has another chapter parent')`, `BessZoningPrecheckError(f'Reviewed section {reviewed_id!r} is not a zone/general section')`, `BessZoningPrecheckError(f'Reviewed section {reviewed_id!r} is unknown')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(excerpt.encode('utf-8')).hexdigest`, `sha256(rule.encode('utf-8')).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: `catalog['decision_linked']`, `catalog[column]`, `catalog_rows`, `links_by_evidence`, `links_by_evidence.setdefault(evidence_id, [])`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_validate_policy_evidence`.

**Complete source-ordered implementation**

```python
def _validate_policy_evidence(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    fragments: pd.DataFrame,
    policy_hash: str,
    evidence_route_links: pd.DataFrame,
) -> tuple[dict[str, dict[str, object]], pd.DataFrame]:
    sections = {
        _strict_string(row["section_id"], "section ID"): row
        for row in structure.sections.to_dict("records")
    }
    fragment_records = {
        (
            _strict_string(row["section_id"], "fragment section ID"),
            _strict_positive_integer(row["page_number"], "fragment page number"),
        ): row
        for row in fragments.to_dict("records")
    }
    chapters = {
        _strict_string(row["zone_chapter_label"], "zone chapter label"): row
        for row in _zone_chapter_rows(structure)
    }
    policy_labels = {chapter.resolved_zone_chapter_label for chapter in policy.chapters}
    if policy_labels != set(chapters):
        missing = sorted(set(chapters).difference(policy_labels))
        extra = sorted(policy_labels.difference(chapters))
        raise BessZoningPrecheckError(
            f"Chapter policy completeness differs; missing={missing}, extra={extra}"
        )
    catalog_rows: list[dict[str, object]] = []
    links_by_evidence: dict[str, list[tuple[str, str]]] = {}
    for link in evidence_route_links.to_dict("records"):
        evidence_id = _strict_string(link["evidence_id"], "linked evidence ID")
        links_by_evidence.setdefault(evidence_id, []).append(
            (
                _strict_string(link["route_id"], "linked route ID"),
                _strict_string(link["route_role"], "route role"),
            )
        )
    required_by_chapter = _required_section_ids_by_chapter(structure, policy)
    for chapter in policy.chapters:
        chapter_row = chapters[chapter.resolved_zone_chapter_label]
        chapter_id = chapter_row["section_id"]
        reviewed_ids = set(chapter.reviewed_section_ids)
        for reviewed_id in chapter.reviewed_section_ids:
            reviewed = sections.get(reviewed_id)
            if reviewed is None:
                raise BessZoningPrecheckError(
                    f"Reviewed section {reviewed_id!r} is unknown"
                )
            if reviewed["section_type"] == "GENERAL":
                continue
            if reviewed["section_type"] not in {"ZONE_CHAPTER", "ARTICLE"}:
                raise BessZoningPrecheckError(
                    f"Reviewed section {reviewed_id!r} is not a zone/general section"
                )
            if reviewed["zone_chapter_label"] != chapter.resolved_zone_chapter_label:
                raise BessZoningPrecheckError(
                    f"Reviewed section {reviewed_id!r} belongs to another chapter"
                )
            if (
                reviewed["section_type"] == "ARTICLE"
                and reviewed["parent_section_id"] != chapter_id
            ):
                raise BessZoningPrecheckError(
                    f"Reviewed section {reviewed_id!r} has another chapter parent"
                )
        required_ids = set(required_by_chapter[chapter.resolved_zone_chapter_label])
        missing_required = sorted(required_ids.difference(reviewed_ids))
        if (
            chapter.review_completeness
            == "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"
            and missing_required
        ):
            raise BessZoningPrecheckError(
                f"Chapter {chapter.resolved_zone_chapter_label} omits required reviewed articles: {missing_required}"
            )
        for evidence in chapter.evidence:
            reverse_links = tuple(
                sorted(links_by_evidence.get(evidence.evidence_id, []))
            )
            section = sections.get(evidence.section_id)
            if section is None:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} references an unknown section"
                )
            section_type = section["section_type"]
            if section_type == "GENERAL":
                pass
            elif section["zone_chapter_label"] != chapter.resolved_zone_chapter_label:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} belongs to another zone chapter"
                )
            if section_type == "ARTICLE" and section["parent_section_id"] != chapter_id:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} has the wrong chapter parent"
                )
            if evidence.section_id not in reviewed_ids:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} is outside reviewed sections"
                )
            fragment = fragment_records.get((evidence.section_id, evidence.page_number))
            if fragment is None:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} has no factual section/page fragment"
                )
            excerpt = evidence.exact_raw_excerpt
            raw_fragment = fragment["raw_text"]
            if not isinstance(raw_fragment, str):
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} fragment text is invalid"
                )
            if fragment["section_page_fragment_sha256"] != evidence.section_page_fragment_sha256:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} fragment SHA256 differs"
                )
            if evidence.excerpt_end > len(raw_fragment) or raw_fragment[
                evidence.excerpt_start : evidence.excerpt_end
            ] != excerpt:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} offsets do not identify its exact excerpt"
                )
            if sha256(excerpt.encode("utf-8")).hexdigest() != evidence.excerpt_sha256:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} excerpt SHA256 differs"
                )
            rule = evidence.source_rule_excerpt
            if evidence.source_rule_end > len(raw_fragment) or raw_fragment[
                evidence.source_rule_start : evidence.source_rule_end
            ] != rule:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} source-rule offsets differ"
                )
            if sha256(rule.encode("utf-8")).hexdigest() != evidence.source_rule_sha256:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} source-rule SHA256 differs"
                )
            relative_start = evidence.excerpt_start - evidence.source_rule_start
            relative_end = evidence.excerpt_end - evidence.source_rule_start
            if rule[relative_start:relative_end] != excerpt:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} is outside its source rule"
                )
            catalog_rows.append(
                {
                    "evidence_id": evidence.evidence_id,
                    "resolved_zone_chapter_label": (
                        chapter.resolved_zone_chapter_label
                    ),
                    "section_id": evidence.section_id,
                    "page_number": evidence.page_number,
                    "evidence_kind": evidence.evidence_kind,
                    "evidence_direction": evidence.evidence_direction,
                    "linked_route_ids": tuple(item[0] for item in reverse_links),
                    "linked_route_roles": tuple(item[1] for item in reverse_links),
                    "decision_linked": bool(reverse_links),
                    "exact_raw_excerpt": excerpt,
                    "excerpt_sha256": evidence.excerpt_sha256,
                    "section_page_fragment_sha256": (
                        evidence.section_page_fragment_sha256
                    ),
                    "excerpt_start": evidence.excerpt_start,
                    "excerpt_end": evidence.excerpt_end,
                    "source_rule_id": evidence.source_rule_id,
                    "source_rule_excerpt": rule,
                    "source_rule_sha256": evidence.source_rule_sha256,
                    "source_rule_start": evidence.source_rule_start,
                    "source_rule_end": evidence.source_rule_end,
                    "interpretation_note": evidence.interpretation_note,
                    "review_completeness": chapter.review_completeness,
                    "review_scope": policy.review_scope,
                    "policy_profile": policy.policy_profile,
                    "policy_sha256": policy_hash,
                    "document_id": index.document_id,
                    "archive_sha256": index.archive_sha256,
                    "pdf_sha256": index.pdf_sha256,
                    "index_content_sha256": index.index_content_sha256,
                    "structure_result_content_sha256": (
                        structure.structure_result_content_sha256
                    ),
                    "structure_profile": structure.structure_profile,
                }
            )
    catalog = pd.DataFrame(catalog_rows, columns=EVIDENCE_CATALOG_COLUMNS)
    for column in (
        "page_number",
        "excerpt_start",
        "excerpt_end",
        "source_rule_start",
        "source_rule_end",
    ):
        catalog[column] = catalog[column].astype("int64")
    catalog["decision_linked"] = catalog["decision_linked"].astype("bool")
    if catalog["evidence_id"].duplicated().any():
        raise BessZoningPrecheckError("Evidence catalog IDs must be unique")
    _validate_evidence_occurrence_uniqueness(catalog)
    return chapters, catalog
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_mapping`

**Exact signature**

```python
def _validate_mapping(
    structure: PlanningRegulationStructureResult,
    zones: pd.DataFrame,
) -> pd.DataFrame:
```

**Purpose**

Rejects malformed or inconsistent mapping; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
mapping
```

**Validation and exceptions**

- Guard with a raise path: `mapped_labels != source_labels`.
- Guard with a raise path: `status not in _RESOLVED_MAPPING_STATUSES`.
- Guard with a raise path: `chapters.get(resolved) != row['matched_section_id']`.
- Explicit raise expressions: `BessZoningPrecheckError('Factual zone mapping is incomplete or has extras')`, `BessZoningPrecheckError('Zone mapping chapter identity is inconsistent')`, `BessZoningPrecheckError(f"Source zone {row['source_zone_label_raw']!r} is not resolved")`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_validate_mapping`.

**Complete source-ordered implementation**

```python
def _validate_mapping(
    structure: PlanningRegulationStructureResult,
    zones: pd.DataFrame,
) -> pd.DataFrame:
    mapping = structure.zone_mapping.copy(deep=True)
    source_labels = set(
        _exact_id_series(zones["zone_label_raw"], "raw zone label", unique=False)
    )
    mapped_labels = set(
        _exact_id_series(
            mapping["source_zone_label_raw"],
            "mapped source zone label",
            unique=True,
        )
    )
    if mapped_labels != source_labels:
        raise BessZoningPrecheckError("Factual zone mapping is incomplete or has extras")
    chapters = {
        row["zone_chapter_label"]: row["section_id"]
        for row in _zone_chapter_rows(structure)
    }
    for row in mapping.to_dict("records"):
        _strict_string(row["source_zone_label_raw"], "mapped source zone label")
        status = _strict_string(row["mapping_status"], "mapping status")
        if status not in _RESOLVED_MAPPING_STATUSES:
            raise BessZoningPrecheckError(
                f"Source zone {row['source_zone_label_raw']!r} is not resolved"
            )
        resolved = _strict_string(
            row["resolved_zone_chapter_label"], "resolved zone chapter"
        )
        if chapters.get(resolved) != row["matched_section_id"]:
            raise BessZoningPrecheckError("Zone mapping chapter identity is inconsistent")
    return mapping
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_lineage`

**Exact signature**

```python
def _lineage(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for lineage; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'planning_precheck_scope': PLANNING_PRECHECK_SCOPE, 'review_scope': REVIEW_SCOPE, 'policy_profile': policy.policy_profile, 'policy_sha256': policy_hash, 'document_id': index.document_id, 'archive_sha256': index.archive_sha256, 'pdf_sha256': index.pdf_sha256, 'index_content_sha256': index.index_content_sha256, 'structure_result_content_sha256': structure.structure_result_content_sha256, 'structure_profile': structure.structure_profile}
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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_chapter_policy` via `_lineage`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_route_assessments` via `_lineage`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_evidence_route_links` via `_lineage`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_source_zone_policy` via `_lineage`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_parcel_zone_interpretations` via `_lineage`.

**Complete source-ordered implementation**

```python
def _lineage(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> dict[str, object]:
    return {
        "planning_precheck_scope": PLANNING_PRECHECK_SCOPE,
        "review_scope": REVIEW_SCOPE,
        "policy_profile": policy.policy_profile,
        "policy_sha256": policy_hash,
        "document_id": index.document_id,
        "archive_sha256": index.archive_sha256,
        "pdf_sha256": index.pdf_sha256,
        "index_content_sha256": index.index_content_sha256,
        "structure_result_content_sha256": structure.structure_result_content_sha256,
        "structure_profile": structure.structure_profile,
    }
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_chapter_policy`

**Exact signature**

```python
def _build_chapter_policy(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
```

**Purpose**

Constructs chapter policy; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
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
- In-memory mutation: `frame['evidence_count']`, `rows`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_build_chapter_policy`.

**Complete source-ordered implementation**

```python
def _build_chapter_policy(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
    by_label = {
        chapter.resolved_zone_chapter_label: chapter for chapter in policy.chapters
    }
    rows: list[dict[str, object]] = []
    lineage = _lineage(index, structure, policy, policy_hash)
    chapters = _zone_chapter_rows(structure)
    required_by_chapter = _required_section_ids_by_chapter(structure, policy)
    for source in chapters:
        label = _strict_string(source["zone_chapter_label"], "zone chapter label")
        chapter_section_id = _strict_string(
            source["section_id"], "zone chapter section ID"
        )
        chapter = by_label[label]
        evidence_ids = tuple(item.evidence_id for item in chapter.evidence)
        decision_evidence_ids = tuple(
            item.evidence_id
            for item in chapter.evidence
            if item.evidence_direction != "CONTEXT_ONLY"
        )
        context_evidence_ids = tuple(
            item.evidence_id
            for item in chapter.evidence
            if item.evidence_direction == "CONTEXT_ONLY"
        )
        rows.append(
            {
                "resolved_zone_chapter_label": label,
                "chapter_section_id": chapter_section_id,
                "review_completeness": chapter.review_completeness,
                "review_scope": policy.review_scope,
                "reviewed_section_ids": tuple(chapter.reviewed_section_ids),
                "missing_required_section_ids": tuple(
                    section_id
                    for section_id in required_by_chapter[label]
                    if section_id not in set(chapter.reviewed_section_ids)
                ),
                "review_note": chapter.review_note,
                "zoning_precheck_status": chapter.zoning_precheck_status,
                "zoning_precheck_confidence": chapter.zoning_precheck_confidence,
                "evidence_count": len(evidence_ids),
                "evidence_ids": evidence_ids,
                "decision_evidence_ids": decision_evidence_ids,
                "context_evidence_ids": context_evidence_ids,
                "rationale": chapter.rationale,
                "missing_information": chapter.missing_information,
                **lineage,
            }
        )
    frame = pd.DataFrame(rows, columns=CHAPTER_POLICY_COLUMNS)
    frame["evidence_count"] = frame["evidence_count"].astype("int64")
    return frame
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_route_status`

**Exact signature**

```python
def _route_status(route_kind: RouteKind) -> ChapterStatus:
```

**Purpose**

Maps each configured written-zoning RouteKind to its deterministic ChapterStatus; this is planning-policy interpretation, not legal authorization.

**Return contract**

- Declared return annotation: `ChapterStatus`.
- Every observed return expression is reproduced without truncation:
```python
statuses[route_kind]
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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_route_assessments` via `_route_status`.

**Complete source-ordered implementation**

```python
def _route_status(route_kind: RouteKind) -> ChapterStatus:
    statuses: dict[RouteKind, ChapterStatus] = {
        "DIRECT_ROUTE": "POTENTIALLY_COMPATIBLE",
        "CONDITIONAL_ROUTE": "CONDITIONAL_REVIEW",
        "RESTRICTION_EXCEPTION_ROUTE": "CONDITIONAL_REVIEW",
        "DIFFICULTY_ONLY": "LIKELY_DIFFICULT",
    }
    return statuses[route_kind]
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_route_assessments`

**Exact signature**

```python
def _build_route_assessments(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
```

**Purpose**

Constructs route assessments; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- Guard with a raise path: `frame['route_id'].duplicated().any()`.
- Explicit raise expressions: `BessZoningPrecheckError('Normalized route IDs must be unique')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_build_route_assessments`.

**Complete source-ordered implementation**

```python
def _build_route_assessments(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
    lineage = _lineage(index, structure, policy, policy_hash)
    rows = [
        {
            "route_id": route.route_id,
            "resolved_zone_chapter_label": chapter.resolved_zone_chapter_label,
            "route_kind": route.route_kind,
            "derived_route_status": _route_status(route.route_kind),
            "positive_evidence_ids": tuple(route.positive_evidence_ids),
            "condition_evidence_ids": tuple(route.condition_evidence_ids),
            "difficulty_evidence_ids": tuple(route.difficulty_evidence_ids),
            "applicability_note": route.applicability_note,
            "review_completeness": chapter.review_completeness,
            "review_scope": policy.review_scope,
            **lineage,
        }
        for chapter in policy.chapters
        for route in chapter.route_assessments
    ]
    frame = pd.DataFrame(rows, columns=ROUTE_ASSESSMENT_COLUMNS)
    if frame["route_id"].duplicated().any():
        raise BessZoningPrecheckError("Normalized route IDs must be unique")
    return frame
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_evidence_route_links`

**Exact signature**

```python
def _build_evidence_route_links(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
```

**Purpose**

Constructs evidence route links; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- Guard with a raise path: `frame.duplicated(['route_id', 'evidence_id']).any()`.
- Explicit raise expressions: `BessZoningPrecheckError('Evidence-route links must be unique by route and evidence')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `rows`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_build_evidence_route_links`.

**Complete source-ordered implementation**

```python
def _build_evidence_route_links(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
    lineage = _lineage(index, structure, policy, policy_hash)
    rows: list[dict[str, object]] = []
    role_fields = (
        ("positive_evidence_ids", "POSITIVE", "SUPPORTS_POTENTIAL_COMPATIBILITY"),
        ("condition_evidence_ids", "CONDITION", "CONDITION"),
        ("difficulty_evidence_ids", "DIFFICULTY", "SUPPORTS_DIFFICULTY"),
    )
    for chapter in policy.chapters:
        for route in chapter.route_assessments:
            for field, role, direction in role_fields:
                for evidence_id in getattr(route, field):
                    rows.append(
                        {
                            "route_id": route.route_id,
                            "resolved_zone_chapter_label": (
                                chapter.resolved_zone_chapter_label
                            ),
                            "route_kind": route.route_kind,
                            "evidence_id": evidence_id,
                            "route_role": role,
                            "evidence_direction": direction,
                            "review_completeness": chapter.review_completeness,
                            "review_scope": policy.review_scope,
                            **lineage,
                        }
                    )
    frame = pd.DataFrame(rows, columns=EVIDENCE_ROUTE_LINK_COLUMNS)
    if not frame.empty:
        frame = frame.sort_values(
            ["route_id", "evidence_id"], kind="mergesort"
        ).reset_index(drop=True)
    if frame.duplicated(["route_id", "evidence_id"]).any():
        raise BessZoningPrecheckError(
            "Evidence-route links must be unique by route and evidence"
        )
    return frame
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_source_zone_policy`

**Exact signature**

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

Constructs source zone policy; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
pd.DataFrame(rows, columns=SOURCE_ZONE_POLICY_COLUMNS)
```

**Validation and exceptions**

- Guard with a raise path: `len(layers) != 1`.
- Explicit raise expressions: `BessZoningPrecheckError(f'Source zone label {label!r} has ambiguous source-layer lineage')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `layers_by_label[str(label)]`, `rows`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_build_source_zone_policy`.

**Complete source-ordered implementation**

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
    policies = chapter_policy.set_index("resolved_zone_chapter_label").to_dict("index")
    lineage = _lineage(index, structure, policy, policy_hash)
    layers_by_label: dict[str, str] = {}
    for label, group in zones.groupby("zone_label_raw", sort=False):
        layers = tuple(dict.fromkeys(group["source_layer"].tolist()))
        if len(layers) != 1:
            raise BessZoningPrecheckError(
                f"Source zone label {label!r} has ambiguous source-layer lineage"
            )
        layers_by_label[str(label)] = _strict_string(layers[0], "zone source layer")
    rows: list[dict[str, object]] = []
    for source in mapping.to_dict("records"):
        chapter = policies[source["resolved_zone_chapter_label"]]
        rows.append(
            {
                "source_zone_label_raw": source["source_zone_label_raw"],
                "resolved_zone_chapter_label": source[
                    "resolved_zone_chapter_label"
                ],
                "mapping_status": source["mapping_status"],
                "matched_section_id": source["matched_section_id"],
                "source_layer": layers_by_label[source["source_zone_label_raw"]],
                "zoning_precheck_status": chapter["zoning_precheck_status"],
                "zoning_precheck_confidence": chapter[
                    "zoning_precheck_confidence"
                ],
                "evidence_ids": tuple(chapter["evidence_ids"]),
                "decision_evidence_ids": tuple(chapter["decision_evidence_ids"]),
                "context_evidence_ids": tuple(chapter["context_evidence_ids"]),
                **lineage,
            }
        )
    return pd.DataFrame(rows, columns=SOURCE_ZONE_POLICY_COLUMNS)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_parcel_zone_interpretations`

**Exact signature**

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

Constructs parcel zone interpretations; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
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
- In-memory mutation: `rows`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_build_parcel_zone_interpretations`.

**Complete source-ordered implementation**

```python
def _build_parcel_zone_interpretations(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
    relations: pd.DataFrame,
    source_policy: pd.DataFrame,
) -> pd.DataFrame:
    policies = source_policy.set_index("source_zone_label_raw").to_dict("index")
    lineage = _lineage(index, structure, policy, policy_hash)
    rows: list[dict[str, object]] = []
    positive = relations.loc[relations["relation_type"].eq("AREA_OVERLAP")]
    for source in positive.to_dict("records"):
        item = policies[source["zone_label_raw"]]
        rows.append(
            {
                "parcel_id": source["parcel_id"],
                "planning_zone_id": source["planning_zone_id"],
                "source_zone_id": source["source_zone_id"],
                "source_zone_label_raw": source["zone_label_raw"],
                "resolved_zone_chapter_label": item[
                    "resolved_zone_chapter_label"
                ],
                "intersection_area_m2": float(source["intersection_area_m2"]),
                "parcel_share_pct": float(source["parcel_share_pct"]),
                "zoning_precheck_status": item["zoning_precheck_status"],
                "zoning_precheck_confidence": item[
                    "zoning_precheck_confidence"
                ],
                "evidence_ids": tuple(item["evidence_ids"]),
                "decision_evidence_ids": tuple(item["decision_evidence_ids"]),
                "context_evidence_ids": tuple(item["context_evidence_ids"]),
                **lineage,
                "source_layer": source["source_layer"],
            }
        )
    frame = pd.DataFrame(rows, columns=PARCEL_ZONE_POLICY_COLUMNS)
    if frame.empty:
        frame = pd.DataFrame(
            {
                column: pd.Series(
                    dtype=(
                        "float64"
                        if column in {"intersection_area_m2", "parcel_share_pct"}
                        else "object"
                    )
                )
                for column in PARCEL_ZONE_POLICY_COLUMNS
            }
        )
    return frame
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_is_null`

**Exact signature**

```python
def _is_null(value: object) -> bool:
```

**Purpose**

Tests whether null; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
isinstance(null, (bool, np.bool_)) and bool(null)

True

False
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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_parcel_output` via `_is_null`.

**Complete source-ordered implementation**

```python
def _is_null(value: object) -> bool:
    if value is None or value is pd.NA:
        return True
    try:
        null = pd.isna(value)
    except (TypeError, ValueError):
        return False
    return isinstance(null, (bool, np.bool_)) and bool(null)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_parcel_output`

**Exact signature**

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

Constructs parcel output; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output
```

**Validation and exceptions**

- Guard with a raise path: `group is None or group.empty`.
- Guard with a raise path: `not _is_null(dominant_id)`.
- Guard with a raise path: `dominant_id != expected_dominant`.
- Explicit raise expressions: `BessZoningPrecheckError('Parcel dominant zone differs from factual positive-area relations')`, `BessZoningPrecheckError('Parcel dominant zone exists without a positive-area relation')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `summary['positive_area_zone_count'].append`.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `output[column]`, `summary['distinct_zone_status_count']`, `summary['dominant_zone_precheck_confidence']`, `summary['dominant_zone_precheck_status']`, `summary['non_dominant_different_status_count']`, `summary['non_zoning_planning_features_interpreted']`, `summary['planning_precheck_scope']`, `summary['positive_area_zone_count']`, `summary['review_scope']`, `summary['touch_only_zone_count']`, `summary['zoning_precheck_context_evidence_ids']`, `summary['zoning_precheck_evidence_ids']`, `summary['zoning_precheck_policy_profile']`, `summary['zoning_precheck_policy_sha256']`, `summary['zoning_precheck_requires_formal_review']`, `summary['zoning_precheck_status']`, `values[:]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_build_parcel_output`.

**Complete source-ordered implementation**

```python
def _build_parcel_output(
    parcels: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    interpretations: pd.DataFrame,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> gpd.GeoDataFrame:
    output = parcels.copy(deep=True)
    positive_by_parcel = {
        parcel_id: group.copy()
        for parcel_id, group in interpretations.groupby("parcel_id", sort=False)
    }
    touch_counts = (
        relations.loc[relations["relation_type"].eq("TOUCH_ONLY")]
        .groupby("parcel_id", sort=False)
        .size()
        .to_dict()
    )
    summary: dict[str, list[object]] = {column: [] for column in PARCEL_PRECHECK_COLUMNS}
    for parcel in parcels.to_dict("records"):
        parcel_id = parcel["parcel_id"]
        group = positive_by_parcel.get(parcel_id)
        dominant_id = parcel["dominant_planning_zone_id"]
        if group is None or group.empty:
            if not _is_null(dominant_id):
                raise BessZoningPrecheckError(
                    "Parcel dominant zone exists without a positive-area relation"
                )
            overall_status = "UNKNOWN"
            dominant_status: object = None
            dominant_confidence: object = None
            positive_count = 0
            distinct_count = 0
            non_dominant_different = 0
            evidence_ids: tuple[str, ...] = ()
            context_evidence_ids: tuple[str, ...] = ()
        else:
            ordered = group.sort_values(
                ["intersection_area_m2", "planning_zone_id"],
                ascending=[False, True],
                kind="mergesort",
            )
            expected_dominant = ordered.iloc[0]["planning_zone_id"]
            if dominant_id != expected_dominant:
                raise BessZoningPrecheckError(
                    "Parcel dominant zone differs from factual positive-area relations"
                )
            dominant = ordered.iloc[0]
            dominant_status = dominant["zoning_precheck_status"]
            dominant_confidence = dominant["zoning_precheck_confidence"]
            statuses = tuple(group["zoning_precheck_status"].tolist())
            distinct_statuses = set(statuses)
            overall_status = (
                statuses[0]
                if len(distinct_statuses) == 1
                else "MIXED_REVIEW_REQUIRED"
            )
            positive_count = len(group)
            distinct_count = len(distinct_statuses)
            non_dominant_different = int(
                (
                    group.loc[
                        ~group["planning_zone_id"].eq(expected_dominant),
                        "zoning_precheck_status",
                    ]
                    != dominant_status
                ).sum()
            )
            evidence_ids = tuple(
                sorted(
                    {
                        _strict_string(evidence_id, "parcel evidence ID")
                        for values in group["decision_evidence_ids"].tolist()
                        for evidence_id in values
                    }
                )
            )
            context_evidence_ids = tuple(
                sorted(
                    {
                        _strict_string(evidence_id, "parcel context evidence ID")
                        for values in group["context_evidence_ids"].tolist()
                        for evidence_id in values
                    }
                )
            )
        summary["zoning_precheck_status"].append(overall_status)
        summary["dominant_zone_precheck_status"].append(dominant_status)
        summary["dominant_zone_precheck_confidence"].append(dominant_confidence)
        summary["positive_area_zone_count"].append(positive_count)
        summary["distinct_zone_status_count"].append(distinct_count)
        summary["non_dominant_different_status_count"].append(
            non_dominant_different
        )
        summary["touch_only_zone_count"].append(int(touch_counts.get(parcel_id, 0)))
        summary["zoning_precheck_evidence_ids"].append(evidence_ids)
        summary["zoning_precheck_context_evidence_ids"].append(
            context_evidence_ids
        )
        summary["zoning_precheck_requires_formal_review"].append(True)
        summary["planning_precheck_scope"].append(PLANNING_PRECHECK_SCOPE)
        summary["review_scope"].append(REVIEW_SCOPE)
        summary["non_zoning_planning_features_interpreted"].append(False)
        summary["zoning_precheck_policy_profile"].append(policy.policy_profile)
        summary["zoning_precheck_policy_sha256"].append(policy_hash)
    for column in PARCEL_PRECHECK_COLUMNS:
        values = np.empty(len(summary[column]), dtype=object)
        values[:] = summary[column]
        output[column] = values
    for column in (
        "positive_area_zone_count",
        "distinct_zone_status_count",
        "non_dominant_different_status_count",
        "touch_only_zone_count",
    ):
        output[column] = output[column].astype("int64")
    for column in (
        "zoning_precheck_requires_formal_review",
        "non_zoning_planning_features_interpreted",
    ):
        output[column] = output[column].astype("bool")
    return output
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_result_component_metadata`

**Exact signature**

```python
def _result_component_metadata(result: BessZoningPrecheckResult) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for result component metadata; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'result_hash_schema_version': result.result_hash_schema_version, 'policy_schema_version': result.policy_schema_version, 'policy_profile': result.policy_profile, 'planning_precheck_scope': result.planning_precheck_scope, 'review_scope': result.review_scope, 'document_id': result.document_id, 'archive_sha256': result.archive_sha256, 'pdf_sha256': result.pdf_sha256, 'index_content_sha256': result.index_content_sha256, 'structure_result_content_sha256': result.structure_result_content_sha256, 'structure_profile': result.structure_profile, 'policy_config_sha256': result.policy_config_sha256, 'factual_structure_content_sha256': result.factual_structure_content_sha256, 'zone_mapping_input_sha256': result.zone_mapping_input_sha256, 'zoning_relation_hash_columns': list(result.zoning_relation_hash_columns), 'zoning_relations_input_sha256': result.zoning_relations_input_sha256, 'touch_only_relation_count': result.touch_only_relation_count}
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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_result_frame_sha256` via `_result_component_metadata`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_complete_result_sha256` via `_result_component_metadata`.

**Complete source-ordered implementation**

```python
def _result_component_metadata(result: BessZoningPrecheckResult) -> dict[str, object]:
    return {
        "result_hash_schema_version": result.result_hash_schema_version,
        "policy_schema_version": result.policy_schema_version,
        "policy_profile": result.policy_profile,
        "planning_precheck_scope": result.planning_precheck_scope,
        "review_scope": result.review_scope,
        "document_id": result.document_id,
        "archive_sha256": result.archive_sha256,
        "pdf_sha256": result.pdf_sha256,
        "index_content_sha256": result.index_content_sha256,
        "structure_result_content_sha256": result.structure_result_content_sha256,
        "structure_profile": result.structure_profile,
        "policy_config_sha256": result.policy_config_sha256,
        "factual_structure_content_sha256": result.factual_structure_content_sha256,
        "zone_mapping_input_sha256": result.zone_mapping_input_sha256,
        "zoning_relation_hash_columns": list(result.zoning_relation_hash_columns),
        "zoning_relations_input_sha256": result.zoning_relations_input_sha256,
        "touch_only_relation_count": result.touch_only_relation_count,
    }
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_result_frame_sha256`

**Exact signature**

```python
def _result_frame_sha256(
    domain: str,
    result: BessZoningPrecheckResult,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
```

**Purpose**

Private `planning` helper for result frame sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': domain, **_result_component_metadata(result), 'frame': _frame_payload(frame, columns)})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_result_with_hashes` via `_result_frame_sha256`.

**Complete source-ordered implementation**

```python
def _result_frame_sha256(
    domain: str,
    result: BessZoningPrecheckResult,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
    return _canonical_sha256(
        {
            "domain": domain,
            **_result_component_metadata(result),
            "frame": _frame_payload(frame, columns),
        }
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_complete_result_sha256`

**Exact signature**

```python
def _complete_result_sha256(result: BessZoningPrecheckResult) -> str:
```

**Purpose**

Private `planning` helper for complete result sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_sha256({'domain': 'landscout.bess_zoning.precheck_result', **_result_component_metadata(result), 'evidence_catalog_content_sha256': result.evidence_catalog_content_sha256, 'evidence_route_links_content_sha256': result.evidence_route_links_content_sha256, 'route_assessments_content_sha256': result.route_assessments_content_sha256, 'chapter_policy_content_sha256': result.chapter_policy_content_sha256, 'source_zone_policy_content_sha256': result.source_zone_policy_content_sha256, 'parcel_zone_policy_content_sha256': result.parcel_zone_policy_content_sha256, 'parcel_output_content_sha256': result.parcel_output_content_sha256})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_result_with_hashes` via `_complete_result_sha256`.

**Complete source-ordered implementation**

```python
def _complete_result_sha256(result: BessZoningPrecheckResult) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.bess_zoning.precheck_result",
            **_result_component_metadata(result),
            "evidence_catalog_content_sha256": (
                result.evidence_catalog_content_sha256
            ),
            "evidence_route_links_content_sha256": (
                result.evidence_route_links_content_sha256
            ),
            "route_assessments_content_sha256": (
                result.route_assessments_content_sha256
            ),
            "chapter_policy_content_sha256": result.chapter_policy_content_sha256,
            "source_zone_policy_content_sha256": (
                result.source_zone_policy_content_sha256
            ),
            "parcel_zone_policy_content_sha256": (
                result.parcel_zone_policy_content_sha256
            ),
            "parcel_output_content_sha256": result.parcel_output_content_sha256,
        }
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_result_with_hashes`

**Exact signature**

```python
def _result_with_hashes(
    result: BessZoningPrecheckResult,
) -> BessZoningPrecheckResult:
```

**Purpose**

Private `planning` helper for result with hashes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessZoningPrecheckResult`.
- Every observed return expression is reproduced without truncation:
```python
replace(component, complete_result_content_sha256=_complete_result_sha256(component))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_complete_result_sha256`, `_result_frame_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.interpret_bess_zoning import (
    CHAPTER_POLICY_COLUMNS,
    EVIDENCE_CATALOG_COLUMNS,
    EVIDENCE_ROUTE_LINK_COLUMNS,
    PARCEL_ZONE_POLICY_COLUMNS,
    ROUTE_ASSESSMENT_COLUMNS,
    SOURCE_ZONE_POLICY_COLUMNS,
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    _result_with_hashes,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_result_with_hashes`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_repeated_excerpt_occurrence_is_bound_to_policy` via `_result_with_hashes`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_result_mutation_is_rejected` via `_result_with_hashes`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_evidence_catalog_mutation_is_rejected` via `_result_with_hashes`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_catalog_occurrence_duplicate_is_rejected` via `_result_with_hashes`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_route_table_mutation_is_rejected` via `_result_with_hashes`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_evidence_route_link_mutation_is_rejected` via `_result_with_hashes`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_coordinated_reverse_link_mutation_is_rejected` via `_result_with_hashes`.

**Complete source-ordered implementation**

```python
def _result_with_hashes(
    result: BessZoningPrecheckResult,
) -> BessZoningPrecheckResult:
    component = replace(
        result,
        evidence_catalog_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.evidence_catalog",
            result,
            result.evidence_catalog,
            EVIDENCE_CATALOG_COLUMNS,
        ),
        evidence_route_links_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.evidence_route_links",
            result,
            result.evidence_route_links,
            EVIDENCE_ROUTE_LINK_COLUMNS,
        ),
        route_assessments_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.route_assessments",
            result,
            result.route_assessments,
            ROUTE_ASSESSMENT_COLUMNS,
        ),
        chapter_policy_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.chapter_policy",
            result,
            result.chapter_policy,
            CHAPTER_POLICY_COLUMNS,
        ),
        source_zone_policy_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.source_zone_policy",
            result,
            result.source_zone_policy,
            SOURCE_ZONE_POLICY_COLUMNS,
        ),
        parcel_zone_policy_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.parcel_zone_policy",
            result,
            result.parcel_zone_interpretations,
            PARCEL_ZONE_POLICY_COLUMNS,
        ),
        parcel_output_content_sha256=_result_frame_sha256(
            "landscout.bess_zoning.parcel_output",
            result,
            result.parcels,
            tuple(result.parcels.columns),
        ),
    )
    return replace(
        component,
        complete_result_content_sha256=_complete_result_sha256(component),
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_result`

**Exact signature**

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

Constructs result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessZoningPrecheckResult`.
- Every observed return expression is reproduced without truncation:
```python
_result_with_hashes(result)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_factual_structure_sha256`, `_frame_sha256`, `_policy_sha256`, `_zone_mapping_input_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::validate_bess_zoning_precheck` via `_build_result`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::interpret_bess_zoning` via `_build_result`.

**Complete source-ordered implementation**

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
    validate_planning_regulation_index(index)
    fragments = validate_planning_regulation_structure_with_fragments(
        index,
        zones,
        zoning_intersections,
        structure_config,
        structure,
    )
    _validate_policy_lock(index, structure, policy)
    parcel_copy = _validate_parcels(index, parcels)
    zone_copy = _validate_zones(index, zones)
    relation_copy = _validate_relations(
        index, parcel_copy, zone_copy, zoning_intersections
    )
    mapping = _validate_mapping(structure, zone_copy)
    policy_hash = _policy_sha256(policy)
    route_assessments = _build_route_assessments(
        index, structure, policy, policy_hash
    )
    evidence_route_links = _build_evidence_route_links(
        index, structure, policy, policy_hash
    )
    _, evidence_catalog = _validate_policy_evidence(
        index,
        structure,
        policy,
        fragments,
        policy_hash,
        evidence_route_links,
    )
    chapter_policy = _build_chapter_policy(
        index, structure, policy, policy_hash
    )
    source_policy = _build_source_zone_policy(
        index,
        structure,
        policy,
        policy_hash,
        zone_copy,
        mapping,
        chapter_policy,
    )
    interpretations = _build_parcel_zone_interpretations(
        index,
        structure,
        policy,
        policy_hash,
        relation_copy,
        source_policy,
    )
    parcel_output = _build_parcel_output(
        parcel_copy,
        relation_copy,
        interpretations,
        policy,
        policy_hash,
    )
    relation_columns = tuple(str(column) for column in relation_copy.columns)
    result = BessZoningPrecheckResult(
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        policy_schema_version=policy.schema_version,
        policy_profile=policy.policy_profile,
        planning_precheck_scope=PLANNING_PRECHECK_SCOPE,
        review_scope=REVIEW_SCOPE,
        document_id=index.document_id,
        archive_sha256=index.archive_sha256,
        pdf_sha256=index.pdf_sha256,
        index_content_sha256=index.index_content_sha256,
        structure_result_content_sha256=structure.structure_result_content_sha256,
        structure_profile=structure.structure_profile,
        policy_config_sha256=policy_hash,
        factual_structure_content_sha256=_factual_structure_sha256(structure),
        zone_mapping_input_sha256=_zone_mapping_input_sha256(zone_copy, structure),
        zoning_relation_hash_columns=relation_columns,
        zoning_relations_input_sha256=_frame_sha256(
            "landscout.bess_zoning.zoning_relations_input",
            relation_copy,
            relation_columns,
        ),
        evidence_catalog_content_sha256="",
        evidence_route_links_content_sha256="",
        route_assessments_content_sha256="",
        chapter_policy_content_sha256="",
        source_zone_policy_content_sha256="",
        parcel_zone_policy_content_sha256="",
        parcel_output_content_sha256="",
        complete_result_content_sha256="",
        touch_only_relation_count=int(
            relation_copy["relation_type"].eq("TOUCH_ONLY").sum()
        ),
        evidence_catalog=evidence_catalog,
        evidence_route_links=evidence_route_links,
        route_assessments=route_assessments,
        chapter_policy=chapter_policy,
        source_zone_policy=source_policy,
        parcel_zone_interpretations=interpretations,
        parcels=parcel_output,
    )
    return _result_with_hashes(result)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_frames`

**Exact signature**

```python
def _compare_frames(
    actual: pd.DataFrame,
    expected: pd.DataFrame,
    columns: Sequence[str],
    label: str,
) -> None:
```

**Purpose**

Private `planning` helper for compare frames; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `tuple(actual.columns) != tuple(expected.columns) or tuple(actual.columns) != tuple(columns)`.
- Guard with a raise path: `_canonical_value(_frame_payload(actual, columns)) != _canonical_value(_frame_payload(expected, columns))`.
- Explicit raise expressions: `BessZoningPrecheckError(f'{label} differs from rebuilt source evidence')`, `BessZoningPrecheckError(f'{label} schema differs from rebuilt result')`.

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

- direct call: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_compare_frames`.

**Complete source-ordered implementation**

```python
def _compare_frames(
    actual: pd.DataFrame,
    expected: pd.DataFrame,
    columns: Sequence[str],
    label: str,
) -> None:
    if tuple(actual.columns) != tuple(expected.columns) or tuple(actual.columns) != tuple(columns):
        raise BessZoningPrecheckError(f"{label} schema differs from rebuilt result")
    if _canonical_value(_frame_payload(actual, columns)) != _canonical_value(
        _frame_payload(expected, columns)
    ):
        raise BessZoningPrecheckError(f"{label} differs from rebuilt source evidence")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_results`

**Exact signature**

```python
def _compare_results(
    result: BessZoningPrecheckResult,
    expected: BessZoningPrecheckResult,
    original_parcels: gpd.GeoDataFrame,
) -> None:
```

**Purpose**

Private `planning` helper for compare results; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(result, BessZoningPrecheckResult)`.
- Guard with a raise path: `_strict_positive_integer(result.result_hash_schema_version, 'precheck result hash schema version') != RESULT_HASH_SCHEMA_VERSION`.
- Guard with a raise path: `_strict_positive_integer(result.policy_schema_version, 'precheck policy schema version') != POLICY_SCHEMA_VERSION`.
- Guard with a raise path: `type(result.zoning_relation_hash_columns) is not tuple or not all((isinstance(column, str) and column and (column == column.strip()) for column in result.zoning_relation_hash_columns))`.
- Guard with a raise path: `tuple(result.parcels.columns[:len(original_columns)]) != original_columns`.
- Guard with a raise path: `_canonical_value(_frame_payload(result.parcels, original_columns)) != _canonical_value(_frame_payload(original_parcels, original_columns))`.
- Guard with a raise path: `not statuses.issubset(_CHAPTER_STATUSES)`.
- Guard with a raise path: `not parcel_statuses.issubset(_PARCEL_STATUSES)`.
- Guard with a raise path: `not confidences.issubset(_CONFIDENCES)`.
- Guard with a raise path: `len(actual_links) != len(result.evidence_route_links) or actual_links != expected_links`.
- Guard with a raise path: `not result.parcels['zoning_precheck_requires_formal_review'].eq(True).all()`.
- Guard with a raise path: `not result.parcels['non_zoning_planning_features_interpreted'].eq(False).all()`.
- Guard with a raise path: `not result.parcels['review_scope'].eq(REVIEW_SCOPE).all()`.
- Guard with a raise path: `getattr(result, field) != getattr(expected, field)`.
- Guard with a raise path: `evidence_id not in catalog_by_id`.
- Guard with a raise path: `tuple(row['linked_route_ids']) != tuple((item[0] for item in links))`.
- Guard with a raise path: `tuple(row['linked_route_roles']) != tuple((item[1] for item in links))`.
- Guard with a raise path: `bool(row['decision_linked']) != bool(links)`.
- Guard with a raise path: `row['evidence_direction'] == 'CONTEXT_ONLY'`.
- Guard with a raise path: `not set(row['zoning_precheck_evidence_ids']).issubset(decision_ids)`.
- Guard with a raise path: `not set(row['zoning_precheck_context_evidence_ids']).issubset(context_ids)`.
- Guard with a raise path: `not isinstance(values, (tuple, list, np.ndarray))`.
- Guard with a raise path: `links`.
- Guard with a raise path: `not links`.
- Guard with a raise path: `not isinstance(values, (tuple, list, np.ndarray))`.
- Guard with a raise path: `not set(values).issubset(evidence_ids)`.
- Guard with a raise path: `set(row['decision_evidence_ids']) != retained.intersection(decision_ids)`.
- Guard with a raise path: `set(row['context_evidence_ids']) != retained.intersection(context_ids)`.
- Explicit raise expressions: `BessZoningPrecheckError('An output evidence ID is absent from the evidence catalog')`, `BessZoningPrecheckError('CONTEXT_ONLY evidence must not influence a route')`, `BessZoningPrecheckError('Chapter policy confidence is invalid')`, `BessZoningPrecheckError('Chapter policy status is invalid')`, `BessZoningPrecheckError('Context evidence output is inconsistent')`, `BessZoningPrecheckError('Decision evidence must be linked to a route')`, `BessZoningPrecheckError('Decision evidence output is inconsistent')`, `BessZoningPrecheckError('Every parcel must require formal review')`, `BessZoningPrecheckError('Evidence references must be arrays')`, `BessZoningPrecheckError('Evidence reverse decision link is inconsistent')`, `BessZoningPrecheckError('Evidence reverse route IDs are inconsistent')`, `BessZoningPrecheckError('Evidence reverse route roles are inconsistent')`, `BessZoningPrecheckError('Evidence-route link references unknown evidence')`, `BessZoningPrecheckError('Evidence-route links do not exactly reproduce route evidence arrays')`, `BessZoningPrecheckError('Existing parcel columns are not preserved')`, `BessZoningPrecheckError('Non-zoning planning features must remain uninterpreted')`, `BessZoningPrecheckError('Parcel context evidence includes a decision')`, `BessZoningPrecheckError('Parcel count, IDs, order, index, geometry, CRS, or prior fields changed')`, `BessZoningPrecheckError('Parcel decision evidence includes context')`, `BessZoningPrecheckError('Parcel precheck status is invalid')`, `BessZoningPrecheckError('Parcel review scope is invalid')`, `BessZoningPrecheckError('Route evidence IDs must be arrays')`, `BessZoningPrecheckError('Unsupported precheck policy schema')`, `BessZoningPrecheckError('Unsupported precheck result hash schema')`, `BessZoningPrecheckError('Zoning relation hash columns must be an exact string tuple')`, `BessZoningPrecheckError('result must be a BessZoningPrecheckResult')`, `BessZoningPrecheckError(f'BESS zoning result {field} differs from rebuilt source evidence')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `retained.intersection`.
- Hashing: `_validated_sha256`.
- Environment/process effects: none.
- In-memory mutation: `context_ids`, `decision_ids`, `expected_links`, `reverse_links`, `reverse_links.setdefault(evidence_id, [])`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/interpret_bess_zoning.py::validate_bess_zoning_precheck` via `_compare_results`.
- direct call: `src/landscout/stages/interpret_bess_zoning.py::interpret_bess_zoning` via `_compare_results`.

**Complete source-ordered implementation**

```python
def _compare_results(
    result: BessZoningPrecheckResult,
    expected: BessZoningPrecheckResult,
    original_parcels: gpd.GeoDataFrame,
) -> None:
    if not isinstance(result, BessZoningPrecheckResult):
        raise BessZoningPrecheckError("result must be a BessZoningPrecheckResult")
    _validate_evidence_occurrence_uniqueness(result.evidence_catalog)
    scalar_fields = (
        "result_hash_schema_version",
        "policy_schema_version",
        "policy_profile",
        "planning_precheck_scope",
        "review_scope",
        "document_id",
        "archive_sha256",
        "pdf_sha256",
        "index_content_sha256",
        "structure_result_content_sha256",
        "structure_profile",
        "policy_config_sha256",
        "factual_structure_content_sha256",
        "zone_mapping_input_sha256",
        "zoning_relation_hash_columns",
        "zoning_relations_input_sha256",
        "evidence_catalog_content_sha256",
        "evidence_route_links_content_sha256",
        "route_assessments_content_sha256",
        "chapter_policy_content_sha256",
        "source_zone_policy_content_sha256",
        "parcel_zone_policy_content_sha256",
        "parcel_output_content_sha256",
        "complete_result_content_sha256",
        "touch_only_relation_count",
    )
    for field in scalar_fields:
        if getattr(result, field) != getattr(expected, field):
            raise BessZoningPrecheckError(
                f"BESS zoning result {field} differs from rebuilt source evidence"
            )
    if (
        _strict_positive_integer(
            result.result_hash_schema_version,
            "precheck result hash schema version",
        )
        != RESULT_HASH_SCHEMA_VERSION
    ):
        raise BessZoningPrecheckError("Unsupported precheck result hash schema")
    if (
        _strict_positive_integer(
            result.policy_schema_version,
            "precheck policy schema version",
        )
        != POLICY_SCHEMA_VERSION
    ):
        raise BessZoningPrecheckError("Unsupported precheck policy schema")
    _strict_nonnegative_integer(
        result.touch_only_relation_count,
        "touch-only relation count",
    )
    if type(result.zoning_relation_hash_columns) is not tuple or not all(
        isinstance(column, str) and column and column == column.strip()
        for column in result.zoning_relation_hash_columns
    ):
        raise BessZoningPrecheckError(
            "Zoning relation hash columns must be an exact string tuple"
        )
    for field in (
        "archive_sha256",
        "pdf_sha256",
        "index_content_sha256",
        "structure_result_content_sha256",
        "policy_config_sha256",
        "factual_structure_content_sha256",
        "zone_mapping_input_sha256",
        "zoning_relations_input_sha256",
        "evidence_catalog_content_sha256",
        "evidence_route_links_content_sha256",
        "route_assessments_content_sha256",
        "chapter_policy_content_sha256",
        "source_zone_policy_content_sha256",
        "parcel_zone_policy_content_sha256",
        "parcel_output_content_sha256",
        "complete_result_content_sha256",
    ):
        _validated_sha256(getattr(result, field), field)
    _compare_frames(
        result.evidence_catalog,
        expected.evidence_catalog,
        EVIDENCE_CATALOG_COLUMNS,
        "evidence catalog",
    )
    _compare_frames(
        result.evidence_route_links,
        expected.evidence_route_links,
        EVIDENCE_ROUTE_LINK_COLUMNS,
        "evidence-route links",
    )
    _compare_frames(
        result.route_assessments,
        expected.route_assessments,
        ROUTE_ASSESSMENT_COLUMNS,
        "route assessments",
    )
    _compare_frames(
        result.chapter_policy,
        expected.chapter_policy,
        CHAPTER_POLICY_COLUMNS,
        "chapter policy",
    )
    _compare_frames(
        result.source_zone_policy,
        expected.source_zone_policy,
        SOURCE_ZONE_POLICY_COLUMNS,
        "source-zone policy",
    )
    _compare_frames(
        result.parcel_zone_interpretations,
        expected.parcel_zone_interpretations,
        PARCEL_ZONE_POLICY_COLUMNS,
        "parcel/zone policy",
    )
    _compare_frames(
        result.parcels,
        expected.parcels,
        tuple(expected.parcels.columns),
        "parcel precheck",
    )
    original_columns = tuple(original_parcels.columns)
    if tuple(result.parcels.columns[: len(original_columns)]) != original_columns:
        raise BessZoningPrecheckError("Existing parcel columns are not preserved")
    if _canonical_value(_frame_payload(result.parcels, original_columns)) != _canonical_value(
        _frame_payload(original_parcels, original_columns)
    ):
        raise BessZoningPrecheckError(
            "Parcel count, IDs, order, index, geometry, CRS, or prior fields changed"
        )
    statuses = set(result.chapter_policy["zoning_precheck_status"].tolist())
    parcel_statuses = set(result.parcels["zoning_precheck_status"].tolist())
    confidences = set(
        result.chapter_policy["zoning_precheck_confidence"].tolist()
    )
    if not statuses.issubset(_CHAPTER_STATUSES):
        raise BessZoningPrecheckError("Chapter policy status is invalid")
    if not parcel_statuses.issubset(_PARCEL_STATUSES):
        raise BessZoningPrecheckError("Parcel precheck status is invalid")
    if not confidences.issubset(_CONFIDENCES):
        raise BessZoningPrecheckError("Chapter policy confidence is invalid")
    evidence_ids = set(
        _exact_id_series(
            result.evidence_catalog["evidence_id"],
            "catalog evidence ID",
            unique=True,
        )
    )
    catalog_by_id = result.evidence_catalog.set_index("evidence_id").to_dict("index")
    expected_links: set[tuple[str, str, str, str]] = set()
    role_fields = (
        ("positive_evidence_ids", "POSITIVE", "SUPPORTS_POTENTIAL_COMPATIBILITY"),
        ("condition_evidence_ids", "CONDITION", "CONDITION"),
        ("difficulty_evidence_ids", "DIFFICULTY", "SUPPORTS_DIFFICULTY"),
    )
    for route in result.route_assessments.to_dict("records"):
        for field, role, direction in role_fields:
            values = route[field]
            if not isinstance(values, (tuple, list, np.ndarray)):
                raise BessZoningPrecheckError("Route evidence IDs must be arrays")
            for evidence_id in values:
                expected_links.add((route["route_id"], evidence_id, role, direction))
    actual_links = {
        (
            row["route_id"],
            row["evidence_id"],
            row["route_role"],
            row["evidence_direction"],
        )
        for row in result.evidence_route_links.to_dict("records")
    }
    if len(actual_links) != len(result.evidence_route_links) or actual_links != expected_links:
        raise BessZoningPrecheckError(
            "Evidence-route links do not exactly reproduce route evidence arrays"
        )
    reverse_links: dict[str, list[tuple[str, str]]] = {}
    for route_id, evidence_id, role, _ in actual_links:
        if evidence_id not in catalog_by_id:
            raise BessZoningPrecheckError(
                "Evidence-route link references unknown evidence"
            )
        reverse_links.setdefault(evidence_id, []).append((route_id, role))
    decision_ids: set[str] = set()
    context_ids: set[str] = set()
    for evidence_id, row in catalog_by_id.items():
        links = tuple(sorted(reverse_links.get(evidence_id, [])))
        if tuple(row["linked_route_ids"]) != tuple(item[0] for item in links):
            raise BessZoningPrecheckError("Evidence reverse route IDs are inconsistent")
        if tuple(row["linked_route_roles"]) != tuple(item[1] for item in links):
            raise BessZoningPrecheckError("Evidence reverse route roles are inconsistent")
        if bool(row["decision_linked"]) != bool(links):
            raise BessZoningPrecheckError("Evidence reverse decision link is inconsistent")
        if row["evidence_direction"] == "CONTEXT_ONLY":
            context_ids.add(evidence_id)
            if links:
                raise BessZoningPrecheckError(
                    "CONTEXT_ONLY evidence must not influence a route"
                )
        else:
            decision_ids.add(evidence_id)
            if not links:
                raise BessZoningPrecheckError(
                    "Decision evidence must be linked to a route"
                )
    for frame, column in (
        (result.chapter_policy, "evidence_ids"),
        (result.source_zone_policy, "evidence_ids"),
        (result.parcel_zone_interpretations, "evidence_ids"),
        (result.parcels, "zoning_precheck_evidence_ids"),
    ):
        for values in frame[column].tolist():
            if not isinstance(values, (tuple, list, np.ndarray)):
                raise BessZoningPrecheckError("Evidence references must be arrays")
            if not set(values).issubset(evidence_ids):
                raise BessZoningPrecheckError(
                    "An output evidence ID is absent from the evidence catalog"
                )
    for frame in (
        result.chapter_policy,
        result.source_zone_policy,
        result.parcel_zone_interpretations,
    ):
        for row in frame.to_dict("records"):
            retained = set(row["evidence_ids"])
            if set(row["decision_evidence_ids"]) != retained.intersection(decision_ids):
                raise BessZoningPrecheckError("Decision evidence output is inconsistent")
            if set(row["context_evidence_ids"]) != retained.intersection(context_ids):
                raise BessZoningPrecheckError("Context evidence output is inconsistent")
    for row in result.parcels.to_dict("records"):
        if not set(row["zoning_precheck_evidence_ids"]).issubset(decision_ids):
            raise BessZoningPrecheckError("Parcel decision evidence includes context")
        if not set(row["zoning_precheck_context_evidence_ids"]).issubset(context_ids):
            raise BessZoningPrecheckError("Parcel context evidence includes a decision")
    if not result.parcels["zoning_precheck_requires_formal_review"].eq(True).all():
        raise BessZoningPrecheckError("Every parcel must require formal review")
    if not result.parcels["non_zoning_planning_features_interpreted"].eq(False).all():
        raise BessZoningPrecheckError(
            "Non-zoning planning features must remain uninterpreted"
        )
    if not result.parcels["review_scope"].eq(REVIEW_SCOPE).all():
        raise BessZoningPrecheckError("Parcel review scope is invalid")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_bess_zoning_precheck`

**Exact signature**

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

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessZoningPrecheckError('BESS zoning precheck validation failed safely')`, `BessZoningPrecheckError(f'Factual GPU zoning validation failed: {error}')`, `BessZoningPrecheckError(f'Factual regulation structure validation failed: {error}')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`.
- import: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.interpret_bess_zoning import (
    CHAPTER_POLICY_COLUMNS,
    EVIDENCE_CATALOG_COLUMNS,
    EVIDENCE_ROUTE_LINK_COLUMNS,
    PARCEL_ZONE_POLICY_COLUMNS,
    ROUTE_ASSESSMENT_COLUMNS,
    SOURCE_ZONE_POLICY_COLUMNS,
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    _result_with_hashes,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::_validate` via `validate_bess_zoning_precheck`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_source_complete_validator_rejects_later_duplicate_chapter` via `validate_bess_zoning_precheck`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_policy_change_after_result_creation_is_rejected` via `validate_bess_zoning_precheck`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_evidence_change_after_result_creation_is_rejected` via `validate_bess_zoning_precheck`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_zoning_relation_and_zone_mapping_changes_are_rejected` via `validate_bess_zoning_precheck`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_factual_zone_mapping_counts_are_recomputed` via `validate_bess_zoning_precheck`.

**Complete source-ordered implementation**

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
    """Rebuild and validate the precheck from every factual and policy input."""

    try:
        validate_normalized_planning_zoning_inputs(
            planning_document,
            parcels,
            zones,  # type: ignore[arg-type]
            zoning_intersections,
        )
        resolved_policy = _resolved_policy(policy)
        expected = _build_result(
            index,
            structure,
            structure_config,
            zones,
            zoning_intersections,
            parcels,
            resolved_policy,
        )
        _compare_results(result, expected, parcels)
    except BessZoningPrecheckError:
        raise
    except PlanningRegulationStructureError as error:
        raise BessZoningPrecheckError(
            f"Factual regulation structure validation failed: {error}"
        ) from error
    except PlanningZoningError as error:
        raise BessZoningPrecheckError(
            f"Factual GPU zoning validation failed: {error}"
        ) from error
    except Exception as error:
        raise BessZoningPrecheckError(
            "BESS zoning precheck validation failed safely"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `interpret_bess_zoning`

**Exact signature**

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

**Return contract**

- Declared return annotation: `BessZoningPrecheckResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessZoningPrecheckError('BESS zoning precheck could not be built safely')`, `BessZoningPrecheckError(f'Factual GPU zoning validation failed: {error}')`, `BessZoningPrecheckError(f'Factual regulation structure validation failed: {error}')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`.
- import: `tests/unit/test_interpret_bess_zoning.py::<module>` via `from landscout.stages.interpret_bess_zoning import (
    CHAPTER_POLICY_COLUMNS,
    EVIDENCE_CATALOG_COLUMNS,
    EVIDENCE_ROUTE_LINK_COLUMNS,
    PARCEL_ZONE_POLICY_COLUMNS,
    ROUTE_ASSESSMENT_COLUMNS,
    SOURCE_ZONE_POLICY_COLUMNS,
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    _result_with_hashes,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::valid_result` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_source_lock_mismatch_is_rejected` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_missing_and_extra_chapter_are_rejected` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_source_rule_identity_and_containment_are_strict` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_absent_excerpt_and_section_page_mismatch_are_rejected` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_one_evidence_may_link_to_multiple_compatible_routes` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_incomplete_review_persists_exact_missing_required_sections` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_unknown_is_accepted_when_evidence_is_insufficient` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_reviewed_sections_cover_required_articles` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_evidence_must_be_inside_reviewed_sections` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_review_cannot_claim_another_chapter_section` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_general_section_review_is_explicit_and_valid` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_same_general_occurrence_may_be_scoped_to_different_chapters` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_wrong_occurrence_identity_is_rejected` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_unmapped_dominant_zone_is_rejected` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_context_evidence_is_separate_from_decision_outputs` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_inputs_are_not_mutated` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_structure_config_and_hierarchy_changes_are_rejected` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_public_source_complete_validator_is_invoked` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_invalid_physical_zoning_fails_before_policy_interpretation` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_relation_area_denominators_are_required` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_relation_percentages_must_match_denominators` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_factual_zone_mapping_counts_are_recomputed` via `interpret_bess_zoning`.
- direct call: `tests/unit/test_interpret_bess_zoning.py::test_relation_identity_change_is_rejected` via `interpret_bess_zoning`.

**Complete source-ordered implementation**

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
    """Build a conservative written-zoning precheck without rejecting parcels."""

    try:
        validate_normalized_planning_zoning_inputs(
            planning_document,
            parcels,
            zones,  # type: ignore[arg-type]
            zoning_intersections,
        )
        resolved_policy = _resolved_policy(policy)
        result = _build_result(
            index,
            structure,
            structure_config,
            zones,
            zoning_intersections,
            parcels,
            resolved_policy,
        )
        _compare_results(result, result, parcels)
        return result
    except BessZoningPrecheckError:
        raise
    except PlanningRegulationStructureError as error:
        raise BessZoningPrecheckError(
            f"Factual regulation structure validation failed: {error}"
        ) from error
    except PlanningZoningError as error:
        raise BessZoningPrecheckError(
            f"Factual GPU zoning validation failed: {error}"
        ) from error
    except Exception as error:
        raise BessZoningPrecheckError(
            "BESS zoning precheck could not be built safely"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


## 7. Data contracts

### Frame-preservation and semantic notes

- `_route_status` is deterministic written-zoning policy logic: RouteKind values map to ChapterStatus values. It is a planning precheck interpretation and explicitly is not authorization, prohibition, or proof that unresolved BESS/ICPE conditions are satisfied.
- `crs` and `geometry_column` appearing in hash/signature payload mappings are mapping keys, not result-frame columns.

### `CHAPTER_POLICY_COLUMNS` — canonical or derived frame-column schema

```python
CHAPTER_POLICY_COLUMNS = (
    "resolved_zone_chapter_label",
    "chapter_section_id",
    "review_completeness",
    "review_scope",
    "reviewed_section_ids",
    "missing_required_section_ids",
    "review_note",
    "zoning_precheck_status",
    "zoning_precheck_confidence",
    "evidence_count",
    "evidence_ids",
    "decision_evidence_ids",
    "context_evidence_ids",
    "rationale",
    "missing_information",
    "planning_precheck_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `resolved_zone_chapter_label` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `chapter_section_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 3 | `review_completeness` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `review_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `reviewed_section_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `missing_required_section_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `review_note` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `zoning_precheck_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 9 | `zoning_precheck_confidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `evidence_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 11 | `evidence_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 12 | `decision_evidence_ids` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 13 | `context_evidence_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `rationale` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 15 | `missing_information` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 16 | `planning_precheck_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 17 | `policy_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 18 | `policy_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 19 | `document_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 20 | `archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 21 | `pdf_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 22 | `index_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 23 | `structure_result_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 24 | `structure_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `EVIDENCE_CATALOG_COLUMNS` — canonical or derived frame-column schema

```python
EVIDENCE_CATALOG_COLUMNS = (
    "evidence_id",
    "resolved_zone_chapter_label",
    "section_id",
    "page_number",
    "evidence_kind",
    "evidence_direction",
    "linked_route_ids",
    "linked_route_roles",
    "decision_linked",
    "exact_raw_excerpt",
    "excerpt_sha256",
    "section_page_fragment_sha256",
    "excerpt_start",
    "excerpt_end",
    "source_rule_id",
    "source_rule_excerpt",
    "source_rule_sha256",
    "source_rule_start",
    "source_rule_end",
    "interpretation_note",
    "review_completeness",
    "review_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `evidence_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `resolved_zone_chapter_label` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `section_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 4 | `page_number` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `evidence_kind` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `evidence_direction` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `linked_route_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `linked_route_roles` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `decision_linked` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 10 | `exact_raw_excerpt` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 11 | `excerpt_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 12 | `section_page_fragment_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 13 | `excerpt_start` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `excerpt_end` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 15 | `source_rule_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `source_rule_excerpt` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 17 | `source_rule_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 18 | `source_rule_start` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 19 | `source_rule_end` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 20 | `interpretation_note` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 21 | `review_completeness` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 22 | `review_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 23 | `policy_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 24 | `policy_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 25 | `document_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 26 | `archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 27 | `pdf_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 28 | `index_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 29 | `structure_result_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 30 | `structure_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `_EVIDENCE_OCCURRENCE_COLUMNS` — canonical or derived frame-column schema

```python
_EVIDENCE_OCCURRENCE_COLUMNS = (
    "resolved_zone_chapter_label",
    "section_id",
    "page_number",
    "section_page_fragment_sha256",
    "excerpt_start",
    "excerpt_end",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `resolved_zone_chapter_label` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `section_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 3 | `page_number` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `section_page_fragment_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 5 | `excerpt_start` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `excerpt_end` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `ROUTE_ASSESSMENT_COLUMNS` — canonical or derived frame-column schema

```python
ROUTE_ASSESSMENT_COLUMNS = (
    "route_id",
    "resolved_zone_chapter_label",
    "route_kind",
    "derived_route_status",
    "positive_evidence_ids",
    "condition_evidence_ids",
    "difficulty_evidence_ids",
    "applicability_note",
    "review_completeness",
    "review_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `route_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `resolved_zone_chapter_label` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `route_kind` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `derived_route_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 5 | `positive_evidence_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `condition_evidence_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `difficulty_evidence_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `applicability_note` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `review_completeness` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `review_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 11 | `policy_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 12 | `policy_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 13 | `document_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 14 | `archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 15 | `pdf_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 16 | `index_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 17 | `structure_result_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 18 | `structure_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `EVIDENCE_ROUTE_LINK_COLUMNS` — canonical or derived frame-column schema

```python
EVIDENCE_ROUTE_LINK_COLUMNS = (
    "route_id",
    "resolved_zone_chapter_label",
    "route_kind",
    "evidence_id",
    "route_role",
    "evidence_direction",
    "review_completeness",
    "review_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `route_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `resolved_zone_chapter_label` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `route_kind` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `evidence_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 5 | `route_role` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `evidence_direction` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `review_completeness` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `review_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `policy_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `policy_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 11 | `document_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 12 | `archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 13 | `pdf_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 14 | `index_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 15 | `structure_result_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 16 | `structure_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `SOURCE_ZONE_POLICY_COLUMNS` — canonical or derived frame-column schema

```python
SOURCE_ZONE_POLICY_COLUMNS = (
    "source_zone_label_raw",
    "resolved_zone_chapter_label",
    "mapping_status",
    "matched_section_id",
    "source_layer",
    "zoning_precheck_status",
    "zoning_precheck_confidence",
    "evidence_ids",
    "decision_evidence_ids",
    "context_evidence_ids",
    "review_scope",
    "planning_precheck_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `source_zone_label_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `resolved_zone_chapter_label` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `mapping_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `matched_section_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 5 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 6 | `zoning_precheck_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 7 | `zoning_precheck_confidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `evidence_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `decision_evidence_ids` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 10 | `context_evidence_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 11 | `review_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 12 | `planning_precheck_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 13 | `policy_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `policy_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 15 | `document_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 16 | `archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 17 | `pdf_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 18 | `index_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 19 | `structure_result_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 20 | `structure_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `PARCEL_ZONE_POLICY_COLUMNS` — canonical or derived frame-column schema

```python
PARCEL_ZONE_POLICY_COLUMNS = (
    "parcel_id",
    "planning_zone_id",
    "source_zone_id",
    "source_zone_label_raw",
    "resolved_zone_chapter_label",
    "intersection_area_m2",
    "parcel_share_pct",
    "zoning_precheck_status",
    "zoning_precheck_confidence",
    "evidence_ids",
    "decision_evidence_ids",
    "context_evidence_ids",
    "review_scope",
    "planning_precheck_scope",
    "policy_profile",
    "policy_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_result_content_sha256",
    "structure_profile",
    "source_layer",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `parcel_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 2 | `planning_zone_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 3 | `source_zone_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `source_zone_label_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 5 | `resolved_zone_chapter_label` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `intersection_area_m2` | float64 when builder initializes NaN/numeric metric; otherwise exact source numeric dtype shown by implementation | null only on the explicit no-measurement/invalid path | geometry metric | Square-metre geometry measurement; not a policy threshold unless the field belongs to configuration. |
| 7 | `parcel_share_pct` | builder/source numeric dtype shown by the implementation; no cast is inferred from the name | null on explicit no-match/unknown paths | derived fact or proxy metric | Numeric evidence in the unit encoded by the suffix; it does not establish legal/capacity suitability. |
| 8 | `zoning_precheck_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 9 | `zoning_precheck_confidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `evidence_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 11 | `decision_evidence_ids` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 12 | `context_evidence_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 13 | `review_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `planning_precheck_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 15 | `policy_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 16 | `policy_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 17 | `document_id` | source/build string dtype shown by the implementation | non-null for owning rows; nearest-match IDs may be null on no-match | identity | Identity for the named entity; portability/uniqueness are only those explicitly validated. |
| 18 | `archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 19 | `pdf_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 20 | `index_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 21 | `structure_result_content_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 22 | `structure_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 23 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |

### `PARCEL_PRECHECK_COLUMNS` — canonical or derived frame-column schema

```python
PARCEL_PRECHECK_COLUMNS = (
    "zoning_precheck_status",
    "dominant_zone_precheck_status",
    "dominant_zone_precheck_confidence",
    "positive_area_zone_count",
    "distinct_zone_status_count",
    "non_dominant_different_status_count",
    "touch_only_zone_count",
    "zoning_precheck_evidence_ids",
    "zoning_precheck_context_evidence_ids",
    "zoning_precheck_requires_formal_review",
    "planning_precheck_scope",
    "review_scope",
    "non_zoning_planning_features_interpreted",
    "zoning_precheck_policy_profile",
    "zoning_precheck_policy_sha256",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `zoning_precheck_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 2 | `dominant_zone_precheck_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 3 | `dominant_zone_precheck_confidence` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `positive_area_zone_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 5 | `distinct_zone_status_count` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 6 | `non_dominant_different_status_count` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 7 | `touch_only_zone_count` | builder/source integer dtype shown by the implementation | null only where the schema expressly represents no match | derived count | Count of the entity named by the field; it is not a score. |
| 8 | `zoning_precheck_evidence_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `zoning_precheck_context_evidence_ids` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 10 | `zoning_precheck_requires_formal_review` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 11 | `planning_precheck_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 12 | `review_scope` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 13 | `non_zoning_planning_features_interpreted` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 14 | `zoning_precheck_policy_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 15 | `zoning_precheck_policy_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `BessZoningPolicyConfig` | public symbol defined in this module | `defined in `src/landscout/stages/interpret_bess_zoning.py`` | yes |
| `BessZoningPrecheckError` | public symbol defined in this module | `defined in `src/landscout/stages/interpret_bess_zoning.py`` | yes |
| `BessZoningPrecheckResult` | public symbol defined in this module | `defined in `src/landscout/stages/interpret_bess_zoning.py`` | yes |
| `interpret_bess_zoning` | public symbol defined in this module | `defined in `src/landscout/stages/interpret_bess_zoning.py`` | yes |
| `load_bess_zoning_policy_config` | public symbol defined in this module | `defined in `src/landscout/stages/interpret_bess_zoning.py`` | yes |
| `validate_bess_zoning_precheck` | public symbol defined in this module | `defined in `src/landscout/stages/interpret_bess_zoning.py`` | yes |

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

The module contributes to the planning flow through the exact facts, proxy evidence, policy results, diagnostics, or prechecks identified above.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Test consumers and framework invocation are included in per-symbol interfaces. Test modules distinguish fixture injection from parameterized values and reproduce setup/action/assertion source.

## 17. Change impact

Any source-byte change invalidates the SHA above. Review exact exports, aliases, canonical frame schemas/dtypes, configured source/policy identities, callers, framework hooks, artifacts, and all linked tests before updating this companion.
