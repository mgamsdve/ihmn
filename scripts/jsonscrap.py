import requests
from bs4 import BeautifulSoup

url = "https://ihmn.be/formations/naturopathie"

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

modules = []

for h in soup.find_all("h6"):

    title = h.get_text(strip=True)

    if title in {"Matière abordée", "Objectif", "Méthodologie"}:
        continue

    # bloc du module
    block = h.find_parent("div")

    popup = block.find_next("div", class_="ba-item-overlay-section")

    module = {
        "module": title,
        "duree": "",
        "formateur": "",
        "matiere": "",
        "objectif": "",
        "methodologie": ""
    }

    if popup:

        text = popup.get_text("\n", strip=True)
        lines = [l.strip() for l in text.split("\n") if l.strip()]

        for i, line in enumerate(lines):

            if "Durée" in line:
                module["duree"] = line

            if "Format" in line:
                module["formateur"] = line

            if line == "Matière abordée" and i + 1 < len(lines):
                module["matiere"] = lines[i+1]

            if line == "Objectif" and i + 1 < len(lines):
                module["objectif"] = lines[i+1]

            if line == "Méthodologie" and i + 1 < len(lines):
                module["methodologie"] = lines[i+1]

    modules.append(module)

for m in modules:
    print("\nMODULE:", m["module"])
    print("Durée:", m["duree"])
    print("Formateur:", m["formateur"])
    print("Matière:", m["matiere"][:120])
    print("Objectif:", m["objectif"][:120])
    print("Méthodologie:", m["methodologie"][:120])