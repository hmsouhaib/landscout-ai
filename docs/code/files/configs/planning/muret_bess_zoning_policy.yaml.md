# `configs/planning/muret_bess_zoning_policy.yaml`

## File identity

- Repository path: `configs/planning/muret_bess_zoning_policy.yaml`
- File type: human-authored YAML policy; no Python symbols owned here.
- Source SHA256: `c736ea8901997f4852fd1f72a3f6f34282452f18dcd9abc0ccbce8255adaad45`
- Source SHA256 basis: `git-content`
- Git blob OID: `a8a1f2d8e5fb04107a3e46de2b67cb140cafa38d`
- Git content: 46,384 UTF-8 bytes; 723 LF, zero CR, final LF.
- Historical checkout: 47,039 bytes; SHA256 `879d50627c063bb10096950d004cf4d4e446ff04ef9a1178b3e3fb28e2ffdae3`; 655 CRLF plus 68 lone LF, final CRLF. Both bases are preserved; the previous companion's checkout hash was not intrinsically wrong.
- Canonical runtime policy hash: `ef1f7cd0f5589e9a07428d25cd2b1a844e7cd49fb6db359951eb6c812c767586`; not either raw-file hash.
- Owner: [interpret_bess_zoning.py](../../../../../src/landscout/stages/interpret_bess_zoning.py), read completely for [R6](../../../audit/R6_BESS_WRITTEN_ZONING_POLICY.md). Independent R6 review: PENDING.

## 1. Purpose

This policy records source-locked written-zoning evidence for Muret: exact excerpts, larger source-rule occurrences, explicit decision routes, chapter precheck statuses and unresolved applicability. It is neither an automatic text classifier nor a legal determination that battery storage belongs to an ICPE, public-interest, technical-equipment or infrastructure category.

The profile is **muret_bess_written_zoning_v6**, **policy schema 5**, with consuming **result hash schema 5**. These are distinct versions. All 13 configured chapters declare CONDITIONAL_REVIEW / LOW; this is not a newly computed parcel distribution or permission to build.

## 2. Position in LandScout architecture

`landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config` reads this YAML. The public interpreter accepts a path or a policy object, plus the regulation index, factual structure and structure config, normalized zoning catalog, parcel/zone relations, parcels and physical GPU planning-document object.

Flow: evidence → role-linked routes → chapter policy → resolved source-zone policy → positive-area parcel/zone interpretations → parcel summary. Unlike the CNIG policy compiler in R5, this module does return parcel statuses. It does not score, rank or reject parcels.

See [planning architecture](../../../PLANNING_PIPELINE.md). R6 reads the implementations but does not reconstruct GPU sources, PDF, structure, intersections or results.

## 3. Imports and dependencies

YAML has no imports. The owner uses Pydantic, the shared [strict YAML reader](../../../../../src/landscout/common/strict_yaml.py), JSON/SHA256, GPU zoning-source validation, regulation-index validation, structure reconstruction with retained fragments, pandas/GeoPandas, NumPy, Shapely, pyproj and the shared overlay tolerance.

This loader has no default-path lookup and no road-policy/scan-profile resolver. It reads precisely `Path(path).read_bytes()`; relative paths resolve from the process working directory.

## 4. Contract taxonomy

There are **7 root fields**, **6 source-lock fields**, **2 required article references**, **13 chapters**, **28 evidence objects**, **13 routes**, **26 reviewed-section references** and **26 route-role references** (13 positive, 10 condition, 3 difficulty). The evidence records use **18 distinct source_rule_id values**. Directions: 13 positive, 10 condition, 3 difficulty, 2 context. Routes: 10 CONDITIONAL_ROUTE and 3 RESTRICTION_EXCEPTION_ROUTE.

The complete ledger has **655 terminal values**, counting an empty list as one terminal: 642 scalars (501 strings, 141 integers) plus 13 explicit empty lists; **zero true nulls**. Nonempty lists expand to indexed members. JSON notation denotes the exact decoded YAML value: `\n` means an internal newline; spaces, accents, punctuation and identifier case remain significant. Section 18 preserves YAML spelling/quoting.

Each ledger contract names an individually explained section-5 field. All values enter the canonical policy hash, including notes, empty arrays, positions and locks. This field-level explanation plus the complete path/value ledger applies to every configured occurrence; fields are not automatically DataFrame columns.

| Exact YAML path | Exact decoded value (JSON) | Field contract / runtime |
|---|---|---|
| `schema_version` | `5` | `BessZoningPolicyConfig.schema_version`; int |
| `policy_profile` | `"muret_bess_written_zoning_v6"` | `BessZoningPolicyConfig.policy_profile`; str |
| `planning_precheck_scope` | `"WRITTEN_ZONING_REGULATION_ONLY"` | `BessZoningPolicyConfig.planning_precheck_scope`; str |
| `review_scope` | `"CONFIGURED_USE_CONTROL_ARTICLES_ONLY"` | `BessZoningPolicyConfig.review_scope`; str |
| `source_lock.document_id` | `"33edb4c9f6943c88d8d92518bff20bec"` | `PolicySourceLock.document_id`; str |
| `source_lock.archive_sha256` | `"9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93"` | `PolicySourceLock.archive_sha256`; str |
| `source_lock.pdf_sha256` | `"5358ebad6b0cda6de681ba3536e29b8b6291fb701c7d3711f4ee1d6fdb85c6fb"` | `PolicySourceLock.pdf_sha256`; str |
| `source_lock.index_content_sha256` | `"6a0009228ca17128c0a8bb329d9c2277a1b6638708a67b913b72ee93063e42cd"` | `PolicySourceLock.index_content_sha256`; str |
| `source_lock.structure_result_content_sha256` | `"16f8a9edfff0d330f69579310da085f804f4641de973d98e0046bff5ea96b03c"` | `PolicySourceLock.structure_result_content_sha256`; str |
| `source_lock.structure_profile` | `"muret_plu_20240215_v1"` | `PolicySourceLock.structure_profile`; str |
| `required_zone_article_numbers[0]` | `"1"` | `BessZoningPolicyConfig.required_zone_article_numbers`; str |
| `required_zone_article_numbers[1]` | `"2"` | `BessZoningPolicyConfig.required_zone_article_numbers`; str |
| `chapters[0].resolved_zone_chapter_label` | `"UA"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[0].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[0].reviewed_section_ids[0]` | `"SECTION-0008"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[0].reviewed_section_ids[1]` | `"SECTION-0009"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[0].review_note` | `"Articles UA 1 and UA 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[0].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[0].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[0].rationale` | `"Article UA 2 states a possible ICPE route and states separate compatibility and local-necessity conditions; whether a BESS qualifies remains unresolved."` | `ChapterPolicy.rationale`; str |
| `chapters[0].missing_information` | `"BESS planning-use and ICPE classification, application of all Article UA 1/2 provisions, prescriptions, servitudes, project effects and design."` | `ChapterPolicy.missing_information`; str |
| `chapters[0].evidence[0].evidence_id` | `"MURET-UA-ICPE-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[0].evidence[0].section_id` | `"SECTION-0009"` | `PolicyEvidence.section_id`; str |
| `chapters[0].evidence[0].page_number` | `8` | `PolicyEvidence.page_number`; int |
| `chapters[0].evidence[0].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[0].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[0].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[0].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[0].evidence[0].section_page_fragment_sha256` | `"2da8d15fad096a694d7b56ecfc1d61d0ba375aac1c254794d63388524cc755f6"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[0].evidence[0].excerpt_start` | `100` | `PolicyEvidence.excerpt_start`; int |
| `chapters[0].evidence[0].excerpt_end` | `183` | `PolicyEvidence.excerpt_end`; int |
| `chapters[0].evidence[0].source_rule_id` | `"MURET-UA-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[0].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition d’être compatibles avec le milieu environnant et nécessaires à la vie  du \nquartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[0].evidence[0].source_rule_sha256` | `"8def59e860d434e482899e9709520d221dd576e41e00f276bbe9c87e5127a8df"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[0].evidence[0].source_rule_start` | `100` | `PolicyEvidence.source_rule_start`; int |
| `chapters[0].evidence[0].source_rule_end` | `301` | `PolicyEvidence.source_rule_end`; int |
| `chapters[0].evidence[0].interpretation_note` | `"This is a literal ICPE route phrase; it does not establish that a BESS is an applicable ICPE use."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[0].evidence[1].evidence_id` | `"MURET-UA-ICPE-CONDITION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[0].evidence[1].section_id` | `"SECTION-0009"` | `PolicyEvidence.section_id`; str |
| `chapters[0].evidence[1].page_number` | `8` | `PolicyEvidence.page_number`; int |
| `chapters[0].evidence[1].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[0].evidence[1].evidence_direction` | `"CONDITION"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[0].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[0].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[0].evidence[1].section_page_fragment_sha256` | `"2da8d15fad096a694d7b56ecfc1d61d0ba375aac1c254794d63388524cc755f6"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[0].evidence[1].excerpt_start` | `210` | `PolicyEvidence.excerpt_start`; int |
| `chapters[0].evidence[1].excerpt_end` | `265` | `PolicyEvidence.excerpt_end`; int |
| `chapters[0].evidence[1].source_rule_id` | `"MURET-UA-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[0].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition d’être compatibles avec le milieu environnant et nécessaires à la vie  du \nquartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[0].evidence[1].source_rule_sha256` | `"8def59e860d434e482899e9709520d221dd576e41e00f276bbe9c87e5127a8df"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[0].evidence[1].source_rule_start` | `100` | `PolicyEvidence.source_rule_start`; int |
| `chapters[0].evidence[1].source_rule_end` | `301` | `PolicyEvidence.source_rule_end`; int |
| `chapters[0].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification attached to the ICPE route."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[0].route_assessments[0].route_id` | `"MURET-UA-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[0].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[0].route_assessments[0].positive_evidence_ids[0]` | `"MURET-UA-ICPE-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[0].route_assessments[0].condition_evidence_ids[0]` | `"MURET-UA-ICPE-CONDITION-01"` | `RouteAssessment.condition_evidence_ids`; str |
| `chapters[0].route_assessments[0].difficulty_evidence_ids` | `[]` | `RouteAssessment.difficulty_evidence_ids`; empty tuple |
| `chapters[0].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `RouteAssessment.applicability_note`; str |
| `chapters[1].resolved_zone_chapter_label` | `"UB"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[1].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[1].reviewed_section_ids[0]` | `"SECTION-0021"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[1].reviewed_section_ids[1]` | `"SECTION-0022"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[1].review_note` | `"Articles UB 1 and UB 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[1].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[1].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[1].rationale` | `"Article UB 2 states a possible ICPE route and separate compatibility and local-necessity conditions; BESS applicability is unresolved."` | `ChapterPolicy.rationale`; str |
| `chapters[1].missing_information` | `"BESS planning-use and ICPE classification, application of all Article UB 1/2 provisions, prescriptions, servitudes, project effects and design."` | `ChapterPolicy.missing_information`; str |
| `chapters[1].evidence[0].evidence_id` | `"MURET-UB-ICPE-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[1].evidence[0].section_id` | `"SECTION-0022"` | `PolicyEvidence.section_id`; str |
| `chapters[1].evidence[0].page_number` | `22` | `PolicyEvidence.page_number`; int |
| `chapters[1].evidence[0].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[1].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[1].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[1].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[1].evidence[0].section_page_fragment_sha256` | `"7c678bbc92c2271fbb02f0c228f51e0b408b862780731b78f301b37731a894f3"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[1].evidence[0].excerpt_start` | `98` | `PolicyEvidence.excerpt_start`; int |
| `chapters[1].evidence[0].excerpt_end` | `181` | `PolicyEvidence.excerpt_end`; int |
| `chapters[1].evidence[0].source_rule_id` | `"MURET-UB-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[1].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[1].evidence[0].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[1].evidence[0].source_rule_start` | `98` | `PolicyEvidence.source_rule_start`; int |
| `chapters[1].evidence[0].source_rule_end` | `307` | `PolicyEvidence.source_rule_end`; int |
| `chapters[1].evidence[0].interpretation_note` | `"This is a literal ICPE route phrase, not a BESS authorization."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[1].evidence[1].evidence_id` | `"MURET-UB-ICPE-CONDITION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[1].evidence[1].section_id` | `"SECTION-0022"` | `PolicyEvidence.section_id`; str |
| `chapters[1].evidence[1].page_number` | `22` | `PolicyEvidence.page_number`; int |
| `chapters[1].evidence[1].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[1].evidence[1].evidence_direction` | `"CONDITION"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[1].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[1].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[1].evidence[1].section_page_fragment_sha256` | `"7c678bbc92c2271fbb02f0c228f51e0b408b862780731b78f301b37731a894f3"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[1].evidence[1].excerpt_start` | `217` | `PolicyEvidence.excerpt_start`; int |
| `chapters[1].evidence[1].excerpt_end` | `272` | `PolicyEvidence.excerpt_end`; int |
| `chapters[1].evidence[1].source_rule_id` | `"MURET-UB-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[1].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[1].evidence[1].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[1].evidence[1].source_rule_start` | `98` | `PolicyEvidence.source_rule_start`; int |
| `chapters[1].evidence[1].source_rule_end` | `307` | `PolicyEvidence.source_rule_end`; int |
| `chapters[1].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[1].route_assessments[0].route_id` | `"MURET-UB-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[1].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[1].route_assessments[0].positive_evidence_ids[0]` | `"MURET-UB-ICPE-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[1].route_assessments[0].condition_evidence_ids[0]` | `"MURET-UB-ICPE-CONDITION-01"` | `RouteAssessment.condition_evidence_ids`; str |
| `chapters[1].route_assessments[0].difficulty_evidence_ids` | `[]` | `RouteAssessment.difficulty_evidence_ids`; empty tuple |
| `chapters[1].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `RouteAssessment.applicability_note`; str |
| `chapters[2].resolved_zone_chapter_label` | `"UC"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[2].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[2].reviewed_section_ids[0]` | `"SECTION-0036"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[2].reviewed_section_ids[1]` | `"SECTION-0037"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[2].review_note` | `"Articles UC 1 and UC 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[2].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[2].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[2].rationale` | `"Article UC 2 states a possible ICPE route subject to explicit compatibility and local-necessity conditions; BESS applicability is unresolved."` | `ChapterPolicy.rationale`; str |
| `chapters[2].missing_information` | `"BESS planning-use and ICPE classification, application of all Article UC 1/2 provisions, prescriptions, servitudes, project effects and design."` | `ChapterPolicy.missing_information`; str |
| `chapters[2].evidence[0].evidence_id` | `"MURET-UC-ICPE-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[2].evidence[0].section_id` | `"SECTION-0037"` | `PolicyEvidence.section_id`; str |
| `chapters[2].evidence[0].page_number` | `36` | `PolicyEvidence.page_number`; int |
| `chapters[2].evidence[0].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[2].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[2].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[2].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[2].evidence[0].section_page_fragment_sha256` | `"f6103c4139a65d12a9b6bf4c5edd37382fa6a2fa642c3a5805aa2898b1121365"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[2].evidence[0].excerpt_start` | `98` | `PolicyEvidence.excerpt_start`; int |
| `chapters[2].evidence[0].excerpt_end` | `181` | `PolicyEvidence.excerpt_end`; int |
| `chapters[2].evidence[0].source_rule_id` | `"MURET-UC-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[2].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[2].evidence[0].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[2].evidence[0].source_rule_start` | `98` | `PolicyEvidence.source_rule_start`; int |
| `chapters[2].evidence[0].source_rule_end` | `307` | `PolicyEvidence.source_rule_end`; int |
| `chapters[2].evidence[0].interpretation_note` | `"This is a literal ICPE route phrase, not a BESS authorization."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[2].evidence[1].evidence_id` | `"MURET-UC-ICPE-CONDITION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[2].evidence[1].section_id` | `"SECTION-0037"` | `PolicyEvidence.section_id`; str |
| `chapters[2].evidence[1].page_number` | `36` | `PolicyEvidence.page_number`; int |
| `chapters[2].evidence[1].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[2].evidence[1].evidence_direction` | `"CONDITION"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[2].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[2].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[2].evidence[1].section_page_fragment_sha256` | `"f6103c4139a65d12a9b6bf4c5edd37382fa6a2fa642c3a5805aa2898b1121365"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[2].evidence[1].excerpt_start` | `217` | `PolicyEvidence.excerpt_start`; int |
| `chapters[2].evidence[1].excerpt_end` | `272` | `PolicyEvidence.excerpt_end`; int |
| `chapters[2].evidence[1].source_rule_id` | `"MURET-UC-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[2].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[2].evidence[1].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[2].evidence[1].source_rule_start` | `98` | `PolicyEvidence.source_rule_start`; int |
| `chapters[2].evidence[1].source_rule_end` | `307` | `PolicyEvidence.source_rule_end`; int |
| `chapters[2].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[2].route_assessments[0].route_id` | `"MURET-UC-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[2].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[2].route_assessments[0].positive_evidence_ids[0]` | `"MURET-UC-ICPE-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[2].route_assessments[0].condition_evidence_ids[0]` | `"MURET-UC-ICPE-CONDITION-01"` | `RouteAssessment.condition_evidence_ids`; str |
| `chapters[2].route_assessments[0].difficulty_evidence_ids` | `[]` | `RouteAssessment.difficulty_evidence_ids`; empty tuple |
| `chapters[2].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `RouteAssessment.applicability_note`; str |
| `chapters[3].resolved_zone_chapter_label` | `"UD"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[3].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[3].reviewed_section_ids[0]` | `"SECTION-0051"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[3].reviewed_section_ids[1]` | `"SECTION-0052"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[3].review_note` | `"Articles UD 1 and UD 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[3].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[3].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[3].rationale` | `"Article UD 2 states a possible ICPE route subject to explicit compatibility and local-necessity conditions; BESS applicability is unresolved."` | `ChapterPolicy.rationale`; str |
| `chapters[3].missing_information` | `"BESS planning-use and ICPE classification, application of all Article UD 1/2 provisions, prescriptions, servitudes, project effects and design."` | `ChapterPolicy.missing_information`; str |
| `chapters[3].evidence[0].evidence_id` | `"MURET-UD-ICPE-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[3].evidence[0].section_id` | `"SECTION-0052"` | `PolicyEvidence.section_id`; str |
| `chapters[3].evidence[0].page_number` | `48` | `PolicyEvidence.page_number`; int |
| `chapters[3].evidence[0].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[3].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[3].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[3].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[3].evidence[0].section_page_fragment_sha256` | `"67701fcf91b57f6d4c00a0c26d95c2904e736bd70c3da1bd49b949f2d60f6e9a"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[3].evidence[0].excerpt_start` | `446` | `PolicyEvidence.excerpt_start`; int |
| `chapters[3].evidence[0].excerpt_end` | `529` | `PolicyEvidence.excerpt_end`; int |
| `chapters[3].evidence[0].source_rule_id` | `"MURET-UD-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[3].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[3].evidence[0].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[3].evidence[0].source_rule_start` | `446` | `PolicyEvidence.source_rule_start`; int |
| `chapters[3].evidence[0].source_rule_end` | `655` | `PolicyEvidence.source_rule_end`; int |
| `chapters[3].evidence[0].interpretation_note` | `"This is a literal ICPE route phrase, not a BESS authorization."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[3].evidence[1].evidence_id` | `"MURET-UD-ICPE-CONDITION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[3].evidence[1].section_id` | `"SECTION-0052"` | `PolicyEvidence.section_id`; str |
| `chapters[3].evidence[1].page_number` | `48` | `PolicyEvidence.page_number`; int |
| `chapters[3].evidence[1].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[3].evidence[1].evidence_direction` | `"CONDITION"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[3].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[3].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[3].evidence[1].section_page_fragment_sha256` | `"67701fcf91b57f6d4c00a0c26d95c2904e736bd70c3da1bd49b949f2d60f6e9a"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[3].evidence[1].excerpt_start` | `565` | `PolicyEvidence.excerpt_start`; int |
| `chapters[3].evidence[1].excerpt_end` | `620` | `PolicyEvidence.excerpt_end`; int |
| `chapters[3].evidence[1].source_rule_id` | `"MURET-UD-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[3].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[3].evidence[1].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[3].evidence[1].source_rule_start` | `446` | `PolicyEvidence.source_rule_start`; int |
| `chapters[3].evidence[1].source_rule_end` | `655` | `PolicyEvidence.source_rule_end`; int |
| `chapters[3].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[3].route_assessments[0].route_id` | `"MURET-UD-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[3].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[3].route_assessments[0].positive_evidence_ids[0]` | `"MURET-UD-ICPE-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[3].route_assessments[0].condition_evidence_ids[0]` | `"MURET-UD-ICPE-CONDITION-01"` | `RouteAssessment.condition_evidence_ids`; str |
| `chapters[3].route_assessments[0].difficulty_evidence_ids` | `[]` | `RouteAssessment.difficulty_evidence_ids`; empty tuple |
| `chapters[3].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `RouteAssessment.applicability_note`; str |
| `chapters[4].resolved_zone_chapter_label` | `"UF"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[4].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[4].reviewed_section_ids[0]` | `"SECTION-0065"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[4].reviewed_section_ids[1]` | `"SECTION-0066"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[4].review_note` | `"Articles UF 1 and UF 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[4].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[4].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[4].rationale` | `"Article UF 2 states a possible ICPE route subject to explicit compatibility and local-necessity conditions; sector and BESS applicability remain unresolved."` | `ChapterPolicy.rationale`; str |
| `chapters[4].missing_information` | `"BESS planning-use, sector and ICPE classification, application of all Article UF 1/2 provisions, prescriptions, servitudes, project effects and design."` | `ChapterPolicy.missing_information`; str |
| `chapters[4].evidence[0].evidence_id` | `"MURET-UF-ICPE-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[4].evidence[0].section_id` | `"SECTION-0066"` | `PolicyEvidence.section_id`; str |
| `chapters[4].evidence[0].page_number` | `60` | `PolicyEvidence.page_number`; int |
| `chapters[4].evidence[0].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[4].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[4].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[4].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[4].evidence[0].section_page_fragment_sha256` | `"4fceabfce9821f94b0c023052a654d1d515c86e81056605b876cfbccf54e84ec"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[4].evidence[0].excerpt_start` | `510` | `PolicyEvidence.excerpt_start`; int |
| `chapters[4].evidence[0].excerpt_end` | `593` | `PolicyEvidence.excerpt_end`; int |
| `chapters[4].evidence[0].source_rule_id` | `"MURET-UF-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[4].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[4].evidence[0].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[4].evidence[0].source_rule_start` | `510` | `PolicyEvidence.source_rule_start`; int |
| `chapters[4].evidence[0].source_rule_end` | `719` | `PolicyEvidence.source_rule_end`; int |
| `chapters[4].evidence[0].interpretation_note` | `"This is a literal ICPE route phrase, not a BESS authorization."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[4].evidence[1].evidence_id` | `"MURET-UF-ICPE-CONDITION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[4].evidence[1].section_id` | `"SECTION-0066"` | `PolicyEvidence.section_id`; str |
| `chapters[4].evidence[1].page_number` | `60` | `PolicyEvidence.page_number`; int |
| `chapters[4].evidence[1].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[4].evidence[1].evidence_direction` | `"CONDITION"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[4].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[4].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[4].evidence[1].section_page_fragment_sha256` | `"4fceabfce9821f94b0c023052a654d1d515c86e81056605b876cfbccf54e84ec"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[4].evidence[1].excerpt_start` | `629` | `PolicyEvidence.excerpt_start`; int |
| `chapters[4].evidence[1].excerpt_end` | `684` | `PolicyEvidence.excerpt_end`; int |
| `chapters[4].evidence[1].source_rule_id` | `"MURET-UF-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[4].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[4].evidence[1].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[4].evidence[1].source_rule_start` | `510` | `PolicyEvidence.source_rule_start`; int |
| `chapters[4].evidence[1].source_rule_end` | `719` | `PolicyEvidence.source_rule_end`; int |
| `chapters[4].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[4].route_assessments[0].route_id` | `"MURET-UF-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[4].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[4].route_assessments[0].positive_evidence_ids[0]` | `"MURET-UF-ICPE-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[4].route_assessments[0].condition_evidence_ids[0]` | `"MURET-UF-ICPE-CONDITION-01"` | `RouteAssessment.condition_evidence_ids`; str |
| `chapters[4].route_assessments[0].difficulty_evidence_ids` | `[]` | `RouteAssessment.difficulty_evidence_ids`; empty tuple |
| `chapters[4].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `RouteAssessment.applicability_note`; str |
| `chapters[5].resolved_zone_chapter_label` | `"UP"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[5].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[5].reviewed_section_ids[0]` | `"SECTION-0080"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[5].reviewed_section_ids[1]` | `"SECTION-0081"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[5].review_note` | `"Articles UP 1 and UP 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[5].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[5].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[5].rationale` | `"Article UP 1 states a general restriction with a public or collective-interest equipment exception; whether a BESS belongs to that excepted category remains unresolved. The separate Article UP 2 ICPE rule is retained only as context because BESS ICPE applicability has not been established."` | `ChapterPolicy.rationale`; str |
| `chapters[5].missing_information` | `"Formal classification as public or collective-interest equipment, BESS ICPE applicability, all Article UP 1/2 provisions, prescriptions, servitudes, project effects and design."` | `ChapterPolicy.missing_information`; str |
| `chapters[5].evidence[0].evidence_id` | `"MURET-UP-PUBLIC-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[5].evidence[0].section_id` | `"SECTION-0080"` | `PolicyEvidence.section_id`; str |
| `chapters[5].evidence[0].page_number` | `71` | `PolicyEvidence.page_number`; int |
| `chapters[5].evidence[0].evidence_kind` | `"PUBLIC_INTEREST_EXCEPTION"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[5].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[5].evidence[0].exact_raw_excerpt` | `"à usage d'équipement public  \nou d'intérêt collectif"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[5].evidence[0].excerpt_sha256` | `"301da057642435982e74e393d12e292b81682d4d7672dec60e40a8e10e84530c"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[5].evidence[0].section_page_fragment_sha256` | `"06f8ea334a2fa8ce62337d6a3c59d24e03f9d8b9d8cc9e936c92e97b771babbb"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[5].evidence[0].excerpt_start` | `125` | `PolicyEvidence.excerpt_start`; int |
| `chapters[5].evidence[0].excerpt_end` | `177` | `PolicyEvidence.excerpt_end`; int |
| `chapters[5].evidence[0].source_rule_id` | `"MURET-UP-ROUTE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[5].evidence[0].source_rule_excerpt` | `"Toutes constructions ou  installations autres que celles à usage d'équipement public  \nou d'intérêt collectif, services annexes et les logements de fonction y afférent."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[5].evidence[0].source_rule_sha256` | `"de2615e25b83708c84e9ff9313060dca708ca0a8bc693777b627951bc2de394c"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[5].evidence[0].source_rule_start` | `68` | `PolicyEvidence.source_rule_start`; int |
| `chapters[5].evidence[0].source_rule_end` | `236` | `PolicyEvidence.source_rule_end`; int |
| `chapters[5].evidence[0].interpretation_note` | `"This is the exact category exception; the policy does not decide that a BESS belongs to it."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[5].evidence[1].evidence_id` | `"MURET-UP-RESTRICTION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[5].evidence[1].section_id` | `"SECTION-0080"` | `PolicyEvidence.section_id`; str |
| `chapters[5].evidence[1].page_number` | `71` | `PolicyEvidence.page_number`; int |
| `chapters[5].evidence[1].evidence_kind` | `"USE_RESTRICTION"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[5].evidence[1].evidence_direction` | `"SUPPORTS_DIFFICULTY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[5].evidence[1].exact_raw_excerpt` | `"Toutes constructions ou  installations autres que celles"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[5].evidence[1].excerpt_sha256` | `"edfbe54799b8a6c0e74d86b0e9596e8c68471f11105783b3e4e93825f8308462"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[5].evidence[1].section_page_fragment_sha256` | `"06f8ea334a2fa8ce62337d6a3c59d24e03f9d8b9d8cc9e936c92e97b771babbb"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[5].evidence[1].excerpt_start` | `68` | `PolicyEvidence.excerpt_start`; int |
| `chapters[5].evidence[1].excerpt_end` | `124` | `PolicyEvidence.excerpt_end`; int |
| `chapters[5].evidence[1].source_rule_id` | `"MURET-UP-ROUTE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[5].evidence[1].source_rule_excerpt` | `"Toutes constructions ou  installations autres que celles à usage d'équipement public  \nou d'intérêt collectif, services annexes et les logements de fonction y afférent."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[5].evidence[1].source_rule_sha256` | `"de2615e25b83708c84e9ff9313060dca708ca0a8bc693777b627951bc2de394c"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[5].evidence[1].source_rule_start` | `68` | `PolicyEvidence.source_rule_start`; int |
| `chapters[5].evidence[1].source_rule_end` | `236` | `PolicyEvidence.source_rule_end`; int |
| `chapters[5].evidence[1].interpretation_note` | `"This is the general restriction surrounding the public or collective-interest exception; it does not decide whether a BESS belongs to the exception."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[5].evidence[2].evidence_id` | `"MURET-UP-ICPE-CONDITION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[5].evidence[2].section_id` | `"SECTION-0081"` | `PolicyEvidence.section_id`; str |
| `chapters[5].evidence[2].page_number` | `71` | `PolicyEvidence.page_number`; int |
| `chapters[5].evidence[2].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[5].evidence[2].evidence_direction` | `"CONTEXT_ONLY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[5].evidence[2].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[5].evidence[2].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[5].evidence[2].section_page_fragment_sha256` | `"7a5fac0b06f32a02a34031e9db62b2ccd59a63099fdb378079ab41c4252aed09"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[5].evidence[2].excerpt_start` | `478` | `PolicyEvidence.excerpt_start`; int |
| `chapters[5].evidence[2].excerpt_end` | `533` | `PolicyEvidence.excerpt_end`; int |
| `chapters[5].evidence[2].source_rule_id` | `"MURET-UP-CONDITION-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[5].evidence[2].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[5].evidence[2].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[5].evidence[2].source_rule_start` | `359` | `PolicyEvidence.source_rule_start`; int |
| `chapters[5].evidence[2].source_rule_end` | `568` | `PolicyEvidence.source_rule_end`; int |
| `chapters[5].evidence[2].interpretation_note` | `"This separate ICPE condition is context only unless a future evidence step establishes that the BESS project is subject to it."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[5].route_assessments[0].route_id` | `"MURET-UP-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[5].route_assessments[0].route_kind` | `"RESTRICTION_EXCEPTION_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[5].route_assessments[0].positive_evidence_ids[0]` | `"MURET-UP-PUBLIC-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[5].route_assessments[0].condition_evidence_ids` | `[]` | `RouteAssessment.condition_evidence_ids`; empty tuple |
| `chapters[5].route_assessments[0].difficulty_evidence_ids[0]` | `"MURET-UP-RESTRICTION-01"` | `RouteAssessment.difficulty_evidence_ids`; str |
| `chapters[5].route_assessments[0].applicability_note` | `"The Article UP 1 restriction and its public or collective-interest exception are assessed as one coherent route; BESS membership remains unresolved. The separate ICPE rule is not used to qualify this route."` | `RouteAssessment.applicability_note`; str |
| `chapters[6].resolved_zone_chapter_label` | `"AU"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[6].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[6].reviewed_section_ids[0]` | `"SECTION-0095"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[6].reviewed_section_ids[1]` | `"SECTION-0096"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[6].review_note` | `"Articles AU 1 and AU 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[6].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[6].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[6].rationale` | `"Infrastructure prerequisites were not treated as a route; Article AU 2 separately states a possible ICPE route with compatibility and necessity conditions."` | `ChapterPolicy.rationale`; str |
| `chapters[6].missing_information` | `"BESS planning-use and ICPE classification, infrastructure and sector conditions, all Article AU 1/2 provisions, prescriptions, servitudes, project effects and design."` | `ChapterPolicy.missing_information`; str |
| `chapters[6].evidence[0].evidence_id` | `"MURET-AU-ICPE-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[6].evidence[0].section_id` | `"SECTION-0096"` | `PolicyEvidence.section_id`; str |
| `chapters[6].evidence[0].page_number` | `81` | `PolicyEvidence.page_number`; int |
| `chapters[6].evidence[0].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[6].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[6].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[6].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[6].evidence[0].section_page_fragment_sha256` | `"545168e51a47f7c8b9519575b6d870ab70e11d1043df847e3b5b8661a890652e"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[6].evidence[0].excerpt_start` | `1474` | `PolicyEvidence.excerpt_start`; int |
| `chapters[6].evidence[0].excerpt_end` | `1557` | `PolicyEvidence.excerpt_end`; int |
| `chapters[6].evidence[0].source_rule_id` | `"MURET-AU-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[6].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[6].evidence[0].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[6].evidence[0].source_rule_start` | `1474` | `PolicyEvidence.source_rule_start`; int |
| `chapters[6].evidence[0].source_rule_end` | `1683` | `PolicyEvidence.source_rule_end`; int |
| `chapters[6].evidence[0].interpretation_note` | `"This is the explicit ICPE route phrase; infrastructure prerequisites alone were not used as positive evidence."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[6].evidence[1].evidence_id` | `"MURET-AU-ICPE-CONDITION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[6].evidence[1].section_id` | `"SECTION-0096"` | `PolicyEvidence.section_id`; str |
| `chapters[6].evidence[1].page_number` | `81` | `PolicyEvidence.page_number`; int |
| `chapters[6].evidence[1].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[6].evidence[1].evidence_direction` | `"CONDITION"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[6].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[6].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[6].evidence[1].section_page_fragment_sha256` | `"545168e51a47f7c8b9519575b6d870ab70e11d1043df847e3b5b8661a890652e"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[6].evidence[1].excerpt_start` | `1593` | `PolicyEvidence.excerpt_start`; int |
| `chapters[6].evidence[1].excerpt_end` | `1648` | `PolicyEvidence.excerpt_end`; int |
| `chapters[6].evidence[1].source_rule_id` | `"MURET-AU-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[6].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[6].evidence[1].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[6].evidence[1].source_rule_start` | `1474` | `PolicyEvidence.source_rule_start`; int |
| `chapters[6].evidence[1].source_rule_end` | `1683` | `PolicyEvidence.source_rule_end`; int |
| `chapters[6].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[6].route_assessments[0].route_id` | `"MURET-AU-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[6].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[6].route_assessments[0].positive_evidence_ids[0]` | `"MURET-AU-ICPE-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[6].route_assessments[0].condition_evidence_ids[0]` | `"MURET-AU-ICPE-CONDITION-01"` | `RouteAssessment.condition_evidence_ids`; str |
| `chapters[6].route_assessments[0].difficulty_evidence_ids` | `[]` | `RouteAssessment.difficulty_evidence_ids`; empty tuple |
| `chapters[6].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `RouteAssessment.applicability_note`; str |
| `chapters[7].resolved_zone_chapter_label` | `"AUp"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[7].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[7].reviewed_section_ids[0]` | `"SECTION-0110"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[7].reviewed_section_ids[1]` | `"SECTION-0111"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[7].review_note` | `"Articles AUp 1 and AUp 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[7].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[7].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[7].rationale` | `"Article AUp 1 states a public or collective-interest equipment exception under Article AUp 2 conditions. Article AUp 2 requires indispensable access, road and network infrastructure before authorization. Its separate ICPE rule is retained only as context because BESS ICPE applicability has not been established."` | `ChapterPolicy.rationale`; str |
| `chapters[7].missing_information` | `"Formal BESS classification as public or collective-interest equipment, satisfaction of the Article AUp 2 infrastructure prerequisite, BESS ICPE applicability, all Article AUp 1/2 provisions, prescriptions, servitudes, project effects and design."` | `ChapterPolicy.missing_information`; str |
| `chapters[7].evidence[0].evidence_id` | `"MURET-AUP-PUBLIC-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[7].evidence[0].section_id` | `"SECTION-0110"` | `PolicyEvidence.section_id`; str |
| `chapters[7].evidence[0].page_number` | `93` | `PolicyEvidence.page_number`; int |
| `chapters[7].evidence[0].evidence_kind` | `"PUBLIC_INTEREST_EXCEPTION"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[7].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[7].evidence[0].exact_raw_excerpt` | `"à usage d'équipement public ou \nd'intérêt collectif"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[7].evidence[0].excerpt_sha256` | `"f7be71b131f97c74c8107bc6f14bf2a980d8c3f769a52eef7a899249108c35a2"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[7].evidence[0].section_page_fragment_sha256` | `"4f5b79666858745347ec811398acd19d2761705b3b3d2a31ffd9f4c54a5c93d5"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[7].evidence[0].excerpt_start` | `125` | `PolicyEvidence.excerpt_start`; int |
| `chapters[7].evidence[0].excerpt_end` | `176` | `PolicyEvidence.excerpt_end`; int |
| `chapters[7].evidence[0].source_rule_id` | `"MURET-AUp-ROUTE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[7].evidence[0].source_rule_excerpt` | `"Toutes constructions ou installations autres que celles à usage d'équipement public ou \nd'intérêt collectif, leurs services annexes et les logements de fonction y afférent  sous \nconditions de l’article AUP-2."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[7].evidence[0].source_rule_sha256` | `"01870b2aa63b15491cbf644501dfa8238a94f980d426d15ee2743cc5796c24c3"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[7].evidence[0].source_rule_start` | `69` | `PolicyEvidence.source_rule_start`; int |
| `chapters[7].evidence[0].source_rule_end` | `278` | `PolicyEvidence.source_rule_end`; int |
| `chapters[7].evidence[0].interpretation_note` | `"This is the exact category exception; BESS membership is unresolved."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[7].evidence[1].evidence_id` | `"MURET-AUP-INFRASTRUCTURE-CONDITION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[7].evidence[1].section_id` | `"SECTION-0111"` | `PolicyEvidence.section_id`; str |
| `chapters[7].evidence[1].page_number` | `93` | `PolicyEvidence.page_number`; int |
| `chapters[7].evidence[1].evidence_kind` | `"ACCESS_OR_NETWORK_CONDITION"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[7].evidence[1].evidence_direction` | `"CONDITION"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[7].evidence[1].exact_raw_excerpt` | `"Les constructions et opérations ne pourront être autorisées qu’après réalisation des  \néquipements d’infrastructure indispensable à leur fonctionnement (accès, voirie et  \nréseaux divers) conformément aux articles AUp3 et AUp4."` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[7].evidence[1].excerpt_sha256` | `"b2be9b1f7e3597802d5ed2c301a7e34bb7a9eecaeab55898e55306719b1b315b"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[7].evidence[1].section_page_fragment_sha256` | `"57540d28148aefc320fcc8baa9a92df7e382d72299da6e804a3ebfaf52408b44"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[7].evidence[1].excerpt_start` | `98` | `PolicyEvidence.excerpt_start`; int |
| `chapters[7].evidence[1].excerpt_end` | `325` | `PolicyEvidence.excerpt_end`; int |
| `chapters[7].evidence[1].source_rule_id` | `"MURET-AUp-INFRASTRUCTURE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[7].evidence[1].source_rule_excerpt` | `"Les constructions et opérations ne pourront être autorisées qu’après réalisation des  \néquipements d’infrastructure indispensable à leur fonctionnement (accès, voirie et  \nréseaux divers) conformément aux articles AUp3 et AUp4."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[7].evidence[1].source_rule_sha256` | `"b2be9b1f7e3597802d5ed2c301a7e34bb7a9eecaeab55898e55306719b1b315b"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[7].evidence[1].source_rule_start` | `98` | `PolicyEvidence.source_rule_start`; int |
| `chapters[7].evidence[1].source_rule_end` | `325` | `PolicyEvidence.source_rule_end`; int |
| `chapters[7].evidence[1].interpretation_note` | `"This is the general Article AUp 2 infrastructure prerequisite expressly referenced by Article AUp 1; the policy does not decide that it is satisfied."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[7].evidence[2].evidence_id` | `"MURET-AUP-ICPE-CONDITION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[7].evidence[2].section_id` | `"SECTION-0111"` | `PolicyEvidence.section_id`; str |
| `chapters[7].evidence[2].page_number` | `93` | `PolicyEvidence.page_number`; int |
| `chapters[7].evidence[2].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[7].evidence[2].evidence_direction` | `"CONTEXT_ONLY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[7].evidence[2].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[7].evidence[2].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[7].evidence[2].section_page_fragment_sha256` | `"57540d28148aefc320fcc8baa9a92df7e382d72299da6e804a3ebfaf52408b44"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[7].evidence[2].excerpt_start` | `713` | `PolicyEvidence.excerpt_start`; int |
| `chapters[7].evidence[2].excerpt_end` | `768` | `PolicyEvidence.excerpt_end`; int |
| `chapters[7].evidence[2].source_rule_id` | `"MURET-AUp-CONDITION-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[7].evidence[2].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[7].evidence[2].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[7].evidence[2].source_rule_start` | `594` | `PolicyEvidence.source_rule_start`; int |
| `chapters[7].evidence[2].source_rule_end` | `803` | `PolicyEvidence.source_rule_end`; int |
| `chapters[7].evidence[2].interpretation_note` | `"This separate ICPE condition is context only unless a future evidence step establishes that the BESS project is subject to it."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[7].route_assessments[0].route_id` | `"MURET-AUp-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[7].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[7].route_assessments[0].positive_evidence_ids[0]` | `"MURET-AUP-PUBLIC-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[7].route_assessments[0].condition_evidence_ids[0]` | `"MURET-AUP-INFRASTRUCTURE-CONDITION-01"` | `RouteAssessment.condition_evidence_ids`; str |
| `chapters[7].route_assessments[0].difficulty_evidence_ids` | `[]` | `RouteAssessment.difficulty_evidence_ids`; empty tuple |
| `chapters[7].route_assessments[0].applicability_note` | `"The Article AUp 1 public or collective-interest route is assessed with the general Article AUp 2 infrastructure prerequisite. BESS category membership and satisfaction remain unresolved; the separate ICPE rule does not qualify this route unless independently applicable."` | `RouteAssessment.applicability_note`; str |
| `chapters[8].resolved_zone_chapter_label` | `"AUf"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[8].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[8].reviewed_section_ids[0]` | `"SECTION-0125"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[8].reviewed_section_ids[1]` | `"SECTION-0126"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[8].review_note` | `"Articles AUf 1 and AUf 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[8].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[8].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[8].rationale` | `"Infrastructure prerequisites were not treated as route evidence; Article AUf 2 separately states a possible ICPE route with compatibility and necessity conditions."` | `ChapterPolicy.rationale`; str |
| `chapters[8].missing_information` | `"BESS planning-use, sector and ICPE classification, infrastructure and orientation requirements, all Article AUf 1/2 provisions, prescriptions and project design."` | `ChapterPolicy.missing_information`; str |
| `chapters[8].evidence[0].evidence_id` | `"MURET-AUF-ICPE-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[8].evidence[0].section_id` | `"SECTION-0126"` | `PolicyEvidence.section_id`; str |
| `chapters[8].evidence[0].page_number` | `102` | `PolicyEvidence.page_number`; int |
| `chapters[8].evidence[0].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[8].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[8].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[8].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[8].evidence[0].section_page_fragment_sha256` | `"ef0d2718332307afa871176c64cb8627900702dbd583819fb765adb2d1902769"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[8].evidence[0].excerpt_start` | `1435` | `PolicyEvidence.excerpt_start`; int |
| `chapters[8].evidence[0].excerpt_end` | `1518` | `PolicyEvidence.excerpt_end`; int |
| `chapters[8].evidence[0].source_rule_id` | `"MURET-AUf-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[8].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[8].evidence[0].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[8].evidence[0].source_rule_start` | `1435` | `PolicyEvidence.source_rule_start`; int |
| `chapters[8].evidence[0].source_rule_end` | `1644` | `PolicyEvidence.source_rule_end`; int |
| `chapters[8].evidence[0].interpretation_note` | `"This is the explicit ICPE route phrase; infrastructure prerequisites alone were not used as positive evidence."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[8].evidence[1].evidence_id` | `"MURET-AUF-ICPE-CONDITION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[8].evidence[1].section_id` | `"SECTION-0126"` | `PolicyEvidence.section_id`; str |
| `chapters[8].evidence[1].page_number` | `102` | `PolicyEvidence.page_number`; int |
| `chapters[8].evidence[1].evidence_kind` | `"ICPE_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[8].evidence[1].evidence_direction` | `"CONDITION"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[8].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[8].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[8].evidence[1].section_page_fragment_sha256` | `"ef0d2718332307afa871176c64cb8627900702dbd583819fb765adb2d1902769"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[8].evidence[1].excerpt_start` | `1554` | `PolicyEvidence.excerpt_start`; int |
| `chapters[8].evidence[1].excerpt_end` | `1609` | `PolicyEvidence.excerpt_end`; int |
| `chapters[8].evidence[1].source_rule_id` | `"MURET-AUf-ICPE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[8].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[8].evidence[1].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[8].evidence[1].source_rule_start` | `1435` | `PolicyEvidence.source_rule_start`; int |
| `chapters[8].evidence[1].source_rule_end` | `1644` | `PolicyEvidence.source_rule_end`; int |
| `chapters[8].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[8].route_assessments[0].route_id` | `"MURET-AUf-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[8].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[8].route_assessments[0].positive_evidence_ids[0]` | `"MURET-AUF-ICPE-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[8].route_assessments[0].condition_evidence_ids[0]` | `"MURET-AUF-ICPE-CONDITION-01"` | `RouteAssessment.condition_evidence_ids`; str |
| `chapters[8].route_assessments[0].difficulty_evidence_ids` | `[]` | `RouteAssessment.difficulty_evidence_ids`; empty tuple |
| `chapters[8].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `RouteAssessment.applicability_note`; str |
| `chapters[9].resolved_zone_chapter_label` | `"AU0"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[9].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[9].reviewed_section_ids[0]` | `"SECTION-0140"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[9].reviewed_section_ids[1]` | `"SECTION-0141"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[9].review_note` | `"Articles AU0 1 and AU0 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[9].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[9].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[9].rationale` | `"Article AU0 1 identifies an exception for collective-interest networks and public infrastructure, while Article AU0 2 states a separate PLU-modification prerequisite for new construction or operations."` | `ChapterPolicy.rationale`; str |
| `chapters[9].missing_information` | `"Formal BESS classification within the stated infrastructure exception, applicability of the modification prerequisite, all Article AU0 1/2 provisions, prescriptions and project design."` | `ChapterPolicy.missing_information`; str |
| `chapters[9].evidence[0].evidence_id` | `"MURET-AU0-INFRA-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[9].evidence[0].section_id` | `"SECTION-0140"` | `PolicyEvidence.section_id`; str |
| `chapters[9].evidence[0].page_number` | `114` | `PolicyEvidence.page_number`; int |
| `chapters[9].evidence[0].evidence_kind` | `"TECHNICAL_EQUIPMENT_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[9].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[9].evidence[0].exact_raw_excerpt` | `"installations nécessaires aux réseaux \nd’intérêt collectif, aux ouvrages publics d’infrastructures"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[9].evidence[0].excerpt_sha256` | `"886aaceafb2a40e73e3ebe145b3a58b6a22b239a8ce5fcc3740cb99d7d6298a0"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[9].evidence[0].section_page_fragment_sha256` | `"2f4cf931c76c5a5a29aa69d67b7986b092aff39ea13e4b302513177e5fef6619"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[9].evidence[0].excerpt_start` | `119` | `PolicyEvidence.excerpt_start`; int |
| `chapters[9].evidence[0].excerpt_end` | `217` | `PolicyEvidence.excerpt_end`; int |
| `chapters[9].evidence[0].source_rule_id` | `"MURET-AU0-ROUTE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[9].evidence[0].source_rule_excerpt` | `"Sont interdites toutes les constructions autres que les installations nécessaires aux réseaux \nd’intérêt collectif, aux ouvrages publics d’infrastructures, et les extensions définies à \nl’article AU0 – 2."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[9].evidence[0].source_rule_sha256` | `"fa20142522483be8183df1a43e069fcb350b1de83347bdfdd733f7871bcf207d"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[9].evidence[0].source_rule_start` | `63` | `PolicyEvidence.source_rule_start`; int |
| `chapters[9].evidence[0].source_rule_end` | `267` | `PolicyEvidence.source_rule_end`; int |
| `chapters[9].evidence[0].interpretation_note` | `"This is an exact infrastructure exception; BESS qualification is unresolved."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[9].evidence[1].evidence_id` | `"MURET-AU0-MODIFICATION-CONDITION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[9].evidence[1].section_id` | `"SECTION-0141"` | `PolicyEvidence.section_id`; str |
| `chapters[9].evidence[1].page_number` | `114` | `PolicyEvidence.page_number`; int |
| `chapters[9].evidence[1].evidence_kind` | `"OTHER_RELEVANT_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[9].evidence[1].evidence_direction` | `"CONDITION"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[9].evidence[1].exact_raw_excerpt` | `"Les constructions et opérations nouvelles ne pourront être autorisées qu’après la \nmise en œuvre d’une procédure de modification du PLU"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[9].evidence[1].excerpt_sha256` | `"01594e632fb064a7e4dd408e68c156b66711abe6ae2a0e470c779e94b91f3a48"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[9].evidence[1].section_page_fragment_sha256` | `"a239cf9eff040ca9c9ab608cf040e3c739d5111c877aa68ad1773d3adadf24a5"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[9].evidence[1].excerpt_start` | `99` | `PolicyEvidence.excerpt_start`; int |
| `chapters[9].evidence[1].excerpt_end` | `234` | `PolicyEvidence.excerpt_end`; int |
| `chapters[9].evidence[1].source_rule_id` | `"MURET-AU0-CONDITION-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[9].evidence[1].source_rule_excerpt` | `"Les constructions et opérations nouvelles ne pourront être autorisées qu’après la \nmise en œuvre d’une procédure de modification du PLU."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[9].evidence[1].source_rule_sha256` | `"2d9633774f414a8ad2f8e42bfcbb2507b677906ca6aca480f0239cec007942e3"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[9].evidence[1].source_rule_start` | `99` | `PolicyEvidence.source_rule_start`; int |
| `chapters[9].evidence[1].source_rule_end` | `235` | `PolicyEvidence.source_rule_end`; int |
| `chapters[9].evidence[1].interpretation_note` | `"This prerequisite is a condition only and is not treated as evidence that a BESS route exists."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[9].route_assessments[0].route_id` | `"MURET-AU0-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[9].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[9].route_assessments[0].positive_evidence_ids[0]` | `"MURET-AU0-INFRA-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[9].route_assessments[0].condition_evidence_ids[0]` | `"MURET-AU0-MODIFICATION-CONDITION-01"` | `RouteAssessment.condition_evidence_ids`; str |
| `chapters[9].route_assessments[0].difficulty_evidence_ids` | `[]` | `RouteAssessment.difficulty_evidence_ids`; empty tuple |
| `chapters[9].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `RouteAssessment.applicability_note`; str |
| `chapters[10].resolved_zone_chapter_label` | `"AUf0"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[10].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[10].reviewed_section_ids[0]` | `"SECTION-0155"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[10].reviewed_section_ids[1]` | `"SECTION-0156"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[10].review_note` | `"Articles AUf0 1 and AUf0 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[10].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[10].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[10].rationale` | `"Article AUf0 1 identifies an exception for collective-interest networks and public infrastructure, while Article AUf0 2 states a separate PLU-modification prerequisite."` | `ChapterPolicy.rationale`; str |
| `chapters[10].missing_information` | `"Formal BESS classification within the infrastructure exception, applicability of the modification prerequisite, all Article AUf0 1/2 provisions, prescriptions and project design."` | `ChapterPolicy.missing_information`; str |
| `chapters[10].evidence[0].evidence_id` | `"MURET-AUF0-INFRA-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[10].evidence[0].section_id` | `"SECTION-0155"` | `PolicyEvidence.section_id`; str |
| `chapters[10].evidence[0].page_number` | `120` | `PolicyEvidence.page_number`; int |
| `chapters[10].evidence[0].evidence_kind` | `"TECHNICAL_EQUIPMENT_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[10].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[10].evidence[0].exact_raw_excerpt` | `"installations nécessaires aux réseaux \nd’intérêt collectif, aux ouvrages publics d’infrastructures"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[10].evidence[0].excerpt_sha256` | `"886aaceafb2a40e73e3ebe145b3a58b6a22b239a8ce5fcc3740cb99d7d6298a0"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[10].evidence[0].section_page_fragment_sha256` | `"a23b2c0f7e48711758012d3b176967139a3b87d230c3dea312987693de86c369"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[10].evidence[0].excerpt_start` | `120` | `PolicyEvidence.excerpt_start`; int |
| `chapters[10].evidence[0].excerpt_end` | `218` | `PolicyEvidence.excerpt_end`; int |
| `chapters[10].evidence[0].source_rule_id` | `"MURET-AUf0-ROUTE-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[10].evidence[0].source_rule_excerpt` | `"Sont interdites toutes les constructions autres que les installations nécessaires aux réseaux \nd’intérêt collectif, aux ouvrages publics d’infrastructures, et les extensions définies à \nl’article AUf0 – 2."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[10].evidence[0].source_rule_sha256` | `"5f4af2e2ece550ccc1bcb39eb7436f7dba04f5f21c0346b7d780bf350b77183c"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[10].evidence[0].source_rule_start` | `64` | `PolicyEvidence.source_rule_start`; int |
| `chapters[10].evidence[0].source_rule_end` | `269` | `PolicyEvidence.source_rule_end`; int |
| `chapters[10].evidence[0].interpretation_note` | `"This is an exact infrastructure exception; BESS qualification is unresolved."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[10].evidence[1].evidence_id` | `"MURET-AUF0-MODIFICATION-CONDITION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[10].evidence[1].section_id` | `"SECTION-0156"` | `PolicyEvidence.section_id`; str |
| `chapters[10].evidence[1].page_number` | `120` | `PolicyEvidence.page_number`; int |
| `chapters[10].evidence[1].evidence_kind` | `"OTHER_RELEVANT_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[10].evidence[1].evidence_direction` | `"CONDITION"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[10].evidence[1].exact_raw_excerpt` | `"Les constructions et opérations nouvelles ne pourront être autorisées qu’après la \nmise en œuvre d’une procédure de modification du PLU"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[10].evidence[1].excerpt_sha256` | `"01594e632fb064a7e4dd408e68c156b66711abe6ae2a0e470c779e94b91f3a48"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[10].evidence[1].section_page_fragment_sha256` | `"15040ad2f1b4a5fd1c44bdfead25d12cf4ccdd53a5f28736e4c383ae19a6cac9"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[10].evidence[1].excerpt_start` | `100` | `PolicyEvidence.excerpt_start`; int |
| `chapters[10].evidence[1].excerpt_end` | `235` | `PolicyEvidence.excerpt_end`; int |
| `chapters[10].evidence[1].source_rule_id` | `"MURET-AUf0-CONDITION-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[10].evidence[1].source_rule_excerpt` | `"Les constructions et opérations nouvelles ne pourront être autorisées qu’après la \nmise en œuvre d’une procédure de modification du PLU."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[10].evidence[1].source_rule_sha256` | `"2d9633774f414a8ad2f8e42bfcbb2507b677906ca6aca480f0239cec007942e3"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[10].evidence[1].source_rule_start` | `100` | `PolicyEvidence.source_rule_start`; int |
| `chapters[10].evidence[1].source_rule_end` | `236` | `PolicyEvidence.source_rule_end`; int |
| `chapters[10].evidence[1].interpretation_note` | `"This prerequisite is a condition only and is not treated as route evidence."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[10].route_assessments[0].route_id` | `"MURET-AUf0-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[10].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[10].route_assessments[0].positive_evidence_ids[0]` | `"MURET-AUF0-INFRA-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[10].route_assessments[0].condition_evidence_ids[0]` | `"MURET-AUF0-MODIFICATION-CONDITION-01"` | `RouteAssessment.condition_evidence_ids`; str |
| `chapters[10].route_assessments[0].difficulty_evidence_ids` | `[]` | `RouteAssessment.difficulty_evidence_ids`; empty tuple |
| `chapters[10].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `RouteAssessment.applicability_note`; str |
| `chapters[11].resolved_zone_chapter_label` | `"A"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[11].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[11].reviewed_section_ids[0]` | `"SECTION-0170"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[11].reviewed_section_ids[1]` | `"SECTION-0171"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[11].review_note` | `"Articles A 1 and A 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[11].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[11].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[11].rationale` | `"Article A 1 contains broad restrictive language and a separate exception for necessary technical and infrastructure works. The policy records the conflict without deciding BESS qualification."` | `ChapterPolicy.rationale`; str |
| `chapters[11].missing_information` | `"Formal necessity and BESS infrastructure classification, agricultural-zone effects, all Article A 1/2 provisions, prescriptions, servitudes and project design."` | `ChapterPolicy.missing_information`; str |
| `chapters[11].evidence[0].evidence_id` | `"MURET-A-RESTRICTION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[11].evidence[0].section_id` | `"SECTION-0170"` | `PolicyEvidence.section_id`; str |
| `chapters[11].evidence[0].page_number` | `125` | `PolicyEvidence.page_number`; int |
| `chapters[11].evidence[0].evidence_kind` | `"USE_RESTRICTION"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[11].evidence[0].evidence_direction` | `"SUPPORTS_DIFFICULTY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[11].evidence[0].exact_raw_excerpt` | `"Sont interdites toutes les occupations et utilisations du sol autres que celles"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[11].evidence[0].excerpt_sha256` | `"f18eba9dd56f410853fb685d30b6fcc78ee95359c6577387b78a29c3261b3c61"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[11].evidence[0].section_page_fragment_sha256` | `"51342e0ae335504d0f750e0138a63c2ffe928e11e564872122bec65edb4a8e13"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[11].evidence[0].excerpt_start` | `67` | `PolicyEvidence.excerpt_start`; int |
| `chapters[11].evidence[0].excerpt_end` | `146` | `PolicyEvidence.excerpt_end`; int |
| `chapters[11].evidence[0].source_rule_id` | `"MURET-A-RESTRICTION-EXCEPTION-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[11].evidence[0].source_rule_excerpt` | `"Sont interdites toutes les occupations et utilisations du sol autres que celles : \n- nécessaires à l’exploitation agricole, qu’il s’agisse des constructions et extensions \nà usage d’habitation ou des constructions et installations à usage agricole, \n- nécessaires au bon fonctionnement des systèmes de gestion des eaux, \n- nécessaires aux ouvrages techniques et d’infrastructures, \n- mentionnées à l’article A2"` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[11].evidence[0].source_rule_sha256` | `"4a0a23edf39f707575293cb759d13f6bf2081db5df58ff1e9bed08c98775b1b9"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[11].evidence[0].source_rule_start` | `67` | `PolicyEvidence.source_rule_start`; int |
| `chapters[11].evidence[0].source_rule_end` | `477` | `PolicyEvidence.source_rule_end`; int |
| `chapters[11].evidence[0].interpretation_note` | `"This is the broad restriction phrase, separate from the exception."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[11].evidence[1].evidence_id` | `"MURET-A-INFRA-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[11].evidence[1].section_id` | `"SECTION-0170"` | `PolicyEvidence.section_id`; str |
| `chapters[11].evidence[1].page_number` | `125` | `PolicyEvidence.page_number`; int |
| `chapters[11].evidence[1].evidence_kind` | `"TECHNICAL_EQUIPMENT_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[11].evidence[1].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[11].evidence[1].exact_raw_excerpt` | `"nécessaires aux ouvrages techniques et d’infrastructures"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[11].evidence[1].excerpt_sha256` | `"7eee9f7e595784b2d6a4b605a4f0b5703a0446acb77b7420c709b5516e30e0a2"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[11].evidence[1].section_page_fragment_sha256` | `"51342e0ae335504d0f750e0138a63c2ffe928e11e564872122bec65edb4a8e13"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[11].evidence[1].excerpt_start` | `390` | `PolicyEvidence.excerpt_start`; int |
| `chapters[11].evidence[1].excerpt_end` | `446` | `PolicyEvidence.excerpt_end`; int |
| `chapters[11].evidence[1].source_rule_id` | `"MURET-A-RESTRICTION-EXCEPTION-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[11].evidence[1].source_rule_excerpt` | `"Sont interdites toutes les occupations et utilisations du sol autres que celles : \n- nécessaires à l’exploitation agricole, qu’il s’agisse des constructions et extensions \nà usage d’habitation ou des constructions et installations à usage agricole, \n- nécessaires au bon fonctionnement des systèmes de gestion des eaux, \n- nécessaires aux ouvrages techniques et d’infrastructures, \n- mentionnées à l’article A2"` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[11].evidence[1].source_rule_sha256` | `"4a0a23edf39f707575293cb759d13f6bf2081db5df58ff1e9bed08c98775b1b9"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[11].evidence[1].source_rule_start` | `67` | `PolicyEvidence.source_rule_start`; int |
| `chapters[11].evidence[1].source_rule_end` | `477` | `PolicyEvidence.source_rule_end`; int |
| `chapters[11].evidence[1].interpretation_note` | `"This is the separate technical-infrastructure exception; BESS necessity and classification are unresolved."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[11].route_assessments[0].route_id` | `"MURET-A-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[11].route_assessments[0].route_kind` | `"RESTRICTION_EXCEPTION_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[11].route_assessments[0].positive_evidence_ids[0]` | `"MURET-A-INFRA-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[11].route_assessments[0].condition_evidence_ids` | `[]` | `RouteAssessment.condition_evidence_ids`; empty tuple |
| `chapters[11].route_assessments[0].difficulty_evidence_ids[0]` | `"MURET-A-RESTRICTION-01"` | `RouteAssessment.difficulty_evidence_ids`; str |
| `chapters[11].route_assessments[0].applicability_note` | `"The restriction and its listed exception are assessed as one coherent route; BESS applicability remains unresolved."` | `RouteAssessment.applicability_note`; str |
| `chapters[12].resolved_zone_chapter_label` | `"N"` | `ChapterPolicy.resolved_zone_chapter_label`; str |
| `chapters[12].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `ChapterPolicy.review_completeness`; str |
| `chapters[12].reviewed_section_ids[0]` | `"SECTION-0184"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[12].reviewed_section_ids[1]` | `"SECTION-0185"` | `ChapterPolicy.reviewed_section_ids`; str |
| `chapters[12].review_note` | `"Articles N 1 and N 2 were reviewed in full for written use controls."` | `ChapterPolicy.review_note`; str |
| `chapters[12].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `ChapterPolicy.zoning_precheck_status`; str |
| `chapters[12].zoning_precheck_confidence` | `"LOW"` | `ChapterPolicy.zoning_precheck_confidence`; str |
| `chapters[12].rationale` | `"Article N 1 contains a broad restriction and a separate exception for necessary technical and infrastructure equipment. The policy records the conflict without deciding BESS qualification."` | `ChapterPolicy.rationale`; str |
| `chapters[12].missing_information` | `"Formal necessity and BESS infrastructure classification, natural-zone effects, all Article N 1/2 provisions, prescriptions, servitudes and project design."` | `ChapterPolicy.missing_information`; str |
| `chapters[12].evidence[0].evidence_id` | `"MURET-N-RESTRICTION-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[12].evidence[0].section_id` | `"SECTION-0184"` | `PolicyEvidence.section_id`; str |
| `chapters[12].evidence[0].page_number` | `135` | `PolicyEvidence.page_number`; int |
| `chapters[12].evidence[0].evidence_kind` | `"USE_RESTRICTION"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[12].evidence[0].evidence_direction` | `"SUPPORTS_DIFFICULTY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[12].evidence[0].exact_raw_excerpt` | `"Sont interdites, toutes les occupations et utilisations du sol, à l’exception"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[12].evidence[0].excerpt_sha256` | `"4781673bc1d5c704acd3be46c706805f6eaebacd4fc4b2296877af8bce6688ef"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[12].evidence[0].section_page_fragment_sha256` | `"0cac3a1aeb56859670b715c17e1c166959147a0f90a19a12f87e0025b263e195"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[12].evidence[0].excerpt_start` | `69` | `PolicyEvidence.excerpt_start`; int |
| `chapters[12].evidence[0].excerpt_end` | `146` | `PolicyEvidence.excerpt_end`; int |
| `chapters[12].evidence[0].source_rule_id` | `"MURET-N-RESTRICTION-EXCEPTION-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[12].evidence[0].source_rule_excerpt` | `"Sont interdites, toutes les occupations et utilisations du sol, à l’exception : \n \n- des occupations et utilisations du sol soumises à des conditions particulières et \nrépertoriées à l’article N 2, \n- des équipements nécessaires aux ouvrages techniques et d’infrastructure, \n- des aménagements liés aux ouvrages techniques nécessaires au fonctionnement des \nservices publics, \n- des équipements nécessaires au bon fonctionnement des systèmes de gestion des \neaux, \n- en secteur NL : \n- les constructions, installations et utilisations du sol destinées à l’accueil des \nactivités de loisirs et d’équipements publics sportifs ou socio-culturels, \n- les terrains de camping et de caravaning, excepté dans le secteur inondable \nrepéré au plan de zonage."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[12].evidence[0].source_rule_sha256` | `"c434670531b43bbc23dd24c1fa01bba1eedaee0ba9e241b9f432255c74db30d2"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[12].evidence[0].source_rule_start` | `69` | `PolicyEvidence.source_rule_start`; int |
| `chapters[12].evidence[0].source_rule_end` | `818` | `PolicyEvidence.source_rule_end`; int |
| `chapters[12].evidence[0].interpretation_note` | `"This is the broad restriction phrase, separate from its listed exceptions."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[12].evidence[1].evidence_id` | `"MURET-N-INFRA-ROUTE-01"` | `PolicyEvidence.evidence_id`; str |
| `chapters[12].evidence[1].section_id` | `"SECTION-0184"` | `PolicyEvidence.section_id`; str |
| `chapters[12].evidence[1].page_number` | `135` | `PolicyEvidence.page_number`; int |
| `chapters[12].evidence[1].evidence_kind` | `"TECHNICAL_EQUIPMENT_RULE"` | `PolicyEvidence.evidence_kind`; str |
| `chapters[12].evidence[1].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `PolicyEvidence.evidence_direction`; str |
| `chapters[12].evidence[1].exact_raw_excerpt` | `"des équipements nécessaires aux ouvrages techniques et d’infrastructure"` | `PolicyEvidence.exact_raw_excerpt`; str |
| `chapters[12].evidence[1].excerpt_sha256` | `"b28cb339936e8598faee5c5bba6f1be5f52e40b1ce6f33fe854ae1daff54d867"` | `PolicyEvidence.excerpt_sha256`; str |
| `chapters[12].evidence[1].section_page_fragment_sha256` | `"0cac3a1aeb56859670b715c17e1c166959147a0f90a19a12f87e0025b263e195"` | `PolicyEvidence.section_page_fragment_sha256`; str |
| `chapters[12].evidence[1].excerpt_start` | `270` | `PolicyEvidence.excerpt_start`; int |
| `chapters[12].evidence[1].excerpt_end` | `341` | `PolicyEvidence.excerpt_end`; int |
| `chapters[12].evidence[1].source_rule_id` | `"MURET-N-RESTRICTION-EXCEPTION-RULE-01"` | `PolicyEvidence.source_rule_id`; str |
| `chapters[12].evidence[1].source_rule_excerpt` | `"Sont interdites, toutes les occupations et utilisations du sol, à l’exception : \n \n- des occupations et utilisations du sol soumises à des conditions particulières et \nrépertoriées à l’article N 2, \n- des équipements nécessaires aux ouvrages techniques et d’infrastructure, \n- des aménagements liés aux ouvrages techniques nécessaires au fonctionnement des \nservices publics, \n- des équipements nécessaires au bon fonctionnement des systèmes de gestion des \neaux, \n- en secteur NL : \n- les constructions, installations et utilisations du sol destinées à l’accueil des \nactivités de loisirs et d’équipements publics sportifs ou socio-culturels, \n- les terrains de camping et de caravaning, excepté dans le secteur inondable \nrepéré au plan de zonage."` | `PolicyEvidence.source_rule_excerpt`; str |
| `chapters[12].evidence[1].source_rule_sha256` | `"c434670531b43bbc23dd24c1fa01bba1eedaee0ba9e241b9f432255c74db30d2"` | `PolicyEvidence.source_rule_sha256`; str |
| `chapters[12].evidence[1].source_rule_start` | `69` | `PolicyEvidence.source_rule_start`; int |
| `chapters[12].evidence[1].source_rule_end` | `818` | `PolicyEvidence.source_rule_end`; int |
| `chapters[12].evidence[1].interpretation_note` | `"This is the separate technical-infrastructure exception; BESS necessity and classification are unresolved."` | `PolicyEvidence.interpretation_note`; str |
| `chapters[12].route_assessments[0].route_id` | `"MURET-N-ROUTE-01"` | `RouteAssessment.route_id`; str |
| `chapters[12].route_assessments[0].route_kind` | `"RESTRICTION_EXCEPTION_ROUTE"` | `RouteAssessment.route_kind`; str |
| `chapters[12].route_assessments[0].positive_evidence_ids[0]` | `"MURET-N-INFRA-ROUTE-01"` | `RouteAssessment.positive_evidence_ids`; str |
| `chapters[12].route_assessments[0].condition_evidence_ids` | `[]` | `RouteAssessment.condition_evidence_ids`; empty tuple |
| `chapters[12].route_assessments[0].difficulty_evidence_ids[0]` | `"MURET-N-RESTRICTION-01"` | `RouteAssessment.difficulty_evidence_ids`; str |
| `chapters[12].route_assessments[0].applicability_note` | `"The restriction and its listed exception are assessed as one coherent route; BESS applicability remains unresolved."` | `RouteAssessment.applicability_note`; str |


## STEP 7F.1A.4 dependent-model refresh

This historical heading remains for navigation, not as a new execution claim. R6 corrects explanations without changing YAML, code, tests, schemas or hashes. The six old embedded model blocks matched current source mechanically; that did not establish accuracy/completeness of their generic prose.

## 5. Classes / models / dataclasses

### `_StrictConfigModel`

All five policy models inherit `BaseModel` through this base, with `ConfigDict(extra="forbid", frozen=True)`. Extra fields and attribute reassignment are rejected. Collections are recursively tuples of strict strings or frozen models: required articles; chapters; reviewed sections, evidence and routes; three route-role arrays. YAML lists become tuples without sorting. Ordinary append/remove/item/slice assignment is unavailable.

Unchecked `model_construct` or `model_copy(update=...)` are not authoritative validation. Public boundaries reconstruct supplied policy objects from `model_dump(mode="python")` and revalidate. Model dumps are detached serialization values, not mutable aliases to the retained tuple/model graph. The result's frozen dataclass is different: its DataFrames/GeoDataFrame remain mutable and require result revalidation.

Field conventions: **exact string** = StrictStr, nonempty, rejected if unequal to its stripped value; no stripping transformation, internal whitespace retained. **SHA** = StrictStr matching `^[0-9a-f]{64}$`, not a file read. **Required** = no default and nonnullable. StrictInt rejects booleans and numeric-string coercion. No policy field/member is nullable.

### `PolicySourceLock`

All six fields are required. The root additionally exact-string-checks document_id and structure_profile beyond the lock class's StrictStr/min_length=1. Hash shapes alone establish no source authority.

| Field | Runtime contract | Exact equality in _validate_policy_lock / propagation |
|---|---|---|
| document_id | exact string in a complete policy | index.document_id; document lineage |
| archive_sha256 | SHA | index.archive_sha256; archive lineage |
| pdf_sha256 | SHA | index.pdf_sha256; PDF lineage |
| index_content_sha256 | SHA | index.index_content_sha256; indexed-content identity |
| structure_result_content_sha256 | SHA | structure.structure_result_content_sha256; factual-structure identity |
| structure_profile | exact string in a complete policy | structure.structure_profile; structure-profile lineage |

Comparisons follow factual index/structure validation in `_build_result`, not YAML loading. They use exact case-sensitive values, not approximate filenames/prefixes. R6 does not physically reread the recorded PDF/source identities.

### `PolicyEvidence`

All 16 fields are required, with no defaults.

| Field | Runtime contract / rejection | Meaning and propagation |
|---|---|---|
| evidence_id | exact string | Globally unique key in catalogs, chapter arrays, links and parcel decision/context arrays. |
| section_id | exact string | Structured section ID, not article number; later resolved against factual sections. |
| page_number | StrictInt >= 1 | One-based indexed page number in the section/page key; output int64. |
| evidence_kind | eight-value Literal matrix below | Configured category retained in catalog, not inferred from text. |
| evidence_direction | four-value Literal matrix below | Compatible route role or context-only retention. |
| exact_raw_excerpt | exact string, 1..600 Python characters | Smaller literal quote, copied without normalization. |
| excerpt_sha256 | SHA; equals SHA256(exact_raw_excerpt encoded UTF-8) | Binds quoted text, not its occurrence location. |
| section_page_fragment_sha256 | SHA at model loading | At application must equal reconstructed fragment hash. |
| excerpt_start | StrictInt >= 0 | Inclusive zero-based character offset in fragment raw_text. |
| excerpt_end | StrictInt >= 1 and > excerpt_start | Exclusive character boundary; later <= len(raw_text). |
| source_rule_id | exact string | Global name of one exact larger rule occurrence; coherent identity reuse allowed. |
| source_rule_excerpt | exact string, minimum 1, no 600-character maximum | Larger conditional/restriction frame retained around a shorter phrase. |
| source_rule_sha256 | SHA; equals SHA256(source_rule_excerpt encoded UTF-8) | Full-rule text identity, independently checked. |
| source_rule_start | StrictInt >= 0 | Inclusive character offset in the same fragment. |
| source_rule_end | StrictInt >= 1 and > source_rule_start | Exclusive character offset, later bounded by fragment length. |
| interpretation_note | exact string | Human qualification retained and hashed, not automatically interpreted. |

Directions: **P** = SUPPORTS_POTENTIAL_COMPATIBILITY; **D** = SUPPORTS_DIFFICULTY; **C** = CONDITION; **X** = CONTEXT_ONLY. These are literal values, not weights.

| evidence_kind | Allowed directions |
|---|---|
| USE_PERMISSION | P, X |
| USE_RESTRICTION | D, X |
| PUBLIC_INTEREST_EXCEPTION | P, C, X |
| TECHNICAL_EQUIPMENT_RULE | P, D, C, X |
| ICPE_RULE | P, D, C, X |
| RISK_OR_NUISANCE_CONDITION | D, C, X |
| ACCESS_OR_NETWORK_CONDITION | D, C, X |
| OTHER_RELEVANT_RULE | D, C, X |

The model checks both quoted-string hashes and `source_rule_start <= excerpt_start < excerpt_end <= source_rule_end`, but lacks factual fragment text. At application, `_validate_policy_evidence` resolves section/page, matches fragment SHA, requires exact fragment slices for both excerpt and rule, recomputes both UTF-8 hashes, and checks the excerpt again relative to the rule string. Offsets count Python string characters, not UTF-8 bytes or PDF coordinates. No search/Unicode/whitespace normalization makes these comparisons pass.

Evidence-occurrence key: `(chapter label, section_id, page_number, fragment SHA, excerpt_start, excerpt_end)`. One key must have one evidence ID/kind/direction; even compatible duplicate IDs at the same chapter-scoped location fail. A GENERAL occurrence may be represented for different chapters with different evidence IDs. Identical quote text at distinct offsets is a distinct occurrence.

Rule identity: `(section_id, page_number, fragment SHA, source_rule_start, source_rule_end, source_rule_sha256, source_rule_excerpt)`. One rule ID cannot denote different identities; one location (first five members) cannot use different rule IDs. Within one section/page/fragment, rule ranges cannot partially overlap; identical coherently reused ranges and adjacent nonoverlapping ranges are allowed. This is not a blanket prohibition of overlap between smaller evidence excerpts.

### `RouteAssessment`

| Field | Runtime contract | Use |
|---|---|---|
| route_id | required exact string; unique per chapter and globally | Route and link-table key. |
| route_kind | required four-value Literal below | Role membership and derived route status. |
| positive_evidence_ids | tuple[StrictStr, ...], default () | Exact same-chapter IDs with SUPPORTS_POTENTIAL_COMPATIBILITY direction. |
| condition_evidence_ids | tuple[StrictStr, ...], default () | Exact same-chapter IDs with CONDITION direction. |
| difficulty_evidence_ids | tuple[StrictStr, ...], default () | Exact same-chapter IDs with SUPPORTS_DIFFICULTY direction. |
| applicability_note | required exact string | Retained/hashed human assessment of linkage, not semantic proof of applicability. |

Each role array is unique; an ID cannot occupy two roles in one route. Unknown/another-chapter IDs fail. One evidence may link to multiple compatible routes. Every non-context evidence must link to at least one route. CONTEXT_ONLY cannot occupy any direction-checked role and remains unlinked.

| route_kind | Positive nonempty | Condition nonempty | Difficulty nonempty | Derived route status |
|---|---|---|---|---|
| DIRECT_ROUTE | yes | no | no | POTENTIALLY_COMPATIBLE |
| CONDITIONAL_ROUTE | yes | yes | no | CONDITIONAL_REVIEW |
| RESTRICTION_EXCEPTION_ROUTE | yes | no | yes | CONDITIONAL_REVIEW |
| DIFFICULTY_ONLY | no | no | yes | LIKELY_DIFFICULT |

Nonempty does not mean exactly one member. The code proves structural role/direction coherence, not legal applicability. References need not share a source_rule_id: AUp and AU0/AUf0 explicitly link different occurrences.

### `ChapterPolicy`

| Field | Runtime contract | Use / validation |
|---|---|---|
| resolved_zone_chapter_label | required exact string | Unique root key; exact factual chapter-label set required at application, case preserved. |
| review_completeness | required COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES or INCOMPLETE | Gates status and required-article coverage, not whole-PLU completeness. |
| reviewed_section_ids | tuple[StrictStr, ...], default (), exact unique members | Explicit claims checked against sections and required article IDs. |
| review_note | required exact string | Retained chapter metadata, not proof that a human actually read the PDF. |
| zoning_precheck_status | required POTENTIALLY_COMPATIBLE, CONDITIONAL_REVIEW, LIKELY_DIFFICULT or UNKNOWN | Must equal _derived_chapter_status; propagated to mapped zones/positive relations. |
| zoning_precheck_confidence | required HIGH, MEDIUM or LOW | Retained assessment; INCOMPLETE forces LOW; not derived from evidence quantity or legal certainty. |
| rationale | required exact string | Retained/hashed explanation, not a classifier instruction. |
| missing_information | required exact string | Retained/hashed unresolved matters, not filled automatically. |
| evidence | tuple[PolicyEvidence, ...], default () | Ordered catalog declarations and chapter evidence arrays. |
| route_assessments | tuple[RouteAssessment, ...], default () | Ordered routes, nested/global coherence checks. |

Chapter derivation, in order: INCOMPLETE → UNKNOWN (and independently requires LOW); otherwise any conditional/restriction-exception route → CONDITIONAL_REVIEW; otherwise DIRECT_ROUTE + DIFFICULTY_ONLY → UNKNOWN, DIRECT_ROUTE without difficulty → POTENTIALLY_COMPATIBLE; otherwise difficulty → LIKELY_DIFFICULT; no routes → UNKNOWN. Context alone supplies no route; a bare condition does not create CONDITIONAL_REVIEW.

Every factual ZONE_CHAPTER must appear exactly once in the policy, with no extra chapter. For each chapter and configured article number, `_required_section_ids_by_chapter` requires exactly one ARTICLE with that raw number, label and parent. This existence/uniqueness requirement also applies to INCOMPLETE chapters. COMPLETE additionally requires those IDs in reviewed_section_ids; INCOMPLETE retains ordered missing required IDs.

Reviewed IDs must exist. GENERAL sections are permitted; otherwise only same-chapter ZONE_CHAPTER/ARTICLE, with correct article parent, are accepted. Evidence sections must be reviewed, belong to the correct chapter unless GENERAL, and have a section/page fragment. Completeness covers only configured articles '1' and '2', not all articles, annexes, prescriptions, servitudes or current law.

### `BessZoningPolicyConfig`

| Root field | Runtime contract | Use |
|---|---|---|
| schema_version | required StrictInt exactly 5 | Schema check; policy_schema_version in result. |
| policy_profile | required exact string | Profile lineage; v6 suffix is not schema 6. |
| planning_precheck_scope | required Literal WRITTEN_ZONING_REGULATION_ONLY | Output scope uses the identical module constant. |
| review_scope | required Literal CONFIGURED_USE_CONTROL_ARTICLES_ONLY | Completeness scope; output uses identical module constant. |
| source_lock | required PolicySourceLock | Six shape-checked locks; equality later. |
| required_zone_article_numbers | required tuple[StrictStr, ...], minimum 1, exact unique members | Ordered string identifiers, not numeric quantities. |
| chapters | required tuple[ChapterPolicy, ...], minimum 1 | Ordered chapters; global uniqueness/occurrence/rule/link checks. |

No field is nullable. No entries digest, priority mapping, URL, CRS, legal-reference schema or score is borrowed from the CNIG policy.

## 6. Functions and methods

Exact signatures of the existing loader, public boundaries and policy hash helper (definitions in the owner, not new executable code):

```python
def load_bess_zoning_policy_config(path: str | Path) -> BessZoningPolicyConfig:
```

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

```python
def _resolved_policy(
    policy: BessZoningPolicyConfig | str | Path,
) -> BessZoningPolicyConfig:
```

```python
def _policy_sha256(config: BessZoningPolicyConfig) -> str:
```

`load_bess_zoning_policy_config` reads once, calls `loads_strict_yaml`, requires a Mapping root and validates the complete model. The safe loader decodes UTF-8 bytes and rejects duplicate keys at every mapping depth (including after YAML merge flattening). It does not accept an arbitrary caller-supplied compiled policy as file bytes; the public interpretation API nevertheless explicitly accepts an in-memory BessZoningPolicyConfig and revalidates its dumped contents.

For both public interpretation and validation, control order is:

1. `validate_normalized_planning_zoning_inputs` validates the supplied physical GPU context and reconstructs normalized zoning facts before resolving the policy.
2. `_resolved_policy` reconstructs/revalidates a supplied model or loads the supplied path.
3. `_build_result` validates the regulation index; reconstructs/validates the factual structure and obtains section/page fragments; checks the six policy locks.
4. It validates/copies parcels, zones and relations, and verifies complete resolved zone mapping. It computes policy identity; builds route rows/links; validates exact evidence occurrences and required-article coverage.
5. It builds chapter/source-zone/parcel-zone/parcel outputs, records input identities and computes component/result hashes.
6. The builder calls `_compare_results(result, result, parcels)`: checks the built envelope/frames/references/preservation; this is **not** a second independent reconstruction.
7. The separate public validator instead builds an **expected** result from all factual and policy inputs and compares the supplied result to that reconstruction, then performs its integrity checks.

The GPU gate checks exact GpuPlanningDocument type, appropriate frame kinds and summary columns, calls `revalidate_gpu_spatial_layer_sources` for the zoning layer, rebuilds zoning/intersections using the freshly validated layer and original parcel facts, and compares schemas/values/order/geometry/summary dtypes. This is materially stronger than string-lock comparison. Index validation checks index/page metadata and internal hashes; it does not itself reopen/re-extract the PDF. Structure validation reconstructs from that supplied validated index, zones, relations and structure config, compares the result and returns retained fragment raw_text with its UTF-8 SHA256. None of these physical/factual reconstruction boundaries was executed in R6.

## 7. Data contracts

The policy model is not an output table. The BessZoningPrecheckResult envelope carries schema/profile/scopes, source lineage, input and output identities, touch_only_relation_count, six ordinary DataFrames plus one GeoDataFrame:

| Result field | Granularity / retained policy facts |
|---|---|
| evidence_catalog | One row per evidence, including exact quotes, positions, full-rule identity, kind/direction/note, source lineage, sorted reverse route IDs/roles and decision_linked. |
| evidence_route_links | One row per route/evidence reference, role POSITIVE/CONDITION/DIFFICULTY and compatible direction; sorted by route_id/evidence_id with stable mergesort, no duplicate pair. |
| route_assessments | One row per configured route, in chapter/route declaration order, role tuples, applicability note and derived_route_status. |
| chapter_policy | One row per factual chapter in structure order; review claims, ordered missing required IDs, confidence, rationale, missing information, all/decision/context evidence IDs. |
| source_zone_policy | One row per mapped raw zone label in mapping order; chapter identity, EXACT/CONFIG_ALIAS mapping status, one unambiguous source layer, status/confidence and evidence arrays. |
| parcel_zone_interpretations | One row per AREA_OVERLAP, in retained relation order; zone/source IDs, chapter, area/share, status/confidence/evidence and lineage. TOUCH_ONLY excluded here. |
| parcels | Copy of all original parcel rows/index/geometry/CRS/columns, with the 15 precheck columns below appended. No row filtering. |

Raw zone labels must be covered exactly by the structure's mapping with no extras; only EXACT and CONFIG_ALIAS resolve. Unmapped/ambiguous statuses are rejected, not silently made UNKNOWN and not resolved by label prefixes.

Parcels require unique exact IDs, active geometry named geometry, readable CRS, non-null/nonempty/valid Polygon or MultiPolygon, nonnegative integer existing feature counts and matching document/archive lineage. Existing precheck-column collisions fail. Relations require unique parcel/zone pairs, known identities/layers/lineage, finite nonnegative areas and shares, positive denominators, area/percentage consistency under shared technical overlay tolerance. AREA_OVERLAP must have positive area; TOUCH_ONLY exactly zero. Earlier source-complete checks may reject a mutation before these local checks run.

Appended parcel columns are exactly: `zoning_precheck_status`, `dominant_zone_precheck_status`, `dominant_zone_precheck_confidence`, `positive_area_zone_count`, `distinct_zone_status_count`, `non_dominant_different_status_count`, `touch_only_zone_count`, `zoning_precheck_evidence_ids`, `zoning_precheck_context_evidence_ids`, `zoning_precheck_requires_formal_review`, `planning_precheck_scope`, `review_scope`, `non_zoning_planning_features_interpreted`, `zoning_precheck_policy_profile`, `zoning_precheck_policy_sha256`.

Positive relations are sorted for dominance by descending intersection_area_m2, then ascending planning_zone_id (stable sort); the already supplied dominant ID must equal this result. The dominant confidence/status is retained separately. If all positive-zone statuses agree, that status is the parcel status; otherwise MIXED_REVIEW_REQUIRED, even when the dominant zone has a more favorable status. No area-weighted vote hides a minority status. With no positive overlap, dominant ID must be null and overall status is UNKNOWN, dominant status/confidence are null, evidence tuples empty and positive/distinct/differing counts zero. TOUCH_ONLY is counted but contributes no decision evidence.

Decision/context evidence IDs in parcels are separate sorted unique unions across positive relations. Context is not promoted into decision evidence. All parcels set requires_formal_review=True and non_zoning_planning_features_interpreted=False. The four count columns are int64; the two flags are bool. Confidence is descriptive, not legal certainty.

## 8. Interfaces

The public loader requires a path argument. Interpreter and validator signatures explicitly include the physical planning_document and structure_config; a policy alone cannot create a valid result. Supplied policy objects are not trusted merely because their class is frozen. Neither direct DataFrame mutation nor recalculation of an envelope's own hashes replaces source-bound reconstruction.

R6's one offline loader call produced 1 root model, 1 lock, 13 chapters, 28 evidence models, 13 route models and 80 tuple occurrences, with no reachable list/dict/set/bytearray in that loaded object. It did not call the interpreter/validator or create a BessZoningPrecheckResult.

## 9. Error handling

The loader rethrows BessZoningPrecheckError; StrictYamlError is translated to BessZoningPrecheckError with its message and chained cause; other file/path/model exceptions become `BESS zoning policy is invalid` with cause. Non-mapping YAML roots have their own controlled error. Pydantic validators raise ValueError/validation errors for malformed fields, unsupported schema, incoherent membership/derived status, duplicates, hash or range inconsistencies.

At public application boundaries BessZoningPrecheckError passes through; PlanningRegulationStructureError and PlanningZoningError receive factual-structure/GPU-specific wrappers with chained causes. Other exceptions, including index errors outside those two named types, receive `BESS zoning precheck could not be built safely` or `BESS zoning precheck validation failed safely`. Do not infer which guard ran solely from a broad pytest.raises.

## 10. Side effects

The YAML loader reads the specified file, parses and validates; no network, writes, GIS operation or raw-byte hashing is performed by the loader. Evidence-string SHA checks do run inside the model, so “hashing: none” would be false. The separate `_policy_sha256` hashes validated values.

The full interpreter/validator calls physical source validation and factual/spatial reconstruction through dependencies. Its own result construction uses copies and does not write artifacts or repair geometries. These larger side effects are not attributes of the loader and were not invoked by R6.

## 11. Security / trust boundaries

Shape validation of six lock strings ≠ equality to factual context ≠ physical GPU validation ≠ agreement with indexed raw fragments ≠ legal interpretation. Exact source-rule frames prevent a smaller phrase from being treated as the whole recorded rule, but structural link validation cannot decide whether a BESS satisfies an exception or a requirement. Retained applicability/rationale/missing-information text explicitly marks these unresolved judgments.

Hash validation detects changes relative to a trusted input reconstruction; it is not a digital signature or independent proof of truth. Result frames remain mutable. `validate_bess_zoning_precheck` rebuilds from its supplied factual inputs; do not describe it as rereading every original PDF/legal source afresh.

## 12. GIS / CRS rules

This YAML configures no CRS, distance, buffer, overlay algorithm or geometric threshold. The interpreter preserves parcel storage geometry/CRS; its prerequisite zoning reconstruction uses the existing EPSG:2154 planar-XY overlay implementation. Areas/shares are factual inputs validated against that reconstruction, not policy scores. R6 performs no GIS work.

## 13. Provenance rules

Three identities must remain distinct: documentation Git SHA, historical checkout SHA, and canonical policy hash. The loader reads checkout bytes; its validated values are identical to the Git YAML values despite the preserved EOL difference.

Policy hash payload is exactly `{"domain":"landscout.bess_zoning.policy_config","config":config.model_dump(mode="json")}`. `_canonical_sha256` recursively canonicalizes, JSON-serializes with ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",",":"), UTF-8 encodes and SHA256-hashes. Object key order is sorted; array order is retained. Required-article/chapter/evidence/route/role declaration order is not sorted away. There is no separate entries hash and no hash field inside this policy model to exclude.

Canonical special values in this module: None/pd.NA → null; NumPy scalars → their Python item recursively; float NaN → null; tuple/list/NumPy array → ordered JSON array; mappings → string keys with recursive values; geometry → hexadecimal WKB without SRID; timestamps/datetime/date → ISO string; bytes → hex. Unsupported objects raise a controlled error; infinities fail strict JSON serialization. These general hash rules do not make nulls, NaN or geometries valid policy fields.

Frame payload is `columns` in requested order, `index_names`, ordered `index` and ordered record `rows`. A GeoDataFrame adds CRS.to_json_dict() and geometry_column. Duplicate/missing columns or missing geospatial CRS fail. Frame hashes include their explicit domain; row/index order matters, and dtype metadata is not part of this local frame payload.

Input identities are:
- factual_structure_content_sha256: domain `landscout.bess_zoning.factual_structure_input` plus structure_result_content_sha256, section_hash_schema_version, structure_config_sha256, sections_content_sha256, zone_map_content_sha256 and topic_evidence_content_sha256;
- zone_mapping_input_sha256: domain `landscout.bess_zoning.zone_mapping_input`, frame payload for zones' six selected identity/lineage columns and all structure.zone_mapping columns;
- zoning_relations_input_sha256: domain `landscout.bess_zoning.zoning_relations_input` plus all supplied relation columns and frame payload, with the exact column tuple retained.

Seven component hashes use domain `landscout.bess_zoning.` plus respectively evidence_catalog, evidence_route_links, route_assessments, chapter_policy, source_zone_policy, parcel_zone_policy, parcel_output. Each includes common metadata and its frame payload. Common metadata consists exactly of result_hash_schema_version, policy_schema_version, policy_profile, planning_precheck_scope, review_scope, document_id, archive_sha256, pdf_sha256, index_content_sha256, structure_result_content_sha256, structure_profile, policy_config_sha256, factual_structure_content_sha256, zone_mapping_input_sha256, zoning_relation_hash_columns (as list), zoning_relations_input_sha256 and touch_only_relation_count.

Complete result domain is `landscout.bess_zoning.precheck_result`, with that common metadata and the seven component hashes. Component metadata excludes output hash fields; the complete result excludes its own complete_result_content_sha256. `_result_with_hashes` fills components first and complete hash last. These result hashes were studied, not computed in R6.

## 14. Business meaning

Configured chapter associations below are literal data, not new source validation. Every row declares COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES / CONDITIONAL_REVIEW / LOW. P/C/D columns retain exact ordered route ID arrays; empty arrays remain empty. Context is separate and unlinked.

| Chapter | Reviewed section IDs | Route ID / kind | P / C / D references | Unlinked context |
|---|---|---|---|---|
| `"UA"` | `["SECTION-0008","SECTION-0009"]` | `"MURET-UA-ROUTE-01"` / `"CONDITIONAL_ROUTE"` | `["MURET-UA-ICPE-ROUTE-01"]` / `["MURET-UA-ICPE-CONDITION-01"]` / `[]` | `[]` |
| `"UB"` | `["SECTION-0021","SECTION-0022"]` | `"MURET-UB-ROUTE-01"` / `"CONDITIONAL_ROUTE"` | `["MURET-UB-ICPE-ROUTE-01"]` / `["MURET-UB-ICPE-CONDITION-01"]` / `[]` | `[]` |
| `"UC"` | `["SECTION-0036","SECTION-0037"]` | `"MURET-UC-ROUTE-01"` / `"CONDITIONAL_ROUTE"` | `["MURET-UC-ICPE-ROUTE-01"]` / `["MURET-UC-ICPE-CONDITION-01"]` / `[]` | `[]` |
| `"UD"` | `["SECTION-0051","SECTION-0052"]` | `"MURET-UD-ROUTE-01"` / `"CONDITIONAL_ROUTE"` | `["MURET-UD-ICPE-ROUTE-01"]` / `["MURET-UD-ICPE-CONDITION-01"]` / `[]` | `[]` |
| `"UF"` | `["SECTION-0065","SECTION-0066"]` | `"MURET-UF-ROUTE-01"` / `"CONDITIONAL_ROUTE"` | `["MURET-UF-ICPE-ROUTE-01"]` / `["MURET-UF-ICPE-CONDITION-01"]` / `[]` | `[]` |
| `"UP"` | `["SECTION-0080","SECTION-0081"]` | `"MURET-UP-ROUTE-01"` / `"RESTRICTION_EXCEPTION_ROUTE"` | `["MURET-UP-PUBLIC-ROUTE-01"]` / `[]` / `["MURET-UP-RESTRICTION-01"]` | `["MURET-UP-ICPE-CONDITION-01"]` |
| `"AU"` | `["SECTION-0095","SECTION-0096"]` | `"MURET-AU-ROUTE-01"` / `"CONDITIONAL_ROUTE"` | `["MURET-AU-ICPE-ROUTE-01"]` / `["MURET-AU-ICPE-CONDITION-01"]` / `[]` | `[]` |
| `"AUp"` | `["SECTION-0110","SECTION-0111"]` | `"MURET-AUp-ROUTE-01"` / `"CONDITIONAL_ROUTE"` | `["MURET-AUP-PUBLIC-ROUTE-01"]` / `["MURET-AUP-INFRASTRUCTURE-CONDITION-01"]` / `[]` | `["MURET-AUP-ICPE-CONDITION-01"]` |
| `"AUf"` | `["SECTION-0125","SECTION-0126"]` | `"MURET-AUf-ROUTE-01"` / `"CONDITIONAL_ROUTE"` | `["MURET-AUF-ICPE-ROUTE-01"]` / `["MURET-AUF-ICPE-CONDITION-01"]` / `[]` | `[]` |
| `"AU0"` | `["SECTION-0140","SECTION-0141"]` | `"MURET-AU0-ROUTE-01"` / `"CONDITIONAL_ROUTE"` | `["MURET-AU0-INFRA-ROUTE-01"]` / `["MURET-AU0-MODIFICATION-CONDITION-01"]` / `[]` | `[]` |
| `"AUf0"` | `["SECTION-0155","SECTION-0156"]` | `"MURET-AUf0-ROUTE-01"` / `"CONDITIONAL_ROUTE"` | `["MURET-AUF0-INFRA-ROUTE-01"]` / `["MURET-AUF0-MODIFICATION-CONDITION-01"]` / `[]` | `[]` |
| `"A"` | `["SECTION-0170","SECTION-0171"]` | `"MURET-A-ROUTE-01"` / `"RESTRICTION_EXCEPTION_ROUTE"` | `["MURET-A-INFRA-ROUTE-01"]` / `[]` / `["MURET-A-RESTRICTION-01"]` | `[]` |
| `"N"` | `["SECTION-0184","SECTION-0185"]` | `"MURET-N-ROUTE-01"` / `"RESTRICTION_EXCEPTION_ROUTE"` | `["MURET-N-INFRA-ROUTE-01"]` / `[]` / `["MURET-N-RESTRICTION-01"]` | `[]` |


UA, UB, UC, UD, UF, AU and AUf pair an ICPE route phrase with its compatibility/local-necessity condition from the same full rule. ICPE applicability to BESS is unresolved. AU/AUf explicitly do not use infrastructure prerequisites alone as a positive route.

UP links the Article UP 1 public/collective-interest exception and its surrounding restriction as RESTRICTION_EXCEPTION_ROUTE; the separate Article UP 2 ICPE condition is CONTEXT_ONLY. AUp links the public-interest exception to the distinct Article AUp 2 infrastructure prerequisite as CONDITIONAL_ROUTE; its ICPE clause is likewise only context. Neither context clause is an unconditional prerequisite of the selected route.

AU0/AUf0 link an infrastructure exception to a separate PLU-modification prerequisite. A/N link a broad restriction with a technical/infrastructure exception in the same full rule. Classification, necessity and satisfaction of requirements remain unresolved, exactly as the configured rationale, interpretation/applicability notes and missing_information state. No new legal reading of these excerpts occurred in R6.

## 15. Explicit non-goals

No BESS authorization/prohibition, permit, formal ICPE determination, current-law conclusion, parcel score/rank/rejection, environmental categorization, owner/contact inference, road/legal/heavy-truck access or grid-feasibility conclusion. Non-zoning planning features remain uninterpreted **by this written-zoning result**, without denying the existence of separate application/aggregation stages elsewhere.

## 16. Tests

Evidence below is **source reading, not R6 execution**. [Unit tests](../../../../../tests/unit/test_interpret_bess_zoning.py) were read in full, including helpers and fixtures; [physical integration tests](../../../../../tests/integration/test_gpu_planning_end_to_end.py) likewise. Relevant [immutability tests](../../../../../tests/unit/test_deep_immutability.py) were read at lines 300–481.

| Read test area | What the actual bodies establish when run / limits |
|---|---|
| Unit helpers 51–399, valid output 437–470 | Three synthetic raw-text pages are self-hashed into an index; synthetic zones/relations/parcels and factual structure generate policy fragments. The inputs fixture replaces validate_normalized_planning_zoning_inputs with a no-op and uses object() as planning_document. Output assertions do not prove physical GPU authority. |
| Locks/chapters/model schema 473–766 | All six mismatched lock fields; missing/extra policy chapter; duplicate chapter/IDs/occurrences; literal status/confidence/extra-field and schema 1..4 rejection; duplicate YAML key; full kind/direction matrix. Model checks and private _zone_chapter_rows tests are not PDF validation. |
| Exact rules/real configuration 769–1036 | String hashes/range mutations, model acceptance of repeated text at distinct offsets, checked-in ICPE/UP/AUp frames and exact UP/AUp IDs/excerpts/hashes/offset constants. Real-YAML tests load configuration, not real fragments or the original PDF. |
| Routes 1039–1257 | Declared-vs-derived status, condition-alone/unlinked evidence, incompatible/foreign role references, global route IDs, context exclusion, compatible multiple routes, direct/difficulty/conditional/restriction-exception examples. “Unrelated positive and condition” is rejected through declared-status/link coherence, not semantic natural-language comparison. |
| Review completeness 1260–1524 | INCOMPLETE requires UNKNOWN/LOW and preserves missing IDs; required articles exist once with correct parent; COMPLETE must list them; reviewed/evidence sections respect chapter; GENERAL evidence can be scoped to different chapters. Several exact-one-article cases call the private helper directly. |
| Occurrences/mapping/propagation 1527–1712 | Synthetic fragment slices, a coordinated rehashed move to another repeated occurrence rejected against source rebuild, exact/alias mapping, reverse links and context segregation, mixed parcel statuses and TOUCH_ONLY, prior geometry/order/index/CRS preservation. Forged unresolved mapping can fail upstream structure reconstruction before local _validate_mapping. |
| Mutation and call order 1715–2109 | No mutation of synthetic input frames; changed policies/evidence; changed relation/hierarchy/count/source identities; coordinated output rehashes still rejected by rebuilt expectation; explicit spies count source and structure gates. The physical-source early-failure test is a stub that proves policy resolution is not called after that failure, not an actual physical mutation. |
| Guard-order cautions in those tests | Denominator/share tests use broad errors and can stop at structure validation before local numeric checks. In test_factual_zone_mapping_counts_are_recomputed, the count mutation exercises the interpreter; its later mapping-label mutation passes the module-level valid_result fixture function rather than requesting its value, and only asserts a broad BessZoningPrecheckError. Do not attribute that arm specifically to the final result comparison. |
| Persistence 2114–2164 | Temporary Parquet readback of synthetic result tables/GeoDataFrame is validated; YAML roundtrip validates a synthetic policy. Not a fresh production-artifact run. |
| Physical integration 1–409 | Builds a local ZIP containing a synthetic GeoPackage and generated one-page PDF; uses actual extraction/inspection/intersection/index/structure/public precheck validation, with no no-op zoning gate. Byte mutation, source-config hash mutation and missing required article 2 are rejected. The synthetic policy is UNKNOWN/LOW with empty evidence/routes: not validation of the 28 Muret evidence occurrences or proof of project eligibility. |
| Deep immutability 300–481 | Recursive walk includes the loaded written policy and rejects reachable list/dict/set/bytearray. Operation-by-operation tuple tests use scan commune codes, mapping/alias tests use structure config, and set tests use road policy—not every written-policy field individually. The written policy hash is compared to constant ef1f7cd0…767586. |

Existing historical test limitations remain open as recorded elsewhere; the distinctions above do not automatically create a new application defect. R6 runs no pytest and reports no fresh pass count.

## 17. Change impact

Changing any validated policy value, ordering, lock, note, quote, offset or role changes canonical policy identity and all dependent result identities. A YAML-only presentation/EOL change may change raw hashes without changing canonical values; never mix byte bases. Changes would need a separately authorized source/policy review, tests and directly affected artifacts; none is performed here. A documentation correction changes this companion binding, not application behavior.

R6's one existing-loader invocation succeeded offline with no guarded network attempt. Value counts/types and canonical policy hash were computed from that actual loaded object; raw Git/checkout bytes and old/new snapshots were compared separately. Original PDF fragments, current official sources, legal meaning and physical result hashes were not revalidated. Visual rendering remains PENDING; static Markdown checks are not a visual pass.

## 18. Complete readable configuration and authoritative raw-byte snapshot

### Complete readable YAML

The fence is the **exact 46,384 Git-content bytes** decoded as UTF-8, including all 723 LF and final LF. It is also the checkout's readable text with CRLF reduced to LF, but is not its raw-byte authority. No YAML was rewritten.

```yaml
schema_version: 5
policy_profile: muret_bess_written_zoning_v6
planning_precheck_scope: WRITTEN_ZONING_REGULATION_ONLY
review_scope: CONFIGURED_USE_CONTROL_ARTICLES_ONLY
source_lock:
  document_id: 33edb4c9f6943c88d8d92518bff20bec
  archive_sha256: 9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93
  pdf_sha256: 5358ebad6b0cda6de681ba3536e29b8b6291fb701c7d3711f4ee1d6fdb85c6fb
  index_content_sha256: 6a0009228ca17128c0a8bb329d9c2277a1b6638708a67b913b72ee93063e42cd
  structure_result_content_sha256: 16f8a9edfff0d330f69579310da085f804f4641de973d98e0046bff5ea96b03c
  structure_profile: muret_plu_20240215_v1
required_zone_article_numbers:
- '1'
- '2'
chapters:
- resolved_zone_chapter_label: UA
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0008
  - SECTION-0009
  review_note: Articles UA 1 and UA 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Article UA 2 states a possible ICPE route and states separate compatibility and local-necessity conditions; whether a BESS qualifies remains unresolved.
  missing_information: BESS planning-use and ICPE classification, application of all Article UA 1/2 provisions, prescriptions, servitudes, project effects and design.
  evidence:
  - evidence_id: MURET-UA-ICPE-ROUTE-01
    section_id: SECTION-0009
    page_number: 8
    evidence_kind: ICPE_RULE
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: Les installations classées pour la protection de l’environnement ne sont autorisées
    excerpt_sha256: e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff
    section_page_fragment_sha256: 2da8d15fad096a694d7b56ecfc1d61d0ba375aac1c254794d63388524cc755f6
    excerpt_start: 100
    excerpt_end: 183
    interpretation_note: This is a literal ICPE route phrase; it does not establish that a BESS is an applicable ICPE use.
    source_rule_id: MURET-UA-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition d’être compatibles avec le milieu environnant et nécessaires à la vie  du \nquartier et de la cité."
    source_rule_sha256: 8def59e860d434e482899e9709520d221dd576e41e00f276bbe9c87e5127a8df
    source_rule_start: 100
    source_rule_end: 301
  - evidence_id: MURET-UA-ICPE-CONDITION-01
    section_id: SECTION-0009
    page_number: 8
    evidence_kind: ICPE_RULE
    evidence_direction: CONDITION
    exact_raw_excerpt: compatibles avec le milieu environnant et nécessaires à
    excerpt_sha256: 45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928
    section_page_fragment_sha256: 2da8d15fad096a694d7b56ecfc1d61d0ba375aac1c254794d63388524cc755f6
    excerpt_start: 210
    excerpt_end: 265
    interpretation_note: This is the separate compatibility and necessity qualification attached to the ICPE route.
    source_rule_id: MURET-UA-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition d’être compatibles avec le milieu environnant et nécessaires à la vie  du \nquartier et de la cité."
    source_rule_sha256: 8def59e860d434e482899e9709520d221dd576e41e00f276bbe9c87e5127a8df
    source_rule_start: 100
    source_rule_end: 301
  route_assessments:
  - route_id: MURET-UA-ROUTE-01
    route_kind: CONDITIONAL_ROUTE
    positive_evidence_ids:
    - MURET-UA-ICPE-ROUTE-01
    condition_evidence_ids:
    - MURET-UA-ICPE-CONDITION-01
    difficulty_evidence_ids: []
    applicability_note: The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved.
- resolved_zone_chapter_label: UB
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0021
  - SECTION-0022
  review_note: Articles UB 1 and UB 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Article UB 2 states a possible ICPE route and separate compatibility and local-necessity conditions; BESS applicability is unresolved.
  missing_information: BESS planning-use and ICPE classification, application of all Article UB 1/2 provisions, prescriptions, servitudes, project effects and design.
  evidence:
  - evidence_id: MURET-UB-ICPE-ROUTE-01
    section_id: SECTION-0022
    page_number: 22
    evidence_kind: ICPE_RULE
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: Les installations classées pour la protection de l’environnement ne sont autorisées
    excerpt_sha256: e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff
    section_page_fragment_sha256: 7c678bbc92c2271fbb02f0c228f51e0b408b862780731b78f301b37731a894f3
    excerpt_start: 98
    excerpt_end: 181
    interpretation_note: This is a literal ICPE route phrase, not a BESS authorization.
    source_rule_id: MURET-UB-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 98
    source_rule_end: 307
  - evidence_id: MURET-UB-ICPE-CONDITION-01
    section_id: SECTION-0022
    page_number: 22
    evidence_kind: ICPE_RULE
    evidence_direction: CONDITION
    exact_raw_excerpt: compatibles avec le milieu environnant et nécessaires à
    excerpt_sha256: 45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928
    section_page_fragment_sha256: 7c678bbc92c2271fbb02f0c228f51e0b408b862780731b78f301b37731a894f3
    excerpt_start: 217
    excerpt_end: 272
    interpretation_note: This is the separate compatibility and necessity qualification.
    source_rule_id: MURET-UB-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 98
    source_rule_end: 307
  route_assessments:
  - route_id: MURET-UB-ROUTE-01
    route_kind: CONDITIONAL_ROUTE
    positive_evidence_ids:
    - MURET-UB-ICPE-ROUTE-01
    condition_evidence_ids:
    - MURET-UB-ICPE-CONDITION-01
    difficulty_evidence_ids: []
    applicability_note: The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved.
- resolved_zone_chapter_label: UC
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0036
  - SECTION-0037
  review_note: Articles UC 1 and UC 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Article UC 2 states a possible ICPE route subject to explicit compatibility and local-necessity conditions; BESS applicability is unresolved.
  missing_information: BESS planning-use and ICPE classification, application of all Article UC 1/2 provisions, prescriptions, servitudes, project effects and design.
  evidence:
  - evidence_id: MURET-UC-ICPE-ROUTE-01
    section_id: SECTION-0037
    page_number: 36
    evidence_kind: ICPE_RULE
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: Les installations classées pour la protection de l’environnement ne sont autorisées
    excerpt_sha256: e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff
    section_page_fragment_sha256: f6103c4139a65d12a9b6bf4c5edd37382fa6a2fa642c3a5805aa2898b1121365
    excerpt_start: 98
    excerpt_end: 181
    interpretation_note: This is a literal ICPE route phrase, not a BESS authorization.
    source_rule_id: MURET-UC-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 98
    source_rule_end: 307
  - evidence_id: MURET-UC-ICPE-CONDITION-01
    section_id: SECTION-0037
    page_number: 36
    evidence_kind: ICPE_RULE
    evidence_direction: CONDITION
    exact_raw_excerpt: compatibles avec le milieu environnant et nécessaires à
    excerpt_sha256: 45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928
    section_page_fragment_sha256: f6103c4139a65d12a9b6bf4c5edd37382fa6a2fa642c3a5805aa2898b1121365
    excerpt_start: 217
    excerpt_end: 272
    interpretation_note: This is the separate compatibility and necessity qualification.
    source_rule_id: MURET-UC-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 98
    source_rule_end: 307
  route_assessments:
  - route_id: MURET-UC-ROUTE-01
    route_kind: CONDITIONAL_ROUTE
    positive_evidence_ids:
    - MURET-UC-ICPE-ROUTE-01
    condition_evidence_ids:
    - MURET-UC-ICPE-CONDITION-01
    difficulty_evidence_ids: []
    applicability_note: The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved.
- resolved_zone_chapter_label: UD
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0051
  - SECTION-0052
  review_note: Articles UD 1 and UD 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Article UD 2 states a possible ICPE route subject to explicit compatibility and local-necessity conditions; BESS applicability is unresolved.
  missing_information: BESS planning-use and ICPE classification, application of all Article UD 1/2 provisions, prescriptions, servitudes, project effects and design.
  evidence:
  - evidence_id: MURET-UD-ICPE-ROUTE-01
    section_id: SECTION-0052
    page_number: 48
    evidence_kind: ICPE_RULE
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: Les installations classées pour la protection de l’environnement ne sont autorisées
    excerpt_sha256: e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff
    section_page_fragment_sha256: 67701fcf91b57f6d4c00a0c26d95c2904e736bd70c3da1bd49b949f2d60f6e9a
    excerpt_start: 446
    excerpt_end: 529
    interpretation_note: This is a literal ICPE route phrase, not a BESS authorization.
    source_rule_id: MURET-UD-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 446
    source_rule_end: 655
  - evidence_id: MURET-UD-ICPE-CONDITION-01
    section_id: SECTION-0052
    page_number: 48
    evidence_kind: ICPE_RULE
    evidence_direction: CONDITION
    exact_raw_excerpt: compatibles avec le milieu environnant et nécessaires à
    excerpt_sha256: 45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928
    section_page_fragment_sha256: 67701fcf91b57f6d4c00a0c26d95c2904e736bd70c3da1bd49b949f2d60f6e9a
    excerpt_start: 565
    excerpt_end: 620
    interpretation_note: This is the separate compatibility and necessity qualification.
    source_rule_id: MURET-UD-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 446
    source_rule_end: 655
  route_assessments:
  - route_id: MURET-UD-ROUTE-01
    route_kind: CONDITIONAL_ROUTE
    positive_evidence_ids:
    - MURET-UD-ICPE-ROUTE-01
    condition_evidence_ids:
    - MURET-UD-ICPE-CONDITION-01
    difficulty_evidence_ids: []
    applicability_note: The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved.
- resolved_zone_chapter_label: UF
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0065
  - SECTION-0066
  review_note: Articles UF 1 and UF 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Article UF 2 states a possible ICPE route subject to explicit compatibility and local-necessity conditions; sector and BESS applicability remain unresolved.
  missing_information: BESS planning-use, sector and ICPE classification, application of all Article UF 1/2 provisions, prescriptions, servitudes, project effects and design.
  evidence:
  - evidence_id: MURET-UF-ICPE-ROUTE-01
    section_id: SECTION-0066
    page_number: 60
    evidence_kind: ICPE_RULE
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: Les installations classées pour la protection de l’environnement ne sont autorisées
    excerpt_sha256: e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff
    section_page_fragment_sha256: 4fceabfce9821f94b0c023052a654d1d515c86e81056605b876cfbccf54e84ec
    excerpt_start: 510
    excerpt_end: 593
    interpretation_note: This is a literal ICPE route phrase, not a BESS authorization.
    source_rule_id: MURET-UF-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 510
    source_rule_end: 719
  - evidence_id: MURET-UF-ICPE-CONDITION-01
    section_id: SECTION-0066
    page_number: 60
    evidence_kind: ICPE_RULE
    evidence_direction: CONDITION
    exact_raw_excerpt: compatibles avec le milieu environnant et nécessaires à
    excerpt_sha256: 45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928
    section_page_fragment_sha256: 4fceabfce9821f94b0c023052a654d1d515c86e81056605b876cfbccf54e84ec
    excerpt_start: 629
    excerpt_end: 684
    interpretation_note: This is the separate compatibility and necessity qualification.
    source_rule_id: MURET-UF-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 510
    source_rule_end: 719
  route_assessments:
  - route_id: MURET-UF-ROUTE-01
    route_kind: CONDITIONAL_ROUTE
    positive_evidence_ids:
    - MURET-UF-ICPE-ROUTE-01
    condition_evidence_ids:
    - MURET-UF-ICPE-CONDITION-01
    difficulty_evidence_ids: []
    applicability_note: The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved.
- resolved_zone_chapter_label: UP
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0080
  - SECTION-0081
  review_note: Articles UP 1 and UP 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Article UP 1 states a general restriction with a public or collective-interest equipment exception; whether a BESS belongs to that excepted category remains unresolved. The separate Article UP 2 ICPE rule is retained only as context because BESS ICPE applicability has not been established.
  missing_information: Formal classification as public or collective-interest equipment, BESS ICPE applicability, all Article UP 1/2 provisions, prescriptions, servitudes, project effects and design.
  evidence:
  - evidence_id: MURET-UP-PUBLIC-ROUTE-01
    section_id: SECTION-0080
    page_number: 71
    evidence_kind: PUBLIC_INTEREST_EXCEPTION
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: "à usage d'équipement public  \nou d'intérêt collectif"
    excerpt_sha256: 301da057642435982e74e393d12e292b81682d4d7672dec60e40a8e10e84530c
    section_page_fragment_sha256: 06f8ea334a2fa8ce62337d6a3c59d24e03f9d8b9d8cc9e936c92e97b771babbb
    excerpt_start: 125
    excerpt_end: 177
    interpretation_note: This is the exact category exception; the policy does not decide that a BESS belongs to it.
    source_rule_id: MURET-UP-ROUTE-RULE-01
    source_rule_excerpt: "Toutes constructions ou  installations autres que celles à usage d'équipement public  \nou d'intérêt collectif, services annexes et les logements de fonction y afférent."
    source_rule_sha256: de2615e25b83708c84e9ff9313060dca708ca0a8bc693777b627951bc2de394c
    source_rule_start: 68
    source_rule_end: 236
  - evidence_id: MURET-UP-RESTRICTION-01
    section_id: SECTION-0080
    page_number: 71
    evidence_kind: USE_RESTRICTION
    evidence_direction: SUPPORTS_DIFFICULTY
    exact_raw_excerpt: Toutes constructions ou  installations autres que celles
    excerpt_sha256: edfbe54799b8a6c0e74d86b0e9596e8c68471f11105783b3e4e93825f8308462
    section_page_fragment_sha256: 06f8ea334a2fa8ce62337d6a3c59d24e03f9d8b9d8cc9e936c92e97b771babbb
    excerpt_start: 68
    excerpt_end: 124
    interpretation_note: This is the general restriction surrounding the public or collective-interest exception; it does not decide whether a BESS belongs to the exception.
    source_rule_id: MURET-UP-ROUTE-RULE-01
    source_rule_excerpt: "Toutes constructions ou  installations autres que celles à usage d'équipement public  \nou d'intérêt collectif, services annexes et les logements de fonction y afférent."
    source_rule_sha256: de2615e25b83708c84e9ff9313060dca708ca0a8bc693777b627951bc2de394c
    source_rule_start: 68
    source_rule_end: 236
  - evidence_id: MURET-UP-ICPE-CONDITION-01
    section_id: SECTION-0081
    page_number: 71
    evidence_kind: ICPE_RULE
    evidence_direction: CONTEXT_ONLY
    exact_raw_excerpt: compatibles avec le milieu environnant et nécessaires à
    excerpt_sha256: 45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928
    section_page_fragment_sha256: 7a5fac0b06f32a02a34031e9db62b2ccd59a63099fdb378079ab41c4252aed09
    excerpt_start: 478
    excerpt_end: 533
    interpretation_note: This separate ICPE condition is context only unless a future evidence step establishes that the BESS project is subject to it.
    source_rule_id: MURET-UP-CONDITION-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 359
    source_rule_end: 568
  route_assessments:
  - route_id: MURET-UP-ROUTE-01
    route_kind: RESTRICTION_EXCEPTION_ROUTE
    positive_evidence_ids:
    - MURET-UP-PUBLIC-ROUTE-01
    condition_evidence_ids: []
    difficulty_evidence_ids:
    - MURET-UP-RESTRICTION-01
    applicability_note: The Article UP 1 restriction and its public or collective-interest exception are assessed as one coherent route; BESS membership remains unresolved. The separate ICPE rule is not used to qualify this route.
- resolved_zone_chapter_label: AU
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0095
  - SECTION-0096
  review_note: Articles AU 1 and AU 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Infrastructure prerequisites were not treated as a route; Article AU 2 separately states a possible ICPE route with compatibility and necessity conditions.
  missing_information: BESS planning-use and ICPE classification, infrastructure and sector conditions, all Article AU 1/2 provisions, prescriptions, servitudes, project effects and design.
  evidence:
  - evidence_id: MURET-AU-ICPE-ROUTE-01
    section_id: SECTION-0096
    page_number: 81
    evidence_kind: ICPE_RULE
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: Les installations classées pour la protection de l’environnement ne sont autorisées
    excerpt_sha256: e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff
    section_page_fragment_sha256: 545168e51a47f7c8b9519575b6d870ab70e11d1043df847e3b5b8661a890652e
    excerpt_start: 1474
    excerpt_end: 1557
    interpretation_note: This is the explicit ICPE route phrase; infrastructure prerequisites alone were not used as positive evidence.
    source_rule_id: MURET-AU-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 1474
    source_rule_end: 1683
  - evidence_id: MURET-AU-ICPE-CONDITION-01
    section_id: SECTION-0096
    page_number: 81
    evidence_kind: ICPE_RULE
    evidence_direction: CONDITION
    exact_raw_excerpt: compatibles avec le milieu environnant et nécessaires à
    excerpt_sha256: 45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928
    section_page_fragment_sha256: 545168e51a47f7c8b9519575b6d870ab70e11d1043df847e3b5b8661a890652e
    excerpt_start: 1593
    excerpt_end: 1648
    interpretation_note: This is the separate compatibility and necessity qualification.
    source_rule_id: MURET-AU-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 1474
    source_rule_end: 1683
  route_assessments:
  - route_id: MURET-AU-ROUTE-01
    route_kind: CONDITIONAL_ROUTE
    positive_evidence_ids:
    - MURET-AU-ICPE-ROUTE-01
    condition_evidence_ids:
    - MURET-AU-ICPE-CONDITION-01
    difficulty_evidence_ids: []
    applicability_note: The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved.
- resolved_zone_chapter_label: AUp
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0110
  - SECTION-0111
  review_note: Articles AUp 1 and AUp 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Article AUp 1 states a public or collective-interest equipment exception under Article AUp 2 conditions. Article AUp 2 requires indispensable access, road and network infrastructure before authorization. Its separate ICPE rule is retained only as context because BESS ICPE applicability has not been established.
  missing_information: Formal BESS classification as public or collective-interest equipment, satisfaction of the Article AUp 2 infrastructure prerequisite, BESS ICPE applicability, all Article AUp 1/2 provisions, prescriptions, servitudes, project effects and design.
  evidence:
  - evidence_id: MURET-AUP-PUBLIC-ROUTE-01
    section_id: SECTION-0110
    page_number: 93
    evidence_kind: PUBLIC_INTEREST_EXCEPTION
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: "à usage d'équipement public ou \nd'intérêt collectif"
    excerpt_sha256: f7be71b131f97c74c8107bc6f14bf2a980d8c3f769a52eef7a899249108c35a2
    section_page_fragment_sha256: 4f5b79666858745347ec811398acd19d2761705b3b3d2a31ffd9f4c54a5c93d5
    excerpt_start: 125
    excerpt_end: 176
    interpretation_note: This is the exact category exception; BESS membership is unresolved.
    source_rule_id: MURET-AUp-ROUTE-RULE-01
    source_rule_excerpt: "Toutes constructions ou installations autres que celles à usage d'équipement public ou \nd'intérêt collectif, leurs services annexes et les logements de fonction y afférent  sous \nconditions de l’article AUP-2."
    source_rule_sha256: 01870b2aa63b15491cbf644501dfa8238a94f980d426d15ee2743cc5796c24c3
    source_rule_start: 69
    source_rule_end: 278
  - evidence_id: MURET-AUP-INFRASTRUCTURE-CONDITION-01
    section_id: SECTION-0111
    page_number: 93
    evidence_kind: ACCESS_OR_NETWORK_CONDITION
    evidence_direction: CONDITION
    exact_raw_excerpt: "Les constructions et opérations ne pourront être autorisées qu’après réalisation des  \néquipements d’infrastructure indispensable à leur fonctionnement (accès, voirie et  \nréseaux divers) conformément aux articles AUp3 et AUp4."
    excerpt_sha256: b2be9b1f7e3597802d5ed2c301a7e34bb7a9eecaeab55898e55306719b1b315b
    section_page_fragment_sha256: 57540d28148aefc320fcc8baa9a92df7e382d72299da6e804a3ebfaf52408b44
    excerpt_start: 98
    excerpt_end: 325
    interpretation_note: This is the general Article AUp 2 infrastructure prerequisite expressly referenced by Article AUp 1; the policy does not decide that it is satisfied.
    source_rule_id: MURET-AUp-INFRASTRUCTURE-RULE-01
    source_rule_excerpt: "Les constructions et opérations ne pourront être autorisées qu’après réalisation des  \néquipements d’infrastructure indispensable à leur fonctionnement (accès, voirie et  \nréseaux divers) conformément aux articles AUp3 et AUp4."
    source_rule_sha256: b2be9b1f7e3597802d5ed2c301a7e34bb7a9eecaeab55898e55306719b1b315b
    source_rule_start: 98
    source_rule_end: 325
  - evidence_id: MURET-AUP-ICPE-CONDITION-01
    section_id: SECTION-0111
    page_number: 93
    evidence_kind: ICPE_RULE
    evidence_direction: CONTEXT_ONLY
    exact_raw_excerpt: compatibles avec le milieu environnant et nécessaires à
    excerpt_sha256: 45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928
    section_page_fragment_sha256: 57540d28148aefc320fcc8baa9a92df7e382d72299da6e804a3ebfaf52408b44
    excerpt_start: 713
    excerpt_end: 768
    interpretation_note: This separate ICPE condition is context only unless a future evidence step establishes that the BESS project is subject to it.
    source_rule_id: MURET-AUp-CONDITION-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 594
    source_rule_end: 803
  route_assessments:
  - route_id: MURET-AUp-ROUTE-01
    route_kind: CONDITIONAL_ROUTE
    positive_evidence_ids:
    - MURET-AUP-PUBLIC-ROUTE-01
    condition_evidence_ids:
    - MURET-AUP-INFRASTRUCTURE-CONDITION-01
    difficulty_evidence_ids: []
    applicability_note: The Article AUp 1 public or collective-interest route is assessed with the general Article AUp 2 infrastructure prerequisite. BESS category membership and satisfaction remain unresolved; the separate ICPE rule does not qualify this route unless independently applicable.
- resolved_zone_chapter_label: AUf
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0125
  - SECTION-0126
  review_note: Articles AUf 1 and AUf 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Infrastructure prerequisites were not treated as route evidence; Article AUf 2 separately states a possible ICPE route with compatibility and necessity conditions.
  missing_information: BESS planning-use, sector and ICPE classification, infrastructure and orientation requirements, all Article AUf 1/2 provisions, prescriptions and project design.
  evidence:
  - evidence_id: MURET-AUF-ICPE-ROUTE-01
    section_id: SECTION-0126
    page_number: 102
    evidence_kind: ICPE_RULE
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: Les installations classées pour la protection de l’environnement ne sont autorisées
    excerpt_sha256: e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff
    section_page_fragment_sha256: ef0d2718332307afa871176c64cb8627900702dbd583819fb765adb2d1902769
    excerpt_start: 1435
    excerpt_end: 1518
    interpretation_note: This is the explicit ICPE route phrase; infrastructure prerequisites alone were not used as positive evidence.
    source_rule_id: MURET-AUf-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 1435
    source_rule_end: 1644
  - evidence_id: MURET-AUF-ICPE-CONDITION-01
    section_id: SECTION-0126
    page_number: 102
    evidence_kind: ICPE_RULE
    evidence_direction: CONDITION
    exact_raw_excerpt: compatibles avec le milieu environnant et nécessaires à
    excerpt_sha256: 45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928
    section_page_fragment_sha256: ef0d2718332307afa871176c64cb8627900702dbd583819fb765adb2d1902769
    excerpt_start: 1554
    excerpt_end: 1609
    interpretation_note: This is the separate compatibility and necessity qualification.
    source_rule_id: MURET-AUf-ICPE-RULE-01
    source_rule_excerpt: "Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."
    source_rule_sha256: 890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716
    source_rule_start: 1435
    source_rule_end: 1644
  route_assessments:
  - route_id: MURET-AUf-ROUTE-01
    route_kind: CONDITIONAL_ROUTE
    positive_evidence_ids:
    - MURET-AUF-ICPE-ROUTE-01
    condition_evidence_ids:
    - MURET-AUF-ICPE-CONDITION-01
    difficulty_evidence_ids: []
    applicability_note: The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved.
- resolved_zone_chapter_label: AU0
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0140
  - SECTION-0141
  review_note: Articles AU0 1 and AU0 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Article AU0 1 identifies an exception for collective-interest networks and public infrastructure, while Article AU0 2 states a separate PLU-modification prerequisite for new construction or operations.
  missing_information: Formal BESS classification within the stated infrastructure exception, applicability of the modification prerequisite, all Article AU0 1/2 provisions, prescriptions and project design.
  evidence:
  - evidence_id: MURET-AU0-INFRA-ROUTE-01
    section_id: SECTION-0140
    page_number: 114
    evidence_kind: TECHNICAL_EQUIPMENT_RULE
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: "installations nécessaires aux réseaux \nd’intérêt collectif, aux ouvrages publics d’infrastructures"
    excerpt_sha256: 886aaceafb2a40e73e3ebe145b3a58b6a22b239a8ce5fcc3740cb99d7d6298a0
    section_page_fragment_sha256: 2f4cf931c76c5a5a29aa69d67b7986b092aff39ea13e4b302513177e5fef6619
    excerpt_start: 119
    excerpt_end: 217
    interpretation_note: This is an exact infrastructure exception; BESS qualification is unresolved.
    source_rule_id: MURET-AU0-ROUTE-RULE-01
    source_rule_excerpt: "Sont interdites toutes les constructions autres que les installations nécessaires aux réseaux \nd’intérêt collectif, aux ouvrages publics d’infrastructures, et les extensions définies à \nl’article AU0 – 2."
    source_rule_sha256: fa20142522483be8183df1a43e069fcb350b1de83347bdfdd733f7871bcf207d
    source_rule_start: 63
    source_rule_end: 267
  - evidence_id: MURET-AU0-MODIFICATION-CONDITION-01
    section_id: SECTION-0141
    page_number: 114
    evidence_kind: OTHER_RELEVANT_RULE
    evidence_direction: CONDITION
    exact_raw_excerpt: "Les constructions et opérations nouvelles ne pourront être autorisées qu’après la \nmise en œuvre d’une procédure de modification du PLU"
    excerpt_sha256: 01594e632fb064a7e4dd408e68c156b66711abe6ae2a0e470c779e94b91f3a48
    section_page_fragment_sha256: a239cf9eff040ca9c9ab608cf040e3c739d5111c877aa68ad1773d3adadf24a5
    excerpt_start: 99
    excerpt_end: 234
    interpretation_note: This prerequisite is a condition only and is not treated as evidence that a BESS route exists.
    source_rule_id: MURET-AU0-CONDITION-RULE-01
    source_rule_excerpt: "Les constructions et opérations nouvelles ne pourront être autorisées qu’après la \nmise en œuvre d’une procédure de modification du PLU."
    source_rule_sha256: 2d9633774f414a8ad2f8e42bfcbb2507b677906ca6aca480f0239cec007942e3
    source_rule_start: 99
    source_rule_end: 235
  route_assessments:
  - route_id: MURET-AU0-ROUTE-01
    route_kind: CONDITIONAL_ROUTE
    positive_evidence_ids:
    - MURET-AU0-INFRA-ROUTE-01
    condition_evidence_ids:
    - MURET-AU0-MODIFICATION-CONDITION-01
    difficulty_evidence_ids: []
    applicability_note: The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved.
- resolved_zone_chapter_label: AUf0
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0155
  - SECTION-0156
  review_note: Articles AUf0 1 and AUf0 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Article AUf0 1 identifies an exception for collective-interest networks and public infrastructure, while Article AUf0 2 states a separate PLU-modification prerequisite.
  missing_information: Formal BESS classification within the infrastructure exception, applicability of the modification prerequisite, all Article AUf0 1/2 provisions, prescriptions and project design.
  evidence:
  - evidence_id: MURET-AUF0-INFRA-ROUTE-01
    section_id: SECTION-0155
    page_number: 120
    evidence_kind: TECHNICAL_EQUIPMENT_RULE
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: "installations nécessaires aux réseaux \nd’intérêt collectif, aux ouvrages publics d’infrastructures"
    excerpt_sha256: 886aaceafb2a40e73e3ebe145b3a58b6a22b239a8ce5fcc3740cb99d7d6298a0
    section_page_fragment_sha256: a23b2c0f7e48711758012d3b176967139a3b87d230c3dea312987693de86c369
    excerpt_start: 120
    excerpt_end: 218
    interpretation_note: This is an exact infrastructure exception; BESS qualification is unresolved.
    source_rule_id: MURET-AUf0-ROUTE-RULE-01
    source_rule_excerpt: "Sont interdites toutes les constructions autres que les installations nécessaires aux réseaux \nd’intérêt collectif, aux ouvrages publics d’infrastructures, et les extensions définies à \nl’article AUf0 – 2."
    source_rule_sha256: 5f4af2e2ece550ccc1bcb39eb7436f7dba04f5f21c0346b7d780bf350b77183c
    source_rule_start: 64
    source_rule_end: 269
  - evidence_id: MURET-AUF0-MODIFICATION-CONDITION-01
    section_id: SECTION-0156
    page_number: 120
    evidence_kind: OTHER_RELEVANT_RULE
    evidence_direction: CONDITION
    exact_raw_excerpt: "Les constructions et opérations nouvelles ne pourront être autorisées qu’après la \nmise en œuvre d’une procédure de modification du PLU"
    excerpt_sha256: 01594e632fb064a7e4dd408e68c156b66711abe6ae2a0e470c779e94b91f3a48
    section_page_fragment_sha256: 15040ad2f1b4a5fd1c44bdfead25d12cf4ccdd53a5f28736e4c383ae19a6cac9
    excerpt_start: 100
    excerpt_end: 235
    interpretation_note: This prerequisite is a condition only and is not treated as route evidence.
    source_rule_id: MURET-AUf0-CONDITION-RULE-01
    source_rule_excerpt: "Les constructions et opérations nouvelles ne pourront être autorisées qu’après la \nmise en œuvre d’une procédure de modification du PLU."
    source_rule_sha256: 2d9633774f414a8ad2f8e42bfcbb2507b677906ca6aca480f0239cec007942e3
    source_rule_start: 100
    source_rule_end: 236
  route_assessments:
  - route_id: MURET-AUf0-ROUTE-01
    route_kind: CONDITIONAL_ROUTE
    positive_evidence_ids:
    - MURET-AUF0-INFRA-ROUTE-01
    condition_evidence_ids:
    - MURET-AUF0-MODIFICATION-CONDITION-01
    difficulty_evidence_ids: []
    applicability_note: The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved.
- resolved_zone_chapter_label: A
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0170
  - SECTION-0171
  review_note: Articles A 1 and A 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Article A 1 contains broad restrictive language and a separate exception for necessary technical and infrastructure works. The policy records the conflict without deciding BESS qualification.
  missing_information: Formal necessity and BESS infrastructure classification, agricultural-zone effects, all Article A 1/2 provisions, prescriptions, servitudes and project design.
  evidence:
  - evidence_id: MURET-A-RESTRICTION-01
    section_id: SECTION-0170
    page_number: 125
    evidence_kind: USE_RESTRICTION
    evidence_direction: SUPPORTS_DIFFICULTY
    exact_raw_excerpt: Sont interdites toutes les occupations et utilisations du sol autres que celles
    excerpt_sha256: f18eba9dd56f410853fb685d30b6fcc78ee95359c6577387b78a29c3261b3c61
    section_page_fragment_sha256: 51342e0ae335504d0f750e0138a63c2ffe928e11e564872122bec65edb4a8e13
    excerpt_start: 67
    excerpt_end: 146
    interpretation_note: This is the broad restriction phrase, separate from the exception.
    source_rule_id: MURET-A-RESTRICTION-EXCEPTION-RULE-01
    source_rule_excerpt: "Sont interdites toutes les occupations et utilisations du sol autres que celles : \n- nécessaires à l’exploitation agricole, qu’il s’agisse des constructions et extensions \nà usage d’habitation ou des constructions et installations à usage agricole, \n- nécessaires au bon fonctionnement des systèmes de gestion des eaux, \n- nécessaires aux ouvrages techniques et d’infrastructures, \n- mentionnées à l’article A2"
    source_rule_sha256: 4a0a23edf39f707575293cb759d13f6bf2081db5df58ff1e9bed08c98775b1b9
    source_rule_start: 67
    source_rule_end: 477
  - evidence_id: MURET-A-INFRA-ROUTE-01
    section_id: SECTION-0170
    page_number: 125
    evidence_kind: TECHNICAL_EQUIPMENT_RULE
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: nécessaires aux ouvrages techniques et d’infrastructures
    excerpt_sha256: 7eee9f7e595784b2d6a4b605a4f0b5703a0446acb77b7420c709b5516e30e0a2
    section_page_fragment_sha256: 51342e0ae335504d0f750e0138a63c2ffe928e11e564872122bec65edb4a8e13
    excerpt_start: 390
    excerpt_end: 446
    interpretation_note: This is the separate technical-infrastructure exception; BESS necessity and classification are unresolved.
    source_rule_id: MURET-A-RESTRICTION-EXCEPTION-RULE-01
    source_rule_excerpt: "Sont interdites toutes les occupations et utilisations du sol autres que celles : \n- nécessaires à l’exploitation agricole, qu’il s’agisse des constructions et extensions \nà usage d’habitation ou des constructions et installations à usage agricole, \n- nécessaires au bon fonctionnement des systèmes de gestion des eaux, \n- nécessaires aux ouvrages techniques et d’infrastructures, \n- mentionnées à l’article A2"
    source_rule_sha256: 4a0a23edf39f707575293cb759d13f6bf2081db5df58ff1e9bed08c98775b1b9
    source_rule_start: 67
    source_rule_end: 477
  route_assessments:
  - route_id: MURET-A-ROUTE-01
    route_kind: RESTRICTION_EXCEPTION_ROUTE
    positive_evidence_ids:
    - MURET-A-INFRA-ROUTE-01
    condition_evidence_ids: []
    difficulty_evidence_ids:
    - MURET-A-RESTRICTION-01
    applicability_note: The restriction and its listed exception are assessed as one coherent route; BESS applicability remains unresolved.
- resolved_zone_chapter_label: N
  review_completeness: COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES
  reviewed_section_ids:
  - SECTION-0184
  - SECTION-0185
  review_note: Articles N 1 and N 2 were reviewed in full for written use controls.
  zoning_precheck_status: CONDITIONAL_REVIEW
  zoning_precheck_confidence: LOW
  rationale: Article N 1 contains a broad restriction and a separate exception for necessary technical and infrastructure equipment. The policy records the conflict without deciding BESS qualification.
  missing_information: Formal necessity and BESS infrastructure classification, natural-zone effects, all Article N 1/2 provisions, prescriptions, servitudes and project design.
  evidence:
  - evidence_id: MURET-N-RESTRICTION-01
    section_id: SECTION-0184
    page_number: 135
    evidence_kind: USE_RESTRICTION
    evidence_direction: SUPPORTS_DIFFICULTY
    exact_raw_excerpt: Sont interdites, toutes les occupations et utilisations du sol, à l’exception
    excerpt_sha256: 4781673bc1d5c704acd3be46c706805f6eaebacd4fc4b2296877af8bce6688ef
    section_page_fragment_sha256: 0cac3a1aeb56859670b715c17e1c166959147a0f90a19a12f87e0025b263e195
    excerpt_start: 69
    excerpt_end: 146
    interpretation_note: This is the broad restriction phrase, separate from its listed exceptions.
    source_rule_id: MURET-N-RESTRICTION-EXCEPTION-RULE-01
    source_rule_excerpt: "Sont interdites, toutes les occupations et utilisations du sol, à l’exception : \n \n- des occupations et utilisations du sol soumises à des conditions particulières et \nrépertoriées à l’article N 2, \n- des équipements nécessaires aux ouvrages techniques et d’infrastructure, \n- des aménagements liés aux ouvrages techniques nécessaires au fonctionnement des \nservices publics, \n- des équipements nécessaires au bon fonctionnement des systèmes de gestion des \neaux, \n- en secteur NL : \n- les constructions, installations et utilisations du sol destinées à l’accueil des \nactivités de loisirs et d’équipements publics sportifs ou socio-culturels, \n- les terrains de camping et de caravaning, excepté dans le secteur inondable \nrepéré au plan de zonage."
    source_rule_sha256: c434670531b43bbc23dd24c1fa01bba1eedaee0ba9e241b9f432255c74db30d2
    source_rule_start: 69
    source_rule_end: 818
  - evidence_id: MURET-N-INFRA-ROUTE-01
    section_id: SECTION-0184
    page_number: 135
    evidence_kind: TECHNICAL_EQUIPMENT_RULE
    evidence_direction: SUPPORTS_POTENTIAL_COMPATIBILITY
    exact_raw_excerpt: des équipements nécessaires aux ouvrages techniques et d’infrastructure
    excerpt_sha256: b28cb339936e8598faee5c5bba6f1be5f52e40b1ce6f33fe854ae1daff54d867
    section_page_fragment_sha256: 0cac3a1aeb56859670b715c17e1c166959147a0f90a19a12f87e0025b263e195
    excerpt_start: 270
    excerpt_end: 341
    interpretation_note: This is the separate technical-infrastructure exception; BESS necessity and classification are unresolved.
    source_rule_id: MURET-N-RESTRICTION-EXCEPTION-RULE-01
    source_rule_excerpt: "Sont interdites, toutes les occupations et utilisations du sol, à l’exception : \n \n- des occupations et utilisations du sol soumises à des conditions particulières et \nrépertoriées à l’article N 2, \n- des équipements nécessaires aux ouvrages techniques et d’infrastructure, \n- des aménagements liés aux ouvrages techniques nécessaires au fonctionnement des \nservices publics, \n- des équipements nécessaires au bon fonctionnement des systèmes de gestion des \neaux, \n- en secteur NL : \n- les constructions, installations et utilisations du sol destinées à l’accueil des \nactivités de loisirs et d’équipements publics sportifs ou socio-culturels, \n- les terrains de camping et de caravaning, excepté dans le secteur inondable \nrepéré au plan de zonage."
    source_rule_sha256: c434670531b43bbc23dd24c1fa01bba1eedaee0ba9e241b9f432255c74db30d2
    source_rule_start: 69
    source_rule_end: 818
  route_assessments:
  - route_id: MURET-N-ROUTE-01
    route_kind: RESTRICTION_EXCEPTION_ROUTE
    positive_evidence_ids:
    - MURET-N-INFRA-ROUTE-01
    condition_evidence_ids: []
    difficulty_evidence_ids:
    - MURET-N-RESTRICTION-01
    applicability_note: The restriction and its listed exception are assessed as one coherent route; BESS applicability remains unresolved.
```

### Authoritative raw-byte payload

This payload is explicitly the **historical checkout basis**: 47,039 bytes, SHA256 `879d50627c063bb10096950d004cf4d4e446ff04ef9a1178b3e3fb28e2ffdae3`. RFC 4648 Base64 wrapping is display-only; decode the concatenation to recover 655 CRLF and 68 lone LF, with final CRLF. It is not the Git-content SHA basis in File identity. The readable fence above independently binds exact Git bytes, SHA256 `c736ea8901997f4852fd1f72a3f6f34282452f18dcd9abc0ccbce8255adaad45`.

```text
c2NoZW1hX3ZlcnNpb246IDUKcG9saWN5X3Byb2ZpbGU6IG11cmV0X2Jlc3Nfd3JpdHRlbl96b25p
bmdfdjYKcGxhbm5pbmdfcHJlY2hlY2tfc2NvcGU6IFdSSVRURU5fWk9OSU5HX1JFR1VMQVRJT05f
T05MWQpyZXZpZXdfc2NvcGU6IENPTkZJR1VSRURfVVNFX0NPTlRST0xfQVJUSUNMRVNfT05MWQpz
b3VyY2VfbG9jazoKICBkb2N1bWVudF9pZDogMzNlZGI0YzlmNjk0M2M4OGQ4ZDkyNTE4YmZmMjBi
ZWMNCiAgYXJjaGl2ZV9zaGEyNTY6IDlkNjY3N2NkNjYzNGI1NmI3MTIzMTEwNDJmMGNjNzE0ZDVj
YTQyYTM4ZjgyYTQxN2IyN2RkNDczMjU1ZDdkOTMNCiAgcGRmX3NoYTI1NjogNTM1OGViYWQ2YjBj
ZGE2ZGU2ODFiYTM1MzZlMjliOGI2MjkxZmI3MDFjN2QzNzExZjRlZTFkNmZkYjg1YzZmYg0KICBp
bmRleF9jb250ZW50X3NoYTI1NjogNmEwMDA5MjI4Y2ExNzEyOGMwYThiYjMyOWQ5YzIyNzdhMWI2
NjM4NzA4YTY3YjkxM2I3MmVlOTMwNjNlNDJjZA0KICBzdHJ1Y3R1cmVfcmVzdWx0X2NvbnRlbnRf
c2hhMjU2OiAxNmY4YTllZGZmZjBkMzMwZjY5NTc5MzEwZGEwODVmODA0ZjQ2NDFkZTk3M2Q5OGUw
MDQ2YmZmNWVhOTZiMDNjDQogIHN0cnVjdHVyZV9wcm9maWxlOiBtdXJldF9wbHVfMjAyNDAyMTVf
djENCnJlcXVpcmVkX3pvbmVfYXJ0aWNsZV9udW1iZXJzOg0KLSAnMScNCi0gJzInDQpjaGFwdGVy
czoNCi0gcmVzb2x2ZWRfem9uZV9jaGFwdGVyX2xhYmVsOiBVQQ0KICByZXZpZXdfY29tcGxldGVu
ZXNzOiBDT01QTEVURV9GT1JfQ09ORklHVVJFRF9VU0VfQ09OVFJPTF9BUlRJQ0xFUw0KICByZXZp
ZXdlZF9zZWN0aW9uX2lkczoNCiAgLSBTRUNUSU9OLTAwMDgNCiAgLSBTRUNUSU9OLTAwMDkNCiAg
cmV2aWV3X25vdGU6IEFydGljbGVzIFVBIDEgYW5kIFVBIDIgd2VyZSByZXZpZXdlZCBpbiBmdWxs
IGZvciB3cml0dGVuIHVzZSBjb250cm9scy4NCiAgem9uaW5nX3ByZWNoZWNrX3N0YXR1czogQ09O
RElUSU9OQUxfUkVWSUVXDQogIHpvbmluZ19wcmVjaGVja19jb25maWRlbmNlOiBMT1cNCiAgcmF0
aW9uYWxlOiBBcnRpY2xlIFVBIDIgc3RhdGVzIGEgcG9zc2libGUgSUNQRSByb3V0ZSBhbmQgc3Rh
dGVzIHNlcGFyYXRlIGNvbXBhdGliaWxpdHkgYW5kIGxvY2FsLW5lY2Vzc2l0eSBjb25kaXRpb25z
OyB3aGV0aGVyIGEgQkVTUyBxdWFsaWZpZXMgcmVtYWlucyB1bnJlc29sdmVkLg0KICBtaXNzaW5n
X2luZm9ybWF0aW9uOiBCRVNTIHBsYW5uaW5nLXVzZSBhbmQgSUNQRSBjbGFzc2lmaWNhdGlvbiwg
YXBwbGljYXRpb24gb2YgYWxsIEFydGljbGUgVUEgMS8yIHByb3Zpc2lvbnMsIHByZXNjcmlwdGlv
bnMsIHNlcnZpdHVkZXMsIHByb2plY3QgZWZmZWN0cyBhbmQgZGVzaWduLg0KICBldmlkZW5jZToN
CiAgLSBldmlkZW5jZV9pZDogTVVSRVQtVUEtSUNQRS1ST1VURS0wMQ0KICAgIHNlY3Rpb25faWQ6
IFNFQ1RJT04tMDAwOQ0KICAgIHBhZ2VfbnVtYmVyOiA4DQogICAgZXZpZGVuY2Vfa2luZDogSUNQ
RV9SVUxFDQogICAgZXZpZGVuY2VfZGlyZWN0aW9uOiBTVVBQT1JUU19QT1RFTlRJQUxfQ09NUEFU
SUJJTElUWQ0KICAgIGV4YWN0X3Jhd19leGNlcnB0OiBMZXMgaW5zdGFsbGF0aW9ucyBjbGFzc8Op
ZXMgcG91ciBsYSBwcm90ZWN0aW9uIGRlIGzigJllbnZpcm9ubmVtZW50IG5lIHNvbnQgYXV0b3Jp
c8OpZXMNCiAgICBleGNlcnB0X3NoYTI1NjogZTFjNzY3YmNmMDVlNmUzODc5ZmRhOTM0YWZjMzk2
YjU1ZWNiOGNiMzBiOWJlOWQwZTA5MGM4YmE4NjBlMTNmZg0KICAgIHNlY3Rpb25fcGFnZV9mcmFn
bWVudF9zaGEyNTY6IDJkYThkMTVmYWQwOTZhNjk0ZDdiNTZlY2ZjMWQ2MWQwYmEzNzVhYWMxYzI1
NDc5NGQ2MzM4ODUyNGNjNzU1ZjYNCiAgICBleGNlcnB0X3N0YXJ0OiAxMDANCiAgICBleGNlcnB0
X2VuZDogMTgzDQogICAgaW50ZXJwcmV0YXRpb25fbm90ZTogVGhpcyBpcyBhIGxpdGVyYWwgSUNQ
RSByb3V0ZSBwaHJhc2U7IGl0IGRvZXMgbm90IGVzdGFibGlzaCB0aGF0IGEgQkVTUyBpcyBhbiBh
cHBsaWNhYmxlIElDUEUgdXNlLg0KICAgIHNvdXJjZV9ydWxlX2lkOiBNVVJFVC1VQS1JQ1BFLVJV
TEUtMDENCiAgICBzb3VyY2VfcnVsZV9leGNlcnB0OiAiTGVzIGluc3RhbGxhdGlvbnMgY2xhc3PD
qWVzIHBvdXIgbGEgcHJvdGVjdGlvbiBkZSBs4oCZZW52aXJvbm5lbWVudCBuZSBzb250IGF1dG9y
aXPDqWVzIHF14oCZw6AgXG5sYSBjb25kaXRpb24gZOKAmcOqdHJlIGNvbXBhdGlibGVzIGF2ZWMg
bGUgbWlsaWV1IGVudmlyb25uYW50IGV0IG7DqWNlc3NhaXJlcyDDoCBsYSB2aWUgIGR1IFxucXVh
cnRpZXIgZXQgZGUgbGEgY2l0w6kuIg0KICAgIHNvdXJjZV9ydWxlX3NoYTI1NjogOGRlZjU5ZTg2
MGQ0MzRlNDgyODk5ZTk3MDk1MjBkMjIxZGQ1NzZlNDFlMDBmMjc2YmJlOWM4N2U1MTI3YThkZg0K
ICAgIHNvdXJjZV9ydWxlX3N0YXJ0OiAxMDANCiAgICBzb3VyY2VfcnVsZV9lbmQ6IDMwMQ0KICAt
IGV2aWRlbmNlX2lkOiBNVVJFVC1VQS1JQ1BFLUNPTkRJVElPTi0wMQ0KICAgIHNlY3Rpb25faWQ6
IFNFQ1RJT04tMDAwOQ0KICAgIHBhZ2VfbnVtYmVyOiA4DQogICAgZXZpZGVuY2Vfa2luZDogSUNQ
RV9SVUxFDQogICAgZXZpZGVuY2VfZGlyZWN0aW9uOiBDT05ESVRJT04NCiAgICBleGFjdF9yYXdf
ZXhjZXJwdDogY29tcGF0aWJsZXMgYXZlYyBsZSBtaWxpZXUgZW52aXJvbm5hbnQgZXQgbsOpY2Vz
c2FpcmVzIMOgDQogICAgZXhjZXJwdF9zaGEyNTY6IDQ1ZTdjODIyOTYzYWViNTkzMWIwMDM5MmY2
MDVlNDVmNzQ1ZGU0N2MwODRkMDQ0OTBiZmY2YmIxNWY0NmE5MjgNCiAgICBzZWN0aW9uX3BhZ2Vf
ZnJhZ21lbnRfc2hhMjU2OiAyZGE4ZDE1ZmFkMDk2YTY5NGQ3YjU2ZWNmYzFkNjFkMGJhMzc1YWFj
MWMyNTQ3OTRkNjMzODg1MjRjYzc1NWY2DQogICAgZXhjZXJwdF9zdGFydDogMjEwDQogICAgZXhj
ZXJwdF9lbmQ6IDI2NQ0KICAgIGludGVycHJldGF0aW9uX25vdGU6IFRoaXMgaXMgdGhlIHNlcGFy
YXRlIGNvbXBhdGliaWxpdHkgYW5kIG5lY2Vzc2l0eSBxdWFsaWZpY2F0aW9uIGF0dGFjaGVkIHRv
IHRoZSBJQ1BFIHJvdXRlLg0KICAgIHNvdXJjZV9ydWxlX2lkOiBNVVJFVC1VQS1JQ1BFLVJVTEUt
MDENCiAgICBzb3VyY2VfcnVsZV9leGNlcnB0OiAiTGVzIGluc3RhbGxhdGlvbnMgY2xhc3PDqWVz
IHBvdXIgbGEgcHJvdGVjdGlvbiBkZSBs4oCZZW52aXJvbm5lbWVudCBuZSBzb250IGF1dG9yaXPD
qWVzIHF14oCZw6AgXG5sYSBjb25kaXRpb24gZOKAmcOqdHJlIGNvbXBhdGlibGVzIGF2ZWMgbGUg
bWlsaWV1IGVudmlyb25uYW50IGV0IG7DqWNlc3NhaXJlcyDDoCBsYSB2aWUgIGR1IFxucXVhcnRp
ZXIgZXQgZGUgbGEgY2l0w6kuIg0KICAgIHNvdXJjZV9ydWxlX3NoYTI1NjogOGRlZjU5ZTg2MGQ0
MzRlNDgyODk5ZTk3MDk1MjBkMjIxZGQ1NzZlNDFlMDBmMjc2YmJlOWM4N2U1MTI3YThkZg0KICAg
IHNvdXJjZV9ydWxlX3N0YXJ0OiAxMDANCiAgICBzb3VyY2VfcnVsZV9lbmQ6IDMwMQ0KICByb3V0
ZV9hc3Nlc3NtZW50czoNCiAgLSByb3V0ZV9pZDogTVVSRVQtVUEtUk9VVEUtMDENCiAgICByb3V0
ZV9raW5kOiBDT05ESVRJT05BTF9ST1VURQ0KICAgIHBvc2l0aXZlX2V2aWRlbmNlX2lkczoNCiAg
ICAtIE1VUkVULVVBLUlDUEUtUk9VVEUtMDENCiAgICBjb25kaXRpb25fZXZpZGVuY2VfaWRzOg0K
ICAgIC0gTVVSRVQtVUEtSUNQRS1DT05ESVRJT04tMDENCiAgICBkaWZmaWN1bHR5X2V2aWRlbmNl
X2lkczogW10NCiAgICBhcHBsaWNhYmlsaXR5X25vdGU6IFRoZSBjaXRlZCBwb3NpdGl2ZSBjYXRl
Z29yeSBhbmQgaXRzIGV4cGxpY2l0IHF1YWxpZmljYXRpb24gYXJlIGFzc2Vzc2VkIGFzIG9uZSBj
b2hlcmVudCByb3V0ZTsgQkVTUyBhcHBsaWNhYmlsaXR5IHJlbWFpbnMgdW5yZXNvbHZlZC4NCi0g
cmVzb2x2ZWRfem9uZV9jaGFwdGVyX2xhYmVsOiBVQg0KICByZXZpZXdfY29tcGxldGVuZXNzOiBD
T01QTEVURV9GT1JfQ09ORklHVVJFRF9VU0VfQ09OVFJPTF9BUlRJQ0xFUw0KICByZXZpZXdlZF9z
ZWN0aW9uX2lkczoNCiAgLSBTRUNUSU9OLTAwMjENCiAgLSBTRUNUSU9OLTAwMjINCiAgcmV2aWV3
X25vdGU6IEFydGljbGVzIFVCIDEgYW5kIFVCIDIgd2VyZSByZXZpZXdlZCBpbiBmdWxsIGZvciB3
cml0dGVuIHVzZSBjb250cm9scy4NCiAgem9uaW5nX3ByZWNoZWNrX3N0YXR1czogQ09ORElUSU9O
QUxfUkVWSUVXDQogIHpvbmluZ19wcmVjaGVja19jb25maWRlbmNlOiBMT1cNCiAgcmF0aW9uYWxl
OiBBcnRpY2xlIFVCIDIgc3RhdGVzIGEgcG9zc2libGUgSUNQRSByb3V0ZSBhbmQgc2VwYXJhdGUg
Y29tcGF0aWJpbGl0eSBhbmQgbG9jYWwtbmVjZXNzaXR5IGNvbmRpdGlvbnM7IEJFU1MgYXBwbGlj
YWJpbGl0eSBpcyB1bnJlc29sdmVkLg0KICBtaXNzaW5nX2luZm9ybWF0aW9uOiBCRVNTIHBsYW5u
aW5nLXVzZSBhbmQgSUNQRSBjbGFzc2lmaWNhdGlvbiwgYXBwbGljYXRpb24gb2YgYWxsIEFydGlj
bGUgVUIgMS8yIHByb3Zpc2lvbnMsIHByZXNjcmlwdGlvbnMsIHNlcnZpdHVkZXMsIHByb2plY3Qg
ZWZmZWN0cyBhbmQgZGVzaWduLg0KICBldmlkZW5jZToNCiAgLSBldmlkZW5jZV9pZDogTVVSRVQt
VUItSUNQRS1ST1VURS0wMQ0KICAgIHNlY3Rpb25faWQ6IFNFQ1RJT04tMDAyMg0KICAgIHBhZ2Vf
bnVtYmVyOiAyMg0KICAgIGV2aWRlbmNlX2tpbmQ6IElDUEVfUlVMRQ0KICAgIGV2aWRlbmNlX2Rp
cmVjdGlvbjogU1VQUE9SVFNfUE9URU5USUFMX0NPTVBBVElCSUxJVFkNCiAgICBleGFjdF9yYXdf
ZXhjZXJwdDogTGVzIGluc3RhbGxhdGlvbnMgY2xhc3PDqWVzIHBvdXIgbGEgcHJvdGVjdGlvbiBk
ZSBs4oCZZW52aXJvbm5lbWVudCBuZSBzb250IGF1dG9yaXPDqWVzDQogICAgZXhjZXJwdF9zaGEy
NTY6IGUxYzc2N2JjZjA1ZTZlMzg3OWZkYTkzNGFmYzM5NmI1NWVjYjhjYjMwYjliZTlkMGUwOTBj
OGJhODYwZTEzZmYNCiAgICBzZWN0aW9uX3BhZ2VfZnJhZ21lbnRfc2hhMjU2OiA3YzY3OGJiYzky
YzIyNzFmYmIwMmYwYzIyOGY1MWUwYjQwOGI4NjI3ODA3MzFiNzhmMzAxYjM3NzMxYTg5NGYzDQog
ICAgZXhjZXJwdF9zdGFydDogOTgNCiAgICBleGNlcnB0X2VuZDogMTgxDQogICAgaW50ZXJwcmV0
YXRpb25fbm90ZTogVGhpcyBpcyBhIGxpdGVyYWwgSUNQRSByb3V0ZSBwaHJhc2UsIG5vdCBhIEJF
U1MgYXV0aG9yaXphdGlvbi4NCiAgICBzb3VyY2VfcnVsZV9pZDogTVVSRVQtVUItSUNQRS1SVUxF
LTAxDQogICAgc291cmNlX3J1bGVfZXhjZXJwdDogIkxlcyBpbnN0YWxsYXRpb25zIGNsYXNzw6ll
cyBwb3VyIGxhIHByb3RlY3Rpb24gZGUgbOKAmWVudmlyb25uZW1lbnQgbmUgc29udCBhdXRvcmlz
w6llcyBxdeKAmcOgIFxubGEgY29uZGl0aW9uIHF1J2VsbGVzIHNvaWVudCBjb21wYXRpYmxlcyBh
dmVjIGxlIG1pbGlldSBlbnZpcm9ubmFudCBldCBuw6ljZXNzYWlyZXMgw6AgbGEgXG52aWUgZHUg
cXVhcnRpZXIgZXQgZGUgbGEgY2l0w6kuIg0KICAgIHNvdXJjZV9ydWxlX3NoYTI1NjogODkwZDJl
YWIwMWUwODg5NDhlNzhmZjk2NGJmNjhiYzA0NmQ0YmY4ODg5NGYxOWFlMjA4ODM3OTNlNWFiYjcx
Ng0KICAgIHNvdXJjZV9ydWxlX3N0YXJ0OiA5OA0KICAgIHNvdXJjZV9ydWxlX2VuZDogMzA3DQog
IC0gZXZpZGVuY2VfaWQ6IE1VUkVULVVCLUlDUEUtQ09ORElUSU9OLTAxDQogICAgc2VjdGlvbl9p
ZDogU0VDVElPTi0wMDIyDQogICAgcGFnZV9udW1iZXI6IDIyDQogICAgZXZpZGVuY2Vfa2luZDog
SUNQRV9SVUxFDQogICAgZXZpZGVuY2VfZGlyZWN0aW9uOiBDT05ESVRJT04NCiAgICBleGFjdF9y
YXdfZXhjZXJwdDogY29tcGF0aWJsZXMgYXZlYyBsZSBtaWxpZXUgZW52aXJvbm5hbnQgZXQgbsOp
Y2Vzc2FpcmVzIMOgDQogICAgZXhjZXJwdF9zaGEyNTY6IDQ1ZTdjODIyOTYzYWViNTkzMWIwMDM5
MmY2MDVlNDVmNzQ1ZGU0N2MwODRkMDQ0OTBiZmY2YmIxNWY0NmE5MjgNCiAgICBzZWN0aW9uX3Bh
Z2VfZnJhZ21lbnRfc2hhMjU2OiA3YzY3OGJiYzkyYzIyNzFmYmIwMmYwYzIyOGY1MWUwYjQwOGI4
NjI3ODA3MzFiNzhmMzAxYjM3NzMxYTg5NGYzDQogICAgZXhjZXJwdF9zdGFydDogMjE3DQogICAg
ZXhjZXJwdF9lbmQ6IDI3Mg0KICAgIGludGVycHJldGF0aW9uX25vdGU6IFRoaXMgaXMgdGhlIHNl
cGFyYXRlIGNvbXBhdGliaWxpdHkgYW5kIG5lY2Vzc2l0eSBxdWFsaWZpY2F0aW9uLg0KICAgIHNv
dXJjZV9ydWxlX2lkOiBNVVJFVC1VQi1JQ1BFLVJVTEUtMDENCiAgICBzb3VyY2VfcnVsZV9leGNl
cnB0OiAiTGVzIGluc3RhbGxhdGlvbnMgY2xhc3PDqWVzIHBvdXIgbGEgcHJvdGVjdGlvbiBkZSBs
4oCZZW52aXJvbm5lbWVudCBuZSBzb250IGF1dG9yaXPDqWVzIHF14oCZw6AgXG5sYSBjb25kaXRp
b24gcXUnZWxsZXMgc29pZW50IGNvbXBhdGlibGVzIGF2ZWMgbGUgbWlsaWV1IGVudmlyb25uYW50
IGV0IG7DqWNlc3NhaXJlcyDDoCBsYSBcbnZpZSBkdSBxdWFydGllciBldCBkZSBsYSBjaXTDqS4i
DQogICAgc291cmNlX3J1bGVfc2hhMjU2OiA4OTBkMmVhYjAxZTA4ODk0OGU3OGZmOTY0YmY2OGJj
MDQ2ZDRiZjg4ODk0ZjE5YWUyMDg4Mzc5M2U1YWJiNzE2DQogICAgc291cmNlX3J1bGVfc3RhcnQ6
IDk4DQogICAgc291cmNlX3J1bGVfZW5kOiAzMDcNCiAgcm91dGVfYXNzZXNzbWVudHM6DQogIC0g
cm91dGVfaWQ6IE1VUkVULVVCLVJPVVRFLTAxDQogICAgcm91dGVfa2luZDogQ09ORElUSU9OQUxf
Uk9VVEUNCiAgICBwb3NpdGl2ZV9ldmlkZW5jZV9pZHM6DQogICAgLSBNVVJFVC1VQi1JQ1BFLVJP
VVRFLTAxDQogICAgY29uZGl0aW9uX2V2aWRlbmNlX2lkczoNCiAgICAtIE1VUkVULVVCLUlDUEUt
Q09ORElUSU9OLTAxDQogICAgZGlmZmljdWx0eV9ldmlkZW5jZV9pZHM6IFtdDQogICAgYXBwbGlj
YWJpbGl0eV9ub3RlOiBUaGUgY2l0ZWQgcG9zaXRpdmUgY2F0ZWdvcnkgYW5kIGl0cyBleHBsaWNp
dCBxdWFsaWZpY2F0aW9uIGFyZSBhc3Nlc3NlZCBhcyBvbmUgY29oZXJlbnQgcm91dGU7IEJFU1Mg
YXBwbGljYWJpbGl0eSByZW1haW5zIHVucmVzb2x2ZWQuDQotIHJlc29sdmVkX3pvbmVfY2hhcHRl
cl9sYWJlbDogVUMNCiAgcmV2aWV3X2NvbXBsZXRlbmVzczogQ09NUExFVEVfRk9SX0NPTkZJR1VS
RURfVVNFX0NPTlRST0xfQVJUSUNMRVMNCiAgcmV2aWV3ZWRfc2VjdGlvbl9pZHM6DQogIC0gU0VD
VElPTi0wMDM2DQogIC0gU0VDVElPTi0wMDM3DQogIHJldmlld19ub3RlOiBBcnRpY2xlcyBVQyAx
IGFuZCBVQyAyIHdlcmUgcmV2aWV3ZWQgaW4gZnVsbCBmb3Igd3JpdHRlbiB1c2UgY29udHJvbHMu
DQogIHpvbmluZ19wcmVjaGVja19zdGF0dXM6IENPTkRJVElPTkFMX1JFVklFVw0KICB6b25pbmdf
cHJlY2hlY2tfY29uZmlkZW5jZTogTE9XDQogIHJhdGlvbmFsZTogQXJ0aWNsZSBVQyAyIHN0YXRl
cyBhIHBvc3NpYmxlIElDUEUgcm91dGUgc3ViamVjdCB0byBleHBsaWNpdCBjb21wYXRpYmlsaXR5
IGFuZCBsb2NhbC1uZWNlc3NpdHkgY29uZGl0aW9uczsgQkVTUyBhcHBsaWNhYmlsaXR5IGlzIHVu
cmVzb2x2ZWQuDQogIG1pc3NpbmdfaW5mb3JtYXRpb246IEJFU1MgcGxhbm5pbmctdXNlIGFuZCBJ
Q1BFIGNsYXNzaWZpY2F0aW9uLCBhcHBsaWNhdGlvbiBvZiBhbGwgQXJ0aWNsZSBVQyAxLzIgcHJv
dmlzaW9ucywgcHJlc2NyaXB0aW9ucywgc2Vydml0dWRlcywgcHJvamVjdCBlZmZlY3RzIGFuZCBk
ZXNpZ24uDQogIGV2aWRlbmNlOg0KICAtIGV2aWRlbmNlX2lkOiBNVVJFVC1VQy1JQ1BFLVJPVVRF
LTAxDQogICAgc2VjdGlvbl9pZDogU0VDVElPTi0wMDM3DQogICAgcGFnZV9udW1iZXI6IDM2DQog
ICAgZXZpZGVuY2Vfa2luZDogSUNQRV9SVUxFDQogICAgZXZpZGVuY2VfZGlyZWN0aW9uOiBTVVBQ
T1JUU19QT1RFTlRJQUxfQ09NUEFUSUJJTElUWQ0KICAgIGV4YWN0X3Jhd19leGNlcnB0OiBMZXMg
aW5zdGFsbGF0aW9ucyBjbGFzc8OpZXMgcG91ciBsYSBwcm90ZWN0aW9uIGRlIGzigJllbnZpcm9u
bmVtZW50IG5lIHNvbnQgYXV0b3Jpc8OpZXMNCiAgICBleGNlcnB0X3NoYTI1NjogZTFjNzY3YmNm
MDVlNmUzODc5ZmRhOTM0YWZjMzk2YjU1ZWNiOGNiMzBiOWJlOWQwZTA5MGM4YmE4NjBlMTNmZg0K
ICAgIHNlY3Rpb25fcGFnZV9mcmFnbWVudF9zaGEyNTY6IGY2MTAzYzQxMzlhNjVkMTJhOWI2YmY0
YzVlZGQzNzM4MmZhNmEyZmE2NDJjM2E1ODA1YWEyODk4YjExMjEzNjUNCiAgICBleGNlcnB0X3N0
YXJ0OiA5OA0KICAgIGV4Y2VycHRfZW5kOiAxODENCiAgICBpbnRlcnByZXRhdGlvbl9ub3RlOiBU
aGlzIGlzIGEgbGl0ZXJhbCBJQ1BFIHJvdXRlIHBocmFzZSwgbm90IGEgQkVTUyBhdXRob3JpemF0
aW9uLg0KICAgIHNvdXJjZV9ydWxlX2lkOiBNVVJFVC1VQy1JQ1BFLVJVTEUtMDENCiAgICBzb3Vy
Y2VfcnVsZV9leGNlcnB0OiAiTGVzIGluc3RhbGxhdGlvbnMgY2xhc3PDqWVzIHBvdXIgbGEgcHJv
dGVjdGlvbiBkZSBs4oCZZW52aXJvbm5lbWVudCBuZSBzb250IGF1dG9yaXPDqWVzIHF14oCZw6Ag
XG5sYSBjb25kaXRpb24gcXUnZWxsZXMgc29pZW50IGNvbXBhdGlibGVzIGF2ZWMgbGUgbWlsaWV1
IGVudmlyb25uYW50IGV0IG7DqWNlc3NhaXJlcyDDoCBsYSBcbnZpZSBkdSBxdWFydGllciBldCBk
ZSBsYSBjaXTDqS4iDQogICAgc291cmNlX3J1bGVfc2hhMjU2OiA4OTBkMmVhYjAxZTA4ODk0OGU3
OGZmOTY0YmY2OGJjMDQ2ZDRiZjg4ODk0ZjE5YWUyMDg4Mzc5M2U1YWJiNzE2DQogICAgc291cmNl
X3J1bGVfc3RhcnQ6IDk4DQogICAgc291cmNlX3J1bGVfZW5kOiAzMDcNCiAgLSBldmlkZW5jZV9p
ZDogTVVSRVQtVUMtSUNQRS1DT05ESVRJT04tMDENCiAgICBzZWN0aW9uX2lkOiBTRUNUSU9OLTAw
MzcNCiAgICBwYWdlX251bWJlcjogMzYNCiAgICBldmlkZW5jZV9raW5kOiBJQ1BFX1JVTEUNCiAg
ICBldmlkZW5jZV9kaXJlY3Rpb246IENPTkRJVElPTg0KICAgIGV4YWN0X3Jhd19leGNlcnB0OiBj
b21wYXRpYmxlcyBhdmVjIGxlIG1pbGlldSBlbnZpcm9ubmFudCBldCBuw6ljZXNzYWlyZXMgw6AN
CiAgICBleGNlcnB0X3NoYTI1NjogNDVlN2M4MjI5NjNhZWI1OTMxYjAwMzkyZjYwNWU0NWY3NDVk
ZTQ3YzA4NGQwNDQ5MGJmZjZiYjE1ZjQ2YTkyOA0KICAgIHNlY3Rpb25fcGFnZV9mcmFnbWVudF9z
aGEyNTY6IGY2MTAzYzQxMzlhNjVkMTJhOWI2YmY0YzVlZGQzNzM4MmZhNmEyZmE2NDJjM2E1ODA1
YWEyODk4YjExMjEzNjUNCiAgICBleGNlcnB0X3N0YXJ0OiAyMTcNCiAgICBleGNlcnB0X2VuZDog
MjcyDQogICAgaW50ZXJwcmV0YXRpb25fbm90ZTogVGhpcyBpcyB0aGUgc2VwYXJhdGUgY29tcGF0
aWJpbGl0eSBhbmQgbmVjZXNzaXR5IHF1YWxpZmljYXRpb24uDQogICAgc291cmNlX3J1bGVfaWQ6
IE1VUkVULVVDLUlDUEUtUlVMRS0wMQ0KICAgIHNvdXJjZV9ydWxlX2V4Y2VycHQ6ICJMZXMgaW5z
dGFsbGF0aW9ucyBjbGFzc8OpZXMgcG91ciBsYSBwcm90ZWN0aW9uIGRlIGzigJllbnZpcm9ubmVt
ZW50IG5lIHNvbnQgYXV0b3Jpc8OpZXMgcXXigJnDoCBcbmxhIGNvbmRpdGlvbiBxdSdlbGxlcyBz
b2llbnQgY29tcGF0aWJsZXMgYXZlYyBsZSBtaWxpZXUgZW52aXJvbm5hbnQgZXQgbsOpY2Vzc2Fp
cmVzIMOgIGxhIFxudmllIGR1IHF1YXJ0aWVyIGV0IGRlIGxhIGNpdMOpLiINCiAgICBzb3VyY2Vf
cnVsZV9zaGEyNTY6IDg5MGQyZWFiMDFlMDg4OTQ4ZTc4ZmY5NjRiZjY4YmMwNDZkNGJmODg4OTRm
MTlhZTIwODgzNzkzZTVhYmI3MTYNCiAgICBzb3VyY2VfcnVsZV9zdGFydDogOTgNCiAgICBzb3Vy
Y2VfcnVsZV9lbmQ6IDMwNw0KICByb3V0ZV9hc3Nlc3NtZW50czoNCiAgLSByb3V0ZV9pZDogTVVS
RVQtVUMtUk9VVEUtMDENCiAgICByb3V0ZV9raW5kOiBDT05ESVRJT05BTF9ST1VURQ0KICAgIHBv
c2l0aXZlX2V2aWRlbmNlX2lkczoNCiAgICAtIE1VUkVULVVDLUlDUEUtUk9VVEUtMDENCiAgICBj
b25kaXRpb25fZXZpZGVuY2VfaWRzOg0KICAgIC0gTVVSRVQtVUMtSUNQRS1DT05ESVRJT04tMDEN
CiAgICBkaWZmaWN1bHR5X2V2aWRlbmNlX2lkczogW10NCiAgICBhcHBsaWNhYmlsaXR5X25vdGU6
IFRoZSBjaXRlZCBwb3NpdGl2ZSBjYXRlZ29yeSBhbmQgaXRzIGV4cGxpY2l0IHF1YWxpZmljYXRp
b24gYXJlIGFzc2Vzc2VkIGFzIG9uZSBjb2hlcmVudCByb3V0ZTsgQkVTUyBhcHBsaWNhYmlsaXR5
IHJlbWFpbnMgdW5yZXNvbHZlZC4NCi0gcmVzb2x2ZWRfem9uZV9jaGFwdGVyX2xhYmVsOiBVRA0K
ICByZXZpZXdfY29tcGxldGVuZXNzOiBDT01QTEVURV9GT1JfQ09ORklHVVJFRF9VU0VfQ09OVFJP
TF9BUlRJQ0xFUw0KICByZXZpZXdlZF9zZWN0aW9uX2lkczoNCiAgLSBTRUNUSU9OLTAwNTENCiAg
LSBTRUNUSU9OLTAwNTINCiAgcmV2aWV3X25vdGU6IEFydGljbGVzIFVEIDEgYW5kIFVEIDIgd2Vy
ZSByZXZpZXdlZCBpbiBmdWxsIGZvciB3cml0dGVuIHVzZSBjb250cm9scy4NCiAgem9uaW5nX3By
ZWNoZWNrX3N0YXR1czogQ09ORElUSU9OQUxfUkVWSUVXDQogIHpvbmluZ19wcmVjaGVja19jb25m
aWRlbmNlOiBMT1cNCiAgcmF0aW9uYWxlOiBBcnRpY2xlIFVEIDIgc3RhdGVzIGEgcG9zc2libGUg
SUNQRSByb3V0ZSBzdWJqZWN0IHRvIGV4cGxpY2l0IGNvbXBhdGliaWxpdHkgYW5kIGxvY2FsLW5l
Y2Vzc2l0eSBjb25kaXRpb25zOyBCRVNTIGFwcGxpY2FiaWxpdHkgaXMgdW5yZXNvbHZlZC4NCiAg
bWlzc2luZ19pbmZvcm1hdGlvbjogQkVTUyBwbGFubmluZy11c2UgYW5kIElDUEUgY2xhc3NpZmlj
YXRpb24sIGFwcGxpY2F0aW9uIG9mIGFsbCBBcnRpY2xlIFVEIDEvMiBwcm92aXNpb25zLCBwcmVz
Y3JpcHRpb25zLCBzZXJ2aXR1ZGVzLCBwcm9qZWN0IGVmZmVjdHMgYW5kIGRlc2lnbi4NCiAgZXZp
ZGVuY2U6DQogIC0gZXZpZGVuY2VfaWQ6IE1VUkVULVVELUlDUEUtUk9VVEUtMDENCiAgICBzZWN0
aW9uX2lkOiBTRUNUSU9OLTAwNTINCiAgICBwYWdlX251bWJlcjogNDgNCiAgICBldmlkZW5jZV9r
aW5kOiBJQ1BFX1JVTEUNCiAgICBldmlkZW5jZV9kaXJlY3Rpb246IFNVUFBPUlRTX1BPVEVOVElB
TF9DT01QQVRJQklMSVRZDQogICAgZXhhY3RfcmF3X2V4Y2VycHQ6IExlcyBpbnN0YWxsYXRpb25z
IGNsYXNzw6llcyBwb3VyIGxhIHByb3RlY3Rpb24gZGUgbOKAmWVudmlyb25uZW1lbnQgbmUgc29u
dCBhdXRvcmlzw6llcw0KICAgIGV4Y2VycHRfc2hhMjU2OiBlMWM3NjdiY2YwNWU2ZTM4NzlmZGE5
MzRhZmMzOTZiNTVlY2I4Y2IzMGI5YmU5ZDBlMDkwYzhiYTg2MGUxM2ZmDQogICAgc2VjdGlvbl9w
YWdlX2ZyYWdtZW50X3NoYTI1NjogNjc3MDFmY2Y5MWI1N2Y2ZDRjMDBhMGMyNmQ5NWMyOTA0ZTcz
NmJkNzBjM2RhMWJkNDliOTQ5ZjJkNjBmNmU5YQ0KICAgIGV4Y2VycHRfc3RhcnQ6IDQ0Ng0KICAg
IGV4Y2VycHRfZW5kOiA1MjkNCiAgICBpbnRlcnByZXRhdGlvbl9ub3RlOiBUaGlzIGlzIGEgbGl0
ZXJhbCBJQ1BFIHJvdXRlIHBocmFzZSwgbm90IGEgQkVTUyBhdXRob3JpemF0aW9uLg0KICAgIHNv
dXJjZV9ydWxlX2lkOiBNVVJFVC1VRC1JQ1BFLVJVTEUtMDENCiAgICBzb3VyY2VfcnVsZV9leGNl
cnB0OiAiTGVzIGluc3RhbGxhdGlvbnMgY2xhc3PDqWVzIHBvdXIgbGEgcHJvdGVjdGlvbiBkZSBs
4oCZZW52aXJvbm5lbWVudCBuZSBzb250IGF1dG9yaXPDqWVzIHF14oCZw6AgXG5sYSBjb25kaXRp
b24gcXUnZWxsZXMgc29pZW50IGNvbXBhdGlibGVzIGF2ZWMgbGUgbWlsaWV1IGVudmlyb25uYW50
IGV0IG7DqWNlc3NhaXJlcyDDoCBsYSBcbnZpZSBkdSBxdWFydGllciBldCBkZSBsYSBjaXTDqS4i
DQogICAgc291cmNlX3J1bGVfc2hhMjU2OiA4OTBkMmVhYjAxZTA4ODk0OGU3OGZmOTY0YmY2OGJj
MDQ2ZDRiZjg4ODk0ZjE5YWUyMDg4Mzc5M2U1YWJiNzE2DQogICAgc291cmNlX3J1bGVfc3RhcnQ6
IDQ0Ng0KICAgIHNvdXJjZV9ydWxlX2VuZDogNjU1DQogIC0gZXZpZGVuY2VfaWQ6IE1VUkVULVVE
LUlDUEUtQ09ORElUSU9OLTAxDQogICAgc2VjdGlvbl9pZDogU0VDVElPTi0wMDUyDQogICAgcGFn
ZV9udW1iZXI6IDQ4DQogICAgZXZpZGVuY2Vfa2luZDogSUNQRV9SVUxFDQogICAgZXZpZGVuY2Vf
ZGlyZWN0aW9uOiBDT05ESVRJT04NCiAgICBleGFjdF9yYXdfZXhjZXJwdDogY29tcGF0aWJsZXMg
YXZlYyBsZSBtaWxpZXUgZW52aXJvbm5hbnQgZXQgbsOpY2Vzc2FpcmVzIMOgDQogICAgZXhjZXJw
dF9zaGEyNTY6IDQ1ZTdjODIyOTYzYWViNTkzMWIwMDM5MmY2MDVlNDVmNzQ1ZGU0N2MwODRkMDQ0
OTBiZmY2YmIxNWY0NmE5MjgNCiAgICBzZWN0aW9uX3BhZ2VfZnJhZ21lbnRfc2hhMjU2OiA2Nzcw
MWZjZjkxYjU3ZjZkNGMwMGEwYzI2ZDk1YzI5MDRlNzM2YmQ3MGMzZGExYmQ0OWI5NDlmMmQ2MGY2
ZTlhDQogICAgZXhjZXJwdF9zdGFydDogNTY1DQogICAgZXhjZXJwdF9lbmQ6IDYyMA0KICAgIGlu
dGVycHJldGF0aW9uX25vdGU6IFRoaXMgaXMgdGhlIHNlcGFyYXRlIGNvbXBhdGliaWxpdHkgYW5k
IG5lY2Vzc2l0eSBxdWFsaWZpY2F0aW9uLg0KICAgIHNvdXJjZV9ydWxlX2lkOiBNVVJFVC1VRC1J
Q1BFLVJVTEUtMDENCiAgICBzb3VyY2VfcnVsZV9leGNlcnB0OiAiTGVzIGluc3RhbGxhdGlvbnMg
Y2xhc3PDqWVzIHBvdXIgbGEgcHJvdGVjdGlvbiBkZSBs4oCZZW52aXJvbm5lbWVudCBuZSBzb250
IGF1dG9yaXPDqWVzIHF14oCZw6AgXG5sYSBjb25kaXRpb24gcXUnZWxsZXMgc29pZW50IGNvbXBh
dGlibGVzIGF2ZWMgbGUgbWlsaWV1IGVudmlyb25uYW50IGV0IG7DqWNlc3NhaXJlcyDDoCBsYSBc
bnZpZSBkdSBxdWFydGllciBldCBkZSBsYSBjaXTDqS4iDQogICAgc291cmNlX3J1bGVfc2hhMjU2
OiA4OTBkMmVhYjAxZTA4ODk0OGU3OGZmOTY0YmY2OGJjMDQ2ZDRiZjg4ODk0ZjE5YWUyMDg4Mzc5
M2U1YWJiNzE2DQogICAgc291cmNlX3J1bGVfc3RhcnQ6IDQ0Ng0KICAgIHNvdXJjZV9ydWxlX2Vu
ZDogNjU1DQogIHJvdXRlX2Fzc2Vzc21lbnRzOg0KICAtIHJvdXRlX2lkOiBNVVJFVC1VRC1ST1VU
RS0wMQ0KICAgIHJvdXRlX2tpbmQ6IENPTkRJVElPTkFMX1JPVVRFDQogICAgcG9zaXRpdmVfZXZp
ZGVuY2VfaWRzOg0KICAgIC0gTVVSRVQtVUQtSUNQRS1ST1VURS0wMQ0KICAgIGNvbmRpdGlvbl9l
dmlkZW5jZV9pZHM6DQogICAgLSBNVVJFVC1VRC1JQ1BFLUNPTkRJVElPTi0wMQ0KICAgIGRpZmZp
Y3VsdHlfZXZpZGVuY2VfaWRzOiBbXQ0KICAgIGFwcGxpY2FiaWxpdHlfbm90ZTogVGhlIGNpdGVk
IHBvc2l0aXZlIGNhdGVnb3J5IGFuZCBpdHMgZXhwbGljaXQgcXVhbGlmaWNhdGlvbiBhcmUgYXNz
ZXNzZWQgYXMgb25lIGNvaGVyZW50IHJvdXRlOyBCRVNTIGFwcGxpY2FiaWxpdHkgcmVtYWlucyB1
bnJlc29sdmVkLg0KLSByZXNvbHZlZF96b25lX2NoYXB0ZXJfbGFiZWw6IFVGDQogIHJldmlld19j
b21wbGV0ZW5lc3M6IENPTVBMRVRFX0ZPUl9DT05GSUdVUkVEX1VTRV9DT05UUk9MX0FSVElDTEVT
DQogIHJldmlld2VkX3NlY3Rpb25faWRzOg0KICAtIFNFQ1RJT04tMDA2NQ0KICAtIFNFQ1RJT04t
MDA2Ng0KICByZXZpZXdfbm90ZTogQXJ0aWNsZXMgVUYgMSBhbmQgVUYgMiB3ZXJlIHJldmlld2Vk
IGluIGZ1bGwgZm9yIHdyaXR0ZW4gdXNlIGNvbnRyb2xzLg0KICB6b25pbmdfcHJlY2hlY2tfc3Rh
dHVzOiBDT05ESVRJT05BTF9SRVZJRVcNCiAgem9uaW5nX3ByZWNoZWNrX2NvbmZpZGVuY2U6IExP
Vw0KICByYXRpb25hbGU6IEFydGljbGUgVUYgMiBzdGF0ZXMgYSBwb3NzaWJsZSBJQ1BFIHJvdXRl
IHN1YmplY3QgdG8gZXhwbGljaXQgY29tcGF0aWJpbGl0eSBhbmQgbG9jYWwtbmVjZXNzaXR5IGNv
bmRpdGlvbnM7IHNlY3RvciBhbmQgQkVTUyBhcHBsaWNhYmlsaXR5IHJlbWFpbiB1bnJlc29sdmVk
Lg0KICBtaXNzaW5nX2luZm9ybWF0aW9uOiBCRVNTIHBsYW5uaW5nLXVzZSwgc2VjdG9yIGFuZCBJ
Q1BFIGNsYXNzaWZpY2F0aW9uLCBhcHBsaWNhdGlvbiBvZiBhbGwgQXJ0aWNsZSBVRiAxLzIgcHJv
dmlzaW9ucywgcHJlc2NyaXB0aW9ucywgc2Vydml0dWRlcywgcHJvamVjdCBlZmZlY3RzIGFuZCBk
ZXNpZ24uDQogIGV2aWRlbmNlOg0KICAtIGV2aWRlbmNlX2lkOiBNVVJFVC1VRi1JQ1BFLVJPVVRF
LTAxDQogICAgc2VjdGlvbl9pZDogU0VDVElPTi0wMDY2DQogICAgcGFnZV9udW1iZXI6IDYwDQog
ICAgZXZpZGVuY2Vfa2luZDogSUNQRV9SVUxFDQogICAgZXZpZGVuY2VfZGlyZWN0aW9uOiBTVVBQ
T1JUU19QT1RFTlRJQUxfQ09NUEFUSUJJTElUWQ0KICAgIGV4YWN0X3Jhd19leGNlcnB0OiBMZXMg
aW5zdGFsbGF0aW9ucyBjbGFzc8OpZXMgcG91ciBsYSBwcm90ZWN0aW9uIGRlIGzigJllbnZpcm9u
bmVtZW50IG5lIHNvbnQgYXV0b3Jpc8OpZXMNCiAgICBleGNlcnB0X3NoYTI1NjogZTFjNzY3YmNm
MDVlNmUzODc5ZmRhOTM0YWZjMzk2YjU1ZWNiOGNiMzBiOWJlOWQwZTA5MGM4YmE4NjBlMTNmZg0K
ICAgIHNlY3Rpb25fcGFnZV9mcmFnbWVudF9zaGEyNTY6IDRmY2VhYmZjZTk4MjFmOTRiMGMwMjMw
NTJhNjU0ZDFkNTE1Yzg2ZTgxMDU2NjA1Yjg3NmNmYmNjZjU0ZTg0ZWMNCiAgICBleGNlcnB0X3N0
YXJ0OiA1MTANCiAgICBleGNlcnB0X2VuZDogNTkzDQogICAgaW50ZXJwcmV0YXRpb25fbm90ZTog
VGhpcyBpcyBhIGxpdGVyYWwgSUNQRSByb3V0ZSBwaHJhc2UsIG5vdCBhIEJFU1MgYXV0aG9yaXph
dGlvbi4NCiAgICBzb3VyY2VfcnVsZV9pZDogTVVSRVQtVUYtSUNQRS1SVUxFLTAxDQogICAgc291
cmNlX3J1bGVfZXhjZXJwdDogIkxlcyBpbnN0YWxsYXRpb25zIGNsYXNzw6llcyBwb3VyIGxhIHBy
b3RlY3Rpb24gZGUgbOKAmWVudmlyb25uZW1lbnQgbmUgc29udCBhdXRvcmlzw6llcyBxdeKAmcOg
IFxubGEgY29uZGl0aW9uIHF1J2VsbGVzIHNvaWVudCBjb21wYXRpYmxlcyBhdmVjIGxlIG1pbGll
dSBlbnZpcm9ubmFudCBldCBuw6ljZXNzYWlyZXMgw6AgbGEgXG52aWUgZHUgcXVhcnRpZXIgZXQg
ZGUgbGEgY2l0w6kuIg0KICAgIHNvdXJjZV9ydWxlX3NoYTI1NjogODkwZDJlYWIwMWUwODg5NDhl
NzhmZjk2NGJmNjhiYzA0NmQ0YmY4ODg5NGYxOWFlMjA4ODM3OTNlNWFiYjcxNg0KICAgIHNvdXJj
ZV9ydWxlX3N0YXJ0OiA1MTANCiAgICBzb3VyY2VfcnVsZV9lbmQ6IDcxOQ0KICAtIGV2aWRlbmNl
X2lkOiBNVVJFVC1VRi1JQ1BFLUNPTkRJVElPTi0wMQ0KICAgIHNlY3Rpb25faWQ6IFNFQ1RJT04t
MDA2Ng0KICAgIHBhZ2VfbnVtYmVyOiA2MA0KICAgIGV2aWRlbmNlX2tpbmQ6IElDUEVfUlVMRQ0K
ICAgIGV2aWRlbmNlX2RpcmVjdGlvbjogQ09ORElUSU9ODQogICAgZXhhY3RfcmF3X2V4Y2VycHQ6
IGNvbXBhdGlibGVzIGF2ZWMgbGUgbWlsaWV1IGVudmlyb25uYW50IGV0IG7DqWNlc3NhaXJlcyDD
oA0KICAgIGV4Y2VycHRfc2hhMjU2OiA0NWU3YzgyMjk2M2FlYjU5MzFiMDAzOTJmNjA1ZTQ1Zjc0
NWRlNDdjMDg0ZDA0NDkwYmZmNmJiMTVmNDZhOTI4DQogICAgc2VjdGlvbl9wYWdlX2ZyYWdtZW50
X3NoYTI1NjogNGZjZWFiZmNlOTgyMWY5NGIwYzAyMzA1MmE2NTRkMWQ1MTVjODZlODEwNTY2MDVi
ODc2Y2ZiY2NmNTRlODRlYw0KICAgIGV4Y2VycHRfc3RhcnQ6IDYyOQ0KICAgIGV4Y2VycHRfZW5k
OiA2ODQNCiAgICBpbnRlcnByZXRhdGlvbl9ub3RlOiBUaGlzIGlzIHRoZSBzZXBhcmF0ZSBjb21w
YXRpYmlsaXR5IGFuZCBuZWNlc3NpdHkgcXVhbGlmaWNhdGlvbi4NCiAgICBzb3VyY2VfcnVsZV9p
ZDogTVVSRVQtVUYtSUNQRS1SVUxFLTAxDQogICAgc291cmNlX3J1bGVfZXhjZXJwdDogIkxlcyBp
bnN0YWxsYXRpb25zIGNsYXNzw6llcyBwb3VyIGxhIHByb3RlY3Rpb24gZGUgbOKAmWVudmlyb25u
ZW1lbnQgbmUgc29udCBhdXRvcmlzw6llcyBxdeKAmcOgIFxubGEgY29uZGl0aW9uIHF1J2VsbGVz
IHNvaWVudCBjb21wYXRpYmxlcyBhdmVjIGxlIG1pbGlldSBlbnZpcm9ubmFudCBldCBuw6ljZXNz
YWlyZXMgw6AgbGEgXG52aWUgZHUgcXVhcnRpZXIgZXQgZGUgbGEgY2l0w6kuIg0KICAgIHNvdXJj
ZV9ydWxlX3NoYTI1NjogODkwZDJlYWIwMWUwODg5NDhlNzhmZjk2NGJmNjhiYzA0NmQ0YmY4ODg5
NGYxOWFlMjA4ODM3OTNlNWFiYjcxNg0KICAgIHNvdXJjZV9ydWxlX3N0YXJ0OiA1MTANCiAgICBz
b3VyY2VfcnVsZV9lbmQ6IDcxOQ0KICByb3V0ZV9hc3Nlc3NtZW50czoNCiAgLSByb3V0ZV9pZDog
TVVSRVQtVUYtUk9VVEUtMDENCiAgICByb3V0ZV9raW5kOiBDT05ESVRJT05BTF9ST1VURQ0KICAg
IHBvc2l0aXZlX2V2aWRlbmNlX2lkczoNCiAgICAtIE1VUkVULVVGLUlDUEUtUk9VVEUtMDENCiAg
ICBjb25kaXRpb25fZXZpZGVuY2VfaWRzOg0KICAgIC0gTVVSRVQtVUYtSUNQRS1DT05ESVRJT04t
MDENCiAgICBkaWZmaWN1bHR5X2V2aWRlbmNlX2lkczogW10NCiAgICBhcHBsaWNhYmlsaXR5X25v
dGU6IFRoZSBjaXRlZCBwb3NpdGl2ZSBjYXRlZ29yeSBhbmQgaXRzIGV4cGxpY2l0IHF1YWxpZmlj
YXRpb24gYXJlIGFzc2Vzc2VkIGFzIG9uZSBjb2hlcmVudCByb3V0ZTsgQkVTUyBhcHBsaWNhYmls
aXR5IHJlbWFpbnMgdW5yZXNvbHZlZC4NCi0gcmVzb2x2ZWRfem9uZV9jaGFwdGVyX2xhYmVsOiBV
UA0KICByZXZpZXdfY29tcGxldGVuZXNzOiBDT01QTEVURV9GT1JfQ09ORklHVVJFRF9VU0VfQ09O
VFJPTF9BUlRJQ0xFUw0KICByZXZpZXdlZF9zZWN0aW9uX2lkczoNCiAgLSBTRUNUSU9OLTAwODAN
CiAgLSBTRUNUSU9OLTAwODENCiAgcmV2aWV3X25vdGU6IEFydGljbGVzIFVQIDEgYW5kIFVQIDIg
d2VyZSByZXZpZXdlZCBpbiBmdWxsIGZvciB3cml0dGVuIHVzZSBjb250cm9scy4NCiAgem9uaW5n
X3ByZWNoZWNrX3N0YXR1czogQ09ORElUSU9OQUxfUkVWSUVXDQogIHpvbmluZ19wcmVjaGVja19j
b25maWRlbmNlOiBMT1cNCiAgcmF0aW9uYWxlOiBBcnRpY2xlIFVQIDEgc3RhdGVzIGEgZ2VuZXJh
bCByZXN0cmljdGlvbiB3aXRoIGEgcHVibGljIG9yIGNvbGxlY3RpdmUtaW50ZXJlc3QgZXF1aXBt
ZW50IGV4Y2VwdGlvbjsgd2hldGhlciBhIEJFU1MgYmVsb25ncyB0byB0aGF0IGV4Y2VwdGVkIGNh
dGVnb3J5IHJlbWFpbnMgdW5yZXNvbHZlZC4gVGhlIHNlcGFyYXRlIEFydGljbGUgVVAgMiBJQ1BF
IHJ1bGUgaXMgcmV0YWluZWQgb25seSBhcyBjb250ZXh0IGJlY2F1c2UgQkVTUyBJQ1BFIGFwcGxp
Y2FiaWxpdHkgaGFzIG5vdCBiZWVuIGVzdGFibGlzaGVkLgogIG1pc3NpbmdfaW5mb3JtYXRpb246
IEZvcm1hbCBjbGFzc2lmaWNhdGlvbiBhcyBwdWJsaWMgb3IgY29sbGVjdGl2ZS1pbnRlcmVzdCBl
cXVpcG1lbnQsIEJFU1MgSUNQRSBhcHBsaWNhYmlsaXR5LCBhbGwgQXJ0aWNsZSBVUCAxLzIgcHJv
dmlzaW9ucywgcHJlc2NyaXB0aW9ucywgc2Vydml0dWRlcywgcHJvamVjdCBlZmZlY3RzIGFuZCBk
ZXNpZ24uCiAgZXZpZGVuY2U6DQogIC0gZXZpZGVuY2VfaWQ6IE1VUkVULVVQLVBVQkxJQy1ST1VU
RS0wMQ0KICAgIHNlY3Rpb25faWQ6IFNFQ1RJT04tMDA4MA0KICAgIHBhZ2VfbnVtYmVyOiA3MQ0K
ICAgIGV2aWRlbmNlX2tpbmQ6IFBVQkxJQ19JTlRFUkVTVF9FWENFUFRJT04NCiAgICBldmlkZW5j
ZV9kaXJlY3Rpb246IFNVUFBPUlRTX1BPVEVOVElBTF9DT01QQVRJQklMSVRZDQogICAgZXhhY3Rf
cmF3X2V4Y2VycHQ6ICLDoCB1c2FnZSBkJ8OpcXVpcGVtZW50IHB1YmxpYyAgXG5vdSBkJ2ludMOp
csOqdCBjb2xsZWN0aWYiDQogICAgZXhjZXJwdF9zaGEyNTY6IDMwMWRhMDU3NjQyNDM1OTgyZTc0
ZTM5M2QxMmUyOTJiODE2ODJkNGQ3NjcyZGVjNjBlNDBhOGUxMGU4NDUzMGMNCiAgICBzZWN0aW9u
X3BhZ2VfZnJhZ21lbnRfc2hhMjU2OiAwNmY4ZWEzMzRhMmZhOGNlNjIzMzdkNmEzYzU5ZDI0ZTAz
ZjlkOGI5ZDhjYzllOTM2YzkyZTk3Yjc3MWJhYmJiDQogICAgZXhjZXJwdF9zdGFydDogMTI1DQog
ICAgZXhjZXJwdF9lbmQ6IDE3Nw0KICAgIGludGVycHJldGF0aW9uX25vdGU6IFRoaXMgaXMgdGhl
IGV4YWN0IGNhdGVnb3J5IGV4Y2VwdGlvbjsgdGhlIHBvbGljeSBkb2VzIG5vdCBkZWNpZGUgdGhh
dCBhIEJFU1MgYmVsb25ncyB0byBpdC4NCiAgICBzb3VyY2VfcnVsZV9pZDogTVVSRVQtVVAtUk9V
VEUtUlVMRS0wMQ0KICAgIHNvdXJjZV9ydWxlX2V4Y2VycHQ6ICJUb3V0ZXMgY29uc3RydWN0aW9u
cyBvdSAgaW5zdGFsbGF0aW9ucyBhdXRyZXMgcXVlIGNlbGxlcyDDoCB1c2FnZSBkJ8OpcXVpcGVt
ZW50IHB1YmxpYyAgXG5vdSBkJ2ludMOpcsOqdCBjb2xsZWN0aWYsIHNlcnZpY2VzIGFubmV4ZXMg
ZXQgbGVzIGxvZ2VtZW50cyBkZSBmb25jdGlvbiB5IGFmZsOpcmVudC4iDQogICAgc291cmNlX3J1
bGVfc2hhMjU2OiBkZTI2MTVlMjViODM3MDhjODRlOWZmOTMxMzA2MGRjYTcwOGNhMGE4YmM2OTM3
NzdiNjI3OTUxYmMyZGUzOTRjCiAgICBzb3VyY2VfcnVsZV9zdGFydDogNjgKICAgIHNvdXJjZV9y
dWxlX2VuZDogMjM2CiAgLSBldmlkZW5jZV9pZDogTVVSRVQtVVAtUkVTVFJJQ1RJT04tMDEKICAg
IHNlY3Rpb25faWQ6IFNFQ1RJT04tMDA4MAogICAgcGFnZV9udW1iZXI6IDcxCiAgICBldmlkZW5j
ZV9raW5kOiBVU0VfUkVTVFJJQ1RJT04KICAgIGV2aWRlbmNlX2RpcmVjdGlvbjogU1VQUE9SVFNf
RElGRklDVUxUWQogICAgZXhhY3RfcmF3X2V4Y2VycHQ6IFRvdXRlcyBjb25zdHJ1Y3Rpb25zIG91
ICBpbnN0YWxsYXRpb25zIGF1dHJlcyBxdWUgY2VsbGVzCiAgICBleGNlcnB0X3NoYTI1NjogZWRm
YmU1NDc5OWI4YTZjMGU3NGQ4NmIwZTk1OTZlOGM2ODQ3MWYxMTEwNTc4M2IzZTRlOTM4MjVmODMw
ODQ2MgogICAgc2VjdGlvbl9wYWdlX2ZyYWdtZW50X3NoYTI1NjogMDZmOGVhMzM0YTJmYThjZTYy
MzM3ZDZhM2M1OWQyNGUwM2Y5ZDhiOWQ4Y2M5ZTkzNmM5MmU5N2I3NzFiYWJiYgogICAgZXhjZXJw
dF9zdGFydDogNjgKICAgIGV4Y2VycHRfZW5kOiAxMjQKICAgIGludGVycHJldGF0aW9uX25vdGU6
IFRoaXMgaXMgdGhlIGdlbmVyYWwgcmVzdHJpY3Rpb24gc3Vycm91bmRpbmcgdGhlIHB1YmxpYyBv
ciBjb2xsZWN0aXZlLWludGVyZXN0IGV4Y2VwdGlvbjsgaXQgZG9lcyBub3QgZGVjaWRlIHdoZXRo
ZXIgYSBCRVNTIGJlbG9uZ3MgdG8gdGhlIGV4Y2VwdGlvbi4KICAgIHNvdXJjZV9ydWxlX2lkOiBN
VVJFVC1VUC1ST1VURS1SVUxFLTAxCiAgICBzb3VyY2VfcnVsZV9leGNlcnB0OiAiVG91dGVzIGNv
bnN0cnVjdGlvbnMgb3UgIGluc3RhbGxhdGlvbnMgYXV0cmVzIHF1ZSBjZWxsZXMgw6AgdXNhZ2Ug
ZCfDqXF1aXBlbWVudCBwdWJsaWMgIFxub3UgZCdpbnTDqXLDqnQgY29sbGVjdGlmLCBzZXJ2aWNl
cyBhbm5leGVzIGV0IGxlcyBsb2dlbWVudHMgZGUgZm9uY3Rpb24geSBhZmbDqXJlbnQuIgogICAg
c291cmNlX3J1bGVfc2hhMjU2OiBkZTI2MTVlMjViODM3MDhjODRlOWZmOTMxMzA2MGRjYTcwOGNh
MGE4YmM2OTM3NzdiNjI3OTUxYmMyZGUzOTRjCiAgICBzb3VyY2VfcnVsZV9zdGFydDogNjgKICAg
IHNvdXJjZV9ydWxlX2VuZDogMjM2CiAgLSBldmlkZW5jZV9pZDogTVVSRVQtVVAtSUNQRS1DT05E
SVRJT04tMDEKICAgIHNlY3Rpb25faWQ6IFNFQ1RJT04tMDA4MQ0KICAgIHBhZ2VfbnVtYmVyOiA3
MQ0KICAgIGV2aWRlbmNlX2tpbmQ6IElDUEVfUlVMRQ0KICAgIGV2aWRlbmNlX2RpcmVjdGlvbjog
Q09OVEVYVF9PTkxZCiAgICBleGFjdF9yYXdfZXhjZXJwdDogY29tcGF0aWJsZXMgYXZlYyBsZSBt
aWxpZXUgZW52aXJvbm5hbnQgZXQgbsOpY2Vzc2FpcmVzIMOgDQogICAgZXhjZXJwdF9zaGEyNTY6
IDQ1ZTdjODIyOTYzYWViNTkzMWIwMDM5MmY2MDVlNDVmNzQ1ZGU0N2MwODRkMDQ0OTBiZmY2YmIx
NWY0NmE5MjgNCiAgICBzZWN0aW9uX3BhZ2VfZnJhZ21lbnRfc2hhMjU2OiA3YTVmYWMwYjA2ZjMy
YTAyYTM0MDMxZTlkYjYyYjJjY2Q1OWE2MzA5OWZkYjM3ODA3OWFiNDFjNDI1MmFlZDA5DQogICAg
ZXhjZXJwdF9zdGFydDogNDc4DQogICAgZXhjZXJwdF9lbmQ6IDUzMw0KICAgIGludGVycHJldGF0
aW9uX25vdGU6IFRoaXMgc2VwYXJhdGUgSUNQRSBjb25kaXRpb24gaXMgY29udGV4dCBvbmx5IHVu
bGVzcyBhIGZ1dHVyZSBldmlkZW5jZSBzdGVwIGVzdGFibGlzaGVzIHRoYXQgdGhlIEJFU1MgcHJv
amVjdCBpcyBzdWJqZWN0IHRvIGl0LgogICAgc291cmNlX3J1bGVfaWQ6IE1VUkVULVVQLUNPTkRJ
VElPTi1SVUxFLTAxDQogICAgc291cmNlX3J1bGVfZXhjZXJwdDogIkxlcyBpbnN0YWxsYXRpb25z
IGNsYXNzw6llcyBwb3VyIGxhIHByb3RlY3Rpb24gZGUgbOKAmWVudmlyb25uZW1lbnQgbmUgc29u
dCBhdXRvcmlzw6llcyBxdeKAmcOgIFxubGEgY29uZGl0aW9uIHF1J2VsbGVzIHNvaWVudCBjb21w
YXRpYmxlcyBhdmVjIGxlIG1pbGlldSBlbnZpcm9ubmFudCBldCBuw6ljZXNzYWlyZXMgw6AgbGEg
XG52aWUgZHUgcXVhcnRpZXIgZXQgZGUgbGEgY2l0w6kuIg0KICAgIHNvdXJjZV9ydWxlX3NoYTI1
NjogODkwZDJlYWIwMWUwODg5NDhlNzhmZjk2NGJmNjhiYzA0NmQ0YmY4ODg5NGYxOWFlMjA4ODM3
OTNlNWFiYjcxNg0KICAgIHNvdXJjZV9ydWxlX3N0YXJ0OiAzNTkNCiAgICBzb3VyY2VfcnVsZV9l
bmQ6IDU2OA0KICByb3V0ZV9hc3Nlc3NtZW50czoKICAtIHJvdXRlX2lkOiBNVVJFVC1VUC1ST1VU
RS0wMQogICAgcm91dGVfa2luZDogUkVTVFJJQ1RJT05fRVhDRVBUSU9OX1JPVVRFCiAgICBwb3Np
dGl2ZV9ldmlkZW5jZV9pZHM6CiAgICAtIE1VUkVULVVQLVBVQkxJQy1ST1VURS0wMQogICAgY29u
ZGl0aW9uX2V2aWRlbmNlX2lkczogW10KICAgIGRpZmZpY3VsdHlfZXZpZGVuY2VfaWRzOgogICAg
LSBNVVJFVC1VUC1SRVNUUklDVElPTi0wMQogICAgYXBwbGljYWJpbGl0eV9ub3RlOiBUaGUgQXJ0
aWNsZSBVUCAxIHJlc3RyaWN0aW9uIGFuZCBpdHMgcHVibGljIG9yIGNvbGxlY3RpdmUtaW50ZXJl
c3QgZXhjZXB0aW9uIGFyZSBhc3Nlc3NlZCBhcyBvbmUgY29oZXJlbnQgcm91dGU7IEJFU1MgbWVt
YmVyc2hpcCByZW1haW5zIHVucmVzb2x2ZWQuIFRoZSBzZXBhcmF0ZSBJQ1BFIHJ1bGUgaXMgbm90
IHVzZWQgdG8gcXVhbGlmeSB0aGlzIHJvdXRlLgotIHJlc29sdmVkX3pvbmVfY2hhcHRlcl9sYWJl
bDogQVUNCiAgcmV2aWV3X2NvbXBsZXRlbmVzczogQ09NUExFVEVfRk9SX0NPTkZJR1VSRURfVVNF
X0NPTlRST0xfQVJUSUNMRVMNCiAgcmV2aWV3ZWRfc2VjdGlvbl9pZHM6DQogIC0gU0VDVElPTi0w
MDk1DQogIC0gU0VDVElPTi0wMDk2DQogIHJldmlld19ub3RlOiBBcnRpY2xlcyBBVSAxIGFuZCBB
VSAyIHdlcmUgcmV2aWV3ZWQgaW4gZnVsbCBmb3Igd3JpdHRlbiB1c2UgY29udHJvbHMuDQogIHpv
bmluZ19wcmVjaGVja19zdGF0dXM6IENPTkRJVElPTkFMX1JFVklFVw0KICB6b25pbmdfcHJlY2hl
Y2tfY29uZmlkZW5jZTogTE9XDQogIHJhdGlvbmFsZTogSW5mcmFzdHJ1Y3R1cmUgcHJlcmVxdWlz
aXRlcyB3ZXJlIG5vdCB0cmVhdGVkIGFzIGEgcm91dGU7IEFydGljbGUgQVUgMiBzZXBhcmF0ZWx5
IHN0YXRlcyBhIHBvc3NpYmxlIElDUEUgcm91dGUgd2l0aCBjb21wYXRpYmlsaXR5IGFuZCBuZWNl
c3NpdHkgY29uZGl0aW9ucy4NCiAgbWlzc2luZ19pbmZvcm1hdGlvbjogQkVTUyBwbGFubmluZy11
c2UgYW5kIElDUEUgY2xhc3NpZmljYXRpb24sIGluZnJhc3RydWN0dXJlIGFuZCBzZWN0b3IgY29u
ZGl0aW9ucywgYWxsIEFydGljbGUgQVUgMS8yIHByb3Zpc2lvbnMsIHByZXNjcmlwdGlvbnMsIHNl
cnZpdHVkZXMsIHByb2plY3QgZWZmZWN0cyBhbmQgZGVzaWduLg0KICBldmlkZW5jZToNCiAgLSBl
dmlkZW5jZV9pZDogTVVSRVQtQVUtSUNQRS1ST1VURS0wMQ0KICAgIHNlY3Rpb25faWQ6IFNFQ1RJ
T04tMDA5Ng0KICAgIHBhZ2VfbnVtYmVyOiA4MQ0KICAgIGV2aWRlbmNlX2tpbmQ6IElDUEVfUlVM
RQ0KICAgIGV2aWRlbmNlX2RpcmVjdGlvbjogU1VQUE9SVFNfUE9URU5USUFMX0NPTVBBVElCSUxJ
VFkNCiAgICBleGFjdF9yYXdfZXhjZXJwdDogTGVzIGluc3RhbGxhdGlvbnMgY2xhc3PDqWVzIHBv
dXIgbGEgcHJvdGVjdGlvbiBkZSBs4oCZZW52aXJvbm5lbWVudCBuZSBzb250IGF1dG9yaXPDqWVz
DQogICAgZXhjZXJwdF9zaGEyNTY6IGUxYzc2N2JjZjA1ZTZlMzg3OWZkYTkzNGFmYzM5NmI1NWVj
YjhjYjMwYjliZTlkMGUwOTBjOGJhODYwZTEzZmYNCiAgICBzZWN0aW9uX3BhZ2VfZnJhZ21lbnRf
c2hhMjU2OiA1NDUxNjhlNTFhNDdmN2M4Yjk1MTk1NzViNmQ4NzBhYjcwZTExZDEwNDNkZjg0N2Uz
YjViODY2MWE4OTA2NTJlDQogICAgZXhjZXJwdF9zdGFydDogMTQ3NA0KICAgIGV4Y2VycHRfZW5k
OiAxNTU3DQogICAgaW50ZXJwcmV0YXRpb25fbm90ZTogVGhpcyBpcyB0aGUgZXhwbGljaXQgSUNQ
RSByb3V0ZSBwaHJhc2U7IGluZnJhc3RydWN0dXJlIHByZXJlcXVpc2l0ZXMgYWxvbmUgd2VyZSBu
b3QgdXNlZCBhcyBwb3NpdGl2ZSBldmlkZW5jZS4NCiAgICBzb3VyY2VfcnVsZV9pZDogTVVSRVQt
QVUtSUNQRS1SVUxFLTAxDQogICAgc291cmNlX3J1bGVfZXhjZXJwdDogIkxlcyBpbnN0YWxsYXRp
b25zIGNsYXNzw6llcyBwb3VyIGxhIHByb3RlY3Rpb24gZGUgbOKAmWVudmlyb25uZW1lbnQgbmUg
c29udCBhdXRvcmlzw6llcyBxdeKAmcOgIFxubGEgY29uZGl0aW9uIHF1J2VsbGVzIHNvaWVudCBj
b21wYXRpYmxlcyBhdmVjIGxlIG1pbGlldSBlbnZpcm9ubmFudCBldCBuw6ljZXNzYWlyZXMgw6Ag
bGEgXG52aWUgZHUgcXVhcnRpZXIgZXQgZGUgbGEgY2l0w6kuIg0KICAgIHNvdXJjZV9ydWxlX3No
YTI1NjogODkwZDJlYWIwMWUwODg5NDhlNzhmZjk2NGJmNjhiYzA0NmQ0YmY4ODg5NGYxOWFlMjA4
ODM3OTNlNWFiYjcxNg0KICAgIHNvdXJjZV9ydWxlX3N0YXJ0OiAxNDc0DQogICAgc291cmNlX3J1
bGVfZW5kOiAxNjgzDQogIC0gZXZpZGVuY2VfaWQ6IE1VUkVULUFVLUlDUEUtQ09ORElUSU9OLTAx
DQogICAgc2VjdGlvbl9pZDogU0VDVElPTi0wMDk2DQogICAgcGFnZV9udW1iZXI6IDgxDQogICAg
ZXZpZGVuY2Vfa2luZDogSUNQRV9SVUxFDQogICAgZXZpZGVuY2VfZGlyZWN0aW9uOiBDT05ESVRJ
T04NCiAgICBleGFjdF9yYXdfZXhjZXJwdDogY29tcGF0aWJsZXMgYXZlYyBsZSBtaWxpZXUgZW52
aXJvbm5hbnQgZXQgbsOpY2Vzc2FpcmVzIMOgDQogICAgZXhjZXJwdF9zaGEyNTY6IDQ1ZTdjODIy
OTYzYWViNTkzMWIwMDM5MmY2MDVlNDVmNzQ1ZGU0N2MwODRkMDQ0OTBiZmY2YmIxNWY0NmE5MjgN
CiAgICBzZWN0aW9uX3BhZ2VfZnJhZ21lbnRfc2hhMjU2OiA1NDUxNjhlNTFhNDdmN2M4Yjk1MTk1
NzViNmQ4NzBhYjcwZTExZDEwNDNkZjg0N2UzYjViODY2MWE4OTA2NTJlDQogICAgZXhjZXJwdF9z
dGFydDogMTU5Mw0KICAgIGV4Y2VycHRfZW5kOiAxNjQ4DQogICAgaW50ZXJwcmV0YXRpb25fbm90
ZTogVGhpcyBpcyB0aGUgc2VwYXJhdGUgY29tcGF0aWJpbGl0eSBhbmQgbmVjZXNzaXR5IHF1YWxp
ZmljYXRpb24uDQogICAgc291cmNlX3J1bGVfaWQ6IE1VUkVULUFVLUlDUEUtUlVMRS0wMQ0KICAg
IHNvdXJjZV9ydWxlX2V4Y2VycHQ6ICJMZXMgaW5zdGFsbGF0aW9ucyBjbGFzc8OpZXMgcG91ciBs
YSBwcm90ZWN0aW9uIGRlIGzigJllbnZpcm9ubmVtZW50IG5lIHNvbnQgYXV0b3Jpc8OpZXMgcXXi
gJnDoCBcbmxhIGNvbmRpdGlvbiBxdSdlbGxlcyBzb2llbnQgY29tcGF0aWJsZXMgYXZlYyBsZSBt
aWxpZXUgZW52aXJvbm5hbnQgZXQgbsOpY2Vzc2FpcmVzIMOgIGxhIFxudmllIGR1IHF1YXJ0aWVy
IGV0IGRlIGxhIGNpdMOpLiINCiAgICBzb3VyY2VfcnVsZV9zaGEyNTY6IDg5MGQyZWFiMDFlMDg4
OTQ4ZTc4ZmY5NjRiZjY4YmMwNDZkNGJmODg4OTRmMTlhZTIwODgzNzkzZTVhYmI3MTYNCiAgICBz
b3VyY2VfcnVsZV9zdGFydDogMTQ3NA0KICAgIHNvdXJjZV9ydWxlX2VuZDogMTY4Mw0KICByb3V0
ZV9hc3Nlc3NtZW50czoNCiAgLSByb3V0ZV9pZDogTVVSRVQtQVUtUk9VVEUtMDENCiAgICByb3V0
ZV9raW5kOiBDT05ESVRJT05BTF9ST1VURQ0KICAgIHBvc2l0aXZlX2V2aWRlbmNlX2lkczoNCiAg
ICAtIE1VUkVULUFVLUlDUEUtUk9VVEUtMDENCiAgICBjb25kaXRpb25fZXZpZGVuY2VfaWRzOg0K
ICAgIC0gTVVSRVQtQVUtSUNQRS1DT05ESVRJT04tMDENCiAgICBkaWZmaWN1bHR5X2V2aWRlbmNl
X2lkczogW10NCiAgICBhcHBsaWNhYmlsaXR5X25vdGU6IFRoZSBjaXRlZCBwb3NpdGl2ZSBjYXRl
Z29yeSBhbmQgaXRzIGV4cGxpY2l0IHF1YWxpZmljYXRpb24gYXJlIGFzc2Vzc2VkIGFzIG9uZSBj
b2hlcmVudCByb3V0ZTsgQkVTUyBhcHBsaWNhYmlsaXR5IHJlbWFpbnMgdW5yZXNvbHZlZC4NCi0g
cmVzb2x2ZWRfem9uZV9jaGFwdGVyX2xhYmVsOiBBVXANCiAgcmV2aWV3X2NvbXBsZXRlbmVzczog
Q09NUExFVEVfRk9SX0NPTkZJR1VSRURfVVNFX0NPTlRST0xfQVJUSUNMRVMNCiAgcmV2aWV3ZWRf
c2VjdGlvbl9pZHM6DQogIC0gU0VDVElPTi0wMTEwDQogIC0gU0VDVElPTi0wMTExDQogIHJldmll
d19ub3RlOiBBcnRpY2xlcyBBVXAgMSBhbmQgQVVwIDIgd2VyZSByZXZpZXdlZCBpbiBmdWxsIGZv
ciB3cml0dGVuIHVzZSBjb250cm9scy4NCiAgem9uaW5nX3ByZWNoZWNrX3N0YXR1czogQ09ORElU
SU9OQUxfUkVWSUVXDQogIHpvbmluZ19wcmVjaGVja19jb25maWRlbmNlOiBMT1cNCiAgcmF0aW9u
YWxlOiBBcnRpY2xlIEFVcCAxIHN0YXRlcyBhIHB1YmxpYyBvciBjb2xsZWN0aXZlLWludGVyZXN0
IGVxdWlwbWVudCBleGNlcHRpb24gdW5kZXIgQXJ0aWNsZSBBVXAgMiBjb25kaXRpb25zLiBBcnRp
Y2xlIEFVcCAyIHJlcXVpcmVzIGluZGlzcGVuc2FibGUgYWNjZXNzLCByb2FkIGFuZCBuZXR3b3Jr
IGluZnJhc3RydWN0dXJlIGJlZm9yZSBhdXRob3JpemF0aW9uLiBJdHMgc2VwYXJhdGUgSUNQRSBy
dWxlIGlzIHJldGFpbmVkIG9ubHkgYXMgY29udGV4dCBiZWNhdXNlIEJFU1MgSUNQRSBhcHBsaWNh
YmlsaXR5IGhhcyBub3QgYmVlbiBlc3RhYmxpc2hlZC4KICBtaXNzaW5nX2luZm9ybWF0aW9uOiBG
b3JtYWwgQkVTUyBjbGFzc2lmaWNhdGlvbiBhcyBwdWJsaWMgb3IgY29sbGVjdGl2ZS1pbnRlcmVz
dCBlcXVpcG1lbnQsIHNhdGlzZmFjdGlvbiBvZiB0aGUgQXJ0aWNsZSBBVXAgMiBpbmZyYXN0cnVj
dHVyZSBwcmVyZXF1aXNpdGUsIEJFU1MgSUNQRSBhcHBsaWNhYmlsaXR5LCBhbGwgQXJ0aWNsZSBB
VXAgMS8yIHByb3Zpc2lvbnMsIHByZXNjcmlwdGlvbnMsIHNlcnZpdHVkZXMsIHByb2plY3QgZWZm
ZWN0cyBhbmQgZGVzaWduLgogIGV2aWRlbmNlOg0KICAtIGV2aWRlbmNlX2lkOiBNVVJFVC1BVVAt
UFVCTElDLVJPVVRFLTAxDQogICAgc2VjdGlvbl9pZDogU0VDVElPTi0wMTEwDQogICAgcGFnZV9u
dW1iZXI6IDkzDQogICAgZXZpZGVuY2Vfa2luZDogUFVCTElDX0lOVEVSRVNUX0VYQ0VQVElPTg0K
ICAgIGV2aWRlbmNlX2RpcmVjdGlvbjogU1VQUE9SVFNfUE9URU5USUFMX0NPTVBBVElCSUxJVFkN
CiAgICBleGFjdF9yYXdfZXhjZXJwdDogIsOgIHVzYWdlIGQnw6lxdWlwZW1lbnQgcHVibGljIG91
IFxuZCdpbnTDqXLDqnQgY29sbGVjdGlmIg0KICAgIGV4Y2VycHRfc2hhMjU2OiBmN2JlNzFiMTMx
Zjk3Yzc0YzgxMDdiYzZmMTRiZjJhOTgwZDhjM2Y3NjlhNTJlZWY3YTg5OTI0OTEwOGMzNWEyDQog
ICAgc2VjdGlvbl9wYWdlX2ZyYWdtZW50X3NoYTI1NjogNGY1Yjc5NjY2ODU4NzQ1MzQ3ZWM4MTEz
OThhY2QxOWQyNzYxNzA1YjNiM2QyYTMxZmZkOWY0YzU0YTVjOTNkNQ0KICAgIGV4Y2VycHRfc3Rh
cnQ6IDEyNQ0KICAgIGV4Y2VycHRfZW5kOiAxNzYNCiAgICBpbnRlcnByZXRhdGlvbl9ub3RlOiBU
aGlzIGlzIHRoZSBleGFjdCBjYXRlZ29yeSBleGNlcHRpb247IEJFU1MgbWVtYmVyc2hpcCBpcyB1
bnJlc29sdmVkLg0KICAgIHNvdXJjZV9ydWxlX2lkOiBNVVJFVC1BVXAtUk9VVEUtUlVMRS0wMQ0K
ICAgIHNvdXJjZV9ydWxlX2V4Y2VycHQ6ICJUb3V0ZXMgY29uc3RydWN0aW9ucyBvdSBpbnN0YWxs
YXRpb25zIGF1dHJlcyBxdWUgY2VsbGVzIMOgIHVzYWdlIGQnw6lxdWlwZW1lbnQgcHVibGljIG91
IFxuZCdpbnTDqXLDqnQgY29sbGVjdGlmLCBsZXVycyBzZXJ2aWNlcyBhbm5leGVzIGV0IGxlcyBs
b2dlbWVudHMgZGUgZm9uY3Rpb24geSBhZmbDqXJlbnQgIHNvdXMgXG5jb25kaXRpb25zIGRlIGzi
gJlhcnRpY2xlIEFVUC0yLiINCiAgICBzb3VyY2VfcnVsZV9zaGEyNTY6IDAxODcwYjJhYTYzYjE1
NDkxY2JmNjQ0NTAxZGZhODIzOGE5NGY5ODBkNDI2ZDE1ZWUyNzQzY2M1Nzk2YzI0YzMKICAgIHNv
dXJjZV9ydWxlX3N0YXJ0OiA2OQogICAgc291cmNlX3J1bGVfZW5kOiAyNzgKICAtIGV2aWRlbmNl
X2lkOiBNVVJFVC1BVVAtSU5GUkFTVFJVQ1RVUkUtQ09ORElUSU9OLTAxCiAgICBzZWN0aW9uX2lk
OiBTRUNUSU9OLTAxMTEKICAgIHBhZ2VfbnVtYmVyOiA5MwogICAgZXZpZGVuY2Vfa2luZDogQUND
RVNTX09SX05FVFdPUktfQ09ORElUSU9OCiAgICBldmlkZW5jZV9kaXJlY3Rpb246IENPTkRJVElP
TgogICAgZXhhY3RfcmF3X2V4Y2VycHQ6ICJMZXMgY29uc3RydWN0aW9ucyBldCBvcMOpcmF0aW9u
cyBuZSBwb3Vycm9udCDDqnRyZSBhdXRvcmlzw6llcyBxdeKAmWFwcsOocyByw6lhbGlzYXRpb24g
ZGVzICBcbsOpcXVpcGVtZW50cyBk4oCZaW5mcmFzdHJ1Y3R1cmUgaW5kaXNwZW5zYWJsZSDDoCBs
ZXVyIGZvbmN0aW9ubmVtZW50IChhY2PDqHMsIHZvaXJpZSBldCAgXG5yw6lzZWF1eCBkaXZlcnMp
IGNvbmZvcm3DqW1lbnQgYXV4IGFydGljbGVzIEFVcDMgZXQgQVVwNC4iCiAgICBleGNlcnB0X3No
YTI1NjogYjJiZTliMWY3ZTM1OTc4MDJkNWVkMmMzMDFhN2UzNGJiN2E5ZWVjYWVhYjU1ODk4ZTU1
MzA2NzE5YjFiMzE1YgogICAgc2VjdGlvbl9wYWdlX2ZyYWdtZW50X3NoYTI1NjogNTc1NDBkMjgx
NDhhZWZjMzIwZmNjOGJhYTlhOTJkZjdlMzgyZDcyMjk5ZGE2ZTgwNGEzZWJmYWY1MjQwOGI0NAog
ICAgZXhjZXJwdF9zdGFydDogOTgKICAgIGV4Y2VycHRfZW5kOiAzMjUKICAgIGludGVycHJldGF0
aW9uX25vdGU6IFRoaXMgaXMgdGhlIGdlbmVyYWwgQXJ0aWNsZSBBVXAgMiBpbmZyYXN0cnVjdHVy
ZSBwcmVyZXF1aXNpdGUgZXhwcmVzc2x5IHJlZmVyZW5jZWQgYnkgQXJ0aWNsZSBBVXAgMTsgdGhl
IHBvbGljeSBkb2VzIG5vdCBkZWNpZGUgdGhhdCBpdCBpcyBzYXRpc2ZpZWQuCiAgICBzb3VyY2Vf
cnVsZV9pZDogTVVSRVQtQVVwLUlORlJBU1RSVUNUVVJFLVJVTEUtMDEKICAgIHNvdXJjZV9ydWxl
X2V4Y2VycHQ6ICJMZXMgY29uc3RydWN0aW9ucyBldCBvcMOpcmF0aW9ucyBuZSBwb3Vycm9udCDD
qnRyZSBhdXRvcmlzw6llcyBxdeKAmWFwcsOocyByw6lhbGlzYXRpb24gZGVzICBcbsOpcXVpcGVt
ZW50cyBk4oCZaW5mcmFzdHJ1Y3R1cmUgaW5kaXNwZW5zYWJsZSDDoCBsZXVyIGZvbmN0aW9ubmVt
ZW50IChhY2PDqHMsIHZvaXJpZSBldCAgXG5yw6lzZWF1eCBkaXZlcnMpIGNvbmZvcm3DqW1lbnQg
YXV4IGFydGljbGVzIEFVcDMgZXQgQVVwNC4iCiAgICBzb3VyY2VfcnVsZV9zaGEyNTY6IGIyYmU5
YjFmN2UzNTk3ODAyZDVlZDJjMzAxYTdlMzRiYjdhOWVlY2FlYWI1NTg5OGU1NTMwNjcxOWIxYjMx
NWIKICAgIHNvdXJjZV9ydWxlX3N0YXJ0OiA5OAogICAgc291cmNlX3J1bGVfZW5kOiAzMjUKICAt
IGV2aWRlbmNlX2lkOiBNVVJFVC1BVVAtSUNQRS1DT05ESVRJT04tMDEKICAgIHNlY3Rpb25faWQ6
IFNFQ1RJT04tMDExMQ0KICAgIHBhZ2VfbnVtYmVyOiA5Mw0KICAgIGV2aWRlbmNlX2tpbmQ6IElD
UEVfUlVMRQ0KICAgIGV2aWRlbmNlX2RpcmVjdGlvbjogQ09OVEVYVF9PTkxZCiAgICBleGFjdF9y
YXdfZXhjZXJwdDogY29tcGF0aWJsZXMgYXZlYyBsZSBtaWxpZXUgZW52aXJvbm5hbnQgZXQgbsOp
Y2Vzc2FpcmVzIMOgDQogICAgZXhjZXJwdF9zaGEyNTY6IDQ1ZTdjODIyOTYzYWViNTkzMWIwMDM5
MmY2MDVlNDVmNzQ1ZGU0N2MwODRkMDQ0OTBiZmY2YmIxNWY0NmE5MjgNCiAgICBzZWN0aW9uX3Bh
Z2VfZnJhZ21lbnRfc2hhMjU2OiA1NzU0MGQyODE0OGFlZmMzMjBmY2M4YmFhOWE5MmRmN2UzODJk
NzIyOTlkYTZlODA0YTNlYmZhZjUyNDA4YjQ0DQogICAgZXhjZXJwdF9zdGFydDogNzEzDQogICAg
ZXhjZXJwdF9lbmQ6IDc2OA0KICAgIGludGVycHJldGF0aW9uX25vdGU6IFRoaXMgc2VwYXJhdGUg
SUNQRSBjb25kaXRpb24gaXMgY29udGV4dCBvbmx5IHVubGVzcyBhIGZ1dHVyZSBldmlkZW5jZSBz
dGVwIGVzdGFibGlzaGVzIHRoYXQgdGhlIEJFU1MgcHJvamVjdCBpcyBzdWJqZWN0IHRvIGl0Lgog
ICAgc291cmNlX3J1bGVfaWQ6IE1VUkVULUFVcC1DT05ESVRJT04tUlVMRS0wMQ0KICAgIHNvdXJj
ZV9ydWxlX2V4Y2VycHQ6ICJMZXMgaW5zdGFsbGF0aW9ucyBjbGFzc8OpZXMgcG91ciBsYSBwcm90
ZWN0aW9uIGRlIGzigJllbnZpcm9ubmVtZW50IG5lIHNvbnQgYXV0b3Jpc8OpZXMgcXXigJnDoCBc
bmxhIGNvbmRpdGlvbiBxdSdlbGxlcyBzb2llbnQgY29tcGF0aWJsZXMgYXZlYyBsZSBtaWxpZXUg
ZW52aXJvbm5hbnQgZXQgbsOpY2Vzc2FpcmVzIMOgIGxhIFxudmllIGR1IHF1YXJ0aWVyIGV0IGRl
IGxhIGNpdMOpLiINCiAgICBzb3VyY2VfcnVsZV9zaGEyNTY6IDg5MGQyZWFiMDFlMDg4OTQ4ZTc4
ZmY5NjRiZjY4YmMwNDZkNGJmODg4OTRmMTlhZTIwODgzNzkzZTVhYmI3MTYNCiAgICBzb3VyY2Vf
cnVsZV9zdGFydDogNTk0DQogICAgc291cmNlX3J1bGVfZW5kOiA4MDMNCiAgcm91dGVfYXNzZXNz
bWVudHM6DQogIC0gcm91dGVfaWQ6IE1VUkVULUFVcC1ST1VURS0wMQ0KICAgIHJvdXRlX2tpbmQ6
IENPTkRJVElPTkFMX1JPVVRFDQogICAgcG9zaXRpdmVfZXZpZGVuY2VfaWRzOgogICAgLSBNVVJF
VC1BVVAtUFVCTElDLVJPVVRFLTAxCiAgICBjb25kaXRpb25fZXZpZGVuY2VfaWRzOgogICAgLSBN
VVJFVC1BVVAtSU5GUkFTVFJVQ1RVUkUtQ09ORElUSU9OLTAxCiAgICBkaWZmaWN1bHR5X2V2aWRl
bmNlX2lkczogW10KICAgIGFwcGxpY2FiaWxpdHlfbm90ZTogVGhlIEFydGljbGUgQVVwIDEgcHVi
bGljIG9yIGNvbGxlY3RpdmUtaW50ZXJlc3Qgcm91dGUgaXMgYXNzZXNzZWQgd2l0aCB0aGUgZ2Vu
ZXJhbCBBcnRpY2xlIEFVcCAyIGluZnJhc3RydWN0dXJlIHByZXJlcXVpc2l0ZS4gQkVTUyBjYXRl
Z29yeSBtZW1iZXJzaGlwIGFuZCBzYXRpc2ZhY3Rpb24gcmVtYWluIHVucmVzb2x2ZWQ7IHRoZSBz
ZXBhcmF0ZSBJQ1BFIHJ1bGUgZG9lcyBub3QgcXVhbGlmeSB0aGlzIHJvdXRlIHVubGVzcyBpbmRl
cGVuZGVudGx5IGFwcGxpY2FibGUuCi0gcmVzb2x2ZWRfem9uZV9jaGFwdGVyX2xhYmVsOiBBVWYN
CiAgcmV2aWV3X2NvbXBsZXRlbmVzczogQ09NUExFVEVfRk9SX0NPTkZJR1VSRURfVVNFX0NPTlRS
T0xfQVJUSUNMRVMNCiAgcmV2aWV3ZWRfc2VjdGlvbl9pZHM6DQogIC0gU0VDVElPTi0wMTI1DQog
IC0gU0VDVElPTi0wMTI2DQogIHJldmlld19ub3RlOiBBcnRpY2xlcyBBVWYgMSBhbmQgQVVmIDIg
d2VyZSByZXZpZXdlZCBpbiBmdWxsIGZvciB3cml0dGVuIHVzZSBjb250cm9scy4NCiAgem9uaW5n
X3ByZWNoZWNrX3N0YXR1czogQ09ORElUSU9OQUxfUkVWSUVXDQogIHpvbmluZ19wcmVjaGVja19j
b25maWRlbmNlOiBMT1cNCiAgcmF0aW9uYWxlOiBJbmZyYXN0cnVjdHVyZSBwcmVyZXF1aXNpdGVz
IHdlcmUgbm90IHRyZWF0ZWQgYXMgcm91dGUgZXZpZGVuY2U7IEFydGljbGUgQVVmIDIgc2VwYXJh
dGVseSBzdGF0ZXMgYSBwb3NzaWJsZSBJQ1BFIHJvdXRlIHdpdGggY29tcGF0aWJpbGl0eSBhbmQg
bmVjZXNzaXR5IGNvbmRpdGlvbnMuDQogIG1pc3NpbmdfaW5mb3JtYXRpb246IEJFU1MgcGxhbm5p
bmctdXNlLCBzZWN0b3IgYW5kIElDUEUgY2xhc3NpZmljYXRpb24sIGluZnJhc3RydWN0dXJlIGFu
ZCBvcmllbnRhdGlvbiByZXF1aXJlbWVudHMsIGFsbCBBcnRpY2xlIEFVZiAxLzIgcHJvdmlzaW9u
cywgcHJlc2NyaXB0aW9ucyBhbmQgcHJvamVjdCBkZXNpZ24uDQogIGV2aWRlbmNlOg0KICAtIGV2
aWRlbmNlX2lkOiBNVVJFVC1BVUYtSUNQRS1ST1VURS0wMQ0KICAgIHNlY3Rpb25faWQ6IFNFQ1RJ
T04tMDEyNg0KICAgIHBhZ2VfbnVtYmVyOiAxMDINCiAgICBldmlkZW5jZV9raW5kOiBJQ1BFX1JV
TEUNCiAgICBldmlkZW5jZV9kaXJlY3Rpb246IFNVUFBPUlRTX1BPVEVOVElBTF9DT01QQVRJQklM
SVRZDQogICAgZXhhY3RfcmF3X2V4Y2VycHQ6IExlcyBpbnN0YWxsYXRpb25zIGNsYXNzw6llcyBw
b3VyIGxhIHByb3RlY3Rpb24gZGUgbOKAmWVudmlyb25uZW1lbnQgbmUgc29udCBhdXRvcmlzw6ll
cw0KICAgIGV4Y2VycHRfc2hhMjU2OiBlMWM3NjdiY2YwNWU2ZTM4NzlmZGE5MzRhZmMzOTZiNTVl
Y2I4Y2IzMGI5YmU5ZDBlMDkwYzhiYTg2MGUxM2ZmDQogICAgc2VjdGlvbl9wYWdlX2ZyYWdtZW50
X3NoYTI1NjogZWYwZDI3MTgzMzIzMDdhZmE4NzExNzZjNjRjYjg2Mjc5MDA3MDJkYmQ1ODM4MTlm
Yjc2NWFkYjJkMTkwMjc2OQ0KICAgIGV4Y2VycHRfc3RhcnQ6IDE0MzUNCiAgICBleGNlcnB0X2Vu
ZDogMTUxOA0KICAgIGludGVycHJldGF0aW9uX25vdGU6IFRoaXMgaXMgdGhlIGV4cGxpY2l0IElD
UEUgcm91dGUgcGhyYXNlOyBpbmZyYXN0cnVjdHVyZSBwcmVyZXF1aXNpdGVzIGFsb25lIHdlcmUg
bm90IHVzZWQgYXMgcG9zaXRpdmUgZXZpZGVuY2UuDQogICAgc291cmNlX3J1bGVfaWQ6IE1VUkVU
LUFVZi1JQ1BFLVJVTEUtMDENCiAgICBzb3VyY2VfcnVsZV9leGNlcnB0OiAiTGVzIGluc3RhbGxh
dGlvbnMgY2xhc3PDqWVzIHBvdXIgbGEgcHJvdGVjdGlvbiBkZSBs4oCZZW52aXJvbm5lbWVudCBu
ZSBzb250IGF1dG9yaXPDqWVzIHF14oCZw6AgXG5sYSBjb25kaXRpb24gcXUnZWxsZXMgc29pZW50
IGNvbXBhdGlibGVzIGF2ZWMgbGUgbWlsaWV1IGVudmlyb25uYW50IGV0IG7DqWNlc3NhaXJlcyDD
oCBsYSBcbnZpZSBkdSBxdWFydGllciBldCBkZSBsYSBjaXTDqS4iDQogICAgc291cmNlX3J1bGVf
c2hhMjU2OiA4OTBkMmVhYjAxZTA4ODk0OGU3OGZmOTY0YmY2OGJjMDQ2ZDRiZjg4ODk0ZjE5YWUy
MDg4Mzc5M2U1YWJiNzE2DQogICAgc291cmNlX3J1bGVfc3RhcnQ6IDE0MzUNCiAgICBzb3VyY2Vf
cnVsZV9lbmQ6IDE2NDQNCiAgLSBldmlkZW5jZV9pZDogTVVSRVQtQVVGLUlDUEUtQ09ORElUSU9O
LTAxDQogICAgc2VjdGlvbl9pZDogU0VDVElPTi0wMTI2DQogICAgcGFnZV9udW1iZXI6IDEwMg0K
ICAgIGV2aWRlbmNlX2tpbmQ6IElDUEVfUlVMRQ0KICAgIGV2aWRlbmNlX2RpcmVjdGlvbjogQ09O
RElUSU9ODQogICAgZXhhY3RfcmF3X2V4Y2VycHQ6IGNvbXBhdGlibGVzIGF2ZWMgbGUgbWlsaWV1
IGVudmlyb25uYW50IGV0IG7DqWNlc3NhaXJlcyDDoA0KICAgIGV4Y2VycHRfc2hhMjU2OiA0NWU3
YzgyMjk2M2FlYjU5MzFiMDAzOTJmNjA1ZTQ1Zjc0NWRlNDdjMDg0ZDA0NDkwYmZmNmJiMTVmNDZh
OTI4DQogICAgc2VjdGlvbl9wYWdlX2ZyYWdtZW50X3NoYTI1NjogZWYwZDI3MTgzMzIzMDdhZmE4
NzExNzZjNjRjYjg2Mjc5MDA3MDJkYmQ1ODM4MTlmYjc2NWFkYjJkMTkwMjc2OQ0KICAgIGV4Y2Vy
cHRfc3RhcnQ6IDE1NTQNCiAgICBleGNlcnB0X2VuZDogMTYwOQ0KICAgIGludGVycHJldGF0aW9u
X25vdGU6IFRoaXMgaXMgdGhlIHNlcGFyYXRlIGNvbXBhdGliaWxpdHkgYW5kIG5lY2Vzc2l0eSBx
dWFsaWZpY2F0aW9uLg0KICAgIHNvdXJjZV9ydWxlX2lkOiBNVVJFVC1BVWYtSUNQRS1SVUxFLTAx
DQogICAgc291cmNlX3J1bGVfZXhjZXJwdDogIkxlcyBpbnN0YWxsYXRpb25zIGNsYXNzw6llcyBw
b3VyIGxhIHByb3RlY3Rpb24gZGUgbOKAmWVudmlyb25uZW1lbnQgbmUgc29udCBhdXRvcmlzw6ll
cyBxdeKAmcOgIFxubGEgY29uZGl0aW9uIHF1J2VsbGVzIHNvaWVudCBjb21wYXRpYmxlcyBhdmVj
IGxlIG1pbGlldSBlbnZpcm9ubmFudCBldCBuw6ljZXNzYWlyZXMgw6AgbGEgXG52aWUgZHUgcXVh
cnRpZXIgZXQgZGUgbGEgY2l0w6kuIg0KICAgIHNvdXJjZV9ydWxlX3NoYTI1NjogODkwZDJlYWIw
MWUwODg5NDhlNzhmZjk2NGJmNjhiYzA0NmQ0YmY4ODg5NGYxOWFlMjA4ODM3OTNlNWFiYjcxNg0K
ICAgIHNvdXJjZV9ydWxlX3N0YXJ0OiAxNDM1DQogICAgc291cmNlX3J1bGVfZW5kOiAxNjQ0DQog
IHJvdXRlX2Fzc2Vzc21lbnRzOg0KICAtIHJvdXRlX2lkOiBNVVJFVC1BVWYtUk9VVEUtMDENCiAg
ICByb3V0ZV9raW5kOiBDT05ESVRJT05BTF9ST1VURQ0KICAgIHBvc2l0aXZlX2V2aWRlbmNlX2lk
czoNCiAgICAtIE1VUkVULUFVRi1JQ1BFLVJPVVRFLTAxDQogICAgY29uZGl0aW9uX2V2aWRlbmNl
X2lkczoNCiAgICAtIE1VUkVULUFVRi1JQ1BFLUNPTkRJVElPTi0wMQ0KICAgIGRpZmZpY3VsdHlf
ZXZpZGVuY2VfaWRzOiBbXQ0KICAgIGFwcGxpY2FiaWxpdHlfbm90ZTogVGhlIGNpdGVkIHBvc2l0
aXZlIGNhdGVnb3J5IGFuZCBpdHMgZXhwbGljaXQgcXVhbGlmaWNhdGlvbiBhcmUgYXNzZXNzZWQg
YXMgb25lIGNvaGVyZW50IHJvdXRlOyBCRVNTIGFwcGxpY2FiaWxpdHkgcmVtYWlucyB1bnJlc29s
dmVkLg0KLSByZXNvbHZlZF96b25lX2NoYXB0ZXJfbGFiZWw6IEFVMA0KICByZXZpZXdfY29tcGxl
dGVuZXNzOiBDT01QTEVURV9GT1JfQ09ORklHVVJFRF9VU0VfQ09OVFJPTF9BUlRJQ0xFUw0KICBy
ZXZpZXdlZF9zZWN0aW9uX2lkczoNCiAgLSBTRUNUSU9OLTAxNDANCiAgLSBTRUNUSU9OLTAxNDEN
CiAgcmV2aWV3X25vdGU6IEFydGljbGVzIEFVMCAxIGFuZCBBVTAgMiB3ZXJlIHJldmlld2VkIGlu
IGZ1bGwgZm9yIHdyaXR0ZW4gdXNlIGNvbnRyb2xzLg0KICB6b25pbmdfcHJlY2hlY2tfc3RhdHVz
OiBDT05ESVRJT05BTF9SRVZJRVcNCiAgem9uaW5nX3ByZWNoZWNrX2NvbmZpZGVuY2U6IExPVw0K
ICByYXRpb25hbGU6IEFydGljbGUgQVUwIDEgaWRlbnRpZmllcyBhbiBleGNlcHRpb24gZm9yIGNv
bGxlY3RpdmUtaW50ZXJlc3QgbmV0d29ya3MgYW5kIHB1YmxpYyBpbmZyYXN0cnVjdHVyZSwgd2hp
bGUgQXJ0aWNsZSBBVTAgMiBzdGF0ZXMgYSBzZXBhcmF0ZSBQTFUtbW9kaWZpY2F0aW9uIHByZXJl
cXVpc2l0ZSBmb3IgbmV3IGNvbnN0cnVjdGlvbiBvciBvcGVyYXRpb25zLg0KICBtaXNzaW5nX2lu
Zm9ybWF0aW9uOiBGb3JtYWwgQkVTUyBjbGFzc2lmaWNhdGlvbiB3aXRoaW4gdGhlIHN0YXRlZCBp
bmZyYXN0cnVjdHVyZSBleGNlcHRpb24sIGFwcGxpY2FiaWxpdHkgb2YgdGhlIG1vZGlmaWNhdGlv
biBwcmVyZXF1aXNpdGUsIGFsbCBBcnRpY2xlIEFVMCAxLzIgcHJvdmlzaW9ucywgcHJlc2NyaXB0
aW9ucyBhbmQgcHJvamVjdCBkZXNpZ24uDQogIGV2aWRlbmNlOg0KICAtIGV2aWRlbmNlX2lkOiBN
VVJFVC1BVTAtSU5GUkEtUk9VVEUtMDENCiAgICBzZWN0aW9uX2lkOiBTRUNUSU9OLTAxNDANCiAg
ICBwYWdlX251bWJlcjogMTE0DQogICAgZXZpZGVuY2Vfa2luZDogVEVDSE5JQ0FMX0VRVUlQTUVO
VF9SVUxFDQogICAgZXZpZGVuY2VfZGlyZWN0aW9uOiBTVVBQT1JUU19QT1RFTlRJQUxfQ09NUEFU
SUJJTElUWQ0KICAgIGV4YWN0X3Jhd19leGNlcnB0OiAiaW5zdGFsbGF0aW9ucyBuw6ljZXNzYWly
ZXMgYXV4IHLDqXNlYXV4IFxuZOKAmWludMOpcsOqdCBjb2xsZWN0aWYsIGF1eCBvdXZyYWdlcyBw
dWJsaWNzIGTigJlpbmZyYXN0cnVjdHVyZXMiDQogICAgZXhjZXJwdF9zaGEyNTY6IDg4NmFhY2Vh
ZmIyYTQwZTczZTNlYmUxNDViM2E1OGI2YTIyYjIzOWE4Y2U1ZmNjMzc0MGNiOTlkN2Q2Mjk4YTAN
CiAgICBzZWN0aW9uX3BhZ2VfZnJhZ21lbnRfc2hhMjU2OiAyZjRjZjkzMWM3NmM1YTVhMjlhYTY5
ZDY3Yjc5ODZiMDkyYWZmMzllYTEzZTRiMzAyNTEzMTc3ZTVmZWY2NjE5DQogICAgZXhjZXJwdF9z
dGFydDogMTE5DQogICAgZXhjZXJwdF9lbmQ6IDIxNw0KICAgIGludGVycHJldGF0aW9uX25vdGU6
IFRoaXMgaXMgYW4gZXhhY3QgaW5mcmFzdHJ1Y3R1cmUgZXhjZXB0aW9uOyBCRVNTIHF1YWxpZmlj
YXRpb24gaXMgdW5yZXNvbHZlZC4NCiAgICBzb3VyY2VfcnVsZV9pZDogTVVSRVQtQVUwLVJPVVRF
LVJVTEUtMDENCiAgICBzb3VyY2VfcnVsZV9leGNlcnB0OiAiU29udCBpbnRlcmRpdGVzIHRvdXRl
cyBsZXMgY29uc3RydWN0aW9ucyBhdXRyZXMgcXVlIGxlcyBpbnN0YWxsYXRpb25zIG7DqWNlc3Nh
aXJlcyBhdXggcsOpc2VhdXggXG5k4oCZaW50w6lyw6p0IGNvbGxlY3RpZiwgYXV4IG91dnJhZ2Vz
IHB1YmxpY3MgZOKAmWluZnJhc3RydWN0dXJlcywgZXQgbGVzIGV4dGVuc2lvbnMgZMOpZmluaWVz
IMOgIFxubOKAmWFydGljbGUgQVUwIOKAkyAyLiINCiAgICBzb3VyY2VfcnVsZV9zaGEyNTY6IGZh
MjAxNDI1MjI0ODNiZTgxODNkZjFhNDNlMDY5ZmNiMzUwYjFkZTgzMzQ3YmRmZGQ3MzNmNzg3MWJj
ZjIwN2QNCiAgICBzb3VyY2VfcnVsZV9zdGFydDogNjMNCiAgICBzb3VyY2VfcnVsZV9lbmQ6IDI2
Nw0KICAtIGV2aWRlbmNlX2lkOiBNVVJFVC1BVTAtTU9ESUZJQ0FUSU9OLUNPTkRJVElPTi0wMQ0K
ICAgIHNlY3Rpb25faWQ6IFNFQ1RJT04tMDE0MQ0KICAgIHBhZ2VfbnVtYmVyOiAxMTQNCiAgICBl
dmlkZW5jZV9raW5kOiBPVEhFUl9SRUxFVkFOVF9SVUxFDQogICAgZXZpZGVuY2VfZGlyZWN0aW9u
OiBDT05ESVRJT04NCiAgICBleGFjdF9yYXdfZXhjZXJwdDogIkxlcyBjb25zdHJ1Y3Rpb25zIGV0
IG9ww6lyYXRpb25zIG5vdXZlbGxlcyBuZSBwb3Vycm9udCDDqnRyZSBhdXRvcmlzw6llcyBxdeKA
mWFwcsOocyBsYSBcbm1pc2UgZW4gxZN1dnJlIGTigJl1bmUgcHJvY8OpZHVyZSBkZSBtb2RpZmlj
YXRpb24gZHUgUExVIg0KICAgIGV4Y2VycHRfc2hhMjU2OiAwMTU5NGU2MzJmYjA2NGE3ZTRkZDQw
OGU2OGMxNTZiNjY3MTFhYmU2YWUyYTBlNDcwYzc3OWU5NGI5MWYzYTQ4DQogICAgc2VjdGlvbl9w
YWdlX2ZyYWdtZW50X3NoYTI1NjogYTIzOWNmOWVmZjA0MGNhOWM5YWI2MDhjZjA0MGUzYzczOWQ1
MTExYzg3N2FhNjhhZDE3NzNkM2FkYWRmMjRhNQ0KICAgIGV4Y2VycHRfc3RhcnQ6IDk5DQogICAg
ZXhjZXJwdF9lbmQ6IDIzNA0KICAgIGludGVycHJldGF0aW9uX25vdGU6IFRoaXMgcHJlcmVxdWlz
aXRlIGlzIGEgY29uZGl0aW9uIG9ubHkgYW5kIGlzIG5vdCB0cmVhdGVkIGFzIGV2aWRlbmNlIHRo
YXQgYSBCRVNTIHJvdXRlIGV4aXN0cy4NCiAgICBzb3VyY2VfcnVsZV9pZDogTVVSRVQtQVUwLUNP
TkRJVElPTi1SVUxFLTAxDQogICAgc291cmNlX3J1bGVfZXhjZXJwdDogIkxlcyBjb25zdHJ1Y3Rp
b25zIGV0IG9ww6lyYXRpb25zIG5vdXZlbGxlcyBuZSBwb3Vycm9udCDDqnRyZSBhdXRvcmlzw6ll
cyBxdeKAmWFwcsOocyBsYSBcbm1pc2UgZW4gxZN1dnJlIGTigJl1bmUgcHJvY8OpZHVyZSBkZSBt
b2RpZmljYXRpb24gZHUgUExVLiINCiAgICBzb3VyY2VfcnVsZV9zaGEyNTY6IDJkOTYzMzc3NGY0
MTRhOGFkMmY4ZTQyYmZjYmIyNTA3YjY3NzkwNmNhNmFjYTQ4MGYwMjM5Y2VjMDA3OTQyZTMNCiAg
ICBzb3VyY2VfcnVsZV9zdGFydDogOTkNCiAgICBzb3VyY2VfcnVsZV9lbmQ6IDIzNQ0KICByb3V0
ZV9hc3Nlc3NtZW50czoNCiAgLSByb3V0ZV9pZDogTVVSRVQtQVUwLVJPVVRFLTAxDQogICAgcm91
dGVfa2luZDogQ09ORElUSU9OQUxfUk9VVEUNCiAgICBwb3NpdGl2ZV9ldmlkZW5jZV9pZHM6DQog
ICAgLSBNVVJFVC1BVTAtSU5GUkEtUk9VVEUtMDENCiAgICBjb25kaXRpb25fZXZpZGVuY2VfaWRz
Og0KICAgIC0gTVVSRVQtQVUwLU1PRElGSUNBVElPTi1DT05ESVRJT04tMDENCiAgICBkaWZmaWN1
bHR5X2V2aWRlbmNlX2lkczogW10NCiAgICBhcHBsaWNhYmlsaXR5X25vdGU6IFRoZSBjaXRlZCBw
b3NpdGl2ZSBjYXRlZ29yeSBhbmQgaXRzIGV4cGxpY2l0IHF1YWxpZmljYXRpb24gYXJlIGFzc2Vz
c2VkIGFzIG9uZSBjb2hlcmVudCByb3V0ZTsgQkVTUyBhcHBsaWNhYmlsaXR5IHJlbWFpbnMgdW5y
ZXNvbHZlZC4NCi0gcmVzb2x2ZWRfem9uZV9jaGFwdGVyX2xhYmVsOiBBVWYwDQogIHJldmlld19j
b21wbGV0ZW5lc3M6IENPTVBMRVRFX0ZPUl9DT05GSUdVUkVEX1VTRV9DT05UUk9MX0FSVElDTEVT
DQogIHJldmlld2VkX3NlY3Rpb25faWRzOg0KICAtIFNFQ1RJT04tMDE1NQ0KICAtIFNFQ1RJT04t
MDE1Ng0KICByZXZpZXdfbm90ZTogQXJ0aWNsZXMgQVVmMCAxIGFuZCBBVWYwIDIgd2VyZSByZXZp
ZXdlZCBpbiBmdWxsIGZvciB3cml0dGVuIHVzZSBjb250cm9scy4NCiAgem9uaW5nX3ByZWNoZWNr
X3N0YXR1czogQ09ORElUSU9OQUxfUkVWSUVXDQogIHpvbmluZ19wcmVjaGVja19jb25maWRlbmNl
OiBMT1cNCiAgcmF0aW9uYWxlOiBBcnRpY2xlIEFVZjAgMSBpZGVudGlmaWVzIGFuIGV4Y2VwdGlv
biBmb3IgY29sbGVjdGl2ZS1pbnRlcmVzdCBuZXR3b3JrcyBhbmQgcHVibGljIGluZnJhc3RydWN0
dXJlLCB3aGlsZSBBcnRpY2xlIEFVZjAgMiBzdGF0ZXMgYSBzZXBhcmF0ZSBQTFUtbW9kaWZpY2F0
aW9uIHByZXJlcXVpc2l0ZS4NCiAgbWlzc2luZ19pbmZvcm1hdGlvbjogRm9ybWFsIEJFU1MgY2xh
c3NpZmljYXRpb24gd2l0aGluIHRoZSBpbmZyYXN0cnVjdHVyZSBleGNlcHRpb24sIGFwcGxpY2Fi
aWxpdHkgb2YgdGhlIG1vZGlmaWNhdGlvbiBwcmVyZXF1aXNpdGUsIGFsbCBBcnRpY2xlIEFVZjAg
MS8yIHByb3Zpc2lvbnMsIHByZXNjcmlwdGlvbnMgYW5kIHByb2plY3QgZGVzaWduLg0KICBldmlk
ZW5jZToNCiAgLSBldmlkZW5jZV9pZDogTVVSRVQtQVVGMC1JTkZSQS1ST1VURS0wMQ0KICAgIHNl
Y3Rpb25faWQ6IFNFQ1RJT04tMDE1NQ0KICAgIHBhZ2VfbnVtYmVyOiAxMjANCiAgICBldmlkZW5j
ZV9raW5kOiBURUNITklDQUxfRVFVSVBNRU5UX1JVTEUNCiAgICBldmlkZW5jZV9kaXJlY3Rpb246
IFNVUFBPUlRTX1BPVEVOVElBTF9DT01QQVRJQklMSVRZDQogICAgZXhhY3RfcmF3X2V4Y2VycHQ6
ICJpbnN0YWxsYXRpb25zIG7DqWNlc3NhaXJlcyBhdXggcsOpc2VhdXggXG5k4oCZaW50w6lyw6p0
IGNvbGxlY3RpZiwgYXV4IG91dnJhZ2VzIHB1YmxpY3MgZOKAmWluZnJhc3RydWN0dXJlcyINCiAg
ICBleGNlcnB0X3NoYTI1NjogODg2YWFjZWFmYjJhNDBlNzNlM2ViZTE0NWIzYTU4YjZhMjJiMjM5
YThjZTVmY2MzNzQwY2I5OWQ3ZDYyOThhMA0KICAgIHNlY3Rpb25fcGFnZV9mcmFnbWVudF9zaGEy
NTY6IGEyM2IyYzBmN2U0ODcxMTc1ODAxMmQzYjE3Njk2NzEzOWEzYjg3ZDIzMGMzZGVhMzEyOTg3
NjkzZGU4NmMzNjkNCiAgICBleGNlcnB0X3N0YXJ0OiAxMjANCiAgICBleGNlcnB0X2VuZDogMjE4
DQogICAgaW50ZXJwcmV0YXRpb25fbm90ZTogVGhpcyBpcyBhbiBleGFjdCBpbmZyYXN0cnVjdHVy
ZSBleGNlcHRpb247IEJFU1MgcXVhbGlmaWNhdGlvbiBpcyB1bnJlc29sdmVkLg0KICAgIHNvdXJj
ZV9ydWxlX2lkOiBNVVJFVC1BVWYwLVJPVVRFLVJVTEUtMDENCiAgICBzb3VyY2VfcnVsZV9leGNl
cnB0OiAiU29udCBpbnRlcmRpdGVzIHRvdXRlcyBsZXMgY29uc3RydWN0aW9ucyBhdXRyZXMgcXVl
IGxlcyBpbnN0YWxsYXRpb25zIG7DqWNlc3NhaXJlcyBhdXggcsOpc2VhdXggXG5k4oCZaW50w6ly
w6p0IGNvbGxlY3RpZiwgYXV4IG91dnJhZ2VzIHB1YmxpY3MgZOKAmWluZnJhc3RydWN0dXJlcywg
ZXQgbGVzIGV4dGVuc2lvbnMgZMOpZmluaWVzIMOgIFxubOKAmWFydGljbGUgQVVmMCDigJMgMi4i
DQogICAgc291cmNlX3J1bGVfc2hhMjU2OiA1ZjRhZjJlMmVjZTU1MGNjYzFiY2IzOWViNzQzNmY3
ZGJhMDRmNWYyMWMwMzQ2YjdkNzgwYmYzNTBiNzcxODNjDQogICAgc291cmNlX3J1bGVfc3RhcnQ6
IDY0DQogICAgc291cmNlX3J1bGVfZW5kOiAyNjkNCiAgLSBldmlkZW5jZV9pZDogTVVSRVQtQVVG
MC1NT0RJRklDQVRJT04tQ09ORElUSU9OLTAxDQogICAgc2VjdGlvbl9pZDogU0VDVElPTi0wMTU2
DQogICAgcGFnZV9udW1iZXI6IDEyMA0KICAgIGV2aWRlbmNlX2tpbmQ6IE9USEVSX1JFTEVWQU5U
X1JVTEUNCiAgICBldmlkZW5jZV9kaXJlY3Rpb246IENPTkRJVElPTg0KICAgIGV4YWN0X3Jhd19l
eGNlcnB0OiAiTGVzIGNvbnN0cnVjdGlvbnMgZXQgb3DDqXJhdGlvbnMgbm91dmVsbGVzIG5lIHBv
dXJyb250IMOqdHJlIGF1dG9yaXPDqWVzIHF14oCZYXByw6hzIGxhIFxubWlzZSBlbiDFk3V2cmUg
ZOKAmXVuZSBwcm9jw6lkdXJlIGRlIG1vZGlmaWNhdGlvbiBkdSBQTFUiDQogICAgZXhjZXJwdF9z
aGEyNTY6IDAxNTk0ZTYzMmZiMDY0YTdlNGRkNDA4ZTY4YzE1NmI2NjcxMWFiZTZhZTJhMGU0NzBj
Nzc5ZTk0YjkxZjNhNDgNCiAgICBzZWN0aW9uX3BhZ2VfZnJhZ21lbnRfc2hhMjU2OiAxNTA0MGFk
MmYxYjRhNWZkMWM0NGJkZmVhZDI1ZDEyY2Y0Y2NkZDUzYTVmMjg3MzZlNGMzODNhZTE5YTZjYWM5
DQogICAgZXhjZXJwdF9zdGFydDogMTAwDQogICAgZXhjZXJwdF9lbmQ6IDIzNQ0KICAgIGludGVy
cHJldGF0aW9uX25vdGU6IFRoaXMgcHJlcmVxdWlzaXRlIGlzIGEgY29uZGl0aW9uIG9ubHkgYW5k
IGlzIG5vdCB0cmVhdGVkIGFzIHJvdXRlIGV2aWRlbmNlLg0KICAgIHNvdXJjZV9ydWxlX2lkOiBN
VVJFVC1BVWYwLUNPTkRJVElPTi1SVUxFLTAxDQogICAgc291cmNlX3J1bGVfZXhjZXJwdDogIkxl
cyBjb25zdHJ1Y3Rpb25zIGV0IG9ww6lyYXRpb25zIG5vdXZlbGxlcyBuZSBwb3Vycm9udCDDqnRy
ZSBhdXRvcmlzw6llcyBxdeKAmWFwcsOocyBsYSBcbm1pc2UgZW4gxZN1dnJlIGTigJl1bmUgcHJv
Y8OpZHVyZSBkZSBtb2RpZmljYXRpb24gZHUgUExVLiINCiAgICBzb3VyY2VfcnVsZV9zaGEyNTY6
IDJkOTYzMzc3NGY0MTRhOGFkMmY4ZTQyYmZjYmIyNTA3YjY3NzkwNmNhNmFjYTQ4MGYwMjM5Y2Vj
MDA3OTQyZTMNCiAgICBzb3VyY2VfcnVsZV9zdGFydDogMTAwDQogICAgc291cmNlX3J1bGVfZW5k
OiAyMzYNCiAgcm91dGVfYXNzZXNzbWVudHM6DQogIC0gcm91dGVfaWQ6IE1VUkVULUFVZjAtUk9V
VEUtMDENCiAgICByb3V0ZV9raW5kOiBDT05ESVRJT05BTF9ST1VURQ0KICAgIHBvc2l0aXZlX2V2
aWRlbmNlX2lkczoNCiAgICAtIE1VUkVULUFVRjAtSU5GUkEtUk9VVEUtMDENCiAgICBjb25kaXRp
b25fZXZpZGVuY2VfaWRzOg0KICAgIC0gTVVSRVQtQVVGMC1NT0RJRklDQVRJT04tQ09ORElUSU9O
LTAxDQogICAgZGlmZmljdWx0eV9ldmlkZW5jZV9pZHM6IFtdDQogICAgYXBwbGljYWJpbGl0eV9u
b3RlOiBUaGUgY2l0ZWQgcG9zaXRpdmUgY2F0ZWdvcnkgYW5kIGl0cyBleHBsaWNpdCBxdWFsaWZp
Y2F0aW9uIGFyZSBhc3Nlc3NlZCBhcyBvbmUgY29oZXJlbnQgcm91dGU7IEJFU1MgYXBwbGljYWJp
bGl0eSByZW1haW5zIHVucmVzb2x2ZWQuDQotIHJlc29sdmVkX3pvbmVfY2hhcHRlcl9sYWJlbDog
QQ0KICByZXZpZXdfY29tcGxldGVuZXNzOiBDT01QTEVURV9GT1JfQ09ORklHVVJFRF9VU0VfQ09O
VFJPTF9BUlRJQ0xFUw0KICByZXZpZXdlZF9zZWN0aW9uX2lkczoNCiAgLSBTRUNUSU9OLTAxNzAN
CiAgLSBTRUNUSU9OLTAxNzENCiAgcmV2aWV3X25vdGU6IEFydGljbGVzIEEgMSBhbmQgQSAyIHdl
cmUgcmV2aWV3ZWQgaW4gZnVsbCBmb3Igd3JpdHRlbiB1c2UgY29udHJvbHMuDQogIHpvbmluZ19w
cmVjaGVja19zdGF0dXM6IENPTkRJVElPTkFMX1JFVklFVw0KICB6b25pbmdfcHJlY2hlY2tfY29u
ZmlkZW5jZTogTE9XDQogIHJhdGlvbmFsZTogQXJ0aWNsZSBBIDEgY29udGFpbnMgYnJvYWQgcmVz
dHJpY3RpdmUgbGFuZ3VhZ2UgYW5kIGEgc2VwYXJhdGUgZXhjZXB0aW9uIGZvciBuZWNlc3Nhcnkg
dGVjaG5pY2FsIGFuZCBpbmZyYXN0cnVjdHVyZSB3b3Jrcy4gVGhlIHBvbGljeSByZWNvcmRzIHRo
ZSBjb25mbGljdCB3aXRob3V0IGRlY2lkaW5nIEJFU1MgcXVhbGlmaWNhdGlvbi4NCiAgbWlzc2lu
Z19pbmZvcm1hdGlvbjogRm9ybWFsIG5lY2Vzc2l0eSBhbmQgQkVTUyBpbmZyYXN0cnVjdHVyZSBj
bGFzc2lmaWNhdGlvbiwgYWdyaWN1bHR1cmFsLXpvbmUgZWZmZWN0cywgYWxsIEFydGljbGUgQSAx
LzIgcHJvdmlzaW9ucywgcHJlc2NyaXB0aW9ucywgc2Vydml0dWRlcyBhbmQgcHJvamVjdCBkZXNp
Z24uDQogIGV2aWRlbmNlOg0KICAtIGV2aWRlbmNlX2lkOiBNVVJFVC1BLVJFU1RSSUNUSU9OLTAx
DQogICAgc2VjdGlvbl9pZDogU0VDVElPTi0wMTcwDQogICAgcGFnZV9udW1iZXI6IDEyNQ0KICAg
IGV2aWRlbmNlX2tpbmQ6IFVTRV9SRVNUUklDVElPTg0KICAgIGV2aWRlbmNlX2RpcmVjdGlvbjog
U1VQUE9SVFNfRElGRklDVUxUWQ0KICAgIGV4YWN0X3Jhd19leGNlcnB0OiBTb250IGludGVyZGl0
ZXMgdG91dGVzIGxlcyBvY2N1cGF0aW9ucyBldCB1dGlsaXNhdGlvbnMgZHUgc29sIGF1dHJlcyBx
dWUgY2VsbGVzDQogICAgZXhjZXJwdF9zaGEyNTY6IGYxOGViYTlkZDU2ZjQxMDg1M2ZiNjg1ZDMw
YjZmY2M3OGVlOTUzNTljNjU3NzM4N2I3OGEyOWMzMjYxYjNjNjENCiAgICBzZWN0aW9uX3BhZ2Vf
ZnJhZ21lbnRfc2hhMjU2OiA1MTM0MmUwYWUzMzU1MDRkMGY3NTBlMDEzOGE2M2MyZmZlOTI4ZTEx
ZTU2NDg3MjEyMmJlYzY1ZWRiNGE4ZTEzDQogICAgZXhjZXJwdF9zdGFydDogNjcNCiAgICBleGNl
cnB0X2VuZDogMTQ2DQogICAgaW50ZXJwcmV0YXRpb25fbm90ZTogVGhpcyBpcyB0aGUgYnJvYWQg
cmVzdHJpY3Rpb24gcGhyYXNlLCBzZXBhcmF0ZSBmcm9tIHRoZSBleGNlcHRpb24uDQogICAgc291
cmNlX3J1bGVfaWQ6IE1VUkVULUEtUkVTVFJJQ1RJT04tRVhDRVBUSU9OLVJVTEUtMDENCiAgICBz
b3VyY2VfcnVsZV9leGNlcnB0OiAiU29udCBpbnRlcmRpdGVzIHRvdXRlcyBsZXMgb2NjdXBhdGlv
bnMgZXQgdXRpbGlzYXRpb25zIGR1IHNvbCBhdXRyZXMgcXVlIGNlbGxlcyA6IFxuLSBuw6ljZXNz
YWlyZXMgw6AgbOKAmWV4cGxvaXRhdGlvbiBhZ3JpY29sZSwgcXXigJlpbCBz4oCZYWdpc3NlIGRl
cyBjb25zdHJ1Y3Rpb25zIGV0IGV4dGVuc2lvbnMgXG7DoCB1c2FnZSBk4oCZaGFiaXRhdGlvbiBv
dSBkZXMgY29uc3RydWN0aW9ucyBldCBpbnN0YWxsYXRpb25zIMOgIHVzYWdlIGFncmljb2xlLCBc
bi0gbsOpY2Vzc2FpcmVzIGF1IGJvbiBmb25jdGlvbm5lbWVudCBkZXMgc3lzdMOobWVzIGRlIGdl
c3Rpb24gZGVzIGVhdXgsIFxuLSBuw6ljZXNzYWlyZXMgYXV4IG91dnJhZ2VzIHRlY2huaXF1ZXMg
ZXQgZOKAmWluZnJhc3RydWN0dXJlcywgXG4tIG1lbnRpb25uw6llcyDDoCBs4oCZYXJ0aWNsZSBB
MiINCiAgICBzb3VyY2VfcnVsZV9zaGEyNTY6IDRhMGEyM2VkZjM5ZjcwNzU3NTI5M2NiNzU5ZDEz
ZjZiZjIwODFkYjVkZjU4ZmYxZTliZWQwOGM5ODc3NWIxYjkNCiAgICBzb3VyY2VfcnVsZV9zdGFy
dDogNjcNCiAgICBzb3VyY2VfcnVsZV9lbmQ6IDQ3Nw0KICAtIGV2aWRlbmNlX2lkOiBNVVJFVC1B
LUlORlJBLVJPVVRFLTAxDQogICAgc2VjdGlvbl9pZDogU0VDVElPTi0wMTcwDQogICAgcGFnZV9u
dW1iZXI6IDEyNQ0KICAgIGV2aWRlbmNlX2tpbmQ6IFRFQ0hOSUNBTF9FUVVJUE1FTlRfUlVMRQ0K
ICAgIGV2aWRlbmNlX2RpcmVjdGlvbjogU1VQUE9SVFNfUE9URU5USUFMX0NPTVBBVElCSUxJVFkN
CiAgICBleGFjdF9yYXdfZXhjZXJwdDogbsOpY2Vzc2FpcmVzIGF1eCBvdXZyYWdlcyB0ZWNobmlx
dWVzIGV0IGTigJlpbmZyYXN0cnVjdHVyZXMNCiAgICBleGNlcnB0X3NoYTI1NjogN2VlZTlmN2U1
OTU3ODRiMmQ2YTRiNjA1YTRmMGI1NzAzYTA0NDZhY2I3N2I3NDIwYzcwOWI1NTE2ZTMwZTBhMg0K
ICAgIHNlY3Rpb25fcGFnZV9mcmFnbWVudF9zaGEyNTY6IDUxMzQyZTBhZTMzNTUwNGQwZjc1MGUw
MTM4YTYzYzJmZmU5MjhlMTFlNTY0ODcyMTIyYmVjNjVlZGI0YThlMTMNCiAgICBleGNlcnB0X3N0
YXJ0OiAzOTANCiAgICBleGNlcnB0X2VuZDogNDQ2DQogICAgaW50ZXJwcmV0YXRpb25fbm90ZTog
VGhpcyBpcyB0aGUgc2VwYXJhdGUgdGVjaG5pY2FsLWluZnJhc3RydWN0dXJlIGV4Y2VwdGlvbjsg
QkVTUyBuZWNlc3NpdHkgYW5kIGNsYXNzaWZpY2F0aW9uIGFyZSB1bnJlc29sdmVkLg0KICAgIHNv
dXJjZV9ydWxlX2lkOiBNVVJFVC1BLVJFU1RSSUNUSU9OLUVYQ0VQVElPTi1SVUxFLTAxDQogICAg
c291cmNlX3J1bGVfZXhjZXJwdDogIlNvbnQgaW50ZXJkaXRlcyB0b3V0ZXMgbGVzIG9jY3VwYXRp
b25zIGV0IHV0aWxpc2F0aW9ucyBkdSBzb2wgYXV0cmVzIHF1ZSBjZWxsZXMgOiBcbi0gbsOpY2Vz
c2FpcmVzIMOgIGzigJlleHBsb2l0YXRpb24gYWdyaWNvbGUsIHF14oCZaWwgc+KAmWFnaXNzZSBk
ZXMgY29uc3RydWN0aW9ucyBldCBleHRlbnNpb25zIFxuw6AgdXNhZ2UgZOKAmWhhYml0YXRpb24g
b3UgZGVzIGNvbnN0cnVjdGlvbnMgZXQgaW5zdGFsbGF0aW9ucyDDoCB1c2FnZSBhZ3JpY29sZSwg
XG4tIG7DqWNlc3NhaXJlcyBhdSBib24gZm9uY3Rpb25uZW1lbnQgZGVzIHN5c3TDqG1lcyBkZSBn
ZXN0aW9uIGRlcyBlYXV4LCBcbi0gbsOpY2Vzc2FpcmVzIGF1eCBvdXZyYWdlcyB0ZWNobmlxdWVz
IGV0IGTigJlpbmZyYXN0cnVjdHVyZXMsIFxuLSBtZW50aW9ubsOpZXMgw6AgbOKAmWFydGljbGUg
QTIiDQogICAgc291cmNlX3J1bGVfc2hhMjU2OiA0YTBhMjNlZGYzOWY3MDc1NzUyOTNjYjc1OWQx
M2Y2YmYyMDgxZGI1ZGY1OGZmMWU5YmVkMDhjOTg3NzViMWI5DQogICAgc291cmNlX3J1bGVfc3Rh
cnQ6IDY3DQogICAgc291cmNlX3J1bGVfZW5kOiA0NzcNCiAgcm91dGVfYXNzZXNzbWVudHM6DQog
IC0gcm91dGVfaWQ6IE1VUkVULUEtUk9VVEUtMDENCiAgICByb3V0ZV9raW5kOiBSRVNUUklDVElP
Tl9FWENFUFRJT05fUk9VVEUNCiAgICBwb3NpdGl2ZV9ldmlkZW5jZV9pZHM6DQogICAgLSBNVVJF
VC1BLUlORlJBLVJPVVRFLTAxDQogICAgY29uZGl0aW9uX2V2aWRlbmNlX2lkczogW10NCiAgICBk
aWZmaWN1bHR5X2V2aWRlbmNlX2lkczoNCiAgICAtIE1VUkVULUEtUkVTVFJJQ1RJT04tMDENCiAg
ICBhcHBsaWNhYmlsaXR5X25vdGU6IFRoZSByZXN0cmljdGlvbiBhbmQgaXRzIGxpc3RlZCBleGNl
cHRpb24gYXJlIGFzc2Vzc2VkIGFzIG9uZSBjb2hlcmVudCByb3V0ZTsgQkVTUyBhcHBsaWNhYmls
aXR5IHJlbWFpbnMgdW5yZXNvbHZlZC4NCi0gcmVzb2x2ZWRfem9uZV9jaGFwdGVyX2xhYmVsOiBO
DQogIHJldmlld19jb21wbGV0ZW5lc3M6IENPTVBMRVRFX0ZPUl9DT05GSUdVUkVEX1VTRV9DT05U
Uk9MX0FSVElDTEVTDQogIHJldmlld2VkX3NlY3Rpb25faWRzOg0KICAtIFNFQ1RJT04tMDE4NA0K
ICAtIFNFQ1RJT04tMDE4NQ0KICByZXZpZXdfbm90ZTogQXJ0aWNsZXMgTiAxIGFuZCBOIDIgd2Vy
ZSByZXZpZXdlZCBpbiBmdWxsIGZvciB3cml0dGVuIHVzZSBjb250cm9scy4NCiAgem9uaW5nX3By
ZWNoZWNrX3N0YXR1czogQ09ORElUSU9OQUxfUkVWSUVXDQogIHpvbmluZ19wcmVjaGVja19jb25m
aWRlbmNlOiBMT1cNCiAgcmF0aW9uYWxlOiBBcnRpY2xlIE4gMSBjb250YWlucyBhIGJyb2FkIHJl
c3RyaWN0aW9uIGFuZCBhIHNlcGFyYXRlIGV4Y2VwdGlvbiBmb3IgbmVjZXNzYXJ5IHRlY2huaWNh
bCBhbmQgaW5mcmFzdHJ1Y3R1cmUgZXF1aXBtZW50LiBUaGUgcG9saWN5IHJlY29yZHMgdGhlIGNv
bmZsaWN0IHdpdGhvdXQgZGVjaWRpbmcgQkVTUyBxdWFsaWZpY2F0aW9uLg0KICBtaXNzaW5nX2lu
Zm9ybWF0aW9uOiBGb3JtYWwgbmVjZXNzaXR5IGFuZCBCRVNTIGluZnJhc3RydWN0dXJlIGNsYXNz
aWZpY2F0aW9uLCBuYXR1cmFsLXpvbmUgZWZmZWN0cywgYWxsIEFydGljbGUgTiAxLzIgcHJvdmlz
aW9ucywgcHJlc2NyaXB0aW9ucywgc2Vydml0dWRlcyBhbmQgcHJvamVjdCBkZXNpZ24uDQogIGV2
aWRlbmNlOg0KICAtIGV2aWRlbmNlX2lkOiBNVVJFVC1OLVJFU1RSSUNUSU9OLTAxDQogICAgc2Vj
dGlvbl9pZDogU0VDVElPTi0wMTg0DQogICAgcGFnZV9udW1iZXI6IDEzNQ0KICAgIGV2aWRlbmNl
X2tpbmQ6IFVTRV9SRVNUUklDVElPTg0KICAgIGV2aWRlbmNlX2RpcmVjdGlvbjogU1VQUE9SVFNf
RElGRklDVUxUWQ0KICAgIGV4YWN0X3Jhd19leGNlcnB0OiBTb250IGludGVyZGl0ZXMsIHRvdXRl
cyBsZXMgb2NjdXBhdGlvbnMgZXQgdXRpbGlzYXRpb25zIGR1IHNvbCwgw6AgbOKAmWV4Y2VwdGlv
bg0KICAgIGV4Y2VycHRfc2hhMjU2OiA0NzgxNjczYmMxZDVjNzA0YWNkM2JlNDZjNzA2ODA1ZjZl
YWViYWNkNGZjNGIyMjk2ODc3YWY4YmNlNjY4OGVmDQogICAgc2VjdGlvbl9wYWdlX2ZyYWdtZW50
X3NoYTI1NjogMGNhYzNhMWFlYjU2ODU5NjcwYjcxNWMxN2UxYzE2Njk1OTE0N2EwZjkwYTE5YTEy
Zjg3ZTAwMjViMjYzZTE5NQ0KICAgIGV4Y2VycHRfc3RhcnQ6IDY5DQogICAgZXhjZXJwdF9lbmQ6
IDE0Ng0KICAgIGludGVycHJldGF0aW9uX25vdGU6IFRoaXMgaXMgdGhlIGJyb2FkIHJlc3RyaWN0
aW9uIHBocmFzZSwgc2VwYXJhdGUgZnJvbSBpdHMgbGlzdGVkIGV4Y2VwdGlvbnMuDQogICAgc291
cmNlX3J1bGVfaWQ6IE1VUkVULU4tUkVTVFJJQ1RJT04tRVhDRVBUSU9OLVJVTEUtMDENCiAgICBz
b3VyY2VfcnVsZV9leGNlcnB0OiAiU29udCBpbnRlcmRpdGVzLCB0b3V0ZXMgbGVzIG9jY3VwYXRp
b25zIGV0IHV0aWxpc2F0aW9ucyBkdSBzb2wsIMOgIGzigJlleGNlcHRpb24gOiBcbiBcbi0gZGVz
IG9jY3VwYXRpb25zIGV0IHV0aWxpc2F0aW9ucyBkdSBzb2wgc291bWlzZXMgw6AgZGVzIGNvbmRp
dGlvbnMgcGFydGljdWxpw6hyZXMgZXQgXG5yw6lwZXJ0b3Jpw6llcyDDoCBs4oCZYXJ0aWNsZSBO
IDIsIFxuLSBkZXMgw6lxdWlwZW1lbnRzIG7DqWNlc3NhaXJlcyBhdXggb3V2cmFnZXMgdGVjaG5p
cXVlcyBldCBk4oCZaW5mcmFzdHJ1Y3R1cmUsIFxuLSBkZXMgYW3DqW5hZ2VtZW50cyBsacOpcyBh
dXggb3V2cmFnZXMgdGVjaG5pcXVlcyBuw6ljZXNzYWlyZXMgYXUgZm9uY3Rpb25uZW1lbnQgZGVz
IFxuc2VydmljZXMgcHVibGljcywgXG4tIGRlcyDDqXF1aXBlbWVudHMgbsOpY2Vzc2FpcmVzIGF1
IGJvbiBmb25jdGlvbm5lbWVudCBkZXMgc3lzdMOobWVzIGRlIGdlc3Rpb24gZGVzIFxuZWF1eCwg
XG4tIGVuIHNlY3RldXIgTkwgOiBcbi0gbGVzIGNvbnN0cnVjdGlvbnMsIGluc3RhbGxhdGlvbnMg
ZXQgdXRpbGlzYXRpb25zIGR1IHNvbCBkZXN0aW7DqWVzIMOgIGzigJlhY2N1ZWlsIGRlcyBcbmFj
dGl2aXTDqXMgZGUgbG9pc2lycyBldCBk4oCZw6lxdWlwZW1lbnRzIHB1YmxpY3Mgc3BvcnRpZnMg
b3Ugc29jaW8tY3VsdHVyZWxzLCBcbi0gbGVzIHRlcnJhaW5zIGRlIGNhbXBpbmcgZXQgZGUgY2Fy
YXZhbmluZywgZXhjZXB0w6kgZGFucyBsZSBzZWN0ZXVyIGlub25kYWJsZSBcbnJlcMOpcsOpIGF1
IHBsYW4gZGUgem9uYWdlLiINCiAgICBzb3VyY2VfcnVsZV9zaGEyNTY6IGM0MzQ2NzA1MzFiNDNi
YmMyM2RkMjRjMWZhMDFiYmExZWVkYWVlMGJhOWUyNDFiOWY0MzIyNTVjNzRkYjMwZDINCiAgICBz
b3VyY2VfcnVsZV9zdGFydDogNjkNCiAgICBzb3VyY2VfcnVsZV9lbmQ6IDgxOA0KICAtIGV2aWRl
bmNlX2lkOiBNVVJFVC1OLUlORlJBLVJPVVRFLTAxDQogICAgc2VjdGlvbl9pZDogU0VDVElPTi0w
MTg0DQogICAgcGFnZV9udW1iZXI6IDEzNQ0KICAgIGV2aWRlbmNlX2tpbmQ6IFRFQ0hOSUNBTF9F
UVVJUE1FTlRfUlVMRQ0KICAgIGV2aWRlbmNlX2RpcmVjdGlvbjogU1VQUE9SVFNfUE9URU5USUFM
X0NPTVBBVElCSUxJVFkNCiAgICBleGFjdF9yYXdfZXhjZXJwdDogZGVzIMOpcXVpcGVtZW50cyBu
w6ljZXNzYWlyZXMgYXV4IG91dnJhZ2VzIHRlY2huaXF1ZXMgZXQgZOKAmWluZnJhc3RydWN0dXJl
DQogICAgZXhjZXJwdF9zaGEyNTY6IGIyOGNiMzM5OTM2ZTg1OThmYWVlNWM1YmJhNmYxYmU1ZjUy
ZTQwYjFjZTZmMzNmZTg1NGFlMWRhZmY1NGQ4NjcNCiAgICBzZWN0aW9uX3BhZ2VfZnJhZ21lbnRf
c2hhMjU2OiAwY2FjM2ExYWViNTY4NTk2NzBiNzE1YzE3ZTFjMTY2OTU5MTQ3YTBmOTBhMTlhMTJm
ODdlMDAyNWIyNjNlMTk1DQogICAgZXhjZXJwdF9zdGFydDogMjcwDQogICAgZXhjZXJwdF9lbmQ6
IDM0MQ0KICAgIGludGVycHJldGF0aW9uX25vdGU6IFRoaXMgaXMgdGhlIHNlcGFyYXRlIHRlY2hu
aWNhbC1pbmZyYXN0cnVjdHVyZSBleGNlcHRpb247IEJFU1MgbmVjZXNzaXR5IGFuZCBjbGFzc2lm
aWNhdGlvbiBhcmUgdW5yZXNvbHZlZC4NCiAgICBzb3VyY2VfcnVsZV9pZDogTVVSRVQtTi1SRVNU
UklDVElPTi1FWENFUFRJT04tUlVMRS0wMQ0KICAgIHNvdXJjZV9ydWxlX2V4Y2VycHQ6ICJTb250
IGludGVyZGl0ZXMsIHRvdXRlcyBsZXMgb2NjdXBhdGlvbnMgZXQgdXRpbGlzYXRpb25zIGR1IHNv
bCwgw6AgbOKAmWV4Y2VwdGlvbiA6IFxuIFxuLSBkZXMgb2NjdXBhdGlvbnMgZXQgdXRpbGlzYXRp
b25zIGR1IHNvbCBzb3VtaXNlcyDDoCBkZXMgY29uZGl0aW9ucyBwYXJ0aWN1bGnDqHJlcyBldCBc
bnLDqXBlcnRvcmnDqWVzIMOgIGzigJlhcnRpY2xlIE4gMiwgXG4tIGRlcyDDqXF1aXBlbWVudHMg
bsOpY2Vzc2FpcmVzIGF1eCBvdXZyYWdlcyB0ZWNobmlxdWVzIGV0IGTigJlpbmZyYXN0cnVjdHVy
ZSwgXG4tIGRlcyBhbcOpbmFnZW1lbnRzIGxpw6lzIGF1eCBvdXZyYWdlcyB0ZWNobmlxdWVzIG7D
qWNlc3NhaXJlcyBhdSBmb25jdGlvbm5lbWVudCBkZXMgXG5zZXJ2aWNlcyBwdWJsaWNzLCBcbi0g
ZGVzIMOpcXVpcGVtZW50cyBuw6ljZXNzYWlyZXMgYXUgYm9uIGZvbmN0aW9ubmVtZW50IGRlcyBz
eXN0w6htZXMgZGUgZ2VzdGlvbiBkZXMgXG5lYXV4LCBcbi0gZW4gc2VjdGV1ciBOTCA6IFxuLSBs
ZXMgY29uc3RydWN0aW9ucywgaW5zdGFsbGF0aW9ucyBldCB1dGlsaXNhdGlvbnMgZHUgc29sIGRl
c3RpbsOpZXMgw6AgbOKAmWFjY3VlaWwgZGVzIFxuYWN0aXZpdMOpcyBkZSBsb2lzaXJzIGV0IGTi
gJnDqXF1aXBlbWVudHMgcHVibGljcyBzcG9ydGlmcyBvdSBzb2Npby1jdWx0dXJlbHMsIFxuLSBs
ZXMgdGVycmFpbnMgZGUgY2FtcGluZyBldCBkZSBjYXJhdmFuaW5nLCBleGNlcHTDqSBkYW5zIGxl
IHNlY3RldXIgaW5vbmRhYmxlIFxucmVww6lyw6kgYXUgcGxhbiBkZSB6b25hZ2UuIg0KICAgIHNv
dXJjZV9ydWxlX3NoYTI1NjogYzQzNDY3MDUzMWI0M2JiYzIzZGQyNGMxZmEwMWJiYTFlZWRhZWUw
YmE5ZTI0MWI5ZjQzMjI1NWM3NGRiMzBkMg0KICAgIHNvdXJjZV9ydWxlX3N0YXJ0OiA2OQ0KICAg
IHNvdXJjZV9ydWxlX2VuZDogODE4DQogIHJvdXRlX2Fzc2Vzc21lbnRzOg0KICAtIHJvdXRlX2lk
OiBNVVJFVC1OLVJPVVRFLTAxDQogICAgcm91dGVfa2luZDogUkVTVFJJQ1RJT05fRVhDRVBUSU9O
X1JPVVRFDQogICAgcG9zaXRpdmVfZXZpZGVuY2VfaWRzOg0KICAgIC0gTVVSRVQtTi1JTkZSQS1S
T1VURS0wMQ0KICAgIGNvbmRpdGlvbl9ldmlkZW5jZV9pZHM6IFtdDQogICAgZGlmZmljdWx0eV9l
dmlkZW5jZV9pZHM6DQogICAgLSBNVVJFVC1OLVJFU1RSSUNUSU9OLTAxDQogICAgYXBwbGljYWJp
bGl0eV9ub3RlOiBUaGUgcmVzdHJpY3Rpb24gYW5kIGl0cyBsaXN0ZWQgZXhjZXB0aW9uIGFyZSBh
c3Nlc3NlZCBhcyBvbmUgY29oZXJlbnQgcm91dGU7IEJFU1MgYXBwbGljYWJpbGl0eSByZW1haW5z
IHVucmVzb2x2ZWQuDQo=
```
