# IHMN - Projet de refonte du site web

## Vue d'ensemble

Ce depot centralise le travail de preparation de la refonte du site IHMN (https://ihmn.be).

L'objectif principal est de:

- comprendre et documenter le site actuel
- structurer les contenus (formations, pages institutionnelles, therapeutes, FAQ, documents)
- preparer une architecture plus claire pour le futur site
- conserver une base de reference exploitable pour la suite du projet

Ce repository est donc un espace de cadrage, d'analyse et d'organisation de contenu avant la mise en production d'un nouveau site.

## Perimetre de ce README

Ce README decrit volontairement le projet et la structure du repository hors dossier design.

## Etat actuel du projet (mars 2026)

Le projet est dans une phase de structuration avancee:

- inventaire detaille du site actuel deja constitue
- analyse des pages, des formations et de l'annuaire des therapeutes
- collecte de ressources du site existant (HTML et fichiers associes)
- scripts disponibles pour extraire et consolider les informations
- documentation de pilotage presente, avec certaines sections encore a completer

En resume: le socle documentaire et d'inventaire est bien en place, et sert de base pour la refonte.

## Synthese des issues GitHub (lecture via GH CLI)

Reference repo: https://github.com/mgamsdve/ihmn

Photo du backlog au 14 mars 2026:

- 37 issues au total
- 31 issues ouvertes
- 6 issues fermees

Repartition des priorites sur les issues ouvertes:

- 15 en priorite haute
- 8 en priorite moyenne
- 1 en priorite basse
- 7 sans priorite explicite (principalement des EPICs de pilotage)

## Ce qui est deja termine

La premiere brique du projet est cloturee:

- EPIC 1 ferme: inventaire complet du contenu actuel
- Issues 1.1 a 1.5 fermees: institutionnel, formations, annuaire therapeutes, PDF, FAQ

En clair, la base de connaissance du site existant est construite.

## Ce qui reste ouvert (en gros)

Le backlog encore ouvert suit une logique de progression claire, de l'analyse vers la preparation de la phase suivante:

1. EPIC 2: analyse de l'architecture actuelle (navigation, URLs, maillage, audit CMS)
2. EPIC 3: audit UX (parcours inscription, accessibilite, CTA, mobile)
3. EPIC 4: audit SEO (metadonnees, mots-cles, performances, schema/backlinks)
4. EPIC 5: synthese des problemes et opportunites
5. EPIC 6: definition de la future architecture et du sitemap
6. EPIC 7: mapping des contenus + plan de redirections + plan editorial de migration
7. EPIC 8: rapport final de Phase 1 + brief de Phase 2 + retrospective client

## Structure actuelle du repository (hors design)

```text
ihmn/
|- Docs/
|  |- **projects**/
|  |  |- current-site-analysis.md
|  |  \- site-architecture.md
|  |- project/
|  |  |- decisions.md
|  |  |- ihmn-web-offer.md
|  |  |- meetings.md
|  |  |- notes.md
|  |  \- roadmap.md
|  |- site/
|  |  |- analysis/
|  |  |  |- issues.md
|  |  |  \- strengths.md
|  |  |- architecture/
|  |  |  |- navigation.md
|  |  |  \- sitemap.md
|  |  |- current-site/
|  |  |  |- formations/
|  |  |  |- institut/
|  |  |  |- therapeutes/
|  |  |  |- INVENTAIRE_COMPLET_IHMN_2026.md
|  |  |  |- overview.md
|  |  |  \- pages.md
|  |  |- pages/
|  |  |  |- admissions.md
|  |  |  |- blog.md
|  |  |  |- formation-naturopathie.md
|  |  |  |- homepage.md
|  |  |  \- therapeutess.md
|  |  |- content-model.md
|  |  |- current-site-analysis.md
|  |  |- design-direction.md
|  |  |- seo-plan.md
|  |  \- site-architecture.md
|  \- technical/
|     |- cms-structure.md
|     |- data-model.md
|     |- deployment.md
|     \- tech-stack.md
|- scripts/
|  |- faq.py
|  |- jsonscrap.py
|  |- meta.py
|  |- pdf.py
|  |- scrapFormation.py
|  |- therapeutes.py
|  |- IHMN - Bourse 2025-26.pdf
|  |- ihmn---tarifs-2025-26.pdf
|  \- ihmn_25-26_contrat_inscription_1e-anne.pdf
|- web-scrap/
|  |- Drainage lymphatique manuel (formation).html
|  |- Examens & Certificats.html
|  |- Formations hors cursus (formation).html
|  |- Formations.html
|  |- Hygiene Vitale et Nutrition (formation).html
|  |- Inscriptions & Tarifs.html
|  |- Naturopathie (formation).html
|  \- configFolder/
\- year_structure.json
```

## Role des dossiers principaux

### Docs/

Dossier coeur du projet documentaire.

- `project/` contient le cadrage global du projet (objectifs, orientation, suivi).
- `site/` contient l'analyse du site actuel, la structure cible et la preparation des futures pages.
- `site/current-site/` contient l'inventaire detaille du site existant (pages, formations, therapeutes).
- `technical/` existe deja comme espace de reference, mais reste volontairement peu detaille a ce stade.

### scripts/

Scripts utilitaires de collecte et d'analyse de contenu.

Leur role global:

- recuperer des informations depuis le site actuel
- extraire des donnees (FAQ, therapeutes, formations, metadonnees, PDF)
- produire des inventaires exploitables pour la documentation

### web-scrap/

Archive de pages HTML et ressources associees recuperees depuis le site existant.

Ce dossier sert de reference de contenu et de structure pour travailler hors ligne, comparer les pages, et verifier les informations a migrer.

### year_structure.json

Fichier de reference de la structure pedagogique (annees 1 a 4) et des modules de formation associes.

## Ce que le projet couvre fonctionnellement

Le travail actuel couvre les blocs de contenu majeurs du site IHMN:

- presentation de l'ecole et informations institutionnelles
- offre de formations (naturopathie, hygiene de vie et nutrition, drainage lymphatique, hors cursus)
- admissions, examens, certificats, tarifs
- annuaire des therapeutes (repartition geographique, fiches, pagination)
- FAQ et informations de contact
- documents administratifs PDF

## Vision cible deja posee

Les documents existants posent deja une structure cible claire autour de:

- Accueil
- Formations
- Admissions
- L'ecole
- Therapeutes
- Blog
- FAQ
- Contact

Cette base sert de fil conducteur pour la suite de la refonte.

## Prochaines priorites (contenu et organisation)

- finaliser les sections de documentation encore vides
- homogeniser les inventaires et conventions de nommage
- valider la structure cible page par page
- preparer la migration des contenus prioritaires

## Source de reference

Site actuel analyse: https://ihmn.be

## Autre document : 
Docs des erreurs du site actuel : https://docs.google.com/document/d/1XI-_SjZgNvJTdke4OqBZ9DcyvGulNmndoXHAmBo2jm0/edit?usp=sharing 