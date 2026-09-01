# `configs/planning/cnig_plu_2017_feature_codes.yaml`

## File identity

- Repository path: `configs/planning/cnig_plu_2017_feature_codes.yaml`
- File type: YAML checked-in configuration/policy/source lock
- Responsibility: Defines the approved CNIG PLU v2017 official planning-feature code pairs, labels, references, and profile identity.
- Source SHA256: `77407429fd414eece8f6b20ca4da587aac76ab6b0b93e02f148622ab85ee253e`

## 1. Purpose

Defines the approved CNIG PLU v2017 official planning-feature code pairs, labels, references, and profile identity.

## 2. Position in LandScout architecture

The exact YAML bytes are parsed by `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile` into `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile`. Runtime consumers include `resolve_planning_feature_codes`.

## 3. Imports and dependencies

Not applicable to YAML. Python/Pydantic consumers are named above and reproduced below.

## 4. Contract taxonomy

Every row below is a configuration field/list leaf. It is not a DataFrame column unless a consuming stage explicitly copies it into a documented result schema.

| Exact YAML path | Checked-in value | Runtime type | Required/nullability/allowed-domain/unit contract | Semantic role | Consumers |
|---|---|---|---|---|---|
| `schema_version` | `2` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required supported schema integer; accepted versions are pinned by the owning Literal/validator | Selects the strict configuration schema; unsupported versions are rejected. | `resolve_planning_feature_codes` |
| `profile` | `"cnig_plu_2017_muret_observed_pairs_v2"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `profile` under the exact parent path `<root>`. | `resolve_planning_feature_codes` |
| `standard_model` | `"CNIG PLU v2017"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Names the official planning standard/model against which records are validated. | `resolve_planning_feature_codes` |
| `official_text_normalization` | `"GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official text normalization` under the exact parent path `<root>`. | `resolve_planning_feature_codes` |
| `official_sources.prescription` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `prescription` under the exact parent path `official_sources`. | `resolve_planning_feature_codes` |
| `official_sources.information` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `information` under the exact parent path `official_sources`. | `resolve_planning_feature_codes` |
| `retrieval_date` | `"2026-08-12"` | `date` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `retrieval date` under the exact parent path `<root>`. | `resolve_planning_feature_codes` |
| `canonical_records_sha256` | `"5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `canonical_records_sha256`. | `resolve_planning_feature_codes` |
| `records[0].feature_family` | `"INFORMATION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[0]`. | `resolve_planning_feature_codes` |
| `records[0].type_code` | `"02"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[0]`. | `resolve_planning_feature_codes` |
| `records[0].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[0]`. | `resolve_planning_feature_codes` |
| `records[0].official_label` | `"Zone d'aménagement concerté"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[0]`. | `resolve_planning_feature_codes` |
| `records[0].legal_reference` | `"L311-1 code de l’urbanisme"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[0]`. | `resolve_planning_feature_codes` |
| `records[0].regulation_or_annex_reference` | `"R151-52 8°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[0]`. | `resolve_planning_feature_codes` |
| `records[0].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[1].feature_family` | `"INFORMATION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[1]`. | `resolve_planning_feature_codes` |
| `records[1].type_code` | `"14"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[1]`. | `resolve_planning_feature_codes` |
| `records[1].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[1]`. | `resolve_planning_feature_codes` |
| `records[1].official_label` | `"Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[1]`. | `resolve_planning_feature_codes` |
| `records[1].legal_reference` | `"L571-10 code de l’environnement"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[1]`. | `resolve_planning_feature_codes` |
| `records[1].regulation_or_annex_reference` | `"R151-53 5°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[1]`. | `resolve_planning_feature_codes` |
| `records[1].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[2].feature_family` | `"INFORMATION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[2]`. | `resolve_planning_feature_codes` |
| `records[2].type_code` | `"27"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[2]`. | `resolve_planning_feature_codes` |
| `records[2].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[2]`. | `resolve_planning_feature_codes` |
| `records[2].official_label` | `"Plan d'exposition au bruit des aérodromes"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[2]`. | `resolve_planning_feature_codes` |
| `records[2].legal_reference` | `"L112-6 code de l’urbanisme"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[2]`. | `resolve_planning_feature_codes` |
| `records[2].regulation_or_annex_reference` | `"R151-52 2°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[2]`. | `resolve_planning_feature_codes` |
| `records[2].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[3].feature_family` | `"INFORMATION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[3]`. | `resolve_planning_feature_codes` |
| `records[3].type_code` | `"99"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[3]`. | `resolve_planning_feature_codes` |
| `records[3].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[3]`. | `resolve_planning_feature_codes` |
| `records[3].official_label` | `"Autre périmètre, secteur, plan, document, site, projet, espace."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[3]`. | `resolve_planning_feature_codes` |
| `records[3].legal_reference` | `null` | `NoneType` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; true YAML null; accepted only where the owning model field is optional/nullable | Configures `legal reference` under the exact parent path `records[3]`. | `resolve_planning_feature_codes` |
| `records[3].regulation_or_annex_reference` | `null` | `NoneType` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; true YAML null; accepted only where the owning model field is optional/nullable | Configures `regulation or annex reference` under the exact parent path `records[3]`. | `resolve_planning_feature_codes` |
| `records[3].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[4].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[4]`. | `resolve_planning_feature_codes` |
| `records[4].type_code` | `"01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[4]`. | `resolve_planning_feature_codes` |
| `records[4].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[4]`. | `resolve_planning_feature_codes` |
| `records[4].official_label` | `"Espace boisé classé"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[4]`. | `resolve_planning_feature_codes` |
| `records[4].legal_reference` | `"L113-1"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[4]`. | `resolve_planning_feature_codes` |
| `records[4].regulation_or_annex_reference` | `"R151-31 1°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[4]`. | `resolve_planning_feature_codes` |
| `records[4].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[5].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[5]`. | `resolve_planning_feature_codes` |
| `records[5].type_code` | `"05"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[5]`. | `resolve_planning_feature_codes` |
| `records[5].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[5]`. | `resolve_planning_feature_codes` |
| `records[5].official_label` | `"Emplacement réservé"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[5]`. | `resolve_planning_feature_codes` |
| `records[5].legal_reference` | `"L151-41 1° à 3°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[5]`. | `resolve_planning_feature_codes` |
| `records[5].regulation_or_annex_reference` | `"R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[5]`. | `resolve_planning_feature_codes` |
| `records[5].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[6].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[6]`. | `resolve_planning_feature_codes` |
| `records[6].type_code` | `"07"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[6]`. | `resolve_planning_feature_codes` |
| `records[6].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[6]`. | `resolve_planning_feature_codes` |
| `records[6].official_label` | `"Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[6]`. | `resolve_planning_feature_codes` |
| `records[6].legal_reference` | `"L151-19 et L151-23"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[6]`. | `resolve_planning_feature_codes` |
| `records[6].regulation_or_annex_reference` | `"R151-41 3° Et R151-43"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[6]`. | `resolve_planning_feature_codes` |
| `records[6].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[7].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[7]`. | `resolve_planning_feature_codes` |
| `records[7].type_code` | `"07"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[7]`. | `resolve_planning_feature_codes` |
| `records[7].subtype_code` | `"04"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[7]`. | `resolve_planning_feature_codes` |
| `records[7].official_label` | `"Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[7]`. | `resolve_planning_feature_codes` |
| `records[7].legal_reference` | `"L151-23"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[7]`. | `resolve_planning_feature_codes` |
| `records[7].regulation_or_annex_reference` | `"R151-43 5°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[7]`. | `resolve_planning_feature_codes` |
| `records[7].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[8].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[8]`. | `resolve_planning_feature_codes` |
| `records[8].type_code` | `"15"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[8]`. | `resolve_planning_feature_codes` |
| `records[8].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[8]`. | `resolve_planning_feature_codes` |
| `records[8].official_label` | `"Règles d’implantation des constructions"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[8]`. | `resolve_planning_feature_codes` |
| `records[8].legal_reference` | `"L151-17 et L151-18"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[8]`. | `resolve_planning_feature_codes` |
| `records[8].regulation_or_annex_reference` | `"R151-39 dernier al."` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[8]`. | `resolve_planning_feature_codes` |
| `records[8].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[9].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[9]`. | `resolve_planning_feature_codes` |
| `records[9].type_code` | `"15"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[9]`. | `resolve_planning_feature_codes` |
| `records[9].subtype_code` | `"01"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[9]`. | `resolve_planning_feature_codes` |
| `records[9].official_label` | `"Implantation des constructions par rapport aux voies et aux emprises publiques"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[9]`. | `resolve_planning_feature_codes` |
| `records[9].legal_reference` | `"L151-17 et L151-18"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[9]`. | `resolve_planning_feature_codes` |
| `records[9].regulation_or_annex_reference` | `"R151-39"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[9]`. | `resolve_planning_feature_codes` |
| `records[9].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[10].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[10]`. | `resolve_planning_feature_codes` |
| `records[10].type_code` | `"17"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[10]`. | `resolve_planning_feature_codes` |
| `records[10].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[10]`. | `resolve_planning_feature_codes` |
| `records[10].official_label` | `"Secteur à programme de logements mixité sociale en zone U et AU"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[10]`. | `resolve_planning_feature_codes` |
| `records[10].legal_reference` | `"L151-15"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[10]`. | `resolve_planning_feature_codes` |
| `records[10].regulation_or_annex_reference` | `"R151-38 3°"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[10]`. | `resolve_planning_feature_codes` |
| `records[10].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[11].feature_family` | `"PRESCRIPTION"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[11]`. | `resolve_planning_feature_codes` |
| `records[11].type_code` | `"18"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[11]`. | `resolve_planning_feature_codes` |
| `records[11].subtype_code` | `"00"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[11]`. | `resolve_planning_feature_codes` |
| `records[11].official_label` | `"Périmètre comportant des orientations d’aménagement et de programmation (OAP)"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[11]`. | `resolve_planning_feature_codes` |
| `records[11].legal_reference` | `"L151-6 et L151-7"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[11]`. | `resolve_planning_feature_codes` |
| `records[11].regulation_or_annex_reference` | `"R151-6 à R151-8-1"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[11]`. | `resolve_planning_feature_codes` |
| `records[11].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |

## STEP 7F.1A.4 dependent-model refresh

- The YAML bytes and checked-in values are unchanged. STEP 7F.1A.4 changes their owning validation/authority boundary through `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile`; section 5 now embeds the exact current owning model sources and qualified consumers.
- Decision-input models are frozen/deeply immutable where their current source declares that contract; trust-bearing YAML is decoded through the shared duplicate-rejecting loader where the owning loader source shows that call.
- No configured policy meaning, source identity, threshold, artifact schema, or output schema is changed by this dependent documentation refresh.

## 5. Classes / models / dataclasses

- Exact checked-in configuration SHA256 remains `77407429fd414eece8f6b20ca4da587aac76ab6b0b93e02f148622ab85ee253e`; its values are unchanged by STEP 7F.1A.4.
- Authoritative loader/config boundary: `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile`.
- Owning Python module: `landscout.stages.resolve_planning_feature_codes`.
- The owning model declarations below are refreshed from the current source so frozen/deeply immutable fields, strict serialization, exact domains, validators, and internal metadata schemas cannot remain stale merely because the YAML bytes did not change.

### `_StrictModel`

**Source purpose:** Defines `_StrictModel`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

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
class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
```

### `OfficialSourceUrls`

**Source purpose:** Defines `OfficialSourceUrls`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `prescription` | `StrictStr` | `required` | `prescription: StrictStr` |
| `information` | `StrictStr` | `required` | `information: StrictStr` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.resolve_planning_feature_codes::OfficialSourceUrls._validate_urls` via `OfficialSourceUrls`

**Exact class source**

```python
class OfficialSourceUrls(_StrictModel):
    prescription: StrictStr
    information: StrictStr

    @model_validator(mode="after")
    def _validate_urls(self) -> OfficialSourceUrls:
        if self.prescription != PRESCRIPTION_OFFICIAL_SOURCE_URL:
            raise ValueError(
                "prescription source URL is not the exact official GPU host endpoint"
            )
        if self.information != INFORMATION_OFFICIAL_SOURCE_URL:
            raise ValueError(
                "information source URL is not the exact official GPU host endpoint"
            )
        return self
```

### `CnigFeatureCodeRecord`

**Source purpose:** Defines `CnigFeatureCodeRecord`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `feature_family` | `FeatureFamily` | `required` | `feature_family: FeatureFamily` |
| `type_code` | `StrictStr` | `required` | `type_code: StrictStr` |
| `subtype_code` | `StrictStr` | `required` | `subtype_code: StrictStr` |
| `official_label` | `StrictStr` | `required` | `official_label: StrictStr` |
| `legal_reference` | `StrictStr \| None` | `required` | `legal_reference: StrictStr \| None` |
| `regulation_or_annex_reference` | `StrictStr \| None` | `required` | `regulation_or_annex_reference: StrictStr \| None` |
| `official_source_url` | `StrictStr` | `required` | `official_source_url: StrictStr` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.resolve_planning_feature_codes::CnigFeatureCodeRecord._validate_record` via `CnigFeatureCodeRecord`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_record_payload` via `CnigFeatureCodeRecord`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_records_sha256` via `CnigFeatureCodeRecord`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_lookup` via `CnigFeatureCodeRecord`

**Exact class source**

```python
class CnigFeatureCodeRecord(_StrictModel):
    feature_family: FeatureFamily
    type_code: StrictStr
    subtype_code: StrictStr
    official_label: StrictStr
    legal_reference: StrictStr | None
    regulation_or_annex_reference: StrictStr | None
    official_source_url: StrictStr

    @model_validator(mode="after")
    def _validate_record(self) -> CnigFeatureCodeRecord:
        for code, label in (
            (self.type_code, "type code"),
            (self.subtype_code, "subtype code"),
        ):
            if _CODE_PATTERN.fullmatch(code) is None:
                raise ValueError(f"{label} must contain exactly two digits")
        _validate_official_text(self.official_label, "official label")
        _validate_optional_official_text(self.legal_reference, "legal reference")
        _validate_optional_official_text(
            self.regulation_or_annex_reference,
            "regulation or annex reference",
        )
        expected_url = (
            PRESCRIPTION_OFFICIAL_SOURCE_URL
            if self.feature_family == "PRESCRIPTION"
            else INFORMATION_OFFICIAL_SOURCE_URL
        )
        if self.official_source_url != expected_url:
            raise ValueError("record source URL is not the exact family endpoint")
        return self
```

### `CnigFeatureCodeProfile`

**Source purpose:** Strict offline snapshot of official CNIG feature code records.

- Exact decorators: none.
- Exact bases: `_StrictModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `profile` | `StrictStr` | `Field(min_length=1)` | `profile: StrictStr = Field(min_length=1)` |
| `standard_model` | `Literal['CNIG PLU v2017']` | `required` | `standard_model: Literal["CNIG PLU v2017"]` |
| `official_text_normalization` | `Literal['GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1']` | `required` | `official_text_normalization: Literal["GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"]` |
| `official_sources` | `OfficialSourceUrls` | `required` | `official_sources: OfficialSourceUrls` |
| `retrieval_date` | `date` | `required` | `retrieval_date: date` |
| `canonical_records_sha256` | `StrictStr` | `required` | `canonical_records_sha256: StrictStr` |
| `records` | `tuple[CnigFeatureCodeRecord, ...]` | `Field(min_length=1)` | `records: tuple[CnigFeatureCodeRecord, ...] = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    load_cnig_feature_code_profile,
    resolve_planning_feature_codes,
    validate_planning_feature_code_result,
    validate_planning_feature_code_result_envelope,
)`
- import: `landscout.stages.aggregate_bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
)`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::_validate_application_source` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::aggregate_bess_planning_feature_policy_to_parcels` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.aggregate_bess_planning_feature_policy::validate_bess_planning_feature_parcel_aggregation_result` via `CnigFeatureCodeProfile`
- import: `landscout.stages.apply_bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result_envelope,
)`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::_validate_policy_source` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::apply_bess_planning_feature_policy` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.apply_bess_planning_feature_policy::validate_bess_planning_feature_application_result` via `CnigFeatureCodeProfile`
- import: `landscout.stages.bess_planning_feature_policy::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CnigFeatureCodeProfile,
    PlanningFeatureCodeResult,
    validate_planning_feature_code_result,
)`
- value/type reference: `landscout.stages.bess_planning_feature_policy::_validate_coded_source` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.bess_planning_feature_policy::compile_bess_planning_feature_policy` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.bess_planning_feature_policy::validate_bess_planning_feature_policy_result` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::CnigFeatureCodeProfile._validate_profile` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::load_cnig_feature_code_profile` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_resolved_profile` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_profile_sha256` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_dictionary` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_lookup` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_coded_catalog` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::_build_result` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::validate_planning_feature_code_result` via `CnigFeatureCodeProfile`
- value/type reference: `landscout.stages.resolve_planning_feature_codes::resolve_planning_feature_codes` via `CnigFeatureCodeProfile`
- import: `tests.unit.test_resolve_planning_feature_codes::<module>` via `from landscout.stages.resolve_planning_feature_codes import (
    CODE_DICTIONARY_COLUMNS,
    OFFICIAL_CODE_COLUMNS,
    CnigFeatureCodeProfile,
    PlanningFeatureCodeError,
    PlanningFeatureCodeResult,
    _result_with_hashes,
    load_cnig_feature_code_profile,
)`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_profile` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_mutated_profile` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_integration_inputs` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::_inputs` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::resolve_planning_feature_codes` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::validate_planning_feature_code_result` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_no_type_only_or_cross_family_fallback_and_unknown_is_retained` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_invalid_schema_is_revalidated` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_in_memory_profile_model_construct_with_duplicate_pair_is_revalidated` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_official_family_endpoints_require_exact_identity` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_official_text_must_already_be_canonical` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_malformed_code_is_rejected` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_duplicate_pair_and_profile_hash_mutation_are_rejected` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_wrong_official_host_and_unknown_field_are_rejected` via `CnigFeatureCodeProfile`
- value/type reference: `tests.unit.test_resolve_planning_feature_codes::test_record_order_must_be_deterministic` via `CnigFeatureCodeProfile`

**Exact class source**

```python
class CnigFeatureCodeProfile(_StrictModel):
    """Strict offline snapshot of official CNIG feature code records."""

    schema_version: StrictInt
    profile: StrictStr = Field(min_length=1)
    standard_model: Literal["CNIG PLU v2017"]
    official_text_normalization: Literal["GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"]
    official_sources: OfficialSourceUrls
    retrieval_date: date
    canonical_records_sha256: StrictStr
    records: tuple[CnigFeatureCodeRecord, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def _validate_profile(self) -> CnigFeatureCodeProfile:
        if self.schema_version != PROFILE_SCHEMA_VERSION:
            raise ValueError(
                f"unsupported CNIG feature-code profile schema: {self.schema_version}"
            )
        _exact_string(self.profile, "code profile")
        if _SHA_PATTERN.fullmatch(self.canonical_records_sha256) is None:
            raise ValueError("canonical records SHA256 is invalid")
        keys = [
            (record.feature_family, record.type_code, record.subtype_code)
            for record in self.records
        ]
        if len(set(keys)) != len(keys):
            raise ValueError("configured CNIG code pairs contain a duplicate")
        if keys != sorted(keys):
            raise ValueError("configured CNIG records must use deterministic order")
        if _records_sha256(self.records) != self.canonical_records_sha256:
            raise ValueError("canonical records SHA256 differs from configured records")
        return self
```

## 6. Functions and methods

Loader: `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, exact validation, and any hashing actually performed by that loader.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `resolve_planning_feature_codes`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

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

### Authoritative raw-byte payload

- Raw byte length: `4934`.
- Raw SHA256: `77407429fd414eece8f6b20ca4da587aac76ab6b0b93e02f148622ab85ee253e` (identical to **File identity**).
- Encoding: RFC 4648 Base64, wrapped for display only. Decoding the concatenated payload reproduces every original byte, including mixed CRLF/LF positions.

```text
c2NoZW1hX3ZlcnNpb246IDIKcHJvZmlsZTogY25pZ19wbHVfMjAxN19tdXJldF9vYnNlcnZlZF9w
YWlyc192MgpzdGFuZGFyZF9tb2RlbDogQ05JRyBQTFUgdjIwMTcKb2ZmaWNpYWxfdGV4dF9ub3Jt
YWxpemF0aW9uOiBHUFVfRElTUExBWV9URVhUX05GQ19XSElURVNQQUNFX1YxCm9mZmljaWFsX3Nv
dXJjZXM6CiAgcHJlc2NyaXB0aW9uOiBodHRwczovL3d3dy5nZW9wb3J0YWlsLXVyYmFuaXNtZS5n
b3V2LmZyL3N0YW5kYXJkL2NuaWdfUExVXzIwMTcvY29kZXMvUHJlc2NyaXB0aW9uVXJiYVR5cGUK
ICBpbmZvcm1hdGlvbjogaHR0cHM6Ly93d3cuZ2VvcG9ydGFpbC11cmJhbmlzbWUuZ291di5mci9z
dGFuZGFyZC9jbmlnX1BMVV8yMDE3L2NvZGVzL0luZm9ybWF0aW9uVXJiYVR5cGUKcmV0cmlldmFs
X2RhdGU6IDIwMjYtMDgtMTIKY2Fub25pY2FsX3JlY29yZHNfc2hhMjU2OiA1OTkwNTUyYTY4MWE5
ZTUwYzA3MmViMjA3YmY4OGQyNWM4NzZmNjFjODllZWI4ODYxOGU3NGQ5MDU0ODc2NzJjCnJlY29y
ZHM6CiAgLSBmZWF0dXJlX2ZhbWlseTogSU5GT1JNQVRJT04KICAgIHR5cGVfY29kZTogIjAyIgog
ICAgc3VidHlwZV9jb2RlOiAiMDAiCiAgICBvZmZpY2lhbF9sYWJlbDogWm9uZSBkJ2Ftw6luYWdl
bWVudCBjb25jZXJ0w6kKICAgIGxlZ2FsX3JlZmVyZW5jZTogTDMxMS0xIGNvZGUgZGUgbOKAmXVy
YmFuaXNtZQogICAgcmVndWxhdGlvbl9vcl9hbm5leF9yZWZlcmVuY2U6IFIxNTEtNTIgOMKwCiAg
ICBvZmZpY2lhbF9zb3VyY2VfdXJsOiBodHRwczovL3d3dy5nZW9wb3J0YWlsLXVyYmFuaXNtZS5n
b3V2LmZyL3N0YW5kYXJkL2NuaWdfUExVXzIwMTcvY29kZXMvSW5mb3JtYXRpb25VcmJhVHlwZQog
IC0gZmVhdHVyZV9mYW1pbHk6IElORk9STUFUSU9OCiAgICB0eXBlX2NvZGU6ICIxNCIKICAgIHN1
YnR5cGVfY29kZTogIjAwIgogICAgb2ZmaWNpYWxfbGFiZWw6IFDDqXJpbcOodHJlIGRlIHZvaXNp
bmFnZSBkJ2luZnJhc3RydWN0dXJlIGRlIHRyYW5zcG9ydCB0ZXJyZXN0cmUgKHNlY3RldXIgYWZm
ZWN0w6kgcGFyIGxlIGJydWl0KQogICAgbGVnYWxfcmVmZXJlbmNlOiBMNTcxLTEwIGNvZGUgZGUg
bOKAmWVudmlyb25uZW1lbnQKICAgIHJlZ3VsYXRpb25fb3JfYW5uZXhfcmVmZXJlbmNlOiBSMTUx
LTUzIDXCsAogICAgb2ZmaWNpYWxfc291cmNlX3VybDogaHR0cHM6Ly93d3cuZ2VvcG9ydGFpbC11
cmJhbmlzbWUuZ291di5mci9zdGFuZGFyZC9jbmlnX1BMVV8yMDE3L2NvZGVzL0luZm9ybWF0aW9u
VXJiYVR5cGUKICAtIGZlYXR1cmVfZmFtaWx5OiBJTkZPUk1BVElPTgogICAgdHlwZV9jb2RlOiAi
MjciCiAgICBzdWJ0eXBlX2NvZGU6ICIwMCIKICAgIG9mZmljaWFsX2xhYmVsOiBQbGFuIGQnZXhw
b3NpdGlvbiBhdSBicnVpdCBkZXMgYcOpcm9kcm9tZXMKICAgIGxlZ2FsX3JlZmVyZW5jZTogTDEx
Mi02IGNvZGUgZGUgbOKAmXVyYmFuaXNtZQogICAgcmVndWxhdGlvbl9vcl9hbm5leF9yZWZlcmVu
Y2U6IFIxNTEtNTIgMsKwCiAgICBvZmZpY2lhbF9zb3VyY2VfdXJsOiBodHRwczovL3d3dy5nZW9w
b3J0YWlsLXVyYmFuaXNtZS5nb3V2LmZyL3N0YW5kYXJkL2NuaWdfUExVXzIwMTcvY29kZXMvSW5m
b3JtYXRpb25VcmJhVHlwZQogIC0gZmVhdHVyZV9mYW1pbHk6IElORk9STUFUSU9OCiAgICB0eXBl
X2NvZGU6ICI5OSIKICAgIHN1YnR5cGVfY29kZTogIjAwIgogICAgb2ZmaWNpYWxfbGFiZWw6IEF1
dHJlIHDDqXJpbcOodHJlLCBzZWN0ZXVyLCBwbGFuLCBkb2N1bWVudCwgc2l0ZSwgcHJvamV0LCBl
c3BhY2UuCiAgICBsZWdhbF9yZWZlcmVuY2U6IG51bGwKICAgIHJlZ3VsYXRpb25fb3JfYW5uZXhf
cmVmZXJlbmNlOiBudWxsCiAgICBvZmZpY2lhbF9zb3VyY2VfdXJsOiBodHRwczovL3d3dy5nZW9w
b3J0YWlsLXVyYmFuaXNtZS5nb3V2LmZyL3N0YW5kYXJkL2NuaWdfUExVXzIwMTcvY29kZXMvSW5m
b3JtYXRpb25VcmJhVHlwZQogIC0gZmVhdHVyZV9mYW1pbHk6IFBSRVNDUklQVElPTgogICAgdHlw
ZV9jb2RlOiAiMDEiCiAgICBzdWJ0eXBlX2NvZGU6ICIwMCIKICAgIG9mZmljaWFsX2xhYmVsOiBF
c3BhY2UgYm9pc8OpIGNsYXNzw6kKICAgIGxlZ2FsX3JlZmVyZW5jZTogTDExMy0xCiAgICByZWd1
bGF0aW9uX29yX2FubmV4X3JlZmVyZW5jZTogUjE1MS0zMSAxwrAKICAgIG9mZmljaWFsX3NvdXJj
ZV91cmw6IGh0dHBzOi8vd3d3Lmdlb3BvcnRhaWwtdXJiYW5pc21lLmdvdXYuZnIvc3RhbmRhcmQv
Y25pZ19QTFVfMjAxNy9jb2Rlcy9QcmVzY3JpcHRpb25VcmJhVHlwZQogIC0gZmVhdHVyZV9mYW1p
bHk6IFBSRVNDUklQVElPTgogICAgdHlwZV9jb2RlOiAiMDUiCiAgICBzdWJ0eXBlX2NvZGU6ICIw
MCIKICAgIG9mZmljaWFsX2xhYmVsOiBFbXBsYWNlbWVudCByw6lzZXJ2w6kKICAgIGxlZ2FsX3Jl
ZmVyZW5jZTogTDE1MS00MSAxwrAgw6AgM8KwCiAgICByZWd1bGF0aW9uX29yX2FubmV4X3JlZmVy
ZW5jZTogUjE1MS0zNCA0wrAsIFIxNTEtMzggMcKwLCBSMTUxLTQzIDPCsCwgUjE1MS00OCAywrAs
IFIxNTEtNTAgMcKwCiAgICBvZmZpY2lhbF9zb3VyY2VfdXJsOiBodHRwczovL3d3dy5nZW9wb3J0
YWlsLXVyYmFuaXNtZS5nb3V2LmZyL3N0YW5kYXJkL2NuaWdfUExVXzIwMTcvY29kZXMvUHJlc2Ny
aXB0aW9uVXJiYVR5cGUKICAtIGZlYXR1cmVfZmFtaWx5OiBQUkVTQ1JJUFRJT04KICAgIHR5cGVf
Y29kZTogIjA3IgogICAgc3VidHlwZV9jb2RlOiAiMDAiCiAgICBvZmZpY2lhbF9sYWJlbDogUGF0
cmltb2luZSBiw6J0aSwgcGF5c2FnZXIgb3Ugw6lsw6ltZW50cyBkZSBwYXlzYWdlcyDDoCBwcm90
w6lnZXIgcG91ciBkZXMgbW90aWZzIGQnb3JkcmUgY3VsdHVyZWwsIGhpc3RvcmlxdWUsIGFyY2hp
dGVjdHVyYWwgb3Ugw6ljb2xvZ2lxdWUKICAgIGxlZ2FsX3JlZmVyZW5jZTogTDE1MS0xOSBldCBM
MTUxLTIzCiAgICByZWd1bGF0aW9uX29yX2FubmV4X3JlZmVyZW5jZTogUjE1MS00MSAzwrAgRXQg
UjE1MS00MwogICAgb2ZmaWNpYWxfc291cmNlX3VybDogaHR0cHM6Ly93d3cuZ2VvcG9ydGFpbC11
cmJhbmlzbWUuZ291di5mci9zdGFuZGFyZC9jbmlnX1BMVV8yMDE3L2NvZGVzL1ByZXNjcmlwdGlv
blVyYmFUeXBlCiAgLSBmZWF0dXJlX2ZhbWlseTogUFJFU0NSSVBUSU9OCiAgICB0eXBlX2NvZGU6
ICIwNyIKICAgIHN1YnR5cGVfY29kZTogIjA0IgogICAgb2ZmaWNpYWxfbGFiZWw6IMOJbMOpbWVu
dHMgZGUgcGF5c2FnZSwgKHNpdGVzIGV0IHNlY3RldXJzKSDDoCBwcsOpc2VydmVyIHBvdXIgZGVz
IG1vdGlmcyBkJ29yZHJlIMOpY29sb2dpcXVlCiAgICBsZWdhbF9yZWZlcmVuY2U6IEwxNTEtMjMK
ICAgIHJlZ3VsYXRpb25fb3JfYW5uZXhfcmVmZXJlbmNlOiBSMTUxLTQzIDXCsAogICAgb2ZmaWNp
YWxfc291cmNlX3VybDogaHR0cHM6Ly93d3cuZ2VvcG9ydGFpbC11cmJhbmlzbWUuZ291di5mci9z
dGFuZGFyZC9jbmlnX1BMVV8yMDE3L2NvZGVzL1ByZXNjcmlwdGlvblVyYmFUeXBlCiAgLSBmZWF0
dXJlX2ZhbWlseTogUFJFU0NSSVBUSU9OCiAgICB0eXBlX2NvZGU6ICIxNSIKICAgIHN1YnR5cGVf
Y29kZTogIjAwIgogICAgb2ZmaWNpYWxfbGFiZWw6IFLDqGdsZXMgZOKAmWltcGxhbnRhdGlvbiBk
ZXMgY29uc3RydWN0aW9ucwogICAgbGVnYWxfcmVmZXJlbmNlOiBMMTUxLTE3IGV0IEwxNTEtMTgK
ICAgIHJlZ3VsYXRpb25fb3JfYW5uZXhfcmVmZXJlbmNlOiBSMTUxLTM5IGRlcm5pZXIgYWwuCiAg
ICBvZmZpY2lhbF9zb3VyY2VfdXJsOiBodHRwczovL3d3dy5nZW9wb3J0YWlsLXVyYmFuaXNtZS5n
b3V2LmZyL3N0YW5kYXJkL2NuaWdfUExVXzIwMTcvY29kZXMvUHJlc2NyaXB0aW9uVXJiYVR5cGUK
ICAtIGZlYXR1cmVfZmFtaWx5OiBQUkVTQ1JJUFRJT04KICAgIHR5cGVfY29kZTogIjE1IgogICAg
c3VidHlwZV9jb2RlOiAiMDEiCiAgICBvZmZpY2lhbF9sYWJlbDogSW1wbGFudGF0aW9uIGRlcyBj
b25zdHJ1Y3Rpb25zIHBhciByYXBwb3J0IGF1eCB2b2llcyBldCBhdXggZW1wcmlzZXMgcHVibGlx
dWVzCiAgICBsZWdhbF9yZWZlcmVuY2U6IEwxNTEtMTcgZXQgTDE1MS0xOAogICAgcmVndWxhdGlv
bl9vcl9hbm5leF9yZWZlcmVuY2U6IFIxNTEtMzkKICAgIG9mZmljaWFsX3NvdXJjZV91cmw6IGh0
dHBzOi8vd3d3Lmdlb3BvcnRhaWwtdXJiYW5pc21lLmdvdXYuZnIvc3RhbmRhcmQvY25pZ19QTFVf
MjAxNy9jb2Rlcy9QcmVzY3JpcHRpb25VcmJhVHlwZQogIC0gZmVhdHVyZV9mYW1pbHk6IFBSRVND
UklQVElPTgogICAgdHlwZV9jb2RlOiAiMTciCiAgICBzdWJ0eXBlX2NvZGU6ICIwMCIKICAgIG9m
ZmljaWFsX2xhYmVsOiBTZWN0ZXVyIMOgIHByb2dyYW1tZSBkZSBsb2dlbWVudHMgbWl4aXTDqSBz
b2NpYWxlIGVuIHpvbmUgVSBldCBBVQogICAgbGVnYWxfcmVmZXJlbmNlOiBMMTUxLTE1CiAgICBy
ZWd1bGF0aW9uX29yX2FubmV4X3JlZmVyZW5jZTogUjE1MS0zOCAzwrAKICAgIG9mZmljaWFsX3Nv
dXJjZV91cmw6IGh0dHBzOi8vd3d3Lmdlb3BvcnRhaWwtdXJiYW5pc21lLmdvdXYuZnIvc3RhbmRh
cmQvY25pZ19QTFVfMjAxNy9jb2Rlcy9QcmVzY3JpcHRpb25VcmJhVHlwZQogIC0gZmVhdHVyZV9m
YW1pbHk6IFBSRVNDUklQVElPTgogICAgdHlwZV9jb2RlOiAiMTgiCiAgICBzdWJ0eXBlX2NvZGU6
ICIwMCIKICAgIG9mZmljaWFsX2xhYmVsOiBQw6lyaW3DqHRyZSBjb21wb3J0YW50IGRlcyBvcmll
bnRhdGlvbnMgZOKAmWFtw6luYWdlbWVudCBldCBkZSBwcm9ncmFtbWF0aW9uIChPQVApCiAgICBs
ZWdhbF9yZWZlcmVuY2U6IEwxNTEtNiBldCBMMTUxLTcKICAgIHJlZ3VsYXRpb25fb3JfYW5uZXhf
cmVmZXJlbmNlOiBSMTUxLTYgw6AgUjE1MS04LTEKICAgIG9mZmljaWFsX3NvdXJjZV91cmw6IGh0
dHBzOi8vd3d3Lmdlb3BvcnRhaWwtdXJiYW5pc21lLmdvdXYuZnIvc3RhbmRhcmQvY25pZ19QTFVf
MjAxNy9jb2Rlcy9QcmVzY3JpcHRpb25VcmJhVHlwZQo=
```
