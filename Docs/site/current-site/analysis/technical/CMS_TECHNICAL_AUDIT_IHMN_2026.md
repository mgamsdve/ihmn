# CMS_TECHNICAL_AUDIT_IHMN_2026

## Description

Cet audit analyse l'infrastructure technique du site actuel https://ihmn.be afin d'identifier :

- le CMS utilisé
- les extensions installées
- la structure du contenu
- les performances actuelles
- les contraintes techniques pour la migration.

---

# 1. CMS utilisé

Le site est construit avec :

Joomla! – Open Source Content Management System.

La version exacte n'est pas exposée dans le code public mais la structure du site indique une version Joomla moderne compatible avec les extensions actuelles.

---

# 2. Page builder utilisé

Le site utilise l'extension :

Balbooa Gridbox  
version : 2.20.0.2

Gridbox est un page builder visuel permettant de construire les pages via un système de sections et blocs.

Les pages sont composées de :

- sections
- colonnes
- blocs de contenu
- modales
- éléments dynamiques.

---

# 3. Extensions détectées

Extensions principales observées :

com_gridbox  
com_content  
com_contact

Gridbox est utilisé pour la majorité des pages du site.

---

# 4. Types de contenus utilisés

Le contenu du site est structuré principalement via Gridbox.

Exemples :

Formations  
pages Gridbox avec blocs de contenu.

Modules de cours  
contenus affichés via fenêtres modales.

FAQ  
accordéon Gridbox.

Annuaire des thérapeutes  
module Gridbox de type blog posts.

Formateurs  
contenu Gridbox.

Le site utilise donc très peu les articles Joomla classiques.

---

# 5. Structure probable de la base de données

Tables Joomla standard :

#__content  
#__categories  
#__menu  
#__modules  
#__extensions  

Tables Gridbox :

#__gridbox_pages  
#__gridbox_items  

Les pages Gridbox stockent souvent les layouts sous forme de données JSON.

---

# 6. Hébergement

Registrar :

Diogenius SPRL

Serveurs DNS :

NS1.BEHOSTINGS.NET  
NS2.BEHOSTINGS.NET

Adresse IP :

193.105.73.253

Localisation serveur :

Belgique.

Le site semble hébergé sur un serveur mutualisé.

---

# 7. Performances actuelles

Analyse PageSpeed :

Mobile

Performance : 71  
Accessibility : 81  
Best practices : 96  
SEO : 92  

First Contentful Paint : 3.3 s  
Largest Contentful Paint : 5.3 s  

Desktop

Performance : 81  

First Contentful Paint : 0.8 s  
Largest Contentful Paint : 1.7 s  

Les performances desktop sont satisfaisantes mais les performances mobile peuvent être améliorées.

---

# 8. Contraintes techniques pour la migration

Plusieurs contraintes sont identifiées.

Utilisation intensive de Gridbox

Le contenu est structuré via un builder visuel et stocké sous forme de layouts.

Cela peut compliquer l'extraction automatique du contenu.

Modules affichés en modales

Certains contenus importants (modules de formation) sont affichés dans des fenêtres modales sans URL propre.

Ces contenus devront être restructurés lors de la migration.

Contenu dynamique Gridbox

Certaines sections utilisent des modules Gridbox spécifiques (blog posts, accordéons).

Ces structures devront être transformées dans le nouveau CMS.

---

# 9. Opportunités techniques

La structure du site reste relativement simple.

Le nombre de pages est limité et l'architecture globale est claire.

Cela rend une migration vers un CMS plus moderne tout à fait réalisable.

Une refonte permettra également :

- d'améliorer le SEO
- d'améliorer les performances mobiles
- de restructurer les contenus pédagogiques.

---

# Conclusion

Le site IHMN repose sur Joomla et l'extension Gridbox.

L'utilisation intensive de Gridbox constitue la principale contrainte technique pour la migration car une partie du contenu est stockée dans des layouts propriétaires.

Cependant la taille du site et la clarté de sa structure rendent une migration techniquement réalisable.