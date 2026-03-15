# Analyse de la navigation du site — IHMN (2026)

## Description

Ce document analyse la structure de navigation actuelle du site https://ihmn.be.

L’objectif est de comprendre :

- l’organisation des menus
- la hiérarchie des pages
- la cohérence entre navigation et architecture réelle
- le comportement mobile
- les problèmes d’ergonomie et d’accessibilité

Cette analyse sert de base pour la future restructuration du site.

---

# 1. Structure générale de la navigation

La navigation principale du site est organisée autour d’un **menu principal situé dans le header**.

Structure actuelle :

| Item | URL |
|-----|-----|
| Accueil | / |
| Formations | /formations |
| IHMN | /ihmn |
| FAQ | /faq |
| Thérapeutes | /nos-therapeuthes |
| Contact | /contact |

Ce menu est présent sur toutes les pages du site.

---

# 2. Sous-menus

## Formations

Le menu "Formations" contient les pages suivantes :

| Page | URL |
|-----|-----|
| Naturopathie | /formations/naturopathie |
| Hygiène de vie et nutrition | /formations/hygiene-de-vie-et-nutrition |
| Drainage lymphatique manuel | /formations/drainage-lymphatique-manuel |
| Formations hors cursus | /formations/formations-hors-cursus |
| Inscriptions & tarifs | /formations/inscriptions-tarifs |
| Examens & certificats | /formations/examens-certificats |

Observation :

Les pages administratives (inscriptions, examens) sont mélangées avec les formations.

---

## IHMN

Le menu "IHMN" contient :

| Page | URL |
|-----|-----|
| Histoire de l'IHMN | /ihmn/lhistoire-ihmn |
| En pratique | /ihmn/en-pratique |
| Formateurs | /ihmn/formateurs |

Cette section regroupe les pages institutionnelles de l’école.

---

# 3. Navigation secondaire

## Footer

Le footer est identique sur toutes les pages.

Il contient :

- lieu des cours
- siège social
- coordonnées de contact
- lien vers les mentions légales
- logo World Naturopathic Federation
- lien Facebook

Le footer joue principalement un rôle **informatif** et très peu un rôle de navigation.

Observation :

Peu de liens utiles sont présents dans le footer.

---

# 4. Navigation contextuelle

Certaines pages proposent une navigation interne limitée.

Exemple :

pages de formations :

- modules de cours
- descriptions des modules
- formateurs

Cependant ces contenus sont souvent affichés dans **des fenêtres modales** et ne disposent pas toujours d’URL propre.

Conséquence :

- navigation limitée
- contenu difficile à indexer.

---

# 5. Profondeur de navigation

Profondeur maximale observée :

| Niveau | Exemple |
|------|------|
| 0 | Accueil |
| 1 | Formations |
| 2 | Formation spécifique |
| 3 | Modules (popup/modal) |

La profondeur reste raisonnable, mais certains contenus importants ne sont pas accessibles via des pages dédiées.

---

# 6. Navigation mobile

Sur mobile :

- le menu devient un **menu hamburger**
- les sous-menus sont affichés sous forme d’accordéons.

Structure du menu mobile :

- Accueil
- Formations
- IHMN
- FAQ
- Thérapeutes
- Contact

---

# 7. Problèmes observés sur mobile

## Lisibilité du menu

Les sous-pages du menu "Formations" apparaissent avec un **contraste très faible**.

Conséquence :

les liens sont difficilement lisibles.

Cela constitue un problème d’accessibilité.

---

## Scroll excessif

Certaines pages nécessitent un **scroll très important**.

Exemple :

pages de modules de formation.

Conséquence :

navigation peu confortable sur mobile.

---

## Widgets non adaptés

Certains widgets externes (ex : Facebook) apparaissent mal adaptés aux écrans mobiles.

Problèmes observés :

- blocs vides
- mauvaise mise en page.

---

# 8. Cohérence navigation / structure

La navigation principale correspond globalement à la structure du site.

Cependant certains contenus importants ne sont pas accessibles directement via la navigation :

- modules de formation
- détails pédagogiques
- certaines informations internes.

---

# 9. Pages potentiellement orphelines

Plusieurs contenus importants ne disposent pas d’URL propre :

- fiches modules
- contenus pédagogiques détaillés.

Ces contenus sont donc :

- difficiles à indexer
- difficilement partageables.

---

# 10. Analyse UX

Points positifs :

- navigation simple
- peu d’items
- hiérarchie globale compréhensible
- accès direct aux formations.

Points perfectibles :

- navigation secondaire limitée
- contenus pédagogiques peu accessibles
- structure du menu formations peu logique
- expérience mobile perfectible.

---

# 11. Recommandations pour la refonte

Plusieurs améliorations sont recommandées.

## Clarifier la structure du menu

Séparer les formations et les informations administratives.

Exemple :

Formations
- naturopathie
- hygiène de vie et nutrition
- drainage lymphatique manuel
- formations hors cursus

Admissions
- inscriptions
- tarifs
- organisation des cours

---

## Donner des URL aux contenus pédagogiques

Créer des pages dédiées pour :

- les années de formation
- les modules
- les contenus pédagogiques.

---

## Améliorer la navigation mobile

Améliorer :

- le contraste des menus
- l’organisation des contenus
- la lisibilité des sous-menus.

---

## Améliorer le footer

Ajouter des liens utiles :

- formations
- FAQ
- contact
- admissions.

---

# Conclusion

La navigation actuelle du site IHMN est globalement simple et fonctionnelle.

Cependant elle présente plusieurs limites :

- certains contenus importants sont difficiles à atteindre
- l’organisation du menu pourrait être améliorée
- l’expérience mobile présente plusieurs problèmes d’ergonomie.

Cette analyse servira de base pour la refonte de l’architecture du site et l’amélioration de l’expérience utilisateur.