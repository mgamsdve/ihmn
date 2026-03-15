# Analyse de la structure des URLs — IHMN (2026)

## Description

Cette analyse examine la structure des URLs du site https://ihmn.be afin d'identifier :

- les patterns de nommage
- les incohérences structurelles
- les problèmes potentiels pour le SEO
- les améliorations possibles lors de la migration du site.

L’analyse est basée sur un crawl complet du site et sur l’exploration manuelle des pages.

---

# 1. Structure générale des URLs

Le site utilise une structure relativement simple et lisible.

Les principales sections sont organisées comme suit :

/

 /formations

 /formations/naturopathie

 /formations/hygiene-de-vie-et-nutrition

 /formations/drainage-lymphatique-manuel

 /formations/formations-hors-cursus

 /formations/examens-certificats

 /formations/inscriptions-tarifs

 /ihmn

 /ihmn/lhistoire-ihmn

 /ihmn/en-pratique

 /ihmn/formateurs

 /faq

 /contact

 /mentions-legales

La structure générale repose donc sur quelques grandes sections clairement identifiables.

---

# 2. Patterns de nommage

Les URLs utilisent majoritairement :

- des mots en français
- des tirets pour séparer les mots
- des structures relativement courtes.

Exemple :

hygiene-de-vie-et-nutrition

Ce pattern est conforme aux bonnes pratiques SEO.

---

# 3. Cohérence linguistique

Les URLs sont entièrement en français.

Aucune structure multilingue n’est présente.

Le site ne propose qu’une seule langue.

---

# 4. URLs redondantes

Une redondance apparaît dans certaines URLs.

Exemple :

/formations/formations-hors-cursus

La répétition du mot *formations* n’est pas idéale et pourrait être simplifiée lors de la refonte.

---

# 5. Pagination

Certaines sections utilisent une pagination avec paramètres.

Exemple :

/nos-therapeuthes?page=1  
/nos-therapeuthes?page=2  
/nos-therapeuthes?page=3  
/nos-therapeuthes?page=4  

Ces URLs correspondent à la pagination de l’annuaire des thérapeutes.

Ce fonctionnement est normal et ne pose pas de problème particulier.

---

# 6. URLs avec ancres (#)

Le site utilise fréquemment des ancres d’URL pour gérer l’affichage dynamique de certains contenus.

Exemples :

- accordéons de la FAQ
- sections internes de page
- modales des modules de formation.

Ces URLs prennent la forme :

/faq#collapse-1682976300268  
/faq#accordion-1682976374378  

Ces ancres permettent d’ouvrir automatiquement un élément de la page.

Cependant :

- ces contenus ne correspondent pas à de véritables pages
- ils ne possèdent pas d’URL indépendante.

---

# 7. Contenus sans URL propre

Plusieurs contenus importants ne possèdent pas d’URL dédiée.

Exemple :

modules de formation.

Les informations pédagogiques sont affichées via :

- fenêtres modales
- interactions JavaScript.

Conséquences :

- impossibilité de partager un module spécifique
- indexation SEO limitée
- navigation interne moins claire.

---

# 8. Canonicalisation

Le site est accessible avec et sans "www".

Exemple :

https://www.ihmn.be/faq

redirige vers :

https://ihmn.be/faq

Cela indique que la redirection vers la version non-www est correctement configurée.

La version canonique du site est donc :

https://ihmn.be

---

# 9. Caractères spéciaux

Quelques URLs contiennent des caractères encodés.

Cela concerne principalement les documents PDF.

Exemple :

IHMN%20-%20Bourse%202025-26.pdf

Cela est normal pour des fichiers téléchargés.

---

# 10. Analyse SEO

Points positifs :

- URLs lisibles
- utilisation de tirets
- structure simple
- redirection www correctement configurée.

Points perfectibles :

- certaines URLs redondantes
- absence d’URL pour certains contenus pédagogiques
- utilisation de modales pour des contenus importants.

---

# 11. Recommandations pour la refonte

Lors de la migration du site, plusieurs améliorations sont recommandées.

## créer des pages pour les modules

exemple :

/formations/naturopathie/anatomie-physiologie

---

## améliorer la structure pédagogique

exemple :

/formations/naturopathie/programme  
/formations/naturopathie/annee-1

---

## simplifier certaines URLs

exemple :

/formations/hors-cursus

au lieu de :

/formations/formations-hors-cursus

---

# Conclusion

La structure actuelle des URLs du site IHMN est globalement simple et lisible.

Cependant certains contenus importants ne disposent pas d’URL propre et sont affichés uniquement via des interactions JavaScript.

Lors de la refonte du site, il sera pertinent de créer des URLs dédiées pour ces contenus afin d’améliorer :

- la navigation
- le partage de contenu
- le référencement naturel.