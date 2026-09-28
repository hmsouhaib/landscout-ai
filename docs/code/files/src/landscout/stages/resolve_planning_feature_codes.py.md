# `src/landscout/stages/resolve_planning_feature_codes.py`

- Source: [src/landscout/stages/resolve_planning_feature_codes.py](../../../../../../src/landscout/stages/resolve_planning_feature_codes.py)
- Source SHA256: `cdb463f06cea6f58881681bca7e95e80b0770e69f4cdf3cc373329eca7bc0235`
- Source SHA256 basis: `git-content`
- Source lines: 1177; Git blob at R12 start: `0205c2e41d57f978b4be91eeddb1577be7f4a447`

Git/index/checkout Python bytes remain unchanged. Local semantic closure is not independent approval. [R12 receipt](../../../../../../docs/code/audit/R12_CNIG_FEATURE_CODE_RESOLVER.md).

## Scope, imports and ownership

This component attaches configured offline CNIG meanings to factual GPU feature codes. It does not compile/apply BESS policy, aggregate parcel statuses, grant legal/BESS/ICPE permission, exclude parcels, score/rank or assess grid capacity/access. RESOLVED_OFFICIAL and UNKNOWN_CODE_PAIR describe dictionary resolution, not BESS suitability. Profile schema is 2; result/hash schema is 5; standard is CNIG PLU v2017.

Seven declared exports are imported and listed in `landscout.stages`: `CnigFeatureCodeProfile`, `PlanningFeatureCodeError`, `PlanningFeatureCodeResult`, `load_cnig_feature_code_profile`, `resolve_planning_feature_codes`, `validate_planning_feature_code_result`, `validate_planning_feature_code_result_envelope`. Other directly importable models/helpers are not declared exports. No artifact manifest, Parquet loader or writer exists in this module.

Actual repository imports belong to [frame integrity](../common/frame_integrity.py.md), [planning feature schema](../common/planning_feature_schema.py.md), [strict YAML](../common/strict_yaml.py.md), [GPU](../sources/gpu_fr.py.md) and [factual planning features](enrich_planning_features.py.md). Downstream [compiler](bess_planning_feature_policy.py.md) uses the source-complete validator; [application artifact loader](apply_bess_planning_feature_policy.py.md) uses the public local envelope guard. Their contracts are not transferred to this module. [R4](../../../../audit/R4_CNIG_CONFIGURATION.md) covers configured YAML separately; [tests](../../../tests/unit/test_resolve_planning_feature_codes.py.md) exercise synthetic physical sources.

Standard-library imports own JSON/SHA, Unicode, regex/numeric/date checks, Mapping/Sequence, dataclass replacement and paths. Pydantic owns strict individual fields/frozen models, pandas/NumPy frames/scalars, GeoPandas geospatial frames, Shapely WKB/geometry. There is no direct HTTP, ZIP, overlay, PDF or artifact-manifest import. Shared factual validation can perform physical reads and geometry reconstruction.

## Public paths and ordering

| Boundary | Required inputs | Actual work |
| --- | --- | --- |
| Loader | path | Read bytes, strict YAML, Mapping guard, validate profile. |
| Resolver | planning_document, parcels, surface_features, line_features, point_features, relations, code_profile | Reconstruct/load profile; standard; shared factual validation; builder reuses that result; intrinsic envelope; return. |
| Full validator | Same seven then result | Envelope first; reconstruct/load profile; builder triggers factual validation; compare 19 scalars and five frames; return None. |
| Envelope validator | result | Exact type, scalar/schema/row consistency and recomputed local hashes; no source reconstruction. |

All public arguments are required positional-or-keyword arguments. code_profile accepts the model or str/Path, not an arbitrary compiled BESS policy. Private _build_result optionally accepts an already obtained factual_validation; that branch skips a second call, not the entire public source boundary. Public error wrappers differ and are specified in their notices.

The factual owner validates supplied catalogs/relations/parcels, rebuilds canonical catalogs from physical related GPU layers, compares them, reconstructs expected relations and compares them. Its GPU owner revalidates source-config identity/extraction evidence and batch-reloads related spatial sources with FIDs, compares inspected data/summary and performs source-family postchecks. Those are delegated contracts, not new archive acquisition or universal filesystem safety promises here. Counting one batch call does not count underlying reads.

## Tables, nulls, units and propagation

The dictionary has exactly ten columns in CODE_DICTIONARY_COLUMNS order, all pandas str dtype, nonempty, with unnamed plain pandas.Index/int64 (not RangeIndex). Rows are all configured records, sorted by exact family/type/subtype. Profile validation requires order rather than sorting silently. Optional references are required keys allowing None; model text guards admit certain textual-null spellings while result dictionary guards reject None/nan/<NA> strings (existing A-004, not repaired here).

Each factual feature catalog has 27 columns; coding appends the seven OFFICIAL_CODE_COLUMNS to give 34: official_code_status, official_code_label, official_legal_reference, official_regulation_reference, official_code_source_url, official_code_profile, official_code_profile_sha256. Relations have 28 factual columns plus these seven (35 total). Lookup for catalog rows is the exact family/type/subtype triple; relations receive meanings by planning_feature_id from the coded catalog. Unknown triples retain their objects/relations and profile lineage, set UNKNOWN_CODE_PAIR and four null meaning fields. No type-only/prefix/cross-family/wildcard fallback. Features without any relation remain in their catalog.

Factual dtypes come from common.planning_feature_schema: feature text is str except permitted all-null optional raw text/file/URL object representations; geometry dtype geometry, area/length float64, point members int64. Relations use str, seven float64 metric fields and three nullable Int64 member fields. Seven added official columns are str. Area units are m², lengths metres, shares percentages, members counts, not policy scores. Coded canonical schemas require EPSG:2154 active geometry named geometry and unnamed plain int64 Index; source normalized schemas use RangeIndex. Coding preserves index values/name while changing the class. Empty optional catalogs retain schema/CRS. No repair, dropping, reprojection or overlay is done by the coding loops.

Policy profile collections are immutable tuples/frozen models with immutable leaves. Module __all__ and schema-signature dict/list declarations are not claimed immutable. The frozen result still exposes five mutable frames. Copies protect input frames during building, not against later result mutation; public validation must be called at trust boundaries.

## Canonical commitments, not legal proof

| Commitment | Payload / origin |
| --- | --- |
| canonical_records_sha256 | Ordered seven-field record list, canonical JSON, no extra domain/version. |
| profile_sha256 | Complete model_dump(mode=json), including records, date and schema; not YAML bytes. |
| planning_document_context_sha256 | Domain planning_document_input/version5; metadata, archive identity, sorted standards/references, inspected zoning/related frame commitments; no full paths. |
| parcel_identity_input_sha256 | Domain parcel_identity_input/version5; parcel_id and geometry, index and CRS only. |
| normalized_catalogs_input_sha256 | Domain normalized_catalogs_input/version5; surface/line/point full frame payloads. |
| normalized_relations_input_sha256 | Domain normalized_relations_input/version5; full factual relations. |
| gpu_related_source_files_sha256 | Propagated factual owner verified_gpu_sources.v1: archive SHA, sorted logical source identities/relative paths/driver/count/CRS/FIDs and file type/size/SHA/category. |
| expected_relations_content_sha256 | Propagated factual owner expected_relations.v2: rebuilt ordered relation schema/index/rows. |
| Five content hashes | Separate dictionary/surface/line/point/relations domains, 13 common metadata items and complete frame payload. |
| complete_result_content_sha256 | Domain result, same metadata and five component hashes. |

Local domain names above use prefix landscout.cnig_feature_codes; propagated factual-owner domains instead use landscout.planning_features. Exact strings appear in their respective implementations. Canonical JSON is UTF-8, sorted keys, compact, Unicode preserved, NaN disallowed at JSON level. Before numeric conversion, _canonical_value maps true missing scalars including NaN to null; earlier geometry/date/NumPy/container branches remain as documented below. Geometry uses to_wkb(hex=True, include_srid=False), with no explicit output dimension/byte order or new M/Z guarantee. frame_integrity contributes column dtypes, full index class/names/level dtypes and geospatial metadata; unlike the R11 interpreter these signatures participate here. Row/column/index ordering is significant. Metadata hash propagation is not an independent reread of the underlying archive.

Dictionary/row coherence, component hashing and physical source reconstruction are different levels. A nonempty dictionary with canonically empty/resealed outputs can pass the local envelope despite populated original sources; the complete validator rebuilds those sources. This is a documented lightweight boundary, not automatic evidence of a new defect. Configured URLs/date/labels do not perform a live official/legal verification.

## Module declarations

Exact imports are preserved in the full snapshot. Declarations add no extra historical closure units.

<a id="declaration---all--"></a>
### `landscout.stages.resolve_planning_feature_codes.__all__`

Source lines 41–49. Seven-name declared public export list, checked against package imports and __all__.

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

<a id="declaration-profile-schema-version"></a>
### `landscout.stages.resolve_planning_feature_codes.PROFILE_SCHEMA_VERSION`

Source lines 51–51. Exact version/standard/text-normalization declaration; scope and validation are specified above.

```python
PROFILE_SCHEMA_VERSION = 2
```

<a id="declaration-result-hash-schema-version"></a>
### `landscout.stages.resolve_planning_feature_codes.RESULT_HASH_SCHEMA_VERSION`

Source lines 52–52. Exact version/standard/text-normalization declaration; scope and validation are specified above.

```python
RESULT_HASH_SCHEMA_VERSION = 5
```

<a id="declaration-standard-model"></a>
### `landscout.stages.resolve_planning_feature_codes.STANDARD_MODEL`

Source lines 53–53. Exact version/standard/text-normalization declaration; scope and validation are specified above.

```python
STANDARD_MODEL = "CNIG PLU v2017"
```

<a id="declaration-official-text-normalization"></a>
### `landscout.stages.resolve_planning_feature_codes.OFFICIAL_TEXT_NORMALIZATION`

Source lines 54–54. Exact version/standard/text-normalization declaration; scope and validation are specified above.

```python
OFFICIAL_TEXT_NORMALIZATION = "GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"
```

<a id="declaration-prescription-official-source-url"></a>
### `landscout.stages.resolve_planning_feature_codes.PRESCRIPTION_OFFICIAL_SOURCE_URL`

Source lines 55–58. Exact offline configured endpoint identity; no network request is implied.

```python
PRESCRIPTION_OFFICIAL_SOURCE_URL = (
    "https://www.geoportail-urbanisme.gouv.fr/standard/"
    "cnig_PLU_2017/codes/PrescriptionUrbaType"
)
```

<a id="declaration-information-official-source-url"></a>
### `landscout.stages.resolve_planning_feature_codes.INFORMATION_OFFICIAL_SOURCE_URL`

Source lines 59–62. Exact offline configured endpoint identity; no network request is implied.

```python
INFORMATION_OFFICIAL_SOURCE_URL = (
    "https://www.geoportail-urbanisme.gouv.fr/standard/"
    "cnig_PLU_2017/codes/InformationUrbaType"
)
```

<a id="declaration-featurefamily"></a>
### `landscout.stages.resolve_planning_feature_codes.FeatureFamily`

Source lines 64–64. Closed Literal domain for exact lookup family or factual resolution status, not a BESS assessment.

```python
FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
```

<a id="declaration-officialcodestatus"></a>
### `landscout.stages.resolve_planning_feature_codes.OfficialCodeStatus`

Source lines 65–65. Closed Literal domain for exact lookup family or factual resolution status, not a BESS assessment.

```python
OfficialCodeStatus = Literal["RESOLVED_OFFICIAL", "UNKNOWN_CODE_PAIR"]
```

<a id="declaration-code-dictionary-columns"></a>
### `landscout.stages.resolve_planning_feature_codes.CODE_DICTIONARY_COLUMNS`

Source lines 67–78. Exact ten-column ordered dictionary schema, not compiler policy schema.

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

<a id="declaration-code-dictionary-dtypes"></a>
### `landscout.stages.resolve_planning_feature_codes.CODE_DICTIONARY_DTYPES`

Source lines 79–79. Ten str dtypes in dictionary-column order.

```python
CODE_DICTIONARY_DTYPES = tuple("str" for _ in CODE_DICTIONARY_COLUMNS)
```

<a id="declaration-code-dictionary-schema-signature"></a>
### `landscout.stages.resolve_planning_feature_codes.CODE_DICTIONARY_SCHEMA_SIGNATURE`

Source lines 80–86. Mutable module-level reference signature with ordered columns/dtypes and unnamed pandas.Index/int64; not a retained profile collection.

```python
CODE_DICTIONARY_SCHEMA_SIGNATURE: dict[str, object] = {
    "columns": list(CODE_DICTIONARY_COLUMNS),
    "dtypes": list(CODE_DICTIONARY_DTYPES),
    "index_class": "pandas.Index",
    "index_names": [None],
    "index_level_dtypes": ["int64"],
}
```

<a id="declaration--code-pattern"></a>
### `landscout.stages.resolve_planning_feature_codes._CODE_PATTERN`

Source lines 88–88. Compiled fullmatch pattern used for exact ASCII code or lowercase SHA syntax.

```python
_CODE_PATTERN = re.compile(r"[0-9]{2}")
```

<a id="declaration--sha-pattern"></a>
### `landscout.stages.resolve_planning_feature_codes._SHA_PATTERN`

Source lines 89–89. Compiled fullmatch pattern used for exact ASCII code or lowercase SHA syntax.

```python
_SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

<a id="declaration--null-reference-literals"></a>
### `landscout.stages.resolve_planning_feature_codes._NULL_REFERENCE_LITERALS`

Source lines 90–90. Frozen forbidden textual-null spellings for result nullable references; not applied by optional profile text helper.

```python
_NULL_REFERENCE_LITERALS = frozenset({"None", "nan", "<NA>"})
```

## Qualified symbol contracts

Each original symbol has a notice and matching owner note. Literal signatures specify actual parameters, defaults, annotations and returns; missing annotations are not None annotations. Private helpers have only the guards/wrappers stated, not universal exception translation.

<a id="planningfeaturecodeerror"></a>

<a id="symbol-planningfeaturecodeerror"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeError`

Source lines 93–94. Kind: class. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
class PlanningFeatureCodeError(ValueError):
```

ValueError subclass for unprovable factual code integrity; no custom initializer or fields. Explicit errors pass through the public wrappers. It is not a BESS policy exception.

<a id="_strictmodel"></a>

<a id="symbol--strictmodel"></a>
### `landscout.stages.resolve_planning_feature_codes._StrictModel`

Source lines 97–98. Kind: class. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
class _StrictModel(BaseModel):
```

Pydantic base with extra="forbid" and frozen=True, not global strict=True. Strict scalar fields and frozen nested models/record tuples protect retained profile values; this does not freeze module-level schema dictionaries or result DataFrames.

<a id="_exact_string"></a>

<a id="symbol--exact-string"></a>
### `landscout.stages.resolve_planning_feature_codes._exact_string`

Source lines 101–104. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _exact_string(value: object, label: str) -> str:
```

Accept an isinstance(str) value only when nonempty and equal to strip(); return it unchanged or raise ValueError. No normalization or numeric coercion.

<a id="_canonical_official_text"></a>

<a id="symbol--canonical-official-text"></a>
### `landscout.stages.resolve_planning_feature_codes._canonical_official_text`

Source lines 107–108. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _canonical_official_text(value: str) -> str:
```

Return NFC-normalized text joined from split() whitespace fragments with single spaces. Pure string transformation; no local factual field mutation, legal lookup or I/O.

<a id="_validate_official_text"></a>

<a id="symbol--validate-official-text"></a>
### `landscout.stages.resolve_planning_feature_codes._validate_official_text`

Source lines 111–117. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _validate_official_text(value: object, label: str) -> str:
```

First require an exact string, then equality with _canonical_official_text. Return unchanged text; ValueError if noncanonical. It tests that configured display text is already canonical, rather than silently cleaning it.

<a id="_validate_optional_official_text"></a>

<a id="symbol--validate-optional-official-text"></a>
### `landscout.stages.resolve_planning_feature_codes._validate_optional_official_text`

Source lines 120–123. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _validate_optional_official_text(value: object, label: str) -> str | None:
```

Return None unchanged; otherwise delegate to _validate_official_text. The optional annotation permits a null value, not omission of the owning required field. Textual null literals are not specially rejected here (existing A-004).

<a id="officialsourceurls"></a>

<a id="symbol-officialsourceurls"></a>
### `landscout.stages.resolve_planning_feature_codes.OfficialSourceUrls`

Source lines 126–140. Kind: class. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
class OfficialSourceUrls(_StrictModel):
```

Two required StrictStr endpoints in a frozen model. The after-validator compares exact configured identities, not DNS, downloaded content or legal currency.

<a id="symbol-officialsourceurls-prescription"></a>
### `landscout.stages.resolve_planning_feature_codes.OfficialSourceUrls.prescription`

Source lines 127–127. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
prescription: StrictStr
```

Required StrictStr equal to PRESCRIPTION_OFFICIAL_SOURCE_URL. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-officialsourceurls-information"></a>
### `landscout.stages.resolve_planning_feature_codes.OfficialSourceUrls.information`

Source lines 128–128. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
information: StrictStr
```

Required StrictStr equal to INFORMATION_OFFICIAL_SOURCE_URL. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-officialsourceurls--validate-urls"></a>
### `landscout.stages.resolve_planning_feature_codes.OfficialSourceUrls._validate_urls`

Source lines 131–140. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
    def _validate_urls(self) -> OfficialSourceUrls:
```

Check prescription then information against their exact module endpoint constants; ValueError on any mismatch, return self otherwise. No URL normalization/network request; query, port, credentials, alternate host and fragments are not equivalent identities.

Exact decorators (not extra units):

```python
    @model_validator(mode="after")
```

<a id="cnigfeaturecoderecord"></a>

<a id="symbol-cnigfeaturecoderecord"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeRecord`

Source lines 143–173. Kind: class. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
class CnigFeatureCodeRecord(_StrictModel):
```

Seven required fields: closed family, two strict two-digit strings, canonical label, two required nullable canonical references and exact family URL. Frozen scalar record; no mapping retained and no default reference values.

<a id="symbol-cnigfeaturecoderecord-feature-family"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeRecord.feature_family`

Source lines 144–144. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
feature_family: FeatureFamily
```

Required Literal PRESCRIPTION or INFORMATION. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecoderecord-type-code"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeRecord.type_code`

Source lines 145–145. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
type_code: StrictStr
```

Required StrictStr of exactly two ASCII digits; leading zero preserved. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecoderecord-subtype-code"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeRecord.subtype_code`

Source lines 146–146. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
subtype_code: StrictStr
```

Required StrictStr of exactly two ASCII digits; 00 is an exact subtype, not wildcard. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecoderecord-official-label"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeRecord.official_label`

Source lines 147–147. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
official_label: StrictStr
```

Required StrictStr, nonblank exact already-canonical display text. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecoderecord-legal-reference"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeRecord.legal_reference`

Source lines 148–148. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
legal_reference: StrictStr | None
```

Required StrictStr-or-None; true null permitted, omission not defaulted. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecoderecord-regulation-or-annex-reference"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeRecord.regulation_or_annex_reference`

Source lines 149–149. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
regulation_or_annex_reference: StrictStr | None
```

Required StrictStr-or-None; true null permitted, omission not defaulted. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecoderecord-official-source-url"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeRecord.official_source_url`

Source lines 150–150. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
official_source_url: StrictStr
```

Required StrictStr exactly matching its family endpoint. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecoderecord--validate-record"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeRecord._validate_record`

Source lines 153–173. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
    def _validate_record(self) -> CnigFeatureCodeRecord:
```

Require type and subtype fullmatch ASCII [0-9]{2}; validate label and both optional references; select expected URL by family and compare exact identity. Return self, ValueError on failure. Does not infer meaning from prefixes or trim raw codes.

Exact decorators (not extra units):

```python
    @model_validator(mode="after")
```

<a id="_record_payload"></a>

<a id="symbol--record-payload"></a>
### `landscout.stages.resolve_planning_feature_codes._record_payload`

Source lines 176–185. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _record_payload(record: CnigFeatureCodeRecord) -> dict[str, object]:
```

Return a new seven-key dictionary of record declarations, retaining true null references. No lineage/profile/version added and no validation or I/O performed.

<a id="_canonical_json_sha256"></a>

<a id="symbol--canonical-json-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes._canonical_json_sha256`

Source lines 188–201. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _canonical_json_sha256(value: object) -> str:
```

JSON serialize supplied payload with ensure_ascii=False, allow_nan=False, sort_keys=True and compact separators, encode UTF-8, hash SHA256. Serialization exceptions become chained PlanningFeatureCodeError. Unlike _canonical_value, this helper does not first convert arbitrary geometry/NumPy objects.

<a id="_records_sha256"></a>

<a id="symbol--records-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes._records_sha256`

Source lines 204–205. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _records_sha256(records: Sequence[CnigFeatureCodeRecord]) -> str:
```

Hash the ordered list of seven-field _record_payload outputs. No sorting or extra domain/version here; model validation separately requires canonical triple order. Not a raw YAML byte digest.

<a id="cnigfeaturecodeprofile"></a>

<a id="symbol-cnigfeaturecodeprofile"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile`

Source lines 208–239. Kind: class. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
class CnigFeatureCodeProfile(_StrictModel):
```

Eight required fields in a frozen model: strict version/profile/hash, Literal standard/normalization, frozen endpoints, retrieval date and nonempty tuple of frozen records. Date follows Pydantic date validation (not StrictStr); input sequences become tuples preserving their order. No retained mutable input mapping.

<a id="symbol-cnigfeaturecodeprofile-schema-version"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.schema_version`

Source lines 211–211. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
schema_version: StrictInt
```

Required StrictInt exactly 2. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecodeprofile-profile"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.profile`

Source lines 212–212. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
profile: StrictStr = Field(min_length=1)
```

Required StrictStr nonempty and strip-invariant. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecodeprofile-standard-model"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.standard_model`

Source lines 213–213. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
standard_model: Literal["CNIG PLU v2017"]
```

Required Literal CNIG PLU v2017. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecodeprofile-official-text-normalization"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.official_text_normalization`

Source lines 214–214. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
official_text_normalization: Literal["GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"]
```

Required Literal GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecodeprofile-official-sources"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.official_sources`

Source lines 215–215. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
official_sources: OfficialSourceUrls
```

Required frozen OfficialSourceUrls with two exact endpoints. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecodeprofile-retrieval-date"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.retrieval_date`

Source lines 216–216. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
retrieval_date: date
```

Required date; serialized as JSON ISO date in profile digest. Configured metadata, not proof of a retrieval. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecodeprofile-canonical-records-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.canonical_records_sha256`

Source lines 217–217. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
canonical_records_sha256: StrictStr
```

Required StrictStr lowercase 64-hex SHA of ordered seven-field records. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecodeprofile-records"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile.records`

Source lines 218–218. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
records: tuple[CnigFeatureCodeRecord, ...] = Field(min_length=1)
```

Required nonempty tuple of frozen CnigFeatureCodeRecord objects; unique sorted exact triples. YAML lists convert without reordering. Pydantic field validation applies; frozen retained value, no field-level I/O.

<a id="symbol-cnigfeaturecodeprofile--validate-profile"></a>
### `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile._validate_profile`

Source lines 221–239. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
    def _validate_profile(self) -> CnigFeatureCodeProfile:
```

After field/nested validation require schema 2, exact profile string, lowercase 64-hex records hash; form exact family/type/subtype triples, reject duplicates and nonlexicographic order, then compare recomputed ordered-record digest. Return self or ValueError. Does not sort declarations or acquire official sources.

Exact decorators (not extra units):

```python
    @model_validator(mode="after")
```

<a id="load_cnig_feature_code_profile"></a>

<a id="symbol-load-cnig-feature-code-profile"></a>
### `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile`

Source lines 242–259. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def load_cnig_feature_code_profile(path: str | Path) -> CnigFeatureCodeProfile:
```

Required str-or-Path path: read bytes, decode with common.strict_yaml.loads_strict_yaml, require Mapping, model_validate and return profile. Preserve PlanningFeatureCodeError, wrap StrictYamlError with its message/cause, wrap other Exception as invalid profile. Filesystem read only; no default path or remote retrieval.

<a id="planningfeaturecoderesult"></a>

<a id="symbol-planningfeaturecoderesult"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult`

Source lines 263–289. Kind: class. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
class PlanningFeatureCodeResult:
```

Frozen dataclass with 24 required fields: 19 scalars (two integers and 17 strings) plus five mutable tables (dictionary DataFrame, three feature GeoDataFrames and relations DataFrame). No constructor runtime validation or deep table immutability. Explicit validators establish integrity; no artifact manifest/loader/writer is defined here.

Exact decorators (not extra units):

```python
@dataclass(frozen=True)
```

<a id="symbol-planningfeaturecoderesult-result-hash-schema-version"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.result_hash_schema_version`

Source lines 266–266. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
result_hash_schema_version: int
```

Integer version 5; envelope requires exact int, not bool. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-profile-schema-version"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.profile_schema_version`

Source lines 267–267. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
profile_schema_version: int
```

Integer version 2; envelope requires exact int, not bool. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-profile"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.profile`

Source lines 268–268. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
profile: str
```

Configured exact profile name. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-standard-model"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.standard_model`

Source lines 269–269. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
standard_model: str
```

Exact CNIG PLU v2017 standard. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-profile-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.profile_sha256`

Source lines 270–270. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
profile_sha256: str
```

Canonical JSON profile digest, not YAML byte digest. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-source-document-id"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.source_document_id`

Source lines 271–271. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
source_document_id: str
```

Exact source document identifier. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-source-archive-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.source_archive_sha256`

Source lines 272–272. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
source_archive_sha256: str
```

Propagated archive-byte identity; this field alone performs no byte verification. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-planning-document-context-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.planning_document_context_sha256`

Source lines 273–273. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
planning_document_context_sha256: str
```

Recomputed in-memory source-document contextual payload digest. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-parcel-identity-input-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.parcel_identity_input_sha256`

Source lines 274–274. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
parcel_identity_input_sha256: str
```

Digest of parcel_id/geometry, original index and CRS, not every parcel column. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-normalized-catalogs-input-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.normalized_catalogs_input_sha256`

Source lines 275–275. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
normalized_catalogs_input_sha256: str
```

Digest of three complete factual catalog payloads. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-normalized-relations-input-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.normalized_relations_input_sha256`

Source lines 276–276. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
normalized_relations_input_sha256: str
```

Digest of supplied complete factual relation frame. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-gpu-related-source-files-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.gpu_related_source_files_sha256`

Source lines 277–277. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
gpu_related_source_files_sha256: str
```

Propagated shared factual-validation commitment to verified GPU-related source files/FIDs/metadata. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-expected-relations-content-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.expected_relations_content_sha256`

Source lines 278–278. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
expected_relations_content_sha256: str
```

Propagated shared factual-validation digest of relations rebuilt from geometry. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-code-dictionary-content-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.code_dictionary_content_sha256`

Source lines 279–279. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
code_dictionary_content_sha256: str
```

Dictionary frame component digest, bound to common metadata. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-surface-features-content-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.surface_features_content_sha256`

Source lines 280–280. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
surface_features_content_sha256: str
```

Surface coded-frame component digest. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-line-features-content-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.line_features_content_sha256`

Source lines 281–281. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
line_features_content_sha256: str
```

Line coded-frame component digest. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-point-features-content-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.point_features_content_sha256`

Source lines 282–282. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
point_features_content_sha256: str
```

Point coded-frame component digest. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-relations-content-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.relations_content_sha256`

Source lines 283–283. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
relations_content_sha256: str
```

Coded relations component digest. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-complete-result-content-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.complete_result_content_sha256`

Source lines 284–284. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
complete_result_content_sha256: str
```

Complete result digest combining metadata and five component commitments. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-code-dictionary"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.code_dictionary`

Source lines 285–285. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
code_dictionary: pd.DataFrame
```

Mutable ten-column pd.DataFrame, all configured records including unused triples. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-surface-features"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.surface_features`

Source lines 286–286. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
surface_features: gpd.GeoDataFrame
```

Mutable coded SURFACE GeoDataFrame: factual 27 columns plus seven official fields. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-line-features"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.line_features`

Source lines 287–287. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
line_features: gpd.GeoDataFrame
```

Mutable coded LINE GeoDataFrame: factual 27 columns plus seven official fields. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-point-features"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.point_features`

Source lines 288–288. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
point_features: gpd.GeoDataFrame
```

Mutable coded POINT GeoDataFrame: factual 27 columns plus seven official fields. Required dataclass constructor field; annotation is not runtime validation.

<a id="symbol-planningfeaturecoderesult-relations"></a>
### `landscout.stages.resolve_planning_feature_codes.PlanningFeatureCodeResult.relations`

Source lines 289–289. Kind: field. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
relations: pd.DataFrame
```

Mutable pd.DataFrame: factual 28 columns plus seven official fields; no geometry column. Required dataclass constructor field; annotation is not runtime validation.

<a id="_resolved_profile"></a>

<a id="symbol--resolved-profile"></a>
### `landscout.stages.resolve_planning_feature_codes._resolved_profile`

Source lines 292–303. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _resolved_profile(
    profile: CnigFeatureCodeProfile | str | Path,
) -> CnigFeatureCodeProfile:
```

For an existing CnigFeatureCodeProfile, dump mode="python", warnings="error", then reconstruct via model_validate; any Exception becomes an invalid in-memory profile error. Otherwise call the path loader. Frozen supplied objects are not automatically trusted; model_construct/model_copy can bypass model guards before this boundary.

<a id="_profile_sha256"></a>

<a id="symbol--profile-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes._profile_sha256`

Source lines 306–307. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _profile_sha256(profile: CnigFeatureCodeProfile) -> str:
```

Hash profile.model_dump(mode="json") as canonical JSON. Includes date, schema, endpoints, normalization, ordered records and their declared digest; not the source YAML bytes and not a fresh reconstruction here.

<a id="_strict_string"></a>

<a id="symbol--strict-string"></a>
### `landscout.stages.resolve_planning_feature_codes._strict_string`

Source lines 310–314. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _strict_string(value: object, label: str) -> str:
```

Require isinstance(str), nonempty and unchanged by strip(); raise PlanningFeatureCodeError or return original value. Factual scalar guard, no coercion or mutation.

<a id="_planning_standard"></a>

<a id="symbol--planning-standard"></a>
### `landscout.stages.resolve_planning_feature_codes._planning_standard`

Source lines 317–331. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _planning_standard(document: GpuPlanningDocument) -> str:
```

Require GpuPlanningDocument, gather extraction standard identifiers and nonnull metadata standard, deduplicate in encounter order and require exactly one; validate exact nonblank string and return it. It checks object metadata only; no source read or comparison to configured profile until caller.

<a id="_validated_code_series"></a>

<a id="symbol--validated-code-series"></a>
### `landscout.stages.resolve_planning_feature_codes._validated_code_series`

Source lines 334–339. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _validated_code_series(series: pd.Series, label: str) -> None:
```

Visit tolist() and require each value a string fullmatching two ASCII digits; PlanningFeatureCodeError otherwise. Return None; accepts leading zeros, rejects null/numeric values, no fallback or mutation.

<a id="_is_true_null"></a>

<a id="symbol--is-true-null"></a>
### `landscout.stages.resolve_planning_feature_codes._is_true_null`

Source lines 342–349. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _is_true_null(value: object) -> bool:
```

Recognize None and pd.NA; otherwise call pd.isna, treating TypeError/ValueError as false and accepting only a scalar bool/np.bool_ true result. Return bool, not array truth evaluation or recognition of literal null strings.

<a id="_null_safe_equal"></a>

<a id="symbol--null-safe-equal"></a>
### `landscout.stages.resolve_planning_feature_codes._null_safe_equal`

Source lines 352–357. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _null_safe_equal(left: object, right: object) -> bool:
```

If either operand is a true null, require both null; otherwise require identical Python types then equality. Used on scalar row values, not a general array comparator; no coercion, I/O or broad exception wrapper.

<a id="_validate_nullable_official_value"></a>

<a id="symbol--validate-nullable-official-value"></a>
### `landscout.stages.resolve_planning_feature_codes._validate_nullable_official_value`

Source lines 360–368. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _validate_nullable_official_value(value: object, label: str) -> None:
```

Allow true null; reject None/nan/<NA> literal text before delegating exact/canonical text validation. Delegated ValueError is translated to PlanningFeatureCodeError with cause. This is stricter on textual nulls than the record model (existing A-004).

<a id="_validate_code_dictionary"></a>

<a id="symbol--validate-code-dictionary"></a>
### `landscout.stages.resolve_planning_feature_codes._validate_code_dictionary`

Source lines 371–440. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _validate_code_dictionary(
    result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

Require exact pd.DataFrame (not subclass/GeoDataFrame), unique columns and complete deterministic signature: ten ordered str columns and unnamed plain int64 Index. Require nonempty rows, closed family, two-digit codes, unique triples, canonical label, nullable references, exact family URL and matching profile/hash/standard; require lexicographic triple order. Return triple-to-row dictionary. Local PlanningFeatureCodeError guards; caller public wrapper handles unexpected malformed objects. Does not reload profile or prove its full record set.

<a id="_validate_coded_meaning_rows"></a>

<a id="symbol--validate-coded-meaning-rows"></a>
### `landscout.stages.resolve_planning_feature_codes._validate_coded_meaning_rows`

Source lines 443–529. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _validate_coded_meaning_rows(
    result: PlanningFeatureCodeResult,
    dictionary: Mapping[tuple[str, str, str], Mapping[str, object]],
) -> None:
```

Use the dictionary lookup already validated and supplied by the envelope owner. For each of three catalogs check exact family/codes/profile, then RESOLVED_OFFICIAL requires a dictionary triple and null-safe equality of four meaning fields; UNKNOWN_CODE_PAIR requires absent triple and four true-null meanings. Reject other statuses and missing/duplicate global feature IDs. For every relation find planning_feature_id, then compare family/raw codes and seven official columns with that feature. Return None. This is intrinsic row/dictionary consistency, not physical source or overlay reconstruction.

<a id="_validate_catalog_document_lineage"></a>

<a id="symbol--validate-catalog-document-lineage"></a>
### `landscout.stages.resolve_planning_feature_codes._validate_catalog_document_lineage`

Source lines 532–547. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _validate_catalog_document_lineage(
    frame: gpd.GeoDataFrame,
    label: str,
    document: GpuPlanningDocument,
    standard_model: str,
) -> gpd.GeoDataFrame:
```

Check raw type/subtype code series; require every document ID, archive SHA and standard equal supplied source values; return deep frame copy. Series.eq(...).all() is equality, not file writing or hashing. PlanningFeatureCodeError on mismatch; no geometry change.

<a id="_dictionary"></a>

<a id="symbol--dictionary"></a>
### `landscout.stages.resolve_planning_feature_codes._dictionary`

Source lines 550–567. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _dictionary(
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> pd.DataFrame:
```

Build every configured record, including unused triples, with three profile lineage fields; cast ten columns to str arrays and create unnamed plain int64 Index from arange. Return mutable DataFrame in declared order; no sorting, lookup fallback or disk output.

<a id="_lookup"></a>

<a id="symbol--lookup"></a>
### `landscout.stages.resolve_planning_feature_codes._lookup`

Source lines 570–576. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _lookup(
    profile: CnigFeatureCodeProfile,
) -> dict[tuple[str, str, str], CnigFeatureCodeRecord]:
```

Create dict keyed by exact (feature_family, type_code, subtype_code) to record, preserving record identity. Relies on validated unique profile records; no type-only, prefix, wildcard-00 or alternative-family lookup.

<a id="_coded_catalog"></a>

<a id="symbol--coded-catalog"></a>
### `landscout.stages.resolve_planning_feature_codes._coded_catalog`

Source lines 579–610. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _coded_catalog(
    frame: gpd.GeoDataFrame,
    profile: CnigFeatureCodeProfile,
    profile_hash: str,
) -> gpd.GeoDataFrame:
```

Deep-copy entire catalog, exact-triple lookup for every row, append seven str official fields. Known triples carry label/references/URL and RESOLVED_OFFICIAL; absent triples retain row with null meanings and UNKNOWN_CODE_PAIR; both carry profile/hash. Preserve factual columns, geometry, CRS, order and index values/name, converting index to plain pd.Index from copied array. No object is dropped for lack of parcel relation.

<a id="_catalog_by_id"></a>

<a id="symbol--catalog-by-id"></a>
### `landscout.stages.resolve_planning_feature_codes._catalog_by_id`

Source lines 613–625. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _catalog_by_id(
    catalogs: Sequence[gpd.GeoDataFrame],
) -> dict[str, dict[str, object]]:
```

Build feature-ID-to-row mapping across all three coded catalogs; duplicate converted string ID raises PlanningFeatureCodeError. The local helper uses str() keys, while public input validation enforces actual identity strings. No spatial join.

<a id="_coded_relations"></a>

<a id="symbol--coded-relations"></a>
### `landscout.stages.resolve_planning_feature_codes._coded_relations`

Source lines 628–647. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _coded_relations(
    relations: pd.DataFrame,
    coded: Sequence[gpd.GeoDataFrame],
) -> pd.DataFrame:
```

Copy relations, require exact string planning_feature_id and resolve that ID in catalog mapping; unknown ID raises PlanningFeatureCodeError. Append seven official values from the matched feature, not a separate code-pair lookup; plain Index conversion retains values/name. All factual relation fields and order remain.

<a id="_canonical_value"></a>

<a id="symbol--canonical-value"></a>
### `landscout.stages.resolve_planning_feature_codes._canonical_value`

Source lines 650–684. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _canonical_value(value: object) -> object:
```

Convert geometry to WKB hex with include_srid=False; date/datetime/Timestamp to isoformat; NumPy scalar recursively via item; Mapping to string-keyed recursive dict; tuple/list/ndarray to list; None/pd.NA/scalar pd.isna true to None; bool unchanged; Integral to int; Real to finite float; str unchanged. Unsupported values and nonfinite numbers after null handling raise PlanningFeatureCodeError. NaN becomes null; date branch precedes null detection. No bytes support, explicit WKB dimension/byte order, geometry repair or new M/Z guarantee.

<a id="_frame_payload"></a>

<a id="symbol--frame-payload"></a>
### `landscout.stages.resolve_planning_feature_codes._frame_payload`

Source lines 687–696. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
```

Return deterministic schema signature, ordered canonical index values and row lists in actual column/row order. Schema helper includes column names/dtypes, full index class/names/level dtypes and GeoDataFrame active geometry/CRS JSON. No mutation, path I/O or independent validity/metric check.

<a id="_source_frame_sha256"></a>

<a id="symbol--source-frame-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes._source_frame_sha256`

Source lines 699–706. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _source_frame_sha256(domain: str, frame: pd.DataFrame) -> str:
```

Hash {domain, result_hash_schema_version:5, frame:_frame_payload(frame)}. Domain argument distinguishes input roles; schema, row/index order and canonical values matter, not arbitrary Python repr.

<a id="_inspected_layer_payload"></a>

<a id="symbol--inspected-layer-payload"></a>
### `landscout.stages.resolve_planning_feature_codes._inspected_layer_payload`

Source lines 709–731. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _inspected_layer_payload(layer: GpuInspectedLayer) -> dict[str, object]:
```

Return exact logical/source-layer/driver strings, dataclass summary and source-frame hash of GeoDataFrame data under landscout.cnig_feature_codes.gpu_source_layer. Reject nongeospatial data; preserve own errors and wrap other Exception contextually. Hashes inspected in-memory data, not physical file bytes or full path.

<a id="_planning_document_context_sha256"></a>

<a id="symbol--planning-document-context-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes._planning_document_context_sha256`

Source lines 734–777. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _planning_document_context_sha256(document: GpuPlanningDocument) -> str:
```

Hash domain landscout.cnig_feature_codes.planning_document_input and version5; metadata asdict, archive filename/format/size/SHA, sorted standards, all spatial source-layer/driver pairs sorted, zoning inspected payload and related payloads sorted by logical name. Preserve own errors, wrap other Exception contextually. Absolute archive/cache paths are excluded. This recomputes a contextual commitment, not a physical archive read or legal check.

<a id="_parcel_identity_input_sha256"></a>

<a id="symbol--parcel-identity-input-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes._parcel_identity_input_sha256`

Source lines 780–793. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _parcel_identity_input_sha256(parcels: gpd.GeoDataFrame) -> str:
```

Copy parcel_id plus geometry into GeoDataFrame retaining source index and CRS, then source-frame hash under landscout.cnig_feature_codes.parcel_identity_input. Other parcel facts are intentionally excluded; no distance/overlay computed here.

<a id="_normalized_catalogs_input_sha256"></a>

<a id="symbol--normalized-catalogs-input-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes._normalized_catalogs_input_sha256`

Source lines 796–809. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _normalized_catalogs_input_sha256(
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> str:
```

Hash domain landscout.cnig_feature_codes.normalized_catalogs_input, version5 and ordered payloads for surface, line and point. Preserves each frame schema/index/order/geometry; no filtering or source file read.

<a id="_normalized_relations_input_sha256"></a>

<a id="symbol--normalized-relations-input-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes._normalized_relations_input_sha256`

Source lines 812–815. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _normalized_relations_input_sha256(relations: pd.DataFrame) -> str:
```

Source-frame hash of full normalized relations under landscout.cnig_feature_codes.normalized_relations_input; exact schema/index/order and all row values participate, not just identity pairs.

<a id="_component_metadata"></a>

<a id="symbol--component-metadata"></a>
### `landscout.stages.resolve_planning_feature_codes._component_metadata`

Source lines 818–833. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _component_metadata(result: PlanningFeatureCodeResult) -> dict[str, object]:
```

Return 13 propagated metadata items: result/profile versions, profile/standard/profile hash, document/archive and six source-input commitments. No I/O, recomputation or validation of those source hashes.

<a id="_frame_sha256"></a>

<a id="symbol--frame-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes._frame_sha256`

Source lines 836–847. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _frame_sha256(
    domain: str,
    result: PlanningFeatureCodeResult,
    frame: pd.DataFrame,
) -> str:
```

Hash component domain, common metadata and full frame payload. Used for dictionary, surface, line, point and relations with separate domains; changes to either source-binding commitment affect each component.

<a id="_complete_sha256"></a>

<a id="symbol--complete-sha256"></a>
### `landscout.stages.resolve_planning_feature_codes._complete_sha256`

Source lines 850–861. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _complete_sha256(result: PlanningFeatureCodeResult) -> str:
```

Hash landscout.cnig_feature_codes.result with common metadata and five component hashes. It does not hash arbitrary dataclass repr or reread frames itself; _result_with_hashes first recomputes those five commitments.

<a id="_result_with_hashes"></a>

<a id="symbol--result-with-hashes"></a>
### `landscout.stages.resolve_planning_feature_codes._result_with_hashes`

Source lines 864–885. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _result_with_hashes(result: PlanningFeatureCodeResult) -> PlanningFeatureCodeResult:
```

Compute five component hashes, dataclasses.replace to attach them, then second replace for complete digest. Returns new frozen envelope sharing the table objects; not semantic validation, source reread or proof that coherent changes are authorized.

<a id="_build_result"></a>

<a id="symbol--build-result"></a>
### `landscout.stages.resolve_planning_feature_codes._build_result`

Source lines 888–968. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

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

Seven required inputs plus optional factual_validation=None. Recheck standard; if validation absent call validate_normalized_planning_feature_inputs (ValueError translated), otherwise reuse supplied private validation object. Check/copy catalog lineage; hash profile; code three catalogs and relations; build dictionary; compute contextual, parcel, catalog and relation commitments; propagate GPU-files and expected-relations commitments; construct schema5 result then reseal. Conditional delegated physical I/O, no blanket no-I/O claim. It does not itself run final envelope check or reconstruct a supplied profile.

<a id="_validate_result_envelope"></a>

<a id="symbol--validate-result-envelope"></a>
### `landscout.stages.resolve_planning_feature_codes._validate_result_envelope`

Source lines 971–1039. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _validate_result_envelope(result: PlanningFeatureCodeResult) -> None:
```

Require exact result type, exact built-in int versions5/2 (not bool), standard, strict profile/document and lowercase SHA syntax for all hash fields. Validate dictionary; canonical coded feature/relations schemas; row/dictionary/ID meaning agreement; recompute five component and complete hashes and compare all six. Schema TypeError/ValueError are translated. Local validation only: no source/profile loading, physical reconstruction or proof of source completeness.

<a id="validate_planning_feature_code_result_envelope"></a>

<a id="symbol-validate-planning-feature-code-result-envelope"></a>
### `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result_envelope`

Source lines 1042–1054. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def validate_planning_feature_code_result_envelope(
    result: PlanningFeatureCodeResult,
) -> None:
```

One required result, return None. Call private envelope guard; preserve PlanningFeatureCodeError, wrap any other Exception as invalid coded-result envelope. Does not rebuild factual sources; used by downstream artifact validation, not itself an artifact loader.

<a id="_compare_frame"></a>

<a id="symbol--compare-frame"></a>
### `landscout.stages.resolve_planning_feature_codes._compare_frame`

Source lines 1057–1061. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

```python
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
```

Compare canonicalized full frame payloads; mismatch raises PlanningFeatureCodeError with label. Schema/dtype/index class, values, ordering and geospatial metadata participate. No tolerance, source read or mutation.

<a id="validate_planning_feature_code_result"></a>

<a id="symbol-validate-planning-feature-code-result"></a>
### `landscout.stages.resolve_planning_feature_codes.validate_planning_feature_code_result`

Source lines 1064–1126. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

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

Eight required positional-or-keyword inputs: seven source/profile inputs then result; return None. First intrinsic envelope, then resolve/revalidate profile, call builder without cached factual validation (therefore source-complete factual guard), compare 19 scalars and five frame payloads. Preserve own error; other Exception becomes safe-validation error. A malformed envelope can fail before any physical reconstruction.

<a id="resolve_planning_feature_codes"></a>

<a id="symbol-resolve-planning-feature-codes"></a>
### `landscout.stages.resolve_planning_feature_codes.resolve_planning_feature_codes`

Source lines 1129–1177. Kind: function. Owner: `landscout.stages.resolve_planning_feature_codes`.

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

Seven required positional-or-keyword inputs. Resolve/revalidate profile first, compare planning standard, call shared factual validator once, pass returned validation into builder, then private envelope guard before return. Preserve own error, translate ValueError with contextual message, wrap other Exception safely. One shared validation invocation does not mean one physical file read; delegated GPU/overlay work is source-complete.

## Complete source snapshot

Exact full Git-content UTF-8 source. Byte identity supports provenance, not semantic correctness by itself.

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
