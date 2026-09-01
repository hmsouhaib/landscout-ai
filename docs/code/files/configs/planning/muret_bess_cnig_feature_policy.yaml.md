# `configs/planning/muret_bess_cnig_feature_policy.yaml`

## File identity

- Repository path: `configs/planning/muret_bess_cnig_feature_policy.yaml`
- File type: YAML checked-in configuration/policy/source lock
- Responsibility: Defines the Muret BESS precheck policy over official CNIG feature-code meaning only.
- Source SHA256: `8a26fcb8ee7e2f028baca65d94c2b5be5445ba9fc4b82b9b1a21843f933f8b2a`

## 1. Purpose

Defines the Muret BESS precheck policy over official CNIG feature-code meaning only.

## 2. Position in LandScout architecture

The exact YAML bytes are parsed by `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config` into `landscout.stages.bess_planning_feature_policy.BessPlanningFeaturePolicyConfig`. Runtime consumers include `compile_bess_planning_feature_policy`.

## 3. Imports and dependencies

Not applicable to YAML. Python/Pydantic consumers are named above and reproduced below.

## 4. Contract taxonomy

Every row below is a configuration field/list leaf. It is not a DataFrame column unless a consuming stage explicitly copies it into a documented result schema.

| Exact YAML path | Checked-in value | Runtime type | Required/nullability/allowed-domain/unit contract | Semantic role | Consumers |
|---|---|---|---|---|---|
| `schema_version` | `1` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required supported schema integer; accepted versions are pinned by the owning Literal/validator | Selects the strict configuration schema; unsupported versions are rejected. | `compile_bess_planning_feature_policy` |
| `profile` | `"muret_bess_cnig_feature_policy_v1"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `profile` under the exact parent path `<root>`. | `compile_bess_planning_feature_policy` |
| `policy_scope` | `"OFFICIAL_CNIG_CODE_MEANING_ONLY"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Limits the kind of source evidence the policy is allowed to interpret. | `compile_bess_planning_feature_policy` |
| `local_feature_text_interpreted` | `false` | `bool` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required Boolean at this checked-in path unless the exact model declares a default/optional field | Enables/disables the exact local feature text interpreted behavior; Boolean coercion rules belong to the consuming model. | `compile_bess_planning_feature_policy` |
| `local_regulation_content_interpreted` | `false` | `bool` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required Boolean at this checked-in path unless the exact model declares a default/optional field | Enables/disables the exact local regulation content interpreted behavior; Boolean coercion rules belong to the consuming model. | `compile_bess_planning_feature_policy` |
| `legal_conclusion_produced` | `false` | `bool` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required Boolean at this checked-in path unless the exact model declares a default/optional field | Enables/disables the exact legal conclusion produced behavior; Boolean coercion rules belong to the consuming model. | `compile_bess_planning_feature_policy` |
| `source_lock.document_id` | `"33edb4c9f6943c88d8d92518bff20bec"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `document id` under the exact parent path `source_lock`. | `compile_bess_planning_feature_policy` |
| `source_lock.archive_sha256` | `"9d6677cd6634b56b712311042f0cc714d5ca42a38f82a417b27dd473255d7d93"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `archive_sha256`. | `compile_bess_planning_feature_policy` |
| `source_lock.cnig_profile` | `"cnig_plu_2017_muret_observed_pairs_v2"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `cnig profile` under the exact parent path `source_lock`. | `compile_bess_planning_feature_policy` |
| `source_lock.cnig_profile_schema_version` | `2` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required supported schema integer; accepted versions are pinned by the owning Literal/validator | Selects compatibility for the cnig profile schema version; the consuming model accepts only supported integers. | `compile_bess_planning_feature_policy` |
| `source_lock.cnig_profile_sha256` | `"5611b814eb4bc057578b908c6505094f9df5d2c2bf4ca126629b1362983c47ee"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `cnig_profile_sha256`. | `compile_bess_planning_feature_policy` |
| `source_lock.cnig_result_hash_schema_version` | `5` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required supported schema integer; accepted versions are pinned by the owning Literal/validator | Selects compatibility for the cnig result hash schema version; the consuming model accepts only supported integers. | `compile_bess_planning_feature_policy` |
| `source_lock.cnig_complete_result_content_sha256` | `"b56b195b32914583e6599fe96b3d29977c52450c9755228d89ce7e192903ab3e"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `cnig_complete_result_content_sha256`. | `compile_bess_planning_feature_policy` |
| `status_priority.LIKELY_MATERIAL_CONSTRAINT` | `50` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `LIKELY MATERIAL CONSTRAINT` under the exact parent path `status_priority`. | `compile_bess_planning_feature_policy` |
| `status_priority.UNKNOWN` | `40` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `UNKNOWN` under the exact parent path `status_priority`. | `compile_bess_planning_feature_policy` |
| `status_priority.MATERIAL_REVIEW_REQUIRED` | `30` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `MATERIAL REVIEW REQUIRED` under the exact parent path `status_priority`. | `compile_bess_planning_feature_policy` |
| `status_priority.DESIGN_REVIEW_REQUIRED` | `20` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `DESIGN REVIEW REQUIRED` under the exact parent path `status_priority`. | `compile_bess_planning_feature_policy` |
| `status_priority.CONTEXT_REVIEW_REQUIRED` | `10` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `CONTEXT REVIEW REQUIRED` under the exact parent path `status_priority`. | `compile_bess_planning_feature_policy` |
| `canonical_policy_entries_sha256` | `"1d3e63f1123000402065b74402cb1e2295db2ac5655209ce410aaf36bfc2be91"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `canonical_policy_entries_sha256`. | `compile_bess_planning_feature_policy` |
| `entries[0].feature_family` | `"INFORMATION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `entries[0]`. | `compile_bess_planning_feature_policy` |
| `entries[0].type_code` | `"02"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `entries[0]`. | `compile_bess_planning_feature_policy` |
| `entries[0].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `entries[0]`. | `compile_bess_planning_feature_policy` |
| `entries[0].expected_official_label` | `"Zone d'aménagement concerté"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected official label` under the exact parent path `entries[0]`. | `compile_bess_planning_feature_policy` |
| `entries[0].expected_legal_reference` | `"L311-1 code de l’urbanisme"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected legal reference` under the exact parent path `entries[0]`. | `compile_bess_planning_feature_policy` |
| `entries[0].expected_regulation_reference` | `"R151-52 8°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected regulation reference` under the exact parent path `entries[0]`. | `compile_bess_planning_feature_policy` |
| `entries[0].precheck_status` | `"CONTEXT_REVIEW_REQUIRED"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `precheck status` under the exact parent path `entries[0]`. | `compile_bess_planning_feature_policy` |
| `entries[0].confidence` | `"HIGH"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `confidence` under the exact parent path `entries[0]`. | `compile_bess_planning_feature_policy` |
| `entries[0].rationale` | `"The official code identifies a concerted-development-zone context that requires planning-document review but does not establish a direct BESS constraint by itself."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `entries[0]`. | `compile_bess_planning_feature_policy` |
| `entries[0].required_human_action` | `"Review the applicable planning documents and authority context for the identified concerted-development zone."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `required human action` under the exact parent path `entries[0]`. | `compile_bess_planning_feature_policy` |
| `entries[0].limitations` | `"This classification uses only the official CNIG code meaning and does not interpret any local feature text or regulation."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limitations` under the exact parent path `entries[0]`. | `compile_bess_planning_feature_policy` |
| `entries[1].feature_family` | `"INFORMATION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `entries[1]`. | `compile_bess_planning_feature_policy` |
| `entries[1].type_code` | `"14"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `entries[1]`. | `compile_bess_planning_feature_policy` |
| `entries[1].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `entries[1]`. | `compile_bess_planning_feature_policy` |
| `entries[1].expected_official_label` | `"Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected official label` under the exact parent path `entries[1]`. | `compile_bess_planning_feature_policy` |
| `entries[1].expected_legal_reference` | `"L571-10 code de l’environnement"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected legal reference` under the exact parent path `entries[1]`. | `compile_bess_planning_feature_policy` |
| `entries[1].expected_regulation_reference` | `"R151-53 5°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected regulation reference` under the exact parent path `entries[1]`. | `compile_bess_planning_feature_policy` |
| `entries[1].precheck_status` | `"CONTEXT_REVIEW_REQUIRED"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `precheck status` under the exact parent path `entries[1]`. | `compile_bess_planning_feature_policy` |
| `entries[1].confidence` | `"HIGH"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `confidence` under the exact parent path `entries[1]`. | `compile_bess_planning_feature_policy` |
| `entries[1].rationale` | `"The official code identifies transport-infrastructure noise context that must be checked but does not establish a direct BESS constraint by itself."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `entries[1]`. | `compile_bess_planning_feature_policy` |
| `entries[1].required_human_action` | `"Review the applicable noise-sector documents and project-specific context with the competent authority."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `required human action` under the exact parent path `entries[1]`. | `compile_bess_planning_feature_policy` |
| `entries[1].limitations` | `"This classification uses only the official CNIG code meaning and does not interpret local noise rules or project effects."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limitations` under the exact parent path `entries[1]`. | `compile_bess_planning_feature_policy` |
| `entries[2].feature_family` | `"INFORMATION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `entries[2]`. | `compile_bess_planning_feature_policy` |
| `entries[2].type_code` | `"27"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `entries[2]`. | `compile_bess_planning_feature_policy` |
| `entries[2].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `entries[2]`. | `compile_bess_planning_feature_policy` |
| `entries[2].expected_official_label` | `"Plan d'exposition au bruit des aérodromes"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected official label` under the exact parent path `entries[2]`. | `compile_bess_planning_feature_policy` |
| `entries[2].expected_legal_reference` | `"L112-6 code de l’urbanisme"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected legal reference` under the exact parent path `entries[2]`. | `compile_bess_planning_feature_policy` |
| `entries[2].expected_regulation_reference` | `"R151-52 2°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected regulation reference` under the exact parent path `entries[2]`. | `compile_bess_planning_feature_policy` |
| `entries[2].precheck_status` | `"CONTEXT_REVIEW_REQUIRED"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `precheck status` under the exact parent path `entries[2]`. | `compile_bess_planning_feature_policy` |
| `entries[2].confidence` | `"HIGH"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `confidence` under the exact parent path `entries[2]`. | `compile_bess_planning_feature_policy` |
| `entries[2].rationale` | `"The official code identifies an aerodrome noise-exposure-plan context that must be checked but does not establish a direct BESS constraint by itself."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `entries[2]`. | `compile_bess_planning_feature_policy` |
| `entries[2].required_human_action` | `"Review the applicable aerodrome noise-exposure plan and project-specific context with the competent authority."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `required human action` under the exact parent path `entries[2]`. | `compile_bess_planning_feature_policy` |
| `entries[2].limitations` | `"This classification uses only the official CNIG code meaning and does not interpret the local plan or determine project admissibility."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limitations` under the exact parent path `entries[2]`. | `compile_bess_planning_feature_policy` |
| `entries[3].feature_family` | `"INFORMATION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `entries[3]`. | `compile_bess_planning_feature_policy` |
| `entries[3].type_code` | `"99"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `entries[3]`. | `compile_bess_planning_feature_policy` |
| `entries[3].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `entries[3]`. | `compile_bess_planning_feature_policy` |
| `entries[3].expected_official_label` | `"Autre périmètre, secteur, plan, document, site, projet, espace."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected official label` under the exact parent path `entries[3]`. | `compile_bess_planning_feature_policy` |
| `entries[3].expected_legal_reference` | `null` | `NoneType` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; true YAML null; accepted only where the owning model field is optional/nullable | Configures `expected legal reference` under the exact parent path `entries[3]`. | `compile_bess_planning_feature_policy` |
| `entries[3].expected_regulation_reference` | `null` | `NoneType` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; true YAML null; accepted only where the owning model field is optional/nullable | Configures `expected regulation reference` under the exact parent path `entries[3]`. | `compile_bess_planning_feature_policy` |
| `entries[3].precheck_status` | `"UNKNOWN"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `precheck status` under the exact parent path `entries[3]`. | `compile_bess_planning_feature_policy` |
| `entries[3].confidence` | `"LOW"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `confidence` under the exact parent path `entries[3]`. | `compile_bess_planning_feature_policy` |
| `entries[3].rationale` | `"The official code is an unspecified other-information category and is too generic for a more precise BESS precheck."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `entries[3]`. | `compile_bess_planning_feature_policy` |
| `entries[3].required_human_action` | `"Identify and review the feature-specific local source before drawing any planning inference."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `required human action` under the exact parent path `entries[3]`. | `compile_bess_planning_feature_policy` |
| `entries[3].limitations` | `"The official code alone does not identify the local subject, rule, effect, authorization, or prohibition."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limitations` under the exact parent path `entries[3]`. | `compile_bess_planning_feature_policy` |
| `entries[4].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `entries[4]`. | `compile_bess_planning_feature_policy` |
| `entries[4].type_code` | `"01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `entries[4]`. | `compile_bess_planning_feature_policy` |
| `entries[4].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `entries[4]`. | `compile_bess_planning_feature_policy` |
| `entries[4].expected_official_label` | `"Espace boisé classé"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected official label` under the exact parent path `entries[4]`. | `compile_bess_planning_feature_policy` |
| `entries[4].expected_legal_reference` | `"L113-1"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected legal reference` under the exact parent path `entries[4]`. | `compile_bess_planning_feature_policy` |
| `entries[4].expected_regulation_reference` | `"R151-31 1°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected regulation reference` under the exact parent path `entries[4]`. | `compile_bess_planning_feature_policy` |
| `entries[4].precheck_status` | `"LIKELY_MATERIAL_CONSTRAINT"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `precheck status` under the exact parent path `entries[4]`. | `compile_bess_planning_feature_policy` |
| `entries[4].confidence` | `"HIGH"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `confidence` under the exact parent path `entries[4]`. | `compile_bess_planning_feature_policy` |
| `entries[4].rationale` | `"The official code identifies a classified wooded-area protection family likely to be material for a BESS project without meaning prohibited."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `entries[4]`. | `compile_bess_planning_feature_policy` |
| `entries[4].required_human_action` | `"Review the exact classified-area geometry, local prescription, applicable planning provisions, and project design with the competent authority."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `required human action` under the exact parent path `entries[4]`. | `compile_bess_planning_feature_policy` |
| `entries[4].limitations` | `"This preliminary classification does not interpret the local prescription or establish authorization or prohibition."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limitations` under the exact parent path `entries[4]`. | `compile_bess_planning_feature_policy` |
| `entries[5].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `entries[5]`. | `compile_bess_planning_feature_policy` |
| `entries[5].type_code` | `"05"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `entries[5]`. | `compile_bess_planning_feature_policy` |
| `entries[5].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `entries[5]`. | `compile_bess_planning_feature_policy` |
| `entries[5].expected_official_label` | `"Emplacement réservé"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected official label` under the exact parent path `entries[5]`. | `compile_bess_planning_feature_policy` |
| `entries[5].expected_legal_reference` | `"L151-41 1° à 3°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected legal reference` under the exact parent path `entries[5]`. | `compile_bess_planning_feature_policy` |
| `entries[5].expected_regulation_reference` | `"R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected regulation reference` under the exact parent path `entries[5]`. | `compile_bess_planning_feature_policy` |
| `entries[5].precheck_status` | `"MATERIAL_REVIEW_REQUIRED"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `precheck status` under the exact parent path `entries[5]`. | `compile_bess_planning_feature_policy` |
| `entries[5].confidence` | `"HIGH"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `confidence` under the exact parent path `entries[5]`. | `compile_bess_planning_feature_policy` |
| `entries[5].rationale` | `"The official code identifies a reserved-site planning mechanism that may materially affect a project and requires specific review."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `entries[5]`. | `compile_bess_planning_feature_policy` |
| `entries[5].required_human_action` | `"Review the beneficiary, purpose, exact reservation, local planning documents, and project interaction with the competent authority."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `required human action` under the exact parent path `entries[5]`. | `compile_bess_planning_feature_policy` |
| `entries[5].limitations` | `"This classification does not infer the reservation purpose from local text or determine whether a BESS project is authorized or prohibited."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limitations` under the exact parent path `entries[5]`. | `compile_bess_planning_feature_policy` |
| `entries[6].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `entries[6]`. | `compile_bess_planning_feature_policy` |
| `entries[6].type_code` | `"07"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `entries[6]`. | `compile_bess_planning_feature_policy` |
| `entries[6].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `entries[6]`. | `compile_bess_planning_feature_policy` |
| `entries[6].expected_official_label` | `"Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected official label` under the exact parent path `entries[6]`. | `compile_bess_planning_feature_policy` |
| `entries[6].expected_legal_reference` | `"L151-19 et L151-23"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected legal reference` under the exact parent path `entries[6]`. | `compile_bess_planning_feature_policy` |
| `entries[6].expected_regulation_reference` | `"R151-41 3° Et R151-43"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected regulation reference` under the exact parent path `entries[6]`. | `compile_bess_planning_feature_policy` |
| `entries[6].precheck_status` | `"LIKELY_MATERIAL_CONSTRAINT"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `precheck status` under the exact parent path `entries[6]`. | `compile_bess_planning_feature_policy` |
| `entries[6].confidence` | `"MEDIUM"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `confidence` under the exact parent path `entries[6]`. | `compile_bess_planning_feature_policy` |
| `entries[6].rationale` | `"The official code identifies a broad heritage or landscape protection family likely to be material, while its exact local subject remains unspecified."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `entries[6]`. | `compile_bess_planning_feature_policy` |
| `entries[6].required_human_action` | `"Review the protected element, local prescription, project siting and design, and competent-authority requirements."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `required human action` under the exact parent path `entries[6]`. | `compile_bess_planning_feature_policy` |
| `entries[6].limitations` | `"The broad official category does not reveal the feature-specific protected subject or establish authorization or prohibition."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limitations` under the exact parent path `entries[6]`. | `compile_bess_planning_feature_policy` |
| `entries[7].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `entries[7]`. | `compile_bess_planning_feature_policy` |
| `entries[7].type_code` | `"07"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `entries[7]`. | `compile_bess_planning_feature_policy` |
| `entries[7].subtype_code` | `"04"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `entries[7]`. | `compile_bess_planning_feature_policy` |
| `entries[7].expected_official_label` | `"Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected official label` under the exact parent path `entries[7]`. | `compile_bess_planning_feature_policy` |
| `entries[7].expected_legal_reference` | `"L151-23"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected legal reference` under the exact parent path `entries[7]`. | `compile_bess_planning_feature_policy` |
| `entries[7].expected_regulation_reference` | `"R151-43 5°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected regulation reference` under the exact parent path `entries[7]`. | `compile_bess_planning_feature_policy` |
| `entries[7].precheck_status` | `"LIKELY_MATERIAL_CONSTRAINT"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `precheck status` under the exact parent path `entries[7]`. | `compile_bess_planning_feature_policy` |
| `entries[7].confidence` | `"HIGH"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `confidence` under the exact parent path `entries[7]`. | `compile_bess_planning_feature_policy` |
| `entries[7].rationale` | `"The official subtype identifies ecological landscape preservation likely to be material for a BESS project without meaning prohibited."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `entries[7]`. | `compile_bess_planning_feature_policy` |
| `entries[7].required_human_action` | `"Review the exact preserved element, local prescription, ecological context, and project design with the competent authority."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `required human action` under the exact parent path `entries[7]`. | `compile_bess_planning_feature_policy` |
| `entries[7].limitations` | `"This classification does not interpret the local preservation rule or determine project admissibility."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limitations` under the exact parent path `entries[7]`. | `compile_bess_planning_feature_policy` |
| `entries[8].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `entries[8]`. | `compile_bess_planning_feature_policy` |
| `entries[8].type_code` | `"15"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `entries[8]`. | `compile_bess_planning_feature_policy` |
| `entries[8].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `entries[8]`. | `compile_bess_planning_feature_policy` |
| `entries[8].expected_official_label` | `"Règles d’implantation des constructions"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected official label` under the exact parent path `entries[8]`. | `compile_bess_planning_feature_policy` |
| `entries[8].expected_legal_reference` | `"L151-17 et L151-18"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected legal reference` under the exact parent path `entries[8]`. | `compile_bess_planning_feature_policy` |
| `entries[8].expected_regulation_reference` | `"R151-39 dernier al."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected regulation reference` under the exact parent path `entries[8]`. | `compile_bess_planning_feature_policy` |
| `entries[8].precheck_status` | `"DESIGN_REVIEW_REQUIRED"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `precheck status` under the exact parent path `entries[8]`. | `compile_bess_planning_feature_policy` |
| `entries[8].confidence` | `"MEDIUM"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `confidence` under the exact parent path `entries[8]`. | `compile_bess_planning_feature_policy` |
| `entries[8].rationale` | `"The official code primarily identifies construction-implantation rules relevant to project siting and design, while the local rule remains unread."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `entries[8]`. | `compile_bess_planning_feature_policy` |
| `entries[8].required_human_action` | `"Review the exact local implantation rule against the proposed equipment layout and site design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `required human action` under the exact parent path `entries[8]`. | `compile_bess_planning_feature_policy` |
| `entries[8].limitations` | `"This classification does not interpret local setbacks, feature text, or project compliance."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limitations` under the exact parent path `entries[8]`. | `compile_bess_planning_feature_policy` |
| `entries[9].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `entries[9]`. | `compile_bess_planning_feature_policy` |
| `entries[9].type_code` | `"15"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `entries[9]`. | `compile_bess_planning_feature_policy` |
| `entries[9].subtype_code` | `"01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `entries[9]`. | `compile_bess_planning_feature_policy` |
| `entries[9].expected_official_label` | `"Implantation des constructions par rapport aux voies et aux emprises publiques"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected official label` under the exact parent path `entries[9]`. | `compile_bess_planning_feature_policy` |
| `entries[9].expected_legal_reference` | `"L151-17 et L151-18"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected legal reference` under the exact parent path `entries[9]`. | `compile_bess_planning_feature_policy` |
| `entries[9].expected_regulation_reference` | `"R151-39"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected regulation reference` under the exact parent path `entries[9]`. | `compile_bess_planning_feature_policy` |
| `entries[9].precheck_status` | `"DESIGN_REVIEW_REQUIRED"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `precheck status` under the exact parent path `entries[9]`. | `compile_bess_planning_feature_policy` |
| `entries[9].confidence` | `"HIGH"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `confidence` under the exact parent path `entries[9]`. | `compile_bess_planning_feature_policy` |
| `entries[9].rationale` | `"The official subtype specifically identifies construction siting relative to roads and public rights-of-way, requiring design review."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `entries[9]`. | `compile_bess_planning_feature_policy` |
| `entries[9].required_human_action` | `"Review the exact local siting or setback rule against the proposed equipment layout and access design."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `required human action` under the exact parent path `entries[9]`. | `compile_bess_planning_feature_policy` |
| `entries[9].limitations` | `"This classification does not interpret the local setback value or establish project compliance."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limitations` under the exact parent path `entries[9]`. | `compile_bess_planning_feature_policy` |
| `entries[10].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `entries[10]`. | `compile_bess_planning_feature_policy` |
| `entries[10].type_code` | `"17"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `entries[10]`. | `compile_bess_planning_feature_policy` |
| `entries[10].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `entries[10]`. | `compile_bess_planning_feature_policy` |
| `entries[10].expected_official_label` | `"Secteur à programme de logements mixité sociale en zone U et AU"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected official label` under the exact parent path `entries[10]`. | `compile_bess_planning_feature_policy` |
| `entries[10].expected_legal_reference` | `"L151-15"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected legal reference` under the exact parent path `entries[10]`. | `compile_bess_planning_feature_policy` |
| `entries[10].expected_regulation_reference` | `"R151-38 3°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected regulation reference` under the exact parent path `entries[10]`. | `compile_bess_planning_feature_policy` |
| `entries[10].precheck_status` | `"MATERIAL_REVIEW_REQUIRED"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `precheck status` under the exact parent path `entries[10]`. | `compile_bess_planning_feature_policy` |
| `entries[10].confidence` | `"MEDIUM"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `confidence` under the exact parent path `entries[10]`. | `compile_bess_planning_feature_policy` |
| `entries[10].rationale` | `"The official code identifies a social-housing-program planning mechanism that may materially affect land use and requires specific review."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `entries[10]`. | `compile_bess_planning_feature_policy` |
| `entries[10].required_human_action` | `"Review the sector program, local planning provisions, land-use interaction, and authority requirements for the proposed project."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `required human action` under the exact parent path `entries[10]`. | `compile_bess_planning_feature_policy` |
| `entries[10].limitations` | `"This classification does not infer the local program content or determine BESS authorization or prohibition."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limitations` under the exact parent path `entries[10]`. | `compile_bess_planning_feature_policy` |
| `entries[11].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `entries[11]`. | `compile_bess_planning_feature_policy` |
| `entries[11].type_code` | `"18"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `entries[11]`. | `compile_bess_planning_feature_policy` |
| `entries[11].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `entries[11]`. | `compile_bess_planning_feature_policy` |
| `entries[11].expected_official_label` | `"Périmètre comportant des orientations d’aménagement et de programmation (OAP)"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected official label` under the exact parent path `entries[11]`. | `compile_bess_planning_feature_policy` |
| `entries[11].expected_legal_reference` | `"L151-6 et L151-7"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected legal reference` under the exact parent path `entries[11]`. | `compile_bess_planning_feature_policy` |
| `entries[11].expected_regulation_reference` | `"R151-6 à R151-8-1"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `expected regulation reference` under the exact parent path `entries[11]`. | `compile_bess_planning_feature_policy` |
| `entries[11].precheck_status` | `"MATERIAL_REVIEW_REQUIRED"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `precheck status` under the exact parent path `entries[11]`. | `compile_bess_planning_feature_policy` |
| `entries[11].confidence` | `"HIGH"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `confidence` under the exact parent path `entries[11]`. | `compile_bess_planning_feature_policy` |
| `entries[11].rationale` | `"The official code identifies an area governed by planning and development guidelines that may materially affect a project and requires specific review."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `rationale` under the exact parent path `entries[11]`. | `compile_bess_planning_feature_policy` |
| `entries[11].required_human_action` | `"Review the applicable OAP text and graphics, project design interaction, and competent-authority requirements."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `required human action` under the exact parent path `entries[11]`. | `compile_bess_planning_feature_policy` |
| `entries[11].limitations` | `"This classification does not interpret the local OAP or establish authorization, prohibition, or buildability."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `limitations` under the exact parent path `entries[11]`. | `compile_bess_planning_feature_policy` |

## STEP 7F.1A.4 dependent-model refresh

- The YAML bytes and checked-in values are unchanged. STEP 7F.1A.4 changes their owning validation/authority boundary through `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config`; section 5 now embeds the exact current owning model sources and qualified consumers.
- Decision-input models are frozen/deeply immutable where their current source declares that contract; trust-bearing YAML is decoded through the shared duplicate-rejecting loader where the owning loader source shows that call.
- No configured policy meaning, source identity, threshold, artifact schema, or output schema is changed by this dependent documentation refresh.

## 5. Classes / models / dataclasses

- Exact checked-in configuration SHA256 remains `8a26fcb8ee7e2f028baca65d94c2b5be5445ba9fc4b82b9b1a21843f933f8b2a`; its values are unchanged by STEP 7F.1A.4.
- Authoritative loader/config boundary: `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config`.
- Owning Python module: `landscout.stages.bess_planning_feature_policy`.
- The owning model declarations below are refreshed from the current source so frozen/deeply immutable fields, strict serialization, exact domains, validators, and internal metadata schemas cannot remain stale merely because the YAML bytes did not change.

### `_StrictPolicyModel`

**Source purpose:** Defines `_StrictPolicyModel`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

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
class _StrictPolicyModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `PolicyTableSchemaSignature`

**Source purpose:** Immutable persisted schema identity for the normalized policy table.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `columns` | `tuple[StrictStr, ...]` | `required` | `columns: tuple[StrictStr, ...]` |
| `dtypes` | `tuple[StrictStr, ...]` | `required` | `dtypes: tuple[StrictStr, ...]` |
| `index_class` | `StrictStr` | `required` | `index_class: StrictStr` |
| `index_names` | `tuple[StrictStr \| None, ...]` | `required` | `index_names: tuple[StrictStr \| None, ...]` |
| `index_level_dtypes` | `tuple[StrictStr, ...]` | `required` | `index_level_dtypes: tuple[StrictStr, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class PolicyTableSchemaSignature(_StrictPolicyModel):
    """Immutable persisted schema identity for the normalized policy table."""

    columns: tuple[StrictStr, ...]
    dtypes: tuple[StrictStr, ...]
    index_class: StrictStr
    index_names: tuple[StrictStr | None, ...]
    index_level_dtypes: tuple[StrictStr, ...]
```

### `PolicySourceLock`

**Source purpose:** Defines `PolicySourceLock`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `document_id` | `StrictStr` | `required` | `document_id: StrictStr` |
| `archive_sha256` | `StrictStr` | `required` | `archive_sha256: StrictStr` |
| `cnig_profile` | `StrictStr` | `required` | `cnig_profile: StrictStr` |
| `cnig_profile_schema_version` | `StrictInt` | `required` | `cnig_profile_schema_version: StrictInt` |
| `cnig_profile_sha256` | `StrictStr` | `required` | `cnig_profile_sha256: StrictStr` |
| `cnig_result_hash_schema_version` | `StrictInt` | `required` | `cnig_result_hash_schema_version: StrictInt` |
| `cnig_complete_result_content_sha256` | `StrictStr` | `required` | `cnig_complete_result_content_sha256: StrictStr` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.bess_planning_feature_policy::PolicySourceLock._validate_lock` via `PolicySourceLock`

**Exact class source**

```python
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
```

### `PolicyEntry`

**Source purpose:** Defines `PolicyEntry`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `feature_family` | `FeatureFamily` | `required` | `feature_family: FeatureFamily` |
| `type_code` | `StrictStr` | `required` | `type_code: StrictStr` |
| `subtype_code` | `StrictStr` | `required` | `subtype_code: StrictStr` |
| `expected_official_label` | `StrictStr` | `required` | `expected_official_label: StrictStr` |
| `expected_legal_reference` | `StrictStr \| None` | `required` | `expected_legal_reference: StrictStr \| None` |
| `expected_regulation_reference` | `StrictStr \| None` | `required` | `expected_regulation_reference: StrictStr \| None` |
| `precheck_status` | `PrecheckStatus` | `required` | `precheck_status: PrecheckStatus` |
| `confidence` | `Confidence` | `required` | `confidence: Confidence` |
| `rationale` | `StrictStr` | `required` | `rationale: StrictStr` |
| `required_human_action` | `StrictStr` | `required` | `required_human_action: StrictStr` |
| `limitations` | `StrictStr` | `required` | `limitations: StrictStr` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.bess_planning_feature_policy::PolicyEntry._validate_entry` via `PolicyEntry`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_entries_sha256` via `PolicyEntry`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_policy_completeness` via `PolicyEntry`

**Exact class source**

```python
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
```

### `BessPlanningFeaturePolicyConfig`

**Source purpose:** Defines `BessPlanningFeaturePolicyConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictPolicyModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `profile` | `StrictStr` | `required` | `profile: StrictStr` |
| `policy_scope` | `Literal['OFFICIAL_CNIG_CODE_MEANING_ONLY']` | `required` | `policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]` |
| `local_feature_text_interpreted` | `StrictBool` | `required` | `local_feature_text_interpreted: StrictBool` |
| `local_regulation_content_interpreted` | `StrictBool` | `required` | `local_regulation_content_interpreted: StrictBool` |
| `legal_conclusion_produced` | `StrictBool` | `required` | `legal_conclusion_produced: StrictBool` |
| `source_lock` | `PolicySourceLock` | `required` | `source_lock: PolicySourceLock` |
| `status_priority` | `dict[PrecheckStatus, StrictInt]` | `required` | `status_priority: dict[PrecheckStatus, StrictInt]` |
| `canonical_policy_entries_sha256` | `StrictStr` | `required` | `canonical_policy_entries_sha256: StrictStr` |
| `entries` | `tuple[PolicyEntry, ...]` | `required` | `entries: tuple[PolicyEntry, ...]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyArtifactManifest,
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_artifacts,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- import: `landscout.stages.aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
)`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_source` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `BessPlanningFeaturePolicyConfig`
- import: `landscout.stages.apply_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyResult,
    validate_bess_planning_feature_policy_result,
    validate_bess_planning_feature_policy_result_envelope,
)`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_policy_source` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::BessPlanningFeaturePolicyConfig._validate_policy` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::load_bess_planning_feature_policy_config` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_resolved_policy_config` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_sha256` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_source_lock` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_policy_completeness` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_policy_table` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_build_result` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `BessPlanningFeaturePolicyConfig`
- import: `tests.unit.test_bess_planning_feature_policy::<module>` via `from landscout.stages.bess_planning_feature_policy import (
    BessPlanningFeaturePolicyConfig,
    BessPlanningFeaturePolicyError,
    BessPlanningFeaturePolicyResult,
    compile_bess_planning_feature_policy,
    load_bess_planning_feature_policy_config,
    validate_bess_planning_feature_policy_result,
)`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_compiled_fixture` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::_validated_config` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_profile_v1_snapshot_detects_policy_text_drift` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_profile_v1_snapshot_detects_source_lock_drift` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_duplicate_policy_pair_is_rejected` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_invalid_or_legal_conclusion_status_is_rejected` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_invalid_confidence_is_rejected` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_status_priority_contract_is_strict` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_unknown_yaml_field_is_rejected` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_noncanonical_whitespace_is_rejected` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_malformed_sha256_is_rejected` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_policy_entries_require_deterministic_order` via `BessPlanningFeaturePolicyConfig`
- value/type reference: `tests.unit.test_bess_planning_feature_policy::test_compiler_and_public_validator_invoke_source_complete_coding_validation` via `BessPlanningFeaturePolicyConfig`

**Exact class source**

```python
class BessPlanningFeaturePolicyConfig(_StrictPolicyModel):
    schema_version: StrictInt
    profile: StrictStr
    policy_scope: Literal["OFFICIAL_CNIG_CODE_MEANING_ONLY"]
    local_feature_text_interpreted: StrictBool
    local_regulation_content_interpreted: StrictBool
    legal_conclusion_produced: StrictBool
    source_lock: PolicySourceLock
    status_priority: dict[PrecheckStatus, StrictInt]
    canonical_policy_entries_sha256: StrictStr
    entries: tuple[PolicyEntry, ...]

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
```

## 6. Functions and methods

Loader: `landscout.stages.bess_planning_feature_policy.load_bess_planning_feature_policy_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, exact validation, and any hashing actually performed by that loader.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `compile_bess_planning_feature_policy`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

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
