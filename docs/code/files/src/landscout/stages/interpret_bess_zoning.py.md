# `src/landscout/stages/interpret_bess_zoning.py`

## File identity

- Repository path: `src/landscout/stages/interpret_bess_zoning.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.
- Source SHA256: `b60434426a981dab3dcd000a4fc9e745202984672f8e96bc4ea8aa661c86682e`

## 1. STEP 7F.1A.4 contract delta

- Requires exactly one source-closed child section for every configured required article in every configured zone chapter.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

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
- `from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, model_validator`
- `from pyproj import CRS`
- `from shapely import to_wkb`
- `from shapely.geometry.base import BaseGeometry`

### Internal LandScout imports

- `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
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

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `BessZoningPolicyConfig`
  - `BessZoningPrecheckError`
  - `BessZoningPrecheckResult`
  - `interpret_bess_zoning`
  - `load_bess_zoning_policy_config`
  - `validate_bess_zoning_precheck`

### `POLICY_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
POLICY_SCHEMA_VERSION = 5
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `RESULT_HASH_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
RESULT_HASH_SCHEMA_VERSION = 5
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PLANNING_PRECHECK_SCOPE`

- Category: module constant or closed domain.
- Exact declaration:

```python
PLANNING_PRECHECK_SCOPE = "WRITTEN_ZONING_REGULATION_ONLY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `REVIEW_SCOPE`

- Category: module constant or closed domain.
- Exact declaration:

```python
REVIEW_SCOPE = "CONFIGURED_USE_CONTROL_ARTICLES_ONLY"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ChapterStatus`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
ChapterStatus = Literal[
    "POTENTIALLY_COMPATIBLE",
    "CONDITIONAL_REVIEW",
    "LIKELY_DIFFICULT",
    "UNKNOWN",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `Confidence`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
Confidence = Literal["HIGH", "MEDIUM", "LOW"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `ReviewCompleteness`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
ReviewCompleteness = Literal[
    "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES", "INCOMPLETE"
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `RouteKind`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
RouteKind = Literal[
    "DIRECT_ROUTE",
    "CONDITIONAL_ROUTE",
    "RESTRICTION_EXCEPTION_ROUTE",
    "DIFFICULTY_ONLY",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EvidenceKind`

- Category: type alias or closed annotated domain.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `EvidenceDirection`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
EvidenceDirection = Literal[
    "SUPPORTS_POTENTIAL_COMPATIBILITY",
    "SUPPORTS_DIFFICULTY",
    "CONDITION",
    "CONTEXT_ONLY",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_CHAPTER_STATUSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_CHAPTER_STATUSES = frozenset(
    {"POTENTIALLY_COMPATIBLE", "CONDITIONAL_REVIEW", "LIKELY_DIFFICULT", "UNKNOWN"}
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_PARCEL_STATUSES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_PARCEL_STATUSES = _CHAPTER_STATUSES | {"MIXED_REVIEW_REQUIRED"}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_CONFIDENCES`

- Category: module constant or closed domain.
- Exact declaration:

```python
_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_RESOLVED_MAPPING_STATUSES`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
_RESOLVED_MAPPING_STATUSES = frozenset({"EXACT", "CONFIG_ALIAS"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CHAPTER_POLICY_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
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
)`
  - value/type reference: `tests.unit.test_interpret_bess_zoning::test_valid_locked_policy_builds_complete_outputs` via `CHAPTER_POLICY_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `resolved_zone_chapter_label`
  - `chapter_section_id`
  - `review_completeness`
  - `review_scope`
  - `reviewed_section_ids`
  - `missing_required_section_ids`
  - `review_note`
  - `zoning_precheck_status`
  - `zoning_precheck_confidence`
  - `evidence_count`
  - `evidence_ids`
  - `decision_evidence_ids`
  - `context_evidence_ids`
  - `rationale`
  - `missing_information`
  - `planning_precheck_scope`
  - `policy_profile`
  - `policy_sha256`
  - `document_id`
  - `archive_sha256`
  - `pdf_sha256`
  - `index_content_sha256`
  - `structure_result_content_sha256`
  - `structure_profile`

### `EVIDENCE_CATALOG_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
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
)`
  - value/type reference: `tests.unit.test_interpret_bess_zoning::test_valid_locked_policy_builds_complete_outputs` via `EVIDENCE_CATALOG_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `evidence_id`
  - `resolved_zone_chapter_label`
  - `section_id`
  - `page_number`
  - `evidence_kind`
  - `evidence_direction`
  - `linked_route_ids`
  - `linked_route_roles`
  - `decision_linked`
  - `exact_raw_excerpt`
  - `excerpt_sha256`
  - `section_page_fragment_sha256`
  - `excerpt_start`
  - `excerpt_end`
  - `source_rule_id`
  - `source_rule_excerpt`
  - `source_rule_sha256`
  - `source_rule_start`
  - `source_rule_end`
  - `interpretation_note`
  - `review_completeness`
  - `review_scope`
  - `policy_profile`
  - `policy_sha256`
  - `document_id`
  - `archive_sha256`
  - `pdf_sha256`
  - `index_content_sha256`
  - `structure_result_content_sha256`
  - `structure_profile`

### `_EVIDENCE_OCCURRENCE_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `resolved_zone_chapter_label`
  - `section_id`
  - `page_number`
  - `section_page_fragment_sha256`
  - `excerpt_start`
  - `excerpt_end`

### `ROUTE_ASSESSMENT_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
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
)`
  - value/type reference: `tests.unit.test_interpret_bess_zoning::test_valid_locked_policy_builds_complete_outputs` via `ROUTE_ASSESSMENT_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `route_id`
  - `resolved_zone_chapter_label`
  - `route_kind`
  - `derived_route_status`
  - `positive_evidence_ids`
  - `condition_evidence_ids`
  - `difficulty_evidence_ids`
  - `applicability_note`
  - `review_completeness`
  - `review_scope`
  - `policy_profile`
  - `policy_sha256`
  - `document_id`
  - `archive_sha256`
  - `pdf_sha256`
  - `index_content_sha256`
  - `structure_result_content_sha256`
  - `structure_profile`

### `EVIDENCE_ROUTE_LINK_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
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
)`
  - value/type reference: `tests.unit.test_interpret_bess_zoning::test_valid_locked_policy_builds_complete_outputs` via `EVIDENCE_ROUTE_LINK_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `route_id`
  - `resolved_zone_chapter_label`
  - `route_kind`
  - `evidence_id`
  - `route_role`
  - `evidence_direction`
  - `review_completeness`
  - `review_scope`
  - `policy_profile`
  - `policy_sha256`
  - `document_id`
  - `archive_sha256`
  - `pdf_sha256`
  - `index_content_sha256`
  - `structure_result_content_sha256`
  - `structure_profile`

### `SOURCE_ZONE_POLICY_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
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
)`
  - value/type reference: `tests.unit.test_interpret_bess_zoning::test_valid_locked_policy_builds_complete_outputs` via `SOURCE_ZONE_POLICY_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `source_zone_label_raw`
  - `resolved_zone_chapter_label`
  - `mapping_status`
  - `matched_section_id`
  - `source_layer`
  - `zoning_precheck_status`
  - `zoning_precheck_confidence`
  - `evidence_ids`
  - `decision_evidence_ids`
  - `context_evidence_ids`
  - `review_scope`
  - `planning_precheck_scope`
  - `policy_profile`
  - `policy_sha256`
  - `document_id`
  - `archive_sha256`
  - `pdf_sha256`
  - `index_content_sha256`
  - `structure_result_content_sha256`
  - `structure_profile`

### `PARCEL_ZONE_POLICY_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
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
)`
  - value/type reference: `tests.unit.test_interpret_bess_zoning::test_valid_locked_policy_builds_complete_outputs` via `PARCEL_ZONE_POLICY_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `parcel_id`
  - `planning_zone_id`
  - `source_zone_id`
  - `source_zone_label_raw`
  - `resolved_zone_chapter_label`
  - `intersection_area_m2`
  - `parcel_share_pct`
  - `zoning_precheck_status`
  - `zoning_precheck_confidence`
  - `evidence_ids`
  - `decision_evidence_ids`
  - `context_evidence_ids`
  - `review_scope`
  - `planning_precheck_scope`
  - `policy_profile`
  - `policy_sha256`
  - `document_id`
  - `archive_sha256`
  - `pdf_sha256`
  - `index_content_sha256`
  - `structure_result_content_sha256`
  - `structure_profile`
  - `source_layer`

### `PARCEL_PRECHECK_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

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

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `zoning_precheck_status`
  - `dominant_zone_precheck_status`
  - `dominant_zone_precheck_confidence`
  - `positive_area_zone_count`
  - `distinct_zone_status_count`
  - `non_dominant_different_status_count`
  - `touch_only_zone_count`
  - `zoning_precheck_evidence_ids`
  - `zoning_precheck_context_evidence_ids`
  - `zoning_precheck_requires_formal_review`
  - `planning_precheck_scope`
  - `review_scope`
  - `non_zoning_planning_features_interpreted`
  - `zoning_precheck_policy_profile`
  - `zoning_precheck_policy_sha256`


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `BessZoningPrecheckError`

**Source purpose:** Raised when the preliminary zoning interpretation cannot be proven.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`
- constructor call: `landscout.stages.interpret_bess_zoning::load_bess_zoning_policy_config` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::load_bess_zoning_policy_config` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_strict_string` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_strict_string` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_strict_nonnegative_integer` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_strict_nonnegative_integer` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_strict_positive_integer` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_strict_positive_integer` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_validated_sha256` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validated_sha256` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_strict_nonnegative_number` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_strict_nonnegative_number` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_canonical_value` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_canonical_value` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_canonical_sha256` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_canonical_sha256` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_frame_payload` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_frame_payload` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_resolved_policy` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_resolved_policy` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_validate_policy_lock` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_lock` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_exact_id_series` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_exact_id_series` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_validate_parcels` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_parcels` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_validate_zones` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_zones` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_validate_relations` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_relations` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_zone_chapter_rows` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_zone_chapter_rows` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_required_section_ids_by_chapter` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_required_section_ids_by_chapter` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_validate_evidence_occurrence_uniqueness` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_evidence_occurrence_uniqueness` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_validate_mapping` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_mapping` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_build_route_assessments` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_route_assessments` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_build_evidence_route_links` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_evidence_route_links` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_build_source_zone_policy` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_source_zone_policy` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_build_parcel_output` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_parcel_output` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_compare_frames` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_frames` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::_compare_results` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_results` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `BessZoningPrecheckError`
- constructor call: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `BessZoningPrecheckError`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `BessZoningPrecheckError`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    validate_bess_zoning_precheck,
)`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_source_byte_mutation_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_config_hash_mutation_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::test_physical_gpu_missing_required_article_is_rejected` via `BessZoningPrecheckError`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
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
)`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_lock_mismatch_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_missing_and_extra_chapter_are_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_regulation_zone_chapter_labels_and_ids_must_be_unique` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_complete_validator_rejects_later_duplicate_chapter` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_yaml_key_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_rule_identity_and_containment_are_strict` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_absent_excerpt_and_section_page_mismatch_are_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_reviewed_sections_cover_required_articles` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_every_configured_article_must_exist_once_in_every_chapter` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_configured_article_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_configured_article_with_wrong_chapter_parent_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_must_be_inside_reviewed_sections` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_review_cannot_claim_another_chapter_section` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_repeated_excerpt_occurrence_is_bound_to_policy` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_wrong_occurrence_identity_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unmapped_dominant_zone_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_policy_change_after_result_creation_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_change_after_result_creation_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_zoning_relation_and_zone_mapping_changes_are_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_structure_config_and_hierarchy_changes_are_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_invalid_physical_zoning_fails_before_policy_interpretation` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_relation_area_denominators_are_required` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_relation_percentages_must_match_denominators` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_factual_zone_mapping_counts_are_recomputed` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_result_mutation_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_catalog_mutation_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_catalog_occurrence_duplicate_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_route_table_mutation_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_route_link_mutation_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_reverse_link_mutation_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_route_link_hash_mutation_is_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_old_result_hash_schemas_are_rejected` via `BessZoningPrecheckError`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_relation_identity_change_is_rejected` via `BessZoningPrecheckError`

**Exact class source**

```python
class BessZoningPrecheckError(ValueError):
    """Raised when the preliminary zoning interpretation cannot be proven."""
```

### `_StrictConfigModel`

**Source purpose:** Defines `_StrictConfigModel`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _StrictConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `PolicySourceLock`

**Source purpose:** Defines `PolicySourceLock`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `document_id` | `StrictStr` | `Field(min_length=1)` | `document_id: StrictStr = Field(min_length=1)` |
| `archive_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `archive_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `pdf_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `index_content_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `structure_result_content_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `structure_result_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `structure_profile` | `StrictStr` | `Field(min_length=1)` | `structure_profile: StrictStr = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

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

**Source purpose:** Defines `PolicyEvidence`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `evidence_id` | `StrictStr` | `Field(min_length=1)` | `evidence_id: StrictStr = Field(min_length=1)` |
| `section_id` | `StrictStr` | `Field(min_length=1)` | `section_id: StrictStr = Field(min_length=1)` |
| `page_number` | `StrictInt` | `Field(ge=1)` | `page_number: StrictInt = Field(ge=1)` |
| `evidence_kind` | `EvidenceKind` | `required` | `evidence_kind: EvidenceKind` |
| `evidence_direction` | `EvidenceDirection` | `required` | `evidence_direction: EvidenceDirection` |
| `exact_raw_excerpt` | `StrictStr` | `Field(min_length=1, max_length=600)` | `exact_raw_excerpt: StrictStr = Field(min_length=1, max_length=600)` |
| `excerpt_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `excerpt_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `section_page_fragment_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `section_page_fragment_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `excerpt_start` | `StrictInt` | `Field(ge=0)` | `excerpt_start: StrictInt = Field(ge=0)` |
| `excerpt_end` | `StrictInt` | `Field(ge=1)` | `excerpt_end: StrictInt = Field(ge=1)` |
| `source_rule_id` | `StrictStr` | `Field(min_length=1)` | `source_rule_id: StrictStr = Field(min_length=1)` |
| `source_rule_excerpt` | `StrictStr` | `Field(min_length=1)` | `source_rule_excerpt: StrictStr = Field(min_length=1)` |
| `source_rule_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `source_rule_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `source_rule_start` | `StrictInt` | `Field(ge=0)` | `source_rule_start: StrictInt = Field(ge=0)` |
| `source_rule_end` | `StrictInt` | `Field(ge=1)` | `source_rule_end: StrictInt = Field(ge=1)` |
| `interpretation_note` | `StrictStr` | `Field(min_length=1)` | `interpretation_note: StrictStr = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.interpret_bess_zoning::PolicyEvidence._validate_exact_strings` via `PolicyEvidence`

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
        if (
            sha256(self.exact_raw_excerpt.encode("utf-8")).hexdigest()
            != self.excerpt_sha256
        ):
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

**Source purpose:** Defines `RouteAssessment`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `route_id` | `StrictStr` | `Field(min_length=1)` | `route_id: StrictStr = Field(min_length=1)` |
| `route_kind` | `RouteKind` | `required` | `route_kind: RouteKind` |
| `positive_evidence_ids` | `tuple[StrictStr, ...]` | `()` | `positive_evidence_ids: tuple[StrictStr, ...] = ()` |
| `condition_evidence_ids` | `tuple[StrictStr, ...]` | `()` | `condition_evidence_ids: tuple[StrictStr, ...] = ()` |
| `difficulty_evidence_ids` | `tuple[StrictStr, ...]` | `()` | `difficulty_evidence_ids: tuple[StrictStr, ...] = ()` |
| `applicability_note` | `StrictStr` | `Field(min_length=1)` | `applicability_note: StrictStr = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.interpret_bess_zoning::RouteAssessment._validate_route_shape` via `RouteAssessment`
- value/type reference: `landscout.stages.interpret_bess_zoning::_derived_chapter_status` via `RouteAssessment`

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
            normalized = [
                _config_string(value, f"{role} evidence ID") for value in values
            ]
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

**Source purpose:** Defines `ChapterPolicy`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `resolved_zone_chapter_label` | `StrictStr` | `Field(min_length=1)` | `resolved_zone_chapter_label: StrictStr = Field(min_length=1)` |
| `review_completeness` | `ReviewCompleteness` | `required` | `review_completeness: ReviewCompleteness` |
| `reviewed_section_ids` | `tuple[StrictStr, ...]` | `()` | `reviewed_section_ids: tuple[StrictStr, ...] = ()` |
| `review_note` | `StrictStr` | `Field(min_length=1)` | `review_note: StrictStr = Field(min_length=1)` |
| `zoning_precheck_status` | `ChapterStatus` | `required` | `zoning_precheck_status: ChapterStatus` |
| `zoning_precheck_confidence` | `Confidence` | `required` | `zoning_precheck_confidence: Confidence` |
| `rationale` | `StrictStr` | `Field(min_length=1)` | `rationale: StrictStr = Field(min_length=1)` |
| `missing_information` | `StrictStr` | `Field(min_length=1)` | `missing_information: StrictStr = Field(min_length=1)` |
| `evidence` | `tuple[PolicyEvidence, ...]` | `()` | `evidence: tuple[PolicyEvidence, ...] = ()` |
| `route_assessments` | `tuple[RouteAssessment, ...]` | `()` | `route_assessments: tuple[RouteAssessment, ...] = ()` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.interpret_bess_zoning::ChapterPolicy._validate_evidence_semantics` via `ChapterPolicy`

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

**Source purpose:** Strict source-locked interpretation policy.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `policy_profile` | `StrictStr` | `Field(min_length=1)` | `policy_profile: StrictStr = Field(min_length=1)` |
| `planning_precheck_scope` | `Literal['WRITTEN_ZONING_REGULATION_ONLY']` | `required` | `planning_precheck_scope: Literal["WRITTEN_ZONING_REGULATION_ONLY"]` |
| `review_scope` | `Literal['CONFIGURED_USE_CONTROL_ARTICLES_ONLY']` | `required` | `review_scope: Literal["CONFIGURED_USE_CONTROL_ARTICLES_ONLY"]` |
| `source_lock` | `PolicySourceLock` | `required` | `source_lock: PolicySourceLock` |
| `required_zone_article_numbers` | `tuple[StrictStr, ...]` | `Field(min_length=1)` | `required_zone_article_numbers: tuple[StrictStr, ...] = Field(min_length=1)` |
| `chapters` | `tuple[ChapterPolicy, ...]` | `Field(min_length=1)` | `chapters: tuple[ChapterPolicy, ...] = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`
- value/type reference: `landscout.stages.interpret_bess_zoning::BessZoningPolicyConfig._validate_policy` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::load_bess_zoning_policy_config` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_policy_sha256` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_resolved_policy` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_lock` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_required_section_ids_by_chapter` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_lineage` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_chapter_policy` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_route_assessments` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_evidence_route_links` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_source_zone_policy` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_parcel_zone_interpretations` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_parcel_output` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `BessZoningPolicyConfig`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    validate_bess_zoning_precheck,
)`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_policy` via `BessZoningPolicyConfig`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
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
)`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_policy` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_payload` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_policy_with_context_only_evidence` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_lock_mismatch_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_missing_and_extra_chapter_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_chapter_and_evidence_id_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_one_excerpt_cannot_be_reused_with_contradictory_directions` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_occurrence_in_different_compatible_routes_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_forbidden_or_invalid_final_status_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_invalid_confidence_and_unknown_field_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_old_policy_schema_versions_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_rule_identity_and_containment_are_strict` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_same_rule_text_at_distinct_offsets_has_distinct_identity` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_absent_excerpt_and_section_page_mismatch_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_excerpt_hash_and_length_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_declared_status_must_equal_derived_route_status` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_condition_alone_cannot_create_conditional_review` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unrelated_positive_and_condition_do_not_create_conditional_review` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unlinked_context_only_unknown_succeeds` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_positive_condition_and_conflict_status_routes` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_route_references_must_be_same_chapter_and_role_compatible` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_route_ids_are_globally_unique` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unlinked_difficulty_evidence_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unlinked_positive_and_condition_evidence_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_context_only_evidence_must_be_unlinked` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_one_evidence_may_link_to_multiple_compatible_routes` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_difficulty_and_positive_only_status_routes` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_incomplete_review_requires_unknown_low` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_incomplete_review_persists_exact_missing_required_sections` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unknown_is_accepted_when_evidence_is_insufficient` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_reviewed_sections_cover_required_articles` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_must_be_inside_reviewed_sections` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_review_cannot_claim_another_chapter_section` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_general_section_review_is_explicit_and_valid` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_same_general_occurrence_may_be_scoped_to_different_chapters` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_wrong_occurrence_identity_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_policy_change_after_result_creation_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_change_after_result_creation_is_rejected` via `BessZoningPolicyConfig`

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
            raise ValueError(
                f"unsupported BESS zoning policy schema: {self.schema_version}"
            )
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
                if (
                    prior_rule_id is not None
                    and prior_rule_id != evidence.source_rule_id
                ):
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
                    raise ValueError(
                        "CONTEXT_ONLY evidence must not be linked to a route"
                    )
                if evidence.evidence_direction != "CONTEXT_ONLY" and not is_linked:
                    raise ValueError(
                        "decision evidence must be linked to at least one route"
                    )
        return self
```

### `BessZoningPrecheckResult`

**Source purpose:** Immutable envelope around the conservative written-zoning precheck.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `result_hash_schema_version` | `int` | `required` | `result_hash_schema_version: int` |
| `policy_schema_version` | `int` | `required` | `policy_schema_version: int` |
| `policy_profile` | `str` | `required` | `policy_profile: str` |
| `planning_precheck_scope` | `str` | `required` | `planning_precheck_scope: str` |
| `review_scope` | `str` | `required` | `review_scope: str` |
| `document_id` | `str` | `required` | `document_id: str` |
| `archive_sha256` | `str` | `required` | `archive_sha256: str` |
| `pdf_sha256` | `str` | `required` | `pdf_sha256: str` |
| `index_content_sha256` | `str` | `required` | `index_content_sha256: str` |
| `structure_result_content_sha256` | `str` | `required` | `structure_result_content_sha256: str` |
| `structure_profile` | `str` | `required` | `structure_profile: str` |
| `policy_config_sha256` | `str` | `required` | `policy_config_sha256: str` |
| `factual_structure_content_sha256` | `str` | `required` | `factual_structure_content_sha256: str` |
| `zone_mapping_input_sha256` | `str` | `required` | `zone_mapping_input_sha256: str` |
| `zoning_relation_hash_columns` | `tuple[str, ...]` | `required` | `zoning_relation_hash_columns: tuple[str, ...]` |
| `zoning_relations_input_sha256` | `str` | `required` | `zoning_relations_input_sha256: str` |
| `evidence_catalog_content_sha256` | `str` | `required` | `evidence_catalog_content_sha256: str` |
| `evidence_route_links_content_sha256` | `str` | `required` | `evidence_route_links_content_sha256: str` |
| `route_assessments_content_sha256` | `str` | `required` | `route_assessments_content_sha256: str` |
| `chapter_policy_content_sha256` | `str` | `required` | `chapter_policy_content_sha256: str` |
| `source_zone_policy_content_sha256` | `str` | `required` | `source_zone_policy_content_sha256: str` |
| `parcel_zone_policy_content_sha256` | `str` | `required` | `parcel_zone_policy_content_sha256: str` |
| `parcel_output_content_sha256` | `str` | `required` | `parcel_output_content_sha256: str` |
| `complete_result_content_sha256` | `str` | `required` | `complete_result_content_sha256: str` |
| `touch_only_relation_count` | `int` | `required` | `touch_only_relation_count: int` |
| `evidence_catalog` | `pd.DataFrame` | `required` | `evidence_catalog: pd.DataFrame` |
| `evidence_route_links` | `pd.DataFrame` | `required` | `evidence_route_links: pd.DataFrame` |
| `route_assessments` | `pd.DataFrame` | `required` | `route_assessments: pd.DataFrame` |
| `chapter_policy` | `pd.DataFrame` | `required` | `chapter_policy: pd.DataFrame` |
| `source_zone_policy` | `pd.DataFrame` | `required` | `source_zone_policy: pd.DataFrame` |
| `parcel_zone_interpretations` | `pd.DataFrame` | `required` | `parcel_zone_interpretations: pd.DataFrame` |
| `parcels` | `gpd.GeoDataFrame` | `required` | `parcels: gpd.GeoDataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`
- value/type reference: `landscout.stages.interpret_bess_zoning::_result_component_metadata` via `BessZoningPrecheckResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_result_frame_sha256` via `BessZoningPrecheckResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_complete_result_sha256` via `BessZoningPrecheckResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_result_with_hashes` via `BessZoningPrecheckResult`
- constructor call: `landscout.stages.interpret_bess_zoning::_build_result` via `BessZoningPrecheckResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `BessZoningPrecheckResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_results` via `BessZoningPrecheckResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `BessZoningPrecheckResult`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `BessZoningPrecheckResult`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    validate_bess_zoning_precheck,
)`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_interpret` via `BessZoningPrecheckResult`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_validate` via `BessZoningPrecheckResult`

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


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `PolicyEvidence._validate_exact_strings`

**Purpose:** Implements `validate exact strings` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _validate_exact_strings(self) -> PolicyEvidence:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `PolicyEvidence`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("evidence excerpt SHA256 differs from exact_raw_excerpt")` under lexical guard `sha256(self.exact_raw_excerpt.encode("utf-8")).hexdigest()<br>            != self.excerpt_sha256`.
  - `ValueError("evidence excerpt offsets must be ordered")` under lexical guard `self.excerpt_end <= self.excerpt_start`.
  - `ValueError("source rule SHA256 differs from source_rule_excerpt")` under lexical guard `sha256(self.source_rule_excerpt.encode("utf-8")).hexdigest() != (<br>            self.source_rule_sha256<br>        )`.
  - `ValueError("source rule offsets must be ordered")` under lexical guard `self.source_rule_end <= self.source_rule_start`.
  - `ValueError("evidence excerpt must lie inside its source rule")` under lexical guard `not (<br>            self.source_rule_start <= self.excerpt_start<br>            and self.excerpt_end <= self.source_rule_end<br>        )`.
  - `ValueError("evidence kind and direction are incompatible")` under lexical guard `self.evidence_direction not in allowed`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config_string` | `landscout.stages.interpret_bess_zoning._config_string` |
| `sha256(self.exact_raw_excerpt.encode("utf-8")).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `self.exact_raw_excerpt.encode` | `landscout.stages.interpret_bess_zoning.PolicyEvidence.exact_raw_excerpt.encode` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(self.source_rule_excerpt.encode("utf-8")).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `self.source_rule_excerpt.encode` | `landscout.stages.interpret_bess_zoning.PolicyEvidence.source_rule_excerpt.encode` |
| `frozenset` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(self.exact_raw_excerpt.encode("utf-8")).hexdigest`<br>`sha256`<br>`sha256(self.source_rule_excerpt.encode("utf-8")).hexdigest` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
        if (
            sha256(self.exact_raw_excerpt.encode("utf-8")).hexdigest()
            != self.excerpt_sha256
        ):
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `RouteAssessment._validate_route_shape`

**Purpose:** Implements `validate route shape` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _validate_route_shape(self) -> RouteAssessment:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `RouteAssessment`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError(f"{role} evidence IDs must be unique within a route")` under lexical guard `len(set(normalized)) != len(normalized)`.
  - `ValueError("one evidence ID cannot occupy incompatible route roles")` under lexical guard `len(set(combined)) != len(combined)`.
  - `ValueError(<br>                f"{self.route_kind} has incompatible evidence-role membership"<br>            )` under lexical guard `(positive, condition, difficulty) != expected`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config_string` | `landscout.stages.interpret_bess_zoning._config_string` |
| `roles.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `combined.extend` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

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
| In-memory mutation | `combined.extend(normalized)` |
| Direct parameter mutation | None directly present. |

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
            normalized = [
                _config_string(value, f"{role} evidence ID") for value in values
            ]
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_derived_chapter_status`

**Purpose:** Implements `derived chapter status` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _derived_chapter_status(
    review_completeness: ReviewCompleteness,
    routes: Sequence[RouteAssessment],
) -> ChapterStatus:
```

- Exact decorators: none.
- Declared return annotation: `ChapterStatus`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `review_completeness` | positional-or-keyword | `ReviewCompleteness` | `required` |
| `routes` | positional-or-keyword | `Sequence[RouteAssessment]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `"UNKNOWN"`
  - `"CONDITIONAL_REVIEW"`
  - `"UNKNOWN" if "DIFFICULTY_ONLY" in kinds else "POTENTIALLY_COMPATIBLE"`
  - `"LIKELY_DIFFICULT"`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::ChapterPolicy._validate_evidence_semantics` via `_derived_chapter_status`
- value/type reference: `landscout.stages.interpret_bess_zoning::ChapterPolicy._validate_evidence_semantics` via `_derived_chapter_status`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `kinds.intersection` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `ChapterPolicy._validate_evidence_semantics`

**Purpose:** Implements `validate evidence semantics` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _validate_evidence_semantics(self) -> ChapterPolicy:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `ChapterPolicy`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError("reviewed section IDs must be unique")` under lexical guard `len(set(reviewed)) != len(reviewed)`.
  - `ValueError("incomplete review requires UNKNOWN / LOW")` under lexical guard `self.review_completeness == "INCOMPLETE" and (<br>            self.zoning_precheck_status != "UNKNOWN"<br>            or self.zoning_precheck_confidence != "LOW"<br>        )`.
  - `ValueError("route IDs must be unique within a chapter")` under lexical guard `len(set(route_ids)) != len(route_ids)`.
  - `ValueError(<br>                "declared chapter status differs from coherent linked route assessments"<br>            )` under lexical guard `self.zoning_precheck_status != expected_status`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_config_string` | `landscout.stages.interpret_bess_zoning._config_string` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_derived_chapter_status` | `landscout.stages.interpret_bess_zoning._derived_chapter_status` |
| `model_validator` | `pydantic.model_validator` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `BessZoningPolicyConfig._validate_policy`

**Purpose:** Implements `validate policy` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _validate_policy(self) -> BessZoningPolicyConfig:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `BessZoningPolicyConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError(<br>                f"unsupported BESS zoning policy schema: {self.schema_version}"<br>            )` under lexical guard `self.schema_version != POLICY_SCHEMA_VERSION`.
  - `ValueError("required zone article numbers must be unique")` under lexical guard `len(set(article_numbers)) != len(article_numbers)`.
  - `ValueError("chapter policy labels must be unique")` under lexical guard `len(set(labels)) != len(labels)`.
  - `ValueError("evidence IDs must be globally unique")` under lexical guard `evidence.evidence_id in evidence_ids`.
  - `ValueError(<br>                        "one chapter-scoped evidence occurrence must resolve to exactly one evidence ID, kind, and direction"<br>                    )` under lexical guard `previous is not None`.
  - `ValueError(<br>                        "one source rule ID must resolve to one exact occurrence"<br>                    )` under lexical guard `prior_rule is not None and prior_rule != rule_identity`.
  - `ValueError(<br>                        "one exact source-rule occurrence must use one source rule ID"<br>                    )` under lexical guard `prior_rule_id is not None<br>                    and prior_rule_id != evidence.source_rule_id`.
  - `ValueError(<br>                            f"source rule {evidence.source_rule_id!r} partially overlaps {rule_id!r}"<br>                        )` under lexical guard `overlaps and not identical`.
  - `ValueError("route IDs must be globally unique")` under lexical guard `route.route_id in route_ids`.
  - `ValueError(<br>                                f"route references unknown or another-chapter evidence ID {evidence_id!r}"<br>                            )` under lexical guard `referenced_evidence is None`.
  - `ValueError(<br>                                f"route assigns evidence ID {evidence_id!r} to an incompatible {role} role"<br>                            )` under lexical guard `referenced_evidence.evidence_direction != expected_direction`.
  - `ValueError(<br>                        "CONTEXT_ONLY evidence must not be linked to a route"<br>                    )` under lexical guard `evidence.evidence_direction == "CONTEXT_ONLY" and is_linked`.
  - `ValueError(<br>                        "decision evidence must be linked to at least one route"<br>                    )` under lexical guard `evidence.evidence_direction != "CONTEXT_ONLY" and not is_linked`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_config_string` | `landscout.stages.interpret_bess_zoning._config_string` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `evidence_ids.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `chapter_occurrences.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_rules.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_rule_occurrences.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_rule_ranges.setdefault` | `unresolved local/third-party receiver; no ownership inferred` |
| `max` | `unresolved local/third-party receiver; no ownership inferred` |
| `min` | `unresolved local/third-party receiver; no ownership inferred` |
| `ranges.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `route_ids.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `chapter_evidence.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `linked_evidence_ids.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `model_validator` | `pydantic.model_validator` |

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
| In-memory mutation | `evidence_ids.add(evidence.evidence_id)`<br>`chapter_occurrences[key] = (<br>                    evidence.evidence_id,<br>                    evidence.evidence_kind,<br>                    evidence.evidence_direction,<br>                )`<br>`source_rules[evidence.source_rule_id] = rule_identity`<br>`source_rule_occurrences[occurrence] = evidence.source_rule_id`<br>`source_rule_ranges.setdefault(range_key, [])`<br>`ranges.append(current)`<br>`route_ids.add(route.route_id)`<br>`linked_evidence_ids.add(evidence_id)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_policy(self) -> BessZoningPolicyConfig:
        if self.schema_version != POLICY_SCHEMA_VERSION:
            raise ValueError(
                f"unsupported BESS zoning policy schema: {self.schema_version}"
            )
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
                if (
                    prior_rule_id is not None
                    and prior_rule_id != evidence.source_rule_id
                ):
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
                    raise ValueError(
                        "CONTEXT_ONLY evidence must not be linked to a route"
                    )
                if evidence.evidence_direction != "CONTEXT_ONLY" and not is_linked:
                    raise ValueError(
                        "decision evidence must be linked to at least one route"
                    )
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_config_string`

**Purpose:** Implements `config string` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _config_string(value: str, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `ValueError(f"{label} must be a non-empty exact string")` under lexical guard `not value or value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::PolicyEvidence._validate_exact_strings` via `_config_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::PolicyEvidence._validate_exact_strings` via `_config_string`
- direct call: `landscout.stages.interpret_bess_zoning::RouteAssessment._validate_route_shape` via `_config_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::RouteAssessment._validate_route_shape` via `_config_string`
- direct call: `landscout.stages.interpret_bess_zoning::ChapterPolicy._validate_evidence_semantics` via `_config_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::ChapterPolicy._validate_evidence_semantics` via `_config_string`
- direct call: `landscout.stages.interpret_bess_zoning::BessZoningPolicyConfig._validate_policy` via `_config_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::BessZoningPolicyConfig._validate_policy` via `_config_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _config_string(value: str, label: str) -> str:
    if not value or value != value.strip():
        raise ValueError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `load_bess_zoning_policy_config`

**Purpose:** Load a strict policy while rejecting duplicate YAML keys.

**Exact signature**

```python
def load_bess_zoning_policy_config(path: str | Path) -> BessZoningPolicyConfig:
```

- Exact decorators: none.
- Declared return annotation: `BessZoningPolicyConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `BessZoningPolicyConfig.model_validate(payload)`
- Explicit raise paths:
  - `BessZoningPrecheckError("BESS zoning policy must be a mapping")` under lexical guard `not isinstance(payload, Mapping)`.
  - `re-raise`.
  - `BessZoningPrecheckError(str(error))`.
  - `BessZoningPrecheckError("BESS zoning policy is invalid")`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`
- direct call: `landscout.stages.interpret_bess_zoning::_resolved_policy` via `load_bess_zoning_policy_config`
- value/type reference: `landscout.stages.interpret_bess_zoning::_resolved_policy` via `load_bess_zoning_policy_config`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
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
)`
- direct call: `tests.unit.test_interpret_bess_zoning::test_duplicate_yaml_key_is_rejected` via `load_bess_zoning_policy_config`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_yaml_key_is_rejected` via `load_bess_zoning_policy_config`
- direct call: `tests.unit.test_interpret_bess_zoning::test_real_muret_source_rules_preserve_conditional_and_exception_frames` via `load_bess_zoning_policy_config`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_real_muret_source_rules_preserve_conditional_and_exception_frames` via `load_bess_zoning_policy_config`
- direct call: `tests.unit.test_interpret_bess_zoning::test_real_muret_up_route_does_not_use_the_separate_icpe_condition` via `load_bess_zoning_policy_config`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_real_muret_up_route_does_not_use_the_separate_icpe_condition` via `load_bess_zoning_policy_config`
- direct call: `tests.unit.test_interpret_bess_zoning::test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite` via `load_bess_zoning_policy_config`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_real_muret_aup_route_uses_the_general_infrastructure_prerequisite` via `load_bess_zoning_policy_config`
- direct call: `tests.unit.test_interpret_bess_zoning::test_real_muret_up_and_aup_keep_icpe_applicability_as_context` via `load_bess_zoning_policy_config`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_real_muret_up_and_aup_keep_icpe_applicability_as_context` via `load_bess_zoning_policy_config`
- direct call: `tests.unit.test_interpret_bess_zoning::test_policy_yaml_roundtrip_is_strict` via `load_bess_zoning_policy_config`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_policy_yaml_roundtrip_is_strict` via `load_bess_zoning_policy_config`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `loads_strict_yaml` | `landscout.common.strict_yaml.loads_strict_yaml` |
| `Path(path).read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | `Path(path).read_bytes` |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def load_bess_zoning_policy_config(path: str | Path) -> BessZoningPolicyConfig:
    """Load a strict policy while rejecting duplicate YAML keys."""

    try:
        payload = loads_strict_yaml(Path(path).read_bytes())
        if not isinstance(payload, Mapping):
            raise BessZoningPrecheckError("BESS zoning policy must be a mapping")
        return BessZoningPolicyConfig.model_validate(payload)
    except BessZoningPrecheckError:
        raise
    except StrictYamlError as error:
        raise BessZoningPrecheckError(str(error)) from error
    except Exception as error:
        raise BessZoningPrecheckError("BESS zoning policy is invalid") from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_string`

**Purpose:** Implements `strict string` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _strict_string(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `value`
- Explicit raise paths:
  - `BessZoningPrecheckError(f"{label} must be a non-empty exact string")` under lexical guard `not isinstance(value, str) or not value or value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_validated_sha256` via `_strict_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validated_sha256` via `_strict_string`
- direct call: `landscout.stages.interpret_bess_zoning::_exact_id_series` via `_strict_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::_exact_id_series` via `_strict_string`
- direct call: `landscout.stages.interpret_bess_zoning::_validate_zones` via `_strict_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_zones` via `_strict_string`
- direct call: `landscout.stages.interpret_bess_zoning::_validate_relations` via `_strict_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_relations` via `_strict_string`
- direct call: `landscout.stages.interpret_bess_zoning::_zone_chapter_rows` via `_strict_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::_zone_chapter_rows` via `_strict_string`
- direct call: `landscout.stages.interpret_bess_zoning::_required_section_ids_by_chapter` via `_strict_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::_required_section_ids_by_chapter` via `_strict_string`
- direct call: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `_strict_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `_strict_string`
- direct call: `landscout.stages.interpret_bess_zoning::_validate_mapping` via `_strict_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_mapping` via `_strict_string`
- direct call: `landscout.stages.interpret_bess_zoning::_build_chapter_policy` via `_strict_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_chapter_policy` via `_strict_string`
- direct call: `landscout.stages.interpret_bess_zoning::_build_source_zone_policy` via `_strict_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_source_zone_policy` via `_strict_string`
- direct call: `landscout.stages.interpret_bess_zoning::_build_parcel_output` via `_strict_string`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_parcel_output` via `_strict_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |

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
def _strict_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise BessZoningPrecheckError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_nonnegative_integer`

**Purpose:** Implements `strict nonnegative integer` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

- Exact decorators: none.
- Declared return annotation: `int`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `BessZoningPrecheckError(f"{label} must be an integer")` under lexical guard `isinstance(value, bool) or not isinstance(value, Integral)`.
  - `BessZoningPrecheckError(f"{label} must be non-negative")` under lexical guard `result < 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_strict_positive_integer` via `_strict_nonnegative_integer`
- value/type reference: `landscout.stages.interpret_bess_zoning::_strict_positive_integer` via `_strict_nonnegative_integer`
- direct call: `landscout.stages.interpret_bess_zoning::_validate_parcels` via `_strict_nonnegative_integer`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_parcels` via `_strict_nonnegative_integer`
- direct call: `landscout.stages.interpret_bess_zoning::_compare_results` via `_strict_nonnegative_integer`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_results` via `_strict_nonnegative_integer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
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
def _strict_nonnegative_integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise BessZoningPrecheckError(f"{label} must be an integer")
    result = int(value)
    if result < 0:
        raise BessZoningPrecheckError(f"{label} must be non-negative")
    return result
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_positive_integer`

**Purpose:** Implements `strict positive integer` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _strict_positive_integer(value: object, label: str) -> int:
```

- Exact decorators: none.
- Declared return annotation: `int`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `BessZoningPrecheckError(f"{label} must be positive")` under lexical guard `result < 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `_strict_positive_integer`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `_strict_positive_integer`
- direct call: `landscout.stages.interpret_bess_zoning::_compare_results` via `_strict_positive_integer`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_results` via `_strict_positive_integer`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_strict_nonnegative_integer` | `landscout.stages.interpret_bess_zoning._strict_nonnegative_integer` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |

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
def _strict_positive_integer(value: object, label: str) -> int:
    result = _strict_nonnegative_integer(value, label)
    if result < 1:
        raise BessZoningPrecheckError(f"{label} must be positive")
    return result
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validated_sha256`

**Purpose:** Implements `validated sha256` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _validated_sha256(value: object, label: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `checksum`
- Explicit raise paths:
  - `BessZoningPrecheckError(<br>            f"{label} must be exactly 64 lowercase hexadecimal characters"<br>        )` under lexical guard `re.fullmatch(r"[0-9a-f]{64}", checksum) is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_compare_results` via `_validated_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_results` via `_validated_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_strict_string` | `landscout.stages.interpret_bess_zoning._strict_string` |
| `re.fullmatch` | `re.fullmatch` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |

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
def _validated_sha256(value: object, label: str) -> str:
    checksum = _strict_string(value, label)
    if re.fullmatch(r"[0-9a-f]{64}", checksum) is None:
        raise BessZoningPrecheckError(
            f"{label} must be exactly 64 lowercase hexadecimal characters"
        )
    return checksum
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_nonnegative_number`

**Purpose:** Implements `strict nonnegative number` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _strict_nonnegative_number(value: object, label: str) -> float:
```

- Exact decorators: none.
- Declared return annotation: `float`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `BessZoningPrecheckError(f"{label} must be numeric")` under lexical guard `isinstance(value, bool) or not isinstance(value, Real)`.
  - `BessZoningPrecheckError(f"{label} must be finite")`.
  - `BessZoningPrecheckError(f"{label} must be finite and non-negative")` under lexical guard `not math.isfinite(result) or result < 0`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_validate_relations` via `_strict_nonnegative_number`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_relations` via `_strict_nonnegative_number`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `math.isfinite` | `math.isfinite` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_value`

**Purpose:** Implements `canonical value` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _canonical_value(value: object) -> object:
```

- Exact decorators: none.
- Declared return annotation: `object`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `_canonical_value(value.item())`
  - `to_wkb(value, hex=True, include_srid=False)`
  - `value.isoformat()`
  - `value.hex()`
  - `[_canonical_value(item) for item in value]`
  - `{str(key): _canonical_value(item) for key, item in value.items()}`
  - `value`
- Explicit raise paths:
  - `BessZoningPrecheckError(<br>        f"Value of type {type(value).__name__} cannot be canonically serialized"<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_canonical_value` via `_canonical_value`
- value/type reference: `landscout.stages.interpret_bess_zoning::_canonical_value` via `_canonical_value`
- direct call: `landscout.stages.interpret_bess_zoning::_canonical_sha256` via `_canonical_value`
- value/type reference: `landscout.stages.interpret_bess_zoning::_canonical_sha256` via `_canonical_value`
- direct call: `landscout.stages.interpret_bess_zoning::_frame_payload` via `_canonical_value`
- value/type reference: `landscout.stages.interpret_bess_zoning::_frame_payload` via `_canonical_value`
- direct call: `landscout.stages.interpret_bess_zoning::_compare_frames` via `_canonical_value`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_frames` via `_canonical_value`
- direct call: `landscout.stages.interpret_bess_zoning::_compare_results` via `_canonical_value`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_results` via `_canonical_value`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_value` | `landscout.stages.interpret_bess_zoning._canonical_value` |
| `value.item` | `unresolved local/third-party receiver; no ownership inferred` |
| `to_wkb` | `shapely.to_wkb` |
| `value.isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.hex` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `math.isnan` | `math.isnan` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `to_wkb` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_sha256`

**Purpose:** Implements `canonical sha256` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _canonical_sha256(value: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `sha256(serialized).hexdigest()`
- Explicit raise paths:
  - `re-raise`.
  - `BessZoningPrecheckError(<br>            "Canonical integrity serialization failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_frame_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_frame_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.interpret_bess_zoning::_policy_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_policy_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.interpret_bess_zoning::_factual_structure_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_factual_structure_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.interpret_bess_zoning::_zone_mapping_input_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_zone_mapping_input_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.interpret_bess_zoning::_result_frame_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_result_frame_sha256` via `_canonical_sha256`
- direct call: `landscout.stages.interpret_bess_zoning::_complete_result_sha256` via `_canonical_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_complete_result_sha256` via `_canonical_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.dumps(<br>            _canonical_value(value),<br>            ensure_ascii=False,<br>            allow_nan=False,<br>            sort_keys=True,<br>            separators=(",", ":"),<br>        ).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `_canonical_value` | `landscout.stages.interpret_bess_zoning._canonical_value` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `sha256(serialized).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(serialized).hexdigest`<br>`sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
        raise BessZoningPrecheckError(
            "Canonical integrity serialization failed"
        ) from error
    return sha256(serialized).hexdigest()
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_frame_payload`

**Purpose:** Implements `frame payload` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _frame_payload(frame: pd.DataFrame, columns: Sequence[str]) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `columns` | positional-or-keyword | `Sequence[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `payload`
- Explicit raise paths:
  - `BessZoningPrecheckError("DataFrame columns must be unique")` under lexical guard `frame.columns.has_duplicates`.
  - `BessZoningPrecheckError(f"DataFrame is missing columns: {missing}")` under lexical guard `missing`.
  - `BessZoningPrecheckError("GeoDataFrame CRS is required")` under lexical guard `isinstance(frame, gpd.GeoDataFrame)`.
  - `re-raise`.
  - `BessZoningPrecheckError(<br>            "DataFrame integrity serialization failed"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_frame_sha256` via `_frame_payload`
- value/type reference: `landscout.stages.interpret_bess_zoning::_frame_sha256` via `_frame_payload`
- direct call: `landscout.stages.interpret_bess_zoning::_zone_mapping_input_sha256` via `_frame_payload`
- value/type reference: `landscout.stages.interpret_bess_zoning::_zone_mapping_input_sha256` via `_frame_payload`
- direct call: `landscout.stages.interpret_bess_zoning::_result_frame_sha256` via `_frame_payload`
- value/type reference: `landscout.stages.interpret_bess_zoning::_result_frame_sha256` via `_frame_payload`
- direct call: `landscout.stages.interpret_bess_zoning::_compare_frames` via `_frame_payload`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_frames` via `_frame_payload`
- direct call: `landscout.stages.interpret_bess_zoning::_compare_results` via `_frame_payload`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_results` via `_frame_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_value` | `landscout.stages.interpret_bess_zoning._canonical_value` |
| `frame.index.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.loc[:, columns].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input(frame.crs).to_json_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `CRS.from_user_input(frame.crs).to_json_dict` |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `payload["crs"] = CRS.from_user_input(frame.crs).to_json_dict()`<br>`payload["geometry_column"] = frame.geometry.name` |
| Direct parameter mutation | None directly present. |

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
        raise BessZoningPrecheckError(
            "DataFrame integrity serialization failed"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_frame_sha256`

**Purpose:** Implements `frame sha256` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _frame_sha256(domain: str, frame: pd.DataFrame, columns: Sequence[str]) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `domain` | positional-or-keyword | `str` | `required` |
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `columns` | positional-or-keyword | `Sequence[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256({"domain": domain, **_frame_payload(frame, columns)})`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_frame_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_frame_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.interpret_bess_zoning._canonical_sha256` |
| `_frame_payload` | `landscout.stages.interpret_bess_zoning._frame_payload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _frame_sha256(domain: str, frame: pd.DataFrame, columns: Sequence[str]) -> str:
    return _canonical_sha256({"domain": domain, **_frame_payload(frame, columns)})
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_policy_sha256`

**Purpose:** Implements `policy sha256` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _policy_sha256(config: BessZoningPolicyConfig) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `config` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": "landscout.bess_zoning.policy_config",<br>            "config": config.model_dump(mode="json"),<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_policy_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_policy_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.interpret_bess_zoning._canonical_sha256` |
| `config.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_factual_structure_sha256`

**Purpose:** Implements `factual structure sha256` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _factual_structure_sha256(
    structure: PlanningRegulationStructureResult,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": "landscout.bess_zoning.factual_structure_input",<br>            "structure_result_content_sha256": structure.structure_result_content_sha256,<br>            "section_hash_schema_version": structure.section_hash_schema_version,<br>            "structure_config_sha256": structure.structure_config_sha256,<br>            "sections_content_sha256": structure.sections_content_sha256,<br>            "zone_map_content_sha256": structure.zone_map_content_sha256,<br>            "topic_evidence_content_sha256": structure.topic_evidence_content_sha256,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_factual_structure_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_factual_structure_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.interpret_bess_zoning._canonical_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_resolved_policy`

**Purpose:** Implements `resolved policy` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _resolved_policy(
    policy: BessZoningPolicyConfig | str | Path,
) -> BessZoningPolicyConfig:
```

- Exact decorators: none.
- Declared return annotation: `BessZoningPolicyConfig`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `policy` | positional-or-keyword | `BessZoningPolicyConfig \| str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `BessZoningPolicyConfig.model_validate(<br>                policy.model_dump(mode="python")<br>            )`
  - `load_bess_zoning_policy_config(policy)`
- Explicit raise paths:
  - `BessZoningPrecheckError("BESS zoning policy is invalid")` under lexical guard `isinstance(policy, BessZoningPolicyConfig)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `_resolved_policy`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `_resolved_policy`
- direct call: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `_resolved_policy`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `_resolved_policy`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPolicyConfig.model_validate` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.model_validate` |
| `policy.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `load_bess_zoning_policy_config` | `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_policy_lock`

**Purpose:** Implements `validate policy lock` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _validate_policy_lock(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessZoningPrecheckError(<br>                f"BESS zoning policy {label} differs from factual source"<br>            )` under lexical guard `actual != expected`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_validate_policy_lock`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_validate_policy_lock`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_exact_id_series`

**Purpose:** Implements `exact id series` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _exact_id_series(series: pd.Series, label: str, *, unique: bool) -> tuple[str, ...]:
```

- Exact decorators: none.
- Declared return annotation: `tuple[str, ...]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `series` | positional-or-keyword | `pd.Series` | `required` |
| `label` | positional-or-keyword | `str` | `required` |
| `unique` | keyword-only | `bool` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `tuple(values)`
- Explicit raise paths:
  - `BessZoningPrecheckError(f"{label} values must be unique")` under lexical guard `unique and len(set(values)) != len(values)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_validate_parcels` via `_exact_id_series`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_parcels` via `_exact_id_series`
- direct call: `landscout.stages.interpret_bess_zoning::_validate_zones` via `_exact_id_series`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_zones` via `_exact_id_series`
- direct call: `landscout.stages.interpret_bess_zoning::_validate_relations` via `_exact_id_series`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_relations` via `_exact_id_series`
- direct call: `landscout.stages.interpret_bess_zoning::_validate_mapping` via `_exact_id_series`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_mapping` via `_exact_id_series`
- direct call: `landscout.stages.interpret_bess_zoning::_compare_results` via `_exact_id_series`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_results` via `_exact_id_series`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `series.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `values.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.interpret_bess_zoning._strict_string` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `values.append(_strict_string(value, label))` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_parcels`

**Purpose:** Implements `validate parcels` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _validate_parcels(
    index: PlanningRegulationIndex,
    parcels: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `parcels.copy(deep=True)`
- Explicit raise paths:
  - `BessZoningPrecheckError("parcels must be a GeoDataFrame")` under lexical guard `not isinstance(parcels, gpd.GeoDataFrame)`.
  - `BessZoningPrecheckError("Parcel columns must be unique")` under lexical guard `parcels.columns.has_duplicates`.
  - `BessZoningPrecheckError(f"Parcel input is missing columns: {missing}")` under lexical guard `missing`.
  - `BessZoningPrecheckError(<br>            f"Parcel input already contains precheck columns: {collisions}"<br>        )` under lexical guard `collisions`.
  - `BessZoningPrecheckError("Parcel CRS is required")` under lexical guard `parcels.crs is None`.
  - `BessZoningPrecheckError("Parcel geometry must be active")` under lexical guard `parcels.geometry.name != "geometry"`.
  - `re-raise`.
  - `BessZoningPrecheckError("Parcel CRS or geometry is invalid")`.
  - `BessZoningPrecheckError(<br>            "Parcel geometry must be non-null, non-empty, and valid"<br>        )` under lexical guard `geometry.isna().any() or geometry.is_empty.any() or (~geometry.is_valid).any()`.
  - `BessZoningPrecheckError("Parcel geometry must be Polygon or MultiPolygon")` under lexical guard `not geometry.geom_type.isin({"Polygon", "MultiPolygon"}).all()`.
  - `BessZoningPrecheckError(<br>                f"Parcel {document_column} lineage differs from the regulation"<br>            )` under lexical guard `not parcels[document_column].eq(index.document_id).all()`.
  - `BessZoningPrecheckError(<br>                f"Parcel {archive_column} lineage differs from the regulation"<br>            )` under lexical guard `not parcels[archive_column].eq(index.archive_sha256).all()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_validate_parcels`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_validate_parcels`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `required.difference` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(PARCEL_PRECHECK_COLUMNS).intersection` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `CRS.from_user_input` | `pyproj.CRS.from_user_input` |
| `_exact_id_series` | `landscout.stages.interpret_bess_zoning._exact_id_series` |
| `geometry.isna().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.isna` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.is_empty.any` | `unresolved local/third-party receiver; no ownership inferred` |
| `(~geometry.is_valid).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.isin({"Polygon", "MultiPolygon"}).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `geometry.geom_type.isin` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels[column].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_nonnegative_integer` | `landscout.stages.interpret_bess_zoning._strict_nonnegative_integer` |
| `parcels[document_column].eq(index.document_id).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels[document_column].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels[archive_column].eq(index.archive_sha256).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels[archive_column].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `parcels[archive_column].eq(index.archive_sha256).all` |
| CRS/geometry/spatial calculation | `geometry.isna().any`<br>`geometry.isna`<br>`geometry.is_empty.any`<br>`(~geometry.is_valid).any`<br>`geometry.geom_type.isin({"Polygon", "MultiPolygon"}).all`<br>`geometry.geom_type.isin` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_zones`

**Purpose:** Implements `validate zones` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _validate_zones(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `BessZoningPrecheckError("zones must be a DataFrame with unique columns")` under lexical guard `not isinstance(zones, pd.DataFrame) or zones.columns.has_duplicates`.
  - `BessZoningPrecheckError(f"Zone catalog is missing columns: {missing}")` under lexical guard `missing`.
  - `BessZoningPrecheckError("Zone catalog document lineage differs")` under lexical guard `not result["source_document_id"].eq(index.document_id).all()`.
  - `BessZoningPrecheckError("Zone catalog archive lineage differs")` under lexical guard `not result["source_archive_sha256"].eq(index.archive_sha256).all()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_validate_zones`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_validate_zones`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `zones.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_id_series` | `landscout.stages.interpret_bess_zoning._exact_id_series` |
| `result["source_document_id"].eq(index.document_id).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result["source_document_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `result["source_archive_sha256"].eq(index.archive_sha256).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result["source_archive_sha256"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `result["source_layer"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.interpret_bess_zoning._strict_string` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `result["source_archive_sha256"].eq(index.archive_sha256).all`<br>`result["source_archive_sha256"].eq` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_relations`

**Purpose:** Implements `validate relations` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _validate_relations(
    index: PlanningRegulationIndex,
    parcels: gpd.GeoDataFrame,
    zones: pd.DataFrame,
    relations: pd.DataFrame,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `BessZoningPrecheckError(<br>            "zoning_intersections must be a DataFrame with unique columns"<br>        )` under lexical guard `not isinstance(relations, pd.DataFrame) or relations.columns.has_duplicates`.
  - `BessZoningPrecheckError(<br>            f"Zoning relations are missing columns: {missing}"<br>        )` under lexical guard `missing`.
  - `BessZoningPrecheckError("Parcel/zone relations must be unique")` under lexical guard `result.duplicated(["parcel_id", "planning_zone_id"]).any()`.
  - `BessZoningPrecheckError("Zoning relation references an unknown parcel")` under lexical guard `not set(<br>        _exact_id_series(result["parcel_id"], "relation parcel ID", unique=False)<br>    ).issubset(parcel_ids)`.
  - `BessZoningPrecheckError("Zoning relation references an unknown zone")` under lexical guard `expected_zone is None`.
  - `BessZoningPrecheckError(<br>                "Zoning relation zone identity is inconsistent"<br>            )` under lexical guard `source_id != expected_zone["source_zone_id"]<br>            or label != expected_zone["zone_label_raw"]`.
  - `BessZoningPrecheckError(<br>                "Zoning relation source layer is inconsistent"<br>            )` under lexical guard `row["source_layer"] != expected_zone["source_layer"]`.
  - `BessZoningPrecheckError("AREA_OVERLAP requires positive area")` under lexical guard `relation_type == "AREA_OVERLAP" and area <= 0`.
  - `BessZoningPrecheckError("TOUCH_ONLY requires zero area")` under lexical guard `relation_type == "TOUCH_ONLY" and area != 0`.
  - `BessZoningPrecheckError("Zoning relation type is invalid")` under lexical guard `relation_type not in {"AREA_OVERLAP", "TOUCH_ONLY"}`.
  - `BessZoningPrecheckError(<br>                    f"{upper_column} must be positive for a zoning relation"<br>                )` under lexical guard `upper <= 0`.
  - `BessZoningPrecheckError(<br>                    f"Intersection area exceeds {upper_column}"<br>                )` under lexical guard `area - upper > technical_overlay_tolerance(upper)`.
  - `BessZoningPrecheckError(<br>                    f"{area_column} must be positive for a zoning relation"<br>                )` under lexical guard `reference_area <= 0`.
  - `BessZoningPrecheckError(<br>                    f"{percentage_column} is inconsistent with factual areas"<br>                )` under lexical guard `abs(percentage_area - area) > technical_overlay_tolerance(<br>                reference_area<br>            )`.
  - `BessZoningPrecheckError("Zoning relation document lineage differs")` under lexical guard `row["source_document_id"] != index.document_id`.
  - `BessZoningPrecheckError("Zoning relation archive lineage differs")` under lexical guard `row["source_archive_sha256"] != index.archive_sha256`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_validate_relations`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_validate_relations`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.duplicated(["parcel_id", "planning_zone_id"]).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_id_series` | `landscout.stages.interpret_bess_zoning._exact_id_series` |
| `set(<br>        _exact_id_series(result["parcel_id"], "relation parcel ID", unique=False)<br>    ).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `zones.set_index("planning_zone_id")[<br>        ["source_zone_id", "zone_label_raw", "source_layer"]<br>    ].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `zones.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.interpret_bess_zoning._strict_string` |
| `zone_records.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_nonnegative_number` | `landscout.stages.interpret_bess_zoning._strict_nonnegative_number` |
| `technical_overlay_tolerance` | `landscout.stages.planning_overlay.technical_overlay_tolerance` |
| `abs` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | None directly present. |
| CRS/geometry/spatial calculation | `technical_overlay_tolerance` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
        raise BessZoningPrecheckError(
            f"Zoning relations are missing columns: {missing}"
        )
    result = relations.copy(deep=True)
    if result.duplicated(["parcel_id", "planning_zone_id"]).any():
        raise BessZoningPrecheckError("Parcel/zone relations must be unique")
    parcel_ids = set(_exact_id_series(parcels["parcel_id"], "parcel ID", unique=True))
    if not set(
        _exact_id_series(result["parcel_id"], "relation parcel ID", unique=False)
    ).issubset(parcel_ids):
        raise BessZoningPrecheckError("Zoning relation references an unknown parcel")
    zone_records = zones.set_index("planning_zone_id")[
        ["source_zone_id", "zone_label_raw", "source_layer"]
    ].to_dict("index")
    for row in result.to_dict("records"):
        planning_id = _strict_string(
            row["planning_zone_id"], "relation planning zone ID"
        )
        source_id = _strict_string(row["source_zone_id"], "relation source zone ID")
        label = _strict_string(row["zone_label_raw"], "relation raw zone label")
        expected_zone = zone_records.get(planning_id)
        if expected_zone is None:
            raise BessZoningPrecheckError("Zoning relation references an unknown zone")
        if (
            source_id != expected_zone["source_zone_id"]
            or label != expected_zone["zone_label_raw"]
        ):
            raise BessZoningPrecheckError(
                "Zoning relation zone identity is inconsistent"
            )
        if row["source_layer"] != expected_zone["source_layer"]:
            raise BessZoningPrecheckError(
                "Zoning relation source layer is inconsistent"
            )
        relation_type = _strict_string(row["relation_type"], "zoning relation type")
        area = _strict_nonnegative_number(
            row["intersection_area_m2"], "intersection area"
        )
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
            reference_area = _strict_nonnegative_number(row[area_column], area_column)
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_zone_mapping_input_sha256`

**Purpose:** Implements `zone mapping input sha256` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _zone_mapping_input_sha256(
    zones: pd.DataFrame,
    structure: PlanningRegulationStructureResult,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": "landscout.bess_zoning.zone_mapping_input",<br>            "zones": _frame_payload(zones, zone_columns),<br>            "mapping": _frame_payload(<br>                structure.zone_mapping,<br>                tuple(str(column) for column in structure.zone_mapping.columns),<br>            ),<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_zone_mapping_input_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_zone_mapping_input_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.interpret_bess_zoning._canonical_sha256` |
| `_frame_payload` | `landscout.stages.interpret_bess_zoning._frame_payload` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_zone_chapter_rows`

**Purpose:** Implements `zone chapter rows` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _zone_chapter_rows(
    structure: PlanningRegulationStructureResult,
) -> list[dict[str, object]]:
```

- Exact decorators: none.
- Declared return annotation: `list[dict[str, object]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `rows`
- Explicit raise paths:
  - `BessZoningPrecheckError("Regulation zone chapter labels must be unique")` under lexical guard `len(set(labels)) != len(labels)`.
  - `BessZoningPrecheckError(<br>            "Regulation zone chapter section IDs must be unique"<br>        )` under lexical guard `len(set(section_ids)) != len(section_ids)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_required_section_ids_by_chapter` via `_zone_chapter_rows`
- value/type reference: `landscout.stages.interpret_bess_zoning::_required_section_ids_by_chapter` via `_zone_chapter_rows`
- direct call: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `_zone_chapter_rows`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `_zone_chapter_rows`
- direct call: `landscout.stages.interpret_bess_zoning::_validate_mapping` via `_zone_chapter_rows`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_mapping` via `_zone_chapter_rows`
- direct call: `landscout.stages.interpret_bess_zoning::_build_chapter_policy` via `_zone_chapter_rows`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_chapter_policy` via `_zone_chapter_rows`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `structure.sections.loc[<br>        structure.sections["section_type"].eq("ZONE_CHAPTER")<br>    ].to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `structure.sections["section_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.interpret_bess_zoning._strict_string` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |

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
def _zone_chapter_rows(
    structure: PlanningRegulationStructureResult,
) -> list[dict[str, object]]:
    rows = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
    ].to_dict("records")
    labels = [
        _strict_string(row["zone_chapter_label"], "zone chapter label") for row in rows
    ]
    section_ids = [
        _strict_string(row["section_id"], "zone chapter section ID") for row in rows
    ]
    if len(set(labels)) != len(labels):
        raise BessZoningPrecheckError("Regulation zone chapter labels must be unique")
    if len(set(section_ids)) != len(section_ids):
        raise BessZoningPrecheckError(
            "Regulation zone chapter section IDs must be unique"
        )
    return rows
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_required_section_ids_by_chapter`

**Purpose:** Implements `required section ids by chapter` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _required_section_ids_by_chapter(
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> dict[str, tuple[str, ...]]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, tuple[str, ...]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `BessZoningPrecheckError(<br>                    f"Chapter {label} must contain exactly one configured article "<br>                    f"{article_number!r}; found {len(matches)}"<br>                )` under lexical guard `len(matches) != 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `_required_section_ids_by_chapter`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `_required_section_ids_by_chapter`
- direct call: `landscout.stages.interpret_bess_zoning::_build_chapter_policy` via `_required_section_ids_by_chapter`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_chapter_policy` via `_required_section_ids_by_chapter`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_zone_chapter_rows` | `landscout.stages.interpret_bess_zoning._zone_chapter_rows` |
| `structure.sections.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `chapter_ids.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `required_ids.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.interpret_bess_zoning._strict_string` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `required_ids.append(<br>                _strict_string(<br>                    matches[0]["section_id"],<br>                    f"required article {article_number} section ID",<br>                )<br>            )`<br>`result[str(label)] = tuple(required_ids)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _required_section_ids_by_chapter(
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> dict[str, tuple[str, ...]]:
    chapter_ids = {
        row["zone_chapter_label"]: row["section_id"]
        for row in _zone_chapter_rows(structure)
    }
    result: dict[str, tuple[str, ...]] = {}
    section_rows = structure.sections.to_dict("records")
    for label, chapter_id in chapter_ids.items():
        required_ids: list[str] = []
        for article_number in policy.required_zone_article_numbers:
            matches = [
                row
                for row in section_rows
                if row["section_type"] == "ARTICLE"
                and row["parent_section_id"] == chapter_id
                and row["zone_chapter_label"] == label
                and row["article_number_raw"] == article_number
            ]
            if len(matches) != 1:
                raise BessZoningPrecheckError(
                    f"Chapter {label} must contain exactly one configured article "
                    f"{article_number!r}; found {len(matches)}"
                )
            required_ids.append(
                _strict_string(
                    matches[0]["section_id"],
                    f"required article {article_number} section ID",
                )
            )
        result[str(label)] = tuple(required_ids)
    return result
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_evidence_occurrence_uniqueness`

**Purpose:** Implements `validate evidence occurrence uniqueness` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _validate_evidence_occurrence_uniqueness(catalog: pd.DataFrame) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `catalog` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessZoningPrecheckError(<br>            f"Evidence catalog lacks occurrence fields: {sorted(missing)}"<br>        )` under lexical guard `missing`.
  - `BessZoningPrecheckError(<br>            "Evidence catalog contains a duplicate chapter-scoped evidence occurrence"<br>        )` under lexical guard `catalog.duplicated(list(_EVIDENCE_OCCURRENCE_COLUMNS)).any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `_validate_evidence_occurrence_uniqueness`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `_validate_evidence_occurrence_uniqueness`
- direct call: `landscout.stages.interpret_bess_zoning::_compare_results` via `_validate_evidence_occurrence_uniqueness`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_results` via `_validate_evidence_occurrence_uniqueness`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `set(_EVIDENCE_OCCURRENCE_COLUMNS).difference` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `catalog.duplicated(list(_EVIDENCE_OCCURRENCE_COLUMNS)).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `catalog.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_policy_evidence`

**Purpose:** Implements `validate policy evidence` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

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

- Exact decorators: none.
- Declared return annotation: `tuple[dict[str, dict[str, object]], pd.DataFrame]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |
| `fragments` | positional-or-keyword | `pd.DataFrame` | `required` |
| `policy_hash` | positional-or-keyword | `str` | `required` |
| `evidence_route_links` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `chapters, catalog`
- Explicit raise paths:
  - `BessZoningPrecheckError(<br>            f"Chapter policy completeness differs; missing={missing}, extra={extra}"<br>        )` under lexical guard `policy_labels != set(chapters)`.
  - `BessZoningPrecheckError(<br>                    f"Reviewed section {reviewed_id!r} is unknown"<br>                )` under lexical guard `reviewed is None`.
  - `BessZoningPrecheckError(<br>                    f"Reviewed section {reviewed_id!r} is not a zone/general section"<br>                )` under lexical guard `reviewed["section_type"] not in {"ZONE_CHAPTER", "ARTICLE"}`.
  - `BessZoningPrecheckError(<br>                    f"Reviewed section {reviewed_id!r} belongs to another chapter"<br>                )` under lexical guard `reviewed["zone_chapter_label"] != chapter.resolved_zone_chapter_label`.
  - `BessZoningPrecheckError(<br>                    f"Reviewed section {reviewed_id!r} has another chapter parent"<br>                )` under lexical guard `reviewed["section_type"] == "ARTICLE"<br>                and reviewed["parent_section_id"] != chapter_id`.
  - `BessZoningPrecheckError(<br>                f"Chapter {chapter.resolved_zone_chapter_label} omits required reviewed articles: {missing_required}"<br>            )` under lexical guard `chapter.review_completeness<br>            == "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"<br>            and missing_required`.
  - `BessZoningPrecheckError(<br>                    f"Evidence {evidence.evidence_id} references an unknown section"<br>                )` under lexical guard `section is None`.
  - `BessZoningPrecheckError(<br>                    f"Evidence {evidence.evidence_id} belongs to another zone chapter"<br>                )` under lexical guard `section_type == "GENERAL"`.
  - `BessZoningPrecheckError(<br>                    f"Evidence {evidence.evidence_id} has the wrong chapter parent"<br>                )` under lexical guard `section_type == "ARTICLE" and section["parent_section_id"] != chapter_id`.
  - `BessZoningPrecheckError(<br>                    f"Evidence {evidence.evidence_id} is outside reviewed sections"<br>                )` under lexical guard `evidence.section_id not in reviewed_ids`.
  - `BessZoningPrecheckError(<br>                    f"Evidence {evidence.evidence_id} has no factual section/page fragment"<br>                )` under lexical guard `fragment is None`.
  - `BessZoningPrecheckError(<br>                    f"Evidence {evidence.evidence_id} fragment text is invalid"<br>                )` under lexical guard `not isinstance(raw_fragment, str)`.
  - `BessZoningPrecheckError(<br>                    f"Evidence {evidence.evidence_id} fragment SHA256 differs"<br>                )` under lexical guard `fragment["section_page_fragment_sha256"]<br>                != evidence.section_page_fragment_sha256`.
  - `BessZoningPrecheckError(<br>                    f"Evidence {evidence.evidence_id} offsets do not identify its exact excerpt"<br>                )` under lexical guard `evidence.excerpt_end > len(raw_fragment)<br>                or raw_fragment[evidence.excerpt_start : evidence.excerpt_end]<br>                != excerpt`.
  - `BessZoningPrecheckError(<br>                    f"Evidence {evidence.evidence_id} excerpt SHA256 differs"<br>                )` under lexical guard `sha256(excerpt.encode("utf-8")).hexdigest() != evidence.excerpt_sha256`.
  - `BessZoningPrecheckError(<br>                    f"Evidence {evidence.evidence_id} source-rule offsets differ"<br>                )` under lexical guard `evidence.source_rule_end > len(raw_fragment)<br>                or raw_fragment[evidence.source_rule_start : evidence.source_rule_end]<br>                != rule`.
  - `BessZoningPrecheckError(<br>                    f"Evidence {evidence.evidence_id} source-rule SHA256 differs"<br>                )` under lexical guard `sha256(rule.encode("utf-8")).hexdigest() != evidence.source_rule_sha256`.
  - `BessZoningPrecheckError(<br>                    f"Evidence {evidence.evidence_id} is outside its source rule"<br>                )` under lexical guard `rule[relative_start:relative_end] != excerpt`.
  - `BessZoningPrecheckError("Evidence catalog IDs must be unique")` under lexical guard `catalog["evidence_id"].duplicated().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_validate_policy_evidence`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_validate_policy_evidence`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_strict_string` | `landscout.stages.interpret_bess_zoning._strict_string` |
| `structure.sections.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_positive_integer` | `landscout.stages.interpret_bess_zoning._strict_positive_integer` |
| `fragments.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_zone_chapter_rows` | `landscout.stages.interpret_bess_zoning._zone_chapter_rows` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(chapters).difference` | `unresolved local/third-party receiver; no ownership inferred` |
| `policy_labels.difference` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `evidence_route_links.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `links_by_evidence.setdefault(evidence_id, []).append` | `unresolved local/third-party receiver; no ownership inferred` |
| `links_by_evidence.setdefault` | `unresolved local/third-party receiver; no ownership inferred` |
| `_required_section_ids_by_chapter` | `landscout.stages.interpret_bess_zoning._required_section_ids_by_chapter` |
| `sections.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `required_ids.difference` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `links_by_evidence.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `fragment_records.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(excerpt.encode("utf-8")).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256` | `hashlib.sha256` |
| `excerpt.encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `sha256(rule.encode("utf-8")).hexdigest` | `unresolved local/third-party receiver; no ownership inferred` |
| `rule.encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `catalog_rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `catalog[column].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `catalog["decision_linked"].astype` | `unresolved local/third-party receiver; no ownership inferred` |
| `catalog["evidence_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `catalog["evidence_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_evidence_occurrence_uniqueness` | `landscout.stages.interpret_bess_zoning._validate_evidence_occurrence_uniqueness` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `sha256(excerpt.encode("utf-8")).hexdigest`<br>`sha256`<br>`sha256(rule.encode("utf-8")).hexdigest` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `links_by_evidence.setdefault(evidence_id, []).append(<br>            (<br>                _strict_string(link["route_id"], "linked route ID"),<br>                _strict_string(link["route_role"], "route role"),<br>            )<br>        )`<br>`links_by_evidence.setdefault(evidence_id, [])`<br>`catalog_rows.append(<br>                {<br>                    "evidence_id": evidence.evidence_id,<br>                    "resolved_zone_chapter_label": (<br>                        chapter.resolved_zone_chapter_label<br>                    ),<br>                    "section_id": evidence.section_id,<br>                    "page_number": evidence.page_number,<br>                    "evidence_kind": evidence.evidence_kind,<br>                    "evidence_direction": evidence.evidence_direction,<br>                    "linked_route_ids": tuple(item[0] for item in reverse_links),<br>                    "linked_route_roles": tuple(item[1] for item in reverse_links),<br>                    "decision_linked": bool(reverse_links),<br>                    "exact_raw_excerpt": excerpt,<br>                    "excerpt_sha256": evidence.excerpt_sha256,<br>                    "section_page_fragment_sha256": (<br>                        evidence.section_page_fragment_sha256<br>                    ),<br>                    "excerpt_start": evidence.excerpt_start,<br>                    "excerpt_end": evidence.excerpt_end,<br>                    "source_rule_id": evidence.source_rule_id,<br>                    "source_rule_excerpt": rule,<br>                    "source_rule_sha256": evidence.source_rule_sha256,<br>                    "source_rule_start": evidence.source_rule_start,<br>                    "source_rule_end": evidence.source_rule_end,<br>                    "interpretation_note": evidence.interpretation_note,<br>                    "review_completeness": chapter.review_completeness,<br>                    "review_scope": policy.review_scope,<br>                    "policy_profile": policy.policy_profile,<br>                    "policy_sha256": policy_hash,<br>                    "document_id": index.document_id,<br>                    "archive_sha256": index.archive_sha256,<br>                    "pdf_sha256": index.pdf_sha256,<br>                    "index_content_sha256": index.index_content_sha256,<br>                    "structure_result_content_sha256": (<br>                        structure.structure_result_content_sha256<br>                    ),<br>                    "structure_profile": structure.structure_profile,<br>                }<br>            )`<br>`catalog[column] = catalog[column].astype("int64")`<br>`catalog["decision_linked"] = catalog["decision_linked"].astype("bool")` |
| Direct parameter mutation | None directly present. |

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
            if (
                fragment["section_page_fragment_sha256"]
                != evidence.section_page_fragment_sha256
            ):
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} fragment SHA256 differs"
                )
            if (
                evidence.excerpt_end > len(raw_fragment)
                or raw_fragment[evidence.excerpt_start : evidence.excerpt_end]
                != excerpt
            ):
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} offsets do not identify its exact excerpt"
                )
            if sha256(excerpt.encode("utf-8")).hexdigest() != evidence.excerpt_sha256:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} excerpt SHA256 differs"
                )
            rule = evidence.source_rule_excerpt
            if (
                evidence.source_rule_end > len(raw_fragment)
                or raw_fragment[evidence.source_rule_start : evidence.source_rule_end]
                != rule
            ):
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_mapping`

**Purpose:** Implements `validate mapping` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _validate_mapping(
    structure: PlanningRegulationStructureResult,
    zones: pd.DataFrame,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `mapping`
- Explicit raise paths:
  - `BessZoningPrecheckError(<br>            "Factual zone mapping is incomplete or has extras"<br>        )` under lexical guard `mapped_labels != source_labels`.
  - `BessZoningPrecheckError(<br>                f"Source zone {row['source_zone_label_raw']!r} is not resolved"<br>            )` under lexical guard `status not in _RESOLVED_MAPPING_STATUSES`.
  - `BessZoningPrecheckError(<br>                "Zone mapping chapter identity is inconsistent"<br>            )` under lexical guard `chapters.get(resolved) != row["matched_section_id"]`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_validate_mapping`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_validate_mapping`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `structure.zone_mapping.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_id_series` | `landscout.stages.interpret_bess_zoning._exact_id_series` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `_zone_chapter_rows` | `landscout.stages.interpret_bess_zoning._zone_chapter_rows` |
| `mapping.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.interpret_bess_zoning._strict_string` |
| `chapters.get` | `unresolved local/third-party receiver; no ownership inferred` |

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
        raise BessZoningPrecheckError(
            "Factual zone mapping is incomplete or has extras"
        )
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
            raise BessZoningPrecheckError(
                "Zone mapping chapter identity is inconsistent"
            )
    return mapping
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_lineage`

**Purpose:** Implements `lineage` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _lineage(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |
| `policy_hash` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "planning_precheck_scope": PLANNING_PRECHECK_SCOPE,<br>        "review_scope": REVIEW_SCOPE,<br>        "policy_profile": policy.policy_profile,<br>        "policy_sha256": policy_hash,<br>        "document_id": index.document_id,<br>        "archive_sha256": index.archive_sha256,<br>        "pdf_sha256": index.pdf_sha256,<br>        "index_content_sha256": index.index_content_sha256,<br>        "structure_result_content_sha256": structure.structure_result_content_sha256,<br>        "structure_profile": structure.structure_profile,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_chapter_policy` via `_lineage`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_chapter_policy` via `_lineage`
- direct call: `landscout.stages.interpret_bess_zoning::_build_route_assessments` via `_lineage`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_route_assessments` via `_lineage`
- direct call: `landscout.stages.interpret_bess_zoning::_build_evidence_route_links` via `_lineage`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_evidence_route_links` via `_lineage`
- direct call: `landscout.stages.interpret_bess_zoning::_build_source_zone_policy` via `_lineage`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_source_zone_policy` via `_lineage`
- direct call: `landscout.stages.interpret_bess_zoning::_build_parcel_zone_interpretations` via `_lineage`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_parcel_zone_interpretations` via `_lineage`

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_chapter_policy`

**Purpose:** Implements `build chapter policy` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _build_chapter_policy(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |
| `policy_hash` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_build_chapter_policy`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_build_chapter_policy`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lineage` | `landscout.stages.interpret_bess_zoning._lineage` |
| `_zone_chapter_rows` | `landscout.stages.interpret_bess_zoning._zone_chapter_rows` |
| `_required_section_ids_by_chapter` | `landscout.stages.interpret_bess_zoning._required_section_ids_by_chapter` |
| `_strict_string` | `landscout.stages.interpret_bess_zoning._strict_string` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `frame["evidence_count"].astype` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `rows.append(<br>            {<br>                "resolved_zone_chapter_label": label,<br>                "chapter_section_id": chapter_section_id,<br>                "review_completeness": chapter.review_completeness,<br>                "review_scope": policy.review_scope,<br>                "reviewed_section_ids": tuple(chapter.reviewed_section_ids),<br>                "missing_required_section_ids": tuple(<br>                    section_id<br>                    for section_id in required_by_chapter[label]<br>                    if section_id not in set(chapter.reviewed_section_ids)<br>                ),<br>                "review_note": chapter.review_note,<br>                "zoning_precheck_status": chapter.zoning_precheck_status,<br>                "zoning_precheck_confidence": chapter.zoning_precheck_confidence,<br>                "evidence_count": len(evidence_ids),<br>                "evidence_ids": evidence_ids,<br>                "decision_evidence_ids": decision_evidence_ids,<br>                "context_evidence_ids": context_evidence_ids,<br>                "rationale": chapter.rationale,<br>                "missing_information": chapter.missing_information,<br>                **lineage,<br>            }<br>        )`<br>`frame["evidence_count"] = frame["evidence_count"].astype("int64")` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_route_status`

**Purpose:** Implements `route status` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _route_status(route_kind: RouteKind) -> ChapterStatus:
```

- Exact decorators: none.
- Declared return annotation: `ChapterStatus`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `route_kind` | positional-or-keyword | `RouteKind` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `statuses[route_kind]`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_route_assessments` via `_route_status`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_route_assessments` via `_route_status`

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_route_assessments`

**Purpose:** Implements `build route assessments` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _build_route_assessments(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |
| `policy_hash` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- Explicit raise paths:
  - `BessZoningPrecheckError("Normalized route IDs must be unique")` under lexical guard `frame["route_id"].duplicated().any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_build_route_assessments`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_build_route_assessments`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lineage` | `landscout.stages.interpret_bess_zoning._lineage` |
| `_route_status` | `landscout.stages.interpret_bess_zoning._route_status` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `frame["route_id"].duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["route_id"].duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_evidence_route_links`

**Purpose:** Implements `build evidence route links` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _build_evidence_route_links(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |
| `policy_hash` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- Explicit raise paths:
  - `BessZoningPrecheckError(<br>            "Evidence-route links must be unique by route and evidence"<br>        )` under lexical guard `frame.duplicated(["route_id", "evidence_id"]).any()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_build_evidence_route_links`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_build_evidence_route_links`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_lineage` | `landscout.stages.interpret_bess_zoning._lineage` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `frame.sort_values(<br>            ["route_id", "evidence_id"], kind="mergesort"<br>        ).reset_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.sort_values` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.duplicated(["route_id", "evidence_id"]).any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |

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
| In-memory mutation | `rows.append(<br>                        {<br>                            "route_id": route.route_id,<br>                            "resolved_zone_chapter_label": (<br>                                chapter.resolved_zone_chapter_label<br>                            ),<br>                            "route_kind": route.route_kind,<br>                            "evidence_id": evidence_id,<br>                            "route_role": role,<br>                            "evidence_direction": direction,<br>                            "review_completeness": chapter.review_completeness,<br>                            "review_scope": policy.review_scope,<br>                            **lineage,<br>                        }<br>                    )` |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_source_zone_policy`

**Purpose:** Implements `build source zone policy` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

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

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |
| `policy_hash` | positional-or-keyword | `str` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `mapping` | positional-or-keyword | `pd.DataFrame` | `required` |
| `chapter_policy` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `pd.DataFrame(rows, columns=SOURCE_ZONE_POLICY_COLUMNS)`
- Explicit raise paths:
  - `BessZoningPrecheckError(<br>                f"Source zone label {label!r} has ambiguous source-layer lineage"<br>            )` under lexical guard `len(layers) != 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_build_source_zone_policy`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_build_source_zone_policy`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `chapter_policy.set_index("resolved_zone_chapter_label").to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `chapter_policy.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `_lineage` | `landscout.stages.interpret_bess_zoning._lineage` |
| `zones.groupby` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict.fromkeys` | `unresolved local/third-party receiver; no ownership inferred` |
| `group["source_layer"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.interpret_bess_zoning._strict_string` |
| `mapping.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |

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
| In-memory mutation | `layers_by_label[str(label)] = _strict_string(layers[0], "zone source layer")`<br>`rows.append(<br>            {<br>                "source_zone_label_raw": source["source_zone_label_raw"],<br>                "resolved_zone_chapter_label": source["resolved_zone_chapter_label"],<br>                "mapping_status": source["mapping_status"],<br>                "matched_section_id": source["matched_section_id"],<br>                "source_layer": layers_by_label[source["source_zone_label_raw"]],<br>                "zoning_precheck_status": chapter["zoning_precheck_status"],<br>                "zoning_precheck_confidence": chapter["zoning_precheck_confidence"],<br>                "evidence_ids": tuple(chapter["evidence_ids"]),<br>                "decision_evidence_ids": tuple(chapter["decision_evidence_ids"]),<br>                "context_evidence_ids": tuple(chapter["context_evidence_ids"]),<br>                **lineage,<br>            }<br>        )` |
| Direct parameter mutation | None directly present. |

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
                "resolved_zone_chapter_label": source["resolved_zone_chapter_label"],
                "mapping_status": source["mapping_status"],
                "matched_section_id": source["matched_section_id"],
                "source_layer": layers_by_label[source["source_zone_label_raw"]],
                "zoning_precheck_status": chapter["zoning_precheck_status"],
                "zoning_precheck_confidence": chapter["zoning_precheck_confidence"],
                "evidence_ids": tuple(chapter["evidence_ids"]),
                "decision_evidence_ids": tuple(chapter["decision_evidence_ids"]),
                "context_evidence_ids": tuple(chapter["context_evidence_ids"]),
                **lineage,
            }
        )
    return pd.DataFrame(rows, columns=SOURCE_ZONE_POLICY_COLUMNS)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_parcel_zone_interpretations`

**Purpose:** Implements `build parcel zone interpretations` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

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

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |
| `policy_hash` | positional-or-keyword | `str` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `source_policy` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_build_parcel_zone_interpretations`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_build_parcel_zone_interpretations`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `source_policy.set_index("source_zone_label_raw").to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `source_policy.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `_lineage` | `landscout.stages.interpret_bess_zoning._lineage` |
| `relations["relation_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `positive.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `rows.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `pd.Series` | `pandas.Series` |

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
| In-memory mutation | `rows.append(<br>            {<br>                "parcel_id": source["parcel_id"],<br>                "planning_zone_id": source["planning_zone_id"],<br>                "source_zone_id": source["source_zone_id"],<br>                "source_zone_label_raw": source["zone_label_raw"],<br>                "resolved_zone_chapter_label": item["resolved_zone_chapter_label"],<br>                "intersection_area_m2": float(source["intersection_area_m2"]),<br>                "parcel_share_pct": float(source["parcel_share_pct"]),<br>                "zoning_precheck_status": item["zoning_precheck_status"],<br>                "zoning_precheck_confidence": item["zoning_precheck_confidence"],<br>                "evidence_ids": tuple(item["evidence_ids"]),<br>                "decision_evidence_ids": tuple(item["decision_evidence_ids"]),<br>                "context_evidence_ids": tuple(item["context_evidence_ids"]),<br>                **lineage,<br>                "source_layer": source["source_layer"],<br>            }<br>        )` |
| Direct parameter mutation | None directly present. |

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
                "resolved_zone_chapter_label": item["resolved_zone_chapter_label"],
                "intersection_area_m2": float(source["intersection_area_m2"]),
                "parcel_share_pct": float(source["parcel_share_pct"]),
                "zoning_precheck_status": item["zoning_precheck_status"],
                "zoning_precheck_confidence": item["zoning_precheck_confidence"],
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_is_null`

**Purpose:** Implements `is null` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _is_null(value: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `True`
  - `False`
  - `isinstance(null, (bool, np.bool_)) and bool(null)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_parcel_output` via `_is_null`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_parcel_output` via `_is_null`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `pd.isna` | `pandas.isna` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_parcel_output`

**Purpose:** Implements `build parcel output` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

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

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `interpretations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |
| `policy_hash` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- Explicit raise paths:
  - `BessZoningPrecheckError(<br>                    "Parcel dominant zone exists without a positive-area relation"<br>                )` under lexical guard `group is None or group.empty`.
  - `BessZoningPrecheckError(<br>                    "Parcel dominant zone differs from factual positive-area relations"<br>                )` under lexical guard `group is None or group.empty`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_build_parcel_output`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_build_parcel_output`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `parcels.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `group.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `interpretations.groupby` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.loc[relations["relation_type"].eq("TOUCH_ONLY")]<br>        .groupby("parcel_id", sort=False)<br>        .size()<br>        .to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.loc[relations["relation_type"].eq("TOUCH_ONLY")]<br>        .groupby("parcel_id", sort=False)<br>        .size` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.loc[relations["relation_type"].eq("TOUCH_ONLY")]<br>        .groupby` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations["relation_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcels.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `positive_by_parcel.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `_is_null` | `landscout.stages.interpret_bess_zoning._is_null` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `group.sort_values` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `group["zoning_precheck_status"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `(<br>                    group.loc[<br>                        ~group["planning_zone_id"].eq(expected_dominant),<br>                        "zoning_precheck_status",<br>                    ]<br>                    != dominant_status<br>                ).sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `group["planning_zone_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.interpret_bess_zoning._strict_string` |
| `group["decision_evidence_ids"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `group["context_evidence_ids"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["zoning_precheck_status"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["dominant_zone_precheck_status"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["dominant_zone_precheck_confidence"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["positive_area_zone_count"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["distinct_zone_status_count"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["non_dominant_different_status_count"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["touch_only_zone_count"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `touch_counts.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["zoning_precheck_evidence_ids"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["zoning_precheck_context_evidence_ids"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["zoning_precheck_requires_formal_review"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["planning_precheck_scope"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["review_scope"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["non_zoning_planning_features_interpreted"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["zoning_precheck_policy_profile"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `summary["zoning_precheck_policy_sha256"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `np.empty` | `numpy.empty` |
| `output[column].astype` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `summary["zoning_precheck_policy_sha256"].append` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `summary["zoning_precheck_status"].append(overall_status)`<br>`summary["dominant_zone_precheck_status"].append(dominant_status)`<br>`summary["dominant_zone_precheck_confidence"].append(dominant_confidence)`<br>`summary["positive_area_zone_count"].append(positive_count)`<br>`summary["distinct_zone_status_count"].append(distinct_count)`<br>`summary["non_dominant_different_status_count"].append(non_dominant_different)`<br>`summary["touch_only_zone_count"].append(int(touch_counts.get(parcel_id, 0)))`<br>`summary["zoning_precheck_evidence_ids"].append(evidence_ids)`<br>`summary["zoning_precheck_context_evidence_ids"].append(context_evidence_ids)`<br>`summary["zoning_precheck_requires_formal_review"].append(True)`<br>`summary["planning_precheck_scope"].append(PLANNING_PRECHECK_SCOPE)`<br>`summary["review_scope"].append(REVIEW_SCOPE)`<br>`summary["non_zoning_planning_features_interpreted"].append(False)`<br>`summary["zoning_precheck_policy_profile"].append(policy.policy_profile)`<br>`summary["zoning_precheck_policy_sha256"].append(policy_hash)`<br>`values[:] = summary[column]`<br>`output[column] = values`<br>`output[column] = output[column].astype("int64")`<br>`output[column] = output[column].astype("bool")` |
| Direct parameter mutation | None directly present. |

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
    summary: dict[str, list[object]] = {
        column: [] for column in PARCEL_PRECHECK_COLUMNS
    }
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
                statuses[0] if len(distinct_statuses) == 1 else "MIXED_REVIEW_REQUIRED"
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
        summary["non_dominant_different_status_count"].append(non_dominant_different)
        summary["touch_only_zone_count"].append(int(touch_counts.get(parcel_id, 0)))
        summary["zoning_precheck_evidence_ids"].append(evidence_ids)
        summary["zoning_precheck_context_evidence_ids"].append(context_evidence_ids)
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_result_component_metadata`

**Purpose:** Implements `result component metadata` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _result_component_metadata(result: BessZoningPrecheckResult) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessZoningPrecheckResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "result_hash_schema_version": result.result_hash_schema_version,<br>        "policy_schema_version": result.policy_schema_version,<br>        "policy_profile": result.policy_profile,<br>        "planning_precheck_scope": result.planning_precheck_scope,<br>        "review_scope": result.review_scope,<br>        "document_id": result.document_id,<br>        "archive_sha256": result.archive_sha256,<br>        "pdf_sha256": result.pdf_sha256,<br>        "index_content_sha256": result.index_content_sha256,<br>        "structure_result_content_sha256": result.structure_result_content_sha256,<br>        "structure_profile": result.structure_profile,<br>        "policy_config_sha256": result.policy_config_sha256,<br>        "factual_structure_content_sha256": result.factual_structure_content_sha256,<br>        "zone_mapping_input_sha256": result.zone_mapping_input_sha256,<br>        "zoning_relation_hash_columns": list(result.zoning_relation_hash_columns),<br>        "zoning_relations_input_sha256": result.zoning_relations_input_sha256,<br>        "touch_only_relation_count": result.touch_only_relation_count,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_result_frame_sha256` via `_result_component_metadata`
- value/type reference: `landscout.stages.interpret_bess_zoning::_result_frame_sha256` via `_result_component_metadata`
- direct call: `landscout.stages.interpret_bess_zoning::_complete_result_sha256` via `_result_component_metadata`
- value/type reference: `landscout.stages.interpret_bess_zoning::_complete_result_sha256` via `_result_component_metadata`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `list` | `unresolved local/third-party receiver; no ownership inferred` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_result_frame_sha256`

**Purpose:** Implements `result frame sha256` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _result_frame_sha256(
    domain: str,
    result: BessZoningPrecheckResult,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `domain` | positional-or-keyword | `str` | `required` |
| `result` | positional-or-keyword | `BessZoningPrecheckResult` | `required` |
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |
| `columns` | positional-or-keyword | `Sequence[str]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": domain,<br>            **_result_component_metadata(result),<br>            "frame": _frame_payload(frame, columns),<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_result_with_hashes` via `_result_frame_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_result_with_hashes` via `_result_frame_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.interpret_bess_zoning._canonical_sha256` |
| `_result_component_metadata` | `landscout.stages.interpret_bess_zoning._result_component_metadata` |
| `_frame_payload` | `landscout.stages.interpret_bess_zoning._frame_payload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_complete_result_sha256`

**Purpose:** Implements `complete result sha256` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _complete_result_sha256(result: BessZoningPrecheckResult) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessZoningPrecheckResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_sha256(<br>        {<br>            "domain": "landscout.bess_zoning.precheck_result",<br>            **_result_component_metadata(result),<br>            "evidence_catalog_content_sha256": (result.evidence_catalog_content_sha256),<br>            "evidence_route_links_content_sha256": (<br>                result.evidence_route_links_content_sha256<br>            ),<br>            "route_assessments_content_sha256": (<br>                result.route_assessments_content_sha256<br>            ),<br>            "chapter_policy_content_sha256": result.chapter_policy_content_sha256,<br>            "source_zone_policy_content_sha256": (<br>                result.source_zone_policy_content_sha256<br>            ),<br>            "parcel_zone_policy_content_sha256": (<br>                result.parcel_zone_policy_content_sha256<br>            ),<br>            "parcel_output_content_sha256": result.parcel_output_content_sha256,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_result_with_hashes` via `_complete_result_sha256`
- value/type reference: `landscout.stages.interpret_bess_zoning::_result_with_hashes` via `_complete_result_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_sha256` | `landscout.stages.interpret_bess_zoning._canonical_sha256` |
| `_result_component_metadata` | `landscout.stages.interpret_bess_zoning._result_component_metadata` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _complete_result_sha256(result: BessZoningPrecheckResult) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.bess_zoning.precheck_result",
            **_result_component_metadata(result),
            "evidence_catalog_content_sha256": (result.evidence_catalog_content_sha256),
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_result_with_hashes`

**Purpose:** Implements `result with hashes` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _result_with_hashes(
    result: BessZoningPrecheckResult,
) -> BessZoningPrecheckResult:
```

- Exact decorators: none.
- Declared return annotation: `BessZoningPrecheckResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessZoningPrecheckResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(<br>        component,<br>        complete_result_content_sha256=_complete_result_sha256(component),<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_build_result` via `_result_with_hashes`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `_result_with_hashes`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
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
)`
- direct call: `tests.unit.test_interpret_bess_zoning::test_repeated_excerpt_occurrence_is_bound_to_policy` via `_result_with_hashes`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_repeated_excerpt_occurrence_is_bound_to_policy` via `_result_with_hashes`
- direct call: `tests.unit.test_interpret_bess_zoning::test_coordinated_result_mutation_is_rejected` via `_result_with_hashes`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_result_mutation_is_rejected` via `_result_with_hashes`
- direct call: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_catalog_mutation_is_rejected` via `_result_with_hashes`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_catalog_mutation_is_rejected` via `_result_with_hashes`
- direct call: `tests.unit.test_interpret_bess_zoning::test_coordinated_catalog_occurrence_duplicate_is_rejected` via `_result_with_hashes`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_catalog_occurrence_duplicate_is_rejected` via `_result_with_hashes`
- direct call: `tests.unit.test_interpret_bess_zoning::test_coordinated_route_table_mutation_is_rejected` via `_result_with_hashes`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_route_table_mutation_is_rejected` via `_result_with_hashes`
- direct call: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_route_link_mutation_is_rejected` via `_result_with_hashes`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_evidence_route_link_mutation_is_rejected` via `_result_with_hashes`
- direct call: `tests.unit.test_interpret_bess_zoning::test_coordinated_reverse_link_mutation_is_rejected` via `_result_with_hashes`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_coordinated_reverse_link_mutation_is_rejected` via `_result_with_hashes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `_result_frame_sha256` | `landscout.stages.interpret_bess_zoning._result_frame_sha256` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `_complete_result_sha256` | `landscout.stages.interpret_bess_zoning._complete_result_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_result_frame_sha256`<br>`_complete_result_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_result`

**Purpose:** Implements `build result` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

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

- Exact decorators: none.
- Declared return annotation: `BessZoningPrecheckResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `structure_config` | positional-or-keyword | `PlanningRegulationStructureConfig \| str \| Path` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `zoning_intersections` | positional-or-keyword | `pd.DataFrame` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_result_with_hashes(result)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `_build_result`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `_build_result`
- direct call: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `_build_result`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `_build_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_planning_regulation_index` | `landscout.stages.index_planning_regulation.validate_planning_regulation_index` |
| `validate_planning_regulation_structure_with_fragments` | `landscout.stages.structure_planning_regulation.validate_planning_regulation_structure_with_fragments` |
| `_validate_policy_lock` | `landscout.stages.interpret_bess_zoning._validate_policy_lock` |
| `_validate_parcels` | `landscout.stages.interpret_bess_zoning._validate_parcels` |
| `_validate_zones` | `landscout.stages.interpret_bess_zoning._validate_zones` |
| `_validate_relations` | `landscout.stages.interpret_bess_zoning._validate_relations` |
| `_validate_mapping` | `landscout.stages.interpret_bess_zoning._validate_mapping` |
| `_policy_sha256` | `landscout.stages.interpret_bess_zoning._policy_sha256` |
| `_build_route_assessments` | `landscout.stages.interpret_bess_zoning._build_route_assessments` |
| `_build_evidence_route_links` | `landscout.stages.interpret_bess_zoning._build_evidence_route_links` |
| `_validate_policy_evidence` | `landscout.stages.interpret_bess_zoning._validate_policy_evidence` |
| `_build_chapter_policy` | `landscout.stages.interpret_bess_zoning._build_chapter_policy` |
| `_build_source_zone_policy` | `landscout.stages.interpret_bess_zoning._build_source_zone_policy` |
| `_build_parcel_zone_interpretations` | `landscout.stages.interpret_bess_zoning._build_parcel_zone_interpretations` |
| `_build_parcel_output` | `landscout.stages.interpret_bess_zoning._build_parcel_output` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckResult` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult` |
| `_factual_structure_sha256` | `landscout.stages.interpret_bess_zoning._factual_structure_sha256` |
| `_zone_mapping_input_sha256` | `landscout.stages.interpret_bess_zoning._zone_mapping_input_sha256` |
| `_frame_sha256` | `landscout.stages.interpret_bess_zoning._frame_sha256` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy["relation_type"].eq("TOUCH_ONLY").sum` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_copy["relation_type"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `_result_with_hashes` | `landscout.stages.interpret_bess_zoning._result_with_hashes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_policy_sha256`<br>`_factual_structure_sha256`<br>`_zone_mapping_input_sha256`<br>`_frame_sha256`<br>`_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

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
    route_assessments = _build_route_assessments(index, structure, policy, policy_hash)
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
    chapter_policy = _build_chapter_policy(index, structure, policy, policy_hash)
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_compare_frames`

**Purpose:** Implements `compare frames` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _compare_frames(
    actual: pd.DataFrame,
    expected: pd.DataFrame,
    columns: Sequence[str],
    label: str,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `actual` | positional-or-keyword | `pd.DataFrame` | `required` |
| `expected` | positional-or-keyword | `pd.DataFrame` | `required` |
| `columns` | positional-or-keyword | `Sequence[str]` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessZoningPrecheckError(f"{label} schema differs from rebuilt result")` under lexical guard `tuple(actual.columns) != tuple(expected.columns) or tuple(<br>        actual.columns<br>    ) != tuple(columns)`.
  - `BessZoningPrecheckError(f"{label} differs from rebuilt source evidence")` under lexical guard `_canonical_value(_frame_payload(actual, columns)) != _canonical_value(<br>        _frame_payload(expected, columns)<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::_compare_results` via `_compare_frames`
- value/type reference: `landscout.stages.interpret_bess_zoning::_compare_results` via `_compare_frames`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `_canonical_value` | `landscout.stages.interpret_bess_zoning._canonical_value` |
| `_frame_payload` | `landscout.stages.interpret_bess_zoning._frame_payload` |

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
def _compare_frames(
    actual: pd.DataFrame,
    expected: pd.DataFrame,
    columns: Sequence[str],
    label: str,
) -> None:
    if tuple(actual.columns) != tuple(expected.columns) or tuple(
        actual.columns
    ) != tuple(columns):
        raise BessZoningPrecheckError(f"{label} schema differs from rebuilt result")
    if _canonical_value(_frame_payload(actual, columns)) != _canonical_value(
        _frame_payload(expected, columns)
    ):
        raise BessZoningPrecheckError(f"{label} differs from rebuilt source evidence")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_compare_results`

**Purpose:** Implements `compare results` within the file role: Applies the source-locked written-zoning policy after proving every configured required article exactly once per chapter and reviewed-section closure.

**Exact signature**

```python
def _compare_results(
    result: BessZoningPrecheckResult,
    expected: BessZoningPrecheckResult,
    original_parcels: gpd.GeoDataFrame,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `BessZoningPrecheckResult` | `required` |
| `expected` | positional-or-keyword | `BessZoningPrecheckResult` | `required` |
| `original_parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `BessZoningPrecheckError("result must be a BessZoningPrecheckResult")` under lexical guard `not isinstance(result, BessZoningPrecheckResult)`.
  - `BessZoningPrecheckError(<br>                f"BESS zoning result {field} differs from rebuilt source evidence"<br>            )` under lexical guard `getattr(result, field) != getattr(expected, field)`.
  - `BessZoningPrecheckError("Unsupported precheck result hash schema")` under lexical guard `_strict_positive_integer(<br>            result.result_hash_schema_version,<br>            "precheck result hash schema version",<br>        )<br>        != RESULT_HASH_SCHEMA_VERSION`.
  - `BessZoningPrecheckError("Unsupported precheck policy schema")` under lexical guard `_strict_positive_integer(<br>            result.policy_schema_version,<br>            "precheck policy schema version",<br>        )<br>        != POLICY_SCHEMA_VERSION`.
  - `BessZoningPrecheckError(<br>            "Zoning relation hash columns must be an exact string tuple"<br>        )` under lexical guard `type(result.zoning_relation_hash_columns) is not tuple or not all(<br>        isinstance(column, str) and column and column == column.strip()<br>        for column in result.zoning_relation_hash_columns<br>    )`.
  - `BessZoningPrecheckError("Existing parcel columns are not preserved")` under lexical guard `tuple(result.parcels.columns[: len(original_columns)]) != original_columns`.
  - `BessZoningPrecheckError(<br>            "Parcel count, IDs, order, index, geometry, CRS, or prior fields changed"<br>        )` under lexical guard `_canonical_value(<br>        _frame_payload(result.parcels, original_columns)<br>    ) != _canonical_value(_frame_payload(original_parcels, original_columns))`.
  - `BessZoningPrecheckError("Chapter policy status is invalid")` under lexical guard `not statuses.issubset(_CHAPTER_STATUSES)`.
  - `BessZoningPrecheckError("Parcel precheck status is invalid")` under lexical guard `not parcel_statuses.issubset(_PARCEL_STATUSES)`.
  - `BessZoningPrecheckError("Chapter policy confidence is invalid")` under lexical guard `not confidences.issubset(_CONFIDENCES)`.
  - `BessZoningPrecheckError("Route evidence IDs must be arrays")` under lexical guard `not isinstance(values, (tuple, list, np.ndarray))`.
  - `BessZoningPrecheckError(<br>            "Evidence-route links do not exactly reproduce route evidence arrays"<br>        )` under lexical guard `len(actual_links) != len(result.evidence_route_links)<br>        or actual_links != expected_links`.
  - `BessZoningPrecheckError(<br>                "Evidence-route link references unknown evidence"<br>            )` under lexical guard `evidence_id not in catalog_by_id`.
  - `BessZoningPrecheckError("Evidence reverse route IDs are inconsistent")` under lexical guard `tuple(row["linked_route_ids"]) != tuple(item[0] for item in links)`.
  - `BessZoningPrecheckError(<br>                "Evidence reverse route roles are inconsistent"<br>            )` under lexical guard `tuple(row["linked_route_roles"]) != tuple(item[1] for item in links)`.
  - `BessZoningPrecheckError(<br>                "Evidence reverse decision link is inconsistent"<br>            )` under lexical guard `bool(row["decision_linked"]) != bool(links)`.
  - `BessZoningPrecheckError(<br>                    "CONTEXT_ONLY evidence must not influence a route"<br>                )` under lexical guard `row["evidence_direction"] == "CONTEXT_ONLY"`.
  - `BessZoningPrecheckError(<br>                    "Decision evidence must be linked to a route"<br>                )` under lexical guard `row["evidence_direction"] == "CONTEXT_ONLY"`.
  - `BessZoningPrecheckError("Evidence references must be arrays")` under lexical guard `not isinstance(values, (tuple, list, np.ndarray))`.
  - `BessZoningPrecheckError(<br>                    "An output evidence ID is absent from the evidence catalog"<br>                )` under lexical guard `not set(values).issubset(evidence_ids)`.
  - `BessZoningPrecheckError(<br>                    "Decision evidence output is inconsistent"<br>                )` under lexical guard `set(row["decision_evidence_ids"]) != retained.intersection(decision_ids)`.
  - `BessZoningPrecheckError("Context evidence output is inconsistent")` under lexical guard `set(row["context_evidence_ids"]) != retained.intersection(context_ids)`.
  - `BessZoningPrecheckError("Parcel decision evidence includes context")` under lexical guard `not set(row["zoning_precheck_evidence_ids"]).issubset(decision_ids)`.
  - `BessZoningPrecheckError("Parcel context evidence includes a decision")` under lexical guard `not set(row["zoning_precheck_context_evidence_ids"]).issubset(context_ids)`.
  - `BessZoningPrecheckError("Every parcel must require formal review")` under lexical guard `not result.parcels["zoning_precheck_requires_formal_review"].eq(True).all()`.
  - `BessZoningPrecheckError(<br>            "Non-zoning planning features must remain uninterpreted"<br>        )` under lexical guard `not result.parcels["non_zoning_planning_features_interpreted"].eq(False).all()`.
  - `BessZoningPrecheckError("Parcel review scope is invalid")` under lexical guard `not result.parcels["review_scope"].eq(REVIEW_SCOPE).all()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `_compare_results`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `_compare_results`
- direct call: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `_compare_results`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `_compare_results`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `_validate_evidence_occurrence_uniqueness` | `landscout.stages.interpret_bess_zoning._validate_evidence_occurrence_uniqueness` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_positive_integer` | `landscout.stages.interpret_bess_zoning._strict_positive_integer` |
| `_strict_nonnegative_integer` | `landscout.stages.interpret_bess_zoning._strict_nonnegative_integer` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `all` | `unresolved local/third-party receiver; no ownership inferred` |
| `column.strip` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validated_sha256` | `landscout.stages.interpret_bess_zoning._validated_sha256` |
| `_compare_frames` | `landscout.stages.interpret_bess_zoning._compare_frames` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_value` | `landscout.stages.interpret_bess_zoning._canonical_value` |
| `_frame_payload` | `landscout.stages.interpret_bess_zoning._frame_payload` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.chapter_policy["zoning_precheck_status"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["zoning_precheck_status"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.chapter_policy["zoning_precheck_confidence"].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `statuses.issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `parcel_statuses.issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `confidences.issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_id_series` | `landscout.stages.interpret_bess_zoning._exact_id_series` |
| `result.evidence_catalog.set_index("evidence_id").to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.evidence_catalog.set_index` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.route_assessments.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `expected_links.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.evidence_route_links.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `reverse_links.setdefault(evidence_id, []).append` | `unresolved local/third-party receiver; no ownership inferred` |
| `reverse_links.setdefault` | `unresolved local/third-party receiver; no ownership inferred` |
| `catalog_by_id.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `reverse_links.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `context_ids.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `decision_ids.add` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame[column].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(values).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `retained.intersection` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(row["zoning_precheck_evidence_ids"]).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `set(row["zoning_precheck_context_evidence_ids"]).issubset` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["zoning_precheck_requires_formal_review"].eq(True).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["zoning_precheck_requires_formal_review"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["non_zoning_planning_features_interpreted"].eq(False).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["non_zoning_planning_features_interpreted"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["review_scope"].eq(REVIEW_SCOPE).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `result.parcels["review_scope"].eq` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_validated_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `expected_links.add((route["route_id"], evidence_id, role, direction))`<br>`reverse_links.setdefault(evidence_id, []).append((route_id, role))`<br>`reverse_links.setdefault(evidence_id, [])`<br>`context_ids.add(evidence_id)`<br>`decision_ids.add(evidence_id)` |
| Direct parameter mutation | None directly present. |

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
    if _canonical_value(
        _frame_payload(result.parcels, original_columns)
    ) != _canonical_value(_frame_payload(original_parcels, original_columns)):
        raise BessZoningPrecheckError(
            "Parcel count, IDs, order, index, geometry, CRS, or prior fields changed"
        )
    statuses = set(result.chapter_policy["zoning_precheck_status"].tolist())
    parcel_statuses = set(result.parcels["zoning_precheck_status"].tolist())
    confidences = set(result.chapter_policy["zoning_precheck_confidence"].tolist())
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
    if (
        len(actual_links) != len(result.evidence_route_links)
        or actual_links != expected_links
    ):
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
            raise BessZoningPrecheckError(
                "Evidence reverse route roles are inconsistent"
            )
        if bool(row["decision_linked"]) != bool(links):
            raise BessZoningPrecheckError(
                "Evidence reverse decision link is inconsistent"
            )
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
                raise BessZoningPrecheckError(
                    "Decision evidence output is inconsistent"
                )
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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_bess_zoning_precheck`

**Purpose:** Rebuild and validate the precheck from every factual and policy input.

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `structure_config` | positional-or-keyword | `PlanningRegulationStructureConfig \| str \| Path` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `zoning_intersections` | positional-or-keyword | `pd.DataFrame` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig \| str \| Path` | `required` |
| `result` | positional-or-keyword | `BessZoningPrecheckResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `re-raise`.
  - `BessZoningPrecheckError(<br>            f"Factual regulation structure validation failed: {error}"<br>        )`.
  - `BessZoningPrecheckError(<br>            f"Factual GPU zoning validation failed: {error}"<br>        )`.
  - `BessZoningPrecheckError(<br>            "BESS zoning precheck validation failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    validate_bess_zoning_precheck,
)`
- direct call: `tests.integration.test_gpu_planning_end_to_end::_validate` via `validate_bess_zoning_precheck`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_validate` via `validate_bess_zoning_precheck`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
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
)`
- direct call: `tests.unit.test_interpret_bess_zoning::_validate` via `validate_bess_zoning_precheck`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_validate` via `validate_bess_zoning_precheck`
- direct call: `tests.unit.test_interpret_bess_zoning::test_source_complete_validator_rejects_later_duplicate_chapter` via `validate_bess_zoning_precheck`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_complete_validator_rejects_later_duplicate_chapter` via `validate_bess_zoning_precheck`
- direct call: `tests.unit.test_interpret_bess_zoning::test_policy_change_after_result_creation_is_rejected` via `validate_bess_zoning_precheck`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_policy_change_after_result_creation_is_rejected` via `validate_bess_zoning_precheck`
- direct call: `tests.unit.test_interpret_bess_zoning::test_evidence_change_after_result_creation_is_rejected` via `validate_bess_zoning_precheck`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_change_after_result_creation_is_rejected` via `validate_bess_zoning_precheck`
- direct call: `tests.unit.test_interpret_bess_zoning::test_zoning_relation_and_zone_mapping_changes_are_rejected` via `validate_bess_zoning_precheck`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_zoning_relation_and_zone_mapping_changes_are_rejected` via `validate_bess_zoning_precheck`
- direct call: `tests.unit.test_interpret_bess_zoning::test_factual_zone_mapping_counts_are_recomputed` via `validate_bess_zoning_precheck`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_factual_zone_mapping_counts_are_recomputed` via `validate_bess_zoning_precheck`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_normalized_planning_zoning_inputs` | `landscout.stages.enrich_planning_zoning.validate_normalized_planning_zoning_inputs` |
| `_resolved_policy` | `landscout.stages.interpret_bess_zoning._resolved_policy` |
| `_build_result` | `landscout.stages.interpret_bess_zoning._build_result` |
| `_compare_results` | `landscout.stages.interpret_bess_zoning._compare_results` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `interpret_bess_zoning`

**Purpose:** Build a conservative written-zoning precheck without rejecting parcels.

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

- Exact decorators: none.
- Declared return annotation: `BessZoningPrecheckResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `index` | positional-or-keyword | `PlanningRegulationIndex` | `required` |
| `structure` | positional-or-keyword | `PlanningRegulationStructureResult` | `required` |
| `structure_config` | positional-or-keyword | `PlanningRegulationStructureConfig \| str \| Path` | `required` |
| `zones` | positional-or-keyword | `pd.DataFrame` | `required` |
| `zoning_intersections` | positional-or-keyword | `pd.DataFrame` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `policy` | positional-or-keyword | `BessZoningPolicyConfig \| str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `re-raise`.
  - `BessZoningPrecheckError(<br>            f"Factual regulation structure validation failed: {error}"<br>        )`.
  - `BessZoningPrecheckError(<br>            f"Factual GPU zoning validation failed: {error}"<br>        )`.
  - `BessZoningPrecheckError(<br>            "BESS zoning precheck could not be built safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    validate_bess_zoning_precheck,
)`
- direct call: `tests.integration.test_gpu_planning_end_to_end::_interpret` via `interpret_bess_zoning`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_interpret` via `interpret_bess_zoning`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
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
)`
- direct call: `tests.unit.test_interpret_bess_zoning::valid_result` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::valid_result` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_source_lock_mismatch_is_rejected` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_lock_mismatch_is_rejected` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_missing_and_extra_chapter_are_rejected` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_missing_and_extra_chapter_are_rejected` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_source_rule_identity_and_containment_are_strict` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_rule_identity_and_containment_are_strict` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_absent_excerpt_and_section_page_mismatch_are_rejected` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_absent_excerpt_and_section_page_mismatch_are_rejected` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_one_evidence_may_link_to_multiple_compatible_routes` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_one_evidence_may_link_to_multiple_compatible_routes` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_incomplete_review_persists_exact_missing_required_sections` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_incomplete_review_persists_exact_missing_required_sections` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_unknown_is_accepted_when_evidence_is_insufficient` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unknown_is_accepted_when_evidence_is_insufficient` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_reviewed_sections_cover_required_articles` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_reviewed_sections_cover_required_articles` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_evidence_must_be_inside_reviewed_sections` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_must_be_inside_reviewed_sections` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_review_cannot_claim_another_chapter_section` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_review_cannot_claim_another_chapter_section` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_general_section_review_is_explicit_and_valid` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_general_section_review_is_explicit_and_valid` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_same_general_occurrence_may_be_scoped_to_different_chapters` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_same_general_occurrence_may_be_scoped_to_different_chapters` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_wrong_occurrence_identity_is_rejected` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_wrong_occurrence_identity_is_rejected` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_unmapped_dominant_zone_is_rejected` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unmapped_dominant_zone_is_rejected` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_context_evidence_is_separate_from_decision_outputs` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_context_evidence_is_separate_from_decision_outputs` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_inputs_are_not_mutated` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_inputs_are_not_mutated` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_structure_config_and_hierarchy_changes_are_rejected` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_structure_config_and_hierarchy_changes_are_rejected` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_public_source_complete_validator_is_invoked` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_public_source_complete_validator_is_invoked` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_one_precheck_build_performs_one_zoning_source_complete_validation` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_invalid_physical_zoning_fails_before_policy_interpretation` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_invalid_physical_zoning_fails_before_policy_interpretation` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_relation_area_denominators_are_required` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_relation_area_denominators_are_required` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_relation_percentages_must_match_denominators` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_relation_percentages_must_match_denominators` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_factual_zone_mapping_counts_are_recomputed` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_factual_zone_mapping_counts_are_recomputed` via `interpret_bess_zoning`
- direct call: `tests.unit.test_interpret_bess_zoning::test_relation_identity_change_is_rejected` via `interpret_bess_zoning`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_relation_identity_change_is_rejected` via `interpret_bess_zoning`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `validate_normalized_planning_zoning_inputs` | `landscout.stages.enrich_planning_zoning.validate_normalized_planning_zoning_inputs` |
| `_resolved_policy` | `landscout.stages.interpret_bess_zoning._resolved_policy` |
| `_build_result` | `landscout.stages.interpret_bess_zoning._build_result` |
| `_compare_results` | `landscout.stages.interpret_bess_zoning._compare_results` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |

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

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `POLICY_SCHEMA_VERSION`, `RESULT_HASH_SCHEMA_VERSION`, `_RESOLVED_MAPPING_STATUSES`, `CHAPTER_POLICY_COLUMNS`, `EVIDENCE_CATALOG_COLUMNS`, `_EVIDENCE_OCCURRENCE_COLUMNS`, `ROUTE_ASSESSMENT_COLUMNS`, `EVIDENCE_ROUTE_LINK_COLUMNS`, `SOURCE_ZONE_POLICY_COLUMNS`, `PARCEL_ZONE_POLICY_COLUMNS`, `PARCEL_PRECHECK_COLUMNS`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `BessZoningPolicyConfig` | `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig` |
| `BessZoningPrecheckError` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError` |
| `BessZoningPrecheckResult` | `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult` |
| `interpret_bess_zoning` | `landscout.stages.interpret_bess_zoning.interpret_bess_zoning` |
| `load_bess_zoning_policy_config` | `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config` |
| `validate_bess_zoning_precheck` | `landscout.stages.interpret_bess_zoning.validate_bess_zoning_precheck` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Apply a source-locked, evidence-backed BESS zoning precheck policy."""

from __future__ import annotations

import json
import math
import re
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from numbers import Integral, Real
from pathlib import Path
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, model_validator
from pyproj import CRS
from shapely import to_wkb  # type: ignore[import-untyped]
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]

from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml
from landscout.sources.gpu_fr import GpuPlanningDocument
from landscout.stages.enrich_planning_zoning import (
    PlanningZoningError,
    validate_normalized_planning_zoning_inputs,
)
from landscout.stages.index_planning_regulation import (
    PlanningRegulationIndex,
    validate_planning_regulation_index,
)
from landscout.stages.planning_overlay import technical_overlay_tolerance
from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    validate_planning_regulation_structure_with_fragments,
)

__all__ = [
    "BessZoningPolicyConfig",
    "BessZoningPrecheckError",
    "BessZoningPrecheckResult",
    "interpret_bess_zoning",
    "load_bess_zoning_policy_config",
    "validate_bess_zoning_precheck",
]

POLICY_SCHEMA_VERSION = 5
RESULT_HASH_SCHEMA_VERSION = 5
PLANNING_PRECHECK_SCOPE = "WRITTEN_ZONING_REGULATION_ONLY"
REVIEW_SCOPE = "CONFIGURED_USE_CONTROL_ARTICLES_ONLY"

ChapterStatus = Literal[
    "POTENTIALLY_COMPATIBLE",
    "CONDITIONAL_REVIEW",
    "LIKELY_DIFFICULT",
    "UNKNOWN",
]
Confidence = Literal["HIGH", "MEDIUM", "LOW"]
ReviewCompleteness = Literal[
    "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES", "INCOMPLETE"
]
RouteKind = Literal[
    "DIRECT_ROUTE",
    "CONDITIONAL_ROUTE",
    "RESTRICTION_EXCEPTION_ROUTE",
    "DIFFICULTY_ONLY",
]
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
EvidenceDirection = Literal[
    "SUPPORTS_POTENTIAL_COMPATIBILITY",
    "SUPPORTS_DIFFICULTY",
    "CONDITION",
    "CONTEXT_ONLY",
]

_CHAPTER_STATUSES = frozenset(
    {"POTENTIALLY_COMPATIBLE", "CONDITIONAL_REVIEW", "LIKELY_DIFFICULT", "UNKNOWN"}
)
_PARCEL_STATUSES = _CHAPTER_STATUSES | {"MIXED_REVIEW_REQUIRED"}
_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
_RESOLVED_MAPPING_STATUSES = frozenset({"EXACT", "CONFIG_ALIAS"})

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
_EVIDENCE_OCCURRENCE_COLUMNS = (
    "resolved_zone_chapter_label",
    "section_id",
    "page_number",
    "section_page_fragment_sha256",
    "excerpt_start",
    "excerpt_end",
)
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


class BessZoningPrecheckError(ValueError):
    """Raised when the preliminary zoning interpretation cannot be proven."""


class _StrictConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class PolicySourceLock(_StrictConfigModel):
    document_id: StrictStr = Field(min_length=1)
    archive_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    structure_result_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    structure_profile: StrictStr = Field(min_length=1)


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
        if (
            sha256(self.exact_raw_excerpt.encode("utf-8")).hexdigest()
            != self.excerpt_sha256
        ):
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
            normalized = [
                _config_string(value, f"{role} evidence ID") for value in values
            ]
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
            raise ValueError(
                f"unsupported BESS zoning policy schema: {self.schema_version}"
            )
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
                if (
                    prior_rule_id is not None
                    and prior_rule_id != evidence.source_rule_id
                ):
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
                    raise ValueError(
                        "CONTEXT_ONLY evidence must not be linked to a route"
                    )
                if evidence.evidence_direction != "CONTEXT_ONLY" and not is_linked:
                    raise ValueError(
                        "decision evidence must be linked to at least one route"
                    )
        return self


@dataclass(frozen=True)
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


def _config_string(value: str, label: str) -> str:
    if not value or value != value.strip():
        raise ValueError(f"{label} must be a non-empty exact string")
    return value


def load_bess_zoning_policy_config(path: str | Path) -> BessZoningPolicyConfig:
    """Load a strict policy while rejecting duplicate YAML keys."""

    try:
        payload = loads_strict_yaml(Path(path).read_bytes())
        if not isinstance(payload, Mapping):
            raise BessZoningPrecheckError("BESS zoning policy must be a mapping")
        return BessZoningPolicyConfig.model_validate(payload)
    except BessZoningPrecheckError:
        raise
    except StrictYamlError as error:
        raise BessZoningPrecheckError(str(error)) from error
    except Exception as error:
        raise BessZoningPrecheckError("BESS zoning policy is invalid") from error


def _strict_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise BessZoningPrecheckError(f"{label} must be a non-empty exact string")
    return value


def _strict_nonnegative_integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise BessZoningPrecheckError(f"{label} must be an integer")
    result = int(value)
    if result < 0:
        raise BessZoningPrecheckError(f"{label} must be non-negative")
    return result


def _strict_positive_integer(value: object, label: str) -> int:
    result = _strict_nonnegative_integer(value, label)
    if result < 1:
        raise BessZoningPrecheckError(f"{label} must be positive")
    return result


def _validated_sha256(value: object, label: str) -> str:
    checksum = _strict_string(value, label)
    if re.fullmatch(r"[0-9a-f]{64}", checksum) is None:
        raise BessZoningPrecheckError(
            f"{label} must be exactly 64 lowercase hexadecimal characters"
        )
    return checksum


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
        raise BessZoningPrecheckError(
            "Canonical integrity serialization failed"
        ) from error
    return sha256(serialized).hexdigest()


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
        raise BessZoningPrecheckError(
            "DataFrame integrity serialization failed"
        ) from error


def _frame_sha256(domain: str, frame: pd.DataFrame, columns: Sequence[str]) -> str:
    return _canonical_sha256({"domain": domain, **_frame_payload(frame, columns)})


def _policy_sha256(config: BessZoningPolicyConfig) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.bess_zoning.policy_config",
            "config": config.model_dump(mode="json"),
        }
    )


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


def _exact_id_series(series: pd.Series, label: str, *, unique: bool) -> tuple[str, ...]:
    values: list[str] = []
    for value in series.tolist():
        values.append(_strict_string(value, label))
    if unique and len(set(values)) != len(values):
        raise BessZoningPrecheckError(f"{label} values must be unique")
    return tuple(values)


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
        raise BessZoningPrecheckError(
            f"Zoning relations are missing columns: {missing}"
        )
    result = relations.copy(deep=True)
    if result.duplicated(["parcel_id", "planning_zone_id"]).any():
        raise BessZoningPrecheckError("Parcel/zone relations must be unique")
    parcel_ids = set(_exact_id_series(parcels["parcel_id"], "parcel ID", unique=True))
    if not set(
        _exact_id_series(result["parcel_id"], "relation parcel ID", unique=False)
    ).issubset(parcel_ids):
        raise BessZoningPrecheckError("Zoning relation references an unknown parcel")
    zone_records = zones.set_index("planning_zone_id")[
        ["source_zone_id", "zone_label_raw", "source_layer"]
    ].to_dict("index")
    for row in result.to_dict("records"):
        planning_id = _strict_string(
            row["planning_zone_id"], "relation planning zone ID"
        )
        source_id = _strict_string(row["source_zone_id"], "relation source zone ID")
        label = _strict_string(row["zone_label_raw"], "relation raw zone label")
        expected_zone = zone_records.get(planning_id)
        if expected_zone is None:
            raise BessZoningPrecheckError("Zoning relation references an unknown zone")
        if (
            source_id != expected_zone["source_zone_id"]
            or label != expected_zone["zone_label_raw"]
        ):
            raise BessZoningPrecheckError(
                "Zoning relation zone identity is inconsistent"
            )
        if row["source_layer"] != expected_zone["source_layer"]:
            raise BessZoningPrecheckError(
                "Zoning relation source layer is inconsistent"
            )
        relation_type = _strict_string(row["relation_type"], "zoning relation type")
        area = _strict_nonnegative_number(
            row["intersection_area_m2"], "intersection area"
        )
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
            reference_area = _strict_nonnegative_number(row[area_column], area_column)
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


def _zone_chapter_rows(
    structure: PlanningRegulationStructureResult,
) -> list[dict[str, object]]:
    rows = structure.sections.loc[
        structure.sections["section_type"].eq("ZONE_CHAPTER")
    ].to_dict("records")
    labels = [
        _strict_string(row["zone_chapter_label"], "zone chapter label") for row in rows
    ]
    section_ids = [
        _strict_string(row["section_id"], "zone chapter section ID") for row in rows
    ]
    if len(set(labels)) != len(labels):
        raise BessZoningPrecheckError("Regulation zone chapter labels must be unique")
    if len(set(section_ids)) != len(section_ids):
        raise BessZoningPrecheckError(
            "Regulation zone chapter section IDs must be unique"
        )
    return rows


def _required_section_ids_by_chapter(
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> dict[str, tuple[str, ...]]:
    chapter_ids = {
        row["zone_chapter_label"]: row["section_id"]
        for row in _zone_chapter_rows(structure)
    }
    result: dict[str, tuple[str, ...]] = {}
    section_rows = structure.sections.to_dict("records")
    for label, chapter_id in chapter_ids.items():
        required_ids: list[str] = []
        for article_number in policy.required_zone_article_numbers:
            matches = [
                row
                for row in section_rows
                if row["section_type"] == "ARTICLE"
                and row["parent_section_id"] == chapter_id
                and row["zone_chapter_label"] == label
                and row["article_number_raw"] == article_number
            ]
            if len(matches) != 1:
                raise BessZoningPrecheckError(
                    f"Chapter {label} must contain exactly one configured article "
                    f"{article_number!r}; found {len(matches)}"
                )
            required_ids.append(
                _strict_string(
                    matches[0]["section_id"],
                    f"required article {article_number} section ID",
                )
            )
        result[str(label)] = tuple(required_ids)
    return result


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
            if (
                fragment["section_page_fragment_sha256"]
                != evidence.section_page_fragment_sha256
            ):
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} fragment SHA256 differs"
                )
            if (
                evidence.excerpt_end > len(raw_fragment)
                or raw_fragment[evidence.excerpt_start : evidence.excerpt_end]
                != excerpt
            ):
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} offsets do not identify its exact excerpt"
                )
            if sha256(excerpt.encode("utf-8")).hexdigest() != evidence.excerpt_sha256:
                raise BessZoningPrecheckError(
                    f"Evidence {evidence.evidence_id} excerpt SHA256 differs"
                )
            rule = evidence.source_rule_excerpt
            if (
                evidence.source_rule_end > len(raw_fragment)
                or raw_fragment[evidence.source_rule_start : evidence.source_rule_end]
                != rule
            ):
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
        raise BessZoningPrecheckError(
            "Factual zone mapping is incomplete or has extras"
        )
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
            raise BessZoningPrecheckError(
                "Zone mapping chapter identity is inconsistent"
            )
    return mapping


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


def _route_status(route_kind: RouteKind) -> ChapterStatus:
    statuses: dict[RouteKind, ChapterStatus] = {
        "DIRECT_ROUTE": "POTENTIALLY_COMPATIBLE",
        "CONDITIONAL_ROUTE": "CONDITIONAL_REVIEW",
        "RESTRICTION_EXCEPTION_ROUTE": "CONDITIONAL_REVIEW",
        "DIFFICULTY_ONLY": "LIKELY_DIFFICULT",
    }
    return statuses[route_kind]


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
                "resolved_zone_chapter_label": source["resolved_zone_chapter_label"],
                "mapping_status": source["mapping_status"],
                "matched_section_id": source["matched_section_id"],
                "source_layer": layers_by_label[source["source_zone_label_raw"]],
                "zoning_precheck_status": chapter["zoning_precheck_status"],
                "zoning_precheck_confidence": chapter["zoning_precheck_confidence"],
                "evidence_ids": tuple(chapter["evidence_ids"]),
                "decision_evidence_ids": tuple(chapter["decision_evidence_ids"]),
                "context_evidence_ids": tuple(chapter["context_evidence_ids"]),
                **lineage,
            }
        )
    return pd.DataFrame(rows, columns=SOURCE_ZONE_POLICY_COLUMNS)


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
                "resolved_zone_chapter_label": item["resolved_zone_chapter_label"],
                "intersection_area_m2": float(source["intersection_area_m2"]),
                "parcel_share_pct": float(source["parcel_share_pct"]),
                "zoning_precheck_status": item["zoning_precheck_status"],
                "zoning_precheck_confidence": item["zoning_precheck_confidence"],
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


def _is_null(value: object) -> bool:
    if value is None or value is pd.NA:
        return True
    try:
        null = pd.isna(value)
    except (TypeError, ValueError):
        return False
    return isinstance(null, (bool, np.bool_)) and bool(null)


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
    summary: dict[str, list[object]] = {
        column: [] for column in PARCEL_PRECHECK_COLUMNS
    }
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
                statuses[0] if len(distinct_statuses) == 1 else "MIXED_REVIEW_REQUIRED"
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
        summary["non_dominant_different_status_count"].append(non_dominant_different)
        summary["touch_only_zone_count"].append(int(touch_counts.get(parcel_id, 0)))
        summary["zoning_precheck_evidence_ids"].append(evidence_ids)
        summary["zoning_precheck_context_evidence_ids"].append(context_evidence_ids)
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


def _complete_result_sha256(result: BessZoningPrecheckResult) -> str:
    return _canonical_sha256(
        {
            "domain": "landscout.bess_zoning.precheck_result",
            **_result_component_metadata(result),
            "evidence_catalog_content_sha256": (result.evidence_catalog_content_sha256),
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
    route_assessments = _build_route_assessments(index, structure, policy, policy_hash)
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
    chapter_policy = _build_chapter_policy(index, structure, policy, policy_hash)
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


def _compare_frames(
    actual: pd.DataFrame,
    expected: pd.DataFrame,
    columns: Sequence[str],
    label: str,
) -> None:
    if tuple(actual.columns) != tuple(expected.columns) or tuple(
        actual.columns
    ) != tuple(columns):
        raise BessZoningPrecheckError(f"{label} schema differs from rebuilt result")
    if _canonical_value(_frame_payload(actual, columns)) != _canonical_value(
        _frame_payload(expected, columns)
    ):
        raise BessZoningPrecheckError(f"{label} differs from rebuilt source evidence")


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
    if _canonical_value(
        _frame_payload(result.parcels, original_columns)
    ) != _canonical_value(_frame_payload(original_parcels, original_columns)):
        raise BessZoningPrecheckError(
            "Parcel count, IDs, order, index, geometry, CRS, or prior fields changed"
        )
    statuses = set(result.chapter_policy["zoning_precheck_status"].tolist())
    parcel_statuses = set(result.parcels["zoning_precheck_status"].tolist())
    confidences = set(result.chapter_policy["zoning_precheck_confidence"].tolist())
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
    if (
        len(actual_links) != len(result.evidence_route_links)
        or actual_links != expected_links
    ):
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
            raise BessZoningPrecheckError(
                "Evidence reverse route roles are inconsistent"
            )
        if bool(row["decision_linked"]) != bool(links):
            raise BessZoningPrecheckError(
                "Evidence reverse decision link is inconsistent"
            )
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
                raise BessZoningPrecheckError(
                    "Decision evidence output is inconsistent"
                )
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
