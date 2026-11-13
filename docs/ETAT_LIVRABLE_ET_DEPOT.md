# État du travail et procédure de dépôt

**Binôme :** KEUMEKA SOKING WILFRIED GULLIT ; NOUMEME WEMBOU ARNAULD.

**Dépôt :** https://github.com/juste0283-prog/tpsec

## Travail documentaire disponible
- Analyse de la topologie, des politiques de sécurité et de la méthode de déploiement.
- Gabarits de configurations pour les trois routeurs et le serveur Ubuntu.
- Référentiel de 22 vérifications détaillées par routeur et trois essais indépendants de révocation RADIUS.
- Argumentation de l'utilisation uRPF loose sur une bordure multi-opérateurs.
- Rapport Word de cinq pages dans `rapport/Compte_rendu_TP3_Livrable.docx`.

## Limites des preuves
La présence d'un fichier de configuration, d'une commande ou d'une réponse attendue ne prouve pas son application effective. Les captures réelles, les journaux d'administration et les taux NSA ne sont pas déductibles des documents. La grille NSA officielle mentionnée par l'énoncé n'était pas jointe au corpus reçu : `audit/NSA.md` est une synthèse de travail et non sa reproduction.

## Vérification du dépôt avant intégration
1. S'assurer que le PDF historique présent sur `main` n'est pas supprimé.
2. Vérifier que seul le rapport `Compte_rendu_TP3_Livrable.docx` figure dans `rapport/` au titre des comptes rendus Word.
3. Contrôler `git status`, `git diff --cached --stat` et `git diff --cached` après le staging.
4. Vérifier qu'aucun mot de passe réel, secret RADIUS, clé privée ou journal nominatif n'est partagé.
5. Pousser la branche `feature/tp3-hardening-complete`, puis demander une revue avant fusion.

## Commandes de contrôle (PowerShell)
```powershell
cd C:\Users\Wilfried\tpsec
python .\tests\VERIFIER_AVANT_PUSH.py
git status
git add README.md .gitignore CONTRIBUTING.md audit configurations docs rapport serveur-admin tests
git diff --cached --stat
git diff --cached --check
```
