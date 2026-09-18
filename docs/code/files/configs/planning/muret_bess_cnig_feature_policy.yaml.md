# `configs/planning/muret_bess_cnig_feature_policy.yaml`

## File identity

- Repository path: `configs/planning/muret_bess_cnig_feature_policy.yaml`
- File type: checked-in YAML policy configuration, not a Python implementation or a result table.
- Source SHA256 basis: `git-content`
- Source SHA256: `8a26fcb8ee7e2f028baca65d94c2b5be5445ba9fc4b82b9b1a21843f933f8b2a`
- Git blob at R5 input `ab7d9d41fe2444b63d31c7dc075af59cab8884f7`: `b39ed76230fd5b55e3142b031e24d5adbb762121`.
- Exact source: 10,147 UTF-8 bytes, 154 lines. R5 changes documentation only.
- [R5 execution receipt](../../../audit/R5_BESS_CNIG_POLICY.md): one offline configuration load, not source-complete compilation, independent approval or legal verification.

## 1. Purpose

This Muret profile assigns internal BESS preliminary-review classifications to twelve exact official CNIG meanings. It does not classify a parcel or read a feature's local text. The copied official label/references and the policy author's status, confidence, rationale, action and limitations are different evidence layers. CNIG endpoints and legal-reference strings do not authenticate those internal BESS judgments. `LIKELY_MATERIAL_CONSTRAINT` is not “prohibited”; `HIGH` is an allowed confidence label, not a measured probability, legal opinion or feasibility proof.

## 2. Position in LandScout architecture

The [owning implementation](../../../../../src/landscout/stages/bess_planning_feature_policy.py) is `landscout.stages.bess_planning_feature_policy`. Its loader returns `BessPlanningFeaturePolicyConfig`; its compiler consumes that config/path plus a complete coded-source context and returns a meaning-level `policy_table`. Separate [application](../../../../../src/landscout/stages/apply_bess_planning_feature_policy.py) and [aggregation](../../../../../src/landscout/stages/aggregate_bess_planning_feature_policy.py) stages use that table later. This is neither the written-zoning BESS profile nor the CNIG dictionary itself. See the unchanged [CNIG companion](cnig_plu_2017_feature_codes.yaml.md) and [planning pipeline](../../../PLANNING_PIPELINE.md).

## 3. Imports and dependencies

YAML has no imports. The loader uses Path.read_bytes, [strict YAML](../../../../../src/landscout/common/strict_yaml.py), Pydantic and the models below. The safe decoder rejects duplicate keys at every depth, including flattened merges, unhashable keys, invalid UTF-8 and YAML parse errors; it does not fetch URLs. [freeze_mapping](../../../../../src/landscout/common/immutable_mapping.py) copies the priority mapping before protecting its backing dictionary. Canonical JSON/hashing and pandas/NumPy are used by the owning module; complete compilation also invokes the [CNIG validator](../../../../../src/landscout/stages/resolve_planning_feature_codes.py). No road-policy default or scan-profile path resolution belongs to this loader.

## 4. Contract taxonomy

<a id="policy-fields"></a>

All fields are required, with no defaults. Only the two expected-reference fields per entry are nullable; “required but nullable” does not mean omission is allowed. The actual file has **10 root fields, 7 source_lock fields, 5 priority keys, 12 entries × 11 fields and 151 scalar leaves**: seven root scalars + seven lock leaves + five priorities + 132 entry leaves. Values are preserved, not repaired: no stripping, numeric code coercion or sorting on load. Strict integers exclude booleans and numeric strings; strict Booleans exclude integer/string stand-ins.

### Root fields

| Root field | Current value / shape | Input and runtime | Constraint, owner and propagation |
|---|---|---|---|
| `"schema_version"` | `1` | YAML integer → StrictInt / int | Exactly 1, not bool/string; _validate_policy. Result policy_schema_version. |
| `"profile"` | `"muret_bess_cnig_feature_policy_v1"` | YAML string → StrictStr / str | Required nonempty, no edge whitespace; not an equality pin to this name. Result and every table row policy_profile. |
| `"policy_scope"` | `"OFFICIAL_CNIG_CODE_MEANING_ONLY"` | YAML string → Literal / str | Only OFFICIAL_CNIG_CODE_MEANING_ONLY. Result and each table row. |
| `"local_feature_text_interpreted"` | `false` | YAML Boolean → StrictBool / bool | Must be false, not an enable switch; repeated in every policy row. |
| `"local_regulation_content_interpreted"` | `false` | YAML Boolean → StrictBool / bool | Must be false, not an enable switch; repeated in every policy row. |
| `"legal_conclusion_produced"` | `false` | YAML Boolean → StrictBool / bool | Must be false, not an enable switch; repeated in every policy row. |
| `"source_lock"` | seven-field mapping | YAML mapping → PolicySourceLock | Seven required fields below; all compared to coded-result identity before source revalidation. |
| `"status_priority"` | five-key mapping | YAML mapping → Mapping[PrecheckStatus, StrictInt], FrozenDict at runtime | Exactly the five allowed keys, unique strict positive integer values; no model pin to these numeric values. Entry lookup supplies table status_priority. |
| `"canonical_policy_entries_sha256"` | `"1d3e63f1123000402065b74402cb1e2295db2ac5655209ce410aaf36bfc2be91"` | YAML string → StrictStr / str | Lowercase 64-hex syntax and equality to ordered entry JSON hash; not raw YAML hash. |
| `"entries"` | twelve-entry sequence | YAML sequence → tuple[PolicyEntry, ...] | Twelve here, required but no model min_length=1; exact sorted unique triples and declared entry hash required. Compiler separately requires dictionary completeness. |

### Exact source lock

All seven fields are required and non-null. `PolicySourceLock._validate_lock` validates exact nonempty strings without edge whitespace, lowercase 64-hex hashes, and strict positive integer versions. Document/profile names are not locally fixed to these values, and positive versions are **not locally pinned to 2/5 by this lock model**. `_validate_source_lock` compares every field below with the supplied coded-result scalar; subsequent CNIG source validation proves its source context. Policy result envelopes and artifact manifests separately require CNIG schemas exactly 2/5.

| source_lock field | Exact value | YAML → runtime | Compared coded scalar |
|---|---|---|---|
| `"document_id"` | `"33edb4c9f6943c88d8d92518bff20bec"` | string → StrictStr / str | `"source_document_id"` |
| `"archive_sha256"` | `"9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93"` | string → StrictStr / str | `"source_archive_sha256"` |
| `"cnig_profile"` | `"cnig_plu_2017_muret_observed_pairs_v2"` | string → StrictStr / str | `"profile"` |
| `"cnig_profile_schema_version"` | `2` | integer → StrictInt / int | `"profile_schema_version"` |
| `"cnig_profile_sha256"` | `"5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"` | string → StrictStr / str | `"profile_sha256"` |
| `"cnig_result_hash_schema_version"` | `5` | integer → StrictInt / int | `"result_hash_schema_version"` |
| `"cnig_complete_result_content_sha256"` | `"b56b195b32914583e6599fe96b3d29977c52450c9755228d89ce7e192903ab3e"` | string → StrictStr / str | `"complete_result_content_sha256"` |

### Status priority and meaning

| Exact status key | Priority: YAML integer → int | Entries | Internal review focus |
|---|---|---|---|
| `"LIKELY_MATERIAL_CONSTRAINT"` | `50` | 3 | Likely material protection-family concern; not a prohibition. |
| `"UNKNOWN"` | `40` | 1 | Meaning too generic for a more precise precheck; explicitly preserved. |
| `"MATERIAL_REVIEW_REQUIRED"` | `30` | 3 | Potentially material planning mechanism needs specific human review. |
| `"DESIGN_REVIEW_REQUIRED"` | `20` | 2 | Siting/design rule needs project-layout review. |
| `"CONTEXT_REVIEW_REQUIRED"` | `10` | 3 | Context must be checked; code alone establishes no direct BESS constraint. |

These are five configured positive, distinct priorities, not model-hardcoded numbers. `UNKNOWN` is an explicit entry outcome, not a fallback for a missing entry. All five keys must exist even if a different valid policy uses only a subset of statuses. The current file's distribution is 3/1/3/2/3 in descending-priority order above. Confidence distribution is HIGH 8, MEDIUM 3, LOW 1.

### Entry field contracts

`PolicyEntry._validate_entry` owns code/text checks; Literal annotations own family/status/confidence domains. Every entry field participates in the ordered-entry hash and the full-model hash.

| Entry field | YAML → runtime; required/nullability | Validation and actual use |
|---|---|---|
| `feature_family` | string → Literal / str; non-null | PRESCRIPTION or INFORMATION; first exact lookup-key member, not interchangeable namespaces. |
| `type_code` | quoted string → StrictStr / str; non-null | Full match [0-9]{2}; second key member, leading zero retained. |
| `subtype_code` | quoted string → StrictStr / str; non-null | Same full match; third key member. "00" is literal, never a wildcard. |
| `expected_official_label` | string → StrictStr / str; non-null | Exact nonempty/no edge whitespace. Compiler equality to dictionary official_label; table takes the dictionary value. |
| `expected_legal_reference` | string or null → str or None; nullable, still required | Optional exact-string check; compiler null-safe equality to dictionary legal_reference; table official_legal_reference. |
| `expected_regulation_reference` | string or null → str or None; nullable, still required | Same check against dictionary regulation_or_annex_reference; table official_regulation_reference. |
| `precheck_status` | string → Literal / str; non-null | Exactly the five statuses above; copied and used to look up priority. |
| `confidence` | string → Literal / str; non-null | HIGH, MEDIUM or LOW; copied, not inferred from geometry/text or statistically measured. |
| `rationale` | string → StrictStr / str; non-null | Exact nonempty/no edge whitespace; recorded internal reason copied verbatim. |
| `required_human_action` | string → StrictStr / str; non-null | Same exact check; instruction for later human review, not evidence that review occurred. |
| `limitations` | string → StrictStr / str; non-null | Same check; explicit bounds copied with the policy row. |

The BESS entry validator does not itself require NFC or collapse internal whitespace. Upstream CNIG models require already-canonical official text, and compiler equality consequently rejects differing expected text. Optional exact-string acceptance is not a proof against textual-null placeholders: see section 11 and preserved A-004.

### All twelve entries — official expectations

<a id="policy-entries"></a>

The index is the zero-based YAML entry position. JSON-quoted cells below retain exact strings, accents and punctuation; `null` means a true null, not the string "null". The three tables together enumerate every one of the 132 entry leaves. There are four INFORMATION and eight PRESCRIPTION entries; among 24 reference cells, 22 are strings and two are true nulls.

| Entry | `feature_family` | `type_code` | `subtype_code` | `expected_official_label` | `expected_legal_reference` | `expected_regulation_reference` |
|---|---|---|---|---|---|---|
| 0 | `"INFORMATION"` | `"02"` | `"00"` | `"Zone d'aménagement concerté"` | `"L311-1 code de l’urbanisme"` | `"R151-52 8°"` |
| 1 | `"INFORMATION"` | `"14"` | `"00"` | `"Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)"` | `"L571-10 code de l’environnement"` | `"R151-53 5°"` |
| 2 | `"INFORMATION"` | `"27"` | `"00"` | `"Plan d'exposition au bruit des aérodromes"` | `"L112-6 code de l’urbanisme"` | `"R151-52 2°"` |
| 3 | `"INFORMATION"` | `"99"` | `"00"` | `"Autre périmètre, secteur, plan, document, site, projet, espace."` | `null` | `null` |
| 4 | `"PRESCRIPTION"` | `"01"` | `"00"` | `"Espace boisé classé"` | `"L113-1"` | `"R151-31 1°"` |
| 5 | `"PRESCRIPTION"` | `"05"` | `"00"` | `"Emplacement réservé"` | `"L151-41 1° à 3°"` | `"R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1°"` |
| 6 | `"PRESCRIPTION"` | `"07"` | `"00"` | `"Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique"` | `"L151-19 et L151-23"` | `"R151-41 3° Et R151-43"` |
| 7 | `"PRESCRIPTION"` | `"07"` | `"04"` | `"Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique"` | `"L151-23"` | `"R151-43 5°"` |
| 8 | `"PRESCRIPTION"` | `"15"` | `"00"` | `"Règles d’implantation des constructions"` | `"L151-17 et L151-18"` | `"R151-39 dernier al."` |
| 9 | `"PRESCRIPTION"` | `"15"` | `"01"` | `"Implantation des constructions par rapport aux voies et aux emprises publiques"` | `"L151-17 et L151-18"` | `"R151-39"` |
| 10 | `"PRESCRIPTION"` | `"17"` | `"00"` | `"Secteur à programme de logements mixité sociale en zone U et AU"` | `"L151-15"` | `"R151-38 3°"` |
| 11 | `"PRESCRIPTION"` | `"18"` | `"00"` | `"Périmètre comportant des orientations d’aménagement et de programmation (OAP)"` | `"L151-6 et L151-7"` | `"R151-6 à R151-8-1"` |

### All twelve entries — internal classifications

| Entry | `precheck_status` | `confidence` |
|---|---|---|
| 0 | `"CONTEXT_REVIEW_REQUIRED"` | `"HIGH"` |
| 1 | `"CONTEXT_REVIEW_REQUIRED"` | `"HIGH"` |
| 2 | `"CONTEXT_REVIEW_REQUIRED"` | `"HIGH"` |
| 3 | `"UNKNOWN"` | `"LOW"` |
| 4 | `"LIKELY_MATERIAL_CONSTRAINT"` | `"HIGH"` |
| 5 | `"MATERIAL_REVIEW_REQUIRED"` | `"HIGH"` |
| 6 | `"LIKELY_MATERIAL_CONSTRAINT"` | `"MEDIUM"` |
| 7 | `"LIKELY_MATERIAL_CONSTRAINT"` | `"HIGH"` |
| 8 | `"DESIGN_REVIEW_REQUIRED"` | `"MEDIUM"` |
| 9 | `"DESIGN_REVIEW_REQUIRED"` | `"HIGH"` |
| 10 | `"MATERIAL_REVIEW_REQUIRED"` | `"MEDIUM"` |
| 11 | `"MATERIAL_REVIEW_REQUIRED"` | `"HIGH"` |

Priority is derived from the status map, not a twelfth entry field. There is no extra generic rule: a missing or extra dictionary triple makes compilation fail.

### All twelve entries — rationale, human action and limitations

| Entry | `rationale` | `required_human_action` | `limitations` |
|---|---|---|---|
| 0 | `"The official code identifies a concerted-development-zone context that requires planning-document review but does not establish a direct BESS constraint by itself."` | `"Review the applicable planning documents and authority context for the identified concerted-development zone."` | `"This classification uses only the official CNIG code meaning and does not interpret any local feature text or regulation."` |
| 1 | `"The official code identifies transport-infrastructure noise context that must be checked but does not establish a direct BESS constraint by itself."` | `"Review the applicable noise-sector documents and project-specific context with the competent authority."` | `"This classification uses only the official CNIG code meaning and does not interpret local noise rules or project effects."` |
| 2 | `"The official code identifies an aerodrome noise-exposure-plan context that must be checked but does not establish a direct BESS constraint by itself."` | `"Review the applicable aerodrome noise-exposure plan and project-specific context with the competent authority."` | `"This classification uses only the official CNIG code meaning and does not interpret the local plan or determine project admissibility."` |
| 3 | `"The official code is an unspecified other-information category and is too generic for a more precise BESS precheck."` | `"Identify and review the feature-specific local source before drawing any planning inference."` | `"The official code alone does not identify the local subject, rule, effect, authorization, or prohibition."` |
| 4 | `"The official code identifies a classified wooded-area protection family likely to be material for a BESS project without meaning prohibited."` | `"Review the exact classified-area geometry, local prescription, applicable planning provisions, and project design with the competent authority."` | `"This preliminary classification does not interpret the local prescription or establish authorization or prohibition."` |
| 5 | `"The official code identifies a reserved-site planning mechanism that may materially affect a project and requires specific review."` | `"Review the beneficiary, purpose, exact reservation, local planning documents, and project interaction with the competent authority."` | `"This classification does not infer the reservation purpose from local text or determine whether a BESS project is authorized or prohibited."` |
| 6 | `"The official code identifies a broad heritage or landscape protection family likely to be material, while its exact local subject remains unspecified."` | `"Review the protected element, local prescription, project siting and design, and competent-authority requirements."` | `"The broad official category does not reveal the feature-specific protected subject or establish authorization or prohibition."` |
| 7 | `"The official subtype identifies ecological landscape preservation likely to be material for a BESS project without meaning prohibited."` | `"Review the exact preserved element, local prescription, ecological context, and project design with the competent authority."` | `"This classification does not interpret the local preservation rule or determine project admissibility."` |
| 8 | `"The official code primarily identifies construction-implantation rules relevant to project siting and design, while the local rule remains unread."` | `"Review the exact local implantation rule against the proposed equipment layout and site design."` | `"This classification does not interpret local setbacks, feature text, or project compliance."` |
| 9 | `"The official subtype specifically identifies construction siting relative to roads and public rights-of-way, requiring design review."` | `"Review the exact local siting or setback rule against the proposed equipment layout and access design."` | `"This classification does not interpret the local setback value or establish project compliance."` |
| 10 | `"The official code identifies a social-housing-program planning mechanism that may materially affect land use and requires specific review."` | `"Review the sector program, local planning provisions, land-use interaction, and authority requirements for the proposed project."` | `"This classification does not infer the local program content or determine BESS authorization or prohibition."` |
| 11 | `"The official code identifies an area governed by planning and development guidelines that may materially affect a project and requires specific review."` | `"Review the applicable OAP text and graphics, project design interaction, and competent-authority requirements."` | `"This classification does not interpret the local OAP or establish authorization, prohibition, or buildability."` |

## STEP 7F.1A.4 dependent-model refresh

Historical model freezing did not change these YAML bytes. The current deeply immutable representation comes from the subsequently checked-in source. R5 replaces the stale mutable-dict declaration and generic enable-switch/hash claims; it does not alter source, fixtures, policies or schemas.

## 5. Classes / models / dataclasses

### `_StrictPolicyModel`

The local base sets `extra="forbid", frozen=True` for the configuration, entry, lock and artifact models. Field assignment is rejected; supplied external objects are still revalidated at public trust boundaries.

### `PolicySourceLock`

Seven scalar fields, strict shape rules described above. Shape validity is not equality to a physical source, and a configured digest is not a source reconstruction.

### `PolicyEntry`

Eleven scalar fields; no mutable collection. The two nullable references have no defaults. A tuple of these frozen models preserves the required semantic entry order.

### `BessPlanningFeaturePolicyConfig`

`entries: tuple[PolicyEntry, ...]` and `status_priority: Mapping[PrecheckStatus, StrictInt]` are the current declarations. After all schema/flag/priority/key-order/hash checks, `freeze_mapping` produces a `FrozenDict` over a **fresh copied dictionary**. Its recursive helper converts mappings, sequences and sets to frozen mappings, tuples and frozensets; here keys are validated status strings and values are strict integers. It is not a general arbitrary-object canonicality validator. FrozenDict rejects assignment/deletion/update/pop/setdefault/clear and backing-attribute mutation; no caller-owned mutable priority dictionary is retained.

The field serializer returns a new dict; JSON-mode model_dump represents tuples as arrays. That serialization is deliberately mutable output, not a mutable alias into the trust model. `_resolved_policy_config` dumps a supplied model in Python mode with warnings="error" then reconstructs/validates it, rather than trusting model_copy updates. Freezing does not remove that boundary.

### `PolicyTableSchemaSignature`

This is an artifact-model dependency, not a field of the YAML. It holds immutable column/dtype/index-name sequences. The returned `BessPlanningFeaturePolicyResult` is a frozen dataclass with a **mutable pandas DataFrame**; it must not be described as a deeply frozen table. Mutating its table does not immediately fail; the envelope/full validators serve different later integrity checks.

## 6. Functions and methods

<a id="policy-interfaces"></a>

Current public signatures, copied from the owning source (names resolve there, not to YAML-defined functions):

```python
def load_bess_planning_feature_policy_config(
    path: str | Path,
) -> BessPlanningFeaturePolicyConfig:

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

def validate_bess_planning_feature_policy_result_envelope(
    result: BessPlanningFeaturePolicyResult,
) -> None:

def load_bess_planning_feature_policy_artifacts(
    parquet_path: str | Path,
    manifest_path: str | Path,
) -> BessPlanningFeaturePolicyResult:
```

No default policy path is selected by the configuration loader: callers provide a str/Path. Result artifact loading reads a separate Parquet/manifest pair; it does not load this YAML.

## 7. Data contracts

Compilation builds 21 policy-table columns, in `POLICY_TABLE_COLUMNS` order. All are pandas `str` except `status_priority` (`int64`) and three flags (`bool`); the index is a plain unnamed int64 pandas.Index, not a RangeIndex. True missing references become missing string-array values and canonical JSON nulls, never textual placeholders.

| YAML / upstream value | Compiled table / scalar propagation |
|---|---|
| entry family/type/subtype | `feature_family`, `type_code`, `subtype_code` in entry order |
| dictionary texts after expected-text comparisons | `official_label`, `official_legal_reference`, `official_regulation_reference` |
| entry status/confidence plus map lookup | `precheck_status`, `confidence`, `status_priority` |
| entry review narratives | `rationale`, `required_human_action`, `limitations` |
| policy scope and three false flags | `policy_scope`, `local_feature_text_interpreted`, `local_regulation_content_interpreted`, `legal_conclusion_produced` |
| config profile / full-model digest | `policy_profile`, `policy_sha256`, also result scalars |
| validated coded result | `cnig_profile`, `cnig_profile_sha256`, `cnig_complete_result_content_sha256`, also result scalars |
| schema and locked document/archive/version identity | result envelope scalars; document/archive/version fields are not extra table columns |

The result has no parcel_id, planning_feature_id, relation_type or geometry. All dictionary triples must be covered, not only features intersecting a parcel.

## 8. Interfaces

The separate application module's `_policy_lookup`/`_apply_feature_catalog` match the exact triple. `_policy_values` copies status/confidence/priority/narratives to `bess_cnig_*` evidence. A resolved official feature must have a policy row; an UNKNOWN_CODE_PAIR must not. For the latter application emits UNRESOLVED_CODE_PAIR with null policy decision fields, not the configured UNKNOWN/40 entry. It does not interpret LIBELLE or TXT to manufacture a match.

The aggregation module's `_parcel_summary` considers AREA_OVERLAP/LENGTH_OVERLAP/INSIDE controlling; TOUCH_ONLY/BOUNDARY_TOUCH are contextual. Unresolved controlling codes defer selection. Otherwise it chooses the maximum exact controlling priority and the lowest confidence among rows with that selected status/priority. These are later parcel-precheck operations, not work of this compiler, not a parcel score or exclusion. This bounded consumer reading is not an audit closure of those modules.

## 9. Error handling

<a id="policy-validation"></a>

Load order: read bytes → strict YAML → require a mapping → Pydantic fields/nested models → schema=1, exact profile/scope, all flags false, full unique positive priority map, unique sorted triple sequence, valid/equal entry digest → freeze priorities. Missing/extra/coerced invalid fields and bad texts are not repaired. An empty entry tuple with its own valid digest is not excluded by this model alone; dictionary completeness and the nonempty result envelope are separate checks.

Compile order: reconstruct/load policy → compare all seven locks against coded scalars → call source-complete CNIG result validation → check dictionary duplicate keys, **missing triples before extra triples**, then label/legal/regulation equality for every dictionary row → construct table and hashes → validate envelope. It does not accept a matching configured hash as a substitute for source validation. `_null_safe_equal` treats true pandas/None missing values alike; strings remain exact.

The full policy validator first checks the supplied result envelope, then reconstructs config, checks locks, validates all coded sources, rebuilds and compares every scalar and complete frame payload. Thus an earlier schema/hash/lock error can prevent a later guard from running. It requires the actual planning document, parcels, three normalized catalogs, relations, code profile, coded result, policy config and policy result. The CNIG validator rebuilds through its normalized-feature source validator; no synthetic identity replacement proves physical authority.

The lightweight envelope validator only checks result type, supported schemas (policy/result 1/1, CNIG 2/5), scope, scalar syntax, exact columns/dtypes/index schema, nonempty rows, sorted unique triples, text/null rules, status/confidence/priority domains and one-to-one mapping for observed statuses, false flags, row lineage, and table/result hashes. It does not have this YAML or the source dictionary, cannot rederive the declared policy SHA, and can accept one internally valid rehashed row. It is not completeness/source validation.

Loader errors are `BessPlanningFeaturePolicyError` (a ValueError): non-mapping has its own message; StrictYamlError retains its message/cause; other IO/Pydantic failures become "BESS CNIG feature policy is invalid". Direct model calls instead raise Pydantic ValidationError. The in-memory boundary uses its own controlled error; source validator failures are chained under "Source-complete CNIG result validation failed". Compiler/full-validator unexpected exceptions are safely wrapped; semantic mismatch errors remain specific.

## 10. Side effects

The YAML loader reads this local file and recomputes the canonical **entries** digest during validation. It neither computes nor validates a raw-file SHA, performs network IO, writes files nor runs GIS. The full-model digest is calculated by `_policy_sha256` when building a result (and explicitly in R5's bounded inspection), not returned as a config field.

Compilation revalidates physical CNIG/GPU source context through upstream code but neither persists its result nor applies a feature/parcel decision. The artifact loader reads strict JSON, verifies filename/size/SHA of immutable Parquet bytes before parsing those bytes, checks row/schema evidence and the local envelope. It is not a source-complete reconstruction; its caller must invoke the full validator with upstream context for that guarantee. No artifact writer is invoked by this config.

## 11. Security / trust boundaries

Immutability, canonical hashes, source comparisons and physical reconstruction are distinct guards. Neither matching hashes nor exact official endpoints are signatures, freshness evidence or legal approval. Every configured expected text is checked against a validated dictionary at compilation, not at YAML loading.

[A-004](../../../../project/BACKLOG_AND_GAPS.md#application-findings) remains open: the CNIG optional record-text validator accepts canonical textual-null replacements that its result validator rejects. The BESS optional exact-string helper likewise only tests null-or-exact-text, while the policy row envelope explicitly rejects "None", "nan", "<NA>" in non-null reference cells. Current INFORMATION/99/00 uses two real nulls and matches the dictionary. R5 does not repair this boundary, duplicate the finding or claim a new reproduction/full compiler run.

## 12. GIS / CRS rules

No CRS field, distance, overlay, geometry rule or tolerance is configured here. Compilation's source-complete inputs include geospatial evidence for upstream integrity only; its output is a non-geospatial meaning table. Requests in required_human_action to review geometry or design do not mean the compiler performs those reviews.

## 13. Provenance rules

<a id="policy-hashes"></a>

All canonical hashes below use the owning helper: json.dumps(ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")), UTF-8 then SHA256. Mapping key order is canonicalized; sequence order is retained. None serializes as JSON null. No Python repr, class identity or memory address participates.

| Identity | Actual payload / exclusions | Value or propagation |
|---|---|---|
| Documentation raw SHA256 | All 10,147 YAML bytes including formatting; not a runtime policy field/hash | `8a26fcb8ee7e2f028baca65d94c2b5be5445ba9fc4b82b9b1a21843f933f8b2a` |
| `canonical_policy_entries_sha256` | Array of all eleven JSON-mode fields for every entry, in validated order; excludes root metadata, lock, priority map and itself | `1d3e63f1123000402065b74402cb1e2295db2ac5655209ce410aaf36bfc2be91` |
| full policy `_policy_sha256` | Complete config.model_dump(mode="json"): all ten root fields, including entries, their declared digest, every lock, flags and dict-serialized priorities; excludes YAML formatting/path | `1cfca0eb3d777e9b6604748e8a81609abe7b728de8d0695711cd569180df6489` |
| locked CNIG profile SHA | Complete upstream JSON-mode profile including sources, ISO retrieval date and declared ordered-record digest; not CNIG YAML SHA or records-only SHA | `5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee` |
| locked archive/result identities | Archive bytes and upstream complete CNIG result commitment, respectively; seven exact locks listed above | Compared before upstream source validation; **not rebuilt in R5** |
| `policy_table_content_sha256` | domain landscout.bess_cnig_feature_policy.table + twelve _component_metadata scalars + frame schema/index/ordered rows | Carries policy full hash and locked context; no raw YAML bytes or self-hash |
| `complete_result_content_sha256` | domain landscout.bess_cnig_feature_policy.result + same metadata + policy_table_content_sha256 | Table changes affect this transitively; excludes this complete digest itself |

The twelve component scalars are policy_schema_version, result_hash_schema_version, policy_profile, policy_scope, policy_sha256, source_document_id, source_archive_sha256, cnig_profile, cnig_profile_schema_version, cnig_profile_sha256, cnig_result_hash_schema_version and cnig_complete_result_content_sha256. Frame schema includes ordered columns/dtypes and index class/names/level dtypes; payload includes canonical index values and ordered row arrays. Pandas missing scalars become null, NumPy scalars native values, dates ISO; unsupported/nonfinite non-missing values fail.

The CNIG complete-result lock commits its metadata/source-input hashes and dictionary/surface/line/point/relation component hashes. R5 compares only the loaded profile identity and twelve triples/36 text-or-null cells; it does not reconstruct that result, the archive or the two output hashes. Existing snapshot tests pin output hashes `225105fe488e21f8aa080751812dde1671340c26620cae1d8372c2e59488ed41` and `84a59b418f5a53bc61df73296964b2847cc5d3529c10d0c6912c96222edba09c` through an internal synthetic-context helper; they are not fresh R5 outputs.

## 14. Business meaning

The classifications and all narrative text in section 4 are authored conservative prechecks. UNKNOWN/LOW for INFORMATION/99/00 explicitly preserves unspecified subject/rule/effect; the three context statuses still require review. Material and design review labels identify review focus, not measured impact. The numeric ordering can select a later controlling precheck, never by itself legal permission/prohibition or parcel ranking. R5 audits fidelity to existing software and YAML, not whether those judgments are legally or commercially correct.

## 15. Explicit non-goals

No local feature-text interpretation, regulation reading, permit decision, exclusion/rejection, score, global ranking, BESS feasibility, heavy-vehicle access, ownership/contact inference, acquisition or EP semantic rule. No external legal/source freshness verification was performed for R5.

## 16. Tests

<a id="policy-tests"></a>

These are **read assertions, not tests executed in R5**. The [policy test module](../../../../../tests/unit/test_bess_planning_feature_policy.py) was read in full; synthetic setup and early guard order matter.

| Tests / source lines | Actual proof and limits |
|---|---|
| checked-in twelve decisions / complete snapshot, 262–298 | Exact decisions, priorities, false flags, source locks, entries/full-policy digests; local YAML load only. “snapshot_is_immutable” checks snapshot values, not attempted mutation. |
| compiled hash snapshot, 213–241 and 301–304 | _checked_in_policy_result replaces fields of a synthetic coded result with configured locks and a real dictionary, then calls private _build_result. Does not validate that substituted context through the public compiler. |
| text/source-lock drift, 307–331 | Rehashes changed entry text before model validation; changed full digest is asserted, not model rejection. Lock-name drift is valid model shape but changes full-model digest. |
| exact compile and source tests, 122–172, 244–259, 381–487 | _integration_inputs supplies four synthetic meanings and local physical GPKGs. Missing/extra/family/meaning mutations rehash entries; duplicate-key mutation also rehashes. Family change moves one INFORMATION key to PRESCRIPTION; exact triple checks prevent fallback. Not an official Muret acquisition. |
| domains/priority/order/YAML, 490–599 | Rejects legal-conclusion statuses, bad confidence, missing/duplicate/zero/bool/string priorities, unknown field, edge whitespace, malformed digest, reversed entry order; local duplicate-YAML file. _validated_config repairs only declared hashes in test payloads. |
| immutability and revalidation, 536–543 and 583–587 | Direct priority item assignment must raise immediately. model_copy with stale entry digest must fail the public in-memory boundary. |
| null references, 341–378 | Actual missing values asserted; six reference/literal combinations coordinate table/hash updates before intrinsic rejection. Not a test that PolicyEntry rejects such strings. |
| table mutation, 615–634 | Status edit without rehash may hit earlier priority consistency/hash checks. Coordinated valid-text rationale edit rehashes and is rejected against rebuilt policy. Neither implies DataFrame mutation is impossible. |
| artifact tests, 637–804 and 938–1080 | Synthetic local Parquet/JSON IO; separate full validation after readback. Manifest/byte/schema guards, exact verified buffer parsing and no Parquet access before malformed JSON/unsupported versions; no production snapshot execution. |
| fast-fail/source-call tests, 807–905 | Instrument actual CNIG validation: invalid envelope/wrong lock stops before it; forged matching lock still invokes/rejects; compile + full validation each invoke once. Not every failure reaches every guard. |
| intrinsic envelope tests, 927–935 and 1083–1242 | Canonical rehashed empty table rejected, one exact row accepted, schemas 2/5 enforced; coordinated row mutations. bool-priority branch changes dtype to object, so schema rejection precedes the row guard. Reversed rows retain schema and reach order validation. |

[Integration helpers](../../../../../tests/unit/test_resolve_planning_feature_codes.py) create temporary physical GPKGs, reread them, build an extraction manifest/config-bound planning document and real synthetic feature intersections; metadata uses doc-1 / repeated "a" archive digest with a synthetic.zip path, not downloaded official archive bytes. [Deep-immutability tests](../../../../../tests/unit/test_deep_immutability.py) 300–354 include this loaded config in recursive graph inspection, and 456–482 pin the full policy hash. The generic mutation/alias tests at 356–454 target AOI/structure/road collections, not individual BESS-field alias probes; do not attribute them more broadly. [Strict serialization tests](../../../../../tests/unit/test_strict_serialization.py) 1–23 exercise nested duplicate-key rejection and safe YAML scalar decoding.

## 17. Change impact

A future authorized semantic change requires policy/source review, owning validation and test updates, deliberate canonical-hash/schema decisions and affected artifact regeneration only where their contracts require it. Formatting alone affects the documentation raw SHA, not validated canonical hashes. Entry text/order affects the entry/full/output chain; lock, priority or flag changes affect full/output identities without changing the entries-only payload. This R5 documentary correction changes none of them. No new functional or missing-test backlog item is inferred.

## 18. Complete readable configuration and authoritative raw-byte snapshot

### Complete readable YAML

The following is the complete decoded UTF-8 configuration with line endings normalized to LF for stable Markdown display. Every character and logical line is present, but this readable fence is not the authority for original CR/LF byte positions.

```yaml
schema_version: 1
profile: muret_bess_cnig_feature_policy_v1
policy_scope: OFFICIAL_CNIG_CODE_MEANING_ONLY
local_feature_text_interpreted: false
local_regulation_content_interpreted: false
legal_conclusion_produced: false
source_lock:
  document_id: 33edb4c9f6943c88d8d92518bff20bec
  archive_sha256: 9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93
  cnig_profile: cnig_plu_2017_muret_observed_pairs_v2
  cnig_profile_schema_version: 2
  cnig_profile_sha256: 5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee
  cnig_result_hash_schema_version: 5
  cnig_complete_result_content_sha256: b56b195b32914583e6599fe96b3d29977c52450c9755228d89ce7e192903ab3e
status_priority:
  LIKELY_MATERIAL_CONSTRAINT: 50
  UNKNOWN: 40
  MATERIAL_REVIEW_REQUIRED: 30
  DESIGN_REVIEW_REQUIRED: 20
  CONTEXT_REVIEW_REQUIRED: 10
canonical_policy_entries_sha256: 1d3e63f1123000402065b74402cb1e2295db2ac5655209ce410aaf36bfc2be91
entries:
  - feature_family: INFORMATION
    type_code: "02"
    subtype_code: "00"
    expected_official_label: Zone d'aménagement concerté
    expected_legal_reference: L311-1 code de l’urbanisme
    expected_regulation_reference: R151-52 8°
    precheck_status: CONTEXT_REVIEW_REQUIRED
    confidence: HIGH
    rationale: The official code identifies a concerted-development-zone context that requires planning-document review but does not establish a direct BESS constraint by itself.
    required_human_action: Review the applicable planning documents and authority context for the identified concerted-development zone.
    limitations: This classification uses only the official CNIG code meaning and does not interpret any local feature text or regulation.
  - feature_family: INFORMATION
    type_code: "14"
    subtype_code: "00"
    expected_official_label: Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)
    expected_legal_reference: L571-10 code de l’environnement
    expected_regulation_reference: R151-53 5°
    precheck_status: CONTEXT_REVIEW_REQUIRED
    confidence: HIGH
    rationale: The official code identifies transport-infrastructure noise context that must be checked but does not establish a direct BESS constraint by itself.
    required_human_action: Review the applicable noise-sector documents and project-specific context with the competent authority.
    limitations: This classification uses only the official CNIG code meaning and does not interpret local noise rules or project effects.
  - feature_family: INFORMATION
    type_code: "27"
    subtype_code: "00"
    expected_official_label: Plan d'exposition au bruit des aérodromes
    expected_legal_reference: L112-6 code de l’urbanisme
    expected_regulation_reference: R151-52 2°
    precheck_status: CONTEXT_REVIEW_REQUIRED
    confidence: HIGH
    rationale: The official code identifies an aerodrome noise-exposure-plan context that must be checked but does not establish a direct BESS constraint by itself.
    required_human_action: Review the applicable aerodrome noise-exposure plan and project-specific context with the competent authority.
    limitations: This classification uses only the official CNIG code meaning and does not interpret the local plan or determine project admissibility.
  - feature_family: INFORMATION
    type_code: "99"
    subtype_code: "00"
    expected_official_label: Autre périmètre, secteur, plan, document, site, projet, espace.
    expected_legal_reference: null
    expected_regulation_reference: null
    precheck_status: UNKNOWN
    confidence: LOW
    rationale: The official code is an unspecified other-information category and is too generic for a more precise BESS precheck.
    required_human_action: Identify and review the feature-specific local source before drawing any planning inference.
    limitations: The official code alone does not identify the local subject, rule, effect, authorization, or prohibition.
  - feature_family: PRESCRIPTION
    type_code: "01"
    subtype_code: "00"
    expected_official_label: Espace boisé classé
    expected_legal_reference: L113-1
    expected_regulation_reference: R151-31 1°
    precheck_status: LIKELY_MATERIAL_CONSTRAINT
    confidence: HIGH
    rationale: The official code identifies a classified wooded-area protection family likely to be material for a BESS project without meaning prohibited.
    required_human_action: Review the exact classified-area geometry, local prescription, applicable planning provisions, and project design with the competent authority.
    limitations: This preliminary classification does not interpret the local prescription or establish authorization or prohibition.
  - feature_family: PRESCRIPTION
    type_code: "05"
    subtype_code: "00"
    expected_official_label: Emplacement réservé
    expected_legal_reference: L151-41 1° à 3°
    expected_regulation_reference: R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1°
    precheck_status: MATERIAL_REVIEW_REQUIRED
    confidence: HIGH
    rationale: The official code identifies a reserved-site planning mechanism that may materially affect a project and requires specific review.
    required_human_action: Review the beneficiary, purpose, exact reservation, local planning documents, and project interaction with the competent authority.
    limitations: This classification does not infer the reservation purpose from local text or determine whether a BESS project is authorized or prohibited.
  - feature_family: PRESCRIPTION
    type_code: "07"
    subtype_code: "00"
    expected_official_label: Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique
    expected_legal_reference: L151-19 et L151-23
    expected_regulation_reference: R151-41 3° Et R151-43
    precheck_status: LIKELY_MATERIAL_CONSTRAINT
    confidence: MEDIUM
    rationale: The official code identifies a broad heritage or landscape protection family likely to be material, while its exact local subject remains unspecified.
    required_human_action: Review the protected element, local prescription, project siting and design, and competent-authority requirements.
    limitations: The broad official category does not reveal the feature-specific protected subject or establish authorization or prohibition.
  - feature_family: PRESCRIPTION
    type_code: "07"
    subtype_code: "04"
    expected_official_label: Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique
    expected_legal_reference: L151-23
    expected_regulation_reference: R151-43 5°
    precheck_status: LIKELY_MATERIAL_CONSTRAINT
    confidence: HIGH
    rationale: The official subtype identifies ecological landscape preservation likely to be material for a BESS project without meaning prohibited.
    required_human_action: Review the exact preserved element, local prescription, ecological context, and project design with the competent authority.
    limitations: This classification does not interpret the local preservation rule or determine project admissibility.
  - feature_family: PRESCRIPTION
    type_code: "15"
    subtype_code: "00"
    expected_official_label: Règles d’implantation des constructions
    expected_legal_reference: L151-17 et L151-18
    expected_regulation_reference: R151-39 dernier al.
    precheck_status: DESIGN_REVIEW_REQUIRED
    confidence: MEDIUM
    rationale: The official code primarily identifies construction-implantation rules relevant to project siting and design, while the local rule remains unread.
    required_human_action: Review the exact local implantation rule against the proposed equipment layout and site design.
    limitations: This classification does not interpret local setbacks, feature text, or project compliance.
  - feature_family: PRESCRIPTION
    type_code: "15"
    subtype_code: "01"
    expected_official_label: Implantation des constructions par rapport aux voies et aux emprises publiques
    expected_legal_reference: L151-17 et L151-18
    expected_regulation_reference: R151-39
    precheck_status: DESIGN_REVIEW_REQUIRED
    confidence: HIGH
    rationale: The official subtype specifically identifies construction siting relative to roads and public rights-of-way, requiring design review.
    required_human_action: Review the exact local siting or setback rule against the proposed equipment layout and access design.
    limitations: This classification does not interpret the local setback value or establish project compliance.
  - feature_family: PRESCRIPTION
    type_code: "17"
    subtype_code: "00"
    expected_official_label: Secteur à programme de logements mixité sociale en zone U et AU
    expected_legal_reference: L151-15
    expected_regulation_reference: R151-38 3°
    precheck_status: MATERIAL_REVIEW_REQUIRED
    confidence: MEDIUM
    rationale: The official code identifies a social-housing-program planning mechanism that may materially affect land use and requires specific review.
    required_human_action: Review the sector program, local planning provisions, land-use interaction, and authority requirements for the proposed project.
    limitations: This classification does not infer the local program content or determine BESS authorization or prohibition.
  - feature_family: PRESCRIPTION
    type_code: "18"
    subtype_code: "00"
    expected_official_label: Périmètre comportant des orientations d’aménagement et de programmation (OAP)
    expected_legal_reference: L151-6 et L151-7
    expected_regulation_reference: R151-6 à R151-8-1
    precheck_status: MATERIAL_REVIEW_REQUIRED
    confidence: HIGH
    rationale: The official code identifies an area governed by planning and development guidelines that may materially affect a project and requires specific review.
    required_human_action: Review the applicable OAP text and graphics, project design interaction, and competent-authority requirements.
    limitations: This classification does not interpret the local OAP or establish authorization, prohibition, or buildability.
```

### Authoritative raw-byte payload

- Raw byte length: `10147`.
- Raw SHA256: `8a26fcb8ee7e2f028baca65d94c2b5be5445ba9fc4b82b9b1a21843f933f8b2a` (identical to **File identity**).
- Encoding: RFC 4648 Base64, wrapped for display only. Decoding the concatenated payload reproduces every original byte, including mixed CRLF/LF positions.

```text
c2NoZW1hX3ZlcnNpb246IDEKcHJvZmlsZTogbXVyZXRfYmVzc19jbmlnX2ZlYXR1cmVfcG9saWN5
X3YxCnBvbGljeV9zY29wZTogT0ZGSUNJQUxfQ05JR19DT0RFX01FQU5JTkdfT05MWQpsb2NhbF9m
ZWF0dXJlX3RleHRfaW50ZXJwcmV0ZWQ6IGZhbHNlCmxvY2FsX3JlZ3VsYXRpb25fY29udGVudF9p
bnRlcnByZXRlZDogZmFsc2UKbGVnYWxfY29uY2x1c2lvbl9wcm9kdWNlZDogZmFsc2UKc291cmNl
X2xvY2s6CiAgZG9jdW1lbnRfaWQ6IDMzZWRiNGM5ZjY5NDNjODhkOGQ5MjUxOGJmZjIwYmVjCiAg
YXJjaGl2ZV9zaGEyNTY6IDlkNjY3N2NkNjYzNGI1NmI3MTIzMTEwNDJmMGNjNzE0ZDVjYTQyYTM4
ZjgyYTQxN2IyN2RkNDczMjU1ZDdkOTMKICBjbmlnX3Byb2ZpbGU6IGNuaWdfcGx1XzIwMTdfbXVy
ZXRfb2JzZXJ2ZWRfcGFpcnNfdjIKICBjbmlnX3Byb2ZpbGVfc2NoZW1hX3ZlcnNpb246IDIKICBj
bmlnX3Byb2ZpbGVfc2hhMjU2OiA1NjExYjgxNGViNGJjMDU3NTc4YjkwOGM2NTA1MDk0ZjlkZjVk
MmMyYmY0Y2ExMjY2MjliMTM2Mjk4M2M0N2VlCiAgY25pZ19yZXN1bHRfaGFzaF9zY2hlbWFfdmVy
c2lvbjogNQogIGNuaWdfY29tcGxldGVfcmVzdWx0X2NvbnRlbnRfc2hhMjU2OiBiNTZiMTk1YjMy
OTE0NTgzZTY1OTlmZTk2YjNkMjk5NzdjNTI0NTBjOTc1NTIyOGQ4OWNlN2UxOTI5MDNhYjNlCnN0
YXR1c19wcmlvcml0eToKICBMSUtFTFlfTUFURVJJQUxfQ09OU1RSQUlOVDogNTAKICBVTktOT1dO
OiA0MAogIE1BVEVSSUFMX1JFVklFV19SRVFVSVJFRDogMzAKICBERVNJR05fUkVWSUVXX1JFUVVJ
UkVEOiAyMAogIENPTlRFWFRfUkVWSUVXX1JFUVVJUkVEOiAxMApjYW5vbmljYWxfcG9saWN5X2Vu
dHJpZXNfc2hhMjU2OiAxZDNlNjNmMTEyMzAwMDQwMjA2NWI3NDQwMmNiMWUyMjk1ZGIyYWM1NjU1
MjA5Y2U0MTBhYWYzNmJmYzJiZTkxCmVudHJpZXM6CiAgLSBmZWF0dXJlX2ZhbWlseTogSU5GT1JN
QVRJT04KICAgIHR5cGVfY29kZTogIjAyIgogICAgc3VidHlwZV9jb2RlOiAiMDAiCiAgICBleHBl
Y3RlZF9vZmZpY2lhbF9sYWJlbDogWm9uZSBkJ2Ftw6luYWdlbWVudCBjb25jZXJ0w6kKICAgIGV4
cGVjdGVkX2xlZ2FsX3JlZmVyZW5jZTogTDMxMS0xIGNvZGUgZGUgbOKAmXVyYmFuaXNtZQogICAg
ZXhwZWN0ZWRfcmVndWxhdGlvbl9yZWZlcmVuY2U6IFIxNTEtNTIgOMKwCiAgICBwcmVjaGVja19z
dGF0dXM6IENPTlRFWFRfUkVWSUVXX1JFUVVJUkVECiAgICBjb25maWRlbmNlOiBISUdICiAgICBy
YXRpb25hbGU6IFRoZSBvZmZpY2lhbCBjb2RlIGlkZW50aWZpZXMgYSBjb25jZXJ0ZWQtZGV2ZWxv
cG1lbnQtem9uZSBjb250ZXh0IHRoYXQgcmVxdWlyZXMgcGxhbm5pbmctZG9jdW1lbnQgcmV2aWV3
IGJ1dCBkb2VzIG5vdCBlc3RhYmxpc2ggYSBkaXJlY3QgQkVTUyBjb25zdHJhaW50IGJ5IGl0c2Vs
Zi4KICAgIHJlcXVpcmVkX2h1bWFuX2FjdGlvbjogUmV2aWV3IHRoZSBhcHBsaWNhYmxlIHBsYW5u
aW5nIGRvY3VtZW50cyBhbmQgYXV0aG9yaXR5IGNvbnRleHQgZm9yIHRoZSBpZGVudGlmaWVkIGNv
bmNlcnRlZC1kZXZlbG9wbWVudCB6b25lLgogICAgbGltaXRhdGlvbnM6IFRoaXMgY2xhc3NpZmlj
YXRpb24gdXNlcyBvbmx5IHRoZSBvZmZpY2lhbCBDTklHIGNvZGUgbWVhbmluZyBhbmQgZG9lcyBu
b3QgaW50ZXJwcmV0IGFueSBsb2NhbCBmZWF0dXJlIHRleHQgb3IgcmVndWxhdGlvbi4KICAtIGZl
YXR1cmVfZmFtaWx5OiBJTkZPUk1BVElPTgogICAgdHlwZV9jb2RlOiAiMTQiCiAgICBzdWJ0eXBl
X2NvZGU6ICIwMCIKICAgIGV4cGVjdGVkX29mZmljaWFsX2xhYmVsOiBQw6lyaW3DqHRyZSBkZSB2
b2lzaW5hZ2UgZCdpbmZyYXN0cnVjdHVyZSBkZSB0cmFuc3BvcnQgdGVycmVzdHJlIChzZWN0ZXVy
IGFmZmVjdMOpIHBhciBsZSBicnVpdCkKICAgIGV4cGVjdGVkX2xlZ2FsX3JlZmVyZW5jZTogTDU3
MS0xMCBjb2RlIGRlIGzigJllbnZpcm9ubmVtZW50CiAgICBleHBlY3RlZF9yZWd1bGF0aW9uX3Jl
ZmVyZW5jZTogUjE1MS01MyA1wrAKICAgIHByZWNoZWNrX3N0YXR1czogQ09OVEVYVF9SRVZJRVdf
UkVRVUlSRUQKICAgIGNvbmZpZGVuY2U6IEhJR0gKICAgIHJhdGlvbmFsZTogVGhlIG9mZmljaWFs
IGNvZGUgaWRlbnRpZmllcyB0cmFuc3BvcnQtaW5mcmFzdHJ1Y3R1cmUgbm9pc2UgY29udGV4dCB0
aGF0IG11c3QgYmUgY2hlY2tlZCBidXQgZG9lcyBub3QgZXN0YWJsaXNoIGEgZGlyZWN0IEJFU1Mg
Y29uc3RyYWludCBieSBpdHNlbGYuCiAgICByZXF1aXJlZF9odW1hbl9hY3Rpb246IFJldmlldyB0
aGUgYXBwbGljYWJsZSBub2lzZS1zZWN0b3IgZG9jdW1lbnRzIGFuZCBwcm9qZWN0LXNwZWNpZmlj
IGNvbnRleHQgd2l0aCB0aGUgY29tcGV0ZW50IGF1dGhvcml0eS4KICAgIGxpbWl0YXRpb25zOiBU
aGlzIGNsYXNzaWZpY2F0aW9uIHVzZXMgb25seSB0aGUgb2ZmaWNpYWwgQ05JRyBjb2RlIG1lYW5p
bmcgYW5kIGRvZXMgbm90IGludGVycHJldCBsb2NhbCBub2lzZSBydWxlcyBvciBwcm9qZWN0IGVm
ZmVjdHMuCiAgLSBmZWF0dXJlX2ZhbWlseTogSU5GT1JNQVRJT04KICAgIHR5cGVfY29kZTogIjI3
IgogICAgc3VidHlwZV9jb2RlOiAiMDAiCiAgICBleHBlY3RlZF9vZmZpY2lhbF9sYWJlbDogUGxh
biBkJ2V4cG9zaXRpb24gYXUgYnJ1aXQgZGVzIGHDqXJvZHJvbWVzCiAgICBleHBlY3RlZF9sZWdh
bF9yZWZlcmVuY2U6IEwxMTItNiBjb2RlIGRlIGzigJl1cmJhbmlzbWUKICAgIGV4cGVjdGVkX3Jl
Z3VsYXRpb25fcmVmZXJlbmNlOiBSMTUxLTUyIDLCsAogICAgcHJlY2hlY2tfc3RhdHVzOiBDT05U
RVhUX1JFVklFV19SRVFVSVJFRAogICAgY29uZmlkZW5jZTogSElHSAogICAgcmF0aW9uYWxlOiBU
aGUgb2ZmaWNpYWwgY29kZSBpZGVudGlmaWVzIGFuIGFlcm9kcm9tZSBub2lzZS1leHBvc3VyZS1w
bGFuIGNvbnRleHQgdGhhdCBtdXN0IGJlIGNoZWNrZWQgYnV0IGRvZXMgbm90IGVzdGFibGlzaCBh
IGRpcmVjdCBCRVNTIGNvbnN0cmFpbnQgYnkgaXRzZWxmLgogICAgcmVxdWlyZWRfaHVtYW5fYWN0
aW9uOiBSZXZpZXcgdGhlIGFwcGxpY2FibGUgYWVyb2Ryb21lIG5vaXNlLWV4cG9zdXJlIHBsYW4g
YW5kIHByb2plY3Qtc3BlY2lmaWMgY29udGV4dCB3aXRoIHRoZSBjb21wZXRlbnQgYXV0aG9yaXR5
LgogICAgbGltaXRhdGlvbnM6IFRoaXMgY2xhc3NpZmljYXRpb24gdXNlcyBvbmx5IHRoZSBvZmZp
Y2lhbCBDTklHIGNvZGUgbWVhbmluZyBhbmQgZG9lcyBub3QgaW50ZXJwcmV0IHRoZSBsb2NhbCBw
bGFuIG9yIGRldGVybWluZSBwcm9qZWN0IGFkbWlzc2liaWxpdHkuCiAgLSBmZWF0dXJlX2ZhbWls
eTogSU5GT1JNQVRJT04KICAgIHR5cGVfY29kZTogIjk5IgogICAgc3VidHlwZV9jb2RlOiAiMDAi
CiAgICBleHBlY3RlZF9vZmZpY2lhbF9sYWJlbDogQXV0cmUgcMOpcmltw6h0cmUsIHNlY3RldXIs
IHBsYW4sIGRvY3VtZW50LCBzaXRlLCBwcm9qZXQsIGVzcGFjZS4KICAgIGV4cGVjdGVkX2xlZ2Fs
X3JlZmVyZW5jZTogbnVsbAogICAgZXhwZWN0ZWRfcmVndWxhdGlvbl9yZWZlcmVuY2U6IG51bGwK
ICAgIHByZWNoZWNrX3N0YXR1czogVU5LTk9XTgogICAgY29uZmlkZW5jZTogTE9XCiAgICByYXRp
b25hbGU6IFRoZSBvZmZpY2lhbCBjb2RlIGlzIGFuIHVuc3BlY2lmaWVkIG90aGVyLWluZm9ybWF0
aW9uIGNhdGVnb3J5IGFuZCBpcyB0b28gZ2VuZXJpYyBmb3IgYSBtb3JlIHByZWNpc2UgQkVTUyBw
cmVjaGVjay4KICAgIHJlcXVpcmVkX2h1bWFuX2FjdGlvbjogSWRlbnRpZnkgYW5kIHJldmlldyB0
aGUgZmVhdHVyZS1zcGVjaWZpYyBsb2NhbCBzb3VyY2UgYmVmb3JlIGRyYXdpbmcgYW55IHBsYW5u
aW5nIGluZmVyZW5jZS4KICAgIGxpbWl0YXRpb25zOiBUaGUgb2ZmaWNpYWwgY29kZSBhbG9uZSBk
b2VzIG5vdCBpZGVudGlmeSB0aGUgbG9jYWwgc3ViamVjdCwgcnVsZSwgZWZmZWN0LCBhdXRob3Jp
emF0aW9uLCBvciBwcm9oaWJpdGlvbi4KICAtIGZlYXR1cmVfZmFtaWx5OiBQUkVTQ1JJUFRJT04K
ICAgIHR5cGVfY29kZTogIjAxIgogICAgc3VidHlwZV9jb2RlOiAiMDAiCiAgICBleHBlY3RlZF9v
ZmZpY2lhbF9sYWJlbDogRXNwYWNlIGJvaXPDqSBjbGFzc8OpCiAgICBleHBlY3RlZF9sZWdhbF9y
ZWZlcmVuY2U6IEwxMTMtMQogICAgZXhwZWN0ZWRfcmVndWxhdGlvbl9yZWZlcmVuY2U6IFIxNTEt
MzEgMcKwCiAgICBwcmVjaGVja19zdGF0dXM6IExJS0VMWV9NQVRFUklBTF9DT05TVFJBSU5UCiAg
ICBjb25maWRlbmNlOiBISUdICiAgICByYXRpb25hbGU6IFRoZSBvZmZpY2lhbCBjb2RlIGlkZW50
aWZpZXMgYSBjbGFzc2lmaWVkIHdvb2RlZC1hcmVhIHByb3RlY3Rpb24gZmFtaWx5IGxpa2VseSB0
byBiZSBtYXRlcmlhbCBmb3IgYSBCRVNTIHByb2plY3Qgd2l0aG91dCBtZWFuaW5nIHByb2hpYml0
ZWQuCiAgICByZXF1aXJlZF9odW1hbl9hY3Rpb246IFJldmlldyB0aGUgZXhhY3QgY2xhc3NpZmll
ZC1hcmVhIGdlb21ldHJ5LCBsb2NhbCBwcmVzY3JpcHRpb24sIGFwcGxpY2FibGUgcGxhbm5pbmcg
cHJvdmlzaW9ucywgYW5kIHByb2plY3QgZGVzaWduIHdpdGggdGhlIGNvbXBldGVudCBhdXRob3Jp
dHkuCiAgICBsaW1pdGF0aW9uczogVGhpcyBwcmVsaW1pbmFyeSBjbGFzc2lmaWNhdGlvbiBkb2Vz
IG5vdCBpbnRlcnByZXQgdGhlIGxvY2FsIHByZXNjcmlwdGlvbiBvciBlc3RhYmxpc2ggYXV0aG9y
aXphdGlvbiBvciBwcm9oaWJpdGlvbi4KICAtIGZlYXR1cmVfZmFtaWx5OiBQUkVTQ1JJUFRJT04K
ICAgIHR5cGVfY29kZTogIjA1IgogICAgc3VidHlwZV9jb2RlOiAiMDAiCiAgICBleHBlY3RlZF9v
ZmZpY2lhbF9sYWJlbDogRW1wbGFjZW1lbnQgcsOpc2VydsOpCiAgICBleHBlY3RlZF9sZWdhbF9y
ZWZlcmVuY2U6IEwxNTEtNDEgMcKwIMOgIDPCsAogICAgZXhwZWN0ZWRfcmVndWxhdGlvbl9yZWZl
cmVuY2U6IFIxNTEtMzQgNMKwLCBSMTUxLTM4IDHCsCwgUjE1MS00MyAzwrAsIFIxNTEtNDggMsKw
LCBSMTUxLTUwIDHCsAogICAgcHJlY2hlY2tfc3RhdHVzOiBNQVRFUklBTF9SRVZJRVdfUkVRVUlS
RUQKICAgIGNvbmZpZGVuY2U6IEhJR0gKICAgIHJhdGlvbmFsZTogVGhlIG9mZmljaWFsIGNvZGUg
aWRlbnRpZmllcyBhIHJlc2VydmVkLXNpdGUgcGxhbm5pbmcgbWVjaGFuaXNtIHRoYXQgbWF5IG1h
dGVyaWFsbHkgYWZmZWN0IGEgcHJvamVjdCBhbmQgcmVxdWlyZXMgc3BlY2lmaWMgcmV2aWV3Lgog
ICAgcmVxdWlyZWRfaHVtYW5fYWN0aW9uOiBSZXZpZXcgdGhlIGJlbmVmaWNpYXJ5LCBwdXJwb3Nl
LCBleGFjdCByZXNlcnZhdGlvbiwgbG9jYWwgcGxhbm5pbmcgZG9jdW1lbnRzLCBhbmQgcHJvamVj
dCBpbnRlcmFjdGlvbiB3aXRoIHRoZSBjb21wZXRlbnQgYXV0aG9yaXR5LgogICAgbGltaXRhdGlv
bnM6IFRoaXMgY2xhc3NpZmljYXRpb24gZG9lcyBub3QgaW5mZXIgdGhlIHJlc2VydmF0aW9uIHB1
cnBvc2UgZnJvbSBsb2NhbCB0ZXh0IG9yIGRldGVybWluZSB3aGV0aGVyIGEgQkVTUyBwcm9qZWN0
IGlzIGF1dGhvcml6ZWQgb3IgcHJvaGliaXRlZC4KICAtIGZlYXR1cmVfZmFtaWx5OiBQUkVTQ1JJ
UFRJT04KICAgIHR5cGVfY29kZTogIjA3IgogICAgc3VidHlwZV9jb2RlOiAiMDAiCiAgICBleHBl
Y3RlZF9vZmZpY2lhbF9sYWJlbDogUGF0cmltb2luZSBiw6J0aSwgcGF5c2FnZXIgb3Ugw6lsw6lt
ZW50cyBkZSBwYXlzYWdlcyDDoCBwcm90w6lnZXIgcG91ciBkZXMgbW90aWZzIGQnb3JkcmUgY3Vs
dHVyZWwsIGhpc3RvcmlxdWUsIGFyY2hpdGVjdHVyYWwgb3Ugw6ljb2xvZ2lxdWUKICAgIGV4cGVj
dGVkX2xlZ2FsX3JlZmVyZW5jZTogTDE1MS0xOSBldCBMMTUxLTIzCiAgICBleHBlY3RlZF9yZWd1
bGF0aW9uX3JlZmVyZW5jZTogUjE1MS00MSAzwrAgRXQgUjE1MS00MwogICAgcHJlY2hlY2tfc3Rh
dHVzOiBMSUtFTFlfTUFURVJJQUxfQ09OU1RSQUlOVAogICAgY29uZmlkZW5jZTogTUVESVVNCiAg
ICByYXRpb25hbGU6IFRoZSBvZmZpY2lhbCBjb2RlIGlkZW50aWZpZXMgYSBicm9hZCBoZXJpdGFn
ZSBvciBsYW5kc2NhcGUgcHJvdGVjdGlvbiBmYW1pbHkgbGlrZWx5IHRvIGJlIG1hdGVyaWFsLCB3
aGlsZSBpdHMgZXhhY3QgbG9jYWwgc3ViamVjdCByZW1haW5zIHVuc3BlY2lmaWVkLgogICAgcmVx
dWlyZWRfaHVtYW5fYWN0aW9uOiBSZXZpZXcgdGhlIHByb3RlY3RlZCBlbGVtZW50LCBsb2NhbCBw
cmVzY3JpcHRpb24sIHByb2plY3Qgc2l0aW5nIGFuZCBkZXNpZ24sIGFuZCBjb21wZXRlbnQtYXV0
aG9yaXR5IHJlcXVpcmVtZW50cy4KICAgIGxpbWl0YXRpb25zOiBUaGUgYnJvYWQgb2ZmaWNpYWwg
Y2F0ZWdvcnkgZG9lcyBub3QgcmV2ZWFsIHRoZSBmZWF0dXJlLXNwZWNpZmljIHByb3RlY3RlZCBz
dWJqZWN0IG9yIGVzdGFibGlzaCBhdXRob3JpemF0aW9uIG9yIHByb2hpYml0aW9uLgogIC0gZmVh
dHVyZV9mYW1pbHk6IFBSRVNDUklQVElPTgogICAgdHlwZV9jb2RlOiAiMDciCiAgICBzdWJ0eXBl
X2NvZGU6ICIwNCIKICAgIGV4cGVjdGVkX29mZmljaWFsX2xhYmVsOiDDiWzDqW1lbnRzIGRlIHBh
eXNhZ2UsIChzaXRlcyBldCBzZWN0ZXVycykgw6AgcHLDqXNlcnZlciBwb3VyIGRlcyBtb3RpZnMg
ZCdvcmRyZSDDqWNvbG9naXF1ZQogICAgZXhwZWN0ZWRfbGVnYWxfcmVmZXJlbmNlOiBMMTUxLTIz
CiAgICBleHBlY3RlZF9yZWd1bGF0aW9uX3JlZmVyZW5jZTogUjE1MS00MyA1wrAKICAgIHByZWNo
ZWNrX3N0YXR1czogTElLRUxZX01BVEVSSUFMX0NPTlNUUkFJTlQKICAgIGNvbmZpZGVuY2U6IEhJ
R0gKICAgIHJhdGlvbmFsZTogVGhlIG9mZmljaWFsIHN1YnR5cGUgaWRlbnRpZmllcyBlY29sb2dp
Y2FsIGxhbmRzY2FwZSBwcmVzZXJ2YXRpb24gbGlrZWx5IHRvIGJlIG1hdGVyaWFsIGZvciBhIEJF
U1MgcHJvamVjdCB3aXRob3V0IG1lYW5pbmcgcHJvaGliaXRlZC4KICAgIHJlcXVpcmVkX2h1bWFu
X2FjdGlvbjogUmV2aWV3IHRoZSBleGFjdCBwcmVzZXJ2ZWQgZWxlbWVudCwgbG9jYWwgcHJlc2Ny
aXB0aW9uLCBlY29sb2dpY2FsIGNvbnRleHQsIGFuZCBwcm9qZWN0IGRlc2lnbiB3aXRoIHRoZSBj
b21wZXRlbnQgYXV0aG9yaXR5LgogICAgbGltaXRhdGlvbnM6IFRoaXMgY2xhc3NpZmljYXRpb24g
ZG9lcyBub3QgaW50ZXJwcmV0IHRoZSBsb2NhbCBwcmVzZXJ2YXRpb24gcnVsZSBvciBkZXRlcm1p
bmUgcHJvamVjdCBhZG1pc3NpYmlsaXR5LgogIC0gZmVhdHVyZV9mYW1pbHk6IFBSRVNDUklQVElP
TgogICAgdHlwZV9jb2RlOiAiMTUiCiAgICBzdWJ0eXBlX2NvZGU6ICIwMCIKICAgIGV4cGVjdGVk
X29mZmljaWFsX2xhYmVsOiBSw6hnbGVzIGTigJlpbXBsYW50YXRpb24gZGVzIGNvbnN0cnVjdGlv
bnMKICAgIGV4cGVjdGVkX2xlZ2FsX3JlZmVyZW5jZTogTDE1MS0xNyBldCBMMTUxLTE4CiAgICBl
eHBlY3RlZF9yZWd1bGF0aW9uX3JlZmVyZW5jZTogUjE1MS0zOSBkZXJuaWVyIGFsLgogICAgcHJl
Y2hlY2tfc3RhdHVzOiBERVNJR05fUkVWSUVXX1JFUVVJUkVECiAgICBjb25maWRlbmNlOiBNRURJ
VU0KICAgIHJhdGlvbmFsZTogVGhlIG9mZmljaWFsIGNvZGUgcHJpbWFyaWx5IGlkZW50aWZpZXMg
Y29uc3RydWN0aW9uLWltcGxhbnRhdGlvbiBydWxlcyByZWxldmFudCB0byBwcm9qZWN0IHNpdGlu
ZyBhbmQgZGVzaWduLCB3aGlsZSB0aGUgbG9jYWwgcnVsZSByZW1haW5zIHVucmVhZC4KICAgIHJl
cXVpcmVkX2h1bWFuX2FjdGlvbjogUmV2aWV3IHRoZSBleGFjdCBsb2NhbCBpbXBsYW50YXRpb24g
cnVsZSBhZ2FpbnN0IHRoZSBwcm9wb3NlZCBlcXVpcG1lbnQgbGF5b3V0IGFuZCBzaXRlIGRlc2ln
bi4KICAgIGxpbWl0YXRpb25zOiBUaGlzIGNsYXNzaWZpY2F0aW9uIGRvZXMgbm90IGludGVycHJl
dCBsb2NhbCBzZXRiYWNrcywgZmVhdHVyZSB0ZXh0LCBvciBwcm9qZWN0IGNvbXBsaWFuY2UuCiAg
LSBmZWF0dXJlX2ZhbWlseTogUFJFU0NSSVBUSU9OCiAgICB0eXBlX2NvZGU6ICIxNSIKICAgIHN1
YnR5cGVfY29kZTogIjAxIgogICAgZXhwZWN0ZWRfb2ZmaWNpYWxfbGFiZWw6IEltcGxhbnRhdGlv
biBkZXMgY29uc3RydWN0aW9ucyBwYXIgcmFwcG9ydCBhdXggdm9pZXMgZXQgYXV4IGVtcHJpc2Vz
IHB1YmxpcXVlcwogICAgZXhwZWN0ZWRfbGVnYWxfcmVmZXJlbmNlOiBMMTUxLTE3IGV0IEwxNTEt
MTgKICAgIGV4cGVjdGVkX3JlZ3VsYXRpb25fcmVmZXJlbmNlOiBSMTUxLTM5CiAgICBwcmVjaGVj
a19zdGF0dXM6IERFU0lHTl9SRVZJRVdfUkVRVUlSRUQKICAgIGNvbmZpZGVuY2U6IEhJR0gKICAg
IHJhdGlvbmFsZTogVGhlIG9mZmljaWFsIHN1YnR5cGUgc3BlY2lmaWNhbGx5IGlkZW50aWZpZXMg
Y29uc3RydWN0aW9uIHNpdGluZyByZWxhdGl2ZSB0byByb2FkcyBhbmQgcHVibGljIHJpZ2h0cy1v
Zi13YXksIHJlcXVpcmluZyBkZXNpZ24gcmV2aWV3LgogICAgcmVxdWlyZWRfaHVtYW5fYWN0aW9u
OiBSZXZpZXcgdGhlIGV4YWN0IGxvY2FsIHNpdGluZyBvciBzZXRiYWNrIHJ1bGUgYWdhaW5zdCB0
aGUgcHJvcG9zZWQgZXF1aXBtZW50IGxheW91dCBhbmQgYWNjZXNzIGRlc2lnbi4KICAgIGxpbWl0
YXRpb25zOiBUaGlzIGNsYXNzaWZpY2F0aW9uIGRvZXMgbm90IGludGVycHJldCB0aGUgbG9jYWwg
c2V0YmFjayB2YWx1ZSBvciBlc3RhYmxpc2ggcHJvamVjdCBjb21wbGlhbmNlLgogIC0gZmVhdHVy
ZV9mYW1pbHk6IFBSRVNDUklQVElPTgogICAgdHlwZV9jb2RlOiAiMTciCiAgICBzdWJ0eXBlX2Nv
ZGU6ICIwMCIKICAgIGV4cGVjdGVkX29mZmljaWFsX2xhYmVsOiBTZWN0ZXVyIMOgIHByb2dyYW1t
ZSBkZSBsb2dlbWVudHMgbWl4aXTDqSBzb2NpYWxlIGVuIHpvbmUgVSBldCBBVQogICAgZXhwZWN0
ZWRfbGVnYWxfcmVmZXJlbmNlOiBMMTUxLTE1CiAgICBleHBlY3RlZF9yZWd1bGF0aW9uX3JlZmVy
ZW5jZTogUjE1MS0zOCAzwrAKICAgIHByZWNoZWNrX3N0YXR1czogTUFURVJJQUxfUkVWSUVXX1JF
UVVJUkVECiAgICBjb25maWRlbmNlOiBNRURJVU0KICAgIHJhdGlvbmFsZTogVGhlIG9mZmljaWFs
IGNvZGUgaWRlbnRpZmllcyBhIHNvY2lhbC1ob3VzaW5nLXByb2dyYW0gcGxhbm5pbmcgbWVjaGFu
aXNtIHRoYXQgbWF5IG1hdGVyaWFsbHkgYWZmZWN0IGxhbmQgdXNlIGFuZCByZXF1aXJlcyBzcGVj
aWZpYyByZXZpZXcuCiAgICByZXF1aXJlZF9odW1hbl9hY3Rpb246IFJldmlldyB0aGUgc2VjdG9y
IHByb2dyYW0sIGxvY2FsIHBsYW5uaW5nIHByb3Zpc2lvbnMsIGxhbmQtdXNlIGludGVyYWN0aW9u
LCBhbmQgYXV0aG9yaXR5IHJlcXVpcmVtZW50cyBmb3IgdGhlIHByb3Bvc2VkIHByb2plY3QuCiAg
ICBsaW1pdGF0aW9uczogVGhpcyBjbGFzc2lmaWNhdGlvbiBkb2VzIG5vdCBpbmZlciB0aGUgbG9j
YWwgcHJvZ3JhbSBjb250ZW50IG9yIGRldGVybWluZSBCRVNTIGF1dGhvcml6YXRpb24gb3IgcHJv
aGliaXRpb24uCiAgLSBmZWF0dXJlX2ZhbWlseTogUFJFU0NSSVBUSU9OCiAgICB0eXBlX2NvZGU6
ICIxOCIKICAgIHN1YnR5cGVfY29kZTogIjAwIgogICAgZXhwZWN0ZWRfb2ZmaWNpYWxfbGFiZWw6
IFDDqXJpbcOodHJlIGNvbXBvcnRhbnQgZGVzIG9yaWVudGF0aW9ucyBk4oCZYW3DqW5hZ2VtZW50
IGV0IGRlIHByb2dyYW1tYXRpb24gKE9BUCkKICAgIGV4cGVjdGVkX2xlZ2FsX3JlZmVyZW5jZTog
TDE1MS02IGV0IEwxNTEtNwogICAgZXhwZWN0ZWRfcmVndWxhdGlvbl9yZWZlcmVuY2U6IFIxNTEt
NiDDoCBSMTUxLTgtMQogICAgcHJlY2hlY2tfc3RhdHVzOiBNQVRFUklBTF9SRVZJRVdfUkVRVUlS
RUQKICAgIGNvbmZpZGVuY2U6IEhJR0gKICAgIHJhdGlvbmFsZTogVGhlIG9mZmljaWFsIGNvZGUg
aWRlbnRpZmllcyBhbiBhcmVhIGdvdmVybmVkIGJ5IHBsYW5uaW5nIGFuZCBkZXZlbG9wbWVudCBn
dWlkZWxpbmVzIHRoYXQgbWF5IG1hdGVyaWFsbHkgYWZmZWN0IGEgcHJvamVjdCBhbmQgcmVxdWly
ZXMgc3BlY2lmaWMgcmV2aWV3LgogICAgcmVxdWlyZWRfaHVtYW5fYWN0aW9uOiBSZXZpZXcgdGhl
IGFwcGxpY2FibGUgT0FQIHRleHQgYW5kIGdyYXBoaWNzLCBwcm9qZWN0IGRlc2lnbiBpbnRlcmFj
dGlvbiwgYW5kIGNvbXBldGVudC1hdXRob3JpdHkgcmVxdWlyZW1lbnRzLgogICAgbGltaXRhdGlv
bnM6IFRoaXMgY2xhc3NpZmljYXRpb24gZG9lcyBub3QgaW50ZXJwcmV0IHRoZSBsb2NhbCBPQVAg
b3IgZXN0YWJsaXNoIGF1dGhvcml6YXRpb24sIHByb2hpYml0aW9uLCBvciBidWlsZGFiaWxpdHku
Cg==
```
