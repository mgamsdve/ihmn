# Phase 1 — Backlog GitHub : Analyse de l'existant et préparation de la refonte
> Site : [ihmn.be](https://ihmn.be)  
> CMS actuel : Joomla + Gridbox  
> Objectif : Analyser l'existant et préparer la refonte complète du site
---
## Labels suggérés
| Label | Description | Couleur |
|---|---|---|
| `epic` | Issue de type EPIC (regroupement de tâches) | `#1d76db` |
| `phase-1` | Tâches de la Phase 1 | `#0075ca` |
| `content-inventory` | Inventaire et analyse du contenu | `#e4e669` |
| `architecture` | Architecture de l'information | `#d93f0b` |
| `ux-audit` | Audit UX et parcours utilisateur | `#0e8a16` |
| `seo-audit` | Audit SEO | `#5319e7` |
| `analysis` | Analyse et identification des problèmes | `#f9d0c4` |
| `documentation` | Documentation et livrables | `#cfd3d7` |
| `priority-high` | Priorité haute | `#b60205` |
| `priority-medium` | Priorité moyenne | `#fbca04` |
| `priority-low` | Priorité basse | `#0e8a16` |
---
## Vue d'ensemble — 8 EPICs, 26 Issues
| # | EPIC | Issues |
|---|---|---|
| E1 | Inventaire complet du contenu | 5 issues |
| E2 | Analyse de l'architecture actuelle | 4 issues |
| E3 | Audit UX du site actuel | 4 issues |
| E4 | Audit SEO du site actuel | 4 issues |
| E5 | Identification des problèmes et opportunités | 3 issues |
| E6 | Préparation de la future architecture | 3 issues |
| E7 | Préparation du mapping des contenus | 3 issues |
| E8 | Documentation de l'analyse Phase 1 | 3 issues |
---
## EPIC 1 — Inventaire complet du contenu du site actuel
**Labels :** `epic`, `phase-1`, `content-inventory`
**Description :**
Réaliser un inventaire exhaustif de tout le contenu publié sur le site ihmn.be actuel. Cet inventaire constitue la base de toutes les analyses suivantes et permet de ne rien oublier lors de la migration.
**Issues associées :** 1.1, 1.2, 1.3, 1.4, 1.5
---
### Issue 1.1 — Inventaire des pages institutionnelles
**Labels :** `phase-1`, `content-inventory`, `priority-high`
**Description :**
Recenser et documenter toutes les pages institutionnelles du site actuel (pages hors formations et hors annuaire thérapeutes).
**Checklist :**
- [ ] Lister toutes les URLs des pages institutionnelles
- [ ] Documenter le H1, le titre de page et la meta description de chaque page
- [ ] Identifier le type de contenu (texte, images, formulaires, vidéos)
- [ ] Évaluer la qualité du contenu (à conserver / à réviser / à supprimer)
- [ ] Estimer le volume de contenu textuel (nombre de mots approximatif)
- [ ] Identifier les images et médias associés à chaque page
- [ ] Documenter les liens internes présents sur chaque page
**Pages à inventorier :**
- `/` — Accueil
- `/ihmn` — IHMN (présentation de l'école)
- `/ihmn/lhistoire-ihmn` — Histoire de l'IHMN
- `/ihmn/en-pratique` — En pratique
- `/ihmn/formateurs` — Nos formateurs
- `/contact` — Contact
- `/faq` — FAQ
- `/mentions-legales` — Mentions légales
**Livrable attendu :**
Tableau d'inventaire au format CSV/Markdown avec colonnes : URL, H1, Titre, Meta description, Type de contenu, Qualité estimée, Volume textuel, Médias, Statut (à conserver / réviser / supprimer).
---
### Issue 1.2 — Inventaire des pages de formations et des modules
**Labels :** `phase-1`, `content-inventory`, `priority-high`
**Description :**
Recenser et documenter toutes les pages de formations et leurs modules de cours. Cette section est le cœur du site et nécessite une analyse détaillée.
**Checklist :**
- [ ] Lister toutes les URLs des pages de formations
- [ ] Documenter la structure de chaque formation (années, modules)
- [ ] Pour chaque module de cours, documenter : titre, formateur, durée, description, objectifs, méthodologie
- [ ] Identifier les informations manquantes ou incomplètes dans les modules
- [ ] Recenser les examens et certificats associés à chaque formation
- [ ] Documenter les informations d'inscription et de tarifs
- [ ] Identifier les incohérences ou doublons dans la présentation des formations
**Pages à inventorier :**
- `/formations` — Hub formations
- `/formations/naturopathie` — Formation Naturopathie (4 ans, modules par année)
- `/formations/hygiene-de-vie-et-nutrition` — Hygiène de vie et nutrition
- `/formations/drainage-lymphatique-manuel` — Drainage lymphatique manuel
- `/formations/formations-hors-cursus` — Formations hors cursus
- `/formations/examens-certificats` — Examens & Certificats
- `/formations/inscriptions-tarifs` — Inscriptions & Tarifs
**Livrable attendu :**
Tableau d'inventaire des formations + fiche détaillée par formation avec la liste complète des modules (titre, formateur, durée, description). Format CSV/Markdown.
---
### Issue 1.3 — Inventaire et analyse de l'annuaire des thérapeutes
**Labels :** `phase-1`, `content-inventory`, `priority-medium`
**Description :**
Recenser et documenter la structure complète de l'annuaire des thérapeutes : pages régionales, fiches individuelles, système de pagination et carte interactive.
**Checklist :**
- [ ] Lister toutes les URLs des pages régionales de l'annuaire
- [ ] Compter le nombre total de thérapeutes référencés
- [ ] Documenter les informations présentes sur chaque fiche thérapeute (nom, région, spécialités, contact, photo, etc.)
- [ ] Identifier les champs systématiquement renseignés vs les champs souvent vides
- [ ] Analyser le système de pagination (nombre de pages, nombre par page)
- [ ] Documenter le fonctionnement de la carte interactive
- [ ] Identifier les thérapeutes présents dans plusieurs régions (doublons potentiels)
- [ ] Analyser les filtres disponibles
**Régions à inventorier :**
Bruxelles, Brabant Wallon, Brabant Flamand, Hainaut, Liège, Namur, Luxembourg, Limbourg, France
**Livrable attendu :**
Inventaire structuré de l'annuaire avec : nombre de thérapeutes par région, liste des champs disponibles sur les fiches, analyse des doublons, évaluation du système de navigation de l'annuaire.
---
### Issue 1.4 — Inventaire et analyse des documents PDF
**Labels :** `phase-1`, `content-inventory`, `priority-medium`
**Description :**
Recenser tous les documents PDF publiés sur le site, évaluer leur pertinence et leur état, et préparer les recommandations pour la migration.
**Checklist :**
- [ ] Lister tous les PDF accessibles sur le site (inspection du code source + navigation)
- [ ] Documenter pour chaque PDF : URL, nom du fichier, page de référencement, date de mise à jour estimée
- [ ] Identifier les PDF obsolètes (tarifs anciens, contrats dépassés)
- [ ] Identifier les PDF à conserver, mettre à jour ou supprimer
- [ ] Vérifier les liens morts vers des PDF supprimés
- [ ] Évaluer le format et l'accessibilité des PDF (mise en page, lisibilité)
**PDFs connus :**
- `ihmn_25-26_contrat_inscription_1e-anne.pdf`
- `IHMN - Bourse 2025-26.pdf`
- `ihmn---tarifs-2025-26.pdf`
- `ihmn_mentions_legales_230601.pdf`
**Livrable attendu :**
Tableau des PDFs avec colonnes : URL, Nom, Page de référence, État (actuel / obsolète), Action recommandée (conserver / mettre à jour / supprimer / remplacer par page web).
---
### Issue 1.5 — Inventaire et analyse de la FAQ
**Labels :** `phase-1`, `content-inventory`, `priority-medium`
**Description :**
Recenser et analyser toutes les questions/réponses de la FAQ, évaluer leur pertinence et préparer leur restructuration.
**Checklist :**
- [ ] Lister toutes les questions présentes dans la FAQ
- [ ] Catégoriser les questions par thème (formation, inscription, naturopathie, école, etc.)
- [ ] Identifier les questions redondantes ou trop similaires
- [ ] Identifier les questions manquantes par rapport aux thèmes couverts
- [ ] Évaluer la qualité et la complétude des réponses
- [ ] Analyser le système d'affichage actuel (accordéon, liste, etc.)
- [ ] Identifier les questions avec potentiel SEO (questions = requêtes utilisateur)
**Livrable attendu :**
Inventaire complet de la FAQ catégorisé par thème + recommandations (questions à conserver / reformuler / supprimer / ajouter). Format Markdown.
---
## EPIC 2 — Analyse de l'architecture actuelle du site
**Labels :** `epic`, `phase-1`, `architecture`
**Description :**
Analyser en profondeur l'architecture de l'information du site actuel : structure des URLs, hiérarchie des pages, navigation, aspects techniques du CMS.
**Issues associées :** 2.1, 2.2, 2.3, 2.4
---
### Issue 2.1 — Cartographie de la navigation et des menus
**Labels :** `phase-1`, `architecture`, `priority-high`
**Description :**
Documenter et analyser tous les éléments de navigation du site : menus principaux, menus secondaires, liens en pied de page, liens contextuels.
**Checklist :**
- [ ] Documenter la structure du menu principal (items, sous-items, profondeur)
- [ ] Documenter la structure du menu pied de page
- [ ] Identifier les menus secondaires ou contextuels
- [ ] Analyser la cohérence entre la navigation et la structure réelle des pages
- [ ] Identifier les pages orphelines (non accessibles depuis la navigation)
- [ ] Identifier les pages en doublon dans la navigation
- [ ] Analyser le comportement du menu sur mobile (hamburger, accordéon, etc.)
- [ ] Évaluer la profondeur maximale de navigation (nombre de clics depuis l'accueil)
**Livrable attendu :**
Diagramme/schéma de la navigation actuelle + tableau d'analyse avec : item de menu, URL cible, profondeur, présence mobile. Format Markdown/image.
---
### Issue 2.2 — Analyse de la structure des URLs
**Labels :** `phase-1`, `architecture`, `priority-high`
**Description :**
Analyser les patterns d'URLs du site actuel pour identifier les bonnes pratiques et les problèmes avant la migration.
**Checklist :**
- [ ] Lister toutes les URLs du site (crawl complet)
- [ ] Analyser les patterns de nommage des URLs
- [ ] Identifier les URLs avec des paramètres (`?page=`, etc.)
- [ ] Identifier les URLs trop longues ou mal structurées
- [ ] Vérifier la cohérence linguistique des URLs (fr/en/mélange)
- [ ] Identifier les URLs avec des caractères spéciaux ou des problèmes d'encodage
- [ ] Vérifier la canonicalisation (URLs en `www` vs sans `www`, `http` vs `https`)
- [ ] Lister les URLs des pages de pagination de l'annuaire
**Outils suggérés :** Screaming Frog, Sitebulb, ou crawl manuel
**Livrable attendu :**
Export CSV de toutes les URLs avec colonnes : URL, Profondeur, Code HTTP, Titre, H1, Meta description, Liens entrants, Liens sortants.
---
### Issue 2.3 — Analyse de la hiérarchie des pages et du maillage interne
**Labels :** `phase-1`, `architecture`, `priority-medium`
**Description :**
Analyser la hiérarchie des pages, le maillage interne et la cohérence éditoriale du site.
**Checklist :**
- [ ] Créer un sitemap visuel du site actuel
- [ ] Analyser le maillage interne (liens entre les pages)
- [ ] Identifier les pages avec peu ou pas de liens intrants
- [ ] Identifier les opportunités de maillage interne non exploitées
- [ ] Analyser la distribution du PageRank interne (pages les plus et moins liées)
- [ ] Vérifier la présence et la cohérence des breadcrumbs
- [ ] Analyser les liens entre formations, thérapeutes et pages institutionnelles
**Livrable attendu :**
Sitemap visuel du site actuel + analyse du maillage interne avec recommandations. Format Markdown/schéma.
---
### Issue 2.4 — Audit technique Joomla / Gridbox
**Labels :** `phase-1`, `architecture`, `priority-medium`
**Description :**
Réaliser un audit technique de l'infrastructure CMS actuelle pour identifier les contraintes et opportunités de la migration.
**Checklist :**
- [ ] Identifier la version de Joomla utilisée
- [ ] Identifier la version de Gridbox et les extensions/plugins actifs
- [ ] Documenter les types de contenus Joomla utilisés (articles, catégories, etc.)
- [ ] Identifier les modules et plugins tiers installés
- [ ] Analyser la structure de la base de données (tables, relations)
- [ ] Évaluer les performances actuelles (temps de chargement, score PageSpeed)
- [ ] Documenter le système d'hébergement actuel
- [ ] Identifier les contraintes de migration (formats propriétaires, données liées)
**Livrable attendu :**
Rapport technique : version CMS, extensions, structure données, performances actuelles. Format Markdown.
---
## EPIC 3 — Audit UX du site actuel
**Labels :** `epic`, `phase-1`, `ux-audit`
**Description :**
Analyser l'expérience utilisateur du site actuel : parcours de navigation, accessibilité, appels à l'action, expérience mobile. Identifier les freins et les points de friction.
**Issues associées :** 3.1, 3.2, 3.3, 3.4
---
### Issue 3.1 — Analyse du parcours utilisateur principal (funnel inscription)
**Labels :** `phase-1`, `ux-audit`, `priority-high`
**Description :**
Analyser le parcours d'un utilisateur souhaitant s'inscrire à une formation, de la page d'accueil jusqu'au formulaire d'inscription.
**Checklist :**
- [ ] Identifier les profils utilisateurs principaux (personas) : futur étudiant, professionnel en reconversion, curieux de la naturopathie
- [ ] Cartographier le parcours "découverte → information → décision → inscription"
- [ ] Identifier toutes les pages du funnel d'inscription
- [ ] Compter le nombre de clics nécessaires depuis l'accueil pour accéder au formulaire d'inscription
- [ ] Identifier les pages de sortie fréquentes dans le funnel
- [ ] Analyser la lisibilité des informations sur les tarifs et modalités
- [ ] Identifier les informations manquantes qui pourraient bloquer la décision d'inscription
- [ ] Analyser la confiance générée par le site (témoignages, certifications, etc.)
**Livrable attendu :**
Carte du parcours utilisateur (user journey map) avec identification des friction points. Format schéma/Markdown.
---
### Issue 3.2 — Analyse de la navigation et de l'accessibilité
**Labels :** `phase-1`, `ux-audit`, `priority-high`
**Description :**
Évaluer la facilité de navigation et l'accessibilité globale du site pour tous les types d'utilisateurs.
**Checklist :**
- [ ] Évaluer la clarté et l'intuitivité du menu principal
- [ ] Analyser la visibilité des éléments de navigation (contraste, taille)
- [ ] Tester la navigation au clavier (accessibilité)
- [ ] Vérifier la présence et la pertinence des balises ARIA
- [ ] Analyser les contrastes de couleurs (WCAG AA minimum)
- [ ] Évaluer la lisibilité des textes (taille de police, espacement, longueur des lignes)
- [ ] Analyser la hiérarchie visuelle des pages (H1, H2, H3, paragraphes)
- [ ] Identifier les éléments interactifs sans feedback visuel clair
- [ ] Évaluer la cohérence visuelle entre les pages
**Livrable attendu :**
Rapport d'accessibilité et de navigation avec score global et liste priorisée des problèmes. Format Markdown.
---
### Issue 3.3 — Analyse des appels à l'action (CTA)
**Labels :** `phase-1`, `ux-audit`, `priority-medium`
**Description :**
Recenser et évaluer tous les appels à l'action du site pour identifier leur efficacité et leur cohérence avec les objectifs du site.
**Checklist :**
- [ ] Lister tous les CTA présents sur le site (boutons, liens d'action)
- [ ] Analyser la clarté et la lisibilité de chaque CTA
- [ ] Évaluer le positionnement des CTA (above/below the fold)
- [ ] Identifier les pages sans CTA clair
- [ ] Analyser la cohérence des CTA avec les objectifs de chaque page
- [ ] Identifier les CTA manquants sur les pages clés (formations, accueil)
- [ ] Évaluer l'urgence/motivation créée par les CTA actuels
- [ ] Comparer les CTA selon les devices (desktop vs mobile)
**Livrable attendu :**
Inventaire des CTA avec évaluation qualitative + recommandations d'amélioration. Format Markdown.
---
### Issue 3.4 — Analyse de l'expérience mobile et du responsive design
**Labels :** `phase-1`, `ux-audit`, `priority-high`
**Description :**
Tester et analyser l'expérience utilisateur sur mobile (smartphones et tablettes).
**Checklist :**
- [ ] Tester l'affichage sur au moins 3 tailles d'écran : mobile (375px), tablette (768px), desktop (1280px)
- [ ] Vérifier le test "Mobile-Friendly" de Google Search Console
- [ ] Analyser la vitesse de chargement sur mobile (score PageSpeed Insights)
- [ ] Identifier les éléments non adaptés au mobile (tableaux larges, textes trop petits, etc.)
- [ ] Tester les formulaires sur mobile (facilité de saisie)
- [ ] Analyser le comportement des modales (modules de cours) sur mobile
- [ ] Évaluer l'accessibilité du menu hamburger sur mobile
- [ ] Identifier les images non optimisées pour mobile
**Outils suggérés :** Chrome DevTools, Google PageSpeed Insights, BrowserStack
**Livrable attendu :**
Rapport d'audit mobile avec captures d'écran des problèmes identifiés + score de performance mobile. Format Markdown.
---
## EPIC 4 — Audit SEO du site actuel
**Labels :** `epic`, `phase-1`, `seo-audit`
**Description :**
Réaliser un audit SEO complet du site actuel pour identifier les problèmes techniques, les opportunités de contenu et les points d'amélioration avant la refonte.
**Issues associées :** 4.1, 4.2, 4.3, 4.4
---
### Issue 4.1 — Audit des métadonnées et balises HTML
**Labels :** `phase-1`, `seo-audit`, `priority-high`
**Description :**
Analyser les métadonnées, titres et balises HTML de toutes les pages pour identifier les problèmes SEO on-page.
**Checklist :**
- [ ] Vérifier la présence et l'unicité des titres `<title>` sur toutes les pages
- [ ] Vérifier la présence et la qualité des meta descriptions
- [ ] Analyser la structure des balises H1/H2/H3 sur chaque page
- [ ] Identifier les pages avec H1 manquant ou multiples H1
- [ ] Vérifier la présence des balises Open Graph (og:title, og:description, og:image)
- [ ] Vérifier les balises canonical
- [ ] Analyser le robots.txt et le sitemap.xml
- [ ] Vérifier la présence de données structurées (Schema.org)
- [ ] Identifier les titres dupliqués ou trop courts/trop longs
**Livrable attendu :**
Rapport des métadonnées SEO avec tableaux page par page + liste des corrections prioritaires. Format CSV/Markdown.
---
### Issue 4.2 — Analyse des contenus et des mots-clés
**Labels :** `phase-1`, `seo-audit`, `priority-high`
**Description :**
Analyser le positionnement actuel du site sur les mots-clés cibles et identifier les opportunités SEO de contenu.
**Checklist :**
- [ ] Identifier les mots-clés principaux actuellement ciblés
- [ ] Analyser le positionnement Google sur les mots-clés stratégiques (naturopathie, formation naturopathie, école naturopathie Belgique, etc.)
- [ ] Utiliser Google Search Console pour extraire les requêtes actuelles et le CTR
- [ ] Analyser la densité des mots-clés sur les pages principales
- [ ] Identifier les cannibalisation de mots-clés (plusieurs pages ciblant le même mot-clé)
- [ ] Identifier les mots-clés manquants à fort potentiel
- [ ] Analyser les contenus des concurrents directs (autres écoles de naturopathie en Belgique)
- [ ] Identifier les questions de l'annuaire thérapeutes exploitables en SEO
**Outils suggérés :** Google Search Console, SEMrush, Ahrefs, Ubersuggest
**Livrable attendu :**
Tableau de mots-clés avec : mot-clé, volume, position actuelle, page ciblée, opportunité. Format CSV.
---
### Issue 4.3 — Audit des performances techniques (Core Web Vitals)
**Labels :** `phase-1`, `seo-audit`, `priority-high`
**Description :**
Mesurer et analyser les performances techniques du site qui impactent le référencement (Core Web Vitals, vitesse de chargement).
**Checklist :**
- [ ] Mesurer les Core Web Vitals (LCP, INP, CLS) sur les pages principales
- [ ] Analyser le score PageSpeed Insights desktop et mobile
- [ ] Analyser le temps de chargement total (TTFB, FCP, LCP)
- [ ] Identifier les ressources bloquant le rendu (render-blocking)
- [ ] Analyser le poids des images et leur format (WebP vs JPEG/PNG)
- [ ] Vérifier la présence d'un cache serveur
- [ ] Analyser le code JavaScript et CSS (minification, bundling)
- [ ] Vérifier le protocole HTTPS et la validité du certificat SSL
- [ ] Analyser les erreurs 4xx et 5xx via Search Console
**Outils suggérés :** Google PageSpeed Insights, GTmetrix, Lighthouse, Search Console
**Livrable attendu :**
Rapport de performances avec scores LCP/INP/CLS par page + liste des optimisations techniques recommandées. Format Markdown.
---
### Issue 4.4 — Analyse des données structurées et du profil de liens
**Labels :** `phase-1`, `seo-audit`, `priority-medium`
**Description :**
Analyser les données structurées (Schema.org) et le profil de backlinks du site pour évaluer l'autorité de domaine.
**Checklist :**
- [ ] Vérifier la présence et la validité des données structurées existantes
- [ ] Identifier les opportunités de balisage Schema.org (Organization, Course, FAQPage, BreadcrumbList, LocalBusiness)
- [ ] Analyser le profil de backlinks (domaines référents, ancre de liens, qualité)
- [ ] Identifier les backlinks toxiques à désavouer
- [ ] Analyser le Domain Authority / Domain Rating actuel
- [ ] Identifier les opportunités de netlinking (annuaires santé, associations naturopathie, etc.)
- [ ] Vérifier les mentions de la marque non liées (unlinked brand mentions)
**Outils suggérés :** Ahrefs, Majestic, Google Search Console, Schema Markup Validator
**Livrable attendu :**
Rapport backlinks + recommandations de données structurées Schema.org à implémenter. Format Markdown.
---
## EPIC 5 — Identification des problèmes et des opportunités
**Labels :** `epic`, `phase-1`, `analysis`
**Description :**
Consolider toutes les analyses précédentes pour dresser un tableau complet des problèmes structurels et des opportunités d'amélioration.
**Issues associées :** 5.1, 5.2, 5.3
---
### Issue 5.1 — Synthèse des problèmes structurels identifiés
**Labels :** `phase-1`, `analysis`, `priority-high`
**Description :**
Consolider les résultats des audits (UX, SEO, technique, contenu) en une synthèse priorisée des problèmes à résoudre lors de la refonte.
**Checklist :**
- [ ] Regrouper les problèmes identifiés dans les EPICs 1 à 4 par catégorie
- [ ] Prioriser les problèmes selon leur impact (high / medium / low)
- [ ] Pour chaque problème : décrire l'impact utilisateur et l'impact SEO
- [ ] Identifier les problèmes bloquants pour la migration
- [ ] Identifier les quick wins (améliorations rapides à fort impact)
- [ ] Associer chaque problème à une recommandation de solution
- [ ] Valider la synthèse avec le client/chef de projet
**Problèmes connus à documenter (base de départ) :**
- Design daté
- Navigation peu claire
- Hiérarchie visuelle faible
- Absence de blog SEO
- Parcours utilisateur peu guidé
- Pages longues et difficiles à parcourir
- SEO sous-exploité
**Livrable attendu :**
Document de synthèse des problèmes priorisés avec tableau : problème, catégorie, impact, priorité, solution recommandée. Format Markdown.
---
### Issue 5.2 — Identification des opportunités SEO
**Labels :** `phase-1`, `analysis`, `seo-audit`, `priority-high`
**Description :**
Identifier et prioriser toutes les opportunités SEO à exploiter lors de la refonte du site.
**Checklist :**
- [ ] Identifier les mots-clés à fort potentiel non encore ciblés
- [ ] Analyser les questions des utilisateurs autour de la naturopathie (People Also Ask, forums, etc.)
- [ ] Identifier les contenus de blog à fort potentiel SEO à créer
- [ ] Analyser les pages de résultats Google pour les requêtes cibles (SERP analysis)
- [ ] Identifier les featured snippets potentiels (FAQ, définitions, listes)
- [ ] Analyser les opportunités de référencement local (naturopathie Belgique, par ville)
- [ ] Identifier les opportunités de création de pages piliers + cluster de contenus
- [ ] Évaluer le potentiel de l'annuaire thérapeutes comme levier SEO (pages régionales)
**Opportunités connues à documenter :**
- Création d'un blog SEO sur la naturopathie
- Restructuration des pages formations pour le SEO
- Meilleure mise en avant des témoignages
- Simplification du parcours inscription
**Livrable attendu :**
Liste priorisée des opportunités SEO avec estimations de trafic potentiel et effort d'implémentation. Format Markdown.
---
### Issue 5.3 — Analyse des gaps de contenu
**Labels :** `phase-1`, `analysis`, `content-inventory`, `priority-medium`
**Description :**
Identifier le contenu manquant sur le site actuel par rapport aux besoins des utilisateurs et aux standards du secteur.
**Checklist :**
- [ ] Analyser les questions fréquentes non couvertes par le site actuel
- [ ] Identifier les informations que les candidats recherchent avant de s'inscrire
- [ ] Comparer le contenu du site avec les sites concurrents (benchmark de contenu)
- [ ] Identifier les pages manquantes nécessaires pour le SEO
- [ ] Analyser les données de Search Console pour identifier des requêtes sans page dédiée
- [ ] Identifier les témoignages et cas d'usage manquants
- [ ] Analyser les besoins de contenu pour chaque étape du funnel d'inscription
- [ ] Lister les contenus à créer pour la Phase 2 de la refonte
**Livrable attendu :**
Gap analysis de contenu : liste des contenus manquants avec priorité et phase de création recommandée. Format Markdown.
---
## EPIC 6 — Préparation de la future architecture
**Labels :** `epic`, `phase-1`, `architecture`
**Description :**
Sur la base des analyses précédentes, définir la nouvelle architecture de l'information, le sitemap futur et le content model du nouveau site.
**Issues associées :** 6.1, 6.2, 6.3
---
### Issue 6.1 — Définition de la nouvelle architecture de l'information
**Labels :** `phase-1`, `architecture`, `priority-high`
**Description :**
Définir la structure des sections et sous-sections du futur site, en tenant compte des objectifs SEO, UX et des contraintes du contenu existant.
**Checklist :**
- [ ] Définir les sections principales de la nouvelle architecture
- [ ] Définir la hiérarchie des sous-pages pour chaque section
- [ ] Valider l'architecture avec les objectifs SEO (mots-clés par section)
- [ ] Valider l'architecture avec le parcours utilisateur cible
- [ ] Définir la profondeur maximale de navigation (3 niveaux max recommandé)
- [ ] Identifier les nouvelles pages à créer (blog, page pilier, nouvelles formations)
- [ ] Documenter la logique de chaque section et son rôle dans le funnel
**Architecture proposée à documenter et valider :**
- Accueil
- Formation Naturopathie (+ sous-pages par année + examens)
- Hygiène de vie et nutrition
- Drainage lymphatique manuel
- Formations complémentaires (hors cursus)
- Admissions (inscription + tarifs)
- L'école (histoire, philosophie, formateurs)
- Thérapeutes (annuaire par région)
- Blog
- FAQ
- Contact
- Mentions légales
**Livrable attendu :**
Document d'architecture de l'information validé avec schéma visuel de la hiérarchie des pages. Format Markdown/schéma.
---
### Issue 6.2 — Création du sitemap de la future architecture
**Labels :** `phase-1`, `architecture`, `priority-medium`
**Description :**
Créer le sitemap complet du futur site avec toutes les URLs planifiées et leur hiérarchie.
**Checklist :**
- [ ] Définir la nomenclature des URLs futures (conventions de nommage)
- [ ] Créer le sitemap arborescent complet du futur site
- [ ] Définir les nouvelles URLs pour chaque page (SEO-friendly)
- [ ] Identifier les URLs à conserver à l'identique (bon positionnement SEO existant)
- [ ] Documenter les URLs qui changeront (nécessitant une redirection 301)
- [ ] Valider le sitemap avec le client/chef de projet
- [ ] Préparer la liste des redirections 301 nécessaires
**Livrable attendu :**
Sitemap complet du futur site (toutes les URLs planifiées) + document des nouvelles conventions d'URLs. Format Markdown.
---
### Issue 6.3 — Définition du content model futur
**Labels :** `phase-1`, `architecture`, `content-inventory`, `priority-high`
**Description :**
Définir les types de contenus du futur site, leurs champs, leurs relations et leur structure pour le nouveau CMS.
**Checklist :**
- [ ] Lister tous les types de contenus nécessaires (page, formation, module, thérapeute, article de blog, FAQ, etc.)
- [ ] Pour chaque type de contenu, définir les champs nécessaires avec leur type de données
- [ ] Définir les relations entre les types de contenus (ex: une formation a plusieurs modules)
- [ ] Définir les règles de validation des champs (obligatoire, format, longueur)
- [ ] Identifier les champs communs entre types de contenus (réutilisabilité)
- [ ] Définir les règles d'affichage et de présentation pour chaque type
- [ ] Valider le content model avec les besoins SEO (champs meta, titre SEO, etc.)
- [ ] Documenter les contraintes de migration des données existantes
**Types de contenus à modéliser :**
- `Page` (institutionnelle)
- `Formation` (avec sous-type : cursus complet / atelier hors cursus)
- `Module de cours` (appartenant à une Formation et une Année)
- `Formateur`
- `Thérapeute` (avec région, spécialités, contact)
- `Article de blog`
- `FAQ` (question + réponse + catégorie)
- `Document` (PDF)
**Livrable attendu :**
Content model complet avec diagramme de types de contenus et leurs relations. Format Markdown/schéma.
---
## EPIC 7 — Préparation du mapping des contenus
**Labels :** `epic`, `phase-1`, `content-inventory`
**Description :**
Créer le mapping complet entre les contenus actuels et la future architecture : quelles pages vont où, quelles URLs changent, quels contenus sont créés ou supprimés.
**Issues associées :** 7.1, 7.2, 7.3
---
### Issue 7.1 — Mapping des URLs actuelles vers la nouvelle architecture
**Labels :** `phase-1`, `content-inventory`, `architecture`, `priority-high`
**Description :**
Créer le tableau de correspondance entre chaque URL actuelle et son équivalent dans la nouvelle architecture.
**Checklist :**
- [ ] Partir de l'inventaire complet des URLs actuelles (Issue 2.2)
- [ ] Associer chaque URL actuelle à sa destination dans la nouvelle architecture
- [ ] Documenter le statut de chaque URL : conserver / rediriger / fusionner / supprimer
- [ ] Identifier les contenus qui seront fusionnés sur une seule page
- [ ] Identifier les contenus qui seront découpés sur plusieurs pages
- [ ] Vérifier qu'aucune URL stratégique (bon SEO) n'est supprimée sans redirection
- [ ] Documenter les changements de structure pour les modules de formations
**Mapping partiel existant à compléter et valider :**
| Ancienne URL | Nouvelle section | Action |
|---|---|---|
| `/` | Accueil | Conserver |
| `/formations` | Formation Naturopathie | Rediriger |
| `/formations/naturopathie` | Formation Naturopathie | Conserver si bon SEO |
| `/formations/inscriptions-tarifs` | Admissions | Rediriger |
| `/ihmn` | L'école | Rediriger |
| `/ihmn/formateurs` | L'école → Formateurs | Conserver ou rediriger |
| `/nos-therapeuthes` | Thérapeutes | Conserver ou rediriger |
**Livrable attendu :**
Tableau complet de mapping URL (ancienne URL → nouvelle URL → action). Format CSV.
---
### Issue 7.2 — Plan de redirections 301
**Labels :** `phase-1`, `architecture`, `seo-audit`, `priority-high`
**Description :**
Préparer le plan complet des redirections 301 nécessaires lors du lancement du nouveau site pour préserver le capital SEO.
**Checklist :**
- [ ] Lister toutes les URLs qui changeront lors de la migration
- [ ] Définir la règle de redirection pour chaque URL (URL par URL ou pattern)
- [ ] Prioriser les redirections selon l'importance SEO de chaque page
- [ ] Identifier les redirections en chaîne à éviter (A→B→C)
- [ ] Documenter les cas particuliers (pages de pagination, pages de filtres)
- [ ] Préparer le fichier `.htaccess` ou équivalent pour le serveur
- [ ] Prévoir un processus de vérification post-lancement
- [ ] Identifier les backlinks externes pointant vers des URLs qui changeront
**Livrable attendu :**
Plan de redirections 301 complet au format CSV + règles `.htaccess` prêtes à l'emploi. Format CSV + texte.
---
### Issue 7.3 — Identification des contenus à créer, modifier ou supprimer
**Labels :** `phase-1`, `content-inventory`, `priority-medium`
**Description :**
Créer le plan éditorial de migration : quels contenus sont migrés à l'identique, lesquels nécessitent une révision, lesquels sont nouveaux et lesquels sont supprimés.
**Checklist :**
- [ ] Pour chaque page existante : définir l'action (migrer tel quel / réécrire / fusionner / supprimer)
- [ ] Identifier les contenus nécessitant une mise à jour avant migration
- [ ] Lister les nouvelles pages à créer ex nihilo pour la refonte
- [ ] Estimer l'effort de rédaction/révision pour chaque contenu
- [ ] Identifier les contenus qui nécessitent une validation côté client
- [ ] Préparer un brief de rédaction pour les nouveaux contenus
- [ ] Planifier la production de contenu (ordre de priorité)
**Livrable attendu :**
Plan éditorial de migration avec tableau : page, action, priorité, effort estimé, responsable, statut. Format CSV/Markdown.
---
## EPIC 8 — Documentation de l'analyse Phase 1
**Labels :** `epic`, `phase-1`, `documentation`
**Description :**
Rédiger et livrer tous les documents de synthèse de la Phase 1 pour servir de base à la Phase 2 (conception et développement).
**Issues associées :** 8.1, 8.2, 8.3
---
### Issue 8.1 — Rédaction du rapport d'analyse complet Phase 1
**Labels :** `phase-1`, `documentation`, `priority-high`
**Description :**
Rédiger le rapport d'analyse complet de la Phase 1 intégrant tous les livrables produits lors des EPICs 1 à 7.
**Checklist :**
- [ ] Rédiger l'introduction et le contexte du projet
- [ ] Synthétiser l'inventaire du contenu (résumé des volumes et de la qualité)
- [ ] Synthétiser l'analyse de l'architecture actuelle
- [ ] Synthétiser l'audit UX (points clés, problèmes identifiés)
- [ ] Synthétiser l'audit SEO (problèmes et opportunités)
- [ ] Présenter la nouvelle architecture proposée avec justifications
- [ ] Présenter le content model futur
- [ ] Présenter le plan de migration (mapping + redirections)
- [ ] Rédiger les recommandations priorisées pour la Phase 2
- [ ] Relire et valider le rapport avec toutes les parties prenantes
**Structure du rapport :**
1. Résumé exécutif
2. Inventaire du contenu actuel
3. Analyse de l'architecture actuelle
4. Audit UX
5. Audit SEO
6. Problèmes identifiés et opportunités
7. Architecture future proposée
8. Content model
9. Plan de migration
10. Recommandations Phase 2
**Livrable attendu :**
Rapport complet Phase 1 (PDF + Markdown). Stocké dans `Docs/project/backlog/rapport-phase-1.md`.
---
### Issue 8.2 — Préparation du brief technique pour la Phase 2
**Labels :** `phase-1`, `documentation`, `priority-medium`
**Description :**
Rédiger le brief technique qui servira de base au développement du nouveau site lors de la Phase 2.
**Checklist :**
- [ ] Documenter les exigences fonctionnelles (fonctionnalités requises)
- [ ] Documenter les exigences techniques (CMS cible, hébergement, performances)
- [ ] Documenter les exigences SEO (structure des URLs, données structurées, etc.)
- [ ] Documenter les exigences d'accessibilité (WCAG AA minimum)
- [ ] Documenter les exigences de design (charte graphique, typographie)
- [ ] Décrire les intégrations nécessaires (formulaires, carte thérapeutes, etc.)
- [ ] Définir les critères d'acceptance pour la Phase 2
- [ ] Préparer la liste des livrables attendus pour la Phase 2
- [ ] Estimer le plan de développement Phase 2 (épics, sprints, timeline)
**Livrable attendu :**
Brief technique Phase 2 complet (Markdown). Stocké dans `Docs/project/phase-2-brief.md`.
---
### Issue 8.3 — Rétrospective et validation de la Phase 1
**Labels :** `phase-1`, `documentation`, `priority-low`
**Description :**
Réaliser la rétrospective de la Phase 1 : valider tous les livrables, recueillir les retours du client et préparer le lancement de la Phase 2.
**Checklist :**
- [ ] Vérifier la complétude de tous les livrables de la Phase 1
- [ ] Préparer et présenter le rapport Phase 1 au client
- [ ] Recueillir et documenter les retours et décisions du client
- [ ] Valider l'architecture future proposée avec le client
- [ ] Valider le plan de migration avec le client
- [ ] Identifier et documenter les points ouverts ou décisions à prendre
- [ ] Mettre à jour le backlog Phase 2 en fonction des retours
- [ ] Marquer toutes les issues Phase 1 comme terminées
- [ ] Créer le milestone Phase 2 dans GitHub Projects
**Livrable attendu :**
Compte-rendu de validation Phase 1 + backlog Phase 2 initialisé. Format Markdown.
---
## Workflow Kanban suggéré
| Colonne | Description |
|---|---|
| **Backlog** | Issues créées, non encore planifiées |
| **Todo** | Issues planifiées pour le sprint en cours |
| **In Progress** | Issues en cours de traitement |
| **In Review** | Issues terminées, en attente de validation |
| **Done** | Issues validées et livrables acceptés |
## Ordre de traitement recommandé
1. Commencer par les EPICs 1 et 2 (inventaire + architecture actuelle) — base de tout
2. Mener en parallèle les EPICs 3 et 4 (audit UX + audit SEO)
3. Traiter l'EPIC 5 (problèmes + opportunités) après les audits
4. Traiter les EPICs 6 et 7 (architecture future + mapping) après la synthèse
5. Terminer par l'EPIC 8 (documentation)
Collapse 861 lines
Now let me create the JSON data file for the issues (used by the automation script):


Create Docs/project/backlog/issues-data.json
Original file line number	Diff line number	Diff line change
{
  "labels": [
    { "name": "epic", "color": "1d76db", "description": "Issue de type EPIC (regroupement de tâches)" },
    { "name": "phase-1", "color": "0075ca", "description": "Tâches de la Phase 1 - Analyse de l'existant" },
    { "name": "content-inventory", "color": "e4e669", "description": "Inventaire et analyse du contenu" },
    { "name": "architecture", "color": "d93f0b", "description": "Architecture de l'information" },
    { "name": "ux-audit", "color": "0e8a16", "description": "Audit UX et parcours utilisateur" },
    { "name": "seo-audit", "color": "5319e7", "description": "Audit SEO" },
    { "name": "analysis", "color": "f9d0c4", "description": "Analyse et identification des problèmes" },
    { "name": "documentation", "color": "cfd3d7", "description": "Documentation et livrables" },
    { "name": "priority-high", "color": "b60205", "description": "Priorité haute" },
    { "name": "priority-medium", "color": "fbca04", "description": "Priorité moyenne" },
    { "name": "priority-low", "color": "0e8a16", "description": "Priorité basse" }
  ],
  "epics": [
    {
      "id": "E1",
      "title": "[EPIC 1] Inventaire complet du contenu du site actuel",
      "labels": ["epic", "phase-1", "content-inventory"],
      "body": "## 🎯 Objectif\n\nRéaliser un inventaire exhaustif de tout le contenu publié sur le site ihmn.be actuel.\n\nCet inventaire constitue la base de toutes les analyses suivantes et permet de ne rien oublier lors de la migration.\n\n## 📋 Issues associées\n\n- [ ] #issue-1.1 — Inventaire des pages institutionnelles\n- [ ] #issue-1.2 — Inventaire des pages de formations et des modules\n- [ ] #issue-1.3 — Inventaire et analyse de l'annuaire des thérapeutes\n- [ ] #issue-1.4 — Inventaire et analyse des documents PDF\n- [ ] #issue-1.5 — Inventaire et analyse de la FAQ\n\n## ✅ Définition of Done\n\nL'EPIC est terminé quand toutes les issues associées sont en statut **Done** et que les livrables ont été validés."
    },
    {
      "id": "E2",
      "title": "[EPIC 2] Analyse de l'architecture actuelle du site",
      "labels": ["epic", "phase-1", "architecture"],
      "body": "## 🎯 Objectif\n\nAnalyser en profondeur l'architecture de l'information du site actuel : structure des URLs, hiérarchie des pages, navigation, aspects techniques du CMS Joomla/Gridbox.\n\n## 📋 Issues associées\n\n- [ ] #issue-2.1 — Cartographie de la navigation et des menus\n- [ ] #issue-2.2 — Analyse de la structure des URLs\n- [ ] #issue-2.3 — Analyse de la hiérarchie des pages et du maillage interne\n- [ ] #issue-2.4 — Audit technique Joomla / Gridbox\n\n## ✅ Définition of Done\n\nL'EPIC est terminé quand toutes les issues associées sont en statut **Done** et que les livrables ont été validés."
    },
    {
      "id": "E3",
      "title": "[EPIC 3] Audit UX du site actuel",
      "labels": ["epic", "phase-1", "ux-audit"],
      "body": "## 🎯 Objectif\n\nAnalyser l'expérience utilisateur du site actuel : parcours de navigation, accessibilité, appels à l'action, expérience mobile. Identifier les freins et les points de friction dans le funnel d'inscription.\n\n## 📋 Issues associées\n\n- [ ] #issue-3.1 — Analyse du parcours utilisateur principal (funnel inscription)\n- [ ] #issue-3.2 — Analyse de la navigation et de l'accessibilité\n- [ ] #issue-3.3 — Analyse des appels à l'action (CTA)\n- [ ] #issue-3.4 — Analyse de l'expérience mobile et du responsive design\n\n## ✅ Définition of Done\n\nL'EPIC est terminé quand toutes les issues associées sont en statut **Done** et que les livrables ont été validés."
    },
    {
      "id": "E4",
      "title": "[EPIC 4] Audit SEO du site actuel",
      "labels": ["epic", "phase-1", "seo-audit"],
      "body": "## 🎯 Objectif\n\nRéaliser un audit SEO complet du site actuel pour identifier les problèmes techniques, les opportunités de contenu et les points d'amélioration avant la refonte.\n\n## 📋 Issues associées\n\n- [ ] #issue-4.1 — Audit des métadonnées et balises HTML\n- [ ] #issue-4.2 — Analyse des contenus et des mots-clés\n- [ ] #issue-4.3 — Audit des performances techniques (Core Web Vitals)\n- [ ] #issue-4.4 — Analyse des données structurées et du profil de liens\n\n## ✅ Définition of Done\n\nL'EPIC est terminé quand toutes les issues associées sont en statut **Done** et que les livrables ont été validés."
    },
    {
      "id": "E5",
      "title": "[EPIC 5] Identification des problèmes et des opportunités",
      "labels": ["epic", "phase-1", "analysis"],
      "body": "## 🎯 Objectif\n\nConsolider toutes les analyses précédentes pour dresser un tableau complet des problèmes structurels et des opportunités d'amélioration à adresser lors de la refonte.\n\n## 📋 Issues associées\n\n- [ ] #issue-5.1 — Synthèse des problèmes structurels identifiés\n- [ ] #issue-5.2 — Identification des opportunités SEO\n- [ ] #issue-5.3 — Analyse des gaps de contenu\n\n## ⚠️ Dépendances\n\nCet EPIC doit être traité **après** la complétion des EPICs 1, 2, 3 et 4.\n\n## ✅ Définition of Done\n\nL'EPIC est terminé quand toutes les issues associées sont en statut **Done** et que les livrables ont été validés."
    },
    {
      "id": "E6",
      "title": "[EPIC 6] Préparation de la future architecture",
      "labels": ["epic", "phase-1", "architecture"],
      "body": "## 🎯 Objectif\n\nSur la base des analyses précédentes, définir la nouvelle architecture de l'information, le sitemap futur et le content model du nouveau site.\n\n## 📋 Issues associées\n\n- [ ] #issue-6.1 — Définition de la nouvelle architecture de l'information\n- [ ] #issue-6.2 — Création du sitemap de la future architecture\n- [ ] #issue-6.3 — Définition du content model futur\n\n## ⚠️ Dépendances\n\nCet EPIC doit être traité **après** la complétion de l'EPIC 5.\n\n## ✅ Définition of Done\n\nL'EPIC est terminé quand toutes les issues associées sont en statut **Done** et que les livrables ont été validés."
    },
    {
      "id": "E7",
      "title": "[EPIC 7] Préparation du mapping des contenus",
      "labels": ["epic", "phase-1", "content-inventory"],
      "body": "## 🎯 Objectif\n\nCréer le mapping complet entre les contenus actuels et la future architecture : quelles pages vont où, quelles URLs changent, quels contenus sont créés ou supprimés.\n\n## 📋 Issues associées\n\n- [ ] #issue-7.1 — Mapping des URLs actuelles vers la nouvelle architecture\n- [ ] #issue-7.2 — Plan de redirections 301\n- [ ] #issue-7.3 — Identification des contenus à créer, modifier ou supprimer\n\n## ⚠️ Dépendances\n\nCet EPIC doit être traité **après** la complétion de l'EPIC 6.\n\n## ✅ Définition of Done\n\nL'EPIC est terminé quand toutes les issues associées sont en statut **Done** et que les livrables ont été validés."
    },
    {
      "id": "E8",
      "title": "[EPIC 8] Documentation de l'analyse Phase 1",
      "labels": ["epic", "phase-1", "documentation"],
      "body": "## 🎯 Objectif\n\nRédiger et livrer tous les documents de synthèse de la Phase 1 pour servir de base à la Phase 2 (conception et développement).\n\n## 📋 Issues associées\n\n- [ ] #issue-8.1 — Rédaction du rapport d'analyse complet Phase 1\n- [ ] #issue-8.2 — Préparation du brief technique pour la Phase 2\n- [ ] #issue-8.3 — Rétrospective et validation de la Phase 1\n\n## ⚠️ Dépendances\n\nCet EPIC doit être traité **après** la complétion de tous les EPICs précédents.\n\n## ✅ Définition of Done\n\nL'EPIC est terminé quand tous les livrables sont produits, validés par le client, et que le brief Phase 2 est prêt."
    }
  ],
  "issues": [
    {
      "id": "1.1",
      "epic": "E1",
      "title": "[1.1] Inventaire des pages institutionnelles",
      "labels": ["phase-1", "content-inventory", "priority-high"],
      "body": "## 🎯 Objectif\n\nRecenser et documenter toutes les pages institutionnelles du site actuel (pages hors formations et hors annuaire thérapeutes).\n\n## 📋 Checklist\n\n- [ ] Lister toutes les URLs des pages institutionnelles\n- [ ] Documenter le H1, le titre de page et la meta description de chaque page\n- [ ] Identifier le type de contenu (texte, images, formulaires, vidéos)\n- [ ] Évaluer la qualité du contenu (à conserver / à réviser / à supprimer)\n- [ ] Estimer le volume de contenu textuel (nombre de mots approximatif)\n- [ ] Identifier les images et médias associés à chaque page\n- [ ] Documenter les liens internes présents sur chaque page\n\n## 📄 Pages à inventorier\n\n- `/` — Accueil\n- `/ihmn` — IHMN (présentation de l'école)\n- `/ihmn/lhistoire-ihmn` — Histoire de l'IHMN\n- `/ihmn/en-pratique` — En pratique\n- `/ihmn/formateurs` — Nos formateurs\n- `/contact` — Contact\n- `/faq` — FAQ\n- `/mentions-legales` — Mentions légales\n\n## ✅ Livrable attendu\n\nTableau d'inventaire (CSV ou Markdown) avec colonnes :\n`URL | H1 | Titre | Meta description | Type de contenu | Qualité estimée | Volume textuel | Médias | Statut`\n\nStatuts possibles : `conserver` / `réviser` / `supprimer`\n\n---\n_EPIC parent : [EPIC 1] Inventaire complet du contenu du site actuel_"
    },
    {
      "id": "1.2",
      "epic": "E1",
      "title": "[1.2] Inventaire des pages de formations et des modules",
      "labels": ["phase-1", "content-inventory", "priority-high"],
      "body": "## 🎯 Objectif\n\nRecenser et documenter toutes les pages de formations et leurs modules de cours. Cette section est le cœur du site et nécessite une analyse détaillée.\n\n## 📋 Checklist\n\n- [ ] Lister toutes les URLs des pages de formations\n- [ ] Documenter la structure de chaque formation (années, modules)\n- [ ] Pour chaque module de cours, documenter : titre, formateur, durée, description, objectifs, méthodologie\n- [ ] Identifier les informations manquantes ou incomplètes dans les modules\n- [ ] Recenser les examens et certificats associés à chaque formation\n- [ ] Documenter les informations d'inscription et de tarifs\n- [ ] Identifier les incohérences ou doublons dans la présentation des formations\n\n## 📄 Pages à inventorier\n\n- `/formations` — Hub formations\n- `/formations/naturopathie` — Formation Naturopathie (4 ans, modules par année)\n- `/formations/hygiene-de-vie-et-nutrition` — Hygiène de vie et nutrition\n- `/formations/drainage-lymphatique-manuel` — Drainage lymphatique manuel\n- `/formations/formations-hors-cursus` — Formations hors cursus\n- `/formations/examens-certificats` — Examens & Certificats\n- `/formations/inscriptions-tarifs` — Inscriptions & Tarifs\n\n## ✅ Livrable attendu\n\n1. Tableau d'inventaire des formations (CSV/Markdown)\n2. Fiche détaillée par formation avec la liste complète des modules (titre, formateur, durée, description)\n\n---\n_EPIC parent : [EPIC 1] Inventaire complet du contenu du site actuel_"
    },
    {
      "id": "1.3",
      "epic": "E1",
      "title": "[1.3] Inventaire et analyse de l'annuaire des thérapeutes",
      "labels": ["phase-1", "content-inventory", "priority-medium"],
      "body": "## 🎯 Objectif\n\nRecenser et documenter la structure complète de l'annuaire des thérapeutes : pages régionales, fiches individuelles, système de pagination et carte interactive.\n\n## 📋 Checklist\n\n- [ ] Lister toutes les URLs des pages régionales de l'annuaire\n- [ ] Compter le nombre total de thérapeutes référencés\n- [ ] Documenter les informations présentes sur chaque fiche thérapeute (nom, région, spécialités, contact, photo, etc.)\n- [ ] Identifier les champs systématiquement renseignés vs les champs souvent vides\n- [ ] Analyser le système de pagination (nombre de pages, nombre par page)\n- [ ] Documenter le fonctionnement de la carte interactive\n- [ ] Identifier les thérapeutes présents dans plusieurs régions (doublons potentiels)\n- [ ] Analyser les filtres disponibles\n\n## 📄 Régions à inventorier\n\nBruxelles, Brabant Wallon, Brabant Flamand, Hainaut, Liège, Namur, Luxembourg, Limbourg, France\n\n## ✅ Livrable attendu\n\nInventaire structuré de l'annuaire :\n- Nombre de thérapeutes par région\n- Liste des champs disponibles sur les fiches\n- Analyse des doublons\n- Évaluation du système de navigation de l'annuaire\n\n---\n_EPIC parent : [EPIC 1] Inventaire complet du contenu du site actuel_"
    },
    {
      "id": "1.4",
      "epic": "E1",
      "title": "[1.4] Inventaire et analyse des documents PDF",
      "labels": ["phase-1", "content-inventory", "priority-medium"],
      "body": "## 🎯 Objectif\n\nRecenser tous les documents PDF publiés sur le site, évaluer leur pertinence et leur état, et préparer les recommandations pour la migration.\n\n## 📋 Checklist\n\n- [ ] Lister tous les PDF accessibles sur le site (inspection du code source + navigation)\n- [ ] Documenter pour chaque PDF : URL, nom du fichier, page de référencement, date estimée\n- [ ] Identifier les PDF obsolètes (tarifs anciens, contrats dépassés)\n- [ ] Identifier les PDF à conserver, mettre à jour ou supprimer\n- [ ] Vérifier les liens morts vers des PDF supprimés\n- [ ] Évaluer le format et l'accessibilité des PDF (mise en page, lisibilité)\n\n## 📄 PDFs connus\n\n- `ihmn_25-26_contrat_inscription_1e-anne.pdf`\n- `IHMN - Bourse 2025-26.pdf`\n- `ihmn---tarifs-2025-26.pdf`\n- `ihmn_mentions_legales_230601.pdf`\n\n## ✅ Livrable attendu\n\nTableau des PDFs :\n`URL | Nom | Page de référence | État | Action recommandée`\n\nActions : `conserver` / `mettre à jour` / `supprimer` / `remplacer par page web`\n\n---\n_EPIC parent : [EPIC 1] Inventaire complet du contenu du site actuel_"
    },
    {
      "id": "1.5",
      "epic": "E1",
      "title": "[1.5] Inventaire et analyse de la FAQ",
      "labels": ["phase-1", "content-inventory", "priority-medium"],
      "body": "## 🎯 Objectif\n\nRecenser et analyser toutes les questions/réponses de la FAQ, évaluer leur pertinence et préparer leur restructuration.\n\n## 📋 Checklist\n\n- [ ] Lister toutes les questions présentes dans la FAQ\n- [ ] Catégoriser les questions par thème (formation, inscription, naturopathie, école, etc.)\n- [ ] Identifier les questions redondantes ou trop similaires\n- [ ] Identifier les questions manquantes par rapport aux thèmes couverts\n- [ ] Évaluer la qualité et la complétude des réponses\n- [ ] Analyser le système d'affichage actuel (accordéon, liste, etc.)\n- [ ] Identifier les questions avec potentiel SEO (questions = requêtes utilisateur)\n\n## ✅ Livrable attendu\n\nInventaire complet de la FAQ catégorisé par thème + recommandations :\n- Questions à conserver\n- Questions à reformuler\n- Questions à supprimer\n- Questions à ajouter\n\n---\n_EPIC parent : [EPIC 1] Inventaire complet du contenu du site actuel_"
    },
    {
      "id": "2.1",
      "epic": "E2",
      "title": "[2.1] Cartographie de la navigation et des menus",
      "labels": ["phase-1", "architecture", "priority-high"],
      "body": "## 🎯 Objectif\n\nDocumenter et analyser tous les éléments de navigation du site : menus principaux, menus secondaires, liens en pied de page, liens contextuels.\n\n## 📋 Checklist\n\n- [ ] Documenter la structure du menu principal (items, sous-items, profondeur)\n- [ ] Documenter la structure du menu pied de page\n- [ ] Identifier les menus secondaires ou contextuels\n- [ ] Analyser la cohérence entre la navigation et la structure réelle des pages\n- [ ] Identifier les pages orphelines (non accessibles depuis la navigation)\n- [ ] Identifier les pages en doublon dans la navigation\n- [ ] Analyser le comportement du menu sur mobile (hamburger, accordéon, etc.)\n- [ ] Évaluer la profondeur maximale de navigation (nombre de clics depuis l'accueil)\n\n## ✅ Livrable attendu\n\n1. Diagramme/schéma de la navigation actuelle\n2. Tableau d'analyse : `item de menu | URL cible | profondeur | présence mobile`\n\n---\n_EPIC parent : [EPIC 2] Analyse de l'architecture actuelle du site_"
    },
    {
      "id": "2.2",
      "epic": "E2",
      "title": "[2.2] Analyse de la structure des URLs",
      "labels": ["phase-1", "architecture", "priority-high"],
      "body": "## 🎯 Objectif\n\nAnalyser les patterns d'URLs du site actuel pour identifier les bonnes pratiques et les problèmes avant la migration.\n\n## 📋 Checklist\n\n- [ ] Lister toutes les URLs du site (crawl complet via Screaming Frog ou équivalent)\n- [ ] Analyser les patterns de nommage des URLs\n- [ ] Identifier les URLs avec des paramètres (`?page=`, etc.)\n- [ ] Identifier les URLs trop longues ou mal structurées\n- [ ] Vérifier la cohérence linguistique des URLs (fr/en/mélange)\n- [ ] Identifier les URLs avec des caractères spéciaux ou des problèmes d'encodage\n- [ ] Vérifier la canonicalisation (`www` vs sans `www`, `http` vs `https`)\n- [ ] Lister les URLs des pages de pagination de l'annuaire\n\n## 🛠️ Outils suggérés\n\n- Screaming Frog SEO Spider\n- Sitebulb\n- Google Search Console > Couverture\n\n## ✅ Livrable attendu\n\nExport CSV de toutes les URLs :\n`URL | Profondeur | Code HTTP | Titre | H1 | Meta description | Liens entrants | Liens sortants`\n\n---\n_EPIC parent : [EPIC 2] Analyse de l'architecture actuelle du site_"
    },
    {
      "id": "2.3",
      "epic": "E2",
      "title": "[2.3] Analyse de la hiérarchie des pages et du maillage interne",
      "labels": ["phase-1", "architecture", "priority-medium"],
      "body": "## 🎯 Objectif\n\nAnalyser la hiérarchie des pages, le maillage interne et la cohérence éditoriale du site.\n\n## 📋 Checklist\n\n- [ ] Créer un sitemap visuel du site actuel\n- [ ] Analyser le maillage interne (liens entre les pages)\n- [ ] Identifier les pages avec peu ou pas de liens intrants\n- [ ] Identifier les opportunités de maillage interne non exploitées\n- [ ] Analyser la distribution du PageRank interne (pages les plus et moins liées)\n- [ ] Vérifier la présence et la cohérence des breadcrumbs\n- [ ] Analyser les liens entre formations, thérapeutes et pages institutionnelles\n\n## ✅ Livrable attendu\n\n1. Sitemap visuel du site actuel\n2. Analyse du maillage interne avec recommandations\n\n---\n_EPIC parent : [EPIC 2] Analyse de l'architecture actuelle du site_"
    },
    {
      "id": "2.4",
      "epic": "E2",
      "title": "[2.4] Audit technique Joomla / Gridbox",
      "labels": ["phase-1", "architecture", "priority-medium"],
      "body": "## 🎯 Objectif\n\nRéaliser un audit technique de l'infrastructure CMS actuelle pour identifier les contraintes et opportunités de la migration.\n\n## 📋 Checklist\n\n- [ ] Identifier la version de Joomla utilisée\n- [ ] Identifier la version de Gridbox et les extensions/plugins actifs\n- [ ] Documenter les types de contenus Joomla utilisés (articles, catégories, etc.)\n- [ ] Identifier les modules et plugins tiers installés\n- [ ] Analyser la structure de la base de données (tables, relations)\n- [ ] Évaluer les performances actuelles (temps de chargement, score PageSpeed)\n- [ ] Documenter le système d'hébergement actuel\n- [ ] Identifier les contraintes de migration (formats propriétaires, données liées)\n\n## ✅ Livrable attendu\n\nRapport technique (Markdown) :\n- Version CMS et extensions\n- Structure des données\n- Performances actuelles\n- Contraintes de migration identifiées\n\n---\n_EPIC parent : [EPIC 2] Analyse de l'architecture actuelle du site_"
    },
    {
      "id": "3.1",
      "epic": "E3",
      "title": "[3.1] Analyse du parcours utilisateur principal (funnel inscription)",
      "labels": ["phase-1", "ux-audit", "priority-high"],
      "body": "## 🎯 Objectif\n\nAnalyser le parcours d'un utilisateur souhaitant s'inscrire à une formation, de la page d'accueil jusqu'au formulaire d'inscription.\n\n## 📋 Checklist\n\n- [ ] Identifier les profils utilisateurs principaux (personas) :\n  - Futur étudiant en naturopathie\n  - Professionnel en reconversion\n  - Curieux de la naturopathie\n- [ ] Cartographier le parcours « découverte → information → décision → inscription »\n- [ ] Identifier toutes les pages du funnel d'inscription\n- [ ] Compter le nombre de clics nécessaires depuis l'accueil pour accéder au formulaire\n- [ ] Identifier les pages de sortie fréquentes dans le funnel\n- [ ] Analyser la lisibilité des informations sur les tarifs et modalités\n- [ ] Identifier les informations manquantes bloquant la décision d'inscription\n- [ ] Analyser la confiance générée par le site (témoignages, certifications, etc.)\n\n## ✅ Livrable attendu\n\nCarte du parcours utilisateur (user journey map) :\n- Étapes du parcours\n- Points de friction identifiés\n- Recommandations d'amélioration\n\n---\n_EPIC parent : [EPIC 3] Audit UX du site actuel_"
    },
    {
      "id": "3.2",
      "epic": "E3",
      "title": "[3.2] Analyse de la navigation et de l'accessibilité",
      "labels": ["phase-1", "ux-audit", "priority-high"],
      "body": "## 🎯 Objectif\n\nÉvaluer la facilité de navigation et l'accessibilité globale du site pour tous les types d'utilisateurs.\n\n## 📋 Checklist\n\n- [ ] Évaluer la clarté et l'intuitivité du menu principal\n- [ ] Analyser la visibilité des éléments de navigation (contraste, taille)\n- [ ] Tester la navigation au clavier (accessibilité)\n- [ ] Vérifier la présence et la pertinence des balises ARIA\n- [ ] Analyser les contrastes de couleurs (WCAG AA minimum)\n- [ ] Évaluer la lisibilité des textes (taille de police, espacement, longueur des lignes)\n- [ ] Analyser la hiérarchie visuelle des pages (H1, H2, H3, paragraphes)\n- [ ] Identifier les éléments interactifs sans feedback visuel clair\n- [ ] Évaluer la cohérence visuelle entre les pages\n\n## 🛠️ Outils suggérés\n\n- WAVE Accessibility Tool\n- axe DevTools\n- Colour Contrast Analyser\n\n## ✅ Livrable attendu\n\nRapport d'accessibilité et de navigation :\n- Score global\n- Liste priorisée des problèmes identifiés\n- Recommandations d'amélioration\n\n---\n_EPIC parent : [EPIC 3] Audit UX du site actuel_"
    },
    {
      "id": "3.3",
      "epic": "E3",
      "title": "[3.3] Analyse des appels à l'action (CTA)",
      "labels": ["phase-1", "ux-audit", "priority-medium"],
      "body": "## 🎯 Objectif\n\nRecenser et évaluer tous les appels à l'action du site pour identifier leur efficacité et leur cohérence avec les objectifs du site.\n\n## 📋 Checklist\n\n- [ ] Lister tous les CTA présents sur le site (boutons, liens d'action)\n- [ ] Analyser la clarté et la lisibilité de chaque CTA\n- [ ] Évaluer le positionnement des CTA (above/below the fold)\n- [ ] Identifier les pages sans CTA clair\n- [ ] Analyser la cohérence des CTA avec les objectifs de chaque page\n- [ ] Identifier les CTA manquants sur les pages clés (formations, accueil)\n- [ ] Évaluer l'urgence/motivation créée par les CTA actuels\n- [ ] Comparer les CTA selon les devices (desktop vs mobile)\n\n## ✅ Livrable attendu\n\nInventaire des CTA :\n- Tableau : `page | CTA | positionnement | évaluation`\n- Recommandations d'amélioration\n\n---\n_EPIC parent : [EPIC 3] Audit UX du site actuel_"
    },
    {
      "id": "3.4",
      "epic": "E3",
      "title": "[3.4] Analyse de l'expérience mobile et du responsive design",
      "labels": ["phase-1", "ux-audit", "priority-high"],
      "body": "## 🎯 Objectif\n\nTester et analyser l'expérience utilisateur sur mobile (smartphones et tablettes).\n\n## 📋 Checklist\n\n- [ ] Tester l'affichage sur 3 tailles d'écran : mobile (375px), tablette (768px), desktop (1280px)\n- [ ] Vérifier le test « Mobile-Friendly » de Google Search Console\n- [ ] Analyser la vitesse de chargement sur mobile (score PageSpeed Insights)\n- [ ] Identifier les éléments non adaptés au mobile (tableaux larges, textes trop petits, etc.)\n- [ ] Tester les formulaires sur mobile (facilité de saisie)\n- [ ] Analyser le comportement des modales (modules de cours) sur mobile\n- [ ] Évaluer l'accessibilité du menu hamburger sur mobile\n- [ ] Identifier les images non optimisées pour mobile\n\n## 🛠️ Outils suggérés\n\n- Chrome DevTools (Device Mode)\n- Google PageSpeed Insights\n- BrowserStack\n\n## ✅ Livrable attendu\n\nRapport d'audit mobile :\n- Captures d'écran des problèmes identifiés\n- Score de performance mobile (PageSpeed)\n- Liste des corrections recommandées\n\n---\n_EPIC parent : [EPIC 3] Audit UX du site actuel_"
    },
    {
      "id": "4.1",
      "epic": "E4",
      "title": "[4.1] Audit des métadonnées et balises HTML",
      "labels": ["phase-1", "seo-audit", "priority-high"],
      "body": "## 🎯 Objectif\n\nAnalyser les métadonnées, titres et balises HTML de toutes les pages pour identifier les problèmes SEO on-page.\n\n## 📋 Checklist\n\n- [ ] Vérifier la présence et l'unicité des titres `<title>` sur toutes les pages\n- [ ] Vérifier la présence et la qualité des meta descriptions\n- [ ] Analyser la structure des balises H1/H2/H3 sur chaque page\n- [ ] Identifier les pages avec H1 manquant ou multiples H1\n- [ ] Vérifier la présence des balises Open Graph (og:title, og:description, og:image)\n- [ ] Vérifier les balises canonical\n- [ ] Analyser le `robots.txt` et le `sitemap.xml`\n- [ ] Vérifier la présence de données structurées (Schema.org)\n- [ ] Identifier les titres dupliqués ou hors normes (< 30 ou > 60 caractères)\n\n## 🛠️ Outils suggérés\n\n- Screaming Frog SEO Spider\n- Google Search Console\n- SEOptimer\n\n## ✅ Livrable attendu\n\nRapport des métadonnées SEO :\n- Tableau page par page\n- Liste des corrections prioritaires\n\n---\n_EPIC parent : [EPIC 4] Audit SEO du site actuel_"
    },
    {
      "id": "4.2",
      "epic": "E4",
      "title": "[4.2] Analyse des contenus et des mots-clés",
      "labels": ["phase-1", "seo-audit", "priority-high"],
      "body": "## 🎯 Objectif\n\nAnalyser le positionnement actuel du site sur les mots-clés cibles et identifier les opportunités SEO de contenu.\n\n## 📋 Checklist\n\n- [ ] Identifier les mots-clés principaux actuellement ciblés\n- [ ] Analyser le positionnement Google sur les mots-clés stratégiques :\n  - « naturopathie belgique »\n  - « formation naturopathie »\n  - « école naturopathie »\n  - « thérapeute naturopathe »\n- [ ] Utiliser Google Search Console pour extraire les requêtes et le CTR\n- [ ] Analyser la densité des mots-clés sur les pages principales\n- [ ] Identifier les cannibalisation de mots-clés\n- [ ] Identifier les mots-clés manquants à fort potentiel\n- [ ] Analyser les contenus des concurrents directs (benchmark)\n- [ ] Identifier les questions de l'annuaire thérapeutes exploitables en SEO\n\n## 🛠️ Outils suggérés\n\n- Google Search Console\n- SEMrush / Ahrefs\n- Ubersuggest\n- AnswerThePublic\n\n## ✅ Livrable attendu\n\nTableau de mots-clés (CSV) :\n`mot-clé | volume mensuel | position actuelle | page ciblée | opportunité`\n\n---\n_EPIC parent : [EPIC 4] Audit SEO du site actuel_"
    },
    {
      "id": "4.3",
      "epic": "E4",
      "title": "[4.3] Audit des performances techniques (Core Web Vitals)",
      "labels": ["phase-1", "seo-audit", "priority-high"],
      "body": "## 🎯 Objectif\n\nMesurer et analyser les performances techniques du site qui impactent le référencement (Core Web Vitals, vitesse de chargement).\n\n## 📋 Checklist\n\n- [ ] Mesurer les Core Web Vitals (LCP, INP, CLS) sur les pages principales\n- [ ] Analyser le score PageSpeed Insights desktop et mobile\n- [ ] Analyser le temps de chargement total (TTFB, FCP, LCP)\n- [ ] Identifier les ressources bloquant le rendu (render-blocking)\n- [ ] Analyser le poids des images et leur format (WebP vs JPEG/PNG)\n- [ ] Vérifier la présence d'un cache serveur\n- [ ] Analyser le code JavaScript et CSS (minification, bundling)\n- [ ] Vérifier le protocole HTTPS et la validité du certificat SSL\n- [ ] Analyser les erreurs 4xx et 5xx via Search Console\n\n## 🛠️ Outils suggérés\n\n- Google PageSpeed Insights\n- GTmetrix\n- Lighthouse (Chrome DevTools)\n- Google Search Console > Expérience\n\n## ✅ Livrable attendu\n\nRapport de performances :\n- Scores LCP/INP/CLS par page principale\n- Liste des optimisations techniques recommandées\n\n---\n_EPIC parent : [EPIC 4] Audit SEO du site actuel_"
    },
    {
      "id": "4.4",
      "epic": "E4",
      "title": "[4.4] Analyse des données structurées et du profil de liens",
      "labels": ["phase-1", "seo-audit", "priority-medium"],
      "body": "## 🎯 Objectif\n\nAnalyser les données structurées (Schema.org) et le profil de backlinks du site pour évaluer l'autorité de domaine.\n\n## 📋 Checklist\n\n- [ ] Vérifier la présence et la validité des données structurées existantes\n- [ ] Identifier les opportunités de balisage Schema.org :\n  - `Organization`\n  - `Course`\n  - `FAQPage`\n  - `BreadcrumbList`\n  - `LocalBusiness`\n- [ ] Analyser le profil de backlinks (domaines référents, ancres, qualité)\n- [ ] Identifier les backlinks toxiques à désavouer\n- [ ] Analyser le Domain Authority / Domain Rating actuel\n- [ ] Identifier les opportunités de netlinking (annuaires santé, associations)\n- [ ] Vérifier les mentions de la marque non liées (unlinked brand mentions)\n\n## 🛠️ Outils suggérés\n\n- Ahrefs / Majestic\n- Google Search Console\n- Schema Markup Validator\n\n## ✅ Livrable attendu\n\nRapport backlinks + recommandations Schema.org à implémenter\n\n---\n_EPIC parent : [EPIC 4] Audit SEO du site actuel_"
    },
    {
      "id": "5.1",
      "epic": "E5",
      "title": "[5.1] Synthèse des problèmes structurels identifiés",
      "labels": ["phase-1", "analysis", "priority-high"],
      "body": "## 🎯 Objectif\n\nConsolider les résultats des audits (UX, SEO, technique, contenu) en une synthèse priorisée des problèmes à résoudre lors de la refonte.\n\n## ⚠️ Prérequis\n\nCette issue doit être traitée après la complétion des EPICs 1, 2, 3 et 4.\n\n## 📋 Checklist\n\n- [ ] Regrouper les problèmes identifiés dans les EPICs 1 à 4 par catégorie\n- [ ] Prioriser les problèmes selon leur impact (high / medium / low)\n- [ ] Pour chaque problème : décrire l'impact utilisateur ET l'impact SEO\n- [ ] Identifier les problèmes bloquants pour la migration\n- [ ] Identifier les quick wins (améliorations rapides à fort impact)\n- [ ] Associer chaque problème à une recommandation de solution\n- [ ] Valider la synthèse avec le client/chef de projet\n\n## 📝 Problèmes déjà identifiés (base de départ)\n\n- Design daté\n- Navigation peu claire\n- Hiérarchie visuelle faible\n- Absence de blog SEO\n- Parcours utilisateur peu guidé\n- Pages longues et difficiles à parcourir\n- SEO sous-exploité\n\n## ✅ Livrable attendu\n\nDocument de synthèse des problèmes priorisés :\n`problème | catégorie | impact | priorité | solution recommandée`\n\n---\n_EPIC parent : [EPIC 5] Identification des problèmes et des opportunités_"
    },
    {
      "id": "5.2",
      "epic": "E5",
      "title": "[5.2] Identification des opportunités SEO",
      "labels": ["phase-1", "analysis", "seo-audit", "priority-high"],
      "body": "## 🎯 Objectif\n\nIdentifier et prioriser toutes les opportunités SEO à exploiter lors de la refonte du site.\n\n## ⚠️ Prérequis\n\nCette issue doit être traitée après la complétion de l'EPIC 4 (Audit SEO).\n\n## 📋 Checklist\n\n- [ ] Identifier les mots-clés à fort potentiel non encore ciblés\n- [ ] Analyser les questions utilisateurs autour de la naturopathie (People Also Ask, forums)\n- [ ] Identifier les contenus de blog à fort potentiel SEO à créer\n- [ ] Analyser les pages de résultats Google pour les requêtes cibles (SERP analysis)\n- [ ] Identifier les featured snippets potentiels (FAQ, définitions, listes)\n- [ ] Analyser les opportunités de référencement local (naturopathie Belgique, par ville)\n- [ ] Identifier les opportunités de création de pages piliers + cluster de contenus\n- [ ] Évaluer le potentiel SEO de l'annuaire thérapeutes (pages régionales)\n\n## 📝 Opportunités déjà identifiées (base de départ)\n\n- Création d'un blog SEO sur la naturopathie\n- Restructuration des pages formations pour le SEO\n- Meilleure mise en avant des témoignages\n- Simplification du parcours inscription\n- Pages thérapeutes par ville/région comme levier SEO local\n\n## ✅ Livrable attendu\n\nListe priorisée des opportunités SEO :\n`opportunité | trafic potentiel estimé | effort d'implémentation | priorité`\n\n---\n_EPIC parent : [EPIC 5] Identification des problèmes et des opportunités_"
    },
    {
      "id": "5.3",
      "epic": "E5",
      "title": "[5.3] Analyse des gaps de contenu",
      "labels": ["phase-1", "analysis", "content-inventory", "priority-medium"],
      "body": "## 🎯 Objectif\n\nIdentifier le contenu manquant sur le site actuel par rapport aux besoins des utilisateurs et aux standards du secteur.\n\n## 📋 Checklist\n\n- [ ] Analyser les questions fréquentes non couvertes par le site actuel\n- [ ] Identifier les informations que les candidats recherchent avant de s'inscrire\n- [ ] Comparer le contenu du site avec les sites concurrents (benchmark de contenu)\n- [ ] Identifier les pages manquantes nécessaires pour le SEO\n- [ ] Analyser les données de Search Console pour identifier des requêtes sans page dédiée\n- [ ] Identifier les témoignages et cas d'usage manquants\n- [ ] Analyser les besoins de contenu pour chaque étape du funnel d'inscription\n- [ ] Lister les contenus à créer pour la Phase 2 de la refonte\n\n## ✅ Livrable attendu\n\nGap analysis de contenu :\n`contenu manquant | type | priorité | phase de création recommandée`\n\n---\n_EPIC parent : [EPIC 5] Identification des problèmes et des opportunités_"
    },
    {
      "id": "6.1",
      "epic": "E6",
      "title": "[6.1] Définition de la nouvelle architecture de l'information",
      "labels": ["phase-1", "architecture", "priority-high"],
      "body": "## 🎯 Objectif\n\nDéfinir la structure des sections et sous-sections du futur site, en tenant compte des objectifs SEO, UX et des contraintes du contenu existant.\n\n## ⚠️ Prérequis\n\nCette issue doit être traitée après la complétion de l'EPIC 5.\n\n## 📋 Checklist\n\n- [ ] Définir les sections principales de la nouvelle architecture\n- [ ] Définir la hiérarchie des sous-pages pour chaque section\n- [ ] Valider l'architecture avec les objectifs SEO (mots-clés par section)\n- [ ] Valider l'architecture avec le parcours utilisateur cible\n- [ ] Définir la profondeur maximale de navigation (3 niveaux max)\n- [ ] Identifier les nouvelles pages à créer (blog, page pilier, nouvelles formations)\n- [ ] Documenter la logique de chaque section et son rôle dans le funnel\n\n## 🏗️ Architecture proposée à valider\n\n```\nAccueil\n├── Formation Naturopathie\n│   ├── Programme Année 1\n│   ├── Programme Année 2\n│   ├── Programme Année 3\n│   ├── Programme Année 4\n│   └── Examens & Certifications\n├── Hygiène de vie et Nutrition\n├── Drainage Lymphatique Manuel\n├── Formations Complémentaires\n├── Admissions\n│   ├── Inscription\n│   └── Tarifs\n├── L'école\n│   ├── Histoire\n│   ├── Philosophie\n│   └── Formateurs\n├── Thérapeutes (annuaire)\n├── Blog\n├── FAQ\n├── Contact\n└── Mentions légales\n```\n\n## ✅ Livrable attendu\n\nDocument d'architecture de l'information validé avec schéma visuel de la hiérarchie des pages\n\n---\n_EPIC parent : [EPIC 6] Préparation de la future architecture_"
    },
    {
      "id": "6.2",
      "epic": "E6",
      "title": "[6.2] Création du sitemap de la future architecture",
      "labels": ["phase-1", "architecture", "priority-medium"],
      "body": "## 🎯 Objectif\n\nCréer le sitemap complet du futur site avec toutes les URLs planifiées et leur hiérarchie.\n\n## 📋 Checklist\n\n- [ ] Définir la nomenclature des URLs futures (conventions de nommage)\n- [ ] Créer le sitemap arborescent complet du futur site\n- [ ] Définir les nouvelles URLs pour chaque page (SEO-friendly)\n- [ ] Identifier les URLs à conserver à l'identique (bon positionnement SEO existant)\n- [ ] Documenter les URLs qui changeront (nécessitant une redirection 301)\n- [ ] Valider le sitemap avec le client/chef de projet\n- [ ] Préparer la liste des redirections 301 nécessaires\n\n## ✅ Livrable attendu\n\n1. Sitemap complet du futur site (toutes les URLs planifiées)\n2. Document des nouvelles conventions d'URLs\n\n---\n_EPIC parent : [EPIC 6] Préparation de la future architecture_"
    },
    {
      "id": "6.3",
      "epic": "E6",
      "title": "[6.3] Définition du content model futur",
      "labels": ["phase-1", "architecture", "content-inventory", "priority-high"],
      "body": "## 🎯 Objectif\n\nDéfinir les types de contenus du futur site, leurs champs, leurs relations et leur structure pour le nouveau CMS.\n\n## 📋 Checklist\n\n- [ ] Lister tous les types de contenus nécessaires\n- [ ] Pour chaque type de contenu, définir les champs avec leur type de données\n- [ ] Définir les relations entre les types de contenus\n- [ ] Définir les règles de validation des champs\n- [ ] Identifier les champs communs entre types de contenus\n- [ ] Définir les règles d'affichage pour chaque type\n- [ ] Valider le content model avec les besoins SEO\n- [ ] Documenter les contraintes de migration des données existantes\n\n## 📦 Types de contenus à modéliser\n\n| Type | Description |\n|---|---|\n| `Page` | Page institutionnelle |\n| `Formation` | Cursus complet ou atelier hors cursus |\n| `Module de cours` | Appartenant à une Formation et une Année |\n| `Formateur` | Profil d'un formateur |\n| `Thérapeute` | Praticien avec région, spécialités, contact |\n| `Article de blog` | Article SEO |\n| `FAQ` | Question + réponse + catégorie |\n| `Document` | Fichier PDF |\n\n## ✅ Livrable attendu\n\nContent model complet avec :\n- Diagramme de types de contenus et leurs relations\n- Définition de tous les champs pour chaque type\n\n---\n_EPIC parent : [EPIC 6] Préparation de la future architecture_"
    },
    {
      "id": "7.1",
      "epic": "E7",
      "title": "[7.1] Mapping des URLs actuelles vers la nouvelle architecture",
      "labels": ["phase-1", "content-inventory", "architecture", "priority-high"],
      "body": "## 🎯 Objectif\n\nCréer le tableau de correspondance entre chaque URL actuelle et son équivalent dans la nouvelle architecture.\n\n## ⚠️ Prérequis\n\nCette issue dépend de l'Issue 2.2 (liste des URLs actuelles) et de l'Issue 6.2 (sitemap futur).\n\n## 📋 Checklist\n\n- [ ] Partir de l'inventaire complet des URLs actuelles (Issue 2.2)\n- [ ] Associer chaque URL actuelle à sa destination dans la nouvelle architecture\n- [ ] Documenter le statut de chaque URL : conserver / rediriger / fusionner / supprimer\n- [ ] Identifier les contenus qui seront fusionnés sur une seule page\n- [ ] Identifier les contenus qui seront découpés sur plusieurs pages\n- [ ] Vérifier qu'aucune URL stratégique (bon SEO) n'est supprimée sans redirection\n- [ ] Documenter les changements de structure pour les modules de formations\n\n## 📋 Mapping partiel existant (à compléter)\n\n| Ancienne URL | Nouvelle URL | Action |\n|---|---|---|\n| `/` | `/` | Conserver |\n| `/formations` | `/formations` | Conserver / Rediriger |\n| `/formations/naturopathie` | `/formations/naturopathie` | À valider |\n| `/formations/inscriptions-tarifs` | `/admissions` | Rediriger |\n| `/ihmn` | `/ecole` | Rediriger |\n| `/ihmn/formateurs` | `/ecole/formateurs` | Rediriger |\n| `/nos-therapeuthes` | `/therapeutes` | Rediriger |\n| `/faq` | `/faq` | Conserver |\n\n## ✅ Livrable attendu\n\nTableau complet de mapping URL (CSV) :\n`ancienne URL | nouvelle URL | action | priorité SEO`\n\n---\n_EPIC parent : [EPIC 7] Préparation du mapping des contenus_"
    },
    {
      "id": "7.2",
      "epic": "E7",
      "title": "[7.2] Plan de redirections 301",
      "labels": ["phase-1", "architecture", "seo-audit", "priority-high"],
      "body": "## 🎯 Objectif\n\nPréparer le plan complet des redirections 301 nécessaires lors du lancement du nouveau site pour préserver le capital SEO.\n\n## ⚠️ Prérequis\n\nCette issue dépend de l'Issue 7.1 (mapping des URLs).\n\n## 📋 Checklist\n\n- [ ] Lister toutes les URLs qui changeront lors de la migration\n- [ ] Définir la règle de redirection pour chaque URL (URL par URL ou pattern regex)\n- [ ] Prioriser les redirections selon l'importance SEO de chaque page\n- [ ] Identifier les redirections en chaîne à éviter (A→B→C)\n- [ ] Documenter les cas particuliers (pages de pagination, pages de filtres)\n- [ ] Préparer le fichier `.htaccess` ou équivalent pour le serveur\n- [ ] Prévoir un processus de vérification post-lancement\n- [ ] Identifier les backlinks externes pointant vers des URLs qui changeront\n\n## ✅ Livrable attendu\n\n1. Plan de redirections 301 complet (CSV) :\n`ancienne URL | nouvelle URL | type de règle | priorité`\n\n2. Fichier de configuration serveur prêt à l'emploi (`.htaccess` ou équivalent)\n\n---\n_EPIC parent : [EPIC 7] Préparation du mapping des contenus_"
    },
    {
      "id": "7.3",
      "epic": "E7",
      "title": "[7.3] Identification des contenus à créer, modifier ou supprimer",
      "labels": ["phase-1", "content-inventory", "priority-medium"],
      "body": "## 🎯 Objectif\n\nCréer le plan éditorial de migration : quels contenus sont migrés à l'identique, lesquels nécessitent une révision, lesquels sont nouveaux et lesquels sont supprimés.\n\n## 📋 Checklist\n\n- [ ] Pour chaque page existante : définir l'action (migrer / réécrire / fusionner / supprimer)\n- [ ] Identifier les contenus nécessitant une mise à jour avant migration\n- [ ] Lister les nouvelles pages à créer ex nihilo pour la refonte\n- [ ] Estimer l'effort de rédaction/révision pour chaque contenu\n- [ ] Identifier les contenus nécessitant une validation côté client\n- [ ] Préparer un brief de rédaction pour les nouveaux contenus\n- [ ] Planifier la production de contenu (ordre de priorité)\n\n## ✅ Livrable attendu\n\nPlan éditorial de migration (CSV/Markdown) :\n`page | action | priorité | effort estimé | responsable | statut`\n\nActions : `migrer` / `réécrire` / `fusionner` / `supprimer` / `créer`\n\n---\n_EPIC parent : [EPIC 7] Préparation du mapping des contenus_"
    },
    {
      "id": "8.1",
      "epic": "E8",
      "title": "[8.1] Rédaction du rapport d'analyse complet Phase 1",
      "labels": ["phase-1", "documentation", "priority-high"],
      "body": "## 🎯 Objectif\n\nRédiger le rapport d'analyse complet de la Phase 1 intégrant tous les livrables produits lors des EPICs 1 à 7.\n\n## ⚠️ Prérequis\n\nCette issue doit être traitée après la complétion de tous les EPICs 1 à 7.\n\n## 📋 Checklist\n\n- [ ] Rédiger l'introduction et le contexte du projet\n- [ ] Synthétiser l'inventaire du contenu (résumé des volumes et de la qualité)\n- [ ] Synthétiser l'analyse de l'architecture actuelle\n- [ ] Synthétiser l'audit UX (points clés, problèmes identifiés)\n- [ ] Synthétiser l'audit SEO (problèmes et opportunités)\n- [ ] Présenter la nouvelle architecture proposée avec justifications\n- [ ] Présenter le content model futur\n- [ ] Présenter le plan de migration (mapping + redirections)\n- [ ] Rédiger les recommandations priorisées pour la Phase 2\n- [ ] Relire et valider le rapport avec toutes les parties prenantes\n\n## 📄 Structure du rapport\n\n1. Résumé exécutif\n2. Inventaire du contenu actuel\n3. Analyse de l'architecture actuelle\n4. Audit UX\n5. Audit SEO\n6. Problèmes identifiés et opportunités\n7. Architecture future proposée\n8. Content model\n9. Plan de migration\n10. Recommandations Phase 2\n\n## ✅ Livrable attendu\n\nRapport complet Phase 1 stocké dans `Docs/project/backlog/rapport-phase-1.md`\n\n---\n_EPIC parent : [EPIC 8] Documentation de l'analyse Phase 1_"
    },
    {
      "id": "8.2",
      "epic": "E8",
      "title": "[8.2] Préparation du brief technique pour la Phase 2",
      "labels": ["phase-1", "documentation", "priority-medium"],
      "body": "## 🎯 Objectif\n\nRédiger le brief technique qui servira de base au développement du nouveau site lors de la Phase 2.\n\n## 📋 Checklist\n\n- [ ] Documenter les exigences fonctionnelles (fonctionnalités requises)\n- [ ] Documenter les exigences techniques (CMS cible, hébergement, performances)\n- [ ] Documenter les exigences SEO (structure des URLs, données structurées, etc.)\n- [ ] Documenter les exigences d'accessibilité (WCAG AA minimum)\n- [ ] Documenter les exigences de design (charte graphique, typographie)\n- [ ] Décrire les intégrations nécessaires (formulaires, carte thérapeutes, etc.)\n- [ ] Définir les critères d'acceptance pour la Phase 2\n- [ ] Préparer la liste des livrables attendus pour la Phase 2\n- [ ] Estimer le plan de développement Phase 2 (épics, sprints, timeline)\n\n## ✅ Livrable attendu\n\nBrief technique Phase 2 complet stocké dans `Docs/project/phase-2-brief.md`\n\n---\n_EPIC parent : [EPIC 8] Documentation de l'analyse Phase 1_"
    },
    {
      "id": "8.3",
      "epic": "E8",
      "title": "[8.3] Rétrospective et validation de la Phase 1",
      "labels": ["phase-1", "documentation", "priority-low"],
      "body": "## 🎯 Objectif\n\nRéaliser la rétrospective de la Phase 1 : valider tous les livrables, recueillir les retours du client et préparer le lancement de la Phase 2.\n\n## 📋 Checklist\n\n- [ ] Vérifier la complétude de tous les livrables de la Phase 1\n- [ ] Préparer et présenter le rapport Phase 1 au client\n- [ ] Recueillir et documenter les retours et décisions du client\n- [ ] Valider l'architecture future proposée avec le client\n- [ ] Valider le plan de migration avec le client\n- [ ] Identifier et documenter les points ouverts ou décisions à prendre\n- [ ] Mettre à jour le backlog Phase 2 en fonction des retours\n- [ ] Marquer toutes les issues Phase 1 comme terminées\n- [ ] Créer le milestone Phase 2 dans GitHub Projects\n\n## ✅ Livrable attendu\n\n1. Compte-rendu de validation Phase 1\n2. Backlog Phase 2 initialisé\n\n---\n_EPIC parent : [EPIC 8] Documentation de l'analyse Phase 1_"
    }
  ]
}
Collapse 252 lines
Now let me create the GitHub Actions workflow to create all issues:


Create .github/workflows/create-phase1-issues.yml
Copilot finished the session before it could pick up this message
peut tu toi-meme creer des issues ?
mgamsdve's avatar
Copilot's work was cancelled
The session was cancelled by the user.
Send message
This pull request was merged. To continue iterating, start a new session.

