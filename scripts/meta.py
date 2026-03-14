import requests
from bs4 import BeautifulSoup

urls = [
    "https://ihmn.be/",
    "https://ihmn.be/ihmn",
    "https://ihmn.be/ihmn/lhistoire-ihmn",
    "https://ihmn.be/ihmn/en-pratique",
    "https://ihmn.be/ihmn/formateurs",
    "https://ihmn.be/contact",
    "https://ihmn.be/faq",
    "https://ihmn.be/mentions-legales"
]

for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    title = soup.title.string if soup.title else "N/A"

    meta = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta["content"] if meta else "None"

    h1 = soup.find("h1")
    h1_text = h1.text.strip() if h1 else "None"

    print(f"\nURL: {url}")
    print(f"Title: {title}")
    print(f"H1: {h1_text}")
    print(f"Meta description: {meta_desc}")