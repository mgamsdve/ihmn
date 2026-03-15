# Issue 3.2 — Analyse de la navigation et de l’accessibilité

## Contexte

Dans le cadre de l’audit du site https://ihmn.be, cette analyse vise à évaluer la qualité de la navigation et l’accessibilité globale du site pour différents types d’utilisateurs.

L’objectif est d’identifier les obstacles potentiels à la navigation et à la compréhension de l’interface, notamment en ce qui concerne :

* la structure du menu principal
* la lisibilité des éléments de navigation
* l’accessibilité clavier
* la hiérarchie visuelle des contenus
* les contrastes de couleurs
* la cohérence visuelle globale

Cette analyse s’appuie sur une évaluation heuristique basée sur les principes d’accessibilité web (WCAG) et les bonnes pratiques UX.

---

# Méthodologie

L’évaluation repose sur :

* observation manuelle de la navigation sur plusieurs pages
* analyse du header et du footer
* tests de navigation au clavier
* analyse des contrastes visuels
* vérification de la hiérarchie visuelle des contenus

Les critères évalués sont :

* structure et logique de navigation
* visibilité des éléments interactifs
* accessibilité clavier
* lisibilité et typographie
* cohérence visuelle globale

---

# Analyse de la navigation

## Menu principal (header)

Le header est présent sur toutes les pages du site et constitue l’élément principal de navigation.

Il contient :

* le logo de l’IHMN (lien vers la page d’accueil)
* le menu principal
* une icône de recherche
* un lien vers Facebook

### Structure du menu

Le menu principal comporte les entrées suivantes :

* Accueil
* Formations
* IHMN
* FAQ
* Thérapeutes
* Contact

Le menu **Formations** contient un sous-menu permettant d’accéder aux différentes formations et aux pages administratives associées.

### Points positifs

* nombre d’items limité
* structure simple et compréhensible
* accès direct aux principales sections du site
* comportement standard du logo (retour à l’accueil)

### Points perfectibles

Certaines pages administratives sont intégrées dans le menu des formations :

* Inscriptions & tarifs
* Examens & certificats

Ce mélange entre contenus pédagogiques et administratifs peut rendre la navigation moins intuitive.

---

# Analyse du footer

Le footer est identique sur toutes les pages du site.

Il contient principalement :

* lieu des cours
* siège social
* coordonnées de contact
* logo de la World Naturopathic Federation
* lien vers les mentions légales

### Points positifs

* informations institutionnelles clairement affichées
* coordonnées complètes facilement accessibles
* cohérence visuelle avec le reste du site

### Points perfectibles

Le footer joue essentiellement un rôle informatif et ne propose pas de navigation secondaire.

Seul lien présent :

* Mentions légales

Dans de nombreux sites, le footer permet également d’accéder à des pages importantes telles que :

* formations
* FAQ
* contact
* politique de confidentialité

L’absence de navigation secondaire limite son rôle dans l’orientation des utilisateurs.

---

# Navigation au clavier

Un test de navigation clavier a été réalisé à l’aide de la touche **TAB**.

### Comportement observé

* la touche TAB permet de naviguer entre les liens
* les champs de formulaire reçoivent correctement le focus
* les éléments interactifs sont accessibles

Cependant, certains menus déroulants semblent dépendre principalement du comportement de **survol (hover)**.

### Impact potentiel

Cette dépendance peut rendre l’interaction moins intuitive pour :

* les utilisateurs naviguant uniquement au clavier
* certains lecteurs d’écran.

---

# Analyse des contrastes (WCAG)

L’analyse visuelle montre plusieurs contrastes insuffisants entre le texte et les arrière-plans.

### Exemple : footer

Le footer utilise :

* un fond vert turquoise
* du texte blanc ou gris clair

Certains éléments présentent un contraste faible, notamment :

* le lien "Mentions légales"

Ces contrastes peuvent être inférieurs aux recommandations WCAG AA.

---

# Lisibilité des contenus

La lisibilité globale du site est correcte.

### Points positifs

* typographie simple
* taille de texte généralement lisible
* paragraphes relativement courts

### Points perfectibles

Certaines pages présentent :

* de longues listes de contenu
* peu de séparation visuelle entre les sections

Cela peut rendre la lecture plus difficile sur certaines pages.

---

# Hiérarchie visuelle

La hiérarchie visuelle des pages suit généralement une structure claire :

```
H1
H2
paragraphes
listes
```

Cependant certaines pages présentent :

* des sections longues
* peu de séparation entre blocs de contenu

Une structuration plus marquée pourrait améliorer la lisibilité.

---

# Analyse du moteur de recherche

Le site possède une fonction de recherche accessible depuis le header.

### Problèmes observés

Dans certains cas, la recherche ne retourne pas de résultats alors que des contenus correspondants existent sur le site.

Exemple :

recherche : **"naturopathie"**

résultat :

```
Aucun résultat de recherche correspondant
```

Ce comportement peut indiquer :

* un index incomplet du moteur de recherche
* une configuration incorrecte du système de recherche.

### Impact UX

Un moteur de recherche inefficace peut :

* empêcher les utilisateurs de trouver rapidement l’information recherchée
* réduire la confiance dans la navigation du site.

---

# Cohérence visuelle

Le design du site est globalement cohérent.

Les éléments suivants restent constants sur l’ensemble des pages :

* header
* footer
* palette de couleurs
* typographie principale

Cependant certains éléments pourraient être améliorés :

* contrastes de couleurs
* hiérarchie visuelle des contenus
* organisation du footer.

---

## Utilisation des attributs ARIA

Plusieurs attributs ARIA sont présents dans le code HTML, notamment :

- aria-current="page" dans la navigation principale
- aria-label pour certains champs de formulaire
- aria-hidden="true" pour certaines icônes décoratives

Ces attributs contribuent à améliorer l'accessibilité pour les technologies d'assistance.

Cependant, l'utilisation d'ARIA semble limitée et ne remplace pas toujours les bonnes pratiques HTML natives (par exemple l'utilisation de balises <label> pour les champs de formulaire).

---

# Score global d’accessibilité et de navigation

Évaluation heuristique basée sur les critères analysés :

| Critère               | Score  |
| --------------------- | ------ |
| Navigation générale   | 7 / 10 |
| Lisibilité            | 6 / 10 |
| Contraste visuel      | 4 / 10 |
| Navigation clavier    | 6 / 10 |
| Accessibilité globale | 5 / 10 |

Score global estimé :

**5.5 / 10**

---

# Liste priorisée des problèmes

## Priorité haute

* contraste insuffisant dans certains éléments de navigation
* moteur de recherche peu fiable
* dépendance partielle au hover pour certains menus

---

## Priorité moyenne

* absence de navigation secondaire dans le footer
* hiérarchie visuelle perfectible sur certaines pages

---

## Priorité faible

* amélioration générale de la lisibilité de certaines sections
* optimisation esthétique de certains éléments.

---

# Recommandations

Pour améliorer la navigation et l’accessibilité lors de la refonte :

### améliorer les contrastes

vérifier les contrastes selon les normes WCAG AA.

---

### améliorer la navigation clavier

permettre l’ouverture des menus avec :

```
ENTER
SPACE
```

---

### améliorer la structure du footer

ajouter une navigation secondaire incluant :

* formations
* FAQ
* contact
* politique de confidentialité

---

### améliorer le moteur de recherche

vérifier l’indexation des contenus et améliorer la pertinence des résultats.

---

# Conclusion

La navigation du site IHMN est globalement simple et compréhensible, mais plusieurs points d’amélioration ont été identifiés.

Les principaux problèmes concernent :

* les contrastes visuels
* la fiabilité du moteur de recherche
* l’absence de navigation secondaire dans le footer
* certaines limites d’accessibilité clavier

Une refonte du site permettra d’améliorer significativement l’accessibilité et l’expérience de navigation pour l’ensemble des utilisateurs.
