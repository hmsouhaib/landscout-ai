LANDSCOUT — DOCS.CONTINUITY.1.R16.1
Corriger les contrats de types et les preuves de tests documentés par R16
Un seul correctif documentaire. Ne pas recommencer R16. Aucun changement applicatif ni R17.
Ancrage	Valeur
Dépôt	hmsouhaib/landscout-ai
Checkout Codex	C:\souhaib\landscout-ai
Branche autorisée	recovery/docs-continuity-1-partial
HEAD de départ requis — R16	2f2dabe99825989f5fee8093dc7d5aeb129fce89
Parent R15.1 approuvé	7f00e8c29e9bb85222abb708e0fc6a45ad2ba178
Main à préserver	aa4ebc7063f2abdfcbae95154ba89b5b1a0dba02


1. Reçu fourni de revue indépendante
Reviewer : ChatGPT, lecture seule. Verdict : CORRECTION_REQUIRED — documentation R16 au SHA de départ ci-dessus.
Les lectures intégrales antérieures de l'adaptateur RTE, de ses tests et de la configuration sont réutilisées sous leurs mêmes identités de blobs. Les explications des deux compagnons R16 ont été parcourues jusqu'à leurs dernières sections de prose, avec les notices, champs, interfaces, erreurs, effets et index des scénarios. Les corps nécessaires aux constats ont été reconfrontés au Python publié. Les répétitions de code ne sont pas présentées comme une nouvelle exécution ou un deuxième audit indépendant.
Trois groupes d'écarts établis empêchent la clôture : cinq descriptions de classe/champs inventent un type int exact là où les constructeurs admettent les sous-classes hors bool ; deux descriptions de tests inventent une preuve sur les .bak, et l'une situe en plus l'échec sur la mauvaise requête ; cinq cellules omettent une suppression locale ou une modification de variable nonlocal. Les cinq notes propriétaires du premier groupe et les deux notes du deuxième reproduisent les erreurs : elles doivent être corrigées avec les compagnons.
Ces constats concernent la fidélité documentaire, pas de nouveaux défauts applicatifs. Les parties exactes sur le cache, le rollback asymétrique, les frontières de parsing, les données synthétiques, les contrôles par chemins et A-002 ne sont pas à refaire. L'approbation documentaire R15.1 et les retouches R14 restent acquises dans leur portée antérieure.
La publication R16 et son parent direct ont été lus via GitHub ; main était inchangé lors du contrôle. Le point d'accès commit présente sept chemins documentaires, mais ne fournit pas de patch exploitable pour certains grands fichiers. La revue ciblée des notes n'est ni une comparaison byte-for-byte intégrale de foundations.json, ni une certification individuelle de ses 145 notes. Aucun recalcul exhaustif des snapshots, signatures, ancres ou fichiers protégés n'est revendiqué.
Aucun pytest, import applicatif, auditeur INDEX, rendu visuel, acquisition officielle ou accès au checkout Windows n'a été exécuté par le reviewer. Le reçu R16 rapporte un candidat INDEX avec sortie native 1, completed=true, 10 204 constats, puis une complétion du reçu distincte. Ces résultats et les contrôles du disque Windows restent des exécutions rapportées, pas des résultats indépendants. L'identité octet pour octet entre le Markdown initialement émis et l'archive reçue/publiée n'est pas attestée par le reviewer ; distinguer les représentations transmises sans accuser un acteur d'une transformation non prouvée.
Le présent verdict n'attend pas la lecture de composants indépendants : il demande ce correctif précis. L'audit global demeure PARTIAL.
2. Objectif et périmètre de lecture
Rétablir l'accord entre 12 localisations de prose/cellules et le code existant, puis synchroniser les sept notes erronées identifiées, les deux bindings de compagnons et une provenance successorale compacte. Ne pas modifier le code ou les assertions pour rendre les explications vraies.
Vérifier la racine, HEAD, la branche, le suivi, l'index/worktree, les opérations Git en cours et les références serveur. Une divergence n'autorise aucun reset, changement de branche ou écrasement. En reprise interrompue de ce ticket, préserver ses changements identifiables et reprendre le premier contrôle manquant. Réutiliser les règles déjà acquises et les instructions effectivement applicables, sans nouveau chantier d'inventaire.
Lire ce ticket, le reçu R16, les 12 notices concernées, les corps correspondants et leurs véritables notes propriétaires. Les autres passages ne sont relus que pour résoudre une dépendance nécessaire. Le code complet déjà lu peut être réutilisé après vérification de son identité ; pas de réaudit général des voisins.
Identités du Python à préserver :
Fichier	Git blob
src/landscout/sources/rte_odre_fr.py	6896e2cf6e6b33189082bde9f0967b2fa55a3dd4
tests/unit/test_rte_odre_fr.py	47dba3dca3644d22fb365bb8f544e5ca21d2b3bb


3. Corrections requises
R16-REV01 — ne pas transformer isinstance en contrat de type exact
Fichier : docs/code/files/src/landscout/sources/rte_odre_fr.py.md.
Corriger exclusivement la qualification du type dans les descriptions suivantes, en conservant le reste exact :
Classe ou champ	Erreur actuelle
RteOdreDatasetMetadata.records_count	Le __post_init__ est décrit comme exigeant un « nonnegative exact int excluding bool or None ».
RteOdreExportSummary	La description de classe parle de « nonnegative exact int counts ».
RteOdreExportSummary.feature_count	Le champ est décrit comme un int exact.
RteOdreExportSummary.null_geometry_count	Même restriction de type exacte inventée.
RteOdreExportSummary.non_null_geometry_count	Même restriction de type exacte inventée.


La référence est le corps des deux __post_init__, dans la plage 145–209 du source publié. Les comptes sont contrôlés par isinstance(value, int), exclusion de bool et non-négativité, pas par type(value) is int. Décrire l'admission des sous-classes ordinaires d'int satisfaisant ces gardes. Le compte des métadonnées peut aussi être None. Conserver l'égalité entre somme des deux comptes géométriques et total, ainsi que les autres gardes réellement présentes.
Ne pas appliquer un remplacement global du mot « exact ». _metadata_from_dict applique notamment un contrôle type(records_count) is int à sa propre frontière ; _load_cached_download contrôle aussi exactement le type de file_size. Ces contrôles distincts restent documentés comme tels. Les notices de fonctions déjà exactes n'ont pas à être réécrites. Aucun durcissement de constructeur ni test de sous-classe nouveau n'est autorisé.
Dans la ligne source RTE de foundations.json, les cinq review_notes correspondantes reproduisent les formulations erronées et sont explicitement autorisées à changer. Ne pas toucher leurs signatures, plages, ancres ou états de lecture.
R16-REV02 — deux preuves de tests surestimées
Fichier : docs/code/files/tests/unit/test_rte_odre_fr.py.md, paragraphes Verified purpose des deux notices ci-dessous. Leurs notices sont réunies dans la plage documentaire 3000–3220 ; les corps sont aux lignes 517–565 du test publié.
A. test_http_failure_raises_and_cleans_temporary_files — source 517–533.
L'explication annonce « no lingering .part or .bak files ». Le test reçoit des métadonnées simulées puis un HTTPError sur l'export. Il ne vérifie que :
assert not list(tmp_path.glob("*.part"))
assert not list(tmp_path.glob("*.geojson"))
Décrire ces deux assertions exactes ; retirer la prétendue preuve d'absence des .bak. Conserver le caractère simulé du transport et le rejet attendu. Ne pas ajouter une assertion de backup au Python.
B. test_failed_refresh_preserves_previous_valid_cache — source 536–565.
L'explication dit que la requête d'export échoue et que les fichiers « part/backup » sont absents. En réalité, après expiration du cache, le test construit l'erreur avec build_rte_odre_metadata_url(...) et remplace open_safe_https par cette erreur. L'échec intervient pendant la requête de métadonnées, avant la requête d'export de ce rafraîchissement.
Décrire exactement les quatre assertions : ancienne archive conservée ; métadonnées expirées conservées ; ces métadonnées diffèrent de celles sauvegardées avant expiration ; aucun .part. Il n'existe pas d'assertion d'absence des .bak. Conserver la limite : un cache expiré préservé n'est pas devenu un cache frais valide.
Les deux review_notes du propriétaire reproduisent respectivement « .part or .bak » et « export request ... part/backup ». Les corriger avec les deux paragraphes. L'index de tests peut conserver ses liens vers ces notices ; ne pas modifier ses comptes ou les blocs d'assertions exacts, déjà corrects.
R16-REV03 — cinq cellules d'effets directs incomplètes
Même compagnon des tests, cellules In-memory mutation actuellement à None directly present.. Les noms longs ci-dessous sont relatifs au module tests.unit.test_rte_odre_fr.
Notice qualifiée	Opération à décrire
test_missing_dataset_id_fails	del config_data["datasets"]["sites"]["dataset_id"] supprime une clé du dictionnaire local chargé pour le test.
test_mutated_loaded_api_origin_is_rejected_before_metadata_network.fail_network	Le callback incrémente la variable capturée network_calls via nonlocal, avant de lever sa sentinelle s'il est appelé.
test_metadata_publication_failure_restores_previous_pair.fail_metadata_publication	Dans la branche ciblant la publication des métadonnées, le callback affecte failure_injected = True dans la portée englobante, puis lève PermissionError.
test_temporary_link_or_junction_cannot_modify_target_before_rte_network.record_network	Le callback incrémente le compteur capturé network_calls à chaque invocation, avant de retourner le flux synthétique adapté à l'URL.
test_rte_cleanup_failure_does_not_mask_double_failure_recovery_error.fail_publication_and_rollback	Dans la branche de restauration archive-backup vers primaire, affectation capturée rollback_failed = True avant l'exception. La branche d'échec de publication des métadonnées ne fait pas cette affectation.


Parages documentaires déjà inspectés : 1201–1550, 1551–1900, 3601–3950 et 5701–6051, avec les corps adjacents. Les fonctions et leurs noms qualifiés sont les clés de localisation ; ne pas remplacer arbitrairement la première cellule ressemblante.
Distinguer réaffectation d'une variable capturée et mutation de l'objet entier Python : il ne s'agit pas de rendre un int mutable. Pour les deux callbacks réseau, le test positif attend zéro appel ; documenter l'effet conditionnel du callback s'il était invoqué, pas prétendre qu'il est exécuté pendant le scénario qui réussit. Le dictionnaire local n'est pas le YAML sur disque. Aucune mutation du paramètre original n'est établie par ces opérations : conserver les cellules Direct parameter mutation correctes.
Les descriptions de purpose qui explicitent déjà ces opérations restent en place. Ne pas modifier leurs notes propriétaires exactes par automatisme. Si l'une des cinq notes manque réellement de précision sur l'opération ciblée, seule cette précision est autorisée, avec avant/après et justification ; aucun changement de notes sans lien avec ces cinq cellules.
4. Sept fichiers autorisés, historique et crédit
1. docs/code/files/src/landscout/sources/rte_odre_fr.py.md — les cinq descriptions de R16-REV01 seulement.
2. docs/code/files/tests/unit/test_rte_odre_fr.py.md — les deux purposes et cinq cellules identifiés seulement.
3. docs/code/audit/reviews/foundations.json — les deux unités RTE réelles : sept notes erronées, précision conditionnelle autorisée ci-dessus, nouveaux SHA256 des compagnons et provenance compacte r16_1_provenance.
4. docs/code/audit/R16_1_DOCUMENTATION_FIDELITY.md — nouveau reçu borné, avec emplacement réservé aux résultats INDEX.
5. docs/project/tickets/DOCS.CONTINUITY.1.R16.1.md — archive exacte du fichier de ce ticket effectivement reçu, section 1 comprise ; pas une reformulation depuis le chat.
6. docs/project/CURRENT_STATE.md — renvoi successoral court au verdict de correction et au résultat local en attente de revue.
7. docs/code/audit/DOCUMENTATION_AUDIT.md — ajout compact du correctif et de ses limites.
Conserver les états locaux antérieurs et les anciennes preuves r16_prior_evidence / r16_provenance. Ajouter séparément le verdict fourni et la correction locale, sans se déclarer approuvé. Ne pas créer de lignes propriétaires de compagnons supplémentaires : utiliser les états imbriqués existants.
Gain : zéro fichier / zéro symbole. R16 rapporte 115/245 fichiers et 3 475/4 769 symboles, reste 130/1 294. Ce correctif n'augmente pas ces totaux et ne prétend pas qu'ils ont été recomptés par le reviewer. Conserver le dénominateur historique distinct de l'inventaire courant.
Tous les autres fichiers restent inchangés : Python, tests, configurations, dépendances/lock, auditeur, autres compagnons/fragments, coverage.json, matrice, backlog, anciennes archives et reçus R16/R15.1/R15/R14. Ne pas réécrire l'archive R16 pour masquer une différence de représentation. Le nouveau reçu identifie la représentation de R16.1 effectivement reçue et son hash externe ; ne pas assimiler un texte collé linéarisé à des octets Markdown non disponibles.
Conserver A-001..A-004, OPEN R5-D01, les limites R16 et antérieures, rendu/cold-start/global/EP et les lacunes de reçus. Aucune correction d'A-002, politique EP, score, capacité électrique, accès légal ou autre évolution fonctionnelle. Dernière frontière fonctionnelle approuvée consignée : 7F.1B.4.
5. Contrôles bornés
A. Statique, sans import applicatif ni pytest
Utiliser l'environnement existant. Des scripts temporaires hors dépôt peuvent comparer texte/AST/JSON/octet et liens. Vérifier les 12 localisations et les sept notes, la correspondance avec les vrais corps, les nouveaux fingerprints et la provenance. Comparer le delta au HEAD de départ : tout autre paragraphe, code répété, snapshot, signature, ancre, plage et état doit rester inchangé hors provenance autorisée.
Vérifier JSON strict, Unicode, tableaux/fences et liens affectés, exactitude de l'archive réellement reçue, git diff --check, les 106 fichiers protégés contre leurs bases et tous les chemins initialement suivis hors des sept autorisés. Recompter ce dernier ensemble, ne pas recycler un nombre d'un ancien ticket. Conserver les deux exceptions EOL et treize observations whitespace historiques ; ne pas normaliser globalement.
Distinguer Git-content, index et checkout. Ne pas annoncer un rendu visuel à partir d'un contrôle syntaxique. Ne pas convertir une revue de prose en exécution de code. Aucun pytest, import applicatif, téléchargement RTE/IGN/EP, installation ou changement de sécurité.
B. Une seule exécution du candidat INDEX avec l'auditeur inchangé
Relire et stager explicitement les seuls chemins autorisés réellement modifiés, reçu avec emplacement de résultat encore réservé. Capturer le manifeste candidat exact, trié path/mode/OID, puis exécuter une seule fois :
.venv\Scripts\python.exe -B -X utf8 tools/audit_documentation.py --check --progress > C:\souhaib\r16-1-candidate.stdout.txt 2> C:\souhaib\r16-1-candidate.stderr.txt
$code = $LASTEXITCODE
Préserver toute preuve préexistante ; en reprise, réutiliser le run terminé identifié, sans l'écraser. Si ces noms sont déjà occupés par d'autres preuves, choisir avant le run un suffixe unique et consigner les chemins effectifs.
Enregistrer sortie native, completed, nombre réel et qualification des constats. exit 1 / completed=true n'est pas vert ; sortie 2 ou interruption n'est pas une exécution terminée. Ne pas toucher l'auditeur, ses exclusions ou le registre global pour réduire les constats.
Comparer avec les vrais logs/manifeste du candidat R16 seulement s'ils sont disponibles et identifiés. Les 10 204 constats rapportés ne sont ni une cible ni le total du commit final. Classer le delta et les diagnostics affectant les corrections ; les constats partagés ne sont pas tous bénins. Indisponibilité des logs : la signaler, pas inventer une comparaison.
Après le run, ne compléter que l'emplacement réservé au résultat dans le nouveau reçu. Vérifier le delta exact de ce reçu et l'identité de tous les autres OID du candidat. Garder les preuves hors Git. Pas de second auditeur de façade, de self-hash circulaire, de SHA futur ou de total présenté comme audité sur le commit final.
6. Critères de fin, publication et arrêt
Le correctif est localement terminé lorsque les 12 descriptions/cellules et leurs notes ciblées sont fidèles, les autres contenus sont préservés, les deux bindings sont exacts et le candidat INDEX a terminé avec ses réserves correctement qualifiées. Toute autre anomalie hors périmètre est signalée, pas réparée silencieusement.
Rapport demandé : corrections avant/après par REV ; notes modifiées ou conservées ; preuves de préservation ; contrôles statiques ; run INDEX et distinction candidat/reçu final ; zéro crédit ; SHA et état réel de publication.
Aucun reset/restore/clean/stash/rebase/amend/squash/merge/force-push, suppression de sauvegardes ou modification d'ACL/sécurité. Une exception safe.directory n'est permise que par commande, sur le chemin exact, après erreur effectivement diagnostiquée ; jamais confiance persistante ou wildcard.
Après réussite des contrôles bornés et qualification de l'audit global PARTIAL :
# Staging explicite des seuls chemins modifiés de la section 4, chacun nommé.
# Aucun git add . / -A, commit -a, fichier applicatif ou merge vers main.
git commit -m "docs: correct RTE reference contracts and test evidence"
git push origin recovery/docs-continuity-1-partial
Vérifier le vrai SHA publié, index/worktree propres, suivi/serveur concordants et main local/suivi/serveur inchangé. En cas d'échec, préserver le travail et rapporter le résultat, sans contournement destructif.
Statut local final : DOCS.CONTINUITY.1.R16.1 completed — documentary correction only; global audit PARTIAL; independent review pending. Puis STOP pour revue. Codex ne s'accorde pas l'approbation R16/R16.1 et n'enchaîne pas R17. Souhaib transmettra la publication au reviewer.