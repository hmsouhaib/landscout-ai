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
| `schema_version` | `2` | `int` | annotation `<class 'int'>`; required; Strict(strict=True); required supported schema integer; accepted versions are pinned by the owning Literal/validator | Selects the strict configuration schema; unsupported versions are rejected. | `resolve_planning_feature_codes` |
| `profile` | `"cnig_plu_2017_muret_observed_pairs_v2"` | `str` | annotation `<class 'str'>`; required; MinLen(min_length=1), Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `profile` under the exact parent path `<root>`. | `resolve_planning_feature_codes` |
| `standard_model` | `"CNIG PLU v2017"` | `str` | annotation `Literal['CNIG PLU v2017']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Names the official planning standard/model against which records are validated. | `resolve_planning_feature_codes` |
| `official_text_normalization` | `"GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1"` | `str` | annotation `Literal['GPU_DISPLAY_TEXT_NFC_WHITESPACE_V1']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official text normalization` under the exact parent path `<root>`. | `resolve_planning_feature_codes` |
| `official_sources.prescription` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `prescription` under the exact parent path `official_sources`. | `resolve_planning_feature_codes` |
| `official_sources.information` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `information` under the exact parent path `official_sources`. | `resolve_planning_feature_codes` |
| `retrieval_date` | `"2026-08-12"` | `date` | annotation `<class 'datetime.date'>`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `retrieval date` under the exact parent path `<root>`. | `resolve_planning_feature_codes` |
| `canonical_records_sha256` | `"5990552a681a9e50c072eb207bf88d25c876f61c89eeb88618e74d905487672c"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `canonical_records_sha256`. | `resolve_planning_feature_codes` |
| `records[0].feature_family` | `"INFORMATION"` | `str` | annotation `Literal['PRESCRIPTION', 'INFORMATION']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[0]`. | `resolve_planning_feature_codes` |
| `records[0].type_code` | `"02"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[0]`. | `resolve_planning_feature_codes` |
| `records[0].subtype_code` | `"00"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[0]`. | `resolve_planning_feature_codes` |
| `records[0].official_label` | `"Zone d'aménagement concerté"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[0]`. | `resolve_planning_feature_codes` |
| `records[0].legal_reference` | `"L311-1 code de l’urbanisme"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[0]`. | `resolve_planning_feature_codes` |
| `records[0].regulation_or_annex_reference` | `"R151-52 8°"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[0]`. | `resolve_planning_feature_codes` |
| `records[0].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[1].feature_family` | `"INFORMATION"` | `str` | annotation `Literal['PRESCRIPTION', 'INFORMATION']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[1]`. | `resolve_planning_feature_codes` |
| `records[1].type_code` | `"14"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[1]`. | `resolve_planning_feature_codes` |
| `records[1].subtype_code` | `"00"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[1]`. | `resolve_planning_feature_codes` |
| `records[1].official_label` | `"Périmètre de voisinage d'infrastructure de transport terrestre (secteur affecté par le bruit)"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[1]`. | `resolve_planning_feature_codes` |
| `records[1].legal_reference` | `"L571-10 code de l’environnement"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[1]`. | `resolve_planning_feature_codes` |
| `records[1].regulation_or_annex_reference` | `"R151-53 5°"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[1]`. | `resolve_planning_feature_codes` |
| `records[1].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[2].feature_family` | `"INFORMATION"` | `str` | annotation `Literal['PRESCRIPTION', 'INFORMATION']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[2]`. | `resolve_planning_feature_codes` |
| `records[2].type_code` | `"27"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[2]`. | `resolve_planning_feature_codes` |
| `records[2].subtype_code` | `"00"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[2]`. | `resolve_planning_feature_codes` |
| `records[2].official_label` | `"Plan d'exposition au bruit des aérodromes"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[2]`. | `resolve_planning_feature_codes` |
| `records[2].legal_reference` | `"L112-6 code de l’urbanisme"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[2]`. | `resolve_planning_feature_codes` |
| `records[2].regulation_or_annex_reference` | `"R151-52 2°"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[2]`. | `resolve_planning_feature_codes` |
| `records[2].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[3].feature_family` | `"INFORMATION"` | `str` | annotation `Literal['PRESCRIPTION', 'INFORMATION']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[3]`. | `resolve_planning_feature_codes` |
| `records[3].type_code` | `"99"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[3]`. | `resolve_planning_feature_codes` |
| `records[3].subtype_code` | `"00"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[3]`. | `resolve_planning_feature_codes` |
| `records[3].official_label` | `"Autre périmètre, secteur, plan, document, site, projet, espace."` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[3]`. | `resolve_planning_feature_codes` |
| `records[3].legal_reference` | `null` | `NoneType` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; true YAML null; accepted only where the owning model field is optional/nullable | Configures `legal reference` under the exact parent path `records[3]`. | `resolve_planning_feature_codes` |
| `records[3].regulation_or_annex_reference` | `null` | `NoneType` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; true YAML null; accepted only where the owning model field is optional/nullable | Configures `regulation or annex reference` under the exact parent path `records[3]`. | `resolve_planning_feature_codes` |
| `records[3].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/InformationUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[4].feature_family` | `"PRESCRIPTION"` | `str` | annotation `Literal['PRESCRIPTION', 'INFORMATION']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[4]`. | `resolve_planning_feature_codes` |
| `records[4].type_code` | `"01"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[4]`. | `resolve_planning_feature_codes` |
| `records[4].subtype_code` | `"00"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[4]`. | `resolve_planning_feature_codes` |
| `records[4].official_label` | `"Espace boisé classé"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[4]`. | `resolve_planning_feature_codes` |
| `records[4].legal_reference` | `"L113-1"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[4]`. | `resolve_planning_feature_codes` |
| `records[4].regulation_or_annex_reference` | `"R151-31 1°"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[4]`. | `resolve_planning_feature_codes` |
| `records[4].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[5].feature_family` | `"PRESCRIPTION"` | `str` | annotation `Literal['PRESCRIPTION', 'INFORMATION']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[5]`. | `resolve_planning_feature_codes` |
| `records[5].type_code` | `"05"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[5]`. | `resolve_planning_feature_codes` |
| `records[5].subtype_code` | `"00"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[5]`. | `resolve_planning_feature_codes` |
| `records[5].official_label` | `"Emplacement réservé"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[5]`. | `resolve_planning_feature_codes` |
| `records[5].legal_reference` | `"L151-41 1° à 3°"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[5]`. | `resolve_planning_feature_codes` |
| `records[5].regulation_or_annex_reference` | `"R151-34 4°, R151-38 1°, R151-43 3°, R151-48 2°, R151-50 1°"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[5]`. | `resolve_planning_feature_codes` |
| `records[5].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[6].feature_family` | `"PRESCRIPTION"` | `str` | annotation `Literal['PRESCRIPTION', 'INFORMATION']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[6]`. | `resolve_planning_feature_codes` |
| `records[6].type_code` | `"07"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[6]`. | `resolve_planning_feature_codes` |
| `records[6].subtype_code` | `"00"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[6]`. | `resolve_planning_feature_codes` |
| `records[6].official_label` | `"Patrimoine bâti, paysager ou éléments de paysages à protéger pour des motifs d'ordre culturel, historique, architectural ou écologique"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[6]`. | `resolve_planning_feature_codes` |
| `records[6].legal_reference` | `"L151-19 et L151-23"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[6]`. | `resolve_planning_feature_codes` |
| `records[6].regulation_or_annex_reference` | `"R151-41 3° Et R151-43"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[6]`. | `resolve_planning_feature_codes` |
| `records[6].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[7].feature_family` | `"PRESCRIPTION"` | `str` | annotation `Literal['PRESCRIPTION', 'INFORMATION']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[7]`. | `resolve_planning_feature_codes` |
| `records[7].type_code` | `"07"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[7]`. | `resolve_planning_feature_codes` |
| `records[7].subtype_code` | `"04"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[7]`. | `resolve_planning_feature_codes` |
| `records[7].official_label` | `"Éléments de paysage, (sites et secteurs) à préserver pour des motifs d'ordre écologique"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[7]`. | `resolve_planning_feature_codes` |
| `records[7].legal_reference` | `"L151-23"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[7]`. | `resolve_planning_feature_codes` |
| `records[7].regulation_or_annex_reference` | `"R151-43 5°"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[7]`. | `resolve_planning_feature_codes` |
| `records[7].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[8].feature_family` | `"PRESCRIPTION"` | `str` | annotation `Literal['PRESCRIPTION', 'INFORMATION']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[8]`. | `resolve_planning_feature_codes` |
| `records[8].type_code` | `"15"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[8]`. | `resolve_planning_feature_codes` |
| `records[8].subtype_code` | `"00"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[8]`. | `resolve_planning_feature_codes` |
| `records[8].official_label` | `"Règles d’implantation des constructions"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[8]`. | `resolve_planning_feature_codes` |
| `records[8].legal_reference` | `"L151-17 et L151-18"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[8]`. | `resolve_planning_feature_codes` |
| `records[8].regulation_or_annex_reference` | `"R151-39 dernier al."` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[8]`. | `resolve_planning_feature_codes` |
| `records[8].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[9].feature_family` | `"PRESCRIPTION"` | `str` | annotation `Literal['PRESCRIPTION', 'INFORMATION']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[9]`. | `resolve_planning_feature_codes` |
| `records[9].type_code` | `"15"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[9]`. | `resolve_planning_feature_codes` |
| `records[9].subtype_code` | `"01"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[9]`. | `resolve_planning_feature_codes` |
| `records[9].official_label` | `"Implantation des constructions par rapport aux voies et aux emprises publiques"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[9]`. | `resolve_planning_feature_codes` |
| `records[9].legal_reference` | `"L151-17 et L151-18"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[9]`. | `resolve_planning_feature_codes` |
| `records[9].regulation_or_annex_reference` | `"R151-39"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[9]`. | `resolve_planning_feature_codes` |
| `records[9].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[10].feature_family` | `"PRESCRIPTION"` | `str` | annotation `Literal['PRESCRIPTION', 'INFORMATION']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[10]`. | `resolve_planning_feature_codes` |
| `records[10].type_code` | `"17"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[10]`. | `resolve_planning_feature_codes` |
| `records[10].subtype_code` | `"00"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[10]`. | `resolve_planning_feature_codes` |
| `records[10].official_label` | `"Secteur à programme de logements mixité sociale en zone U et AU"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[10]`. | `resolve_planning_feature_codes` |
| `records[10].legal_reference` | `"L151-15"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[10]`. | `resolve_planning_feature_codes` |
| `records[10].regulation_or_annex_reference` | `"R151-38 3°"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[10]`. | `resolve_planning_feature_codes` |
| `records[10].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |
| `records[11].feature_family` | `"PRESCRIPTION"` | `str` | annotation `Literal['PRESCRIPTION', 'INFORMATION']`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `feature family` under the exact parent path `records[11]`. | `resolve_planning_feature_codes` |
| `records[11].type_code` | `"18"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `type code` under the exact parent path `records[11]`. | `resolve_planning_feature_codes` |
| `records[11].subtype_code` | `"00"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `subtype code` under the exact parent path `records[11]`. | `resolve_planning_feature_codes` |
| `records[11].official_label` | `"Périmètre comportant des orientations d’aménagement et de programmation (OAP)"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `official label` under the exact parent path `records[11]`. | `resolve_planning_feature_codes` |
| `records[11].legal_reference` | `"L151-6 et L151-7"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `legal reference` under the exact parent path `records[11]`. | `resolve_planning_feature_codes` |
| `records[11].regulation_or_annex_reference` | `"R151-6 à R151-8-1"` | `str` | annotation `Optional[Annotated[str, Strict(strict=True)]]`; required; no inline Field metadata; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `regulation or annex reference` under the exact parent path `records[11]`. | `resolve_planning_feature_codes` |
| `records[11].official_source_url` | `"https://www.geoportail-urbanisme.gouv.fr/standard/cnig_PLU_2017/codes/PrescriptionUrbaType"` | `str` | annotation `<class 'str'>`; required; Strict(strict=True); required URL under the owning model's exact HTTPS/origin/path/credential/query/fragment validator | Configures the exact official source url; HTTPS/origin/path validation is defined by the consuming model. | `resolve_planning_feature_codes` |

## 5. Classes / models / dataclasses

Authoritative owning model: `landscout.stages.resolve_planning_feature_codes.CnigFeatureCodeProfile`. The checked-in file currently validates as `CnigFeatureCodeProfile`.

```python
class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

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

Loader: `landscout.stages.resolve_planning_feature_codes.load_cnig_feature_code_profile`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, byte hashing, and cross-field validation.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `resolve_planning_feature_codes`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

## 9. Error handling

The owning Pydantic model rejects extra/missing/unsupported/coerced values according to the exact model/validators above; the loader translates YAML/path/model failures into its documented controlled error.

## 10. Side effects

Network I/O: none. Filesystem read: the loader reads this YAML. Filesystem write: none. Input mutation: none. GIS calculation: none. Hashing: loaders that expose config identity hash these exact bytes.

## 11. Security / trust boundaries

A configured URL/provider/hash is a source lock or provenance input. Physical authority requires the consuming source adapter's safe transport and byte/source revalidation.

## 12. GIS / CRS rules

Only explicit CRS fields impose GIS rules; configured storage/calculation CRS values are policy/configuration, not an implicit reprojection of data.

## 13. Provenance rules

The file's SHA256 binds this exact policy/configuration snapshot. Source identities remain textual until the adapter validates physical bytes/content.

## 14. Business meaning

Thresholds and outcomes are policy/configuration values. They are never relabeled as measured geometry or legal conclusions.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

The loader/model companion and relevant test companion document exact valid/invalid values, cross-field failures, consumer loading, and byte-hash behavior.

## 17. Change impact

Any YAML byte/value change requires policy/source review, affected config/result hashes, consumer tests, generated artifacts where applicable, and this companion SHA update.
