import requests
from bs4 import BeautifulSoup

url = "https://ihmn.be/faq"

html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

faq = []

categories = soup.select(".accordion > .accordion-group")

for cat in categories:

    cat_title = cat.select_one(".accordion-title")
    if not cat_title:
        continue

    category = cat_title.get_text(strip=True)

    sub_questions = cat.select(".accordion-inner .accordion-group")

    for q in sub_questions:

        q_title = q.select_one(".accordion-title")
        q_body = q.select_one(".accordion-inner")

        if not q_title or not q_body:
            continue

        question = q_title.get_text(strip=True)
        answer = q_body.get_text(separator="\n", strip=True)

        faq.append((category, question, answer))

# écrire markdown
with open("faq-inventaire.md", "w") as f:

    f.write("# Inventaire FAQ IHMN\n\n")

    current_cat = None

    for category, question, answer in faq:

        if category != current_cat:
            f.write(f"\n## {category}\n\n")
            current_cat = category

        f.write(f"### {question}\n\n")
        f.write(answer + "\n\n")

print("FAQ exportée dans faq-inventaire.md")