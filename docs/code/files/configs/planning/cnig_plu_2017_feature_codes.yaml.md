# `configs/planning/cnig_plu_2017_feature_codes.yaml`

## File identity

- Repository path: `configs/planning/cnig_plu_2017_feature_codes.yaml`
- File type: offline YAML configuration; observed-pair dictionary, not BESS policy.
- Source SHA256: `77407429fd414eece8f6b20ca4da587aac76ab6b0b93e02f148622ab85ee253e`
- Source SHA256 basis: `git-content`
- Exact source size: 4,934 UTF-8 bytes, LF endings, including final newline.
- R4 documentation fidelity review: [receipt](../../../audit/R4_CNIG_CONFIGURATION.md);
  independent acceptance PENDING. YAML bytes are unchanged.

<a id="r4-purpose"></a>

## Purpose and authority

This profile supplies twelve exact CNIG PLU v2017 family/type/subtype meanings
observed in the Muret pilot: four INFORMATION and eight PRESCRIPTION records.
It is neither the entire official nomenclature nor a universal BESS policy.
The profile name identifies a snapshot; it does not restrict the whole product
to Muret. There is no geometry-kind selector, spatial threshold or policy outcome
in this file.

Three versions must not be conflated: profile schema **2** is the accepted YAML
model shape; **2017** identifies the planning standard; result-hash schema **5**
belongs to the consuming coded-result envelope, not this YAML.

The [loader](../../src/landscout/stages/resolve_planning_feature_codes.py.md#load_cnig_feature_code_profile)
reads local bytes only. Exact source URLs bind strings; it does not fetch them,
validate current law or independently establish official meaning.
[DEV_LOG 7D.5A](../../../../DEV_LOG.md#step-7d5a--resolve-official-cnig-meanings-for-planning-feature-codes)
reports inspection of the two GPU tables on 2026-08-12.
[7D.5A.1](../../../../DEV_LOG.md#step-7d5a1--harden-cnig-snapshot-fidelity-and-public-coding-contracts)
records the reviewed v2 canonical-display correction for INFORMATION 99/00 and
PRESCRIPTION 15/00, and pins all twelve records. That historical report is
preserved, not a new R4 web/legal verification or a newly supplied independent
review receipt. A retained byte snapshot of each external table and a complete
original independent verdict are not established by the evidence read here.
EP 7F.1C.1 research and its pending semantic review are separate.

<a id="r4-fields"></a>

## Complete field contract

Owners are the actual
[profile](../../src/landscout/stages/resolve_planning_feature_codes.py.md#cnigfeaturecodeprofile),
[source URLs](../../src/landscout/stages/resolve_planning_feature_codes.py.md#officialsourceurls)
and [record](../../src/landscout/stages/resolve_planning_feature_codes.py.md#cnigfeaturecoderecord)
models. All **8 root fields**, **2 source fields** and **7 fields per record**
are required; none has a default. Nullable is not optional-to-omit.
There are **92 scalar leaves**: 6 root scalars + 2 URL scalars + 12 × 7 record
scalars. The field rules below and the twelve-row value table cover every leaf.

Hash notation: **R** = ordered records hash; **P** = complete parsed profile hash;
**O** = result payload, directly or through the propagated P digest. All fields
enter P; the seven record fields enter R. No value is measured geometry.

| Profile field | Exact YAML representation → runtime value/type | Validation, consumer and hash effect |
|---|---|---|
| `schema_version` | plain integer `2` → `int` | `StrictInt` plus equality to PROFILE_SCHEMA_VERSION=2; booleans, numeric strings and other versions are not accepted. P; copied to result.profile_schema_version and O metadata. |
| `profile` | plain `cnig_plu_2017_muret_observed_pairs_v2` → `str` | `StrictStr`, min length 1, nonempty and equal to its stripped value. Identifier is not pinned to this one name by the model. P; dictionary/profile columns and O metadata. |
| `standard_model` | plain `CNIG PLU v2017` → `str` | Exact Literal. Consumer compares it with the unique planning-document standard before factual validation. P; dictionary and result metadata/O. |
| `official_text_normalization` | plain `GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1` → `str` | Exact Literal naming the implemented NFC/whitespace check; not a selectable repair mode. P; O through profile digest only. |
| `official_sources` | mapping → frozen `OfficialSourceUrls` | Both required StrictStr fields below; extra keys forbidden. P; no standalone result source-map column. |
| `retrieval_date` | unquoted `2026-08-12` → `datetime.date` | SafeLoader parses this date; Pydantic field is `date`, not StrictStr/strict date. ISO date strings are also accepted in the synthetic tests. No custom freshness, exact-date or relation-to-download check. P emits ISO date; O through profile digest only. |
| `canonical_records_sha256` | plain `5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c` → `str` | StrictStr, full lowercase ASCII hex match `[0-9a-f]{64}`, equality to recomputed R. Not part of R itself; P and therefore O. |
| `records` | ordered YAML sequence of 12 mappings → `tuple[CnigFeatureCodeRecord, ...]` | At least one record, not hardcoded to twelve; unique keys already lexically ordered by family/type/subtype; mismatch rejects, never sorts. Ordered content enters R and P; all records enter output dictionary, even if no feature references them. |

Exact family endpoint identities (plain YAML scalars; runtime **str**, not HttpUrl):

| Source field / model owner | Exact checked-in value | Allowed domain and use |
|---|---|---|
| `official_sources.prescription` / OfficialSourceUrls | `https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType` | Exact equality to PRESCRIPTION_OFFICIAL_SOURCE_URL; P, not R. Each PRESCRIPTION record independently requires this same constant. |
| `official_sources.information` / OfficialSourceUrls | `https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType` | Exact equality to INFORMATION_OFFICIAL_SOURCE_URL; P, not R. Each INFORMATION record independently requires this same constant. |

This is exact-string validation, not a generic URL-parser/origin allowlist.
Swapped families, other paths, ports, credentials, queries, fragments, HTTP,
host spellings or trailing slashes differ from the constants and fail.

| Record field / owner CnigFeatureCodeRecord | YAML representation → runtime type | Domain, meaning and output use (all enter R/P) |
|---|---|---|
| `feature_family` | plain INFORMATION or PRESCRIPTION → `str` | Exact Literal of those two values; selects endpoint and first lookup-key component. Copied to dictionary; factual feature family is preserved. |
| `type_code` | double-quoted two-digit value → `str` | StrictStr with full `[0-9]{2}` match, preserving leading zeros; second key component/dictionary field. No integer-to-string conversion. |
| `subtype_code` | double-quoted two-digit value → `str` | Same strict rule; third key component. `"00"` is a literal subtype, neither wildcard nor null; no fallback. |
| `official_label` | plain text → `str` | StrictStr, nonempty, already canonical official display text. Dictionary field; copied to official_code_label for a known pair. |
| `legal_reference` | plain text or true `null` → `str` or `NoneType` | Required but nullable; non-null text must already be canonical. Dictionary field; copied to official_legal_reference, retaining true null. See boundary discrepancy below. |
| `regulation_or_annex_reference` | plain text or true `null` → `str` or `NoneType` | Same required/nullable text rule; dictionary field; copied to official_regulation_reference. No parsing of cited article applicability. |
| `official_source_url` | plain family endpoint → `str` | StrictStr and exact family-constant equality; dictionary field; copied to official_code_source_url. Twelve occurrences, only two distinct URLs. |

Canonical official display text means exact equality to
`" ".join(unicodedata.normalize("NFC", text).split())`, together with
nonempty/no-edge-whitespace checking. Internal Unicode whitespace must already
be one ASCII space; decomposed accents, repeated spaces and newlines fail.
The loader rejects, not repairs, supplied text; case, punctuation and accents are
not reinterpreted. This is distinct from factual GPU LIBELLE preservation:
[A-003](../../../../project/BACKLOG_AND_GAPS.md#application-findings) remains OPEN.

True YAML `null` is Python None, not the string `"None"`.
**Observed boundary discrepancy A-004:** the record model's optional-text
validator does not ban canonical strings `"None"`, `"nan"` or `"<NA>"`;
the result dictionary's
[_validate_nullable_official_value](../../src/landscout/stages/resolve_planning_feature_codes.py.md#_validate_nullable_official_value)
explicitly rejects these literals. R4 reproduced the `"None"` model/helper
difference in memory only. The checked-in references contain no such strings;
no source-complete resolver run or production fix is claimed.

<a id="r4-records"></a>

## All twelve checked-in records

Rows are in exact file/lookup order. **I** means the exact INFORMATION endpoint
above; **P** means the exact PRESCRIPTION endpoint above, not an alternative URL.
There are 24 legal/annex cells: **22 non-null strings and 2 true nulls**.
These are recorded display references, not fresh legal findings.

| records index | feature_family | type_code | subtype_code | official_label | legal_reference | regulation_or_annex_reference | official_source_url |
|---|---|---|---|---|---|---|---|
| 0 | INFORMATION | `02` | `00` | Zone d'aménagement concerté | L311-1 code de l’urbanisme | R151-52 8° | I |
| 1 | INFORMATION | `14` | `00` | Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit) | L571-10 code de l’environnement | R151-53 5° | I |
| 2 | INFORMATION | `27` | `00` | Plan d'exposition au bruit des aérodromes | L112-6 code de l’urbanisme | R151-52 2° | I |
| 3 | INFORMATION | `99` | `00` | Autre périmètre, secteur, plan, document, site, projet, espace. | `null` | `null` | I |
| 4 | PRESCRIPTION | `01` | `00` | Espace boisé classé | L113-1 | R151-31 1° | P |
| 5 | PRESCRIPTION | `05` | `00` | Emplacement réservé | L151-41 1° à 3° | R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1° | P |
| 6 | PRESCRIPTION | `07` | `00` | Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique | L151-19 et L151-23 | R151-41 3° Et R151-43 | P |
| 7 | PRESCRIPTION | `07` | `04` | Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique | L151-23 | R151-43 5° | P |
| 8 | PRESCRIPTION | `15` | `00` | Règles d’implantation des constructions | L151-17 et L151-18 | R151-39 dernier al. | P |
| 9 | PRESCRIPTION | `15` | `01` | Implantation des constructions par rapport aux voies et aux emprises publiques | L151-17 et L151-18 | R151-39 | P |
| 10 | PRESCRIPTION | `17` | `00` | Secteur à programme de logements mixité sociale en zone U et AU | L151-15 | R151-38 3° | P |
| 11 | PRESCRIPTION | `18` | `00` | Périmètre comportant des orientations d’aménagement et de programmation (OAP) | L151-6 et L151-7 | R151-6 à R151-8-1 | P |

<a id="r4-loading"></a>

## Loading, immutability and errors

Actual public loader signature:

```python
def load_cnig_feature_code_profile(path: str | Path) -> CnigFeatureCodeProfile:
```

No default path: the caller supplies one; relative paths are relative to the
process working directory. Path construction/read_bytes occur inside the loader's
try block. No write, network, GIS, GPU download or environment change occurs.

[Strict YAML decoding](../../src/landscout/common/strict_yaml.py.md) uses a
SafeLoader subclass, accepts exact str/bytes, decodes bytes as UTF-8, flattens
mapping merges and rejects duplicate constructed keys at every depth, including
duplicates after flattening. Unhashable keys raise StrictYamlError. Invalid UTF-8,
TypeError, ValueError and YAML parser/constructor errors are controlled; unsafe
Python constructors are not enabled. A non-mapping top level is rejected by this
profile loader.

Do not borrow strict-JSON semantics: this YAML helper does **not** contain a
general nonfinite-number rejection. SafeLoader can construct `.nan`/`.inf`;
this profile's strict string/integer, Literal, date and nested-model fields reject
inapplicable numeric values. Canonical hashing additionally uses allow_nan=False.

Every owning model inherits `ConfigDict(extra="forbid", frozen=True)`, **not**
model-wide strict=True. StrictInt/StrictStr, Literal and explicit validators
supply the field-specific rules. YAML lists/mappings are parsed into a tuple and
frozen nested models; date parsing is allowed. There is no list/dict/set in the
validated public field graph. Normal field assignment and tuple mutation fail;
input dictionaries/lists are not retained as mutable collection aliases.
Dumped Python/JSON data is a separate serialization, not writable model state.
Unvalidated model_construct/model_copy updates are not trustworthy: consumers'
[_resolved_profile](../../src/landscout/stages/resolve_planning_feature_codes.py.md#_resolved_profile)
dumps a supplied profile with mode="python", warnings="error", reconstructs and
revalidates it. A path instead goes through the loader.

Direct model validation yields Pydantic ValidationError (a ValueError) for
missing/extra fields or validator failures. The loader preserves existing
PlanningFeatureCodeError, translates StrictYamlError with its message, and wraps
other exceptions (including path/read/model failures) as
PlanningFeatureCodeError("CNIG feature-code profile is invalid"), with cause.
In-memory reconstruction wraps failures as
PlanningFeatureCodeError("In-memory CNIG feature-code profile is invalid").
No acceptance proves that a URL was visited, a reference remains current or a
parcel satisfies its requirements.

<a id="r4-hashes"></a>

## Three identities, not one

| Identity | Actual input and current SHA256 |
|---|---|
| Documentation Source SHA256 | Exact Git-stored YAML bytes, including formatting: `77407429fd414eece8f6b20ca4da587aac76ab6b0b93e02f148622ab85ee253e`. Not calculated as a raw-file hash by the runtime loader; not Git's blob OID. |
| Ordered records R | [_records_sha256](../../src/landscout/stages/resolve_planning_feature_codes.py.md#_records_sha256): array of [_record_payload](../../src/landscout/stages/resolve_planning_feature_codes.py.md#_record_payload) objects in existing tuple order: `5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c`. Recomputed during profile validation. |
| Complete profile P | [_profile_sha256](../../src/landscout/stages/resolve_planning_feature_codes.py.md#_profile_sha256): complete `profile.model_dump(mode="json")`, including schema/profile/standard/normalization, both source URLs, ISO retrieval date, canonical_records_sha256 and records: `5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee`. Computed by the resolver and by the R4 read-only check. |

_record_payload contains exactly feature_family, type_code, subtype_code,
official_label, legal_reference, regulation_or_annex_reference,
official_source_url: the seven record fields above, no geometry/status/profile.
R/P use UTF-8 JSON, ensure_ascii=False, allow_nan=False, sort_keys=True,
separators=(",", ":"). Object keys are sorted for serialization; record order is
preserved and validated, not sorted by _records_sha256. True null becomes JSON
null; tuple records serialize as an array. No Python repr/class/address enters
these hashes. Formatting-only YAML changes can alter the documentation hash
without altering R/P. Metadata-only changes can alter P without altering R.
A changed record must have a matching R but still requires semantic review;
a recomputable digest is not an external authenticity signature.

P is propagated into result metadata and every dictionary/catalog/relation row.
Result component hashes include that metadata and frame payloads; the complete
schema-5 result digest binds the component digests. Thus metadata not copied as
its own frame column still affects O through P. No hash/schema changed in R4.

<a id="r4-resolution"></a>

## Exact-pair consumption and trust boundaries

Actual public API (not the compact wrapper used inside tests):

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

It resolves/revalidates the profile, checks the planning standard, invokes the
source-complete normalized-input validator once, and passes that validation to
_build_result so it is not repeated there. It copies factual frames, builds the
dictionary, performs exact tuple lookup and validates the result envelope.
[Physical validation](../../src/landscout/stages/enrich_planning_features.py.md#r3-validate-normalized-planning-feature-inputs)
belongs to the upstream validator, not this YAML or a URL lookup.

_lookup keys are (feature_family, type_code, subtype_code).
_coded_catalog queries (feature_family, type_code_raw, subtype_code_raw).
Conceptual examples with this exact file: PRESCRIPTION/07/04 resolves;
PRESCRIPTION/07/99 stays UNKNOWN_CODE_PAIR although 07/00 exists.
No type-only, prefix, fuzzy or cross-family fallback; raw code strings are not
modified. The code dictionary holds all twelve rows plus profile, profile_sha256
and standard_model.

| Appended field | Exact match | Missing exact pair |
|---|---|---|
| official_code_status | RESOLVED_OFFICIAL | UNKNOWN_CODE_PAIR |
| official_code_label | record.official_label | true null |
| official_legal_reference | record.legal_reference (may be null) | true null |
| official_regulation_reference | record.regulation_or_annex_reference (may be null) | true null |
| official_code_source_url | record.official_source_url | true null |
| official_code_profile | profile.profile | same profile.profile |
| official_code_profile_sha256 | P | same P |

Relations receive these same seven fields from their referenced coded feature ID.
Strings use Pandas "str" columns; true nulls may display as the dtype's missing
sentinel, not literal null-replacement strings. Factual columns, row order, raw
codes and geometry are preserved in copies; frozen result envelopes do not make
their DataFrames deeply immutable.

[Envelope validation](../../src/landscout/stages/resolve_planning_feature_codes.py.md#validate_planning_feature_code_result_envelope)
checks local schemas, nonempty ordered dictionary, exact meanings/statuses,
profile lineage, relation-to-feature agreement and hashes without physical reads.
[Source-complete validation](../../src/landscout/stages/resolve_planning_feature_codes.py.md#validate_planning_feature_code_result)
first checks that envelope, then re-resolves the supplied profile and independently
rebuilds from all factual/source inputs before scalar/frame comparison.
Intrinsic coherence alone is not physical authority.

The separate [BESS policy compiler](../../src/landscout/stages/bess_planning_feature_policy.py.md#compile_bess_planning_feature_policy)
validates source locks, the source-complete coded result, exact dictionary/policy
pair-set equality and expected label/references. Its policy entries supply
precheck status, priority, confidence, rationale and human action, not this YAML.
A CNIG match alone does not authorize construction, establish BESS compatibility,
require parcel exclusion or determine a complete regulatory regime.

<a id="r4-tests"></a>

## Existing test evidence and limits

The following are source-read assertions, **not tests executed in R4**.
Links point to the owning test sections; reading these definitions does not
close the whole resolver/test inventory unit.

| Existing test | Literal setup and asserted boundary |
|---|---|
| [checked-in snapshot](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_checked_in_official_snapshot_is_complete_for_observed_muret_pairs) | Loads this path; compares all 12 seven-field tuples, profile metadata, endpoints, retrieval date, R and P constants. Offline equality, not fresh official-table evidence or exhaustive nomenclature coverage. |
| [exact family/leading zeros](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_exact_family_pair_resolution_and_leading_zeros) | Synthetic dictionary and real temporary GPKGs; asserts distinct INFORMATION 02/00, PRESCRIPTION 07/00 and 07/04 labels and unchanged raw 07/04 strings. |
| [no fallback](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_no_type_only_or_cross_family_fallback_and_unknown_is_retained) | Removes PRESCRIPTION 07/04 and INFORMATION 99/00, recomputes R, checks both features retained/unknown and line label null. No competing same-code record in another family is introduced, so this is not an isolated cross-family collision test despite its name; it does not assert all four null meaning fields. |
| [model_copy hash](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_in_memory_profile_model_copy_with_wrong_hash_is_revalidated), [model_construct schema](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated), [model_construct duplicate](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated) | Supplies forged profiles to public resolution; expects controlled profile errors. Profile rejection precedes source-complete validation in the resolver; fixture construction itself has already performed local physical IO. |
| [endpoint identity](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_official_family_endpoints_require_exact_identity) | Ten root-and-record coordinated URL mutations, recomputed R; model rejection. Multiple nested errors can coexist; no claim that only the record endpoint guard fired. |
| [canonical text](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_official_text_must_already_be_canonical) | Repeated spaces/decomposed accent/newline/edge space in four label/reference cases; R recomputed first; model rejection, not hash mismatch or repair. |
| [malformed code](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_malformed_code_is_rejected) | Changes type_code to "1", "001", "A1", padded "01" or integer 1; expects ValueError. Does not separately parameterize subtype_code at the profile-model boundary. |
| [duplicate/hash](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_duplicate_pair_and_profile_hash_mutation_are_rejected), [record order](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_record_order_must_be_deterministic) | Duplicate append rejects before hash comparison; wrong R rejects; reversed records reject deterministic order, not automatic sorting. Test helper _records_hash sorts its fixture inputs; production _records_sha256 does not. |
| [host/extra field](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_wrong_official_host_and_unknown_field_are_rejected), [duplicate YAML](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_duplicate_yaml_key_is_rejected), [valid YAML](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_yaml_snapshot_loads_strictly) | Wrong root endpoint and extra semantic_policy fail; duplicate schema_version=1 keys fail at decoding before unsupported-version validation; safe_dump synthetic payload reload equals validated synthetic profile. |
| [dictionary intrinsic rows](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_schema_v5_dictionary_rows_are_intrinsically_validated) | Rehashes dictionary mutations including malformed type/subtype, family/URL/profile, duplicate/order and literal "None" reference; checks envelope rejection. This tests result rows, not profile-model literal-null rejection (A-004). |
| [physical validation call counts](../../tests/unit/test_resolve_planning_feature_codes.py.md#test_resolver_runs_heavy_factual_validation_once_and_public_validator_repeats) | Spies delegate to real physical revalidation/relation builder after fixture construction; counts 1/1 after resolution, 2/2 after separate public validation. Not an official GPU acquisition. |
| [immutable field graph](../../tests/unit/test_deep_immutability.py.md#test_all_loaded_trust_families_have_no_reachable_mutable_collection), [stable hashes](../../tests/unit/test_deep_immutability.py.md#test_canonical_config_and_policy_hashes_match_starting_commit) | CNIG is one loaded family in recursive field-graph checks; P is pinned unchanged. The separate immediate sequence-mutation test uses scan AOI, and alias tests use AOI/structure, not a dedicated CNIG alias mutation. |

The inspected synthetic helpers write/read tiny local GPKGs and a schema-2
extraction manifest with a fabricated ZIP envelope; geometries are synthetic
EPSG:2154 coordinates, not surveyed Muret geography. Test-local wrappers insert
_integration_parcels into the real seven-argument API. No R4 pytest, GPU/EP run,
artifact rebuild or external page read was performed. Dedicated profile cases
for every missing/nullable/date/nonfinite input are not established by this
bounded reading; this is a coverage limit, not evidence of a new defect.
A-001/A-002/A-003, previous test-evidence limitations and A-004 remain open.

<a id="r4-snapshot"></a>

## Complete exact Git-content snapshot

This single UTF-8 YAML fence reproduces all 4,934 Git-content bytes, including
the final LF. It is the source snapshot, not a claim that explanatory prose or
official meanings are certified by its digest.

```yaml
schema_version: 2
profile: cnig_plu_2017_muret_observed_pairs_v2
standard_model: CNIG PLU v2017
official_text_normalization: GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1
official_sources:
  prescription: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType
  information: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType
retrieval_date: 2026-08-12
canonical_records_sha256: 5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c
records:
  - feature_family: INFORMATION
    type_code: "02"
    subtype_code: "00"
    official_label: Zone d'aménagement concerté
    legal_reference: L311-1 code de l’urbanisme
    regulation_or_annex_reference: R151-52 8°
    official_source_url: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType
  - feature_family: INFORMATION
    type_code: "14"
    subtype_code: "00"
    official_label: Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)
    legal_reference: L571-10 code de l’environnement
    regulation_or_annex_reference: R151-53 5°
    official_source_url: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType
  - feature_family: INFORMATION
    type_code: "27"
    subtype_code: "00"
    official_label: Plan d'exposition au bruit des aérodromes
    legal_reference: L112-6 code de l’urbanisme
    regulation_or_annex_reference: R151-52 2°
    official_source_url: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType
  - feature_family: INFORMATION
    type_code: "99"
    subtype_code: "00"
    official_label: Autre périmètre, secteur, plan, document, site, projet, espace.
    legal_reference: null
    regulation_or_annex_reference: null
    official_source_url: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType
  - feature_family: PRESCRIPTION
    type_code: "01"
    subtype_code: "00"
    official_label: Espace boisé classé
    legal_reference: L113-1
    regulation_or_annex_reference: R151-31 1°
    official_source_url: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType
  - feature_family: PRESCRIPTION
    type_code: "05"
    subtype_code: "00"
    official_label: Emplacement réservé
    legal_reference: L151-41 1° à 3°
    regulation_or_annex_reference: R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1°
    official_source_url: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType
  - feature_family: PRESCRIPTION
    type_code: "07"
    subtype_code: "00"
    official_label: Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique
    legal_reference: L151-19 et L151-23
    regulation_or_annex_reference: R151-41 3° Et R151-43
    official_source_url: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType
  - feature_family: PRESCRIPTION
    type_code: "07"
    subtype_code: "04"
    official_label: Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique
    legal_reference: L151-23
    regulation_or_annex_reference: R151-43 5°
    official_source_url: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType
  - feature_family: PRESCRIPTION
    type_code: "15"
    subtype_code: "00"
    official_label: Règles d’implantation des constructions
    legal_reference: L151-17 et L151-18
    regulation_or_annex_reference: R151-39 dernier al.
    official_source_url: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType
  - feature_family: PRESCRIPTION
    type_code: "15"
    subtype_code: "01"
    official_label: Implantation des constructions par rapport aux voies et aux emprises publiques
    legal_reference: L151-17 et L151-18
    regulation_or_annex_reference: R151-39
    official_source_url: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType
  - feature_family: PRESCRIPTION
    type_code: "17"
    subtype_code: "00"
    official_label: Secteur à programme de logements mixité sociale en zone U et AU
    legal_reference: L151-15
    regulation_or_annex_reference: R151-38 3°
    official_source_url: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType
  - feature_family: PRESCRIPTION
    type_code: "18"
    subtype_code: "00"
    official_label: Périmètre comportant des orientations d’aménagement et de programmation (OAP)
    legal_reference: L151-6 et L151-7
    regulation_or_annex_reference: R151-6 à R151-8-1
    official_source_url: https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType
```
