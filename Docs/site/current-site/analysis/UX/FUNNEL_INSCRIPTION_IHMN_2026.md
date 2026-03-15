# Issue 3.1 — Analyse du parcours utilisateur d'inscription

## Contexte

Dans le cadre du projet de refonte du site https://ihmn.be, cette analyse vise à comprendre le parcours d’un utilisateur souhaitant s’inscrire à une formation.

L’objectif est d’identifier :

- les étapes du parcours utilisateur
- les pages impliquées dans le funnel d’inscription
- les points de friction dans l’expérience utilisateur
- les informations manquantes ou difficiles à trouver
- les éléments influençant la décision d’inscription

Cette analyse servira de base pour améliorer l’expérience utilisateur dans la future architecture du site.

---

# Méthodologie d’analyse

L’analyse repose sur :

- l’inventaire complet des pages du site
- l’observation manuelle du parcours utilisateur
- l’analyse de la navigation et du maillage interne
- l’évaluation heuristique de l’expérience utilisateur

Les étapes étudiées correspondent au parcours classique d’un futur étudiant :
Découverte → Information → Décision → Inscription

---

# Personas principaux

Les profils utilisateurs principaux identifiés sont les suivants.

## Futur étudiant en reconversion

Profil :

- adulte en reconversion professionnelle
- recherche une formation complète en naturopathie
- souhaite exercer comme thérapeute

Besoins :

- comprendre la formation
- connaître les débouchés
- évaluer le coût et la durée de la formation

---

## Professionnel souhaitant compléter son activité

Profil :

- professionnel du secteur santé/bien-être
- souhaite compléter ses compétences

Exemples :

- kinésithérapeutes
- infirmiers
- coachs sportifs
- thérapeutes

Besoins :

- identifier les modules pertinents
- comprendre la compatibilité avec leur activité actuelle

---

## Personne curieuse de la naturopathie

Profil :

- intérêt personnel pour la santé naturelle
- souhaite se former sans nécessairement exercer

Besoins :

- comprendre les contenus
- vérifier l’accessibilité des formations
- évaluer l’investissement nécessaire

---

# Parcours utilisateur actuel

Le parcours d’un utilisateur souhaitant s’inscrire suit généralement les étapes suivantes.

## Étape 1 — Découverte

Pages d'entrée possibles :

- Accueil
- Formations

L’utilisateur découvre les différentes formations disponibles :

- naturopathie
- hygiène de vie et nutrition
- drainage lymphatique manuel
- formations hors cursus
---

## Étape 3 — Consultation d’une formation

Exemple :
Formations → Naturopathie
La page présente :

- les années de formation
- les modules
- les contenus pédagogiques.

Les informations détaillées des modules sont accessibles via des **fenêtres modales (popups)**.

---

## Étape 4 — Recherche d’informations administratives

Pour connaître les modalités d’inscription et les tarifs, l’utilisateur doit accéder à la page :
Formations → Inscriptions & tarifs
Cette page est principalement accessible via le menu de navigation.

---

## Étape 5 — Contact

Pour s’inscrire, l’utilisateur doit :

- contacter l’école par mail
- téléphoner
- ou utiliser le formulaire de contact.

---

## Étape 6 — Inscription réelle

L’inscription se fait hors du site :

1. télécharger le contrat d’inscription PDF
2. compléter le document
3. l’envoyer par mail ou par poste
4. verser un acompte pour valider l’inscription.

---

# Cartographie du parcours utilisateur

User Journey Map simplifiée :
```
Découverte
│
├── Accueil
│
▼
Exploration
│
├── Formations
│
▼
Information
│
├── Formation spécifique
│
▼
Décision
│
├── Inscriptions & tarifs
│
▼
Contact
│
├── Contact
│   ├── Formulaire
│   ├── Téléphone
│   └── Email
│
▼
Inscription
│
└── Téléchargement du contrat PDF
```

---

# Nombre de clics nécessaires

Parcours minimal :
Accueil
→ Formation
→ Inscriptions & tarifs
→ Contact

Nombre minimal de clics :

**3 clics**

Cependant ce parcours dépend fortement de l’utilisation du menu principal.

---

# Analyse UX du funnel

## Points positifs

### Structure du site simple

La structure du site reste claire :

- peu d’items de navigation
- hiérarchie compréhensible.

---

### Présentation détaillée des formations

Les pages formations contiennent :

- une description complète des modules
- un programme détaillé.

---

### Présence d’éléments de confiance

Le site présente :

- plus de 40 ans d’expérience
- reconnaissance par des associations professionnelles
- témoignages d’élèves
- annuaire des thérapeutes.

Ces éléments renforcent la crédibilité de l’institution.

---

# Friction points identifiés

## Absence de CTA d’inscription

Les pages formations ne contiennent pas :

- bouton "S’inscrire"
- bouton "Demander des informations"
- lien direct vers les inscriptions.

Conséquence :

l’utilisateur doit revenir au menu pour poursuivre son parcours.

---

## Dépendance au menu principal

La page "Inscriptions & tarifs" est accessible principalement via le menu.

Cela crée une rupture dans la navigation.

---

## Informations pédagogiques difficiles à parcourir

Les modules sont présentés sous forme :

- de longues listes
- avec des informations détaillées dans des popups.

Conséquences :

- navigation fragmentée
- difficulté à parcourir rapidement le programme.

---

## Informations tarifaires peu lisibles

Les tarifs sont :

- partiellement indiqués sur la page
- détaillés dans un PDF externe.

Conséquence :

l’utilisateur doit télécharger un document pour comprendre le coût réel.

---

## Conversion hors site

L’inscription ne peut pas être réalisée directement sur le site.

Le processus repose sur :

- téléchargement d’un contrat
- envoi manuel
- paiement par virement.

Cela introduit une friction importante dans le funnel.

---

# Informations manquantes pouvant bloquer l’inscription

Certaines informations importantes pour la décision d’inscription ne sont pas immédiatement visibles :

- coût total estimé de la formation
- organisation détaillée des cours
- débouchés professionnels concrets
- processus d’inscription simplifié.

---

# Analyse de la confiance

Le site comporte plusieurs éléments renforçant la confiance :

- ancienneté de l’école
- reconnaissance par des associations professionnelles
- témoignages d’élèves
- annuaire de thérapeutes formés.

Cependant ces éléments pourraient être davantage mis en valeur dans le parcours d’inscription.

---

# Recommandations UX

Plusieurs améliorations sont recommandées.

## Ajouter des CTA sur les pages formations

Exemple :
S’inscrire
Demander des informations
Télécharger la brochure

---

## Relier les pages formations aux inscriptions

Ajouter des liens directs vers :
/formations/inscriptions-tarifs

---

## Améliorer la lisibilité des tarifs

Afficher clairement :

- le coût par année
- le coût total estimé.

---

## Simplifier le processus d’inscription

Créer :

- un formulaire d’inscription
- ou une pré-inscription en ligne.

---

## Structurer les programmes de formation

Créer des pages distinctes pour :

- chaque année
- chaque module.

---

# Conclusion

Le parcours utilisateur actuel permet d’accéder aux informations nécessaires pour s’inscrire, mais il présente plusieurs points de friction.

Les principales limites identifiées sont :

- absence de CTA
- dépendance au menu de navigation
- informations pédagogiques fragmentées
- tarifs peu lisibles
- inscription réalisée hors du site.

Une refonte de l’architecture et du parcours d’inscription permettra d’améliorer significativement l’expérience utilisateur et de faciliter la conversion des visiteurs en futurs étudiants.

| Étape       | Page         | Friction              |
| ----------- | ------------ | --------------------- |
| Découverte  | Accueil      | Pas de CTA            |
| Information | Formation    | Modules en popup      |
| Décision    | Inscriptions | Tarifs peu lisibles   |
| Action      | Contact      | Inscription hors site |
