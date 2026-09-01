# `src/landscout/stages/resolve_planning_feature_codes.py`

## File identity

- Repository path: `src/landscout/stages/resolve_planning_feature_codes.py`
- File type: Python source
- Layer: pipeline stage
- Domain: factual transformation, evidence, or policy boundary
- Responsibility: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.
- Source SHA256: `cdb463f06cea6f58881681bca7e95e80b0770e69f4cdf3cc373329eca7bc0235`

## 1. STEP 7F.1A.4 contract delta

- Uses strict duplicate-safe CNIG profile YAML, frozen/deeply immutable decision inputs, and controlled public-envelope revalidation.
- This delta is validation/source-authority/API hardening unless the exact source below says otherwise; no undocumented schema or business-semantic change is inferred.

## 2. Purpose and architectural position

Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

The file belongs to the **pipeline stage** layer and **factual transformation, evidence, or policy boundary** domain. Its authority is limited to the declarations, exact qualified relationships, validation paths, and side effects reproduced below.

## 3. Imports and dependencies

### Python 3.12 standard library

- `from __future__ import annotations`
- `import json`
- `import math`
- `import re`
- `import unicodedata`
- `from collections.abc import Mapping, Sequence`
- `from dataclasses import asdict, dataclass, replace`
- `from datetime import date, datetime`
- `from hashlib import sha256`
- `from numbers import Integral, Real`
- `from pathlib import Path`
- `from typing import Literal, cast`

### Third-party packages

- `import geopandas as gpd`
- `import numpy as np`
- `import pandas as pd`
- `from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, model_validator`
- `from shapely import to_wkb`
- `from shapely.geometry.base import BaseGeometry`

### Internal LandScout imports

- `from landscout.common.frame_integrity import deterministic_frame_schema_signature`
- `from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)`
- `from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml`
- `from landscout.sources.gpu_fr import GpuInspectedLayer, GpuPlanningDocument`
- `from landscout.stages.enrich_planning_features import (
    PlanningFeatureInputValidation,
    validate_normalized_planning_feature_inputs,
)`

## 4. Contract taxonomy

Module constants, type aliases, canonical schema/mapping declarations, dunders, and exports are kept separate from model fields, mapping keys, JSON keys, and frame columns. A string literal is never called a frame column unless its owning declaration establishes that role.

### `__all__`

- Category: explicit package/module export list.
- Exact declaration:

```python
__all__ = [
    "CnigFeatureCodeProfile",
    "PlanningFeatureCodeError",
    "PlanningFeatureCodeResult",
    "load_cnig_feature_code_profile",
    "resolve_planning_feature_codes",
    "validate_planning_feature_code_result",
    "validate_planning_feature_code_result_envelope",
]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `CnigFeatureCodeProfile`
  - `PlanningFeatureCodeError`
  - `PlanningFeatureCodeResult`
  - `load_cnig_feature_code_profile`
  - `resolve_planning_feature_codes`
  - `validate_planning_feature_code_result`
  - `validate_planning_feature_code_result_envelope`

### `PROFILE_SCHEMA_VERSION`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
PROFILE_SCHEMA_VERSION = 2
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

### `STANDARD_MODEL`

- Category: module constant or closed domain.
- Exact declaration:

```python
STANDARD_MODEL = "CNIG PLU v2017"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `OFFICIAL_TEXT_NORMALIZATION`

- Category: module constant or closed domain.
- Exact declaration:

```python
OFFICIAL_TEXT_NORMALIZATION = "GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `PRESCRIPTION_OFFICIAL_SOURCE_URL`

- Category: module constant or closed domain.
- Exact declaration:

```python
PRESCRIPTION_OFFICIAL_SOURCE_URL = (
    "https://www.geoportail-urbanisme.gouv.fr/standard/"
    "cnig_PLU_2017/codes/PrescriptionUrbaType"
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `INFORMATION_OFFICIAL_SOURCE_URL`

- Category: module constant or closed domain.
- Exact declaration:

```python
INFORMATION_OFFICIAL_SOURCE_URL = (
    "https://www.geoportail-urbanisme.gouv.fr/standard/"
    "cnig_PLU_2017/codes/InformationUrbaType"
)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `FeatureFamily`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `OfficialCodeStatus`

- Category: type alias or closed annotated domain.
- Exact declaration:

```python
OfficialCodeStatus = Literal["RESOLVED_OFFICIAL", "UNKNOWN_CODE_PAIR"]
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CODE_DICTIONARY_COLUMNS`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
CODE_DICTIONARY_COLUMNS = (
    "feature_family",
    "type_code",
    "subtype_code",
    "official_label",
    "legal_reference",
    "regulation_or_annex_reference",
    "official_source_url",
    "profile",
    "profile_sha256",
    "standard_model",
)
```

- Qualified consumers:
  - import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`
  - value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_catalogs_and_relations_are_preserved_and_inputs_immutable` via `CODE_DICTIONARY_COLUMNS`
- Exact ordered/literal string members (these are not classified as DataFrame columns unless the declaration category above says schema):
  - `feature_family`
  - `type_code`
  - `subtype_code`
  - `official_label`
  - `legal_reference`
  - `regulation_or_annex_reference`
  - `official_source_url`
  - `profile`
  - `profile_sha256`
  - `standard_model`

### `CODE_DICTIONARY_DTYPES`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
CODE_DICTIONARY_DTYPES = tuple("str" for _ in CODE_DICTIONARY_COLUMNS)
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `CODE_DICTIONARY_SCHEMA_SIGNATURE`

- Category: canonical schema/mapping declaration.
- Exact declaration:

```python
CODE_DICTIONARY_SCHEMA_SIGNATURE: dict[str, object] = {
    "columns": list(CODE_DICTIONARY_COLUMNS),
    "dtypes": list(CODE_DICTIONARY_DTYPES),
    "index_class": "pandas.Index",
    "index_names": [None],
    "index_level_dtypes": ["int64"],
}
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_CODE_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
_CODE_PATTERN = re.compile(r"[0-9]{2}")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_SHA_PATTERN`

- Category: module constant or closed domain.
- Exact declaration:

```python
_SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.

### `_NULL_REFERENCE_LITERALS`

- Category: module constant or closed domain.
- Exact declaration:

```python
_NULL_REFERENCE_LITERALS = frozenset({"None", "nan", "<NA>"})
```

- Qualified consumers:
  - No conservative direct import/call/value reference was found outside the declaration.


### Executable module-import-time statements

No executable module-import-time statement is declared outside imports, assignments, and definitions.

## 5. Classes, models, dataclasses, and fields

### `PlanningFeatureCodeError`

**Source purpose:** Raised when official code resolution integrity cannot be proven.

- Exact decorators: none.
- Exact bases: `ValueError`.

**Fields and model attributes**

No direct class/model/dataclass or `self` field assignment is declared.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_canonical_json_sha256` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_canonical_json_sha256` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::load_cnig_feature_code_profile` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::load_cnig_feature_code_profile` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_resolved_profile` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_resolved_profile` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_strict_string` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_strict_string` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_planning_standard` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_planning_standard` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_validated_code_series` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validated_code_series` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_validate_nullable_official_value` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_nullable_official_value` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_validate_code_dictionary` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_code_dictionary` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_validate_coded_meaning_rows` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_coded_meaning_rows` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_validate_catalog_document_lineage` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_catalog_document_lineage` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_catalog_by_id` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_catalog_by_id` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_coded_relations` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_coded_relations` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_canonical_value` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_canonical_value` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_inspected_layer_payload` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_inspected_layer_payload` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_planning_document_context_sha256` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_planning_document_context_sha256` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_parcel_identity_input_sha256` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_parcel_identity_input_sha256` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result_envelope` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result_envelope` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_compare_frame` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_compare_frame` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `PlanningFeatureCodeError`
- constructor call: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `PlanningFeatureCodeError`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `PlanningFeatureCodeError`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_yaml_key_is_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_wrong_planning_standard_is_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_complete_normalized_catalog_schema_is_required` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_unexpected_factual_catalog_column_is_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_cnig_identity_provenance_is_exact` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_ogr_fid_provenance_is_restricted` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_source_feature_id_is_unique_inside_logical_layer` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_catalog_crs_must_be_canonical_epsg_2154` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_catalog_geometry_metrics_are_revalidated` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_complete_relation_schema_is_required` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_unexpected_factual_relation_column_is_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_cnig_resolver_invokes_shared_factual_contract` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_complete_relation_catalog_agreement_is_required` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_surface_relation_metrics_are_revalidated` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_line_relation_metrics_are_revalidated` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_catalog_columns_are_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_missing_catalog_crs_is_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_unparseable_catalog_crs_is_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_inactive_or_wrong_geometry_column_is_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_surface_geometry_contract_is_enforced` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_catalog_semantic_and_string_contracts_are_enforced` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_every_required_catalog_identity_is_an_exact_non_null_string` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_line_and_point_geometry_types_are_enforced` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_planning_feature_ids_are_globally_unique_across_catalogs` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_relation_catalog_code_mismatch_is_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_relation_columns_are_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_relation_identity_must_be_an_exact_non_null_string` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_parcel_feature_relation_is_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_unknown_relation_feature_id_is_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_relation_type_must_match_catalog_geometry_kind` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_coordinated_output_hash_mutation_is_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_result_schema_versions_are_strict` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_source_input_hash_mutation_is_rejected` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_parcel_source_change_invalidates_coded_result` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_gpu_document_context_change_invalidates_coded_result` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_normalized_relation_change_invalidates_coded_result` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_coding_api_rejects_relation_set_not_rebuilt_from_geometry` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_rejects_canonical_empty_code_dictionary` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_controls_malformed_dictionary_type` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_rejects_geospatial_code_dictionary` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_dictionary_schema_is_explicit` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_dictionary_rows_are_intrinsically_validated` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_scalar_lineage_contracts_are_intrinsic` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic` via `PlanningFeatureCodeError`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result` via `PlanningFeatureCodeError`

**Exact class source**

```python
class PlanningFeatureCodeError(ValueError):
    """Raised when official code resolution integrity cannot be proven."""
```

### `_StrictModel`

**Source purpose:** Defines `_StrictModel`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

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
class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `OfficialSourceUrls`

**Source purpose:** Defines `OfficialSourceUrls`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `prescription` | `StrictStr` | `required` | `prescription: StrictStr` |
| `information` | `StrictStr` | `required` | `information: StrictStr` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.resolve_planning_feature_codes::OfficialSourceUrls._validate_urls` via `OfficialSourceUrls`

**Exact class source**

```python
class OfficialSourceUrls(_StrictModel):
    prescription: StrictStr
    information: StrictStr

    @model_validator(mode="after")
    def _validate_urls(self) -> OfficialSourceUrls:
        if self.prescription != PRESCRIPTION_OFFICIAL_SOURCE_URL:
            raise ValueError(
                "prescription source URL is not the exact official GPU host endpoint"
            )
        if self.information != INFORMATION_OFFICIAL_SOURCE_URL:
            raise ValueError(
                "information source URL is not the exact official GPU host endpoint"
            )
        return self
```

### `CnigFeatureCodeRecord`

**Source purpose:** Defines `CnigFeatureCodeRecord`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `feature_family` | `FeatureFamily` | `required` | `feature_family: FeatureFamily` |
| `type_code` | `StrictStr` | `required` | `type_code: StrictStr` |
| `subtype_code` | `StrictStr` | `required` | `subtype_code: StrictStr` |
| `official_label` | `StrictStr` | `required` | `official_label: StrictStr` |
| `legal_reference` | `StrictStr \| None` | `required` | `legal_reference: StrictStr \| None` |
| `regulation_or_annex_reference` | `StrictStr \| None` | `required` | `regulation_or_annex_reference: StrictStr \| None` |
| `official_source_url` | `StrictStr` | `required` | `official_source_url: StrictStr` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.resolve_planning_feature_codes::CnigFeatureCodeRecord._validate_record` via `CnigFeatureCodeRecord`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_record_payload` via `CnigFeatureCodeRecord`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_records_sha256` via `CnigFeatureCodeRecord`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_lookup` via `CnigFeatureCodeRecord`

**Exact class source**

```python
class CnigFeatureCodeRecord(_StrictModel):
    feature_family: FeatureFamily
    type_code: StrictStr
    subtype_code: StrictStr
    official_label: StrictStr
    legal_reference: StrictStr | None
    regulation_or_annex_reference: StrictStr | None
    official_source_url: StrictStr

    @model_validator(mode="after")
    def _validate_record(self) -> CnigFeatureCodeRecord:
        for code, label in (
            (self.type_code, "type code"),
            (self.subtype_code, "subtype code"),
        ):
            if _CODE_PATTERN.fullmatch(code) is None:
                raise ValueError(f"{label} must contain exactly two digits")
        _validate_official_text(self.official_label, "official label")
        _validate_optional_official_text(self.legal_reference, "legal reference")
        _validate_optional_official_text(
            self.regulation_or_annex_reference,
            "regulation or annex reference",
        )
        expected_url = (
            PRESCRIPTION_OFFICIAL_SOURCE_URL
            if self.feature_family == "PRESCRIPTION"
            else INFORMATION_OFFICIAL_SOURCE_URL
        )
        if self.official_source_url != expected_url:
            raise ValueError("record source URL is not the exact family endpoint")
        return self
```

### `CnigFeatureCodeProfile`

**Source purpose:** Strict offline snapshot of official CNIG feature code records.

- Exact decorators: none.
- Exact bases: `_StrictModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `profile` | `StrictStr` | `Field(min_length=1)` | `profile: StrictStr = Field(min_length=1)` |
| `standard_model` | `Literal['CNIG PLU v2017']` | `required` | `standard_model: Literal["CNIG PLU v2017"]` |
| `official_text_normalization` | `Literal['GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1']` | `required` | `official_text_normalization: Literal["GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"]` |
| `official_sources` | `OfficialSourceUrls` | `required` | `official_sources: OfficialSourceUrls` |
| `retrieval_date` | `date` | `required` | `retrieval_date: date` |
| `canonical_records_sha256` | `StrictStr` | `required` | `canonical_records_sha256: StrictStr` |
| `records` | `tuple[CnigFeatureCodeRecord, ...]` | `Field(min_length=1)` | `records: tuple[CnigFeatureCodeRecord, ...] = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`
- import: `landscout.stages.aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
)`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_source` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `CnigFeatureCodeProfile`
- import: `landscout.stages.apply_bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result_envelope,
)`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_policy_source` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `CnigFeatureCodeProfile`
- import: `landscout.stages.bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result,
)`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_coded_source` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::CnigFeatureCodeProfile._validate_profile` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::load_cnig_feature_code_profile` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_resolved_profile` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_profile_sha256` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_dictionary` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_lookup` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_coded_catalog` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `CnigFeatureCodeProfile`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_profile` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_mutated_profile` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_inputs` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::resolve_planning_feature_codes` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::validate_planning_feature_code_result` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_official_family_endpoints_require_exact_identity` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_official_text_must_already_be_canonical` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_malformed_code_is_rejected` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_pair_and_profile_hash_mutation_are_rejected` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_wrong_official_host_and_unknown_field_are_rejected` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_record_order_must_be_deterministic` via `CnigFeatureCodeProfile`

**Exact class source**

```python
class CnigFeatureCodeProfile(_StrictModel):
    """Strict offline snapshot of official CNIG feature code records."""

    schema_version: StrictInt
    profile: StrictStr = Field(min_length=1)
    standard_model: Literal["CNIG PLU v2017"]
    official_text_normalization: Literal["GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"]
    official_sources: OfficialSourceUrls
    retrieval_date: date
    canonical_records_sha256: StrictStr
    records: tuple[CnigFeatureCodeRecord, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_profile(self) -> CnigFeatureCodeProfile:
        if self.schema_version != PROFILE_SCHEMA_VERSION:
            raise ValueError(
                f"unsupported CNIG feature-code profile schema: {self.schema_version}"
            )
        _exact_string(self.profile, "code profile")
        if _SHA_PATTERN.fullmatch(self.canonical_records_sha256) is None:
            raise ValueError("canonical records SHA256 is invalid")
        keys = [
            (record.feature_family, record.type_code, record.subtype_code)
            for record in self.records
        ]
        if len(set(keys)) != len(keys):
            raise ValueError("configured CNIG code pairs contain a duplicate")
        if keys != sorted(keys):
            raise ValueError("configured CNIG records must use deterministic order")
        if _records_sha256(self.records) != self.canonical_records_sha256:
            raise ValueError("canonical records SHA256 differs from configured records")
        return self
```

### `PlanningFeatureCodeResult`

**Source purpose:** Immutable envelope around exact official code resolution outputs.

- Exact decorators: `dataclass(frozen=True)`.
- Exact bases: plain object.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `result_hash_schema_version` | `int` | `required` | `result_hash_schema_version: int` |
| `profile_schema_version` | `int` | `required` | `profile_schema_version: int` |
| `profile` | `str` | `required` | `profile: str` |
| `standard_model` | `str` | `required` | `standard_model: str` |
| `profile_sha256` | `str` | `required` | `profile_sha256: str` |
| `source_document_id` | `str` | `required` | `source_document_id: str` |
| `source_archive_sha256` | `str` | `required` | `source_archive_sha256: str` |
| `planning_document_context_sha256` | `str` | `required` | `planning_document_context_sha256: str` |
| `parcel_identity_input_sha256` | `str` | `required` | `parcel_identity_input_sha256: str` |
| `normalized_catalogs_input_sha256` | `str` | `required` | `normalized_catalogs_input_sha256: str` |
| `normalized_relations_input_sha256` | `str` | `required` | `normalized_relations_input_sha256: str` |
| `gpu_related_source_files_sha256` | `str` | `required` | `gpu_related_source_files_sha256: str` |
| `expected_relations_content_sha256` | `str` | `required` | `expected_relations_content_sha256: str` |
| `code_dictionary_content_sha256` | `str` | `required` | `code_dictionary_content_sha256: str` |
| `surface_features_content_sha256` | `str` | `required` | `surface_features_content_sha256: str` |
| `line_features_content_sha256` | `str` | `required` | `line_features_content_sha256: str` |
| `point_features_content_sha256` | `str` | `required` | `point_features_content_sha256: str` |
| `relations_content_sha256` | `str` | `required` | `relations_content_sha256: str` |
| `complete_result_content_sha256` | `str` | `required` | `complete_result_content_sha256: str` |
| `code_dictionary` | `pd.DataFrame` | `required` | `code_dictionary: pd.DataFrame` |
| `surface_features` | `gpd.GeoDataFrame` | `required` | `surface_features: gpd.GeoDataFrame` |
| `line_features` | `gpd.GeoDataFrame` | `required` | `line_features: gpd.GeoDataFrame` |
| `point_features` | `gpd.GeoDataFrame` | `required` | `point_features: gpd.GeoDataFrame` |
| `relations` | `pd.DataFrame` | `required` | `relations: pd.DataFrame` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`
- import: `landscout.stages.aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
)`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_source` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `PlanningFeatureCodeResult`
- import: `landscout.stages.apply_bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result_envelope,
)`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_build_result` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_coded_policy_compatibility` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_source_locks` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_policy_source` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `PlanningFeatureCodeResult`
- import: `landscout.stages.bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result,
)`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_source_lock` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_dictionary_by_pair` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_policy_completeness` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_table` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_build_result` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_coded_source` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_code_dictionary` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_coded_meaning_rows` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_component_metadata` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_frame_sha256` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_complete_sha256` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_result_with_hashes` via `PlanningFeatureCodeResult`
- constructor call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result_envelope` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `PlanningFeatureCodeResult`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `PlanningFeatureCodeResult`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::resolve_planning_feature_codes` via `PlanningFeatureCodeResult`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::validate_planning_feature_code_result` via `PlanningFeatureCodeResult`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_schema_v5_envelope_result` via `PlanningFeatureCodeResult`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_canonical_empty_coded_result` via `PlanningFeatureCodeResult`

**Exact class source**

```python
class PlanningFeatureCodeResult:
    """Immutable envelope around exact official code resolution outputs."""

    result_hash_schema_version: int
    profile_schema_version: int
    profile: str
    standard_model: str
    profile_sha256: str
    source_document_id: str
    source_archive_sha256: str
    planning_document_context_sha256: str
    parcel_identity_input_sha256: str
    normalized_catalogs_input_sha256: str
    normalized_relations_input_sha256: str
    gpu_related_source_files_sha256: str
    expected_relations_content_sha256: str
    code_dictionary_content_sha256: str
    surface_features_content_sha256: str
    line_features_content_sha256: str
    point_features_content_sha256: str
    relations_content_sha256: str
    complete_result_content_sha256: str
    code_dictionary: pd.DataFrame
    surface_features: gpd.GeoDataFrame
    line_features: gpd.GeoDataFrame
    point_features: gpd.GeoDataFrame
    relations: pd.DataFrame
```


## 6. Functions, methods, validators, fixtures, callbacks, and tests

### `_exact_string`

**Purpose:** Implements `exact string` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _exact_string(value: object, label: str) -> str:
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
  - `ValueError(f"{label} must be a non-empty exact string")` under lexical guard `not isinstance(value, str) or not value or value != value.strip()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_official_text` via `_exact_string`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_official_text` via `_exact_string`
- direct call: `landscout.stages.resolve_planning_feature_codes::CnigFeatureCodeProfile._validate_profile` via `_exact_string`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::CnigFeatureCodeProfile._validate_profile` via `_exact_string`
- direct call: `landscout.stages.resolve_planning_feature_codes::_strict_string` via `_exact_string`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_strict_string` via `_exact_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_official_text`

**Purpose:** Implements `canonical official text` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _canonical_official_text(value: str) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `" ".join(unicodedata.normalize("NFC", value).split())`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_official_text` via `_canonical_official_text`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_official_text` via `_canonical_official_text`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `" ".join` | `unresolved local/third-party receiver; no ownership inferred` |
| `unicodedata.normalize("NFC", value).split` | `unresolved local/third-party receiver; no ownership inferred` |
| `unicodedata.normalize` | `unicodedata.normalize` |

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
def _canonical_official_text(value: str) -> str:
    return " ".join(unicodedata.normalize("NFC", value).split())
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_official_text`

**Purpose:** Implements `validate official text` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _validate_official_text(value: object, label: str) -> str:
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
  - `text`
- Explicit raise paths:
  - `ValueError(<br>            f"{label} must already use canonical {OFFICIAL_TEXT_NORMALIZATION} text"<br>        )` under lexical guard `text != _canonical_official_text(text)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_optional_official_text` via `_validate_official_text`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_optional_official_text` via `_validate_official_text`
- direct call: `landscout.stages.resolve_planning_feature_codes::CnigFeatureCodeRecord._validate_record` via `_validate_official_text`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::CnigFeatureCodeRecord._validate_record` via `_validate_official_text`
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_nullable_official_value` via `_validate_official_text`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_nullable_official_value` via `_validate_official_text`
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_code_dictionary` via `_validate_official_text`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_code_dictionary` via `_validate_official_text`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_exact_string` | `landscout.stages.resolve_planning_feature_codes._exact_string` |
| `_canonical_official_text` | `landscout.stages.resolve_planning_feature_codes._canonical_official_text` |
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
def _validate_official_text(value: object, label: str) -> str:
    text = _exact_string(value, label)
    if text != _canonical_official_text(text):
        raise ValueError(
            f"{label} must already use canonical {OFFICIAL_TEXT_NORMALIZATION} text"
        )
    return text
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_optional_official_text`

**Purpose:** Implements `validate optional official text` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _validate_optional_official_text(value: object, label: str) -> str | None:
```

- Exact decorators: none.
- Declared return annotation: `str | None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
  - `_validate_official_text(value, label)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::CnigFeatureCodeRecord._validate_record` via `_validate_optional_official_text`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::CnigFeatureCodeRecord._validate_record` via `_validate_optional_official_text`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_official_text` | `landscout.stages.resolve_planning_feature_codes._validate_official_text` |

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
def _validate_optional_official_text(value: object, label: str) -> str | None:
    if value is None:
        return None
    return _validate_official_text(value, label)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `OfficialSourceUrls._validate_urls`

**Purpose:** Implements `validate urls` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _validate_urls(self) -> OfficialSourceUrls:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `OfficialSourceUrls`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError(<br>                "prescription source URL is not the exact official GPU host endpoint"<br>            )` under lexical guard `self.prescription != PRESCRIPTION_OFFICIAL_SOURCE_URL`.
  - `ValueError(<br>                "information source URL is not the exact official GPU host endpoint"<br>            )` under lexical guard `self.information != INFORMATION_OFFICIAL_SOURCE_URL`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
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
def _validate_urls(self) -> OfficialSourceUrls:
        if self.prescription != PRESCRIPTION_OFFICIAL_SOURCE_URL:
            raise ValueError(
                "prescription source URL is not the exact official GPU host endpoint"
            )
        if self.information != INFORMATION_OFFICIAL_SOURCE_URL:
            raise ValueError(
                "information source URL is not the exact official GPU host endpoint"
            )
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `CnigFeatureCodeRecord._validate_record`

**Purpose:** Implements `validate record` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _validate_record(self) -> CnigFeatureCodeRecord:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `CnigFeatureCodeRecord`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError(f"{label} must contain exactly two digits")` under lexical guard `_CODE_PATTERN.fullmatch(code) is None`.
  - `ValueError("record source URL is not the exact family endpoint")` under lexical guard `self.official_source_url != expected_url`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_CODE_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_official_text` | `landscout.stages.resolve_planning_feature_codes._validate_official_text` |
| `_validate_optional_official_text` | `landscout.stages.resolve_planning_feature_codes._validate_optional_official_text` |
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
def _validate_record(self) -> CnigFeatureCodeRecord:
        for code, label in (
            (self.type_code, "type code"),
            (self.subtype_code, "subtype code"),
        ):
            if _CODE_PATTERN.fullmatch(code) is None:
                raise ValueError(f"{label} must contain exactly two digits")
        _validate_official_text(self.official_label, "official label")
        _validate_optional_official_text(self.legal_reference, "legal reference")
        _validate_optional_official_text(
            self.regulation_or_annex_reference,
            "regulation or annex reference",
        )
        expected_url = (
            PRESCRIPTION_OFFICIAL_SOURCE_URL
            if self.feature_family == "PRESCRIPTION"
            else INFORMATION_OFFICIAL_SOURCE_URL
        )
        if self.official_source_url != expected_url:
            raise ValueError("record source URL is not the exact family endpoint")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_record_payload`

**Purpose:** Implements `record payload` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _record_payload(record: CnigFeatureCodeRecord) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `record` | positional-or-keyword | `CnigFeatureCodeRecord` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "feature_family": record.feature_family,<br>        "type_code": record.type_code,<br>        "subtype_code": record.subtype_code,<br>        "official_label": record.official_label,<br>        "legal_reference": record.legal_reference,<br>        "regulation_or_annex_reference": record.regulation_or_annex_reference,<br>        "official_source_url": record.official_source_url,<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_records_sha256` via `_record_payload`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_records_sha256` via `_record_payload`
- direct call: `landscout.stages.resolve_planning_feature_codes::_dictionary` via `_record_payload`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_dictionary` via `_record_payload`

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
def _record_payload(record: CnigFeatureCodeRecord) -> dict[str, object]:
    return {
        "feature_family": record.feature_family,
        "type_code": record.type_code,
        "subtype_code": record.subtype_code,
        "official_label": record.official_label,
        "legal_reference": record.legal_reference,
        "regulation_or_annex_reference": record.regulation_or_annex_reference,
        "official_source_url": record.official_source_url,
    }
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_json_sha256`

**Purpose:** Implements `canonical json sha256` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _canonical_json_sha256(value: object) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `sha256(encoded).hexdigest()`
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>            "Canonical integrity payload cannot be serialized"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_records_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_records_sha256` via `_canonical_json_sha256`
- direct call: `landscout.stages.resolve_planning_feature_codes::_profile_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_profile_sha256` via `_canonical_json_sha256`
- direct call: `landscout.stages.resolve_planning_feature_codes::_source_frame_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_source_frame_sha256` via `_canonical_json_sha256`
- direct call: `landscout.stages.resolve_planning_feature_codes::_planning_document_context_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_planning_document_context_sha256` via `_canonical_json_sha256`
- direct call: `landscout.stages.resolve_planning_feature_codes::_normalized_catalogs_input_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_normalized_catalogs_input_sha256` via `_canonical_json_sha256`
- direct call: `landscout.stages.resolve_planning_feature_codes::_frame_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_frame_sha256` via `_canonical_json_sha256`
- direct call: `landscout.stages.resolve_planning_feature_codes::_complete_sha256` via `_canonical_json_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_complete_sha256` via `_canonical_json_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `json.dumps(<br>            value,<br>            ensure_ascii=False,<br>            allow_nan=False,<br>            sort_keys=True,<br>            separators=(",", ":"),<br>        ).encode` | `unresolved local/third-party receiver; no ownership inferred` |
| `json.dumps` | `json.dumps` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
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
def _canonical_json_sha256(value: object) -> str:
    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Canonical integrity payload cannot be serialized"
        ) from error
    return sha256(encoded).hexdigest()
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_records_sha256`

**Purpose:** Implements `records sha256` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _records_sha256(records: Sequence[CnigFeatureCodeRecord]) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `records` | positional-or-keyword | `Sequence[CnigFeatureCodeRecord]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256([_record_payload(record) for record in records])`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::CnigFeatureCodeProfile._validate_profile` via `_records_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::CnigFeatureCodeProfile._validate_profile` via `_records_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_json_sha256` | `landscout.stages.resolve_planning_feature_codes._canonical_json_sha256` |
| `_record_payload` | `landscout.stages.resolve_planning_feature_codes._record_payload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_json_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _records_sha256(records: Sequence[CnigFeatureCodeRecord]) -> str:
    return _canonical_json_sha256([_record_payload(record) for record in records])
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `CnigFeatureCodeProfile._validate_profile`

**Purpose:** Implements `validate profile` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _validate_profile(self) -> CnigFeatureCodeProfile:
```

- Exact decorators: `model_validator(mode="after")`.
- Declared return annotation: `CnigFeatureCodeProfile`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `self` | positional-or-keyword | `None` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `self`
- Explicit raise paths:
  - `ValueError(<br>                f"unsupported CNIG feature-code profile schema: {self.schema_version}"<br>            )` under lexical guard `self.schema_version != PROFILE_SCHEMA_VERSION`.
  - `ValueError("canonical records SHA256 is invalid")` under lexical guard `_SHA_PATTERN.fullmatch(self.canonical_records_sha256) is None`.
  - `ValueError("configured CNIG code pairs contain a duplicate")` under lexical guard `len(set(keys)) != len(keys)`.
  - `ValueError("configured CNIG records must use deterministic order")` under lexical guard `keys != sorted(keys)`.
  - `ValueError("canonical records SHA256 differs from configured records")` under lexical guard `_records_sha256(self.records) != self.canonical_records_sha256`.

**Qualified relationships**

Inbound conservative repository consumers:
- None found by exact import/direct-call/value-reference resolution.

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `ValueError` | `unresolved local/third-party receiver; no ownership inferred` |
| `_exact_string` | `landscout.stages.resolve_planning_feature_codes._exact_string` |
| `_SHA_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `set` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_records_sha256` | `landscout.stages.resolve_planning_feature_codes._records_sha256` |
| `model_validator` | `pydantic.model_validator` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_records_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_profile(self) -> CnigFeatureCodeProfile:
        if self.schema_version != PROFILE_SCHEMA_VERSION:
            raise ValueError(
                f"unsupported CNIG feature-code profile schema: {self.schema_version}"
            )
        _exact_string(self.profile, "code profile")
        if _SHA_PATTERN.fullmatch(self.canonical_records_sha256) is None:
            raise ValueError("canonical records SHA256 is invalid")
        keys = [
            (record.feature_family, record.type_code, record.subtype_code)
            for record in self.records
        ]
        if len(set(keys)) != len(keys):
            raise ValueError("configured CNIG code pairs contain a duplicate")
        if keys != sorted(keys):
            raise ValueError("configured CNIG records must use deterministic order")
        if _records_sha256(self.records) != self.canonical_records_sha256:
            raise ValueError("canonical records SHA256 differs from configured records")
        return self
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `load_cnig_feature_code_profile`

**Purpose:** Load a strict offline CNIG feature-code profile.

**Exact signature**

```python
def load_cnig_feature_code_profile(path: str | Path) -> CnigFeatureCodeProfile:
```

- Exact decorators: none.
- Declared return annotation: `CnigFeatureCodeProfile`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `path` | positional-or-keyword | `str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `CnigFeatureCodeProfile.model_validate(payload)`
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>                "CNIG feature-code profile must be a mapping"<br>            )` under lexical guard `not isinstance(payload, Mapping)`.
  - `re-raise`.
  - `PlanningFeatureCodeError(str(error))`.
  - `PlanningFeatureCodeError(<br>            "CNIG feature-code profile is invalid"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`
- direct call: `landscout.stages.resolve_planning_feature_codes::_resolved_profile` via `load_cnig_feature_code_profile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_resolved_profile` via `load_cnig_feature_code_profile`
- import: `tests.unit.test_bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
)`
- direct call: `tests.unit.test_bess_planning_feature_policy::_checked_in_policy_result` via `load_cnig_feature_code_profile`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_checked_in_policy_result` via `load_cnig_feature_code_profile`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_yaml_key_is_rejected` via `load_cnig_feature_code_profile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_yaml_key_is_rejected` via `load_cnig_feature_code_profile`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_yaml_snapshot_loads_strictly` via `load_cnig_feature_code_profile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_yaml_snapshot_loads_strictly` via `load_cnig_feature_code_profile`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs` via `load_cnig_feature_code_profile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs` via `load_cnig_feature_code_profile`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `loads_strict_yaml` | `landscout.common.strict_yaml.loads_strict_yaml` |
| `Path(path).read_bytes` | `unresolved local/third-party receiver; no ownership inferred` |
| `Path` | `pathlib.Path` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `CnigFeatureCodeProfile.model_validate` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.model_validate` |
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
def load_cnig_feature_code_profile(path: str | Path) -> CnigFeatureCodeProfile:
    """Load a strict offline CNIG feature-code profile."""

    try:
        payload = loads_strict_yaml(Path(path).read_bytes())
        if not isinstance(payload, Mapping):
            raise PlanningFeatureCodeError(
                "CNIG feature-code profile must be a mapping"
            )
        return CnigFeatureCodeProfile.model_validate(payload)
    except PlanningFeatureCodeError:
        raise
    except StrictYamlError as error:
        raise PlanningFeatureCodeError(str(error)) from error
    except Exception as error:
        raise PlanningFeatureCodeError(
            "CNIG feature-code profile is invalid"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_resolved_profile`

**Purpose:** Implements `resolved profile` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _resolved_profile(
    profile: CnigFeatureCodeProfile | str | Path,
) -> CnigFeatureCodeProfile:
```

- Exact decorators: none.
- Declared return annotation: `CnigFeatureCodeProfile`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `profile` | positional-or-keyword | `CnigFeatureCodeProfile \| str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `load_cnig_feature_code_profile(profile)`
  - `CnigFeatureCodeProfile.model_validate(payload)`
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>            "In-memory CNIG feature-code profile is invalid"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `_resolved_profile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `_resolved_profile`
- direct call: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `_resolved_profile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `_resolved_profile`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `load_cnig_feature_code_profile` | `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile` |
| `profile.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |
| `CnigFeatureCodeProfile.model_validate` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.model_validate` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |

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
def _resolved_profile(
    profile: CnigFeatureCodeProfile | str | Path,
) -> CnigFeatureCodeProfile:
    if not isinstance(profile, CnigFeatureCodeProfile):
        return load_cnig_feature_code_profile(profile)
    try:
        payload = profile.model_dump(mode="python", warnings="error")
        return CnigFeatureCodeProfile.model_validate(payload)
    except Exception as error:
        raise PlanningFeatureCodeError(
            "In-memory CNIG feature-code profile is invalid"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_profile_sha256`

**Purpose:** Implements `profile sha256` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _profile_sha256(profile: CnigFeatureCodeProfile) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `profile` | positional-or-keyword | `CnigFeatureCodeProfile` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256(profile.model_dump(mode="json"))`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_profile_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_profile_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_json_sha256` | `landscout.stages.resolve_planning_feature_codes._canonical_json_sha256` |
| `profile.model_dump` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_json_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _profile_sha256(profile: CnigFeatureCodeProfile) -> str:
    return _canonical_json_sha256(profile.model_dump(mode="json"))
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_strict_string`

**Purpose:** Implements `strict string` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

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
  - `_exact_string(value, label)`
- Explicit raise paths:
  - `PlanningFeatureCodeError(str(error))`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_planning_standard` via `_strict_string`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_planning_standard` via `_strict_string`
- direct call: `landscout.stages.resolve_planning_feature_codes::_coded_relations` via `_strict_string`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_coded_relations` via `_strict_string`
- direct call: `landscout.stages.resolve_planning_feature_codes::_inspected_layer_payload` via `_strict_string`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_inspected_layer_payload` via `_strict_string`
- direct call: `landscout.stages.resolve_planning_feature_codes::_planning_document_context_sha256` via `_strict_string`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_planning_document_context_sha256` via `_strict_string`
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `_strict_string`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `_strict_string`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_exact_string` | `landscout.stages.resolve_planning_feature_codes._exact_string` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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
    try:
        return _exact_string(value, label)
    except ValueError as error:
        raise PlanningFeatureCodeError(str(error)) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_planning_standard`

**Purpose:** Implements `planning standard` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _planning_standard(document: GpuPlanningDocument) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `document` | positional-or-keyword | `GpuPlanningDocument` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_strict_string(distinct[0], "planning document standard")`
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>            "planning_document must be a GpuPlanningDocument"<br>        )` under lexical guard `not isinstance(document, GpuPlanningDocument)`.
  - `PlanningFeatureCodeError(<br>            "Planning document standard lineage is ambiguous"<br>        )` under lexical guard `len(distinct) != 1`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_planning_standard`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_planning_standard`
- direct call: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `_planning_standard`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `_planning_standard`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `list` | `unresolved local/third-party receiver; no ownership inferred` |
| `models.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `tuple` | `unresolved local/third-party receiver; no ownership inferred` |
| `dict.fromkeys` | `unresolved local/third-party receiver; no ownership inferred` |
| `len` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.resolve_planning_feature_codes._strict_string` |

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
| In-memory mutation | `models.append(metadata.standard_model)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _planning_standard(document: GpuPlanningDocument) -> str:
    if not isinstance(document, GpuPlanningDocument):
        raise PlanningFeatureCodeError(
            "planning_document must be a GpuPlanningDocument"
        )
    metadata = document.extraction.archive.document
    models = list(document.extraction.standard_models)
    if metadata.standard_model is not None:
        models.append(metadata.standard_model)
    distinct = tuple(dict.fromkeys(models))
    if len(distinct) != 1:
        raise PlanningFeatureCodeError(
            "Planning document standard lineage is ambiguous"
        )
    return _strict_string(distinct[0], "planning document standard")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validated_code_series`

**Purpose:** Implements `validated code series` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _validated_code_series(series: pd.Series, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `series` | positional-or-keyword | `pd.Series` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>                f"{label} must contain exact two-character digit strings"<br>            )` under lexical guard `not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_catalog_document_lineage` via `_validated_code_series`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_catalog_document_lineage` via `_validated_code_series`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `series.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_CODE_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |

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
def _validated_code_series(series: pd.Series, label: str) -> None:
    for value in series.tolist():
        if not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None:
            raise PlanningFeatureCodeError(
                f"{label} must contain exact two-character digit strings"
            )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_is_true_null`

**Purpose:** Implements `is true null` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _is_true_null(value: object) -> bool:
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
  - `isinstance(missing, (bool, np.bool_)) and bool(missing)`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_null_safe_equal` via `_is_true_null`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_null_safe_equal` via `_is_true_null`
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_nullable_official_value` via `_is_true_null`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_nullable_official_value` via `_is_true_null`
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_coded_meaning_rows` via `_is_true_null`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_coded_meaning_rows` via `_is_true_null`

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
def _is_true_null(value: object) -> bool:
    if value is None or value is pd.NA:
        return True
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        return False
    return isinstance(missing, (bool, np.bool_)) and bool(missing)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_null_safe_equal`

**Purpose:** Implements `null safe equal` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _null_safe_equal(left: object, right: object) -> bool:
```

- Exact decorators: none.
- Declared return annotation: `bool`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `left` | positional-or-keyword | `object` | `required` |
| `right` | positional-or-keyword | `object` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `left_null and right_null`
  - `type(left) is type(right) and left == right`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_coded_meaning_rows` via `_null_safe_equal`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_coded_meaning_rows` via `_null_safe_equal`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_true_null` | `landscout.stages.resolve_planning_feature_codes._is_true_null` |
| `type` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _null_safe_equal(left: object, right: object) -> bool:
    left_null = _is_true_null(left)
    right_null = _is_true_null(right)
    if left_null or right_null:
        return left_null and right_null
    return type(left) is type(right) and left == right
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_nullable_official_value`

**Purpose:** Implements `validate nullable official value` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _validate_nullable_official_value(value: object, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `value` | positional-or-keyword | `object` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `None`
- Explicit raise paths:
  - `PlanningFeatureCodeError(f"{label} contains a literal null replacement")` under lexical guard `isinstance(value, str) and value in _NULL_REFERENCE_LITERALS`.
  - `PlanningFeatureCodeError(str(error))`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_code_dictionary` via `_validate_nullable_official_value`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_code_dictionary` via `_validate_nullable_official_value`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_is_true_null` | `landscout.stages.resolve_planning_feature_codes._is_true_null` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `_validate_official_text` | `landscout.stages.resolve_planning_feature_codes._validate_official_text` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _validate_nullable_official_value(value: object, label: str) -> None:
    if _is_true_null(value):
        return
    if isinstance(value, str) and value in _NULL_REFERENCE_LITERALS:
        raise PlanningFeatureCodeError(f"{label} contains a literal null replacement")
    try:
        _validate_official_text(value, label)
    except ValueError as error:
        raise PlanningFeatureCodeError(str(error)) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_code_dictionary`

**Purpose:** Implements `validate code dictionary` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _validate_code_dictionary(
    result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

- Exact decorators: none.
- Declared return annotation: `dict[tuple[str, str, str], dict[str, object]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `records`
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>            "code dictionary must be a non-geospatial DataFrame"<br>        )` under lexical guard `type(frame) is not pd.DataFrame`.
  - `PlanningFeatureCodeError("code dictionary canonical schema is invalid")` under lexical guard `frame.columns.duplicated().any() or (<br>        deterministic_frame_schema_signature(frame) != CODE_DICTIONARY_SCHEMA_SIGNATURE<br>    )`.
  - `PlanningFeatureCodeError(<br>            "code dictionary must contain at least one official code record"<br>        )` under lexical guard `frame.empty`.
  - `PlanningFeatureCodeError(<br>                f"code dictionary row {position} feature family is invalid"<br>            )` under lexical guard `family not in {"PRESCRIPTION", "INFORMATION"}`.
  - `PlanningFeatureCodeError(<br>                    f"code dictionary row {position} {field} is invalid"<br>                )` under lexical guard `not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None`.
  - `PlanningFeatureCodeError("code dictionary contains duplicate pairs")` under lexical guard `key in records`.
  - `PlanningFeatureCodeError(str(error))`.
  - `PlanningFeatureCodeError(<br>                f"code dictionary row {position} official URL is invalid"<br>            )` under lexical guard `row["official_source_url"] != expected_url`.
  - `PlanningFeatureCodeError(<br>                f"code dictionary row {position} result lineage differs"<br>            )` under lexical guard `row["profile"] != result.profile<br>            or row["profile_sha256"] != result.profile_sha256<br>            or row["standard_model"] != result.standard_model`.
  - `PlanningFeatureCodeError("code dictionary pair order is not canonical")` under lexical guard `ordered_keys != sorted(ordered_keys)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `_validate_code_dictionary`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `_validate_code_dictionary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `frame.columns.duplicated().any` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.columns.duplicated` | `unresolved local/third-party receiver; no ownership inferred` |
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_CODE_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_official_text` | `landscout.stages.resolve_planning_feature_codes._validate_official_text` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_nullable_official_value` | `landscout.stages.resolve_planning_feature_codes._validate_nullable_official_value` |
| `ordered_keys.append` | `unresolved local/third-party receiver; no ownership inferred` |
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `records[key] = row`<br>`ordered_keys.append(key)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_code_dictionary(
    result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    frame = result.code_dictionary
    if type(frame) is not pd.DataFrame:
        raise PlanningFeatureCodeError(
            "code dictionary must be a non-geospatial DataFrame"
        )
    if frame.columns.duplicated().any() or (
        deterministic_frame_schema_signature(frame) != CODE_DICTIONARY_SCHEMA_SIGNATURE
    ):
        raise PlanningFeatureCodeError("code dictionary canonical schema is invalid")
    if frame.empty:
        raise PlanningFeatureCodeError(
            "code dictionary must contain at least one official code record"
        )
    records: dict[tuple[str, str, str], dict[str, object]] = {}
    ordered_keys: list[tuple[str, str, str]] = []
    for position, row in enumerate(frame.to_dict("records")):
        family = row["feature_family"]
        if family not in {"PRESCRIPTION", "INFORMATION"}:
            raise PlanningFeatureCodeError(
                f"code dictionary row {position} feature family is invalid"
            )
        for field in ("type_code", "subtype_code"):
            value = row[field]
            if not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None:
                raise PlanningFeatureCodeError(
                    f"code dictionary row {position} {field} is invalid"
                )
        key = (family, row["type_code"], row["subtype_code"])
        if key in records:
            raise PlanningFeatureCodeError("code dictionary contains duplicate pairs")
        try:
            _validate_official_text(
                row["official_label"],
                f"code dictionary row {position} official label",
            )
        except ValueError as error:
            raise PlanningFeatureCodeError(str(error)) from error
        _validate_nullable_official_value(
            row["legal_reference"],
            f"code dictionary row {position} legal reference",
        )
        _validate_nullable_official_value(
            row["regulation_or_annex_reference"],
            f"code dictionary row {position} regulation reference",
        )
        expected_url = (
            PRESCRIPTION_OFFICIAL_SOURCE_URL
            if family == "PRESCRIPTION"
            else INFORMATION_OFFICIAL_SOURCE_URL
        )
        if row["official_source_url"] != expected_url:
            raise PlanningFeatureCodeError(
                f"code dictionary row {position} official URL is invalid"
            )
        if (
            row["profile"] != result.profile
            or row["profile_sha256"] != result.profile_sha256
            or row["standard_model"] != result.standard_model
        ):
            raise PlanningFeatureCodeError(
                f"code dictionary row {position} result lineage differs"
            )
        records[key] = row
        ordered_keys.append(key)
    if ordered_keys != sorted(ordered_keys):
        raise PlanningFeatureCodeError("code dictionary pair order is not canonical")
    return records
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_coded_meaning_rows`

**Purpose:** Implements `validate coded meaning rows` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _validate_coded_meaning_rows(
    result: PlanningFeatureCodeResult,
    dictionary: Mapping[tuple[str, str, str], Mapping[str, object]],
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |
| `dictionary` | positional-or-keyword | `Mapping[tuple[str, str, str], Mapping[str, object]]` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningFeatureCodeError("coded feature family is invalid")` under lexical guard `family not in {"PRESCRIPTION", "INFORMATION"}`.
  - `PlanningFeatureCodeError(f"coded feature {label} is invalid")` under lexical guard `not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None`.
  - `PlanningFeatureCodeError("coded feature profile lineage differs")` under lexical guard `row["official_code_profile"] != result.profile<br>                or row["official_code_profile_sha256"] != result.profile_sha256`.
  - `PlanningFeatureCodeError(<br>                        "resolved coded feature meaning differs from code dictionary"<br>                    )` under lexical guard `status == "RESOLVED_OFFICIAL"`.
  - `PlanningFeatureCodeError(<br>                        "unknown coded feature contains an official meaning"<br>                    )` under lexical guard `status == "RESOLVED_OFFICIAL"`.
  - `PlanningFeatureCodeError(<br>                    f"coded feature official status is invalid at row {position}"<br>                )` under lexical guard `status == "RESOLVED_OFFICIAL"`.
  - `PlanningFeatureCodeError("coded feature ID is invalid")` under lexical guard `not isinstance(identifier, str) or not identifier`.
  - `PlanningFeatureCodeError(<br>                    "coded feature IDs are not globally unique"<br>                )` under lexical guard `identifier in features`.
  - `PlanningFeatureCodeError(<br>                "coded relation references an unknown feature ID"<br>            )` under lexical guard `feature is None`.
  - `PlanningFeatureCodeError(<br>                "coded relation official meaning differs from its feature"<br>            )` under lexical guard `any(<br>            not _null_safe_equal(row[field], feature[field])<br>            for field in compared_fields<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `_validate_coded_meaning_rows`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `_validate_coded_meaning_rows`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `enumerate` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_CODE_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `dictionary.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `any` | `unresolved local/third-party receiver; no ownership inferred` |
| `_null_safe_equal` | `landscout.stages.resolve_planning_feature_codes._null_safe_equal` |
| `_is_true_null` | `landscout.stages.resolve_planning_feature_codes._is_true_null` |
| `result.relations.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `features.get` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `features[identifier] = row` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_coded_meaning_rows(
    result: PlanningFeatureCodeResult,
    dictionary: Mapping[tuple[str, str, str], Mapping[str, object]],
) -> None:
    catalogs = (
        result.surface_features,
        result.line_features,
        result.point_features,
    )
    features: dict[str, dict[str, object]] = {}
    for frame in catalogs:
        for position, row in enumerate(frame.to_dict("records")):
            family = row["feature_family"]
            type_code = row["type_code_raw"]
            subtype_code = row["subtype_code_raw"]
            if family not in {"PRESCRIPTION", "INFORMATION"}:
                raise PlanningFeatureCodeError("coded feature family is invalid")
            for value, label in (
                (type_code, "type code"),
                (subtype_code, "subtype code"),
            ):
                if not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None:
                    raise PlanningFeatureCodeError(f"coded feature {label} is invalid")
            if (
                row["official_code_profile"] != result.profile
                or row["official_code_profile_sha256"] != result.profile_sha256
            ):
                raise PlanningFeatureCodeError("coded feature profile lineage differs")
            key = (family, type_code, subtype_code)
            record = dictionary.get(key)
            status = row["official_code_status"]
            meaning_fields = (
                ("official_code_label", "official_label"),
                ("official_legal_reference", "legal_reference"),
                (
                    "official_regulation_reference",
                    "regulation_or_annex_reference",
                ),
                ("official_code_source_url", "official_source_url"),
            )
            if status == "RESOLVED_OFFICIAL":
                if record is None or any(
                    not _null_safe_equal(row[field], record[dictionary_field])
                    for field, dictionary_field in meaning_fields
                ):
                    raise PlanningFeatureCodeError(
                        "resolved coded feature meaning differs from code dictionary"
                    )
            elif status == "UNKNOWN_CODE_PAIR":
                if record is not None or any(
                    not _is_true_null(row[field]) for field, _ in meaning_fields
                ):
                    raise PlanningFeatureCodeError(
                        "unknown coded feature contains an official meaning"
                    )
            else:
                raise PlanningFeatureCodeError(
                    f"coded feature official status is invalid at row {position}"
                )
            identifier = row["planning_feature_id"]
            if not isinstance(identifier, str) or not identifier:
                raise PlanningFeatureCodeError("coded feature ID is invalid")
            if identifier in features:
                raise PlanningFeatureCodeError(
                    "coded feature IDs are not globally unique"
                )
            features[identifier] = row
    compared_fields = (
        "feature_family",
        "type_code_raw",
        "subtype_code_raw",
        *OFFICIAL_CODE_COLUMNS,
    )
    for row in result.relations.to_dict("records"):
        identifier = row["planning_feature_id"]
        feature = features.get(identifier)
        if feature is None:
            raise PlanningFeatureCodeError(
                "coded relation references an unknown feature ID"
            )
        if any(
            not _null_safe_equal(row[field], feature[field])
            for field in compared_fields
        ):
            raise PlanningFeatureCodeError(
                "coded relation official meaning differs from its feature"
            )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_catalog_document_lineage`

**Purpose:** Implements `validate catalog document lineage` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _validate_catalog_document_lineage(
    frame: gpd.GeoDataFrame,
    label: str,
    document: GpuPlanningDocument,
    standard_model: str,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `label` | positional-or-keyword | `str` | `required` |
| `document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `standard_model` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `frame.copy(deep=True)`
- Explicit raise paths:
  - `PlanningFeatureCodeError(f"{label} document lineage differs")` under lexical guard `not frame["source_document_id"].eq(metadata.document_id).all()`.
  - `PlanningFeatureCodeError(f"{label} archive lineage differs")` under lexical guard `not frame["source_archive_sha256"].eq(document.extraction.archive.sha256).all()`.
  - `PlanningFeatureCodeError(f"{label} source standard lineage differs")` under lexical guard `not frame["source_standard_model"].eq(standard_model).all()`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_validate_catalog_document_lineage`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_validate_catalog_document_lineage`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validated_code_series` | `landscout.stages.resolve_planning_feature_codes._validated_code_series` |
| `frame["source_document_id"].eq(metadata.document_id).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_document_id"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `frame["source_archive_sha256"].eq(document.extraction.archive.sha256).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_archive_sha256"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_standard_model"].eq(standard_model).all` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame["source_standard_model"].eq` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.copy` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | `frame["source_archive_sha256"].eq(document.extraction.archive.sha256).all` |
| Hashing/byte identity | `frame["source_archive_sha256"].eq(document.extraction.archive.sha256).all`<br>`frame["source_archive_sha256"].eq` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _validate_catalog_document_lineage(
    frame: gpd.GeoDataFrame,
    label: str,
    document: GpuPlanningDocument,
    standard_model: str,
) -> gpd.GeoDataFrame:
    _validated_code_series(frame["type_code_raw"], f"{label} type code")
    _validated_code_series(frame["subtype_code_raw"], f"{label} subtype code")
    metadata = document.extraction.archive.document
    if not frame["source_document_id"].eq(metadata.document_id).all():
        raise PlanningFeatureCodeError(f"{label} document lineage differs")
    if not frame["source_archive_sha256"].eq(document.extraction.archive.sha256).all():
        raise PlanningFeatureCodeError(f"{label} archive lineage differs")
    if not frame["source_standard_model"].eq(standard_model).all():
        raise PlanningFeatureCodeError(f"{label} source standard lineage differs")
    return frame.copy(deep=True)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_dictionary`

**Purpose:** Implements `dictionary` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _dictionary(
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `profile` | positional-or-keyword | `CnigFeatureCodeProfile` | `required` |
| `profile_hash` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_dictionary`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_dictionary`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_record_payload` | `landscout.stages.resolve_planning_feature_codes._record_payload` |
| `pd.DataFrame` | `pandas.DataFrame` |
| `pd.array` | `pandas.array` |
| `output[column].tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.Index` | `pandas.Index` |
| `np.arange` | `numpy.arange` |
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
| In-memory mutation | `output[column] = pd.array(output[column].tolist(), dtype="str")`<br>`output.index = pd.Index(np.arange(len(output), dtype="int64"))` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _dictionary(
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> pd.DataFrame:
    rows = [
        {
            **_record_payload(record),
            "profile": profile.profile,
            "profile_sha256": profile_hash,
            "standard_model": profile.standard_model,
        }
        for record in profile.records
    ]
    output = pd.DataFrame(rows, columns=CODE_DICTIONARY_COLUMNS)
    for column in CODE_DICTIONARY_COLUMNS:
        output[column] = pd.array(output[column].tolist(), dtype="str")
    output.index = pd.Index(np.arange(len(output), dtype="int64"))
    return output
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_lookup`

**Purpose:** Implements `lookup` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _lookup(
    profile: CnigFeatureCodeProfile,
) -> dict[tuple[str, str, str], CnigFeatureCodeRecord]:
```

- Exact decorators: none.
- Declared return annotation: `dict[tuple[str, str, str], CnigFeatureCodeRecord]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `profile` | positional-or-keyword | `CnigFeatureCodeProfile` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        (record.feature_family, record.type_code, record.subtype_code): record<br>        for record in profile.records<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_coded_catalog` via `_lookup`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_coded_catalog` via `_lookup`

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
def _lookup(
    profile: CnigFeatureCodeProfile,
) -> dict[tuple[str, str, str], CnigFeatureCodeRecord]:
    return {
        (record.feature_family, record.type_code, record.subtype_code): record
        for record in profile.records
    }
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_coded_catalog`

**Purpose:** Implements `coded catalog` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _coded_catalog(
    frame: gpd.GeoDataFrame,
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> gpd.GeoDataFrame:
```

- Exact decorators: none.
- Declared return annotation: `gpd.GeoDataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `profile` | positional-or-keyword | `CnigFeatureCodeProfile` | `required` |
| `profile_hash` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_coded_catalog`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_coded_catalog`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `frame.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `_lookup` | `landscout.stages.resolve_planning_feature_codes._lookup` |
| `frame.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `mapping.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `columns["official_code_status"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `columns["official_code_label"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `columns["official_legal_reference"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `columns["official_regulation_reference"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `columns["official_code_source_url"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `columns["official_code_profile"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `columns["official_code_profile_sha256"].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.array` | `pandas.array` |
| `pd.Index` | `pandas.Index` |
| `output.index.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `columns["official_code_profile_sha256"].append` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | `columns["official_code_status"].append(<br>            "RESOLVED_OFFICIAL" if record is not None else "UNKNOWN_CODE_PAIR"<br>        )`<br>`columns["official_code_label"].append(<br>            record.official_label if record is not None else None<br>        )`<br>`columns["official_legal_reference"].append(<br>            record.legal_reference if record is not None else None<br>        )`<br>`columns["official_regulation_reference"].append(<br>            record.regulation_or_annex_reference if record is not None else None<br>        )`<br>`columns["official_code_source_url"].append(<br>            record.official_source_url if record is not None else None<br>        )`<br>`columns["official_code_profile"].append(profile.profile)`<br>`columns["official_code_profile_sha256"].append(profile_hash)`<br>`output[column] = pd.array(columns[column], dtype="str")`<br>`output.index = pd.Index(output.index.to_numpy(copy=True), name=output.index.name)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _coded_catalog(
    frame: gpd.GeoDataFrame,
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> gpd.GeoDataFrame:
    output = frame.copy(deep=True)
    mapping = _lookup(profile)
    columns: dict[str, list[object]] = {column: [] for column in OFFICIAL_CODE_COLUMNS}
    for row in frame.to_dict("records"):
        key = (row["feature_family"], row["type_code_raw"], row["subtype_code_raw"])
        record = mapping.get(key)
        columns["official_code_status"].append(
            "RESOLVED_OFFICIAL" if record is not None else "UNKNOWN_CODE_PAIR"
        )
        columns["official_code_label"].append(
            record.official_label if record is not None else None
        )
        columns["official_legal_reference"].append(
            record.legal_reference if record is not None else None
        )
        columns["official_regulation_reference"].append(
            record.regulation_or_annex_reference if record is not None else None
        )
        columns["official_code_source_url"].append(
            record.official_source_url if record is not None else None
        )
        columns["official_code_profile"].append(profile.profile)
        columns["official_code_profile_sha256"].append(profile_hash)
    for column in OFFICIAL_CODE_COLUMNS:
        output[column] = pd.array(columns[column], dtype="str")
    output.index = pd.Index(output.index.to_numpy(copy=True), name=output.index.name)
    return output
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_catalog_by_id`

**Purpose:** Implements `catalog by id` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _catalog_by_id(
    catalogs: Sequence[gpd.GeoDataFrame],
) -> dict[str, dict[str, object]]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, dict[str, object]]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `catalogs` | positional-or-keyword | `Sequence[gpd.GeoDataFrame]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `records`
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>                    "Planning feature IDs must be unique across feature catalogs"<br>                )` under lexical guard `identifier in records`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_coded_relations` via `_catalog_by_id`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_coded_relations` via `_catalog_by_id`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `catalog.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |

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
| In-memory mutation | `records[identifier] = row` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _catalog_by_id(
    catalogs: Sequence[gpd.GeoDataFrame],
) -> dict[str, dict[str, object]]:
    records: dict[str, dict[str, object]] = {}
    for catalog in catalogs:
        for row in catalog.to_dict("records"):
            identifier = str(row["planning_feature_id"])
            if identifier in records:
                raise PlanningFeatureCodeError(
                    "Planning feature IDs must be unique across feature catalogs"
                )
            records[identifier] = row
    return records
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_coded_relations`

**Purpose:** Implements `coded relations` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _coded_relations(
    relations: pd.DataFrame,
    coded: Sequence[gpd.GeoDataFrame],
) -> pd.DataFrame:
```

- Exact decorators: none.
- Declared return annotation: `pd.DataFrame`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `coded` | positional-or-keyword | `Sequence[gpd.GeoDataFrame]` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `output`
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>                "Relation references an unknown feature catalog ID"<br>            )` under lexical guard `meaning is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_coded_relations`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_coded_relations`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_catalog_by_id` | `landscout.stages.resolve_planning_feature_codes._catalog_by_id` |
| `relations.copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `relations.to_dict` | `unresolved local/third-party receiver; no ownership inferred` |
| `_strict_string` | `landscout.stages.resolve_planning_feature_codes._strict_string` |
| `meanings.get` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `appended[column].append` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.array` | `pandas.array` |
| `pd.Index` | `pandas.Index` |
| `output.index.to_numpy` | `unresolved local/third-party receiver; no ownership inferred` |

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
| In-memory mutation | `appended[column].append(meaning[column])`<br>`output[column] = pd.array(appended[column], dtype="str")`<br>`output.index = pd.Index(output.index.to_numpy(copy=True), name=output.index.name)` |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _coded_relations(
    relations: pd.DataFrame,
    coded: Sequence[gpd.GeoDataFrame],
) -> pd.DataFrame:
    meanings = _catalog_by_id(coded)
    output = relations.copy(deep=True)
    appended: dict[str, list[object]] = {column: [] for column in OFFICIAL_CODE_COLUMNS}
    for row in relations.to_dict("records"):
        identifier = _strict_string(row["planning_feature_id"], "relation feature ID")
        meaning = meanings.get(identifier)
        if meaning is None:
            raise PlanningFeatureCodeError(
                "Relation references an unknown feature catalog ID"
            )
        for column in OFFICIAL_CODE_COLUMNS:
            appended[column].append(meaning[column])
    for column in OFFICIAL_CODE_COLUMNS:
        output[column] = pd.array(appended[column], dtype="str")
    output.index = pd.Index(output.index.to_numpy(copy=True), name=output.index.name)
    return output
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_canonical_value`

**Purpose:** Implements `canonical value` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

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
  - `to_wkb(value, hex=True, include_srid=False)`
  - `value.isoformat()`
  - `_canonical_value(value.item())`
  - `{str(key): _canonical_value(item) for key, item in value.items()}`
  - `[_canonical_value(item) for item in value]`
  - `None`
  - `value`
  - `int(value)`
  - `number`
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>                "Integrity payload contains non-finite numeric data"<br>            )` under lexical guard `isinstance(value, Real)`.
  - `PlanningFeatureCodeError(<br>        f"Integrity payload contains unsupported value {type(value).__name__}"<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_canonical_value` via `_canonical_value`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_canonical_value` via `_canonical_value`
- direct call: `landscout.stages.resolve_planning_feature_codes::_frame_payload` via `_canonical_value`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_frame_payload` via `_canonical_value`
- direct call: `landscout.stages.resolve_planning_feature_codes::_compare_frame` via `_canonical_value`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_compare_frame` via `_canonical_value`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `to_wkb` | `shapely.to_wkb` |
| `value.isoformat` | `unresolved local/third-party receiver; no ownership inferred` |
| `_canonical_value` | `landscout.stages.resolve_planning_feature_codes._canonical_value` |
| `value.item` | `unresolved local/third-party receiver; no ownership inferred` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `value.items` | `unresolved local/third-party receiver; no ownership inferred` |
| `pd.isna` | `pandas.isna` |
| `bool` | `unresolved local/third-party receiver; no ownership inferred` |
| `int` | `unresolved local/third-party receiver; no ownership inferred` |
| `float` | `unresolved local/third-party receiver; no ownership inferred` |
| `math.isfinite` | `math.isfinite` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
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
    if isinstance(value, BaseGeometry):
        return to_wkb(value, hex=True, include_srid=False)
    if isinstance(value, (datetime, date, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, np.generic):
        return _canonical_value(value.item())
    if isinstance(value, Mapping):
        return {str(key): _canonical_value(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, np.ndarray)):
        return [_canonical_value(item) for item in value]
    if value is None or value is pd.NA:
        return None
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        missing = False
    if isinstance(missing, (bool, np.bool_)) and bool(missing):
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        number = float(value)
        if not math.isfinite(number):
            raise PlanningFeatureCodeError(
                "Integrity payload contains non-finite numeric data"
            )
        return number
    if isinstance(value, str):
        return value
    raise PlanningFeatureCodeError(
        f"Integrity payload contains unsupported value {type(value).__name__}"
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_frame_payload`

**Purpose:** Implements `frame payload` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `payload`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_source_frame_sha256` via `_frame_payload`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_source_frame_sha256` via `_frame_payload`
- direct call: `landscout.stages.resolve_planning_feature_codes::_normalized_catalogs_input_sha256` via `_frame_payload`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_normalized_catalogs_input_sha256` via `_frame_payload`
- direct call: `landscout.stages.resolve_planning_feature_codes::_frame_sha256` via `_frame_payload`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_frame_sha256` via `_frame_payload`
- direct call: `landscout.stages.resolve_planning_feature_codes::_compare_frame` via `_frame_payload`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_compare_frame` via `_frame_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `deterministic_frame_schema_signature` | `landscout.common.frame_integrity.deterministic_frame_schema_signature` |
| `_canonical_value` | `landscout.stages.resolve_planning_feature_codes._canonical_value` |
| `frame.index.tolist` | `unresolved local/third-party receiver; no ownership inferred` |
| `frame.itertuples` | `unresolved local/third-party receiver; no ownership inferred` |

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
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
    payload: dict[str, object] = {
        "schema": deterministic_frame_schema_signature(frame),
        "index": [_canonical_value(value) for value in frame.index.tolist()],
        "rows": [
            [_canonical_value(value) for value in row]
            for row in frame.itertuples(index=False, name=None)
        ],
    }
    return payload
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_source_frame_sha256`

**Purpose:** Implements `source frame sha256` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _source_frame_sha256(domain: str, frame: pd.DataFrame) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `domain` | positional-or-keyword | `str` | `required` |
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256(<br>        {<br>            "domain": domain,<br>            "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,<br>            "frame": _frame_payload(frame),<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_inspected_layer_payload` via `_source_frame_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_inspected_layer_payload` via `_source_frame_sha256`
- direct call: `landscout.stages.resolve_planning_feature_codes::_parcel_identity_input_sha256` via `_source_frame_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_parcel_identity_input_sha256` via `_source_frame_sha256`
- direct call: `landscout.stages.resolve_planning_feature_codes::_normalized_relations_input_sha256` via `_source_frame_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_normalized_relations_input_sha256` via `_source_frame_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_json_sha256` | `landscout.stages.resolve_planning_feature_codes._canonical_json_sha256` |
| `_frame_payload` | `landscout.stages.resolve_planning_feature_codes._frame_payload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_json_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _source_frame_sha256(domain: str, frame: pd.DataFrame) -> str:
    return _canonical_json_sha256(
        {
            "domain": domain,
            "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,
            "frame": _frame_payload(frame),
        }
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_inspected_layer_payload`

**Purpose:** Implements `inspected layer payload` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _inspected_layer_payload(layer: GpuInspectedLayer) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `layer` | positional-or-keyword | `GpuInspectedLayer` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>            "logical_name": logical_name,<br>            "source_layer": _strict_string(reference.source_layer, "GPU source layer"),<br>            "driver": _strict_string(reference.driver, "GPU driver"),<br>            "summary": asdict(summary),<br>            "source_data_sha256": _source_frame_sha256(<br>                "landscout.cnig_feature_codes.gpu_source_layer", data<br>            ),<br>        }`
- Explicit raise paths:
  - `PlanningFeatureCodeError("GPU inspected layer data is invalid")` under lexical guard `not isinstance(data, gpd.GeoDataFrame)`.
  - `re-raise`.
  - `PlanningFeatureCodeError(<br>            "GPU inspected-layer context cannot be serialized"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_planning_document_context_sha256` via `_inspected_layer_payload`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_planning_document_context_sha256` via `_inspected_layer_payload`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_strict_string` | `landscout.stages.resolve_planning_feature_codes._strict_string` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `asdict` | `dataclasses.asdict` |
| `_source_frame_sha256` | `landscout.stages.resolve_planning_feature_codes._source_frame_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_source_frame_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _inspected_layer_payload(layer: GpuInspectedLayer) -> dict[str, object]:
    try:
        logical_name = _strict_string(layer.logical_name, "GPU logical layer name")
        reference = layer.reference
        summary = layer.summary
        data = layer.data
        if not isinstance(data, gpd.GeoDataFrame):
            raise PlanningFeatureCodeError("GPU inspected layer data is invalid")
        return {
            "logical_name": logical_name,
            "source_layer": _strict_string(reference.source_layer, "GPU source layer"),
            "driver": _strict_string(reference.driver, "GPU driver"),
            "summary": asdict(summary),
            "source_data_sha256": _source_frame_sha256(
                "landscout.cnig_feature_codes.gpu_source_layer", data
            ),
        }
    except PlanningFeatureCodeError:
        raise
    except Exception as error:
        raise PlanningFeatureCodeError(
            "GPU inspected-layer context cannot be serialized"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_planning_document_context_sha256`

**Purpose:** Implements `planning document context sha256` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _planning_document_context_sha256(document: GpuPlanningDocument) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `document` | positional-or-keyword | `GpuPlanningDocument` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256(<br>            {<br>                "domain": "landscout.cnig_feature_codes.planning_document_input",<br>                "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,<br>                "document_metadata": asdict(archive.document),<br>                "archive": {<br>                    "filename": archive.filename,<br>                    "archive_format": archive.archive_format,<br>                    "file_size": archive.file_size,<br>                    "sha256": archive.sha256,<br>                },<br>                "standard_models": sorted(document.extraction.standard_models),<br>                "spatial_references": spatial_references,<br>                "zoning": _inspected_layer_payload(document.zoning),<br>                "related_layers": related,<br>            }<br>        )`
- Explicit raise paths:
  - `re-raise`.
  - `PlanningFeatureCodeError(<br>            "Planning-document context cannot be hashed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_planning_document_context_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_planning_document_context_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `sorted` | `unresolved local/third-party receiver; no ownership inferred` |
| `_inspected_layer_payload` | `landscout.stages.resolve_planning_feature_codes._inspected_layer_payload` |
| `_strict_string` | `landscout.stages.resolve_planning_feature_codes._strict_string` |
| `_canonical_json_sha256` | `landscout.stages.resolve_planning_feature_codes._canonical_json_sha256` |
| `asdict` | `dataclasses.asdict` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_json_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _planning_document_context_sha256(document: GpuPlanningDocument) -> str:
    try:
        archive = document.extraction.archive
        related = sorted(
            (_inspected_layer_payload(layer) for layer in document.related_layers),
            key=lambda item: str(item["logical_name"]),
        )
        spatial_references = sorted(
            (
                {
                    "source_layer": _strict_string(
                        reference.source_layer, "GPU spatial source layer"
                    ),
                    "driver": _strict_string(
                        reference.driver, "GPU spatial source driver"
                    ),
                }
                for reference in document.all_spatial_layers
            ),
            key=lambda item: (str(item["source_layer"]), str(item["driver"])),
        )
        return _canonical_json_sha256(
            {
                "domain": "landscout.cnig_feature_codes.planning_document_input",
                "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,
                "document_metadata": asdict(archive.document),
                "archive": {
                    "filename": archive.filename,
                    "archive_format": archive.archive_format,
                    "file_size": archive.file_size,
                    "sha256": archive.sha256,
                },
                "standard_models": sorted(document.extraction.standard_models),
                "spatial_references": spatial_references,
                "zoning": _inspected_layer_payload(document.zoning),
                "related_layers": related,
            }
        )
    except PlanningFeatureCodeError:
        raise
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Planning-document context cannot be hashed safely"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_parcel_identity_input_sha256`

**Purpose:** Implements `parcel identity input sha256` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _parcel_identity_input_sha256(parcels: gpd.GeoDataFrame) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_source_frame_sha256(<br>        "landscout.cnig_feature_codes.parcel_identity_input", identity<br>    )`
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>            "Parcel identity input cannot be serialized"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_parcel_identity_input_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_parcel_identity_input_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `gpd.GeoDataFrame` | `geopandas.GeoDataFrame` |
| `parcels[["parcel_id", "geometry"]].copy` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `_source_frame_sha256` | `landscout.stages.resolve_planning_feature_codes._source_frame_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_source_frame_sha256` |
| CRS/geometry/spatial calculation | `parcels[["parcel_id", "geometry"]].copy` |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _parcel_identity_input_sha256(parcels: gpd.GeoDataFrame) -> str:
    try:
        identity = gpd.GeoDataFrame(
            parcels[["parcel_id", "geometry"]].copy(deep=True),
            geometry="geometry",
            crs=parcels.crs,
        )
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Parcel identity input cannot be serialized"
        ) from error
    return _source_frame_sha256(
        "landscout.cnig_feature_codes.parcel_identity_input", identity
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_normalized_catalogs_input_sha256`

**Purpose:** Implements `normalized catalogs input sha256` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _normalized_catalogs_input_sha256(
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `surface_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `line_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `point_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256(<br>        {<br>            "domain": "landscout.cnig_feature_codes.normalized_catalogs_input",<br>            "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,<br>            "surface": _frame_payload(surface_features),<br>            "line": _frame_payload(line_features),<br>            "point": _frame_payload(point_features),<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_normalized_catalogs_input_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_normalized_catalogs_input_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_json_sha256` | `landscout.stages.resolve_planning_feature_codes._canonical_json_sha256` |
| `_frame_payload` | `landscout.stages.resolve_planning_feature_codes._frame_payload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_json_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _normalized_catalogs_input_sha256(
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.cnig_feature_codes.normalized_catalogs_input",
            "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,
            "surface": _frame_payload(surface_features),
            "line": _frame_payload(line_features),
            "point": _frame_payload(point_features),
        }
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_normalized_relations_input_sha256`

**Purpose:** Implements `normalized relations input sha256` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _normalized_relations_input_sha256(relations: pd.DataFrame) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_source_frame_sha256(<br>        "landscout.cnig_feature_codes.normalized_relations_input", relations<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_normalized_relations_input_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_normalized_relations_input_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_source_frame_sha256` | `landscout.stages.resolve_planning_feature_codes._source_frame_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_source_frame_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _normalized_relations_input_sha256(relations: pd.DataFrame) -> str:
    return _source_frame_sha256(
        "landscout.cnig_feature_codes.normalized_relations_input", relations
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_component_metadata`

**Purpose:** Implements `component metadata` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _component_metadata(result: PlanningFeatureCodeResult) -> dict[str, object]:
```

- Exact decorators: none.
- Declared return annotation: `dict[str, object]`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `{<br>        "result_hash_schema_version": result.result_hash_schema_version,<br>        "profile_schema_version": result.profile_schema_version,<br>        "profile": result.profile,<br>        "standard_model": result.standard_model,<br>        "profile_sha256": result.profile_sha256,<br>        "source_document_id": result.source_document_id,<br>        "source_archive_sha256": result.source_archive_sha256,<br>        "planning_document_context_sha256": (result.planning_document_context_sha256),<br>        "parcel_identity_input_sha256": result.parcel_identity_input_sha256,<br>        "normalized_catalogs_input_sha256": (result.normalized_catalogs_input_sha256),<br>        "normalized_relations_input_sha256": (result.normalized_relations_input_sha256),<br>        "gpu_related_source_files_sha256": (result.gpu_related_source_files_sha256),<br>        "expected_relations_content_sha256": (result.expected_relations_content_sha256),<br>    }`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_frame_sha256` via `_component_metadata`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_frame_sha256` via `_component_metadata`
- direct call: `landscout.stages.resolve_planning_feature_codes::_complete_sha256` via `_component_metadata`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_complete_sha256` via `_component_metadata`

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
def _component_metadata(result: PlanningFeatureCodeResult) -> dict[str, object]:
    return {
        "result_hash_schema_version": result.result_hash_schema_version,
        "profile_schema_version": result.profile_schema_version,
        "profile": result.profile,
        "standard_model": result.standard_model,
        "profile_sha256": result.profile_sha256,
        "source_document_id": result.source_document_id,
        "source_archive_sha256": result.source_archive_sha256,
        "planning_document_context_sha256": (result.planning_document_context_sha256),
        "parcel_identity_input_sha256": result.parcel_identity_input_sha256,
        "normalized_catalogs_input_sha256": (result.normalized_catalogs_input_sha256),
        "normalized_relations_input_sha256": (result.normalized_relations_input_sha256),
        "gpu_related_source_files_sha256": (result.gpu_related_source_files_sha256),
        "expected_relations_content_sha256": (result.expected_relations_content_sha256),
    }
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_frame_sha256`

**Purpose:** Implements `frame sha256` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _frame_sha256(
    domain: str,
    result: PlanningFeatureCodeResult,
    frame: pd.DataFrame,
) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `domain` | positional-or-keyword | `str` | `required` |
| `result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |
| `frame` | positional-or-keyword | `pd.DataFrame` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256(<br>        {<br>            "domain": domain,<br>            **_component_metadata(result),<br>            "frame": _frame_payload(frame),<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_result_with_hashes` via `_frame_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_result_with_hashes` via `_frame_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_json_sha256` | `landscout.stages.resolve_planning_feature_codes._canonical_json_sha256` |
| `_component_metadata` | `landscout.stages.resolve_planning_feature_codes._component_metadata` |
| `_frame_payload` | `landscout.stages.resolve_planning_feature_codes._frame_payload` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_json_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _frame_sha256(
    domain: str,
    result: PlanningFeatureCodeResult,
    frame: pd.DataFrame,
) -> str:
    return _canonical_json_sha256(
        {
            "domain": domain,
            **_component_metadata(result),
            "frame": _frame_payload(frame),
        }
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_complete_sha256`

**Purpose:** Implements `complete sha256` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _complete_sha256(result: PlanningFeatureCodeResult) -> str:
```

- Exact decorators: none.
- Declared return annotation: `str`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `_canonical_json_sha256(<br>        {<br>            "domain": "landscout.cnig_feature_codes.result",<br>            **_component_metadata(result),<br>            "code_dictionary_content_sha256": result.code_dictionary_content_sha256,<br>            "surface_features_content_sha256": result.surface_features_content_sha256,<br>            "line_features_content_sha256": result.line_features_content_sha256,<br>            "point_features_content_sha256": result.point_features_content_sha256,<br>            "relations_content_sha256": result.relations_content_sha256,<br>        }<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_result_with_hashes` via `_complete_sha256`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_result_with_hashes` via `_complete_sha256`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_json_sha256` | `landscout.stages.resolve_planning_feature_codes._canonical_json_sha256` |
| `_component_metadata` | `landscout.stages.resolve_planning_feature_codes._component_metadata` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_canonical_json_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _complete_sha256(result: PlanningFeatureCodeResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.cnig_feature_codes.result",
            **_component_metadata(result),
            "code_dictionary_content_sha256": result.code_dictionary_content_sha256,
            "surface_features_content_sha256": result.surface_features_content_sha256,
            "line_features_content_sha256": result.line_features_content_sha256,
            "point_features_content_sha256": result.point_features_content_sha256,
            "relations_content_sha256": result.relations_content_sha256,
        }
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_result_with_hashes`

**Purpose:** Implements `result with hashes` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _result_with_hashes(result: PlanningFeatureCodeResult) -> PlanningFeatureCodeResult:
```

- Exact decorators: none.
- Declared return annotation: `PlanningFeatureCodeResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `replace(<br>        component, complete_result_content_sha256=_complete_sha256(component)<br>    )`
- No explicit `raise` expression in this callable; delegated calls may still raise their documented controlled errors.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_result_with_hashes`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `_result_with_hashes`
- direct call: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `_result_with_hashes`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_validate_result_envelope` via `_result_with_hashes`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_coordinated_output_hash_mutation_is_rejected` via `_result_with_hashes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_coordinated_output_hash_mutation_is_rejected` via `_result_with_hashes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_source_binding_hashes_bind_every_component_hash` via `_result_with_hashes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_source_binding_hashes_bind_every_component_hash` via `_result_with_hashes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::_canonical_empty_coded_result` via `_result_with_hashes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_canonical_empty_coded_result` via `_result_with_hashes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_dictionary_schema_is_explicit` via `_result_with_hashes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_dictionary_schema_is_explicit` via `_result_with_hashes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_dictionary_rows_are_intrinsically_validated` via `_result_with_hashes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_dictionary_rows_are_intrinsically_validated` via `_result_with_hashes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_scalar_lineage_contracts_are_intrinsic` via `_result_with_hashes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_scalar_lineage_contracts_are_intrinsic` via `_result_with_hashes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic` via `_result_with_hashes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic` via `_result_with_hashes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `replace` | `dataclasses.replace` |
| `_frame_sha256` | `landscout.stages.resolve_planning_feature_codes._frame_sha256` |
| `_complete_sha256` | `landscout.stages.resolve_planning_feature_codes._complete_sha256` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_frame_sha256`<br>`_complete_sha256` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

```python
def _result_with_hashes(result: PlanningFeatureCodeResult) -> PlanningFeatureCodeResult:
    component = replace(
        result,
        code_dictionary_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.dictionary", result, result.code_dictionary
        ),
        surface_features_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.surface", result, result.surface_features
        ),
        line_features_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.line", result, result.line_features
        ),
        point_features_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.point", result, result.point_features
        ),
        relations_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.relations", result, result.relations
        ),
    )
    return replace(
        component, complete_result_content_sha256=_complete_sha256(component)
    )
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_build_result`

**Purpose:** Implements `build result` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

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

- Exact decorators: none.
- Declared return annotation: `PlanningFeatureCodeResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `surface_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `line_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `point_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `code_profile` | positional-or-keyword | `CnigFeatureCodeProfile` | `required` |
| `factual_validation` | positional-or-keyword | `PlanningFeatureInputValidation \| None` | `None` |

**Return and exception contract**

- Exact observed return expressions:
  - `_result_with_hashes(result)`
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>            f"Planning document standard {standard!r} differs from code-profile standard"<br>        )` under lexical guard `standard != code_profile.standard_model`.
  - `PlanningFeatureCodeError(<br>                f"Normalized planning-feature inputs are invalid: {error}"<br>            )` under lexical guard `factual_validation is None`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `_build_result`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `_build_result`
- direct call: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `_build_result`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `_build_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_planning_standard` | `landscout.stages.resolve_planning_feature_codes._planning_standard` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `validate_normalized_planning_feature_inputs` | `landscout.stages.enrich_planning_features.validate_normalized_planning_feature_inputs` |
| `_validate_catalog_document_lineage` | `landscout.stages.resolve_planning_feature_codes._validate_catalog_document_lineage` |
| `_profile_sha256` | `landscout.stages.resolve_planning_feature_codes._profile_sha256` |
| `_coded_catalog` | `landscout.stages.resolve_planning_feature_codes._coded_catalog` |
| `_coded_relations` | `landscout.stages.resolve_planning_feature_codes._coded_relations` |
| `PlanningFeatureCodeResult` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult` |
| `_planning_document_context_sha256` | `landscout.stages.resolve_planning_feature_codes._planning_document_context_sha256` |
| `_parcel_identity_input_sha256` | `landscout.stages.resolve_planning_feature_codes._parcel_identity_input_sha256` |
| `_normalized_catalogs_input_sha256` | `landscout.stages.resolve_planning_feature_codes._normalized_catalogs_input_sha256` |
| `_normalized_relations_input_sha256` | `landscout.stages.resolve_planning_feature_codes._normalized_relations_input_sha256` |
| `_dictionary` | `landscout.stages.resolve_planning_feature_codes._dictionary` |
| `_result_with_hashes` | `landscout.stages.resolve_planning_feature_codes._result_with_hashes` |

**Source-observed side-effect matrix**

A category is claimed only when the exact call/assignment evidence is listed. Empty evidence means no direct operation of that category is present in this callable.

| Category | Exact evidence |
|---|---|
| Network I/O | None directly present. |
| Filesystem/archive read or metadata access | None directly present. |
| Filesystem/archive write or publication | None directly present. |
| Hashing/byte identity | `_profile_sha256`<br>`_planning_document_context_sha256`<br>`_parcel_identity_input_sha256`<br>`_normalized_catalogs_input_sha256`<br>`_normalized_relations_input_sha256`<br>`_result_with_hashes` |
| CRS/geometry/spatial calculation | None directly present. |
| External process/environment | None directly present. |
| In-memory mutation | None directly present. |
| Direct parameter mutation | None directly present. |

**Complete source-ordered implementation**

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
    standard = _planning_standard(planning_document)
    if standard != code_profile.standard_model:
        raise PlanningFeatureCodeError(
            f"Planning document standard {standard!r} differs from code-profile standard"
        )
    if factual_validation is None:
        try:
            factual_validation = validate_normalized_planning_feature_inputs(
                planning_document,
                parcels,
                surface_features,
                line_features,
                point_features,
                relations,
            )
        except ValueError as error:
            raise PlanningFeatureCodeError(
                f"Normalized planning-feature inputs are invalid: {error}"
            ) from error
    surface = _validate_catalog_document_lineage(
        surface_features, "surface feature catalog", planning_document, standard
    )
    line = _validate_catalog_document_lineage(
        line_features, "line feature catalog", planning_document, standard
    )
    point = _validate_catalog_document_lineage(
        point_features, "point feature catalog", planning_document, standard
    )
    profile_hash = _profile_sha256(code_profile)
    coded_surface = _coded_catalog(surface, code_profile, profile_hash)
    coded_line = _coded_catalog(line, code_profile, profile_hash)
    coded_point = _coded_catalog(point, code_profile, profile_hash)
    coded_relations = _coded_relations(
        relations, (coded_surface, coded_line, coded_point)
    )
    archive = planning_document.extraction.archive
    result = PlanningFeatureCodeResult(
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        profile_schema_version=code_profile.schema_version,
        profile=code_profile.profile,
        standard_model=standard,
        profile_sha256=profile_hash,
        source_document_id=archive.document.document_id,
        source_archive_sha256=archive.sha256,
        planning_document_context_sha256=_planning_document_context_sha256(
            planning_document
        ),
        parcel_identity_input_sha256=_parcel_identity_input_sha256(parcels),
        normalized_catalogs_input_sha256=_normalized_catalogs_input_sha256(
            surface_features, line_features, point_features
        ),
        normalized_relations_input_sha256=_normalized_relations_input_sha256(relations),
        gpu_related_source_files_sha256=(
            factual_validation.gpu_related_source_files_sha256
        ),
        expected_relations_content_sha256=(
            factual_validation.expected_relations_content_sha256
        ),
        code_dictionary_content_sha256="",
        surface_features_content_sha256="",
        line_features_content_sha256="",
        point_features_content_sha256="",
        relations_content_sha256="",
        complete_result_content_sha256="",
        code_dictionary=_dictionary(code_profile, profile_hash),
        surface_features=coded_surface,
        line_features=coded_line,
        point_features=coded_point,
        relations=coded_relations,
    )
    return _result_with_hashes(result)
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_validate_result_envelope`

**Purpose:** Implements `validate result envelope` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _validate_result_envelope(result: PlanningFeatureCodeResult) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningFeatureCodeError("result must be a PlanningFeatureCodeResult")` under lexical guard `type(result) is not PlanningFeatureCodeResult`.
  - `PlanningFeatureCodeError(f"unsupported {label}: {version!r}")` under lexical guard `type(version) is not int or version != expected_version`.
  - `PlanningFeatureCodeError("result standard model is invalid")` under lexical guard `result.standard_model != STANDARD_MODEL`.
  - `PlanningFeatureCodeError(f"{field} must be a lowercase SHA256")` under lexical guard `not isinstance(value, str) or _SHA_PATTERN.fullmatch(value) is None`.
  - `PlanningFeatureCodeError(str(error))`.
  - `PlanningFeatureCodeError(str(error))`.
  - `PlanningFeatureCodeError(f"result hash {field} is invalid")` under lexical guard `getattr(result, field) != getattr(rebuilt_hashes, field)`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result_envelope` via `_validate_result_envelope`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result_envelope` via `_validate_result_envelope`
- direct call: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `_validate_result_envelope`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `_validate_result_envelope`
- direct call: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `_validate_result_envelope`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `_validate_result_envelope`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `type` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `_strict_string` | `landscout.stages.resolve_planning_feature_codes._strict_string` |
| `field.endswith` | `unresolved local/third-party receiver; no ownership inferred` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `isinstance` | `unresolved local/third-party receiver; no ownership inferred` |
| `_SHA_PATTERN.fullmatch` | `unresolved local/third-party receiver; no ownership inferred` |
| `_validate_code_dictionary` | `landscout.stages.resolve_planning_feature_codes._validate_code_dictionary` |
| `cast` | `typing.cast` |
| `validate_canonical_frame_schema` | `landscout.common.planning_feature_schema.validate_canonical_frame_schema` |
| `feature_columns` | `landscout.common.planning_feature_schema.feature_columns` |
| `feature_dtypes` | `landscout.common.planning_feature_schema.feature_dtypes` |
| `str` | `unresolved local/third-party receiver; no ownership inferred` |
| `relation_columns` | `landscout.common.planning_feature_schema.relation_columns` |
| `relation_dtypes` | `landscout.common.planning_feature_schema.relation_dtypes` |
| `_validate_coded_meaning_rows` | `landscout.stages.resolve_planning_feature_codes._validate_coded_meaning_rows` |
| `_result_with_hashes` | `landscout.stages.resolve_planning_feature_codes._result_with_hashes` |

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
def _validate_result_envelope(result: PlanningFeatureCodeResult) -> None:
    if type(result) is not PlanningFeatureCodeResult:
        raise PlanningFeatureCodeError("result must be a PlanningFeatureCodeResult")
    for version, expected_version, label in (
        (
            result.result_hash_schema_version,
            RESULT_HASH_SCHEMA_VERSION,
            "result hash schema version",
        ),
        (
            result.profile_schema_version,
            PROFILE_SCHEMA_VERSION,
            "profile schema version",
        ),
    ):
        if type(version) is not int or version != expected_version:
            raise PlanningFeatureCodeError(f"unsupported {label}: {version!r}")
    if result.standard_model != STANDARD_MODEL:
        raise PlanningFeatureCodeError("result standard model is invalid")
    for value, label in (
        (result.profile, "result profile"),
        (result.source_document_id, "result source document ID"),
    ):
        _strict_string(value, label)
    for field in PlanningFeatureCodeResult.__dataclass_fields__:
        if not field.endswith("_sha256"):
            continue
        value = getattr(result, field)
        if not isinstance(value, str) or _SHA_PATTERN.fullmatch(value) is None:
            raise PlanningFeatureCodeError(f"{field} must be a lowercase SHA256")
    dictionary = _validate_code_dictionary(result)
    for frame, label, kind in (
        (result.surface_features, "surface features", "SURFACE"),
        (result.line_features, "line features", "LINE"),
        (result.point_features, "point features", "POINT"),
    ):
        geometry_kind = cast(GeometryKind, kind)
        try:
            validate_canonical_frame_schema(
                frame,
                columns=feature_columns(geometry_kind),
                dtypes=feature_dtypes(geometry_kind, frame=frame),
                label=label,
                geospatial=True,
            )
        except (TypeError, ValueError) as error:
            raise PlanningFeatureCodeError(str(error)) from error
    try:
        validate_canonical_frame_schema(
            result.relations,
            columns=relation_columns(),
            dtypes=relation_dtypes(),
            label="coded relations",
            geospatial=False,
        )
    except (TypeError, ValueError) as error:
        raise PlanningFeatureCodeError(str(error)) from error
    _validate_coded_meaning_rows(result, dictionary)
    rebuilt_hashes = _result_with_hashes(result)
    for field in (
        "code_dictionary_content_sha256",
        "surface_features_content_sha256",
        "line_features_content_sha256",
        "point_features_content_sha256",
        "relations_content_sha256",
        "complete_result_content_sha256",
    ):
        if getattr(result, field) != getattr(rebuilt_hashes, field):
            raise PlanningFeatureCodeError(f"result hash {field} is invalid")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_planning_feature_code_result_envelope`

**Purpose:** Validate one coded-result envelope without rebuilding factual sources.

**Exact signature**

```python
def validate_planning_feature_code_result_envelope(
    result: PlanningFeatureCodeResult,
) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `re-raise`.
  - `PlanningFeatureCodeError(<br>            "Planning feature code result envelope is invalid"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`
- import: `landscout.stages.apply_bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result_envelope,
)`
- direct call: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `validate_planning_feature_code_result_envelope`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::load_bess_planning_feature_application_artifacts` via `validate_planning_feature_code_result_envelope`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_result_envelope` | `landscout.stages.resolve_planning_feature_codes._validate_result_envelope` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |

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
def validate_planning_feature_code_result_envelope(
    result: PlanningFeatureCodeResult,
) -> None:
    """Validate one coded-result envelope without rebuilding factual sources."""

    try:
        _validate_result_envelope(result)
    except PlanningFeatureCodeError:
        raise
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Planning feature code result envelope is invalid"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `_compare_frame`

**Purpose:** Implements `compare frame` within the file role: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

**Exact signature**

```python
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
```

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `actual` | positional-or-keyword | `pd.DataFrame` | `required` |
| `expected` | positional-or-keyword | `pd.DataFrame` | `required` |
| `label` | positional-or-keyword | `str` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningFeatureCodeError(f"{label} differs from rebuilt source result")` under lexical guard `_canonical_value(_frame_payload(actual)) != _canonical_value(<br>        _frame_payload(expected)<br>    )`.

**Qualified relationships**

Inbound conservative repository consumers:
- direct call: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `_compare_frame`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `_compare_frame`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_canonical_value` | `landscout.stages.resolve_planning_feature_codes._canonical_value` |
| `_frame_payload` | `landscout.stages.resolve_planning_feature_codes._frame_payload` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |

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
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _canonical_value(_frame_payload(actual)) != _canonical_value(
        _frame_payload(expected)
    ):
        raise PlanningFeatureCodeError(f"{label} differs from rebuilt source result")
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `validate_planning_feature_code_result`

**Purpose:** Rebuild and validate a coded result from every factual source input.

**Exact signature**

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

- Exact decorators: none.
- Declared return annotation: `None`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `surface_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `line_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `point_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `code_profile` | positional-or-keyword | `CnigFeatureCodeProfile \| str \| Path` | `required` |
| `result` | positional-or-keyword | `PlanningFeatureCodeResult` | `required` |

**Return and exception contract**

- No explicit return expression; normal completion therefore returns `None` unless a framework consumes the callable specially.
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>                    f"result {field} differs from rebuilt source result"<br>                )` under lexical guard `getattr(result, field) != getattr(expected, field)`.
  - `re-raise`.
  - `PlanningFeatureCodeError(<br>            "Planning-feature code result validation failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`
- import: `landscout.stages.bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result,
)`
- direct call: `landscout.stages.bess_planning_feature_policy::_validate_coded_source` via `validate_planning_feature_code_result`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_coded_source` via `validate_planning_feature_code_result`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    validate_planning_feature_code_result as _public_validate_planning_feature_code_result,
)`
- direct call: `tests.unit.test_resolve_planning_feature_codes::validate_planning_feature_code_result` via `_public_validate_planning_feature_code_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::validate_planning_feature_code_result` via `_public_validate_planning_feature_code_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_step_7d_3_1_output_integrates_with_public_coding_api` via `_public_validate_planning_feature_code_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_step_7d_3_1_output_integrates_with_public_coding_api` via `_public_validate_planning_feature_code_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_source_input_hash_mutation_is_rejected` via `_public_validate_planning_feature_code_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_source_input_hash_mutation_is_rejected` via `_public_validate_planning_feature_code_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_parcel_source_change_invalidates_coded_result` via `_public_validate_planning_feature_code_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_parcel_source_change_invalidates_coded_result` via `_public_validate_planning_feature_code_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_gpu_document_context_change_invalidates_coded_result` via `_public_validate_planning_feature_code_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_gpu_document_context_change_invalidates_coded_result` via `_public_validate_planning_feature_code_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent` via `_public_validate_planning_feature_code_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent` via `_public_validate_planning_feature_code_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_normalized_relation_change_invalidates_coded_result` via `_public_validate_planning_feature_code_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_normalized_relation_change_invalidates_coded_result` via `_public_validate_planning_feature_code_result`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_parquet_readback_preserves_source_hash_envelope` via `_public_validate_planning_feature_code_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_parquet_readback_preserves_source_hash_envelope` via `_public_validate_planning_feature_code_result`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_public_api_signatures_remain_source_complete` via `_public_validate_planning_feature_code_result`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_validate_result_envelope` | `landscout.stages.resolve_planning_feature_codes._validate_result_envelope` |
| `_build_result` | `landscout.stages.resolve_planning_feature_codes._build_result` |
| `_resolved_profile` | `landscout.stages.resolve_planning_feature_codes._resolved_profile` |
| `getattr` | `unresolved local/third-party receiver; no ownership inferred` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `_compare_frame` | `landscout.stages.resolve_planning_feature_codes._compare_frame` |

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
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    result: PlanningFeatureCodeResult,
) -> None:
    """Rebuild and validate a coded result from every factual source input."""

    try:
        _validate_result_envelope(result)
        expected = _build_result(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            _resolved_profile(code_profile),
        )
        scalar_fields = (
            "result_hash_schema_version",
            "profile_schema_version",
            "profile",
            "standard_model",
            "profile_sha256",
            "source_document_id",
            "source_archive_sha256",
            "planning_document_context_sha256",
            "parcel_identity_input_sha256",
            "normalized_catalogs_input_sha256",
            "normalized_relations_input_sha256",
            "gpu_related_source_files_sha256",
            "expected_relations_content_sha256",
            "code_dictionary_content_sha256",
            "surface_features_content_sha256",
            "line_features_content_sha256",
            "point_features_content_sha256",
            "relations_content_sha256",
            "complete_result_content_sha256",
        )
        for field in scalar_fields:
            if getattr(result, field) != getattr(expected, field):
                raise PlanningFeatureCodeError(
                    f"result {field} differs from rebuilt source result"
                )
        for actual, rebuilt, label in (
            (result.code_dictionary, expected.code_dictionary, "code dictionary"),
            (result.surface_features, expected.surface_features, "surface features"),
            (result.line_features, expected.line_features, "line features"),
            (result.point_features, expected.point_features, "point features"),
            (result.relations, expected.relations, "coded relations"),
        ):
            _compare_frame(actual, rebuilt, label)
    except PlanningFeatureCodeError:
        raise
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Planning-feature code result validation failed safely"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.

### `resolve_planning_feature_codes`

**Purpose:** Attach exact official CNIG meanings without interpreting their impact.

**Exact signature**

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

- Exact decorators: none.
- Declared return annotation: `PlanningFeatureCodeResult`.

**Inputs**

| Name | Kind | Annotation | Default |
|---|---|---|---|
| `planning_document` | positional-or-keyword | `GpuPlanningDocument` | `required` |
| `parcels` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `surface_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `line_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `point_features` | positional-or-keyword | `gpd.GeoDataFrame` | `required` |
| `relations` | positional-or-keyword | `pd.DataFrame` | `required` |
| `code_profile` | positional-or-keyword | `CnigFeatureCodeProfile \| str \| Path` | `required` |

**Return and exception contract**

- Exact observed return expressions:
  - `result`
- Explicit raise paths:
  - `PlanningFeatureCodeError(<br>                f"Planning document standard {standard!r} differs from "<br>                "code-profile standard"<br>            )` under lexical guard `standard != profile.standard_model`.
  - `re-raise`.
  - `PlanningFeatureCodeError(<br>            f"Planning-feature code resolution failed: {error}"<br>        )`.
  - `PlanningFeatureCodeError(<br>            "Planning-feature code resolution failed safely"<br>        )`.

**Qualified relationships**

Inbound conservative repository consumers:
- public re-export: `landscout.stages::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`
- import: `tests.unit.test_bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
)`
- direct call: `tests.unit.test_bess_planning_feature_policy::_compiled_fixture` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_compiled_fixture` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::_checked_in_policy_result` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_checked_in_policy_result` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_missing_policy_pair_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_missing_policy_pair_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_extra_policy_pair_is_rejected_without_type_fallback` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_extra_policy_pair_is_rejected_without_type_fallback` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_duplicate_policy_pair_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_duplicate_policy_pair_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_prescription_information_code_spaces_remain_separate` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_prescription_information_code_spaces_remain_separate` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_official_meaning_mismatch_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_official_meaning_mismatch_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_invalid_or_legal_conclusion_status_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_invalid_or_legal_conclusion_status_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_invalid_confidence_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_invalid_confidence_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_status_priority_contract_is_strict` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_status_priority_contract_is_strict` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_unknown_yaml_field_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_unknown_yaml_field_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_noncanonical_whitespace_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_noncanonical_whitespace_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_malformed_sha256_is_rejected` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_malformed_sha256_is_rejected` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_policy_entries_require_deterministic_order` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_entries_require_deterministic_order` via `resolve_planning_feature_codes`
- direct call: `tests.unit.test_bess_planning_feature_policy::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `resolve_planning_feature_codes`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    resolve_planning_feature_codes as _public_resolve_planning_feature_codes,
)`
- direct call: `tests.unit.test_resolve_planning_feature_codes::resolve_planning_feature_codes` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::resolve_planning_feature_codes` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_multi_geometries_are_accepted` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_multi_geometries_are_accepted` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_empty_optional_catalogs_preserve_schema_and_crs` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_empty_optional_catalogs_preserve_schema_and_crs` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_valid_relation_types_are_retained` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_valid_relation_types_are_retained` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_step_7d_3_1_output_integrates_with_public_coding_api` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_step_7d_3_1_output_integrates_with_public_coding_api` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_coded_result_persists_all_source_input_hashes` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_coded_result_persists_all_source_input_hashes` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_source_input_hash_mutation_is_rejected` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_source_input_hash_mutation_is_rejected` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_gpu_related_source_hash_is_deterministic_across_cache_roots` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_gpu_related_source_hash_is_deterministic_across_cache_roots` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_source_binding_hashes_bind_every_component_hash` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_source_binding_hashes_bind_every_component_hash` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_parcel_source_change_invalidates_coded_result` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_parcel_source_change_invalidates_coded_result` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_gpu_document_context_change_invalidates_coded_result` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_gpu_document_context_change_invalidates_coded_result` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_normalized_relation_change_invalidates_coded_result` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_normalized_relation_change_invalidates_coded_result` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_coding_api_rejects_relation_set_not_rebuilt_from_geometry` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_coding_api_rejects_relation_set_not_rebuilt_from_geometry` via `_public_resolve_planning_feature_codes`
- direct call: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_parquet_readback_preserves_source_hash_envelope` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_parquet_readback_preserves_source_hash_envelope` via `_public_resolve_planning_feature_codes`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_schema_v5_public_api_signatures_remain_source_complete` via `_public_resolve_planning_feature_codes`

Outbound call expressions and conservative ownership:
| Exact call expression | Resolved owner |
|---|---|
| `_resolved_profile` | `landscout.stages.resolve_planning_feature_codes._resolved_profile` |
| `_planning_standard` | `landscout.stages.resolve_planning_feature_codes._planning_standard` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `validate_normalized_planning_feature_inputs` | `landscout.stages.enrich_planning_features.validate_normalized_planning_feature_inputs` |
| `_build_result` | `landscout.stages.resolve_planning_feature_codes._build_result` |
| `_validate_result_envelope` | `landscout.stages.resolve_planning_feature_codes._validate_result_envelope` |

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
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
) -> PlanningFeatureCodeResult:
    """Attach exact official CNIG meanings without interpreting their impact."""

    try:
        profile = _resolved_profile(code_profile)
        standard = _planning_standard(planning_document)
        if standard != profile.standard_model:
            raise PlanningFeatureCodeError(
                f"Planning document standard {standard!r} differs from "
                "code-profile standard"
            )
        factual_validation = validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
        )
        result = _build_result(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            profile,
            factual_validation,
        )
        _validate_result_envelope(result)
        return result
    except PlanningFeatureCodeError:
        raise
    except ValueError as error:
        raise PlanningFeatureCodeError(
            f"Planning-feature code resolution failed: {error}"
        ) from error
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Planning-feature code resolution failed safely"
        ) from error
```

**Business boundary**

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.


## 7. Validation and data-contract summary

- Canonical schema/mapping declarations inventoried above: `PROFILE_SCHEMA_VERSION`, `RESULT_HASH_SCHEMA_VERSION`, `CODE_DICTIONARY_COLUMNS`, `CODE_DICTIONARY_DTYPES`, `CODE_DICTIONARY_SCHEMA_SIGNATURE`.
- Exact value/null/index/CRS/geometry/hash behavior is claimed only where the reproduced validators and operations enforce it.

## 8. Public exports and package ownership

Exact `__all__` members and local origins:

| Export | Local origin binding |
|---|---|
| `CnigFeatureCodeProfile` | `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile` |
| `PlanningFeatureCodeError` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError` |
| `PlanningFeatureCodeResult` | `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult` |
| `load_cnig_feature_code_profile` | `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile` |
| `resolve_planning_feature_codes` | `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes` |
| `validate_planning_feature_code_result` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result` |
| `validate_planning_feature_code_result_envelope` | `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result_envelope` |

## 9. Trust, provenance, side effects, and business boundary

- The stage is limited to the factual transformation, proxy evidence, diagnostic, or policy application stated in its role. It does not create cross-criterion ranking, scoring, ownership/contact, or legal authorization.
- Configured identity, textual lineage, byte identity, physical source reconstruction, local envelope validation, and source-complete validation remain distinct trust levels. This companion attributes only the levels implemented in the exact source.
- Filesystem, network, hashing, CRS/geometry, process, mutation, and expected-exception evidence is listed per callable; an empty category is not silently promoted to an effect.

## 10. Change impact

A source-byte change invalidates the SHA above and requires re-auditing imports/re-exports, constants/aliases/schemas, model fields/immutability, qualified callers, side effects, controlled errors, tests, source/artifact locks, and the exact full snapshot.

## 11. Exact complete current file content

The following UTF-8 snapshot is the complete current repository file, not an excerpt. Its raw-byte SHA256 is the value in **File identity**.

```python
"""Resolve factual GPU planning-feature codes against an offline CNIG snapshot."""

from __future__ import annotations

import json
import math
import re
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import asdict, dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from numbers import Integral, Real
from pathlib import Path
from typing import Literal, cast

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, model_validator
from shapely import to_wkb  # type: ignore[import-untyped]
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]

from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.planning_feature_schema import (
    OFFICIAL_CODE_COLUMNS,
    GeometryKind,
    feature_columns,
    feature_dtypes,
    relation_columns,
    relation_dtypes,
    validate_canonical_frame_schema,
)
from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml
from landscout.sources.gpu_fr import GpuInspectedLayer, GpuPlanningDocument
from landscout.stages.enrich_planning_features import (
    PlanningFeatureInputValidation,
    validate_normalized_planning_feature_inputs,
)

__all__ = [
    "CnigFeatureCodeProfile",
    "PlanningFeatureCodeError",
    "PlanningFeatureCodeResult",
    "load_cnig_feature_code_profile",
    "resolve_planning_feature_codes",
    "validate_planning_feature_code_result",
    "validate_planning_feature_code_result_envelope",
]

PROFILE_SCHEMA_VERSION = 2
RESULT_HASH_SCHEMA_VERSION = 5
STANDARD_MODEL = "CNIG PLU v2017"
OFFICIAL_TEXT_NORMALIZATION = "GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"
PRESCRIPTION_OFFICIAL_SOURCE_URL = (
    "https://www.geoportail-urbanisme.gouv.fr/standard/"
    "cnig_PLU_2017/codes/PrescriptionUrbaType"
)
INFORMATION_OFFICIAL_SOURCE_URL = (
    "https://www.geoportail-urbanisme.gouv.fr/standard/"
    "cnig_PLU_2017/codes/InformationUrbaType"
)

FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
OfficialCodeStatus = Literal["RESOLVED_OFFICIAL", "UNKNOWN_CODE_PAIR"]

CODE_DICTIONARY_COLUMNS = (
    "feature_family",
    "type_code",
    "subtype_code",
    "official_label",
    "legal_reference",
    "regulation_or_annex_reference",
    "official_source_url",
    "profile",
    "profile_sha256",
    "standard_model",
)
CODE_DICTIONARY_DTYPES = tuple("str" for _ in CODE_DICTIONARY_COLUMNS)
CODE_DICTIONARY_SCHEMA_SIGNATURE: dict[str, object] = {
    "columns": list(CODE_DICTIONARY_COLUMNS),
    "dtypes": list(CODE_DICTIONARY_DTYPES),
    "index_class": "pandas.Index",
    "index_names": [None],
    "index_level_dtypes": ["int64"],
}

_CODE_PATTERN = re.compile(r"[0-9]{2}")
_SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
_NULL_REFERENCE_LITERALS = frozenset({"None", "nan", "<NA>"})


class PlanningFeatureCodeError(ValueError):
    """Raised when official code resolution integrity cannot be proven."""


class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be a non-empty exact string")
    return value


def _canonical_official_text(value: str) -> str:
    return " ".join(unicodedata.normalize("NFC", value).split())


def _validate_official_text(value: object, label: str) -> str:
    text = _exact_string(value, label)
    if text != _canonical_official_text(text):
        raise ValueError(
            f"{label} must already use canonical {OFFICIAL_TEXT_NORMALIZATION} text"
        )
    return text


def _validate_optional_official_text(value: object, label: str) -> str | None:
    if value is None:
        return None
    return _validate_official_text(value, label)


class OfficialSourceUrls(_StrictModel):
    prescription: StrictStr
    information: StrictStr

    @model_validator(mode="after")
    def _validate_urls(self) -> OfficialSourceUrls:
        if self.prescription != PRESCRIPTION_OFFICIAL_SOURCE_URL:
            raise ValueError(
                "prescription source URL is not the exact official GPU host endpoint"
            )
        if self.information != INFORMATION_OFFICIAL_SOURCE_URL:
            raise ValueError(
                "information source URL is not the exact official GPU host endpoint"
            )
        return self


class CnigFeatureCodeRecord(_StrictModel):
    feature_family: FeatureFamily
    type_code: StrictStr
    subtype_code: StrictStr
    official_label: StrictStr
    legal_reference: StrictStr | None
    regulation_or_annex_reference: StrictStr | None
    official_source_url: StrictStr

    @model_validator(mode="after")
    def _validate_record(self) -> CnigFeatureCodeRecord:
        for code, label in (
            (self.type_code, "type code"),
            (self.subtype_code, "subtype code"),
        ):
            if _CODE_PATTERN.fullmatch(code) is None:
                raise ValueError(f"{label} must contain exactly two digits")
        _validate_official_text(self.official_label, "official label")
        _validate_optional_official_text(self.legal_reference, "legal reference")
        _validate_optional_official_text(
            self.regulation_or_annex_reference,
            "regulation or annex reference",
        )
        expected_url = (
            PRESCRIPTION_OFFICIAL_SOURCE_URL
            if self.feature_family == "PRESCRIPTION"
            else INFORMATION_OFFICIAL_SOURCE_URL
        )
        if self.official_source_url != expected_url:
            raise ValueError("record source URL is not the exact family endpoint")
        return self


def _record_payload(record: CnigFeatureCodeRecord) -> dict[str, object]:
    return {
        "feature_family": record.feature_family,
        "type_code": record.type_code,
        "subtype_code": record.subtype_code,
        "official_label": record.official_label,
        "legal_reference": record.legal_reference,
        "regulation_or_annex_reference": record.regulation_or_annex_reference,
        "official_source_url": record.official_source_url,
    }


def _canonical_json_sha256(value: object) -> str:
    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Canonical integrity payload cannot be serialized"
        ) from error
    return sha256(encoded).hexdigest()


def _records_sha256(records: Sequence[CnigFeatureCodeRecord]) -> str:
    return _canonical_json_sha256([_record_payload(record) for record in records])


class CnigFeatureCodeProfile(_StrictModel):
    """Strict offline snapshot of official CNIG feature code records."""

    schema_version: StrictInt
    profile: StrictStr = Field(min_length=1)
    standard_model: Literal["CNIG PLU v2017"]
    official_text_normalization: Literal["GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"]
    official_sources: OfficialSourceUrls
    retrieval_date: date
    canonical_records_sha256: StrictStr
    records: tuple[CnigFeatureCodeRecord, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_profile(self) -> CnigFeatureCodeProfile:
        if self.schema_version != PROFILE_SCHEMA_VERSION:
            raise ValueError(
                f"unsupported CNIG feature-code profile schema: {self.schema_version}"
            )
        _exact_string(self.profile, "code profile")
        if _SHA_PATTERN.fullmatch(self.canonical_records_sha256) is None:
            raise ValueError("canonical records SHA256 is invalid")
        keys = [
            (record.feature_family, record.type_code, record.subtype_code)
            for record in self.records
        ]
        if len(set(keys)) != len(keys):
            raise ValueError("configured CNIG code pairs contain a duplicate")
        if keys != sorted(keys):
            raise ValueError("configured CNIG records must use deterministic order")
        if _records_sha256(self.records) != self.canonical_records_sha256:
            raise ValueError("canonical records SHA256 differs from configured records")
        return self


def load_cnig_feature_code_profile(path: str | Path) -> CnigFeatureCodeProfile:
    """Load a strict offline CNIG feature-code profile."""

    try:
        payload = loads_strict_yaml(Path(path).read_bytes())
        if not isinstance(payload, Mapping):
            raise PlanningFeatureCodeError(
                "CNIG feature-code profile must be a mapping"
            )
        return CnigFeatureCodeProfile.model_validate(payload)
    except PlanningFeatureCodeError:
        raise
    except StrictYamlError as error:
        raise PlanningFeatureCodeError(str(error)) from error
    except Exception as error:
        raise PlanningFeatureCodeError(
            "CNIG feature-code profile is invalid"
        ) from error


@dataclass(frozen=True)
class PlanningFeatureCodeResult:
    """Immutable envelope around exact official code resolution outputs."""

    result_hash_schema_version: int
    profile_schema_version: int
    profile: str
    standard_model: str
    profile_sha256: str
    source_document_id: str
    source_archive_sha256: str
    planning_document_context_sha256: str
    parcel_identity_input_sha256: str
    normalized_catalogs_input_sha256: str
    normalized_relations_input_sha256: str
    gpu_related_source_files_sha256: str
    expected_relations_content_sha256: str
    code_dictionary_content_sha256: str
    surface_features_content_sha256: str
    line_features_content_sha256: str
    point_features_content_sha256: str
    relations_content_sha256: str
    complete_result_content_sha256: str
    code_dictionary: pd.DataFrame
    surface_features: gpd.GeoDataFrame
    line_features: gpd.GeoDataFrame
    point_features: gpd.GeoDataFrame
    relations: pd.DataFrame


def _resolved_profile(
    profile: CnigFeatureCodeProfile | str | Path,
) -> CnigFeatureCodeProfile:
    if not isinstance(profile, CnigFeatureCodeProfile):
        return load_cnig_feature_code_profile(profile)
    try:
        payload = profile.model_dump(mode="python", warnings="error")
        return CnigFeatureCodeProfile.model_validate(payload)
    except Exception as error:
        raise PlanningFeatureCodeError(
            "In-memory CNIG feature-code profile is invalid"
        ) from error


def _profile_sha256(profile: CnigFeatureCodeProfile) -> str:
    return _canonical_json_sha256(profile.model_dump(mode="json"))


def _strict_string(value: object, label: str) -> str:
    try:
        return _exact_string(value, label)
    except ValueError as error:
        raise PlanningFeatureCodeError(str(error)) from error


def _planning_standard(document: GpuPlanningDocument) -> str:
    if not isinstance(document, GpuPlanningDocument):
        raise PlanningFeatureCodeError(
            "planning_document must be a GpuPlanningDocument"
        )
    metadata = document.extraction.archive.document
    models = list(document.extraction.standard_models)
    if metadata.standard_model is not None:
        models.append(metadata.standard_model)
    distinct = tuple(dict.fromkeys(models))
    if len(distinct) != 1:
        raise PlanningFeatureCodeError(
            "Planning document standard lineage is ambiguous"
        )
    return _strict_string(distinct[0], "planning document standard")


def _validated_code_series(series: pd.Series, label: str) -> None:
    for value in series.tolist():
        if not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None:
            raise PlanningFeatureCodeError(
                f"{label} must contain exact two-character digit strings"
            )


def _is_true_null(value: object) -> bool:
    if value is None or value is pd.NA:
        return True
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        return False
    return isinstance(missing, (bool, np.bool_)) and bool(missing)


def _null_safe_equal(left: object, right: object) -> bool:
    left_null = _is_true_null(left)
    right_null = _is_true_null(right)
    if left_null or right_null:
        return left_null and right_null
    return type(left) is type(right) and left == right


def _validate_nullable_official_value(value: object, label: str) -> None:
    if _is_true_null(value):
        return
    if isinstance(value, str) and value in _NULL_REFERENCE_LITERALS:
        raise PlanningFeatureCodeError(f"{label} contains a literal null replacement")
    try:
        _validate_official_text(value, label)
    except ValueError as error:
        raise PlanningFeatureCodeError(str(error)) from error


def _validate_code_dictionary(
    result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    frame = result.code_dictionary
    if type(frame) is not pd.DataFrame:
        raise PlanningFeatureCodeError(
            "code dictionary must be a non-geospatial DataFrame"
        )
    if frame.columns.duplicated().any() or (
        deterministic_frame_schema_signature(frame) != CODE_DICTIONARY_SCHEMA_SIGNATURE
    ):
        raise PlanningFeatureCodeError("code dictionary canonical schema is invalid")
    if frame.empty:
        raise PlanningFeatureCodeError(
            "code dictionary must contain at least one official code record"
        )
    records: dict[tuple[str, str, str], dict[str, object]] = {}
    ordered_keys: list[tuple[str, str, str]] = []
    for position, row in enumerate(frame.to_dict("records")):
        family = row["feature_family"]
        if family not in {"PRESCRIPTION", "INFORMATION"}:
            raise PlanningFeatureCodeError(
                f"code dictionary row {position} feature family is invalid"
            )
        for field in ("type_code", "subtype_code"):
            value = row[field]
            if not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None:
                raise PlanningFeatureCodeError(
                    f"code dictionary row {position} {field} is invalid"
                )
        key = (family, row["type_code"], row["subtype_code"])
        if key in records:
            raise PlanningFeatureCodeError("code dictionary contains duplicate pairs")
        try:
            _validate_official_text(
                row["official_label"],
                f"code dictionary row {position} official label",
            )
        except ValueError as error:
            raise PlanningFeatureCodeError(str(error)) from error
        _validate_nullable_official_value(
            row["legal_reference"],
            f"code dictionary row {position} legal reference",
        )
        _validate_nullable_official_value(
            row["regulation_or_annex_reference"],
            f"code dictionary row {position} regulation reference",
        )
        expected_url = (
            PRESCRIPTION_OFFICIAL_SOURCE_URL
            if family == "PRESCRIPTION"
            else INFORMATION_OFFICIAL_SOURCE_URL
        )
        if row["official_source_url"] != expected_url:
            raise PlanningFeatureCodeError(
                f"code dictionary row {position} official URL is invalid"
            )
        if (
            row["profile"] != result.profile
            or row["profile_sha256"] != result.profile_sha256
            or row["standard_model"] != result.standard_model
        ):
            raise PlanningFeatureCodeError(
                f"code dictionary row {position} result lineage differs"
            )
        records[key] = row
        ordered_keys.append(key)
    if ordered_keys != sorted(ordered_keys):
        raise PlanningFeatureCodeError("code dictionary pair order is not canonical")
    return records


def _validate_coded_meaning_rows(
    result: PlanningFeatureCodeResult,
    dictionary: Mapping[tuple[str, str, str], Mapping[str, object]],
) -> None:
    catalogs = (
        result.surface_features,
        result.line_features,
        result.point_features,
    )
    features: dict[str, dict[str, object]] = {}
    for frame in catalogs:
        for position, row in enumerate(frame.to_dict("records")):
            family = row["feature_family"]
            type_code = row["type_code_raw"]
            subtype_code = row["subtype_code_raw"]
            if family not in {"PRESCRIPTION", "INFORMATION"}:
                raise PlanningFeatureCodeError("coded feature family is invalid")
            for value, label in (
                (type_code, "type code"),
                (subtype_code, "subtype code"),
            ):
                if not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None:
                    raise PlanningFeatureCodeError(f"coded feature {label} is invalid")
            if (
                row["official_code_profile"] != result.profile
                or row["official_code_profile_sha256"] != result.profile_sha256
            ):
                raise PlanningFeatureCodeError("coded feature profile lineage differs")
            key = (family, type_code, subtype_code)
            record = dictionary.get(key)
            status = row["official_code_status"]
            meaning_fields = (
                ("official_code_label", "official_label"),
                ("official_legal_reference", "legal_reference"),
                (
                    "official_regulation_reference",
                    "regulation_or_annex_reference",
                ),
                ("official_code_source_url", "official_source_url"),
            )
            if status == "RESOLVED_OFFICIAL":
                if record is None or any(
                    not _null_safe_equal(row[field], record[dictionary_field])
                    for field, dictionary_field in meaning_fields
                ):
                    raise PlanningFeatureCodeError(
                        "resolved coded feature meaning differs from code dictionary"
                    )
            elif status == "UNKNOWN_CODE_PAIR":
                if record is not None or any(
                    not _is_true_null(row[field]) for field, _ in meaning_fields
                ):
                    raise PlanningFeatureCodeError(
                        "unknown coded feature contains an official meaning"
                    )
            else:
                raise PlanningFeatureCodeError(
                    f"coded feature official status is invalid at row {position}"
                )
            identifier = row["planning_feature_id"]
            if not isinstance(identifier, str) or not identifier:
                raise PlanningFeatureCodeError("coded feature ID is invalid")
            if identifier in features:
                raise PlanningFeatureCodeError(
                    "coded feature IDs are not globally unique"
                )
            features[identifier] = row
    compared_fields = (
        "feature_family",
        "type_code_raw",
        "subtype_code_raw",
        *OFFICIAL_CODE_COLUMNS,
    )
    for row in result.relations.to_dict("records"):
        identifier = row["planning_feature_id"]
        feature = features.get(identifier)
        if feature is None:
            raise PlanningFeatureCodeError(
                "coded relation references an unknown feature ID"
            )
        if any(
            not _null_safe_equal(row[field], feature[field])
            for field in compared_fields
        ):
            raise PlanningFeatureCodeError(
                "coded relation official meaning differs from its feature"
            )


def _validate_catalog_document_lineage(
    frame: gpd.GeoDataFrame,
    label: str,
    document: GpuPlanningDocument,
    standard_model: str,
) -> gpd.GeoDataFrame:
    _validated_code_series(frame["type_code_raw"], f"{label} type code")
    _validated_code_series(frame["subtype_code_raw"], f"{label} subtype code")
    metadata = document.extraction.archive.document
    if not frame["source_document_id"].eq(metadata.document_id).all():
        raise PlanningFeatureCodeError(f"{label} document lineage differs")
    if not frame["source_archive_sha256"].eq(document.extraction.archive.sha256).all():
        raise PlanningFeatureCodeError(f"{label} archive lineage differs")
    if not frame["source_standard_model"].eq(standard_model).all():
        raise PlanningFeatureCodeError(f"{label} source standard lineage differs")
    return frame.copy(deep=True)


def _dictionary(
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> pd.DataFrame:
    rows = [
        {
            **_record_payload(record),
            "profile": profile.profile,
            "profile_sha256": profile_hash,
            "standard_model": profile.standard_model,
        }
        for record in profile.records
    ]
    output = pd.DataFrame(rows, columns=CODE_DICTIONARY_COLUMNS)
    for column in CODE_DICTIONARY_COLUMNS:
        output[column] = pd.array(output[column].tolist(), dtype="str")
    output.index = pd.Index(np.arange(len(output), dtype="int64"))
    return output


def _lookup(
    profile: CnigFeatureCodeProfile,
) -> dict[tuple[str, str, str], CnigFeatureCodeRecord]:
    return {
        (record.feature_family, record.type_code, record.subtype_code): record
        for record in profile.records
    }


def _coded_catalog(
    frame: gpd.GeoDataFrame,
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> gpd.GeoDataFrame:
    output = frame.copy(deep=True)
    mapping = _lookup(profile)
    columns: dict[str, list[object]] = {column: [] for column in OFFICIAL_CODE_COLUMNS}
    for row in frame.to_dict("records"):
        key = (row["feature_family"], row["type_code_raw"], row["subtype_code_raw"])
        record = mapping.get(key)
        columns["official_code_status"].append(
            "RESOLVED_OFFICIAL" if record is not None else "UNKNOWN_CODE_PAIR"
        )
        columns["official_code_label"].append(
            record.official_label if record is not None else None
        )
        columns["official_legal_reference"].append(
            record.legal_reference if record is not None else None
        )
        columns["official_regulation_reference"].append(
            record.regulation_or_annex_reference if record is not None else None
        )
        columns["official_code_source_url"].append(
            record.official_source_url if record is not None else None
        )
        columns["official_code_profile"].append(profile.profile)
        columns["official_code_profile_sha256"].append(profile_hash)
    for column in OFFICIAL_CODE_COLUMNS:
        output[column] = pd.array(columns[column], dtype="str")
    output.index = pd.Index(output.index.to_numpy(copy=True), name=output.index.name)
    return output


def _catalog_by_id(
    catalogs: Sequence[gpd.GeoDataFrame],
) -> dict[str, dict[str, object]]:
    records: dict[str, dict[str, object]] = {}
    for catalog in catalogs:
        for row in catalog.to_dict("records"):
            identifier = str(row["planning_feature_id"])
            if identifier in records:
                raise PlanningFeatureCodeError(
                    "Planning feature IDs must be unique across feature catalogs"
                )
            records[identifier] = row
    return records


def _coded_relations(
    relations: pd.DataFrame,
    coded: Sequence[gpd.GeoDataFrame],
) -> pd.DataFrame:
    meanings = _catalog_by_id(coded)
    output = relations.copy(deep=True)
    appended: dict[str, list[object]] = {column: [] for column in OFFICIAL_CODE_COLUMNS}
    for row in relations.to_dict("records"):
        identifier = _strict_string(row["planning_feature_id"], "relation feature ID")
        meaning = meanings.get(identifier)
        if meaning is None:
            raise PlanningFeatureCodeError(
                "Relation references an unknown feature catalog ID"
            )
        for column in OFFICIAL_CODE_COLUMNS:
            appended[column].append(meaning[column])
    for column in OFFICIAL_CODE_COLUMNS:
        output[column] = pd.array(appended[column], dtype="str")
    output.index = pd.Index(output.index.to_numpy(copy=True), name=output.index.name)
    return output


def _canonical_value(value: object) -> object:
    if isinstance(value, BaseGeometry):
        return to_wkb(value, hex=True, include_srid=False)
    if isinstance(value, (datetime, date, pd.Timestamp)):
        return value.isoformat()
    if isinstance(value, np.generic):
        return _canonical_value(value.item())
    if isinstance(value, Mapping):
        return {str(key): _canonical_value(item) for key, item in value.items()}
    if isinstance(value, (tuple, list, np.ndarray)):
        return [_canonical_value(item) for item in value]
    if value is None or value is pd.NA:
        return None
    try:
        missing = pd.isna(value)
    except (TypeError, ValueError):
        missing = False
    if isinstance(missing, (bool, np.bool_)) and bool(missing):
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, Integral):
        return int(value)
    if isinstance(value, Real):
        number = float(value)
        if not math.isfinite(number):
            raise PlanningFeatureCodeError(
                "Integrity payload contains non-finite numeric data"
            )
        return number
    if isinstance(value, str):
        return value
    raise PlanningFeatureCodeError(
        f"Integrity payload contains unsupported value {type(value).__name__}"
    )


def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
    payload: dict[str, object] = {
        "schema": deterministic_frame_schema_signature(frame),
        "index": [_canonical_value(value) for value in frame.index.tolist()],
        "rows": [
            [_canonical_value(value) for value in row]
            for row in frame.itertuples(index=False, name=None)
        ],
    }
    return payload


def _source_frame_sha256(domain: str, frame: pd.DataFrame) -> str:
    return _canonical_json_sha256(
        {
            "domain": domain,
            "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,
            "frame": _frame_payload(frame),
        }
    )


def _inspected_layer_payload(layer: GpuInspectedLayer) -> dict[str, object]:
    try:
        logical_name = _strict_string(layer.logical_name, "GPU logical layer name")
        reference = layer.reference
        summary = layer.summary
        data = layer.data
        if not isinstance(data, gpd.GeoDataFrame):
            raise PlanningFeatureCodeError("GPU inspected layer data is invalid")
        return {
            "logical_name": logical_name,
            "source_layer": _strict_string(reference.source_layer, "GPU source layer"),
            "driver": _strict_string(reference.driver, "GPU driver"),
            "summary": asdict(summary),
            "source_data_sha256": _source_frame_sha256(
                "landscout.cnig_feature_codes.gpu_source_layer", data
            ),
        }
    except PlanningFeatureCodeError:
        raise
    except Exception as error:
        raise PlanningFeatureCodeError(
            "GPU inspected-layer context cannot be serialized"
        ) from error


def _planning_document_context_sha256(document: GpuPlanningDocument) -> str:
    try:
        archive = document.extraction.archive
        related = sorted(
            (_inspected_layer_payload(layer) for layer in document.related_layers),
            key=lambda item: str(item["logical_name"]),
        )
        spatial_references = sorted(
            (
                {
                    "source_layer": _strict_string(
                        reference.source_layer, "GPU spatial source layer"
                    ),
                    "driver": _strict_string(
                        reference.driver, "GPU spatial source driver"
                    ),
                }
                for reference in document.all_spatial_layers
            ),
            key=lambda item: (str(item["source_layer"]), str(item["driver"])),
        )
        return _canonical_json_sha256(
            {
                "domain": "landscout.cnig_feature_codes.planning_document_input",
                "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,
                "document_metadata": asdict(archive.document),
                "archive": {
                    "filename": archive.filename,
                    "archive_format": archive.archive_format,
                    "file_size": archive.file_size,
                    "sha256": archive.sha256,
                },
                "standard_models": sorted(document.extraction.standard_models),
                "spatial_references": spatial_references,
                "zoning": _inspected_layer_payload(document.zoning),
                "related_layers": related,
            }
        )
    except PlanningFeatureCodeError:
        raise
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Planning-document context cannot be hashed safely"
        ) from error


def _parcel_identity_input_sha256(parcels: gpd.GeoDataFrame) -> str:
    try:
        identity = gpd.GeoDataFrame(
            parcels[["parcel_id", "geometry"]].copy(deep=True),
            geometry="geometry",
            crs=parcels.crs,
        )
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Parcel identity input cannot be serialized"
        ) from error
    return _source_frame_sha256(
        "landscout.cnig_feature_codes.parcel_identity_input", identity
    )


def _normalized_catalogs_input_sha256(
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.cnig_feature_codes.normalized_catalogs_input",
            "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,
            "surface": _frame_payload(surface_features),
            "line": _frame_payload(line_features),
            "point": _frame_payload(point_features),
        }
    )


def _normalized_relations_input_sha256(relations: pd.DataFrame) -> str:
    return _source_frame_sha256(
        "landscout.cnig_feature_codes.normalized_relations_input", relations
    )


def _component_metadata(result: PlanningFeatureCodeResult) -> dict[str, object]:
    return {
        "result_hash_schema_version": result.result_hash_schema_version,
        "profile_schema_version": result.profile_schema_version,
        "profile": result.profile,
        "standard_model": result.standard_model,
        "profile_sha256": result.profile_sha256,
        "source_document_id": result.source_document_id,
        "source_archive_sha256": result.source_archive_sha256,
        "planning_document_context_sha256": (result.planning_document_context_sha256),
        "parcel_identity_input_sha256": result.parcel_identity_input_sha256,
        "normalized_catalogs_input_sha256": (result.normalized_catalogs_input_sha256),
        "normalized_relations_input_sha256": (result.normalized_relations_input_sha256),
        "gpu_related_source_files_sha256": (result.gpu_related_source_files_sha256),
        "expected_relations_content_sha256": (result.expected_relations_content_sha256),
    }


def _frame_sha256(
    domain: str,
    result: PlanningFeatureCodeResult,
    frame: pd.DataFrame,
) -> str:
    return _canonical_json_sha256(
        {
            "domain": domain,
            **_component_metadata(result),
            "frame": _frame_payload(frame),
        }
    )


def _complete_sha256(result: PlanningFeatureCodeResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.cnig_feature_codes.result",
            **_component_metadata(result),
            "code_dictionary_content_sha256": result.code_dictionary_content_sha256,
            "surface_features_content_sha256": result.surface_features_content_sha256,
            "line_features_content_sha256": result.line_features_content_sha256,
            "point_features_content_sha256": result.point_features_content_sha256,
            "relations_content_sha256": result.relations_content_sha256,
        }
    )


def _result_with_hashes(result: PlanningFeatureCodeResult) -> PlanningFeatureCodeResult:
    component = replace(
        result,
        code_dictionary_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.dictionary", result, result.code_dictionary
        ),
        surface_features_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.surface", result, result.surface_features
        ),
        line_features_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.line", result, result.line_features
        ),
        point_features_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.point", result, result.point_features
        ),
        relations_content_sha256=_frame_sha256(
            "landscout.cnig_feature_codes.relations", result, result.relations
        ),
    )
    return replace(
        component, complete_result_content_sha256=_complete_sha256(component)
    )


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
    standard = _planning_standard(planning_document)
    if standard != code_profile.standard_model:
        raise PlanningFeatureCodeError(
            f"Planning document standard {standard!r} differs from code-profile standard"
        )
    if factual_validation is None:
        try:
            factual_validation = validate_normalized_planning_feature_inputs(
                planning_document,
                parcels,
                surface_features,
                line_features,
                point_features,
                relations,
            )
        except ValueError as error:
            raise PlanningFeatureCodeError(
                f"Normalized planning-feature inputs are invalid: {error}"
            ) from error
    surface = _validate_catalog_document_lineage(
        surface_features, "surface feature catalog", planning_document, standard
    )
    line = _validate_catalog_document_lineage(
        line_features, "line feature catalog", planning_document, standard
    )
    point = _validate_catalog_document_lineage(
        point_features, "point feature catalog", planning_document, standard
    )
    profile_hash = _profile_sha256(code_profile)
    coded_surface = _coded_catalog(surface, code_profile, profile_hash)
    coded_line = _coded_catalog(line, code_profile, profile_hash)
    coded_point = _coded_catalog(point, code_profile, profile_hash)
    coded_relations = _coded_relations(
        relations, (coded_surface, coded_line, coded_point)
    )
    archive = planning_document.extraction.archive
    result = PlanningFeatureCodeResult(
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        profile_schema_version=code_profile.schema_version,
        profile=code_profile.profile,
        standard_model=standard,
        profile_sha256=profile_hash,
        source_document_id=archive.document.document_id,
        source_archive_sha256=archive.sha256,
        planning_document_context_sha256=_planning_document_context_sha256(
            planning_document
        ),
        parcel_identity_input_sha256=_parcel_identity_input_sha256(parcels),
        normalized_catalogs_input_sha256=_normalized_catalogs_input_sha256(
            surface_features, line_features, point_features
        ),
        normalized_relations_input_sha256=_normalized_relations_input_sha256(relations),
        gpu_related_source_files_sha256=(
            factual_validation.gpu_related_source_files_sha256
        ),
        expected_relations_content_sha256=(
            factual_validation.expected_relations_content_sha256
        ),
        code_dictionary_content_sha256="",
        surface_features_content_sha256="",
        line_features_content_sha256="",
        point_features_content_sha256="",
        relations_content_sha256="",
        complete_result_content_sha256="",
        code_dictionary=_dictionary(code_profile, profile_hash),
        surface_features=coded_surface,
        line_features=coded_line,
        point_features=coded_point,
        relations=coded_relations,
    )
    return _result_with_hashes(result)


def _validate_result_envelope(result: PlanningFeatureCodeResult) -> None:
    if type(result) is not PlanningFeatureCodeResult:
        raise PlanningFeatureCodeError("result must be a PlanningFeatureCodeResult")
    for version, expected_version, label in (
        (
            result.result_hash_schema_version,
            RESULT_HASH_SCHEMA_VERSION,
            "result hash schema version",
        ),
        (
            result.profile_schema_version,
            PROFILE_SCHEMA_VERSION,
            "profile schema version",
        ),
    ):
        if type(version) is not int or version != expected_version:
            raise PlanningFeatureCodeError(f"unsupported {label}: {version!r}")
    if result.standard_model != STANDARD_MODEL:
        raise PlanningFeatureCodeError("result standard model is invalid")
    for value, label in (
        (result.profile, "result profile"),
        (result.source_document_id, "result source document ID"),
    ):
        _strict_string(value, label)
    for field in PlanningFeatureCodeResult.__dataclass_fields__:
        if not field.endswith("_sha256"):
            continue
        value = getattr(result, field)
        if not isinstance(value, str) or _SHA_PATTERN.fullmatch(value) is None:
            raise PlanningFeatureCodeError(f"{field} must be a lowercase SHA256")
    dictionary = _validate_code_dictionary(result)
    for frame, label, kind in (
        (result.surface_features, "surface features", "SURFACE"),
        (result.line_features, "line features", "LINE"),
        (result.point_features, "point features", "POINT"),
    ):
        geometry_kind = cast(GeometryKind, kind)
        try:
            validate_canonical_frame_schema(
                frame,
                columns=feature_columns(geometry_kind),
                dtypes=feature_dtypes(geometry_kind, frame=frame),
                label=label,
                geospatial=True,
            )
        except (TypeError, ValueError) as error:
            raise PlanningFeatureCodeError(str(error)) from error
    try:
        validate_canonical_frame_schema(
            result.relations,
            columns=relation_columns(),
            dtypes=relation_dtypes(),
            label="coded relations",
            geospatial=False,
        )
    except (TypeError, ValueError) as error:
        raise PlanningFeatureCodeError(str(error)) from error
    _validate_coded_meaning_rows(result, dictionary)
    rebuilt_hashes = _result_with_hashes(result)
    for field in (
        "code_dictionary_content_sha256",
        "surface_features_content_sha256",
        "line_features_content_sha256",
        "point_features_content_sha256",
        "relations_content_sha256",
        "complete_result_content_sha256",
    ):
        if getattr(result, field) != getattr(rebuilt_hashes, field):
            raise PlanningFeatureCodeError(f"result hash {field} is invalid")


def validate_planning_feature_code_result_envelope(
    result: PlanningFeatureCodeResult,
) -> None:
    """Validate one coded-result envelope without rebuilding factual sources."""

    try:
        _validate_result_envelope(result)
    except PlanningFeatureCodeError:
        raise
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Planning feature code result envelope is invalid"
        ) from error


def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _canonical_value(_frame_payload(actual)) != _canonical_value(
        _frame_payload(expected)
    ):
        raise PlanningFeatureCodeError(f"{label} differs from rebuilt source result")


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
    """Rebuild and validate a coded result from every factual source input."""

    try:
        _validate_result_envelope(result)
        expected = _build_result(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            _resolved_profile(code_profile),
        )
        scalar_fields = (
            "result_hash_schema_version",
            "profile_schema_version",
            "profile",
            "standard_model",
            "profile_sha256",
            "source_document_id",
            "source_archive_sha256",
            "planning_document_context_sha256",
            "parcel_identity_input_sha256",
            "normalized_catalogs_input_sha256",
            "normalized_relations_input_sha256",
            "gpu_related_source_files_sha256",
            "expected_relations_content_sha256",
            "code_dictionary_content_sha256",
            "surface_features_content_sha256",
            "line_features_content_sha256",
            "point_features_content_sha256",
            "relations_content_sha256",
            "complete_result_content_sha256",
        )
        for field in scalar_fields:
            if getattr(result, field) != getattr(expected, field):
                raise PlanningFeatureCodeError(
                    f"result {field} differs from rebuilt source result"
                )
        for actual, rebuilt, label in (
            (result.code_dictionary, expected.code_dictionary, "code dictionary"),
            (result.surface_features, expected.surface_features, "surface features"),
            (result.line_features, expected.line_features, "line features"),
            (result.point_features, expected.point_features, "point features"),
            (result.relations, expected.relations, "coded relations"),
        ):
            _compare_frame(actual, rebuilt, label)
    except PlanningFeatureCodeError:
        raise
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Planning-feature code result validation failed safely"
        ) from error


def resolve_planning_feature_codes(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
) -> PlanningFeatureCodeResult:
    """Attach exact official CNIG meanings without interpreting their impact."""

    try:
        profile = _resolved_profile(code_profile)
        standard = _planning_standard(planning_document)
        if standard != profile.standard_model:
            raise PlanningFeatureCodeError(
                f"Planning document standard {standard!r} differs from "
                "code-profile standard"
            )
        factual_validation = validate_normalized_planning_feature_inputs(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
        )
        result = _build_result(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            profile,
            factual_validation,
        )
        _validate_result_envelope(result)
        return result
    except PlanningFeatureCodeError:
        raise
    except ValueError as error:
        raise PlanningFeatureCodeError(
            f"Planning-feature code resolution failed: {error}"
        ) from error
    except Exception as error:
        raise PlanningFeatureCodeError(
            "Planning-feature code resolution failed safely"
        ) from error
```
