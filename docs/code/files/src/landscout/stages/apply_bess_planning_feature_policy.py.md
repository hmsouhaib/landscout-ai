# `src/landscout/stages/apply_bess_planning_feature_policy.py`

## File identity

- Repository path: `src/landscout/stages/apply_bess_planning_feature_policy.py`
- File type: Python source
- Layer: processing/policy stage
- Domain: planning
- Responsibility: Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.
- Source SHA256: `35c40953ec24f8ce27c8de89f3f2ff8538b48c9e594407e7ce2a877f0375b174`

## 1. Purpose

Applies exact coded-result and policy-result evidence to planning feature catalogs and relations.

## 2. Position in LandScout architecture

This file belongs to the **processing/policy stage** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import math`
- `import re`
- `from dataclasses import dataclass, replace`
- `from datetime import date, datetime`
- `from hashlib import sha256`
- `from io import BytesIO`
- `from numbers import Integral, Real`
- `from pathlib import Path`
- `from typing import Literal`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `from pydantic import (
    BaseModel,
    ConfigDict,
    StrictBool,
    StrictInt,
    StrictStr,
    model_validator,
)`
- `from pyproj import CRS`
- `from shapely import get_coordinate_dimension, to_wkb`
- `from shapely.geometry.base import BaseGeometry`

### Internal LandScout imports

- `from landscout.common.artifact_paths import validate_portable_parquet_filename`
- `from landscout.common.bess_application_contract import (
    APPLICATION_SCOPE,
    FLAG_COLUMNS,
    POLICY_COLUMNS,
    POLICY_SCOPE,
    STRING_POLICY_COLUMNS,
    ApplicationStatus,
    validate_bess_application_feature_catalogs,
    validate_bess_application_relation_frame,
)`
- `from landscout.common.frame_integrity import deterministic_frame_schema_signature`
- `from landscout.common.planning_overlay import technical_overlay_tolerance`
- `from landscout.sources.gpu_fr import GpuPlanningDocument`
- `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result_envelope,
)`

## 4. Contract taxonomy

### A. Python constants

#### `RESULT_HASH_SCHEMA_VERSION`

```python
RESULT_HASH_SCHEMA_VERSION = 2
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_build_result` (value argument/reference), `src/landscout/stages/apply_bess_planning_feature_policy.py::_build_result` (value argument/reference), `src/landscout/stages/bess_planning_feature_policy.py::_build_result` (value argument/reference), `src/landscout/stages/interpret_bess_zoning.py::_build_result` (value argument/reference), `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` (value argument/reference).

#### `ARTIFACT_MANIFEST_SCHEMA_VERSION`

```python
ARTIFACT_MANIFEST_SCHEMA_VERSION = 2
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing.

#### `ARTIFACT_KIND`

```python
ARTIFACT_KIND = "BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `ARTIFACT_ROLES`

```python
ARTIFACT_ROLES: tuple[ArtifactRole, ...] = (
    "SURFACE_FEATURES",
    "LINE_FEATURES",
    "POINT_FEATURES",
    "RELATIONS",
)
```

Closed vocabulary, ordering, or accepted-domain constant. Its member strings are values, not DataFrame columns unless separately listed in a schema.

#### `RELATION_FEATURE_AGREEMENT_COLUMNS`

```python
RELATION_FEATURE_AGREEMENT_COLUMNS = (
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
    "official_code_status",
    "official_code_label",
    "official_legal_reference",
    "official_regulation_reference",
    "official_code_source_url",
    "official_code_profile",
    "official_code_profile_sha256",
)
```

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section.

#### `SHA_PATTERN`

```python
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly.

#### `CODE_PATTERN`

```python
CODE_PATTERN = re.compile(r"[0-9]{2}")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly.

#### `RESULT_FRAME_FIELDS`

```python
RESULT_FRAME_FIELDS = (
    "surface_features",
    "line_features",
    "point_features",
    "relations",
)
```

Module-level technical/source/policy constant consumed by the exact references below.

#### `RESULT_SCALAR_FIELDS`

```python
RESULT_SCALAR_FIELDS = tuple(
    field
    for field in BessPlanningFeatureApplicationResult.__dataclass_fields__
    if field not in RESULT_FRAME_FIELDS
)
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` (property/attribute access).


### B. Type aliases and closed domains

#### `ArtifactRole`

```python
ArtifactRole = Literal[
    "SURFACE_FEATURES",
    "LINE_FEATURES",
    "POINT_FEATURES",
    "RELATIONS",
]
```

Closed Literal value domain shown exactly above; members are values, not frame columns. It is consumed by annotations or Pydantic validation in this module.


### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
```python
__all__ = [
    "BessPlanningFeatureApplicationArtifactManifest",
    "BessPlanningFeatureApplicationError",
    "BessPlanningFeatureApplicationResult",
    "apply_bess_planning_feature_policy",
    "load_bess_planning_feature_application_artifacts",
    "validate_bess_planning_feature_application_result",
    "validate_bess_planning_feature_application_result_envelope",
]
```


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `BessPlanningFeatureApplicationError`

**Purpose:** Raised when exact feature-policy propagation cannot be proven.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_canonical_value` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_application_geometry` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_canonical_json_sha256` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_policy_lookup` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_feature_catalog` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_feature_rows_by_id` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_relations` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_relation_rows` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_coded_policy_compatibility` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_source_locks` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_policy_source` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::apply_bess_planning_feature_policy` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_compare_frame` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_unique_json_object` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_read_verified_artifact` via `BessPlanningFeatureApplicationError`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `BessPlanningFeatureApplicationError`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_m_and_zm_application_geometries_are_rejected` via `pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_inconsistent_official_status_and_policy_match_is_rejected` via `pytest.raises(BessPlanningFeatureApplicationError, match='policy|official')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature` via `pytest.raises(BessPlanningFeatureApplicationError, match='relation|feature')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_relation_feature_id_is_rejected` via `pytest.raises(BessPlanningFeatureApplicationError, match='feature ID')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `pytest.raises(BessPlanningFeatureApplicationError, match='rebuilt|feature')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `pytest.raises(BessPlanningFeatureApplicationError, match='relation|rebuilt')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally` via `pytest.raises(BessPlanningFeatureApplicationError, match='duplicate|unique')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_feature_id_is_exact_and_portable` via `pytest.raises(BessPlanningFeatureApplicationError, match='feature|identity')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact` via `pytest.raises(BessPlanningFeatureApplicationError, match='parcel|identity')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally` via `pytest.raises(BessPlanningFeatureApplicationError, match='relation type')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_invalid_policy_domains_fail_local_validation` via `pytest.raises(BessPlanningFeatureApplicationError, match=message)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_literal_null_replacements_are_rejected` via `pytest.raises(BessPlanningFeatureApplicationError, match='literal|missing')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_policy_suffix_dtype_is_rejected` via `pytest.raises(BessPlanningFeatureApplicationError, match='dtype|schema')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `pytest.raises(BessPlanningFeatureApplicationError, match='official|status')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_any_true_row_boundary_flag_is_rejected` via `pytest.raises(BessPlanningFeatureApplicationError, match='flag|false')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `pytest.raises(BessPlanningFeatureApplicationError, match='hash|SHA|sha256|invalid')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `pytest.raises(BessPlanningFeatureApplicationError, match='source lock')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading` via `pytest.raises(BessPlanningFeatureApplicationError, match='duplicate|unique')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `pytest.raises(BessPlanningFeatureApplicationError, match='priority|mapping')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `pytest.raises(BessPlanningFeatureApplicationError, match='surface|metric|type')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `pytest.raises(BessPlanningFeatureApplicationError, match='surface|geometry')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic` via `pytest.raises(BessPlanningFeatureApplicationError, match='geometry')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry` via `pytest.raises(BessPlanningFeatureApplicationError, match='metric|geometry|count')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `pytest.raises(BessPlanningFeatureApplicationError, match='identity|layer|kind')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `pytest.raises(BessPlanningFeatureApplicationError, match='EPSG:2154|CRS')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `pytest.raises(BessPlanningFeatureApplicationError, match='identity|unique')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally` via `pytest.raises(BessPlanningFeatureApplicationError, match='feature|identity|GPU')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping` via `pytest.raises(BessPlanningFeatureApplicationError, match='priority|mapping')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly` via `pytest.raises(BessPlanningFeatureApplicationError, match='policy.*schema')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly` via `pytest.raises(BessPlanningFeatureApplicationError, match='CNIG|cnig.*schema')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `pytest.raises(BessPlanningFeatureApplicationError, match='duplicate|unique')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_z_geoparquet_artifact_is_rejected` via `pytest.raises(BessPlanningFeatureApplicationError, match='2D|dimension')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_dtype_artifact_is_rejected` via `pytest.raises(BessPlanningFeatureApplicationError, match='dtype|schema')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_manifest_rejects_invalid_contract` via `pytest.raises(BessPlanningFeatureApplicationError, match=message)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_manifest_rejects_duplicate_json_key` via `pytest.raises(BessPlanningFeatureApplicationError, match='Duplicate JSON')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_physical_replacement_before_loading_is_rejected` via `pytest.raises(BessPlanningFeatureApplicationError, match='size|SHA|hash')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `pytest.raises(BessPlanningFeatureApplicationError, match='document|lineage')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `pytest.raises(BessPlanningFeatureApplicationError, match='lineage|document')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_referenced_row_lineage_cannot_bypass_envelope` via `pytest.raises(BessPlanningFeatureApplicationError, match='lineage|document')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_resolved_official_row_requires_label_and_envelope_profile` via `pytest.raises(BessPlanningFeatureApplicationError, match='official|profile|label')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_official_row_rejects_invented_label_or_url` via `pytest.raises(BessPlanningFeatureApplicationError, match='official|null')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_feature_prefix_has_exact_canonical_schema` via `pytest.raises(BessPlanningFeatureApplicationError, match='schema|dtype|index')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_prefix_has_exact_canonical_schema` via `pytest.raises(BessPlanningFeatureApplicationError, match='schema|dtype')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `pytest.raises(BessPlanningFeatureApplicationError, match='schema|dtype')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `pytest.raises(BessPlanningFeatureApplicationError)`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams` via `pytest.raises(BessPlanningFeatureApplicationError, match='hash|invalid')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `pytest.raises(BessPlanningFeatureApplicationError, match='upstream|rebuilt')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `pytest.raises(BessPlanningFeatureApplicationError, match='upstream')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `pytest.raises(BessPlanningFeatureApplicationError, match='upstream')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `pytest.raises(BessPlanningFeatureApplicationError, match='upstream')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `pytest.raises(BessPlanningFeatureApplicationError, match='upstream')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `pytest.raises(BessPlanningFeatureApplicationError, match='Policy|policy|CNIG|pair|source|schema|official|reference')`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `pytest.raises(BessPlanningFeatureApplicationError, match='dictionary|policy|table|pair|empty|record|entry')`.
- import/re-export: `tests/unit/test_apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)`.

**Exact class source**

```python
class BessPlanningFeatureApplicationError(ValueError):
    """Raised when exact feature-policy propagation cannot be proven."""
```

### `_StrictModel`

**Purpose:** Validates the planning contract carried by its explicit validators and inherited fields.

**Kind:** Pydantic model.

**Inheritance:** `BaseModel`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `BessPlanningFeatureApplicationArtifactRecord`

**Purpose:** One physical output record within the application manifest.

**Kind:** Pydantic model.

**Inheritance:** `_StrictModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `artifact_role` | `artifact_role: ArtifactRole` | Closed role identifying how the source/result participates in the pipeline; it is not a suitability outcome. |
| `filename` | `filename: StrictStr` | Portable basename for the named physical file; it must agree with the owning path/manifest contract where validated. |
| `row_count` | `row_count: StrictInt` | Count/byte quantity with exact integer strictness and bounds enforced by the owning model/function. |
| `size_bytes` | `size_bytes: StrictInt` | Stores `BessPlanningFeatureApplicationArtifactRecord`'s `size bytes` value under exact annotation `StrictInt`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `sha256` | `sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `frame_schema_signature` | `frame_schema_signature: dict[StrictStr, object]` | Structured `frame schema signature` collection owned by `BessPlanningFeatureApplicationArtifactRecord`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |
| `geospatial` | `geospatial: StrictBool` | Boolean `geospatial` flag on `BessPlanningFeatureApplicationArtifactRecord`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `crs` | `crs: dict[StrictStr, object] \| None` | Coordinate reference system identity; exact accepted/storage/calculation behavior is enforced by the owning CRS validator. |

**Validators (exact source)**

`_validate_record`:

```python
def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be a non-negative integer")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be a positive integer")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geospatial = self.artifact_role != "RELATIONS"
        if self.geospatial is not expected_geospatial:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = self.frame_schema_signature.get("crs")
        signature_geometry = self.frame_schema_signature.get("geometry_column")
        if expected_geospatial:
            if self.crs is None or signature_crs != self.crs:
                raise ValueError("geospatial artifact CRS is missing or inconsistent")
            if not isinstance(signature_geometry, str) or not signature_geometry:
                raise ValueError("geospatial artifact geometry column is missing")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("non-geospatial artifact must not declare a CRS")
        return self
```

**Interface consumers**

- Pydantic constructs this model during direct/model_validate or nested-model validation; its exact validators and the module's loader/build functions below define the active framework entry points.

**Exact class source**

```python
class BessPlanningFeatureApplicationArtifactRecord(_StrictModel):
    """One physical output record within the application manifest."""

    artifact_role: ArtifactRole
    filename: StrictStr
    row_count: StrictInt
    size_bytes: StrictInt
    sha256: StrictStr
    frame_schema_signature: dict[StrictStr, object]
    geospatial: StrictBool
    crs: dict[StrictStr, object] | None

    @model_validator(mode="after")
    def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be a non-negative integer")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be a positive integer")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geospatial = self.artifact_role != "RELATIONS"
        if self.geospatial is not expected_geospatial:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = self.frame_schema_signature.get("crs")
        signature_geometry = self.frame_schema_signature.get("geometry_column")
        if expected_geospatial:
            if self.crs is None or signature_crs != self.crs:
                raise ValueError("geospatial artifact CRS is missing or inconsistent")
            if not isinstance(signature_geometry, str) or not signature_geometry:
                raise ValueError("geospatial artifact geometry column is missing")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("non-geospatial artifact must not declare a CRS")
        return self
```

### `BessPlanningFeatureApplicationResult`

**Purpose:** Immutable exact policy propagation over coded features and relations.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `result_hash_schema_version` | `result_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `application_scope` | `application_scope: str` | Closed or validated `application scope` classification on `BessPlanningFeatureApplicationResult`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `policy_scope` | `policy_scope: str` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `local_feature_text_interpreted` | `local_feature_text_interpreted: bool` | Boolean `local feature text interpreted` flag on `BessPlanningFeatureApplicationResult`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `local_regulation_content_interpreted` | `local_regulation_content_interpreted: bool` | Boolean `local regulation content interpreted` flag on `BessPlanningFeatureApplicationResult`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `legal_conclusion_produced` | `legal_conclusion_produced: bool` | Boolean `legal conclusion produced` flag on `BessPlanningFeatureApplicationResult`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `parcel_status_aggregated` | `parcel_status_aggregated: bool` | Boolean `parcel status aggregated` flag on `BessPlanningFeatureApplicationResult`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `parcel_rejection_performed` | `parcel_rejection_performed: bool` | Boolean `parcel rejection performed` flag on `BessPlanningFeatureApplicationResult`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `score_calculated` | `score_calculated: bool` | Boolean `score calculated` flag on `BessPlanningFeatureApplicationResult`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `policy_profile` | `policy_profile: str` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `policy_sha256` | `policy_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `policy_result_hash_schema_version` | `policy_result_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `policy_complete_result_content_sha256` | `policy_complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_profile` | `cnig_profile: str` | Stores `BessPlanningFeatureApplicationResult`'s `cnig profile` value under exact annotation `str`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `cnig_profile_sha256` | `cnig_profile_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_result_hash_schema_version` | `cnig_result_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `cnig_complete_result_content_sha256` | `cnig_complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_document_id` | `source_document_id: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_archive_sha256` | `source_archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_surface_features_content_sha256` | `cnig_surface_features_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_line_features_content_sha256` | `cnig_line_features_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_point_features_content_sha256` | `cnig_point_features_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_relations_content_sha256` | `cnig_relations_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `surface_features_content_sha256` | `surface_features_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `line_features_content_sha256` | `line_features_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `point_features_content_sha256` | `point_features_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `relations_content_sha256` | `relations_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `complete_result_content_sha256` | `complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `surface_features` | `surface_features: gpd.GeoDataFrame` | Stores `BessPlanningFeatureApplicationResult`'s `surface features` value under exact annotation `gpd.GeoDataFrame`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `line_features` | `line_features: gpd.GeoDataFrame` | Stores `BessPlanningFeatureApplicationResult`'s `line features` value under exact annotation `gpd.GeoDataFrame`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `point_features` | `point_features: gpd.GeoDataFrame` | Stores `BessPlanningFeatureApplicationResult`'s `point features` value under exact annotation `gpd.GeoDataFrame`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `relations` | `relations: pd.DataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`.
- import/re-export: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationResult,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_build_result` via `BessPlanningFeatureApplicationResult`.
- callback/function object: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `isinstance(result, BessPlanningFeatureApplicationResult)`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `BessPlanningFeatureApplicationResult`.
- callback/function object: `tests/unit/test_apply_bess_planning_feature_policy.py::_write_application_artifacts` via `fields(BessPlanningFeatureApplicationResult)`.
- import/re-export: `tests/unit/test_apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)`.

**Exact class source**

```python
class BessPlanningFeatureApplicationResult:
    """Immutable exact policy propagation over coded features and relations."""

    result_hash_schema_version: int
    application_scope: str
    policy_scope: str
    local_feature_text_interpreted: bool
    local_regulation_content_interpreted: bool
    legal_conclusion_produced: bool
    parcel_status_aggregated: bool
    parcel_rejection_performed: bool
    score_calculated: bool
    policy_profile: str
    policy_sha256: str
    policy_result_hash_schema_version: int
    policy_complete_result_content_sha256: str
    cnig_profile: str
    cnig_profile_sha256: str
    cnig_result_hash_schema_version: int
    cnig_complete_result_content_sha256: str
    source_document_id: str
    source_archive_sha256: str
    cnig_surface_features_content_sha256: str
    cnig_line_features_content_sha256: str
    cnig_point_features_content_sha256: str
    cnig_relations_content_sha256: str
    surface_features_content_sha256: str
    line_features_content_sha256: str
    point_features_content_sha256: str
    relations_content_sha256: str
    complete_result_content_sha256: str
    surface_features: gpd.GeoDataFrame
    line_features: gpd.GeoDataFrame
    point_features: gpd.GeoDataFrame
    relations: pd.DataFrame
```

### `BessPlanningFeatureApplicationArtifactManifest`

**Purpose:** Strict four-file physical artifact envelope.

**Kind:** Pydantic model.

**Inheritance:** `_StrictModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `schema_version` | `schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `artifact_kind` | `artifact_kind: Literal["BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"]` | Closed or validated `artifact kind` classification on `BessPlanningFeatureApplicationArtifactManifest`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `result_hash_schema_version` | `result_hash_schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `application_scope` | `application_scope: Literal["FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"]` | Closed or validated `application scope` classification on `BessPlanningFeatureApplicationArtifactManifest`; accepted values and downstream branches are recoverable from the reproduced validators and consumers. |
| `policy_scope` | `policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `local_feature_text_interpreted` | `local_feature_text_interpreted: StrictBool` | Boolean `local feature text interpreted` flag on `BessPlanningFeatureApplicationArtifactManifest`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `local_regulation_content_interpreted` | `local_regulation_content_interpreted: StrictBool` | Boolean `local regulation content interpreted` flag on `BessPlanningFeatureApplicationArtifactManifest`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `legal_conclusion_produced` | `legal_conclusion_produced: StrictBool` | Boolean `legal conclusion produced` flag on `BessPlanningFeatureApplicationArtifactManifest`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `parcel_status_aggregated` | `parcel_status_aggregated: StrictBool` | Boolean `parcel status aggregated` flag on `BessPlanningFeatureApplicationArtifactManifest`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `parcel_rejection_performed` | `parcel_rejection_performed: StrictBool` | Boolean `parcel rejection performed` flag on `BessPlanningFeatureApplicationArtifactManifest`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `score_calculated` | `score_calculated: StrictBool` | Boolean `score calculated` flag on `BessPlanningFeatureApplicationArtifactManifest`; exact strictness and cross-field effects are defined by the reproduced declaration and validators. |
| `policy_profile` | `policy_profile: StrictStr` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `policy_sha256` | `policy_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `policy_result_hash_schema_version` | `policy_result_hash_schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `policy_complete_result_content_sha256` | `policy_complete_result_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_profile` | `cnig_profile: StrictStr` | Stores `BessPlanningFeatureApplicationArtifactManifest`'s `cnig profile` value under exact annotation `StrictStr`; its reproduced constructors, validators, and consumers establish the operational meaning without reclassifying it as a frame column. |
| `cnig_profile_sha256` | `cnig_profile_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_result_hash_schema_version` | `cnig_result_hash_schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `cnig_complete_result_content_sha256` | `cnig_complete_result_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_document_id` | `source_document_id: StrictStr` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_archive_sha256` | `source_archive_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_surface_features_content_sha256` | `cnig_surface_features_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_line_features_content_sha256` | `cnig_line_features_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_point_features_content_sha256` | `cnig_point_features_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `cnig_relations_content_sha256` | `cnig_relations_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `surface_features_content_sha256` | `surface_features_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `line_features_content_sha256` | `line_features_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `point_features_content_sha256` | `point_features_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `relations_content_sha256` | `relations_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `complete_result_content_sha256` | `complete_result_content_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `artifacts` | `artifacts: tuple[BessPlanningFeatureApplicationArtifactRecord, ...]` | Structured `artifacts` collection owned by `BessPlanningFeatureApplicationArtifactManifest`; the declaration fixes member shape and the reproduced validators/callers define ordering, uniqueness, and completeness. |

**Validators (exact source)**

`_validate_manifest`:

```python
def _validate_manifest(self) -> BessPlanningFeatureApplicationArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application artifact manifest schema")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application result hash schema")
        if any(
            value is not False
            for value in (
                self.local_feature_text_interpreted,
                self.local_regulation_content_interpreted,
                self.legal_conclusion_produced,
                self.parcel_status_aggregated,
                self.parcel_rejection_performed,
                self.score_calculated,
            )
        ):
            raise ValueError("application boundary flags must all be false")
        for exact_value, label in (
            (self.policy_profile, "policy_profile"),
            (self.cnig_profile, "cnig_profile"),
            (self.source_document_id, "source_document_id"),
        ):
            _exact_string(exact_value, label)
        if self.policy_result_hash_schema_version != 1:
            raise ValueError("policy result hash schema must be exactly 1")
        if self.cnig_result_hash_schema_version != 5:
            raise ValueError("CNIG result hash schema must be exactly 5")
        for field in RESULT_SCALAR_FIELDS:
            if field.endswith("sha256"):
                _sha256_string(getattr(self, field), field)
        roles = tuple(record.artifact_role for record in self.artifacts)
        if roles != ARTIFACT_ROLES:
            raise ValueError(
                "application artifact roles are missing, extra, or unordered"
            )
        filenames = tuple(record.filename.casefold() for record in self.artifacts)
        if len(filenames) != len(set(filenames)):
            raise ValueError("application artifact filenames contain a duplicate")
        return self
```

**Interface consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`.
- import/re-export: `tests/unit/test_apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)`.

**Exact class source**

```python
class BessPlanningFeatureApplicationArtifactManifest(_StrictModel):
    """Strict four-file physical artifact envelope."""

    schema_version: StrictInt
    artifact_kind: Literal["BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"]
    result_hash_schema_version: StrictInt
    application_scope: Literal["FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"]
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    local_feature_text_interpreted: StrictBool
    local_regulation_content_interpreted: StrictBool
    legal_conclusion_produced: StrictBool
    parcel_status_aggregated: StrictBool
    parcel_rejection_performed: StrictBool
    score_calculated: StrictBool
    policy_profile: StrictStr
    policy_sha256: StrictStr
    policy_result_hash_schema_version: StrictInt
    policy_complete_result_content_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_sha256: StrictStr
    cnig_result_hash_schema_version: StrictInt
    cnig_complete_result_content_sha256: StrictStr
    source_document_id: StrictStr
    source_archive_sha256: StrictStr
    cnig_surface_features_content_sha256: StrictStr
    cnig_line_features_content_sha256: StrictStr
    cnig_point_features_content_sha256: StrictStr
    cnig_relations_content_sha256: StrictStr
    surface_features_content_sha256: StrictStr
    line_features_content_sha256: StrictStr
    point_features_content_sha256: StrictStr
    relations_content_sha256: StrictStr
    complete_result_content_sha256: StrictStr
    artifacts: tuple[BessPlanningFeatureApplicationArtifactRecord, ...]

    @model_validator(mode="after")
    def _validate_manifest(self) -> BessPlanningFeatureApplicationArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application artifact manifest schema")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application result hash schema")
        if any(
            value is not False
            for value in (
                self.local_feature_text_interpreted,
                self.local_regulation_content_interpreted,
                self.legal_conclusion_produced,
                self.parcel_status_aggregated,
                self.parcel_rejection_performed,
                self.score_calculated,
            )
        ):
            raise ValueError("application boundary flags must all be false")
        for exact_value, label in (
            (self.policy_profile, "policy_profile"),
            (self.cnig_profile, "cnig_profile"),
            (self.source_document_id, "source_document_id"),
        ):
            _exact_string(exact_value, label)
        if self.policy_result_hash_schema_version != 1:
            raise ValueError("policy result hash schema must be exactly 1")
        if self.cnig_result_hash_schema_version != 5:
            raise ValueError("CNIG result hash schema must be exactly 5")
        for field in RESULT_SCALAR_FIELDS:
            if field.endswith("sha256"):
                _sha256_string(getattr(self, field), field)
        roles = tuple(record.artifact_role for record in self.artifacts)
        if roles != ARTIFACT_ROLES:
            raise ValueError(
                "application artifact roles are missing, extra, or unordered"
            )
        filenames = tuple(record.filename.casefold() for record in self.artifacts)
        if len(filenames) != len(set(filenames)):
            raise ValueError("application artifact filenames contain a duplicate")
        return self
```


## 6. Functions and methods

### `_exact_string`

**Exact signature**

```python
def _exact_string(value: object, label: str) -> str:
```

**Purpose**

Private `planning` helper for exact string; its complete implementation below is the authoritative behavioral contract.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/bess_application_contract.py::_sha256` via `_exact_string`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::_optional_official_string` via `_exact_string`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` via `_exact_string`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::_relation_identity_string` via `_exact_string`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::validate_bess_application_feature_catalogs` via `_exact_string`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_sha256_string` via `_exact_string`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_exact_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_sha256_string` via `_exact_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::BessPlanningFeatureApplicationArtifactManifest._validate_manifest` via `_exact_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_optional_exact_string` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_sha256_string` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::PolicySourceLock._validate_lock` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::PolicyEntry._validate_entry` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` via `_exact_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `_exact_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_official_text` via `_exact_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeProfile._validate_profile` via `_exact_string`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_strict_string` via `_exact_string`.
- callback/function object: `src/landscout/stages/road_vehicle_proxy_policy.py::<module>` via `AfterValidator(_exact_string)`.

**Complete source-ordered implementation**

```python
def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be an exact non-empty string")
    return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_sha256_string`

**Exact signature**

```python
def _sha256_string(value: object, label: str) -> str:
```

**Purpose**

Private `planning` helper for sha256 string; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
text
```

**Validation and exceptions**

- Guard with a raise path: `SHA_PATTERN.fullmatch(text) is None`.
- Explicit raise expressions: `ValueError(f'{label} must be a lowercase SHA256')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `SHA_PATTERN.fullmatch`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::BessPlanningFeatureParcelAggregationArtifactRecord._validate_record` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::BessPlanningFeatureParcelAggregationArtifactManifest._validate_manifest` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::BessPlanningFeatureApplicationArtifactRecord._validate_record` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::BessPlanningFeatureApplicationArtifactManifest._validate_manifest` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::PolicySourceLock._validate_lock` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyConfig._validate_policy` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::BessPlanningFeaturePolicyArtifactManifest._validate_manifest` via `_sha256_string`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `_sha256_string`.

**Complete source-ordered implementation**

```python
def _sha256_string(value: object, label: str) -> str:
    text = _exact_string(value, label)
    if SHA_PATTERN.fullmatch(text) is None:
        raise ValueError(f"{label} must be a lowercase SHA256")
    return text
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessPlanningFeatureApplicationArtifactRecord._validate_record`

**Exact signature**

```python
def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:
```

**Purpose**

Rejects malformed or inconsistent record; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationArtifactRecord`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `type(self.row_count) is not int or self.row_count < 0`.
- Guard with a raise path: `type(self.size_bytes) is not int or self.size_bytes < 1`.
- Guard with a raise path: `self.geospatial is not expected_geospatial`.
- Guard with a raise path: `expected_geospatial`.
- Guard with a raise path: `self.crs is None or signature_crs != self.crs`.
- Guard with a raise path: `not isinstance(signature_geometry, str) or not signature_geometry`.
- Guard with a raise path: `self.crs is not None or signature_crs is not None`.
- Explicit raise expressions: `ValueError('artifact geospatial flag differs from its role')`, `ValueError('artifact row_count must be a non-negative integer')`, `ValueError('artifact size_bytes must be a positive integer')`, `ValueError('geospatial artifact CRS is missing or inconsistent')`, `ValueError('geospatial artifact geometry column is missing')`, `ValueError('non-geospatial artifact must not declare a CRS')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_sha256_string`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be a non-negative integer")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be a positive integer")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geospatial = self.artifact_role != "RELATIONS"
        if self.geospatial is not expected_geospatial:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = self.frame_schema_signature.get("crs")
        signature_geometry = self.frame_schema_signature.get("geometry_column")
        if expected_geospatial:
            if self.crs is None or signature_crs != self.crs:
                raise ValueError("geospatial artifact CRS is missing or inconsistent")
            if not isinstance(signature_geometry, str) or not signature_geometry:
                raise ValueError("geospatial artifact geometry column is missing")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("non-geospatial artifact must not declare a CRS")
        return self
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `BessPlanningFeatureApplicationArtifactManifest._validate_manifest`

**Exact signature**

```python
def _validate_manifest(self) -> BessPlanningFeatureApplicationArtifactManifest:
```

**Purpose**

Rejects malformed or inconsistent manifest; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationArtifactManifest`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `type(self.schema_version) is not int or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION`.
- Guard with a raise path: `type(self.result_hash_schema_version) is not int or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`.
- Guard with a raise path: `any((value is not False for value in (self.local_feature_text_interpreted, self.local_regulation_content_interpreted, self.legal_conclusion_produced, self.parcel_status_aggregated, self.parcel_rejection_performed, self.score_calculated)))`.
- Guard with a raise path: `self.policy_result_hash_schema_version != 1`.
- Guard with a raise path: `self.cnig_result_hash_schema_version != 5`.
- Guard with a raise path: `roles != ARTIFACT_ROLES`.
- Guard with a raise path: `len(filenames) != len(set(filenames))`.
- Explicit raise expressions: `ValueError('CNIG result hash schema must be exactly 5')`, `ValueError('application artifact filenames contain a duplicate')`, `ValueError('application artifact roles are missing, extra, or unordered')`, `ValueError('application boundary flags must all be false')`, `ValueError('policy result hash schema must be exactly 1')`, `ValueError('unsupported application artifact manifest schema')`, `ValueError('unsupported application result hash schema')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_sha256_string`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

**Complete source-ordered implementation**

```python
def _validate_manifest(self) -> BessPlanningFeatureApplicationArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application artifact manifest schema")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("unsupported application result hash schema")
        if any(
            value is not False
            for value in (
                self.local_feature_text_interpreted,
                self.local_regulation_content_interpreted,
                self.legal_conclusion_produced,
                self.parcel_status_aggregated,
                self.parcel_rejection_performed,
                self.score_calculated,
            )
        ):
            raise ValueError("application boundary flags must all be false")
        for exact_value, label in (
            (self.policy_profile, "policy_profile"),
            (self.cnig_profile, "cnig_profile"),
            (self.source_document_id, "source_document_id"),
        ):
            _exact_string(exact_value, label)
        if self.policy_result_hash_schema_version != 1:
            raise ValueError("policy result hash schema must be exactly 1")
        if self.cnig_result_hash_schema_version != 5:
            raise ValueError("CNIG result hash schema must be exactly 5")
        for field in RESULT_SCALAR_FIELDS:
            if field.endswith("sha256"):
                _sha256_string(getattr(self, field), field)
        roles = tuple(record.artifact_role for record in self.artifacts)
        if roles != ARTIFACT_ROLES:
            raise ValueError(
                "application artifact roles are missing, extra, or unordered"
            )
        filenames = tuple(record.filename.casefold() for record in self.artifacts)
        if len(filenames) != len(set(filenames)):
            raise ValueError("application artifact filenames contain a duplicate")
        return self
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_null_value`

**Exact signature**

```python
def _null_value(value: object) -> object:
```

**Purpose**

Private `planning` helper for null value; its complete implementation below is the authoritative behavioral contract.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/common/bess_application_contract.py::_optional_official_string` via `_null_value`.
- direct call or construction: `src/landscout/common/bess_application_contract.py::validate_bess_application_policy_frame` via `_null_value`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_canonical_value` via `_null_value`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_local_domains` via `_null_value`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_canonical_value` via `_null_value`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_null_safe_equal` via `_null_value`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_null_safe_equal` via `_null_value`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_canonical_value` via `_null_value`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_table_rows` via `_null_value`.

**Complete source-ordered implementation**

```python
def _null_value(value: object) -> object:
    if value is None or value is pd.NA:
        return None
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        missing = False
    if isinstance(missing, (bool, np.bool_)) and bool(missing):
        return None
    return value
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

{'coordinate_dimension': coordinate_dimension, 'wkb_hex': to_wkb(value, hex=True, output_dimension=2, byte_order=1, include_srid=False)}

value.isoformat()

_canonical_value(value.item())

value

int(value)

number

value
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, BaseGeometry)`.
- Guard with a raise path: `isinstance(value, Real)`.
- Guard with a raise path: `coordinate_dimension != 2`.
- Guard with a raise path: `not math.isfinite(number)`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError('Application geometry coordinate dimension must be exactly 2D')`, `BessPlanningFeatureApplicationError('Application integrity payload contains non-finite data')`, `BessPlanningFeatureApplicationError(f'Unsupported application integrity value {type(value).__name__}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_canonical_sha256` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_frames` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_payload` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_compare_frame` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_canonical_value` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_canonical_sha256` via `_canonical_value`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_canonical_frame_rows` via `_canonical_value`.

**Complete source-ordered implementation**

```python
def _canonical_value(value: object) -> object:
    value = _null_value(value)
    if value is None:
        return None
    if isinstance(value, BaseGeometry):
        coordinate_dimension = int(get_coordinate_dimension(value))
        if coordinate_dimension != 2:
            raise BessPlanningFeatureApplicationError(
                "Application geometry coordinate dimension must be exactly 2D"
            )
        return {
            "coordinate_dimension": coordinate_dimension,
            "wkb_hex": to_wkb(
                value,
                hex=True,
                output_dimension=2,
                byte_order=1,
                include_srid=False,
            ),
        }
    if isinstance(value, (datetime, date, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, np.generic):
        return _canonical_value(value.item())
    if isinstance(value, bool):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        number = float(value)
        if not math.isfinite(number):
            raise BessPlanningFeatureApplicationError(
                "Application integrity payload contains non-finite data"
            )
        return number
    if isinstance(value, str):
        return value
    raise BessPlanningFeatureApplicationError(
        f"Unsupported application integrity value {type(value).__name__}"
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_frame_payload`

**Exact signature**

```python
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for frame payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'schema': deterministic_frame_schema_signature(frame), 'index': [_canonical_value(value) for value in frame.index.tolist()], 'rows': [[_canonical_value(value) for value in row] for row in frame.itertuples(index=False, name=None)]}
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_frame_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_result_with_hashes` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_compare_frame` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_component_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_compare_frame` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_policy_table_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_frame_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_zone_mapping_input_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_result_frame_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_frames` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_compare_results` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_source_frame_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_normalized_catalogs_input_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_sha256` via `_frame_payload`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_compare_frame` via `_frame_payload`.

**Complete source-ordered implementation**

```python
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
    return {
        "schema": deterministic_frame_schema_signature(frame),
        "index": [_canonical_value(value) for value in frame.index.tolist()],
        "rows": [
            [_canonical_value(value) for value in row]
            for row in frame.itertuples(index=False, name=None)
        ],
    }
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_application_geometry`

**Exact signature**

```python
def _validate_application_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
```

**Purpose**

Require supplied application geometry to remain canonical two-dimensional.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `geometry_name not in frame.columns`.
- Guard with a raise path: `not isinstance(geometry, BaseGeometry)`.
- Guard with a raise path: `int(get_coordinate_dimension(geometry)) != 2`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError(f'{label} active geometry column is missing')`, `BessPlanningFeatureApplicationError(f'{label} geometry at row {position} is missing or invalid')`, `BessPlanningFeatureApplicationError(f'{label} geometry at row {position} must be canonical 2D')`, `BessPlanningFeatureApplicationError(f'{label} geometry contract is invalid')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_feature_catalog` via `_validate_application_geometry`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_empty_optional_application_catalog_retains_schema_and_crs` via `module._validate_application_geometry`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_empty_optional_application_catalog_retains_schema_and_crs` via `module._validate_application_geometry`.

**Complete source-ordered implementation**

```python
def _validate_application_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
    """Require supplied application geometry to remain canonical two-dimensional."""

    try:
        geometry_name = frame.geometry.name
        if geometry_name not in frame.columns:
            raise BessPlanningFeatureApplicationError(
                f"{label} active geometry column is missing"
            )
        for position, geometry in enumerate(frame.geometry.array):
            if not isinstance(geometry, BaseGeometry):
                raise BessPlanningFeatureApplicationError(
                    f"{label} geometry at row {position} is missing or invalid"
                )
            if int(get_coordinate_dimension(geometry)) != 2:
                raise BessPlanningFeatureApplicationError(
                    f"{label} geometry at row {position} must be canonical 2D"
                )
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            f"{label} geometry contract is invalid"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_json_sha256`

**Exact signature**

```python
def _canonical_json_sha256(value: object) -> str:
```

**Purpose**

Private `planning` helper for canonical json sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
sha256(encoded).hexdigest()
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessPlanningFeatureApplicationError('Application integrity payload is not canonical JSON')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(encoded).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_component_sha256` via `_canonical_json_sha256`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_complete_result_sha256` via `_canonical_json_sha256`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_policy_entries_sha256` via `_canonical_json_sha256`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_policy_sha256` via `_canonical_json_sha256`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_policy_table_sha256` via `_canonical_json_sha256`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_complete_result_sha256` via `_canonical_json_sha256`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_records_sha256` via `_canonical_json_sha256`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_profile_sha256` via `_canonical_json_sha256`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_source_frame_sha256` via `_canonical_json_sha256`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_planning_document_context_sha256` via `_canonical_json_sha256`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_normalized_catalogs_input_sha256` via `_canonical_json_sha256`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_sha256` via `_canonical_json_sha256`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_complete_sha256` via `_canonical_json_sha256`.

**Complete source-ordered implementation**

```python
def _canonical_json_sha256(value: object) -> str:
    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureApplicationError(
            "Application integrity payload is not canonical JSON"
        ) from error
    return sha256(encoded).hexdigest()
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_null_safe_equal`

**Exact signature**

```python
def _null_safe_equal(left: object, right: object) -> bool:
```

**Purpose**

Private `planning` helper for null safe equal; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
left is None and right is None

bool(left == right)

False
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_relations` via `_null_safe_equal`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `_null_safe_equal`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_coded_policy_compatibility` via `_null_safe_equal`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_completeness` via `_null_safe_equal`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_validate_relation_catalog_consistency` via `_null_safe_equal`.
- direct call or construction: `src/landscout/stages/enrich_planning_features.py::_compare_rebuilt_relations` via `_null_safe_equal`.
- direct call or construction: `src/landscout/stages/enrich_road_proximity.py::_validate_selected_evidence` via `_null_safe_equal`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_coded_meaning_rows` via `_null_safe_equal`.

**Complete source-ordered implementation**

```python
def _null_safe_equal(left: object, right: object) -> bool:
    left = _null_value(left)
    right = _null_value(right)
    if left is None or right is None:
        return left is None and right is None
    try:
        return bool(left == right)
    except (TypeError, ValueError):
        return False
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_lookup`

**Exact signature**

```python
def _policy_lookup(
    policy: BessPlanningFeaturePolicyResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

**Purpose**

Private `planning` helper for policy lookup; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[tuple[str, str, str], dict[str, object]]`.
- Every observed return expression is reproduced without truncation:
```python
lookup
```

**Validation and exceptions**

- Guard with a raise path: `key in lookup`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError('Compiled policy contains a duplicate exact code pair')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `lookup[key]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_feature_catalog` via `_policy_lookup`.

**Complete source-ordered implementation**

```python
def _policy_lookup(
    policy: BessPlanningFeaturePolicyResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    lookup: dict[tuple[str, str, str], dict[str, object]] = {}
    for row in policy.policy_table.to_dict("records"):
        key = (
            str(row["feature_family"]),
            str(row["type_code"]),
            str(row["subtype_code"]),
        )
        if key in lookup:
            raise BessPlanningFeatureApplicationError(
                "Compiled policy contains a duplicate exact code pair"
            )
        lookup[key] = row
    return lookup
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_policy_values`

**Exact signature**

```python
def _policy_values(
    row: dict[str, object] | None,
    application_status: ApplicationStatus,
    policy: BessPlanningFeaturePolicyResult,
) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for policy values; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'bess_cnig_policy_application_status': application_status, 'bess_cnig_precheck_status': None if row is None else row['precheck_status'], 'bess_cnig_precheck_confidence': None if row is None else row['confidence'], 'bess_cnig_status_priority': None if row is None else row['status_priority'], 'bess_cnig_rationale': None if row is None else row['rationale'], 'bess_cnig_required_human_action': None if row is None else row['required_human_action'], 'bess_cnig_limitations': None if row is None else row['limitations'], 'bess_cnig_application_scope': APPLICATION_SCOPE, 'bess_cnig_policy_scope': policy.policy_scope, 'bess_cnig_local_feature_text_interpreted': False, 'bess_cnig_local_regulation_content_interpreted': False, 'bess_cnig_legal_conclusion_produced': False, 'bess_cnig_parcel_status_aggregated': False, 'bess_cnig_parcel_rejection_performed': False, 'bess_cnig_score_calculated': False, 'bess_cnig_policy_profile': policy.policy_profile, 'bess_cnig_policy_sha256': policy.policy_sha256, 'bess_cnig_policy_result_sha256': policy.complete_result_content_sha256}
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_feature_catalog` via `_policy_values`.

**Complete source-ordered implementation**

```python
def _policy_values(
    row: dict[str, object] | None,
    application_status: ApplicationStatus,
    policy: BessPlanningFeaturePolicyResult,
) -> dict[str, object]:
    return {
        "bess_cnig_policy_application_status": application_status,
        "bess_cnig_precheck_status": None if row is None else row["precheck_status"],
        "bess_cnig_precheck_confidence": None if row is None else row["confidence"],
        "bess_cnig_status_priority": None if row is None else row["status_priority"],
        "bess_cnig_rationale": None if row is None else row["rationale"],
        "bess_cnig_required_human_action": (
            None if row is None else row["required_human_action"]
        ),
        "bess_cnig_limitations": None if row is None else row["limitations"],
        "bess_cnig_application_scope": APPLICATION_SCOPE,
        "bess_cnig_policy_scope": policy.policy_scope,
        "bess_cnig_local_feature_text_interpreted": False,
        "bess_cnig_local_regulation_content_interpreted": False,
        "bess_cnig_legal_conclusion_produced": False,
        "bess_cnig_parcel_status_aggregated": False,
        "bess_cnig_parcel_rejection_performed": False,
        "bess_cnig_score_calculated": False,
        "bess_cnig_policy_profile": policy.policy_profile,
        "bess_cnig_policy_sha256": policy.policy_sha256,
        "bess_cnig_policy_result_sha256": policy.complete_result_content_sha256,
    }
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_assign_policy_columns`

**Exact signature**

```python
def _assign_policy_columns(
    frame: pd.DataFrame,
    rows: list[dict[str, object]],
) -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for assign policy columns; its complete implementation below is the authoritative behavioral contract.

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

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `frame[column]`, `values['bess_cnig_status_priority']`, `values[column]`.
- Input mutation: `frame[column]`.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_feature_catalog` via `_assign_policy_columns`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_relations` via `_assign_policy_columns`.

**Complete source-ordered implementation**

```python
def _assign_policy_columns(
    frame: pd.DataFrame,
    rows: list[dict[str, object]],
) -> pd.DataFrame:
    values: dict[str, object] = {}
    for column in STRING_POLICY_COLUMNS:
        values[column] = pd.array([row[column] for row in rows], dtype="str")
    values["bess_cnig_status_priority"] = pd.array(
        [row["bess_cnig_status_priority"] for row in rows], dtype="Int64"
    )
    for column in FLAG_COLUMNS:
        values[column] = pd.array([row[column] for row in rows], dtype="bool")
    for column in POLICY_COLUMNS:
        frame[column] = values[column]
    return frame
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_apply_feature_catalog`

**Exact signature**

```python
def _apply_feature_catalog(
    catalog: gpd.GeoDataFrame,
    policy: BessPlanningFeaturePolicyResult,
) -> gpd.GeoDataFrame:
```

**Purpose**

Apply exact family/type/subtype policy to one already-coded catalog.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
applied
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(catalog, gpd.GeoDataFrame)`.
- Guard with a raise path: `any((column in catalog.columns for column in POLICY_COLUMNS))`.
- Guard with a raise path: `not required.issubset(catalog.columns)`.
- Guard with a raise path: `not isinstance(type_code, str) or CODE_PATTERN.fullmatch(type_code) is None`.
- Guard with a raise path: `not isinstance(subtype_code, str) or CODE_PATTERN.fullmatch(subtype_code) is None`.
- Guard with a raise path: `official_status == 'RESOLVED_OFFICIAL'`.
- Guard with a raise path: `policy_row is None`.
- Guard with a raise path: `official_status == 'UNKNOWN_CODE_PAIR'`.
- Guard with a raise path: `policy_row is not None`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError('Coded feature catalog already contains BESS policy columns')`, `BessPlanningFeatureApplicationError('Coded feature catalog is not geospatial')`, `BessPlanningFeatureApplicationError('Coded feature catalog lacks exact policy lookup fields')`, `BessPlanningFeatureApplicationError('Feature official-code status is invalid')`, `BessPlanningFeatureApplicationError('Feature subtype code is not an exact two-character string')`, `BessPlanningFeatureApplicationError('Feature type code is not an exact two-character string')`, `BessPlanningFeatureApplicationError(f'Resolved official feature has no exact policy row: {key}')`, `BessPlanningFeatureApplicationError(f'Unknown official feature unexpectedly matches policy row: {key}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: `_validate_application_geometry`.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_build_result` via `_apply_feature_catalog`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_empty_optional_application_catalog_retains_schema_and_crs` via `module._apply_feature_catalog`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_empty_optional_application_catalog_retains_schema_and_crs` via `module._apply_feature_catalog`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct` via `module._apply_feature_catalog`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_exact_pair_identity_keeps_family_subtype_and_leading_zeroes_distinct` via `module._apply_feature_catalog`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_pair_remains_present_with_true_null_decision_fields` via `module._apply_feature_catalog`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_pair_remains_present_with_true_null_decision_fields` via `module._apply_feature_catalog`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_inconsistent_official_status_and_policy_match_is_rejected` via `module._apply_feature_catalog`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_inconsistent_official_status_and_policy_match_is_rejected` via `module._apply_feature_catalog`.

**Complete source-ordered implementation**

```python
def _apply_feature_catalog(
    catalog: gpd.GeoDataFrame,
    policy: BessPlanningFeaturePolicyResult,
) -> gpd.GeoDataFrame:
    """Apply exact family/type/subtype policy to one already-coded catalog."""

    if not isinstance(catalog, gpd.GeoDataFrame):
        raise BessPlanningFeatureApplicationError(
            "Coded feature catalog is not geospatial"
        )
    if any(column in catalog.columns for column in POLICY_COLUMNS):
        raise BessPlanningFeatureApplicationError(
            "Coded feature catalog already contains BESS policy columns"
        )
    required = {
        "planning_feature_id",
        "feature_family",
        "type_code_raw",
        "subtype_code_raw",
        "official_code_status",
    }
    if not required.issubset(catalog.columns):
        raise BessPlanningFeatureApplicationError(
            "Coded feature catalog lacks exact policy lookup fields"
        )
    lookup = _policy_lookup(policy)
    policy_rows: list[dict[str, object]] = []
    for row in catalog.to_dict("records"):
        type_code = row["type_code_raw"]
        subtype_code = row["subtype_code_raw"]
        if not isinstance(type_code, str) or CODE_PATTERN.fullmatch(type_code) is None:
            raise BessPlanningFeatureApplicationError(
                "Feature type code is not an exact two-character string"
            )
        if (
            not isinstance(subtype_code, str)
            or CODE_PATTERN.fullmatch(subtype_code) is None
        ):
            raise BessPlanningFeatureApplicationError(
                "Feature subtype code is not an exact two-character string"
            )
        key = (str(row["feature_family"]), type_code, subtype_code)
        official_status = row["official_code_status"]
        policy_row = lookup.get(key)
        if official_status == "RESOLVED_OFFICIAL":
            if policy_row is None:
                raise BessPlanningFeatureApplicationError(
                    f"Resolved official feature has no exact policy row: {key}"
                )
            application_status: ApplicationStatus = "APPLIED_EXACT_POLICY"
        elif official_status == "UNKNOWN_CODE_PAIR":
            if policy_row is not None:
                raise BessPlanningFeatureApplicationError(
                    f"Unknown official feature unexpectedly matches policy row: {key}"
                )
            application_status = "UNRESOLVED_CODE_PAIR"
        else:
            raise BessPlanningFeatureApplicationError(
                "Feature official-code status is invalid"
            )
        policy_rows.append(_policy_values(policy_row, application_status, policy))
    output = catalog.copy(deep=True)
    _assign_policy_columns(output, policy_rows)
    applied = gpd.GeoDataFrame(output, geometry=catalog.geometry.name, crs=catalog.crs)
    _validate_application_geometry(applied, "applied feature catalog")
    return applied
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_feature_rows_by_id`

**Exact signature**

```python
def _feature_rows_by_id(
    *catalogs: gpd.GeoDataFrame,
) -> dict[str, dict[str, object]]:
```

**Purpose**

Private `planning` helper for feature rows by id; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, dict[str, object]]`.
- Every observed return expression is reproduced without truncation:
```python
indexed
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(feature_id, str) or not feature_id`.
- Guard with a raise path: `feature_id in indexed`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError('Enriched feature ID must be an exact string')`, `BessPlanningFeatureApplicationError('Enriched planning feature ID is not globally unique')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `indexed[feature_id]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_apply_relations` via `_feature_rows_by_id`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `_feature_rows_by_id`.

**Complete source-ordered implementation**

```python
def _feature_rows_by_id(
    *catalogs: gpd.GeoDataFrame,
) -> dict[str, dict[str, object]]:
    indexed: dict[str, dict[str, object]] = {}
    for catalog in catalogs:
        for row in catalog.to_dict("records"):
            feature_id = row["planning_feature_id"]
            if not isinstance(feature_id, str) or not feature_id:
                raise BessPlanningFeatureApplicationError(
                    "Enriched feature ID must be an exact string"
                )
            if feature_id in indexed:
                raise BessPlanningFeatureApplicationError(
                    "Enriched planning feature ID is not globally unique"
                )
            indexed[feature_id] = row
    return indexed
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_apply_relations`

**Exact signature**

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

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
_assign_policy_columns(output, policy_rows)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(relations, pd.DataFrame) or isinstance(relations, gpd.GeoDataFrame)`.
- Guard with a raise path: `any((column in relations.columns for column in POLICY_COLUMNS))`.
- Guard with a raise path: `not required.issubset(relations.columns)`.
- Guard with a raise path: `feature is None`.
- Guard with a raise path: `not _null_safe_equal(relation[column], feature[column])`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError('Coded relations already contain BESS policy columns')`, `BessPlanningFeatureApplicationError('Coded relations lack feature-policy agreement fields')`, `BessPlanningFeatureApplicationError('Coded relations must be a DataFrame')`, `BessPlanningFeatureApplicationError(f'Relation references unknown planning feature ID: {feature_id!r}')`, `BessPlanningFeatureApplicationError(f'Relation {column} differs from referenced feature')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_build_result` via `_apply_relations`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_relation_feature_id_is_rejected` via `module._apply_relations`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_relation_feature_id_is_rejected` via `module._apply_relations`.

**Complete source-ordered implementation**

```python
def _apply_relations(
    relations: pd.DataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> pd.DataFrame:
    """Propagate feature policy to relations only through planning_feature_id."""

    if not isinstance(relations, pd.DataFrame) or isinstance(
        relations, gpd.GeoDataFrame
    ):
        raise BessPlanningFeatureApplicationError("Coded relations must be a DataFrame")
    if any(column in relations.columns for column in POLICY_COLUMNS):
        raise BessPlanningFeatureApplicationError(
            "Coded relations already contain BESS policy columns"
        )
    required = {"planning_feature_id", *RELATION_FEATURE_AGREEMENT_COLUMNS}
    if not required.issubset(relations.columns):
        raise BessPlanningFeatureApplicationError(
            "Coded relations lack feature-policy agreement fields"
        )
    features = _feature_rows_by_id(surface_features, line_features, point_features)
    policy_rows: list[dict[str, object]] = []
    for relation in relations.to_dict("records"):
        feature_id = relation["planning_feature_id"]
        feature = features.get(str(feature_id))
        if feature is None:
            raise BessPlanningFeatureApplicationError(
                f"Relation references unknown planning feature ID: {feature_id!r}"
            )
        for column in RELATION_FEATURE_AGREEMENT_COLUMNS:
            if not _null_safe_equal(relation[column], feature[column]):
                raise BessPlanningFeatureApplicationError(
                    f"Relation {column} differs from referenced feature"
                )
        policy_rows.append({column: feature[column] for column in POLICY_COLUMNS})
    output = relations.copy(deep=True)
    return _assign_policy_columns(output, policy_rows)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_component_metadata`

**Exact signature**

```python
def _component_metadata(
    result: BessPlanningFeatureApplicationResult,
) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for component metadata; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'result_hash_schema_version': result.result_hash_schema_version, 'application_scope': result.application_scope, 'policy_scope': result.policy_scope, 'local_feature_text_interpreted': result.local_feature_text_interpreted, 'local_regulation_content_interpreted': result.local_regulation_content_interpreted, 'legal_conclusion_produced': result.legal_conclusion_produced, 'parcel_status_aggregated': result.parcel_status_aggregated, 'parcel_rejection_performed': result.parcel_rejection_performed, 'score_calculated': result.score_calculated, 'policy_profile': result.policy_profile, 'policy_sha256': result.policy_sha256, 'policy_result_hash_schema_version': result.policy_result_hash_schema_version, 'policy_complete_result_content_sha256': result.policy_complete_result_content_sha256, 'cnig_profile': result.cnig_profile, 'cnig_profile_sha256': result.cnig_profile_sha256, 'cnig_result_hash_schema_version': result.cnig_result_hash_schema_version, 'cnig_complete_result_content_sha256': result.cnig_complete_result_content_sha256, 'source_document_id': result.source_document_id, 'source_archive_sha256': result.source_archive_sha256, 'cnig_surface_features_content_sha256': result.cnig_surface_features_content_sha256, 'cnig_line_features_content_sha256': result.cnig_line_features_content_sha256, 'cnig_point_features_content_sha256': result.cnig_point_features_content_sha256, 'cnig_relations_content_sha256': result.cnig_relations_content_sha256}
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_result_with_hashes` via `_component_metadata`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_component_sha256` via `_component_metadata`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_complete_result_sha256` via `_component_metadata`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_policy_table_sha256` via `_component_metadata`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_complete_result_sha256` via `_component_metadata`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_sha256` via `_component_metadata`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_complete_sha256` via `_component_metadata`.

**Complete source-ordered implementation**

```python
def _component_metadata(
    result: BessPlanningFeatureApplicationResult,
) -> dict[str, object]:
    return {
        "result_hash_schema_version": result.result_hash_schema_version,
        "application_scope": result.application_scope,
        "policy_scope": result.policy_scope,
        "local_feature_text_interpreted": result.local_feature_text_interpreted,
        "local_regulation_content_interpreted": (
            result.local_regulation_content_interpreted
        ),
        "legal_conclusion_produced": result.legal_conclusion_produced,
        "parcel_status_aggregated": result.parcel_status_aggregated,
        "parcel_rejection_performed": result.parcel_rejection_performed,
        "score_calculated": result.score_calculated,
        "policy_profile": result.policy_profile,
        "policy_sha256": result.policy_sha256,
        "policy_result_hash_schema_version": (result.policy_result_hash_schema_version),
        "policy_complete_result_content_sha256": (
            result.policy_complete_result_content_sha256
        ),
        "cnig_profile": result.cnig_profile,
        "cnig_profile_sha256": result.cnig_profile_sha256,
        "cnig_result_hash_schema_version": result.cnig_result_hash_schema_version,
        "cnig_complete_result_content_sha256": (
            result.cnig_complete_result_content_sha256
        ),
        "source_document_id": result.source_document_id,
        "source_archive_sha256": result.source_archive_sha256,
        "cnig_surface_features_content_sha256": (
            result.cnig_surface_features_content_sha256
        ),
        "cnig_line_features_content_sha256": result.cnig_line_features_content_sha256,
        "cnig_point_features_content_sha256": (
            result.cnig_point_features_content_sha256
        ),
        "cnig_relations_content_sha256": result.cnig_relations_content_sha256,
    }
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_component_sha256`

**Exact signature**

```python
def _component_sha256(
    result: BessPlanningFeatureApplicationResult,
    frame: pd.DataFrame,
    role: str,
) -> str:
```

**Purpose**

Private `planning` helper for component sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256({'domain': f'landscout.bess_planning_feature_application.{role}', **_component_metadata(result), 'frame': _frame_payload(frame)})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_result_with_hashes` via `_component_sha256`.

**Complete source-ordered implementation**

```python
def _component_sha256(
    result: BessPlanningFeatureApplicationResult,
    frame: pd.DataFrame,
    role: str,
) -> str:
    return _canonical_json_sha256(
        {
            "domain": f"landscout.bess_planning_feature_application.{role}",
            **_component_metadata(result),
            "frame": _frame_payload(frame),
        }
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_complete_result_sha256`

**Exact signature**

```python
def _complete_result_sha256(result: BessPlanningFeatureApplicationResult) -> str:
```

**Purpose**

Private `planning` helper for complete result sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256({'domain': 'landscout.bess_planning_feature_application.result', **_component_metadata(result), 'surface_features_content_sha256': result.surface_features_content_sha256, 'line_features_content_sha256': result.line_features_content_sha256, 'point_features_content_sha256': result.point_features_content_sha256, 'relations_content_sha256': result.relations_content_sha256})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_result_with_hashes` via `_complete_result_sha256`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_result_with_hashes` via `_complete_result_sha256`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_result_with_hashes` via `_complete_result_sha256`.

**Complete source-ordered implementation**

```python
def _complete_result_sha256(result: BessPlanningFeatureApplicationResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.bess_planning_feature_application.result",
            **_component_metadata(result),
            "surface_features_content_sha256": (result.surface_features_content_sha256),
            "line_features_content_sha256": result.line_features_content_sha256,
            "point_features_content_sha256": result.point_features_content_sha256,
            "relations_content_sha256": result.relations_content_sha256,
        }
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_result_with_hashes`

**Exact signature**

```python
def _result_with_hashes(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Private `planning` helper for result with hashes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
replace(components, complete_result_content_sha256=_complete_result_sha256(components))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_complete_result_sha256`, `_component_sha256`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_build_structure_result` via `_result_with_hashes`.
- direct call or construction: `src/landscout/stages/structure_planning_regulation.py::_validate_result_self` via `_result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `importlib.import_module('landscout.stages.apply_bess_planning_feature_policy')._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_rehash_coordinated_result` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_rehash_coordinated_result` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_local_corruption_fast_fails_before_heavy_validation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_authorized_status_artifact_fails_local_verified_byte_loading` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_no_relation_parcel_rejects_textual_null_identity` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_representative_intrinsic_failures_all_precede_heavy_validation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_changed_parcel_geometry_upstreams` via `application_module._result_with_hashes`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_changed_parcel_geometry_upstreams` via `application_module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_policy_mutation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_policy_mutation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_feature_id_mutation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_feature_id_mutation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_surface_touch_with_positive_area` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_surface_touch_with_positive_area` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_replace_application_frame` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_replace_application_frame` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_referenced_lineage_mutation` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_coordinated_referenced_lineage_mutation` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_swap_referenced_feature_values` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::_swap_referenced_feature_values` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `coding_module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `coding_module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `policy_module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `policy_module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `module._result_with_hashes`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `module._result_with_hashes`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_compatible_policy_mutation` via `module._result_with_hashes`.

**Complete source-ordered implementation**

```python
def _result_with_hashes(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
    components = replace(
        result,
        surface_features_content_sha256=_component_sha256(
            result, result.surface_features, "surface_features"
        ),
        line_features_content_sha256=_component_sha256(
            result, result.line_features, "line_features"
        ),
        point_features_content_sha256=_component_sha256(
            result, result.point_features, "point_features"
        ),
        relations_content_sha256=_component_sha256(
            result, result.relations, "relations"
        ),
    )
    return replace(
        components,
        complete_result_content_sha256=_complete_result_sha256(components),
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_result`

**Exact signature**

```python
def _build_result(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeatureApplicationResult:
```

**Purpose**

Constructs result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
_result_with_hashes(result)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_result_with_hashes`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::aggregate_bess_planning_feature_policy_to_parcels` via `_build_result`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `_build_result`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `_build_result`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::apply_bess_planning_feature_policy` via `_build_result`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `_build_result`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `_build_result`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `_build_result`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `_build_result`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::validate_bess_zoning_precheck` via `_build_result`.
- direct call or construction: `src/landscout/stages/interpret_bess_zoning.py::interpret_bess_zoning` via `_build_result`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `_build_result`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `_build_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `module._build_result`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_build_from_relations` via `module._build_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_surface_touch_semantic_corruption_result` via `module._build_result`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_surface_touch_semantic_corruption_result` via `module._build_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_validate_parcel_geometries` via `module._build_result`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_validate_parcel_geometries` via `module._build_result`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `module._build_result`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `module._build_result`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rebuilds_once_without_mutating_upstreams` via `module._build_result`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._build_result`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._build_result`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `module._build_result`.
- direct call or construction: `tests/unit/test_bess_planning_feature_policy.py::_checked_in_policy_result` via `policy_module._build_result`.
- property/attribute access: `tests/unit/test_bess_planning_feature_policy.py::_checked_in_policy_result` via `policy_module._build_result`.
- direct call or construction: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `interpret_module._build_result`.
- property/attribute access: `tests/unit/test_interpret_bess_zoning.py::test_one_build_result_performs_one_factual_structure_rebuild` via `interpret_module._build_result`.

**Complete source-ordered implementation**

```python
def _build_result(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeatureApplicationResult:
    surface = _apply_feature_catalog(coded.surface_features, policy)
    line = _apply_feature_catalog(coded.line_features, policy)
    point = _apply_feature_catalog(coded.point_features, policy)
    relations = _apply_relations(coded.relations, surface, line, point)
    result = BessPlanningFeatureApplicationResult(
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        application_scope=APPLICATION_SCOPE,
        policy_scope=policy.policy_scope,
        local_feature_text_interpreted=False,
        local_regulation_content_interpreted=False,
        legal_conclusion_produced=False,
        parcel_status_aggregated=False,
        parcel_rejection_performed=False,
        score_calculated=False,
        policy_profile=policy.policy_profile,
        policy_sha256=policy.policy_sha256,
        policy_result_hash_schema_version=policy.result_hash_schema_version,
        policy_complete_result_content_sha256=policy.complete_result_content_sha256,
        cnig_profile=coded.profile,
        cnig_profile_sha256=coded.profile_sha256,
        cnig_result_hash_schema_version=coded.result_hash_schema_version,
        cnig_complete_result_content_sha256=coded.complete_result_content_sha256,
        source_document_id=coded.source_document_id,
        source_archive_sha256=coded.source_archive_sha256,
        cnig_surface_features_content_sha256=coded.surface_features_content_sha256,
        cnig_line_features_content_sha256=coded.line_features_content_sha256,
        cnig_point_features_content_sha256=coded.point_features_content_sha256,
        cnig_relations_content_sha256=coded.relations_content_sha256,
        surface_features_content_sha256="",
        line_features_content_sha256="",
        point_features_content_sha256="",
        relations_content_sha256="",
        complete_result_content_sha256="",
        surface_features=surface,
        line_features=line,
        point_features=point,
        relations=relations,
    )
    return _result_with_hashes(result)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_relation_rows`

**Exact signature**

```python
def _validate_relation_rows(
    frame: pd.DataFrame,
    label: str,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[dict[int, str], dict[str, int]]:
```

**Purpose**

Rejects malformed or inconsistent relation rows; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `tuple[dict[int, str], dict[str, int]]`.
- Every observed return expression is reproduced without truncation:
```python
validate_bess_application_relation_frame(frame, label=label, policy_profile=result.policy_profile, policy_sha256=result.policy_sha256, policy_result_sha256=result.policy_complete_result_content_sha256, source_document_id=result.source_document_id, source_archive_sha256=result.source_archive_sha256, cnig_profile=result.cnig_profile, cnig_profile_sha256=result.cnig_profile_sha256)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessPlanningFeatureApplicationError(str(error))`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_result_envelope` via `_validate_relation_rows`.

**Complete source-ordered implementation**

```python
def _validate_relation_rows(
    frame: pd.DataFrame,
    label: str,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[dict[int, str], dict[str, int]]:
    try:
        return validate_bess_application_relation_frame(
            frame,
            label=label,
            policy_profile=result.policy_profile,
            policy_sha256=result.policy_sha256,
            policy_result_sha256=result.policy_complete_result_content_sha256,
            source_document_id=result.source_document_id,
            source_archive_sha256=result.source_archive_sha256,
            cnig_profile=result.cnig_profile,
            cnig_profile_sha256=result.cnig_profile_sha256,
        )
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureApplicationError(str(error)) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result_envelope`

**Exact signature**

```python
def _validate_result_envelope(result: BessPlanningFeatureApplicationResult) -> None:
```

**Purpose**

Rejects malformed or inconsistent result envelope; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(result, BessPlanningFeatureApplicationResult)`.
- Guard with a raise path: `type(result.result_hash_schema_version) is not int or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION`.
- Guard with a raise path: `result.application_scope != APPLICATION_SCOPE or result.policy_scope != POLICY_SCOPE`.
- Guard with a raise path: `result.policy_result_hash_schema_version != 1`.
- Guard with a raise path: `result.cnig_result_hash_schema_version != 5`.
- Guard with a raise path: `any((value is not False for value in (result.local_feature_text_interpreted, result.local_regulation_content_interpreted, result.legal_conclusion_produced, result.parcel_status_aggregated, result.parcel_rejection_performed, result.score_calculated)))`.
- Guard with a raise path: `not isinstance(result.relations, pd.DataFrame) or isinstance(result.relations, gpd.GeoDataFrame)`.
- Guard with a raise path: `result.relations.columns.duplicated().any()`.
- Guard with a raise path: `any((feature_mapping[0].get(priority) != status for priority, status in relation_mapping[0].items())) or any((feature_mapping[1].get(status) != priority for status, priority in relation_mapping[1].items()))`.
- Guard with a raise path: `not isinstance(frame, gpd.GeoDataFrame)`.
- Guard with a raise path: `frame.columns.duplicated().any()`.
- Guard with a raise path: `feature is None`.
- Guard with a raise path: `not metric_equal`.
- Guard with a raise path: `field.endswith('sha256')`.
- Guard with a raise path: `getattr(result, field) != getattr(rebuilt, field)`.
- Guard with a raise path: `not _null_safe_equal(relation[column], feature[column])`.
- Guard with a raise path: `isinstance(actual_value, bool) or not isinstance(actual_value, Real) or isinstance(expected_value, bool) or (not isinstance(expected_value, Real))`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError('Application relation feature metric differs from its feature')`, `BessPlanningFeatureApplicationError('Application relation feature metric is not numeric')`, `BessPlanningFeatureApplicationError('Application relation references an unknown feature')`, `BessPlanningFeatureApplicationError('CNIG result hash schema must be exactly 5')`, `BessPlanningFeatureApplicationError('application result boundary flags must all be false')`, `BessPlanningFeatureApplicationError('application result scope is invalid')`, `BessPlanningFeatureApplicationError('policy result hash schema must be exactly 1')`, `BessPlanningFeatureApplicationError('relation policy mapping differs from the feature mapping')`, `BessPlanningFeatureApplicationError('relations must be a DataFrame')`, `BessPlanningFeatureApplicationError('relations policy schema is invalid')`, `BessPlanningFeatureApplicationError('result must be a BessPlanningFeatureApplicationResult')`, `BessPlanningFeatureApplicationError('unsupported result hash schema')`, `BessPlanningFeatureApplicationError(f'Application relation {column} differs from its feature')`, `BessPlanningFeatureApplicationError(f'{field} is invalid')`, `BessPlanningFeatureApplicationError(f'{label} must be geospatial')`, `BessPlanningFeatureApplicationError(f'{label} policy schema is invalid')`, `BessPlanningFeatureApplicationError(str(error))`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `_result_with_hashes`, `_sha256_string`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::aggregate_bess_planning_feature_policy_to_parcels` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result_envelope` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::apply_bess_planning_feature_policy` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result_envelope` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_artifacts` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result_envelope` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `_validate_result_envelope`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `_validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_coordinated_local_cross_table_corruption_is_rejected` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_invalid_output_dtype_and_non_2d_parcel_fail_locally` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_selected_relation_role_requires_selected_status_and_priority` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_validate_parcel_geometries` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_validate_parcel_geometries` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_output_columns_are_rejected_intrinsically` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_duplicate_output_columns_are_rejected_intrinsically` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_only_application_result_schema_two_is_accepted` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_application_result_schema_two_remains_accepted` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_application_result_schema_two_remains_accepted` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_decision_status_domain_rejects_forbidden_vocabulary` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_persisted_feature_id_json_must_be_portable_and_canonical` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_relation_parcel_area_is_bound_to_real_parcel_geometry` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_validation_uses_reprojected_calculation_copy` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_parcel_area_validation_uses_reprojected_calculation_copy` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_changed_parcel_geometry_upstreams` via `application_module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_changed_parcel_geometry_upstreams` via `application_module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_source_bound_aggregation_loader_rejects_coordinated_upstream_changes` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_schema_v1_dimension_blind_hash_representation_is_rejected_locally` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_m_and_zm_application_geometries_are_rejected` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_m_and_zm_application_geometries_are_rejected` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_complete_relation_facts_must_match_referenced_feature` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_application_relation_pair_is_rejected_locally` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_feature_id_is_exact_and_portable` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_feature_id_is_exact_and_portable` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_parcel_id_is_exact` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_application_relation_type_is_rejected_locally` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_invalid_policy_domains_fail_local_validation` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_invalid_policy_domains_fail_local_validation` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_literal_null_replacements_are_rejected` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_literal_null_replacements_are_rejected` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_policy_suffix_dtype_is_rejected` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_policy_suffix_dtype_is_rejected` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_official_and_application_statuses_cannot_contradict` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_any_true_row_boundary_flag_is_rejected` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_any_true_row_boundary_flag_is_rejected` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_geometry_role_is_intrinsic` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_metric_must_match_geometry` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_catalog_identity_fields_are_intrinsic` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_catalog_requires_canonical_crs_and_global_identity` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_policy_result_schema_exactly` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_locks_cnig_result_schema_exactly` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_accepts_only_current_policy_and_cnig_source_schemas` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_accepts_only_current_policy_and_cnig_source_schemas` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_row_lineage_must_match_application_envelope` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_referenced_row_lineage_cannot_bypass_envelope` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_referenced_row_lineage_cannot_bypass_envelope` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_resolved_official_row_requires_label_and_envelope_profile` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_resolved_official_row_requires_label_and_envelope_profile` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_official_row_rejects_invented_label_or_url` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unknown_official_row_rejects_invented_label_or_url` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_feature_prefix_has_exact_canonical_schema` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_feature_prefix_has_exact_canonical_schema` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_prefix_has_exact_canonical_schema` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_relation_prefix_has_exact_canonical_schema` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module._validate_result_envelope`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._validate_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module._validate_result_envelope`.

**Complete source-ordered implementation**

```python
def _validate_result_envelope(result: BessPlanningFeatureApplicationResult) -> None:
    if not isinstance(result, BessPlanningFeatureApplicationResult):
        raise BessPlanningFeatureApplicationError(
            "result must be a BessPlanningFeatureApplicationResult"
        )
    if (
        type(result.result_hash_schema_version) is not int
        or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
    ):
        raise BessPlanningFeatureApplicationError("unsupported result hash schema")
    if (
        result.application_scope != APPLICATION_SCOPE
        or result.policy_scope != POLICY_SCOPE
    ):
        raise BessPlanningFeatureApplicationError("application result scope is invalid")
    for exact_value, label in (
        (result.policy_profile, "policy_profile"),
        (result.cnig_profile, "cnig_profile"),
        (result.source_document_id, "source_document_id"),
    ):
        try:
            _exact_string(exact_value, label)
        except ValueError as error:
            raise BessPlanningFeatureApplicationError(str(error)) from error
    if result.policy_result_hash_schema_version != 1:
        raise BessPlanningFeatureApplicationError(
            "policy result hash schema must be exactly 1"
        )
    if result.cnig_result_hash_schema_version != 5:
        raise BessPlanningFeatureApplicationError(
            "CNIG result hash schema must be exactly 5"
        )
    if any(
        value is not False
        for value in (
            result.local_feature_text_interpreted,
            result.local_regulation_content_interpreted,
            result.legal_conclusion_produced,
            result.parcel_status_aggregated,
            result.parcel_rejection_performed,
            result.score_calculated,
        )
    ):
        raise BessPlanningFeatureApplicationError(
            "application result boundary flags must all be false"
        )
    for frame, label in (
        (result.surface_features, "surface features"),
        (result.line_features, "line features"),
        (result.point_features, "point features"),
    ):
        if not isinstance(frame, gpd.GeoDataFrame):
            raise BessPlanningFeatureApplicationError(f"{label} must be geospatial")
        if frame.columns.duplicated().any():
            raise BessPlanningFeatureApplicationError(
                f"{label} policy schema is invalid"
            )
        deterministic_frame_schema_signature(frame)
    try:
        feature_mapping = validate_bess_application_feature_catalogs(
            result.surface_features,
            result.line_features,
            result.point_features,
            policy_profile=result.policy_profile,
            policy_sha256=result.policy_sha256,
            policy_result_sha256=result.policy_complete_result_content_sha256,
            source_document_id=result.source_document_id,
            source_archive_sha256=result.source_archive_sha256,
            cnig_profile=result.cnig_profile,
            cnig_profile_sha256=result.cnig_profile_sha256,
        )
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureApplicationError(str(error)) from error
    if not isinstance(result.relations, pd.DataFrame) or isinstance(
        result.relations, gpd.GeoDataFrame
    ):
        raise BessPlanningFeatureApplicationError("relations must be a DataFrame")
    if result.relations.columns.duplicated().any():
        raise BessPlanningFeatureApplicationError("relations policy schema is invalid")
    relation_mapping = _validate_relation_rows(result.relations, "relations", result)
    if any(
        feature_mapping[0].get(priority) != status
        for priority, status in relation_mapping[0].items()
    ) or any(
        feature_mapping[1].get(status) != priority
        for status, priority in relation_mapping[1].items()
    ):
        raise BessPlanningFeatureApplicationError(
            "relation policy mapping differs from the feature mapping"
        )
    feature_rows = _feature_rows_by_id(
        result.surface_features, result.line_features, result.point_features
    )
    for relation in result.relations.to_dict("records"):
        feature = feature_rows.get(str(relation["planning_feature_id"]))
        if feature is None:
            raise BessPlanningFeatureApplicationError(
                "Application relation references an unknown feature"
            )
        for column in (*RELATION_FEATURE_AGREEMENT_COLUMNS, *POLICY_COLUMNS):
            if not _null_safe_equal(relation[column], feature[column]):
                raise BessPlanningFeatureApplicationError(
                    f"Application relation {column} differs from its feature"
                )
        kind = relation["geometry_kind"]
        relation_metric, feature_metric = {
            "SURFACE": ("feature_area_m2", "feature_area_m2"),
            "LINE": ("source_line_length_m", "feature_length_m"),
            "POINT": ("point_member_count", "point_member_count"),
        }[kind]
        if kind == "POINT":
            metric_equal = _null_safe_equal(
                relation[relation_metric], feature[feature_metric]
            )
        else:
            actual_value = relation[relation_metric]
            expected_value = feature[feature_metric]
            if (
                isinstance(actual_value, bool)
                or not isinstance(actual_value, Real)
                or isinstance(expected_value, bool)
                or not isinstance(expected_value, Real)
            ):
                raise BessPlanningFeatureApplicationError(
                    "Application relation feature metric is not numeric"
                )
            actual = float(actual_value)
            expected = float(expected_value)
            metric_equal = abs(actual - expected) <= technical_overlay_tolerance(
                max(abs(actual), abs(expected))
            )
        if not metric_equal:
            raise BessPlanningFeatureApplicationError(
                "Application relation feature metric differs from its feature"
            )
    for field in RESULT_SCALAR_FIELDS:
        if field.endswith("sha256"):
            try:
                _sha256_string(getattr(result, field), field)
            except ValueError as error:
                raise BessPlanningFeatureApplicationError(str(error)) from error
    rebuilt = _result_with_hashes(result)
    for field in (
        "surface_features_content_sha256",
        "line_features_content_sha256",
        "point_features_content_sha256",
        "relations_content_sha256",
        "complete_result_content_sha256",
    ):
        if getattr(result, field) != getattr(rebuilt, field):
            raise BessPlanningFeatureApplicationError(f"{field} is invalid")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_bess_planning_feature_application_result_envelope`

**Exact signature**

```python
def validate_bess_planning_feature_application_result_envelope(
    result: BessPlanningFeatureApplicationResult,
) -> None:
```

**Purpose**

Validate one application envelope without reconstructing source inputs.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `validate_bess_planning_feature_application_result_envelope`.
- import/re-export: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationResult,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams` via `module.validate_bess_planning_feature_application_result_envelope`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams` via `module.validate_bess_planning_feature_application_result_envelope`.

**Complete source-ordered implementation**

```python
def validate_bess_planning_feature_application_result_envelope(
    result: BessPlanningFeatureApplicationResult,
) -> None:
    """Validate one application envelope without reconstructing source inputs."""

    _validate_result_envelope(result)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_coded_policy_compatibility`

**Exact signature**

```python
def _validate_coded_policy_compatibility(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent coded policy compatibility; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not coded_rows or not policy_rows`.
- Guard with a raise path: `set(policy_rows) != set(coded_rows)`.
- Guard with a raise path: `actual != expected`.
- Guard with a raise path: `any((not _null_safe_equal(actual, expected) for actual, expected in meaning_comparisons))`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError('Policy and code dictionary pair sets differ')`, `BessPlanningFeatureApplicationError('Policy and code dictionary pair sets must be non-empty')`, `BessPlanningFeatureApplicationError(f'Policy and coded result differ for {label}')`, `BessPlanningFeatureApplicationError(f'Policy official meaning differs from code dictionary for pair {key}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `_validate_coded_policy_compatibility`.

**Complete source-ordered implementation**

```python
def _validate_coded_policy_compatibility(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
    comparisons = (
        (policy.source_document_id, coded.source_document_id, "document ID"),
        (policy.source_archive_sha256, coded.source_archive_sha256, "archive SHA256"),
        (policy.cnig_profile, coded.profile, "CNIG profile"),
        (
            policy.cnig_profile_schema_version,
            coded.profile_schema_version,
            "CNIG profile schema",
        ),
        (policy.cnig_profile_sha256, coded.profile_sha256, "CNIG profile SHA256"),
        (
            policy.cnig_result_hash_schema_version,
            coded.result_hash_schema_version,
            "CNIG result hash schema",
        ),
        (
            policy.cnig_complete_result_content_sha256,
            coded.complete_result_content_sha256,
            "CNIG complete result SHA256",
        ),
    )
    for actual, expected, label in comparisons:
        if actual != expected:
            raise BessPlanningFeatureApplicationError(
                f"Policy and coded result differ for {label}"
            )
    coded_rows = {
        (row["feature_family"], row["type_code"], row["subtype_code"]): row
        for row in coded.code_dictionary.to_dict("records")
    }
    policy_rows = {
        (row["feature_family"], row["type_code"], row["subtype_code"]): row
        for row in policy.policy_table.to_dict("records")
    }
    if not coded_rows or not policy_rows:
        raise BessPlanningFeatureApplicationError(
            "Policy and code dictionary pair sets must be non-empty"
        )
    if set(policy_rows) != set(coded_rows):
        raise BessPlanningFeatureApplicationError(
            "Policy and code dictionary pair sets differ"
        )
    for key, coded_row in coded_rows.items():
        policy_row = policy_rows[key]
        meaning_comparisons = (
            (policy_row["official_label"], coded_row["official_label"]),
            (
                policy_row["official_legal_reference"],
                coded_row["legal_reference"],
            ),
            (
                policy_row["official_regulation_reference"],
                coded_row["regulation_or_annex_reference"],
            ),
        )
        if any(
            not _null_safe_equal(actual, expected)
            for actual, expected in meaning_comparisons
        ):
            raise BessPlanningFeatureApplicationError(
                f"Policy official meaning differs from code dictionary for pair {key}"
            )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_source_locks`

**Exact signature**

```python
def _validate_source_locks(
    result: BessPlanningFeatureApplicationResult
    | BessPlanningFeatureApplicationArtifactManifest,
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
```

**Purpose**

Rejects malformed or inconsistent source locks; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `actual != expected`.
- Guard with a raise path: `actual != expected`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError(f'Application source lock differs for {label}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `_validate_source_locks`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `_validate_source_locks`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `_validate_source_locks`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `_validate_source_locks`.

**Complete source-ordered implementation**

```python
def _validate_source_locks(
    result: BessPlanningFeatureApplicationResult
    | BessPlanningFeatureApplicationArtifactManifest,
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
    comparisons = (
        (result.policy_profile, policy.policy_profile, "policy profile"),
        (result.policy_sha256, policy.policy_sha256, "policy SHA256"),
        (
            result.policy_result_hash_schema_version,
            policy.result_hash_schema_version,
            "policy result hash schema",
        ),
        (
            result.policy_complete_result_content_sha256,
            policy.complete_result_content_sha256,
            "policy result SHA256",
        ),
        (result.cnig_profile, coded.profile, "CNIG profile"),
        (result.cnig_profile_sha256, coded.profile_sha256, "CNIG profile SHA256"),
        (
            result.cnig_result_hash_schema_version,
            coded.result_hash_schema_version,
            "CNIG result hash schema",
        ),
        (
            result.cnig_complete_result_content_sha256,
            coded.complete_result_content_sha256,
            "CNIG result SHA256",
        ),
        (result.source_document_id, coded.source_document_id, "document ID"),
        (result.source_archive_sha256, coded.source_archive_sha256, "archive SHA256"),
        (
            result.cnig_surface_features_content_sha256,
            coded.surface_features_content_sha256,
            "coded surface SHA256",
        ),
        (
            result.cnig_line_features_content_sha256,
            coded.line_features_content_sha256,
            "coded line SHA256",
        ),
        (
            result.cnig_point_features_content_sha256,
            coded.point_features_content_sha256,
            "coded point SHA256",
        ),
        (
            result.cnig_relations_content_sha256,
            coded.relations_content_sha256,
            "coded relations SHA256",
        ),
    )
    for actual, expected, label in comparisons:
        if actual != expected:
            raise BessPlanningFeatureApplicationError(
                f"Application source lock differs for {label}"
            )

    policy_coded_comparisons = (
        (policy.source_document_id, coded.source_document_id, "policy document ID"),
        (
            policy.source_archive_sha256,
            coded.source_archive_sha256,
            "policy archive SHA256",
        ),
        (policy.cnig_profile, coded.profile, "policy CNIG profile"),
        (
            policy.cnig_profile_schema_version,
            coded.profile_schema_version,
            "policy CNIG profile schema",
        ),
        (
            policy.cnig_profile_sha256,
            coded.profile_sha256,
            "policy CNIG profile SHA256",
        ),
        (
            policy.cnig_result_hash_schema_version,
            coded.result_hash_schema_version,
            "policy CNIG result hash schema",
        ),
        (
            policy.cnig_complete_result_content_sha256,
            coded.complete_result_content_sha256,
            "policy CNIG result SHA256",
        ),
    )
    for actual, expected, label in policy_coded_comparisons:
        if actual != expected:
            raise BessPlanningFeatureApplicationError(
                f"Application source lock differs for {label}"
            )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_policy_source`

**Exact signature**

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

Rejects malformed or inconsistent policy source; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessPlanningFeatureApplicationError('Source-complete BESS planning-feature policy validation failed')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::apply_bess_planning_feature_policy` via `_validate_policy_source`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `_validate_policy_source`.

**Complete source-ordered implementation**

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
    try:
        validate_bess_planning_feature_policy_result(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
            policy_config,
            policy_result,
        )
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            "Source-complete BESS planning-feature policy validation failed"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `apply_bess_planning_feature_policy`

**Exact signature**

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

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `BessPlanningFeatureApplicationError('BESS planning-feature policy application failed safely')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::_application_fixture` via `apply_bess_planning_feature_policy`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_feature_and_relation_inputs_are_preserved_and_not_mutated` via `apply_bess_planning_feature_policy`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `module.apply_bess_planning_feature_policy`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `module.apply_bess_planning_feature_policy`.
- import/re-export: `tests/unit/test_apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)`.

**Complete source-ordered implementation**

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
    """Validate once, then propagate exact compiled policy to features and relations."""

    try:
        _validate_policy_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
            policy_config,
            policy_result,
        )
        result = _build_result(coded_result, policy_result)
        _validate_result_envelope(result)
        return result
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            "BESS planning-feature policy application failed safely"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_compare_frame`

**Exact signature**

```python
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
```

**Purpose**

Private `planning` helper for compare frame; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `_frame_payload(actual) != _frame_payload(expected)`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError(f'Application {label} differs from rebuilt result')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_result_envelope` via `_compare_frame`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `_compare_frame`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `_compare_frame`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `_compare_frame`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `_compare_frame`.
- direct call or construction: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `_compare_frame`.

**Complete source-ordered implementation**

```python
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _frame_payload(actual) != _frame_payload(expected):
        raise BessPlanningFeatureApplicationError(
            f"Application {label} differs from rebuilt result"
        )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_bess_planning_feature_application_result`

**Exact signature**

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

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `getattr(result, field) != getattr(expected, field)`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError('BESS planning-feature application result validation failed safely')`, `BessPlanningFeatureApplicationError(f'Application {field} differs from rebuilt result')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`.
- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_application_source` via `validate_bess_planning_feature_application_result`.
- import/re-export: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationResult,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::test_one_aggregation_and_one_public_validation_each_call_heavy_once` via `module.validate_bess_planning_feature_application_result`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `module.validate_bess_planning_feature_application_result`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_every_non_2d_application_geometry_kind_fast_fails_before_source_validation` via `module.validate_bess_planning_feature_application_result`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_feature_or_relation_policy_mutation_is_rejected` via `validate_bess_planning_feature_application_result`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `module.validate_bess_planning_feature_application_result`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_and_public_validator_heavy_validation_counts` via `module.validate_bess_planning_feature_application_result`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `module.validate_bess_planning_feature_application_result`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_malformed_local_result_fast_fails_before_heavy_validation` via `module.validate_bess_planning_feature_application_result`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `module.validate_bess_planning_feature_application_result`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_coordinated_application_source_lock_mutation_fast_fails` via `module.validate_bess_planning_feature_application_result`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_four_file_manifest_and_verified_byte_readback` via `validate_bess_planning_feature_application_result`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `module.validate_bess_planning_feature_application_result`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_identity_fast_fails_before_policy_source_validation` via `module.validate_bess_planning_feature_application_result`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_lineage_defect_fast_fails_before_policy_source_validation` via `validate_bess_planning_feature_application_result`.
- import/re-export: `tests/unit/test_apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    validate_bess_planning_feature_application_result,
)`.

**Complete source-ordered implementation**

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
    """Independently rebuild exact policy propagation from every source input."""

    try:
        _validate_result_envelope(result)
        _validate_source_locks(result, coded_result, policy_result)
        _validate_policy_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
            policy_config,
            policy_result,
        )
        expected = _build_result(coded_result, policy_result)
        for field in RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeatureApplicationError(
                    f"Application {field} differs from rebuilt result"
                )
        for actual, rebuilt, label in (
            (result.surface_features, expected.surface_features, "surface features"),
            (result.line_features, expected.line_features, "line features"),
            (result.point_features, expected.point_features, "point features"),
            (result.relations, expected.relations, "relations"),
        ):
            _compare_frame(actual, rebuilt, label)
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            "BESS planning-feature application result validation failed safely"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_unique_json_object`

**Exact signature**

```python
def _unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for unique json object; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
output
```

**Validation and exceptions**

- Guard with a raise path: `key in output`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError(f'Duplicate JSON application artifact key: {key!r}')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: none directly visible.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: `output[key]`.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- callback/function object: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `json.loads(Path(manifest_path).read_text(encoding='utf-8'), object_pairs_hook=_unique_json_object)`.
- callback/function object: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `json.loads(Path(manifest_path).read_text(encoding='utf-8'), object_pairs_hook=_unique_json_object)`.
- callback/function object: `src/landscout/stages/bess_planning_feature_policy.py::load_bess_planning_feature_policy_artifacts` via `json.loads(manifest_file.read_text(encoding='utf-8'), object_pairs_hook=_unique_json_object)`.
- callback/property argument: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `json.loads(Path(manifest_path).read_text(encoding='utf-8'), object_pairs_hook=module._unique_json_object)`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `module._unique_json_object`.

**Complete source-ordered implementation**

```python
def _unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise BessPlanningFeatureApplicationError(
                f"Duplicate JSON application artifact key: {key!r}"
            )
        output[key] = value
    return output
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_read_verified_artifact`

**Exact signature**

```python
def _read_verified_artifact(
    path: Path,
    record: BessPlanningFeatureApplicationArtifactRecord,
) -> pd.DataFrame:
```

**Purpose**

Reads verified artifact; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame
```

**Validation and exceptions**

- Guard with a raise path: `path.name != record.filename`.
- Guard with a raise path: `len(payload) != record.size_bytes`.
- Guard with a raise path: `sha256(payload).hexdigest() != record.sha256`.
- Guard with a raise path: `len(frame) != record.row_count`.
- Guard with a raise path: `signature != record.frame_schema_signature`.
- Guard with a raise path: `record.geospatial`.
- Guard with a raise path: `not isinstance(frame, gpd.GeoDataFrame) or frame.crs is None`.
- Guard with a raise path: `CRS.from_user_input(frame.crs).to_json_dict() != record.crs`.
- Guard with a raise path: `isinstance(frame, gpd.GeoDataFrame)`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError('Relations artifact unexpectedly loaded as geospatial')`, `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} CRS differs')`, `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} SHA256 differs')`, `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} byte size differs')`, `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} filename differs')`, `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} frame schema differs')`, `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} geospatial contract differs')`, `BessPlanningFeatureApplicationError(f'Artifact {record.artifact_role} row count differs')`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `gpd.read_parquet`, `path.read_bytes`, `pd.read_parquet`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: `sha256`, `sha256(payload).hexdigest`.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- direct call or construction: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::load_bess_planning_feature_parcel_aggregation_artifacts` via `_read_verified_artifact`.
- direct call or construction: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `_read_verified_artifact`.
- direct call or construction: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `module._read_verified_artifact`.
- property/attribute access: `tests/unit/test_aggregate_bess_planning_feature_policy.py::_load_legacy_local_aggregation_artifacts` via `module._read_verified_artifact`.

**Complete source-ordered implementation**

```python
def _read_verified_artifact(
    path: Path,
    record: BessPlanningFeatureApplicationArtifactRecord,
) -> pd.DataFrame:
    if path.name != record.filename:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} filename differs"
        )
    payload = path.read_bytes()
    if len(payload) != record.size_bytes:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} byte size differs"
        )
    if sha256(payload).hexdigest() != record.sha256:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} SHA256 differs"
        )
    buffer = BytesIO(payload)
    frame: pd.DataFrame
    if record.geospatial:
        frame = gpd.read_parquet(buffer)
    else:
        frame = pd.read_parquet(buffer)
    if len(frame) != record.row_count:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} row count differs"
        )
    signature = deterministic_frame_schema_signature(frame)
    if signature != record.frame_schema_signature:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} frame schema differs"
        )
    if record.geospatial:
        if not isinstance(frame, gpd.GeoDataFrame) or frame.crs is None:
            raise BessPlanningFeatureApplicationError(
                f"Artifact {record.artifact_role} geospatial contract differs"
            )
        if CRS.from_user_input(frame.crs).to_json_dict() != record.crs:
            raise BessPlanningFeatureApplicationError(
                f"Artifact {record.artifact_role} CRS differs"
            )
    elif isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureApplicationError(
            "Relations artifact unexpectedly loaded as geospatial"
        )
    return frame
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_bess_planning_feature_application_artifacts`

**Exact signature**

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

**Return contract**

- Declared return annotation: `BessPlanningFeatureApplicationResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `getattr(result, field) != getattr(expected, field)`.
- Explicit raise expressions: `BessPlanningFeatureApplicationError(f'Application artifact scalar {field} differs from upstream rebuild')`, `BessPlanningFeatureApplicationError(f'BESS planning-feature application artifacts are invalid: {error}')`, `re-raise`.

**Side effects**

- Network I/O: none directly visible.
- Filesystem read: `Path(manifest_path).read_text`.
- Filesystem write: none directly visible.
- CRS/geometry calculation: none directly visible.
- Hashing: none directly visible.
- Environment/process effects: none directly visible.
- In-memory mutation: none directly visible.
- Input mutation: none detected; copy/preservation behavior is shown in the implementation.

**Repository interfaces and consumers**

- import/re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationArtifactManifest,
    BessPlanningFeatureApplicationError,
    BessPlanningFeatureApplicationResult,
    apply_bess_planning_feature_policy,
    load_bess_planning_feature_application_artifacts,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_valid_four_file_manifest_and_verified_byte_readback` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_duplicate_relation_pair_artifact_fails_local_loading` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_document_wide_mapping_conflict_artifact_fails_local_loading` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_positive_surface_overlap_cannot_be_relabelled_touch_only_in_artifact` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_wrong_2d_feature_geometry_fails_local_artifact_loading` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_identity_is_validated_locally` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_participates_in_global_policy_mapping` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_z_geoparquet_artifact_is_rejected` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_wrong_dtype_artifact_is_rejected` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_manifest_rejects_invalid_contract` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_manifest_rejects_duplicate_json_key` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_artifact_loader_parses_only_verified_bytes` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_physical_replacement_before_loading_is_rejected` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_unreferenced_feature_document_lineage_is_bound_to_envelope_artifact` via `load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_self_consistent_factual_prefix_dtype_artifact_is_rejected` via `load_bess_planning_feature_application_artifacts`.
- callback/property argument: `tests/unit/test_apply_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams` via `inspect.signature(module.load_bess_planning_feature_application_artifacts)`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_step_7d_5b_2b_5_application_loader_requires_exact_upstreams` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_application_loader_rejects_locally_valid_rationale_change` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_valid_domain_cross_pair_swaps` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_factual_prefix_lineage_change` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_all_null_raw_column_transition` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_source_bound_loader_rejects_unreferenced_feature_and_row_reordering` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_validates_upstreams_and_rebuilds_once_lightweight` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_incompatible_upstreams_before_io_or_rebuild` via `module.load_bess_planning_feature_application_artifacts`.
- direct call or construction: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `module.load_bess_planning_feature_application_artifacts`.
- property/attribute access: `tests/unit/test_apply_bess_planning_feature_policy.py::test_application_loader_rejects_empty_upstreams_before_any_io_or_rebuild` via `module.load_bess_planning_feature_application_artifacts`.
- import/re-export: `tests/unit/test_apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.apply_bess_planning_feature_policy import (
    load_bess_planning_feature_application_artifacts as _load_application_artifacts,
)`.

**Complete source-ordered implementation**

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
    """Load byte-sealed outputs and bind them to exact validated upstream results."""

    try:
        validate_planning_feature_code_result_envelope(coded_result)
        validate_bess_planning_feature_policy_result_envelope(policy_result)
        _validate_coded_policy_compatibility(coded_result, policy_result)
        payload = json.loads(
            Path(manifest_path).read_text(encoding="utf-8"),
            object_pairs_hook=_unique_json_object,
        )
        manifest = BessPlanningFeatureApplicationArtifactManifest.model_validate(
            payload
        )
        _validate_source_locks(manifest, coded_result, policy_result)
        paths = {
            "SURFACE_FEATURES": Path(surface_features_path),
            "LINE_FEATURES": Path(line_features_path),
            "POINT_FEATURES": Path(point_features_path),
            "RELATIONS": Path(relations_path),
        }
        records = {record.artifact_role: record for record in manifest.artifacts}
        loaded = {
            role: _read_verified_artifact(paths[role], records[role])
            for role in ARTIFACT_ROLES
        }
        result = BessPlanningFeatureApplicationResult(
            **{field: getattr(manifest, field) for field in RESULT_SCALAR_FIELDS},
            surface_features=loaded["SURFACE_FEATURES"],
            line_features=loaded["LINE_FEATURES"],
            point_features=loaded["POINT_FEATURES"],
            relations=loaded["RELATIONS"],
        )
        _validate_result_envelope(result)
        expected = _build_result(coded_result, policy_result)
        for field in RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeatureApplicationError(
                    f"Application artifact scalar {field} differs from upstream rebuild"
                )
        for field in RESULT_FRAME_FIELDS:
            _compare_frame(
                getattr(result, field),
                getattr(expected, field),
                f"artifact {field}",
            )
        return result
    except BessPlanningFeatureApplicationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureApplicationError(
            f"BESS planning-feature application artifacts are invalid: {error}"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


## 7. Data contracts

### `RELATION_FEATURE_AGREEMENT_COLUMNS` — canonical or derived frame-column schema

```python
RELATION_FEATURE_AGREEMENT_COLUMNS = (
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
    "official_code_status",
    "official_code_label",
    "official_legal_reference",
    "official_regulation_reference",
    "official_code_source_url",
    "official_code_profile",
    "official_code_profile_sha256",
)
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `source_feature_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 2 | `source_identity_kind` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 3 | `source_identity_field` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 4 | `logical_layer` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `feature_family` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `geometry_kind` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `type_code_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 8 | `subtype_code_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 9 | `label_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 10 | `text_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 11 | `source_document_id` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 12 | `source_archive_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 13 | `source_layer` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 14 | `source_validity_date_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 15 | `regulation_filename_raw` | source-preserved/dynamic Pandas dtype (the normalizer copies the source Series without casting) | source nulls are preserved unless an explicit identity guard rejects them | source fact | Copied source value; no semantic interpretation is implied by normalization. |
| 16 | `official_code_status` | builder/source string dtype shown by the implementation | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 17 | `official_code_label` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 18 | `official_legal_reference` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 19 | `official_regulation_reference` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 20 | `official_code_source_url` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 21 | `official_code_profile` | source-preserved or builder-dependent dtype; this schema declaration fixes presence/order but performs no cast | source/build nullability; this presence/order declaration itself does not cast or add a null constraint | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 22 | `official_code_profile_sha256` | source/build string dtype (no cast is imposed by this declaration) | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `BessPlanningFeatureApplicationArtifactManifest` | re-exported/defined Python symbol | `defined in `src/landscout/stages/apply_bess_planning_feature_policy.py`` | yes |
| `BessPlanningFeatureApplicationError` | re-exported/defined Python symbol | `defined in `src/landscout/stages/apply_bess_planning_feature_policy.py`` | yes |
| `BessPlanningFeatureApplicationResult` | re-exported/defined Python symbol | `defined in `src/landscout/stages/apply_bess_planning_feature_policy.py`` | yes |
| `apply_bess_planning_feature_policy` | re-exported/defined Python symbol | `defined in `src/landscout/stages/apply_bess_planning_feature_policy.py`` | yes |
| `load_bess_planning_feature_application_artifacts` | re-exported/defined Python symbol | `defined in `src/landscout/stages/apply_bess_planning_feature_policy.py`` | yes |
| `validate_bess_planning_feature_application_result` | re-exported/defined Python symbol | `defined in `src/landscout/stages/apply_bess_planning_feature_policy.py`` | yes |
| `validate_bess_planning_feature_application_result_envelope` | re-exported/defined Python symbol | `defined in `src/landscout/stages/apply_bess_planning_feature_policy.py`` | yes |

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
