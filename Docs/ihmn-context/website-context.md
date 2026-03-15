# IHMN — Contexte et structure du site web

## Informations techniques

- **URL** : https://ihmn.be
- **CMS** : Joomla (avec Gridbox/BaBuilder)
- **Langue** : Français uniquement
- **Domaine canonique** : https://ihmn.be (redirection www correcte)

---

## Structure globale du site

Le site actuel comporte **12 pages structurées**, organisées en 6 pages principales et 6 pages secondaires/sous-pages.

### Pages principales

| URL | Titre | Rôle |
|-----|-------|------|
| `/` | La Naturopathie, une Passion, un Art, un Métier | Page d'accueil : présentation de l'école, formations, témoignages |
| `/formations` | Formations | Hub listant les 4 formations + pages administratives |
| `/ihmn` | IHMN | Présentation institutionnelle de l'école |
| `/faq` | FAQ | Questions-réponses organisées en 6 catégories (~30 questions) |
| `/nos-therapeuthes` | Thérapeutes | Annuaire des 39 praticiens formés par l'IHMN |
| `/contact` | Contact | Formulaire de contact + carte Google Maps |

### Sous-pages formations

| URL | Titre | Rôle |
|-----|-------|------|
| `/formations/naturopathie` | Naturopathie | Programme détaillé sur 4 ans |
| `/formations/hygiene-de-vie-et-nutrition` | Hygiène de Vie et Nutrition | Programme sur 2 ans |
| `/formations/drainage-lymphatique-manuel` | Drainage Lymphatique Manuel | Programme sur 1 an |
| `/formations/formations-hors-cursus` | Formations Hors Cursus | Séminaires complémentaires |
| `/formations/examens-certificats` | Examens & Certificats | Conditions de certification |
| `/formations/inscriptions-tarifs` | Inscriptions & Tarifs | Informations administratives |

### Sous-pages institutionnelles

| URL | Titre | Rôle |
|-----|-------|------|
| `/ihmn/lhistoire-ihmn` | Historique | Histoire de l'école depuis 1976 |
| `/ihmn/en-pratique` | En pratique | Lieu, horaires, accès |
| `/ihmn/formateurs` | Nos formateurs | Grille de 17 profils |

### Autres pages

| URL | Titre | Rôle |
|-----|-------|------|
| `/mentions-legales` | Mentions légales | PDF téléchargeable |

### Pages de l'annuaire thérapeutes

- 9 pages régionales (`/nos-therapeuthes/[region]`)
- ~39 pages individuelles (`/nos-therapeuthes/[region]/[nom]`)
- Pagination (`/nos-therapeuthes?page=1` à `?page=4`)

---

## Navigation

### Menu principal (header)

Le header est identique sur toutes les pages et contient :
- **Logo IHMN** (lien vers l'accueil)
- **Menu principal** : Accueil, Formations, IHMN, FAQ, Thérapeutes, Contact
- **Icône Facebook**
- **Icône de recherche**

### Sous-menus

Le menu **Formations** déploie un menu déroulant avec les 6 sous-pages (4 formations + inscriptions + examens).

Le menu **IHMN** déploie un menu déroulant avec les 3 sous-pages (Histoire, En pratique, Formateurs).

### Footer

Identique sur toutes les pages, il contient :
- Adresse du lieu des cours (Namur)
- Adresse du siège social (Liège)
- Coordonnées de contact (email, téléphones)
- Logo WNF
- Lien Facebook
- Lien mentions légales
- Slogan de l'école

Le footer est principalement **informatif** et ne propose quasiment pas de navigation secondaire.

### Navigation mobile

- Menu hamburger
- Sous-menus en accordéons
- Contraste faible identifié sur les sous-pages du menu Formations

---

## Logique de navigation

### Parcours utilisateur principal (inféré)

```
Accueil
  └→ Formations (hub)
       └→ Formation spécifique (Naturopathie, HVN, DLM, Hors-cursus)
            └→ Modules (affichés en modales/popups — pas d'URL propre)
  └→ FAQ (réponses aux questions courantes)
  └→ Contact (formulaire)
```

### Parcours secondaire

```
Accueil
  └→ IHMN (présentation)
       └→ Histoire
       └→ En pratique (accès, horaires)
       └→ Formateurs (17 profils)
  └→ Thérapeutes (annuaire)
       └→ Filtres par région
       └→ Fiches individuelles
```

---

## Sections clés et leur finalité

| Section | Finalité principale |
|---------|-------------------|
| **Page d'accueil** | Présenter l'école et orienter vers les formations |
| **Formations** | Détailler l'offre pédagogique et permettre le choix d'un cursus |
| **IHMN** | Établir la crédibilité et légitimité de l'institution |
| **FAQ** | Répondre aux questions des prospects et réduire les freins à l'inscription |
| **Thérapeutes** | Servir de preuve sociale (débouchés concrets) et référencer les diplômés |
| **Contact** | Convertir les visiteurs intéressés en prise de contact |

---

## Éléments récurrents

- Informations de contact (footer de chaque page)
- Certifications WNF, UNB, Naturo
- Slogan de l'école
- Lien Facebook

---

## Formulaires

Un seul formulaire identifié sur le site :
- **Formulaire de contact** (page `/contact`) : Email, Prénom/Nom, Message, Téléphone (optionnel)

---

## Documents PDF

| Document | Localisation |
|----------|-------------|
| Mentions légales (2023-06-01) | `/mentions-legales` |
| Contrat d'inscription 1re année 2025-26 | Scripts/PDFs |
| Tarifs 2025-26 | Scripts/PDFs |
| Bourse 2025-26 | Scripts/PDFs |

---

## Modules interactifs

| Module | Localisation |
|--------|-------------|
| Carrousel de formations | Page d'accueil |
| Intégration Facebook | Page d'accueil |
| Carte Google Maps (thérapeutes) | Page thérapeutes |
| Carte Google Maps (localisation école) | Page contact |
| Onglets interactifs par année | Pages formations |
| Descriptions déroulantes (modales) | Pages formations |
| Grille de profils + lightbox | Page formateurs |
| Accordéons Q&A | Page FAQ |
| Pagination | Annuaire thérapeutes |

---

## Points structurels notables

### Points positifs

- Structure simple et accessible (2 clics maximum pour les pages importantes)
- Navigation claire avec peu d'items
- Contenu riche et détaillé
- FAQ très complète servant de guide pour les futurs élèves
- Informations pratiques bien documentées

### Limites identifiées

- **Pas de blog/actualités** : Facebook utilisé à la place
- **Pas d'espace membres** ni de zone privée
- **Pas de boutique en ligne**
- **Pas de breadcrumbs** (fil d'Ariane)
- **Modules de formation en modales** sans URL propre (problème SEO et partage)
- **Maillage interne limité** : peu de liens éditoriaux entre les sections
- **Aucune meta description** définie sur les pages
- **Sections en silos** : pas de lien Formations ↔ Thérapeutes, ni Formateurs ↔ Modules

### Architecture mélangée

Les pages administratives (inscriptions, examens) sont mélangées avec les pages de formations dans le menu, ce qui peut créer une confusion. La recommandation pour la refonte est de séparer : Formations / Admissions.

---

## Contexte du projet de refonte

Le repository documente un projet de **refonte complète du site** avec les objectifs suivants :

- Moderniser l'interface et la structure
- Améliorer le référencement naturel (SEO)
- Clarifier la présentation des formations
- Améliorer le parcours des visiteurs
- Permettre à l'équipe de modifier facilement le contenu (migration vers Sanity, headless CMS)
- Ajouter un blog

### État d'avancement (mars 2026)

- **EPIC 1** (terminé) : Inventaire complet du contenu actuel
- **EPIC 2** (terminé) : Analyse de l'architecture actuelle
- **EPICs 3-8** (en cours) : Audit UX, Audit SEO, Synthèse, Architecture cible, Plan de migration, Documentation finale

---

*Document généré à partir de l'analyse du repository du projet de refonte du site IHMN — Mars 2026*
*Voir aussi : [ihmn-identity.md](./ihmn-identity.md) | [ihmn-offer.md](./ihmn-offer.md)*
