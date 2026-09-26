# `configs/planning/muret_plu_structure.yaml`

## File identity

- Repository path: `configs/planning/muret_plu_structure.yaml`.
- File type: human-authored YAML documentary grammar, not a BESS policy.
- Source SHA256 basis: `git-content`
- Source SHA256: `74bf407441b66cde62efda581fbbb7df0d27b9d2148b210b7749ddf61b1b763a`
- Git blob OID: `77d73d96066a0b4a8ee18c4de3bf24d07a1aacf5`.
- Git and R7 checkout: identical 2,287 UTF-8 bytes, 101 LF, zero CR, final LF.
- Canonical validated-model SHA256: `13d028fe4b58d30929ff9fdedae90e2cc95983a3296f2f83c2817d0da381107a`; this is not the raw-file digest.

The [R7 receipt](../../../audit/R7_PLU_STRUCTURE_CONFIGURATION.md) records the one offline loader call, byte checks, read ranges and limitations. The YAML is unchanged. The old raw digest/snapshots were already correct; the old model declaration and generic explanatory text were not a reliable account of the current boundary.

## 1. Purpose and boundary

This file configures how indexed Muret PLU text is partitioned into factual headings/sections, how exact source-zone labels map to chapters, and which literal thematic terms are reported. It does not decide land-use eligibility. `muret_plu_20240215_v1` is a profile identifier, not schema version 1: the supported configuration schema is **2**.

A heading match, alias, topic count or source hash proves neither legal applicability nor a BESS permission/prohibition. An ICPE term is not an ICPE classification. A missing term does not prove absence of a real constraint. No scoring, ranking, parcel rejection, owner/contact logic, new PDF interpretation or official-source acquisition occurs in this configuration audit.

## 2. Owner and data flow

The owner is [structure_planning_regulation.py](../../../../../src/landscout/stages/structure_planning_regulation.py), with [its technical companion](../../src/landscout/stages/structure_planning_regulation.py.md). Its loader returns `PlanningRegulationStructureConfig`. The high-level API is also re-exported by `landscout.stages`.

`PlanningRegulationIndex` + zone catalog + zoning intersections + this config produce `PlanningRegulationStructureResult`: three ordinary mutable DataFrames, `sections`, `zone_mapping` and `topic_evidence`, inside a frozen dataclass carrying lineage and hashes. A frozen result envelope is not a deeply immutable frame.

Downstream [interpret_bess_zoning.py](../../../../../src/landscout/stages/interpret_bess_zoning.py) receives those inputs plus parcels, a GPU planning document and a **separate** written-zoning policy. It physically revalidates zoning first, rebuilds/validates the factual structure and fragments, then applies its own locks, required-article completeness and evidence routes. Required article IDs and BESS outcomes are not fields in this YAML. See the separately audited [written-zoning policy](muret_bess_zoning_policy.yaml.md); its approval does not approve this companion.

## 3. Loading, immutable models and field contracts

`load_planning_regulation_structure_config` constructs `Path(path)`, reads bytes and calls [loads_strict_yaml](../../../../../src/landscout/common/strict_yaml.py). Paths are relative to the caller's working directory unless absolute; there is no default config path or adjacent-file discovery. The safe YAML loader requires UTF-8 and rejects duplicate keys at every depth, including after merge flattening. The root must be a mapping.

All six concrete config models inherit `_StrictConfigModel` with `extra="forbid", frozen=True`. Missing required fields, null for any field, unknown keys, wrong literals and scalar coercions prohibited by `StrictStr`/`StrictInt`/`StrictBool` fail validation. Strict integers exclude booleans, strings and floats. Lists in YAML become ordered tuples, not sorted sets. Root mappings become independently copied `FrozenDict` values through [freeze_mapping](../../../../../src/landscout/common/immutable_mapping.py); nested term lists become tuples. No caller-owned backing dictionary is retained. Mutation through mapping operations or field assignment fails.

`zone_aliases` is declared `Mapping[StrictStr, StrictStr]` and `topics` is `Mapping[StrictStr, tuple[StrictStr, ...]]`, **not dict fields**. Serializers return fresh ordinary dictionaries; JSON topic serialization returns fresh lists while Python mode retains immutable tuple values. These detached serialization products are not aliases for mutation of the retained config. `_resolved_config` reconstructs an incoming model from `model_dump(mode="python")` and validates it again; passing a frozen instance or an unchecked `model_copy(update=...)` does not bypass this boundary. A path is reloaded instead.

| Field/family | Required/default and retained type | Validation, transformation and use |
|---|---|---|
| `schema_version` | Required strict integer | Root accepts exactly 2. It is copied into result lineage and hashed. |
| `structure_profile` | Required strict string, nonempty | Root requires equality with its stripped value; no trimming is performed. Exact profile appears in all output frames and hashes. |
| `document_lock` | Required `DocumentLockConfig`, five required strings | Nested model requires nonempty document/profile strings and three lowercase 64-hex SHA strings. Root additionally checks document ID and normalization profile for nonempty exact stripped equality. This is not a document-ID-format or profile-enum validator. |
| `document_layout` | Required `DocumentLayoutConfig` | Four fields below; checks on real indexed page existence occur later, not in the loader. |
| `body_start_page` | Required strict integer ≥1 | First page eligible for structural heading recognition and body extraction-error gating; does not discard preceding records/topic text. Configured 1. |
| `table_of_contents_pages` | Optional tuple of strict integers, default `()` | Positive, unique, ascending; validator compares with sorted unique pages but never sorts the input. Configured YAML `[]` becomes `()`. |
| `max_heading_continuation_lines` | Required strict integer, 0..10 inclusive | Maximum extra lines after a non-zone heading, same source page. Configured 2, not a default. |
| `include_table_of_contents_in_topic_evidence` | Optional strict Boolean, default `False` | Configured false; suppresses thematic rows on declared TOC pages without dropping their retained records/sections. |
| `heading_patterns` | Required `HeadingPatternsConfig` | `zone_chapter`, `article`, `general_section` required nonempty tuples of strict strings. `continuation` defaults to `()`. Nested model checks types/lengths; root performs regex/exactness/capture checks. |
| `ignored_patterns` | Required `IgnoredPatternsConfig` | `page_headers` and `page_footers` each default to `()`; root validates their member strings/regexes. The enclosing object itself has no default. |
| `zone_aliases` | Required immutable mapping; empty mapping allowed | Both keys and targets nonempty exact strings; root rejects cycles including self-cycles. It does not require terminal targets to be present in an index it has not received. |
| `topics` | Required immutable mapping of tuple terms | Root requires ≥1 topic and ≥1 term per topic. Topic names and terms nonempty/exact. Every term normalizes nonempty; duplicate normalized terms rejected **within** each topic, not across topics. |
| `topic_match_policy` | Required `TopicMatchPolicyConfig` | Both fields required; only `boundary_mode="token"` and `overlap_resolution="longest_match"`. Derived `identifier` is `token_longest_match`, not another YAML field. |
| `topic_context_characters` | Required strict integer ≥0, no upper bound in this model | Configured 80 normalized Python characters on each side of the first retained match, clipped to the section/page fragment. Included in the model hash. |

All fields participate in the complete model hash. Nested model construction alone is not equivalent to the root's regex, exact-string, alias-cycle or normalized-term checks. The local SHA shape is not physical proof of the indexed pages.

## 4. Exact configuration values

Ten root fields; five locks; four layout fields; four heading families containing four regexes; two ignored families containing two header regexes and zero footer regexes; 17 aliases; 13 topics / 30 terms; two match-policy fields. **68 terminal values**: 61 strings, four integers, one Boolean and two empty arrays; no nulls. Keys, list order, apostrophes, accents and case below are literal. JSON strings use doubled backslashes to display a single decoded regex backslash; the exact YAML snapshot retains its original single-quoted regex scalars.

| Exact YAML path | Exact decoded value as JSON | Retained leaf type |
|---|---|---|
| `schema_version` | `2` | `int` |
| `structure_profile` | `"muret_plu_20240215_v1"` | `str` |
| `document_lock.document_id` | `"33edb4c9f6943c88d8d92518bff20bec"` | `str` |
| `document_lock.pdf_sha256` | `"5358ebad6b0cda6de681ba3536e29b8b6291fb701c7d3711f4ee1d6fdb85c6fb"` | `str` |
| `document_lock.pages_content_sha256` | `"928e7e59c45e27c38e39d3f28f3eb10bd2590886416df57efc4ac8e5d8901ec9"` | `str` |
| `document_lock.index_content_sha256` | `"6a0009228ca17128c0a8bb329d9c2277a1b6638708a67b913b72ee93063e42cd"` | `str` |
| `document_lock.normalization_profile` | `"fr_literal_v1"` | `str` |
| `document_layout.body_start_page` | `1` | `int` |
| `document_layout.table_of_contents_pages` | `[]` | `tuple (empty)` |
| `document_layout.max_heading_continuation_lines` | `2` | `int` |
| `document_layout.include_table_of_contents_in_topic_evidence` | `false` | `bool` |
| `heading_patterns.zone_chapter[0]` | `"^ZONE\\s+(?P<label>[A-Za-z]+(?:\\s*0)?)\\s*$"` | `str` |
| `heading_patterns.article[0]` | `"^ARTICLE\\s+(?P<zone>[A-Za-z]+(?:\\s*0)?)\\s+(?P<number>\\d+(?:\\.\\d+)?)\\s*[-–—]\\s*(?P<title>.*)$"` | `str` |
| `heading_patterns.general_section[0]` | `"^ARTICLE\\s+(?P<number>\\d+(?:\\.\\d+)?)\\s*[-–—]\\s*(?P<title>.*)$"` | `str` |
| `heading_patterns.continuation[0]` | `"^[^a-z]*[A-ZÀ-ÖØ-ÞŒ][^a-z]*$"` | `str` |
| `ignored_patterns.page_headers[0]` | `"^Muret-12ème modification du PLU$"` | `str` |
| `ignored_patterns.page_headers[1]` | `"^\\d+$"` | `str` |
| `ignored_patterns.page_footers` | `[]` | `tuple (empty)` |
| `zone_aliases.UAa` | `"UA"` | `str` |
| `zone_aliases.UAb` | `"UA"` | `str` |
| `zone_aliases.UBa` | `"UB"` | `str` |
| `zone_aliases.UBb` | `"UB"` | `str` |
| `zone_aliases.UFa` | `"UF"` | `str` |
| `zone_aliases.UFc` | `"UF"` | `str` |
| `zone_aliases.UFd` | `"UF"` | `str` |
| `zone_aliases.AUa` | `"AU"` | `str` |
| `zone_aliases.AUfa` | `"AUf"` | `str` |
| `zone_aliases.AUfb` | `"AUf"` | `str` |
| `zone_aliases.AUfc` | `"AUf"` | `str` |
| `zone_aliases.AUfd` | `"AUf"` | `str` |
| `zone_aliases.AUfo` | `"AUf0"` | `str` |
| `zone_aliases.NL` | `"N"` | `str` |
| `zone_aliases.Ne` | `"N"` | `str` |
| `zone_aliases.Nh` | `"N"` | `str` |
| `zone_aliases.Nr` | `"N"` | `str` |
| `topics.destination_and_use[0]` | `"occupation du sol"` | `str` |
| `topics.destination_and_use[1]` | `"utilisation du sol"` | `str` |
| `topics.destination_and_use[2]` | `"destination"` | `str` |
| `topics.public_interest_equipment[0]` | `"équipement public"` | `str` |
| `topics.public_interest_equipment[1]` | `"équipement d'intérêt collectif"` | `str` |
| `topics.public_interest_equipment[2]` | `"service public"` | `str` |
| `topics.public_interest_equipment[3]` | `"intérêt collectif"` | `str` |
| `topics.technical_equipment[0]` | `"ouvrage technique"` | `str` |
| `topics.technical_equipment[1]` | `"installations techniques"` | `str` |
| `topics.technical_equipment[2]` | `"locaux techniques"` | `str` |
| `topics.energy[0]` | `"énergie"` | `str` |
| `topics.electricity[0]` | `"électricité"` | `str` |
| `topics.electricity[1]` | `"électrique"` | `str` |
| `topics.transformer[0]` | `"transformateur"` | `str` |
| `topics.classified_installation[0]` | `"installation classée"` | `str` |
| `topics.classified_installation[1]` | `"installations classées"` | `str` |
| `topics.classified_installation[2]` | `"ICPE"` | `str` |
| `topics.risk[0]` | `"risque"` | `str` |
| `topics.risk[1]` | `"risques"` | `str` |
| `topics.nuisance[0]` | `"nuisance"` | `str` |
| `topics.nuisance[1]` | `"nuisances"` | `str` |
| `topics.fire_safety[0]` | `"incendie"` | `str` |
| `topics.fire_safety[1]` | `"défense contre l'incendie"` | `str` |
| `topics.access[0]` | `"accès"` | `str` |
| `topics.access[1]` | `"desserte"` | `str` |
| `topics.setbacks[0]` | `"recul"` | `str` |
| `topics.setbacks[1]` | `"distance minimale"` | `str` |
| `topics.setbacks[2]` | `"implantation"` | `str` |
| `topics.networks[0]` | `"réseau"` | `str` |
| `topics.networks[1]` | `"réseaux"` | `str` |
| `topic_match_policy.boundary_mode` | `"token"` | `str` |
| `topic_match_policy.overlap_resolution` | `"longest_match"` | `str` |
| `topic_context_characters` | `80` | `int` |

## 5. Document locks and retained pages

After resolving/revalidating config, `_validate_document_lock` first calls `validate_planning_regulation_index(index)`. That validator checks index metadata, supported normalization/schema versions, page order/count, extraction status, raw/normalized text, character counts and all page/pages/index hashes in memory. It does **not** reopen the PDF.

The five exact comparisons then run in this order: index `document_id` against the lock; `pdf_sha256`; `pages_content_sha256`; `index_content_sha256`; `search_normalization_profile` against `normalization_profile`. Any mismatch raises `PlanningRegulationStructureError`. There is no sixth archive lock in this YAML; archive lineage is carried by the index and checked against zoning inputs.

Next, the body start and every TOC page must be real indexed page numbers. Any page at/after body start, outside the configured TOC set, with extraction status `ERROR` stops processing. A successfully extracted blank `EMPTY` page remains valid. The loader alone receives no index and performs none of these equalities or existence checks. A correctly shaped lock/hash is not evidence that current physical PDF bytes were read.

`_line_records` visits all indexed pages in their validated order, splits raw text with `splitlines()` and applies positional header/footer filtering. The first nonblank line must fullmatch a header pattern before a leading run of matching headers and blanks is removed; symmetrically the last nonblank line must fullmatch a footer before a trailing run is removed. Matching text inside the body is preserved. With the configured empty footer list, no footer removal is enabled; the numeric regex is a **header** rule here, not a universal page-number deletion rule.

Remaining raw lines, including blanks, retain their original page/line numbers and receive sequential `RECORD-000001` IDs. No records at all fails. Before-body and TOC records remain; only their heading eligibility differs. Empty configured TOC pages prove no declared exclusion, not that the real document has no table of contents.

## 6. Exact regex behavior

All six regexes are compiled with `re.compile(pattern)` and **no added flags**: case-sensitive Unicode behavior, no IGNORECASE/MULTILINE/DOTALL. Both ignored patterns and structural/continuation patterns use `fullmatch` on the raw line's `strip()` value. Search normalization is used for output fields and topics, not before title classification. Anchors below therefore supplement whole-string matching. In these expressions `\s` and `\d` have Python's Unicode meanings, whereas `[A-Za-z]` is the literal ASCII alphabet.

| Configured member | Meaning of the exact expression shown in section 4 |
|---|---|
| `heading_patterns.zone_chapter[0]` | Literal uppercase `ZONE`, ≥1 whitespace, named `label` of ≥1 ASCII letters followed optionally by whitespace and exactly the digit `0`; optional trailing whitespace. No other numeric suffix. Captured label whitespace is removed by `_canonical_chapter_label`. |
| `heading_patterns.article[0]` | Literal uppercase `ARTICLE`; named `zone` with the same letter/optional-zero grammar; whitespace then named `number` of digits, optionally a dot and further digits; optional whitespace around one hyphen/en dash/em dash; named `title` captures the remaining text, including an initially empty title. |
| `heading_patterns.general_section[0]` | Same article-number, separator and title grammar without a zone capture between `ARTICLE` and the number. It yields GENERAL rather than a zone ARTICLE. |
| `heading_patterns.continuation[0]` | Whole line without ASCII lowercase `a-z`, containing at least one character in `A-ZÀ-ÖØ-ÞŒ`. Other characters are allowed by the two negated classes. This is **not** a Unicode-wide “uppercase only” test: e.g. lowercase accented letters are not excluded by `[^a-z]`. |
| `ignored_patterns.page_headers[0]` | Exact case/accent/hyphen/spaces of `Muret-12ème modification du PLU` after border stripping; no generic Muret/header heuristic. |
| `ignored_patterns.page_headers[1]` | One or more Unicode decimal digits only after border stripping; no punctuation or sign. It acts only within an eligible leading header run. |

Root validation first rejects exact duplicates **within each** of the six lists, empty/whitespace-padded strings and uncompilable regexes. It separately rejects an identical regex reused across the three structural groups (ZONE_CHAPTER, GENERAL, ARTICLE). Continuation/header/footer reuse across different groups is not covered by that structural cross-group check. Every structural pattern must contain the required named capture keys: `label`; `zone, number, title`; or `number, title` respectively. Presence of a capture name does not prove that a custom pattern always captures a nonempty usable value.

At runtime `_classify_structural_heading` collects **all** matches, in zone/general/article group order and pattern order. Multiple matches fail with record ID, page, line and category/pattern indexes; there is no first-match policy winner. Different valid expressions can overlap even though they pass the exact-duplicate check.

For GENERAL/ARTICLE headings only, up to two extra contiguous nonblank lines on the same page can be consumed. A continuation candidate is first checked against all structural regexes: another heading stops continuation; ambiguous structural matches raise rather than being swallowed. It must then match a continuation regex. Zero allowed continuation lines means no extra line; zone-chapter headings never continue. `heading_raw` joins original lines by LF; normalized heading is separately derived. The title joins stripped captured title and continuation lines with spaces, then strips; an empty final title becomes None and is rejected by the later GENERAL/ARTICLE section contract.

Article numbers remain captured strings (including any decimal syntax), not integers or required-article completeness judgments. Chapter labels remove captured whitespace. The builder compares an ARTICLE's captured zone to the active chapter with `casefold()` and retains the chapter spelling; this local parent check is distinct from the case-sensitive GPU-label mapping below.

## 7. Section partition and page fragments

`_section_starts` builds boundaries at recognized headings and at contiguous configured TOC blocks; TOC sections are forced OTHER. Nonempty prefix text becomes OTHER; ordinary blank prefixes/gaps attach to the next actual heading, trailing blank records to the preceding section. Explicit blank TOC blocks remain OTHER even if blank-only (a following blank tail can join them). Empty pages with no retained lines do not manufacture a record. Source records form a lossless, ordered partition **after positional filtering**, not a byte-for-byte copy of the whole original PDF or its original newline separators.

Sections have sequential `SECTION-0001` IDs. ZONE_CHAPTER opens the active chapter; ARTICLE must have a preceding chapter and matching captured zone; GENERAL clears the active chapter; OTHER itself has no parent/zone/article fields. Chapter/OTHER article fields are null. ARTICLE and GENERAL require nonempty article number/title in final validation. No new chapter-title semantics or legal conclusion is inferred.

Each section retains raw text joined by LF, separately normalized text, Python-character count, inclusive first/last record IDs, record count/hash, source pages in ascending unique order, heading, nullable parent/zone/article information and lineage. The page fragment for each section/page joins that section's retained lines on that page by LF. Fragment offsets later used by policy refer to this reconstructed text, not PDF file-byte offsets.

Self-validation checks exact frame column order, nonempty sections, sequential IDs, known/in-order pages, source-record partition without omission/duplication, raw/normalized text and counts, row/record/lineage hashes and parent semantics. Reconstruction subsequently compares the expected values independently; a coordinated outer rehash is not source authority.

## 8. Exact aliases, mapping and counts

All 17 literal alias pairs are listed in section 4 and the snapshot. They are not fuzzy prefixes or case-normalization instructions. In particular `AUfo → AUf0` maps source lowercase letter **o** to target digit **0** for this **one exact key**; it does not enable a general o/0 substitution. Heading grammar capture, captured-label whitespace removal and source-label resolution are separate operations. Raw GPU labels are required exact nonempty strings and are not stripped or rewritten.

For each sorted distinct raw label in the supplied zone catalog, `_build_zone_mapping` first counts chapters with exactly that label. One yields EXACT / EXACT_HEADING, same label and section ID. More than one yields AMBIGUOUS / AMBIGUOUS with no resolved label or section. Only zero exact chapters allows traversal of the explicit alias mapping to its final non-key target; cycles are rejected by root validation and guarded again during traversal. One target chapter yields CONFIG_ALIAS / CONFIG_ALIAS; several yield AMBIGUOUS with the final target label but no matched section. No key, or no chapter at the terminal target, yields UNMAPPED / NONE with null resolved label/section. An exact match takes priority over any configured alias.

The loader does not validate that all aliases are used or targets exist in a future document. No fallback by prefix, casefold, spelling similarity, general zero replacement or implicit parent-zone family exists in this mapping.

Per-label counts are: catalog polygons; distinct candidate parcels; all candidate intersection rows (including TOUCH_ONLY); and dominant candidates. Dominance uses only positive areas, stable ordering by parcel ID, descending intersection area, then ascending planning-zone ID, and keeps one row per parcel. Any dominant label not EXACT/CONFIG_ALIAS aborts. Non-dominant unresolved labels stay explicit. Counts must satisfy dominant ≤ parcels ≤ intersections; polygon count is positive. These counts are factual coverage, not scores.

## 9. Literal topics, ordering and character positions

The terms in section 4 are literal strings, not regexes. The index and structure use the same [planning_text.py](../../../../../src/landscout/common/planning_text.py) functions under `fr_literal_v1`: NFKD decomposition, combining-mark removal, case folding, œ/æ expansion, configured apostrophe/dash unification, soft-hyphen removal with raw-span retention, whitespace collapse and removal of leading/trailing search whitespace. Raw text and exact configured terms remain separately available; accents/apostrophe typography in displayed raw context are not overwritten.

For each topic in **sorted topic-key order**, then each section in source order, then each page fragment, `_literal_topic_matches` scans each normalized term using `str.find` with the next cursor at start+1. Both outer neighbors must be absent or neither alphanumeric (`isalnum()`) nor underscore. Thus `risque` does not match inside `risques` or `dérisque`. It is not linguistic stemming or a whole-word library.

Overlap competition is only among terms **within that one topic and one section/page fragment**. Candidates sort by descending normalized length, then configured term index, then start position. Greedy selection rejects any strict interval overlap with an already selected candidate; adjacent spans may coexist. Selected matches are finally ordered by start and term index. Equal-length overlap uses configured term order, not alphabetic spelling; different topics do not suppress each other.

Output rows are emitted in topic-key, section, page and **configured term** order. A row exists only when that term retains at least one match, with `occurrence_count` counting those retained nonoverlapping matches in that section/page, not across the document. The row stores the first retained occurrence. Searches do not cross page or section boundaries. Declared TOC fragments are skipped when the flag is false; pre-body OTHER text is not automatically excluded.

Scope is purely section-derived: GENERAL → GENERAL_RULE; ZONE_CHAPTER or ARTICLE → ZONE_SPECIFIC_RULE; OTHER → OTHER_TEXT. These labels identify location, not applicability.

`first_match_normalized_start/end` and `first_match_raw_start/end` are zero-based **Python character offsets, half-open [start,end)**, relative to the normalized/raw section-page fragment. They are neither UTF-8 byte offsets nor whole-PDF/page-global offsets. The raw mapping takes the first normalized character's raw start and last matched character's raw end. Normalization expansions and combining characters mean raw and normalized lengths need not agree.

Configured context 80 expands from the first match by at most 80 normalized characters on **each** side, clipped to that fragment. `normalized_context` is the normalized slice; `raw_context` is the exact raw substring spanning it, via the mapping. Eighty does not mean 80 raw bytes/characters or a fixed total snippet length. Evidence validation reruns matching and verifies counts, positions, scope, contexts, section/page ownership, term policy, uniqueness and lineage.

## 10. Public APIs and revalidation

These signatures are copied from the owner, not guessed CLI interfaces:

```python
def load_planning_regulation_structure_config(
    path: str | Path,
) -> PlanningRegulationStructureConfig:
```

```python
def structure_planning_regulation(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
) -> PlanningRegulationStructureResult:
```

```python
def validate_planning_regulation_structure(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
    result: PlanningRegulationStructureResult,
) -> None:
```

```python
def validate_planning_regulation_structure_with_fragments(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
    result: PlanningRegulationStructureResult,
) -> pd.DataFrame:
```

```python
def planning_regulation_section_page_fragments(
    index: PlanningRegulationIndex,
    zones: pd.DataFrame,
    zoning_intersections: pd.DataFrame,
    config: PlanningRegulationStructureConfig | str | Path,
    result: PlanningRegulationStructureResult,
) -> pd.DataFrame:
```

```python
def _config_sha256(config: PlanningRegulationStructureConfig) -> str:
```

```python
def _resolved_config(
    config: PlanningRegulationStructureConfig | str | Path,
) -> PlanningRegulationStructureConfig:
```

The builder resolves config, validates the index/locks/layout, checks/copies factual zoning inputs, builds all components, then calls the public validator, which reconstructs them again. `validate_planning_regulation_structure_with_fragments` resolves config, repeats the input checks, rebuilds expected result/records/fragments, validates the supplied envelope and compares it with the reconstruction before returning fragments. The no-return validator delegates to it. The fragment wrapper also delegates; it is not an unchecked slicing shortcut.

The zoning-input boundary here requires DataFrames and selected identity/lineage/metric columns, unique catalog IDs and parcel/zone pairs, catalog-reference agreement and AREA_OVERLAP/TOUCH_ONLY area consistency. Areas are finite nonnegative real values, booleans rejected; intersection area is copied as float64. Optional parcel/zone upper areas, when supplied, must be finite/nonnegative and obey the shared tolerance `max(1e-6, reference_area * 1e-12)`. This code does not compute/reproject geometry or reread a GPU source.

This structure API reconstructs against **supplied validated in-memory inputs**. It does not accept a GPU document, reopen the original PDF, prove the zone catalog against a physical layer, or reread all source files. Config path input causes a YAML read; model input causes reconstruction only. PDF opening belongs to `index_planning_regulation` when creating an index. Physical GPU zoning revalidation belongs to the separate downstream `validate_normalized_planning_zoning_inputs` call; that boundary delegates extraction/layer revalidation and rebuilds/exact-compares zoning facts. Do not transfer its physical authority to the structure-only API.

Self-validation is distinct from `_compare_expected_result`. The latter compares all 16 scalar lineage/hash fields and canonical records in the three exact column schemas, in row order. It does not compare DataFrame index labels, dtypes, attrs, CRS or geometry metadata. The returned frames are not sealed against later mutation; validation must be used again at a trust boundary.

## 11. Canonical hashes and output schemas

`_config_sha256` hashes the complete `model_dump(mode="json")` under this payload, explicitly rebuilding topics in sorted key order while preserving each term list:

```json
{"domain":"landscout.planning_regulation.structure_config","config":"<complete validated model JSON object, not this placeholder string>"}
```

The displayed placeholder explains payload shape only; it is not a runnable fixture. Canonical serialization recursively handles Mapping keys as strings, tuples/lists/NumPy arrays as arrays, NumPy scalars via `item()`, None/pd.NA and float NaN as null. Strings/integers/finite floats/booleans retain JSON values. Unsupported objects raise; infinities are rejected by `allow_nan=False`. JSON uses `ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")` then UTF-8 and SHA256. No Python repr, memory address or mapping insertion order enters the digest.

The config hash is independent of YAML quoting/comments/formatting and mapping insertion order, but **not** list/term order. Sorted topic keys also govern evidence traversal, so reversing topic-key insertion order preserves outputs and hashes; reversing equally long overlapping terms can change both. No schema/hash migration occurs in R7 because no model, value or algorithm changes.

Distinct payloads in the owner (domain strings are data, not qualified Python functions):

| Identity | Exact payload content and ordering |
|---|---|
| Raw YAML SHA256 / Git OID | SHA256 of file bytes for documentation; Git's blob OID is a different object identity. Neither is computed by the runtime loader. |
| Config SHA256 | Domain above plus complete validated JSON model; all ten root fields included. No hash of an `entries` list exists. |
| Input catalog/relations | `_input_frame_sha256`: `domain`, ordered `columns` array, selected `rows` as records in frame row order. Catalog selects the five identity/lineage columns; relations select eight required fields plus present optional upper-area fields in fixed optional order. Domain literals below. |
| Retained records | `domain`, `section_hash_schema_version=3`, `records` array. Each record contains `record_id, page_number, page_line_number, raw_text`; source order retained. Used for full retained text and each section's subset. |
| Section row | `domain`, `section_hash_schema_version=3`, `section` object containing all SECTION_COLUMNS except `section_content_sha256` itself. Parent/zone/article nulls and the subset-record hash are included. |
| Three output-frame hashes | `domain`, all 12 shared envelope fields listed below, and selected `rows`. No separate output `columns` key is inserted by `_frame_hash`; each role uses its exact predefined columns. |
| Complete structure hash | `domain` plus the same 12 shared fields and `sections_content_sha256, zone_map_content_sha256, topic_evidence_content_sha256`. Does not include its own hash. |
| Section/page fragment hash | Plain SHA256 of `raw_text.encode("utf-8")` only; not canonical JSON, not the whole fragment row or geometry. Fragment rows also carry lineage and the structure-result hash separately. |

The 12 shared frame/result envelope fields are exactly `section_hash_schema_version, document_id, archive_sha256, pdf_sha256, index_content_sha256, structure_profile, structure_config_schema_version, structure_config_sha256, zones_content_sha256, zoning_intersection_hash_columns, zoning_intersections_content_sha256, source_records_sha256`.

The canonical domain literals are:

```text
landscout.planning_regulation.structure_config
landscout.planning_regulation.zones_input
landscout.planning_regulation.intersections_input
landscout.planning_regulation.source_records
landscout.planning_regulation.section
landscout.planning_regulation.sections
landscout.planning_regulation.zone_map
landscout.planning_regulation.topic_evidence
landscout.planning_regulation.structure_result
```

Selected column arrays are copied from owner constants below. Catalog/relations may contain extra columns, but these input hashes omit extra fields, geometry, CRS, index labels, dtype metadata and attrs. No CRS field in this YAML imposes a reprojection. Output hashes likewise include selected row values, not frame metadata. The complete result binds input identities and frame identities, not a fresh physical-source read.

```json
{
  "_ZONE_INPUT_COLUMNS": [
    "planning_zone_id",
    "source_zone_id",
    "zone_label_raw",
    "source_document_id",
    "source_archive_sha256"
  ],
  "_REQUIRED_INTERSECTION_INPUT_COLUMNS": [
    "parcel_id",
    "planning_zone_id",
    "source_zone_id",
    "zone_label_raw",
    "relation_type",
    "intersection_area_m2",
    "source_document_id",
    "source_archive_sha256"
  ],
  "_OPTIONAL_INTERSECTION_INPUT_COLUMNS": [
    "parcel_metric_area_m2",
    "zone_area_m2"
  ],
  "SECTION_COLUMNS": [
    "section_id",
    "parent_section_id",
    "section_type",
    "heading_raw",
    "heading_normalized",
    "zone_chapter_label",
    "article_number_raw",
    "article_title_raw",
    "start_record_id",
    "end_record_id",
    "source_record_count",
    "source_records_sha256",
    "start_page",
    "end_page",
    "page_numbers",
    "raw_text",
    "normalized_text",
    "character_count",
    "section_content_sha256",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_profile"
  ],
  "ZONE_MAPPING_COLUMNS": [
    "source_zone_label_raw",
    "resolved_zone_chapter_label",
    "mapping_status",
    "mapping_method",
    "matched_section_id",
    "zone_polygon_count",
    "candidate_parcel_count",
    "candidate_intersection_count",
    "dominant_candidate_count",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_profile"
  ],
  "TOPIC_EVIDENCE_COLUMNS": [
    "topic",
    "search_term",
    "normalized_search_term",
    "match_policy",
    "section_id",
    "evidence_scope",
    "zone_chapter_label",
    "article_number_raw",
    "page_number",
    "occurrence_count",
    "first_match_normalized_start",
    "first_match_normalized_end",
    "first_match_raw_start",
    "first_match_raw_end",
    "raw_context",
    "normalized_context",
    "document_id",
    "archive_sha256",
    "pdf_sha256",
    "index_content_sha256",
    "structure_profile"
  ]
}
```

`SECTION_HASH_SCHEMA_VERSION=3` governs section/record/frame identities; `STRUCTURE_MANIFEST_SCHEMA_VERSION=4` is declared by this owner but not inserted into `_structure_result_content_sha256`. Configuration schema remains 2. Do not infer a fixed source-version rule from unrelated CNIG or road modules.

## 12. Errors, I/O and business meaning

The loader preserves existing `PlanningRegulationStructureError`; strict YAML errors are translated with their message; other path/read/model exceptions become `Planning structure configuration is invalid` with the cause retained. Direct model validation raises Pydantic ValueError/ValidationError rather than the loader's wrapper.

Public build/validation wrappers preserve structure errors and wrap unexpected exceptions (including upstream index-validation failures) in controlled structure errors. Runtime failures include no retained text/no matched body headings, invalid parent/zone relationship, ambiguous structural matches, unresolved dominant labels, inconsistent record partition, fabricated topic contexts and hash drift. A later error is not proof of which earlier guard a broad test isolated.

Loader I/O is only reading the supplied YAML. It does not hash file bytes, read the PDF/GPKG, access the network, write artifacts or create frames. The explicit private hash call made in R7 observes the loaded model, not a produced structure. Structure construction/validation copies input frames and computes factual text/metric checks and hashes in memory; it does not perform a new spatial overlay.

Topics such as access, setbacks, classified installations or public-interest equipment remain text-search categories. Exact aliases are documentary mappings, not zoning-law equivalences. No term's presence or absence settles ICPE applicability, road access, infrastructure eligibility, a legal right, authorization, prohibition or parcel suitability.

## 13. Test evidence and its limits

Read evidence, **not tests rerun under R7**:

| Test source / exact test or group | What its actual body establishes, and limits |
|---|---|
| [test_structure_planning_regulation.py](../../../../../tests/unit/test_structure_planning_regulation.py), helpers `_index, _config, _zones, _intersections, valid_result, _validate` | Index pages and hashes are self-constructed from synthetic strings with dummy source lineage. Zones/relations are plain DataFrames without physical geometry. No PDF/GPU reread is possible here; no no-op physical monkeypatch is needed because structure's API does not call that boundary. |
| `test_structure_schema_versions_are_explicit` and old/unknown schema tests | Config 2, section hash 3, manifest constant 4; incompatible config/result versions rejected on synthetic inputs. |
| TOC Boolean/page tests and five `test_document_lock_mismatch_is_rejected` parameters | Strict Boolean rejection/acceptance, real indexed page references, blank indexed TOC acceptance and each lock mismatch. The forged TOC page zero can fail model revalidation before the missing-page guard; broad exception is not isolated proof of that later branch. |
| `test_invalid_regex_and_unknown_yaml_field_are_controlled` | Writes one temporary YAML containing **both** an invalid regex and an extra root field; controlled loader failure, not independent isolation of both errors. Duplicate alias-key test separately asserts duplicate-YAML message; cycle test writes A→B→A. |
| Deterministic structure / parent and multi-page / exact-alias tests | Sequential sections, ignored synthetic TOC heading, one U chapter, correct parent and pages (3,4), U EXACT, Ua CONFIG_ALIAS, X/UX UNMAPPED, duplicate Z AMBIGUOUS. No general prefix fallback. |
| `test_alias_chain_resolves_to_final_configured_target` | Model copy with Ua→Urban→U is reconstructed at public boundary and resolves to U. Does not validate every real alias against Muret's original PDF. |
| Header/footer, blank prefix/gap/tail and TOC-block tests | Actual retained line numbering; matching interior text preserved; explicit multi-block/blank TOC sections; flag toggles TOC topic evidence without changing sections/mapping. Synthetic footer regex differs from this YAML's empty footer list. |
| Named-capture, optional-list and ambiguous-heading tests | Missing captures, empty optional lists, exact cross-group duplicate rejection, two zone/article regex matches and cross-category ambiguity. Diagnostic assertions include record/page/line/pattern indexes and avoid raw heading text. Ambiguous continuation candidate and changed grammar validator fail while rebuilding, before comparison of final results. |
| `test_normal_muret_compatible_grammar_remains_deterministic` | Calls synthetic `_config(_index())` twice and compares frames/hash. Despite its name, it does **not** load this checked-in YAML. |
| Topic scope, reversed topic keys, equal-length overlap and `test_token_boundary_and_longest_match_policy` | Four exact section→scope mappings; sorted topic traversal/hash equality despite reversed key insertion; term-order tie behavior in private helper and built synthetic result; accented French singular/plural, nested expressions and token neighbors. They do not establish legal relationships among topics. |
| Source-record/parent/mapping/topic/input mutation and hash tests | Reject mismatched schemas, record partition, unknown pages, source-zone IDs, optional metric changes, counts, contexts and hash fields. The test named coordinated-frame mutation inserts `"f"*64` as the outer digest, not a coherently recomputed hash; the section-row mutation recomputes only the row hash and already violates retained raw-text equality. Parent mutations leave row hashes stale, allowing that earlier check to intercept before parent semantics. |
| `test_coordinated_topic_evidence_and_hash_mutation_is_rebuilt_and_rejected` | Recomputes all exposed frame/result hashes via the private helper after fabricating context. Public validator rejects against retained text; its broad assertion does not specifically isolate the final expected-frame comparison because topic self-validation checks context first. |
| `test_source_complete_validator_rejects_post_build_source_change` | Changes aliases, topics, headings, coherent zone/source-ID references, area or relation and rejects old result. These are supplied in-memory facts/config changes, not on-disk source mutations. `test_inputs_are_not_mutated` compares the original pages/zones/intersections afterward. |
| [test_deep_immutability.py](../../../../../tests/unit/test_deep_immutability.py): recursive loaded-family walk; mapping-operation matrix; nested-input aliases; canonical hash test | Loads this real YAML. Traverses retained nested values; rejects mapping assignment/update/setdefault/pop/deletion/clear/union/backing replacement; mutates detached input alias/term lists after reconstruction and checks model isolation. The fixed config-hash expectation is `13d028fe4b58d30929ff9fdedae90e2cc95983a3296f2f83c2817d0da381107a`. Tuple mutation-operation matrix itself uses scan AOI, not each structure tuple. |
| [test_index_planning_regulation.py](../../../../../tests/unit/test_index_planning_regulation.py): `test_french_literal_normalization, test_raw_context_preserves_source_typography, test_zero_context_preserves_complete_raw_unicode_span` | Direct common-normalizer cases plus search tests with a fake PdfReader over synthetic PDF bytes and a temporary physical zoning source. They cover accents, combining marks, ligatures, apostrophes, soft hyphens and raw substrings. Search is the index helper, not an execution of this exact structure grammar. |
| [test_gpu_planning_end_to_end.py](../../../../../tests/integration/test_gpu_planning_end_to_end.py), all four tests | Builds real synthetic ZIP/GPKG/PDF, runs real indexing/structure/zoning and public BESS validation without mocking physical zoning. Its grammar is a small synthetic profile, continuation limit 0, one factual term; policy is UNKNOWN/LOW with empty evidence/routes. Checks success/preserved parcel fact, physical dataset mutation, config hash mutation and missing article 2. Not the real Muret grammar, 30-term coverage or approval of official PDF content. |

No pytest was executed in this documentary ticket. The one offline real-YAML loader/hash observation and exhaustive value/snapshot comparisons are separately recorded in the receipt. No untested branch is silently called tested, and a test-evidence limitation alone is not promoted to a production defect.

## 14. Change impact and review limits

Changing any grammar, alias, layout, lock, topic or order requires separate authority and review. Consider canonical config hashes and all downstream record/section/mapping/topic/result identities; BESS policy's structure lock may require deliberate revalidation. Raw-only formatting changes affect the documentation byte binding, not necessarily the model hash. R7 changes neither, regenerates no artifact and gives no functional approval.

Review is confined to this YAML and companion. Dependency reading closes no other file/symbol. The [receipt](../../../audit/R7_PLU_STRUCTURE_CONFIGURATION.md) names full versus partial source/test ranges; no original PDF, real GPU layer or legal source was opened. Static links/tables/fences are not visual rendering; rendering remains PENDING.

## 15. Complete exact YAML snapshot

This UTF-8 fence reproduces the Git and current checkout bytes exactly, including final LF. Both have only LF line endings; **there are no mixed CRLF/LF positions in this file**. The separate historic R6 YAML and RESUME-ticket exceptions remain untouched.

```yaml
schema_version: 2
structure_profile: "muret_plu_20240215_v1"

document_lock:
  document_id: "33edb4c9f6943c88d8d92518bff20bec"
  pdf_sha256: "5358ebad6b0cda6de681ba3536e29b8b6291fb701c7d3711f4ee1d6fdb85c6fb"
  pages_content_sha256: "928e7e59c45e27c38e39d3f28f3eb10bd2590886416df57efc4ac8e5d8901ec9"
  index_content_sha256: "6a0009228ca17128c0a8bb329d9c2277a1b6638708a67b913b72ee93063e42cd"
  normalization_profile: "fr_literal_v1"

document_layout:
  body_start_page: 1
  table_of_contents_pages: []
  max_heading_continuation_lines: 2
  include_table_of_contents_in_topic_evidence: false

heading_patterns:
  zone_chapter:
    - '^ZONE\s+(?P<label>[A-Za-z]+(?:\s*0)?)\s*$'
  article:
    - '^ARTICLE\s+(?P<zone>[A-Za-z]+(?:\s*0)?)\s+(?P<number>\d+(?:\.\d+)?)\s*[-–—]\s*(?P<title>.*)$'
  general_section:
    - '^ARTICLE\s+(?P<number>\d+(?:\.\d+)?)\s*[-–—]\s*(?P<title>.*)$'
  continuation:
    - '^[^a-z]*[A-ZÀ-ÖØ-ÞŒ][^a-z]*$'

ignored_patterns:
  page_headers:
    - '^Muret-12ème modification du PLU$'
    - '^\d+$'
  page_footers: []

zone_aliases:
  UAa: "UA"
  UAb: "UA"
  UBa: "UB"
  UBb: "UB"
  UFa: "UF"
  UFc: "UF"
  UFd: "UF"
  AUa: "AU"
  AUfa: "AUf"
  AUfb: "AUf"
  AUfc: "AUf"
  AUfd: "AUf"
  AUfo: "AUf0"
  NL: "N"
  Ne: "N"
  Nh: "N"
  Nr: "N"

topics:
  destination_and_use:
    - "occupation du sol"
    - "utilisation du sol"
    - "destination"
  public_interest_equipment:
    - "équipement public"
    - "équipement d'intérêt collectif"
    - "service public"
    - "intérêt collectif"
  technical_equipment:
    - "ouvrage technique"
    - "installations techniques"
    - "locaux techniques"
  energy:
    - "énergie"
  electricity:
    - "électricité"
    - "électrique"
  transformer:
    - "transformateur"
  classified_installation:
    - "installation classée"
    - "installations classées"
    - "ICPE"
  risk:
    - "risque"
    - "risques"
  nuisance:
    - "nuisance"
    - "nuisances"
  fire_safety:
    - "incendie"
    - "défense contre l'incendie"
  access:
    - "accès"
    - "desserte"
  setbacks:
    - "recul"
    - "distance minimale"
    - "implantation"
  networks:
    - "réseau"
    - "réseaux"

topic_match_policy:
  boundary_mode: "token"
  overlap_resolution: "longest_match"

topic_context_characters: 80
```
