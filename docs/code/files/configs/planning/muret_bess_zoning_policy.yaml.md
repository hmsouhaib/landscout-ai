# `configs/planning/muret_bess_zoning_policy.yaml`

## File identity

- Repository path: `configs/planning/muret_bess_zoning_policy.yaml`
- File type: YAML checked-in configuration/policy/source lock
- Responsibility: Defines the source-locked Muret written-zoning evidence occurrences, routes, chapter decisions, and applicability notes.
- Source SHA256: `879d50627c063bb10096950d004cf4d4e446ff04ef9a1178b3e3fb28e2ffdae3`

## 1. Purpose

Defines the source-locked Muret written-zoning evidence occurrences, routes, chapter decisions, and applicability notes.

## 2. Position in LandScout architecture

The exact YAML bytes are parsed by `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config` into `landscout.stages.interpret_bess_zoning.BessZoningPolicyConfig`. Runtime consumers include `interpret_bess_zoning`.

## 3. Imports and dependencies

Not applicable to YAML. Python/Pydantic consumers are named above and reproduced below.

## 4. Contract taxonomy

Every row below is a configuration field/list leaf. It is not a DataFrame column unless a consuming stage explicitly copies it into a documented result schema.

| Exact YAML path | Checked-in value | Runtime type | Required/nullability/allowed-domain/unit contract | Semantic role | Consumers |
|---|---|---|---|---|---|
| `schema_version` | `5` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required supported schema integer; accepted versions are pinned by the owning Literal/validator | Selects the strict configuration schema; unsupported versions are rejected. | `interpret_bess_zoning` |
| `policy_profile` | `"muret_bess_written_zoning_v6"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Identifies the versioned semantic policy snapshot. | `interpret_bess_zoning` |
| `planning_precheck_scope` | `"WRITTEN_ZONING_REGULATION_ONLY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `planning precheck scope` under the exact parent path `<root>`. | `interpret_bess_zoning` |
| `review_scope` | `"CONFIGURED_USE_CONTROL_ARTICLES_ONLY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review scope` under the exact parent path `<root>`. | `interpret_bess_zoning` |
| `source_lock.document_id` | `"33edb4c9f6943c88d8d92518bff20bec"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `document id` under the exact parent path `source_lock`. | `interpret_bess_zoning` |
| `source_lock.archive_sha256` | `"9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `archive_sha256`. | `interpret_bess_zoning` |
| `source_lock.pdf_sha256` | `"5358ebad6b0cda6de681ba3536e29b8b6291fb701c7d3711f4ee1d6fdb85c6fb"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `pdf_sha256`. | `interpret_bess_zoning` |
| `source_lock.index_content_sha256` | `"6a0009228ca17128c0a8bb329d9c2277a1b6638708a67b913b72ee93063e42cd"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `index_content_sha256`. | `interpret_bess_zoning` |
| `source_lock.structure_result_content_sha256` | `"16f8a9edfff0d330f69579310da085f804f4641de973d98e0046bff5ea96b03c"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `structure_result_content_sha256`. | `interpret_bess_zoning` |
| `source_lock.structure_profile` | `"muret_plu_20240215_v1"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `structure profile` under the exact parent path `source_lock`. | `interpret_bess_zoning` |
| `required_zone_article_numbers[0]` | `"1"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `required_zone_article_numbers`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `required_zone_article_numbers[1]` | `"2"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `required_zone_article_numbers`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[0].resolved_zone_chapter_label` | `"UA"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[0]`. | `interpret_bess_zoning` |
| `chapters[0].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[0]`. | `interpret_bess_zoning` |
| `chapters[0].reviewed_section_ids[0]` | `"SECTION-0008"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[0].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[0].reviewed_section_ids[1]` | `"SECTION-0009"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[0].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[0].review_note` | `"Articles UA 1 and UA 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[0]`. | `interpret_bess_zoning` |
| `chapters[0].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[0]`. | `interpret_bess_zoning` |
| `chapters[0].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[0]`. | `interpret_bess_zoning` |
| `chapters[0].rationale` | `"Article UA 2 states a possible ICPE route and states separate compatibility and local-necessity conditions; whether a BESS qualifies remains unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[0]`. | `interpret_bess_zoning` |
| `chapters[0].missing_information` | `"BESS planning-use and ICPE classification, application of all Article UA 1/2 provisions, prescriptions, servitudes, project effects and design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].evidence_id` | `"MURET-UA-ICPE-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].section_id` | `"SECTION-0009"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].page_number` | `8` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].section_page_fragment_sha256` | `"2da8d15fad096a694d7b56ecfc1d61d0ba375aac1c254794d63388524cc755f6"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].excerpt_start` | `100` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].excerpt_end` | `183` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].interpretation_note` | `"This is a literal ICPE route phrase; it does not establish that a BESS is an applicable ICPE use."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].source_rule_id` | `"MURET-UA-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition d’être compatibles avec le milieu environnant et nécessaires à la vie  du \nquartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].source_rule_sha256` | `"8def59e860d434e482899e9709520d221dd576e41e00f276bbe9c87e5127a8df"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].source_rule_start` | `100` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[0].source_rule_end` | `301` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[0].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].evidence_id` | `"MURET-UA-ICPE-CONDITION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].section_id` | `"SECTION-0009"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].page_number` | `8` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].evidence_direction` | `"CONDITION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].section_page_fragment_sha256` | `"2da8d15fad096a694d7b56ecfc1d61d0ba375aac1c254794d63388524cc755f6"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].excerpt_start` | `210` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].excerpt_end` | `265` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification attached to the ICPE route."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].source_rule_id` | `"MURET-UA-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition d’être compatibles avec le milieu environnant et nécessaires à la vie  du \nquartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].source_rule_sha256` | `"8def59e860d434e482899e9709520d221dd576e41e00f276bbe9c87e5127a8df"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].source_rule_start` | `100` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].evidence[1].source_rule_end` | `301` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[0].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[0].route_assessments[0].route_id` | `"MURET-UA-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[0].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[0].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[0].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[0].route_assessments[0].positive_evidence_ids[0]` | `"MURET-UA-ICPE-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[0].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[0].route_assessments[0].condition_evidence_ids[0]` | `"MURET-UA-ICPE-CONDITION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[0].route_assessments[0].condition_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[0].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[0].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[1].resolved_zone_chapter_label` | `"UB"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[1]`. | `interpret_bess_zoning` |
| `chapters[1].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[1]`. | `interpret_bess_zoning` |
| `chapters[1].reviewed_section_ids[0]` | `"SECTION-0021"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[1].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[1].reviewed_section_ids[1]` | `"SECTION-0022"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[1].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[1].review_note` | `"Articles UB 1 and UB 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[1]`. | `interpret_bess_zoning` |
| `chapters[1].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[1]`. | `interpret_bess_zoning` |
| `chapters[1].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[1]`. | `interpret_bess_zoning` |
| `chapters[1].rationale` | `"Article UB 2 states a possible ICPE route and separate compatibility and local-necessity conditions; BESS applicability is unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[1]`. | `interpret_bess_zoning` |
| `chapters[1].missing_information` | `"BESS planning-use and ICPE classification, application of all Article UB 1/2 provisions, prescriptions, servitudes, project effects and design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].evidence_id` | `"MURET-UB-ICPE-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].section_id` | `"SECTION-0022"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].page_number` | `22` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].section_page_fragment_sha256` | `"7c678bbc92c2271fbb02f0c228f51e0b408b862780731b78f301b37731a894f3"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].excerpt_start` | `98` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].excerpt_end` | `181` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].interpretation_note` | `"This is a literal ICPE route phrase, not a BESS authorization."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].source_rule_id` | `"MURET-UB-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].source_rule_start` | `98` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[0].source_rule_end` | `307` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[1].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].evidence_id` | `"MURET-UB-ICPE-CONDITION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].section_id` | `"SECTION-0022"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].page_number` | `22` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].evidence_direction` | `"CONDITION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].section_page_fragment_sha256` | `"7c678bbc92c2271fbb02f0c228f51e0b408b862780731b78f301b37731a894f3"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].excerpt_start` | `217` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].excerpt_end` | `272` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].source_rule_id` | `"MURET-UB-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].source_rule_start` | `98` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].evidence[1].source_rule_end` | `307` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[1].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[1].route_assessments[0].route_id` | `"MURET-UB-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[1].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[1].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[1].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[1].route_assessments[0].positive_evidence_ids[0]` | `"MURET-UB-ICPE-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[1].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[1].route_assessments[0].condition_evidence_ids[0]` | `"MURET-UB-ICPE-CONDITION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[1].route_assessments[0].condition_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[1].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[1].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[2].resolved_zone_chapter_label` | `"UC"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[2]`. | `interpret_bess_zoning` |
| `chapters[2].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[2]`. | `interpret_bess_zoning` |
| `chapters[2].reviewed_section_ids[0]` | `"SECTION-0036"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[2].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[2].reviewed_section_ids[1]` | `"SECTION-0037"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[2].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[2].review_note` | `"Articles UC 1 and UC 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[2]`. | `interpret_bess_zoning` |
| `chapters[2].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[2]`. | `interpret_bess_zoning` |
| `chapters[2].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[2]`. | `interpret_bess_zoning` |
| `chapters[2].rationale` | `"Article UC 2 states a possible ICPE route subject to explicit compatibility and local-necessity conditions; BESS applicability is unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[2]`. | `interpret_bess_zoning` |
| `chapters[2].missing_information` | `"BESS planning-use and ICPE classification, application of all Article UC 1/2 provisions, prescriptions, servitudes, project effects and design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[2]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].evidence_id` | `"MURET-UC-ICPE-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].section_id` | `"SECTION-0037"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].page_number` | `36` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].section_page_fragment_sha256` | `"f6103c4139a65d12a9b6bf4c5edd37382fa6a2fa642c3a5805aa2898b1121365"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].excerpt_start` | `98` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].excerpt_end` | `181` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].interpretation_note` | `"This is a literal ICPE route phrase, not a BESS authorization."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].source_rule_id` | `"MURET-UC-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].source_rule_start` | `98` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[0].source_rule_end` | `307` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[2].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].evidence_id` | `"MURET-UC-ICPE-CONDITION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].section_id` | `"SECTION-0037"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].page_number` | `36` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].evidence_direction` | `"CONDITION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].section_page_fragment_sha256` | `"f6103c4139a65d12a9b6bf4c5edd37382fa6a2fa642c3a5805aa2898b1121365"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].excerpt_start` | `217` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].excerpt_end` | `272` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].source_rule_id` | `"MURET-UC-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].source_rule_start` | `98` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].evidence[1].source_rule_end` | `307` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[2].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[2].route_assessments[0].route_id` | `"MURET-UC-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[2].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[2].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[2].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[2].route_assessments[0].positive_evidence_ids[0]` | `"MURET-UC-ICPE-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[2].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[2].route_assessments[0].condition_evidence_ids[0]` | `"MURET-UC-ICPE-CONDITION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[2].route_assessments[0].condition_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[2].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[2].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[3].resolved_zone_chapter_label` | `"UD"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[3]`. | `interpret_bess_zoning` |
| `chapters[3].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[3]`. | `interpret_bess_zoning` |
| `chapters[3].reviewed_section_ids[0]` | `"SECTION-0051"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[3].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[3].reviewed_section_ids[1]` | `"SECTION-0052"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[3].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[3].review_note` | `"Articles UD 1 and UD 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[3]`. | `interpret_bess_zoning` |
| `chapters[3].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[3]`. | `interpret_bess_zoning` |
| `chapters[3].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[3]`. | `interpret_bess_zoning` |
| `chapters[3].rationale` | `"Article UD 2 states a possible ICPE route subject to explicit compatibility and local-necessity conditions; BESS applicability is unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[3]`. | `interpret_bess_zoning` |
| `chapters[3].missing_information` | `"BESS planning-use and ICPE classification, application of all Article UD 1/2 provisions, prescriptions, servitudes, project effects and design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[3]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].evidence_id` | `"MURET-UD-ICPE-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].section_id` | `"SECTION-0052"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].page_number` | `48` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].section_page_fragment_sha256` | `"67701fcf91b57f6d4c00a0c26d95c2904e736bd70c3da1bd49b949f2d60f6e9a"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].excerpt_start` | `446` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].excerpt_end` | `529` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].interpretation_note` | `"This is a literal ICPE route phrase, not a BESS authorization."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].source_rule_id` | `"MURET-UD-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].source_rule_start` | `446` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[0].source_rule_end` | `655` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[3].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].evidence_id` | `"MURET-UD-ICPE-CONDITION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].section_id` | `"SECTION-0052"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].page_number` | `48` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].evidence_direction` | `"CONDITION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].section_page_fragment_sha256` | `"67701fcf91b57f6d4c00a0c26d95c2904e736bd70c3da1bd49b949f2d60f6e9a"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].excerpt_start` | `565` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].excerpt_end` | `620` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].source_rule_id` | `"MURET-UD-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].source_rule_start` | `446` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].evidence[1].source_rule_end` | `655` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[3].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[3].route_assessments[0].route_id` | `"MURET-UD-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[3].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[3].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[3].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[3].route_assessments[0].positive_evidence_ids[0]` | `"MURET-UD-ICPE-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[3].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[3].route_assessments[0].condition_evidence_ids[0]` | `"MURET-UD-ICPE-CONDITION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[3].route_assessments[0].condition_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[3].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[3].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[4].resolved_zone_chapter_label` | `"UF"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[4]`. | `interpret_bess_zoning` |
| `chapters[4].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[4]`. | `interpret_bess_zoning` |
| `chapters[4].reviewed_section_ids[0]` | `"SECTION-0065"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[4].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[4].reviewed_section_ids[1]` | `"SECTION-0066"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[4].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[4].review_note` | `"Articles UF 1 and UF 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[4]`. | `interpret_bess_zoning` |
| `chapters[4].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[4]`. | `interpret_bess_zoning` |
| `chapters[4].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[4]`. | `interpret_bess_zoning` |
| `chapters[4].rationale` | `"Article UF 2 states a possible ICPE route subject to explicit compatibility and local-necessity conditions; sector and BESS applicability remain unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[4]`. | `interpret_bess_zoning` |
| `chapters[4].missing_information` | `"BESS planning-use, sector and ICPE classification, application of all Article UF 1/2 provisions, prescriptions, servitudes, project effects and design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[4]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].evidence_id` | `"MURET-UF-ICPE-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].section_id` | `"SECTION-0066"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].page_number` | `60` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].section_page_fragment_sha256` | `"4fceabfce9821f94b0c023052a654d1d515c86e81056605b876cfbccf54e84ec"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].excerpt_start` | `510` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].excerpt_end` | `593` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].interpretation_note` | `"This is a literal ICPE route phrase, not a BESS authorization."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].source_rule_id` | `"MURET-UF-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].source_rule_start` | `510` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[0].source_rule_end` | `719` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[4].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].evidence_id` | `"MURET-UF-ICPE-CONDITION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].section_id` | `"SECTION-0066"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].page_number` | `60` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].evidence_direction` | `"CONDITION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].section_page_fragment_sha256` | `"4fceabfce9821f94b0c023052a654d1d515c86e81056605b876cfbccf54e84ec"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].excerpt_start` | `629` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].excerpt_end` | `684` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].source_rule_id` | `"MURET-UF-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].source_rule_start` | `510` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].evidence[1].source_rule_end` | `719` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[4].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[4].route_assessments[0].route_id` | `"MURET-UF-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[4].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[4].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[4].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[4].route_assessments[0].positive_evidence_ids[0]` | `"MURET-UF-ICPE-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[4].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[4].route_assessments[0].condition_evidence_ids[0]` | `"MURET-UF-ICPE-CONDITION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[4].route_assessments[0].condition_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[4].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[4].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[5].resolved_zone_chapter_label` | `"UP"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[5]`. | `interpret_bess_zoning` |
| `chapters[5].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[5]`. | `interpret_bess_zoning` |
| `chapters[5].reviewed_section_ids[0]` | `"SECTION-0080"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[5].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[5].reviewed_section_ids[1]` | `"SECTION-0081"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[5].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[5].review_note` | `"Articles UP 1 and UP 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[5]`. | `interpret_bess_zoning` |
| `chapters[5].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[5]`. | `interpret_bess_zoning` |
| `chapters[5].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[5]`. | `interpret_bess_zoning` |
| `chapters[5].rationale` | `"Article UP 1 states a general restriction with a public or collective-interest equipment exception; whether a BESS belongs to that excepted category remains unresolved. The separate Article UP 2 ICPE rule is retained only as context because BESS ICPE applicability has not been established."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[5]`. | `interpret_bess_zoning` |
| `chapters[5].missing_information` | `"Formal classification as public or collective-interest equipment, BESS ICPE applicability, all Article UP 1/2 provisions, prescriptions, servitudes, project effects and design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[5]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].evidence_id` | `"MURET-UP-PUBLIC-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].section_id` | `"SECTION-0080"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].page_number` | `71` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].evidence_kind` | `"PUBLIC_INTEREST_EXCEPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].exact_raw_excerpt` | `"à usage d'équipement public  \nou d'intérêt collectif"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].excerpt_sha256` | `"301da057642435982e74e393d12e292b81682d4d7672dec60e40a8e10e84530c"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].section_page_fragment_sha256` | `"06f8ea334a2fa8ce62337d6a3c59d24e03f9d8b9d8cc9e936c92e97b771babbb"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].excerpt_start` | `125` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].excerpt_end` | `177` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].interpretation_note` | `"This is the exact category exception; the policy does not decide that a BESS belongs to it."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].source_rule_id` | `"MURET-UP-ROUTE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].source_rule_excerpt` | `"Toutes constructions ou  installations autres que celles à usage d'équipement public  \nou d'intérêt collectif, services annexes et les logements de fonction y afférent."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].source_rule_sha256` | `"de2615e25b83708c84e9ff9313060dca708ca0a8bc693777b627951bc2de394c"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].source_rule_start` | `68` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[0].source_rule_end` | `236` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[5].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].evidence_id` | `"MURET-UP-RESTRICTION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].section_id` | `"SECTION-0080"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].page_number` | `71` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].evidence_kind` | `"USE_RESTRICTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].evidence_direction` | `"SUPPORTS_DIFFICULTY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].exact_raw_excerpt` | `"Toutes constructions ou  installations autres que celles"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].excerpt_sha256` | `"edfbe54799b8a6c0e74d86b0e9596e8c68471f11105783b3e4e93825f8308462"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].section_page_fragment_sha256` | `"06f8ea334a2fa8ce62337d6a3c59d24e03f9d8b9d8cc9e936c92e97b771babbb"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].excerpt_start` | `68` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].excerpt_end` | `124` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].interpretation_note` | `"This is the general restriction surrounding the public or collective-interest exception; it does not decide whether a BESS belongs to the exception."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].source_rule_id` | `"MURET-UP-ROUTE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].source_rule_excerpt` | `"Toutes constructions ou  installations autres que celles à usage d'équipement public  \nou d'intérêt collectif, services annexes et les logements de fonction y afférent."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].source_rule_sha256` | `"de2615e25b83708c84e9ff9313060dca708ca0a8bc693777b627951bc2de394c"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].source_rule_start` | `68` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[1].source_rule_end` | `236` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[5].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].evidence_id` | `"MURET-UP-ICPE-CONDITION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].section_id` | `"SECTION-0081"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].page_number` | `71` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].evidence_direction` | `"CONTEXT_ONLY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].section_page_fragment_sha256` | `"7a5fac0b06f32a02a34031e9db62b2ccd59a63099fdb378079ab41c4252aed09"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].excerpt_start` | `478` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].excerpt_end` | `533` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].interpretation_note` | `"This separate ICPE condition is context only unless a future evidence step establishes that the BESS project is subject to it."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].source_rule_id` | `"MURET-UP-CONDITION-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].source_rule_start` | `359` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].evidence[2].source_rule_end` | `568` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[5].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[5].route_assessments[0].route_id` | `"MURET-UP-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[5].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[5].route_assessments[0].route_kind` | `"RESTRICTION_EXCEPTION_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[5].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[5].route_assessments[0].positive_evidence_ids[0]` | `"MURET-UP-PUBLIC-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[5].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[5].route_assessments[0].difficulty_evidence_ids[0]` | `"MURET-UP-RESTRICTION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[5].route_assessments[0].difficulty_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[5].route_assessments[0].applicability_note` | `"The Article UP 1 restriction and its public or collective-interest exception are assessed as one coherent route; BESS membership remains unresolved. The separate ICPE rule is not used to qualify this route."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[5].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[6].resolved_zone_chapter_label` | `"AU"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[6]`. | `interpret_bess_zoning` |
| `chapters[6].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[6]`. | `interpret_bess_zoning` |
| `chapters[6].reviewed_section_ids[0]` | `"SECTION-0095"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[6].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[6].reviewed_section_ids[1]` | `"SECTION-0096"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[6].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[6].review_note` | `"Articles AU 1 and AU 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[6]`. | `interpret_bess_zoning` |
| `chapters[6].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[6]`. | `interpret_bess_zoning` |
| `chapters[6].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[6]`. | `interpret_bess_zoning` |
| `chapters[6].rationale` | `"Infrastructure prerequisites were not treated as a route; Article AU 2 separately states a possible ICPE route with compatibility and necessity conditions."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[6]`. | `interpret_bess_zoning` |
| `chapters[6].missing_information` | `"BESS planning-use and ICPE classification, infrastructure and sector conditions, all Article AU 1/2 provisions, prescriptions, servitudes, project effects and design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[6]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].evidence_id` | `"MURET-AU-ICPE-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].section_id` | `"SECTION-0096"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].page_number` | `81` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].section_page_fragment_sha256` | `"545168e51a47f7c8b9519575b6d870ab70e11d1043df847e3b5b8661a890652e"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].excerpt_start` | `1474` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].excerpt_end` | `1557` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].interpretation_note` | `"This is the explicit ICPE route phrase; infrastructure prerequisites alone were not used as positive evidence."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].source_rule_id` | `"MURET-AU-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].source_rule_start` | `1474` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[0].source_rule_end` | `1683` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[6].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].evidence_id` | `"MURET-AU-ICPE-CONDITION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].section_id` | `"SECTION-0096"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].page_number` | `81` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].evidence_direction` | `"CONDITION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].section_page_fragment_sha256` | `"545168e51a47f7c8b9519575b6d870ab70e11d1043df847e3b5b8661a890652e"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].excerpt_start` | `1593` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].excerpt_end` | `1648` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].source_rule_id` | `"MURET-AU-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].source_rule_start` | `1474` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].evidence[1].source_rule_end` | `1683` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[6].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[6].route_assessments[0].route_id` | `"MURET-AU-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[6].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[6].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[6].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[6].route_assessments[0].positive_evidence_ids[0]` | `"MURET-AU-ICPE-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[6].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[6].route_assessments[0].condition_evidence_ids[0]` | `"MURET-AU-ICPE-CONDITION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[6].route_assessments[0].condition_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[6].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[6].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[7].resolved_zone_chapter_label` | `"AUp"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[7]`. | `interpret_bess_zoning` |
| `chapters[7].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[7]`. | `interpret_bess_zoning` |
| `chapters[7].reviewed_section_ids[0]` | `"SECTION-0110"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[7].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[7].reviewed_section_ids[1]` | `"SECTION-0111"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[7].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[7].review_note` | `"Articles AUp 1 and AUp 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[7]`. | `interpret_bess_zoning` |
| `chapters[7].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[7]`. | `interpret_bess_zoning` |
| `chapters[7].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[7]`. | `interpret_bess_zoning` |
| `chapters[7].rationale` | `"Article AUp 1 states a public or collective-interest equipment exception under Article AUp 2 conditions. Article AUp 2 requires indispensable access, road and network infrastructure before authorization. Its separate ICPE rule is retained only as context because BESS ICPE applicability has not been established."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[7]`. | `interpret_bess_zoning` |
| `chapters[7].missing_information` | `"Formal BESS classification as public or collective-interest equipment, satisfaction of the Article AUp 2 infrastructure prerequisite, BESS ICPE applicability, all Article AUp 1/2 provisions, prescriptions, servitudes, project effects and design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[7]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].evidence_id` | `"MURET-AUP-PUBLIC-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].section_id` | `"SECTION-0110"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].page_number` | `93` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].evidence_kind` | `"PUBLIC_INTEREST_EXCEPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].exact_raw_excerpt` | `"à usage d'équipement public ou \nd'intérêt collectif"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].excerpt_sha256` | `"f7be71b131f97c74c8107bc6f14bf2a980d8c3f769a52eef7a899249108c35a2"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].section_page_fragment_sha256` | `"4f5b79666858745347ec811398acd19d2761705b3b3d2a31ffd9f4c54a5c93d5"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].excerpt_start` | `125` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].excerpt_end` | `176` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].interpretation_note` | `"This is the exact category exception; BESS membership is unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].source_rule_id` | `"MURET-AUp-ROUTE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].source_rule_excerpt` | `"Toutes constructions ou installations autres que celles à usage d'équipement public ou \nd'intérêt collectif, leurs services annexes et les logements de fonction y afférent  sous \nconditions de l’article AUP-2."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].source_rule_sha256` | `"01870b2aa63b15491cbf644501dfa8238a94f980d426d15ee2743cc5796c24c3"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].source_rule_start` | `69` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[0].source_rule_end` | `278` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[7].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].evidence_id` | `"MURET-AUP-INFRASTRUCTURE-CONDITION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].section_id` | `"SECTION-0111"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].page_number` | `93` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].evidence_kind` | `"ACCESS_OR_NETWORK_CONDITION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].evidence_direction` | `"CONDITION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].exact_raw_excerpt` | `"Les constructions et opérations ne pourront être autorisées qu’après réalisation des  \néquipements d’infrastructure indispensable à leur fonctionnement (accès, voirie et  \nréseaux divers) conformément aux articles AUp3 et AUp4."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].excerpt_sha256` | `"b2be9b1f7e3597802d5ed2c301a7e34bb7a9eecaeab55898e55306719b1b315b"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].section_page_fragment_sha256` | `"57540d28148aefc320fcc8baa9a92df7e382d72299da6e804a3ebfaf52408b44"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].excerpt_start` | `98` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].excerpt_end` | `325` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].interpretation_note` | `"This is the general Article AUp 2 infrastructure prerequisite expressly referenced by Article AUp 1; the policy does not decide that it is satisfied."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].source_rule_id` | `"MURET-AUp-INFRASTRUCTURE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].source_rule_excerpt` | `"Les constructions et opérations ne pourront être autorisées qu’après réalisation des  \néquipements d’infrastructure indispensable à leur fonctionnement (accès, voirie et  \nréseaux divers) conformément aux articles AUp3 et AUp4."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].source_rule_sha256` | `"b2be9b1f7e3597802d5ed2c301a7e34bb7a9eecaeab55898e55306719b1b315b"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].source_rule_start` | `98` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[1].source_rule_end` | `325` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[7].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].evidence_id` | `"MURET-AUP-ICPE-CONDITION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].section_id` | `"SECTION-0111"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].page_number` | `93` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].evidence_direction` | `"CONTEXT_ONLY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].section_page_fragment_sha256` | `"57540d28148aefc320fcc8baa9a92df7e382d72299da6e804a3ebfaf52408b44"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].excerpt_start` | `713` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].excerpt_end` | `768` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].interpretation_note` | `"This separate ICPE condition is context only unless a future evidence step establishes that the BESS project is subject to it."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].source_rule_id` | `"MURET-AUp-CONDITION-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].source_rule_start` | `594` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].evidence[2].source_rule_end` | `803` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[7].evidence[2]`. | `interpret_bess_zoning` |
| `chapters[7].route_assessments[0].route_id` | `"MURET-AUp-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[7].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[7].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[7].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[7].route_assessments[0].positive_evidence_ids[0]` | `"MURET-AUP-PUBLIC-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[7].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[7].route_assessments[0].condition_evidence_ids[0]` | `"MURET-AUP-INFRASTRUCTURE-CONDITION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[7].route_assessments[0].condition_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[7].route_assessments[0].applicability_note` | `"The Article AUp 1 public or collective-interest route is assessed with the general Article AUp 2 infrastructure prerequisite. BESS category membership and satisfaction remain unresolved; the separate ICPE rule does not qualify this route unless independently applicable."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[7].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[8].resolved_zone_chapter_label` | `"AUf"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[8]`. | `interpret_bess_zoning` |
| `chapters[8].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[8]`. | `interpret_bess_zoning` |
| `chapters[8].reviewed_section_ids[0]` | `"SECTION-0125"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[8].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[8].reviewed_section_ids[1]` | `"SECTION-0126"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[8].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[8].review_note` | `"Articles AUf 1 and AUf 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[8]`. | `interpret_bess_zoning` |
| `chapters[8].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[8]`. | `interpret_bess_zoning` |
| `chapters[8].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[8]`. | `interpret_bess_zoning` |
| `chapters[8].rationale` | `"Infrastructure prerequisites were not treated as route evidence; Article AUf 2 separately states a possible ICPE route with compatibility and necessity conditions."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[8]`. | `interpret_bess_zoning` |
| `chapters[8].missing_information` | `"BESS planning-use, sector and ICPE classification, infrastructure and orientation requirements, all Article AUf 1/2 provisions, prescriptions and project design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[8]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].evidence_id` | `"MURET-AUF-ICPE-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].section_id` | `"SECTION-0126"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].page_number` | `102` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].exact_raw_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].excerpt_sha256` | `"e1c767bcf05e6e3879fda934afc396b55ecb8cb30b9be9d0e090c8ba860e13ff"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].section_page_fragment_sha256` | `"ef0d2718332307afa871176c64cb8627900702dbd583819fb765adb2d1902769"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].excerpt_start` | `1435` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].excerpt_end` | `1518` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].interpretation_note` | `"This is the explicit ICPE route phrase; infrastructure prerequisites alone were not used as positive evidence."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].source_rule_id` | `"MURET-AUf-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].source_rule_start` | `1435` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[0].source_rule_end` | `1644` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[8].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].evidence_id` | `"MURET-AUF-ICPE-CONDITION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].section_id` | `"SECTION-0126"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].page_number` | `102` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].evidence_kind` | `"ICPE_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].evidence_direction` | `"CONDITION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].exact_raw_excerpt` | `"compatibles avec le milieu environnant et nécessaires à"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].excerpt_sha256` | `"45e7c822963aeb5931b00392f605e45f745de47c084d04490bff6bb15f46a928"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].section_page_fragment_sha256` | `"ef0d2718332307afa871176c64cb8627900702dbd583819fb765adb2d1902769"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].excerpt_start` | `1554` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].excerpt_end` | `1609` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].interpretation_note` | `"This is the separate compatibility and necessity qualification."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].source_rule_id` | `"MURET-AUf-ICPE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].source_rule_excerpt` | `"Les installations classées pour la protection de l’environnement ne sont autorisées qu’à \nla condition qu'elles soient compatibles avec le milieu environnant et nécessaires à la \nvie du quartier et de la cité."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].source_rule_sha256` | `"890d2eab01e088948e78ff964bf68bc046d4bf88894f19ae20883793e5abb716"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].source_rule_start` | `1435` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].evidence[1].source_rule_end` | `1644` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[8].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[8].route_assessments[0].route_id` | `"MURET-AUf-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[8].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[8].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[8].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[8].route_assessments[0].positive_evidence_ids[0]` | `"MURET-AUF-ICPE-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[8].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[8].route_assessments[0].condition_evidence_ids[0]` | `"MURET-AUF-ICPE-CONDITION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[8].route_assessments[0].condition_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[8].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[8].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[9].resolved_zone_chapter_label` | `"AU0"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[9]`. | `interpret_bess_zoning` |
| `chapters[9].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[9]`. | `interpret_bess_zoning` |
| `chapters[9].reviewed_section_ids[0]` | `"SECTION-0140"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[9].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[9].reviewed_section_ids[1]` | `"SECTION-0141"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[9].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[9].review_note` | `"Articles AU0 1 and AU0 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[9]`. | `interpret_bess_zoning` |
| `chapters[9].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[9]`. | `interpret_bess_zoning` |
| `chapters[9].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[9]`. | `interpret_bess_zoning` |
| `chapters[9].rationale` | `"Article AU0 1 identifies an exception for collective-interest networks and public infrastructure, while Article AU0 2 states a separate PLU-modification prerequisite for new construction or operations."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[9]`. | `interpret_bess_zoning` |
| `chapters[9].missing_information` | `"Formal BESS classification within the stated infrastructure exception, applicability of the modification prerequisite, all Article AU0 1/2 provisions, prescriptions and project design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[9]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].evidence_id` | `"MURET-AU0-INFRA-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].section_id` | `"SECTION-0140"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].page_number` | `114` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].evidence_kind` | `"TECHNICAL_EQUIPMENT_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].exact_raw_excerpt` | `"installations nécessaires aux réseaux \nd’intérêt collectif, aux ouvrages publics d’infrastructures"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].excerpt_sha256` | `"886aaceafb2a40e73e3ebe145b3a58b6a22b239a8ce5fcc3740cb99d7d6298a0"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].section_page_fragment_sha256` | `"2f4cf931c76c5a5a29aa69d67b7986b092aff39ea13e4b302513177e5fef6619"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].excerpt_start` | `119` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].excerpt_end` | `217` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].interpretation_note` | `"This is an exact infrastructure exception; BESS qualification is unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].source_rule_id` | `"MURET-AU0-ROUTE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].source_rule_excerpt` | `"Sont interdites toutes les constructions autres que les installations nécessaires aux réseaux \nd’intérêt collectif, aux ouvrages publics d’infrastructures, et les extensions définies à \nl’article AU0 – 2."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].source_rule_sha256` | `"fa20142522483be8183df1a43e069fcb350b1de83347bdfdd733f7871bcf207d"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].source_rule_start` | `63` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[0].source_rule_end` | `267` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[9].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].evidence_id` | `"MURET-AU0-MODIFICATION-CONDITION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].section_id` | `"SECTION-0141"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].page_number` | `114` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].evidence_kind` | `"OTHER_RELEVANT_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].evidence_direction` | `"CONDITION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].exact_raw_excerpt` | `"Les constructions et opérations nouvelles ne pourront être autorisées qu’après la \nmise en œuvre d’une procédure de modification du PLU"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].excerpt_sha256` | `"01594e632fb064a7e4dd408e68c156b66711abe6ae2a0e470c779e94b91f3a48"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].section_page_fragment_sha256` | `"a239cf9eff040ca9c9ab608cf040e3c739d5111c877aa68ad1773d3adadf24a5"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].excerpt_start` | `99` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].excerpt_end` | `234` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].interpretation_note` | `"This prerequisite is a condition only and is not treated as evidence that a BESS route exists."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].source_rule_id` | `"MURET-AU0-CONDITION-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].source_rule_excerpt` | `"Les constructions et opérations nouvelles ne pourront être autorisées qu’après la \nmise en œuvre d’une procédure de modification du PLU."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].source_rule_sha256` | `"2d9633774f414a8ad2f8e42bfcbb2507b677906ca6aca480f0239cec007942e3"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].source_rule_start` | `99` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].evidence[1].source_rule_end` | `235` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[9].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[9].route_assessments[0].route_id` | `"MURET-AU0-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[9].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[9].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[9].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[9].route_assessments[0].positive_evidence_ids[0]` | `"MURET-AU0-INFRA-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[9].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[9].route_assessments[0].condition_evidence_ids[0]` | `"MURET-AU0-MODIFICATION-CONDITION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[9].route_assessments[0].condition_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[9].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[9].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[10].resolved_zone_chapter_label` | `"AUf0"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[10]`. | `interpret_bess_zoning` |
| `chapters[10].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[10]`. | `interpret_bess_zoning` |
| `chapters[10].reviewed_section_ids[0]` | `"SECTION-0155"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[10].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[10].reviewed_section_ids[1]` | `"SECTION-0156"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[10].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[10].review_note` | `"Articles AUf0 1 and AUf0 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[10]`. | `interpret_bess_zoning` |
| `chapters[10].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[10]`. | `interpret_bess_zoning` |
| `chapters[10].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[10]`. | `interpret_bess_zoning` |
| `chapters[10].rationale` | `"Article AUf0 1 identifies an exception for collective-interest networks and public infrastructure, while Article AUf0 2 states a separate PLU-modification prerequisite."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[10]`. | `interpret_bess_zoning` |
| `chapters[10].missing_information` | `"Formal BESS classification within the infrastructure exception, applicability of the modification prerequisite, all Article AUf0 1/2 provisions, prescriptions and project design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[10]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].evidence_id` | `"MURET-AUF0-INFRA-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].section_id` | `"SECTION-0155"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].page_number` | `120` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].evidence_kind` | `"TECHNICAL_EQUIPMENT_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].exact_raw_excerpt` | `"installations nécessaires aux réseaux \nd’intérêt collectif, aux ouvrages publics d’infrastructures"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].excerpt_sha256` | `"886aaceafb2a40e73e3ebe145b3a58b6a22b239a8ce5fcc3740cb99d7d6298a0"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].section_page_fragment_sha256` | `"a23b2c0f7e48711758012d3b176967139a3b87d230c3dea312987693de86c369"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].excerpt_start` | `120` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].excerpt_end` | `218` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].interpretation_note` | `"This is an exact infrastructure exception; BESS qualification is unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].source_rule_id` | `"MURET-AUf0-ROUTE-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].source_rule_excerpt` | `"Sont interdites toutes les constructions autres que les installations nécessaires aux réseaux \nd’intérêt collectif, aux ouvrages publics d’infrastructures, et les extensions définies à \nl’article AUf0 – 2."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].source_rule_sha256` | `"5f4af2e2ece550ccc1bcb39eb7436f7dba04f5f21c0346b7d780bf350b77183c"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].source_rule_start` | `64` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[0].source_rule_end` | `269` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[10].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].evidence_id` | `"MURET-AUF0-MODIFICATION-CONDITION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].section_id` | `"SECTION-0156"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].page_number` | `120` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].evidence_kind` | `"OTHER_RELEVANT_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].evidence_direction` | `"CONDITION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].exact_raw_excerpt` | `"Les constructions et opérations nouvelles ne pourront être autorisées qu’après la \nmise en œuvre d’une procédure de modification du PLU"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].excerpt_sha256` | `"01594e632fb064a7e4dd408e68c156b66711abe6ae2a0e470c779e94b91f3a48"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].section_page_fragment_sha256` | `"15040ad2f1b4a5fd1c44bdfead25d12cf4ccdd53a5f28736e4c383ae19a6cac9"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].excerpt_start` | `100` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].excerpt_end` | `235` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].interpretation_note` | `"This prerequisite is a condition only and is not treated as route evidence."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].source_rule_id` | `"MURET-AUf0-CONDITION-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].source_rule_excerpt` | `"Les constructions et opérations nouvelles ne pourront être autorisées qu’après la \nmise en œuvre d’une procédure de modification du PLU."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].source_rule_sha256` | `"2d9633774f414a8ad2f8e42bfcbb2507b677906ca6aca480f0239cec007942e3"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].source_rule_start` | `100` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].evidence[1].source_rule_end` | `236` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[10].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[10].route_assessments[0].route_id` | `"MURET-AUf0-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[10].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[10].route_assessments[0].route_kind` | `"CONDITIONAL_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[10].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[10].route_assessments[0].positive_evidence_ids[0]` | `"MURET-AUF0-INFRA-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[10].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[10].route_assessments[0].condition_evidence_ids[0]` | `"MURET-AUF0-MODIFICATION-CONDITION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[10].route_assessments[0].condition_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[10].route_assessments[0].applicability_note` | `"The cited positive category and its explicit qualification are assessed as one coherent route; BESS applicability remains unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[10].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[11].resolved_zone_chapter_label` | `"A"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[11]`. | `interpret_bess_zoning` |
| `chapters[11].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[11]`. | `interpret_bess_zoning` |
| `chapters[11].reviewed_section_ids[0]` | `"SECTION-0170"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[11].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[11].reviewed_section_ids[1]` | `"SECTION-0171"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[11].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[11].review_note` | `"Articles A 1 and A 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[11]`. | `interpret_bess_zoning` |
| `chapters[11].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[11]`. | `interpret_bess_zoning` |
| `chapters[11].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[11]`. | `interpret_bess_zoning` |
| `chapters[11].rationale` | `"Article A 1 contains broad restrictive language and a separate exception for necessary technical and infrastructure works. The policy records the conflict without deciding BESS qualification."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[11]`. | `interpret_bess_zoning` |
| `chapters[11].missing_information` | `"Formal necessity and BESS infrastructure classification, agricultural-zone effects, all Article A 1/2 provisions, prescriptions, servitudes and project design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[11]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].evidence_id` | `"MURET-A-RESTRICTION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].section_id` | `"SECTION-0170"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].page_number` | `125` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].evidence_kind` | `"USE_RESTRICTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].evidence_direction` | `"SUPPORTS_DIFFICULTY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].exact_raw_excerpt` | `"Sont interdites toutes les occupations et utilisations du sol autres que celles"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].excerpt_sha256` | `"f18eba9dd56f410853fb685d30b6fcc78ee95359c6577387b78a29c3261b3c61"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].section_page_fragment_sha256` | `"51342e0ae335504d0f750e0138a63c2ffe928e11e564872122bec65edb4a8e13"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].excerpt_start` | `67` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].excerpt_end` | `146` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].interpretation_note` | `"This is the broad restriction phrase, separate from the exception."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].source_rule_id` | `"MURET-A-RESTRICTION-EXCEPTION-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].source_rule_excerpt` | `"Sont interdites toutes les occupations et utilisations du sol autres que celles : \n- nécessaires à l’exploitation agricole, qu’il s’agisse des constructions et extensions \nà usage d’habitation ou des constructions et installations à usage agricole, \n- nécessaires au bon fonctionnement des systèmes de gestion des eaux, \n- nécessaires aux ouvrages techniques et d’infrastructures, \n- mentionnées à l’article A2"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].source_rule_sha256` | `"4a0a23edf39f707575293cb759d13f6bf2081db5df58ff1e9bed08c98775b1b9"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].source_rule_start` | `67` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[0].source_rule_end` | `477` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[11].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].evidence_id` | `"MURET-A-INFRA-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].section_id` | `"SECTION-0170"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].page_number` | `125` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].evidence_kind` | `"TECHNICAL_EQUIPMENT_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].exact_raw_excerpt` | `"nécessaires aux ouvrages techniques et d’infrastructures"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].excerpt_sha256` | `"7eee9f7e595784b2d6a4b605a4f0b5703a0446acb77b7420c709b5516e30e0a2"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].section_page_fragment_sha256` | `"51342e0ae335504d0f750e0138a63c2ffe928e11e564872122bec65edb4a8e13"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].excerpt_start` | `390` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].excerpt_end` | `446` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].interpretation_note` | `"This is the separate technical-infrastructure exception; BESS necessity and classification are unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].source_rule_id` | `"MURET-A-RESTRICTION-EXCEPTION-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].source_rule_excerpt` | `"Sont interdites toutes les occupations et utilisations du sol autres que celles : \n- nécessaires à l’exploitation agricole, qu’il s’agisse des constructions et extensions \nà usage d’habitation ou des constructions et installations à usage agricole, \n- nécessaires au bon fonctionnement des systèmes de gestion des eaux, \n- nécessaires aux ouvrages techniques et d’infrastructures, \n- mentionnées à l’article A2"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].source_rule_sha256` | `"4a0a23edf39f707575293cb759d13f6bf2081db5df58ff1e9bed08c98775b1b9"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].source_rule_start` | `67` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].evidence[1].source_rule_end` | `477` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[11].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[11].route_assessments[0].route_id` | `"MURET-A-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[11].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[11].route_assessments[0].route_kind` | `"RESTRICTION_EXCEPTION_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[11].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[11].route_assessments[0].positive_evidence_ids[0]` | `"MURET-A-INFRA-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[11].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[11].route_assessments[0].difficulty_evidence_ids[0]` | `"MURET-A-RESTRICTION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[11].route_assessments[0].difficulty_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[11].route_assessments[0].applicability_note` | `"The restriction and its listed exception are assessed as one coherent route; BESS applicability remains unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[11].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[12].resolved_zone_chapter_label` | `"N"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `resolved zone chapter label` under the exact parent path `chapters[12]`. | `interpret_bess_zoning` |
| `chapters[12].review_completeness` | `"COMPLETE_FOR_CONFIGURED_USE_CONTROL_ARTICLES"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review completeness` under the exact parent path `chapters[12]`. | `interpret_bess_zoning` |
| `chapters[12].reviewed_section_ids[0]` | `"SECTION-0184"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[12].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[12].reviewed_section_ids[1]` | `"SECTION-0185"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[12].reviewed_section_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[12].review_note` | `"Articles N 1 and N 2 were reviewed in full for written use controls."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `review note` under the exact parent path `chapters[12]`. | `interpret_bess_zoning` |
| `chapters[12].zoning_precheck_status` | `"CONDITIONAL_REVIEW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck status` under the exact parent path `chapters[12]`. | `interpret_bess_zoning` |
| `chapters[12].zoning_precheck_confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `zoning precheck confidence` under the exact parent path `chapters[12]`. | `interpret_bess_zoning` |
| `chapters[12].rationale` | `"Article N 1 contains a broad restriction and a separate exception for necessary technical and infrastructure equipment. The policy records the conflict without deciding BESS qualification."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `chapters[12]`. | `interpret_bess_zoning` |
| `chapters[12].missing_information` | `"Formal necessity and BESS infrastructure classification, natural-zone effects, all Article N 1/2 provisions, prescriptions, servitudes and project design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `missing information` under the exact parent path `chapters[12]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].evidence_id` | `"MURET-N-RESTRICTION-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].section_id` | `"SECTION-0184"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].page_number` | `135` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].evidence_kind` | `"USE_RESTRICTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].evidence_direction` | `"SUPPORTS_DIFFICULTY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].exact_raw_excerpt` | `"Sont interdites, toutes les occupations et utilisations du sol, à l’exception"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].excerpt_sha256` | `"4781673bc1d5c704acd3be46c706805f6eaebacd4fc4b2296877af8bce6688ef"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].section_page_fragment_sha256` | `"0cac3a1aeb56859670b715c17e1c166959147a0f90a19a12f87e0025b263e195"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].excerpt_start` | `69` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].excerpt_end` | `146` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].interpretation_note` | `"This is the broad restriction phrase, separate from its listed exceptions."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].source_rule_id` | `"MURET-N-RESTRICTION-EXCEPTION-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].source_rule_excerpt` | `"Sont interdites, toutes les occupations et utilisations du sol, à l’exception : \n \n- des occupations et utilisations du sol soumises à des conditions particulières et \nrépertoriées à l’article N 2, \n- des équipements nécessaires aux ouvrages techniques et d’infrastructure, \n- des aménagements liés aux ouvrages techniques nécessaires au fonctionnement des \nservices publics, \n- des équipements nécessaires au bon fonctionnement des systèmes de gestion des \neaux, \n- en secteur NL : \n- les constructions, installations et utilisations du sol destinées à l’accueil des \nactivités de loisirs et d’équipements publics sportifs ou socio-culturels, \n- les terrains de camping et de caravaning, excepté dans le secteur inondable \nrepéré au plan de zonage."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].source_rule_sha256` | `"c434670531b43bbc23dd24c1fa01bba1eedaee0ba9e241b9f432255c74db30d2"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].source_rule_start` | `69` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[0].source_rule_end` | `818` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[12].evidence[0]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].evidence_id` | `"MURET-N-INFRA-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence id` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].section_id` | `"SECTION-0184"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `section id` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].page_number` | `135` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `page number` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].evidence_kind` | `"TECHNICAL_EQUIPMENT_RULE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence kind` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].evidence_direction` | `"SUPPORTS_POTENTIAL_COMPATIBILITY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `evidence direction` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].exact_raw_excerpt` | `"des équipements nécessaires aux ouvrages techniques et d’infrastructure"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `exact raw excerpt` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].excerpt_sha256` | `"b28cb339936e8598faee5c5bba6f1be5f52e40b1ce6f33fe854ae1daff54d867"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `excerpt_sha256`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].section_page_fragment_sha256` | `"0cac3a1aeb56859670b715c17e1c166959147a0f90a19a12f87e0025b263e195"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `section_page_fragment_sha256`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].excerpt_start` | `270` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt start` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].excerpt_end` | `341` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `excerpt end` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].interpretation_note` | `"This is the separate technical-infrastructure exception; BESS necessity and classification are unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `interpretation note` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].source_rule_id` | `"MURET-N-RESTRICTION-EXCEPTION-RULE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule id` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].source_rule_excerpt` | `"Sont interdites, toutes les occupations et utilisations du sol, à l’exception : \n \n- des occupations et utilisations du sol soumises à des conditions particulières et \nrépertoriées à l’article N 2, \n- des équipements nécessaires aux ouvrages techniques et d’infrastructure, \n- des aménagements liés aux ouvrages techniques nécessaires au fonctionnement des \nservices publics, \n- des équipements nécessaires au bon fonctionnement des systèmes de gestion des \neaux, \n- en secteur NL : \n- les constructions, installations et utilisations du sol destinées à l’accueil des \nactivités de loisirs et d’équipements publics sportifs ou socio-culturels, \n- les terrains de camping et de caravaning, excepté dans le secteur inondable \nrepéré au plan de zonage."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `source rule excerpt` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].source_rule_sha256` | `"c434670531b43bbc23dd24c1fa01bba1eedaee0ba9e241b9f432255c74db30d2"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `source_rule_sha256`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].source_rule_start` | `69` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule start` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].evidence[1].source_rule_end` | `818` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `source rule end` under the exact parent path `chapters[12].evidence[1]`. | `interpret_bess_zoning` |
| `chapters[12].route_assessments[0].route_id` | `"MURET-N-ROUTE-01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route id` under the exact parent path `chapters[12].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[12].route_assessments[0].route_kind` | `"RESTRICTION_EXCEPTION_ROUTE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `route kind` under the exact parent path `chapters[12].route_assessments[0]`. | `interpret_bess_zoning` |
| `chapters[12].route_assessments[0].positive_evidence_ids[0]` | `"MURET-N-INFRA-ROUTE-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[12].route_assessments[0].positive_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[12].route_assessments[0].difficulty_evidence_ids[0]` | `"MURET-N-RESTRICTION-01"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `chapters[12].route_assessments[0].difficulty_evidence_ids`; order and uniqueness are validated/consumed where required. | `interpret_bess_zoning` |
| `chapters[12].route_assessments[0].applicability_note` | `"The restriction and its listed exception are assessed as one coherent route; BESS applicability remains unresolved."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `applicability note` under the exact parent path `chapters[12].route_assessments[0]`. | `interpret_bess_zoning` |

## STEP 7F.1A.4 dependent-model refresh

- The YAML bytes and checked-in values are unchanged. STEP 7F.1A.4 changes their owning validation/authority boundary through `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config`; section 5 now embeds the exact current owning model sources and qualified consumers.
- Decision-input models are frozen/deeply immutable where their current source declares that contract; trust-bearing YAML is decoded through the shared duplicate-rejecting loader where the owning loader source shows that call.
- No configured policy meaning, source identity, threshold, artifact schema, or output schema is changed by this dependent documentation refresh.

## 5. Classes / models / dataclasses

- Exact checked-in configuration SHA256 remains `879d50627c063bb10096950d004cf4d4e446ff04ef9a1178b3e3fb28e2ffdae3`; its values are unchanged by STEP 7F.1A.4.
- Authoritative loader/config boundary: `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config`.
- Owning Python module: `landscout.stages.interpret_bess_zoning`.
- The owning model declarations below are refreshed from the current source so frozen/deeply immutable fields, strict serialization, exact domains, validators, and internal metadata schemas cannot remain stale merely because the YAML bytes did not change.

### `_StrictConfigModel`

**Source purpose:** Defines `_StrictConfigModel`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `BaseModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `model_config` | `inferred from assignment` | `ConfigDict(extra="forbid", frozen=True)` | `model_config = ConfigDict(extra="forbid", frozen=True)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class _StrictConfigModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `PolicySourceLock`

**Source purpose:** Defines `PolicySourceLock`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `document_id` | `StrictStr` | `Field(min_length=1)` | `document_id: StrictStr = Field(min_length=1)` |
| `archive_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `archive_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `pdf_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `index_content_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `structure_result_content_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `structure_result_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `structure_profile` | `StrictStr` | `Field(min_length=1)` | `structure_profile: StrictStr = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class PolicySourceLock(_StrictConfigModel):
    document_id: StrictStr = Field(min_length=1)
    archive_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    structure_result_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    structure_profile: StrictStr = Field(min_length=1)
```

### `PolicyEvidence`

**Source purpose:** Defines `PolicyEvidence`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `evidence_id` | `StrictStr` | `Field(min_length=1)` | `evidence_id: StrictStr = Field(min_length=1)` |
| `section_id` | `StrictStr` | `Field(min_length=1)` | `section_id: StrictStr = Field(min_length=1)` |
| `page_number` | `StrictInt` | `Field(ge=1)` | `page_number: StrictInt = Field(ge=1)` |
| `evidence_kind` | `EvidenceKind` | `required` | `evidence_kind: EvidenceKind` |
| `evidence_direction` | `EvidenceDirection` | `required` | `evidence_direction: EvidenceDirection` |
| `exact_raw_excerpt` | `StrictStr` | `Field(min_length=1, max_length=600)` | `exact_raw_excerpt: StrictStr = Field(min_length=1, max_length=600)` |
| `excerpt_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `excerpt_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `section_page_fragment_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `section_page_fragment_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `excerpt_start` | `StrictInt` | `Field(ge=0)` | `excerpt_start: StrictInt = Field(ge=0)` |
| `excerpt_end` | `StrictInt` | `Field(ge=1)` | `excerpt_end: StrictInt = Field(ge=1)` |
| `source_rule_id` | `StrictStr` | `Field(min_length=1)` | `source_rule_id: StrictStr = Field(min_length=1)` |
| `source_rule_excerpt` | `StrictStr` | `Field(min_length=1)` | `source_rule_excerpt: StrictStr = Field(min_length=1)` |
| `source_rule_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `source_rule_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `source_rule_start` | `StrictInt` | `Field(ge=0)` | `source_rule_start: StrictInt = Field(ge=0)` |
| `source_rule_end` | `StrictInt` | `Field(ge=1)` | `source_rule_end: StrictInt = Field(ge=1)` |
| `interpretation_note` | `StrictStr` | `Field(min_length=1)` | `interpretation_note: StrictStr = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.interpret_bess_zoning::PolicyEvidence._validate_exact_strings` via `PolicyEvidence`

**Exact class source**

```python
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
```

### `RouteAssessment`

**Source purpose:** Defines `RouteAssessment`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `route_id` | `StrictStr` | `Field(min_length=1)` | `route_id: StrictStr = Field(min_length=1)` |
| `route_kind` | `RouteKind` | `required` | `route_kind: RouteKind` |
| `positive_evidence_ids` | `tuple[StrictStr, ...]` | `()` | `positive_evidence_ids: tuple[StrictStr, ...] = ()` |
| `condition_evidence_ids` | `tuple[StrictStr, ...]` | `()` | `condition_evidence_ids: tuple[StrictStr, ...] = ()` |
| `difficulty_evidence_ids` | `tuple[StrictStr, ...]` | `()` | `difficulty_evidence_ids: tuple[StrictStr, ...] = ()` |
| `applicability_note` | `StrictStr` | `Field(min_length=1)` | `applicability_note: StrictStr = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.interpret_bess_zoning::RouteAssessment._validate_route_shape` via `RouteAssessment`
- value/type reference: `landscout.stages.interpret_bess_zoning::_derived_chapter_status` via `RouteAssessment`

**Exact class source**

```python
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
```

### `ChapterPolicy`

**Source purpose:** Defines `ChapterPolicy`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `resolved_zone_chapter_label` | `StrictStr` | `Field(min_length=1)` | `resolved_zone_chapter_label: StrictStr = Field(min_length=1)` |
| `review_completeness` | `ReviewCompleteness` | `required` | `review_completeness: ReviewCompleteness` |
| `reviewed_section_ids` | `tuple[StrictStr, ...]` | `()` | `reviewed_section_ids: tuple[StrictStr, ...] = ()` |
| `review_note` | `StrictStr` | `Field(min_length=1)` | `review_note: StrictStr = Field(min_length=1)` |
| `zoning_precheck_status` | `ChapterStatus` | `required` | `zoning_precheck_status: ChapterStatus` |
| `zoning_precheck_confidence` | `Confidence` | `required` | `zoning_precheck_confidence: Confidence` |
| `rationale` | `StrictStr` | `Field(min_length=1)` | `rationale: StrictStr = Field(min_length=1)` |
| `missing_information` | `StrictStr` | `Field(min_length=1)` | `missing_information: StrictStr = Field(min_length=1)` |
| `evidence` | `tuple[PolicyEvidence, ...]` | `()` | `evidence: tuple[PolicyEvidence, ...] = ()` |
| `route_assessments` | `tuple[RouteAssessment, ...]` | `()` | `route_assessments: tuple[RouteAssessment, ...] = ()` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.interpret_bess_zoning::ChapterPolicy._validate_evidence_semantics` via `ChapterPolicy`

**Exact class source**

```python
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
```

### `BessZoningPolicyConfig`

**Source purpose:** Strict source-locked interpretation policy.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `policy_profile` | `StrictStr` | `Field(min_length=1)` | `policy_profile: StrictStr = Field(min_length=1)` |
| `planning_precheck_scope` | `Literal['WRITTEN_ZONING_REGULATION_ONLY']` | `required` | `planning_precheck_scope: Literal["WRITTEN_ZONING_REGULATION_ONLY"]` |
| `review_scope` | `Literal['CONFIGURED_USE_CONTROL_ARTICLES_ONLY']` | `required` | `review_scope: Literal["CONFIGURED_USE_CONTROL_ARTICLES_ONLY"]` |
| `source_lock` | `PolicySourceLock` | `required` | `source_lock: PolicySourceLock` |
| `required_zone_article_numbers` | `tuple[StrictStr, ...]` | `Field(min_length=1)` | `required_zone_article_numbers: tuple[StrictStr, ...] = Field(min_length=1)` |
| `chapters` | `tuple[ChapterPolicy, ...]` | `Field(min_length=1)` | `chapters: tuple[ChapterPolicy, ...] = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`
- value/type reference: `landscout.stages.interpret_bess_zoning::BessZoningPolicyConfig._validate_policy` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::load_bess_zoning_policy_config` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_policy_sha256` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_resolved_policy` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_lock` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_required_section_ids_by_chapter` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_validate_policy_evidence` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_lineage` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_chapter_policy` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_route_assessments` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_evidence_route_links` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_source_zone_policy` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_parcel_zone_interpretations` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_parcel_output` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `BessZoningPolicyConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `BessZoningPolicyConfig`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.interpret_bess_zoning import (
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    BessZoningPrecheckResult,
    interpret_bess_zoning,
    validate_bess_zoning_precheck,
)`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_policy` via `BessZoningPolicyConfig`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.interpret_bess_zoning import (
    CHAPTER_POLICY_COLUMNS,
    EVIDENCE_CATALOG_COLUMNS,
    EVIDENCE_ROUTE_LINK_COLUMNS,
    PARCEL_ZONE_POLICY_COLUMNS,
    ROUTE_ASSESSMENT_COLUMNS,
    SOURCE_ZONE_POLICY_COLUMNS,
    BessZoningPolicyConfig,
    BessZoningPrecheckError,
    _result_with_hashes,
    interpret_bess_zoning,
    load_bess_zoning_policy_config,
    validate_bess_zoning_precheck,
)`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_policy` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_payload` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_policy_with_context_only_evidence` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_lock_mismatch_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_missing_and_extra_chapter_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_chapter_and_evidence_id_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_one_excerpt_cannot_be_reused_with_contradictory_directions` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_chapter_scoped_occurrence_in_one_route_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_duplicate_occurrence_in_different_compatible_routes_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_forbidden_or_invalid_final_status_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_invalid_confidence_and_unknown_field_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_old_policy_schema_versions_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_source_rule_identity_and_containment_are_strict` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_same_rule_text_at_distinct_offsets_has_distinct_identity` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_absent_excerpt_and_section_page_mismatch_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_excerpt_hash_and_length_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_declared_status_must_equal_derived_route_status` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_condition_alone_cannot_create_conditional_review` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unrelated_positive_and_condition_do_not_create_conditional_review` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unlinked_context_only_unknown_succeeds` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_positive_condition_and_conflict_status_routes` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_route_references_must_be_same_chapter_and_role_compatible` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_route_ids_are_globally_unique` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unlinked_difficulty_evidence_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unlinked_positive_and_condition_evidence_are_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_context_only_evidence_must_be_unlinked` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_one_evidence_may_link_to_multiple_compatible_routes` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_difficulty_and_positive_only_status_routes` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_incomplete_review_requires_unknown_low` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_incomplete_review_persists_exact_missing_required_sections` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_unknown_is_accepted_when_evidence_is_insufficient` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_reviewed_sections_cover_required_articles` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_must_be_inside_reviewed_sections` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_review_cannot_claim_another_chapter_section` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_general_section_review_is_explicit_and_valid` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_same_general_occurrence_may_be_scoped_to_different_chapters` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_wrong_occurrence_identity_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_policy_change_after_result_creation_is_rejected` via `BessZoningPolicyConfig`
- value/type reference: `tests.unit.test_interpret_bess_zoning::test_evidence_change_after_result_creation_is_rejected` via `BessZoningPolicyConfig`

**Exact class source**

```python
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
```

## 6. Functions and methods

Loader: `landscout.stages.interpret_bess_zoning.load_bess_zoning_policy_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, exact validation, and any hashing actually performed by that loader.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `interpret_bess_zoning`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

## 9. Error handling

The owning Pydantic model rejects extra/missing/unsupported/coerced values according to the exact model/validators above; the loader translates YAML/path/model failures into its documented controlled error.

## 10. Side effects

Network I/O: none. Filesystem read: the loader reads this YAML. Filesystem write: none. Input mutation: none. GIS calculation: none. Hashing: none; this loader parses/validates configuration values but does not hash this file's bytes.

## 11. Security / trust boundaries

A configured URL/provider/hash is a source lock or provenance input. Physical authority requires the consuming source adapter's safe transport and byte/source revalidation.

## 12. GIS / CRS rules

Only explicit CRS fields impose GIS rules; configured storage/calculation CRS values are policy/configuration, not an implicit reprojection of data.

## 13. Provenance rules

The companion's Source SHA256 binds this checked-in file for documentation fidelity; that documentation digest is not attributed to the runtime loader. Source identities remain textual until the adapter validates physical bytes/content.

## 14. Business meaning

Thresholds and outcomes are policy/configuration values. They are never relabeled as measured geometry or legal conclusions.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

The loader/model companion and relevant test companion document exact valid/invalid values, cross-field failures, consumer loading, and byte-hash behavior only where the runtime source actually computes a hash.

## 17. Change impact

Any YAML byte/value change requires policy/source review, consumer tests, generated artifacts where applicable, this companion SHA update, and only those runtime hashes whose documented algorithm actually includes these bytes or validated values.

## 18. Complete readable configuration and authoritative raw-byte snapshot

### Complete readable YAML

The following is the complete decoded UTF-8 configuration with line endings normalized to LF for stable Markdown display. Every character and logical line is present, but this readable fence is not the authority for original CR/LF byte positions.

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

- Raw byte length: `47039`.
- Raw SHA256: `879d50627c063bb10096950d004cf4d4e446ff04ef9a1178b3e3fb28e2ffdae3` (identical to **File identity**).
- Encoding: RFC 4648 Base64, wrapped for display only. Decoding the concatenated payload reproduces every original byte, including mixed CRLF/LF positions.

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
