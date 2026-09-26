# `src/landscout/stages/apply_bess_planning_feature_policy.py`

- Source: [src/landscout/stages/apply_bess_planning_feature_policy.py](../../../../../../src/landscout/stages/apply_bess_planning_feature_policy.py)
- Source SHA256: `76b4f4d2fa3dbe09442718810c0a113cc8d7b4b1c2ffa3f7f07fcc4f3a250a61`
- Source SHA256 basis: `git-content`
- Source lines: 1350; Git blob at R9 start: `3d542b089b9763f4ed1b212e1253a9fe87c865ac`

Git/index/checkout source bytes are unchanged; the full source snapshot below is exact UTF-8 LF. Semantic local closure is not independent approval. [R9 evidence](../../../../../../docs/code/audit/R9_BESS_CNIG_APPLICATION.md).

## Scope, owners and public interfaces

This stage propagates already-compiled exact BESS/CNIG policy evidence to three coded feature catalogs and their existing relations. It does not aggregate a parcel status, select a winning priority/confidence, interpret local text, issue a legal conclusion, reject parcels or score them. It performs no new spatial join in its own propagation algorithm; source-complete validation delegated upstream can rebuild factual intersections. No environmental classification, Natura 2000 or ZNIEFF policy is introduced.

Seven names are exported by this module and reexported as the application subset of `landscout.stages`: `BessPlanningFeatureApplicationArtifactManifest`, `BessPlanningFeatureApplicationError`, `BessPlanningFeatureApplicationResult`, `apply_bess_planning_feature_policy`, `load_bess_planning_feature_application_artifacts`, `validate_bess_planning_feature_application_result` and `validate_bess_planning_feature_application_result_envelope`. The ArtifactRecord is importable but absent from both public lists. No public artifact writer exists here.

Repository owners: [common row contracts](../common/bess_application_contract.py.md), [canonical schemas](../common/planning_feature_schema.py.md), [intrinsic relation metrics](../common/planning_feature_contract.py.md), [frame signatures](../common/frame_integrity.py.md), [portable names](../common/artifact_paths.py.md), [immutable JSON](../common/immutable_mapping.py.md), [strict JSON](../common/strict_json.py.md), [technical tolerance](../common/planning_overlay.py.md), [GPU source](../sources/gpu_fr.py.md), [CNIG coding](resolve_planning_feature_codes.py.md) and [compiled policy](bess_planning_feature_policy.py.md). The downstream [aggregator](aggregate_bess_planning_feature_policy.py.md) is separately approved documentary R8/R8.1, not re-audited here. The [paired tests](../../../tests/unit/test_apply_bess_planning_feature_policy.py.md) exercise both public paths and private helpers. Standard-library imports supply dataclass replacement, canonical JSON/hash, numeric/time types, regex, mappings, paths and BytesIO; GeoPandas, NumPy, Pandas, Pydantic, PyProj and Shapely are third-party owners, not repository policy authorities.

## Exact propagation and preservation

The lookup key is the exact `(feature_family, type_code, subtype_code)` triple from the compiled table, matched to feature_family/type_code_raw/subtype_code_raw. Type/subtype are two ASCII digits; leading zeroes remain meaningful. There is no prefix, family-agnostic, text, legal or nearest-code fallback. A RESOLVED_OFFICIAL row must have a matching policy entry and becomes APPLIED_EXACT_POLICY. An UNKNOWN_CODE_PAIR row must have no matching entry and becomes UNRESOLVED_CODE_PAIR with six truly null decision values. Missing resolved entries, unexpected entries for unknown rows and other official statuses fail. An applied entry whose configured precheck_status is UNKNOWN remains exact applied evidence, not an unresolved pair.

Catalogs are copied deeply before the suffix is appended, retaining factual/official columns, rows, index, active geometry and CRS. There is no feature filtering or geometry repair. Relations copy the suffix from the referenced enriched object by planning_feature_id, not by a second independent code lookup. Every referenced object must exist. The 22 factual/official agreement columns in the declaration below must agree null-safely; the local result envelope also compares all 18 policy columns and the appropriate source metric. All catalog objects, including those without any relation, undergo intrinsic validation and contribute to the document-wide status/priority bijection. Missing relations do not prove absence of constraints or legal clearance.

Canonical catalogs use active geometry `geometry`, EPSG:2154, plain unnamed int64 Index, exact ordered factual + seven official + eighteen policy columns. The common schema owner defines optional raw text/filename/URL dtype variants: in nonempty catalogs an all-null optional raw field is object, otherwise str; empty catalogs retain role-specific declared defaults. Relations are a non-geospatial DataFrame with its exact ordered prefix, str official columns, float64 metrics and nullable Int64 point counts. The result retains no parcel frame and adds no parcel decision.

| Suffix position / field (all start with bess_cnig_) | Dtype and meaning |
| --- | --- |
| 1 policy_application_status | str; APPLIED_EXACT_POLICY or UNRESOLVED_CODE_PAIR |
| 2 precheck_status | str; copied exact decision, or true null |
| 3 precheck_confidence | str; copied HIGH/MEDIUM/LOW, or true null |
| 4 status_priority | nullable Int64; copied positive configured priority, or null; not a score |
| 5 rationale | str; copied exact nonempty text, or null |
| 6 required_human_action | str; copied exact nonempty text, or null |
| 7 limitations | str; copied exact nonempty text, or null |
| 8 application_scope | str; FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY |
| 9 policy_scope | str; OFFICIAL_CNIG_CODE_MEANING_ONLY |
| 10 local_feature_text_interpreted | nonnullable bool False |
| 11 local_regulation_content_interpreted | nonnullable bool False |
| 12 legal_conclusion_produced | nonnullable bool False |
| 13 parcel_status_aggregated | nonnullable bool False; unlike downstream aggregation |
| 14 parcel_rejection_performed | nonnullable bool False |
| 15 score_calculated | nonnullable bool False |
| 16 policy_profile | str; supplied compiled-policy profile |
| 17 policy_sha256 | str; propagated policy-config content digest |
| 18 policy_result_sha256 | str; propagated complete compiled-policy result digest |

The common row owner checks exact policy dtypes before domains: five precheck statuses including UNKNOWN, three confidences, positive integral priority (not bool), exact nonempty decision text, no textual null sentinels, all six flags literally False, scopes and row/envelope lineage. Resolved official rows require label plus HTTPS source URL; legal/regulation references may be null. Unknown official rows require all four official meaning fields null. The scope is evidence only; HTTPS-format validation of an official reference is not network acquisition.

## Geometry and metric integrity

The common catalog guard validates every geometry as nonempty, valid, exactly 2D and appropriate to SURFACE Polygon/MultiPolygon, LINE LineString/MultiLineString or POINT Point/MultiPoint. Exact GPU feature IDs bind document, logical layer and source ID; families and logical layers agree; source_crs must be Lambert-93-equivalent. IDs are globally unique across catalogs. Area m² and length m must be finite, positive and agree with measured geometry within the technical tolerance; point_member_count is a positive integral exact member count.

The common intrinsic relation owner requires positive parcel area, nonnegative finite applicable metrics and unrelated metrics null. SURFACE: positive area means AREA_OVERLAP, zero means TOUCH_ONLY; intersection cannot exceed parcel/feature areas beyond tolerance and shares equal 100×intersection/denominator within the derived percentage tolerance. LINE: positive length means LENGTH_OVERLAP, zero means TOUCH_ONLY; intersection cannot exceed positive source length beyond tolerance. POINT: inside + boundary counts cannot exceed source members; INSIDE requires at least one inside member, BOUNDARY_TOUCH requires zero inside and at least one boundary member. Parcel/feature pairs must be unique.

Application then compares relation feature_area_m2 to catalog feature_area_m2, source_line_length_m to feature_length_m, or point_member_count to point_member_count. POINT uses exact null-safe equality. SURFACE/LINE reject bool/non-Real values and compare using `max(1e-6, reference * 1e-12)`, reference=max(abs(stored),abs(feature)). The common guards already checked finiteness/positivity. This tolerance is numerical integrity, never a BESS threshold. Local envelopes do not recompute spatial intersection membership against parcels; the source-complete chain does.

## Four distinct trust paths

1. Builder: ten required inputs (planning_document, parcels, surface_features, line_features, point_features, relations, code_profile, coded_result, policy_config, policy_result); call the full policy validator through _validate_policy_source once, build once, validate the application envelope, return. Profile/config may be validated models or str/Path inputs under their owners' reconstruction rules.
2. Full result validator: those ten inputs plus result; application envelope first, fourteen application/upstream locks plus seven policy/CNIG locks, one source-complete policy-owner validation, one build, exact comparison of all 28 scalars and all four frame payloads. Local/lock failures occur before expensive source validation.
3. Public envelope validator: one result; directly calls _validate_result_envelope. No broad try/except or physical GPU I/O is present in this public wrapper. It proves intrinsic consistency and five recomputed application digests, not equality to actual upstream frames or a physical source.
4. Artifact loader: seven required arguments, five str-or-Path locations then coded_result and policy_result. Validate both upstream envelopes and their compatibility BEFORE manifest.read_bytes; parse strict JSON/model, compare locks, capture/read four artifacts, construct result, validate its envelope, build once from supplied upstreams, compare every scalar/frame. It does not accept omitted upstreams and does not call heavy physical GPU validation.

The source-complete chain for paths 1/2 is application → compiled-policy validator → CNIG result validator → normalized planning-feature input validator → GPU spatial source revalidation. It rebuilds normalized catalogs/relations from inspected physical related layers and compares complete content. One instrumented owner call is not one physical read or one internal pass. The source chain is not a download or proof of opening the fabricated archive path of a synthetic fixture.

Loader compatibility checks seven source identities (including CNIG profile schema 2), nonempty exact equality of policy/dictionary key sets, and null-safe equality of official label/legal/regulation references for every key. Official source URL is not one of that helper's three text comparisons; upstream envelope owners separately validate coded meaning and policy rows. Upstream envelope validation is stronger than identity equality but is still not physical GPU revalidation. The application envelope does not independently strip/recompute the four propagated coded-prefix hashes; source locks and reconstruction from exact upstreams provide that separate binding.

## Models, bytes and error ownership

Result hash schema 2 and manifest schema 2 are distinct from policy result schema 1 and CNIG result schema 5 (profile schema 2 upstream). Result is a frozen dataclass with 28 scalar fields plus three GeoDataFrames and one DataFrame: construction alone validates nothing and frames remain mutable. Both Pydantic metadata classes inherit extra=forbid/frozen=True; there is no global strict mode. Required scalar StrictStr/StrictInt/StrictBool and Literal fields, required nullable CRS, and ordered tuple records are detailed per field below.

ArtifactRecord first creates local frozen copies of schema/CRS, then validates basename/counts/SHA/role-geospatial/CRS/active-geometry-name, and only then assigns the frozen signature and, when nonnull, the frozen CRS with object.__setattr__. Canonical JSON freezing rejects cycles, non-string keys, nonfinite floats and unsupported/mutable leaves; mappings are detached FrozenDict and sequences tuples. Serializers return fresh plain JSON containers. Local helpers/after-validators raise ValueError (Pydantic turns validation failures into ValidationError); they are not already application errors. The result envelope wraps only its explicit local guards, not every conceivable third-party error. Builder, full validator and loader preserve application errors and wrap other Exception causes; the source-owner adapter wraps any delegated Exception.

Records must be SURFACE_FEATURES, LINE_FEATURES, POINT_FEATURES, RELATIONS in exactly that order and casefold-unique filenames. First three geospatial flags are True with nonnull CRS equal to schema CRS and nonempty geometry_column; relation flag False with null CRS in both positions. Filenames are exact portable Parquet basenames: reject separators/absolute paths, controls, Windows forbidden characters/reserved stems and trailing dot/space; extension is case-insensitive. Count is nonnegative strict int, size positive strict int in bytes, SHA lowercase 64 hex. Record construction alone does not prove actual rows, geometry or file bytes.

The private reader compares Path.name, captures bytes once, checks byte length then raw SHA256, parses exactly those bytes via BytesIO using GeoPandas/Pandas, checks rows, complete frozen schema and CRS/type. It has explicit application-error mismatch guards but no broad wrapper around read_bytes/Parquet/PyProj; the public loader supplies that wrapper. No root containment, same-directory requirement, symlink rejection, atomic fileset, post-read path check or public writer is promised. A path replacement after capture need not invalidate the bytes already captured. Manifest is strict UTF-8 JSON with duplicate/nonfinite/non-object rejection, but no external manifest byte seal is an argument here.

## Canonical hashes

Canonical JSON uses ensure_ascii=False, allow_nan=False, sort_keys=True, compact separators and UTF-8 SHA256. Only object keys are sorted: row, index, column and list order remains significant. _frame_payload commits the entire deterministic schema (ordered columns/dtypes; qualified index class, names, level dtypes; active geometry and CRS PROJJSON for GeoDataFrames), every index value and every cell in order. DataFrame attrs and external path names are excluded unless actual supported cell content. The explicit index-class schema field is not a Python object repr.

Scalar canonicalization: None/pd.NA/scalar missing values including NaN/NaT become null; an array missing-test does not become scalar null. Exactly 2D geometry becomes coordinate_dimension=2 plus little-endian 2D WKB hex with no SRID; CRS is separately committed. Dates/datetimes/Timestamps use isoformat, NumPy scalars recurse through item(), bool is checked before Integral, finite Real becomes float. Infinity and unsupported cells fail. MultiIndex tuple values are not supported merely because the schema helper can describe a MultiIndex.

Domain strings are data, not fictitious callable owners. Prefix (literal data, not a Python reference):

```text
landscout.bess_planning_feature_application.
```

| Digest | Domain suffix | Payload besides domain |
| --- | --- | --- |
| surface_features_content_sha256 | surface_features | all 23 component metadata fields + full surface frame |
| line_features_content_sha256 | line_features | same metadata + full line frame |
| point_features_content_sha256 | point_features | same metadata + full point frame |
| relations_content_sha256 | relations | same metadata + full relation frame |
| complete_result_content_sha256 | result | same metadata + the four application component digests above |

The 23 metadata fields are all result scalars EXCEPT those five output digests: schema/scopes/six flags, policy profile/config/result version/result digest, CNIG profile/config/result version/result digest, source document/archive and four cnig_*_content_sha256 prefix digests. They are literal named keys in _component_metadata, reproduced in the complete snapshot. Policy/config/CNIG/source hashes are propagated, not redefined by this module. The four output digests and complete digest are recalculated here. Record.sha256 instead hashes raw Parquet bytes: compression changes may alter it without altering canonical frame content. Schema versions/payloads remain unchanged by R9.

## Documentation and evidence limits

The 109 original source symbols below are manually described; declarations/imports/exports add no denominator credit. Signatures/ranges and the full source snapshot are mechanical byte bindings, not a semantic certification. The paired companion records first-guard and instrumentation limits. Independent R9 review, global audit acceptance and visual rendering remain pending; only the focused existing tests and offline checks reported in the R9 receipt are execution evidence.

## Module declarations

These literal declarations add no original symbol credit. Imports and owners are explained above; declaration values are source excerpts, not runtime imports.

<a id="declaration---all--"></a>
### `landscout.stages.apply_bess_planning_feature_policy.__all__`

Source lines 64–72. Seven stable application exports; mutable module export metadata is not a loaded policy model.

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

<a id="declaration-result-hash-schema-version"></a>
### `landscout.stages.apply_bess_planning_feature_policy.RESULT_HASH_SCHEMA_VERSION`

Source lines 74–74. Canonical application result version2; unchanged by documentary R9.

```python
RESULT_HASH_SCHEMA_VERSION = 2
```

<a id="declaration-artifact-manifest-schema-version"></a>
### `landscout.stages.apply_bess_planning_feature_policy.ARTIFACT_MANIFEST_SCHEMA_VERSION`

Source lines 75–75. Manifest metadata version2; distinct constant despite same number.

```python
ARTIFACT_MANIFEST_SCHEMA_VERSION = 2
```

<a id="declaration-artifact-kind"></a>
### `landscout.stages.apply_bess_planning_feature_policy.ARTIFACT_KIND`

Source lines 76–76. Literal identity of this application artifact family.

```python
ARTIFACT_KIND = "BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"
```

<a id="declaration-artifactrole"></a>
### `landscout.stages.apply_bess_planning_feature_policy.ArtifactRole`

Source lines 78–83. Type alias for four literal role strings; no standalone runtime validation.

```python
ArtifactRole = Literal[
    "SURFACE_FEATURES",
    "LINE_FEATURES",
    "POINT_FEATURES",
    "RELATIONS",
]
```

<a id="declaration-artifact-roles"></a>
### `landscout.stages.apply_bess_planning_feature_policy.ARTIFACT_ROLES`

Source lines 85–90. Required role tuple/order, used by manifest and loader strict zip.

```python
ARTIFACT_ROLES: tuple[ArtifactRole, ...] = (
    "SURFACE_FEATURES",
    "LINE_FEATURES",
    "POINT_FEATURES",
    "RELATIONS",
)
```

<a id="declaration-relation-feature-agreement-columns"></a>
### `landscout.stages.apply_bess_planning_feature_policy.RELATION_FEATURE_AGREEMENT_COLUMNS`

Source lines 91–114. Exactly22 shared factual/official columns checked null-safely before propagation and again in envelope. Provider/portal and regulation_url_raw are not members; full upstream reconstruction protects complete prefixes separately.

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

<a id="declaration-sha-pattern"></a>
### `landscout.stages.apply_bess_planning_feature_policy.SHA_PATTERN`

Source lines 115–115. Fullmatch is used for lowercase64-hex textual digest checks, not byte hashing.

```python
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

<a id="declaration-code-pattern"></a>
### `landscout.stages.apply_bess_planning_feature_policy.CODE_PATTERN`

Source lines 116–116. Fullmatch requires exactly two ASCII digits; preserves leading zeroes.

```python
CODE_PATTERN = re.compile(r"[0-9]{2}")
```

<a id="declaration-result-frame-fields"></a>
### `landscout.stages.apply_bess_planning_feature_policy.RESULT_FRAME_FIELDS`

Source lines 228–233. Four frame attributes excluded when deriving scalar field list.

```python
RESULT_FRAME_FIELDS = (
    "surface_features",
    "line_features",
    "point_features",
    "relations",
)
```

<a id="declaration-result-scalar-fields"></a>
### `landscout.stages.apply_bess_planning_feature_policy.RESULT_SCALAR_FIELDS`

Source lines 234–238. Dataclass declaration order of all28 non-frame fields; used for manifest/hash syntax/scalar reconstruction comparisons. Includes five output digests; component metadata excludes them.

```python
RESULT_SCALAR_FIELDS = tuple(
    field
    for field in BessPlanningFeatureApplicationResult.__dataclass_fields__
    if field not in RESULT_FRAME_FIELDS
)
```

## Qualified symbol contracts

Each heading owns exactly one original symbol. Quoted signatures give parameter order/types/defaults and return annotation; notices distinguish actual behavior, callers and effects. Fields are required unless explicitly declared otherwise. Complete bodies, imports and decorators are in the final snapshot.

<a id="symbol-bessplanningfeatureapplicationerror"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationError`

Source lines 119–120. Kind: class. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
class BessPlanningFeatureApplicationError(ValueError):
```

Application-specific ValueError subclass; explicit integrity failures and public broad wrappers use it. No methods or I/O. It does not imply that every private helper directly raises this subclass.

<a id="symbol--strictmodel"></a>
### `landscout.stages.apply_bess_planning_feature_policy._StrictModel`

Source lines 123–124. Kind: class. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
class _StrictModel(BaseModel):
```

Internal Pydantic base for record and manifest; extra fields forbidden and attribute assignment frozen. No global strict setting. Metadata deep freezing is performed by the record validator, not by this base alone.

<a id="symbol--exact-string"></a>
### `landscout.stages.apply_bess_planning_feature_policy._exact_string`

Source lines 127–130. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _exact_string(value: object, label: str) -> str:
```

Given value and diagnostic label, require a str that is nonempty and already stripped; return the same string unchanged or raise builtin ValueError. Called by SHA/model/envelope checks. Pure: no coercion, trimming or I/O.

<a id="symbol--sha256-string"></a>
### `landscout.stages.apply_bess_planning_feature_policy._sha256_string`

Source lines 133–137. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _sha256_string(value: object, label: str) -> str:
```

Validate the exact string first, then lowercase 64-hex fullmatch; return unchanged digest or builtin ValueError. Record/manifest/envelope callers determine subsequent wrapping. No bytes are hashed here.

<a id="symbol-bessplanningfeatureapplicationartifactrecord"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactRecord`

Source lines 140–187. Kind: class. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
class BessPlanningFeatureApplicationArtifactRecord(_StrictModel):
```

Eight required fields describe one captured Parquet artifact; CRS is nullable but required. Frozen extra-forbidden model; role controls geospatial semantics. Pydantic validation/serialization calls the two methods below; public loader later verifies physical bytes/schema. No constructor file I/O.

<a id="symbol-bessplanningfeatureapplicationartifactrecord-artifact-role"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactRecord.artifact_role`

Source lines 143–143. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
artifact_role: ArtifactRole
```

Required Literal of the four roles; selects geospatial expectation. No row ordering or sorting is inferred from this field.

<a id="symbol-bessplanningfeatureapplicationartifactrecord-filename"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactRecord.filename`

Source lines 144–144. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
filename: StrictStr
```

Required StrictStr portable local Parquet basename; Path.name must match at readback. No root/symlink guarantee.

<a id="symbol-bessplanningfeatureapplicationartifactrecord-row-count"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactRecord.row_count`

Source lines 145–145. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
row_count: StrictInt
```

Required StrictInt ≥0; physical reader compares len(frame). Unit rows, not bytes.

<a id="symbol-bessplanningfeatureapplicationartifactrecord-size-bytes"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactRecord.size_bytes`

Source lines 146–146. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
size_bytes: StrictInt
```

Required StrictInt ≥1; compared to length of captured raw bytes before parsing.

<a id="symbol-bessplanningfeatureapplicationartifactrecord-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactRecord.sha256`

Source lines 147–147. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
sha256: StrictStr
```

Required StrictStr lowercase64-hex SHA of captured raw Parquet bytes; independent of canonical frame/result digests.

<a id="symbol-bessplanningfeatureapplicationartifactrecord-frame-schema-signature"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactRecord.frame_schema_signature`

Source lines 148–148. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
frame_schema_signature: Mapping[StrictStr, object]
```

Required Mapping[str,object], canonical-JSON copied/frozen after parsing; complete measured signature must match at readback. Serializer returns fresh containers.

<a id="symbol-bessplanningfeatureapplicationartifactrecord-geospatial"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactRecord.geospatial`

Source lines 149–149. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
geospatial: StrictBool
```

Required StrictBool; True for first three roles, False for RELATIONS; dictates reader and CRS/type checks.

<a id="symbol-bessplanningfeatureapplicationartifactrecord-crs"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactRecord.crs`

Source lines 150–150. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
crs: Mapping[StrictStr, object] | None
```

Required nullable Mapping[str,object]; geospatial roles require nonnull canonical frozen CRS equal to schema CRS, relations require None in both places. Omission is not equivalent to explicit None.

<a id="symbol-bessplanningfeatureapplicationartifactrecord--serialize-immutable-json-mapping"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactRecord._serialize_immutable_json_mapping`

Source lines 153–156. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
    def _serialize_immutable_json_mapping(
        self, value: Mapping[str, object] | None
    ) -> object:
```

Pydantic serializer for both schema and CRS receives Mapping or None; return fresh plain canonical JSON containers through to_plain_json_value, never a mutable backing alias. No model mutation or I/O; canonical-leaf ValueError belongs to the common serializer.

Exact decorators/parametrization (not extra closure units):

```python
    @field_serializer("frame_schema_signature", "crs")
```

<a id="symbol-bessplanningfeatureapplicationartifactrecord--validate-record"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactRecord._validate_record`

Source lines 159–187. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
    def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:
```

After parsing, create local frozen schema and nullable CRS; validate portable filename, strict nonnegative row count, strict positive byte size, SHA, role/geospatial equality, CRS agreement and nonempty geometry_column for geospatial records. Only after these checks assign the frozen signature and assign CRS only when its frozen value is nonnull; return self. Explicit failures are builtin ValueError/Pydantic validation failures, not prewrapped application errors. No file read.

Exact decorators/parametrization (not extra closure units):

```python
    @model_validator(mode="after")
```

<a id="symbol-bessplanningfeatureapplicationresult"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult`

Source lines 191–225. Kind: class. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
class BessPlanningFeatureApplicationResult:
```

Frozen dataclass holding 28 required scalars and four required mutable frames. Builder creates copied frames; dataclass construction itself neither copies arbitrary caller frames nor validates them. Hashes and later envelope/full validators detect inconsistencies; no parcel frame or writer is present.

<a id="symbol-bessplanningfeatureapplicationresult-result-hash-schema-version"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.result_hash_schema_version`

Source lines 194–194. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
result_hash_schema_version: int
```

Application canonical-content hash schema2; exact int enforced by local envelope, strict int in manifest. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-application-scope"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.application_scope`

Source lines 195–195. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
application_scope: str
```

FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY; no parcel-status aggregation. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-policy-scope"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.policy_scope`

Source lines 196–196. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
policy_scope: str
```

OFFICIAL_CNIG_CODE_MEANING_ONLY; official code evidence is not a local legal decision. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-local-feature-text-interpreted"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.local_feature_text_interpreted`

Source lines 197–197. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
local_feature_text_interpreted: bool
```

False: raw feature text remains factual and is not interpreted. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-local-regulation-content-interpreted"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.local_regulation_content_interpreted`

Source lines 198–198. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
local_regulation_content_interpreted: bool
```

False: no local written regulation interpretation. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-legal-conclusion-produced"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.legal_conclusion_produced`

Source lines 199–199. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
legal_conclusion_produced: bool
```

False: no legal authorization/prohibition conclusion. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-parcel-status-aggregated"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.parcel_status_aggregated`

Source lines 200–200. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
parcel_status_aggregated: bool
```

False: application does not choose a parcel status; downstream aggregation is separate. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-parcel-rejection-performed"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.parcel_rejection_performed`

Source lines 201–201. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
parcel_rejection_performed: bool
```

False: no parcel is rejected by this stage. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-score-calculated"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.score_calculated`

Source lines 202–202. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
score_calculated: bool
```

False: policy priority is propagated evidence, not a score. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-policy-profile"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.policy_profile`

Source lines 203–203. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
policy_profile: str
```

Exact nonempty untrimmed compiled-policy profile string; propagated and checked against upstream. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-policy-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.policy_sha256`

Source lines 204–204. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
policy_sha256: str
```

Lowercase64-hex policy-config identity propagated from policy_result; not a raw Parquet digest. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-policy-result-hash-schema-version"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.policy_result_hash_schema_version`

Source lines 205–205. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
policy_result_hash_schema_version: int
```

Required upstream compiled-policy result version1; distinct from application schema2. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-policy-complete-result-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.policy_complete_result_content_sha256`

Source lines 206–206. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
policy_complete_result_content_sha256: str
```

Complete compiled-policy upstream digest, propagated into metadata and row suffix; NOT complete application digest. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-cnig-profile"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.cnig_profile`

Source lines 207–207. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_profile: str
```

Exact nonempty CNIG profile string propagated from coded_result.profile. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-cnig-profile-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.cnig_profile_sha256`

Source lines 208–208. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_profile_sha256: str
```

Lowercase64-hex CNIG profile content identity propagated from coded_result.profile_sha256. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-cnig-result-hash-schema-version"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.cnig_result_hash_schema_version`

Source lines 209–209. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_result_hash_schema_version: int
```

Required upstream coded-result version5, not its profile schema2. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-cnig-complete-result-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.cnig_complete_result_content_sha256`

Source lines 210–210. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_complete_result_content_sha256: str
```

Complete coded-result upstream digest; source lock, not application output digest. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-source-document-id"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.source_document_id`

Source lines 211–211. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
source_document_id: str
```

Exact nonempty source planning document identity; common rows must agree with it. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-source-archive-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.source_archive_sha256`

Source lines 212–212. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
source_archive_sha256: str
```

Propagated lowercase64-hex source archive identity; application does not independently hash/archive-download it. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-cnig-surface-features-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.cnig_surface_features_content_sha256`

Source lines 213–213. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_surface_features_content_sha256: str
```

Propagated coded surface prefix digest; checked against exact coded upstream by source locks, not recomputed from stripped application frames locally. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-cnig-line-features-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.cnig_line_features_content_sha256`

Source lines 214–214. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_line_features_content_sha256: str
```

Propagated coded line prefix digest with the same separate source-lock responsibility. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-cnig-point-features-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.cnig_point_features_content_sha256`

Source lines 215–215. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_point_features_content_sha256: str
```

Propagated coded point prefix digest, including zero-relation points through upstream content. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-cnig-relations-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.cnig_relations_content_sha256`

Source lines 216–216. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_relations_content_sha256: str
```

Propagated coded relation prefix digest; not the application relations digest below. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-surface-features-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.surface_features_content_sha256`

Source lines 217–217. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
surface_features_content_sha256: str
```

Recalculated application surface component digest over metadata and entire enriched surface frame. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-line-features-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.line_features_content_sha256`

Source lines 218–218. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
line_features_content_sha256: str
```

Recalculated application line component digest over metadata and entire enriched line frame. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-point-features-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.point_features_content_sha256`

Source lines 219–219. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
point_features_content_sha256: str
```

Recalculated application point component digest over metadata and entire enriched point frame. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-relations-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.relations_content_sha256`

Source lines 220–220. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
relations_content_sha256: str
```

Recalculated application relation component digest over metadata and entire enriched relation frame. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-complete-result-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.complete_result_content_sha256`

Source lines 221–221. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
complete_result_content_sha256: str
```

Recalculated application result digest over23 metadata fields and four application component hashes; not an upstream/Parquet digest. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-surface-features"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.surface_features`

Source lines 222–222. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
surface_features: gpd.GeoDataFrame
```

Required mutable GeoDataFrame: exact enriched surface catalog, including objects without relations; canonical EPSG:2154 2D Polygon/MultiPolygon, area m². Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-line-features"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.line_features`

Source lines 223–223. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
line_features: gpd.GeoDataFrame
```

Required mutable GeoDataFrame: exact enriched line catalog; canonical EPSG:2154 2D LineString/MultiLineString, length m. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-point-features"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.point_features`

Source lines 224–224. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
point_features: gpd.GeoDataFrame
```

Required mutable GeoDataFrame: exact enriched point catalog; canonical EPSG:2154 2D Point/MultiPoint, positive integral member count. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationresult-relations"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationResult.relations`

Source lines 225–225. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
relations: pd.DataFrame
```

Required mutable plain DataFrame: preserved coded relations plus18-column policy suffix; metric nulls/dtypes and pair identity remain intrinsic facts. Required field, no default; dataclass construction does not validate it. Result envelope/full-source validation supplies the guards; assigning attributes is frozen, frames themselves remain mutable.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest`

Source lines 241–321. Kind: class. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
class BessPlanningFeatureApplicationArtifactManifest(_StrictModel):
```

Frozen extra-forbidden Pydantic envelope with two manifest-only fields, the 28 result scalars, and required tuple of four ArtifactRecords. All fields required. Parsing/after-validation is local metadata validation; loader separately verifies upstream locks, captured files and complete reconstruction.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-schema-version"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.schema_version`

Source lines 244–244. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
schema_version: StrictInt
```

Manifest metadata schema2, not result schema1 from the downstream aggregator. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-artifact-kind"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.artifact_kind`

Source lines 245–245. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
artifact_kind: Literal["BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"]
```

Literal BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT; identifies this four-artifact family. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-result-hash-schema-version"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.result_hash_schema_version`

Source lines 246–246. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
result_hash_schema_version: StrictInt
```

Application canonical-content hash schema2; exact int enforced by local envelope, strict int in manifest. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-application-scope"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.application_scope`

Source lines 247–247. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
application_scope: Literal["FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY"]
```

FEATURE_AND_RELATION_POLICY_PROPAGATION_ONLY; no parcel-status aggregation. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-policy-scope"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.policy_scope`

Source lines 248–248. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
```

OFFICIAL_CNIG_CODE_MEANING_ONLY; official code evidence is not a local legal decision. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-local-feature-text-interpreted"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.local_feature_text_interpreted`

Source lines 249–249. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
local_feature_text_interpreted: StrictBool
```

False: raw feature text remains factual and is not interpreted. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-local-regulation-content-interpreted"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.local_regulation_content_interpreted`

Source lines 250–250. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
local_regulation_content_interpreted: StrictBool
```

False: no local written regulation interpretation. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-legal-conclusion-produced"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.legal_conclusion_produced`

Source lines 251–251. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
legal_conclusion_produced: StrictBool
```

False: no legal authorization/prohibition conclusion. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-parcel-status-aggregated"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.parcel_status_aggregated`

Source lines 252–252. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
parcel_status_aggregated: StrictBool
```

False: application does not choose a parcel status; downstream aggregation is separate. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-parcel-rejection-performed"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.parcel_rejection_performed`

Source lines 253–253. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
parcel_rejection_performed: StrictBool
```

False: no parcel is rejected by this stage. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-score-calculated"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.score_calculated`

Source lines 254–254. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
score_calculated: StrictBool
```

False: policy priority is propagated evidence, not a score. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-policy-profile"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.policy_profile`

Source lines 255–255. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
policy_profile: StrictStr
```

Exact nonempty untrimmed compiled-policy profile string; propagated and checked against upstream. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-policy-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.policy_sha256`

Source lines 256–256. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
policy_sha256: StrictStr
```

Lowercase64-hex policy-config identity propagated from policy_result; not a raw Parquet digest. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-policy-result-hash-schema-version"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.policy_result_hash_schema_version`

Source lines 257–257. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
policy_result_hash_schema_version: StrictInt
```

Required upstream compiled-policy result version1; distinct from application schema2. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-policy-complete-result-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.policy_complete_result_content_sha256`

Source lines 258–258. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
policy_complete_result_content_sha256: StrictStr
```

Complete compiled-policy upstream digest, propagated into metadata and row suffix; NOT complete application digest. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-cnig-profile"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.cnig_profile`

Source lines 259–259. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_profile: StrictStr
```

Exact nonempty CNIG profile string propagated from coded_result.profile. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-cnig-profile-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.cnig_profile_sha256`

Source lines 260–260. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_profile_sha256: StrictStr
```

Lowercase64-hex CNIG profile content identity propagated from coded_result.profile_sha256. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-cnig-result-hash-schema-version"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.cnig_result_hash_schema_version`

Source lines 261–261. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_result_hash_schema_version: StrictInt
```

Required upstream coded-result version5, not its profile schema2. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-cnig-complete-result-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.cnig_complete_result_content_sha256`

Source lines 262–262. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_complete_result_content_sha256: StrictStr
```

Complete coded-result upstream digest; source lock, not application output digest. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-source-document-id"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.source_document_id`

Source lines 263–263. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
source_document_id: StrictStr
```

Exact nonempty source planning document identity; common rows must agree with it. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-source-archive-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.source_archive_sha256`

Source lines 264–264. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
source_archive_sha256: StrictStr
```

Propagated lowercase64-hex source archive identity; application does not independently hash/archive-download it. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-cnig-surface-features-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.cnig_surface_features_content_sha256`

Source lines 265–265. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_surface_features_content_sha256: StrictStr
```

Propagated coded surface prefix digest; checked against exact coded upstream by source locks, not recomputed from stripped application frames locally. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-cnig-line-features-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.cnig_line_features_content_sha256`

Source lines 266–266. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_line_features_content_sha256: StrictStr
```

Propagated coded line prefix digest with the same separate source-lock responsibility. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-cnig-point-features-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.cnig_point_features_content_sha256`

Source lines 267–267. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_point_features_content_sha256: StrictStr
```

Propagated coded point prefix digest, including zero-relation points through upstream content. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-cnig-relations-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.cnig_relations_content_sha256`

Source lines 268–268. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
cnig_relations_content_sha256: StrictStr
```

Propagated coded relation prefix digest; not the application relations digest below. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-surface-features-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.surface_features_content_sha256`

Source lines 269–269. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
surface_features_content_sha256: StrictStr
```

Recalculated application surface component digest over metadata and entire enriched surface frame. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-line-features-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.line_features_content_sha256`

Source lines 270–270. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
line_features_content_sha256: StrictStr
```

Recalculated application line component digest over metadata and entire enriched line frame. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-point-features-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.point_features_content_sha256`

Source lines 271–271. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
point_features_content_sha256: StrictStr
```

Recalculated application point component digest over metadata and entire enriched point frame. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-relations-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.relations_content_sha256`

Source lines 272–272. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
relations_content_sha256: StrictStr
```

Recalculated application relation component digest over metadata and entire enriched relation frame. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-complete-result-content-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.complete_result_content_sha256`

Source lines 273–273. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
complete_result_content_sha256: StrictStr
```

Recalculated application result digest over23 metadata fields and four application component hashes; not an upstream/Parquet digest. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest-artifacts"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest.artifacts`

Source lines 274–274. Kind: field. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
artifacts: tuple[BessPlanningFeatureApplicationArtifactRecord, ...]
```

Required tuple of validated records, exactly SURFACE_FEATURES/LINE_FEATURES/POINT_FEATURES/RELATIONS in order, casefold-unique filenames. It is metadata, not a collection of loaded frames. Required field, no default; Pydantic annotation below controls strict scalar/Literal/tuple parsing, then _validate_manifest enforces this envelope contract. File/upstream truth is verified later by loader; metadata is frozen.

<a id="symbol-bessplanningfeatureapplicationartifactmanifest--validate-manifest"></a>
### `landscout.stages.apply_bess_planning_feature_policy.BessPlanningFeatureApplicationArtifactManifest._validate_manifest`

Source lines 277–321. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
    def _validate_manifest(self) -> BessPlanningFeatureApplicationArtifactManifest:
```

After Pydantic strict/Literal parsing require manifest/result versions2, six flags literally False, exact profile/document strings, policy result1 and CNIG result5, SHA syntax for all digest fields, exactly the ordered four roles and casefold-unique filenames. Return self; explicit errors builtin ValueError. Does not hash or read files; nested record validation already performed its freeze/guards.

Exact decorators/parametrization (not extra closure units):

```python
    @model_validator(mode="after")
```

<a id="symbol--null-value"></a>
### `landscout.stages.apply_bess_planning_feature_policy._null_value`

Source lines 324–333. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _null_value(value: object) -> object:
```

Normalize None/pd.NA and a scalar pd.isna result that is bool/np.bool_ and true to None; catch TypeError/ValueError from isna and preserve the original value. Used by canonicalization/equality. Arrays are not collapsed into missing scalars; no mutation/I/O.

<a id="symbol--canonical-value"></a>
### `landscout.stages.apply_bess_planning_feature_policy._canonical_value`

Source lines 336–375. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _canonical_value(value: object) -> object:
```

Return canonical JSON scalar/geometry data following the ordered null, BaseGeometry, date/time, NumPy scalar, bool, Integral, finite Real, str branches. Exactly2D geometry only; dimension guard and unsupported/nonfinite values raise application errors. Recurses for numpy.item(); allocates geometry dicts, never repairs geometry or reads paths. Payload builder calls it on index and cells.

<a id="symbol--frame-payload"></a>
### `landscout.stages.apply_bess_planning_feature_policy._frame_payload`

Source lines 378–386. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
```

Return dict with complete deterministic_frame_schema_signature, ordered canonical index values and ordered canonical rows from itertuples(index=False,name=None). Includes all columns/geometry, not DataFrame attrs. Read-only memory operation used by hashes and exact comparisons; schema/canonicalization exceptions propagate to caller boundaries.

<a id="symbol--validate-application-geometry"></a>
### `landscout.stages.apply_bess_planning_feature_policy._validate_application_geometry`

Source lines 389–412. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _validate_application_geometry(frame: gpd.GeoDataFrame, label: str) -> None:
```

For one GeoDataFrame and diagnostic label, require an accessible active column and BaseGeometry values of exactly two dimensions; return None. Preserve owned errors and translate other Exceptions. This helper alone does not test valid/nonempty/role types/metric CRS; the common catalog owner does. Called after copied catalog construction; no repair or I/O.

<a id="symbol--canonical-json-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy._canonical_json_sha256`

Source lines 415–428. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _canonical_json_sha256(value: object) -> str:
```

Serialize supplied JSON-compatible value with UTF-8, sorted object keys and compact finite JSON; return lowercase SHA256. TypeError/ValueError becomes application error with cause. Lists remain ordered. Used by component and complete hashes, not raw-file SHA checks; no I/O.

<a id="symbol--null-safe-equal"></a>
### `landscout.stages.apply_bess_planning_feature_policy._null_safe_equal`

Source lines 431–439. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _null_safe_equal(left: object, right: object) -> bool:
```

Normalize both operands; null equals only null, otherwise attempt bool(left == right), returning False on TypeError/ValueError. Used for row/text/point agreement; does not perform geospatial comparison or coercive text normalization.

<a id="symbol--policy-lookup"></a>
### `landscout.stages.apply_bess_planning_feature_policy._policy_lookup`

Source lines 442–457. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _policy_lookup(
    policy: BessPlanningFeaturePolicyResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

Read policy_table records into a new dict keyed by str family/type/subtype; duplicate triples raise application error. Private caller assumes validated policy envelope and does not fully validate it here. Used for each catalog propagation; no input mutation or file I/O.

<a id="symbol--policy-values"></a>
### `landscout.stages.apply_bess_planning_feature_policy._policy_values`

Source lines 460–486. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _policy_values(
    row: dict[str, object] | None,
    application_status: ApplicationStatus,
    policy: BessPlanningFeaturePolicyResult,
) -> dict[str, object]:
```

Create one 18-key suffix dict from policy lineage and optional entry: exact match copies six decisions; absent entry gives UNRESOLVED_CODE_PAIR and six None values. All flags False, scopes/profile/config/result hash propagated. Pure helper for catalogs; it does not infer a decision from feature text.

<a id="symbol--assign-policy-columns"></a>
### `landscout.stages.apply_bess_planning_feature_policy._assign_policy_columns`

Source lines 489–503. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _assign_policy_columns(
    frame: pd.DataFrame,
    rows: list[dict[str, object]],
) -> pd.DataFrame:
```

Append/assign all POLICY_COLUMNS to the supplied frame IN PLACE in declared order from row dictionaries: eleven str arrays, Int64 priority, six bool arrays. Return that same frame. Catalog/relation callers pass deep copies. No validation wrapper or filesystem I/O; pandas construction errors propagate.

<a id="symbol--apply-feature-catalog"></a>
### `landscout.stages.apply_bess_planning_feature_policy._apply_feature_catalog`

Source lines 506–571. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _apply_feature_catalog(
    catalog: gpd.GeoDataFrame,
    policy: BessPlanningFeaturePolicyResult,
) -> gpd.GeoDataFrame:
```

Require GeoDataFrame, no suffix collisions and five code/identity columns; create duplicate-checked policy lookup; check exact two-digit code strings per row. RESOLVED_OFFICIAL requires an entry, UNKNOWN_CODE_PAIR forbids one, other statuses fail. Copy deeply, assign suffix, reconstruct GeoDataFrame with original active geometry/CRS and call 2D helper. Return new catalog without filtering. Private subset guard is not the full common intrinsic/source validation.

<a id="symbol--feature-rows-by-id"></a>
### `landscout.stages.apply_bess_planning_feature_policy._feature_rows_by_id`

Source lines 574–590. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _feature_rows_by_id(
    *catalogs: gpd.GeoDataFrame,
) -> dict[str, dict[str, object]]:
```

Build a fresh global ID→row dict across supplied catalogs; IDs must be nonempty str and unique across all frames, otherwise application error. Used by relation propagation and result envelope. This helper alone does not validate exact stripping/GPU grammar, which belongs to common guards. No input mutation/I/O.

<a id="symbol--apply-relations"></a>
### `landscout.stages.apply_bess_planning_feature_policy._apply_relations`

Source lines 593–630. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _apply_relations(
    relations: pd.DataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
) -> pd.DataFrame:
```

Require plain DataFrame, no suffix collisions and IDs plus all22 agreement columns. Build catalog ID lookup; every relation must resolve to a feature, and those factual/official columns must agree null-safely. Copy that feature's full18-column policy suffix into a deep relation copy; return plain DataFrame. No second policy lookup, grouping, parcel aggregation or file read. Full metric/domain checks belong to envelope validation.

<a id="symbol--component-metadata"></a>
### `landscout.stages.apply_bess_planning_feature_policy._component_metadata`

Source lines 633–670. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _component_metadata(
    result: BessPlanningFeatureApplicationResult,
) -> dict[str, object]:
```

Return new dict of exactly23 scalar provenance/scope/version/flag fields, including four propagated coded-prefix digests but excluding five output digests. Called by both hash paths. No frame copy, validation or I/O; values are taken from the supplied result.

<a id="symbol--component-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy._component_sha256`

Source lines 673–684. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _component_sha256(
    result: BessPlanningFeatureApplicationResult,
    frame: pd.DataFrame,
    role: str,
) -> str:
```

Given result, full frame and role string, hash domain prefix+role, all23 metadata keys and frame payload; return digest. Caller passes four exact role suffixes. Pure hashing, no file bytes or upstream physical validation.

<a id="symbol--complete-result-sha256"></a>
### `landscout.stages.apply_bess_planning_feature_policy._complete_result_sha256`

Source lines 687–697. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _complete_result_sha256(result: BessPlanningFeatureApplicationResult) -> str:
```

Hash literal result domain, all23 metadata keys and four application frame digest fields; return complete application digest. Does not reread frames independently or use aggregation formulas; called after component resealing.

<a id="symbol--result-with-hashes"></a>
### `landscout.stages.apply_bess_planning_feature_policy._result_with_hashes`

Source lines 700–721. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _result_with_hashes(
    result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureApplicationResult:
```

Return dataclass replacements with four recalculated frame digests then complete digest. Frames remain the same object references. Used by build/envelope/tests, not a validation substitute; propagated upstream digests are not recomputed here and no physical source I/O occurs.

<a id="symbol--build-result"></a>
### `landscout.stages.apply_bess_planning_feature_policy._build_result`

Source lines 724–766. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _build_result(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeatureApplicationResult:
```

Propagate policy to surface/line/point catalogs then existing coded relations; construct result with fixed schemas/scopes/six False flags, copied upstream lineage, empty output hash placeholders; reseal and return. Its own body does not call application envelope or heavy validation. Public builder/full validator/light loader supply distinct surrounding guards. No parcels or file reads here; copied outputs retain full prefixes.

<a id="symbol--validate-relation-rows"></a>
### `landscout.stages.apply_bess_planning_feature_policy._validate_relation_rows`

Source lines 769–787. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _validate_relation_rows(
    frame: pd.DataFrame,
    label: str,
    result: BessPlanningFeatureApplicationResult,
) -> tuple[dict[int, str], dict[str, int]]:
```

Delegate the complete common relation-frame contract with result lineage; return (priority→status, status→priority) mappings. TypeError/ValueError becomes application error. No aggregation or file I/O; common owner checks schema, official/policy rows, exact IDs, unique pair and intrinsic metrics.

<a id="symbol--validate-result-envelope"></a>
### `landscout.stages.apply_bess_planning_feature_policy._validate_result_envelope`

Source lines 790–940. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _validate_result_envelope(result: BessPlanningFeatureApplicationResult) -> None:
```

Read-only local guard: result isinstance, exact int schema2, scopes, profile/document strings, policy1/CNIG5 equality checks, six False flags; catalog types/duplicate columns/signatures; common full catalog validation; plain relation type/schema/common validation; relation mappings included consistently in global feature mappings; all relation IDs and22+18 column agreements; source metric equality; digest syntax; recompute/compare five output hashes. TypeError/ValueError from common catalogs is wrapped, but there is no universal wrapper (e.g. preliminary signature errors may escape here). All unreferenced features are checked. Does not compare actual upstream objects or reread GPU files. Unlike own schema2, policy/CNIG version checks here are equality checks, not independent exact-int tests on dataclass fields.

<a id="symbol-validate-bess-planning-feature-application-result-envelope"></a>
### `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result_envelope`

Source lines 943–948. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def validate_bess_planning_feature_application_result_envelope(
    result: BessPlanningFeatureApplicationResult,
) -> None:
```

One required result, return None; directly invoke private envelope guard, without a try/except wrapper, upstream objects or I/O. Caller aggregation may use this lightweight API. Internal self-consistency is not source authority; direct third-party errors outside private guarded blocks are not universally translated here.

<a id="symbol--validate-coded-policy-compatibility"></a>
### `landscout.stages.apply_bess_planning_feature_policy._validate_coded_policy_compatibility`

Source lines 951–1016. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _validate_coded_policy_compatibility(
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
```

For two already envelope-validated upstreams, compare seven identities, require nonempty exact equality of policy/dictionary family/type/subtype key sets, then official label/legal/regulation text equality per pair. Return None or application error. Does not compare source_url in this helper, reload configs or GPU; invoked before manifest I/O by loader.

<a id="symbol--validate-source-locks"></a>
### `landscout.stages.apply_bess_planning_feature_policy._validate_source_locks`

Source lines 1019–1112. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _validate_source_locks(
    result: BessPlanningFeatureApplicationResult
    | BessPlanningFeatureApplicationArtifactManifest,
    coded: PlanningFeatureCodeResult,
    policy: BessPlanningFeaturePolicyResult,
) -> None:
```

Compare fourteen application-to-upstream scalar locks (policy profile/config/schema/result; CNIG profile/config/schema/result; document/archive; four coded frame digests), then seven policy-to-CNIG source identities including profile schema. Return None or application source-lock error. Used by full validator and loader; no content reconstruction or I/O.

<a id="symbol--validate-policy-source"></a>
### `landscout.stages.apply_bess_planning_feature_policy._validate_policy_source`

Source lines 1115–1143. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

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

Forward ten source/policy inputs to the compiled-policy owner's full result validator once, return None. Any delegated Exception is chained into application source-complete validation error. This is the heavy boundary, potentially reading supplied config/profile paths and physical synthetic/real GPU layers; the caller determines which source is supplied. No download is initiated by this adapter.

<a id="symbol-apply-bess-planning-feature-policy"></a>
### `landscout.stages.apply_bess_planning_feature_policy.apply_bess_planning_feature_policy`

Source lines 1146–1181. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

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

Public ten-input builder: validate complete upstream policy/source once, build once, validate local envelope, return application result. Preserve application errors; wrap other Exceptions with cause. Output copies and no local text interpretation/parcel aggregation; delegated validation can rebuild physical sources/relations. Package and tests call it; not an artifact writer.

<a id="symbol--compare-frame"></a>
### `landscout.stages.apply_bess_planning_feature_policy._compare_frame`

Source lines 1184–1188. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
```

Compare complete _frame_payload(actual) and expected, returning None or application error with label. Exact order/index/dtype/geometry/CRS and every cell matter, not only policy columns. Called by full validator and loader; no mutation/I/O.

<a id="symbol-validate-bess-planning-feature-application-result"></a>
### `landscout.stages.apply_bess_planning_feature_policy.validate_bess_planning_feature_application_result`

Source lines 1191–1239. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

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

Public eleven-input validator returning None: local envelope → upstream scalar locks → heavy policy owner once → one rebuilt result → all28 scalars then4 complete frames. Preserve owned errors, wrap other Exceptions with cause. Supplied result frames are not repaired or mutated; delegated upstream source I/O differs from the local preliminary checks.

<a id="symbol--read-verified-artifact"></a>
### `landscout.stages.apply_bess_planning_feature_policy._read_verified_artifact`

Source lines 1242–1290. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

```python
def _read_verified_artifact(
    path: Path,
    record: BessPlanningFeatureApplicationArtifactRecord,
) -> pd.DataFrame:
```

Given Path and validated record, compare basename then capture bytes once, size/SHA, parse BytesIO with geo/nongeo reader, row count, complete frozen schema, and geo CRS/type. Return DataFrame (GeoDataFrame for geospatial role). Explicit mismatches use application errors; read/parser/CRS failures have no broad private wrapper and are translated by public loader. Does not reread path after capture, constrain roots, reject symlinks or write files.

<a id="symbol-load-bess-planning-feature-application-artifacts"></a>
### `landscout.stages.apply_bess_planning_feature_policy.load_bess_planning_feature_application_artifacts`

Source lines 1293–1350. Kind: function. Owner: `landscout.stages.apply_bess_planning_feature_policy`.

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

Public seven required inputs: manifest/surface/line/point/relation paths (each str or Path) and exact coded_result/policy_result. Validate both upstream envelopes and compatibility before manifest read; strict JSON+Pydantic; locks; capture four files in role order; construct and validate result; build once from supplied upstreams; compare28 scalars and4 frames; return. Owned errors pass through, all other Exceptions chained into application artifact error. No heavy GPU/source validation, writer, omitted-upstream fallback or parcel aggregation.

## Complete source snapshot

One exact full source snapshot follows. Byte equality does not substitute for the semantic explanations above.

```python
"""Apply a validated BESS CNIG policy exactly to coded features and relations."""

from __future__ import annotations

import json
import math
import re
from collections.abc import Mapping
from dataclasses import dataclass, replace
from datetime import date, datetime
from hashlib import sha256
from io import BytesIO
from numbers import Integral, Real
from pathlib import Path
from typing import Literal

import geopandas as gpd  # type: ignore[import-untyped]
import numpy as np
import pandas as pd  # type: ignore[import-untyped]
from pydantic import (
    BaseModel,
    ConfigDict,
    StrictBool,
    StrictInt,
    StrictStr,
    field_serializer,
    model_validator,
)
from pyproj import CRS
from shapely import get_coordinate_dimension, to_wkb  # type: ignore[import-untyped]
from shapely.geometry.base import BaseGeometry  # type: ignore[import-untyped]

from landscout.common.artifact_paths import validate_portable_parquet_filename
from landscout.common.bess_application_contract import (
    APPLICATION_SCOPE,
    FLAG_COLUMNS,
    POLICY_COLUMNS,
    POLICY_SCOPE,
    STRING_POLICY_COLUMNS,
    ApplicationStatus,
    validate_bess_application_feature_catalogs,
    validate_bess_application_relation_frame,
)
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.immutable_mapping import (
    freeze_json_mapping,
    to_plain_json_value,
)
from landscout.common.planning_overlay import technical_overlay_tolerance
from landscout.common.strict_json import loads_strict_json_object
from landscout.sources.gpu_fr import GpuPlanningDocument
from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)
from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result_envelope,
)

__all__ = [
    "BessPlanningFeatureApplicationArtifactManifest",
    "BessPlanningFeatureApplicationError",
    "BessPlanningFeatureApplicationResult",
    "apply_bess_planning_feature_policy",
    "load_bess_planning_feature_application_artifacts",
    "validate_bess_planning_feature_application_result",
    "validate_bess_planning_feature_application_result_envelope",
]

RESULT_HASH_SCHEMA_VERSION = 2
ARTIFACT_MANIFEST_SCHEMA_VERSION = 2
ARTIFACT_KIND = "BESS_PLANNING_FEATURE_POLICY_APPLICATION_RESULT"

ArtifactRole = Literal[
    "SURFACE_FEATURES",
    "LINE_FEATURES",
    "POINT_FEATURES",
    "RELATIONS",
]

ARTIFACT_ROLES: tuple[ArtifactRole, ...] = (
    "SURFACE_FEATURES",
    "LINE_FEATURES",
    "POINT_FEATURES",
    "RELATIONS",
)
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
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
CODE_PATTERN = re.compile(r"[0-9]{2}")


class BessPlanningFeatureApplicationError(ValueError):
    """Raised when exact feature-policy propagation cannot be proven."""


class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be an exact non-empty string")
    return value


def _sha256_string(value: object, label: str) -> str:
    text = _exact_string(value, label)
    if SHA_PATTERN.fullmatch(text) is None:
        raise ValueError(f"{label} must be a lowercase SHA256")
    return text


class BessPlanningFeatureApplicationArtifactRecord(_StrictModel):
    """One physical output record within the application manifest."""

    artifact_role: ArtifactRole
    filename: StrictStr
    row_count: StrictInt
    size_bytes: StrictInt
    sha256: StrictStr
    frame_schema_signature: Mapping[StrictStr, object]
    geospatial: StrictBool
    crs: Mapping[StrictStr, object] | None

    @field_serializer("frame_schema_signature", "crs")
    def _serialize_immutable_json_mapping(
        self, value: Mapping[str, object] | None
    ) -> object:
        return to_plain_json_value(value)

    @model_validator(mode="after")
    def _validate_record(self) -> BessPlanningFeatureApplicationArtifactRecord:
        frozen_signature = freeze_json_mapping(self.frame_schema_signature)
        frozen_crs = freeze_json_mapping(self.crs) if self.crs is not None else None
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be a non-negative integer")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be a positive integer")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geospatial = self.artifact_role != "RELATIONS"
        if self.geospatial is not expected_geospatial:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = frozen_signature.get("crs")
        signature_geometry = frozen_signature.get("geometry_column")
        if expected_geospatial:
            if frozen_crs is None or signature_crs != frozen_crs:
                raise ValueError("geospatial artifact CRS is missing or inconsistent")
            if not isinstance(signature_geometry, str) or not signature_geometry:
                raise ValueError("geospatial artifact geometry column is missing")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("non-geospatial artifact must not declare a CRS")
        object.__setattr__(
            self,
            "frame_schema_signature",
            frozen_signature,
        )
        if frozen_crs is not None:
            object.__setattr__(self, "crs", frozen_crs)
        return self


@dataclass(frozen=True)
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


RESULT_FRAME_FIELDS = (
    "surface_features",
    "line_features",
    "point_features",
    "relations",
)
RESULT_SCALAR_FIELDS = tuple(
    field
    for field in BessPlanningFeatureApplicationResult.__dataclass_fields__
    if field not in RESULT_FRAME_FIELDS
)


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


def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
    return {
        "schema": deterministic_frame_schema_signature(frame),
        "index": [_canonical_value(value) for value in frame.index.tolist()],
        "rows": [
            [_canonical_value(value) for value in row]
            for row in frame.itertuples(index=False, name=None)
        ],
    }


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


def _null_safe_equal(left: object, right: object) -> bool:
    left = _null_value(left)
    right = _null_value(right)
    if left is None or right is None:
        return left is None and right is None
    try:
        return bool(left == right)
    except (TypeError, ValueError):
        return False


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


def validate_bess_planning_feature_application_result_envelope(
    result: BessPlanningFeatureApplicationResult,
) -> None:
    """Validate one application envelope without reconstructing source inputs."""

    _validate_result_envelope(result)


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


def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _frame_payload(actual) != _frame_payload(expected):
        raise BessPlanningFeatureApplicationError(
            f"Application {label} differs from rebuilt result"
        )


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
    if freeze_json_mapping(signature) != record.frame_schema_signature:
        raise BessPlanningFeatureApplicationError(
            f"Artifact {record.artifact_role} frame schema differs"
        )
    if record.geospatial:
        if not isinstance(frame, gpd.GeoDataFrame) or frame.crs is None:
            raise BessPlanningFeatureApplicationError(
                f"Artifact {record.artifact_role} geospatial contract differs"
            )
        if (
            freeze_json_mapping(CRS.from_user_input(frame.crs).to_json_dict())
            != record.crs
        ):
            raise BessPlanningFeatureApplicationError(
                f"Artifact {record.artifact_role} CRS differs"
            )
    elif isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureApplicationError(
            "Relations artifact unexpectedly loaded as geospatial"
        )
    return frame


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
        payload = loads_strict_json_object(Path(manifest_path).read_bytes())
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
