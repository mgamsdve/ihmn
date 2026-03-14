import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

BASE = "https://ihmn.be"

visited = set()
to_visit = {BASE}

pdfs = set()

while to_visit:
    url = to_visit.pop()

    if url in visited:
        continue

    visited.add(url)

    try:
        r = requests.get(url, timeout=10)
    except:
        continue

    if "text/html" not in r.headers.get("Content-Type", ""):
        continue

    soup = BeautifulSoup(r.text, "html.parser")

    for a in soup.find_all("a", href=True):

        link = urljoin(url, a["href"])

        if link.endswith(".pdf"):
            pdfs.add(link)

        if urlparse(link).netloc == "ihmn.be":
            if link not in visited:
                to_visit.add(link)

print("\nPDFs trouvés :\n")

for p in sorted(pdfs):
    print(p)

print("\nTOTAL:", len(pdfs))