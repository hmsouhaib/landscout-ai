# `src/landscout/stages/interpret_bess_zoning.py`

- Source: [src/landscout/stages/interpret_bess_zoning.py](../../../../../../src/landscout/stages/interpret_bess_zoning.py)
- Source SHA256: `b60434426a981dab3dcd000a4fc9e745202984672f8e96bc4ea8aa661c86682e`
- Source SHA256 basis: `git-content`
- Source lines: 2394; Git blob at R11 start: `4b1dc0ee036f2c318c1a56db8c2b5ff883ca85cc`

Git/index/checkout Python bytes remain unchanged. Local semantic closure is not independent approval. [R11 receipt](../../../../../../docs/code/audit/R11_BESS_WRITTEN_ZONING.md).

## Scope and ownership

This interpreter applies a source-locked written-zoning assessment to validated factual chapter/zone/parcel relations. It DOES produce parcel precheck statuses, unlike the CNIG compiler. It does not issue legal permission/refusal, reject parcels, score/rank, establish BESS/ICPE applicability, or interpret non-zoning planning features. Formal review remains required for every parcel. Policy schema and result hash schema are both 5; scope is WRITTEN_ZONING_REGULATION_ONLY and review_scope CONFIGURED_USE_CONTROL_ARTICLES_ONLY.

Six declared exports are also imported and listed in `landscout.stages`: `BessZoningPolicyConfig`, `BessZoningPrecheckError`, `BessZoningPrecheckResult`, `interpret_bess_zoning`, `load_bess_zoning_policy_config`, `validate_bess_zoning_precheck`. Direct importability of other classes/helpers is not an additional public export guarantee. There is no manifest, public envelope-only validator, artifact loader or writer in this module.

Repository owners are [GPU](../sources/gpu_fr.py.md), [normalized zoning](enrich_planning_zoning.py.md), [index](index_planning_regulation.py.md), [structure/fragments](structure_planning_regulation.py.md), [strict YAML](../common/strict_yaml.py.md). The actual tolerance import is [stages.planning_overlay](planning_overlay.py.md), a compatibility reexport from [common.planning_overlay](../common/planning_overlay.py.md), not an invented direct import. [R6](../../../../audit/R6_BESS_WRITTEN_ZONING_POLICY.md) supplies bounded checked-in YAML context; its independent approval is not an audit of this interpreter. [Tests](../../../tests/unit/test_interpret_bess_zoning.py.md) use a bypassed GPU guard and synthetic extracted index.

Standard-library imports own JSON/SHA, numeric/date checks, regex, Mapping/Sequence, dataclass replacement, paths and literal annotations. Pydantic owns frozen strict-field models and after-validators; pandas/NumPy table/scalar handling; GeoPandas the parcel type; PyProj CRS metadata; Shapely geometry types/WKB. No immutable_mapping, strict_json or frame_integrity import exists here. Frozen tuples/models make policy collections immutable; frozen result envelope still contains seven mutable frames.

## Public flow and evidence boundary

| Boundary | Required arguments and return | Actual order |
| --- | --- | --- |
| Policy loader | path: str or Path -> config | Read bytes, strict YAML, Mapping guard, model validation. No default path. |
| Interpreter | index, structure, structure_config, zones, zoning_intersections, parcels, planning_document, policy -> result | Physical normalized-zoning guard; policy reconstruction/load; build once; compare result against itself plus original parcels. |
| Validator | Same eight then result -> None | Physical normalized-zoning guard; policy reconstruction/load; independently rebuild expected result; compare supplied result with it. |

All parameters are positional-or-keyword and required. Although zones is annotated DataFrame here, the delegated public GPU gate requires a GeoDataFrame; relations must be a non-geospatial DataFrame. That owner revalidates/reloads physical extracted GPU zoning, rebuilds normalized catalog/intersections and parcel summaries and compares them. Its reconstruction uses planar XY metric work in EPSG:2154, with storage parcel geometry/CRS retained. This module does not itself acquire sources or run overlay. The gate can read physical files; a counter of gate invocations is not a file-read counter.

Inside _build_result: validate extracted index, source-rebuild structure and retained fragments, compare six locks, copy/check parcels/zones/relations, check complete resolved mapping, compute policy hash, build routes/links, unpack chapter map and catalog, build chapter/source-label/positive-relation/parcel outputs, then hashes. Structure is reconstructed from index text/config, not by reopening the original PDF. Index validation recomputes its in-memory page/index commitments; propagated archive/PDF hashes do not prove a fresh PDF read.

Explicit BessZoningPrecheckError passes through public wrappers. Structure errors and zoning errors have separate chained contextual wrappers; other Exception gets a generic safe-build or safe-validation message. Loader separately exposes strict-YAML message and wraps other failures. Direct model_validate raises Pydantic ValueError-family errors; private helpers do not acquire a universal wrapper just because public callers have one.

## Occurrences, review and routes

Short quote, retained section/page fragment and full containing rule are distinct. Page is one-based; offsets are zero-based half-open Python-character intervals [start:end], NOT UTF-8 byte offsets. Quote/full rule SHA uses their exact UTF-8 bytes; fragment SHA is compared to the source-rebuilt retained fragment. Quote max length is 600; full rule has no corresponding cap. Exact source slice, SHA and containment must all agree. A matching hash alone does not prove legal interpretation.

Chapter-scoped duplicate key is (chapter,section,page,fragment SHA,quote start,end), irrespective of ID/kind/direction. Rule identity binds section/page/fragment/range/hash/text; one occurrence uses one rule ID. Partially overlapping, nonidentical rule ranges in a fragment fail. The same GENERAL occurrence may be explicitly reviewed/scoped in different chapters. Evidence IDs and route IDs are globally unique; compatible routes may reuse ONE evidence ID, but may not duplicate its occurrence under a new ID.

| Route kind | Nonempty roles required; all others empty | Derived route status |
| --- | --- | --- |
| DIRECT_ROUTE | positive | POTENTIALLY_COMPATIBLE |
| CONDITIONAL_ROUTE | positive and condition | CONDITIONAL_REVIEW |
| RESTRICTION_EXCEPTION_ROUTE | positive and difficulty | CONDITIONAL_REVIEW |
| DIFFICULTY_ONLY | difficulty | LIKELY_DIFFICULT |

Roles require same-chapter references and matching directions. CONTEXT_ONLY must remain unlinked; every other evidence must be linked at least once. Shape means presence, not exactly one member. Chapter derivation: INCOMPLETE -> UNKNOWN/LOW requirement first; otherwise any conditional/exception route -> CONDITIONAL_REVIEW; direct plus difficulty-only -> UNKNOWN; direct alone -> potential; difficulty-only -> difficult; no route -> UNKNOWN. Complete review confidence otherwise remains configured LOW/MEDIUM/HIGH, not calculated. Empty evidence can produce UNKNOWN with configured MEDIUM confidence. Required articles must physically exist once under the correct observed chapter even if review is incomplete. COMPLETE requires their IDs in reviewed sections; it means configured-use-control coverage only, not all regulation articles.

R6/checked-in test context: UP uses a restriction/exception route without automatically attaching the separate ICPE clause as condition. AUp explicitly links general infrastructure as condition; its ICPE clause remains context, as for UP. No BESS == ICPE conclusion follows.

## Geographic propagation, schema and mutability

Raw source labels are retained alongside resolved chapter labels. EXACT and CONFIG_ALIAS are accepted only with full label-set/section-ID closure. Ambiguous/unmapped results fail; no prefix guess or UNKNOWN fallback for an unresolved mapping. Each raw label must resolve to one source-layer lineage. Source-label rows follow mapping order; chapters factual order; evidence/routes policy order; link table nonempty sorts route_id/evidence_id stably; positive interpretations follow relation order; parcels keep original order/index.

Relations require unique parcel/zone pairs, known identities, finite nonnegative metric values and correct lineage. AREA_OVERLAP has area >0 m2, TOUCH_ONLY exactly0. Denominators are >0 and share percentages reproduce area within max(1e-6, reference_area*1e-12). This is numerical integrity tolerance, not BESS suitability. Only positive relations receive interpretation rows. Touches are counted separately and never contribute status/evidence. Dominance is largest area then smallest planning_zone_id, validated against upstream fact. All positive statuses equal -> that status; any disagreement -> MIXED_REVIEW_REQUIRED; no positive -> UNKNOWN with null dominant status/confidence. Dominant status/confidence are retained but do not erase dissent. Evidence ID unions are separately deduplicated/sorted for decisions/context.

No union/coverage/gap/overlap-excess calculation or status threshold is added here. Those factual summaries are delegated to normalized zoning and preserved as prior parcel fields; they are not votes or weights for the written policy. No overall confidence aggregation is produced. Configured chapter confidence propagates to source and relation rows and dominant parcel confidence only.

| Frame or suffix | Ordered column declaration | Construction and null/dtype boundary |
| --- | --- | --- |
| chapter_policy | CHAPTER_POLICY_COLUMNS: 24 | evidence_count int64; remaining inferred, tuple reviewed/missing/evidence IDs; no semantic null required. |
| evidence_catalog | EVIDENCE_CATALOG_COLUMNS: 30 | page_number and four offsets int64; decision_linked bool; remaining inferred strings/tuples. Exact nonnull evidence text. |
| route_assessments | ROUTE_ASSESSMENT_COLUMNS: 18 | Inferred strings/tuples, no explicit casts; empty role tuples are allowed by shape. |
| evidence_route_links | EVIDENCE_ROUTE_LINK_COLUMNS: 16 | Inferred; reset index after nonempty sort; no context membership. |
| source_zone_policy | SOURCE_ZONE_POLICY_COLUMNS: 20 | Inferred; exact raw and resolved labels, tuple evidence, no geometry. |
| parcel_zone_interpretations | PARCEL_ZONE_POLICY_COLUMNS: 23 | Two float metric values; empty frame explicitly float64 for them/object otherwise; nonempty inferred. |
| parcels appended suffix | PARCEL_PRECHECK_COLUMNS: 15 | Four int64 counts, two bool flags, other nine object arrays; dominant status/confidence None when no positive relation; empty evidence tuples. |

Six new plain frames use constructor indexes (and link reset), no CRS. All parcel original columns precede suffix; copy preserves geometry/CRS/index/names/order. General string/tuple column dtypes are inferred rather than a mandated pandas str schema. Canonical comparison accepts tuple/list/ndarray equivalence for evidence readback; no index-class/dtype equality claim. Literal ordered column declarations below are authoritative, not a borrowed CNIG schema. No M/Z-preservation guarantee, geometry repair or local reprojection is inferred from WKB hashing.

## Hash commitments

JSON canonicalization uses UTF-8, ensure_ascii=False, allow_nan=False, sorted object keys and compact separators. Sequence, row, column and index order remains meaningful. NumPy scalar -> item, None/pd.NA/float NaN -> null, bytes -> hex, dates -> ISO, arrays/tuples -> arrays, mapping keys -> str. WKB uses only explicit hex=True/include_srid=False options; CRS is separately to_json_dict and active geometry name. Unsupported leaves fail. Frame payload contains columns/index_names/index/rows, not dtype or index-class signature. to_json_dict is in-memory metadata, not a filesystem write.

| Exact domain after landscout.bess_zoning. prefix | Payload |
| --- | --- |
| policy_config | Whole validated config JSON including schema 5 and ordered declarations; not raw YAML. |
| factual_structure_input | Six propagated structure hashes/version described in helper notice; not raw PDF. |
| zone_mapping_input | Six zone identity/lineage columns plus every mapping column, with frame metadata. |
| zoning_relations_input | All supplied relation columns, index and rows. |
| evidence_catalog, evidence_route_links, route_assessments, chapter_policy, source_zone_policy, parcel_zone_policy, parcel_output | Domain plus 17 shared metadata items and corresponding frame payload (all parcel columns for last). |
| precheck_result | Domain plus same 17 metadata and seven component hashes. |

The metadata includes result/policy versions5/5, profiles/scopes, upstream/input hashes, ordered relation-column list and touch count. It excludes output/complete hashes to avoid cycles. _result_with_hashes recomputes seven components then complete hash using two dataclass replacements, sharing frames. Public validator builds independent expected hashes; builder self-comparison does not. There is no raw-Parquet SHA or persisted manifest contract here. No hash/schema migration occurs in this documentation-only ticket.

## Module declarations

Exact imports are preserved in the full snapshot. These constants/aliases add no extra closure units.

<a id="declaration---all--"></a>
### `landscout.stages.interpret_bess_zoning.__all__`

Source lines 42–49. Six-name module public export list, compared to package imports and __all__; declarations add no historical symbol credit.

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

<a id="declaration-policy-schema-version"></a>
### `landscout.stages.interpret_bess_zoning.POLICY_SCHEMA_VERSION`

Source lines 51–51. Version 5 for the policy or canonical result envelope respectively; unchanged.

```python
POLICY_SCHEMA_VERSION = 5
```

<a id="declaration-result-hash-schema-version"></a>
### `landscout.stages.interpret_bess_zoning.RESULT_HASH_SCHEMA_VERSION`

Source lines 52–52. Version 5 for the policy or canonical result envelope respectively; unchanged.

```python
RESULT_HASH_SCHEMA_VERSION = 5
```

<a id="declaration-planning-precheck-scope"></a>
### `landscout.stages.interpret_bess_zoning.PLANNING_PRECHECK_SCOPE`

Source lines 53–53. Exact closed scope for written-zoning preanalysis and configured-use-control review respectively, not legal permission.

```python
PLANNING_PRECHECK_SCOPE = "WRITTEN_ZONING_REGULATION_ONLY"
```

<a id="declaration-review-scope"></a>
### `landscout.stages.interpret_bess_zoning.REVIEW_SCOPE`

Source lines 54–54. Exact closed scope for written-zoning preanalysis and configured-use-control review respectively, not legal permission.

```python
REVIEW_SCOPE = "CONFIGURED_USE_CONTROL_ARTICLES_ONLY"
```

<a id="declaration-chapterstatus"></a>
### `landscout.stages.interpret_bess_zoning.ChapterStatus`

Source lines 56–61. Closed Literal type domain; validation semantics and propagation are described above, not inferred from text alone.

```python
ChapterStatus = Literal[
    "POTENTIALLY_COMPATIBLE",
    "CONDITIONAL_REVIEW",
    "LIKELY_DIFFICULT",
    "UNKNOWN",
]
```

<a id="declaration-confidence"></a>
### `landscout.stages.interpret_bess_zoning.Confidence`

Source lines 62–62. Closed Literal type domain; validation semantics and propagation are described above, not inferred from text alone.

```python
Confidence = Literal["HIGH", "MEDIUM", "LOW"]
```

<a id="declaration-reviewcompleteness"></a>
### `landscout.stages.interpret_bess_zoning.ReviewCompleteness`

Source lines 63–65. Closed Literal type domain; validation semantics and propagation are described above, not inferred from text alone.

```python
ReviewCompleteness = Literal[
    "COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES", "INCOMPLETE"
]
```

<a id="declaration-routekind"></a>
### `landscout.stages.interpret_bess_zoning.RouteKind`

Source lines 66–71. Closed Literal type domain; validation semantics and propagation are described above, not inferred from text alone.

```python
RouteKind = Literal[
    "DIRECT_ROUTE",
    "CONDITIONAL_ROUTE",
    "RESTRICTION_EXCEPTION_ROUTE",
    "DIFFICULTY_ONLY",
]
```

<a id="declaration-evidencekind"></a>
### `landscout.stages.interpret_bess_zoning.EvidenceKind`

Source lines 72–81. Closed Literal type domain; validation semantics and propagation are described above, not inferred from text alone.

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

<a id="declaration-evidencedirection"></a>
### `landscout.stages.interpret_bess_zoning.EvidenceDirection`

Source lines 82–87. Closed Literal type domain; validation semantics and propagation are described above, not inferred from text alone.

```python
EvidenceDirection = Literal[
    "SUPPORTS_POTENTIAL_COMPATIBILITY",
    "SUPPORTS_DIFFICULTY",
    "CONDITION",
    "CONTEXT_ONLY",
]
```

<a id="declaration--chapter-statuses"></a>
### `landscout.stages.interpret_bess_zoning._CHAPTER_STATUSES`

Source lines 89–91. Frozen membership domain for result validation/mapping, not precedence ordering.

```python
_CHAPTER_STATUSES = frozenset(
    {"POTENTIALLY_COMPATIBLE", "CONDITIONAL_REVIEW", "LIKELY_DIFFICULT", "UNKNOWN"}
)
```

<a id="declaration--parcel-statuses"></a>
### `landscout.stages.interpret_bess_zoning._PARCEL_STATUSES`

Source lines 92–92. Frozen membership domain for result validation/mapping, not precedence ordering.

```python
_PARCEL_STATUSES = _CHAPTER_STATUSES | {"MIXED_REVIEW_REQUIRED"}
```

<a id="declaration--confidences"></a>
### `landscout.stages.interpret_bess_zoning._CONFIDENCES`

Source lines 93–93. Frozen membership domain for result validation/mapping, not precedence ordering.

```python
_CONFIDENCES = frozenset({"HIGH", "MEDIUM", "LOW"})
```

<a id="declaration--resolved-mapping-statuses"></a>
### `landscout.stages.interpret_bess_zoning._RESOLVED_MAPPING_STATUSES`

Source lines 94–94. Frozen membership domain for result validation/mapping, not precedence ordering.

```python
_RESOLVED_MAPPING_STATUSES = frozenset({"EXACT", "CONFIG_ALIAS"})
```

<a id="declaration-chapter-policy-columns"></a>
### `landscout.stages.interpret_bess_zoning.CHAPTER_POLICY_COLUMNS`

Source lines 96–121. Exact ordered frame-column declaration; PARCEL_PRECHECK_COLUMNS is an appended suffix, others full table schemas. Dtypes/order/nulls are specified above.

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

<a id="declaration-evidence-catalog-columns"></a>
### `landscout.stages.interpret_bess_zoning.EVIDENCE_CATALOG_COLUMNS`

Source lines 122–153. Exact ordered frame-column declaration; PARCEL_PRECHECK_COLUMNS is an appended suffix, others full table schemas. Dtypes/order/nulls are specified above.

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

<a id="declaration--evidence-occurrence-columns"></a>
### `landscout.stages.interpret_bess_zoning._EVIDENCE_OCCURRENCE_COLUMNS`

Source lines 154–161. Ordered six-column chapter-scoped duplicate key, not an output frame schema by itself.

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

<a id="declaration-route-assessment-columns"></a>
### `landscout.stages.interpret_bess_zoning.ROUTE_ASSESSMENT_COLUMNS`

Source lines 162–181. Exact ordered frame-column declaration; PARCEL_PRECHECK_COLUMNS is an appended suffix, others full table schemas. Dtypes/order/nulls are specified above.

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

<a id="declaration-evidence-route-link-columns"></a>
### `landscout.stages.interpret_bess_zoning.EVIDENCE_ROUTE_LINK_COLUMNS`

Source lines 182–199. Exact ordered frame-column declaration; PARCEL_PRECHECK_COLUMNS is an appended suffix, others full table schemas. Dtypes/order/nulls are specified above.

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

<a id="declaration-source-zone-policy-columns"></a>
### `landscout.stages.interpret_bess_zoning.SOURCE_ZONE_POLICY_COLUMNS`

Source lines 200–221. Exact ordered frame-column declaration; PARCEL_PRECHECK_COLUMNS is an appended suffix, others full table schemas. Dtypes/order/nulls are specified above.

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

<a id="declaration-parcel-zone-policy-columns"></a>
### `landscout.stages.interpret_bess_zoning.PARCEL_ZONE_POLICY_COLUMNS`

Source lines 222–246. Exact ordered frame-column declaration; PARCEL_PRECHECK_COLUMNS is an appended suffix, others full table schemas. Dtypes/order/nulls are specified above.

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

<a id="declaration-parcel-precheck-columns"></a>
### `landscout.stages.interpret_bess_zoning.PARCEL_PRECHECK_COLUMNS`

Source lines 247–263. Exact ordered frame-column declaration; PARCEL_PRECHECK_COLUMNS is an appended suffix, others full table schemas. Dtypes/order/nulls are specified above.

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

## Qualified symbol contracts

Every original symbol has one notice and a matching owner note. Exact signatures specify all parameters/types/defaults; missing annotations are not None annotations. For fields, Field constraints without a supplied value do not create defaults. Private lookup/third-party exceptions propagate unless an explicit wrapper is described. Full implementations and imports appear once below.

<a id="symbol-besszoningprecheckerror"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckError`

Source lines 266–267. Kind: class. Owner: `landscout.stages.interpret_bess_zoning`.

```python
class BessZoningPrecheckError(ValueError):
```

ValueError subclass for unprovable written-zoning prechecks. It has no fields or custom initializer. Explicit policy errors pass through public wrappers; delegated/unexpected errors are translated as described at each boundary.

<a id="symbol--strictconfigmodel"></a>
### `landscout.stages.interpret_bess_zoning._StrictConfigModel`

Source lines 270–271. Kind: class. Owner: `landscout.stages.interpret_bess_zoning`.

```python
class _StrictConfigModel(BaseModel):
```

Internal Pydantic base: extra="forbid", frozen=True; no global strict=True. Strict scalar annotations and Literal domains enforce individual fields. Subclass sequences are tuples of immutable leaves/models; the result DataFrames are not models and remain mutable.

<a id="symbol-policysourcelock"></a>
### `landscout.stages.interpret_bess_zoning.PolicySourceLock`

Source lines 274–280. Kind: class. Owner: `landscout.stages.interpret_bess_zoning`.

```python
class PolicySourceLock(_StrictConfigModel):
```

Six required strict strings bind document, archive, PDF, index, structure content and structure profile. Four hashes require lowercase 64-hex syntax. Root policy validation checks exact nonblank document/profile strings; physical correspondence is not proven by this model, but compared later by _validate_policy_lock.

<a id="symbol-policysourcelock-document-id"></a>
### `landscout.stages.interpret_bess_zoning.PolicySourceLock.document_id`

Source lines 275–275. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
document_id: StrictStr = Field(min_length=1)
```

Exact GPU document identifier compared to index.document_id; nonempty StrictStr; exact whitespace guard at root policy. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policysourcelock-archive-sha256"></a>
### `landscout.stages.interpret_bess_zoning.PolicySourceLock.archive_sha256`

Source lines 276–276. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
archive_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
```

Declared archive byte SHA compared to index.archive_sha256; lowercase 64-hex, not recalculated here. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policysourcelock-pdf-sha256"></a>
### `landscout.stages.interpret_bess_zoning.PolicySourceLock.pdf_sha256`

Source lines 277–277. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
```

Declared PDF byte SHA compared to index.pdf_sha256; no file access from this field. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policysourcelock-index-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.PolicySourceLock.index_content_sha256`

Source lines 278–278. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
```

Canonical extracted-index commitment compared to index.index_content_sha256, not the PDF byte hash. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policysourcelock-structure-result-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.PolicySourceLock.structure_result_content_sha256`

Source lines 279–279. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
structure_result_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
```

Complete factual structure commitment compared to supplied validated structure. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policysourcelock-structure-profile"></a>
### `landscout.stages.interpret_bess_zoning.PolicySourceLock.structure_profile`

Source lines 280–280. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
structure_profile: StrictStr = Field(min_length=1)
```

Exact structure-profile text compared to structure.structure_profile; not a version number. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence`

Source lines 283–371. Kind: class. Owner: `landscout.stages.interpret_bess_zoning`.

```python
class PolicyEvidence(_StrictConfigModel):
```

Sixteen required fields distinguish a short exact quote, its section/page occurrence and its containing full source-rule text. Strict integers and strings, closed kind/direction domains, model-level hashes/containment; actual fragment slices are checked later. All text remains exact; no trimming, keyword classifier or legal inference.

<a id="symbol-policyevidence-evidence-id"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.evidence_id`

Source lines 284–284. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
evidence_id: StrictStr = Field(min_length=1)
```

Global exact nonblank evidence key; one ID per chapter-scoped occurrence and referenced by compatible routes. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-section-id"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.section_id`

Source lines 285–285. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
section_id: StrictStr = Field(min_length=1)
```

Exact nonblank section key; later must exist in rebuilt structure and reviewed IDs for this chapter. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-page-number"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.page_number`

Source lines 286–286. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
page_number: StrictInt = Field(ge=1)
```

Strict positive integer, one-based source page; paired with section_id to locate fragment. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-evidence-kind"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.evidence_kind`

Source lines 287–287. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
evidence_kind: EvidenceKind
```

Eight-member EvidenceKind literal; its admissible direction is checked by after-validator. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-evidence-direction"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.evidence_direction`

Source lines 288–288. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
evidence_direction: EvidenceDirection
```

Four-member EvidenceDirection literal; controls route role or unlinked context, not legal fact. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-exact-raw-excerpt"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.exact_raw_excerpt`

Source lines 289–289. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
exact_raw_excerpt: StrictStr = Field(min_length=1, max_length=600)
```

Exact nonblank untrimmed quote, 1..600 Python characters. UTF-8 bytes hashed, fragment characters sliced. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-excerpt-sha256"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.excerpt_sha256`

Source lines 290–290. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
excerpt_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
```

Lowercase 64-hex SHA of exact_raw_excerpt UTF-8; recalculated at model and factual occurrence validation. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-section-page-fragment-sha256"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.section_page_fragment_sha256`

Source lines 291–291. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
section_page_fragment_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
```

Lowercase 64-hex commitment to full retained raw section/page fragment; compared to rebuilt fragment. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-excerpt-start"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.excerpt_start`

Source lines 292–292. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
excerpt_start: StrictInt = Field(ge=0)
```

Strict integer >=0, inclusive Python-character offset within fragment; not UTF-8 byte offset. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-excerpt-end"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.excerpt_end`

Source lines 293–293. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
excerpt_end: StrictInt = Field(ge=1)
```

Strict integer >=1, exclusive fragment-character endpoint; must exceed start and lie inside rule. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-source-rule-id"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.source_rule_id`

Source lines 294–294. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
source_rule_id: StrictStr = Field(min_length=1)
```

Exact nonblank rule key; globally identifies one exact full-rule occurrence, reusable by evidence for that occurrence. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-source-rule-excerpt"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.source_rule_excerpt`

Source lines 295–295. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
source_rule_excerpt: StrictStr = Field(min_length=1)
```

Exact nonblank full rule, without the short quote 600-character cap; source slice must match. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-source-rule-sha256"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.source_rule_sha256`

Source lines 296–296. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
source_rule_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
```

Lowercase 64-hex SHA of source_rule_excerpt UTF-8; checked locally and against retained rule text. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-source-rule-start"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.source_rule_start`

Source lines 297–297. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
source_rule_start: StrictInt = Field(ge=0)
```

Strict >=0 inclusive character offset in same section/page fragment; bounds excerpt_start. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-source-rule-end"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.source_rule_end`

Source lines 298–298. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
source_rule_end: StrictInt = Field(ge=1)
```

Strict >=1 exclusive character offset; greater than rule start and bounds excerpt_end. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence-interpretation-note"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence.interpretation_note`

Source lines 299–299. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
interpretation_note: StrictStr = Field(min_length=1)
```

Exact nonblank human-authored explanation retained in catalog, not automatically inferred or legally proven. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-policyevidence--validate-exact-strings"></a>
### `landscout.stages.interpret_bess_zoning.PolicyEvidence._validate_exact_strings`

Source lines 302–371. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
    def _validate_exact_strings(self) -> PolicyEvidence:
```

After field validation, check six exact strings; UTF-8 excerpt SHA; ordered excerpt offsets; UTF-8 rule SHA; ordered rule offsets; numerical containment; then kind/direction matrix. Return self. Local violations raise ValueError (Pydantic wraps model validation); no fragment lookup here. USE_PERMISSION allows positive/context; USE_RESTRICTION difficulty/context; PUBLIC_INTEREST_EXCEPTION positive/condition/context; TECHNICAL_EQUIPMENT_RULE and ICPE_RULE all four; remaining three kinds difficulty/condition/context. Local temporary frozensets do not mutate the model.

Exact decorators (not extra units):

```python
    @model_validator(mode="after")
```

<a id="symbol-routeassessment"></a>
### `landscout.stages.interpret_bess_zoning.RouteAssessment`

Source lines 374–414. Kind: class. Owner: `landscout.stages.interpret_bess_zoning`.

```python
class RouteAssessment(_StrictConfigModel):
```

Required route_id, route_kind and applicability_note; three ordered evidence-ID tuples default to (). This declares an assessed relationship, not a physical or legal route. Frozen model validation rejects duplicates and invalid role shape; root policy later checks references and direction.

<a id="symbol-routeassessment-route-id"></a>
### `landscout.stages.interpret_bess_zoning.RouteAssessment.route_id`

Source lines 375–375. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
route_id: StrictStr = Field(min_length=1)
```

Exact nonblank route key; unique within chapter then globally at root policy. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-routeassessment-route-kind"></a>
### `landscout.stages.interpret_bess_zoning.RouteAssessment.route_kind`

Source lines 376–376. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
route_kind: RouteKind
```

One of four RouteKind literals; selects required presence/absence of three evidence roles. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-routeassessment-positive-evidence-ids"></a>
### `landscout.stages.interpret_bess_zoning.RouteAssessment.positive_evidence_ids`

Source lines 377–377. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
positive_evidence_ids: tuple[StrictStr, ...] = ()
```

Ordered tuple of exact StrictStr IDs, default (); if present must reference same-chapter positive-direction evidence. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-routeassessment-condition-evidence-ids"></a>
### `landscout.stages.interpret_bess_zoning.RouteAssessment.condition_evidence_ids`

Source lines 378–378. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
condition_evidence_ids: tuple[StrictStr, ...] = ()
```

Ordered tuple default (); required nonempty only for CONDITIONAL_ROUTE, direction CONDITION. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-routeassessment-difficulty-evidence-ids"></a>
### `landscout.stages.interpret_bess_zoning.RouteAssessment.difficulty_evidence_ids`

Source lines 379–379. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
difficulty_evidence_ids: tuple[StrictStr, ...] = ()
```

Ordered tuple default (); required nonempty for RESTRICTION_EXCEPTION_ROUTE or DIFFICULTY_ONLY, difficulty direction. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-routeassessment-applicability-note"></a>
### `landscout.stages.interpret_bess_zoning.RouteAssessment.applicability_note`

Source lines 380–380. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
applicability_note: StrictStr = Field(min_length=1)
```

Exact nonblank configured assessment note; copied to route table, not formal applicability proof. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-routeassessment--validate-route-shape"></a>
### `landscout.stages.interpret_bess_zoning.RouteAssessment._validate_route_shape`

Source lines 383–414. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
    def _validate_route_shape(self) -> RouteAssessment:
```

Check exact route/note/ID strings; uniqueness within each role, then uniqueness across combined roles. Compare presence booleans (positive, condition, difficulty) with DIRECT (1,0,0), CONDITIONAL (1,1,0), RESTRICTION_EXCEPTION (1,0,1), DIFFICULTY_ONLY (0,0,1). Return self; ValueError on mismatch. Temporary combined list is local. It checks nonempty membership, not exactly one ID or legal applicability.

Exact decorators (not extra units):

```python
    @model_validator(mode="after")
```

<a id="symbol--derived-chapter-status"></a>
### `landscout.stages.interpret_bess_zoning._derived_chapter_status`

Source lines 417–430. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _derived_chapter_status(
    review_completeness: ReviewCompleteness,
    routes: Sequence[RouteAssessment],
) -> ChapterStatus:
```

Pure status derivation from review_completeness and supplied routes. INCOMPLETE first returns UNKNOWN. Any CONDITIONAL_ROUTE or RESTRICTION_EXCEPTION_ROUTE yields CONDITIONAL_REVIEW. Otherwise DIRECT_ROUTE yields UNKNOWN if DIFFICULTY_ONLY also exists, else POTENTIALLY_COMPATIBLE; difficulty alone LIKELY_DIFFICULT; empty set UNKNOWN. No confidence calculation or weighting; no explicit exception wrapper.

<a id="symbol-chapterpolicy"></a>
### `landscout.stages.interpret_bess_zoning.ChapterPolicy`

Source lines 433–473. Kind: class. Owner: `landscout.stages.interpret_bess_zoning`.

```python
class ChapterPolicy(_StrictConfigModel):
```

Ten fields: seven required text/domain declarations and three ordered tuples defaulting to (). Reviewed IDs, evidence and routes remain immutable. Declared chapter status must agree with route derivation; confidence is configured, not a numerical certainty. INCOMPLETE requires UNKNOWN/LOW but does not automatically erase evidence/routes.

<a id="symbol-chapterpolicy-resolved-zone-chapter-label"></a>
### `landscout.stages.interpret_bess_zoning.ChapterPolicy.resolved_zone_chapter_label`

Source lines 434–434. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
resolved_zone_chapter_label: StrictStr = Field(min_length=1)
```

Exact nonblank resolved written chapter label; globally unique and required to match full observed chapter set. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-chapterpolicy-review-completeness"></a>
### `landscout.stages.interpret_bess_zoning.ChapterPolicy.review_completeness`

Source lines 435–435. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
review_completeness: ReviewCompleteness
```

COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES or INCOMPLETE; complete is not all-regulation/legal completeness. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-chapterpolicy-reviewed-section-ids"></a>
### `landscout.stages.interpret_bess_zoning.ChapterPolicy.reviewed_section_ids`

Source lines 436–436. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
reviewed_section_ids: tuple[StrictStr, ...] = ()
```

Ordered exact-ID tuple default (); duplicates fail; GENERAL or same-chapter sections only at factual gate. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-chapterpolicy-review-note"></a>
### `landscout.stages.interpret_bess_zoning.ChapterPolicy.review_note`

Source lines 437–437. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
review_note: StrictStr = Field(min_length=1)
```

Exact nonblank review explanation retained in chapter table. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-chapterpolicy-zoning-precheck-status"></a>
### `landscout.stages.interpret_bess_zoning.ChapterPolicy.zoning_precheck_status`

Source lines 438–438. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
zoning_precheck_status: ChapterStatus
```

Configured ChapterStatus required to equal derived routes/completeness; never ALLOWED/FORBIDDEN/PROHIBITED. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-chapterpolicy-zoning-precheck-confidence"></a>
### `landscout.stages.interpret_bess_zoning.ChapterPolicy.zoning_precheck_confidence`

Source lines 439–439. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
zoning_precheck_confidence: Confidence
```

Configured LOW/MEDIUM/HIGH; INCOMPLETE requires LOW. Not independently derived probability. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-chapterpolicy-rationale"></a>
### `landscout.stages.interpret_bess_zoning.ChapterPolicy.rationale`

Source lines 440–440. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
rationale: StrictStr = Field(min_length=1)
```

Exact nonblank configured rationale retained and hashed; no legal meaning generated from tokens. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-chapterpolicy-missing-information"></a>
### `landscout.stages.interpret_bess_zoning.ChapterPolicy.missing_information`

Source lines 441–441. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
missing_information: StrictStr = Field(min_length=1)
```

Exact nonblank statement of unresolved review information, not an optional null or inferred fact. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-chapterpolicy-evidence"></a>
### `landscout.stages.interpret_bess_zoning.ChapterPolicy.evidence`

Source lines 442–442. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
evidence: tuple[PolicyEvidence, ...] = ()
```

Ordered immutable tuple of PolicyEvidence, default (); empty permitted when status/routes remain coherent. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-chapterpolicy-route-assessments"></a>
### `landscout.stages.interpret_bess_zoning.ChapterPolicy.route_assessments`

Source lines 443–443. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
route_assessments: tuple[RouteAssessment, ...] = ()
```

Ordered immutable tuple of RouteAssessment, default (); determines chapter status, not geometry. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-chapterpolicy--validate-evidence-semantics"></a>
### `landscout.stages.interpret_bess_zoning.ChapterPolicy._validate_evidence_semantics`

Source lines 446–473. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
    def _validate_evidence_semantics(self) -> ChapterPolicy:
```

Validate exact label/review note/rationale/missing-information strings, unique reviewed IDs, INCOMPLETE status/confidence, unique within-chapter route IDs, then declared-versus-derived status. Return self; ValueError on disagreement. Does not check section membership or physical required articles; those depend on rebuilt structure.

Exact decorators (not extra units):

```python
    @model_validator(mode="after")
```

<a id="symbol-besszoningpolicyconfig"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig`

Source lines 476–624. Kind: class. Owner: `landscout.stages.interpret_bess_zoning`.

```python
class BessZoningPolicyConfig(_StrictConfigModel):
```

Seven required fields, schema 5 and exact scope literals. Required articles and chapters are nonempty tuples; input YAML sequences are validated into tuples with strict immutable leaves/nested frozen models. No retained mapping or FrozenDict here. Model validation proves declaration coherence, not GPU/PDF truth; public supplied-model resolution reconstructs and revalidates it.

<a id="symbol-besszoningpolicyconfig-schema-version"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.schema_version`

Source lines 479–479. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
schema_version: StrictInt
```

Required StrictInt exactly 5, older schemas rejected; not a default or coercible numeric string. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-besszoningpolicyconfig-policy-profile"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.policy_profile`

Source lines 480–480. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
policy_profile: StrictStr = Field(min_length=1)
```

Exact nonblank profile identifier; participates in policy hash and output lineage. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-besszoningpolicyconfig-planning-precheck-scope"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.planning_precheck_scope`

Source lines 481–481. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
planning_precheck_scope: Literal["WRITTEN_ZONING_REGULATION_ONLY"]
```

Required exact WRITTEN_ZONING_REGULATION_ONLY literal; not CNIG-code policy scope. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-besszoningpolicyconfig-review-scope"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.review_scope`

Source lines 482–482. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
review_scope: Literal["CONFIGURED_USE_CONTROL_ARTICLES_ONLY"]
```

Required CONFIGURED_USE_CONTROL_ARTICLES_ONLY literal; no exhaustive legal review implied. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-besszoningpolicyconfig-source-lock"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.source_lock`

Source lines 483–483. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
source_lock: PolicySourceLock
```

Required frozen PolicySourceLock, reconstructed at public supplied-model boundary. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-besszoningpolicyconfig-required-zone-article-numbers"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.required_zone_article_numbers`

Source lines 484–484. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
required_zone_article_numbers: tuple[StrictStr, ...] = Field(min_length=1)
```

Required nonempty ordered tuple of exact unique StrictStr article numbers, not integers; no sorting. Every observed chapter must have each child exactly once. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-besszoningpolicyconfig-chapters"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig.chapters`

Source lines 485–485. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
chapters: tuple[ChapterPolicy, ...] = Field(min_length=1)
```

Required nonempty ordered tuple of frozen ChapterPolicy; exact full observed chapter set checked later. Evidence/route build order follows this tuple. Pydantic validation applies; frozen retained value, no field-level I/O.

<a id="symbol-besszoningpolicyconfig--validate-policy"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig._validate_policy`

Source lines 488–624. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
    def _validate_policy(self) -> BessZoningPolicyConfig:
```

After nested validation, require version 5; exact profile/lock text; unique required article strings and chapter labels. Enforce globally unique evidence IDs and one ID/kind/direction per chapter-scoped occurrence. One source_rule_id maps to one full identity (section,page,fragment SHA,start,end,rule SHA,text); the exact occurrence maps back to one rule ID. Within a section/page/fragment, overlapping nonidentical rule ranges fail; identical ranges and touching endpoints are not that conflict. Enforce global route IDs, same-chapter evidence references, role-compatible direction, unlinked CONTEXT_ONLY and at least one link for every decision evidence. Return self; ValueError guards, no physical I/O or mutation of retained collections.

Exact decorators (not extra units):

```python
    @model_validator(mode="after")
```

<a id="symbol-besszoningprecheckresult"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult`

Source lines 628–662. Kind: class. Owner: `landscout.stages.interpret_bess_zoning`.

```python
class BessZoningPrecheckResult:
```

Frozen dataclass with 32 required fields: 24 scalars, one ordered relation-column tuple and seven mutable frames (six DataFrames and parcel GeoDataFrame). No default, post-init validator or deep table freezing. Copies/builders and explicit public validation, not annotations/construction, establish evidence. No artifact manifest/loader/writer is declared here.

Exact decorators (not extra units):

```python
@dataclass(frozen=True)
```

<a id="symbol-besszoningprecheckresult-result-hash-schema-version"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.result_hash_schema_version`

Source lines 631–631. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
result_hash_schema_version: int
```

Result integrity schema 5, validated explicitly; plain int annotation alone does not enforce it. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-policy-schema-version"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.policy_schema_version`

Source lines 632–632. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
policy_schema_version: int
```

Resolved policy schema 5; compared to rebuilt result and supported version. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-policy-profile"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.policy_profile`

Source lines 633–633. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
policy_profile: str
```

Copied resolved policy profile; compared and included in component metadata. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-planning-precheck-scope"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.planning_precheck_scope`

Source lines 634–634. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
planning_precheck_scope: str
```

Copied WRITTEN_ZONING_REGULATION_ONLY scope. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-review-scope"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.review_scope`

Source lines 635–635. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
review_scope: str
```

Copied CONFIGURED_USE_CONTROL_ARTICLES_ONLY scope. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-document-id"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.document_id`

Source lines 636–636. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
document_id: str
```

Copied index document identity; no physical read at dataclass construction. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-archive-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.archive_sha256`

Source lines 637–637. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
archive_sha256: str
```

Copied index archive-byte identity, later compared and syntax checked. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-pdf-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.pdf_sha256`

Source lines 638–638. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
pdf_sha256: str
```

Copied index PDF-byte identity, not recalculated from PDF in this module. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-index-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.index_content_sha256`

Source lines 639–639. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
index_content_sha256: str
```

Copied validated in-memory index-content identity. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-structure-result-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.structure_result_content_sha256`

Source lines 640–640. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
structure_result_content_sha256: str
```

Copied complete source-rebuilt structure identity. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-structure-profile"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.structure_profile`

Source lines 641–641. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
structure_profile: str
```

Copied factual structure profile text. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-policy-config-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.policy_config_sha256`

Source lines 642–642. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
policy_config_sha256: str
```

Recomputed canonical whole-policy SHA, not YAML byte SHA. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-factual-structure-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.factual_structure_content_sha256`

Source lines 643–643. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
factual_structure_content_sha256: str
```

Recomputed wrapper hash over six validated structure metadata commitments. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-zone-mapping-input-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.zone_mapping_input_sha256`

Source lines 644–644. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
zone_mapping_input_sha256: str
```

Recomputed six-column zone/all-column mapping input payload commitment. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-zoning-relation-hash-columns"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.zoning_relation_hash_columns`

Source lines 645–645. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
zoning_relation_hash_columns: tuple[str, ...]
```

Exact ordered tuple of all supplied relation column names; list only in hash payload, not retained runtime field. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-zoning-relations-input-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.zoning_relations_input_sha256`

Source lines 646–646. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
zoning_relations_input_sha256: str
```

Recomputed full relation selected-column/index/row payload SHA. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-evidence-catalog-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.evidence_catalog_content_sha256`

Source lines 647–647. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
evidence_catalog_content_sha256: str
```

Recomputed 30-column evidence frame plus 17-metadata SHA. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-evidence-route-links-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.evidence_route_links_content_sha256`

Source lines 648–648. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
evidence_route_links_content_sha256: str
```

Recomputed 16-column links frame plus 17-metadata SHA. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-route-assessments-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.route_assessments_content_sha256`

Source lines 649–649. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
route_assessments_content_sha256: str
```

Recomputed 18-column routes frame plus 17-metadata SHA. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-chapter-policy-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.chapter_policy_content_sha256`

Source lines 650–650. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
chapter_policy_content_sha256: str
```

Recomputed 24-column chapter frame plus 17-metadata SHA. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-source-zone-policy-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.source_zone_policy_content_sha256`

Source lines 651–651. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
source_zone_policy_content_sha256: str
```

Recomputed 20-column source-label frame plus 17-metadata SHA. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-parcel-zone-policy-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.parcel_zone_policy_content_sha256`

Source lines 652–652. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
parcel_zone_policy_content_sha256: str
```

Recomputed 23-column positive-area interpretation frame plus 17-metadata SHA. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-parcel-output-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.parcel_output_content_sha256`

Source lines 653–653. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
parcel_output_content_sha256: str
```

Recomputed all-column parcel output frame plus 17-metadata SHA, with CRS and geometry encoding. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-complete-result-content-sha256"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.complete_result_content_sha256`

Source lines 654–654. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
complete_result_content_sha256: str
```

Recomputed complete metadata and seven component-hash envelope SHA. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-touch-only-relation-count"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.touch_only_relation_count`

Source lines 655–655. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
touch_only_relation_count: int
```

Nonnegative count of all supplied TOUCH_ONLY rows, including no interpretation rows for them. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-evidence-catalog"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.evidence_catalog`

Source lines 656–656. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
evidence_catalog: pd.DataFrame
```

Mutable 30-column DataFrame; policy evidence order; exact text/positions/identities/reverse links; five int64 positions/page and one bool. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-evidence-route-links"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.evidence_route_links`

Source lines 657–657. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
evidence_route_links: pd.DataFrame
```

Mutable 16-column DataFrame; nonempty sorted route_id/evidence_id, unique pairs and compatible roles. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-route-assessments"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.route_assessments`

Source lines 658–658. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
route_assessments: pd.DataFrame
```

Mutable 18-column DataFrame in policy route order, tuple evidence-role memberships. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-chapter-policy"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.chapter_policy`

Source lines 659–659. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
chapter_policy: pd.DataFrame
```

Mutable 24-column DataFrame in factual chapter order, int64 evidence_count and exact review/evidence/status facts. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-source-zone-policy"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.source_zone_policy`

Source lines 660–660. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
source_zone_policy: pd.DataFrame
```

Mutable 20-column DataFrame in mapping order, one row per raw source label with resolved chapter policy. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-parcel-zone-interpretations"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.parcel_zone_interpretations`

Source lines 661–661. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
parcel_zone_interpretations: pd.DataFrame
```

Mutable 23-column DataFrame in positive relation order, float64 metric area/share, no TOUCH_ONLY rows or geometry. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol-besszoningprecheckresult-parcels"></a>
### `landscout.stages.interpret_bess_zoning.BessZoningPrecheckResult.parcels`

Source lines 662–662. Kind: field. Owner: `landscout.stages.interpret_bess_zoning`.

```python
parcels: gpd.GeoDataFrame
```

Mutable GeoDataFrame copy with all original columns followed by 15 precheck fields; same row order/index/geometry/CRS. Required dataclass field, not default empty frame. Required constructor field; dataclass annotation is not a runtime guard.

<a id="symbol--config-string"></a>
### `landscout.stages.interpret_bess_zoning._config_string`

Source lines 665–668. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _config_string(value: str, label: str) -> str:
```

Return unchanged annotated str when nonempty and equal to strip(); otherwise ValueError. No isinstance test or coercion: a wrong private-call object can leak AttributeError. Used after StrictStr validation by models, not the factual scalar guard.

<a id="symbol-load-bess-zoning-policy-config"></a>
### `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config`

Source lines 671–684. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def load_bess_zoning_policy_config(path: str | Path) -> BessZoningPolicyConfig:
```

Read required str-or-Path bytes, use common.strict_yaml.loads_strict_yaml, require top-level Mapping, model_validate and return BessZoningPolicyConfig. Preserve BessZoningPrecheckError; wrap StrictYamlError with its message/cause; wrap every other Exception as "BESS zoning policy is invalid". Local filesystem read, no download or default policy path.

<a id="symbol--strict-string"></a>
### `landscout.stages.interpret_bess_zoning._strict_string`

Source lines 687–690. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _strict_string(value: object, label: str) -> str:
```

Reject non-str, empty or surrounding-whitespace text with BessZoningPrecheckError; return unchanged str. No trimming, normalization or numeric coercion.

<a id="symbol--strict-nonnegative-integer"></a>
### `landscout.stages.interpret_bess_zoning._strict_nonnegative_integer`

Source lines 693–699. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _strict_nonnegative_integer(value: object, label: str) -> int:
```

Reject bool and non-Integral, convert Integral (including supported NumPy integral values) with int(), require >=0 and return int. Raises BessZoningPrecheckError for domain guards; no broad conversion wrapper. Not an exact built-in-int-only guard.

<a id="symbol--strict-positive-integer"></a>
### `landscout.stages.interpret_bess_zoning._strict_positive_integer`

Source lines 702–706. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _strict_positive_integer(value: object, label: str) -> int:
```

Delegate integer validation, require >=1 and return int; BessZoningPrecheckError for zero. Used for pages and schema versions, not metre values.

<a id="symbol--validated-sha256"></a>
### `landscout.stages.interpret_bess_zoning._validated_sha256`

Source lines 709–715. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _validated_sha256(value: object, label: str) -> str:
```

Validate exact nonblank string then fullmatch 64 lowercase hexadecimal characters; return string. Syntax only, no byte read/recalculation.

<a id="symbol--strict-nonnegative-number"></a>
### `landscout.stages.interpret_bess_zoning._strict_nonnegative_number`

Source lines 718–727. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _strict_nonnegative_number(value: object, label: str) -> float:
```

Reject bool/non-Real; float() conversion catches TypeError, ValueError and OverflowError; require finite >=0. Return float. Every listed rejection is BessZoningPrecheckError. Numeric strings, None, NaN and infinities are not valid metric facts.

<a id="symbol--canonical-value"></a>
### `landscout.stages.interpret_bess_zoning._canonical_value`

Source lines 730–751. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _canonical_value(value: object) -> object:
```

Convert None/pd.NA to None; NumPy scalar via item recursively; geometry via shapely.to_wkb(hex=True, include_srid=False); Timestamp/datetime/date via isoformat; bytes via hex; tuple/list/ndarray recursively to list; Mapping keys via str with recursive values; float NaN to None; other str/int/float/bool unchanged. Unsupported type raises BessZoningPrecheckError. Infinity passes this helper but fails allow_nan=False in JSON. No explicit WKB byte order/output dimension or M/Z guarantee, and no dtype signature.

<a id="symbol--canonical-sha256"></a>
### `landscout.stages.interpret_bess_zoning._canonical_sha256`

Source lines 754–769. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _canonical_sha256(value: object) -> str:
```

Canonicalize then JSON serialize with ensure_ascii=False, allow_nan=False, sort_keys=True and compact separators; encode UTF-8 and return SHA256 hex. Preserve BessZoningPrecheckError; all other serialization Exception become chained canonical-integrity errors. In-memory operation, no file write.

<a id="symbol--frame-payload"></a>
### `landscout.stages.interpret_bess_zoning._frame_payload`

Source lines 772–796. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _frame_payload(frame: pd.DataFrame, columns: Sequence[str]) -> dict[str, object]:
```

Require unique frame columns and every selected column; return dict of ordered selected columns, index names/values and selected row records. For GeoDataFrame require CRS and add CRS.to_json_dict plus active geometry-column name. Canonical values normalize arrays/nulls; no dtype or index-class signature. Preserve own error and wrap other Exception. No mutation of frame, no filesystem write from to_json_dict.

<a id="symbol--frame-sha256"></a>
### `landscout.stages.interpret_bess_zoning._frame_sha256`

Source lines 799–800. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _frame_sha256(domain: str, frame: pd.DataFrame, columns: Sequence[str]) -> str:
```

Return canonical SHA of {domain, **frame payload}; selected columns and their order are required. Called for factual relation input; no independent schema validation beyond delegated frame helper.

<a id="symbol--policy-sha256"></a>
### `landscout.stages.interpret_bess_zoning._policy_sha256`

Source lines 803–809. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _policy_sha256(config: BessZoningPolicyConfig) -> str:
```

Return SHA of domain landscout.bess_zoning.policy_config and config.model_dump(mode="json"). Includes schema 5, locks, text, ordered chapters/evidence/routes/articles; not raw YAML bytes. No input reconstruction here (public resolver does that).

<a id="symbol--factual-structure-sha256"></a>
### `landscout.stages.interpret_bess_zoning._factual_structure_sha256`

Source lines 812–825. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _factual_structure_sha256(
    structure: PlanningRegulationStructureResult,
) -> str:
```

Return SHA under landscout.bess_zoning.factual_structure_input of six propagated structure commitments: complete structure hash, section hash version, config hash, sections hash, zone-map hash and topic-evidence hash. No table/PDF read here; upstream structure validation precedes use.

<a id="symbol--resolved-policy"></a>
### `landscout.stages.interpret_bess_zoning._resolved_policy`

Source lines 828–838. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _resolved_policy(
    policy: BessZoningPolicyConfig | str | Path,
) -> BessZoningPolicyConfig:
```

Existing BessZoningPolicyConfig is model_dump(mode="python") then model_validate; any Exception in that branch becomes chained BessZoningPrecheckError. Otherwise delegate to path loader. Never trust a supplied frozen model without reconstruction; no warnings="error" argument or arbitrary compiled-policy interface.

<a id="symbol--validate-policy-lock"></a>
### `landscout.stages.interpret_bess_zoning._validate_policy_lock`

Source lines 841–863. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _validate_policy_lock(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> None:
```

Compare six configured values to index document/archive/PDF/index hashes and structure complete hash/profile in declared order. Return None or first BessZoningPrecheckError naming mismatch. Equality comparisons, not physical byte validation.

<a id="symbol--exact-id-series"></a>
### `landscout.stages.interpret_bess_zoning._exact_id_series`

Source lines 866–872. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _exact_id_series(series: pd.Series, label: str, *, unique: bool) -> tuple[str, ...]:
```

Visit Series.tolist in order; apply factual exact-string guard; optionally require uniqueness via required keyword-only unique flag. Return tuple[str,...]; no defaults, trimming or mutation of Series.

<a id="symbol--validate-parcels"></a>
### `landscout.stages.interpret_bess_zoning._validate_parcels`

Source lines 875–945. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _validate_parcels(
    index: PlanningRegulationIndex,
    parcels: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
```

Require GeoDataFrame, unique columns, 12 required factual names and no precheck-name collision; CRS and active geometry named geometry; exact unique parcel IDs; nonnull/nonempty/valid Polygon or MultiPolygon; five nonnegative Integral feature counts; both planning and planning-feature document/archive lineage pairs equal index. Return deep frame copy. CRS inspection errors are locally wrapped; other explicit guards use BessZoningPrecheckError. No local reprojection/repair/Z-or-M guard or spatial overlay.

<a id="symbol--validate-zones"></a>
### `landscout.stages.interpret_bess_zoning._validate_zones`

Source lines 948–975. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _validate_zones(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
) -> pd.DataFrame:
```

Require DataFrame with unique columns and six identity/lineage columns; deep copy; unique planning_zone_id and source_zone_id, exact raw labels (duplicates allowed), matching document/archive and exact nonblank source_layer. Return copy with extra columns/index retained. Does not itself validate geometry; public GPU gate does.

<a id="symbol--validate-relations"></a>
### `landscout.stages.interpret_bess_zoning._validate_relations`

Source lines 978–1084. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _validate_relations(
    index: PlanningRegulationIndex,
    parcels: gpd.GeoDataFrame,
    zones: pd.DataFrame,
    relations: pd.DataFrame,
) -> pd.DataFrame:
```

Require unique-column DataFrame and 13 fields, copy, reject duplicate parcel/zone pairs and unknown parcels/zones; compare exact source ID/raw label/layer to zone. AREA_OVERLAP requires positive area, TOUCH_ONLY exactly zero; only these types. Finite nonnegative areas/shares, positive parcel/zone denominators; excess area and share-derived area error must stay within technical_overlay_tolerance(reference area). Compare document/archive/layer, return copy retaining order/index/extra columns. No summed coverage, union, percentage averaging or business suitability threshold; local guards raise BessZoningPrecheckError.

<a id="symbol--zone-mapping-input-sha256"></a>
### `landscout.stages.interpret_bess_zoning._zone_mapping_input_sha256`

Source lines 1087–1108. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _zone_mapping_input_sha256(
    zones: pd.DataFrame,
    structure: PlanningRegulationStructureResult,
) -> str:
```

Hash domain landscout.bess_zoning.zone_mapping_input with six selected zone identity/lineage columns and all structure.zone_mapping columns in actual order. Uses frame payloads, including index and GeoDataFrame CRS metadata if applicable, not selected zone geometry unless included (it is not).

<a id="symbol--zone-chapter-rows"></a>
### `landscout.stages.interpret_bess_zoning._zone_chapter_rows`

Source lines 1111–1129. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _zone_chapter_rows(
    structure: PlanningRegulationStructureResult,
) -> list[dict[str, object]]:
```

Filter structure.sections to ZONE_CHAPTER in source order; require exact unique chapter labels and section IDs. Return list of row dicts. Both duplicate labels (used or unused) and duplicate IDs raise BessZoningPrecheckError; caller input unchanged.

<a id="symbol--required-section-ids-by-chapter"></a>
### `landscout.stages.interpret_bess_zoning._required_section_ids_by_chapter`

Source lines 1132–1165. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _required_section_ids_by_chapter(
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
) -> dict[str, tuple[str, ...]]:
```

For every observed unique chapter and every policy required article in declared order, require exactly one ARTICLE with that chapter label AND parent section ID AND exact article_number_raw. Return dict label -> tuple of section IDs in required-article order. Missing/duplicate/wrong-parent counts raise BessZoningPrecheckError even for INCOMPLETE review; does not require every possible article in the regulation.

<a id="symbol--validate-evidence-occurrence-uniqueness"></a>
### `landscout.stages.interpret_bess_zoning._validate_evidence_occurrence_uniqueness`

Source lines 1168–1177. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _validate_evidence_occurrence_uniqueness(catalog: pd.DataFrame) -> None:
```

Require six occurrence columns then reject duplicated (chapter label, section ID, page, fragment SHA, excerpt start/end). Return None; local BessZoningPrecheckError. This key does not include evidence ID/kind/direction, so changing them cannot authorize duplicate occurrences.

<a id="symbol--validate-policy-evidence"></a>
### `landscout.stages.interpret_bess_zoning._validate_policy_evidence`

Source lines 1180–1384. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

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

Return TWO items: chapter-label -> section-row dict, and 30-column evidence catalog. Build section/fragment lookups, require exact policy/observed chapter set, derive reverse route links and required article IDs. Review sections must exist and be GENERAL or correct chapter/ARTICLE parent; complete reviews must include all required IDs. Each evidence must belong to an explicitly reviewed section, resolve section/page fragment, match fragment SHA, exact [start:end] quote and UTF-8 quote SHA, exact full-rule slice/SHA and relative quote slice. GENERAL can be scoped in multiple chapters. Catalog follows policy chapter/evidence order, reverse link pairs sorted; five position/page columns int64 and decision_linked bool. Reject duplicate IDs/occurrences. policy_hash and links are required inputs; _build_result discards the returned chapter dict. Local lookups/rows only, no original PDF access.

<a id="symbol--validate-mapping"></a>
### `landscout.stages.interpret_bess_zoning._validate_mapping`

Source lines 1387–1424. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _validate_mapping(
    structure: PlanningRegulationStructureResult,
    zones: pd.DataFrame,
) -> pd.DataFrame:
```

Deep-copy factual mapping; require raw-label set equal zones, unique mapping labels, EXACT/CONFIG_ALIAS only, and resolved label -> matched section ID equal unique chapter map. Unresolved/ambiguous mappings fail with BessZoningPrecheckError, not UNKNOWN fallback. No prefix inference or raw-label rewriting.

<a id="symbol--lineage"></a>
### `landscout.stages.interpret_bess_zoning._lineage`

Source lines 1427–1444. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _lineage(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> dict[str, object]:
```

Return ten named metadata values: two scope constants, profile/policy_hash, index document/archive/PDF/index hash, structure complete hash/profile. All four inputs required. Propagates identity, does not validate/recompute hashes or perform I/O.

<a id="symbol--build-chapter-policy"></a>
### `landscout.stages.interpret_bess_zoning._build_chapter_policy`

Source lines 1447–1503. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _build_chapter_policy(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
```

Build 24 columns in factual chapter order, using validated policy by label and required-section map. Preserve policy order of reviewed/evidence/decision/context tuples; missing required IDs retain configured required-article order. Copy declared status/confidence/rationale, add lineage; evidence_count int64. Return new DataFrame, no source mutation; missing dictionary keys in malformed private calls are not locally wrapped.

<a id="symbol--route-status"></a>
### `landscout.stages.interpret_bess_zoning._route_status`

Source lines 1506–1513. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _route_status(route_kind: RouteKind) -> ChapterStatus:
```

Map four route kinds to chapter status: DIRECT potential, CONDITIONAL and RESTRICTION_EXCEPTION conditional, DIFFICULTY_ONLY difficult. Return literal; invalid private input raises ordinary KeyError (no fallback/wrapper). Does not consider chapter completeness or confidence.

<a id="symbol--build-route-assessments"></a>
### `landscout.stages.interpret_bess_zoning._build_route_assessments`

Source lines 1516–1543. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _build_route_assessments(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
```

Create 18-column DataFrame in policy chapter/route order; copy ordered evidence-role tuples and configured note, derive per-route status, add completeness/lineage. Reject duplicate route IDs with BessZoningPrecheckError. No explicit dtype cast; route status can remain derived even when chapter INCOMPLETE is UNKNOWN.

<a id="symbol--build-evidence-route-links"></a>
### `landscout.stages.interpret_bess_zoning._build_evidence_route_links`

Source lines 1546–1587. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _build_evidence_route_links(
    index: PlanningRegulationIndex,
    structure: PlanningRegulationStructureResult,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> pd.DataFrame:
```

Build 16-column rows for positive, condition, difficulty memberships with expected direction and lineage. Nonempty frame stable-mergesort by route_id/evidence_id and reset index; reject duplicate route/evidence pairs. Context not linked. Return new DataFrame; no explicit dtype casts, no legal applicability validation.

<a id="symbol--build-source-zone-policy"></a>
### `landscout.stages.interpret_bess_zoning._build_source_zone_policy`

Source lines 1590–1627. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

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

Use chapter_policy indexed by resolved label, zones grouped by raw label without sorting, and mapping row order. Each raw label must have exactly one source layer (otherwise BessZoningPrecheckError). Copy chapter status/confidence and all/decision/context evidence tuples into 20-column source-label table with lineage. No zone geometry or parcel aggregate here; malformed private lookups may raise KeyError.

<a id="symbol--build-parcel-zone-interpretations"></a>
### `landscout.stages.interpret_bess_zoning._build_parcel_zone_interpretations`

Source lines 1630–1676. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

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

Select AREA_OVERLAP relations in their existing order; look up source-label policy; build 23-column plain DataFrame with exact IDs/raw and resolved labels, float area m2/share percent, statuses/confidence and tuple evidence/lineage. TOUCH_ONLY absent. Empty output explicitly float64 for two metrics and object otherwise. Nonempty construction infers dtypes. No union, spatial join or mutation.

<a id="symbol--is-null"></a>
### `landscout.stages.interpret_bess_zoning._is_null`

Source lines 1679–1686. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _is_null(value: object) -> bool:
```

Return True for None/pd.NA; otherwise pd.isna and only scalar bool/np.bool_ truth counts. Catch TypeError/ValueError as False; array-like null masks yield False. Used for absent dominant ID, not universal canonicalization.

<a id="symbol--build-parcel-output"></a>
### `landscout.stages.interpret_bess_zoning._build_parcel_output`

Source lines 1689–1806. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _build_parcel_output(
    parcels: gpd.GeoDataFrame,
    relations: pd.DataFrame,
    interpretations: pd.DataFrame,
    policy: BessZoningPolicyConfig,
    policy_hash: str,
) -> gpd.GeoDataFrame:
```

Deep-copy parcels and append 15 fields. Group positive interpretations and count touch-only relations. With no positive group, require null dominant ID, set UNKNOWN, null dominant status/confidence, zero positive/distinct/different counts and empty evidence tuples. Otherwise stable sort area descending/zone ID ascending, require factual dominant ID agreement; unanimous positive status retained, any disagreement MIXED_REVIEW_REQUIRED regardless of dominance. Count nondominant statuses differing from dominant. Decision/context ID unions separately deduplicate and sort. Require formal review True, non-zoning interpreted False. Assign via object arrays preserving parcel order/index/CRS/geometry, cast four counts int64 and two flags bool. No overall confidence, coverage threshold, weighting, score or row rejection.

<a id="symbol--result-component-metadata"></a>
### `landscout.stages.interpret_bess_zoning._result_component_metadata`

Source lines 1809–1828. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _result_component_metadata(result: BessZoningPrecheckResult) -> dict[str, object]:
```

Return 17 metadata items including schema 5/5, scopes/profiles, upstream and input hashes, relation columns converted to list and touch count. Excludes seven output hashes and complete hash to avoid cycles. No validation or hashing by itself.

<a id="symbol--result-frame-sha256"></a>
### `landscout.stages.interpret_bess_zoning._result_frame_sha256`

Source lines 1831–1843. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _result_frame_sha256(
    domain: str,
    result: BessZoningPrecheckResult,
    frame: pd.DataFrame,
    columns: Sequence[str],
) -> str:
```

Hash required domain, 17 result metadata items and frame payload for supplied ordered columns. Returns hex str. No Parquet bytes, dtype signature or file write.

<a id="symbol--complete-result-sha256"></a>
### `landscout.stages.interpret_bess_zoning._complete_result_sha256`

Source lines 1846–1867. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _complete_result_sha256(result: BessZoningPrecheckResult) -> str:
```

Hash landscout.bess_zoning.precheck_result, the same 17 metadata items and seven existing output frame hashes. It commits propagated component values, not recomputed frames; _result_with_hashes refreshes them first.

<a id="symbol--result-with-hashes"></a>
### `landscout.stages.interpret_bess_zoning._result_with_hashes`

Source lines 1870–1921. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _result_with_hashes(
    result: BessZoningPrecheckResult,
) -> BessZoningPrecheckResult:
```

dataclasses.replace with seven computed frame hashes under evidence_catalog, evidence_route_links, route_assessments, chapter_policy, source_zone_policy, parcel_zone_policy, parcel_output domains; then replace again with complete result SHA. Return new envelope sharing frame objects, not deep immutable frames. No source completeness check or IO.

<a id="symbol--build-result"></a>
### `landscout.stages.interpret_bess_zoning._build_result`

Source lines 1924–2027. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

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

Validate index; invoke full structure/fragments validator once; six policy locks; parcel/zone/relation copies; mapping; policy SHA; build routes and links; unpack (_, evidence_catalog); build chapter/source/positive relation/parcel tables. Retain all relation columns in order, calculate four input/config commitments and touch count; construct 32-field envelope then refresh seven frame hashes and complete hash. Return result. Does not receive planning_document or run GPU gate itself; no local catch; public callers wrap delegated failures. Textual rebuild uses extracted index, not original PDF.

<a id="symbol--compare-frames"></a>
### `landscout.stages.interpret_bess_zoning._compare_frames`

Source lines 2030–2043. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _compare_frames(
    actual: pd.DataFrame,
    expected: pd.DataFrame,
    columns: Sequence[str],
    label: str,
) -> None:
```

Require actual/expected full ordered columns equal specified sequence, then compare canonical frame payloads. Return None or BessZoningPrecheckError. Row/index values/names/CRS/geometry name included; dtype/index-class identity not compared. No broad local exception wrapper.

<a id="symbol--compare-results"></a>
### `landscout.stages.interpret_bess_zoning._compare_results`

Source lines 2046–2300. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

```python
def _compare_results(
    result: BessZoningPrecheckResult,
    expected: BessZoningPrecheckResult,
    original_parcels: gpd.GeoDataFrame,
) -> None:
```

Require result isinstance; duplicate catalog occurrence check BEFORE 25 metadata/scalar comparisons. Require positive supported schemas, nonnegative touch count, exact tuple of exact relation-column strings, syntactically valid 16 hashes. Compare seven frames and original parcel-column prefix/payload; statuses/confidence membership; route-role arrays and exact link set, reverse arrays/bool, context versus decision references; formal-review/non-zoning flags and review scope. Return None, explicit BessZoningPrecheckError; unexpected private exceptions unwrapped. In public validation expected is freshly rebuilt, but builder passes result as both sides: that is not a second independent reconstruction.

<a id="symbol-validate-bess-zoning-precheck"></a>
### `landscout.stages.interpret_bess_zoning.validate_bess_zoning_precheck`

Source lines 2303–2347. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

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

Nine required positional-or-keyword arguments, no defaults; return None. First delegated physical normalized-zoning gate, then policy resolve/revalidate, _build_result from all textual/factual inputs, then compare supplied result with expected. Preserve own error; wrap PlanningRegulationStructureError with factual-structure message, PlanningZoningError with factual-GPU message, all other Exception with safe-validation message/cause. Index errors reach the generic wrapper when directly raised. Can read GPU files through delegate and YAML paths; does not reopen original PDF or write artifacts.

<a id="symbol-interpret-bess-zoning"></a>
### `landscout.stages.interpret_bess_zoning.interpret_bess_zoning`

Source lines 2350–2394. Kind: function. Owner: `landscout.stages.interpret_bess_zoning`.

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

Eight required positional-or-keyword arguments, no defaults; return BessZoningPrecheckResult. GPU normalized-zoning gate precedes policy resolution; build once, then _compare_results(result,result,parcels), return. Same own/structure/GPU exception distinctions as public validator; generic message is "BESS zoning precheck could not be built safely". Produces parcel PRECHECK statuses, not legal authorization/refusal, exclusion or score. No module-local manifest/writer/load-result path.

## Complete source snapshot

Exact full Git-content UTF-8 source. Byte identity supports provenance, not semantic correctness of prose by itself.

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
