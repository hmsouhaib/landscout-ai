# `src/landscout/stages/bess_planning_feature_policy.py`

- Source: [src/landscout/stages/bess_planning_feature_policy.py](../../../../../../src/landscout/stages/bess_planning_feature_policy.py)
- Source SHA256: `9568f12e7f70c8e7d06b105020d486e285d0a2eef2a0eee5a266d5c1a7d545dd`
- Source SHA256 basis: `git-content`
- Source lines: 1114; Git blob at R10 start: `e9b3f5dd3664b7e710ad47fbc07691e3d5829bd2`

Git/index/checkout source bytes are unchanged. Local semantic closure is not independent approval. [R10 receipt](../../../../../../docs/code/audit/R10_BESS_CNIG_COMPILER.md).

## Scope and owners

This compiler joins a validated, source-locked policy declaration to the exact official CNIG dictionary by `(feature_family, type_code, subtype_code)`. Official labels/references come from the dictionary; expected texts in the configuration must agree with them. Decisions, confidence, rationale, human action and limitations come from the policy. It produces one non-geospatial policy table, not statuses on features, relations or parcels. Application and aggregation are separate stages. No local feature/regulation interpretation, legal authorization, scoring, ranking or automatic BESS/ICPE inference is added.

The nine exports, also imported and listed by `landscout.stages`, are `BessPlanningFeaturePolicyArtifactManifest`, `BessPlanningFeaturePolicyConfig`, `BessPlanningFeaturePolicyError`, `BessPlanningFeaturePolicyResult`, `compile_bess_planning_feature_policy`, `load_bess_planning_feature_policy_artifacts`, `load_bess_planning_feature_policy_config`, `validate_bess_planning_feature_policy_result` and `validate_bess_planning_feature_policy_result_envelope`. Other models/helpers are directly importable but not promised by this export list. There is no public writer.

Repository dependencies: [strict YAML](../common/strict_yaml.py.md), [strict JSON](../common/strict_json.py.md), [immutable mapping](../common/immutable_mapping.py.md), [portable artifact names](../common/artifact_paths.py.md), [frame signatures](../common/frame_integrity.py.md), [GPU document](../sources/gpu_fr.py.md), [CNIG owner](resolve_planning_feature_codes.py.md). [Application](apply_bess_planning_feature_policy.py.md) delegates its full policy check here; its lightweight compatibility check separately compares upstream identities, nonempty pair sets and official meanings. [Aggregation](aggregate_bess_planning_feature_policy.py.md) is downstream, not this compiler. R5 YAML, R8/R8.1 aggregation and R9/R9.1 application documentary approvals are reused within their limits, not reopened. [Tests](../../../tests/unit/test_bess_planning_feature_policy.py.md) include synthetic physical inputs and a distinct private checked-in-policy helper.

Standard library imports own JSON, regular expressions, SHA256, numeric/date handling, dataclass replacement, Mapping, Literal, Path and BytesIO. Pandas owns tables/Parquet, NumPy scalar detection, GeoPandas the rejected geospatial table subtype and source annotations, Pydantic the models, strict scalar fields, after-validators and priority field serializer. None of these imports is a source authority by itself.

## Public paths and validation order

| Boundary | Required positional-or-keyword inputs | Order and return |
| --- | --- | --- |
| Config loader | One str-or-Path location | Read bytes, strict YAML object, validate model; return config. |
| Compiler | planning_document, parcels, surface_features, line_features, point_features, relations, code_profile, coded_result, policy_config | Resolve/revalidate config; seven lock comparisons; full CNIG validator; build table and hashes; local envelope; return result. |
| Full validator | The same nine, then result | Local envelope first; resolve config; locks; full CNIG validator; rebuild; compare 14 scalars then exact frame payload; return None. |
| Public envelope | result | Intrinsic schema/rows/hashes only; return None. It has a broad Exception wrapper. |
| Artifact loader | parquet_path, manifest_path (both str or Path) | Strict JSON/model; basename; capture Parquet bytes; size/SHA; BytesIO parse; row count/schema; reconstruct; local envelope; return result. No upstream objects required. |

All signatures below are literal: no inferred optional defaults. Passing an existing config still invokes model_dump and model_validate. The lock comparator uses equality, not an independent exact-type proof of coded_result. The CNIG owner validates its result, reconstructs normalized factual inputs and compares source-bound output; one owner invocation is not one file read. Source-bound paths can therefore reread synthetic or real source files supplied by their caller; the compiler's table builder does not itself perform geometry calculations.

The artifact loader validates locally captured bytes but not current source completeness. It does not take the application's seven arguments, regenerate a dictionary, write files, promise an atomic multi-file snapshot, enforce directory containment, reject symlinks, or recheck the Parquet path after capture. Errors explicitly raised as BessPlanningFeaturePolicyError pass through; its broad wrapper chains other exceptions. The local public envelope also wraps unexpected Exception, unlike the application envelope described in R9.

## Schema, ordering and mutability

Configuration/policy schema is 1, result hash schema 1, artifact manifest schema 2; CNIG profile/result versions at the result/manifest boundary are 2 and 5. Scope is OFFICIAL_CNIG_CODE_MEANING_ONLY. The five statuses and three confidence literals are enumerated below; they are precheck evidence, not permissions. Config requires all five unique positive priorities. Local table rows need only a one-to-one status/priority mapping among statuses present, not all five statuses.

There are 21 ordered columns: priority uses non-nullable int64, three interpretation/legal flags use bool and must be False, the other 17 use Pandas str. This is not the nullable Int64 suffix of application. Two official-reference columns may contain true missing values. Family and two-character ASCII digit codes preserve leading zeroes and separate code spaces. Config entries must already be sorted by the exact triple; duplicates and out-of-order input are rejected rather than sorted into acceptance. Table construction preserves that order; the local envelope enforces triple order again. The builder uses a plain Pandas Index with int64 values and no name. The local schema guard commits the index class/dtype/name but does not require contiguous or unique index values; hash payloads retain actual values and order.

Pydantic models forbid extra fields and freeze attributes; this is not a global strict=True setting. StrictStr/StrictInt/StrictBool and Literal annotations provide field-specific validation. YAML sequences become tuples. Priorities use Mapping, then freeze_mapping copies them into backing-alias-free FrozenDict after validation. Its serializer returns a fresh dict for canonical model serialization, not a mutable alias. This is not freeze_json_value: validated priority leaves are integers and keys are status strings. Schema-signature sequences are tuples. The result is a frozen dataclass with 14 required scalars and a mutable DataFrame. Its annotations and constructor do not validate values or freeze the table; result validators own those checks.

## Content commitments and null boundaries

Canonical JSON uses UTF-8, ensure_ascii=False, allow_nan=False, sort_keys=True and compact separators. Object keys are sorted; arrays, tuple-derived arrays, rows, columns and index values retain order. No repr/class-memory identity enters value hashes. Frame schema explicitly includes the index class name as a declared schema field, not repr of an object.

| Digest | Exact commitment |
| --- | --- |
| canonical_policy_entries_sha256 | Ordered list of entry.model_dump(mode="json") values, canonical JSON; no domain prefix. Not raw YAML bytes. |
| policy_sha256 | Entire validated config.model_dump(mode="json"), including source_lock, priorities, ordered entries and their declared digest; no separate domain. |
| policy_table_content_sha256 | Table domain, 12 scalar metadata fields (the result fields except table and the two computed hashes), plus frame schema/index/row values. |
| complete_result_content_sha256 | Result domain, same 12 metadata fields and the table content digest, not raw table bytes. |
| parquet_sha256 | SHA256 of the captured physical Parquet bytes, before decoding those same bytes. |

Literal domain strings (data, not Python owners):

```text
landscout.bess_cnig_feature_policy.table
landscout.bess_cnig_feature_policy.result
```

The table payload contains deterministic_frame_schema_signature, each canonicalized index value, and canonicalized rows in order. Scalar conversion handles true nulls first, then ISO dates/timestamps, NumPy scalar item conversion, bool before Integral, integer, finite Real and str. NaN recognized as missing becomes null before the finite-number branch; infinities fail. Unsupported scalar values fail, not stringify. Source archive/profile/coded-result digests are propagated after source validation, not recomputed by these two result hash helpers.

_exact_string requires a nonempty str already stripped, without Unicode normalization or textual-null exclusion. Optional expected references accept None, otherwise the same exact-string guard. Thus literal "None", "nan" or "<NA>" can satisfy that model-level string guard, while intrinsic compiled-reference validation explicitly rejects those literals. This is source-body deduction, not a new runtime reproduction; it parallels existing OPEN A-004 in the CNIG model/result boundary. Full compilation additionally compares against the validated CNIG dictionary. Current checked-in YAML uses true nulls; no affected official row, new A-005 or correction is claimed.

## Module declarations

Literal source declarations below add no symbol closure credit.

<a id="declaration---all--"></a>
### `landscout.stages.bess_planning_feature_policy.__all__`

Source lines 42–52. Exact nine-name module API; package reexports were compared, not inferred from importability.

```python
__all__ = [
    "BessPlanningFeaturePolicyArtifactManifest",
    "BessPlanningFeaturePolicyConfig",
    "BessPlanningFeaturePolicyError",
    "BessPlanningFeaturePolicyResult",
    "compile_bess_planning_feature_policy",
    "load_bess_planning_feature_policy_artifacts",
    "load_bess_planning_feature_policy_config",
    "validate_bess_planning_feature_policy_result",
    "validate_bess_planning_feature_policy_result_envelope",
]
```

<a id="declaration-policy-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.POLICY_SCHEMA_VERSION`

Source lines 54–54. Config and result policy version 1.

```python
POLICY_SCHEMA_VERSION = 1
```

<a id="declaration-result-hash-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.RESULT_HASH_SCHEMA_VERSION`

Source lines 55–55. Canonical policy result hash version 1.

```python
RESULT_HASH_SCHEMA_VERSION = 1
```

<a id="declaration-artifact-manifest-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.ARTIFACT_MANIFEST_SCHEMA_VERSION`

Source lines 56–56. Persisted physical manifest version 2.

```python
ARTIFACT_MANIFEST_SCHEMA_VERSION = 2
```

<a id="declaration-policy-scope"></a>
### `landscout.stages.bess_planning_feature_policy.POLICY_SCOPE`

Source lines 57–57. Official CNIG meaning only, not local text/legal interpretation.

```python
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"
```

<a id="declaration-artifact-kind"></a>
### `landscout.stages.bess_planning_feature_policy.ARTIFACT_KIND`

Source lines 58–58. Manifest family discriminator.

```python
ARTIFACT_KIND = "BESS_CNIG_FEATURE_POLICY_RESULT"
```

<a id="declaration-featurefamily"></a>
### `landscout.stages.bess_planning_feature_policy.FeatureFamily`

Source lines 60–60. Two exact namespaces for triple matching.

```python
FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
```

<a id="declaration-precheckstatus"></a>
### `landscout.stages.bess_planning_feature_policy.PrecheckStatus`

Source lines 61–67. Five permitted precheck outcomes, not legal conclusions.

```python
PrecheckStatus = Literal[
    "LIKELY_MATERIAL_CONSTRAINT",
    "MATERIAL_REVIEW_REQUIRED",
    "DESIGN_REVIEW_REQUIRED",
    "CONTEXT_REVIEW_REQUIRED",
    "UNKNOWN",
]
```

<a id="declaration-confidence"></a>
### `landscout.stages.bess_planning_feature_policy.Confidence`

Source lines 68–68. Three policy confidence literals, not computed probabilities.

```python
Confidence = Literal["HIGH", "MEDIUM", "LOW"]
```

<a id="declaration-allowed-statuses"></a>
### `landscout.stages.bess_planning_feature_policy.ALLOWED_STATUSES`

Source lines 70–78. Frozen membership set for config and row validation; not precedence order.

```python
ALLOWED_STATUSES = frozenset(
    {
        "LIKELY_MATERIAL_CONSTRAINT",
        "MATERIAL_REVIEW_REQUIRED",
        "DESIGN_REVIEW_REQUIRED",
        "CONTEXT_REVIEW_REQUIRED",
        "UNKNOWN",
    }
)
```

<a id="declaration-allowed-confidences"></a>
### `landscout.stages.bess_planning_feature_policy.ALLOWED_CONFIDENCES`

Source lines 79–79. Frozen row-domain membership set.

```python
ALLOWED_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
```

<a id="declaration-code-pattern"></a>
### `landscout.stages.bess_planning_feature_policy.CODE_PATTERN`

Source lines 80–80. Fullmatch callers require two ASCII digits.

```python
CODE_PATTERN = re.compile(r"[0-9]{2}")
```

<a id="declaration-sha-pattern"></a>
### `landscout.stages.bess_planning_feature_policy.SHA_PATTERN`

Source lines 81–81. Fullmatch callers require lowercase 64-hex text.

```python
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

<a id="declaration-policy-table-columns"></a>
### `landscout.stages.bess_planning_feature_policy.POLICY_TABLE_COLUMNS`

Source lines 83–105. Exact output order of 21 columns; references are nullable and no geometry/parcel column is produced.

```python
POLICY_TABLE_COLUMNS = (
    "feature_family",
    "type_code",
    "subtype_code",
    "official_label",
    "official_legal_reference",
    "official_regulation_reference",
    "precheck_status",
    "confidence",
    "status_priority",
    "rationale",
    "required_human_action",
    "limitations",
    "policy_scope",
    "local_feature_text_interpreted",
    "local_regulation_content_interpreted",
    "legal_conclusion_produced",
    "policy_profile",
    "policy_sha256",
    "cnig_profile",
    "cnig_profile_sha256",
    "cnig_complete_result_content_sha256",
)
```

<a id="declaration-policy-table-dtypes"></a>
### `landscout.stages.bess_planning_feature_policy.POLICY_TABLE_DTYPES`

Source lines 106–118. Priority int64, three flags bool, remaining 17 str, derived in column order.

```python
POLICY_TABLE_DTYPES = tuple(
    "int64"
    if column == "status_priority"
    else "bool"
    if column
    in {
        "local_feature_text_interpreted",
        "local_regulation_content_interpreted",
        "legal_conclusion_produced",
    }
    else "str"
    for column in POLICY_TABLE_COLUMNS
)
```

<a id="declaration-policy-table-schema-signature"></a>
### `landscout.stages.bess_planning_feature_policy.POLICY_TABLE_SCHEMA_SIGNATURE`

Source lines 119–125. Canonical schema dict constant used for comparison; not a loaded immutable configuration. Actual index values are hashed separately.

```python
POLICY_TABLE_SCHEMA_SIGNATURE: dict[str, object] = {
    "columns": list(POLICY_TABLE_COLUMNS),
    "dtypes": list(POLICY_TABLE_DTYPES),
    "index_class": "pandas.Index",
    "index_names": [None],
    "index_level_dtypes": ["int64"],
}
```

<a id="declaration-null-reference-literals"></a>
### `landscout.stages.bess_planning_feature_policy.NULL_REFERENCE_LITERALS`

Source lines 126–126. These three non-null strings are rejected in compiled reference cells, not converted to None.

```python
NULL_REFERENCE_LITERALS = frozenset({"None", "nan", "<NA>"})
```

<a id="declaration-policy-result-scalar-fields"></a>
### `landscout.stages.bess_planning_feature_policy.POLICY_RESULT_SCALAR_FIELDS`

Source lines 127–142. Ordered 14-scalar reconstruction/comparison inventory, excluding mutable table.

```python
POLICY_RESULT_SCALAR_FIELDS = (
    "policy_schema_version",
    "result_hash_schema_version",
    "policy_profile",
    "policy_scope",
    "policy_sha256",
    "source_document_id",
    "source_archive_sha256",
    "cnig_profile",
    "cnig_profile_schema_version",
    "cnig_profile_sha256",
    "cnig_result_hash_schema_version",
    "cnig_complete_result_content_sha256",
    "policy_table_content_sha256",
    "complete_result_content_sha256",
)
```

## Qualified symbol contracts

Each notice owns one original symbol. Literal signatures specify argument order, annotations and defaults; fields have no default unless shown. Full bodies/imports appear in the exact final snapshot. No physical units attach to codes/statuses/digests; counts and byte sizes are identified explicitly.

<a id="symbol-bessplanningfeaturepolicyerror"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyError`

Source lines 145–146. Kind: class. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
class BessPlanningFeaturePolicyError(ValueError):
```

ValueError subclass for controlled policy failures. Model validators raise ValueError (reported by Pydantic as ValidationError); public loaders/builders translate their failures at the boundaries below. No I/O in this class.

<a id="symbol--strictpolicymodel"></a>
### `landscout.stages.bess_planning_feature_policy._StrictPolicyModel`

Source lines 149–150. Kind: class. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
class _StrictPolicyModel(BaseModel):
```

Shared Pydantic base sets extra="forbid" and frozen=True. Field-specific strictness is in annotations; this class alone does not deeply freeze arbitrary frames or mutable collections. No I/O.

<a id="symbol-policytableschemasignature"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyTableSchemaSignature`

Source lines 153–160. Kind: class. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
class PolicyTableSchemaSignature(_StrictPolicyModel):
```

Five required persisted schema fields. Tuple annotations copy ordered sequences of strict strings (index names also permit None). No custom validator enforces lengths or the canonical policy schema here: artifact loader compares actual signature, then envelope compares the canonical constant. No I/O.

<a id="symbol-policytableschemasignature-columns"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyTableSchemaSignature.columns`

Source lines 156–156. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
columns: tuple[StrictStr, ...]
```

Ordered strict column names; tuple conversion does not itself enforce the policy column list. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policytableschemasignature-dtypes"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyTableSchemaSignature.dtypes`

Source lines 157–157. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
dtypes: tuple[StrictStr, ...]
```

Ordered strict dtype labels parallel to columns by convention; no length check in this model. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policytableschemasignature-index-class"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyTableSchemaSignature.index_class`

Source lines 158–158. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
index_class: StrictStr
```

Strict persisted class-name string; canonical result requires pandas.Index later. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policytableschemasignature-index-names"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyTableSchemaSignature.index_names`

Source lines 159–159. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
index_names: tuple[StrictStr | None, ...]
```

Ordered tuple of strict strings or None; canonical result requires [None] in JSON form. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policytableschemasignature-index-level-dtypes"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyTableSchemaSignature.index_level_dtypes`

Source lines 160–160. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
index_level_dtypes: tuple[StrictStr, ...]
```

Ordered strict index dtype labels; canonical result requires ["int64"] later. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol--exact-string"></a>
### `landscout.stages.bess_planning_feature_policy._exact_string`

Source lines 163–168. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _exact_string(value: object, label: str) -> str:
```

Return the same value if isinstance(value, str), nonempty and exactly equal to strip(); otherwise raise ValueError labelled by caller. No trimming, normalization, null-literal filtering, copying or I/O. Used by models and row/envelope guards.

<a id="symbol--optional-exact-string"></a>
### `landscout.stages.bess_planning_feature_policy._optional_exact_string`

Source lines 171–174. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _optional_exact_string(value: object, label: str) -> str | None:
```

Return None only for value is None; otherwise delegate to _exact_string. Non-None non-string values fail there. Required nullable fields are not optional constructor arguments. No I/O.

<a id="symbol--sha256-string"></a>
### `landscout.stages.bess_planning_feature_policy._sha256_string`

Source lines 177–181. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _sha256_string(value: object, label: str) -> str:
```

Validate exact nonempty text then fullmatch lowercase 64-hex syntax; return unchanged string or raise ValueError. It checks syntax, not content bytes or authenticity. No hashing or I/O.

<a id="symbol-policysourcelock"></a>
### `landscout.stages.bess_planning_feature_policy.PolicySourceLock`

Source lines 184–209. Kind: class. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
class PolicySourceLock(_StrictPolicyModel):
```

Frozen seven-field source identity declaration. Strings/digests and positive strict integer versions are validated; this model alone permits positive versions other than 2/5. _validate_source_lock compares to coded_result; result and manifest impose supported versions. No source reads here.

<a id="symbol-policysourcelock-document-id"></a>
### `landscout.stages.bess_planning_feature_policy.PolicySourceLock.document_id`

Source lines 185–185. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
document_id: StrictStr
```

Exact nonempty source document lock compared to coded source_document_id. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policysourcelock-archive-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.PolicySourceLock.archive_sha256`

Source lines 186–186. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
archive_sha256: StrictStr
```

Lowercase 64-hex archive lock compared to coded source_archive_sha256; not bytes read here. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policysourcelock-cnig-profile"></a>
### `landscout.stages.bess_planning_feature_policy.PolicySourceLock.cnig_profile`

Source lines 187–187. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_profile: StrictStr
```

Exact nonempty CNIG profile identity, propagated from coded.profile or compared to it by the lock guard. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policysourcelock-cnig-profile-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.PolicySourceLock.cnig_profile_schema_version`

Source lines 188–188. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_profile_schema_version: StrictInt
```

CNIG profile version: source lock requires a positive exact int; result envelope/manifest require exact 2. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policysourcelock-cnig-profile-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.PolicySourceLock.cnig_profile_sha256`

Source lines 189–189. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_profile_sha256: StrictStr
```

Lowercase 64-hex canonical CNIG profile identity, propagated/compared, not recomputed here. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policysourcelock-cnig-result-hash-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.PolicySourceLock.cnig_result_hash_schema_version`

Source lines 190–190. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_result_hash_schema_version: StrictInt
```

CNIG result hash version: positive exact int in lock, exact 5 in result envelope/manifest. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policysourcelock-cnig-complete-result-content-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.PolicySourceLock.cnig_complete_result_content_sha256`

Source lines 191–191. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_complete_result_content_sha256: StrictStr
```

Lowercase 64-hex upstream complete-result commitment; lock comparison and full CNIG validation are distinct checks. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policysourcelock--validate-lock"></a>
### `landscout.stages.bess_planning_feature_policy.PolicySourceLock._validate_lock`

Source lines 194–209. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
    def _validate_lock(self) -> PolicySourceLock:
```

After field validation, check document text, archive SHA syntax, CNIG profile text and both CNIG digest strings; then require exact positive int for the two versions. Return self or ValueError through Pydantic. No mutation, hash recomputation or I/O.

Exact decorators/parameters (not extra closure units):

```python
    @model_validator(mode="after")
```

<a id="symbol-policyentry"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry`

Source lines 212–242. Kind: class. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
class PolicyEntry(_StrictPolicyModel):
```

Frozen declaration for one exact family/type/subtype pair, three expected official-text fields and five decision fields: status, confidence, rationale, required human action and limitations. Priority is derived from the config mapping, not stored in this model. Required nullable expected references have no default. Domain literals and strict scalar annotations precede text/code checks. No dictionary lookup or I/O at construction.

<a id="symbol-policyentry-feature-family"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry.feature_family`

Source lines 213–213. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
feature_family: FeatureFamily
```

Literal PRESCRIPTION or INFORMATION; first component of exact pair namespace. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policyentry-type-code"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry.type_code`

Source lines 214–214. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
type_code: StrictStr
```

Strict string matching exactly two ASCII digits; no numeric coercion or lost leading zeroes. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policyentry-subtype-code"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry.subtype_code`

Source lines 215–215. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
subtype_code: StrictStr
```

Strict string matching exactly two ASCII digits; second code component, not a fallback key. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policyentry-expected-official-label"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry.expected_official_label`

Source lines 216–216. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
expected_official_label: StrictStr
```

Required exact nonempty expected label; later equality checked against dictionary official_label. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policyentry-expected-legal-reference"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry.expected_legal_reference`

Source lines 217–217. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
expected_legal_reference: StrictStr | None
```

Required but nullable expected legal reference; None or exact nonempty text. Literal-null strings are not excluded at model level; see A-004 boundary discussion. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policyentry-expected-regulation-reference"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry.expected_regulation_reference`

Source lines 218–218. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
expected_regulation_reference: StrictStr | None
```

Required but nullable expected regulation/annex reference; None or exact nonempty text, later null-safe compared to dictionary regulation_or_annex_reference. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policyentry-precheck-status"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry.precheck_status`

Source lines 219–219. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
precheck_status: PrecheckStatus
```

One of five declared precheck status literals; not a legal authorization/prohibition. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policyentry-confidence"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry.confidence`

Source lines 220–220. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
confidence: Confidence
```

One of HIGH, MEDIUM, LOW; copied policy evidence, not estimated from geometry. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policyentry-rationale"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry.rationale`

Source lines 221–221. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
rationale: StrictStr
```

Exact nonempty policy explanation, copied unchanged into table. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policyentry-required-human-action"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry.required_human_action`

Source lines 222–222. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
required_human_action: StrictStr
```

Exact nonempty human-review action text, not an automated approval. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policyentry-limitations"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry.limitations`

Source lines 223–223. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
limitations: StrictStr
```

Exact nonempty policy limitation text retained in the compiled row. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-policyentry--validate-entry"></a>
### `landscout.stages.bess_planning_feature_policy.PolicyEntry._validate_entry`

Source lines 226–242. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
    def _validate_entry(self) -> PolicyEntry:
```

Check both full two-ASCII-digit codes; validate exact label, nullable expected references, rationale, required action and limitations in that order. Return self; invalid fields raise ValueError through Pydantic. Does not trim or interpret text, compare dictionary meanings, or reject textual-null reference literals. No I/O.

Exact decorators/parameters (not extra closure units):

```python
    @model_validator(mode="after")
```

<a id="symbol--canonical-json-sha256"></a>
### `landscout.stages.bess_planning_feature_policy._canonical_json_sha256`

Source lines 245–258. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _canonical_json_sha256(value: object) -> str:
```

Serialize any supplied JSON-compatible value using the canonical options in the digest section, encode UTF-8 and return hex SHA256. Translate TypeError/ValueError to BessPlanningFeaturePolicyError with cause; other failures are left to callers. No disk/network I/O.

<a id="symbol--policy-entries-sha256"></a>
### `landscout.stages.bess_planning_feature_policy._policy_entries_sha256`

Source lines 261–262. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _policy_entries_sha256(entries: tuple[PolicyEntry, ...]) -> str:
```

Convert entries, in existing tuple order, to a list of model_dump(mode="json") objects and hash canonically. No sorting or raw YAML read; serializer errors propagate to caller.

<a id="symbol-bessplanningfeaturepolicyconfig"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig`

Source lines 265–335. Kind: class. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
class BessPlanningFeaturePolicyConfig(_StrictPolicyModel):
```

Frozen source-locked policy model, schema 1. Ordered entries are a tuple of frozen models, lock is frozen, status_priority becomes a copied FrozenDict via freeze_mapping. All ten fields are required. Completeness against a dictionary is not a model check; even an empty tuple with a consistent entry digest can pass this model, but a compiled empty table cannot pass the result envelope.

<a id="symbol-bessplanningfeaturepolicyconfig-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.schema_version`

Source lines 266–266. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
schema_version: StrictInt
```

Exact schema version 1 for configuration. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyconfig-profile"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.profile`

Source lines 267–267. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
profile: StrictStr
```

Exact nonempty policy profile name; config hash includes it, but name alone does not pin payload. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyconfig-policy-scope"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.policy_scope`

Source lines 268–268. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
```

Scope OFFICIAL_CNIG_CODE_MEANING_ONLY; literal in config/manifest and equality checked in result envelope. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyconfig-local-feature-text-interpreted"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.local_feature_text_interpreted`

Source lines 269–269. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
local_feature_text_interpreted: StrictBool
```

Strict boolean required to be False; no interpretation of local feature text. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyconfig-local-regulation-content-interpreted"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.local_regulation_content_interpreted`

Source lines 270–270. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
local_regulation_content_interpreted: StrictBool
```

Strict boolean required to be False; no local regulation-content interpretation. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyconfig-legal-conclusion-produced"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.legal_conclusion_produced`

Source lines 271–271. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
legal_conclusion_produced: StrictBool
```

Strict boolean required to be False; precheck evidence is not a legal conclusion. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyconfig-source-lock"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.source_lock`

Source lines 272–272. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
source_lock: PolicySourceLock
```

Required frozen PolicySourceLock containing seven declared source identity/version/hash locks. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyconfig-status-priority"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.status_priority`

Source lines 273–273. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
status_priority: Mapping[PrecheckStatus, StrictInt]
```

Mapping from all five status literals to unique strict positive integers. Validator detaches/freezes with freeze_mapping; serializer returns a fresh dict. No ranking across parcels is computed here. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyconfig-canonical-policy-entries-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.canonical_policy_entries_sha256`

Source lines 274–274. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
canonical_policy_entries_sha256: StrictStr
```

Declared lowercase 64-hex ordered canonical entry-list digest; model validator recomputes it, not a raw YAML checksum. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyconfig-entries"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig.entries`

Source lines 275–275. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
entries: tuple[PolicyEntry, ...]
```

Ordered tuple of frozen PolicyEntry objects. Unique triples must already be lexicographically sorted; digest includes order. Dictionary completeness is a later builder check. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyconfig--serialize-status-priority"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig._serialize_status_priority`

Source lines 278–281. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
    def _serialize_status_priority(
        self, value: Mapping[PrecheckStatus, int]
    ) -> dict[PrecheckStatus, int]:
```

Pydantic field serializer receives Mapping and returns a new dict of the same key/value pairs. This detached serialization value keeps canonical JSON shape stable; it is not an alias allowing priority mutation. No I/O or validation.

Exact decorators/parameters (not extra closure units):

```python
    @field_serializer("status_priority")
```

<a id="symbol-bessplanningfeaturepolicyconfig--validate-policy"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig._validate_policy`

Source lines 284–335. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
    def _validate_policy(self) -> BessPlanningFeaturePolicyConfig:
```

After fields: exact schema 1, exact profile, supported scope, three flags identity-False; all five status keys; exact positive and unique integer priorities; duplicate triples; already-sorted triple order; entry digest syntax and recomputation. Only then assign freeze_mapping(status_priority) using object.__setattr__, and return self. ValueError becomes Pydantic ValidationError; canonical hashing can raise the policy error. Reading values() is an in-memory mapping operation, not filesystem access.

Exact decorators/parameters (not extra closure units):

```python
    @model_validator(mode="after")
```

<a id="symbol-load-bess-planning-feature-policy-config"></a>
### `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config`

Source lines 338–355. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def load_bess_planning_feature_policy_config(
    path: str | Path,
) -> BessPlanningFeaturePolicyConfig:
```

Read Path(path).read_bytes, decode via duplicate-rejecting strict YAML, require top-level Mapping, then model_validate; return frozen config. Preserve policy errors; translate StrictYamlError with its text and cause; wrap other Exception (including file/model failures) as a policy configuration error. Only config bytes are read, no source reconstruction.

<a id="symbol--resolved-policy-config"></a>
### `landscout.stages.bess_planning_feature_policy._resolved_policy_config`

Source lines 358–369. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _resolved_policy_config(
    config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyConfig:
```

For an isinstance config (subclasses included), dump mode="python" with warnings="error" and reconstruct through model_validate; wrap any Exception as invalid in-memory policy. Otherwise use the file loader. Does not trust model_copy/model_construct merely because the class matches. Returns a validated config, without mutating supplied model.

<a id="symbol--policy-sha256"></a>
### `landscout.stages.bess_planning_feature_policy._policy_sha256`

Source lines 372–373. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _policy_sha256(config: BessPlanningFeaturePolicyConfig) -> str:
```

Hash complete config.model_dump(mode="json") canonically, including entry list and entry digest; return lowercase SHA. No raw-file identity, no I/O and no additional validation here.

<a id="symbol-bessplanningfeaturepolicyresult"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult`

Source lines 377–394. Kind: class. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
class BessPlanningFeaturePolicyResult:
```

Frozen dataclass envelope of 14 scalars plus one mutable policy_table. All are required; constructor annotations do not validate them. Freezing prevents field reassignment, not DataFrame mutation. Builders return a new table and validators can detect altered schema/content; this is not immediate deep table immutability despite the original docstring wording.

<a id="symbol-bessplanningfeaturepolicyresult-policy-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.policy_schema_version`

Source lines 380–380. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_schema_version: int
```

Policy/config schema version, exact 1 at validated result/manifest boundary. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-result-hash-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.result_hash_schema_version`

Source lines 381–381. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
result_hash_schema_version: int
```

Canonical result hash version, exact 1 at validated result/manifest boundary. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-policy-profile"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.policy_profile`

Source lines 382–382. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_profile: str
```

Exact nonempty profile identity propagated from config.profile. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-policy-scope"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.policy_scope`

Source lines 383–383. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_scope: str
```

Scope OFFICIAL_CNIG_CODE_MEANING_ONLY; literal in config/manifest and equality checked in result envelope. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-policy-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.policy_sha256`

Source lines 384–384. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_sha256: str
```

Lowercase 64-hex digest of the complete validated config’s canonical JSON; propagated to each row. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-source-document-id"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.source_document_id`

Source lines 385–385. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
source_document_id: str
```

Exact nonempty identity propagated from coded result, not a physical source proof by itself. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-source-archive-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.source_archive_sha256`

Source lines 386–386. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
source_archive_sha256: str
```

Lowercase 64-hex upstream archive identity propagated from coded result; not recomputed by policy table hashing. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-cnig-profile"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.cnig_profile`

Source lines 387–387. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_profile: str
```

Exact nonempty CNIG profile identity, propagated from coded.profile or compared to it by the lock guard. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-cnig-profile-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.cnig_profile_schema_version`

Source lines 388–388. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_profile_schema_version: int
```

CNIG profile version: source lock requires a positive exact int; result envelope/manifest require exact 2. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-cnig-profile-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.cnig_profile_sha256`

Source lines 389–389. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_profile_sha256: str
```

Lowercase 64-hex canonical CNIG profile identity, propagated/compared, not recomputed here. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-cnig-result-hash-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.cnig_result_hash_schema_version`

Source lines 390–390. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_result_hash_schema_version: int
```

CNIG result hash version: positive exact int in lock, exact 5 in result envelope/manifest. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-cnig-complete-result-content-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.cnig_complete_result_content_sha256`

Source lines 391–391. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_complete_result_content_sha256: str
```

Lowercase 64-hex upstream complete-result commitment; lock comparison and full CNIG validation are distinct checks. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-policy-table-content-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.policy_table_content_sha256`

Source lines 392–392. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_table_content_sha256: str
```

Lowercase 64-hex table-domain commitment to metadata and ordered frame payload; recomputed at envelope validation. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-complete-result-content-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.complete_result_content_sha256`

Source lines 393–393. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
complete_result_content_sha256: str
```

Lowercase 64-hex result-domain commitment to metadata and table digest; recomputed at envelope validation. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyresult-policy-table"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyResult.policy_table`

Source lines 394–394. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_table: pd.DataFrame
```

Mutable non-geospatial DataFrame holding 21 columns. Schema, nonempty rows, triple order, domains, lineage and hashes are validated at result boundaries, not by dataclass construction. Required dataclass field, no default or constructor validation; field assignment is frozen, table content is not.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest`

Source lines 397–479. Kind: class. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
class BessPlanningFeaturePolicyArtifactManifest(_StrictPolicyModel):
```

Frozen Pydantic physical/local envelope: schema 2, kind literal, 14 result scalars, one portable Parquet basename, row count, byte size, raw-byte SHA and nested immutable schema signature. All required. It binds claims; reading/comparing physical bytes and reconstructing local result occur later in the loader. No source completeness or I/O in model validation.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.schema_version`

Source lines 400–400. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
schema_version: StrictInt
```

Exact manifest schema version 2. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-artifact-kind"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.artifact_kind`

Source lines 401–401. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
artifact_kind: Literal["BESS_CNIG_FEATURE_POLICY_RESULT"]
```

Literal BESS_CNIG_FEATURE_POLICY_RESULT identifies this manifest family. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-policy-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.policy_schema_version`

Source lines 402–402. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_schema_version: StrictInt
```

Policy/config schema version, exact 1 at validated result/manifest boundary. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-result-hash-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.result_hash_schema_version`

Source lines 403–403. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
result_hash_schema_version: StrictInt
```

Canonical result hash version, exact 1 at validated result/manifest boundary. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-policy-profile"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.policy_profile`

Source lines 404–404. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_profile: StrictStr
```

Exact nonempty profile identity propagated from config.profile. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-policy-scope"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.policy_scope`

Source lines 405–405. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
```

Scope OFFICIAL_CNIG_CODE_MEANING_ONLY; literal in config/manifest and equality checked in result envelope. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-policy-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.policy_sha256`

Source lines 406–406. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_sha256: StrictStr
```

Lowercase 64-hex digest of the complete validated config’s canonical JSON; propagated to each row. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-source-document-id"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.source_document_id`

Source lines 407–407. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
source_document_id: StrictStr
```

Exact nonempty identity propagated from coded result, not a physical source proof by itself. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-source-archive-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.source_archive_sha256`

Source lines 408–408. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
source_archive_sha256: StrictStr
```

Lowercase 64-hex upstream archive identity propagated from coded result; not recomputed by policy table hashing. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-cnig-profile"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.cnig_profile`

Source lines 409–409. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_profile: StrictStr
```

Exact nonempty CNIG profile identity, propagated from coded.profile or compared to it by the lock guard. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-cnig-profile-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.cnig_profile_schema_version`

Source lines 410–410. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_profile_schema_version: StrictInt
```

CNIG profile version: source lock requires a positive exact int; result envelope/manifest require exact 2. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-cnig-profile-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.cnig_profile_sha256`

Source lines 411–411. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_profile_sha256: StrictStr
```

Lowercase 64-hex canonical CNIG profile identity, propagated/compared, not recomputed here. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-cnig-result-hash-schema-version"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.cnig_result_hash_schema_version`

Source lines 412–412. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_result_hash_schema_version: StrictInt
```

CNIG result hash version: positive exact int in lock, exact 5 in result envelope/manifest. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-cnig-complete-result-content-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.cnig_complete_result_content_sha256`

Source lines 413–413. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
cnig_complete_result_content_sha256: StrictStr
```

Lowercase 64-hex upstream complete-result commitment; lock comparison and full CNIG validation are distinct checks. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-policy-table-content-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.policy_table_content_sha256`

Source lines 414–414. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_table_content_sha256: StrictStr
```

Lowercase 64-hex table-domain commitment to metadata and ordered frame payload; recomputed at envelope validation. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-complete-result-content-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.complete_result_content_sha256`

Source lines 415–415. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
complete_result_content_sha256: StrictStr
```

Lowercase 64-hex result-domain commitment to metadata and table digest; recomputed at envelope validation. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-parquet-filename"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.parquet_filename`

Source lines 416–416. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
parquet_filename: StrictStr
```

Strict portable Parquet basename; common guard excludes paths, separators, reserved Windows device names/control characters/forbidden characters and requires .parquet. Loader separately compares it to supplied path.name. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-parquet-row-count"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.parquet_row_count`

Source lines 417–417. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
parquet_row_count: StrictInt
```

Strict nonnegative integer count, no unit beyond rows. Loader compares actual rows; local result rejects zero-row table even though manifest model allows zero. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-parquet-size-bytes"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.parquet_size_bytes`

Source lines 418–418. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
parquet_size_bytes: StrictInt
```

Strict positive integer physical byte count; loader compares captured length before parsing. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-parquet-sha256"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.parquet_sha256`

Source lines 419–419. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
parquet_sha256: StrictStr
```

Lowercase 64-hex raw Parquet byte digest; loader compares the captured bytes, distinct from canonical table hash. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest-policy-table-schema-signature"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest.policy_table_schema_signature`

Source lines 420–420. Kind: field. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
policy_table_schema_signature: PolicyTableSchemaSignature
```

Frozen nested PolicyTableSchemaSignature; loader compares actual schema, then local envelope compares canonical schema constant. Required field with no default. Annotation below governs Pydantic parsing; inherited extra-field rejection and freezing apply. No field-level I/O.

<a id="symbol-bessplanningfeaturepolicyartifactmanifest--validate-manifest"></a>
### `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyArtifactManifest._validate_manifest`

Source lines 423–479. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
    def _validate_manifest(self) -> BessPlanningFeaturePolicyArtifactManifest:
```

Require exact ints for manifest/policy/result versions 2/1/1 and CNIG 2/5, three exact identity strings, seven SHA syntax checks, nonnegative row count and strictly positive byte size, then portable filename. Return self or ValueError (Pydantic ValidationError). Does not assert canonical table content, nonempty actual table or physical SHA equality; those are loader/envelope checks.

Exact decorators/parameters (not extra closure units):

```python
    @model_validator(mode="after")
```

<a id="symbol--null-value"></a>
### `landscout.stages.bess_planning_feature_policy._null_value`

Source lines 482–491. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _null_value(value: object) -> object:
```

Return None for None/pd.NA, or scalar bool/np.bool_ true returned by pd.isna. Catch TypeError/ValueError from pd.isna and return original; non-scalar masks do not become truth values. Otherwise preserve value. No mutation or I/O.

<a id="symbol--null-safe-equal"></a>
### `landscout.stages.bess_planning_feature_policy._null_safe_equal`

Source lines 494–502. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _null_safe_equal(left: object, right: object) -> bool:
```

Normalize both sides with _null_value. If either is None, require both None; otherwise return bool(left == right), returning False for TypeError/ValueError. Used for expected dictionary references; not a general recursive comparison. No I/O.

<a id="symbol--canonical-value"></a>
### `landscout.stages.bess_planning_feature_policy._canonical_value`

Source lines 505–528. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _canonical_value(value: object) -> object:
```

Canonicalize one frame scalar in the exact null/date/NumPy/bool/integer/finite-real/string order described above. Unsupported types or nonfinite real values not already recognized as missing raise policy error. Returns JSON-compatible scalar, never mutates value or handles geometry. No I/O.

<a id="symbol--frame-payload"></a>
### `landscout.stages.bess_planning_feature_policy._frame_payload`

Source lines 531–539. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
```

Return a new dict of deterministic schema signature, ordered canonical index values and ordered rows from itertuples(index=False, name=None). No row sorting, index normalization or frame mutation; canonical scalar failures propagate. Used by table hash and full reconstruction comparison, not physical serialization.

<a id="symbol--validate-source-lock"></a>
### `landscout.stages.bess_planning_feature_policy._validate_source_lock`

Source lines 542–572. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _validate_source_lock(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> None:
```

Compare the seven configured identity/version/hash values to coded result attributes using !=, in document/archive/profile/profile-schema/profile-hash/result-schema/complete-hash order. First mismatch raises policy error; success returns None. No file reads, type-exact coded validation or hash recomputation; full CNIG validation follows at public source boundaries.

<a id="symbol--dictionary-by-pair"></a>
### `landscout.stages.bess_planning_feature_policy._dictionary_by_pair`

Source lines 575–591. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _dictionary_by_pair(
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

Read code_dictionary.to_dict("records"), form three-part keys using str on family/codes, reject duplicate keys and return a new key-to-row dict. Assumes previously validated CNIG content; not itself a canonical dtype/text/source validator. No input mutation or disk I/O.

<a id="symbol--validate-policy-completeness"></a>
### `landscout.stages.bess_planning_feature_policy._validate_policy_completeness`

Source lines 594–630. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _validate_policy_completeness(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
```

Build dictionary lookup, compare config entry keys with dictionary keys, reject sorted missing keys first and extras second. For every entry require exact expected label equality, then null-safe legal and regulation reference equality. Return lookup. No type-only or cross-family fallback, no local regulation interpretation and no I/O.

<a id="symbol--policy-table"></a>
### `landscout.stages.bess_planning_feature_policy._policy_table`

Source lines 633–698. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _policy_table(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
    dictionary: dict[tuple[str, str, str], dict[str, object]],
    policy_hash: str,
) -> pd.DataFrame:
```

For each already-ordered config entry, copy triple from entry and official label/references from dictionary and decisions/priority/flags from config; append policy/CNIG identity fields. Create a new DataFrame with the exact 21 columns, convert 17 string columns with pd.array(dtype="str"), then priority with astype("int64") and three flags with astype("bool") and replace its index with a plain Pandas Index copy. True missing references remain missing. No source frame mutation, geometry output or disk I/O; casting errors propagate.

<a id="symbol--component-metadata"></a>
### `landscout.stages.bess_planning_feature_policy._component_metadata`

Source lines 701–717. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _component_metadata(result: BessPlanningFeaturePolicyResult) -> dict[str, object]:
```

Return a new dict of the 12 named scalar identities/versions/scope in source order, excluding table and its two computed digests. No validation, coercion, source hashing or I/O; used by both result digest helpers.

<a id="symbol--policy-table-sha256"></a>
### `landscout.stages.bess_planning_feature_policy._policy_table_sha256`

Source lines 720–727. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _policy_table_sha256(result: BessPlanningFeaturePolicyResult) -> str:
```

Return canonical SHA of table domain + 12 metadata entries + frame payload. Commits ordered schema/index/rows, not Parquet bytes; no validation beyond called serializers and no I/O.

<a id="symbol--complete-result-sha256"></a>
### `landscout.stages.bess_planning_feature_policy._complete_result_sha256`

Source lines 730–737. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _complete_result_sha256(result: BessPlanningFeaturePolicyResult) -> str:
```

Return canonical SHA of result domain + same metadata + policy_table_content_sha256. Does not embed the complete hash itself or directly duplicate table payload. No physical I/O or independent source verification.

<a id="symbol--result-with-hashes"></a>
### `landscout.stages.bess_planning_feature_policy._result_with_hashes`

Source lines 740–749. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _result_with_hashes(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
```

dataclasses.replace first installs table hash, then complete hash calculated from that component result. Return a new frozen envelope sharing the same mutable table; does not validate semantics or copy the table. Tests use this private resealing helper to isolate guards.

<a id="symbol--validate-policy-table-rows"></a>
### `landscout.stages.bess_planning_feature_policy._validate_policy_table_rows`

Source lines 752–851. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _validate_policy_table_rows(result: BessPlanningFeaturePolicyResult) -> None:
```

Iterate record copies: family and exact codes, duplicate triple, exact label/rationale/action/limitations, nullable references (reject textual-null literals), status/confidence, exact positive priority and bidirectional status/priority consistency among present rows, scope equality, three flags identity-False, five row/envelope lineage equalities. Finally require sorted triple order. Returns None or explicit policy errors, wrapping exact-string ValueError locally. No expected config/dictionary argument, no completeness/source comparison or I/O.

<a id="symbol--build-result"></a>
### `landscout.stages.bess_planning_feature_policy._build_result`

Source lines 854–879. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _build_result(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> BessPlanningFeaturePolicyResult:
```

Private builder checks dictionary completeness/text agreement, hashes config, builds fresh table, propagates coded identities/versions, installs empty computed hashes and calls _result_with_hashes. It does NOT resolve/revalidate config, compare source locks or invoke the CNIG source owner itself. No physical reads; public callers own those preceding checks.

<a id="symbol--validate-result-envelope"></a>
### `landscout.stages.bess_planning_feature_policy._validate_result_envelope`

Source lines 882–940. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _validate_result_envelope(result: BessPlanningFeaturePolicyResult) -> None:
```

Require exact result type (subclasses rejected), exact integer versions 1/1 and CNIG 2/5, supported scope, exact identity text; then a DataFrame instance that is not GeoDataFrame, no duplicate columns, exact ordered columns and schema, nonempty table, scalar SHA syntax, intrinsic row checks, and recomputed table/complete hash equality. Return None. Local helper can leak unexpected exceptions; public wrapper below controls them. Does not receive config/dictionary, so locally valid one-row subsets can pass. No I/O.

<a id="symbol-validate-bess-planning-feature-policy-result-envelope"></a>
### `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result_envelope`

Source lines 943–955. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def validate_bess_planning_feature_policy_result_envelope(
    result: BessPlanningFeaturePolicyResult,
) -> None:
```

One required result, None return on valid local envelope. Call private envelope, preserve explicit policy errors and wrap every other Exception as a policy envelope error with cause. No source/config reload, reconstruction or disk I/O. This wrapper genuinely exists here, unlike the application wrapper.

<a id="symbol-load-bess-planning-feature-policy-artifacts"></a>
### `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_artifacts`

Source lines 958–1004. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def load_bess_planning_feature_policy_artifacts(
    parquet_path: str | Path,
    manifest_path: str | Path,
) -> BessPlanningFeaturePolicyResult:
```

Two required str-or-Path parameters, Parquet then manifest. Read strict JSON object from manifest bytes and validate model; compare declared filename to parquet.name; capture parquet.read_bytes once, compare len and SHA; pd.read_parquet(BytesIO(captured)); compare rows and schema to model_dump(mode="json"); reconstruct 14 scalars plus table, then private local envelope. Return result; preserve policy errors and wrap other Exception with cause. No source-complete validation, writer, containment, symlink rejection, atomic snapshot or live-path postcondition.

<a id="symbol--validate-coded-source"></a>
### `landscout.stages.bess_planning_feature_policy._validate_coded_source`

Source lines 1007–1031. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def _validate_coded_source(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
) -> None:
```

Forward eight required source/profile/result inputs once to validate_planning_feature_code_result. Catch any Exception from that owner and chain a Source-complete CNIG policy error; return None. It does not count or collapse the owner’s internal physical reads/rebuilds. No independent local table mutation.

<a id="compile_bess_planning_feature_policy"></a>
<a id="symbol-compile-bess-planning-feature-policy"></a>
### `landscout.stages.bess_planning_feature_policy.compile_bess_planning_feature_policy`

Source lines 1034–1068. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def compile_bess_planning_feature_policy(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyResult:
```

Nine required inputs. Resolve policy config, compare seven source locks, invoke full CNIG owner through _validate_coded_source, build new policy result, validate local envelope, return result. Preserve explicit policy errors and broadly wrap other Exception with cause. A policy path reads YAML; delegated owner can reread/rebuild factual sources. No policy application to features/relations/parcels or scoring.

<a id="symbol-validate-bess-planning-feature-policy-result"></a>
### `landscout.stages.bess_planning_feature_policy.validate_bess_planning_feature_policy_result`

Source lines 1071–1114. Kind: function. Owner: `landscout.stages.bess_planning_feature_policy`.

```python
def validate_bess_planning_feature_policy_result(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    result: BessPlanningFeaturePolicyResult,
) -> None:
```

Ten required inputs: compiler inputs then result. Validate result envelope BEFORE config resolution/locks/source owner; build expected result from those validated inputs; compare all 14 named scalars then frame payload equality. Return None or controlled policy error; other Exception wrapped with cause. Rejects coordinated but false table/hash content through source reconstruction; no mutation or publication.

## Complete source snapshot

Exact full Git-content UTF-8 snapshot, not evidence that the prose is correct by itself.

```python
"""Compile a source-locked BESS policy for official CNIG feature-code meanings."""

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

from landscout.common.artifact_paths import validate_portable_parquet_filename
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.immutable_mapping import freeze_mapping
from landscout.common.strict_json import loads_strict_json_object
from landscout.common.strict_yaml import StrictYamlError, loads_strict_yaml
from landscout.sources.gpu_fr import GpuPlanningDocument
from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result,
)

__all__ = [
    "BessPlanningFeaturePolicyArtifactManifest",
    "BessPlanningFeaturePolicyConfig",
    "BessPlanningFeaturePolicyError",
    "BessPlanningFeaturePolicyResult",
    "compile_bess_planning_feature_policy",
    "load_bess_planning_feature_policy_artifacts",
    "load_bess_planning_feature_policy_config",
    "validate_bess_planning_feature_policy_result",
    "validate_bess_planning_feature_policy_result_envelope",
]

POLICY_SCHEMA_VERSION = 1
RESULT_HASH_SCHEMA_VERSION = 1
ARTIFACT_MANIFEST_SCHEMA_VERSION = 2
POLICY_SCOPE = "OFFICIAL_CNIG_CODE_MEANING_ONLY"
ARTIFACT_KIND = "BESS_CNIG_FEATURE_POLICY_RESULT"

FeatureFamily = Literal["PRESCRIPTION", "INFORMATION"]
PrecheckStatus = Literal[
    "LIKELY_MATERIAL_CONSTRAINT",
    "MATERIAL_REVIEW_REQUIRED",
    "DESIGN_REVIEW_REQUIRED",
    "CONTEXT_REVIEW_REQUIRED",
    "UNKNOWN",
]
Confidence = Literal["HIGH", "MEDIUM", "LOW"]

ALLOWED_STATUSES = frozenset(
    {
        "LIKELY_MATERIAL_CONSTRAINT",
        "MATERIAL_REVIEW_REQUIRED",
        "DESIGN_REVIEW_REQUIRED",
        "CONTEXT_REVIEW_REQUIRED",
        "UNKNOWN",
    }
)
ALLOWED_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
CODE_PATTERN = re.compile(r"[0-9]{2}")
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")

POLICY_TABLE_COLUMNS = (
    "feature_family",
    "type_code",
    "subtype_code",
    "official_label",
    "official_legal_reference",
    "official_regulation_reference",
    "precheck_status",
    "confidence",
    "status_priority",
    "rationale",
    "required_human_action",
    "limitations",
    "policy_scope",
    "local_feature_text_interpreted",
    "local_regulation_content_interpreted",
    "legal_conclusion_produced",
    "policy_profile",
    "policy_sha256",
    "cnig_profile",
    "cnig_profile_sha256",
    "cnig_complete_result_content_sha256",
)
POLICY_TABLE_DTYPES = tuple(
    "int64"
    if column == "status_priority"
    else "bool"
    if column
    in {
        "local_feature_text_interpreted",
        "local_regulation_content_interpreted",
        "legal_conclusion_produced",
    }
    else "str"
    for column in POLICY_TABLE_COLUMNS
)
POLICY_TABLE_SCHEMA_SIGNATURE: dict[str, object] = {
    "columns": list(POLICY_TABLE_COLUMNS),
    "dtypes": list(POLICY_TABLE_DTYPES),
    "index_class": "pandas.Index",
    "index_names": [None],
    "index_level_dtypes": ["int64"],
}
NULL_REFERENCE_LITERALS = frozenset({"None", "nan", "<NA>"})
POLICY_RESULT_SCALAR_FIELDS = (
    "policy_schema_version",
    "result_hash_schema_version",
    "policy_profile",
    "policy_scope",
    "policy_sha256",
    "source_document_id",
    "source_archive_sha256",
    "cnig_profile",
    "cnig_profile_schema_version",
    "cnig_profile_sha256",
    "cnig_result_hash_schema_version",
    "cnig_complete_result_content_sha256",
    "policy_table_content_sha256",
    "complete_result_content_sha256",
)


class BessPlanningFeaturePolicyError(ValueError):
    """Raised when the official-code BESS policy cannot be proven exact."""


class _StrictPolicyModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class PolicyTableSchemaSignature(_StrictPolicyModel):
    """Immutable persisted schema identity for the normalized policy table."""

    columns: tuple[StrictStr, ...]
    dtypes: tuple[StrictStr, ...]
    index_class: StrictStr
    index_names: tuple[StrictStr | None, ...]
    index_level_dtypes: tuple[StrictStr, ...]


def _exact_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(
            f"{label} must be an exact non-empty string without edge whitespace"
        )
    return value


def _optional_exact_string(value: object, label: str) -> str | None:
    if value is None:
        return None
    return _exact_string(value, label)


def _sha256_string(value: object, label: str) -> str:
    text = _exact_string(value, label)
    if SHA_PATTERN.fullmatch(text) is None:
        raise ValueError(f"{label} must be a lowercase SHA256")
    return text


class PolicySourceLock(_StrictPolicyModel):
    document_id: StrictStr
    archive_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_schema_version: StrictInt
    cnig_profile_sha256: StrictStr
    cnig_result_hash_schema_version: StrictInt
    cnig_complete_result_content_sha256: StrictStr

    @model_validator(mode="after")
    def _validate_lock(self) -> PolicySourceLock:
        _exact_string(self.document_id, "document_id")
        _sha256_string(self.archive_sha256, "archive_sha256")
        _exact_string(self.cnig_profile, "cnig_profile")
        _sha256_string(self.cnig_profile_sha256, "cnig_profile_sha256")
        _sha256_string(
            self.cnig_complete_result_content_sha256,
            "cnig_complete_result_content_sha256",
        )
        for value, label in (
            (self.cnig_profile_schema_version, "cnig_profile_schema_version"),
            (self.cnig_result_hash_schema_version, "cnig_result_hash_schema_version"),
        ):
            if type(value) is not int or value < 1:
                raise ValueError(f"{label} must be a strict positive integer")
        return self


class PolicyEntry(_StrictPolicyModel):
    feature_family: FeatureFamily
    type_code: StrictStr
    subtype_code: StrictStr
    expected_official_label: StrictStr
    expected_legal_reference: StrictStr | None
    expected_regulation_reference: StrictStr | None
    precheck_status: PrecheckStatus
    confidence: Confidence
    rationale: StrictStr
    required_human_action: StrictStr
    limitations: StrictStr

    @model_validator(mode="after")
    def _validate_entry(self) -> PolicyEntry:
        if CODE_PATTERN.fullmatch(self.type_code) is None:
            raise ValueError("type_code must be an exact two-character digit string")
        if CODE_PATTERN.fullmatch(self.subtype_code) is None:
            raise ValueError("subtype_code must be an exact two-character digit string")
        _exact_string(self.expected_official_label, "expected_official_label")
        _optional_exact_string(
            self.expected_legal_reference, "expected_legal_reference"
        )
        _optional_exact_string(
            self.expected_regulation_reference,
            "expected_regulation_reference",
        )
        _exact_string(self.rationale, "rationale")
        _exact_string(self.required_human_action, "required_human_action")
        _exact_string(self.limitations, "limitations")
        return self


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
        raise BessPlanningFeaturePolicyError(
            "Policy integrity payload is not canonical JSON"
        ) from error
    return sha256(encoded).hexdigest()


def _policy_entries_sha256(entries: tuple[PolicyEntry, ...]) -> str:
    return _canonical_json_sha256([entry.model_dump(mode="json") for entry in entries])


class BessPlanningFeaturePolicyConfig(_StrictPolicyModel):
    schema_version: StrictInt
    profile: StrictStr
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    local_feature_text_interpreted: StrictBool
    local_regulation_content_interpreted: StrictBool
    legal_conclusion_produced: StrictBool
    source_lock: PolicySourceLock
    status_priority: Mapping[PrecheckStatus, StrictInt]
    canonical_policy_entries_sha256: StrictStr
    entries: tuple[PolicyEntry, ...]

    @field_serializer("status_priority")
    def _serialize_status_priority(
        self, value: Mapping[PrecheckStatus, int]
    ) -> dict[PrecheckStatus, int]:
        return dict(value)

    @model_validator(mode="after")
    def _validate_policy(self) -> BessPlanningFeaturePolicyConfig:
        if (
            type(self.schema_version) is not int
            or self.schema_version != POLICY_SCHEMA_VERSION
        ):
            raise ValueError(
                f"policy schema version must equal {POLICY_SCHEMA_VERSION}"
            )
        _exact_string(self.profile, "profile")
        if self.policy_scope != POLICY_SCOPE:
            raise ValueError("policy_scope is unsupported")
        if (
            self.local_feature_text_interpreted is not False
            or self.local_regulation_content_interpreted is not False
            or self.legal_conclusion_produced is not False
        ):
            raise ValueError(
                "policy interpretation and legal-conclusion flags must be false"
            )
        if set(self.status_priority) != ALLOWED_STATUSES:
            raise ValueError(
                "status priority must contain every allowed status exactly once"
            )
        priorities = list(self.status_priority.values())
        if any(type(value) is not int or value <= 0 for value in priorities):
            raise ValueError("status priority values must be strict positive integers")
        if len(set(priorities)) != len(priorities):
            raise ValueError("status priority values must be unique")
        keys = [
            (entry.feature_family, entry.type_code, entry.subtype_code)
            for entry in self.entries
        ]
        if len(keys) != len(set(keys)):
            raise ValueError(
                "policy entries contain a duplicate family/type/subtype pair"
            )
        if keys != sorted(keys):
            raise ValueError(
                "policy entries must use deterministic family/type/subtype order"
            )
        _sha256_string(
            self.canonical_policy_entries_sha256,
            "canonical_policy_entries_sha256",
        )
        if _policy_entries_sha256(self.entries) != self.canonical_policy_entries_sha256:
            raise ValueError(
                "canonical policy-entry SHA256 differs from policy entries"
            )
        object.__setattr__(
            self, "status_priority", freeze_mapping(self.status_priority)
        )
        return self


def load_bess_planning_feature_policy_config(
    path: str | Path,
) -> BessPlanningFeaturePolicyConfig:
    """Load a strict offline BESS policy for official CNIG feature-code pairs."""

    try:
        payload = loads_strict_yaml(Path(path).read_bytes())
        if not isinstance(payload, Mapping):
            raise BessPlanningFeaturePolicyError("BESS CNIG policy must be a mapping")
        return BessPlanningFeaturePolicyConfig.model_validate(payload)
    except BessPlanningFeaturePolicyError:
        raise
    except StrictYamlError as error:
        raise BessPlanningFeaturePolicyError(str(error)) from error
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy is invalid"
        ) from error


def _resolved_policy_config(
    config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyConfig:
    if not isinstance(config, BessPlanningFeaturePolicyConfig):
        return load_bess_planning_feature_policy_config(config)
    try:
        payload = config.model_dump(mode="python", warnings="error")
        return BessPlanningFeaturePolicyConfig.model_validate(payload)
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "in-memory BESS planning-feature policy config is invalid"
        ) from error


def _policy_sha256(config: BessPlanningFeaturePolicyConfig) -> str:
    return _canonical_json_sha256(config.model_dump(mode="json"))


@dataclass(frozen=True)
class BessPlanningFeaturePolicyResult:
    """Immutable normalized policy table and its source-complete hash envelope."""

    policy_schema_version: int
    result_hash_schema_version: int
    policy_profile: str
    policy_scope: str
    policy_sha256: str
    source_document_id: str
    source_archive_sha256: str
    cnig_profile: str
    cnig_profile_schema_version: int
    cnig_profile_sha256: str
    cnig_result_hash_schema_version: int
    cnig_complete_result_content_sha256: str
    policy_table_content_sha256: str
    complete_result_content_sha256: str
    policy_table: pd.DataFrame


class BessPlanningFeaturePolicyArtifactManifest(_StrictPolicyModel):
    """Strict physical binding between one policy table and its hash envelope."""

    schema_version: StrictInt
    artifact_kind: Literal["BESS_CNIG_FEATURE_POLICY_RESULT"]
    policy_schema_version: StrictInt
    result_hash_schema_version: StrictInt
    policy_profile: StrictStr
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    policy_sha256: StrictStr
    source_document_id: StrictStr
    source_archive_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_schema_version: StrictInt
    cnig_profile_sha256: StrictStr
    cnig_result_hash_schema_version: StrictInt
    cnig_complete_result_content_sha256: StrictStr
    policy_table_content_sha256: StrictStr
    complete_result_content_sha256: StrictStr
    parquet_filename: StrictStr
    parquet_row_count: StrictInt
    parquet_size_bytes: StrictInt
    parquet_sha256: StrictStr
    policy_table_schema_signature: PolicyTableSchemaSignature

    @model_validator(mode="after")
    def _validate_manifest(self) -> BessPlanningFeaturePolicyArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError(
                "artifact manifest schema version must equal "
                f"{ARTIFACT_MANIFEST_SCHEMA_VERSION}"
            )
        if (
            type(self.policy_schema_version) is not int
            or self.policy_schema_version != POLICY_SCHEMA_VERSION
        ):
            raise ValueError("artifact policy schema version is unsupported")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("artifact result hash schema version is unsupported")
        if (
            type(self.cnig_profile_schema_version) is not int
            or self.cnig_profile_schema_version != 2
        ):
            raise ValueError("artifact CNIG profile schema version is unsupported")
        if (
            type(self.cnig_result_hash_schema_version) is not int
            or self.cnig_result_hash_schema_version != 5
        ):
            raise ValueError("artifact CNIG result hash schema version is unsupported")
        for exact_value, label in (
            (self.policy_profile, "policy_profile"),
            (self.source_document_id, "source_document_id"),
            (self.cnig_profile, "cnig_profile"),
        ):
            _exact_string(exact_value, label)
        for hash_value, label in (
            (self.policy_sha256, "policy_sha256"),
            (self.source_archive_sha256, "source_archive_sha256"),
            (self.cnig_profile_sha256, "cnig_profile_sha256"),
            (
                self.cnig_complete_result_content_sha256,
                "cnig_complete_result_content_sha256",
            ),
            (self.policy_table_content_sha256, "policy_table_content_sha256"),
            (self.complete_result_content_sha256, "complete_result_content_sha256"),
            (self.parquet_sha256, "parquet_sha256"),
        ):
            _sha256_string(hash_value, label)
        for integer_value, label, allow_zero in (
            (self.parquet_row_count, "parquet_row_count", True),
            (self.parquet_size_bytes, "parquet_size_bytes", False),
        ):
            minimum = 0 if allow_zero else 1
            if type(integer_value) is not int or integer_value < minimum:
                raise ValueError(f"{label} is invalid")
        validate_portable_parquet_filename(self.parquet_filename, "parquet_filename")
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


def _null_safe_equal(left: object, right: object) -> bool:
    normalized_left = _null_value(left)
    normalized_right = _null_value(right)
    if normalized_left is None or normalized_right is None:
        return normalized_left is None and normalized_right is None
    try:
        return bool(normalized_left == normalized_right)
    except (TypeError, ValueError):
        return False


def _canonical_value(value: object) -> object:
    value = _null_value(value)
    if value is None:
        return None
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
            raise BessPlanningFeaturePolicyError(
                "Policy integrity payload contains non-finite data"
            )
        return number
    if isinstance(value, str):
        return value
    raise BessPlanningFeaturePolicyError(
        f"Policy integrity payload contains unsupported {type(value).__name__}"
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


def _validate_source_lock(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> None:
    lock = config.source_lock
    comparisons = (
        (lock.document_id, coded_result.source_document_id, "document ID"),
        (lock.archive_sha256, coded_result.source_archive_sha256, "archive SHA256"),
        (lock.cnig_profile, coded_result.profile, "CNIG profile"),
        (
            lock.cnig_profile_schema_version,
            coded_result.profile_schema_version,
            "CNIG profile schema version",
        ),
        (lock.cnig_profile_sha256, coded_result.profile_sha256, "CNIG profile SHA256"),
        (
            lock.cnig_result_hash_schema_version,
            coded_result.result_hash_schema_version,
            "CNIG result hash schema version",
        ),
        (
            lock.cnig_complete_result_content_sha256,
            coded_result.complete_result_content_sha256,
            "CNIG complete result SHA256",
        ),
    )
    for configured, actual, label in comparisons:
        if configured != actual:
            raise BessPlanningFeaturePolicyError(
                f"Policy source lock differs from validated {label}"
            )


def _dictionary_by_pair(
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    rows = coded_result.code_dictionary.to_dict("records")
    indexed: dict[tuple[str, str, str], dict[str, object]] = {}
    for row in rows:
        key = (
            str(row["feature_family"]),
            str(row["type_code"]),
            str(row["subtype_code"]),
        )
        if key in indexed:
            raise BessPlanningFeaturePolicyError(
                "Validated CNIG code dictionary contains a duplicate pair"
            )
        indexed[key] = row
    return indexed


def _validate_policy_completeness(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> dict[tuple[str, str, str], dict[str, object]]:
    dictionary = _dictionary_by_pair(coded_result)
    entries: dict[tuple[str, str, str], PolicyEntry] = {
        (entry.feature_family, entry.type_code, entry.subtype_code): entry
        for entry in config.entries
    }
    missing = sorted(set(dictionary) - set(entries))
    extra = sorted(set(entries) - set(dictionary))
    if missing:
        raise BessPlanningFeaturePolicyError(
            f"Policy is missing validated CNIG pair(s): {missing}"
        )
    if extra:
        raise BessPlanningFeaturePolicyError(
            f"Policy contains extra CNIG pair(s): {extra}"
        )
    for key, row in dictionary.items():
        entry = entries[key]
        if entry.expected_official_label != row["official_label"]:
            raise BessPlanningFeaturePolicyError(
                f"Policy official label mismatch for pair {key}"
            )
        if not _null_safe_equal(entry.expected_legal_reference, row["legal_reference"]):
            raise BessPlanningFeaturePolicyError(
                f"Policy legal reference mismatch for pair {key}"
            )
        if not _null_safe_equal(
            entry.expected_regulation_reference,
            row["regulation_or_annex_reference"],
        ):
            raise BessPlanningFeaturePolicyError(
                f"Policy regulation reference mismatch for pair {key}"
            )
    return dictionary


def _policy_table(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
    dictionary: dict[tuple[str, str, str], dict[str, object]],
    policy_hash: str,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for entry in config.entries:
        key = (entry.feature_family, entry.type_code, entry.subtype_code)
        official = dictionary[key]
        rows.append(
            {
                "feature_family": entry.feature_family,
                "type_code": entry.type_code,
                "subtype_code": entry.subtype_code,
                "official_label": official["official_label"],
                "official_legal_reference": official["legal_reference"],
                "official_regulation_reference": (
                    official["regulation_or_annex_reference"]
                ),
                "precheck_status": entry.precheck_status,
                "confidence": entry.confidence,
                "status_priority": config.status_priority[entry.precheck_status],
                "rationale": entry.rationale,
                "required_human_action": entry.required_human_action,
                "limitations": entry.limitations,
                "policy_scope": config.policy_scope,
                "local_feature_text_interpreted": (
                    config.local_feature_text_interpreted
                ),
                "local_regulation_content_interpreted": (
                    config.local_regulation_content_interpreted
                ),
                "legal_conclusion_produced": config.legal_conclusion_produced,
                "policy_profile": config.profile,
                "policy_sha256": policy_hash,
                "cnig_profile": coded_result.profile,
                "cnig_profile_sha256": coded_result.profile_sha256,
                "cnig_complete_result_content_sha256": (
                    coded_result.complete_result_content_sha256
                ),
            }
        )
    output = pd.DataFrame(rows, columns=POLICY_TABLE_COLUMNS)
    string_columns = tuple(
        column
        for column in POLICY_TABLE_COLUMNS
        if column
        not in {
            "status_priority",
            "local_feature_text_interpreted",
            "local_regulation_content_interpreted",
            "legal_conclusion_produced",
        }
    )
    for column in string_columns:
        output[column] = pd.array(output[column].tolist(), dtype="str")
    output["status_priority"] = output["status_priority"].astype("int64")
    for column in (
        "local_feature_text_interpreted",
        "local_regulation_content_interpreted",
        "legal_conclusion_produced",
    ):
        output[column] = output[column].astype("bool")
    output.index = pd.Index(output.index.to_numpy(copy=True), name=output.index.name)
    return output


def _component_metadata(result: BessPlanningFeaturePolicyResult) -> dict[str, object]:
    return {
        "policy_schema_version": result.policy_schema_version,
        "result_hash_schema_version": result.result_hash_schema_version,
        "policy_profile": result.policy_profile,
        "policy_scope": result.policy_scope,
        "policy_sha256": result.policy_sha256,
        "source_document_id": result.source_document_id,
        "source_archive_sha256": result.source_archive_sha256,
        "cnig_profile": result.cnig_profile,
        "cnig_profile_schema_version": result.cnig_profile_schema_version,
        "cnig_profile_sha256": result.cnig_profile_sha256,
        "cnig_result_hash_schema_version": result.cnig_result_hash_schema_version,
        "cnig_complete_result_content_sha256": (
            result.cnig_complete_result_content_sha256
        ),
    }


def _policy_table_sha256(result: BessPlanningFeaturePolicyResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.bess_cnig_feature_policy.table",
            **_component_metadata(result),
            "frame": _frame_payload(result.policy_table),
        }
    )


def _complete_result_sha256(result: BessPlanningFeaturePolicyResult) -> str:
    return _canonical_json_sha256(
        {
            "domain": "landscout.bess_cnig_feature_policy.result",
            **_component_metadata(result),
            "policy_table_content_sha256": result.policy_table_content_sha256,
        }
    )


def _result_with_hashes(
    result: BessPlanningFeaturePolicyResult,
) -> BessPlanningFeaturePolicyResult:
    component = replace(
        result, policy_table_content_sha256=_policy_table_sha256(result)
    )
    return replace(
        component,
        complete_result_content_sha256=_complete_result_sha256(component),
    )


def _validate_policy_table_rows(result: BessPlanningFeaturePolicyResult) -> None:
    records: dict[tuple[str, str, str], dict[str, object]] = {}
    ordered_keys: list[tuple[str, str, str]] = []
    priority_to_status: dict[int, str] = {}
    status_to_priority: dict[str, int] = {}
    for position, row in enumerate(result.policy_table.to_dict("records")):
        family = row["feature_family"]
        type_code = row["type_code"]
        subtype_code = row["subtype_code"]
        if family not in {"PRESCRIPTION", "INFORMATION"}:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} feature family is invalid"
            )
        for value, label in (
            (type_code, "type code"),
            (subtype_code, "subtype code"),
        ):
            if not isinstance(value, str) or CODE_PATTERN.fullmatch(value) is None:
                raise BessPlanningFeaturePolicyError(
                    f"policy table row {position} {label} is invalid"
                )
        key = (family, type_code, subtype_code)
        if key in records:
            raise BessPlanningFeaturePolicyError(
                "policy table contains a duplicate code pair"
            )
        for field, label in (
            ("official_label", "official label"),
            ("rationale", "rationale"),
            ("required_human_action", "required human action"),
            ("limitations", "limitations"),
        ):
            try:
                _exact_string(row[field], f"policy row {position} {label}")
            except ValueError as error:
                raise BessPlanningFeaturePolicyError(str(error)) from error
        for field in (
            "official_legal_reference",
            "official_regulation_reference",
        ):
            value = row[field]
            if _null_value(value) is None:
                continue
            if isinstance(value, str) and value in NULL_REFERENCE_LITERALS:
                raise BessPlanningFeaturePolicyError(
                    f"{field} contains a literal null replacement"
                )
            try:
                _exact_string(value, f"policy row {position} {field}")
            except ValueError as error:
                raise BessPlanningFeaturePolicyError(str(error)) from error
        status = row["precheck_status"]
        confidence = row["confidence"]
        priority = row["status_priority"]
        if status not in ALLOWED_STATUSES:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} status is invalid"
            )
        if confidence not in ALLOWED_CONFIDENCES:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} confidence is invalid"
            )
        if type(priority) is not int or priority <= 0:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} priority is invalid"
            )
        previous_status = priority_to_status.setdefault(priority, status)
        previous_priority = status_to_priority.setdefault(status, priority)
        if previous_status != status or previous_priority != priority:
            raise BessPlanningFeaturePolicyError(
                "policy table status and priority mapping is not one-to-one"
            )
        if row["policy_scope"] != result.policy_scope:
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} scope differs from result"
            )
        for field in (
            "local_feature_text_interpreted",
            "local_regulation_content_interpreted",
            "legal_conclusion_produced",
        ):
            if row[field] is not False:
                raise BessPlanningFeaturePolicyError(
                    f"policy table row {position} {field} must be false"
                )
        if (
            row["policy_profile"] != result.policy_profile
            or row["policy_sha256"] != result.policy_sha256
            or row["cnig_profile"] != result.cnig_profile
            or row["cnig_profile_sha256"] != result.cnig_profile_sha256
            or row["cnig_complete_result_content_sha256"]
            != result.cnig_complete_result_content_sha256
        ):
            raise BessPlanningFeaturePolicyError(
                f"policy table row {position} result lineage differs"
            )
        records[key] = row
        ordered_keys.append(key)
    if ordered_keys != sorted(ordered_keys):
        raise BessPlanningFeaturePolicyError("policy table pair order is not canonical")


def _build_result(
    config: BessPlanningFeaturePolicyConfig,
    coded_result: PlanningFeatureCodeResult,
) -> BessPlanningFeaturePolicyResult:
    dictionary = _validate_policy_completeness(config, coded_result)
    policy_hash = _policy_sha256(config)
    result = BessPlanningFeaturePolicyResult(
        policy_schema_version=config.schema_version,
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        policy_profile=config.profile,
        policy_scope=config.policy_scope,
        policy_sha256=policy_hash,
        source_document_id=coded_result.source_document_id,
        source_archive_sha256=coded_result.source_archive_sha256,
        cnig_profile=coded_result.profile,
        cnig_profile_schema_version=coded_result.profile_schema_version,
        cnig_profile_sha256=coded_result.profile_sha256,
        cnig_result_hash_schema_version=coded_result.result_hash_schema_version,
        cnig_complete_result_content_sha256=(
            coded_result.complete_result_content_sha256
        ),
        policy_table_content_sha256="",
        complete_result_content_sha256="",
        policy_table=_policy_table(config, coded_result, dictionary, policy_hash),
    )
    return _result_with_hashes(result)


def _validate_result_envelope(result: BessPlanningFeaturePolicyResult) -> None:
    if type(result) is not BessPlanningFeaturePolicyResult:
        raise BessPlanningFeaturePolicyError(
            "result must be a BessPlanningFeaturePolicyResult"
        )
    for version, expected, label in (
        (result.policy_schema_version, POLICY_SCHEMA_VERSION, "policy schema"),
        (
            result.result_hash_schema_version,
            RESULT_HASH_SCHEMA_VERSION,
            "result hash schema",
        ),
        (result.cnig_profile_schema_version, 2, "CNIG profile schema"),
        (result.cnig_result_hash_schema_version, 5, "CNIG result hash schema"),
    ):
        if type(version) is not int or version != expected:
            raise BessPlanningFeaturePolicyError(f"unsupported {label} version")
    if result.policy_scope != POLICY_SCOPE:
        raise BessPlanningFeaturePolicyError("result policy scope is invalid")
    for value, label in (
        (result.policy_profile, "policy profile"),
        (result.source_document_id, "source document ID"),
        (result.cnig_profile, "CNIG profile"),
    ):
        try:
            _exact_string(value, label)
        except ValueError as error:
            raise BessPlanningFeaturePolicyError(str(error)) from error
    if not isinstance(result.policy_table, pd.DataFrame) or isinstance(
        result.policy_table, gpd.GeoDataFrame
    ):
        raise BessPlanningFeaturePolicyError("policy table must be a DataFrame")
    if (
        result.policy_table.columns.duplicated().any()
        or tuple(result.policy_table.columns) != POLICY_TABLE_COLUMNS
    ):
        raise BessPlanningFeaturePolicyError("policy table schema is invalid")
    if (
        deterministic_frame_schema_signature(result.policy_table)
        != POLICY_TABLE_SCHEMA_SIGNATURE
    ):
        raise BessPlanningFeaturePolicyError("policy table schema is invalid")
    if result.policy_table.empty:
        raise BessPlanningFeaturePolicyError(
            "policy table must contain at least one policy entry"
        )
    for field in POLICY_RESULT_SCALAR_FIELDS:
        if not field.endswith("_sha256"):
            continue
        try:
            _sha256_string(getattr(result, field), field)
        except ValueError as error:
            raise BessPlanningFeaturePolicyError(str(error)) from error
    _validate_policy_table_rows(result)
    rebuilt = _result_with_hashes(result)
    if result.policy_table_content_sha256 != rebuilt.policy_table_content_sha256:
        raise BessPlanningFeaturePolicyError("policy table hash is invalid")
    if result.complete_result_content_sha256 != rebuilt.complete_result_content_sha256:
        raise BessPlanningFeaturePolicyError("complete result hash is invalid")


def validate_bess_planning_feature_policy_result_envelope(
    result: BessPlanningFeaturePolicyResult,
) -> None:
    """Validate one compiled-policy envelope without rebuilding CNIG sources."""

    try:
        _validate_result_envelope(result)
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS planning-feature policy result envelope is invalid"
        ) from error


def load_bess_planning_feature_policy_artifacts(
    parquet_path: str | Path,
    manifest_path: str | Path,
) -> BessPlanningFeaturePolicyResult:
    """Load and locally validate one physically sealed compiled-policy artifact."""

    try:
        parquet = Path(parquet_path)
        manifest_file = Path(manifest_path)
        payload = loads_strict_json_object(manifest_file.read_bytes())
        manifest = BessPlanningFeaturePolicyArtifactManifest.model_validate(payload)
        if manifest.parquet_filename != parquet.name:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet filename differs from the supplied file"
            )
        parquet_payload = parquet.read_bytes()
        if len(parquet_payload) != manifest.parquet_size_bytes:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet size differs from the supplied file"
            )
        if sha256(parquet_payload).hexdigest() != manifest.parquet_sha256:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet SHA256 differs from the supplied file"
            )
        table = pd.read_parquet(BytesIO(parquet_payload))
        if len(table) != manifest.parquet_row_count:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest Parquet row count differs from the supplied file"
            )
        actual_schema = deterministic_frame_schema_signature(table)
        declared_schema = manifest.policy_table_schema_signature.model_dump(mode="json")
        if actual_schema != declared_schema:
            raise BessPlanningFeaturePolicyError(
                "Artifact manifest policy-table schema differs from the supplied file"
            )
        result = BessPlanningFeaturePolicyResult(
            **{name: getattr(manifest, name) for name in POLICY_RESULT_SCALAR_FIELDS},
            policy_table=table,
        )
        _validate_result_envelope(result)
        return result
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            f"BESS CNIG feature policy artifacts are invalid: {error}"
        ) from error


def _validate_coded_source(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
) -> None:
    try:
        validate_planning_feature_code_result(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
        )
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "Source-complete CNIG result validation failed"
        ) from error


def compile_bess_planning_feature_policy(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
) -> BessPlanningFeaturePolicyResult:
    """Compile the exact source-locked policy without applying it to features."""

    try:
        config = _resolved_policy_config(policy_config)
        _validate_source_lock(config, coded_result)
        _validate_coded_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
        )
        result = _build_result(config, coded_result)
        _validate_result_envelope(result)
        return result
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy compilation failed safely"
        ) from error


def validate_bess_planning_feature_policy_result(
    planning_document: GpuPlanningDocument,
    parcels: gpd.GeoDataFrame,
    surface_features: gpd.GeoDataFrame,
    line_features: gpd.GeoDataFrame,
    point_features: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    code_profile: CnigFeatureCodeProfile | str | Path,
    coded_result: PlanningFeatureCodeResult,
    policy_config: BessPlanningFeaturePolicyConfig | str | Path,
    result: BessPlanningFeaturePolicyResult,
) -> None:
    """Rebuild and validate a normalized policy from every factual source input."""

    try:
        _validate_result_envelope(result)
        config = _resolved_policy_config(policy_config)
        _validate_source_lock(config, coded_result)
        _validate_coded_source(
            planning_document,
            parcels,
            surface_features,
            line_features,
            point_features,
            relations,
            code_profile,
            coded_result,
        )
        expected = _build_result(config, coded_result)
        for field in POLICY_RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeaturePolicyError(
                    f"result {field} differs from rebuilt policy"
                )
        if _frame_payload(result.policy_table) != _frame_payload(expected.policy_table):
            raise BessPlanningFeaturePolicyError(
                "policy table differs from rebuilt policy"
            )
    except BessPlanningFeaturePolicyError:
        raise
    except Exception as error:
        raise BessPlanningFeaturePolicyError(
            "BESS CNIG feature policy result validation failed safely"
        ) from error
```
