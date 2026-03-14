import requests
from bs4 import BeautifulSoup
from collections import Counter

BASE_URL = "https://ihmn.be"

therapeutes = []

# ---------------------------
# SCRAPER THERAPEUTES
# ---------------------------

for page in range(1,5):

    url = f"{BASE_URL}/nos-therapeuthes?page={page}"

    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    posts = soup.find_all("div", class_="ba-blog-post")

    for post in posts:

        fiche = {}

        container = post.find("div", class_="ba-blog-post-field-value")

        if not container:
            continue

        # NOM
        name = container.find("h3")
        if name:
            fiche["nom"] = name.text.strip()

        # TELEPHONE
        tel = container.find("a", href=lambda x: x and x.startswith("tel"))
        if tel:
            fiche["telephone"] = tel.text.strip()

        # EMAIL
        mail = container.find("a", href=lambda x: x and x.startswith("mailto"))
        if mail:
            fiche["email"] = mail.text.replace("mailto:", "").strip()

        # SITE
        site = container.find("a", href=lambda x: x and "http" in x)
        if site:
            fiche["site"] = site.text.strip()

        # ADRESSE
        addr = container.find("strong")
        if addr:
            fiche["adresse"] = addr.text.strip()

        therapeutes.append(fiche)


# ---------------------------
# SCRAPER FORMATEURS
# ---------------------------

formateurs = []

url = f"{BASE_URL}/ihmn/formateurs"

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

sections = soup.find_all("div", class_="ba-overlay-section-backdrop")

for section in sections:

    name = section.find("h6")

    if not name:
        continue

    formateur = {}
    formateur["nom"] = name.text.strip()

    text = section.find_all("p")

    desc = []

    for p in text:
        t = p.text.strip()
        if t:
            desc.append(t)

    formateur["description"] = " ".join(desc)

    formateurs.append(formateur)


# ---------------------------
# ANALYSE DOUBLONS
# ---------------------------

names = [t["nom"] for t in therapeutes if "nom" in t]

duplicates = [n for n,c in Counter(names).items() if c>1]


# ---------------------------
# GENERATION MARKDOWN
# ---------------------------

with open("annuaire-ihmn-inventaire.md","w") as f:

    f.write("# Inventaire Annuaire IHMN\n\n")

    f.write("## Nombre total de thérapeutes\n\n")
    f.write(f"{len(therapeutes)} thérapeutes recensés.\n\n")

    f.write("## Tableau des thérapeutes\n\n")

    f.write("| Nom | Téléphone | Email | Site | Adresse |\n")
    f.write("|-----|-----------|-------|------|---------|\n")

    for t in therapeutes:

        f.write(
            f"| {t.get('nom','')} | "
            f"{t.get('telephone','')} | "
            f"{t.get('email','')} | "
            f"{t.get('site','')} | "
            f"{t.get('adresse','')} |\n"
        )

    f.write("\n\n")

    f.write("## Doublons détectés\n\n")

    if duplicates:
        for d in duplicates:
            f.write(f"- {d}\n")
    else:
        f.write("Aucun doublon détecté\n")

    f.write("\n\n")

    f.write("## Formateurs IHMN\n\n")

    f.write("| Nom | Description |\n")
    f.write("|-----|-------------|\n")

    for form in formateurs:

        f.write(
            f"| {form.get('nom','')} | "
            f"{form.get('description','')} |\n"
        )


    f.write("\n\n")

    f.write("## Analyse\n\n")

    f.write("### Pagination\n")
    f.write("L'annuaire est réparti sur 4 pages.\n\n")

    f.write("### Structure des fiches thérapeutes\n")
    f.write("Champs identifiés : nom, téléphone, email, site web, adresse.\n\n")

    f.write("### Carte interactive\n")
    f.write("Une carte interactive affiche la localisation des thérapeutes via des marqueurs géographiques.\n\n")

print("Fichier généré : annuaire-ihmn-inventaire.md")