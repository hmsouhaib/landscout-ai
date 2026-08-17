# `src/landscout/stages/resolve_planning_feature_codes.py`

## File identity

- Repository path: `src/landscout/stages/resolve_planning_feature_codes.py`
- File type: Python source
- Layer: artifact validation/loading stage
- Domain: planning
- Responsibility: Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.
- Source SHA256: `57907fd137407beeceaf0dee2cd1419a7746945032577782bcfa209711d5c2ae`

## 1. Purpose

Resolves normalized factual planning features against the checked-in CNIG PLU code dictionary.

## 2. Position in LandScout architecture

This file belongs to the **artifact validation/loading stage** layer and the **planning** domain. Its trust and business authority is limited to the exact source, validators, schemas, and callers reproduced below.

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
- `import yaml`
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
- `from landscout.sources.gpu_fr import GpuInspectedLayer, GpuPlanningDocument`
- `from landscout.stages.enrich_planning_features import (
    PlanningFeatureInputValidation,
    validate_normalized_planning_feature_inputs,
)`

## 4. Contract taxonomy

### A. Python constants

#### `PROFILE_SCHEMA_VERSION`

```python
PROFILE_SCHEMA_VERSION = 2
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeProfile._validate_profile` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` (value reference).

#### `RESULT_HASH_SCHEMA_VERSION`

```python
RESULT_HASH_SCHEMA_VERSION = 5
```

Supported schema/hash/manifest compatibility version used by validators and canonical hashing. Consumers include `src/landscout/stages/resolve_planning_feature_codes.py::_source_frame_sha256` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_planning_document_context_sha256` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_normalized_catalogs_input_sha256` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` (value reference).

#### `STANDARD_MODEL`

```python
STANDARD_MODEL = "CNIG PLU v2017"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` (value reference).

#### `OFFICIAL_TEXT_NORMALIZATION`

```python
OFFICIAL_TEXT_NORMALIZATION = "GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/resolve_planning_feature_codes.py::_validate_official_text` (value reference).

#### `PRESCRIPTION_OFFICIAL_SOURCE_URL`

```python
PRESCRIPTION_OFFICIAL_SOURCE_URL = (
    "https://www.geoportail-urbanisme.gouv.fr/standard/"
    "cnig_PLU_2017/codes/PrescriptionUrbaType"
)
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes. Consumers include `src/landscout/stages/resolve_planning_feature_codes.py::OfficialSourceUrls._validate_urls` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeRecord._validate_record` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_validate_code_dictionary` (value reference).

#### `INFORMATION_OFFICIAL_SOURCE_URL`

```python
INFORMATION_OFFICIAL_SOURCE_URL = (
    "https://www.geoportail-urbanisme.gouv.fr/standard/"
    "cnig_PLU_2017/codes/InformationUrbaType"
)
```

Configured/constructed URL component or origin constraint; it is textual identity until the transport/source validator proves bytes. Consumers include `src/landscout/stages/resolve_planning_feature_codes.py::OfficialSourceUrls._validate_urls` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeRecord._validate_record` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_validate_code_dictionary` (value reference).

#### `CODE_DICTIONARY_COLUMNS`

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

Named frame schema/required-field contract; the resolved fields and dtypes are documented in the Data contracts section. Consumers include `tests/unit/test_resolve_planning_feature_codes.py::<module>` (import), `src/landscout/stages/resolve_planning_feature_codes.py::<module>` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_dictionary` (value reference), `tests/unit/test_resolve_planning_feature_codes.py::test_catalogs_and_relations_are_preserved_and_inputs_immutable` (value reference).

#### `CODE_DICTIONARY_DTYPES`

```python
CODE_DICTIONARY_DTYPES = tuple("str" for _ in CODE_DICTIONARY_COLUMNS)
```

Canonical Pandas/GeoPandas dtype contract aligned with the named schema. Consumers include `src/landscout/stages/resolve_planning_feature_codes.py::<module>` (value reference).

#### `CODE_DICTIONARY_SCHEMA_SIGNATURE`

```python
CODE_DICTIONARY_SCHEMA_SIGNATURE: dict[str, object] = {
    "columns": list(CODE_DICTIONARY_COLUMNS),
    "dtypes": list(CODE_DICTIONARY_DTYPES),
    "index_class": "pandas.Index",
    "index_names": [None],
    "index_level_dtypes": ["int64"],
}
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/resolve_planning_feature_codes.py::_validate_code_dictionary` (value reference).

#### `_CODE_PATTERN`

```python
_CODE_PATTERN = re.compile(r"[0-9]{2}")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly. Consumers include `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeRecord._validate_record` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_validated_code_series` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_validate_code_dictionary` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_validate_coded_meaning_rows` (value reference).

#### `_SHA_PATTERN`

```python
_SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

Compiled/text regular expression used by the named validation path; the fenced declaration preserves every metacharacter exactly. Consumers include `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeProfile._validate_profile` (value reference), `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` (value reference).

#### `_NULL_REFERENCE_LITERALS`

```python
_NULL_REFERENCE_LITERALS = frozenset({"None", "nan", "<NA>"})
```

Module-level technical/source/policy constant consumed by the exact references below. Consumers include `src/landscout/stages/resolve_planning_feature_codes.py::_validate_nullable_official_value` (value reference).


### B. Type aliases and closed domains

#### `FeatureFamily`

```python
FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
```

Official planning-feature family domain: PRESCRIPTION or INFORMATION. Enforced/consumed by `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeRecord` (type annotation).

#### `OfficialCodeStatus`

```python
OfficialCodeStatus = Literal["RESOLVED_OFFICIAL", "UNKNOWN_CODE_PAIR"]
```

CNIG resolution state: exact official pair resolved or unknown pair retained unresolved. No statically owned repository consumer was proven; the declaration remains authoritative for its local runtime use.


### C. Meaningful dunder contracts

- `__all__` — explicit public export allow-list.
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


### D–J. Models, frames, JSON/mappings, configuration, filesystem metadata, exports

Models/dataclasses are documented in section 5. Frame columns and mappings are documented below. JSON/config/filesystem fields are identified by their owning declarations rather than merged with frame columns.


## 5. Classes / models / dataclasses

### `PlanningFeatureCodeError`

**Purpose:** Raised when official code resolution integrity cannot be proven.

**Kind:** controlled exception.

**Inheritance:** `ValueError`.

**Exact decorators:** none.

**Fields:** none declared directly on this class.

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`.
- import: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_canonical_json_sha256` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_construct_unique_mapping` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::load_cnig_feature_code_profile` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_resolved_profile` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_strict_string` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_planning_standard` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_validated_code_series` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_nullable_official_value` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_code_dictionary` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_coded_meaning_rows` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_catalog_document_lineage` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_catalog_by_id` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_coded_relations` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_canonical_value` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_inspected_layer_payload` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_planning_document_context_sha256` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_parcel_identity_input_sha256` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result_envelope` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_compare_frame` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `PlanningFeatureCodeError`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `PlanningFeatureCodeError`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated` via `pytest.raises(PlanningFeatureCodeError, match='profile|canonical')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `pytest.raises(PlanningFeatureCodeError, match='schema|profile')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `pytest.raises(PlanningFeatureCodeError, match='duplicate|profile')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_yaml_key_is_rejected` via `pytest.raises(PlanningFeatureCodeError, match='Duplicate YAML')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_wrong_planning_standard_is_rejected` via `pytest.raises(PlanningFeatureCodeError, match='standard')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_complete_normalized_catalog_schema_is_required` via `pytest.raises(PlanningFeatureCodeError, match='normalized|schema|column')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_unexpected_factual_catalog_column_is_rejected` via `pytest.raises(PlanningFeatureCodeError, match='normalized|schema|column')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_cnig_identity_provenance_is_exact` via `pytest.raises(PlanningFeatureCodeError, match='identity|provenance|normalized')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_ogr_fid_provenance_is_restricted` via `pytest.raises(PlanningFeatureCodeError, match='OGR|identity|provenance|normalized')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_source_feature_id_is_unique_inside_logical_layer` via `pytest.raises(PlanningFeatureCodeError, match='source_feature_id|unique')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_crs_must_be_canonical_epsg_2154` via `pytest.raises(PlanningFeatureCodeError, match='EPSG:2154|CRS')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_geometry_metrics_are_revalidated` via `pytest.raises(PlanningFeatureCodeError, match='metric|area|length|member')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_complete_relation_schema_is_required` via `pytest.raises(PlanningFeatureCodeError, match='relation|schema|column')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_unexpected_factual_relation_column_is_rejected` via `pytest.raises(PlanningFeatureCodeError, match='relation|schema')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_cnig_resolver_invokes_shared_factual_contract` via `pytest.raises(PlanningFeatureCodeError, match='shared factual contract marker')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_complete_relation_catalog_agreement_is_required` via `pytest.raises(PlanningFeatureCodeError, match='catalog|metric|normalized|feature share')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_surface_relation_metrics_are_revalidated` via `pytest.raises(PlanningFeatureCodeError, match='relation|metric|finite|percentage')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_line_relation_metrics_are_revalidated` via `pytest.raises(PlanningFeatureCodeError, match='relation|length|catalog')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_catalog_columns_are_rejected` via `pytest.raises(PlanningFeatureCodeError, match='duplicate|columns')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_missing_catalog_crs_is_rejected` via `pytest.raises(PlanningFeatureCodeError, match='CRS')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_unparseable_catalog_crs_is_rejected` via `pytest.raises(PlanningFeatureCodeError, match='CRS')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_inactive_or_wrong_geometry_column_is_rejected` via `pytest.raises(PlanningFeatureCodeError, match='geometry')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_surface_geometry_contract_is_enforced` via `pytest.raises(PlanningFeatureCodeError, match=message)`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_catalog_semantic_and_string_contracts_are_enforced` via `pytest.raises(PlanningFeatureCodeError, match=message)`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_every_required_catalog_identity_is_an_exact_non_null_string` via `pytest.raises(PlanningFeatureCodeError, match='exact string|non-empty')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_line_and_point_geometry_types_are_enforced` via `pytest.raises(PlanningFeatureCodeError, match='geometry|type')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_planning_feature_ids_are_globally_unique_across_catalogs` via `pytest.raises(PlanningFeatureCodeError, match='unique|catalog|deterministic')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_relation_catalog_code_mismatch_is_rejected` via `pytest.raises(PlanningFeatureCodeError, match='catalog')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_relation_columns_are_rejected` via `pytest.raises(PlanningFeatureCodeError, match='duplicate|columns')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_relation_identity_must_be_an_exact_non_null_string` via `pytest.raises(PlanningFeatureCodeError, match='relation|exact string')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_parcel_feature_relation_is_rejected` via `pytest.raises(PlanningFeatureCodeError, match='unique|duplicate')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_unknown_relation_feature_id_is_rejected` via `pytest.raises(PlanningFeatureCodeError, match='unknown')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_relation_type_must_match_catalog_geometry_kind` via `pytest.raises(PlanningFeatureCodeError, match='[Rr]elation type|geometry')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_coordinated_output_hash_mutation_is_rejected` via `pytest.raises(PlanningFeatureCodeError, match='rebuilt|meaning|dictionary')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_result_schema_versions_are_strict` via `pytest.raises(PlanningFeatureCodeError, match='schema version')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_source_input_hash_mutation_is_rejected` via `pytest.raises(PlanningFeatureCodeError, match='hash|rebuilt|source')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_parcel_source_change_invalidates_coded_result` via `pytest.raises(PlanningFeatureCodeError, match='parcel|source|rebuilt')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_gpu_document_context_change_invalidates_coded_result` via `pytest.raises(PlanningFeatureCodeError, match='document|source|rebuilt')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent` via `pytest.raises(PlanningFeatureCodeError, match='normalized|source|rebuilt')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_relation_change_invalidates_coded_result` via `pytest.raises(PlanningFeatureCodeError, match='[Rr]elation|source|rebuilt')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_coding_api_rejects_relation_set_not_rebuilt_from_geometry` via `pytest.raises(PlanningFeatureCodeError, match='relation|parcel|source|rebuilt|normalized')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_step_7d_5b_2b_5_exposes_lightweight_coded_result_validator` via `pytest.raises(PlanningFeatureCodeError, match='hash|invalid')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_rejects_canonical_empty_code_dictionary` via `pytest.raises(PlanningFeatureCodeError, match='dictionary|empty|record')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_controls_malformed_dictionary_type` via `pytest.raises(PlanningFeatureCodeError)`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_rejects_geospatial_code_dictionary` via `pytest.raises(PlanningFeatureCodeError, match='dictionary|DataFrame')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_dictionary_schema_is_explicit` via `pytest.raises(PlanningFeatureCodeError, match='dictionary|schema|dtype|index')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_dictionary_rows_are_intrinsically_validated` via `pytest.raises(PlanningFeatureCodeError, match='dictionary|pair|code|family|URL|profile|order')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_scalar_lineage_contracts_are_intrinsic` via `pytest.raises(PlanningFeatureCodeError, match='standard|SHA|sha|lineage')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic` via `pytest.raises(PlanningFeatureCodeError, match='official|meaning|UNKNOWN|relation|feature')`.
- expected exception type: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_envelope_requires_exact_result_type_and_accepts_valid_result` via `pytest.raises(PlanningFeatureCodeError, match='type|result')`.

**Exact class source**

```python
class PlanningFeatureCodeError(ValueError):
    """Raised when official code resolution integrity cannot be proven."""
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

### `OfficialSourceUrls`

**Purpose:** Family-specific official CNIG HTTPS source URLs used by code-dictionary row validation.

**Kind:** Pydantic model.

**Inheritance:** `_StrictModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `prescription` | `prescription: StrictStr` | Official CNIG prescription-family source URL. |
| `information` | `information: StrictStr` | `OfficialSourceUrls.information` represents the `information` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |

**Validators (exact source)**

`_validate_urls`:

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

**Interface consumers**

- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::OfficialSourceUrls._validate_urls` via `OfficialSourceUrls`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeProfile` via `OfficialSourceUrls`.

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

**Purpose:** One official CNIG feature family/type/subtype record with label, nullable references, source URL, profile, and standard identity.

**Kind:** Pydantic model.

**Inheritance:** `_StrictModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `feature_family` | `feature_family: FeatureFamily` | `CnigFeatureCodeRecord.feature_family` represents the `feature_family` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `type_code` | `type_code: StrictStr` | `CnigFeatureCodeRecord.type_code` represents the `type_code` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `subtype_code` | `subtype_code: StrictStr` | `CnigFeatureCodeRecord.subtype_code` represents the `subtype_code` classification consumed by the exact validators/branches reproduced below; a closed vocabulary is claimed only where those validators enforce one. |
| `official_label` | `official_label: StrictStr` | `CnigFeatureCodeRecord.official_label` carries the official label used by the reproduced constructors and validators; its declared type is `StrictStr` and no legal meaning is inferred beyond that owner. |
| `legal_reference` | `legal_reference: StrictStr \| None` | `CnigFeatureCodeRecord.legal_reference` carries the legal reference used by the reproduced constructors and validators; its declared type is `StrictStr | None` and no legal meaning is inferred beyond that owner. |
| `regulation_or_annex_reference` | `regulation_or_annex_reference: StrictStr \| None` | `CnigFeatureCodeRecord.regulation_or_annex_reference` carries the regulation or annex reference used by the reproduced constructors and validators; its declared type is `StrictStr | None` and no legal meaning is inferred beyond that owner. |
| `official_source_url` | `official_source_url: StrictStr` | Exact source/evidence URL whose HTTPS/origin/path constraints are enforced by the owning configuration or source validator. |

**Validators (exact source)**

`_validate_record`:

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

**Interface consumers**

- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeRecord._validate_record` via `CnigFeatureCodeRecord`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_record_payload` via `CnigFeatureCodeRecord`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_records_sha256` via `CnigFeatureCodeRecord`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeProfile` via `CnigFeatureCodeRecord`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_lookup` via `CnigFeatureCodeRecord`.

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

**Purpose:** Strict offline snapshot of official CNIG feature code records.

**Kind:** Pydantic model.

**Inheritance:** `_StrictModel`.

**Exact decorators:** none.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `schema_version` | `schema_version: StrictInt` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `profile` | `profile: StrictStr = Field(min_length=1)` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `standard_model` | `standard_model: Literal["CNIG PLU v2017"]` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `official_text_normalization` | `official_text_normalization: Literal["GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"]` | `CnigFeatureCodeProfile.official_text_normalization` carries the official text normalization used by the reproduced constructors and validators; its declared type is `Literal['GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1']` and no legal meaning is inferred beyond that owner. |
| `official_sources` | `official_sources: OfficialSourceUrls` | Family-specific official CNIG HTTPS reference URLs. |
| `retrieval_date` | `retrieval_date: date` | Declared date on which the official CNIG source references were retrieved for this profile. |
| `canonical_records_sha256` | `canonical_records_sha256: StrictStr` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `records` | `records: tuple[CnigFeatureCodeRecord, ...] = Field(min_length=1)` | Ordered collection of the named source/configuration records; member type, uniqueness, order, and identity are validated by the owning model/source boundary. |

**Validators (exact source)**

`_validate_profile`:

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

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`.
- import: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
)`.
- import: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result_envelope,
)`.
- import: `src/landscout/stages/bess_planning_feature_policy.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result,
)`.
- import: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`.
- type annotation: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_application_source` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::aggregate_bess_planning_feature_policy_to_parcels` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_policy_source` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::apply_bess_planning_feature_policy` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_validate_coded_source` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeProfile._validate_profile` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::load_cnig_feature_code_profile` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_resolved_profile` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_profile_sha256` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_dictionary` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_lookup` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_coded_catalog` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `CnigFeatureCodeProfile`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `CnigFeatureCodeProfile`.
- type annotation: `tests/unit/test_resolve_planning_feature_codes.py::_profile` via `CnigFeatureCodeProfile`.
- type annotation: `tests/unit/test_resolve_planning_feature_codes.py::_mutated_profile` via `CnigFeatureCodeProfile`.
- type annotation: `tests/unit/test_resolve_planning_feature_codes.py::_integration_inputs` via `CnigFeatureCodeProfile`.
- type annotation: `tests/unit/test_resolve_planning_feature_codes.py::_inputs` via `CnigFeatureCodeProfile`.
- type annotation: `tests/unit/test_resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `CnigFeatureCodeProfile`.
- type annotation: `tests/unit/test_resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `CnigFeatureCodeProfile`.

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

### `PlanningFeatureCodeResult`

**Purpose:** Immutable envelope around exact official code resolution outputs.

**Kind:** dataclass.

**Inheritance:** plain object.

**Exact decorators:** `dataclass(frozen=True)`.

**Fields**

| Field | Exact declaration | Meaning |
|---|---|---|
| `result_hash_schema_version` | `result_hash_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `profile_schema_version` | `profile_schema_version: int` | Strict compatibility version; the owning validator accepts only its documented supported integer. |
| `profile` | `profile: str` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `standard_model` | `standard_model: str` | Versioned policy/profile identity or scope propagated to compiled/results rows and checked against the authoritative configuration bytes. |
| `profile_sha256` | `profile_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `source_document_id` | `source_document_id: str` | Exact source-lineage scalar named by the field; it is compared with configuration/result/row lineage but is not physical proof without source-byte revalidation. |
| `source_archive_sha256` | `source_archive_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `planning_document_context_sha256` | `planning_document_context_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `parcel_identity_input_sha256` | `parcel_identity_input_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `normalized_catalogs_input_sha256` | `normalized_catalogs_input_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `normalized_relations_input_sha256` | `normalized_relations_input_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `gpu_related_source_files_sha256` | `gpu_related_source_files_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `expected_relations_content_sha256` | `expected_relations_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `code_dictionary_content_sha256` | `code_dictionary_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `surface_features_content_sha256` | `surface_features_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `line_features_content_sha256` | `line_features_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `point_features_content_sha256` | `point_features_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `relations_content_sha256` | `relations_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `complete_result_content_sha256` | `complete_result_content_sha256: str` | Lowercase SHA256 binding the bytes or canonical result component named by the field prefix. |
| `code_dictionary` | `code_dictionary: pd.DataFrame` | Canonical official CNIG code-pair dictionary carried by the coded result. |
| `surface_features` | `surface_features: gpd.GeoDataFrame` | Canonical surface planning-feature catalog in this result envelope. |
| `line_features` | `line_features: gpd.GeoDataFrame` | Canonical line planning-feature catalog in this result envelope. |
| `point_features` | `point_features: gpd.GeoDataFrame` | Canonical point planning-feature catalog in this result envelope. |
| `relations` | `relations: pd.DataFrame` | Pandas/GeoPandas result frame named by this field; its exact ordered schema, dtype, CRS/index, and preservation contract is documented by the owning result validator and schema declarations. |

**Interface consumers**

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`.
- import: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
)`.
- import: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result_envelope,
)`.
- import: `src/landscout/stages/bess_planning_feature_policy.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result,
)`.
- import: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`.
- type annotation: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::_validate_application_source` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::aggregate_bess_planning_feature_policy_to_parcels` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/aggregate_bess_planning_feature_policy.py::validate_bess_planning_feature_parcel_aggregation_result` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_build_result` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_coded_policy_compatibility` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_source_locks` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::_validate_policy_source` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::apply_bess_planning_feature_policy` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::validate_bess_planning_feature_application_result` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_validate_source_lock` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_dictionary_by_pair` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_validate_policy_completeness` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_policy_table` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_build_result` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::_validate_coded_source` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::compile_bess_planning_feature_policy` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/bess_planning_feature_policy.py::validate_bess_planning_feature_policy_result` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_code_dictionary` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_coded_meaning_rows` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_component_metadata` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_sha256` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_complete_sha256` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_result_with_hashes` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `PlanningFeatureCodeResult`.
- constructor call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result_envelope` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `PlanningFeatureCodeResult`.
- type annotation: `src/landscout/stages/resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `PlanningFeatureCodeResult`.
- type annotation: `tests/unit/test_resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `PlanningFeatureCodeResult`.
- type annotation: `tests/unit/test_resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `PlanningFeatureCodeResult`.
- type annotation: `tests/unit/test_resolve_planning_feature_codes.py::_schema_v5_envelope_result` via `PlanningFeatureCodeResult`.
- type annotation: `tests/unit/test_resolve_planning_feature_codes.py::_canonical_empty_coded_result` via `PlanningFeatureCodeResult`.

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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_official_text` via `_exact_string`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeProfile._validate_profile` via `_exact_string`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_strict_string` via `_exact_string`.

**Complete source-ordered implementation**

```python
def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be a non-empty exact string")
    return value
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_canonical_official_text`

**Exact signature**

```python
def _canonical_official_text(value: str) -> str:
```

**Purpose**

Private `planning` helper for canonical official text; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
' '.join(unicodedata.normalize('NFC', value).split())
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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_official_text` via `_canonical_official_text`.

**Complete source-ordered implementation**

```python
def _canonical_official_text(value: str) -> str:
    return " ".join(unicodedata.normalize("NFC", value).split())
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_official_text`

**Exact signature**

```python
def _validate_official_text(value: object, label: str) -> str:
```

**Purpose**

Rejects malformed or inconsistent official text; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
text
```

**Validation and exceptions**

- Guard with a raise path: `text != _canonical_official_text(text)`.
- Explicit raise expressions: `ValueError(f'{label} must already use canonical {OFFICIAL_TEXT_NORMALIZATION} text')`.

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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_optional_official_text` via `_validate_official_text`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeRecord._validate_record` via `_validate_official_text`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_nullable_official_value` via `_validate_official_text`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_code_dictionary` via `_validate_official_text`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_optional_official_text`

**Exact signature**

```python
def _validate_optional_official_text(value: object, label: str) -> str | None:
```

**Purpose**

Rejects malformed or inconsistent optional official text; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str | None`.
- Every observed return expression is reproduced without truncation:
```python
_validate_official_text(value, label)

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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeRecord._validate_record` via `_validate_optional_official_text`.

**Complete source-ordered implementation**

```python
def _validate_optional_official_text(value: object, label: str) -> str | None:
    if value is None:
        return None
    return _validate_official_text(value, label)
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `OfficialSourceUrls._validate_urls`

**Exact signature**

```python
def _validate_urls(self) -> OfficialSourceUrls:
```

**Purpose**

Rejects malformed or inconsistent urls; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `OfficialSourceUrls`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `self.prescription != PRESCRIPTION_OFFICIAL_SOURCE_URL`.
- Guard with a raise path: `self.information != INFORMATION_OFFICIAL_SOURCE_URL`.
- Explicit raise expressions: `ValueError('information source URL is not the exact official GPU host endpoint')`, `ValueError('prescription source URL is not the exact official GPU host endpoint')`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `CnigFeatureCodeRecord._validate_record`

**Exact signature**

```python
def _validate_record(self) -> CnigFeatureCodeRecord:
```

**Purpose**

Rejects malformed or inconsistent record; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CnigFeatureCodeRecord`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `self.official_source_url != expected_url`.
- Guard with a raise path: `_CODE_PATTERN.fullmatch(code) is None`.
- Explicit raise expressions: `ValueError('record source URL is not the exact family endpoint')`, `ValueError(f'{label} must contain exactly two digits')`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_record_payload`

**Exact signature**

```python
def _record_payload(record: CnigFeatureCodeRecord) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for record payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'feature_family': record.feature_family, 'type_code': record.type_code, 'subtype_code': record.subtype_code, 'official_label': record.official_label, 'legal_reference': record.legal_reference, 'regulation_or_annex_reference': record.regulation_or_annex_reference, 'official_source_url': record.official_source_url}
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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_records_sha256` via `_record_payload`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_dictionary` via `_record_payload`.

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
- Explicit raise expressions: `PlanningFeatureCodeError('Canonical integrity payload cannot be serialized')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `sha256`, `sha256(encoded).hexdigest`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_records_sha256` via `_canonical_json_sha256`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_profile_sha256` via `_canonical_json_sha256`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_source_frame_sha256` via `_canonical_json_sha256`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_planning_document_context_sha256` via `_canonical_json_sha256`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_normalized_catalogs_input_sha256` via `_canonical_json_sha256`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_sha256` via `_canonical_json_sha256`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_complete_sha256` via `_canonical_json_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_records_sha256`

**Exact signature**

```python
def _records_sha256(records: Sequence[CnigFeatureCodeRecord]) -> str:
```

**Purpose**

Private `planning` helper for records sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256([_record_payload(record) for record in records])
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::CnigFeatureCodeProfile._validate_profile` via `_records_sha256`.

**Complete source-ordered implementation**

```python
def _records_sha256(records: Sequence[CnigFeatureCodeRecord]) -> str:
    return _canonical_json_sha256([_record_payload(record) for record in records])
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `CnigFeatureCodeProfile._validate_profile`

**Exact signature**

```python
def _validate_profile(self) -> CnigFeatureCodeProfile:
```

**Purpose**

Rejects malformed or inconsistent profile; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `CnigFeatureCodeProfile`.
- Every observed return expression is reproduced without truncation:
```python
self
```

**Validation and exceptions**

- Guard with a raise path: `self.schema_version != PROFILE_SCHEMA_VERSION`.
- Guard with a raise path: `_SHA_PATTERN.fullmatch(self.canonical_records_sha256) is None`.
- Guard with a raise path: `len(set(keys)) != len(keys)`.
- Guard with a raise path: `keys != sorted(keys)`.
- Guard with a raise path: `_records_sha256(self.records) != self.canonical_records_sha256`.
- Explicit raise expressions: `ValueError('canonical records SHA256 differs from configured records')`, `ValueError('canonical records SHA256 is invalid')`, `ValueError('configured CNIG code pairs contain a duplicate')`, `ValueError('configured CNIG records must use deterministic order')`, `ValueError(f'unsupported CNIG feature-code profile schema: {self.schema_version}')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_records_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- No direct call/construction/property/import/decorator/callback reference was found. Framework-decorated invocation is documented on the decorator-bearing function itself.

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
- Explicit raise expressions: `PlanningFeatureCodeError(f'Duplicate YAML code-profile key: {key!r}')`.

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

- function object argument: `src/landscout/stages/resolve_planning_feature_codes.py::<module>` via `_UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)`.

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
            raise PlanningFeatureCodeError(f"Duplicate YAML code-profile key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `load_cnig_feature_code_profile`

**Exact signature**

```python
def load_cnig_feature_code_profile(path: str | Path) -> CnigFeatureCodeProfile:
```

**Purpose**

Load a strict offline CNIG feature-code profile.

**Return contract**

- Declared return annotation: `CnigFeatureCodeProfile`.
- Every observed return expression is reproduced without truncation:
```python
CnigFeatureCodeProfile.model_validate(payload)
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(payload, Mapping)`.
- Explicit raise expressions: `PlanningFeatureCodeError('CNIG feature-code profile is invalid')`, `PlanningFeatureCodeError('CNIG feature-code profile must be a mapping')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`.
- import: `tests/unit/test_bess_planning_feature_policy.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
)`.
- import: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_resolved_profile` via `load_cnig_feature_code_profile`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::_checked_in_policy_result` via `load_cnig_feature_code_profile`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_duplicate_yaml_key_is_rejected` via `load_cnig_feature_code_profile`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_yaml_snapshot_loads_strictly` via `load_cnig_feature_code_profile`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs` via `load_cnig_feature_code_profile`.

**Complete source-ordered implementation**

```python
def load_cnig_feature_code_profile(path: str | Path) -> CnigFeatureCodeProfile:
    """Load a strict offline CNIG feature-code profile."""

    try:
        payload = yaml.load(
            Path(path).read_text(encoding="utf-8"), Loader=_UniqueKeyLoader
        )
        if not isinstance(payload, Mapping):
            raise PlanningFeatureCodeError(
                "CNIG feature-code profile must be a mapping"
            )
        return CnigFeatureCodeProfile.model_validate(payload)
    except PlanningFeatureCodeError:
        raise
    except Exception as error:
        raise PlanningFeatureCodeError(
            "CNIG feature-code profile is invalid"
        ) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_resolved_profile`

**Exact signature**

```python
def _resolved_profile(
    profile: CnigFeatureCodeProfile | str | Path,
) -> CnigFeatureCodeProfile:
```

**Purpose**

Private `planning` helper for resolved profile; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `CnigFeatureCodeProfile`.
- Every observed return expression is reproduced without truncation:
```python
load_cnig_feature_code_profile(profile)

CnigFeatureCodeProfile.model_validate(payload)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningFeatureCodeError('In-memory CNIG feature-code profile is invalid')`.

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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `_resolved_profile`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `_resolved_profile`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_profile_sha256`

**Exact signature**

```python
def _profile_sha256(profile: CnigFeatureCodeProfile) -> str:
```

**Purpose**

Computes non-decisional summary statistics for sha256; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256(profile.model_dump(mode='json'))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_profile_sha256`.

**Complete source-ordered implementation**

```python
def _profile_sha256(profile: CnigFeatureCodeProfile) -> str:
    return _canonical_json_sha256(profile.model_dump(mode="json"))
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
_exact_string(value, label)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningFeatureCodeError(str(error))`.

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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_planning_standard` via `_strict_string`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_coded_relations` via `_strict_string`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_inspected_layer_payload` via `_strict_string`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_planning_document_context_sha256` via `_strict_string`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `_strict_string`.

**Complete source-ordered implementation**

```python
def _strict_string(value: object, label: str) -> str:
    try:
        return _exact_string(value, label)
    except ValueError as error:
        raise PlanningFeatureCodeError(str(error)) from error
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_planning_standard`

**Exact signature**

```python
def _planning_standard(document: GpuPlanningDocument) -> str:
```

**Purpose**

Private `planning` helper for planning standard; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_strict_string(distinct[0], 'planning document standard')
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(document, GpuPlanningDocument)`.
- Guard with a raise path: `len(distinct) != 1`.
- Explicit raise expressions: `PlanningFeatureCodeError('Planning document standard lineage is ambiguous')`, `PlanningFeatureCodeError('planning_document must be a GpuPlanningDocument')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `models`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_planning_standard`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `_planning_standard`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validated_code_series`

**Exact signature**

```python
def _validated_code_series(series: pd.Series, label: str) -> None:
```

**Purpose**

Checks and returns canonical code series; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None`.
- Explicit raise expressions: `PlanningFeatureCodeError(f'{label} must contain exact two-character digit strings')`.

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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_catalog_document_lineage` via `_validated_code_series`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_is_true_null`

**Exact signature**

```python
def _is_true_null(value: object) -> bool:
```

**Purpose**

Tests whether true null; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `bool`.
- Every observed return expression is reproduced without truncation:
```python
isinstance(missing, (bool, np.bool_)) and bool(missing)

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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_null_safe_equal` via `_is_true_null`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_nullable_official_value` via `_is_true_null`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_coded_meaning_rows` via `_is_true_null`.

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
type(left) is type(right) and left == right

left_null and right_null
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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_coded_meaning_rows` via `_null_safe_equal`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_nullable_official_value`

**Exact signature**

```python
def _validate_nullable_official_value(value: object, label: str) -> None:
```

**Purpose**

Rejects malformed or inconsistent nullable official value; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- Every observed return expression is reproduced without truncation:
```python
None
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, str) and value in _NULL_REFERENCE_LITERALS`.
- Explicit raise expressions: `PlanningFeatureCodeError(f'{label} contains a literal null replacement')`, `PlanningFeatureCodeError(str(error))`.

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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_code_dictionary` via `_validate_nullable_official_value`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_code_dictionary`

**Exact signature**

```python
def _validate_code_dictionary(
    result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

**Purpose**

Rejects malformed or inconsistent code dictionary; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `dict[tuple[str, str, str], dict[str, object]]`.
- Every observed return expression is reproduced without truncation:
```python
records
```

**Validation and exceptions**

- Guard with a raise path: `type(frame) is not pd.DataFrame`.
- Guard with a raise path: `frame.columns.duplicated().any() or deterministic_frame_schema_signature(frame) != CODE_DICTIONARY_SCHEMA_SIGNATURE`.
- Guard with a raise path: `frame.empty`.
- Guard with a raise path: `ordered_keys != sorted(ordered_keys)`.
- Guard with a raise path: `family not in {'PRESCRIPTION', 'INFORMATION'}`.
- Guard with a raise path: `key in records`.
- Guard with a raise path: `row['official_source_url'] != expected_url`.
- Guard with a raise path: `row['profile'] != result.profile or row['profile_sha256'] != result.profile_sha256 or row['standard_model'] != result.standard_model`.
- Guard with a raise path: `not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None`.
- Explicit raise expressions: `PlanningFeatureCodeError('code dictionary canonical schema is invalid')`, `PlanningFeatureCodeError('code dictionary contains duplicate pairs')`, `PlanningFeatureCodeError('code dictionary must be a non-geospatial DataFrame')`, `PlanningFeatureCodeError('code dictionary must contain at least one official code record')`, `PlanningFeatureCodeError('code dictionary pair order is not canonical')`, `PlanningFeatureCodeError(f'code dictionary row {position} feature family is invalid')`, `PlanningFeatureCodeError(f'code dictionary row {position} official URL is invalid')`, `PlanningFeatureCodeError(f'code dictionary row {position} result lineage differs')`, `PlanningFeatureCodeError(f'code dictionary row {position} {field} is invalid')`, `PlanningFeatureCodeError(str(error))`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `ordered_keys`, `records[key]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `_validate_code_dictionary`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_coded_meaning_rows`

**Exact signature**

```python
def _validate_coded_meaning_rows(
    result: PlanningFeatureCodeResult,
    dictionary: Mapping[tuple[str, str, str], Mapping[str, object]],
) -> None:
```

**Purpose**

Rejects malformed or inconsistent coded meaning rows; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `feature is None`.
- Guard with a raise path: `any((not _null_safe_equal(row[field], feature[field]) for field in compared_fields))`.
- Guard with a raise path: `family not in {'PRESCRIPTION', 'INFORMATION'}`.
- Guard with a raise path: `row['official_code_profile'] != result.profile or row['official_code_profile_sha256'] != result.profile_sha256`.
- Guard with a raise path: `status == 'RESOLVED_OFFICIAL'`.
- Guard with a raise path: `not isinstance(identifier, str) or not identifier`.
- Guard with a raise path: `identifier in features`.
- Guard with a raise path: `not isinstance(value, str) or _CODE_PATTERN.fullmatch(value) is None`.
- Guard with a raise path: `record is None or any((not _null_safe_equal(row[field], record[dictionary_field]) for field, dictionary_field in meaning_fields))`.
- Guard with a raise path: `status == 'UNKNOWN_CODE_PAIR'`.
- Guard with a raise path: `record is not None or any((not _is_true_null(row[field]) for field, _ in meaning_fields))`.
- Explicit raise expressions: `PlanningFeatureCodeError('coded feature ID is invalid')`, `PlanningFeatureCodeError('coded feature IDs are not globally unique')`, `PlanningFeatureCodeError('coded feature family is invalid')`, `PlanningFeatureCodeError('coded feature profile lineage differs')`, `PlanningFeatureCodeError('coded relation official meaning differs from its feature')`, `PlanningFeatureCodeError('coded relation references an unknown feature ID')`, `PlanningFeatureCodeError('resolved coded feature meaning differs from code dictionary')`, `PlanningFeatureCodeError('unknown coded feature contains an official meaning')`, `PlanningFeatureCodeError(f'coded feature official status is invalid at row {position}')`, `PlanningFeatureCodeError(f'coded feature {label} is invalid')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `features[identifier]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `_validate_coded_meaning_rows`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_catalog_document_lineage`

**Exact signature**

```python
def _validate_catalog_document_lineage(
    frame: gpd.GeoDataFrame,
    label: str,
    document: GpuPlanningDocument,
    standard_model: str,
) -> gpd.GeoDataFrame:
```

**Purpose**

Rejects malformed or inconsistent catalog document lineage; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
frame.copy(deep=True)
```

**Validation and exceptions**

- Guard with a raise path: `not frame['source_document_id'].eq(metadata.document_id).all()`.
- Guard with a raise path: `not frame['source_archive_sha256'].eq(document.extraction.archive.sha256).all()`.
- Guard with a raise path: `not frame['source_standard_model'].eq(standard_model).all()`.
- Explicit raise expressions: `PlanningFeatureCodeError(f'{label} archive lineage differs')`, `PlanningFeatureCodeError(f'{label} document lineage differs')`, `PlanningFeatureCodeError(f'{label} source standard lineage differs')`.

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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_validate_catalog_document_lineage`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_dictionary`

**Exact signature**

```python
def _dictionary(
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for dictionary; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output
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
- In-memory mutation: `output.index`, `output[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_dictionary`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_lookup`

**Exact signature**

```python
def _lookup(
    profile: CnigFeatureCodeProfile,
) -> dict[tuple[str, str, str], CnigFeatureCodeRecord]:
```

**Purpose**

Private `planning` helper for lookup; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[tuple[str, str, str], CnigFeatureCodeRecord]`.
- Every observed return expression is reproduced without truncation:
```python
{(record.feature_family, record.type_code, record.subtype_code): record for record in profile.records}
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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_coded_catalog` via `_lookup`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_coded_catalog`

**Exact signature**

```python
def _coded_catalog(
    frame: gpd.GeoDataFrame,
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> gpd.GeoDataFrame:
```

**Purpose**

Private `planning` helper for coded catalog; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `gpd.GeoDataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output
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
- In-memory mutation: `columns['official_code_label']`, `columns['official_code_profile']`, `columns['official_code_profile_sha256']`, `columns['official_code_source_url']`, `columns['official_code_status']`, `columns['official_legal_reference']`, `columns['official_regulation_reference']`, `output.index`, `output[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_coded_catalog`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_catalog_by_id`

**Exact signature**

```python
def _catalog_by_id(
    catalogs: Sequence[gpd.GeoDataFrame],
) -> dict[str, dict[str, object]]:
```

**Purpose**

Private `planning` helper for catalog by id; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, dict[str, object]]`.
- Every observed return expression is reproduced without truncation:
```python
records
```

**Validation and exceptions**

- Guard with a raise path: `identifier in records`.
- Explicit raise expressions: `PlanningFeatureCodeError('Planning feature IDs must be unique across feature catalogs')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `records[identifier]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_coded_relations` via `_catalog_by_id`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_coded_relations`

**Exact signature**

```python
def _coded_relations(
    relations: pd.DataFrame,
    coded: Sequence[gpd.GeoDataFrame],
) -> pd.DataFrame:
```

**Purpose**

Private `planning` helper for coded relations; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `pd.DataFrame`.
- Every observed return expression is reproduced without truncation:
```python
output
```

**Validation and exceptions**

- Guard with a raise path: `meaning is None`.
- Explicit raise expressions: `PlanningFeatureCodeError('Relation references an unknown feature catalog ID')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: none.
- Environment/process effects: none.
- In-memory mutation: `appended[column]`, `output.index`, `output[column]`.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_coded_relations`.

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
to_wkb(value, hex=True, include_srid=False)

value.isoformat()

_canonical_value(value.item())

{str(key): _canonical_value(item) for key, item in value.items()}

[_canonical_value(item) for item in value]

None

None

value

int(value)

number

value
```

**Validation and exceptions**

- Guard with a raise path: `isinstance(value, Real)`.
- Guard with a raise path: `not math.isfinite(number)`.
- Explicit raise expressions: `PlanningFeatureCodeError('Integrity payload contains non-finite numeric data')`, `PlanningFeatureCodeError(f'Integrity payload contains unsupported value {type(value).__name__}')`.

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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_payload` via `_canonical_value`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_compare_frame` via `_canonical_value`.

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
payload
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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_source_frame_sha256` via `_frame_payload`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_normalized_catalogs_input_sha256` via `_frame_payload`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_sha256` via `_frame_payload`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_compare_frame` via `_frame_payload`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_source_frame_sha256`

**Exact signature**

```python
def _source_frame_sha256(domain: str, frame: pd.DataFrame) -> str:
```

**Purpose**

Private `planning` helper for source frame sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256({'domain': domain, 'result_hash_schema_version': RESULT_HASH_SCHEMA_VERSION, 'frame': _frame_payload(frame)})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_inspected_layer_payload` via `_source_frame_sha256`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_parcel_identity_input_sha256` via `_source_frame_sha256`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_normalized_relations_input_sha256` via `_source_frame_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_inspected_layer_payload`

**Exact signature**

```python
def _inspected_layer_payload(layer: GpuInspectedLayer) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for inspected layer payload; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'logical_name': logical_name, 'source_layer': _strict_string(reference.source_layer, 'GPU source layer'), 'driver': _strict_string(reference.driver, 'GPU driver'), 'summary': asdict(summary), 'source_data_sha256': _source_frame_sha256('landscout.cnig_feature_codes.gpu_source_layer', data)}
```

**Validation and exceptions**

- Guard with a raise path: `not isinstance(data, gpd.GeoDataFrame)`.
- Explicit raise expressions: `PlanningFeatureCodeError('GPU inspected layer data is invalid')`, `PlanningFeatureCodeError('GPU inspected-layer context cannot be serialized')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_source_frame_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_planning_document_context_sha256` via `_inspected_layer_payload`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_planning_document_context_sha256`

**Exact signature**

```python
def _planning_document_context_sha256(document: GpuPlanningDocument) -> str:
```

**Purpose**

Private `planning` helper for planning document context sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256({'domain': 'landscout.cnig_feature_codes.planning_document_input', 'result_hash_schema_version': RESULT_HASH_SCHEMA_VERSION, 'document_metadata': asdict(archive.document), 'archive': {'filename': archive.filename, 'archive_format': archive.archive_format, 'file_size': archive.file_size, 'sha256': archive.sha256}, 'standard_models': sorted(document.extraction.standard_models), 'spatial_references': spatial_references, 'zoning': _inspected_layer_payload(document.zoning), 'related_layers': related})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningFeatureCodeError('Planning-document context cannot be hashed safely')`, `re-raise`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_planning_document_context_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_parcel_identity_input_sha256`

**Exact signature**

```python
def _parcel_identity_input_sha256(parcels: gpd.GeoDataFrame) -> str:
```

**Purpose**

Private `planning` helper for parcel identity input sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_source_frame_sha256('landscout.cnig_feature_codes.parcel_identity_input', identity)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningFeatureCodeError('Parcel identity input cannot be serialized')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: `parcels[['parcel_id', 'geometry']].copy`.
- Hashing: `_source_frame_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_parcel_identity_input_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalized_catalogs_input_sha256`

**Exact signature**

```python
def _normalized_catalogs_input_sha256(
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> str:
```

**Purpose**

Private `planning` helper for normalized catalogs input sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256({'domain': 'landscout.cnig_feature_codes.normalized_catalogs_input', 'result_hash_schema_version': RESULT_HASH_SCHEMA_VERSION, 'surface': _frame_payload(surface_features), 'line': _frame_payload(line_features), 'point': _frame_payload(point_features)})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_normalized_catalogs_input_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_normalized_relations_input_sha256`

**Exact signature**

```python
def _normalized_relations_input_sha256(relations: pd.DataFrame) -> str:
```

**Purpose**

Private `planning` helper for normalized relations input sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_source_frame_sha256('landscout.cnig_feature_codes.normalized_relations_input', relations)
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_source_frame_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_normalized_relations_input_sha256`.

**Complete source-ordered implementation**

```python
def _normalized_relations_input_sha256(relations: pd.DataFrame) -> str:
    return _source_frame_sha256(
        "landscout.cnig_feature_codes.normalized_relations_input", relations
    )
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_component_metadata`

**Exact signature**

```python
def _component_metadata(result: PlanningFeatureCodeResult) -> dict[str, object]:
```

**Purpose**

Private `planning` helper for component metadata; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `dict[str, object]`.
- Every observed return expression is reproduced without truncation:
```python
{'result_hash_schema_version': result.result_hash_schema_version, 'profile_schema_version': result.profile_schema_version, 'profile': result.profile, 'standard_model': result.standard_model, 'profile_sha256': result.profile_sha256, 'source_document_id': result.source_document_id, 'source_archive_sha256': result.source_archive_sha256, 'planning_document_context_sha256': result.planning_document_context_sha256, 'parcel_identity_input_sha256': result.parcel_identity_input_sha256, 'normalized_catalogs_input_sha256': result.normalized_catalogs_input_sha256, 'normalized_relations_input_sha256': result.normalized_relations_input_sha256, 'gpu_related_source_files_sha256': result.gpu_related_source_files_sha256, 'expected_relations_content_sha256': result.expected_relations_content_sha256}
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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_frame_sha256` via `_component_metadata`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_complete_sha256` via `_component_metadata`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_frame_sha256`

**Exact signature**

```python
def _frame_sha256(
    domain: str,
    result: PlanningFeatureCodeResult,
    frame: pd.DataFrame,
) -> str:
```

**Purpose**

Private `planning` helper for frame sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256({'domain': domain, **_component_metadata(result), 'frame': _frame_payload(frame)})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_result_with_hashes` via `_frame_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_complete_sha256`

**Exact signature**

```python
def _complete_sha256(result: PlanningFeatureCodeResult) -> str:
```

**Purpose**

Private `planning` helper for complete sha256; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `str`.
- Every observed return expression is reproduced without truncation:
```python
_canonical_json_sha256({'domain': 'landscout.cnig_feature_codes.result', **_component_metadata(result), 'code_dictionary_content_sha256': result.code_dictionary_content_sha256, 'surface_features_content_sha256': result.surface_features_content_sha256, 'line_features_content_sha256': result.line_features_content_sha256, 'point_features_content_sha256': result.point_features_content_sha256, 'relations_content_sha256': result.relations_content_sha256})
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_canonical_json_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_result_with_hashes` via `_complete_sha256`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_result_with_hashes`

**Exact signature**

```python
def _result_with_hashes(result: PlanningFeatureCodeResult) -> PlanningFeatureCodeResult:
```

**Purpose**

Private `planning` helper for result with hashes; its complete implementation below is the authoritative behavioral contract.

**Return contract**

- Declared return annotation: `PlanningFeatureCodeResult`.
- Every observed return expression is reproduced without truncation:
```python
replace(component, complete_result_content_sha256=_complete_sha256(component))
```

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: none.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_complete_sha256`, `_frame_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- import: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_build_result` via `_result_with_hashes`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::_validate_result_envelope` via `_result_with_hashes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_coordinated_output_hash_mutation_is_rejected` via `_result_with_hashes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_source_binding_hashes_bind_every_component_hash` via `_result_with_hashes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::_canonical_empty_coded_result` via `_result_with_hashes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_dictionary_schema_is_explicit` via `_result_with_hashes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_dictionary_rows_are_intrinsically_validated` via `_result_with_hashes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_scalar_lineage_contracts_are_intrinsic` via `_result_with_hashes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_official_rows_and_relation_feature_agreement_are_intrinsic` via `_result_with_hashes`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_build_result`

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

**Purpose**

Constructs result; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `PlanningFeatureCodeResult`.
- Every observed return expression is reproduced without truncation:
```python
_result_with_hashes(result)
```

**Validation and exceptions**

- Guard with a raise path: `standard != code_profile.standard_model`.
- Guard with a raise path: `factual_validation is None`.
- Explicit raise expressions: `PlanningFeatureCodeError(f'Normalized planning-feature inputs are invalid: {error}')`, `PlanningFeatureCodeError(f'Planning document standard {standard!r} differs from code-profile standard')`.

**Side effects**

- Network I/O: none.
- Filesystem read: none.
- Filesystem write: none.
- CRS/geometry calculation: none.
- Hashing: `_normalized_catalogs_input_sha256`, `_normalized_relations_input_sha256`, `_parcel_identity_input_sha256`, `_planning_document_context_sha256`, `_profile_sha256`.
- Environment/process effects: none.
- In-memory mutation: none.
- Input mutation: none.

**Repository interfaces and consumers**

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `_build_result`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `_build_result`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `_validate_result_envelope`

**Exact signature**

```python
def _validate_result_envelope(result: PlanningFeatureCodeResult) -> None:
```

**Purpose**

Rejects malformed or inconsistent result envelope; exact branches, calls, and return construction are reproduced below.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `type(result) is not PlanningFeatureCodeResult`.
- Guard with a raise path: `result.standard_model != STANDARD_MODEL`.
- Guard with a raise path: `type(version) is not int or version != expected_version`.
- Guard with a raise path: `not isinstance(value, str) or _SHA_PATTERN.fullmatch(value) is None`.
- Guard with a raise path: `getattr(result, field) != getattr(rebuilt_hashes, field)`.
- Explicit raise expressions: `PlanningFeatureCodeError('result must be a PlanningFeatureCodeResult')`, `PlanningFeatureCodeError('result standard model is invalid')`, `PlanningFeatureCodeError(f'result hash {field} is invalid')`, `PlanningFeatureCodeError(f'unsupported {label}: {version!r}')`, `PlanningFeatureCodeError(f'{field} must be a lowercase SHA256')`, `PlanningFeatureCodeError(str(error))`.

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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result_envelope` via `_validate_result_envelope`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `_validate_result_envelope`.
- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `_validate_result_envelope`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_planning_feature_code_result_envelope`

**Exact signature**

```python
def validate_planning_feature_code_result_envelope(
    result: PlanningFeatureCodeResult,
) -> None:
```

**Purpose**

Validate one coded-result envelope without rebuilding factual sources.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- No local `if` branch directly contains a raise; called validators and exception handlers remain visible in the complete implementation.
- Explicit raise expressions: `PlanningFeatureCodeError('Planning feature code result envelope is invalid')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`.
- import: `src/landscout/stages/apply_bess_planning_feature_policy.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result_envelope,
)`.
- direct call: `src/landscout/stages/apply_bess_planning_feature_policy.py::load_bess_planning_feature_application_artifacts` via `validate_planning_feature_code_result_envelope`.

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

- Guard with a raise path: `_canonical_value(_frame_payload(actual)) != _canonical_value(_frame_payload(expected))`.
- Explicit raise expressions: `PlanningFeatureCodeError(f'{label} differs from rebuilt source result')`.

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

- direct call: `src/landscout/stages/resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `_compare_frame`.

**Complete source-ordered implementation**

```python
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _canonical_value(_frame_payload(actual)) != _canonical_value(
        _frame_payload(expected)
    ):
        raise PlanningFeatureCodeError(f"{label} differs from rebuilt source result")
```

**Business boundary**

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `validate_planning_feature_code_result`

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

**Purpose**

Rebuild and validate a coded result from every factual source input.

**Return contract**

- Declared return annotation: `None`.
- No explicit return; normal completion returns `None`.

**Validation and exceptions**

- Guard with a raise path: `getattr(result, field) != getattr(expected, field)`.
- Explicit raise expressions: `PlanningFeatureCodeError('Planning-feature code result validation failed safely')`, `PlanningFeatureCodeError(f'result {field} differs from rebuilt source result')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`.
- import: `src/landscout/stages/bess_planning_feature_policy.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result,
)`.
- import: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    validate_planning_feature_code_result as _public_validate_planning_feature_code_result,
)`.
- direct call: `src/landscout/stages/bess_planning_feature_policy.py::_validate_coded_source` via `validate_planning_feature_code_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::validate_planning_feature_code_result` via `_public_validate_planning_feature_code_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_step_7d_3_1_output_integrates_with_public_coding_api` via `_public_validate_planning_feature_code_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_source_input_hash_mutation_is_rejected` via `_public_validate_planning_feature_code_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_parcel_source_change_invalidates_coded_result` via `_public_validate_planning_feature_code_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_gpu_document_context_change_invalidates_coded_result` via `_public_validate_planning_feature_code_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent` via `_public_validate_planning_feature_code_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_relation_change_invalidates_coded_result` via `_public_validate_planning_feature_code_result`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_parquet_readback_preserves_source_hash_envelope` via `_public_validate_planning_feature_code_result`.
- function object argument: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_public_api_signatures_remain_source_complete` via `inspect.signature(_public_validate_planning_feature_code_result)`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

### `resolve_planning_feature_codes`

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

**Purpose**

Attach exact official CNIG meanings without interpreting their impact.

**Return contract**

- Declared return annotation: `PlanningFeatureCodeResult`.
- Every observed return expression is reproduced without truncation:
```python
result
```

**Validation and exceptions**

- Guard with a raise path: `standard != profile.standard_model`.
- Explicit raise expressions: `PlanningFeatureCodeError('Planning-feature code resolution failed safely')`, `PlanningFeatureCodeError(f'Planning document standard {standard!r} differs from code-profile standard')`, `PlanningFeatureCodeError(f'Planning-feature code resolution failed: {error}')`, `re-raise`.

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

- re-export: `src/landscout/stages/__init__.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`.
- import: `tests/unit/test_bess_planning_feature_policy.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
)`.
- import: `tests/unit/test_resolve_planning_feature_codes.py::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    resolve_planning_feature_codes as _public_resolve_planning_feature_codes,
)`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::_compiled_fixture` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::_checked_in_policy_result` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_missing_policy_pair_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_extra_policy_pair_is_rejected_without_type_fallback` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_duplicate_policy_pair_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_prescription_information_code_spaces_remain_separate` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_official_meaning_mismatch_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_invalid_or_legal_conclusion_status_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_invalid_confidence_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_status_priority_contract_is_strict` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_unknown_yaml_field_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_noncanonical_whitespace_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_malformed_sha256_is_rejected` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_policy_entries_require_deterministic_order` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_bess_planning_feature_policy.py::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::resolve_planning_feature_codes` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_multi_geometries_are_accepted` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_empty_optional_catalogs_preserve_schema_and_crs` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_valid_relation_types_are_retained` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_step_7d_3_1_output_integrates_with_public_coding_api` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_coded_result_persists_all_source_input_hashes` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_source_input_hash_mutation_is_rejected` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_gpu_related_source_hash_is_deterministic_across_cache_roots` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_source_binding_hashes_bind_every_component_hash` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_parcel_source_change_invalidates_coded_result` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_gpu_document_context_change_invalidates_coded_result` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_catalog_change_invalidates_coded_result_even_when_coherent` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_normalized_relation_change_invalidates_coded_result` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_coding_api_rejects_relation_set_not_rebuilt_from_geometry` via `_public_resolve_planning_feature_codes`.
- direct call: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_parquet_readback_preserves_source_hash_envelope` via `_public_resolve_planning_feature_codes`.
- function object argument: `tests/unit/test_resolve_planning_feature_codes.py::test_schema_v5_public_api_signatures_remain_source_complete` via `inspect.signature(_public_resolve_planning_feature_codes)`.

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

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.


## 7. Data contracts

### `CODE_DICTIONARY_COLUMNS` — canonical or derived frame-column schema

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

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `feature_family` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `type_code` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `subtype_code` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 4 | `official_label` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `legal_reference` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 6 | `regulation_or_annex_reference` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 7 | `official_source_url` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 8 | `profile` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 9 | `profile_sha256` | Pandas nullable string dtype | non-null where the owning lineage validator requires it | source lineage | Textual lineage; physical proof requires the corresponding byte/source revalidation boundary. |
| 10 | `standard_model` | Pandas nullable string dtype | physical dtype permits true null; row-semantic validators below determine where null is allowed | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |

### `CODE_DICTIONARY_DTYPES` — dtype contract aligned with a canonical schema

```python
CODE_DICTIONARY_DTYPES = tuple("str" for _ in CODE_DICTIONARY_COLUMNS)
```

### `CODE_DICTIONARY_SCHEMA_SIGNATURE` — portable schema/index signature

```python
CODE_DICTIONARY_SCHEMA_SIGNATURE: dict[str, object] = {
    "columns": list(CODE_DICTIONARY_COLUMNS),
    "dtypes": list(CODE_DICTIONARY_DTYPES),
    "index_class": "pandas.Index",
    "index_names": [None],
    "index_level_dtypes": ["int64"],
}
```

| Position/value | Exact field | Dtype | Nullability | Classification | Meaning / explicit non-meaning |
|---:|---|---|---|---|---|
| 1 | `columns` | ['feature_family', 'type_code', 'subtype_code', 'official_label', 'legal_reference', 'regulation_or_annex_reference', 'official_source_url', 'profile', 'profile_sha256', 'standard_model'] | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 2 | `dtypes` | ['str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str', 'str'] | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 3 | `index_class` | pandas.Index | non-null where each row must receive a classification | diagnostic or policy-derived result | Stores one value from its separately documented closed domain; domain values are not columns. |
| 4 | `index_names` | [None] | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |
| 5 | `index_level_dtypes` | ['int64'] | membership/order comes from this declaration; effective null/value rules come from the owning validators reproduced in section 6 and the module-specific contract notes | factual/derived field identified by the owning schema | The complete introducing and consuming implementations below define the value; no proxy/policy meaning is inferred from spelling alone. |


No enum/status/Literal value is classified as a column unless it is separately present in a canonical schema declaration. Mapping keys, JSON keys, dataclass fields, and configuration leaves remain distinct categories.

## 8. Interfaces

This module defines an exact `__all__` contract:

| Export | Kind | Origin | Included in `__all__` |
|---|---|---|---|
| `CnigFeatureCodeProfile` | public symbol defined in this module | `defined in `src/landscout/stages/resolve_planning_feature_codes.py`` | yes |
| `PlanningFeatureCodeError` | public symbol defined in this module | `defined in `src/landscout/stages/resolve_planning_feature_codes.py`` | yes |
| `PlanningFeatureCodeResult` | public symbol defined in this module | `defined in `src/landscout/stages/resolve_planning_feature_codes.py`` | yes |
| `load_cnig_feature_code_profile` | public symbol defined in this module | `defined in `src/landscout/stages/resolve_planning_feature_codes.py`` | yes |
| `resolve_planning_feature_codes` | public symbol defined in this module | `defined in `src/landscout/stages/resolve_planning_feature_codes.py`` | yes |
| `validate_planning_feature_code_result` | public symbol defined in this module | `defined in `src/landscout/stages/resolve_planning_feature_codes.py`` | yes |
| `validate_planning_feature_code_result_envelope` | public symbol defined in this module | `defined in `src/landscout/stages/resolve_planning_feature_codes.py`` | yes |

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
