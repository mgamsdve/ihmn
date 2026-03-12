# Structure des formations

## Pages formations actuellement publiées

- `/formations`
- `/formations/naturopathie`
- `/formations/hygiene-de-vie-et-nutrition`
- `/formations/drainage-lymphatique-manuel`
- `/formations/formations-hors-cursus`
- `/formations/examens-certificats`
- `/formations/inscriptions-tarifs`

## Logique actuelle

La section formations regroupe à la fois :

- une page hub générale
- les pages de formation
- les informations d'examens et certificats
- les informations d'inscription et de tarifs

La formation en naturopathie semble structurée par années, avec une granularité par modules.

## Structure pédagogique observée

Exemple : naturopathie.

Formation :

- Année 1
- Année 2
- Année 3
- Année 4

Chaque année contient plusieurs modules.

## Données visibles par module

Chaque module peut comporter :

- titre
- formateur
- durée
- description
- objectifs pédagogiques
- méthodologie

Les détails sont affichés dans une fenêtre modale.

## Mapping vers la nouvelle architecture

| Ancienne URL | Nouvelle section |
| --- | --- |
| `/` | Accueil |
| `/formations` | Formation Naturopathie |
| `/formations/naturopathie` | Formation Naturopathie |
| `/formations/examens-certificats` | Formation Naturopathie → Examens |
| `/formations/inscriptions-tarifs` | Admissions |
| `/formations/hygiene-de-vie-et-nutrition` | Formation Hygiène de vie |
| `/formations/drainage-lymphatique-manuel` | Formation Drainage |
| `/formations/formations-hors-cursus` | Formations complémentaires |
| `/ihmn` | L'école |
| `/ihmn/lhistoire-ihmn` | L'école → Histoire |
| `/ihmn/en-pratique` | L'école → Organisation |
| `/ihmn/formateurs` | L'école → Formateurs |
| `/nos-therapeuthes` | Thérapeutes |
| `/faq` | FAQ |
| `/contact` | Contact |
| `/mentions-legales` | Mentions légales |
