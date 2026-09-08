# EP 07/2026 — Référence sémantique liée à la source

STEP 7F.1C.1 — dossier de recherche en français, consulté le 8 septembre 2026.

Statut : `RESEARCH_DRAFT_NOT_RUNTIME_POLICY`. Ce dossier et le [JSON associé](inpn_ep_2026_07_semantic_reference.json) sont destinés à la revue indépendante. Aucun code de production ne lit ce JSON. Ni cartographie sémantique opérationnelle ni politique approuvée.

## 1. Périmètre et méthode

Seuls `type_espace`, `statut` et `objectif_protection` sont inventoriés. Les valeurs viennent exclusivement de `bundle.attributes`, après construction par les fonctions publiques approuvées et validation publique physique indépendante du bundle. Le cache EP existant a été utilisé ; aucune nouvelle archive EP, Natura 2000 ou ZNIEFF n’a été téléchargée. Aucun lecteur supplémentaire, aucune table normalisée, aucune jointure attributs/géométrie n’a été ajouté.

Chaque chaîne est conservée entière et exactement : casse, accents, virgules, parenthèses et apostrophes ne sont ni corrigés ni interprétés comme une grammaire de listes. `Nature` et `nature` restent deux valeurs. NULL est séparé du texte vide. Les distributions sont marginales : elles ne prouvent aucune cooccurrence entre les trois champs. Aucune ligne n’a été relue pour construire un croisement de catégories.

Les définitions ci-dessous décrivent uniquement le contexte des documents cités, parfois un exemple local ou historique. Elles ne prouvent pas une correspondance du champ, de la valeur et du snapshot. Un `statut` nul n’établit aucune absence de protection. `objectif_protection` n’est pas un indicateur de faisabilité BESS. Aucune permission, exclusion, note, hiérarchie de risque ou conclusion juridique indépendante du lieu n’est produite.

## 2. Source figée et chaîne de preuve

| Liaison | Valeur exacte |
|---|---|
| `aligned_layer_count` | `15` |
| `archive_filename` | `EP.zip` |
| `archive_sha256` | `73688bc37205a5e7f59e2065a0b81fc8cf2a242bdec5d7d2786f083671c4abe5` |
| `archive_size` | `99835011` |
| `archive_url` | `https://assets.patrinat.fr/files/donnees/ep/EP.zip` |
| `attribute_profile_schema_version` | `1` |
| `attribute_profile_sha256` | `c0bfb73643f2143bd050a7b3f6f59e7ddb52cbcd0efe8612cc45adbc8bc254e8` |
| `authority` | `MNHN` |
| `catalog_schema_version` | `2` |
| `catalog_sha256` | `ba1b9be89d6b951a5c3b5d6b54d1c42f14e0c7bc6669079b1944ff2ffd4c6b34` |
| `dataset_id` | `EP` |
| `dataset_name` | `Base de référence des espaces protégés français` |
| `declared_version` | `07/2026` |
| `evidence_bundle_schema_version` | `1` |
| `evidence_bundle_sha256` | `a558236c6a246999fca83ac10c443cd686807675327cdab2da5405143db56016` |
| `geometry_profile_schema_version` | `1` |
| `geometry_profile_sha256` | `997c8c27cbbedb2860778386b3f2eb5afa9f64de6ad07e41fc67b4cec9060ee7` |
| `matched_fid_count` | `11381` |
| `package_count` | `15` |
| `program` | `INPN` |
| `provider` | `PatriNat` |
| `python_version` | `3.12.13 (main, Jul 18 2026, 17:08:38) [MSC v.1944 64 bit (AMD64)]` |
| `reference_page_url` | `https://www.patrinat.fr/fr/page-temporaire-de-telechargement-des-referentiels-de-donnees-lies-linpn-7353` |
| Outil : `gdal_version` | `3.12.4` |
| Outil : `geos_version` | `3.13.1` |
| Outil : `pyogrio_version` | `0.13.0` |
| Outil : `pyproj_version` | `3.7.2` |
| Outil : `shapely_version` | `2.1.2` |
| Outil : `sqlite_version` | `3.53.1` |

Les quatre schémas techniques et leurs SHA restent inchangés. Les 15 packages, 15 couches alignées et 11 381 FID physiques sont vérifiés, pas estimés. La cohérence CRS/coordonnées de `EP/sig_tadl.gpkg` reste non résolue ; aucun sens de catégorie ne la corrige.

## 3. Domaines observés et couverture

| Champ | Couches | Lignes | NULL | Non-NULL | Valeurs distinctes non-NULL |
|---|---:|---:|---:|---:|---:|
| `type_espace` | 15 | 11381 | 0 | 11381 | 61 |
| `statut` | 15 | 11381 | 11381 | 0 | 0 |
| `objectif_protection` | 15 | 11381 | 2015 | 9366 | 3 |

Le domaine non nul de `statut` est vide : aucune entrée artificielle n’est créée pour NULL. Les trois valeurs d’`objectif_protection` sont `Géologie` (263), `Nature` (8813), `nature` (290), avec 2015 NULL. Aucune chaîne vide n’est observée dans ces trois domaines ; cela ne définit pas le sens d’une chaîne vide éventuelle.

| Champ | CONFIRMED_FOR_SNAPSHOT | OFFICIAL_CONTEXT_ONLY | UNRESOLVED | CONFLICTING_EVIDENCE |
|---|---:|---:|---:|---:|
| `type_espace` | 0 | 55 | 6 | 0 |
| `statut` | 0 | 0 | 0 | 0 |
| `objectif_protection` | 0 | 2 | 1 | 0 |

Couverture des valeurs observées : **64/64 (100 %)**. Correspondances de sens confirmées pour le snapshot : **0/64 (0 %)**. L’applicabilité au snapshot demeure `UNRESOLVED` pour les 64 entrées et les trois champs. Le conflit de chronologie CNIG est une question documentaire distincte, non un état juridique des objets EP.

## 4. Définitions des champs et correspondance export/standard

La page producteur annonce EP 07/2026 ; son annonce d’août décrit des GeoPackages territoriaux avec attributs intégrés et une conformité générale CNIG ENP, sans édition ni correspondance des trois colonnes. Il serait donc faux d’affirmer que le producteur ne mentionne aucun standard. Ce lien général n’établit toutefois **aucune correspondance exacte export → champ/valeur/édition**. Voir [pat_ep_download](#doc-pat_ep_download) et [pat_ep_release](#doc-pat_ep_release).

### `type_espace`

État de recherche : `UNRESOLVED`. Applicabilité au snapshot : `UNRESOLVED`.

Définition / limite : Le sens exact de la colonne de l'export n'est pas établi par les standards consultés ; ceux-ci fournissent seulement un contexte de catégories de protection.

- [pat_ep_release](#doc-pat_ep_release), Contenu du dépôt : Annonce une conformité CNIG générale non versionnée. Limite : Ne nomme ni ne définit cette colonne exacte de l’export.

- [covadis_2013_odt](#doc-covadis_2013_odt), content.xml / Tableau2 et Tableau46 ; PDF associé p. 21-27 : Le modèle utilise reseau et la liste extensible TypeEspaceNaturelProtege. Limite : Ne démontre pas que type_espace est leur représentation dans l'export.

- [covadis_2013_pdf](#doc-covadis_2013_pdf), p. 49 : table Mapinfo N_ENP_PN_S_ddd : CODE_R_ENP distingue CPN et AAPN pour cette table. Limite : Ce nom physique diffère de la colonne EP étudiée.

- [cnig_enp_draft_pdf](#doc-cnig_enp_draft_pdf), p. 15 et 20-24 : TypeENP : Le projet emploie TypeENP et une nomenclature numérique. Limite : Aucun lien établi avec les libellés de type_espace dans EP.

- Question : Quelle spécification du producteur définit la colonne et sa liste de valeurs pour ce millésime ?

### `statut`

État de recherche : `UNRESOLVED`. Applicabilité au snapshot : `UNRESOLVED`.

Définition / limite : Colonne entièrement nulle dans le domaine observé ; aucune signification d'absence de protection ou de validité ne peut être déduite.

- [pat_ep_release](#doc-pat_ep_release), Contenu du dépôt : Annonce une conformité CNIG générale non versionnée. Limite : Ne nomme ni ne définit cette colonne exacte de l’export.

- [cnig_enp_draft_pdf](#doc-cnig_enp_draft_pdf), p. 15 et 19 : StatutENP ; p. 24-25 : Le projet renvoie StatutENP à la nomenclature SANDRE 390. Limite : Ne permet pas de décoder les nulls de statut dans EP.

- [sandre_390](#doc-sandre_390), Informations ; table des éléments : Décrit la validation de nomenclatures et d'éléments de référence. Limite : N'est pas une preuve du régime de protection d'un espace EP.

Domaine documentaire candidat, **non domaine EP ni règle de décodage** : `Gelé`, `Proposition`, `Provisoire`, `Validé`.

- Question : Quel contrat d'export explique statut et sa nullité systématique ?

- Question : Aucune correspondance de cette colonne n'a été démontrée dans le modèle historique inspecté.

### `objectif_protection`

État de recherche : `UNRESOLVED`. Applicabilité au snapshot : `UNRESOLVED`.

Définition / limite : Les standards décrivent des finalités de conservation ; le lien exact avec la colonne EP et ses variantes de casse reste à établir, sans signification de faisabilité BESS.

- [pat_ep_release](#doc-pat_ep_release), Contenu du dépôt : Annonce une conformité CNIG générale non versionnée. Limite : Ne nomme ni ne définit cette colonne exacte de l’export.

- [covadis_2013_odt](#doc-covadis_2013_odt), content.xml / Tableau12 et Tableau19 ; PDF associé p. 15 et 28 : objectifProtection est une classification de finalités ; plusieurs objectifs sont possibles. Limite : Ne définit ni la colonne snake_case ni sa syntaxe de valeurs.

- [covadis_2013_pdf](#doc-covadis_2013_pdf), p. 50 : P1_NATURE à P12_AUTRE : L'implémentation Mapinfo décrit des indicateurs distincts N/T/F. Limite : Ne prouve pas une chaîne composée ni un séparateur dans EP.

- [cnig_enp_draft_pdf](#doc-cnig_enp_draft_pdf), p. 15 et 24 : ObjectifProtectionENP : Le projet liste quatre motifs codés : Nature, Culture, Paysage, Géologie. Limite : Ni cette enumération ni les ressemblances textuelles ne prouvent le contrat EP.

- Question : Quelle source producteur relie cette colonne aux objectifs documentés ?

- Question : Nature et nature sont deux valeurs exactes distinctes ; aucune équivalence de casse n'est établie.

## 5. Registre des documents primaires

Les dates absentes restent non établies. Les dates de version, de mise en ligne et de mise à jour ne sont pas interchangeables. Une norme historique validée, une consultation close, une page institutionnelle actuelle et une notice historique ont des portées distinctes. Les liens ci-dessous sont les URL exactes ; les échecs d’accès restent signalés. Les seules empreintes documentaires sont celles des deux PDF et de l’ODT réellement obtenus hors Git.

Limite de consultation PDF : les textes ont été extraits proprement ; les cellules XML des tableaux de l’ODT officiel 2013 ont été vérifiées. Aucun examen visuel des PDF n’a été accompli : outil de rendu indisponible et tentative Windows bloquée par la politique de scripts, sans contournement ni modification de sécurité. Les tables du projet restent du contexte textuel non confirmé pour le snapshot.

<a id="doc-pat_ep_download"></a>

### pat_ep_download — Page temporaire de téléchargement des référentiels de données liés à l'INPN

[Page temporaire de téléchargement des référentiels de données liés à l'INPN](https://www.patrinat.fr/fr/page-temporaire-de-telechargement-des-referentiels-de-donnees-lies-linpn-7353) — PatriNat.

Statut documentaire : `PRODUCER_PUBLICATION`. Version : non établie. Publication : 2025-08-11T18:02. Mise à jour : 2026-08-04T10:49. Consultation : 2026-09-08.

Localisateurs : Tableau Référentiel / Description / Version / Lien — ligne EP.

- Limite : La page annonce EP 07/2026 et son lien ; elle ne décrit pas les trois champs ni l’empreinte de l’archive.

- Limite : Fuseau horaire des dates affichées non indiqué ; aucun SHA de page HTML déclaré.

<a id="doc-pat_ep_release"></a>

### pat_ep_release — Espaces protégés : la base de données nationale actualisée est disponible !

[Espaces protégés : la base de données nationale actualisée est disponible !](https://www.patrinat.fr/fr/actualites/espaces-proteges-la-base-de-donnees-nationale-actualisee-est-disponible-7417) — PatriNat.

Statut documentaire : `PRODUCER_RELEASE_NOTICE`. Version : non établie. Publication : 2026-08-03T12:03. Mise à jour : 2026-08-03T14:01. Consultation : 2026-09-08.

Localisateurs : Contenu du dépôt ; Actualisation des données.

- Limite : Conformité générale au standard CNIG ENP annoncée sans édition ; aucune correspondance des trois noms physiques et valeurs n’est fournie. Page lue via son lien publié sur le site ; une ouverture directe par le service web a échoué.

- Limite : Fuseau horaire des dates affichées non indiqué ; aucun SHA de page HTML déclaré.

<a id="doc-pat_ep_program"></a>

### pat_ep_program — Espaces protégés

[Espaces protégés](https://www.patrinat.fr/fr/espaces-proteges-6069) — PatriNat.

Statut documentaire : `PRODUCER_PROGRAM_CONTEXT`. Version : non établie. Publication : 2018-07-18T14:00. Mise à jour : 2025-01-27T15:39. Consultation : 2026-09-08.

Localisateurs : Présentation ; Missions de PatriNat — Gestion de la base de données Espaces protégés.

- Limite : Contexte institutionnel, pas dictionnaire de l’export figé.

- Limite : Fuseau horaire des dates affichées non indiqué ; aucun SHA de page HTML déclaré.

<a id="doc-pat_standards"></a>

### pat_standards — Standards d'échange de données

[Standards d'échange de données](https://www.patrinat.fr/fr/standards-dechange-de-donnees-6229) — PatriNat.

Statut documentaire : `PRODUCER_PROGRAM_CONTEXT`. Version : non établie. Publication : 2018-08-31T14:13. Mise à jour : 2025-01-23T11:43. Consultation : 2026-09-08.

Localisateurs : Présentation ; Missions de PatriNat.

- Limite : Mission générale de standardisation ; pas définition des champs EP.

- Limite : Fuseau horaire des dates affichées non indiqué ; aucun SHA de page HTML déclaré.

<a id="doc-inpn_reference_unavailable"></a>

### inpn_reference_unavailable — Titre non établi : source inaccessible

[inpn_reference_unavailable](https://inpn.mnhn.fr/referentiels-donnees) — INPN / MNHN.

Statut documentaire : `INACCESSIBLE_HTTP_403`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : non disponibles — source inaccessible.

- Limite : 403 Forbidden ; aucun contournement.

<a id="doc-inpn_program_unavailable"></a>

### inpn_program_unavailable — Titre non établi : source inaccessible

[inpn_program_unavailable](https://inpn.mnhn.fr/programme/espaces-proteges/presentation) — INPN / MNHN.

Statut documentaire : `INACCESSIBLE_HTTP_403`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : non disponibles — source inaccessible.

- Limite : 403 Forbidden ; aucun contournement.

<a id="doc-sinp_standards_unavailable"></a>

### sinp_standards_unavailable — Titre non établi : source inaccessible

[sinp_standards_unavailable](https://standards-sinp.mnhn.fr/) — SINP / MNHN.

Statut documentaire : `INACCESSIBLE_CACHE_MISS`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : non disponibles — source inaccessible.

- Limite : Le service de consultation retourne Cache miss ; aucun contenu retenu comme preuve.

<a id="doc-inpn_rnn_2022_indexed"></a>

### inpn_rnn_2022_indexed — Base de données nationale Espaces Protégés — Réserves naturelles Nationales + Périmètre de protection de réserve naturelle nationale

[Base de données nationale Espaces Protégés — Réserves naturelles Nationales + Périmètre de protection de réserve naturelle nationale](https://inpn.mnhn.fr/docs/map_pdf/rnn_f.pdf) — PatriNat / INPN.

Statut documentaire : `HISTORICAL_INDEXED_TEXT_ONLY`. Version : Mars 2022 ; date de référence indexée 2022-03-15. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Fiche métropolitaine shapefile/MapInfo — texte indexé.

- Limite : Octets PDF non obtenus ; capture visuelle Cache miss. Ne prouve pas l’export GeoPackage 07/2026.

<a id="doc-covadis_2013_page"></a>

### covadis_2013_page — Géostandard Espaces naturels protégés (ENP) v1.0

[Géostandard Espaces naturels protégés (ENP) v1.0](https://cnig.gouv.fr/geostandard-espaces-naturels-proteges-enp-v1-0-a28820.html) — CNIG / COVADIS.

Statut documentaire : `ADOPTED_HISTORICAL_EXCHANGE_STANDARD`. Version : 1.0. Publication : 2013-04-18. Mise à jour : 2017-09-14. Consultation : 2026-09-08.

Localisateurs : Résumé ; Standard de données validé ; Tables prêtes à l'emploi.

La page atteste la validation COVADIS du 27 mars 2013 et présente un format d'échange vers le MNHN, sans identifier le générateur d'EP 07/2026.

<a id="doc-covadis_2013_pdf"></a>

### covadis_2013_pdf — Standard de données COVADIS — Espaces naturels protégés

[Standard de données COVADIS — Espaces naturels protégés](https://cnig.gouv.fr/IMG/pdf/COVADIS_standard_ENP_v1-0_cle29bee6.pdf) — COVADIS ; hébergement officiel CNIG.

Statut documentaire : `ADOPTED_HISTORICAL_EXCHANGE_STANDARD`. Version : 1.0 — 27 mars 2013. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : p. 1 et 3 : version/date ; p. 15 : modes de classement ; p. 21-27 : réseau et liste codée ; p. 28 : objectifProtection ; p. 49-50 : implémentation Mapinfo.

Le 27 mars 2013 est la date imprimée de version et de validation, pas une date distincte de mise en ligne établie pour ce fichier.

Octets obtenus : 1510383. SHA256 : `0ee84a1b1db75d705bfea15054598231bdd334ce06dbbf39277d6765ec0d3a3d`.

- Limite : PDF obtenu par HTTPS et texte extrait ; examen visuel non réalisé faute de moteur disponible sans modification de l'environnement.

- Limite : Les réponses du service web ont parfois été une page de maintenance ou un délai dépassé ; aucune restriction n'a été contournée.

<a id="doc-covadis_2013_odt"></a>

### covadis_2013_odt — Standard de données COVADIS — Espaces naturels protégés (ODT associé)

[Standard de données COVADIS — Espaces naturels protégés (ODT associé)](https://cnig.gouv.fr/IMG/odt/COVADIS_standard_ENP_v1-0_cle29bee6.odt) — COVADIS ; hébergement officiel CNIG.

Statut documentaire : `OFFICIAL_EDITABLE_REPRESENTATION_OF_HISTORICAL_STANDARD`. Version : 1.0 — 27 mars 2013. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : content.xml / Tableau12 ; content.xml / Tableau4 ; content.xml / Tableau2 ; content.xml / Tableau46 ; content.xml / Tableau19.

Représentation liée à côté du PDF sur la page officielle ; regroupement des cellules vérifié indépendamment de l'extraction PDF.

Octets obtenus : 1180745. SHA256 : `8ce638ab7ef150be4f8614a2700bdd6b211fe725bfab2ec82ebd076f184d3b29`.

- Limite : Cellules XML des tableaux inspectées ; ce contrôle structurel n'est pas un examen visuel du PDF.

<a id="doc-cnig_2026_consultation"></a>

### cnig_2026_consultation — Appel à commentaires : projet de révision du standard d'échange de données relatives aux Espaces naturels protégés (ENP)

[Appel à commentaires : projet de révision du standard d'échange de données relatives aux Espaces naturels protégés (ENP)](https://cnig.gouv.fr/appel-a-commentaires-projet-de-revision-du-a30149.html) — CNIG.

Statut documentaire : `CONSULTATION_CLOSED_PROJECT`. Version : non établie. Publication : 2026-05-11. Mise à jour : 2026-06-22. Consultation : 2026-09-08.

Localisateurs : Titre, statut et dates ; Période ; Projet de standard pour l'appel à commentaires.

Consultation du 11 mai au 14 juin 2026, affichée close. La clôture ne prouve pas une adoption.

- Limite : Le service web renvoyait parfois une maintenance ; une requête HTTPS ordinaire a permis de lire le titre, les dates, le statut et le lien officiel.

<a id="doc-cnig_enp_draft_pdf"></a>

### cnig_enp_draft_pdf — Standard Espace Naturel Protégé (ENP)

[Standard Espace Naturel Protégé (ENP)](https://cnig.gouv.fr/IMG/pdf/cnig_caret_standard_enp_1beta0.pdf) — CNIG ; PatriNat, SIB, CARET.

Statut documentaire : `CONSULTATION_DRAFT_WITH_CONFLICTING_CHRONOLOGY`. Version : 1bêta0 — 27/06/2025. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : p. 1-2 : version et statut ; p. 4, § 2.1 : chronologie ; p. 15 : attributs ENP ; p. 19 : listes de valeurs ; p. 20-24 : TypeENP ; p. 24 : ObjectifProtectionENP ; p. 24-25 : StatutENP.

La p. 2 marque projet et consultation, mais la p. 4 affirme une validation plénière le 5 juin 2025. Cette contradiction ne permet pas de conclure à l'adoption.

Octets obtenus : 2756919. SHA256 : `60cdba0d8411d5875ad1f0148223f1b66d91ba52725a7b30d9af3224836e1c51`.

- Limite : Texte du PDF obtenu directement ; contrôle visuel indisponible sans modifier l'environnement.

- Limite : Pas de procès-verbal indépendant établissant une adoption trouvé dans la recherche bornée.

<a id="doc-cnig_enp_gt"></a>

### cnig_enp_gt — GT Espaces Naturels Protégés

[GT Espaces Naturels Protégés](https://cnig.gouv.fr/gt-espaces-naturels-proteges-a26277.html) — CNIG.

Statut documentaire : `WORKING_GROUP_CONSULTATION_PAGE`. Version : non établie. Publication : 2024-09-27. Mise à jour : 2026-05-11. Consultation : 2026-09-08.

Localisateurs : Mandat du GT ; Appel à commentaire.

Corrobore le calendrier de consultation et le lien vers le même projet, sans preuve d'adoption ni d'application à l'export.

<a id="doc-cnig_standards_register"></a>

### cnig_standards_register — Les Standards CNIG

[Les Standards CNIG](https://cnig.gouv.fr/les-standards-cnig-a18959.html) — CNIG.

Statut documentaire : `OFFICIAL_REGISTER_ENP_WORK_IN_PROGRESS`. Version : non établie. Publication : 2022-04-05. Mise à jour : 2026-07-07. Consultation : 2026-09-08.

Localisateurs : Introduction ; Travaux en cours / Biodiversité / standard Espaces naturels protégés.

La ligne ENP reste dans les travaux en cours. Cette observation n'est pas une preuve d'absence universelle de décision ultérieure.

- Limite : Le tableau porte aussi une mention de mise à jour au 21 mars 2025 ; sa fraîcheur exhaustive n'est pas démontrée.

<a id="doc-sandre_390"></a>

### sandre_390 — Statut de validation — Référentiels — Nomenclatures

[Statut de validation — Référentiels — Nomenclatures](https://id.eaufrance.fr/nsa/390) — SANDRE / Eaufrance ; contribution Office International de l'Eau.

Statut documentaire : `VALIDATED_REFERENCE_NOMENCLATURE`. Version : Nomenclature 390. Publication : non établie. Mise à jour : 2010-07-23. Consultation : 2026-09-08.

Localisateurs : Informations ; Table des éléments.

Création indiquée au 12 juillet 2004 ; la date de mise à jour concerne la nomenclature, pas nécessairement la page web. Le statut de chaque élément est distinct de son libellé.

<a id="doc-unesco_mab_zonation"></a>

### unesco_mab_zonation — What are biosphere reserves?

[What are biosphere reserves?](https://www.unesco.org/en/mab/wnbr/about) — UNESCO — Man and the Biosphere Programme.

Statut documentaire : `OFFICIAL_PROGRAMME_CONTEXT_WEBPAGE`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Introduction ; The three functions are pursued through an appropriate zonation ; Core area(s) ; Buffer zone(s) ; Transition area(s).

<a id="doc-unesco_world_heritage_convention"></a>

### unesco_world_heritage_convention — Convention Concerning the Protection of the World Cultural and Natural Heritage

[Convention Concerning the Protection of the World Cultural and Natural Heritage](https://whc.unesco.org/en/conventiontext/) — UNESCO — World Heritage Centre.

Statut documentaire : `OFFICIAL_TEXT_OF_ADOPTED_CONVENTION`. Version : Convention adoptée le 16 novembre 1972. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Préambule, date d'adoption ; Articles 1 et 2 ; Article 11.2.

<a id="doc-unesco_geoparks_about"></a>

### unesco_geoparks_about — UNESCO Global Geoparks

[UNESCO Global Geoparks](https://www.unesco.org/en/iggp/geoparks/about) — UNESCO — International Geoscience and Geoparks Programme.

Statut documentaire : `OFFICIAL_PROGRAMME_CONTEXT_WEBPAGE`. Version : non établie. Publication : non établie. Mise à jour : 2026-08-20. Consultation : 2026-09-08.

Localisateurs : What is a UNESCO Global Geopark? ; UNESCO designated sites ; Sustainable development ; Geoconservation.

- Limite : La mise à jour affichée est postérieure au millésime EP 07/2026.

<a id="doc-spa_rac_spami"></a>

### spa_rac_spami — Specially Protected Areas of Mediterranean Importance

[Specially Protected Areas of Mediterranean Importance](https://spa-rac.org/en/themes/specially-protected-areas-of-mediterranean-importance/) — SPA/RAC — Convention de Barcelone / Plan d'action pour la Méditerranée.

Statut documentaire : `OFFICIAL_PROGRAMME_CONTEXT_WEBPAGE`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Overview ; Objectives and criteria of SPAMIs ; The SPAMI List.

<a id="doc-ospar_mpa"></a>

### ospar_mpa — Marine Protected Areas

[Marine Protected Areas](https://www.ospar.org/work-areas/bdc/marine-protected-areas) — OSPAR Commission.

Statut documentaire : `OFFICIAL_PROGRAMME_CONTEXT_WEBPAGE`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Définition introductive ; Objectifs du réseau ; Paragraphe sur les sites proposés ou désignés.

<a id="doc-unep_cep_spaw_areas"></a>

### unep_cep_spaw_areas — Protected areas in the wider Caribbean Region

[Protected areas in the wider Caribbean Region](https://www.unep.org/cep/protected-areas-wider-caribbean-region) — PNUE — Caribbean Environment Programme / Secrétariat de la Convention de Carthagène.

Statut documentaire : `OFFICIAL_PROGRAMME_CONTEXT_WEBPAGE`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Strengthening and Management of Protected Areas in the Wider Caribbean Region ; Guidelines.

- Limite : Les effectifs courants diffèrent entre pages PNUE ; ils ne sont pas utilisés comme preuve des effectifs EP.

<a id="doc-unep_cep_spaw_overview"></a>

### unep_cep_spaw_overview — Specially Protected Areas and Wildlife (SPAW)

[Specially Protected Areas and Wildlife (SPAW)](https://www.unep.org/cep/what-we-do/specially-protected-areas-and-wildlife-spaw) — PNUE — Caribbean Environment Programme.

Statut documentaire : `OFFICIAL_PROGRAMME_CONTEXT_WEBPAGE`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : What is the SPAW Protocol?.

- Limite : La mention May 2021 accompagne le graphique de ratification ; elle n'est pas assimilée à une mise à jour de toute la page.

<a id="doc-ats_protected_areas"></a>

### ats_protected_areas — Area Protection and Management / Historic Sites and Monuments

[Area Protection and Management / Historic Sites and Monuments](https://www.ats.aq/e/protected.html) — Secrétariat du Traité sur l'Antarctique.

Statut documentaire : `OFFICIAL_TREATY_CONTEXT_WEBPAGE`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Premier paragraphe : Annexe V ; Deuxième paragraphe : ASPA et ASMA.

<a id="doc-ramsar_designation"></a>

### ramsar_designation — Designating Ramsar Sites

[Designating Ramsar Sites](https://www.ramsar.org/our-work/wetlands-international-importance/designating-ramsar-sites) — Secrétariat de la Convention sur les zones humides.

Statut documentaire : `OFFICIAL_WEBPAGE_INDEXED_CONTEXT_ONLY`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Texte indexé : processus de désignation et articles 2.1-2.2.

- Limite : Ouverture directe : HTTP 403. Seul le texte indexé de la page officielle a été consulté ; aucune restriction contournée.

<a id="doc-sprep_apia_history"></a>

### sprep_apia_history — SPREP Meetings

[SPREP Meetings](https://www.sprep.org/governance/meetings) — SPREP — Secretariat of the Pacific Regional Environment Programme.

Statut documentaire : `OFFICIAL_HISTORY_INDEXED_CONTEXT_ONLY`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Tableau historique indexé : année 2006.

- Limite : Ouverture directe : HTTP 403. Mention de suspension consultée dans le texte indexé de la source officielle ; aucun contournement.

<a id="doc-sprep_convention_status_2017"></a>

### sprep_convention_status_2017 — Status as at July 2017 of the Apia, Noumea (or SPREP) and Waigani Conventions, for which SPREP is the Secretariat

[Status as at July 2017 of the Apia, Noumea (or SPREP) and Waigani Conventions, for which SPREP is the Secretariat](https://www.sprep.org/attachments/Publications/Corporate_Documents/parties-regional-convention-july-2017.pdf) — SPREP.

Statut documentaire : `HISTORICAL_OFFICIAL_DOCUMENT_INDEXED_ONLY`. Version : État de juillet 2017. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Première page indexée : Apia Convention.

- Limite : Document non téléchargé et non examiné visuellement ; aucun SHA256 revendiqué.

- Limite : L'état historique indiqué n'établit pas à lui seul la situation de juillet 2026.

<a id="doc-fr_ministry_areas"></a>

### fr_ministry_areas — Aires protégées en France

[Aires protégées en France](https://www.ecologie.gouv.fr/politiques-publiques/aires-protegees-france) — Ministère chargé de la transition écologique.

Statut documentaire : `OFFICIAL_CURRENT_CONTEXT`. Version : non établie. Publication : 2019-09-27. Mise à jour : 2026-03-13. Consultation : 2026-09-08.

Localisateurs : Parcs naturels marins ; Parcs naturels régionaux ; Réserves naturelles ; Réserves biologiques ; Arrêtés préfectoraux de protection.

- Limite : Les chiffres datés de 2022 de cette page ne sont pas utilisés comme inventaire EP 07/2026.

<a id="doc-fr_ministry_sites"></a>

### fr_ministry_sites — Politique des sites

[Politique des sites](https://www.ecologie.gouv.fr/politiques-publiques/politique-sites) — Ministère chargé des sites.

Statut documentaire : `OFFICIAL_CURRENT_CONTEXT`. Version : non établie. Publication : 2016-11-15. Mise à jour : 2026-08-05. Consultation : 2026-09-08.

Localisateurs : Les sites classés ; La démarche Grand Site de France ; Le label Grand Site de France.

- Limite : Page mise à jour après juillet 2026 : contexte actuel, non dictionnaire de cet export.

<a id="doc-fr_sdes_parks_2021"></a>

### fr_sdes_parks_2021 — Les parcs nationaux de France — Glossaire

[Les parcs nationaux de France — Glossaire](https://www.statistiques.developpement-durable.gouv.fr/edition-numerique/parcs-nationaux/57-glossaire) — SDES / ministère chargé de la transition écologique.

Statut documentaire : `OFFICIAL_HISTORICAL_CONTEXT`. Version : Édition 2021. Publication : 2021-06. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Aire d’adhésion ; Cœur de parc national.

<a id="doc-fr_ofb_reserves"></a>

### fr_ofb_reserves — Les réserves gérées ou co-gérées par l'Office français de la biodiversité

[Les réserves gérées ou co-gérées par l'Office français de la biodiversité](https://ofb.gouv.fr/les-reserves) — Office français de la biodiversité.

Statut documentaire : `OFFICIAL_CURRENT_CONTEXT`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Les réserves naturelles nationales ; Les réserves nationales de chasse et de faune sauvage.

<a id="doc-fr_cdl_missions"></a>

### fr_cdl_missions — Le conservatoire

[Le conservatoire](https://www.conservatoire-du-littoral.fr/3-le-conservatoire.htm) — Conservatoire du littoral.

Statut documentaire : `OFFICIAL_CURRENT_CONTEXT`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Ses missions — L'acquisition ; Ses missions — La gestion des sites.

<a id="doc-fr_cen_foncier"></a>

### fr_cen_foncier — Foncier

[Foncier](https://reseau-cen.org/aires-espaces-proteges/foncier/) — Fédération des Conservatoires d’espaces naturels.

Statut documentaire : `OFFICIAL_CURRENT_CONTEXT`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Différents outils de maitrise foncière ou d’usage.

<a id="doc-fr_dreal_geology"></a>

### fr_dreal_geology — Arrêtés préfectoraux relatifs à la protection de sites d’intérêt géologique

[Arrêtés préfectoraux relatifs à la protection de sites d’intérêt géologique](https://www.hauts-de-france.developpement-durable.gouv.fr/Les-Arretes-prefectoraux-relatifs-a-la-protection-de-sites-d-interet-geologique.html) — DREAL Hauts-de-France.

Statut documentaire : `OFFICIAL_CONTEXT`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Comment le protéger ? ; 1. Arrêtés préfectoraux fixant les listes départementales de sites d’intérêt géologique ; 2. Arrêtés préfectoraux de protection de géotope (APPG).

- Limite : Date de publication non établie ; présentation administrative, pas acte individuel ni dictionnaire EP.

<a id="doc-fr_ce_l331_16"></a>

### fr_ce_l331_16 — Code de l’environnement — Article L331-16

[Code de l’environnement — Article L331-16](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074220/LEGISCTA000006176508/) — Légifrance / République française.

Statut documentaire : `OFFICIAL_LEGAL_TERMINOLOGY_ONLY`. Version : Version en vigueur depuis le 2006-04-15. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Article L331-16.

<a id="doc-fr_ce_l332_16"></a>

### fr_ce_l332_16 — Code de l’environnement — Article L332-16

[Code de l’environnement — Article L332-16](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000022482577) — Légifrance / République française.

Statut documentaire : `OFFICIAL_LEGAL_TERMINOLOGY_ONLY`. Version : Version en vigueur depuis le 2010-07-14. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Article L332-16.

- Limite : Première URL datée : erreur interne du service de consultation ; page canonique sans date consultée normalement.

<a id="doc-fr_sept_iles_2023"></a>

### fr_sept_iles_2023 — La réserve naturelle nationale des Sept-Îles devient la plus grande de l'hexagone

[La réserve naturelle nationale des Sept-Îles devient la plus grande de l'hexagone](https://www.ecologie.gouv.fr/presse/reserve-naturelle-nationale-sept-iles-devient-plus-grande-lhexagone) — Ministère chargé de la transition écologique.

Statut documentaire : `OFFICIAL_LOCAL_HISTORICAL_CONTEXT`. Version : non établie. Publication : 2023-08-25. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Surface multipliée par 70.

- Limite : Exemple local ; ne désigne aucune des lignes physiques EP à partir des seules marges.

<a id="doc-pf_diren_espaces"></a>

### PF_DIREN_ESPACES — Les espaces naturels

[Les espaces naturels](https://www.service-public.pf/diren/preserver/espaces-naturels/) — Direction de l'environnement — Polynésie française.

Statut documentaire : `OFFICIAL_EXPLANATORY_HTML`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Les espaces classés > 51 sites classés : catégories I à VI, lignes consultées 268–282.

- Limite : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Limite : Page non versionnée; ne pas traiter sa matrice d'objectifs comme le domaine du champ objectif_protection.

<a id="doc-nc_nord_protection"></a>

### NC_NORD_PROTECTION — Protection

[Protection](https://www.province-nord.nc/environnement/protection) — Province Nord — Nouvelle-Calédonie.

Statut documentaire : `OFFICIAL_EXPLANATORY_HTML`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Les aires protégées : six catégories, lignes consultées 34–45.

- Limite : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Limite : La page emploie réserve de nature intégrale; l'équivalence avec le libellé export Réserve naturelle intégrale n'est pas démontrée.

<a id="doc-nc_sud_carte_reglementation"></a>

### NC_SUD_CARTE_REGLEMENTATION — Carte et réglementation

[Carte et réglementation](https://www.province-sud.nc/environnement/aires-protegees/cartes-et-reglementation/) — Province Sud — Nouvelle-Calédonie.

Statut documentaire : `OFFICIAL_EXPLANATORY_HTML`. Version : non établie. Publication : non établie. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : 1. Carte des aires protégées > Liste des aires protégées : sous-types saisonniers, lignes 90–99 ; 2. Réglementation : rubriques RNI, RN, AGDR et Parcs, lignes 130–206.

- Limite : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Limite : Page explicative citant le code provincial; aucune version consolidée de ce code n'a été vérifiée dans cette recherche.

<a id="doc-nc_corail_reserves_2023"></a>

### NC_CORAIL_RESERVES_2023 — Extension des réserves: le Parc sous haute protection

[Extension des réserves: le Parc sous haute protection](https://mer-de-corail.gouv.nc/fr/actualites/13-12-2023/extension-des-reserves-le-parc-sous-haute-protection) — Parc naturel de la mer de Corail — Gouvernement de la Nouvelle-Calédonie.

Statut documentaire : `OFFICIAL_EXPLANATORY_HTML`. Version : non établie. Publication : 2023-12-13. Mise à jour : non établie. Consultation : 2026-09-08.

Localisateurs : Des sanctuaires à préserver : création du parc en 2014, lignes 136–140 ; Quelles différences entre réserve « naturelle » et « intégrale » ?, lignes 154–159 ; LES RÉSERVES NATURELLES, ligne 163; LES RÉSERVES INTÉGRALES, lignes 187–199.

- Limite : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Limite : Article daté décrivant une évolution applicable en 2024; non assimilé à un état consolidé au 07/2026.

<a id="doc-pf_drm_moorea"></a>

### PF_DRM_MOOREA — ZPR de MOOREA

[ZPR de MOOREA](https://www.ressources-marines.gov.pf/cartes-thematiques/zpr/cartes-zpr/zpr-de-moorea/) — Direction des Ressources Marines — Polynésie française.

Statut documentaire : `OFFICIAL_EXPLANATORY_HTML`. Version : non établie. Publication : non établie. Mise à jour : 2025-05-21T14:50:36-10:00. Consultation : 2026-09-08.

Localisateurs : Qu’est-ce qu’une ZPR ?, lignes 43–49 ; Et la ZPR de Moorea ?, lignes 50–58.

- Limite : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Limite : Horodatage de page 2025-05-21; le corps précise Mise à jour novembre 2023 et décrit les actes de 2022/2023.

- Limite : Moorea seulement pour le lien entre anciennes AMP du PGEM et ZPR; aucune identification des lignes EP correspondantes.

## 6. Profils physiques complets des trois champs

Positions zéro-indexées telles que retenues par le profileur. Les SHA portent sur les cellules canoniques adressées par FID ; les noms, positions et dtypes sont liés séparément par chaque profil et le hash complet. Des contenus identiques peuvent partager un SHA. Le JSON conserve aussi taille/SHA/position de package et l’intégralité des domaines de chaque profil. Les fréquences de la section 7 permettent de retrouver chaque domaine, avec zéro dans les autres couches.

| Package exact | Couche exacte | Champ | Position | Dtype source | Dtype runtime | Lignes | NULL | Non-NULL | Distinctes | SHA256 colonne |
|---|---|---|---:|---|---|---:|---:|---:|---:|---|
| `EP/sig_blm.gpkg` | `sig_blm` | `type_espace` | 5 | `object` | `str` | 4 | 0 | 4 | 3 | `3fc7d67590037706f72b0a478d7b89ed81d6bba8ba148eb203e6345af4275beb` |
| `EP/sig_blm.gpkg` | `sig_blm` | `statut` | 7 | `object` | `object` | 4 | 4 | 0 | 0 | `4311f63fd85bd135aa7d611b3b2866c0edcf9637a9f900667a26e104e78a1daf` |
| `EP/sig_blm.gpkg` | `sig_blm` | `objectif_protection` | 6 | `object` | `str` | 4 | 0 | 4 | 1 | `c812c778f2d412c143ad3449abd3023e9fe0c4d22d1ab20819bbadebc5e857ba` |
| `EP/sig_cli.gpkg` | `sig_cli` | `type_espace` | 5 | `object` | `str` | 1 | 0 | 1 | 1 | `d27045b3cba16ee6f46e452ebd439f64a43d74652ede5e33920135d63da69fe9` |
| `EP/sig_cli.gpkg` | `sig_cli` | `statut` | 7 | `object` | `object` | 1 | 1 | 0 | 0 | `c3a7f418188d35915d14f8d06db06bc98703266618252cd00e94561223447cec` |
| `EP/sig_cli.gpkg` | `sig_cli` | `objectif_protection` | 6 | `object` | `str` | 1 | 0 | 1 | 1 | `1adb7ae08d3ae628c499317124c42bc799a40ac21381476603ad5e82c06f4613` |
| `EP/sig_epa.gpkg` | `sig_epa` | `type_espace` | 5 | `object` | `str` | 5 | 0 | 5 | 3 | `58d89f8cbfadfef66f4eec8fbd957af6773c6ce26842f0bdfcd620b48c84c194` |
| `EP/sig_epa.gpkg` | `sig_epa` | `statut` | 7 | `object` | `object` | 5 | 5 | 0 | 0 | `bdae73b9265f54186b3ac92ae2b88d9c7386ade93e06e74bc4aa0e2ef79d02bf` |
| `EP/sig_epa.gpkg` | `sig_epa` | `objectif_protection` | 6 | `object` | `str` | 5 | 0 | 5 | 1 | `8b7fa67c3b1bdf2cc382e17f8b2b74f44af0d6b30cfc738bc96c48868c2590b8` |
| `EP/sig_glp.gpkg` | `sig_glp` | `type_espace` | 5 | `object` | `str` | 94 | 0 | 94 | 12 | `5f0840ef0bf000b085076ac68815e8c862fcd66921b0c9ed470e36003f649af4` |
| `EP/sig_glp.gpkg` | `sig_glp` | `statut` | 7 | `object` | `object` | 94 | 94 | 0 | 0 | `5eb5b034b7b4907c83a34a280eed699ce1fd8910ba04d6ef1d3092ad1bb2ff40` |
| `EP/sig_glp.gpkg` | `sig_glp` | `objectif_protection` | 6 | `object` | `str` | 94 | 5 | 89 | 2 | `d831922b3493547727c8fee2b6a973eb2b414778a9a3ae3bfa5091c2601dfce6` |
| `EP/sig_guf.gpkg` | `sig_guf` | `type_espace` | 5 | `object` | `str` | 42 | 0 | 42 | 11 | `e5573edb635e52215834f9d659fea0901989bbb230a555491034bb88b5f619a5` |
| `EP/sig_guf.gpkg` | `sig_guf` | `statut` | 7 | `object` | `object` | 42 | 42 | 0 | 0 | `48b8e92bd766a5c89968a419356970b02328a47985bb7f57d0517ce308f230a3` |
| `EP/sig_guf.gpkg` | `sig_guf` | `objectif_protection` | 6 | `object` | `str` | 42 | 4 | 38 | 2 | `5b37fd9fa8e900ba36a5041d25b436bcbd610ce4c4e09eef95dac565d0e7325e` |
| `EP/sig_maf.gpkg` | `sig_maf` | `type_espace` | 5 | `object` | `str` | 21 | 0 | 21 | 4 | `96ce383f849722784d1cf0eeb9f3c0a43099669a36056842f8a3ccd9f56c7669` |
| `EP/sig_maf.gpkg` | `sig_maf` | `statut` | 7 | `object` | `object` | 21 | 21 | 0 | 0 | `19f60318f25254aea382daa6cefb5ae7b717ca28859d717b2a8a7a195c847f4e` |
| `EP/sig_maf.gpkg` | `sig_maf` | `objectif_protection` | 6 | `object` | `str` | 21 | 0 | 21 | 1 | `046c30a8bf2c4c46f8afe66f7ae1a737a438e600d3275e7e7d674b36ca6a9513` |
| `EP/sig_metrop.gpkg` | `sig_metrop` | `type_espace` | 5 | `object` | `str` | 10872 | 0 | 10872 | 32 | `4e65bcebd3921405c1e94587b7e362891621e49deacab7322da30d6ecc6c3cf8` |
| `EP/sig_metrop.gpkg` | `sig_metrop` | `statut` | 7 | `object` | `object` | 10872 | 10872 | 0 | 0 | `743e2eba4a1d5cb6ad84ff8f80467066a82d8c71e742db7a5b45e28e701b4312` |
| `EP/sig_metrop.gpkg` | `sig_metrop` | `objectif_protection` | 6 | `object` | `str` | 10872 | 1811 | 9061 | 3 | `12d4352af87f8c6970c1cda2e4da2bb2cd4c845c413d35b71081dbee34b7f6fa` |
| `EP/sig_mtq.gpkg` | `sig_mtq` | `type_espace` | 5 | `object` | `str` | 79 | 0 | 79 | 15 | `67a710eb792b63348c921e82006fc7d0f32fae248767daa9b7b1ea02fefed81f` |
| `EP/sig_mtq.gpkg` | `sig_mtq` | `statut` | 7 | `object` | `object` | 79 | 79 | 0 | 0 | `ab38256082d2ddc143a5badfdfd2ecc60289fd13b553b36c1bd678d584f5575b` |
| `EP/sig_mtq.gpkg` | `sig_mtq` | `objectif_protection` | 6 | `object` | `str` | 79 | 13 | 66 | 2 | `9bd799637b6da012d41330a170bf30f36b5b818729205893f53d883d67879d4d` |
| `EP/sig_myt.gpkg` | `sig_myt` | `type_espace` | 5 | `object` | `str` | 30 | 0 | 30 | 5 | `ce6d65a7d8b4c8a2f1786138fd3a7f45a495a20ca1d01cc183f806cf78f368d5` |
| `EP/sig_myt.gpkg` | `sig_myt` | `statut` | 7 | `object` | `object` | 30 | 30 | 0 | 0 | `c68a84035a1496d7e37df498f5ceb516cc63aeb90e1ad635dbbd05aacff02c53` |
| `EP/sig_myt.gpkg` | `sig_myt` | `objectif_protection` | 6 | `object` | `str` | 30 | 7 | 23 | 1 | `bdc4ab9b7f276a2563f2ea967c91932bdb9ed0be229f09232d12820bc85357f9` |
| `EP/sig_ncl.gpkg` | `sig_ncl` | `type_espace` | 5 | `object` | `str` | 88 | 0 | 88 | 16 | `8818b024cf334def09b27aca91db76e8cf10b52eb0e393776eed04e47ea493f0` |
| `EP/sig_ncl.gpkg` | `sig_ncl` | `statut` | 7 | `object` | `object` | 88 | 88 | 0 | 0 | `3eb66fb886d4ad526c51403966a46865a466306f75b43651dac426864c13cbec` |
| `EP/sig_ncl.gpkg` | `sig_ncl` | `objectif_protection` | 6 | `object` | `str` | 88 | 87 | 1 | 1 | `1eeefc3931d066803ef31e822d148a5e2caff93bf9c83d45b57c146f5744baf6` |
| `EP/sig_pyf.gpkg` | `sig_pyf` | `type_espace` | 5 | `object` | `str` | 87 | 0 | 87 | 18 | `2c9c922f30332e3a9a25e16fd04fe7a5e518377066a9ac164483c18b960ebd55` |
| `EP/sig_pyf.gpkg` | `sig_pyf` | `statut` | 7 | `object` | `object` | 87 | 87 | 0 | 0 | `3a76908a53bd10a23c9b5c040dbea4f1f88c8cc8fc5a0ce87ddd1a4938e6c55c` |
| `EP/sig_pyf.gpkg` | `sig_pyf` | `objectif_protection` | 6 | `object` | `str` | 87 | 86 | 1 | 1 | `5e19cf38e7c34569276000388ae884ecfe395231f23331aceed28192d32f77da` |
| `EP/sig_reu.gpkg` | `sig_reu` | `type_espace` | 5 | `object` | `str` | 44 | 0 | 44 | 10 | `af5749faedfd2c9d808ab9aee5156926791163c19d6d358a45a499db6b99b164` |
| `EP/sig_reu.gpkg` | `sig_reu` | `statut` | 7 | `object` | `object` | 44 | 44 | 0 | 0 | `c48a05b1a6257c145f6b3cfb5b8627cb34e7e037c5ac5f6be534e6655e4e23de` |
| `EP/sig_reu.gpkg` | `sig_reu` | `objectif_protection` | 6 | `object` | `str` | 44 | 0 | 44 | 2 | `5ae2e7aab0ac3fa42e7aee5711fa8433dc48871604635919a1dbfea4c37de2cc` |
| `EP/sig_spm.gpkg` | `sig_spm` | `type_espace` | 5 | `object` | `str` | 2 | 0 | 2 | 1 | `f743b8e218b62f9c473d3bd56932133d92ef390d39facfd13aa51dc6cbc0d7ab` |
| `EP/sig_spm.gpkg` | `sig_spm` | `statut` | 7 | `object` | `object` | 2 | 2 | 0 | 0 | `2ef58295d1cf1ebcdf2f03f5eb6a4f45b868ba1421c238786e3811faed821549` |
| `EP/sig_spm.gpkg` | `sig_spm` | `objectif_protection` | 6 | `object` | `str` | 2 | 0 | 2 | 1 | `df2c6a7f5fc69a042b51a296ea6b0628c8ce81c4b339b4767a311cc8ed9aa5ff` |
| `EP/sig_subant.gpkg` | `sig_subant` | `type_espace` | 5 | `object` | `str` | 11 | 0 | 11 | 4 | `19a42cfb0ab496042ee934bf32ac192ab5d8f37cab977a4d3f8ea71b73fb26c9` |
| `EP/sig_subant.gpkg` | `sig_subant` | `statut` | 7 | `object` | `object` | 11 | 11 | 0 | 0 | `e3195874bc13c81faf56ed854fa8641e38088b7170e0355cc7fb8375fd18ebb6` |
| `EP/sig_subant.gpkg` | `sig_subant` | `objectif_protection` | 6 | `object` | `str` | 11 | 2 | 9 | 1 | `25703e9b54320b2803683a29f763d9d5a2fe6ee0ca4805ae4837eaf2f0a62918` |
| `EP/sig_tadl.gpkg` | `sig_tadl` | `type_espace` | 5 | `object` | `str` | 1 | 0 | 1 | 1 | `885230ab2a22fb0576b3194567faaa85eae350d4cd1f00fcd3d508f87fc109b3` |
| `EP/sig_tadl.gpkg` | `sig_tadl` | `statut` | 7 | `object` | `object` | 1 | 1 | 0 | 0 | `c3a7f418188d35915d14f8d06db06bc98703266618252cd00e94561223447cec` |
| `EP/sig_tadl.gpkg` | `sig_tadl` | `objectif_protection` | 6 | `object` | `str` | 1 | 0 | 1 | 1 | `1adb7ae08d3ae628c499317124c42bc799a40ac21381476603ad5e82c06f4613` |

## 7. Une entrée par valeur non nulle exacte

L’ordre suit les trois champs demandés, puis l’ordre canonique des domaines `(value_kind, canonical_value)`. Les fréquences mentionnent la clé complète `relative_path::layer_name`. Chaque entrée JSON conserve explicitement les 15 effectifs, y compris les zéros ; ci-dessous seuls les effectifs positifs sont imprimés et **toutes les autres couches valent zéro**. Un champ « Définition de contexte » n’est jamais une définition démontrée du champ exporté.

<a id="value-001"></a>

### 001 — Aire de gestion des habitats ou des espèces (Polynésie française)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **12**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Catégorie IV orientée vers les habitats et espèces, nécessitant une gestion active.

Périmètre documentaire : Polynésie française.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 12. Toutes les autres couches : 0.

- Source : [PF_DIREN_ESPACES](#doc-pf_diren_espaces) ; Les espaces classés > 51 sites classés, catégorie IV, ligne 279. Prouve : Objectif général de la catégorie locale. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-002"></a>

### 002 — Aire de gestion durable des ressources (Nouvelle-Calédonie - Province Nord)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **2**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Gestion de la biodiversité sur la durée avec maintien des bénéfices naturels pour la population.

Périmètre documentaire : Nouvelle-Calédonie — Province Nord.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 2. Toutes les autres couches : 0.

- Source : [NC_NORD_PROTECTION](#doc-nc_nord_protection) ; Les aires protégées, sixième catégorie, ligne 45. Prouve : Description provinciale de cette catégorie. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-003"></a>

### 003 — Aire de gestion durable des ressources (Nouvelle-Calédonie - Province Sud)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **10**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Gestion associant préservation durable de la biodiversité et usages compatibles, organisée par un plan.

Périmètre documentaire : Nouvelle-Calédonie — Province Sud.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 10. Toutes les autres couches : 0.

- Source : [NC_SUD_CARTE_REGLEMENTATION](#doc-nc_sud_carte_reglementation) ; 2. Réglementation > AGDR, articles cités 211-13 et 214-1 et suivants, lignes 175–186. Prouve : Finalité provinciale de la catégorie; pas une autorisation de projet. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-004"></a>

### 004 — Aire marine protégée de plan de gestion de l'espace maritime (Polynésie française)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **8**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : À Moorea, des AMP issues de l'ancien PGEM sont conservées dans la réglementation ZPR ultérieure.

Périmètre documentaire : Polynésie française — exemple documenté : Moorea.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 8. Toutes les autres couches : 0.

- Source : [PF_DRM_MOOREA](#doc-pf_drm_moorea) ; Et la ZPR de Moorea ?, lignes 52–53. Prouve : Existence d'AMP d'un ancien PGEM dans un exemple territorial daté. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Les huit occurrences EP concernent-elles ces mêmes objets et quel état juridique/exporté représentent-elles ?

- Question : La formulation intégrale du libellé export n'est pas définie par cette page.

<a id="value-005"></a>

### 005 — Aire protégée de ressources naturelles gérées (Polynésie française)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **10**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Catégorie VI centrée sur un usage pérenne des écosystèmes.

Périmètre documentaire : Polynésie française.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 10. Toutes les autres couches : 0.

- Source : [PF_DIREN_ESPACES](#doc-pf_diren_espaces) ; Les espaces classés > 51 sites classés, catégorie VI, ligne 282. Prouve : Finalité générale de cette catégorie locale. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-006"></a>

### 006 — Aire spécialement protégée d'intérêt méditerranéen de la convention de Barcelone

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **7**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte SPAMI : reconnaissance régionale pour conserver des zones naturelles, des espèces menacées et leurs habitats méditerranéens.

Périmètre documentaire : Méditerranée ; zones marines et côtières, éventuellement haute mer.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 7. Toutes les autres couches : 0.

- Source : [spa_rac_spami](#doc-spa_rac_spami) ; Overview ; Objectives and criteria of SPAMIs ; The SPAMI List. Prouve : Établit les objectifs et le champ géographique du dispositif SPAMI. Ne prouve pas : Ne relie pas le libellé exact EP au dispositif ni aux sept objets du millésime.

- Question : Quelle documentation du producteur établit l'équivalence entre d'intérêt dans EP et d'importance dans la terminologie du standard ?

<a id="value-007"></a>

### 007 — Arrêté de protection de biotope

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **1103**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Protection préfectorale des habitats nécessaires aux espèces protégées.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_blm.gpkg::sig_blm` = 2 ; `EP/sig_cli.gpkg::sig_cli` = 1 ; `EP/sig_glp.gpkg::sig_glp` = 5 ; `EP/sig_guf.gpkg::sig_guf` = 3 ; `EP/sig_maf.gpkg::sig_maf` = 1 ; `EP/sig_metrop.gpkg::sig_metrop` = 1062 ; `EP/sig_mtq.gpkg::sig_mtq` = 24 ; `EP/sig_myt.gpkg::sig_myt` = 2 ; `EP/sig_reu.gpkg::sig_reu` = 3. Toutes les autres couches : 0.

- Source : [fr_ministry_areas](#doc-fr_ministry_areas) ; Arrêtés préfectoraux de protection. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-008"></a>

### 008 — Arrêté de protection de géotope

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **43**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Mesures préfectorales complémentaires pour un site géologique déjà inscrit sur la liste départementale.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 43. Toutes les autres couches : 0.

- Source : [fr_dreal_geology](#doc-fr_dreal_geology) ; 2. Arrêtés préfectoraux de protection de géotope (APPG). Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-009"></a>

### 009 — Arrêté de protection des habitats naturels

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **26**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Protection d’habitats, sans condition de présence d’espèces protégées.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 26. Toutes les autres couches : 0.

- Source : [fr_ministry_areas](#doc-fr_ministry_areas) ; Arrêtés préfectoraux de protection. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-010"></a>

### 010 — Arrêté listes de sites d'intérêt géologique

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **194**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Liste départementale instituant le cadre de protection de sites présentant un intérêt géologique documenté.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 194. Toutes les autres couches : 0.

- Source : [fr_dreal_geology](#doc-fr_dreal_geology) ; 1. Arrêtés préfectoraux fixant les listes départementales de sites d’intérêt géologique. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-011"></a>

### 011 — Bien inscrit sur la liste du patrimoine mondial de l'UNESCO

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **10**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte conventionnel : bien inscrit par le Comité du patrimoine mondial en raison d'une valeur universelle exceptionnelle.

Périmètre documentaire : Convention internationale ; biens des États parties.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 5 ; `EP/sig_mtq.gpkg::sig_mtq` = 1 ; `EP/sig_ncl.gpkg::sig_ncl` = 1 ; `EP/sig_pyf.gpkg::sig_pyf` = 1 ; `EP/sig_reu.gpkg::sig_reu` = 1 ; `EP/sig_subant.gpkg::sig_subant` = 1. Toutes les autres couches : 0.

- Source : [unesco_world_heritage_convention](#doc-unesco_world_heritage_convention) ; Articles 1-2 et 11.2. Prouve : Distingue patrimoines culturel et naturel et institue la liste internationale. Ne prouve pas : N'établit ni les biens retenus dans EP ni le filtrage naturel, culturel ou mixte du producteur.

- Question : Quel périmètre de sélection a été appliqué aux biens UNESCO dans EP 07/2026 ?

<a id="value-012"></a>

### 012 — Gestion de l'espace maritime (Polynésie française)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **1**.

État de recherche : `UNRESOLVED`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Non établie.

Périmètre documentaire : Polynésie française — suffixe observé; catégorie exacte non résolue.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 1. Toutes les autres couches : 0.

- Source : [PF_DRM_MOOREA](#doc-pf_drm_moorea) ; Et la ZPR de Moorea ?, lignes 52–53. Prouve : Contexte PGEM/ZPR seulement. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Que désigne exactement Gestion de l'espace maritime dans le dictionnaire de l'export ?

- Question : Ne pas ajouter Plan, assimiler cette occurrence à Tainui Atea, ni identifier un site d'après son seul effectif.

<a id="value-013"></a>

### 013 — Grand Site de France

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **26**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Label ministériel reconnaissant un projet effectif de préservation et de gestion durable d’un site classé.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 26. Toutes les autres couches : 0.

- Source : [fr_ministry_sites](#doc-fr_ministry_sites) ; Le label Grand Site de France. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-014"></a>

### 014 — Géoparcs mondiaux UNESCO

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **9**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte UNESCO : territoire de patrimoine géologique international, géré en associant conservation, éducation et développement durable.

Périmètre documentaire : Programme mondial des géoparcs UNESCO.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 9. Toutes les autres couches : 0.

- Source : [unesco_geoparks_about](#doc-unesco_geoparks_about) ; What is a UNESCO Global Geopark? ; UNESCO designated sites. Prouve : Décrit une désignation distincte des réserves de biosphère et du patrimoine mondial. Ne prouve pas : La page postérieure au millésime ne démontre pas le contenu de l'export de juillet ni un effet juridique local.

- Question : Quelle spécification relie cette désignation et sa date de validité aux objets du snapshot ?

<a id="value-015"></a>

### 015 — Monument naturel (Polynésie française)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **2**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Catégorie III destinée à sauvegarder des singularités de la nature.

Périmètre documentaire : Polynésie française.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 2. Toutes les autres couches : 0.

- Source : [PF_DIREN_ESPACES](#doc-pf_diren_espaces) ; Les espaces classés > 51 sites classés, catégorie III, ligne 277. Prouve : Finalité générale de cette catégorie locale. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-016"></a>

### 016 — Parc national, aire d'adhésion

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **11**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Territoires des communes ayant adhéré à la charte du parc, en solidarité écologique avec son cœur.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_glp.gpkg::sig_glp` = 1 ; `EP/sig_guf.gpkg::sig_guf` = 1 ; `EP/sig_metrop.gpkg::sig_metrop` = 8 ; `EP/sig_reu.gpkg::sig_reu` = 1. Toutes les autres couches : 0.

- Source : [fr_sdes_parks_2021](#doc-fr_sdes_parks_2021) ; Aire d’adhésion. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-017"></a>

### 017 — Parc national, zone cœur

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **11**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Partie terrestre ou marine du parc soumise à une réglementation spécifique de préservation du patrimoine.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_glp.gpkg::sig_glp` = 1 ; `EP/sig_guf.gpkg::sig_guf` = 1 ; `EP/sig_metrop.gpkg::sig_metrop` = 8 ; `EP/sig_reu.gpkg::sig_reu` = 1. Toutes les autres couches : 0.

- Source : [fr_sdes_parks_2021](#doc-fr_sdes_parks_2021) ; Cœur de parc national. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-018"></a>

### 018 — Parc naturel (Nouvelle-Calédonie)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **1**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Exemple officiel : le parc de la mer de Corail est une vaste aire marine créée en 2014.

Périmètre documentaire : Nouvelle-Calédonie — espace maritime relevant du contexte gouvernemental décrit.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 1. Toutes les autres couches : 0.

- Source : [NC_CORAIL_RESERVES_2023](#doc-nc_corail_reserves_2023) ; Des sanctuaires à préserver, lignes 136–140. Prouve : Existence et contexte de ce parc; pas définition exhaustive du type export. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : L'occurrence EP n'est pas identifiée à ce parc par cette recherche documentaire.

<a id="value-019"></a>

### 019 — Parc naturel marin

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **8**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Connaissance et conservation marines associées au développement durable.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 6 ; `EP/sig_mtq.gpkg::sig_mtq` = 1 ; `EP/sig_myt.gpkg::sig_myt` = 1. Toutes les autres couches : 0.

- Source : [fr_ministry_areas](#doc-fr_ministry_areas) ; Parcs naturels marins. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-020"></a>

### 020 — Parc naturel régional

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **59**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Projet régional conciliant patrimoine et développement territorial.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_guf.gpkg::sig_guf` = 1 ; `EP/sig_metrop.gpkg::sig_metrop` = 57 ; `EP/sig_mtq.gpkg::sig_mtq` = 1. Toutes les autres couches : 0.

- Source : [fr_ministry_areas](#doc-fr_ministry_areas) ; Parcs naturels régionaux. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-021"></a>

### 021 — Parc provincial (Nouvelle-Calédonie - Province Nord)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **1**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Protection des écosystèmes et de leur fonctionnement, avec un encadrement des usages compatibles.

Périmètre documentaire : Nouvelle-Calédonie — Province Nord.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 1. Toutes les autres couches : 0.

- Source : [NC_NORD_PROTECTION](#doc-nc_nord_protection) ; Les aires protégées, troisième catégorie, ligne 42. Prouve : Finalité provinciale du parc. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-022"></a>

### 022 — Parc provincial (Nouvelle-Calédonie - Province Sud)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **8**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Préservation de la nature et accueil encadré, avec un plan de gestion.

Périmètre documentaire : Nouvelle-Calédonie — Province Sud.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 8. Toutes les autres couches : 0.

- Source : [NC_SUD_CARTE_REGLEMENTATION](#doc-nc_sud_carte_reglementation) ; 2. Réglementation > Parcs, articles cités 211-18 et 215-1 et suivants, lignes 201–206. Prouve : Finalité provinciale du parc. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-023"></a>

### 023 — Parc territorial (Polynésie française)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **2**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Catégorie II conjuguant sauvegarde des écosystèmes et récréation.

Périmètre documentaire : Polynésie française.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 2. Toutes les autres couches : 0.

- Source : [PF_DIREN_ESPACES](#doc-pf_diren_espaces) ; Les espaces classés > 51 sites classés, catégorie II, ligne 275. Prouve : Finalité de la catégorie locale. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-024"></a>

### 024 — Paysage naturel protégé (Polynésie française)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **4**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte voisin : la catégorie V Paysage protégé vise les paysages et la récréation.

Périmètre documentaire : Polynésie française.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 4. Toutes les autres couches : 0.

- Source : [PF_DIREN_ESPACES](#doc-pf_diren_espaces) ; Les espaces classés > 51 sites classés, catégorie V, ligne 280. Prouve : Définition du libellé institutionnel Paysage protégé, sans le mot naturel. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : L'équivalence exacte avec Paysage naturel protégé reste à documenter; le libellé brut n'est pas corrigé.

<a id="value-025"></a>

### 025 — Projet de Grand Site de France

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **22**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : La démarche officielle prépare une gestion territoriale ; elle est distincte de l’attribution du label.

Périmètre documentaire : France.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 22. Toutes les autres couches : 0.

- Source : [fr_ministry_sites](#doc-fr_ministry_sites) ; La démarche Grand Site de France. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Le producteur doit préciser les stades inclus par son libellé « Projet » ; ne pas le convertir en label attribué.

<a id="value-026"></a>

### 026 — Périmètre de protection de réserve naturelle intégrale (Polynésie française)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **1**.

État de recherche : `UNRESOLVED`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Non établie.

Périmètre documentaire : Polynésie française — suffixe observé; régime du périmètre non résolu.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 1. Toutes les autres couches : 0.

- Source : [PF_DIREN_ESPACES](#doc-pf_diren_espaces) ; Les espaces classés > 51 sites classés, lignes 268–282. Prouve : Les catégories principales sont documentées, pas ce périmètre. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel acte ou dictionnaire définit le périmètre de protection et son lien avec une réserve ?

- Question : Aucune définition primaire précise de ce libellé n'a été vérifiée dans la recherche bornée.

<a id="value-027"></a>

### 027 — Périmètre de protection d’une réserve naturelle nationale

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **18**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Périmètre autour d’une réserve nationale, instituable par le représentant de l’État.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 17 ; `EP/sig_mtq.gpkg::sig_mtq` = 1. Toutes les autres couches : 0.

- Source : [fr_ce_l332_16](#doc-fr_ce_l332_16) ; Article L332-16. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-028"></a>

### 028 — Périmètre de protection d’une réserve naturelle régionale ou de Corse

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **2**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Périmètre autour d’une réserve régionale ; compétence régionale ou, dans le cas prévu, de l’Assemblée de Corse.

Périmètre documentaire : France — réserves régionales et Corse.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 2. Toutes les autres couches : 0.

- Source : [fr_ce_l332_16](#doc-fr_ce_l332_16) ; Article L332-16. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-029"></a>

### 029 — Réserve biologique dirigée

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **168**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Gestion forestière dédiée à des habitats ou espèces.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_glp.gpkg::sig_glp` = 1 ; `EP/sig_guf.gpkg::sig_guf` = 1 ; `EP/sig_metrop.gpkg::sig_metrop` = 160 ; `EP/sig_reu.gpkg::sig_reu` = 6. Toutes les autres couches : 0.

- Source : [fr_ministry_areas](#doc-fr_ministry_areas) ; Réserves biologiques. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-030"></a>

### 030 — Réserve biologique intégrale

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **117**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Évolution naturelle des écosystèmes forestiers.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_guf.gpkg::sig_guf` = 3 ; `EP/sig_metrop.gpkg::sig_metrop` = 107 ; `EP/sig_mtq.gpkg::sig_mtq` = 3 ; `EP/sig_reu.gpkg::sig_reu` = 4. Toutes les autres couches : 0.

- Source : [fr_ministry_areas](#doc-fr_ministry_areas) ; Réserves biologiques. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-031"></a>

### 031 — Réserve de Biosphère, zone centrale

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **16**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte MAB : noyau dédié à la conservation des écosystèmes, habitats et espèces.

Périmètre documentaire : Programme international UNESCO MAB.

Fréquences par couche : `EP/sig_glp.gpkg::sig_glp` = 1 ; `EP/sig_metrop.gpkg::sig_metrop` = 13 ; `EP/sig_mtq.gpkg::sig_mtq` = 1 ; `EP/sig_pyf.gpkg::sig_pyf` = 1. Toutes les autres couches : 0.

- Source : [unesco_mab_zonation](#doc-unesco_mab_zonation) ; Core area(s). Prouve : Décrit la fonction de conservation du noyau. Ne prouve pas : Ne démontre ni codage EP, ni limites, ni régime local.

- Question : Quel contrat producteur identifie les zones centrales dans cet export ?

<a id="value-032"></a>

### 032 — Réserve de Biosphère, zone de transition

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **16**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte MAB : espace habité et travaillé visant un développement humain et économique durable.

Périmètre documentaire : Programme international UNESCO MAB.

Fréquences par couche : `EP/sig_glp.gpkg::sig_glp` = 1 ; `EP/sig_metrop.gpkg::sig_metrop` = 13 ; `EP/sig_mtq.gpkg::sig_mtq` = 1 ; `EP/sig_pyf.gpkg::sig_pyf` = 1. Toutes les autres couches : 0.

- Source : [unesco_mab_zonation](#doc-unesco_mab_zonation) ; Transition area(s). Prouve : Décrit la fonction de développement de la zone externe. Ne prouve pas : Ne démontre ni codage EP ni autorisation d'un usage particulier.

- Question : Comment le producteur définit-il le périmètre de transition fourni en juillet 2026 ?

<a id="value-033"></a>

### 033 — Réserve de Biosphère, zone tampon

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **16**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte MAB : espace entourant ou jouxtant le noyau, avec des activités compatibles avec la conservation.

Périmètre documentaire : Programme international UNESCO MAB.

Fréquences par couche : `EP/sig_glp.gpkg::sig_glp` = 1 ; `EP/sig_metrop.gpkg::sig_metrop` = 13 ; `EP/sig_mtq.gpkg::sig_mtq` = 1 ; `EP/sig_pyf.gpkg::sig_pyf` = 1. Toutes les autres couches : 0.

- Source : [unesco_mab_zonation](#doc-unesco_mab_zonation) ; Buffer zone(s). Prouve : Distingue le rôle de la zone tampon de celui du noyau. Ne prouve pas : Ne démontre ni frontières EP ni conséquences juridiques d'un projet.

- Question : Quel contrat producteur établit les zones tampons et leurs limites dans EP ?

<a id="value-034"></a>

### 034 — Réserve de nature sauvage (Nouvelle-Calédonie - Province Nord)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **8**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Espace resté proche de son état naturel, sans présence humaine durable ou importante.

Périmètre documentaire : Nouvelle-Calédonie — Province Nord.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 8. Toutes les autres couches : 0.

- Source : [NC_NORD_PROTECTION](#doc-nc_nord_protection) ; Les aires protégées, deuxième catégorie, ligne 41. Prouve : Description provinciale de la catégorie. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-035"></a>

### 035 — Réserve intégrale (Nouvelle-Calédonie)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **15**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Conservation des milieux exceptionnels et de leur diversité, avec recherche prudente et dimension culturelle kanak.

Périmètre documentaire : Nouvelle-Calédonie — aires marines, contexte gouvernemental.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 15. Toutes les autres couches : 0.

- Source : [NC_CORAIL_RESERVES_2023](#doc-nc_corail_reserves_2023) ; LES RÉSERVES INTÉGRALES, lignes 187–199; distinction des statuts, lignes 154–159. Prouve : Objectifs de réserves marines intégrales décrits dans l'article. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Le rattachement des quinze occurrences EP à ces actes et à leur version applicable reste absent.

<a id="value-036"></a>

### 036 — Réserve intégrale de parc national

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **4**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Zone instituable dans le cœur d’un parc pour renforcer la protection à des fins scientifiques.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 4. Toutes les autres couches : 0.

- Source : [fr_ce_l331_16](#doc-fr_ce_l331_16) ; Article L331-16. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-037"></a>

### 037 — Réserve nationale de chasse et de faune sauvage

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **11**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Réserve de chasse d’importance particulière pour la faune, l’étendue du site ou les études conduites.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 11. Toutes les autres couches : 0.

- Source : [fr_ofb_reserves](#doc-fr_ofb_reserves) ; Les réserves nationales de chasse et de faune sauvage. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-038"></a>

### 038 — Réserve naturelle (Nouvelle-Calédonie - Province Sud)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **30**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Protection d'espèces et maintien ou restauration de leurs habitats.

Périmètre documentaire : Nouvelle-Calédonie — Province Sud.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 30. Toutes les autres couches : 0.

- Source : [NC_SUD_CARTE_REGLEMENTATION](#doc-nc_sud_carte_reglementation) ; 2. Réglementation > Réserves naturelles, articles cités 211-11 et 213-1 et suivants, lignes 156–159. Prouve : Finalité provinciale de la réserve. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-039"></a>

### 039 — Réserve naturelle (Nouvelle-Calédonie)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **2**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Protection de dynamiques écologiques étendues, d'espèces mobiles et de leurs zones de déplacement et d'alimentation.

Périmètre documentaire : Nouvelle-Calédonie — aires marines, contexte gouvernemental.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 2. Toutes les autres couches : 0.

- Source : [NC_CORAIL_RESERVES_2023](#doc-nc_corail_reserves_2023) ; LES RÉSERVES NATURELLES, ligne 163; distinction des statuts, lignes 154–159. Prouve : Objectifs de réserves marines naturelles décrits dans l'article. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Ne pas assimiler cette catégorie territoriale aux réserves provinciales; la correspondance des deux lignes EP reste inconnue.

<a id="value-040"></a>

### 040 — Réserve naturelle de Corse

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **7**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Conservation biologique ou géologique par une réglementation adaptée.

Périmètre documentaire : Corse.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 7. Toutes les autres couches : 0.

- Source : [fr_ministry_areas](#doc-fr_ministry_areas) ; Réserves naturelles. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-041"></a>

### 041 — Réserve naturelle intégrale (Nouvelle-Calédonie - Province Nord)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **1**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte voisin : la page nomme une réserve de nature intégrale dédiée aux études et au suivi.

Périmètre documentaire : Nouvelle-Calédonie — Province Nord.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 1. Toutes les autres couches : 0.

- Source : [NC_NORD_PROTECTION](#doc-nc_nord_protection) ; Les aires protégées, première catégorie, ligne 40. Prouve : Description du libellé réserve de nature intégrale employé par la province. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Le document ne prouve pas l'équivalence exacte avec Réserve naturelle intégrale dans l'export.

<a id="value-042"></a>

### 042 — Réserve naturelle intégrale (Nouvelle-Calédonie - Province Sud)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **4**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Préservation des milieux, de la diversité génétique et des processus naturels avec réduction des perturbations humaines.

Périmètre documentaire : Nouvelle-Calédonie — Province Sud.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 4. Toutes les autres couches : 0.

- Source : [NC_SUD_CARTE_REGLEMENTATION](#doc-nc_sud_carte_reglementation) ; 2. Réglementation > RNI, articles cités 211-9 et 212-1 et suivants, lignes 130–139. Prouve : Objectifs provinciaux de la catégorie. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-043"></a>

### 043 — Réserve naturelle intégrale (Polynésie française)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **3**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Catégorie Ia principalement consacrée à l'étude scientifique.

Périmètre documentaire : Polynésie française.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 3. Toutes les autres couches : 0.

- Source : [PF_DIREN_ESPACES](#doc-pf_diren_espaces) ; Les espaces classés > 51 sites classés, catégorie Ia, ligne 274. Prouve : Finalité scientifique de cette catégorie locale. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-044"></a>

### 044 — Réserve naturelle intégrale saisonnière (Nouvelle-Calédonie - Province Sud)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **1**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Sous-type de réserve intégrale dont certaines règles s'appliquent selon la période de l'année.

Périmètre documentaire : Nouvelle-Calédonie — Province Sud.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 1. Toutes les autres couches : 0.

- Source : [NC_SUD_CARTE_REGLEMENTATION](#doc-nc_sud_carte_reglementation) ; 1. Carte > Liste, lignes 90–93; 2. Réglementation > RNI, ligne 154. Prouve : Distinction saisonnière explicitement décrite par la province. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Périodes, périmètres et actes propres à chaque occurrence non vérifiés.

<a id="value-045"></a>

### 045 — Réserve naturelle nationale

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **170**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Classement national visant la conservation du milieu naturel, avec réglementation propre à la réserve.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_blm.gpkg::sig_blm` = 1 ; `EP/sig_epa.gpkg::sig_epa` = 1 ; `EP/sig_glp.gpkg::sig_glp` = 2 ; `EP/sig_guf.gpkg::sig_guf` = 6 ; `EP/sig_maf.gpkg::sig_maf` = 1 ; `EP/sig_metrop.gpkg::sig_metrop` = 152 ; `EP/sig_mtq.gpkg::sig_mtq` = 2 ; `EP/sig_myt.gpkg::sig_myt` = 2 ; `EP/sig_reu.gpkg::sig_reu` = 2 ; `EP/sig_subant.gpkg::sig_subant` = 1. Toutes les autres couches : 0.

- Source : [fr_ofb_reserves](#doc-fr_ofb_reserves) ; Les réserves naturelles nationales. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-046"></a>

### 046 — Réserve naturelle régionale

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **193**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Conservation biologique ou géologique par une réglementation adaptée.

Périmètre documentaire : France — catégorie régionale.

Fréquences par couche : `EP/sig_guf.gpkg::sig_guf` = 1 ; `EP/sig_metrop.gpkg::sig_metrop` = 191 ; `EP/sig_mtq.gpkg::sig_mtq` = 1. Toutes les autres couches : 0.

- Source : [fr_ministry_areas](#doc-fr_ministry_areas) ; Réserves naturelles. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-047"></a>

### 047 — Réserve naturelle saisonnière (Nouvelle-Calédonie - Province Sud)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **2**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Sous-type de réserve naturelle comportant une application saisonnière des règles.

Périmètre documentaire : Nouvelle-Calédonie — Province Sud.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 2. Toutes les autres couches : 0.

- Source : [NC_SUD_CARTE_REGLEMENTATION](#doc-nc_sud_carte_reglementation) ; 1. Carte > Liste, lignes 95–99; 2. Réglementation > Réserves naturelles, ligne 173. Prouve : Distinction saisonnière explicitement décrite par la province. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Périodes, périmètres et actes propres à chaque occurrence non vérifiés.

<a id="value-048"></a>

### 048 — Site classé selon la loi de 1930

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **2665**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Classement de sites ou monuments naturels présentant un intérêt patrimonial justifiant leur préservation.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_glp.gpkg::sig_glp` = 5 ; `EP/sig_guf.gpkg::sig_guf` = 2 ; `EP/sig_metrop.gpkg::sig_metrop` = 2649 ; `EP/sig_mtq.gpkg::sig_mtq` = 4 ; `EP/sig_reu.gpkg::sig_reu` = 5. Toutes les autres couches : 0.

- Source : [fr_ministry_sites](#doc-fr_ministry_sites) ; Les sites classés. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-049"></a>

### 049 — Terrain acquis (ou assimilé) par un Conservatoire d'espaces naturels

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **2848**.

État de recherche : `UNRESOLVED`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : La Fédération distingue propriété et maîtrise d’usage ; l’étendue exacte de « ou assimilé » dans EP reste inconnue.

Périmètre documentaire : France.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 2848. Toutes les autres couches : 0.

- Source : [fr_cen_foncier](#doc-fr_cen_foncier) ; Différents outils de maitrise foncière ou d’usage. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Quels droits ou instruments le producteur assimile-t-il à une acquisition dans cette valeur exacte ?

<a id="value-050"></a>

### 050 — Terrain acquis par le Conservatoire du Littoral

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **819**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Terrains acquis pour la préservation littorale ; leur gestion est confiée à des partenaires.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_glp.gpkg::sig_glp` = 72 ; `EP/sig_guf.gpkg::sig_guf` = 20 ; `EP/sig_maf.gpkg::sig_maf` = 16 ; `EP/sig_metrop.gpkg::sig_metrop` = 629 ; `EP/sig_mtq.gpkg::sig_mtq` = 36 ; `EP/sig_myt.gpkg::sig_myt` = 24 ; `EP/sig_reu.gpkg::sig_reu` = 20 ; `EP/sig_spm.gpkg::sig_spm` = 2. Toutes les autres couches : 0.

- Source : [fr_cdl_missions](#doc-fr_cdl_missions) ; Ses missions — L'acquisition ; La gestion des sites. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-051"></a>

### 051 — Terrain géré (location, convention de gestion) par un Conservatoire d'espaces naturels

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **2496**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : La maîtrise d’usage peut reposer sur des baux ou conventions, distincts de la propriété.

Périmètre documentaire : France — périmètre de la catégorie décrite, non déduit des seules marges EP.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 2496. Toutes les autres couches : 0.

- Source : [fr_cen_foncier](#doc-fr_cen_foncier) ; Différents outils de maitrise foncière ou d’usage. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Obtenir la correspondance explicite du producteur avec cette valeur exacte de l’export figé.

<a id="value-052"></a>

### 052 — Zone de nature sauvage (Polynésie française)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **1**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Catégorie Ib visant le maintien du caractère sauvage des ressources.

Périmètre documentaire : Polynésie française.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 1. Toutes les autres couches : 0.

- Source : [PF_DIREN_ESPACES](#doc-pf_diren_espaces) ; Les espaces classés > 51 sites classés, catégorie Ib, ligne 274. Prouve : Finalité générale de cette catégorie locale. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quel contrat producteur établit le lien exact champ/valeur/snapshot EP 07/2026 ?

<a id="value-053"></a>

### 053 — Zone de protection renforcée d'une réserve naturelle nationale

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **16**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Le communiqué des Sept-Îles décrit un sous-périmètre de protection saisonnière ; c’est un exemple local, non une définition nationale uniforme.

Périmètre documentaire : France — exemple des Sept-Îles (2023).

Fréquences par couche : `EP/sig_epa.gpkg::sig_epa` = 3 ; `EP/sig_metrop.gpkg::sig_metrop` = 5 ; `EP/sig_subant.gpkg::sig_subant` = 8. Toutes les autres couches : 0.

- Source : [fr_sept_iles_2023](#doc-fr_sept_iles_2023) ; Surface multipliée par 70. Prouve : Contexte terminologique décrit ci-dessus. Ne prouve pas : Ni correspondance champ/valeur/export EP 07/2026, ni règle applicable à un projet.

- Question : Quels actes et sous-zonages exacts le producteur regroupe-t-il ? Ne pas confondre ce terme avec toute « protection forte ».

<a id="value-054"></a>

### 054 — Zone de pêche réglementée (Polynésie française)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **35**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Dispositif de réglementation locale de la pêche tenant compte des ressources et pratiques du secteur concerné.

Périmètre documentaire : Polynésie française.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 35. Toutes les autres couches : 0.

- Source : [PF_DRM_MOOREA](#doc-pf_drm_moorea) ; Qu’est-ce qu’une ZPR ?, lignes 43–49. Prouve : Définition générale donnée par l'autorité responsable des ressources marines. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Aucun rattachement individuel des trente-cinq occurrences EP ni inventaire daté équivalent n'est établi.

<a id="value-055"></a>

### 055 — Zone humide protégée par la convention de Ramsar

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **54**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte historique Ramsar : zone humide retenue pour une liste internationale selon son importance écologique.

Périmètre documentaire : Convention internationale sur les zones humides.

Fréquences par couche : `EP/sig_epa.gpkg::sig_epa` = 1 ; `EP/sig_glp.gpkg::sig_glp` = 1 ; `EP/sig_guf.gpkg::sig_guf` = 3 ; `EP/sig_metrop.gpkg::sig_metrop` = 43 ; `EP/sig_mtq.gpkg::sig_mtq` = 1 ; `EP/sig_myt.gpkg::sig_myt` = 1 ; `EP/sig_ncl.gpkg::sig_ncl` = 1 ; `EP/sig_pyf.gpkg::sig_pyf` = 1 ; `EP/sig_reu.gpkg::sig_reu` = 1 ; `EP/sig_subant.gpkg::sig_subant` = 1. Toutes les autres couches : 0.

- Source : [covadis_2013_odt](#doc-covadis_2013_odt) ; content.xml / Tableau46 / RAMSAR ; PDF associé p. 25. Prouve : Documente la catégorie historique du standard. Ne prouve pas : Ne prouve pas son implémentation dans EP 07/2026.

- Source : [ramsar_designation](#doc-ramsar_designation) ; Texte officiel indexé : désignation et articles 2.1-2.2. Prouve : Apporte un contexte limité sur la désignation nationale et les critères internationaux. Ne prouve pas : L'accès direct refusé ne permet pas de revendiquer une revue complète de la page actuelle.

- Question : Quelle documentation du producteur relie le libellé aux sites et limites du snapshot ?

<a id="value-056"></a>

### 056 — Zone marine protégée de la convention OSPAR (Atlantique Nord-est)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **39**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte OSPAR : espace marin soumis à des mesures de protection, conservation, restauration ou précaution écologiques.

Périmètre documentaire : Aire maritime OSPAR de l'Atlantique du Nord-Est.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 39. Toutes les autres couches : 0.

- Source : [ospar_mpa](#doc-ospar_mpa) ; Définition introductive ; objectifs du réseau. Prouve : Décrit les finalités du réseau d'aires marines. Ne prouve pas : N'identifie pas l'édition, les sites ou les mesures locales correspondant à l'export EP.

- Question : Quelle édition OSPAR et quelle règle d'inclusion le producteur a-t-il utilisées ?

<a id="value-057"></a>

### 057 — Zone protégée de la convention d'Apia

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **1**.

État de recherche : `UNRESOLVED`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte historique lié à la convention de conservation de la nature dans le Pacifique Sud ; portée actuelle du libellé EP non établie.

Périmètre documentaire : Pacifique Sud ; portée exacte pour le site EP non établie.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 1. Toutes les autres couches : 0.

- Source : [covadis_2013_odt](#doc-covadis_2013_odt) ; content.xml / Tableau46 / APIA ; PDF associé p. 26. Prouve : Documente une catégorie historique du standard. Ne prouve pas : N'établit pas une protection actuelle du site exporté.

- Source : [sprep_apia_history](#doc-sprep_apia_history) ; Tableau historique indexé : 2006. Prouve : Le texte indexé de la source officielle mentionne une suspension de la convention. Ne prouve pas : La page directement inaccessible ne suffit pas à établir la situation de 2026.

- Source : [sprep_convention_status_2017](#doc-sprep_convention_status_2017) ; Première page indexée : Apia Convention. Prouve : Le document historique indexé date la suspension au 13 septembre 2006. Ne prouve pas : Ne démontre ni les effets actuels ni la disparition d'une protection nationale du site.

- Question : Pourquoi le producteur conserve-t-il cette catégorie dans EP 07/2026 ?

- Question : Quelle portée historique ou juridique lui attribue-t-il, compte tenu de la suspension signalée ?

<a id="value-058"></a>

### 058 — Zone protégée de la convention de Carthagène (Caraïbes)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **8**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte SPAW : dispositif régional de conservation de la biodiversité marine, des habitats et des espèces caraïbes.

Périmètre documentaire : Grande région Caraïbe.

Fréquences par couche : `EP/sig_blm.gpkg::sig_blm` = 1 ; `EP/sig_glp.gpkg::sig_glp` = 3 ; `EP/sig_maf.gpkg::sig_maf` = 3 ; `EP/sig_mtq.gpkg::sig_mtq` = 1. Toutes les autres couches : 0.

- Source : [unep_cep_spaw_areas](#doc-unep_cep_spaw_areas) ; Strengthening and Management of Protected Areas in the Wider Caribbean Region ; Guidelines. Prouve : Présente la gestion et l'inscription de zones au titre du protocole SPAW. Ne prouve pas : Ne démontre pas l'équivalence exacte entre cette liste et les objets EP.

- Source : [unep_cep_spaw_overview](#doc-unep_cep_spaw_overview) ; What is the SPAW Protocol?. Prouve : Situe le protocole dans la protection de la biodiversité marine et côtière caraïbe. Ne prouve pas : N'établit pas le contrat de la colonne type_espace.

- Question : Les objets EP représentent-ils exactement des zones inscrites SPAW, selon quelle édition ?

<a id="value-059"></a>

### 059 — Zone réglementée de pêche de plan de gestion de l'espace maritime (Polynésie française)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **2**.

État de recherche : `UNRESOLVED`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Non établie.

Périmètre documentaire : Polynésie française — suffixe observé; sous-type export exact non résolu.

Fréquences par couche : `EP/sig_pyf.gpkg::sig_pyf` = 2. Toutes les autres couches : 0.

- Source : [PF_DRM_MOOREA](#doc-pf_drm_moorea) ; Et la ZPR de Moorea ?, lignes 52–53. Prouve : Un lien historique PGEM/AMP/ZPR à Moorea; pas la définition de ce libellé composite. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quelles sont les deux zones EP et quel acte définit précisément cette catégorie de PGEM ?

- Question : Ne pas décomposer ni remplacer ce libellé composite par une ZPR générique.

<a id="value-060"></a>

### 060 — Zone spécialement protégée de l'Antarctique

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **1**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte ASPA : zone visant la préservation de valeurs environnementales, scientifiques, historiques, esthétiques ou de nature sauvage, ou la recherche.

Périmètre documentaire : Antarctique ; système du Traité sur l'Antarctique.

Fréquences par couche : `EP/sig_tadl.gpkg::sig_tadl` = 1. Toutes les autres couches : 0.

- Source : [ats_protected_areas](#doc-ats_protected_areas) ; Deux premiers paragraphes : Annexe V, ASPA et ASMA. Prouve : Distingue les finalités ASPA de la coordination d'activités ASMA. Ne prouve pas : N'établit ni le site exact ni la désignation ou le périmètre encodé dans EP.

- Question : Quel acte et quelle édition de périmètre correspondent à l'objet EP sous ce libellé ?

<a id="value-061"></a>

### 061 — Zone tampon d'aire de gestion durable des ressources (Nouvelle-Calédonie - Province Nord)

Champ : `type_espace` ; type : `TEXT`.

Effectif global : **1**.

État de recherche : `UNRESOLVED`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Non établie.

Périmètre documentaire : Nouvelle-Calédonie — Province Nord; suffixe observé.

Fréquences par couche : `EP/sig_ncl.gpkg::sig_ncl` = 1. Toutes les autres couches : 0.

- Source : [NC_NORD_PROTECTION](#doc-nc_nord_protection) ; Les aires protégées, lignes 34–45. Prouve : Définition de l'AGDR seulement; pas celle de sa zone tampon. Ne prouve pas : Contexte institutionnel uniquement : aucun dictionnaire de type_espace ni rattachement des libellés à l'export EP 07/2026 et à ses octets n'est établi.

- Question : Quelle disposition crée et définit cette zone tampon et la distingue de l'AGDR ?

- Question : Des pistes de code/guide provinciaux et du JONC ont été trouvées, mais leurs PDF n'ont pas été lus et rendus dans cette recherche bornée.

<a id="value-062"></a>

### 062 — Géologie

Champ : `objectif_protection` ; type : `TEXT`.

Effectif global : **263**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte du projet de standard : motif géologique de classement, sans correspondance prouvée avec la valeur EP.

Périmètre documentaire : Projet national ENP ; portée exacte du champ exporté non établie.

Fréquences par couche : `EP/sig_metrop.gpkg::sig_metrop` = 263. Toutes les autres couches : 0.

- Source : [cnig_enp_draft_pdf](#doc-cnig_enp_draft_pdf) ; p. 24 : ObjectifProtectionENP / Géologie. Prouve : Ce motif figure dans le projet. Ne prouve pas : N'établit ni correspondance EP ni décodage numérique.

- Question : Le producteur confirme-t-il cette correspondance textuelle pour objectif_protection en juillet 2026 ?

<a id="value-063"></a>

### 063 — Nature

Champ : `objectif_protection` ; type : `TEXT`.

Effectif global : **8813**.

État de recherche : `OFFICIAL_CONTEXT_ONLY`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Contexte du projet de standard : motif naturel de classement, sans correspondance prouvée avec la valeur EP.

Périmètre documentaire : Projet national ENP ; portée exacte du champ exporté non établie.

Fréquences par couche : `EP/sig_blm.gpkg::sig_blm` = 4 ; `EP/sig_cli.gpkg::sig_cli` = 1 ; `EP/sig_epa.gpkg::sig_epa` = 5 ; `EP/sig_glp.gpkg::sig_glp` = 88 ; `EP/sig_guf.gpkg::sig_guf` = 34 ; `EP/sig_maf.gpkg::sig_maf` = 21 ; `EP/sig_metrop.gpkg::sig_metrop` = 8526 ; `EP/sig_mtq.gpkg::sig_mtq` = 63 ; `EP/sig_myt.gpkg::sig_myt` = 23 ; `EP/sig_ncl.gpkg::sig_ncl` = 1 ; `EP/sig_pyf.gpkg::sig_pyf` = 1 ; `EP/sig_reu.gpkg::sig_reu` = 34 ; `EP/sig_spm.gpkg::sig_spm` = 2 ; `EP/sig_subant.gpkg::sig_subant` = 9 ; `EP/sig_tadl.gpkg::sig_tadl` = 1. Toutes les autres couches : 0.

- Source : [cnig_enp_draft_pdf](#doc-cnig_enp_draft_pdf) ; p. 24 : ObjectifProtectionENP / Nature. Prouve : Ce motif figure dans le projet. Ne prouve pas : N'établit ni correspondance EP ni faisabilité d'un projet.

- Question : Quel dictionnaire producteur définit exactement Nature dans cette colonne et ce millésime ?

<a id="value-064"></a>

### 064 — nature

Champ : `objectif_protection` ; type : `TEXT`.

Effectif global : **290**.

État de recherche : `UNRESOLVED`.

Applicabilité au snapshot : `UNRESOLVED`.

Définition de contexte (pas correspondance EP) : Sens exact non établi ; la ressemblance avec Nature ne démontre aucune équivalence officielle de casse.

Périmètre documentaire : Portée du champ exporté non établie.

Fréquences par couche : `EP/sig_glp.gpkg::sig_glp` = 1 ; `EP/sig_guf.gpkg::sig_guf` = 4 ; `EP/sig_metrop.gpkg::sig_metrop` = 272 ; `EP/sig_mtq.gpkg::sig_mtq` = 3 ; `EP/sig_reu.gpkg::sig_reu` = 10. Toutes les autres couches : 0.

- Source : [covadis_2013_odt](#doc-covadis_2013_odt) ; content.xml / Tableau19 / objectifProtection ; PDF associé p. 28. Prouve : Documente historiquement des finalités de protection. Ne prouve pas : N'établit pas l'équivalence nature/Nature dans EP.

- Question : Le producteur documente-t-il nature comme valeur distincte ou variante, sans qu'une normalisation soit présumée ?

## 8. Questions ouvertes et frontière de la prochaine revue

- `producer_export_contract` — `UNRESOLVED` : Quelle édition et quelle spécification d’export relient la conformité CNIG annoncée aux trois noms exacts, valeurs et octets EP 07/2026 ?
  Sources : [pat_ep_download](#doc-pat_ep_download), [pat_ep_release](#doc-pat_ep_release), [covadis_2013_page](#doc-covadis_2013_page), [cnig_2026_consultation](#doc-cnig_2026_consultation).

- `cnig_export_mapping` — `UNRESOLVED` : Quelle spécification du producteur établit les correspondances champ/valeur/version pour EP 07/2026 ?
  Sources : [covadis_2013_page](#doc-covadis_2013_page), [covadis_2013_pdf](#doc-covadis_2013_pdf), [covadis_2013_odt](#doc-covadis_2013_odt), [cnig_enp_draft_pdf](#doc-cnig_enp_draft_pdf).

- `cnig_draft_chronology` — `CONFLICTING_EVIDENCE` : Quelle décision datée résout la contradiction entre le statut de projet et la validation revendiquée dans sa chronologie, sans la présumer applicable à EP ?
  Sources : [cnig_enp_draft_pdf](#doc-cnig_enp_draft_pdf), [cnig_2026_consultation](#doc-cnig_2026_consultation), [cnig_enp_gt](#doc-cnig_enp_gt), [cnig_standards_register](#doc-cnig_standards_register).

- `cnig_visual_inspection` — `UNRESOLVED` : Les pages pertinentes peuvent-elles être examinées visuellement ultérieurement sans modifier la sécurité ni l'environnement gelé ? Le contrôle XML ODT n'est pas une inspection visuelle PDF.
  Sources : [covadis_2013_pdf](#doc-covadis_2013_pdf), [covadis_2013_odt](#doc-covadis_2013_odt), [cnig_enp_draft_pdf](#doc-cnig_enp_draft_pdf).

- `international_limited_access` — `UNRESOLVED` : La documentation actuelle Ramsar et SPREP reste partiellement inaccessible ; distinguer les informations indexées et historiques des pages intégralement consultées.
  Sources : [ramsar_designation](#doc-ramsar_designation), [sprep_apia_history](#doc-sprep_apia_history), [sprep_convention_status_2017](#doc-sprep_convention_status_2017).

- `cnig_no_cross_field_join` — `UNRESOLVED` : Les domaines marginaux n'établissent aucune cooccurrence entre les trois champs ; aucune correspondance de ligne ne doit en être fabriquée.

- `raw_delimiter_contract` — `UNRESOLVED` : Le producteur définit-il une grammaire de valeurs composées ? Aucune séparation de virgules ou parenthèses n’est autorisée par les documents trouvés.
  Sources : [pat_ep_release](#doc-pat_ep_release), [covadis_2013_pdf](#doc-covadis_2013_pdf), [cnig_enp_draft_pdf](#doc-cnig_enp_draft_pdf).

- `null_statut_and_case` — `UNRESOLVED` : Que signifient les 11381 NULL de statut et les variantes Nature/nature ? Ni absence de restriction ni équivalence de casse ne sont établies.
  Sources : [pat_ep_release](#doc-pat_ep_release), [sandre_390](#doc-sandre_390), [cnig_enp_draft_pdf](#doc-cnig_enp_draft_pdf).

- `jurisdiction_and_dates` — `UNRESOLVED` : Quels actes, dates et périmètres sont effectivement rattachés aux catégories locales, saisonnières ou historiques du snapshot ? Une page actuelle ou un exemple local ne suffit pas.
  Sources : [NC_NORD_PROTECTION](#doc-nc_nord_protection), [NC_SUD_CARTE_REGLEMENTATION](#doc-nc_sud_carte_reglementation), [PF_DIREN_ESPACES](#doc-pf_diren_espaces), [PF_DRM_MOOREA](#doc-pf_drm_moorea), [fr_sept_iles_2023](#doc-fr_sept_iles_2023), [sprep_apia_history](#doc-sprep_apia_history).

- `source_consistency_tadl` — `UNRESOLVED` : L’observation physique approuvée sig_tadl (CRS déclaré et coordonnées) reste inchangée et non résolue ; ce dossier sémantique n’apporte aucune correction géométrique.

- `producer_access_limitations` — `UNRESOLVED` : Les liens INPN/SINP inaccessibles et la fiche historique non examinée visuellement ne peuvent combler les correspondances absentes ; l’absence de preuve trouvée n’est pas une preuve d’inexistence.
  Sources : [inpn_reference_unavailable](#doc-inpn_reference_unavailable), [inpn_program_unavailable](#doc-inpn_program_unavailable), [sinp_standards_unavailable](#doc-sinp_standards_unavailable), [inpn_rnn_2022_indexed](#doc-inpn_rnn_2022_indexed).

Les questions propres à un futur projet restent séparées : identifier les actes, versions, périmètres et autorités applicables au lieu concerné, puis faire examiner les règles particulières par une personne compétente. Ce dossier ne fournit aucune réponse d’autorisation, d’exclusion ou d’acceptabilité BESS. La revue indépendante doit déterminer ce qui pourra être traduit dans un futur contrat exécutable ; rien ici ne l’active automatiquement.

## 9. Réseaux, reproductibilité et audits

Préparation EP **hors réseau** : cache de téléchargement et extraction valides, DNS = HTTP = téléchargement = 0. Seules les fonctions publiques et leurs deux lecteurs existants ont été utilisés : 45 lectures attributaires / 34143 lignes ; 45 snapshots SQLite et 45 SELECT FID+BLOB / 34143 lignes ; 285 `list_layers` et 285 `read_info`. Une copie marginale répétée donne le même inventaire, sans aucun appel de lecteur. Durée totale : 144,831 secondes. Aucune réparation, reprojection, lecture géométrique Pyogrio ou analyse parcellaire.

Recherche documentaire **en ligne**, distincte : consultation de pages primaires et de petits documents officiels hors dépôt, avec limitations explicites. Le zéro réseau de la vérification EP ne décrit pas l’ensemble de cette tâche.

L’audit temporaire hors dépôt contrôle les 45 profils, les 64 clés exactes et 960 fréquences par couche, toutes les égalités de sommes/nulls, la résolution des identifiants documentaires, les états non confirmés et l’accord des sections Markdown/JSON. Il ne prouve pas un sens absent des sources. Les tests existants restent inchangés ; les résultats définitifs et les contrôles de bytes sont consignés dans [DEV_LOG](../DEV_LOG.md).

## 10. Petit schéma de recherche JSON

Version de recherche `reference_schema_version = 1`, distincte des schémas techniques inchangés. UTF-8 strict, racine objet, aucune clé dupliquée, aucun NaN/Infinity. Listes déterministes et effectifs entiers exacts. Pas de chargeur, modèle runtime ou migration.

| Clé | Contrat de ce dossier |
|---|---|
| `reference_schema_version` | Version 1 du document de recherche seulement. |
| `status` | RESEARCH_DRAFT_NOT_RUNTIME_POLICY. |
| `source_bindings` | Identités et SHA techniques exacts, comptes et toolchain. |
| `research_method` | Périmètre, conservation des valeurs et absence de cooccurrence. |
| `source_documents` | Identifiant unique id ; URL, éditeur, titre/date/version/statut, date de consultation et localisateurs ; SHA uniquement pour octets obtenus. |
| `field_definitions` | Trois champs ; contexte documentaire, correspondance non établie et références ; tout domaine candidat est explicitement hors observation EP. |
| `observed_field_profiles` | 45 profils complets copiés de l’inventaire validé : noms/positions/dtypes/comptes/domaines/column_content_sha256 et lignage de package. |
| `field_summaries` | Trois totaux marginaux avec nulls séparés. |
| `observed_value_entries` | Clé composite unique (field_name,value_kind,canonical_value) ; global_count et 15 per_layer_counts ; définition de contexte nullable, périmètre, research_state et snapshot_applicability séparés, sources et questions. |
| `unresolved_questions` | Questions globales identifiées ; source_ids résolvables ; conflit documentaire séparé des valeurs observées. |
| `offline_verification` | Compte rendu mesuré de la seule vérification EP, non une règle opérationnelle. |

États de recherche : `CONFIRMED_FOR_SNAPSHOT` exigerait une preuve explicite du lien champ/valeur/snapshot ; `OFFICIAL_CONTEXT_ONLY` décrit un contexte officiel, éventuellement local ou historique ; `UNRESOLVED` indique que la définition exacte manque ; `CONFLICTING_EVIDENCE` indique une contradiction documentaire identifiée. Ces états ne sont ni des classes de parcelles ni des décisions de projet.
