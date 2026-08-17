# `configs/planning/muret_plu_structure.yaml`

## File identity

- Repository path: `configs/planning/muret_plu_structure.yaml`
- File type: YAML configuration
- Primary responsibility: Defines deterministic Muret regulation layout, heading grammar, zone aliases, and topic-evidence terms.
- Layer / domain: `checked-in configuration` / `planning`
- Public or internal role: Repository artifact; not a Python public API.
- Source SHA256: `74bf407441b66cde62efda581fbbb7df0d27b9d2148b210b7749ddf61b1b763a`

## 1. Purpose

Defines deterministic Muret regulation layout, heading grammar, zone aliases, and topic-evidence terms.

## 2. Position in LandScout architecture

This `checked-in configuration` artifact supplies exact checked-in bytes to the current repository. Consumers found by exact path reference are: `docs/DEV_LOG.md`.

## 3. Imports and dependencies

Not a Python module. Its consumers parse or interpret the bytes using the source/configuration functions identified by repository references and pipeline documentation.

## 4. Constants and domains

Every parsed leaf field is listed below; list indices preserve source order.

| Field path | Exact checked-in value | Contract role |
|---|---|---|
| `schema_version` | `2` (`int`) | Selects the strict configuration schema; unsupported versions are rejected. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `structure_profile` | `"muret_plu_20240215_v1"` (`str`) | Configures `structure profile` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `document_lock.document_id` | `"33edb4c9f6943c88d8d92518bff20bec"` (`str`) | Configures `document id` under the exact parent path `document_lock`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `document_lock.pdf_sha256` | `"5358ebad6b0cda6de681ba3536e29b8b6291fb701c7d3711f4ee1d6fdb85c6fb"` (`str`) | Binds the exact bytes or canonical component named by `pdf_sha256`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `document_lock.pages_content_sha256` | `"928e7e59c45e27c38e39d3f28f3eb10bd2590886416df57efc4ac8e5d8901ec9"` (`str`) | Binds the exact bytes or canonical component named by `pages_content_sha256`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `document_lock.index_content_sha256` | `"6a0009228ca17128c0a8bb329d9c2277a1b6638708a67b913b72ee93063e42cd"` (`str`) | Binds the exact bytes or canonical component named by `index_content_sha256`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `document_lock.normalization_profile` | `"fr_literal_v1"` (`str`) | Configures `normalization profile` under the exact parent path `document_lock`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `document_layout.body_start_page` | `1` (`int`) | Configures `body start page` under the exact parent path `document_layout`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `document_layout.table_of_contents_pages` | `[]` (`list`) | Configures `table of contents pages` under the exact parent path `document_layout`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `document_layout.max_heading_continuation_lines` | `2` (`int`) | Configures `max heading continuation lines` under the exact parent path `document_layout`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `document_layout.include_table_of_contents_in_topic_evidence` | `false` (`bool`) | Enables/disables the exact include table of contents in topic evidence behavior; Boolean coercion rules belong to the consuming model. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `heading_patterns.zone_chapter[0]` | `"^ZONE\\s+(?P<label>[A-Za-z]+(?:\\s*0)?)\\s*$"` (`str`) | Ordered configured member of `heading_patterns.zone_chapter`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `heading_patterns.article[0]` | `"^ARTICLE\\s+(?P<zone>[A-Za-z]+(?:\\s*0)?)\\s+(?P<number>\\d+(?:\\.\\d+)?)\\s*[-–—]\\s*(?P<title>.*)$"` (`str`) | Ordered configured member of `heading_patterns.article`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `heading_patterns.general_section[0]` | `"^ARTICLE\\s+(?P<number>\\d+(?:\\.\\d+)?)\\s*[-–—]\\s*(?P<title>.*)$"` (`str`) | Ordered configured member of `heading_patterns.general_section`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `heading_patterns.continuation[0]` | `"^[^a-z]*[A-ZÀ-ÖØ-ÞŒ][^a-z]*$"` (`str`) | Ordered configured member of `heading_patterns.continuation`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `ignored_patterns.page_headers[0]` | `"^Muret-12ème modification du PLU$"` (`str`) | Ordered configured member of `ignored_patterns.page_headers`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `ignored_patterns.page_headers[1]` | `"^\\d+$"` (`str`) | Ordered configured member of `ignored_patterns.page_headers`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `ignored_patterns.page_footers` | `[]` (`list`) | Configures `page footers` under the exact parent path `ignored_patterns`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.UAa` | `"UA"` (`str`) | Configures `UAa` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.UAb` | `"UA"` (`str`) | Configures `UAb` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.UBa` | `"UB"` (`str`) | Configures `UBa` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.UBb` | `"UB"` (`str`) | Configures `UBb` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.UFa` | `"UF"` (`str`) | Configures `UFa` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.UFc` | `"UF"` (`str`) | Configures `UFc` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.UFd` | `"UF"` (`str`) | Configures `UFd` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.AUa` | `"AU"` (`str`) | Configures `AUa` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.AUfa` | `"AUf"` (`str`) | Configures `AUfa` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.AUfb` | `"AUf"` (`str`) | Configures `AUfb` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.AUfc` | `"AUf"` (`str`) | Configures `AUfc` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.AUfd` | `"AUf"` (`str`) | Configures `AUfd` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.AUfo` | `"AUf0"` (`str`) | Configures `AUfo` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.NL` | `"N"` (`str`) | Configures `NL` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.Ne` | `"N"` (`str`) | Configures `Ne` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.Nh` | `"N"` (`str`) | Configures `Nh` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `zone_aliases.Nr` | `"N"` (`str`) | Configures `Nr` under the exact parent path `zone_aliases`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.destination_and_use[0]` | `"occupation du sol"` (`str`) | Ordered configured member of `topics.destination_and_use`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.destination_and_use[1]` | `"utilisation du sol"` (`str`) | Ordered configured member of `topics.destination_and_use`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.destination_and_use[2]` | `"destination"` (`str`) | Ordered configured member of `topics.destination_and_use`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.public_interest_equipment[0]` | `"équipement public"` (`str`) | Ordered configured member of `topics.public_interest_equipment`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.public_interest_equipment[1]` | `"équipement d'intérêt collectif"` (`str`) | Ordered configured member of `topics.public_interest_equipment`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.public_interest_equipment[2]` | `"service public"` (`str`) | Ordered configured member of `topics.public_interest_equipment`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.public_interest_equipment[3]` | `"intérêt collectif"` (`str`) | Ordered configured member of `topics.public_interest_equipment`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.technical_equipment[0]` | `"ouvrage technique"` (`str`) | Ordered configured member of `topics.technical_equipment`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.technical_equipment[1]` | `"installations techniques"` (`str`) | Ordered configured member of `topics.technical_equipment`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.technical_equipment[2]` | `"locaux techniques"` (`str`) | Ordered configured member of `topics.technical_equipment`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.energy[0]` | `"énergie"` (`str`) | Ordered configured member of `topics.energy`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.electricity[0]` | `"électricité"` (`str`) | Ordered configured member of `topics.electricity`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.electricity[1]` | `"électrique"` (`str`) | Ordered configured member of `topics.electricity`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.transformer[0]` | `"transformateur"` (`str`) | Ordered configured member of `topics.transformer`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.classified_installation[0]` | `"installation classée"` (`str`) | Ordered configured member of `topics.classified_installation`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.classified_installation[1]` | `"installations classées"` (`str`) | Ordered configured member of `topics.classified_installation`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.classified_installation[2]` | `"ICPE"` (`str`) | Ordered configured member of `topics.classified_installation`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.risk[0]` | `"risque"` (`str`) | Ordered configured member of `topics.risk`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.risk[1]` | `"risques"` (`str`) | Ordered configured member of `topics.risk`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.nuisance[0]` | `"nuisance"` (`str`) | Ordered configured member of `topics.nuisance`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.nuisance[1]` | `"nuisances"` (`str`) | Ordered configured member of `topics.nuisance`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.fire_safety[0]` | `"incendie"` (`str`) | Ordered configured member of `topics.fire_safety`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.fire_safety[1]` | `"défense contre l'incendie"` (`str`) | Ordered configured member of `topics.fire_safety`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.access[0]` | `"accès"` (`str`) | Ordered configured member of `topics.access`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.access[1]` | `"desserte"` (`str`) | Ordered configured member of `topics.access`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.setbacks[0]` | `"recul"` (`str`) | Ordered configured member of `topics.setbacks`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.setbacks[1]` | `"distance minimale"` (`str`) | Ordered configured member of `topics.setbacks`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.setbacks[2]` | `"implantation"` (`str`) | Ordered configured member of `topics.setbacks`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.networks[0]` | `"réseau"` (`str`) | Ordered configured member of `topics.networks`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topics.networks[1]` | `"réseaux"` (`str`) | Ordered configured member of `topics.networks`; order and uniqueness are validated/consumed where required. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topic_match_policy.boundary_mode` | `"token"` (`str`) | Configures `boundary mode` under the exact parent path `topic_match_policy`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topic_match_policy.overlap_resolution` | `"longest_match"` (`str`) | Configures `overlap resolution` under the exact parent path `topic_match_policy`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |
| `topic_context_characters` | `80` (`int`) | Configures `topic context characters` under the exact parent path `<root>`. Consumers found by exact repository path reference: `docs/DEV_LOG.md`. Exact allowed values/nullability are enforced by the consuming Pydantic/configuration validator. |

## 5. Classes / models / dataclasses

Not applicable; this file declares no Python class.

## 6. Functions and methods

Not applicable; this file declares no Python function or method.

## 7. Data contracts

The exact byte-bound values or text lines above are the data contract for this file. Structured validators in consuming Python modules remain authoritative for types, nullability, allowed values, units, source provenance, calculations, and downstream semantics.

## 8. Interfaces

Direct literal-path consumers are listed above. Git, uv, Python, configuration loaders, documentation readers, or generated-data directory conventions consume project metadata according to the file type.

## 9. Error handling

This passive file raises no exception. Its consumers reject missing, malformed, unsupported, duplicate, semantically invalid, or stale content with their documented controlled errors.

## 10. Side effects

The file itself has no runtime side effect. A consumer may read it, resolve dependencies, configure tools, or use it as source/policy evidence; those effects belong to the consuming function.

## 11. Security / trust boundaries

The SHA256 binds this documentation to exact bytes. Checked-in configuration identity is necessary but does not replace physical source/hash verification performed by source-complete adapters.

## 12. GIS / CRS rules

Only structured CRS fields listed above impose a GIS rule, and their consuming validators define it. Otherwise not applicable.

## 13. Provenance rules

Checked-in source locks, URLs, hashes, versions, profile IDs, and evidence references are textual provenance inputs. Their consuming code determines whether and how physical bytes are revalidated.

## 14. Business meaning

This file supports the `planning` domain only through its exact checked-in values and current consumers.

## 15. Explicit non-goals

- Planning facts and prechecks do not constitute legal advice, authorization, or prohibition.

## 16. Tests

Tests that load or mention this path are documented in their companion files. No test is inferred solely from the filename.

## 17. Change impact

Changing these bytes requires reviewing every consuming validator, source/policy/config hash, generated result or artifact lineage, affected tests, and this companion SHA256. Dependency-lock changes also require `uv lock --check` and `uv pip check`.
