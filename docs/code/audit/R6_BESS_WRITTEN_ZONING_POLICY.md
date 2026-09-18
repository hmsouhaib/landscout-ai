# DOCS.CONTINUITY.1.R6 — BESS written-zoning policy documentary audit

## Scope, authority and review state

Global audit **PARTIAL**; independent R6 review **PENDING**. This is a bounded documentary completion record, not an application/legal/global approval. Last approved functional boundary remains STEP 7F.1B.4. The [exact R6 ticket](../../project/tickets/DOCS.CONTINUITY.1.R6.txt), section 1, supplies ChatGPT's independent **R5 documentary APPROVED** verdict with low/nonblocking **OPEN R5-D01**. It is a supplied reviewer statement, not a new Codex execution or cryptographic signature. [CURRENT_STATE](../../project/CURRENT_STATE.md) records it successorally. R5's receipt and its historical PENDING remain unchanged; the R5 companion/reserve is not repaired here.

Starting recovery HEAD/tracking/actual remote: `86be69fe05f2ec27cd528c05200db3ad63176cc9`. Main/local tracking/actual remote: `aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02`. Branch: `recovery/docs-continuity-1-partial`. Root: `C:/souhaib/landscout-ai`. Initial status/index were clean with no unmerged entry or Git operation in progress. Resolve this receipt's eventual publication SHA from Git; no future self-SHA is embedded.

Readiness commands: `git status --short --untracked-files=all`, `git branch --show-current`, `git rev-parse --show-toplevel`, relevant `git rev-parse` refs, `git ls-files -u`, read-only .git operation-marker inspection, and `git ls-remote --heads origin main recovery/docs-continuity-1-partial`. The sandbox remote command failed connecting to GitHub:443. A first escalated explicit-cwd remote attempt returned “origin does not appear to be a git repository”. Read-only cwd/root/remote/ownership diagnostics then reproduced Git's dubious-ownership failure (repository Hammami/CodexSandboxOffline versus executing HAMMAMI/souha). Only afterward the authorized per-command exception `git -c safe.directory=C:/souhaib/landscout-ai ls-remote --heads origin main recovery/docs-continuity-1-partial` succeeded and observed both required server SHAs. No persistent trust/ACL/security/environment setting was changed.

Exactly six intended documentation paths:

- [Written-zoning companion](../files/configs/planning/muret_bess_zoning_policy.yaml.md).
- [Planning owner fragment](reviews/planning.json): exactly two rows and their R6 evidence.
- This new receipt.
- [Exact ticket archive](../../project/tickets/DOCS.CONTINUITY.1.R6.txt).
- [Documentation audit progress](DOCUMENTATION_AUDIT.md).
- [Current state](../../project/CURRENT_STATE.md).

No YAML, source, test, auditor, dependency, data, cache, artifact, prior receipt/ticket or R4/R5 companion changes. No coverage.json merge or next-unit start. BACKLOG_AND_GAPS unchanged: no new concrete application finding established.

## Ownership and progress

Original matrix and all six review fragments were inspected for both exact paths. Both actual planning.json rows were NOT_READ/read_complete=false, without a duplicate, extension counterpart or transferred_to field. Prior row records are preserved in r6_prior_evidence; no historical transfer note is invented or erased.

Transitions: YAML → CHECKED/true, companion → CORRECTED/true. YAML source_sha256 remains Git-content `c736ea8901997f4852fd1f72a3f6f34282452f18dcd9abc0ccbce8255adaad45`. Companion binding is recomputed over exact candidate Git bytes. No dependency or Python symbol is promoted.

Deduplicated original scope: **77/245 files**, **1,594/4,769 symbols** closed; **168 files / 3,175 symbols** remain. File statuses: CHECKED 29, CORRECTED 48, READ 141, NOT_READ 27. Symbols: CHECKED 1,593, CORRECTED 1, READ 2,078, NOT_READ 1,097. READ is not closure. New receipt/ticket and R5 approval/reserve do not change denominators. Next sorted NOT_READ path: `configs/planning/muret_plu_structure.yaml`, identified only, not begun.

## Reads and fidelity corrections

Entry/context route read: AGENTS; WORKING_RULES; RESUME; CURRENT_STATE; BACKLOG_AND_GAPS; DECISIONS; DOCUMENTATION_AUDIT; code README; R5 receipt; architecture/planning pipeline, relevant STEP_INDEX sections and DATA_FLOW planning branch. The R6 attachment was read completely. Protected-file authority and original ownership matrix/all fragments were consulted, not merged.

Task reads:

| Source | Read scope and qualification |
|---|---|
| configs/planning/muret_bess_zoning_policy.yaml | All 723 lines, including exact multiline quotes and all configured values. |
| Old companion | All unique explanations/field/consumer tables; all 642 scalar value rows. Its six repeated exact model-source blocks were byte-compared with the already-read owner. Readable YAML fence equals Git bytes; Base64 equals checkout bytes. |
| src/landscout/stages/interpret_bess_zoning.py | Entire 1–2394: models, guards, public APIs, canonical serializers, occurrence/route/chapter/parcel algorithms and validation. |
| tests/unit/test_interpret_bess_zoning.py | Entire 1–2164, including synthetic helpers, no-op physical validation fixture, private calls, mutations/rehashes and assertions. Unicode-bearing real-YAML assertions reread explicitly as UTF-8. |
| tests/integration/test_gpu_planning_end_to_end.py | Entire 1–409; actual synthetic ZIP/GeoPackage/PDF chain, empty-evidence UNKNOWN policy and four integration tests; not executed. |
| tests/unit/test_deep_immutability.py | 300–481, recursive family walk, operation/alias fixtures and fixed hash comparison; not executed. |
| src/landscout/common/strict_yaml.py | Complete 1–60, duplicate-key/UTF-8/error behavior. |
| src/landscout/stages/enrich_planning_zoning.py | 240–322 and 739–893: context checks, normalized-source validation and public rebuild. |
| src/landscout/stages/structure_planning_regulation.py | 516–550, 2286–2312 and 2330–2480: selected lock/config boundary, comparison tail, fragment construction and public source-complete wrapper; not a full module audit. |
| src/landscout/stages/index_planning_regulation.py | 715–1030, specifically 801–870 index metadata/page/hash validation; no PDF opened. |
| src/landscout/sources/gpu_fr.py | 2193–2275 public spatial-revalidation wrapper and surrounding inspection context; no full GPU audit claimed. |

Replaced generic/stale contract text with field-specific types/defaults/nullability, exact domains and validation/propagation. Added the 13 explicit empty role lists omitted from the old scalar table. All 642 old scalar cells matched decoded policy data; the old checkout SHA and byte snapshot were valid for that basis, not “wrong Git hashes”.

Explained Python-character offsets versus UTF-8 hashing; excerpt occurrence versus larger rule identity; same-rule reuse, duplicate occurrences and partial overlap; role links/context exclusion; derived route/chapter statuses and configured-article completeness. Traced actual source-zone/positive-area parcel interpretations and mixed/touch/no-overlap handling rather than inheriting R5 compiler non-goals.

Separated model validation, six lock equalities, physical GPU gate, indexed-fragment reconstruction and legal meaning. Distinguished deeply immutable policy graph from mutable result frames, in-memory reconstruction from unchecked model copies, loader evidence hashing from separate policy identity, and source-bound result reconstruction from coordinated rehashes. No new classification or legal conclusion.

Tests are documented according to their actual bodies: unit physical-source no-op; synthetic integration with no decision evidence; private helpers; upstream guard interception; real-YAML constants versus original PDF validation. The mapping-count test's later arm references the module-level valid_result fixture function and only asserts a broad error; no more specific result-check proof is claimed. These evidence qualifications are not automatically a new application finding.

## Single authorized offline loader execution

Exactly one call to the existing `load_bess_zoning_policy_config`, using installed `.venv\Scripts\python.exe -B -X utf8 -` from the repository. No uv/dependency installation, pytest, interpreter, result validator, GPU/EP pipeline, source acquisition, geospatial/PDF reconstruction or artifact production.

Exit **0**, loader elapsed **0.0831051999994088 seconds** (perf_counter around the loader only). The in-process audit hook guarded socket connect/DNS/sendto events; **zero guarded network attempts**. No loader exception or second call. A preliminary JavaScript orchestration syntax error occurred before submitting its read-only mechanical-check script, not during this loader call.

Results from the actual loaded object:

| Measure | Observed value |
|---|---|
| Root / lock fields | 7 / 6 |
| Chapters / evidence / routes | 13 / 28 / 13 |
| Required article IDs | ["1","2"] |
| Reviewed-section references | 26 |
| Distinct source-rule IDs | 18 |
| Positive / condition / difficulty route references | 13 / 10 / 3 |
| Evidence directions | SUPPORTS_POTENTIAL_COMPATIBILITY 13; CONDITION 10; SUPPORTS_DIFFICULTY 3; CONTEXT_ONLY 2 |
| Evidence kinds | ICPE_RULE 16; PUBLIC_INTEREST_EXCEPTION 2; USE_RESTRICTION 3; ACCESS_OR_NETWORK_CONDITION 1; TECHNICAL_EQUIPMENT_RULE 4; OTHER_RELEVANT_RULE 2 |
| Routes | CONDITIONAL_ROUTE 10; RESTRICTION_EXCEPTION_ROUTE 3 |
| Chapter statuses / confidences | CONDITIONAL_REVIEW 13 / LOW 13 |
| Terminal values, counting empty arrays | 655: 501 strings, 141 integers, 13 empty lists; zero nulls |
| Retained runtime graph | Root 1, lock 1, chapters 13, evidence models 28, route models 13, tuple occurrences 80; no reachable list/dict/set/bytearray |
| Canonical policy SHA256 | ef1f7cd0f5589e9a07428d25cd2b1a844e7cd49fb6db359951eb6c812c767586 |

Policy hash equals the existing test constant read at test_deep_immutability.py:469. That is a comparison against recorded expected identity, not execution of that test or proof of source applicability. No result component hash or Muret parcel distribution was generated.

Exact invocation follows; script only reads source/Git and inspects/hashes the loaded model, with output in the tool transcript:

```powershell
@'
import sys, json, importlib, time, subprocess, base64, ast
from pathlib import Path
from hashlib import sha256
from collections import Counter
from pydantic import BaseModel
events=[]
def guard(event,args):
    if event in {"socket.connect","socket.getaddrinfo","socket.gethostbyname","socket.sendto"}:
        events.append(event)
        raise RuntimeError("R6 offline network guard")
sys.addaudithook(guard)
m=importlib.import_module("landscout.stages.interpret_bess_zoning")
path=Path("configs/planning/muret_bess_zoning_policy.yaml")
started=time.perf_counter()
policy=m.load_bess_zoning_policy_config(path)
elapsed=time.perf_counter()-started
data=policy.model_dump(mode="json")
def leaves(v,p=""):
    if isinstance(v,dict):
        return [item for k,x in v.items() for item in leaves(x,p+"."+k if p else k)]
    if isinstance(v,list) and v:
        return [item for i,x in enumerate(v) for item in leaves(x,f"{p}[{i}]")]
    return [(p,v)]
runtime=Counter()
def inspect(v):
    assert not isinstance(v,(list,dict,set,bytearray))
    runtime[type(v).__name__]+=1
    if isinstance(v,BaseModel):
        assert type(v).model_config["frozen"] is True
        for k in type(v).model_fields: inspect(getattr(v,k))
    elif isinstance(v,tuple):
        for x in v: inspect(x)
inspect(policy)
raw=path.read_bytes()
git=subprocess.check_output(["git","show","HEAD:"+path.as_posix()])
oid=subprocess.check_output(["git","rev-parse","HEAD:"+path.as_posix()]).decode().strip()
evidence=[e for c in policy.chapters for e in c.evidence]
routes=[r for c in policy.chapters for r in c.route_assessments]
roles=("positive_evidence_ids","condition_evidence_ids","difficulty_evidence_ids")
result={"loader_calls":1,"loader_seconds":elapsed,"network_attempts":events,"git_oid":oid,
"git":{"bytes":len(git),"sha256":sha256(git).hexdigest(),"CR":git.count(b"\r"),"LF":git.count(b"\n"),"final_lf":git.endswith(b"\n")},
"checkout":{"bytes":len(raw),"sha256":sha256(raw).hexdigest(),"CR":raw.count(b"\r"),"LF":raw.count(b"\n"),"CRLF":raw.count(b"\r\n"),"final_crlf":raw.endswith(b"\r\n")},
"policy_sha256":m._policy_sha256(policy),"root_fields":len(data),"lock_fields":len(data["source_lock"]),
"chapters":len(policy.chapters),"evidence":len(evidence),"routes":len(routes),
"source_rule_ids":len({e.source_rule_id for e in evidence}),
"reviewed_section_references":sum(len(c.reviewed_section_ids) for c in policy.chapters),
"route_role_references":{role:sum(len(getattr(r,role)) for r in routes) for role in roles},
"leaves_including_empty_lists":len(leaves(data)),
"empty_lists":sum(v==[] for _,v in leaves(data)),
"nulls":sum(v is None for _,v in leaves(data)),
"scalar_types":dict(Counter(type(v).__name__ for _,v in leaves(data))),
"runtime_types":dict(runtime),
"kinds":dict(Counter(e.evidence_kind for e in evidence)),
"directions":dict(Counter(e.evidence_direction for e in evidence)),
"route_kinds":dict(Counter(r.route_kind for r in routes)),
"statuses":dict(Counter(c.zoning_precheck_status for c in policy.chapters)),
"confidences":dict(Counter(c.zoning_precheck_confidence for c in policy.chapters))}
print(json.dumps({"result":result,"data":data,"leaves":leaves(data)},ensure_ascii=False))

'@ | .venv\Scripts\python.exe -B -X utf8 -
```

## Byte preservation and bounded documentation checks

Pre-full-audit scoped command `.venv\Scripts\python.exe -B -X utf8 C:\souhaib\r6_check.py` completed exit 0 (WORKTREE); this temporary read-only checker is outside Git and executes no production loader/interpreter. It compares all 106 protected paths to their authority, and all **284 out-of-scope starting paths** against the **288-path starting tree**, including both exact raw-checkout EOL exceptions. Only the six allowed paths differ; all other fragment rows and top-level evidence remain unchanged. The original 245-path / 4,769-symbol ownership reconciliation gives the counts above.

Checks passed: 655 exact path/value cells, 104 chapter-summary JSON literals, five source-exact signatures, both complete YAML snapshots, 13 strictly parsed tracked JSON files, balanced fences/table widths, 52 local links across changed Markdown and zero incoming anchor links from other starting Markdown to this companion. Explicit ID occurrences outside fences: **0**; generated heading-ID occurrences: **51**, with no collision/duplicate. Counts use occurrences, not merely a set. New `git diff --check` exits 0; the cumulative main-to-candidate check retains exactly the same 13 historical whitespace observations (12 cold-start hard-break lines and one original ticket blank EOF), byte-for-byte unchanged. No archive cleanup.

Companion Git-content SHA256: `c5dbf13de941ef153d5759ef54441092b475298c0ab649db9b8fe3a2cc8f3afe`, matched by its sole owner row. Source Git/checkout bindings and the attachment comparison are explicit below. INDEX and post-receipt checks are recorded with the full-audit result separately, not assumed from the worktree pass.

Source OID: `a8a1f2d8e5fb04107a3e46de2b67cb140cafa38d`. Git YAML: **46,384 bytes**, SHA256 `c736ea8901997f4852fd1f72a3f6f34282452f18dcd9abc0ccbce8255adaad45`, 723 LF / zero CR / final LF. Checkout: **47,039 bytes**, SHA256 `879d50627c063bb10096950d004cf4d4e446ff04ef9a1178b3e3fb28e2ffdae3`, 655 CRLF / 68 lone LF / final CRLF. No normalization was written.

Second preserved EOL exception: `docs/project/tickets/DOCS.CONTINUITY.1.RESUME.2026-09-17.txt`, Git SHA256 `b5a0fa80569fbc0b11d28718c0037f9e8ba23caac5dadca6fd60c05c7cc64a5b`, checkout `9e18c25d571c5cfe34391d1f35833634bb4c3672087781360752fa0fba7243ed`. Exact R6 attachment/archive SHA256: `c8d5e70413cc3f068afe3048da9fc2d6666bffbdef8460cdf146d26ab5c3a6f2`.

No visual render: fresh PATH discovery found no pandoc/markdown/marked/node, and installed Python has no markdown/markdown_it/mistune/docutils. Existing earlier VS Code discovery is historical, not exercised R6 rendering. No installation/upload. Fences, table shape and links are static checks only; visual rendering remains PENDING.

Read-only discovery also encountered guessed absent paths (strict_yaml/normalization/matrix names), then used rg to resolve real paths. A large planning-fragment display was truncated; no truncated JSON was accepted. Exact relevant rows were re-read before patching. One apply_patch attempted whole-row matching without its existing trailing comma and failed without altering that fragment; the correctly scoped two-row patch was then applied. No source was modified to resolve tooling errors.

## Unique full INDEX audit and precise final delta

Exactly **one** full unchanged auditor invocation ran after explicit six-path staging:

```powershell
.venv\Scripts\python.exe -B -X utf8 tools/audit_documentation.py --check --progress > C:\souhaib\r6-candidate.stdout.txt
```

It completed **completed=true, exit 1**, with **10,271 findings**: completed PARTIAL, not a clean audit and not an interruption/exit 2. The tool call took 6.4770462 seconds including separate manifest capture and command overhead, not an auditor-only stopwatch. Progress stderr display was truncated by the tool's output budget, but its terminal completion/metrics and exit were visible; the full findings stdout is preserved outside Git.

Candidate manifest (sorted path/mode/blob records): `C:\souhaib\r6-candidate.manifest.json`; canonical manifest SHA256 **efff721c0a29d5c257499f0e02caea343b98a0ec5ccbb5495a60607dd5e6daf4**. Candidate: **290 paths, 287 unique blobs, 28,909,447 bytes**; 94 Python files / 94 AST parses / 4,863 current symbols; original coverage denominator 245 / 4,769; 5 Git processes; shallow_history=false. Candidate receipt blob: `1fe11e5978bbb03b60d0aa88847bbfb3b9b22b9e`, mode 100644.

Phase seconds as returned: index 0.5636317000025883; coverage-input 0.029588599998533027; python 2.449802200000704; checkout-markdown 0.8611774000019068; coverage 0.3496984999983397; references 0.3567548999999417; history 0.20045509999908973; index-postcondition 0.08134330000029877.

Full stdout: UTF-16 PowerShell capture, **2,317,352 bytes**, SHA256 **28f3bbb36179e0590f9a7aa67192dbbd779da2fd119075be8e5133753d147918**. Baseline is the retained R5 stdout, 2,315,742 bytes, SHA256 e6304db38284e9f10fadf88b313f513f59c4c07b0826fecfaa3f58e608e880bc. Multiset comparison of complete lines—not a truncated console excerpt—gives exactly these deltas:

- Removed R6 YAML's ambiguous line-ending-basis and stale-companion-hash diagnostics. The previous checkout hash was valid on its basis; the new explicit Git-content binding resolves these scanner comparisons.
- Replaced the existing inventory-mismatch line by the same line additionally naming the newly archived R6 ticket; the original global inventory is intentionally not merged.
- Added stale-file-fingerprint for this corrected companion relative to that unmerged original coverage.
- Added six unresolved-qualified-reference diagnostics for **literal canonical hash-domain strings**, not imports/callable references. Their source payloads are read in interpret_bess_zoning.py:803–825, 1099–1107, 1846–1867 and 2003–2007; the sixth base token comes from the prose's domain prefix. This is a lexical scanner limitation, not a changed hash or missing Python implementation. No attempt was made to suppress the finding or change the auditor/coverage.

The exact six scanner tokens are:

```text
landscout.bess_zoning
landscout.bess_zoning.factual_structure_input
landscout.bess_zoning.policy_config
landscout.bess_zoning.precheck_result
landscout.bess_zoning.zone_mapping_input
landscout.bess_zoning.zoning_relations_input
```

No other finding line changed. Net +5 findings from R5's 10,266. Full prefix counts: missing documented anchor 4,769; unresolved symbol review 4,769; unresolved semantic review row 245; missing companion exception 131; stale file fingerprint 111; unresolved qualified reference 106; ambiguous line-ending basis 99; export inventory mismatch 24; missing exact source snapshot 8; bad local link 3; DEV_LOG companion diagnostics 2; inventory mismatch 1; semantic ledger not COMPLETE 1; unfinished history audit 1; undeclared raw-checkout/EOL difference 1. These include historical/global diagnostics; bounded local links/values/preservation passed independently.

Unchanged exact SHA256: auditor 5b5aae765c6c32225496d7830e17e83a9bfac89e007949b032b75b13eda3029f; auditor test 0c6ce4167f33c56ad09c3ea7cbe8ebeb039cda7ed013c38022a29d5cc98b0665; coverage.json 5ae2a994effb59947b0dbe4af97b777bc17fb13998a8ba5b8110f2c42052036c; original matrix 5c8e3d02355c6afb640624728b001b7694f08ba2b97271feca103f51f14a8e62.

The pre-audit INDEX scoped check also passed exit 0 with the same 106/284 preservation, 655 values, 104 summary literals, five signatures, 13 strict JSON files, 52 links, 0 explicit / 51 heading-ID occurrences, 793 table lines and 13 unchanged inherited whitespace observations; staged new diff check exited 0.

**Candidate versus final:** after this full run, only this receipt is completed and restaged. A separate read-only index-manifest comparison must and does restrict the final delta to this exact receipt path; final blob/manifest identity is returned in the execution report after finalization, not embedded recursively as this document's own hash. The same scoped checker and new staged diff check verify final bytes/links/fences/preservation. No second full auditor run and no claim that the audited candidate and final content are identical.

## Publication boundary and retained limits

Stage only the six explicit paths; authorized commit message `docs: audit BESS written zoning policy configuration reference`; push only `origin recovery/docs-continuity-1-partial`. Final live publication/clean-tree/server-ref observations belong to the returned execution report, not a guessed self-SHA here.

A-001..A-004, five prior test-evidence limits, R3-T01..04, OPEN R5-D01, cold-start acceptance, visual rendering, global final validation and pending 7F.1C.1 semantic review remain preserved. R6 adds no application repair/finding, changes no historical verdict and does not turn the global audit into COMPLETE. Stop for independent R6 review; do not begin the next structure-config unit.
