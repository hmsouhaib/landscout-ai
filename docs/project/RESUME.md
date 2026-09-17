# Resume LandScout in a new chat

Do not rely on previous chat memory. Explicitly ask the session to read [AGENTS.md](../../AGENTS.md); automatic client loading is not assumed.

## Minimal reading route

1. Check accessible repository/remote identity, branch, HEAD and worktree. State any missing local/remote access.
2. Read [WORKING_RULES](WORKING_RULES.md), [CURRENT_STATE](CURRENT_STATE.md), [STEP_INDEX](STEP_INDEX.md), relevant [DECISIONS](DECISIONS.md) and [BACKLOG_AND_GAPS](BACKLOG_AND_GAPS.md).
3. Verify the scope/provenance of the latest available approval, not just a historical completion label. Read [CONTEXT_PROVENANCE](CONTEXT_PROVENANCE.md) if history is ambiguous.
4. If interrupted work exists, inspect its diff and [audit progress](../code/audit/DOCUMENTATION_AUDIT.md) before invoking any initial clean-tree prerequisite. Preserve it.
5. Return the receipt below; then load only relevant technical docs, source and tests. The complete historical snapshots need not be ingested for an unrelated small task.

## Required context receipt before action

- Exact live HEAD, branch, publication/worktree status and access limitations.
- LandScout's purpose and implemented versus missing outcomes.
- Last independently approved boundary, reviewed SHA, scope and provenance.
- Active ticket, actual implementation/review state and pending work.
- Essential collaboration and evidence prohibitions.
- Unresolved source/product questions and missing historical material.
- Intended next action and the exact authority for it; no assumed next ticket.

## Ready-to-copy reviewer prompt

> Reprends LandScout depuis le dépôt hmsouhaib/landscout-ai. Tu es uniquement reviewer/architecte/PO : aucune écriture Git. Lis explicitement AGENTS.md, puis les règles, l'état courant, le registre des étapes/décisions et le backlog indiqués. Vérifie le HEAD distant et les preuves du dernier verdict, sans considérer « terminé » dans un log comme une approbation indépendante. Charge ensuite les documents techniques nécessaires. Avant de proposer quoi que ce soit, restitue le but, l'état implémenté/approuvé, le ticket actif, les règles, les limites, les informations manquantes et la prochaine action autorisée. Un seul ticket Codex à la fois ; n'invente pas l'historique absent et ne passe pas à l'étape fonctionnelle suivante sans revue. Si l'accès au dépôt manque, signale-le et demande les fichiers nécessaires.

For an implementing Codex session, additionally provide the exact authorized ticket and require the same context receipt; the reviewer prompt itself authorizes no implementation or push.

The reusable [cold-start exercise](COLD_START_EXERCISE.md) tests whether this route is sufficient. Its execution status and independent acceptance remain separate from documentation publication.
