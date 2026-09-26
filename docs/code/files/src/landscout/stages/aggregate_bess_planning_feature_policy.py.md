# `src/landscout/stages/aggregate_bess_planning_feature_policy.py`

- Source: [src/landscout/stages/aggregate_bess_planning_feature_policy.py](../../../../../../src/landscout/stages/aggregate_bess_planning_feature_policy.py)
- Source SHA256: `27bc7dcc9c67fead2c6f0638b033aab6e98282cfd2d865aec37dbf11b681c598`
- Source SHA256 basis: `git-content`
- Source lines: 1495; checkout bytes equal Git content at R8 start `fcf618ca6f569db35dd0f5b55cbca986393451ea`.
- Owner: `landscout.stages.aggregate_bess_planning_feature_policy`; semantic R8 comparison, not an independent approval.

[Paired companion](../../../../../../docs/code/files/tests/unit/test_aggregate_bess_planning_feature_policy.py.md) · [R8 evidence](../../../../../../docs/code/audit/R8_BESS_CNIG_AGGREGATION.md)

## Scope and ownership

This module aggregates already-applied BESS/CNIG feature-policy evidence to preserved parcels. It does not decide local planning compatibility, interpret local text, issue a legal conclusion, reject a parcel or calculate a score. Priority is configured policy precedence, not a parcel ranking or an area weight. Formal human review remains required even for a parcel with no relation.

The module and `landscout.stages` export exactly these six aggregation names: `BessPlanningFeatureParcelAggregationArtifactManifest`, `BessPlanningFeatureParcelAggregationError`, `BessPlanningFeatureParcelAggregationResult`, `aggregate_bess_planning_feature_policy_to_parcels`, `load_bess_planning_feature_parcel_aggregation_artifacts`, `validate_bess_planning_feature_parcel_aggregation_result`. The package has other exports; these six are its aggregation subset. `BessPlanningFeatureParcelAggregationArtifactRecord` is importable, but is absent from both public export lists. There is no public writer here. The test writer is not an application API.

Repository dependencies are the common artifact-path, BESS-application, frame-integrity, immutable-JSON, overlay-tolerance and strict-JSON contracts; GPU document types; application validation; policy and CNIG models. GeoPandas/Pandas/NumPy/Pydantic/PyProj/Shapely are third-party libraries. Standard-library dependencies handle hashing, canonical JSON, paths, numeric/time types, dataclasses and byte streams. Calls are made by the public aggregation API, its private reconstruction/loader path, package exports and the repository unit tests; no autonomous orchestrator or persisted writer is inferred from these exports.

## Decision algorithm and output facts

Before selection, the complete application-relation contract checks exact column order/dtypes/index, official and policy domains, identity/lineage/flags, unique parcel-feature pairs, intrinsic geometry-kind metrics and document-wide status/priority bijection. This includes context rows and other parcels; it is not only a check on the winning relations. SURFACE uses AREA_OVERLAP for positive area and TOUCH_ONLY for zero; LINE uses LENGTH_OVERLAP for positive length and TOUCH_ONLY for zero; POINT uses INSIDE with inside members, or BOUNDARY_TOUCH with only boundary members. Counts and unrelated metric nulls are checked upstream. No minimum positive area/length is introduced by aggregation.

Parcel geometry is validated as non-null, non-empty, valid, exactly 2D Polygon/MultiPolygon with a usable CRS and unique exact parcel IDs. Stored relation parcel area is compared with area measured on a separate EPSG:2154 calculation copy, using the technical tolerance `max(1e-6, abs(reference) * 1e-12)` with reference the larger absolute stored/measured area. Units are square metres. This is an integrity tolerance, not a BESS threshold. Output parcel CRS and geometry are not transformed. The aggregate stage itself performs no new feature intersection; source-complete upstream validation can rebuild spatial relations.

| Condition, in branch order | Aggregation state | Decision and relation effects |
| --- | --- | --- |
| Any controlling relation lacks an exact applied entry | UNRESOLVED_CONTROLLING_CODE_PAIR | Parcel status/confidence/priority all null. Unresolved controlling rows get UNRESOLVED_CONTROLLING; exact controlling rows are DEFERRED_BY_UNRESOLVED_CONTROLLING. |
| Controlling relations exist and all are exact | AGGREGATED_EXACT_POLICY | Select maximum positive configured priority and its unique status; all rows with that status AND priority are SELECTED_CONTROLLING. Other controlling rows are LOWER_PRIORITY_CONTROLLING. |
| Relations exist, all are contacts | TOUCH_ONLY_RELATIONS_ONLY | No parcel status/confidence/priority. All rows are TOUCH_ONLY_CONTEXT. |
| No relations | NO_PLANNING_FEATURE_RELATION | Parcel retained with null decision, zero counts and empty ID arrays. This is not clearance. |

Controlling types are AREA_OVERLAP, LENGTH_OVERLAP and INSIDE. Both contact types remain TOUCH_ONLY_CONTEXT in every state, including unresolved contacts beside exact controlling rows. An exact policy status UNKNOWN is still an applied decision; it is not an unresolved official code pair. For selected status/priority only, confidence is the lowest LOW/MEDIUM/HIGH rank; lower-priority and context rows cannot lower it. Ties retain every matching row, not a first winner. ID JSON is sorted, unique, compact and UTF-8-preserving, with `[]` for empty sets; relation counts count rows, not JSON members.

The 29 parcel columns and six relation columns below are appended in their declared order. All original factual columns, values, row order, index, geometry and CRS remain the copied prefix. Existing output-column collisions are rejected. All input parcels, including those without relations, remain. Relation order is restored after per-parcel grouping. Rebuilding compares complete frame payloads, not selected output columns alone. Frames remain mutable after return: frozen dataclass assignment is not deep frame immutability.

## Three trust paths, not one

1. Public builder: eleven required upstream arguments; call the application owner's source-complete validator once, build the result once, then validate its local envelope. The local envelope itself reaggregates in memory; one `_build_result` call does not mean only one `_aggregate_frames` call.
2. Public result validator: validate the supplied result envelope first; compare twelve upstream locks; call the application owner's source-complete validator once; rebuild once and compare all scalar fields and both full frames. Intrinsic failures stop before that expensive owner call.
3. Artifact loader: five required arguments (manifest path, parcel path, relation path, exact source parcels, exact application result). Validate the application envelope first, then source parcels, strict manifest JSON/model, twelve upstream locks, parcel bytes/Parquet, relation bytes/Parquet, constructed aggregation envelope, and one fresh build from the supplied upstream objects; compare all scalars and frames. It does NOT call the source-complete GPU validator or acquire an archive. Its upstream evidence is the supplied validated objects plus their envelope/identity checks, not a new physical source read.

The physical chain for paths 1/2 is aggregation → application result validator → BESS feature-policy validator → CNIG result validator → normalized planning-feature input validator → GPU extracted-layer revalidation. GPU checks document/config identity, reads related spatial files with physical FIDs, compares data/summary and file-family integrity, then the planning validator rebuilds catalogs/relations. One counted application-owner invocation is not one physical file read. This chain is not an archive download or proof that a fictitious archive path in a synthetic fixture was opened. Envelopes and source locks do not substitute for this boundary.

## Persistence, paths and immutable metadata

Result hash schema is 1, manifest schema is 1, required upstream application hash schema is 2. These are not CNIG profile/result schemas 2/5 or written-zoning schema 5. Artifact kind is BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT; scope is PARCEL_POLICY_AGGREGATION_ONLY and inherited policy scope OFFICIAL_CNIG_CODE_MEANING_ONLY.

Pydantic models forbid extra fields and field reassignment; scalar StrictStr/StrictInt/StrictBool fields reject scalar coercion. The base does not set global strict mode: iterable artifacts may validate into a tuple. Record JSON mappings are copied and recursively frozen with string keys, exact JSON leaves, tuples for sequences, finite floats only, cycle/unsupported-leaf rejection. Serializers return fresh plain JSON containers, not mutable aliases. Nullable CRS is still a required record field. Result and internal lineage dataclasses have frozen attributes, but result frames are mutable and constructors do not validate their payloads.

Records are ordered PARCELS then RELATION_ASSESSMENTS, exactly once each. Filenames are casefold-unique portable Parquet basenames: exact non-empty string, no controls, separators/absolute paths, Windows forbidden characters/reserved stems or trailing dot/space; extension comparison is case-insensitive. Counts are strict nonnegative integers, byte size strict positive integer, SHA lowercase 64 hex. Parcel record is geospatial and its non-null CRS mapping equals schema CRS; relation record is not geospatial and both CRS positions are null. The record does not independently enforce every frame-schema key: readback compares the entire measured signature.

The loader only compares each supplied `Path.name` with its record basename; it does not require the files to share the manifest directory, enforce root containment, reject symlinks or lock three files atomically. It captures each artifact once with `read_bytes`, checks size then SHA, parses that same bytes object via BytesIO, then checks row count, full frozen schema and CRS/frame type. It does not reopen the artifact path for parsing or perform a post-read path-integrity check. A replacement after capture can coexist with successful validation of captured bytes. The fileset is not promised to be an immutable or atomic filesystem snapshot. The manifest itself is parsed from captured strict JSON bytes; it has no separate external byte seal in this API.

## Canonical hash contract

Canonical JSON uses ensure_ascii=False, allow_nan=False, sort_keys=True and compact separators, then UTF-8 and SHA256. Row/index/column list ordering is preserved; only JSON object keys and ID sets are sorted. Each SHA is lowercase hexadecimal (64 characters), while persisted size_bytes is a count of bytes, not characters.

`_frame_payload` includes the entire schema signature, canonicalized index values and all rows/all columns in order. The schema includes ordered column names/dtype strings, fully qualified index class, index names/level dtypes, and for GeoDataFrames active geometry-column name plus CRS PROJJSON. Class identity here is the explicit persisted index-schema field, not an object repr. It includes prior unrelated columns and parcel geometry, even a no-relation parcel. It excludes DataFrame attrs and external filenames/paths unless represented as supported factual cells. Unsupported cells fail instead of being stringified.

Scalar normalization: None/pd.NA/scalar missing values (including NaN/NaT) become JSON null; vector missing tests are not accepted as scalar null. Geometry must be exactly 2D and becomes coordinate_dimension=2 plus little-endian 2D WKB hex without SRID (CRS is separately in schema). Dates/datetimes/Timestamps use isoformat; NumPy scalars recurse through item(); bool precedes Integral; Real becomes finite float. Infinite numbers and unsupported objects fail. In particular a schema can describe MultiIndex, but its tuple index values are unsupported by this scalar canonicalizer. This is not a universal Pandas serialization API.

Domain prefix below is a literal data string, not a Python namespace requiring a callable:

```text
landscout.bess_cnig_parcel_aggregation.
```

| Digest | Domain suffix | Exact top-level payload in addition to domain |
| --- | --- | --- |
| source_parcels_content_sha256 | source_parcels | result_hash_schema_version=1, frame=complete original parcel payload |
| source_application_relations_content_sha256 | source_application_relations | result_hash_schema_version=1, frame=complete upstream application relations |
| relation_assessments_content_sha256 | relation_assessments | every component metadata field, frame=complete output relation payload |
| parcels_content_sha256 | parcels | every component metadata field, frame=complete output parcel payload |
| complete_result_content_sha256 | result | every component metadata field, relation_assessments_content_sha256, parcels_content_sha256 |

Component metadata means every result scalar except the three output digests. Thus it includes schema/scopes/flags, source document/archive, CNIG profile/config/result, policy profile/config/result, application schema/result, and both source frame hashes. Artifact raw-byte SHAs are separate: encoding/compression changes can change them without changing canonical frame content. The local envelope drops only known appended columns into copies, checks source hashes and rebuilds output facts/hashes. A coherently altered upstream frame plus recomputed hashes is not external provenance; the public source locks and source-complete validator provide distinct checks.

## Coverage and limits

The paired test companion documents each scenario and its first possible guard. In particular its same-named loader is a test-only legacy adapter, `_LAST_*` are mutable test context, and several synthetic cases deliberately bypass physical catalog agreement. No test title alone proves the public five-argument loader reached artifact parsing. Byte-stream tests prove captured-byte parsing, not path postconditions. R8 changes documentation only; schemas/hashes, test code, configurations and real snapshots remain unchanged. Independent review and global audit remain separate from the focused run recorded in the R8 receipt.

## Module declarations

Constants/type aliases below are documented in addition to the original symbol denominator (the original AST inventory excludes module assignments). They create no extra closure credit. Signatures/values are literal source excerpts, not runtime imports.

<a id="declaration---all--"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.__all__`

Source lines 63–70. Literal six-name public aggregation export list; package reexports the same subset. Mutable module list is export metadata, not a returned trust-bearing configuration.

```python
__all__ = [
    "BessPlanningFeatureParcelAggregationArtifactManifest",
    "BessPlanningFeatureParcelAggregationError",
    "BessPlanningFeatureParcelAggregationResult",
    "aggregate_bess_planning_feature_policy_to_parcels",
    "load_bess_planning_feature_parcel_aggregation_artifacts",
    "validate_bess_planning_feature_parcel_aggregation_result",
]
```

<a id="declaration-result-hash-schema-version"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.RESULT_HASH_SCHEMA_VERSION`

Source lines 72–72. Aggregation canonical-content version1, used in source hashes and result envelopes.

```python
RESULT_HASH_SCHEMA_VERSION = 1
```

<a id="declaration-artifact-manifest-schema-version"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.ARTIFACT_MANIFEST_SCHEMA_VERSION`

Source lines 73–73. Persisted manifest version1, enforced by after-validator.

```python
ARTIFACT_MANIFEST_SCHEMA_VERSION = 1
```

<a id="declaration-application-result-hash-schema-version"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.APPLICATION_RESULT_HASH_SCHEMA_VERSION`

Source lines 74–74. Only upstream application hash schema2 is accepted; independent of aggregation/manifest versions.

```python
APPLICATION_RESULT_HASH_SCHEMA_VERSION = 2
```

<a id="declaration-aggregation-scope"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.AGGREGATION_SCOPE`

Source lines 75–75. Fixed aggregation-only scope, copied into result and parcel evidence.

```python
AGGREGATION_SCOPE = "PARCEL_POLICY_AGGREGATION_ONLY"
```

<a id="declaration-confidence-method"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.CONFIDENCE_METHOD`

Source lines 76–76. Fixed LOWEST_CONFIDENCE_FOR_SELECTED_STATUS evidence label; numeric rank is internal selection order, not confidence arithmetic.

```python
CONFIDENCE_METHOD = "LOWEST_CONFIDENCE_FOR_SELECTED_STATUS"
```

<a id="declaration-artifact-kind"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.ARTIFACT_KIND`

Source lines 77–77. Fixed aggregation artifact discriminant required by manifest.

```python
ARTIFACT_KIND = "BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"
```

<a id="declaration-controlling-relation-types"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.CONTROLLING_RELATION_TYPES`

Source lines 79–79. Immutable three-type set: positive area, positive line length or interior point evidence; no aggregation size threshold.

```python
CONTROLLING_RELATION_TYPES = frozenset({"AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"})
```

<a id="declaration-context-relation-types"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.CONTEXT_RELATION_TYPES`

Source lines 80–80. Immutable contact-only types; always contextual even when their inherited policy priority is highest.

```python
CONTEXT_RELATION_TYPES = frozenset({"TOUCH_ONLY", "BOUNDARY_TOUCH"})
```

<a id="declaration-aggregation-statuses"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.AGGREGATION_STATUSES`

Source lines 81–88. Immutable four-state domain for parcel and resulting-relation evidence; not the five precheck statuses.

```python
AGGREGATION_STATUSES = frozenset(
    {
        "AGGREGATED_EXACT_POLICY",
        "UNRESOLVED_CONTROLLING_CODE_PAIR",
        "TOUCH_ONLY_RELATIONS_ONLY",
        "NO_PLANNING_FEATURE_RELATION",
    }
)
```

<a id="declaration-relation-roles"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.RELATION_ROLES`

Source lines 89–97. Immutable five-role domain; selection boolean must be true only for SELECTED_CONTROLLING.

```python
RELATION_ROLES = frozenset(
    {
        "SELECTED_CONTROLLING",
        "LOWER_PRIORITY_CONTROLLING",
        "DEFERRED_BY_UNRESOLVED_CONTROLLING",
        "UNRESOLVED_CONTROLLING",
        "TOUCH_ONLY_CONTEXT",
    }
)
```

<a id="declaration-confidence-rank"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.CONFIDENCE_RANK`

Source lines 98–98. Module dict LOW0/MEDIUM1/HIGH2, used for minimum among selected status/priority only. It is not a deeply frozen returned policy object.

```python
CONFIDENCE_RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
```

<a id="declaration-sha-pattern"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.SHA_PATTERN`

Source lines 99–99. Compiled lowercase 64-hex expression used with fullmatch; syntax validation is not a byte-integrity proof.

```python
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")
```

<a id="declaration-parcel-columns"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.PARCEL_COLUMNS`

Source lines 101–131. Ordered29 appended parcel columns. Exact field meanings/dtypes/nulls are tabulated below and consumed by assignment, prefix extraction and validation.

```python
PARCEL_COLUMNS = (
    "bess_cnig_parcel_aggregation_status",
    "bess_cnig_parcel_precheck_status",
    "bess_cnig_parcel_precheck_confidence",
    "bess_cnig_parcel_status_priority",
    "bess_cnig_controlling_relation_count",
    "bess_cnig_exact_controlling_relation_count",
    "bess_cnig_unresolved_controlling_relation_count",
    "bess_cnig_touch_only_relation_count",
    "bess_cnig_selected_relation_count",
    "bess_cnig_lower_priority_controlling_relation_count",
    "bess_cnig_distinct_exact_status_count",
    "bess_cnig_multiple_exact_statuses",
    "bess_cnig_selected_feature_ids_json",
    "bess_cnig_unresolved_feature_ids_json",
    "bess_cnig_touch_only_feature_ids_json",
    "bess_cnig_confidence_aggregation_method",
    "bess_cnig_formal_review_required",
    "bess_cnig_aggregation_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
    "bess_cnig_application_result_sha256",
)
```

<a id="declaration-relation-columns"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.RELATION_COLUMNS`

Source lines 132–139. Ordered6 appended relation evidence columns, not the complete upstream factual relation schema. Consumed by assignment, prefix extraction and validation.

```python
RELATION_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_selected_for_parcel_status",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
    "bess_cnig_resulting_parcel_status_priority",
)
```

<a id="declaration-parcel-string-columns"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.PARCEL_STRING_COLUMNS`

Source lines 140–154. Ordered13 parcel string fields, materialized with Pandas str dtype; decision status/confidence can be missing, other evidence is reconstructed.

```python
PARCEL_STRING_COLUMNS = (
    "bess_cnig_parcel_aggregation_status",
    "bess_cnig_parcel_precheck_status",
    "bess_cnig_parcel_precheck_confidence",
    "bess_cnig_selected_feature_ids_json",
    "bess_cnig_unresolved_feature_ids_json",
    "bess_cnig_touch_only_feature_ids_json",
    "bess_cnig_confidence_aggregation_method",
    "bess_cnig_aggregation_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
    "bess_cnig_application_result_sha256",
)
```

<a id="declaration-parcel-integer-columns"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.PARCEL_INTEGER_COLUMNS`

Source lines 155–164. Ordered8 nullable Int64 fields: decision priority plus seven counters. Counters reconstruct as nonnegative values; priority null outside exact state.

```python
PARCEL_INTEGER_COLUMNS = (
    "bess_cnig_parcel_status_priority",
    "bess_cnig_controlling_relation_count",
    "bess_cnig_exact_controlling_relation_count",
    "bess_cnig_unresolved_controlling_relation_count",
    "bess_cnig_touch_only_relation_count",
    "bess_cnig_selected_relation_count",
    "bess_cnig_lower_priority_controlling_relation_count",
    "bess_cnig_distinct_exact_status_count",
)
```

<a id="declaration-parcel-bool-columns"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.PARCEL_BOOL_COLUMNS`

Source lines 165–174. Ordered8 bool columns, reconstructed without nulls. Multiple-status flag is computed; formal-review and aggregated true, other five boundary flags false.

```python
PARCEL_BOOL_COLUMNS = (
    "bess_cnig_multiple_exact_statuses",
    "bess_cnig_formal_review_required",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
)
```

<a id="declaration-relation-string-columns"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.RELATION_STRING_COLUMNS`

Source lines 175–180. Ordered4 relation str fields; resulting status/confidence null outside exact aggregation state.

```python
RELATION_STRING_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
)
```

<a id="declaration-artifactrole"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.ArtifactRole`

Source lines 182–182. Type alias of two string literals, not a Python enum or runtime classifier.

```python
ArtifactRole = Literal["PARCELS", "RELATION_ASSESSMENTS"]
```

<a id="declaration-artifact-roles"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.ARTIFACT_ROLES`

Source lines 183–183. Ordered tuple fixes PARCELS then RELATION_ASSESSMENTS; reordering is rejected.

```python
ARTIFACT_ROLES: tuple[ArtifactRole, ...] = ("PARCELS", "RELATION_ASSESSMENTS")
```

<a id="declaration-result-frame-fields"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.RESULT_FRAME_FIELDS`

Source lines 294–294. Tuple relation_assessments then parcels, used to distinguish two mutable frames from24 scalar fields.

```python
RESULT_FRAME_FIELDS = ("relation_assessments", "parcels")
```

<a id="declaration-result-scalar-fields"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.RESULT_SCALAR_FIELDS`

Source lines 295–299. Tuple derived in dataclass declaration order excluding two frame names; used for manifest reconstruction, comparisons and component metadata (which further excludes three output hashes).

```python
RESULT_SCALAR_FIELDS = tuple(
    field
    for field in BessPlanningFeatureParcelAggregationResult.__dataclass_fields__
    if field not in RESULT_FRAME_FIELDS
)
```

## Appended column dictionary

Counts are relation counts, never square metres or percentages. Only the separate stored-area integrity check uses m².

| Column (declaration order) | dtype | Meaning and null behavior |
| --- | --- | --- |
| `bess_cnig_parcel_aggregation_status` | `str` | One of four non-null aggregation states; see decision table. |
| `bess_cnig_parcel_precheck_status` | `str` | Selected inherited precheck status; null unless AGGREGATED_EXACT_POLICY. Allowed exact statuses: LIKELY_MATERIAL_CONSTRAINT, UNKNOWN, MATERIAL_REVIEW_REQUIRED, DESIGN_REVIEW_REQUIRED, CONTEXT_REVIEW_REQUIRED. |
| `bess_cnig_parcel_precheck_confidence` | `str` | Minimum LOW/MEDIUM/HIGH among exact controlling rows with selected status AND priority; null otherwise. |
| `bess_cnig_parcel_status_priority` | `Int64` | Maximum configured positive controlling priority; nullable Int64, null outside exact state. Not area weighting/score. |
| `bess_cnig_controlling_relation_count` | `Int64` | Number of AREA_OVERLAP/LENGTH_OVERLAP/INSIDE rows. |
| `bess_cnig_exact_controlling_relation_count` | `Int64` | Number of controlling APPLIED_EXACT_POLICY rows, including deferred exact rows when unresolved evidence exists. |
| `bess_cnig_unresolved_controlling_relation_count` | `Int64` | Number of controlling UNRESOLVED_CODE_PAIR rows, not exact policy UNKNOWN. |
| `bess_cnig_touch_only_relation_count` | `Int64` | Number of both contact types, regardless of inherited policy resolution. |
| `bess_cnig_selected_relation_count` | `Int64` | Count of SELECTED_CONTROLLING roles; zero when unresolved/contacts-only/no-relation. |
| `bess_cnig_lower_priority_controlling_relation_count` | `Int64` | Count of LOWER_PRIORITY_CONTROLLING roles; deferred exact rows are not counted here. |
| `bess_cnig_distinct_exact_status_count` | `Int64` | Distinct precheck statuses among all exact controlling rows, including deferred ones. |
| `bess_cnig_multiple_exact_statuses` | `bool` | True iff distinct exact controlling status count>1. |
| `bess_cnig_selected_feature_ids_json` | `str` | Sorted unique compact feature IDs only from SELECTED_CONTROLLING roles; [] when none. |
| `bess_cnig_unresolved_feature_ids_json` | `str` | Sorted unique compact feature IDs only from UNRESOLVED_CONTROLLING roles; [] when none. |
| `bess_cnig_touch_only_feature_ids_json` | `str` | Sorted unique compact feature IDs from TOUCH_ONLY_CONTEXT roles, including unresolved contacts; [] when none. |
| `bess_cnig_confidence_aggregation_method` | `str` | Non-null fixed CONFIDENCE_METHOD string even for non-decision rows. |
| `bess_cnig_formal_review_required` | `bool` | Always true; no relation is not a clearance decision. |
| `bess_cnig_aggregation_scope` | `str` | Fixed PARCEL_POLICY_AGGREGATION_ONLY. |
| `bess_cnig_policy_scope` | `str` | Fixed OFFICIAL_CNIG_CODE_MEANING_ONLY. |
| `bess_cnig_local_feature_text_interpreted` | `bool` | Always false. |
| `bess_cnig_local_regulation_content_interpreted` | `bool` | Always false. |
| `bess_cnig_legal_conclusion_produced` | `bool` | Always false. |
| `bess_cnig_parcel_status_aggregated` | `bool` | Always true. |
| `bess_cnig_parcel_rejection_performed` | `bool` | Always false. |
| `bess_cnig_score_calculated` | `bool` | Always false. |
| `bess_cnig_policy_profile` | `str` | Exact application policy profile string. |
| `bess_cnig_policy_sha256` | `str` | Exact application policy configuration hash. |
| `bess_cnig_policy_result_sha256` | `str` | Exact application policy complete-result hash. |
| `bess_cnig_application_result_sha256` | `str` | Exact application complete-result hash. |
| `bess_cnig_parcel_relation_role` | `str` | One of five non-null role strings; context priority never selects. |
| `bess_cnig_selected_for_parcel_status` | `bool` | Bool true exactly when role is SELECTED_CONTROLLING. |
| `bess_cnig_resulting_parcel_aggregation_status` | `str` | Parcel state repeated on each relation, including context. |
| `bess_cnig_resulting_parcel_precheck_status` | `str` | Parcel selected status repeated on each relation; null outside exact state. |
| `bess_cnig_resulting_parcel_precheck_confidence` | `str` | Parcel selected confidence repeated on each relation; null outside exact state. |
| `bess_cnig_resulting_parcel_status_priority` | `Int64` | Parcel selected priority repeated on each relation, nullable Int64; null outside exact state. |

## Owned symbol contracts

Each explicit anchor identifies the qualified owner in the following heading. Ranges include the definition body, not decorators. Signature excerpts are exact source text (including indentation); decorators and complete bodies are retained in the final snapshot. Field entries state the applicable parent-model boundary rather than inventing field methods or I/O.

<a id="symbol-bessplanningfeatureparcelaggregationerror"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationError`

Class, source lines 186–187.

```python
class BessPlanningFeatureParcelAggregationError(ValueError):
```

Public ValueError subclass for controlled aggregation boundary failures. Private helpers raise it directly; public builder/validator/loader preserve it and wrap other exceptions. It is not a legal decision status.

<a id="symbol--applicationlineage"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._ApplicationLineage`

Class, source lines 191–199.

```python
class _ApplicationLineage:
```

Frozen internal eight-string lineage envelope assembled from an aggregation result for local inherited-relation checks. No I/O or independent constructor validation; complete_result_content_sha256 here means the upstream APPLICATION digest, not the aggregation digest. Used only by local reconstruction.

<a id="symbol--applicationlineage-source-document-id"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._ApplicationLineage.source_document_id`

Field, source lines 192–192.

```python
source_document_id: str
```

Exact source document identifier from application result; local envelope checks string and public source locks compare it. Text alone is not physical evidence.

<a id="symbol--applicationlineage-source-archive-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._ApplicationLineage.source_archive_sha256`

Field, source lines 193–193.

```python
source_archive_sha256: str
```

Source archive identity propagated from application result; syntax and equality checked, not freshly downloaded by this module.

<a id="symbol--applicationlineage-cnig-profile"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._ApplicationLineage.cnig_profile`

Field, source lines 194–194.

```python
cnig_profile: str
```

CNIG profile identity propagated from application result; source lock and relation lineage must agree.

<a id="symbol--applicationlineage-cnig-profile-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._ApplicationLineage.cnig_profile_sha256`

Field, source lines 195–195.

```python
cnig_profile_sha256: str
```

Upstream CNIG profile canonical digest, propagated unchanged and source-locked.

<a id="symbol--applicationlineage-policy-profile"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._ApplicationLineage.policy_profile`

Field, source lines 196–196.

```python
policy_profile: str
```

Compiled BESS/CNIG policy identity, propagated from application result into result/parcel facts.

<a id="symbol--applicationlineage-policy-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._ApplicationLineage.policy_sha256`

Field, source lines 197–197.

```python
policy_sha256: str
```

Compiled policy configuration digest, propagated/source-locked; not the persisted Parquet digest.

<a id="symbol--applicationlineage-policy-complete-result-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._ApplicationLineage.policy_complete_result_content_sha256`

Field, source lines 198–198.

```python
policy_complete_result_content_sha256: str
```

Complete compiled policy result digest, propagated/source-locked and used for relation lineage.

<a id="symbol--applicationlineage-complete-result-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._ApplicationLineage.complete_result_content_sha256`

Field, source lines 199–199.

```python
complete_result_content_sha256: str
```

Hash of component metadata and both output component digests, with result domain. Internal _ApplicationLineage instead carries the upstream application digest under this field name.

<a id="symbol--strictmodel"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._StrictModel`

Class, source lines 202–203.

```python
class _StrictModel(BaseModel):
```

Internal BaseModel parent with extra=forbid and frozen=True. It does not enable global strict=True; individual Strict fields and after-validators define acceptance. Deep JSON freezing is performed by the record, not this flag alone.

<a id="symbol--exact-string"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._exact_string`

Function, source lines 206–209.

```python
def _exact_string(value: object, label: str) -> str:
```

Return the same non-empty stripped string; reject non-string, empty or surrounding whitespace with aggregation error. Does not reject textual null sentinels on its own. Used by SHA/ID/envelope guards; no mutation or I/O.

<a id="symbol--sha256-string"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._sha256_string`

Function, source lines 212–216.

```python
def _sha256_string(value: object, label: str) -> str:
```

Apply exact-string guard then fullmatch of lowercase 64-hex SHA_PATTERN; return the same string or aggregation error. Used by record, manifest and result envelope; it checks syntax, not bytes.

<a id="symbol-bessplanningfeatureparcelaggregationartifactrecord"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactRecord`

Class, source lines 219–261.

```python
class BessPlanningFeatureParcelAggregationArtifactRecord(_StrictModel):
```

Internal importable record model, not in __all__. Eight required fields describe one physical Parquet artifact. Strict scalar parsing precedes after-validation; Mapping containers are deep-copied/frozen by the record validator. No physical file is opened by construction.

<a id="symbol-bessplanningfeatureparcelaggregationartifactrecord-artifact-role"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactRecord.artifact_role`

Field, source lines 220–220.

```python
artifact_role: ArtifactRole
```

Exact PARCELS or RELATION_ASSESSMENTS role; controls geospatial/CRS checks and required manifest order.

<a id="symbol-bessplanningfeatureparcelaggregationartifactrecord-filename"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactRecord.filename`

Field, source lines 221–221.

```python
filename: StrictStr
```

Required portable local Parquet basename; casefold uniqueness is enforced across manifest records, and readback Path.name must equal it exactly.

<a id="symbol-bessplanningfeatureparcelaggregationartifactrecord-row-count"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactRecord.row_count`

Field, source lines 222–222.

```python
row_count: StrictInt
```

Strict integer >=0; checked against len(decoded frame), not feature count inferred from metadata.

<a id="symbol-bessplanningfeatureparcelaggregationartifactrecord-size-bytes"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactRecord.size_bytes`

Field, source lines 223–223.

```python
size_bytes: StrictInt
```

Strict integer >=1; exact captured artifact byte length, checked before SHA.

<a id="symbol-bessplanningfeatureparcelaggregationartifactrecord-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactRecord.sha256`

Field, source lines 224–224.

```python
sha256: StrictStr
```

Lowercase 64-hex SHA256 of captured Parquet bytes, distinct from canonical frame hashes.

<a id="symbol-bessplanningfeatureparcelaggregationartifactrecord-frame-schema-signature"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactRecord.frame_schema_signature`

Field, source lines 225–225.

```python
frame_schema_signature: Mapping[StrictStr, object]
```

Required mapping copied to recursively immutable JSON. Stores complete measured schema at readback, including index metadata and optional active geometry/CRS. Model construction alone does not enforce every schema key.

<a id="symbol-bessplanningfeatureparcelaggregationartifactrecord-geospatial"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactRecord.geospatial`

Field, source lines 226–226.

```python
geospatial: StrictBool
```

Strict bool: true for PARCELS, false for RELATION_ASSESSMENTS.

<a id="symbol-bessplanningfeatureparcelaggregationartifactrecord-crs"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactRecord.crs`

Field, source lines 227–227.

```python
crs: Mapping[StrictStr, object] | None
```

Required nullable mapping: non-null frozen CRS PROJJSON for parcels equal to schema CRS; None for relations and their schema CRS.

<a id="symbol-bessplanningfeatureparcelaggregationartifactrecord--serialize-immutable-json-mapping"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactRecord._serialize_immutable_json_mapping`

Function, source lines 230–233.

```python
    def _serialize_immutable_json_mapping(
        self, value: Mapping[str, object] | None
    ) -> object:
```

Pydantic field serializer for frame_schema_signature and crs: None remains None, otherwise recursively thaw to fresh plain JSON values. Used by model_dump/model_dump_json; callers cannot mutate retained mappings through returned dict/list containers.

<a id="symbol-bessplanningfeatureparcelaggregationartifactrecord--validate-record"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactRecord._validate_record`

Function, source lines 236–261.

```python
    def _validate_record(self) -> BessPlanningFeatureParcelAggregationArtifactRecord:
```

After-validation first recursively freezes schema/CRS and stores them via object.__setattr__, then checks portable filename, count, size, SHA, role/geospatial equivalence and CRS equality/null rules. Returns self. This controlled initialization mutation does not expose mutable metadata. Full measured schema is checked later at readback.

<a id="symbol-bessplanningfeatureparcelaggregationresult"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult`

Class, source lines 265–291.

```python
class BessPlanningFeatureParcelAggregationResult:
```

Public frozen dataclass with 24 scalar fields and two mutable frames. Plain construction/replace does not validate hashes, frames or flags. Builder and loader validate; callers that alter frame cells must pass validation again. Frozen attributes are not an immutable physical snapshot.

<a id="symbol-bessplanningfeatureparcelaggregationresult-result-hash-schema-version"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.result_hash_schema_version`

Field, source lines 266–266.

```python
result_hash_schema_version: int
```

Aggregation canonical-content schema version, exactly 1; not the upstream application version.

<a id="symbol-bessplanningfeatureparcelaggregationresult-aggregation-scope"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.aggregation_scope`

Field, source lines 267–267.

```python
aggregation_scope: str
```

Fixed PARCEL_POLICY_AGGREGATION_ONLY boundary, checked independently of policy scope.

<a id="symbol-bessplanningfeatureparcelaggregationresult-policy-scope"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.policy_scope`

Field, source lines 268–268.

```python
policy_scope: str
```

Fixed OFFICIAL_CNIG_CODE_MEANING_ONLY inherited boundary; no local-text interpretation.

<a id="symbol-bessplanningfeatureparcelaggregationresult-local-feature-text-interpreted"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.local_feature_text_interpreted`

Field, source lines 269–269.

```python
local_feature_text_interpreted: bool
```

Must be false. Raw local feature text is retained, not interpreted for authorization.

<a id="symbol-bessplanningfeatureparcelaggregationresult-local-regulation-content-interpreted"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.local_regulation_content_interpreted`

Field, source lines 270–270.

```python
local_regulation_content_interpreted: bool
```

Must be false. No local regulation interpretation is performed here.

<a id="symbol-bessplanningfeatureparcelaggregationresult-legal-conclusion-produced"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.legal_conclusion_produced`

Field, source lines 271–271.

```python
legal_conclusion_produced: bool
```

Must be false. Aggregated preliminary evidence is not a legal conclusion.

<a id="symbol-bessplanningfeatureparcelaggregationresult-parcel-status-aggregated"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.parcel_status_aggregated`

Field, source lines 272–272.

```python
parcel_status_aggregated: bool
```

Must be true, unlike the upstream application-only boundary flag.

<a id="symbol-bessplanningfeatureparcelaggregationresult-parcel-rejection-performed"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.parcel_rejection_performed`

Field, source lines 273–273.

```python
parcel_rejection_performed: bool
```

Must be false. Every source parcel is retained.

<a id="symbol-bessplanningfeatureparcelaggregationresult-score-calculated"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.score_calculated`

Field, source lines 274–274.

```python
score_calculated: bool
```

Must be false. Priority selection is not a score or ranking.

<a id="symbol-bessplanningfeatureparcelaggregationresult-source-document-id"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.source_document_id`

Field, source lines 275–275.

```python
source_document_id: str
```

Exact source document identifier from application result; local envelope checks string and public source locks compare it. Text alone is not physical evidence.

<a id="symbol-bessplanningfeatureparcelaggregationresult-source-archive-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.source_archive_sha256`

Field, source lines 276–276.

```python
source_archive_sha256: str
```

Source archive identity propagated from application result; syntax and equality checked, not freshly downloaded by this module.

<a id="symbol-bessplanningfeatureparcelaggregationresult-cnig-profile"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.cnig_profile`

Field, source lines 277–277.

```python
cnig_profile: str
```

CNIG profile identity propagated from application result; source lock and relation lineage must agree.

<a id="symbol-bessplanningfeatureparcelaggregationresult-cnig-profile-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.cnig_profile_sha256`

Field, source lines 278–278.

```python
cnig_profile_sha256: str
```

Upstream CNIG profile canonical digest, propagated unchanged and source-locked.

<a id="symbol-bessplanningfeatureparcelaggregationresult-cnig-complete-result-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.cnig_complete_result_content_sha256`

Field, source lines 279–279.

```python
cnig_complete_result_content_sha256: str
```

Complete upstream coded result digest, propagated and source-locked; not recalculated from a profile string.

<a id="symbol-bessplanningfeatureparcelaggregationresult-policy-profile"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.policy_profile`

Field, source lines 280–280.

```python
policy_profile: str
```

Compiled BESS/CNIG policy identity, propagated from application result into result/parcel facts.

<a id="symbol-bessplanningfeatureparcelaggregationresult-policy-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.policy_sha256`

Field, source lines 281–281.

```python
policy_sha256: str
```

Compiled policy configuration digest, propagated/source-locked; not the persisted Parquet digest.

<a id="symbol-bessplanningfeatureparcelaggregationresult-policy-complete-result-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.policy_complete_result_content_sha256`

Field, source lines 282–282.

```python
policy_complete_result_content_sha256: str
```

Complete compiled policy result digest, propagated/source-locked and used for relation lineage.

<a id="symbol-bessplanningfeatureparcelaggregationresult-application-result-hash-schema-version"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.application_result_hash_schema_version`

Field, source lines 283–283.

```python
application_result_hash_schema_version: int
```

Required upstream application content-hash schema exactly 2; aggregation schema remains 1.

<a id="symbol-bessplanningfeatureparcelaggregationresult-application-complete-result-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.application_complete_result_content_sha256`

Field, source lines 284–284.

```python
application_complete_result_content_sha256: str
```

Complete upstream application digest, propagated and checked against the supplied application envelope.

<a id="symbol-bessplanningfeatureparcelaggregationresult-source-parcels-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.source_parcels_content_sha256`

Field, source lines 285–285.

```python
source_parcels_content_sha256: str
```

Canonical hash of entire original parcel frame (including no-relation parcels, prior columns, index/geometry/CRS), with source_parcels domain.

<a id="symbol-bessplanningfeatureparcelaggregationresult-source-application-relations-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.source_application_relations_content_sha256`

Field, source lines 286–286.

```python
source_application_relations_content_sha256: str
```

Canonical hash of complete upstream application relation frame, ordered factual/policy prefix, with source_application_relations domain.

<a id="symbol-bessplanningfeatureparcelaggregationresult-relation-assessments-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.relation_assessments_content_sha256`

Field, source lines 287–287.

```python
relation_assessments_content_sha256: str
```

Hash of complete output relation frame plus all component metadata, with relation_assessments domain.

<a id="symbol-bessplanningfeatureparcelaggregationresult-parcels-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.parcels_content_sha256`

Field, source lines 288–288.

```python
parcels_content_sha256: str
```

Hash of complete output parcel frame plus all component metadata, with parcels domain.

<a id="symbol-bessplanningfeatureparcelaggregationresult-complete-result-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.complete_result_content_sha256`

Field, source lines 289–289.

```python
complete_result_content_sha256: str
```

Hash of component metadata and both output component digests, with result domain. Internal _ApplicationLineage instead carries the upstream application digest under this field name.

<a id="symbol-bessplanningfeatureparcelaggregationresult-relation-assessments"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.relation_assessments`

Field, source lines 290–290.

```python
relation_assessments: pd.DataFrame
```

Mutable non-geospatial DataFrame: complete upstream relation prefix plus six appended evidence columns. Public validation binds exact schema/order/index and deterministic contents.

<a id="symbol-bessplanningfeatureparcelaggregationresult-parcels"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationResult.parcels`

Field, source lines 291–291.

```python
parcels: gpd.GeoDataFrame
```

Mutable GeoDataFrame: complete supplied parcel prefix plus 29 appended evidence columns. All rows and original geometry/CRS retained; it is not a frozen data buffer.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest`

Class, source lines 302–373.

```python
class BessPlanningFeatureParcelAggregationArtifactManifest(_StrictModel):
```

Public manifest model mirrors all result scalars, adds manifest schema, artifact kind and an ordered tuple of two records; excludes frames. Model validation rejects malformed metadata before Parquet reads, but identifiers typed StrictStr are not all independently checked non-empty here. Loader/envelope enforce identity and content.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-schema-version"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.schema_version`

Field, source lines 303–303.

```python
schema_version: StrictInt
```

Manifest format version; strict integer exactly 1 after validation.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-artifact-kind"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.artifact_kind`

Field, source lines 304–304.

```python
artifact_kind: Literal["BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"]
```

Exact literal BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT, not an arbitrary serializer kind.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-result-hash-schema-version"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.result_hash_schema_version`

Field, source lines 305–305.

```python
result_hash_schema_version: StrictInt
```

Aggregation canonical-content schema version, exactly 1; not the upstream application version.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-aggregation-scope"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.aggregation_scope`

Field, source lines 306–306.

```python
aggregation_scope: Literal["PARCEL_POLICY_AGGREGATION_ONLY"]
```

Fixed PARCEL_POLICY_AGGREGATION_ONLY boundary, checked independently of policy scope.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-policy-scope"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.policy_scope`

Field, source lines 307–307.

```python
policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
```

Fixed OFFICIAL_CNIG_CODE_MEANING_ONLY inherited boundary; no local-text interpretation.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-local-feature-text-interpreted"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.local_feature_text_interpreted`

Field, source lines 308–308.

```python
local_feature_text_interpreted: StrictBool
```

Must be false. Raw local feature text is retained, not interpreted for authorization.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-local-regulation-content-interpreted"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.local_regulation_content_interpreted`

Field, source lines 309–309.

```python
local_regulation_content_interpreted: StrictBool
```

Must be false. No local regulation interpretation is performed here.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-legal-conclusion-produced"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.legal_conclusion_produced`

Field, source lines 310–310.

```python
legal_conclusion_produced: StrictBool
```

Must be false. Aggregated preliminary evidence is not a legal conclusion.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-parcel-status-aggregated"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.parcel_status_aggregated`

Field, source lines 311–311.

```python
parcel_status_aggregated: StrictBool
```

Must be true, unlike the upstream application-only boundary flag.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-parcel-rejection-performed"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.parcel_rejection_performed`

Field, source lines 312–312.

```python
parcel_rejection_performed: StrictBool
```

Must be false. Every source parcel is retained.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-score-calculated"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.score_calculated`

Field, source lines 313–313.

```python
score_calculated: StrictBool
```

Must be false. Priority selection is not a score or ranking.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-source-document-id"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.source_document_id`

Field, source lines 314–314.

```python
source_document_id: StrictStr
```

Exact source document identifier from application result; local envelope checks string and public source locks compare it. Text alone is not physical evidence.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-source-archive-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.source_archive_sha256`

Field, source lines 315–315.

```python
source_archive_sha256: StrictStr
```

Source archive identity propagated from application result; syntax and equality checked, not freshly downloaded by this module.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-cnig-profile"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.cnig_profile`

Field, source lines 316–316.

```python
cnig_profile: StrictStr
```

CNIG profile identity propagated from application result; source lock and relation lineage must agree.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-cnig-profile-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.cnig_profile_sha256`

Field, source lines 317–317.

```python
cnig_profile_sha256: StrictStr
```

Upstream CNIG profile canonical digest, propagated unchanged and source-locked.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-cnig-complete-result-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.cnig_complete_result_content_sha256`

Field, source lines 318–318.

```python
cnig_complete_result_content_sha256: StrictStr
```

Complete upstream coded result digest, propagated and source-locked; not recalculated from a profile string.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-policy-profile"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.policy_profile`

Field, source lines 319–319.

```python
policy_profile: StrictStr
```

Compiled BESS/CNIG policy identity, propagated from application result into result/parcel facts.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-policy-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.policy_sha256`

Field, source lines 320–320.

```python
policy_sha256: StrictStr
```

Compiled policy configuration digest, propagated/source-locked; not the persisted Parquet digest.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-policy-complete-result-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.policy_complete_result_content_sha256`

Field, source lines 321–321.

```python
policy_complete_result_content_sha256: StrictStr
```

Complete compiled policy result digest, propagated/source-locked and used for relation lineage.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-application-result-hash-schema-version"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.application_result_hash_schema_version`

Field, source lines 322–322.

```python
application_result_hash_schema_version: StrictInt
```

Required upstream application content-hash schema exactly 2; aggregation schema remains 1.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-application-complete-result-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.application_complete_result_content_sha256`

Field, source lines 323–323.

```python
application_complete_result_content_sha256: StrictStr
```

Complete upstream application digest, propagated and checked against the supplied application envelope.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-source-parcels-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.source_parcels_content_sha256`

Field, source lines 324–324.

```python
source_parcels_content_sha256: StrictStr
```

Canonical hash of entire original parcel frame (including no-relation parcels, prior columns, index/geometry/CRS), with source_parcels domain.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-source-application-relations-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.source_application_relations_content_sha256`

Field, source lines 325–325.

```python
source_application_relations_content_sha256: StrictStr
```

Canonical hash of complete upstream application relation frame, ordered factual/policy prefix, with source_application_relations domain.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-relation-assessments-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.relation_assessments_content_sha256`

Field, source lines 326–326.

```python
relation_assessments_content_sha256: StrictStr
```

Hash of complete output relation frame plus all component metadata, with relation_assessments domain.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-parcels-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.parcels_content_sha256`

Field, source lines 327–327.

```python
parcels_content_sha256: StrictStr
```

Hash of complete output parcel frame plus all component metadata, with parcels domain.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-complete-result-content-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.complete_result_content_sha256`

Field, source lines 328–328.

```python
complete_result_content_sha256: StrictStr
```

Hash of component metadata and both output component digests, with result domain. Internal _ApplicationLineage instead carries the upstream application digest under this field name.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest-artifacts"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest.artifacts`

Field, source lines 329–329.

```python
artifacts: tuple[BessPlanningFeatureParcelAggregationArtifactRecord, ...]
```

Immutable tuple of exactly two validated records in PARCELS, RELATION_ASSESSMENTS order, casefold-unique filenames; no frame payloads in manifest.

<a id="symbol-bessplanningfeatureparcelaggregationartifactmanifest--validate-manifest"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.BessPlanningFeatureParcelAggregationArtifactManifest._validate_manifest`

Function, source lines 332–373.

```python
    def _validate_manifest(
        self,
    ) -> BessPlanningFeatureParcelAggregationArtifactManifest:
```

After-validator checks schema/result version 1, fixed boundary flags (only parcel_status_aggregated true), every *_sha256 syntax, upstream application version 2, exact ordered roles and casefold-unique filenames. Scope/kind literals and field types were already parsed. Returns self, no I/O; nested records own filename/JSON guards.

<a id="symbol--null-value"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._null_value`

Function, source lines 376–385.

```python
def _null_value(value: object) -> object:
```

Return None for None/pd.NA or scalar bool/np.bool_ missing result from pd.isna; TypeError/ValueError or array results leave input unchanged. This normalizes nulls for hashes and domain checks, not arbitrary vector data.

<a id="symbol--canonical-value"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._canonical_value`

Function, source lines 388–423.

```python
def _canonical_value(value: object) -> object:
```

Canonicalize one cell/index value in the exact order documented above: null, geometry, temporal, NumPy scalar, bool, integral, real, string; reject unsupported or infinite values. Geometry dimension gate is exactly 2; returned dict has coordinate_dimension and wkb_hex. No repair, path lookup or lossy repr fallback.

<a id="symbol--frame-payload"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._frame_payload`

Function, source lines 426–434.

```python
def _frame_payload(frame: pd.DataFrame) -> dict[str, object]:
```

Build new schema/index/rows payload for every cell, using deterministic_frame_schema_signature and _canonical_value; preserve all order. No frame mutation or I/O. Used by hash and equality paths; invalid schemas or unsupported cells may fail.

<a id="symbol--canonical-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._canonical_sha256`

Function, source lines 437–450.

```python
def _canonical_sha256(value: object) -> str:
```

Serialize supplied JSON payload with deterministic UTF-8 options then sha256.hexdigest. TypeError/ValueError become controlled aggregation error; no arbitrary object coercion. Called by all five content digests.

<a id="symbol--frame-sha256"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._frame_sha256`

Function, source lines 453–460.

```python
def _frame_sha256(frame: pd.DataFrame, domain: str) -> str:
```

Hash domain + result_hash_schema_version=1 + complete frame payload. Used for original parcel and application-relation identities; domain is passed by callers, not inferred from file extension.

<a id="symbol--validate-feature-id"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._validate_feature_id`

Function, source lines 463–475.

```python
def _validate_feature_id(value: object) -> str:
```

Require exact string, reject NULL_LITERALS and absolute PurePosixPath/PureWindowsPath. Return original value. This is feature-ID grammar, not portable artifact-basename grammar: colon-bearing GPU IDs can be valid. All role IDs are checked, not only selected JSON IDs.

<a id="symbol--json-ids"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._json_ids`

Function, source lines 478–480.

```python
def _json_ids(values: list[object]) -> str:
```

Validate every supplied feature ID, deduplicate via set, sort lexically and dump compact ensure_ascii=False JSON. Returns string including [] for empty input, no I/O. Used for three parcel evidence lists.

<a id="symbol--validate-json-ids"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._validate_json_ids`

Function, source lines 483–504.

```python
def _validate_json_ids(value: object, label: str) -> None:
```

Require exact string, parse strict JSON, require a list, validate every ID, then require sorted unique IDs and byte-exact equality to canonical compact serialization. Null sentinel/absolute/whitespace IDs, duplicates, order or formatting differences fail. Local parcel-domain guard uses it.

<a id="symbol--validate-parcel-frame"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._validate_parcel_frame`

Function, source lines 507–555.

```python
def _validate_parcel_frame(frame: object, label: str) -> gpd.GeoDataFrame:
```

Require GeoDataFrame, no duplicate columns, parcel_id and valid active geometry/CRS; exact unique non-textual-null parcel IDs; non-null/non-empty/valid Polygon or MultiPolygon, exactly 2D. No fixed output CRS imposed. It validates existing frame, never repairs or drops rows.

<a id="symbol--validate-application-relations"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._validate_application_relations`

Function, source lines 558–580.

```python
def _validate_application_relations(
    frame: object,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> pd.DataFrame:
```

Require a non-geospatial DataFrame, then call the common complete application-relation validator with lineage from application/result envelope. Wrap TypeError/ValueError as aggregation error. This is local factual/schema/global-mapping validation, not feature-catalog or GPU reconstruction.

<a id="symbol--validate-relation-parcel-areas"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._validate_relation_parcel_areas`

Function, source lines 583–632.

```python
def _validate_relation_parcel_areas(
    parcels: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> None:
```

Create a parcel ID/geometry calculation copy preserving active geometry, project copy to EPSG:2154 if needed, require finite positive measured areas, then require every relation parcel ID and finite non-bool numeric stored area to match within technical tolerance. No thresholds or mutation of original geometry/CRS. Called before selection and on local rebuild.

<a id="symbol--validate-local-domains"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._validate_local_domains`

Function, source lines 635–711.

```python
def _validate_local_domains(parcels: gpd.GeoDataFrame, relations: pd.DataFrame) -> None:
```

Validate four parcel states, exact-state allowed status/confidence and positive integer priority, otherwise all three truly null; validate three canonical ID JSON fields. Validate relation role/selected bool and resulting state/decision domains. Exact counters, flags and cross-table agreement are checked by subsequent deterministic reconstruction, not solely by this function.

<a id="symbol--relation-priority"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._relation_priority`

Function, source lines 714–720.

```python
def _relation_priority(row: dict[str, object]) -> int:
```

Read inherited bess_cnig_status_priority, reject bool/non-Integral/nonpositive and return int. Called only for exact controlling relations; no parsing string priorities.

<a id="symbol--parcel-summary"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._parcel_summary`

Function, source lines 723–886.

```python
def _parcel_summary(
    parcel_relations: list[dict[str, object]],
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[dict[str, object], list[dict[str, object]]]:
```

Partition one parcel group into controlling/context, then exact/unresolved. Enforce per-parcel status-priority bijection; apply unresolved-first, exact-max, contacts-only, empty branches. Select every tie, take minimum confidence among selected status/priority, assign all five roles, count rows/distinct exact statuses, produce sorted ID JSON and fixed scopes/review flags. Returns parcel dict plus per-relation dicts; no I/O or frame mutation. Common document-wide mapping check occurs before this narrower per-parcel guard.

<a id="symbol--assign-columns"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._assign_columns`

Function, source lines 889–906.

```python
def _assign_columns(
    frame: pd.DataFrame, rows: list[dict[str, object]], columns: tuple[str, ...]
) -> pd.DataFrame:
```

Append supplied columns to the passed frame itself: declared integer columns pd.array(dtype=Int64), bool columns bool, remainder str. Returns that same frame. Caller _aggregate_frames supplies copies, so this private mutation is not mutation of public inputs. Nullable decision priority remains pd.NA.

<a id="symbol--aggregate-frames"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._aggregate_frames`

Function, source lines 909–965.

```python
def _aggregate_frames(
    source_parcels: gpd.GeoDataFrame,
    source_relations: pd.DataFrame,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[gpd.GeoDataFrame, pd.DataFrame]:
```

Validate parcels, inherited relations and metric areas; reject output-prefix collisions and unknown parcel IDs; group relations for every input parcel and summarize in parcel order. Copy source frames, restore original relation order via group cursors, append exact schemas with typed arrays. Returns relation assessments then parcels. Does not spatially intersect or weight areas.

<a id="symbol--component-metadata"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._component_metadata`

Function, source lines 968–980.

```python
def _component_metadata(
    result: BessPlanningFeatureParcelAggregationResult,
) -> dict[str, object]:
```

Return a fresh dict of RESULT_SCALAR_FIELDS excluding only three output content hashes. This includes both source frame hashes, all lineage/scopes/flags/versions. Used identically in both output component and complete-result payloads.

<a id="symbol--result-with-hashes"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._result_with_hashes`

Function, source lines 983–1014.

```python
def _result_with_hashes(
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

Compute relation and parcel hashes with component metadata, then whole-result hash from metadata and those two digests; return dataclass replacements. Retains frame objects, no validation or I/O. Rehashing is not source revalidation.

<a id="symbol--build-result"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._build_result`

Function, source lines 1017–1057.

```python
def _build_result(
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

Private constructor: aggregate frames, copy lineage from application result, set fixed version/scope/flags, hash complete source parcels/application relations, initialize blank output digests then _result_with_hashes. Does not call the heavy source validator. Called once explicitly by each public path; local envelope separately rebuilds frames.

<a id="symbol--compare-frame"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._compare_frame`

Function, source lines 1060–1064.

```python
def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
```

Compare full canonical frame payloads and raise aggregation error with label on mismatch. Includes factual prefix, index, dtypes, geometry/CRS; no tolerance-based equality or physical-source proof.

<a id="symbol--validate-result-envelope"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._validate_result_envelope`

Function, source lines 1067–1225.

```python
def _validate_result_envelope(
    result: BessPlanningFeatureParcelAggregationResult,
) -> None:
```

Local envelope order: result type; schema/scopes/SHA/identity/application version/flags; frame types/duplicate columns/exact output suffixes/dtypes; parcel geometry and local domains; copied factual prefixes and their source hashes; lineage/common inherited relation checks; _aggregate_frames reconstruction including measured parcel area; complete frame equality; recomputed output and result hashes. No physical GPU I/O. A stale source-prefix hash can precede the later semantic guard named by a corruption test.

<a id="symbol--validate-source-locks"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._validate_source_locks`

Function, source lines 1228–1274.

```python
def _validate_source_locks(
    result: BessPlanningFeatureParcelAggregationResult
    | BessPlanningFeatureParcelAggregationArtifactManifest,
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> None:
```

Compare twelve exact source locks: document/archive, CNIG profile/config/result, policy profile/config/result, application schema/result, actual upstream relation hash and actual original parcel hash. No file reads. Called before heavy source validation in public validator and before artifact reads in loader.

<a id="symbol--validate-application-source"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._validate_application_source`

Function, source lines 1277–1307.

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

Delegate once to application owner source-complete validator using all eleven factual/config/result inputs. Catch any upstream Exception as aggregation source-validation error. This is the only heavy entry here; delegated GPU file reads/reconstruction are not counted individually by tests.

<a id="symbol-aggregate-bess-planning-feature-policy-to-parcels"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.aggregate_bess_planning_feature_policy_to_parcels`

Function, source lines 1310–1346.

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

Public source-complete builder, eleven mandatory arguments, returns validated aggregation result. Heavy application validation → one private build → local result envelope. Re-raise owned errors; wrap any other Exception safely. Reads can occur upstream; this module does not write artifacts or mutate supplied frames.

<a id="symbol-validate-bess-planning-feature-parcel-aggregation-result"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.validate_bess_planning_feature_parcel_aggregation_result`

Function, source lines 1349–1395.

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

Public source-complete validation, eleven upstream arguments plus result, returns None. Local envelope → exact source locks → one heavy validation → one private rebuild → all scalar and both frame comparisons. Failure can precede physical reads; no output writer or repair. Owned errors preserved, others wrapped.

<a id="symbol--read-verified-artifact"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy._read_verified_artifact`

Function, source lines 1398–1443.

```python
def _read_verified_artifact(
    path: Path, record: BessPlanningFeatureParcelAggregationArtifactRecord
) -> pd.DataFrame:
```

Check Path.name equality, capture bytes once, verify size then SHA, decode BytesIO as GeoParquet/Parquet by role, then verify row count, frozen complete schema and CRS/frame kind. Each failure is controlled. It returns a mutable frame from verified captured bytes; no post-read path check, atomic set, symlink guard or external source reconstruction.

<a id="symbol-load-bess-planning-feature-parcel-aggregation-artifacts"></a>
### `landscout.stages.aggregate_bess_planning_feature_policy.load_bess_planning_feature_parcel_aggregation_artifacts`

Function, source lines 1446–1495.

```python
def load_bess_planning_feature_parcel_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
    source_parcels: gpd.GeoDataFrame,
    application_result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
```

Public loader with five mandatory inputs. Validate application envelope before even manifest read; parcel guard; strict manifest/model; upstream locks; read parcel then relation artifact; reconstruct result scalar envelope; local validation; one expected build from exact supplied objects; all scalars/two frames compare. Returns result or wrapped error. Does not call _validate_application_source, despite using source-bound hashes.

## Complete source snapshot

Exactly one full UTF-8 Git-content snapshot follows; source line endings are LF and are not rewritten. Matching this snapshot establishes bytes, not semantic prose accuracy.

```python
"""Aggregate exact BESS CNIG feature-policy relations to preserved parcels."""

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
from pathlib import Path, PurePosixPath, PureWindowsPath
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
    ALLOWED_CONFIDENCES,
    ALLOWED_PRECHECK_STATUSES,
    NULL_LITERALS,
    POLICY_SCOPE,
    validate_bess_application_relation_frame,
)
from landscout.common.frame_integrity import deterministic_frame_schema_signature
from landscout.common.immutable_mapping import (
    freeze_json_mapping,
    to_plain_json_value,
)
from landscout.common.planning_overlay import technical_overlay_tolerance
from landscout.common.strict_json import loads_strict_json, loads_strict_json_object
from landscout.sources.gpu_fr import GpuPlanningDocument
from landscout.stages.apply_bess_planning_feature_policy import (
    BessPlanningFeatureApplicationResult,
    validate_bess_planning_feature_application_result,
    validate_bess_planning_feature_application_result_envelope,
)
from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
)
from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
)

__all__ = [
    "BessPlanningFeatureParcelAggregationArtifactManifest",
    "BessPlanningFeatureParcelAggregationError",
    "BessPlanningFeatureParcelAggregationResult",
    "aggregate_bess_planning_feature_policy_to_parcels",
    "load_bess_planning_feature_parcel_aggregation_artifacts",
    "validate_bess_planning_feature_parcel_aggregation_result",
]

RESULT_HASH_SCHEMA_VERSION = 1
ARTIFACT_MANIFEST_SCHEMA_VERSION = 1
APPLICATION_RESULT_HASH_SCHEMA_VERSION = 2
AGGREGATION_SCOPE = "PARCEL_POLICY_AGGREGATION_ONLY"
CONFIDENCE_METHOD = "LOWEST_CONFIDENCE_FOR_SELECTED_STATUS"
ARTIFACT_KIND = "BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"

CONTROLLING_RELATION_TYPES = frozenset({"AREA_OVERLAP", "LENGTH_OVERLAP", "INSIDE"})
CONTEXT_RELATION_TYPES = frozenset({"TOUCH_ONLY", "BOUNDARY_TOUCH"})
AGGREGATION_STATUSES = frozenset(
    {
        "AGGREGATED_EXACT_POLICY",
        "UNRESOLVED_CONTROLLING_CODE_PAIR",
        "TOUCH_ONLY_RELATIONS_ONLY",
        "NO_PLANNING_FEATURE_RELATION",
    }
)
RELATION_ROLES = frozenset(
    {
        "SELECTED_CONTROLLING",
        "LOWER_PRIORITY_CONTROLLING",
        "DEFERRED_BY_UNRESOLVED_CONTROLLING",
        "UNRESOLVED_CONTROLLING",
        "TOUCH_ONLY_CONTEXT",
    }
)
CONFIDENCE_RANK = {"LOW": 0, "MEDIUM": 1, "HIGH": 2}
SHA_PATTERN = re.compile(r"[0-9a-f]{64}")

PARCEL_COLUMNS = (
    "bess_cnig_parcel_aggregation_status",
    "bess_cnig_parcel_precheck_status",
    "bess_cnig_parcel_precheck_confidence",
    "bess_cnig_parcel_status_priority",
    "bess_cnig_controlling_relation_count",
    "bess_cnig_exact_controlling_relation_count",
    "bess_cnig_unresolved_controlling_relation_count",
    "bess_cnig_touch_only_relation_count",
    "bess_cnig_selected_relation_count",
    "bess_cnig_lower_priority_controlling_relation_count",
    "bess_cnig_distinct_exact_status_count",
    "bess_cnig_multiple_exact_statuses",
    "bess_cnig_selected_feature_ids_json",
    "bess_cnig_unresolved_feature_ids_json",
    "bess_cnig_touch_only_feature_ids_json",
    "bess_cnig_confidence_aggregation_method",
    "bess_cnig_formal_review_required",
    "bess_cnig_aggregation_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
    "bess_cnig_application_result_sha256",
)
RELATION_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_selected_for_parcel_status",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
    "bess_cnig_resulting_parcel_status_priority",
)
PARCEL_STRING_COLUMNS = (
    "bess_cnig_parcel_aggregation_status",
    "bess_cnig_parcel_precheck_status",
    "bess_cnig_parcel_precheck_confidence",
    "bess_cnig_selected_feature_ids_json",
    "bess_cnig_unresolved_feature_ids_json",
    "bess_cnig_touch_only_feature_ids_json",
    "bess_cnig_confidence_aggregation_method",
    "bess_cnig_aggregation_scope",
    "bess_cnig_policy_scope",
    "bess_cnig_policy_profile",
    "bess_cnig_policy_sha256",
    "bess_cnig_policy_result_sha256",
    "bess_cnig_application_result_sha256",
)
PARCEL_INTEGER_COLUMNS = (
    "bess_cnig_parcel_status_priority",
    "bess_cnig_controlling_relation_count",
    "bess_cnig_exact_controlling_relation_count",
    "bess_cnig_unresolved_controlling_relation_count",
    "bess_cnig_touch_only_relation_count",
    "bess_cnig_selected_relation_count",
    "bess_cnig_lower_priority_controlling_relation_count",
    "bess_cnig_distinct_exact_status_count",
)
PARCEL_BOOL_COLUMNS = (
    "bess_cnig_multiple_exact_statuses",
    "bess_cnig_formal_review_required",
    "bess_cnig_local_feature_text_interpreted",
    "bess_cnig_local_regulation_content_interpreted",
    "bess_cnig_legal_conclusion_produced",
    "bess_cnig_parcel_status_aggregated",
    "bess_cnig_parcel_rejection_performed",
    "bess_cnig_score_calculated",
)
RELATION_STRING_COLUMNS = (
    "bess_cnig_parcel_relation_role",
    "bess_cnig_resulting_parcel_aggregation_status",
    "bess_cnig_resulting_parcel_precheck_status",
    "bess_cnig_resulting_parcel_precheck_confidence",
)

ArtifactRole = Literal["PARCELS", "RELATION_ASSESSMENTS"]
ARTIFACT_ROLES: tuple[ArtifactRole, ...] = ("PARCELS", "RELATION_ASSESSMENTS")


class BessPlanningFeatureParcelAggregationError(ValueError):
    """Raised when parcel aggregation integrity cannot be proven."""


@dataclass(frozen=True)
class _ApplicationLineage:
    source_document_id: str
    source_archive_sha256: str
    cnig_profile: str
    cnig_profile_sha256: str
    policy_profile: str
    policy_sha256: str
    policy_complete_result_content_sha256: str
    complete_result_content_sha256: str


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


class BessPlanningFeatureParcelAggregationArtifactRecord(_StrictModel):
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
    def _validate_record(self) -> BessPlanningFeatureParcelAggregationArtifactRecord:
        frozen_signature = freeze_json_mapping(self.frame_schema_signature)
        frozen_crs = freeze_json_mapping(self.crs) if self.crs is not None else None
        validate_portable_parquet_filename(self.filename, "artifact filename")
        if type(self.row_count) is not int or self.row_count < 0:
            raise ValueError("artifact row_count must be non-negative")
        if type(self.size_bytes) is not int or self.size_bytes < 1:
            raise ValueError("artifact size_bytes must be positive")
        _sha256_string(self.sha256, "artifact SHA256")
        expected_geo = self.artifact_role == "PARCELS"
        if self.geospatial is not expected_geo:
            raise ValueError("artifact geospatial flag differs from its role")
        signature_crs = frozen_signature.get("crs")
        if expected_geo:
            if frozen_crs is None or signature_crs != frozen_crs:
                raise ValueError("parcel artifact CRS is missing or inconsistent")
        elif self.crs is not None or signature_crs is not None:
            raise ValueError("relation artifact must not declare CRS")
        object.__setattr__(
            self,
            "frame_schema_signature",
            frozen_signature,
        )
        if frozen_crs is not None:
            object.__setattr__(self, "crs", frozen_crs)
        return self


@dataclass(frozen=True)
class BessPlanningFeatureParcelAggregationResult:
    result_hash_schema_version: int
    aggregation_scope: str
    policy_scope: str
    local_feature_text_interpreted: bool
    local_regulation_content_interpreted: bool
    legal_conclusion_produced: bool
    parcel_status_aggregated: bool
    parcel_rejection_performed: bool
    score_calculated: bool
    source_document_id: str
    source_archive_sha256: str
    cnig_profile: str
    cnig_profile_sha256: str
    cnig_complete_result_content_sha256: str
    policy_profile: str
    policy_sha256: str
    policy_complete_result_content_sha256: str
    application_result_hash_schema_version: int
    application_complete_result_content_sha256: str
    source_parcels_content_sha256: str
    source_application_relations_content_sha256: str
    relation_assessments_content_sha256: str
    parcels_content_sha256: str
    complete_result_content_sha256: str
    relation_assessments: pd.DataFrame
    parcels: gpd.GeoDataFrame


RESULT_FRAME_FIELDS = ("relation_assessments", "parcels")
RESULT_SCALAR_FIELDS = tuple(
    field
    for field in BessPlanningFeatureParcelAggregationResult.__dataclass_fields__
    if field not in RESULT_FRAME_FIELDS
)


class BessPlanningFeatureParcelAggregationArtifactManifest(_StrictModel):
    schema_version: StrictInt
    artifact_kind: Literal["BESS_PLANNING_FEATURE_PARCEL_AGGREGATION_RESULT"]
    result_hash_schema_version: StrictInt
    aggregation_scope: Literal["PARCEL_POLICY_AGGREGATION_ONLY"]
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    local_feature_text_interpreted: StrictBool
    local_regulation_content_interpreted: StrictBool
    legal_conclusion_produced: StrictBool
    parcel_status_aggregated: StrictBool
    parcel_rejection_performed: StrictBool
    score_calculated: StrictBool
    source_document_id: StrictStr
    source_archive_sha256: StrictStr
    cnig_profile: StrictStr
    cnig_profile_sha256: StrictStr
    cnig_complete_result_content_sha256: StrictStr
    policy_profile: StrictStr
    policy_sha256: StrictStr
    policy_complete_result_content_sha256: StrictStr
    application_result_hash_schema_version: StrictInt
    application_complete_result_content_sha256: StrictStr
    source_parcels_content_sha256: StrictStr
    source_application_relations_content_sha256: StrictStr
    relation_assessments_content_sha256: StrictStr
    parcels_content_sha256: StrictStr
    complete_result_content_sha256: StrictStr
    artifacts: tuple[BessPlanningFeatureParcelAggregationArtifactRecord, ...]

    @model_validator(mode="after")
    def _validate_manifest(
        self,
    ) -> BessPlanningFeatureParcelAggregationArtifactManifest:
        if (
            type(self.schema_version) is not int
            or self.schema_version != ARTIFACT_MANIFEST_SCHEMA_VERSION
        ):
            raise ValueError("unsupported parcel aggregation artifact schema")
        if (
            type(self.result_hash_schema_version) is not int
            or self.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("unsupported parcel aggregation result schema")
        if any(
            value is not expected
            for value, expected in (
                (self.local_feature_text_interpreted, False),
                (self.local_regulation_content_interpreted, False),
                (self.legal_conclusion_produced, False),
                (self.parcel_status_aggregated, True),
                (self.parcel_rejection_performed, False),
                (self.score_calculated, False),
            )
        ):
            raise ValueError("parcel aggregation boundary flags are invalid")
        for field in RESULT_SCALAR_FIELDS:
            value = getattr(self, field)
            if field.endswith("sha256"):
                _sha256_string(value, field)
        if (
            type(self.application_result_hash_schema_version) is not int
            or self.application_result_hash_schema_version
            != APPLICATION_RESULT_HASH_SCHEMA_VERSION
        ):
            raise ValueError("application result schema must be exactly 2")
        roles = tuple(record.artifact_role for record in self.artifacts)
        if roles != ARTIFACT_ROLES:
            raise ValueError("parcel aggregation artifact roles differ")
        filenames = tuple(record.filename.casefold() for record in self.artifacts)
        if len(filenames) != len(set(filenames)):
            raise ValueError("parcel aggregation artifact filename is duplicated")
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
        dimension = int(get_coordinate_dimension(value))
        if dimension != 2:
            raise BessPlanningFeatureParcelAggregationError(
                "Parcel aggregation geometry must be canonical 2D"
            )
        return {
            "coordinate_dimension": dimension,
            "wkb_hex": to_wkb(
                value, hex=True, output_dimension=2, byte_order=1, include_srid=False
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
            raise BessPlanningFeatureParcelAggregationError(
                "Aggregation payload contains non-finite data"
            )
        return number
    if isinstance(value, str):
        return value
    raise BessPlanningFeatureParcelAggregationError(
        f"Unsupported aggregation integrity value {type(value).__name__}"
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


def _canonical_sha256(value: object) -> str:
    try:
        payload = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation payload is not canonical JSON"
        ) from error
    return sha256(payload).hexdigest()


def _frame_sha256(frame: pd.DataFrame, domain: str) -> str:
    return _canonical_sha256(
        {
            "domain": domain,
            "result_hash_schema_version": RESULT_HASH_SCHEMA_VERSION,
            "frame": _frame_payload(frame),
        }
    )


def _validate_feature_id(value: object) -> str:
    if (
        not isinstance(value, str)
        or not value
        or value != value.strip()
        or value in NULL_LITERALS
        or PurePosixPath(value).is_absolute()
        or PureWindowsPath(value).is_absolute()
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "Feature ID is not an exact portable string"
        )
    return value


def _json_ids(values: list[object]) -> str:
    ids = sorted({_validate_feature_id(value) for value in values})
    return json.dumps(ids, ensure_ascii=False, allow_nan=False, separators=(",", ":"))


def _validate_json_ids(value: object, label: str) -> None:
    if not isinstance(value, str):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} must be canonical JSON"
        )
    try:
        parsed = loads_strict_json(value)
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} must be canonical JSON"
        ) from error
    if not isinstance(parsed, list):
        raise BessPlanningFeatureParcelAggregationError(f"{label} must be a JSON array")
    ids = [_validate_feature_id(item) for item in parsed]
    canonical = json.dumps(
        sorted(set(ids)),
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
    )
    if len(ids) != len(set(ids)) or ids != sorted(ids) or value != canonical:
        raise BessPlanningFeatureParcelAggregationError(f"{label} is not canonical")


def _validate_parcel_frame(frame: object, label: str) -> gpd.GeoDataFrame:
    if not isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} must be a GeoDataFrame"
        )
    if frame.columns.duplicated().any():
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} contains duplicate columns"
        )
    if "parcel_id" not in frame.columns:
        raise BessPlanningFeatureParcelAggregationError(f"{label} lacks parcel_id")
    try:
        geometry_name = frame.geometry.name
        if geometry_name not in frame.columns:
            raise ValueError("active geometry column is absent")
        if frame.crs is None:
            raise ValueError("CRS is absent")
        CRS.from_user_input(frame.crs)
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} geometry or CRS contract is invalid"
        ) from error
    parcel_ids = frame["parcel_id"]
    if (
        parcel_ids.isna().any()
        or parcel_ids.duplicated().any()
        or any(
            not isinstance(value, str)
            or not value
            or value != value.strip()
            or value in NULL_LITERALS
            for value in parcel_ids
        )
    ):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} parcel IDs must be unique exact strings"
        )
    for geometry in frame.geometry.array:
        if (
            geometry is None
            or geometry.is_empty
            or not geometry.is_valid
            or geometry.geom_type not in {"Polygon", "MultiPolygon"}
            or int(get_coordinate_dimension(geometry)) != 2
        ):
            raise BessPlanningFeatureParcelAggregationError(
                f"{label} requires valid canonical 2D polygon geometry"
            )
    return frame


def _validate_application_relations(
    frame: object,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> pd.DataFrame:
    if not isinstance(frame, pd.DataFrame) or isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureParcelAggregationError(
            "Application relations must be a DataFrame"
        )
    try:
        validate_bess_application_relation_frame(
            frame,
            label="application relations",
            policy_profile=application.policy_profile,
            policy_sha256=application.policy_sha256,
            policy_result_sha256=application.policy_complete_result_content_sha256,
            source_document_id=application.source_document_id,
            source_archive_sha256=application.source_archive_sha256,
            cnig_profile=application.cnig_profile,
            cnig_profile_sha256=application.cnig_profile_sha256,
        )
    except (TypeError, ValueError) as error:
        raise BessPlanningFeatureParcelAggregationError(str(error)) from error
    return frame


def _validate_relation_parcel_areas(
    parcels: gpd.GeoDataFrame,
    relations: pd.DataFrame,
) -> None:
    geometry_name = parcels.geometry.name
    calculation = gpd.GeoDataFrame(
        {"parcel_id": parcels["parcel_id"].copy(deep=True)},
        geometry=parcels.geometry.copy(deep=True),
        crs=parcels.crs,
        index=parcels.index.copy(deep=True),
    )
    try:
        if not CRS.from_user_input(calculation.crs).equals(CRS.from_epsg(2154)):
            calculation = calculation.to_crs("EPSG:2154")
        areas = calculation.geometry.area.to_numpy(dtype="float64")
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            "parcel metric-area calculation failed"
        ) from error
    if not np.isfinite(areas).all() or (areas <= 0).any():
        raise BessPlanningFeatureParcelAggregationError(
            "parcel metric areas must be finite and positive"
        )
    expected = dict(zip(calculation["parcel_id"].tolist(), areas.tolist(), strict=True))
    for parcel_id, stored in relations[
        ["parcel_id", "parcel_metric_area_m2"]
    ].itertuples(index=False, name=None):
        measured = expected.get(parcel_id)
        if measured is None:
            raise BessPlanningFeatureParcelAggregationError(
                "relation references an unknown parcel for metric area"
            )
        if isinstance(stored, bool) or not isinstance(stored, Real):
            raise BessPlanningFeatureParcelAggregationError(
                "relation parcel metric area must be numeric"
            )
        actual = float(stored)
        if not math.isfinite(actual):
            raise BessPlanningFeatureParcelAggregationError(
                "relation parcel metric area must be finite"
            )
        tolerance = technical_overlay_tolerance(max(abs(actual), measured))
        if abs(actual - measured) > tolerance:
            raise BessPlanningFeatureParcelAggregationError(
                "relation parcel metric area differs from parcel geometry"
            )
    if parcels.geometry.name != geometry_name:
        raise BessPlanningFeatureParcelAggregationError(
            "parcel active geometry changed during metric validation"
        )


def _validate_local_domains(parcels: gpd.GeoDataFrame, relations: pd.DataFrame) -> None:
    for row in parcels.to_dict("records"):
        aggregation_status = row["bess_cnig_parcel_aggregation_status"]
        if aggregation_status not in AGGREGATION_STATUSES:
            raise BessPlanningFeatureParcelAggregationError(
                "parcel aggregation status is outside the allowed domain"
            )
        status = _null_value(row["bess_cnig_parcel_precheck_status"])
        confidence = _null_value(row["bess_cnig_parcel_precheck_confidence"])
        priority = _null_value(row["bess_cnig_parcel_status_priority"])
        if aggregation_status == "AGGREGATED_EXACT_POLICY":
            if status not in ALLOWED_PRECHECK_STATUSES:
                raise BessPlanningFeatureParcelAggregationError(
                    "parcel precheck status is outside the allowed domain"
                )
            if confidence not in ALLOWED_CONFIDENCES:
                raise BessPlanningFeatureParcelAggregationError(
                    "parcel confidence is outside the allowed domain"
                )
            if (
                isinstance(priority, bool)
                or not isinstance(priority, Integral)
                or int(priority) <= 0
            ):
                raise BessPlanningFeatureParcelAggregationError(
                    "parcel status priority must be a positive integer"
                )
        elif any(value is not None for value in (status, confidence, priority)):
            raise BessPlanningFeatureParcelAggregationError(
                "non-decision parcel contains an invented decision"
            )
        for column in (
            "bess_cnig_selected_feature_ids_json",
            "bess_cnig_unresolved_feature_ids_json",
            "bess_cnig_touch_only_feature_ids_json",
        ):
            _validate_json_ids(row[column], column)
    for row in relations.to_dict("records"):
        role = row["bess_cnig_parcel_relation_role"]
        if role not in RELATION_ROLES:
            raise BessPlanningFeatureParcelAggregationError(
                "parcel relation role is outside the allowed domain"
            )
        selected = row["bess_cnig_selected_for_parcel_status"]
        if selected is not (role == "SELECTED_CONTROLLING"):
            raise BessPlanningFeatureParcelAggregationError(
                "parcel relation selected flag contradicts its role"
            )
        aggregation_status = row["bess_cnig_resulting_parcel_aggregation_status"]
        if aggregation_status not in AGGREGATION_STATUSES:
            raise BessPlanningFeatureParcelAggregationError(
                "relation aggregation status is outside the allowed domain"
            )
        status = _null_value(row["bess_cnig_resulting_parcel_precheck_status"])
        confidence = _null_value(row["bess_cnig_resulting_parcel_precheck_confidence"])
        priority = _null_value(row["bess_cnig_resulting_parcel_status_priority"])
        if aggregation_status == "AGGREGATED_EXACT_POLICY":
            if status not in ALLOWED_PRECHECK_STATUSES:
                raise BessPlanningFeatureParcelAggregationError(
                    "relation parcel status is outside the allowed domain"
                )
            if confidence not in ALLOWED_CONFIDENCES:
                raise BessPlanningFeatureParcelAggregationError(
                    "relation parcel confidence is outside the allowed domain"
                )
            if (
                isinstance(priority, bool)
                or not isinstance(priority, Integral)
                or int(priority) <= 0
            ):
                raise BessPlanningFeatureParcelAggregationError(
                    "relation parcel priority must be a positive integer"
                )
        elif any(value is not None for value in (status, confidence, priority)):
            raise BessPlanningFeatureParcelAggregationError(
                "non-decision relation contains an invented parcel decision"
            )


def _relation_priority(row: dict[str, object]) -> int:
    value = row["bess_cnig_status_priority"]
    if isinstance(value, bool) or not isinstance(value, Integral) or int(value) <= 0:
        raise BessPlanningFeatureParcelAggregationError(
            "Applied relation priority must be a positive integer"
        )
    return int(value)


def _parcel_summary(
    parcel_relations: list[dict[str, object]],
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[dict[str, object], list[dict[str, object]]]:
    controlling = [
        row
        for row in parcel_relations
        if row["relation_type"] in CONTROLLING_RELATION_TYPES
    ]
    contextual = [
        row
        for row in parcel_relations
        if row["relation_type"] in CONTEXT_RELATION_TYPES
    ]
    if len(controlling) + len(contextual) != len(parcel_relations):
        raise BessPlanningFeatureParcelAggregationError(
            "Relation type is outside the aggregation contract"
        )
    exact = [
        row
        for row in controlling
        if row["bess_cnig_policy_application_status"] == "APPLIED_EXACT_POLICY"
    ]
    unresolved = [
        row
        for row in controlling
        if row["bess_cnig_policy_application_status"] == "UNRESOLVED_CODE_PAIR"
    ]
    if len(exact) + len(unresolved) != len(controlling):
        raise BessPlanningFeatureParcelAggregationError(
            "Controlling application status is invalid"
        )
    selected_status: str | None = None
    selected_confidence: str | None = None
    selected_priority: int | None = None
    priorities: list[int] = []
    priority_statuses: dict[int, set[str]] = {}
    status_priorities: dict[str, set[int]] = {}
    for row in exact:
        priority = row["bess_cnig_status_priority"]
        status = row["bess_cnig_precheck_status"]
        if (
            isinstance(priority, bool)
            or not isinstance(priority, Integral)
            or int(priority) <= 0
            or not isinstance(status, str)
        ):
            raise BessPlanningFeatureParcelAggregationError(
                "Applied relation status and priority are invalid"
            )
        normalized_priority = int(priority)
        priorities.append(normalized_priority)
        priority_statuses.setdefault(normalized_priority, set()).add(status)
        status_priorities.setdefault(status, set()).add(normalized_priority)
    if any(len(statuses) != 1 for statuses in priority_statuses.values()) or any(
        len(priority_values) != 1 for priority_values in status_priorities.values()
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "Applied relation status and priority mapping is not one-to-one"
        )
    if unresolved:
        aggregation_status = "UNRESOLVED_CONTROLLING_CODE_PAIR"
    elif controlling:
        aggregation_status = "AGGREGATED_EXACT_POLICY"
        selected_priority = max(priorities)
        selected_status = next(iter(priority_statuses[selected_priority]))
        confidences = [
            str(row["bess_cnig_precheck_confidence"])
            for row in exact
            if row["bess_cnig_precheck_status"] == selected_status
            and _relation_priority(row) == selected_priority
        ]
        if any(value not in CONFIDENCE_RANK for value in confidences):
            raise BessPlanningFeatureParcelAggregationError(
                "Selected relation confidence is invalid"
            )
        selected_confidence = min(confidences, key=CONFIDENCE_RANK.__getitem__)
    elif parcel_relations:
        aggregation_status = "TOUCH_ONLY_RELATIONS_ONLY"
    else:
        aggregation_status = "NO_PLANNING_FEATURE_RELATION"

    assessed: list[dict[str, object]] = []
    for row in parcel_relations:
        if row["relation_type"] in CONTEXT_RELATION_TYPES:
            role = "TOUCH_ONLY_CONTEXT"
        elif aggregation_status == "UNRESOLVED_CONTROLLING_CODE_PAIR":
            role = (
                "UNRESOLVED_CONTROLLING"
                if row["bess_cnig_policy_application_status"] == "UNRESOLVED_CODE_PAIR"
                else "DEFERRED_BY_UNRESOLVED_CONTROLLING"
            )
        else:
            role = (
                "SELECTED_CONTROLLING"
                if row["bess_cnig_precheck_status"] == selected_status
                and _relation_priority(row) == selected_priority
                else "LOWER_PRIORITY_CONTROLLING"
            )
        assessed.append(
            {
                **row,
                "bess_cnig_parcel_relation_role": role,
                "bess_cnig_selected_for_parcel_status": role == "SELECTED_CONTROLLING",
                "bess_cnig_resulting_parcel_aggregation_status": aggregation_status,
                "bess_cnig_resulting_parcel_precheck_status": selected_status,
                "bess_cnig_resulting_parcel_precheck_confidence": selected_confidence,
                "bess_cnig_resulting_parcel_status_priority": selected_priority,
            }
        )
    roles = [row["bess_cnig_parcel_relation_role"] for row in assessed]
    exact_statuses = {str(row["bess_cnig_precheck_status"]) for row in exact}
    summary: dict[str, object] = {
        "bess_cnig_parcel_aggregation_status": aggregation_status,
        "bess_cnig_parcel_precheck_status": selected_status,
        "bess_cnig_parcel_precheck_confidence": selected_confidence,
        "bess_cnig_parcel_status_priority": selected_priority,
        "bess_cnig_controlling_relation_count": len(controlling),
        "bess_cnig_exact_controlling_relation_count": len(exact),
        "bess_cnig_unresolved_controlling_relation_count": len(unresolved),
        "bess_cnig_touch_only_relation_count": len(contextual),
        "bess_cnig_selected_relation_count": roles.count("SELECTED_CONTROLLING"),
        "bess_cnig_lower_priority_controlling_relation_count": roles.count(
            "LOWER_PRIORITY_CONTROLLING"
        ),
        "bess_cnig_distinct_exact_status_count": len(exact_statuses),
        "bess_cnig_multiple_exact_statuses": len(exact_statuses) > 1,
        "bess_cnig_selected_feature_ids_json": _json_ids(
            [
                row["planning_feature_id"]
                for row in assessed
                if row["bess_cnig_parcel_relation_role"] == "SELECTED_CONTROLLING"
            ]
        ),
        "bess_cnig_unresolved_feature_ids_json": _json_ids(
            [
                row["planning_feature_id"]
                for row in assessed
                if row["bess_cnig_parcel_relation_role"] == "UNRESOLVED_CONTROLLING"
            ]
        ),
        "bess_cnig_touch_only_feature_ids_json": _json_ids(
            [
                row["planning_feature_id"]
                for row in assessed
                if row["bess_cnig_parcel_relation_role"] == "TOUCH_ONLY_CONTEXT"
            ]
        ),
        "bess_cnig_confidence_aggregation_method": CONFIDENCE_METHOD,
        "bess_cnig_formal_review_required": True,
        "bess_cnig_aggregation_scope": AGGREGATION_SCOPE,
        "bess_cnig_policy_scope": POLICY_SCOPE,
        "bess_cnig_local_feature_text_interpreted": False,
        "bess_cnig_local_regulation_content_interpreted": False,
        "bess_cnig_legal_conclusion_produced": False,
        "bess_cnig_parcel_status_aggregated": True,
        "bess_cnig_parcel_rejection_performed": False,
        "bess_cnig_score_calculated": False,
        "bess_cnig_policy_profile": application.policy_profile,
        "bess_cnig_policy_sha256": application.policy_sha256,
        "bess_cnig_policy_result_sha256": application.policy_complete_result_content_sha256,
        "bess_cnig_application_result_sha256": application.complete_result_content_sha256,
    }
    return summary, assessed


def _assign_columns(
    frame: pd.DataFrame, rows: list[dict[str, object]], columns: tuple[str, ...]
) -> pd.DataFrame:
    for column in columns:
        values = [row[column] for row in rows]
        if (
            column in PARCEL_INTEGER_COLUMNS
            or column == "bess_cnig_resulting_parcel_status_priority"
        ):
            frame[column] = pd.array(values, dtype="Int64")
        elif (
            column in PARCEL_BOOL_COLUMNS
            or column == "bess_cnig_selected_for_parcel_status"
        ):
            frame[column] = pd.array(values, dtype="bool")
        else:
            frame[column] = pd.array(values, dtype="str")
    return frame


def _aggregate_frames(
    source_parcels: gpd.GeoDataFrame,
    source_relations: pd.DataFrame,
    application: BessPlanningFeatureApplicationResult | _ApplicationLineage,
) -> tuple[gpd.GeoDataFrame, pd.DataFrame]:
    _validate_parcel_frame(source_parcels, "source parcels")
    _validate_application_relations(source_relations, application)
    _validate_relation_parcel_areas(source_parcels, source_relations)
    if any(column in source_parcels.columns for column in PARCEL_COLUMNS) or any(
        column in source_relations.columns for column in RELATION_COLUMNS
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation columns already exist on source inputs"
        )
    if "parcel_id" not in source_parcels or "parcel_id" not in source_relations:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation inputs lack parcel_id"
        )
    parcel_ids = source_parcels["parcel_id"]
    known = set(parcel_ids.tolist())
    if any(value not in known for value in source_relations["parcel_id"]):
        raise BessPlanningFeatureParcelAggregationError(
            "Relation references an unknown parcel"
        )
    relation_rows = source_relations.to_dict("records")
    grouped: dict[str, list[dict[str, object]]] = {
        value: [] for value in parcel_ids.tolist()
    }
    for row in relation_rows:
        grouped[str(row["parcel_id"])].append(row)
    summaries: list[dict[str, object]] = []
    assessment_rows: list[dict[str, object]] = []
    for parcel_id in parcel_ids.tolist():
        summary, assessed = _parcel_summary(grouped[parcel_id], application)
        summaries.append(summary)
        assessment_rows.extend(assessed)
    parcels = source_parcels.copy(deep=True)
    _assign_columns(parcels, summaries, PARCEL_COLUMNS)
    parcels = gpd.GeoDataFrame(
        parcels, geometry=source_parcels.geometry.name, crs=source_parcels.crs
    )
    assessments = source_relations.copy(deep=True)
    # assessed rows were grouped by parcel; restore exact source relation order by stable source position.
    cursor: dict[str, int] = {parcel_id: 0 for parcel_id in grouped}
    assessed_by_parcel: dict[str, list[dict[str, object]]] = {
        parcel_id: [] for parcel_id in grouped
    }
    for row in assessment_rows:
        assessed_by_parcel[str(row["parcel_id"])].append(row)
    ordered_assessed: list[dict[str, object]] = []
    for source_row in relation_rows:
        parcel_id = str(source_row["parcel_id"])
        item = assessed_by_parcel[parcel_id][cursor[parcel_id]]
        cursor[parcel_id] += 1
        ordered_assessed.append(item)
    _assign_columns(assessments, ordered_assessed, RELATION_COLUMNS)
    return parcels, assessments


def _component_metadata(
    result: BessPlanningFeatureParcelAggregationResult,
) -> dict[str, object]:
    return {
        field: getattr(result, field)
        for field in RESULT_SCALAR_FIELDS
        if field
        not in {
            "relation_assessments_content_sha256",
            "parcels_content_sha256",
            "complete_result_content_sha256",
        }
    }


def _result_with_hashes(
    result: BessPlanningFeatureParcelAggregationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    metadata = _component_metadata(result)
    relations_hash = _canonical_sha256(
        {
            "domain": "landscout.bess_cnig_parcel_aggregation.relation_assessments",
            **metadata,
            "frame": _frame_payload(result.relation_assessments),
        }
    )
    parcels_hash = _canonical_sha256(
        {
            "domain": "landscout.bess_cnig_parcel_aggregation.parcels",
            **metadata,
            "frame": _frame_payload(result.parcels),
        }
    )
    components = replace(
        result,
        relation_assessments_content_sha256=relations_hash,
        parcels_content_sha256=parcels_hash,
    )
    complete = _canonical_sha256(
        {
            "domain": "landscout.bess_cnig_parcel_aggregation.result",
            **metadata,
            "relation_assessments_content_sha256": relations_hash,
            "parcels_content_sha256": parcels_hash,
        }
    )
    return replace(components, complete_result_content_sha256=complete)


def _build_result(
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    parcels, assessments = _aggregate_frames(
        source_parcels, application.relations, application
    )
    result = BessPlanningFeatureParcelAggregationResult(
        result_hash_schema_version=RESULT_HASH_SCHEMA_VERSION,
        aggregation_scope=AGGREGATION_SCOPE,
        policy_scope=POLICY_SCOPE,
        local_feature_text_interpreted=False,
        local_regulation_content_interpreted=False,
        legal_conclusion_produced=False,
        parcel_status_aggregated=True,
        parcel_rejection_performed=False,
        score_calculated=False,
        source_document_id=application.source_document_id,
        source_archive_sha256=application.source_archive_sha256,
        cnig_profile=application.cnig_profile,
        cnig_profile_sha256=application.cnig_profile_sha256,
        cnig_complete_result_content_sha256=application.cnig_complete_result_content_sha256,
        policy_profile=application.policy_profile,
        policy_sha256=application.policy_sha256,
        policy_complete_result_content_sha256=application.policy_complete_result_content_sha256,
        application_result_hash_schema_version=application.result_hash_schema_version,
        application_complete_result_content_sha256=application.complete_result_content_sha256,
        source_parcels_content_sha256=_frame_sha256(
            source_parcels, "landscout.bess_cnig_parcel_aggregation.source_parcels"
        ),
        source_application_relations_content_sha256=_frame_sha256(
            application.relations,
            "landscout.bess_cnig_parcel_aggregation.source_application_relations",
        ),
        relation_assessments_content_sha256="",
        parcels_content_sha256="",
        complete_result_content_sha256="",
        relation_assessments=assessments,
        parcels=parcels,
    )
    return _result_with_hashes(result)


def _compare_frame(actual: pd.DataFrame, expected: pd.DataFrame, label: str) -> None:
    if _frame_payload(actual) != _frame_payload(expected):
        raise BessPlanningFeatureParcelAggregationError(
            f"{label} differs from deterministic aggregation"
        )


def _validate_result_envelope(
    result: BessPlanningFeatureParcelAggregationResult,
) -> None:
    if not isinstance(result, BessPlanningFeatureParcelAggregationResult):
        raise BessPlanningFeatureParcelAggregationError("result has the wrong type")
    if (
        type(result.result_hash_schema_version) is not int
        or result.result_hash_schema_version != RESULT_HASH_SCHEMA_VERSION
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "unsupported parcel aggregation result schema"
        )
    if (
        result.aggregation_scope != AGGREGATION_SCOPE
        or result.policy_scope != POLICY_SCOPE
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "parcel aggregation scope is invalid"
        )
    for field in RESULT_SCALAR_FIELDS:
        if field.endswith("sha256"):
            try:
                _sha256_string(getattr(result, field), field)
            except ValueError as error:
                raise BessPlanningFeatureParcelAggregationError(str(error)) from error
    for value, label in (
        (result.source_document_id, "source_document_id"),
        (result.cnig_profile, "cnig_profile"),
        (result.policy_profile, "policy_profile"),
    ):
        try:
            _exact_string(value, label)
        except ValueError as error:
            raise BessPlanningFeatureParcelAggregationError(str(error)) from error
    if (
        type(result.application_result_hash_schema_version) is not int
        or result.application_result_hash_schema_version
        != APPLICATION_RESULT_HASH_SCHEMA_VERSION
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "application result schema must be exactly 2"
        )
    if any(
        value is not expected
        for value, expected in (
            (result.local_feature_text_interpreted, False),
            (result.local_regulation_content_interpreted, False),
            (result.legal_conclusion_produced, False),
            (result.parcel_status_aggregated, True),
            (result.parcel_rejection_performed, False),
            (result.score_calculated, False),
        )
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "parcel aggregation flags are invalid"
        )
    if (
        not isinstance(result.parcels, gpd.GeoDataFrame)
        or not isinstance(result.relation_assessments, pd.DataFrame)
        or isinstance(result.relation_assessments, gpd.GeoDataFrame)
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "aggregation output frame types are invalid"
        )
    if result.parcels.columns.duplicated().any():
        raise BessPlanningFeatureParcelAggregationError(
            "parcel output contains duplicate columns"
        )
    if result.relation_assessments.columns.duplicated().any():
        raise BessPlanningFeatureParcelAggregationError(
            "relation assessments contain duplicate columns"
        )
    if (
        tuple(result.parcels.columns[-len(PARCEL_COLUMNS) :]) != PARCEL_COLUMNS
        or tuple(result.relation_assessments.columns[-len(RELATION_COLUMNS) :])
        != RELATION_COLUMNS
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "aggregation output suffix schema is invalid"
        )
    for column in PARCEL_STRING_COLUMNS:
        if str(result.parcels[column].dtype) != "str":
            raise BessPlanningFeatureParcelAggregationError(
                "parcel aggregation string dtype is invalid"
            )
    for column in PARCEL_INTEGER_COLUMNS:
        if str(result.parcels[column].dtype) != "Int64":
            raise BessPlanningFeatureParcelAggregationError(
                "parcel aggregation integer dtype is invalid"
            )
    for column in PARCEL_BOOL_COLUMNS:
        if str(result.parcels[column].dtype) != "bool":
            raise BessPlanningFeatureParcelAggregationError(
                "parcel aggregation bool dtype is invalid"
            )
    for column in RELATION_STRING_COLUMNS:
        if str(result.relation_assessments[column].dtype) != "str":
            raise BessPlanningFeatureParcelAggregationError(
                "relation assessment string dtype is invalid"
            )
    if (
        str(result.relation_assessments["bess_cnig_selected_for_parcel_status"].dtype)
        != "bool"
        or str(
            result.relation_assessments[
                "bess_cnig_resulting_parcel_status_priority"
            ].dtype
        )
        != "Int64"
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "relation assessment dtype is invalid"
        )
    _validate_parcel_frame(result.parcels, "parcel output")
    _validate_local_domains(result.parcels, result.relation_assessments)
    source_parcels = result.parcels.drop(columns=list(PARCEL_COLUMNS))
    source_parcels = gpd.GeoDataFrame(
        source_parcels, geometry=result.parcels.geometry.name, crs=result.parcels.crs
    )
    source_relations = result.relation_assessments.drop(columns=list(RELATION_COLUMNS))
    if result.source_parcels_content_sha256 != _frame_sha256(
        source_parcels, "landscout.bess_cnig_parcel_aggregation.source_parcels"
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "source parcel content SHA256 is invalid"
        )
    if result.source_application_relations_content_sha256 != _frame_sha256(
        source_relations,
        "landscout.bess_cnig_parcel_aggregation.source_application_relations",
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "source application relation content SHA256 is invalid"
        )
    lineage = _ApplicationLineage(
        source_document_id=result.source_document_id,
        source_archive_sha256=result.source_archive_sha256,
        cnig_profile=result.cnig_profile,
        cnig_profile_sha256=result.cnig_profile_sha256,
        policy_profile=result.policy_profile,
        policy_sha256=result.policy_sha256,
        policy_complete_result_content_sha256=result.policy_complete_result_content_sha256,
        complete_result_content_sha256=result.application_complete_result_content_sha256,
    )
    _validate_application_relations(source_relations, lineage)
    expected_parcels, expected_relations = _aggregate_frames(
        source_parcels, source_relations, lineage
    )
    _compare_frame(result.parcels, expected_parcels, "parcel output")
    _compare_frame(
        result.relation_assessments, expected_relations, "relation assessments"
    )
    rebuilt = _result_with_hashes(result)
    for field in (
        "relation_assessments_content_sha256",
        "parcels_content_sha256",
        "complete_result_content_sha256",
    ):
        if getattr(result, field) != getattr(rebuilt, field):
            raise BessPlanningFeatureParcelAggregationError(f"{field} is invalid")


def _validate_source_locks(
    result: BessPlanningFeatureParcelAggregationResult
    | BessPlanningFeatureParcelAggregationArtifactManifest,
    source_parcels: gpd.GeoDataFrame,
    application: BessPlanningFeatureApplicationResult,
) -> None:
    comparisons = (
        (result.source_document_id, application.source_document_id),
        (result.source_archive_sha256, application.source_archive_sha256),
        (result.cnig_profile, application.cnig_profile),
        (result.cnig_profile_sha256, application.cnig_profile_sha256),
        (
            result.cnig_complete_result_content_sha256,
            application.cnig_complete_result_content_sha256,
        ),
        (result.policy_profile, application.policy_profile),
        (result.policy_sha256, application.policy_sha256),
        (
            result.policy_complete_result_content_sha256,
            application.policy_complete_result_content_sha256,
        ),
        (
            result.application_result_hash_schema_version,
            application.result_hash_schema_version,
        ),
        (
            result.application_complete_result_content_sha256,
            application.complete_result_content_sha256,
        ),
        (
            result.source_application_relations_content_sha256,
            _frame_sha256(
                application.relations,
                "landscout.bess_cnig_parcel_aggregation.source_application_relations",
            ),
        ),
        (
            result.source_parcels_content_sha256,
            _frame_sha256(
                source_parcels, "landscout.bess_cnig_parcel_aggregation.source_parcels"
            ),
        ),
    )
    if any(actual != expected for actual, expected in comparisons):
        raise BessPlanningFeatureParcelAggregationError(
            "parcel aggregation source lock differs"
        )


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
    try:
        validate_bess_planning_feature_application_result(
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
            application_result,
        )
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            "Source-complete application validation failed"
        ) from error


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
    """Validate the application once and aggregate its relations to every parcel."""
    try:
        _validate_application_source(
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
            application_result,
        )
        result = _build_result(parcels, application_result)
        _validate_result_envelope(result)
        return result
    except BessPlanningFeatureParcelAggregationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            "Parcel aggregation failed safely"
        ) from error


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
    """Independently validate and rebuild one persisted parcel aggregation result."""
    try:
        _validate_result_envelope(result)
        _validate_source_locks(result, parcels, application_result)
        _validate_application_source(
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
            application_result,
        )
        expected = _build_result(parcels, application_result)
        for field in RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeatureParcelAggregationError(
                    f"Aggregation {field} differs"
                )
        _compare_frame(result.parcels, expected.parcels, "parcels")
        _compare_frame(
            result.relation_assessments, expected.relation_assessments, "relations"
        )
    except BessPlanningFeatureParcelAggregationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            "Parcel aggregation result validation failed safely"
        ) from error


def _read_verified_artifact(
    path: Path, record: BessPlanningFeatureParcelAggregationArtifactRecord
) -> pd.DataFrame:
    if path.name != record.filename:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact filename differs"
        )
    payload = path.read_bytes()
    if len(payload) != record.size_bytes:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact byte size differs"
        )
    if sha256(payload).hexdigest() != record.sha256:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact SHA256 differs"
        )
    buffer = BytesIO(payload)
    frame: pd.DataFrame = (
        gpd.read_parquet(buffer) if record.geospatial else pd.read_parquet(buffer)
    )
    if len(frame) != record.row_count:
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact row count differs"
        )
    if (
        freeze_json_mapping(deterministic_frame_schema_signature(frame))
        != record.frame_schema_signature
    ):
        raise BessPlanningFeatureParcelAggregationError(
            "Aggregation artifact frame schema differs"
        )
    if record.geospatial:
        if (
            not isinstance(frame, gpd.GeoDataFrame)
            or frame.crs is None
            or freeze_json_mapping(CRS.from_user_input(frame.crs).to_json_dict())
            != record.crs
        ):
            raise BessPlanningFeatureParcelAggregationError(
                "Aggregation parcel artifact CRS differs"
            )
    elif isinstance(frame, gpd.GeoDataFrame):
        raise BessPlanningFeatureParcelAggregationError(
            "Relation assessment artifact is unexpectedly geospatial"
        )
    return frame


def load_bess_planning_feature_parcel_aggregation_artifacts(
    manifest_path: str | Path,
    parcels_path: str | Path,
    relation_assessments_path: str | Path,
    source_parcels: gpd.GeoDataFrame,
    application_result: BessPlanningFeatureApplicationResult,
) -> BessPlanningFeatureParcelAggregationResult:
    """Load byte-sealed outputs and bind them to exact lightweight upstreams."""
    try:
        validate_bess_planning_feature_application_result_envelope(application_result)
        _validate_parcel_frame(source_parcels, "source parcels")
        payload = loads_strict_json_object(Path(manifest_path).read_bytes())
        manifest = BessPlanningFeatureParcelAggregationArtifactManifest.model_validate(
            payload
        )
        _validate_source_locks(manifest, source_parcels, application_result)
        records = {record.artifact_role: record for record in manifest.artifacts}
        loaded_parcels = _read_verified_artifact(Path(parcels_path), records["PARCELS"])
        loaded_relations = _read_verified_artifact(
            Path(relation_assessments_path), records["RELATION_ASSESSMENTS"]
        )
        if not isinstance(loaded_parcels, gpd.GeoDataFrame):
            raise BessPlanningFeatureParcelAggregationError(
                "Parcel artifact is not geospatial"
            )
        result = BessPlanningFeatureParcelAggregationResult(
            **{field: getattr(manifest, field) for field in RESULT_SCALAR_FIELDS},
            parcels=loaded_parcels,
            relation_assessments=loaded_relations,
        )
        _validate_result_envelope(result)
        expected = _build_result(source_parcels, application_result)
        for field in RESULT_SCALAR_FIELDS:
            if getattr(result, field) != getattr(expected, field):
                raise BessPlanningFeatureParcelAggregationError(
                    f"Aggregation artifact scalar {field} differs from upstream rebuild"
                )
        for field in RESULT_FRAME_FIELDS:
            _compare_frame(
                getattr(result, field),
                getattr(expected, field),
                f"artifact {field}",
            )
        return result
    except BessPlanningFeatureParcelAggregationError:
        raise
    except Exception as error:
        raise BessPlanningFeatureParcelAggregationError(
            f"Parcel aggregation artifacts are invalid: {error}"
        ) from error
```
