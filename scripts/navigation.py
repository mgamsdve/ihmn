import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import csv

start_url = "https://ihmn.be/"
domain = "ihmn.be"

visited = set()
queue = [(start_url, 0)]

data = []

while queue:
    url, depth = queue.pop(0)

    if url in visited:
        continue

    visited.add(url)

    try:
        r = requests.get(url, timeout=10)
        status = r.status_code
        html = r.text
    except:
        continue

    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.text.strip() if soup.title else ""

    h1 = ""
    if soup.find("h1"):
        h1 = soup.find("h1").text.strip()

    meta_desc = ""
    meta = soup.find("meta", attrs={"name":"description"})
    if meta:
        meta_desc = meta.get("content","")

    links = []

    for a in soup.find_all("a", href=True):
        link = urljoin(url, a["href"])

        if domain in urlparse(link).netloc:
            links.append(link)

            if link not in visited:
                queue.append((link, depth + 1))

    data.append({
        "URL": url,
        "Depth": depth,
        "HTTP Code": status,
        "Title": title,
        "H1": h1,
        "Meta Description": meta_desc,
        "Outbound Links": len(links)
    })


with open("urls_ihmn.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("Crawl terminé :", len(data), "pages trouvées")