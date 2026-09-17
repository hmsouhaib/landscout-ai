# Interim fresh-context cold-start exercise — 2026-09-17

Execution status: **EXECUTED_INTERIM_FRESH_CONTEXT**.

Acceptance: **PENDING**. This is not a final global documentation audit, independent ChatGPT approval of DOCS.CONTINUITY.1, or approval of the EP semantic draft. The entry records read during the exercise remained IN_PROGRESS/PARTIAL. A separate bounded verifier must compare the answers with current source/tests and provenance; this executor has not performed that verification.

## Executor, context and authority

Executor/task: `/root/continuity_cold_start`. The task was supplied as a genuinely fresh read-only documentation exercise; no preceding project conversation was present in this executor's initial context. The executor began with `AGENTS.md`, then followed repository documentation links. This is not a same-context claim of forgetting. Exact orchestration configuration beyond the visible supplied task must be retained by the parent rather than invented here.

The original exercise permitted repository documents and read-only local Git queries. It prohibited fetch, edits, staging, commits, production/test execution, application-cache access and choosing a next functional ticket. The exercise obeyed those boundaries. A subsequent explicit parent instruction authorized writing only this new evidence file with `apply_patch`; that archival write is separate from the original read-only exercise. No other file was changed by this executor.

Exact initial task supplied:

> Genuinely fresh read-only documentation exercise. Repository C:\souhaib\landscout-ai. Start ONLY with AGENTS.md, then follow repository-document links and the reusable docs/project/COLD_START_EXERCISE.md prompt. You have no previous chat context. Answer its questions with file/section references and report any ambiguities or missing evidence. You may inspect live read-only Git identity but do not fetch, edit, stage, commit, run production/test code, open caches or choose a next functional ticket. Return your answers and exact files accessed. This exercise is comprehension evidence, not independent ChatGPT approval.

Exact reusable repository prompt read:

> You are a fresh read-only LandScout comprehension reviewer. Repository: `C:\souhaib\landscout-ai`. Start only from `AGENTS.md`, then use repository documents and read-only Git queries. Do not use prior conversation, account memory, external audit scripts, network source data or application caches. Do not edit files, commit, push, run source acquisitions or propose the next functional ticket. Follow the mandatory reading route and return the required context receipt. Answer the questions in `docs/project/COLD_START_EXERCISE.md`, citing repository file/section references and distinguishing publication, reported execution and independent review. Disclose every inaccessible source or unresolved contradiction. Do not infer approval from a “complete” log entry.

## Full returned exercise result

Cold-start comprehension completed as a read-only exercise; acceptance and independent review remain pending. This is not approval of DOCS.CONTINUITY.1 or the EP semantic draft.

Executor: `/root/continuity_cold_start`. I began with `AGENTS.md`, with no prior project conversation supplied. I read repository documentation and used local read-only Git queries. I did not fetch, edit, stage, commit, execute application/tests, open caches or select another functional ticket.

### Context receipt and answers

1. **Purpose and Muret.** LandScout is BESS-first, evidence-led land origination and preliminary analysis, eventually following `SCAN → FILTER → ANALYZE → SCORE → IDENTIFY → EXPORT → HUMAN`. Muret, commune 31395, is a proving ground, not permanent geography. Overnight scanning is an example, not an established scheduling requirement.  
   References: `docs/project/WORKING_RULES.md`, “Permanent collaboration rules”; `docs/project/DECISIONS.md`, DEC-002; `docs/code/ARCHITECTURE.md`, “Product scope”.

2. **Implemented versus absent.** Implemented library components cover source acquisition/verification, cadastral normalization and area/shape screening, IGN grid proxies/proximity/coverage, GPU spatial and written planning, CNIG meaning/policy/application/aggregation, road proxies/proximity/coverage, and EP archive/catalog/attribute/geometry/alignment evidence. Absent are the end-to-end scheduler/orchestrator, global score/ranking, verified owner/contact workflow, production delivery/human workflow, environmental executable category policy and parcel environmental analysis. Library artifact functionality must not be confused with the final product export workflow.  
   References: `docs/code/ARCHITECTURE.md`, “Implemented functional chain” and “Current unimplemented product areas”; `docs/code/DATA_FLOW.md`; `docs/project/CURRENT_STATE.md`, “Implemented components and missing product outcomes”.

3. **Live identity, approval and pending work.** Local repository is `C:/souhaib/landscout-ai`, branch `main`, HEAD `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`; configured origin is `https://github.com/hmsouhaib/landscout-ai.git`. Local `origin/main` resolves to the same SHA. I did not contact the remote, so this is not proof of current remote freshness. The worktree is dirty with extensive documentation edits and untracked continuity/audit/tooling/new-test material.

   The latest publication is the documentation-only STEP 7F.1C.1 draft. The last independently approved functional boundary **as recorded in the supplied conversation summary** is STEP 7F.1B.4, `ca0ec73de37137b5515c1dfea14e2ea8a2a1ba3d`: source-bound EP bundle assembly and complete physical FID alignment. Its complete original review receipt is unavailable.

   DOCS.CONTINUITY.1 is still recorded as IN_PROGRESS/PARTIAL. Pending work includes global audit closure, bindings/checker integration, final validation/reports/publication and independent review. Full EP semantic review also remains pending. The interim checker-test results are reported executions, not executions performed by this exercise.  
   References: `CURRENT_STATE.md`, “Publication versus independent approval” and “Active ticket and next action”; `CONTEXT_PROVENANCE.md`, “Known review boundary”; `docs/code/audit/DOCUMENTATION_AUDIT.md`.

4. **Authority and sequencing.** Souhaib decides product direction. ChatGPT reviews, architects and authors tickets read-only, with no Git writes. Codex implements, validates and publishes only explicitly authorized scoped work; Codex cannot independently approve itself. One explicit ticket at a time, with independent review before the next functional increment. This exercise authorizes no repository mutation.  
   References: `AGENTS.md`, “Roles and authority”; `WORKING_RULES.md`, “Permanent collaboration rules”; DEC-008.

5. **How bytes become trusted results.** Strict serialization and reconstructed validated configuration establish permitted identity. Safe HTTPS establishes transport properties, not dataset semantics. Adapters then verify current bytes, configured size/hash, archive members, extraction structure and configured physical layers. Source-complete consumers reread/rebuild authoritative physical evidence and compare it with supplied objects. For INPN, archive-derived inventory, marker inventory, physical inventory and caller inventory must agree; verified immutable package snapshots feed the approved readers, with final source postconditions.

   A plausible SHA string, matching marker, coherent nested hashes or intrinsic object validation alone cannot establish physical correspondence. Hashing a live path before and after reopening is not equivalent to reading one immutable snapshot. Even genuine matching bytes do not establish environmental meaning, correct georeferencing, legal access, grid capacity, permits or documentation accuracy. Frozen envelopes containing DataFrames are not thereby deeply immutable.  
   References: `SOURCE_TRUST_MODEL.md`, “Core rule”, “Strict serialization and immutable configuration”, “Shared HTTPS boundary” and “INPN / PatriNat”; `ENVIRONMENT_PIPELINE.md`, inventory/catalog/profile/bundle sections.

6. **SQLite rather than Pyogrio for EP geometry rows.** Locked Pyogrio 0.13.0 drops M during geometry materialization, including with `force_2d=False`. The supported route is verified GPKG bytes → `sqlite3.Connection.deserialize` → query-only physical FID/geometry-BLOB projection → Standard GeoPackageBinary validation → embedded WKB parsed by Shapely. Metadata and attribute-only Pyogrio remain supported; no environmental attributes are selected by the geometry path. This preserves supported measured-dimension evidence without repair, dimensional coercion or reprojection.  
   References: DEC-004; `ENVIRONMENT_PIPELINE.md`, “Geometry technical-quality profile”; `TESTING_STRATEGY.md`, “INPN geometry byte-snapshot and measured-dimension evidence”.

7. **FID alignment.** It proves that physically revalidated profiles cover the same complete canonical physical integer-FID domain for every catalog-ordered `(relative_path, layer_name)`, with matching package/source identity, counts, extrema and full sequence hash. Equal counts/extrema are insufficient: `[1,2,4]` and `[1,3,4]` differ. `id_mnhn` is not a substitute. The bundle does not create an attribute-cell/geometry join or prove category meaning, correct CRS, environmental suitability or legal authorization. Private `_align_layers` is structural, not an alternative physical trust boundary.  
   References: DEC-006; `ENVIRONMENT_PIPELINE.md`, “Source-bound evidence bundle”; evidence-module companion §§5–6.

8. **Why `sig_tadl` remains unresolved.** Its recorded declaration is EPSG:32753, while coordinates/bounds near 140/−66 appear inconsistent with that declaration. Matching catalog and independently parsed bounds only show agreement about the stored numbers—not their correct real-world CRS interpretation. Valid XY MultiPolygon topology, byte hashes and FID alignment do not settle georeferencing. No replacement CRS or reprojection is justified by this observation. These are historical recorded results, not a fresh cache inspection.  
   Reference: `ENVIRONMENT_PIPELINE.md`, “Recorded factual result (historical source verification, not rerun by this documentation audit)”; backlog S-004.

9. **Why the semantic draft authorizes no rules.** STEP 7F.1C.1 is explicitly `RESEARCH_DRAFT_NOT_RUNTIME_POLICY`, with no production consumer. Its 64 exact non-null inventory keys are not 64 confirmed executable meanings; zero meanings are confirmed for snapshot applicability. Producer/export edition/field/value correspondence and documentary adoption chronology remain unresolved. Marginal frequencies cannot establish cross-field co-occurrence, compound delimiter grammar or automatic `Nature`/`nature` equivalence. The supplied partial review did not exhaustively validate all 64 entries, 42 sources and MD/JSON equivalences. Independent semantic review and an explicit new ticket are necessary before mapping.  
   References: DEC-007; `CURRENT_STATE.md`; `CONTEXT_PROVENANCE.md`, “Known review boundary”; `CHANGE_IMPACT_GUIDE.md`, “Future INPN semantic boundary”.

10. **INPN acquisition/alignment change impact.** Review these boundaries together, as applicable:

    - `configs/sources/inpn_protected_areas_fr.yaml`, `InpnProtectedAreasSourceConfig`, and `load_inpn_protected_areas_source_config`.
    - Acquisition APIs `download_inpn_protected_areas_archive`, `extract_inpn_protected_areas_archive`, `validate_inpn_protected_areas_extraction`; archive snapshot/member/inventory/postcondition helpers, sidecars and recovery publication.
    - Catalog builder/validator in `inpn_protected_areas_catalog_fr.py`.
    - Attribute builder/validator in `inpn_protected_areas_attributes_fr.py`.
    - Geometry builder/validator in `inpn_protected_areas_geometry_fr.py`.
    - `build_inpn_protected_areas_evidence_bundle`, `validate_inpn_protected_areas_evidence_bundle`, `_align_layers`, `_validate_bundle_intrinsic`, canonical payload/hash and alignment records in `inpn_protected_areas_evidence_fr.py`.
    - `src/landscout/sources/__init__.py` public exports, shared safe HTTPS/serialization boundaries when affected, and downstream schemas/hashes/source locks.
    - All five corresponding `tests/unit/test_inpn_protected_areas*_fr.py` suites; relevant safe-HTTP/immutability regressions if shared contracts change. Alignment tests must retain genuine physical positive controls, differing-FID-set negatives, coordinated forgery, reader ownership/call counts, mutation postconditions and portable/immutable results.

    Preserve the existing attribute-only Pyogrio and geometry-only SQLite readers; do not replace public physical validation with structural checks or introduce a third reader. Hash/schema changes require explicit compatibility decisions.  
    References: `CHANGE_IMPACT_GUIDE.md`, source-adapter and five INPN sections; `FILE_INDEX.md`; acquisition companion §§6–8; evidence companion §§5–8; evidence-test companion §1.

11. **Exact local validation routine.** Ticket §11 requires the documentation auditor and focused new tests, then the complete repository suite once at finalization—not after each prose edit. Every pytest invocation uses its own fresh short unique base under `%LOCALAPPDATA%\LandScout\pytest-runs`, for example:

    ```powershell
    $landscoutTestTemp = Join-Path $env:LOCALAPPDATA ('LandScout\pytest-runs\d' + [guid]::NewGuid().ToString('N').Substring(0, 5))
    uv run pytest -q --basetemp $landscoutTestTemp
    ```

    The focused checker suite is `tests/unit/test_audit_documentation.py`, with a separate fresh base. Required gates include:

    ```text
    uv run ruff check .
    uv run ruff format --check .
    uv run mypy src
    uv run mypy tools/audit_documentation.py
    uv lock --check
    uv pip check
    uv run python -m compileall -q src tests tools
    uv run python tools/audit_documentation.py --check
    git diff --check
    ```

    The tool’s final check reads the explicitly staged candidate; staging is not authorized by this exercise. Record counts, warnings/skips/xfails and final native exit codes including cleanup. The historical application baseline is 3,939 cases; report exact new-test arithmetic rather than treating that old count as a new run. Verify protected production/config/dependency/pre-existing-test bytes against the starting manifest. No weakening tests, reinstalling dependencies, changing security settings, broad temp deletion or documentation-driven EP redownload.  
    References: archived ticket §11; `TESTING_STRATEGY.md`, “Full-suite and focused validation” and “Local documentation checker”; DEC-012.

12. **Interrupted work and deferred work.** Preserve dirty changes, useful caches, recovery `.bak` material, partial findings, audit progress and historical recovery branches. Resume from live Git state, diff and ledger; never reset/restore/stash/clean/rebase/amend/merge/force-push merely to satisfy clean-tree readiness. Partial work is not complete or approved; request appropriate recovery authority if publication is necessary.

    CI/PR/workflow automation is explicitly deferred. Environmental mapping/normalization/parcel analysis, scoring, owner discovery and product delivery/orchestration are unauthorized proposals, not automatic next actions. Open application findings A-001/A-002 require separate correction authority.  
    References: `WORKING_RULES.md`, “Safe work and interruption recovery”; `CACHE_AND_RECOVERY.md`, “Recovery state is not a cache miss”; backlog W/R/P/D/A sections.

### Ambiguities and missing evidence

- **Broken navigation:** `CURRENT_STATE.md` links to `ENVIRONMENT_PIPELINE.md#current-factual-result`; that heading was renamed to “Recorded factual result (historical source verification, not rerun by this documentation audit)”.
- Entry records explicitly remain partial; the exercise document says not to turn an exercise against unfinished entry records into completed acceptance. This result is comprehension evidence only.
- True current remote HEAD was not verified; local `origin/main` may be stale.
- Earlier original prompts/full review receipts and unrecorded decision rationale remain unavailable. Appendix A is a selected summary, not a transcript.
- The independent source/test verifier has not been performed by me. I used documentation, selected embedded excerpts and local Git evidence, not direct executable-source verification.
- I did not inspect external semantic sources, the full semantic-reference pair or caches; their unresolved meanings, source-access/PDF limits and recorded historical executions remain unresolved/reported.
- The audit report still records incomplete full-suite/visual-rendering/global-audit evidence. I did not close those gaps.

### Exact repository files accessed

All paths are relative to `C:\souhaib\landscout-ai`. “Accessed” includes bounded excerpts, searches and diff reads, not an assertion that every long file was fully reviewed.

```text
AGENTS.md
docs/project/WORKING_RULES.md
docs/project/CURRENT_STATE.md
docs/project/STEP_INDEX.md
docs/project/DECISIONS.md
docs/project/BACKLOG_AND_GAPS.md
docs/project/RESUME.md
docs/project/COLD_START_EXERCISE.md
docs/project/CONTEXT_PROVENANCE.md
docs/project/tickets/DOCS.CONTINUITY.1.txt
docs/code/audit/DOCUMENTATION_AUDIT.md
docs/code/README.md
docs/code/ARCHITECTURE.md
docs/code/DATA_FLOW.md
docs/code/SOURCE_TRUST_MODEL.md
docs/code/ENVIRONMENT_PIPELINE.md
docs/code/CHANGE_IMPACT_GUIDE.md
docs/code/TESTING_STRATEGY.md
docs/code/CACHE_AND_RECOVERY.md
docs/code/FILE_INDEX.md
docs/code/files/configs/sources/inpn_protected_areas_fr.yaml.md
docs/code/files/src/landscout/sources/inpn_protected_areas_fr.py.md
docs/code/files/src/landscout/sources/inpn_protected_areas_evidence_fr.py.md
docs/code/files/tests/unit/test_inpn_protected_areas_evidence_fr.py.md
```

Local Git metadata was additionally queried through `rev-parse`, `branch`, `remote -v`, `status`, `log`, `diff --stat` and targeted `diff`.

## Archival operation and verification handoff

The parent subsequently authorized this single new file. Before writing it, the executor checked that `docs/code/audit/cold_start_resume_2026-09-17.md` did not exist. The full returned result above is preserved as exercise-time evidence; later parent edits or successful checks must not silently rewrite what this executor observed.

The archival file itself is an additional accessed/written path, outside the original read-only exercise's accessed-file list. No tests, application code, source caches, external source data or remote Git operations were run during archival. Separate verification and final acceptance remain **PENDING**.
