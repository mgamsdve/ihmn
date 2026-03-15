import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import csv

start_url = "https://ihmn.be"
domain = "ihmn.be"

visited = set()
queue = [start_url]

outgoing = {}
incoming = {}

while queue:
    url = queue.pop(0)

    if url in visited:
        continue

    visited.add(url)

    try:
        r = requests.get(url, timeout=10)
    except:
        continue

    soup = BeautifulSoup(r.text, "html.parser")

    links = []

    for a in soup.find_all("a", href=True):

        link = urljoin(url, a["href"])

        if domain in urlparse(link).netloc:

            links.append(link)

            if link not in visited:
                queue.append(link)

            incoming.setdefault(link, []).append(url)

    outgoing[url] = links


data = []

for url in outgoing:

    data.append({
        "URL": url,
        "Outgoing links": len(outgoing[url]),
        "Incoming links": len(incoming.get(url, []))
    })

with open("internal_linking.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("Crawl terminé :", len(data))