# `configs/planning/muret_plu_structure.yaml`

## File identity

- Repository path: `configs/planning/muret_plu_structure.yaml`
- File type: YAML checked-in configuration/policy/source lock
- Responsibility: Defines deterministic Muret regulation layout, heading grammar, zone aliases, and topic-evidence terms.
- Source SHA256: `74bf407441b66cde62efda581fbbb7df0d27b9d2148b210b7749ddf61b1b763a`

## 1. Purpose

Defines deterministic Muret regulation layout, heading grammar, zone aliases, and topic-evidence terms.

## 2. Position in LandScout architecture

The exact YAML bytes are parsed by `landscout.stages.structure_planning_regulation.load_planning_regulation_structure_config` into `landscout.stages.structure_planning_regulation.PlanningRegulationStructureConfig`. Runtime consumers include `structure_planning_regulation`.

## 3. Imports and dependencies

Not applicable to YAML. Python/Pydantic consumers are named above and reproduced below.

## 4. Contract taxonomy

Every row below is a configuration field/list leaf. It is not a DataFrame column unless a consuming stage explicitly copies it into a documented result schema.

| Exact YAML path | Checked-in value | Runtime type | Required/nullability/allowed-domain/unit contract | Semantic role | Consumers |
|---|---|---|---|---|---|
| `schema_version` | `2` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required supported schema integer; accepted versions are pinned by the owning Literal/validator | Selects the strict configuration schema; unsupported versions are rejected. | `structure_planning_regulation` |
| `structure_profile` | `"muret_plu_20240215_v1"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `structure profile` under the exact parent path `<root>`. | `structure_planning_regulation` |
| `document_lock.document_id` | `"33edb4c9f6943c88d8d92518bff20bec"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `document id` under the exact parent path `document_lock`. | `structure_planning_regulation` |
| `document_lock.pdf_sha256` | `"5358ebad6b0cda6de681ba3536e29b8b6291fb701c7d3711f4ee1d6fdb85c6fb"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `pdf_sha256`. | `structure_planning_regulation` |
| `document_lock.pages_content_sha256` | `"928e7e59c45e27c38e39d3f28f3eb10bd2590886416df57efc4ac8e5d8901ec9"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `pages_content_sha256`. | `structure_planning_regulation` |
| `document_lock.index_content_sha256` | `"6a0009228ca17128c0a8bb329d9c2277a1b6638708a67b913b72ee93063e42cd"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; canonical lowercase SHA256 where the owning model uses CanonicalSha256; required/nullability follows the exact model field | Binds the exact bytes or canonical component named by `index_content_sha256`. | `structure_planning_regulation` |
| `document_lock.normalization_profile` | `"fr_literal_v1"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `normalization profile` under the exact parent path `document_lock`. | `structure_planning_regulation` |
| `document_layout.body_start_page` | `1` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `body start page` under the exact parent path `document_layout`. | `structure_planning_regulation` |
| `document_layout.max_heading_continuation_lines` | `2` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `max heading continuation lines` under the exact parent path `document_layout`. | `structure_planning_regulation` |
| `document_layout.include_table_of_contents_in_topic_evidence` | `false` | `bool` | source-declared default is `False`; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; required Boolean at this checked-in path unless the exact model declares a default/optional field | Enables/disables the exact include table of contents in topic evidence behavior; Boolean coercion rules belong to the consuming model. | `structure_planning_regulation` |
| `heading_patterns.zone_chapter[0]` | `"^ZONE\\s+(?P<label>[A-Za-z]+(?:\\s*0)?)\\s*$"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `heading_patterns.zone_chapter`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `heading_patterns.article[0]` | `"^ARTICLE\\s+(?P<zone>[A-Za-z]+(?:\\s*0)?)\\s+(?P<number>\\d+(?:\\.\\d+)?)\\s*[-–—]\\s*(?P<title>.*)$"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `heading_patterns.article`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `heading_patterns.general_section[0]` | `"^ARTICLE\\s+(?P<number>\\d+(?:\\.\\d+)?)\\s*[-–—]\\s*(?P<title>.*)$"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `heading_patterns.general_section`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `heading_patterns.continuation[0]` | `"^[^a-z]*[A-ZÀ-ÖØ-ÞŒ][^a-z]*$"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `heading_patterns.continuation`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `ignored_patterns.page_headers[0]` | `"^Muret-12ème modification du PLU$"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `ignored_patterns.page_headers`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `ignored_patterns.page_headers[1]` | `"^\\d+$"` | `str` | default/default-factory is reproduced in the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `ignored_patterns.page_headers`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `zone_aliases.UAa` | `"UA"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `UAa` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.UAb` | `"UA"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `UAb` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.UBa` | `"UB"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `UBa` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.UBb` | `"UB"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `UBb` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.UFa` | `"UF"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `UFa` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.UFc` | `"UF"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `UFc` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.UFd` | `"UF"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `UFd` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.AUa` | `"AU"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `AUa` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.AUfa` | `"AUf"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `AUfa` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.AUfb` | `"AUf"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `AUfb` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.AUfc` | `"AUf"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `AUfc` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.AUfd` | `"AUf"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `AUfd` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.AUfo` | `"AUf0"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `AUfo` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.NL` | `"N"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `NL` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.Ne` | `"N"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `Ne` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.Nh` | `"N"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `Nh` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `zone_aliases.Nr` | `"N"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `Nr` under the exact parent path `zone_aliases`. | `structure_planning_regulation` |
| `topics.destination_and_use[0]` | `"occupation du sol"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.destination_and_use`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.destination_and_use[1]` | `"utilisation du sol"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.destination_and_use`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.destination_and_use[2]` | `"destination"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.destination_and_use`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.public_interest_equipment[0]` | `"équipement public"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.public_interest_equipment`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.public_interest_equipment[1]` | `"équipement d'intérêt collectif"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.public_interest_equipment`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.public_interest_equipment[2]` | `"service public"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.public_interest_equipment`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.public_interest_equipment[3]` | `"intérêt collectif"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.public_interest_equipment`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.technical_equipment[0]` | `"ouvrage technique"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.technical_equipment`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.technical_equipment[1]` | `"installations techniques"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.technical_equipment`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.technical_equipment[2]` | `"locaux techniques"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.technical_equipment`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.energy[0]` | `"énergie"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.energy`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.electricity[0]` | `"électricité"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.electricity`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.electricity[1]` | `"électrique"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.electricity`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.transformer[0]` | `"transformateur"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.transformer`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.classified_installation[0]` | `"installation classée"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.classified_installation`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.classified_installation[1]` | `"installations classées"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.classified_installation`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.classified_installation[2]` | `"ICPE"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.classified_installation`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.risk[0]` | `"risque"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.risk`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.risk[1]` | `"risques"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.risk`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.nuisance[0]` | `"nuisance"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.nuisance`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.nuisance[1]` | `"nuisances"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.nuisance`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.fire_safety[0]` | `"incendie"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.fire_safety`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.fire_safety[1]` | `"défense contre l'incendie"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.fire_safety`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.access[0]` | `"accès"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.access`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.access[1]` | `"desserte"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.access`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.setbacks[0]` | `"recul"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.setbacks`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.setbacks[1]` | `"distance minimale"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.setbacks`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.setbacks[2]` | `"implantation"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.setbacks`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.networks[0]` | `"réseau"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.networks`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topics.networks[1]` | `"réseaux"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Ordered configured member of `topics.networks`; order and uniqueness are validated/consumed where required. | `structure_planning_regulation` |
| `topic_match_policy.boundary_mode` | `"token"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `boundary mode` under the exact parent path `topic_match_policy`. | `structure_planning_regulation` |
| `topic_match_policy.overlap_resolution` | `"longest_match"` | `str` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; exact string/list member required by the owning model, Literal, uniqueness, or cross-field validator shown below | Configures `overlap resolution` under the exact parent path `topic_match_policy`. | `structure_planning_regulation` |
| `topic_context_characters` | `80` | `int` | required by the owning source declaration; Annotated/Field/StringConstraints metadata and validators are reproduced as deterministic source below; integer value; strictness/bounds are those shown in the owning model and validators reproduced below | Configures `topic context characters` under the exact parent path `<root>`. | `structure_planning_regulation` |

## STEP 7F.1A.4 dependent-model refresh

- The YAML bytes and checked-in values are unchanged. STEP 7F.1A.4 changes their owning validation/authority boundary through `landscout.stages.structure_planning_regulation.load_planning_regulation_structure_config`; section 5 now embeds the exact current owning model sources and qualified consumers.
- Decision-input models are frozen/deeply immutable where their current source declares that contract; trust-bearing YAML is decoded through the shared duplicate-rejecting loader where the owning loader source shows that call.
- No configured policy meaning, source identity, threshold, artifact schema, or output schema is changed by this dependent documentation refresh.

## 5. Classes / models / dataclasses

- Exact checked-in configuration SHA256 remains `74bf407441b66cde62efda581fbbb7df0d27b9d2148b210b7749ddf61b1b763a`; its values are unchanged by STEP 7F.1A.4.
- Authoritative loader/config boundary: `landscout.stages.structure_planning_regulation.load_planning_regulation_structure_config`.
- Owning Python module: `landscout.stages.structure_planning_regulation`.
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

### `DocumentLockConfig`

**Source purpose:** Defines `DocumentLockConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `document_id` | `StrictStr` | `Field(min_length=1)` | `document_id: StrictStr = Field(min_length=1)` |
| `pdf_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `pages_content_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `pages_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `index_content_sha256` | `StrictStr` | `Field(pattern=r"^[0-9a-f]{64}$")` | `index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")` |
| `normalization_profile` | `StrictStr` | `Field(min_length=1)` | `normalization_profile: StrictStr = Field(min_length=1)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class DocumentLockConfig(_StrictConfigModel):
    document_id: StrictStr = Field(min_length=1)
    pdf_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    pages_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    index_content_sha256: StrictStr = Field(pattern=r"^[0-9a-f]{64}$")
    normalization_profile: StrictStr = Field(min_length=1)
```

### `DocumentLayoutConfig`

**Source purpose:** Defines `DocumentLayoutConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `body_start_page` | `StrictInt` | `Field(ge=1)` | `body_start_page: StrictInt = Field(ge=1)` |
| `table_of_contents_pages` | `tuple[StrictInt, ...]` | `()` | `table_of_contents_pages: tuple[StrictInt, ...] = ()` |
| `max_heading_continuation_lines` | `StrictInt` | `Field(ge=0, le=10)` | `max_heading_continuation_lines: StrictInt = Field(ge=0, le=10)` |
| `include_table_of_contents_in_topic_evidence` | `StrictBool` | `False` | `include_table_of_contents_in_topic_evidence: StrictBool = False` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- value/type reference: `landscout.stages.structure_planning_regulation::DocumentLayoutConfig._validate_pages` via `DocumentLayoutConfig`

**Exact class source**

```python
class DocumentLayoutConfig(_StrictConfigModel):
    body_start_page: StrictInt = Field(ge=1)
    table_of_contents_pages: tuple[StrictInt, ...] = ()
    max_heading_continuation_lines: StrictInt = Field(ge=0, le=10)
    include_table_of_contents_in_topic_evidence: StrictBool = False

    @model_validator(mode="after")
    def _validate_pages(self) -> DocumentLayoutConfig:
        pages = self.table_of_contents_pages
        if any(page < 1 for page in pages) or tuple(sorted(set(pages))) != pages:
            raise ValueError(
                "table_of_contents_pages must contain unique ascending positive integers"
            )
        return self
```

### `HeadingPatternsConfig`

**Source purpose:** Defines `HeadingPatternsConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `zone_chapter` | `tuple[StrictStr, ...]` | `Field(min_length=1)` | `zone_chapter: tuple[StrictStr, ...] = Field(min_length=1)` |
| `article` | `tuple[StrictStr, ...]` | `Field(min_length=1)` | `article: tuple[StrictStr, ...] = Field(min_length=1)` |
| `general_section` | `tuple[StrictStr, ...]` | `Field(min_length=1)` | `general_section: tuple[StrictStr, ...] = Field(min_length=1)` |
| `continuation` | `tuple[StrictStr, ...]` | `()` | `continuation: tuple[StrictStr, ...] = ()` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class HeadingPatternsConfig(_StrictConfigModel):
    zone_chapter: tuple[StrictStr, ...] = Field(min_length=1)
    article: tuple[StrictStr, ...] = Field(min_length=1)
    general_section: tuple[StrictStr, ...] = Field(min_length=1)
    continuation: tuple[StrictStr, ...] = ()
```

### `IgnoredPatternsConfig`

**Source purpose:** Defines `IgnoredPatternsConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `page_headers` | `tuple[StrictStr, ...]` | `()` | `page_headers: tuple[StrictStr, ...] = ()` |
| `page_footers` | `tuple[StrictStr, ...]` | `()` | `page_footers: tuple[StrictStr, ...] = ()` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class IgnoredPatternsConfig(_StrictConfigModel):
    page_headers: tuple[StrictStr, ...] = ()
    page_footers: tuple[StrictStr, ...] = ()
```

### `TopicMatchPolicyConfig`

**Source purpose:** Defines `TopicMatchPolicyConfig`; its exact fields, decorators, bases, methods, and complete source below are authoritative.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `boundary_mode` | `Literal['token']` | `required` | `boundary_mode: Literal["token"]` |
| `overlap_resolution` | `Literal['longest_match']` | `required` | `overlap_resolution: Literal["longest_match"]` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- No conservative direct repository consumer was found.

**Exact class source**

```python
class TopicMatchPolicyConfig(_StrictConfigModel):
    boundary_mode: Literal["token"]
    overlap_resolution: Literal["longest_match"]

    @property
    def identifier(self) -> str:
        return f"{self.boundary_mode}_{self.overlap_resolution}"
```

### `PlanningRegulationStructureConfig`

**Source purpose:** Strict, document-locked grammar for one factual regulation structure.

- Exact decorators: none.
- Exact bases: `_StrictConfigModel`.

**Fields and model attributes**

| Field | Annotation/kind | Default or assignment | Exact declaration |
|---|---|---|---|
| `schema_version` | `StrictInt` | `required` | `schema_version: StrictInt` |
| `structure_profile` | `StrictStr` | `Field(min_length=1)` | `structure_profile: StrictStr = Field(min_length=1)` |
| `document_lock` | `DocumentLockConfig` | `required` | `document_lock: DocumentLockConfig` |
| `document_layout` | `DocumentLayoutConfig` | `required` | `document_layout: DocumentLayoutConfig` |
| `heading_patterns` | `HeadingPatternsConfig` | `required` | `heading_patterns: HeadingPatternsConfig` |
| `ignored_patterns` | `IgnoredPatternsConfig` | `required` | `ignored_patterns: IgnoredPatternsConfig` |
| `zone_aliases` | `dict[StrictStr, StrictStr]` | `required` | `zone_aliases: dict[StrictStr, StrictStr]` |
| `topics` | `dict[StrictStr, tuple[StrictStr, ...]]` | `required` | `topics: dict[StrictStr, tuple[StrictStr, ...]]` |
| `topic_match_policy` | `TopicMatchPolicyConfig` | `required` | `topic_match_policy: TopicMatchPolicyConfig` |
| `topic_context_characters` | `StrictInt` | `Field(ge=0)` | `topic_context_characters: StrictInt = Field(ge=0)` |

Field meaning is owned by this class, its exact annotation/default, validators/methods, and qualified consumers; no field is promoted to a frame column or business conclusion merely from its name.

**Qualified consumers**

- public re-export: `landscout.stages::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    load_planning_regulation_structure_config,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`
- import: `landscout.stages.interpret_bess_zoning::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    PlanningRegulationStructureResult,
    validate_planning_regulation_structure_with_fragments,
)`
- value/type reference: `landscout.stages.interpret_bess_zoning::_build_result` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::validate_bess_zoning_precheck` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.interpret_bess_zoning::interpret_bess_zoning` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::PlanningRegulationStructureConfig._validate_grammar` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::load_planning_regulation_structure_config` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_config_sha256` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_document_lock` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_line_records` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_heading_events` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_section_starts` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_sections` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_zone_mapping` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_topic_evidence` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_sections` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_zone_mapping` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_topic_evidence` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_build_structure_result` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_validate_result_self` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::_resolved_config` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure_with_fragments` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::validate_planning_regulation_structure` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::planning_regulation_section_page_fragments` via `PlanningRegulationStructureConfig`
- value/type reference: `landscout.stages.structure_planning_regulation::structure_planning_regulation` via `PlanningRegulationStructureConfig`
- import: `tests.integration.test_gpu_planning_end_to_end::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureResult,
    structure_planning_regulation,
)`
- value/type reference: `tests.integration.test_gpu_planning_end_to_end::_structure_config` via `PlanningRegulationStructureConfig`
- import: `tests.unit.test_interpret_bess_zoning::<module>` via `from landscout.stages.structure_planning_regulation import (
    PlanningRegulationStructureConfig,
    planning_regulation_section_page_fragments,
    structure_planning_regulation,
)`
- value/type reference: `tests.unit.test_interpret_bess_zoning::_structure_config` via `PlanningRegulationStructureConfig`
- import: `tests.unit.test_structure_planning_regulation::<module>` via `from landscout.stages.structure_planning_regulation import (
    SECTION_HASH_SCHEMA_VERSION,
    STRUCTURE_MANIFEST_SCHEMA_VERSION,
    PlanningRegulationStructureConfig,
    PlanningRegulationStructureError,
    _heading_events,
    _line_records,
    _literal_topic_matches,
    _result_with_hashes,
    _section_content_sha256,
    load_planning_regulation_structure_config,
    structure_planning_regulation,
    validate_planning_regulation_structure,
    validate_planning_regulation_structure_with_fragments,
)`
- value/type reference: `tests.unit.test_structure_planning_regulation::_config` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_old_and_unknown_config_schema_versions_are_rejected` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_topic_evidence_flag_rejects_boolean_coercion` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_topic_evidence_flag_accepts_exact_booleans` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_evidence_scope_is_derived_from_exact_section_type` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_reversed_topic_mapping_keys_do_not_change_output_or_hashes` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_equal_length_overlap_uses_configured_term_order_as_tie_break` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_only_prefix_is_preserved_in_first_actual_section` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_toc_blocks_anywhere_are_other_and_toggle_topic_evidence` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_blank_gap_after_toc_is_preserved_without_a_blank_other_section` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::_structure_with_document_layout` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_heading_patterns_require_mandatory_named_captures` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_optional_pattern_lists_may_be_empty` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::_config_with_structural_patterns` via `PlanningRegulationStructureConfig`
- value/type reference: `tests.unit.test_structure_planning_regulation::test_identical_structural_regex_across_groups_is_rejected_by_config` via `PlanningRegulationStructureConfig`

**Exact class source**

```python
class PlanningRegulationStructureConfig(_StrictConfigModel):
    """Strict, document-locked grammar for one factual regulation structure."""

    schema_version: StrictInt
    structure_profile: StrictStr = Field(min_length=1)
    document_lock: DocumentLockConfig
    document_layout: DocumentLayoutConfig
    heading_patterns: HeadingPatternsConfig
    ignored_patterns: IgnoredPatternsConfig
    zone_aliases: dict[StrictStr, StrictStr]
    topics: dict[StrictStr, tuple[StrictStr, ...]]
    topic_match_policy: TopicMatchPolicyConfig
    topic_context_characters: StrictInt = Field(ge=0)

    @model_validator(mode="after")
    def _validate_grammar(self) -> PlanningRegulationStructureConfig:
        if self.schema_version != _SUPPORTED_CONFIG_SCHEMA_VERSION:
            raise ValueError(
                f"unsupported structure config schema: {self.schema_version}"
            )
        _exact_config_string(self.structure_profile, "structure_profile")
        _exact_config_string(self.document_lock.document_id, "document_id")
        _exact_config_string(
            self.document_lock.normalization_profile,
            "normalization_profile",
        )
        pattern_groups = (
            self.heading_patterns.zone_chapter,
            self.heading_patterns.article,
            self.heading_patterns.general_section,
            self.heading_patterns.continuation,
            self.ignored_patterns.page_headers,
            self.ignored_patterns.page_footers,
        )
        for patterns in pattern_groups:
            if len(set(patterns)) != len(patterns):
                raise ValueError("regular-expression patterns must be unique")
            for pattern in patterns:
                _exact_config_string(pattern, "regular-expression pattern")
                try:
                    re.compile(pattern)
                except re.error as error:
                    raise ValueError(
                        f"invalid regular expression: {pattern}"
                    ) from error
        structural_pattern_owners: dict[str, str] = {}
        for category, patterns in (
            ("ZONE_CHAPTER", self.heading_patterns.zone_chapter),
            ("GENERAL", self.heading_patterns.general_section),
            ("ARTICLE", self.heading_patterns.article),
        ):
            for pattern in patterns:
                previous = structural_pattern_owners.get(pattern)
                if previous is not None:
                    raise ValueError(
                        "identical structural heading regex is reused across "
                        f"groups {previous} and {category}"
                    )
                structural_pattern_owners[pattern] = category
        required_captures = (
            (self.heading_patterns.zone_chapter, {"label"}, "zone chapter"),
            (
                self.heading_patterns.article,
                {"zone", "number", "title"},
                "zone article",
            ),
            (
                self.heading_patterns.general_section,
                {"number", "title"},
                "general section",
            ),
        )
        for patterns, required, label in required_captures:
            for pattern in patterns:
                missing = required.difference(re.compile(pattern).groupindex)
                if missing:
                    raise ValueError(
                        f"{label} pattern lacks named captures: {sorted(missing)}"
                    )
        for alias, target in self.zone_aliases.items():
            _exact_config_string(alias, "zone alias")
            _exact_config_string(target, "zone alias target")
        _validate_alias_cycles(self.zone_aliases)
        if not self.topics:
            raise ValueError("topics must not be empty")
        for topic in sorted(self.topics):
            terms = self.topics[topic]
            _exact_config_string(topic, "topic")
            if not terms:
                raise ValueError(f"topic {topic!r} must contain literal terms")
            normalized: set[str] = set()
            for term in terms:
                _exact_config_string(term, "topic search term")
                normalized_term = _normalize_search_text(term)
                if not normalized_term or normalized_term in normalized:
                    raise ValueError(
                        f"topic {topic!r} contains duplicate normalized terms"
                    )
                normalized.add(normalized_term)
        object.__setattr__(self, "zone_aliases", freeze_mapping(self.zone_aliases))
        object.__setattr__(self, "topics", freeze_mapping(self.topics))
        return self
```

## 6. Functions and methods

Loader: `landscout.stages.structure_planning_regulation.load_planning_regulation_structure_config`. Its source-module companion documents path resolution, YAML parsing, controlled exceptions, exact validation, and any hashing actually performed by that loader.

## 7. Data contracts

This file supplies configuration/policy/source identity. It does not itself create a frame. Any fields copied into output rows are documented by the consuming stage's canonical frame schema.

## 8. Interfaces

Runtime consumers: `structure_planning_regulation`. Dynamic path construction is included: the road policy loader resolves its default access-policy path, and scan loading resolves `ProfileReference.path` to the BESS profile file.

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

### Authoritative raw-byte payload

- Raw byte length: `2287`.
- Raw SHA256: `74bf407441b66cde62efda581fbbb7df0d27b9d2148b210b7749ddf61b1b763a` (identical to **File identity**).
- Encoding: RFC 4648 Base64, wrapped for display only. Decoding the concatenated payload reproduces every original byte, including mixed CRLF/LF positions.

```text
c2NoZW1hX3ZlcnNpb246IDIKc3RydWN0dXJlX3Byb2ZpbGU6ICJtdXJldF9wbHVfMjAyNDAyMTVf
djEiCgpkb2N1bWVudF9sb2NrOgogIGRvY3VtZW50X2lkOiAiMzNlZGI0YzlmNjk0M2M4OGQ4ZDky
NTE4YmZmMjBiZWMiCiAgcGRmX3NoYTI1NjogIjUzNThlYmFkNmIwY2RhNmRlNjgxYmEzNTM2ZTI5
YjhiNjI5MWZiNzAxYzdkMzcxMWY0ZWUxZDZmZGI4NWM2ZmIiCiAgcGFnZXNfY29udGVudF9zaGEy
NTY6ICI5MjhlN2U1OWM0NWUyN2MzOGUzOWQzZjI4ZjNlYjEwYmQyNTkwODg2NDE2ZGY1N2VmYzRh
YzhlNWQ4OTAxZWM5IgogIGluZGV4X2NvbnRlbnRfc2hhMjU2OiAiNmEwMDA5MjI4Y2ExNzEyOGMw
YThiYjMyOWQ5YzIyNzdhMWI2NjM4NzA4YTY3YjkxM2I3MmVlOTMwNjNlNDJjZCIKICBub3JtYWxp
emF0aW9uX3Byb2ZpbGU6ICJmcl9saXRlcmFsX3YxIgoKZG9jdW1lbnRfbGF5b3V0OgogIGJvZHlf
c3RhcnRfcGFnZTogMQogIHRhYmxlX29mX2NvbnRlbnRzX3BhZ2VzOiBbXQogIG1heF9oZWFkaW5n
X2NvbnRpbnVhdGlvbl9saW5lczogMgogIGluY2x1ZGVfdGFibGVfb2ZfY29udGVudHNfaW5fdG9w
aWNfZXZpZGVuY2U6IGZhbHNlCgpoZWFkaW5nX3BhdHRlcm5zOgogIHpvbmVfY2hhcHRlcjoKICAg
IC0gJ15aT05FXHMrKD9QPGxhYmVsPltBLVphLXpdKyg/OlxzKjApPylccyokJwogIGFydGljbGU6
CiAgICAtICdeQVJUSUNMRVxzKyg/UDx6b25lPltBLVphLXpdKyg/OlxzKjApPylccysoP1A8bnVt
YmVyPlxkKyg/OlwuXGQrKT8pXHMqWy3igJPigJRdXHMqKD9QPHRpdGxlPi4qKSQnCiAgZ2VuZXJh
bF9zZWN0aW9uOgogICAgLSAnXkFSVElDTEVccysoP1A8bnVtYmVyPlxkKyg/OlwuXGQrKT8pXHMq
Wy3igJPigJRdXHMqKD9QPHRpdGxlPi4qKSQnCiAgY29udGludWF0aW9uOgogICAgLSAnXlteYS16
XSpbQS1aw4Atw5bDmC3DnsWSXVteYS16XSokJwoKaWdub3JlZF9wYXR0ZXJuczoKICBwYWdlX2hl
YWRlcnM6CiAgICAtICdeTXVyZXQtMTLDqG1lIG1vZGlmaWNhdGlvbiBkdSBQTFUkJwogICAgLSAn
XlxkKyQnCiAgcGFnZV9mb290ZXJzOiBbXQoKem9uZV9hbGlhc2VzOgogIFVBYTogIlVBIgogIFVB
YjogIlVBIgogIFVCYTogIlVCIgogIFVCYjogIlVCIgogIFVGYTogIlVGIgogIFVGYzogIlVGIgog
IFVGZDogIlVGIgogIEFVYTogIkFVIgogIEFVZmE6ICJBVWYiCiAgQVVmYjogIkFVZiIKICBBVWZj
OiAiQVVmIgogIEFVZmQ6ICJBVWYiCiAgQVVmbzogIkFVZjAiCiAgTkw6ICJOIgogIE5lOiAiTiIK
ICBOaDogIk4iCiAgTnI6ICJOIgoKdG9waWNzOgogIGRlc3RpbmF0aW9uX2FuZF91c2U6CiAgICAt
ICJvY2N1cGF0aW9uIGR1IHNvbCIKICAgIC0gInV0aWxpc2F0aW9uIGR1IHNvbCIKICAgIC0gImRl
c3RpbmF0aW9uIgogIHB1YmxpY19pbnRlcmVzdF9lcXVpcG1lbnQ6CiAgICAtICLDqXF1aXBlbWVu
dCBwdWJsaWMiCiAgICAtICLDqXF1aXBlbWVudCBkJ2ludMOpcsOqdCBjb2xsZWN0aWYiCiAgICAt
ICJzZXJ2aWNlIHB1YmxpYyIKICAgIC0gImludMOpcsOqdCBjb2xsZWN0aWYiCiAgdGVjaG5pY2Fs
X2VxdWlwbWVudDoKICAgIC0gIm91dnJhZ2UgdGVjaG5pcXVlIgogICAgLSAiaW5zdGFsbGF0aW9u
cyB0ZWNobmlxdWVzIgogICAgLSAibG9jYXV4IHRlY2huaXF1ZXMiCiAgZW5lcmd5OgogICAgLSAi
w6luZXJnaWUiCiAgZWxlY3RyaWNpdHk6CiAgICAtICLDqWxlY3RyaWNpdMOpIgogICAgLSAiw6ls
ZWN0cmlxdWUiCiAgdHJhbnNmb3JtZXI6CiAgICAtICJ0cmFuc2Zvcm1hdGV1ciIKICBjbGFzc2lm
aWVkX2luc3RhbGxhdGlvbjoKICAgIC0gImluc3RhbGxhdGlvbiBjbGFzc8OpZSIKICAgIC0gImlu
c3RhbGxhdGlvbnMgY2xhc3PDqWVzIgogICAgLSAiSUNQRSIKICByaXNrOgogICAgLSAicmlzcXVl
IgogICAgLSAicmlzcXVlcyIKICBudWlzYW5jZToKICAgIC0gIm51aXNhbmNlIgogICAgLSAibnVp
c2FuY2VzIgogIGZpcmVfc2FmZXR5OgogICAgLSAiaW5jZW5kaWUiCiAgICAtICJkw6lmZW5zZSBj
b250cmUgbCdpbmNlbmRpZSIKICBhY2Nlc3M6CiAgICAtICJhY2PDqHMiCiAgICAtICJkZXNzZXJ0
ZSIKICBzZXRiYWNrczoKICAgIC0gInJlY3VsIgogICAgLSAiZGlzdGFuY2UgbWluaW1hbGUiCiAg
ICAtICJpbXBsYW50YXRpb24iCiAgbmV0d29ya3M6CiAgICAtICJyw6lzZWF1IgogICAgLSAicsOp
c2VhdXgiCgp0b3BpY19tYXRjaF9wb2xpY3k6CiAgYm91bmRhcnlfbW9kZTogInRva2VuIgogIG92
ZXJsYXBfcmVzb2x1dGlvbjogImxvbmdlc3RfbWF0Y2giCgp0b3BpY19jb250ZXh0X2NoYXJhY3Rl
cnM6IDgwCg==
```
