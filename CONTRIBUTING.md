# Workflow du binôme
Branches suggérées : `main` (validé), `dev` (intégration), `feature/wilfried-infrastructure`, `feature/arnauld-routeurs`, `feature/audit-nsa`.
- Avant un push : `git status`, `git diff --cached`, vérifier l'absence de secrets et de données sensibles.
- Aucun résultat de test, capture ou journal synthétique ne doit être présenté comme réel.
- Une PR par bloc de travail, revue croisée, intégration sur dev, puis PR finale vers main.
- Pousser les exports **expurgés**, les preuves redimensionnées et légendées, la grille renseignée et le rapport effectivement déposé.
- Le repo du groupe est public : éviter tout identifiant d'accès réel dans les commits, y compris dans l'historique Git.
