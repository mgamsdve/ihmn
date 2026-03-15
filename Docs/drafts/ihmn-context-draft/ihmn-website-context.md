# IHMN — Structure et contexte du site web

## 1. Informations techniques

| Champ | Valeur |
|---|---|
| **URL racine** | https://ihmn.be |
| **CMS** | Joomla |
| **Langue** | Français |
| **Date d'analyse** | Mars 2026 |

---

## 2. Architecture générale du site

Le site actuel est organisé autour de **6 sections principales** accessibles depuis le menu principal :

| Section | URL | Rôle |
|---|---|---|
| Accueil | `/` | Page d'entrée principale, présentation générale |
| Formations | `/formations` | Hub et détail des formations proposées |
| IHMN | `/ihmn` | Présentation institutionnelle de l'école |
| FAQ | `/faq` | Réponses aux questions fréquentes |
| Thérapeutes | `/nos-therapeuthes` | Annuaire des praticiens diplômés |
| Contact | `/contact` | Formulaire de contact et carte |

---

## 3. Description de chaque section

### 3.1. Accueil (`/`)

**H1 :** La Naturopathie, une Passion, un Art, un Métier

**Contenu :**
- Présentation concise de l'école et de sa mission
- Section « À propos de l'IHMN » : ancienneté, localisation, nombre d'élèves, adhésions à WNF/UNB/Naturo
- Blocs de présentation des 4 formations principales avec liens vers les pages dédiées
- Témoignages d'élèves (Josy G., Fanny M.)
- Section « Nous suivre » avec flux Facebook intégré
- Logos des organisations professionnelles partenaires (WNF, UNB, Naturo)

**Objectif :** Donner une première impression de l'école, orienter vers les formations, établir sa crédibilité.

**Liens sortants principaux :** vers les 4 pages de formations, vers WNF, UNB, Naturo (liens externes)

---

### 3.2. Formations (`/formations` et sous-pages)

**H1 :** Formations

**Structure :**

| Page | URL | Contenu |
|---|---|---|
| Hub formations | `/formations` | Présentation générale + liste des 4 formations |
| Naturopathie | `/formations/naturopathie` | Programme sur 4 ans, modules détaillés (popups) |
| Hygiène de Vie et Nutrition | `/formations/hygiene-de-vie-et-nutrition` | Programme sur 2 ans, modules détaillés (popups) |
| Drainage Lymphatique Manuel | `/formations/drainage-lymphatique-manuel` | Module unique, contenu théorique et pratique |
| Formations Hors Cursus | `/formations/formations-hors-cursus` | Liste de séminaires thématiques ouverts à tous |
| Examens & Certificats | `/formations/examens-certificats` | Conditions d'obtention des certifications |
| Inscriptions & Tarifs | `/formations/inscriptions-tarifs` | Tarifs, modalités d'inscription, bourses, documents PDF |

**Aspects techniques :** Les détails des modules sont présentés dans des **fenêtres modales (popups)**, ce qui rend leur contenu difficilement indexable par les moteurs de recherche.

**Objectif :** Présenter l'offre pédagogique, guider les candidats potentiels vers l'inscription.

---

### 3.3. IHMN — École (`/ihmn` et sous-pages)

**H1 :** IHMN

**Structure :**

| Page | URL | Contenu |
|---|---|---|
| Présentation | `/ihmn` | Histoire concise, positionnement, valeurs |
| Histoire | `/ihmn/lhistoire-ihmn` | Chronologie détaillée, personnages clés, vidéo logo |
| En pratique | `/ihmn/en-pratique` | Adresse, horaires, accès (voiture, train) |
| Formateurs | `/ihmn/formateurs` | Grille de 17 formateurs, fiches lightbox |

**Objectif :** Établir la crédibilité institutionnelle de l'école, présenter son histoire et son équipe.

---

### 3.4. FAQ (`/faq`)

**H1 :** FAQ

**Contenu :** ~30 questions réparties en 6 catégories thématiques :

1. **Naturopathie** — définition, reconnaissance professionnelle
2. **Notre école** — ancienneté, spécificité, corps enseignant, horaires
3. **Nos formations** — durée, matières, supports, examens, stages, travail de fin d'études
4. **Inscriptions et dispenses** — conditions d'accès, inscription, modules à la carte, dispenses, étalement
5. **Le minerval et les frais** — coûts, aides financières, couverture des frais
6. **Après la formation** — débouchés professionnels, exercice de la profession

**Objectif :** Répondre aux questions des futurs étudiants à toutes les étapes du parcours de décision.

---

### 3.5. Thérapeutes (`/nos-therapeuthes`)

**H1 :** Thérapeutes

**Contenu principal :**
- Carte interactive avec géolocalisation des thérapeutes
- Liste paginée (4 pages, ~10 thérapeutes par page)
- Filtres par région
- Fiches individuelles par thérapeute

**Sous-pages régionales :**
- `/nos-therapeuthes/bruxelles`
- `/nos-therapeuthes/brabant-wallon`
- `/nos-therapeuthes/brabant-flamand`
- `/nos-therapeuthes/hainaut`
- `/nos-therapeuthes/liege`
- `/nos-therapeuthes/namur`
- `/nos-therapeuthes/luxembourg`
- `/nos-therapeuthes/limbourg`
- `/nos-therapeuthes/france`

**Objectif :** Permettre au public de trouver un praticien naturopathe formé par l'IHMN ; valoriser le réseau de diplômés.

---

### 3.6. Contact (`/contact`)

**H1 :** Contact

**Contenu :**
- Carte Google Maps interactive (localisation de l'école)
- Formulaire de contact : email (obligatoire), nom et prénom (obligatoire), message (obligatoire), téléphone (optionnel)
- Message de confirmation : « Nous vous revenons dans les meilleurs délais ! »

**Objectif :** Permettre aux visiteurs de prendre contact avec l'école.

---

## 4. Navigation

### Menu principal

Menu horizontal présent sur toutes les pages :

```
ACCUEIL | FORMATIONS | IHMN | FAQ | THÉRAPEUTES | CONTACT
```

Le menu « Formations » dispose d'un sous-menu avec les 6 pages (Naturopathie, HV&N, DLM, Hors Cursus, Examens, Inscriptions).

Le menu « IHMN » dispose d'un sous-menu avec Histoire, En pratique, Formateurs.

### Menu mobile

Sur mobile : menu hamburger avec sous-menus en accordéon. La structure reste la même.

### Pied de page (footer)

Contenu du footer, identique sur toutes les pages :
- Lieu des cours (adresse)
- Siège social
- Coordonnées de contact (téléphone, email)
- Lien vers mentions légales
- Logo World Naturopathic Federation
- Lien Facebook

Le footer sert principalement un rôle **informatif** et peu de navigation.

---

## 5. Profondeur de navigation

La majorité des pages importantes se situent à **2 clics maximum de l'accueil** :

```
Niveau 0 : Accueil
Niveau 1 : Formations, IHMN, FAQ, Thérapeutes, Contact
Niveau 2 : Naturopathie, HV&N, DLM, Histoire, En pratique, Formateurs, pages régions thérapeutes
Niveau 3 : Modules de cours (popups sans URL propre), fiches thérapeutes individuelles
```

---

## 6. Documents PDF publiés sur le site

| Document | Utilisation |
|---|---|
| `ihmn_25-26_contrat_inscription_1e-anne.pdf` | Contrat d'inscription à télécharger |
| `ihmn---tarifs-2025-26.pdf` | Tarifs complets de l'année akademique |
| `IHMN - Bourse 2025-26.pdf` | Formulaire de demande de bourse |
| `ihmn_mentions_legales_230601.pdf` | Mentions légales (page `/mentions-legales`) |

---

## 7. Points forts et limites du site actuel

### Points forts

- Contenu riche sur les formations
- Annuaire des thérapeutes avec carte interactive
- FAQ complète couvrant l'ensemble du parcours candidat
- Structure claire et peu profonde

### Limites identifiées

- Design daté (Joomla, technologie ancienne)
- Contenu des modules en popups : non indexable, non accessible directement
- Mélange de pages administratives et pédagogiques dans le menu Formations
- Peu de liens éditoriaux internes entre pages
- Absence de meta descriptions sur la quasi-totalité des pages
- SEO sous-exploité
- Parcours utilisateur peu guidé vers l'inscription

---

## 8. Projet de refonte

Un projet de refonte complète du site est en cours. Les objectifs sont :

- moderniser l'interface
- améliorer le référencement naturel (SEO)
- clarifier la présentation des formations
- améliorer le parcours des visiteurs
- migrer vers un **Headless CMS (Sanity)**
- intégrer un blog naturopathique
- restructurer la section admissions (inscriptions, tarifs, organisation)

→ Voir [ihmn-web-offer.md](../project/ihmn-web-offer.md) pour le détail du projet.

---

## 9. Liens vers les autres documents

- Inventaire complet du site → [../site/current-site/INVENTAIRE_COMPLET_IHMN_2026.md](../site/current-site/INVENTAIRE_COMPLET_IHMN_2026.md)
- Architecture cible → [../site/architecture/sitemap.md](../site/architecture/sitemap.md)
- Identité de l'institution → [ihmn-identity.md](ihmn-identity.md)
- Offre de formation → [ihmn-offer.md](ihmn-offer.md)
