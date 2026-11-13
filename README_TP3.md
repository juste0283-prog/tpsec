# TP3 — Durcissement des équipements réseau (R-SIEGE, R-DLA, R-FAI)

**Auteurs :** KEUMEKA SOKING WILFRIED GULLIT et NOUMEME WEMBOU ARNAULD.  
**Dépôt du groupe :** https://github.com/juste0283-prog/tpsec

## Contenu du travail
- `rapport/Compte_rendu_TP3_Livrable.docx` : synthèse rédigée, noire et blanche, sur cinq pages; analyse, topologie, justification, référentiel de tests, limites du résultat.
- `configurations/` : configurations de référence Cisco IOSv, MikroTik CHR 7.x et VyOS 1.4, à appliquer par blocs en suivant les sécurités de retour arrière.
- `serveur-admin/` : Netplan, FreeRADIUS, rsyslog, chrony, installation Ubuntu.
- `tests/` : 22 contrôles techniques des routeurs, 3 contrôles de révocation, inventaire et détecteur de secrets.
- `audit/` : grille NSA de synthèse, étude des écarts, format de chronologie.
- `docs/` : analyse technique, protocole reproductible et sources officielles.

## État de validité
Les configurations, interprétations et réponses théoriques sont fournies. Le compte rendu ne déclare **aucune réussite expérimentale non observée**. Une simulation ou une attente de résultat ne se substitue pas à une capture issue d'EVE-NG. La grille officielle du support n'a pas été fournie.

## Mise en œuvre
1. Préparer la topologie TP0.1 et VLAN TP2.1 et sauvegarder les configurations initiales.
2. Préparer le serveur Ubuntu 10.10.99.20 et vérifier les routes retour.
3. Exécuter TP3.1, TP3.2 et TP3.3 en mode sécurisé (Safe Mode, reload in 10, commit-confirm).
4. Procéder au scénario prestataire.temp et établir la chronologie depuis syslog.
5. Réaliser les captures et intégrer la grille NSA officielle et les mesures dans le rapport remis.

## Publication
Ne jamais committer mots de passe, secrets RADIUS/SNMP, clés privées, exports contenant des identifiants ou journaux nominatifs bruts. Vérifier chaque diff avant un push. La Pull Request doit être relue par les deux membres.

## Livrable remis
Le rapport du binôme est `rapport/Compte_rendu_TP3_Livrable.docx` (5 pages, noir et blanc). Les contrôles détaillés dans ce rapport expriment les résultats attendus, pas des validations expérimentales. Le PDF déjà présent à la racine du dépôt GitHub appartient à l'historique du groupe et ne doit pas être supprimé lors de l'intégration du dossier.

## Intégration de cette archive
Décompresser ce ZIP puis copier son **contenu** dans `C:\Users\Wilfried\tpsec` : les dossiers doivent se trouver à la racine du dépôt, sans dossier supplémentaire. Exécuter `python tests/VERIFIER_AVANT_PUSH.py`, puis `git status`, `git diff --cached` après `git add`. Éviter tout push de secrets ou de captures contenant des identifiants.
