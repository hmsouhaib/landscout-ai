# `README.md`

## File identity

- Repository path: `README.md`
- File type: Markdown
- Responsibility: Introduces LandScout's current evidence-first BESS scope and links to the detailed technical reference.
- Source SHA256: `356e0c4cc2a7c52bd798f4ce0d9b0d8230688d9a8298207eef3070e66a6d33bf`

## 1. Purpose

Introduces LandScout's current evidence-first BESS scope and links to the detailed technical reference.

## 2. Position in LandScout architecture

This is human engineering documentation/history, consumed by engineers and repository documentation readers.

## 3. Imports and dependencies

Not applicable: this is not Python source.

## 4. Contract taxonomy

Its exact content is reproduced below. No Python alias, frame column, model field, or runtime business semantic is inferred from passive text.

````text
# LandScout AI

LandScout AI is an evidence-first system for land origination and preliminary
site analysis. Development is currently BESS-first, with Muret serving as a
proving ground rather than the product's permanent geographic identity.

Implemented evidence foundations include cadastral parcels and shape screening,
IGN electricity-grid proxies, GPU/PLU zoning and CNIG planning features, IGN road
proxies and proximity, and official protected-area source acquisition. Source
snapshots, provenance, factual geometry, and unresolved evidence are preserved
so later decisions can be audited.

These outputs are preliminary evidence, not authorization. A mapped road does
not prove legal or heavy-vehicle access; mapped grid infrastructure does not
prove capacity or connection feasibility; planning prechecks are not permits;
and protected-area acquisition does not yet provide parcel-level environmental
semantics.

The project remains under active development. Final scoring, owner/contact
identification, delivery workflows, and autonomous production operation are not
yet complete.

## Technical documentation

See [the living file-by-file technical reference](docs/code/README.md).
````

## 5. Classes / models / dataclasses

Not applicable.

## 6. Functions and methods

Not applicable.

## 7. Data contracts

Interpreted only as human engineering documentation/history by engineers and repository documentation readers; not a Pandas/GeoPandas schema.

## 8. Interfaces

Consumer: engineers and repository documentation readers.

## 9. Error handling

Not applicable to the passive file itself; its consumer reports malformed or unsupported content.

## 10. Side effects

The passive file performs no operation. Reads/resolution belong to its named consumer.

## 11. Security / trust boundaries

The companion SHA binds exact bytes. No source authority is inferred unless a runtime adapter validates it.

## 12. GIS / CRS rules

Not applicable unless an exact configuration field in the reproduced content is consumed by a GIS validator.

## 13. Provenance rules

The path and SHA identify this repository snapshot; passive prose/history is not implementation proof.

## 14. Business meaning

No business decision is executed by this passive file.

## 15. Explicit non-goals

- Does not independently run a source adapter, GIS calculation, policy, score, ranking, or legal decision.

## 16. Tests

Not applicable directly; repository/tool configuration may be exercised by the mandated validation commands.

## 17. Change impact

Review engineers and repository documentation readers, repository workflows, and this companion SHA after any byte change.
