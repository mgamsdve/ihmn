from pdfminer.high_level import extract_text
import requests
import os

pdf_urls = [
    "https://ihmn.be/images/Documents/ihmn_25-26_contrat_inscription_1e-anne.pdf",
    "https://ihmn.be/images/Documents/ihmn---tarifs-2025-26.pdf",
    "https://ihmn.be/images/Documents/IHMN%20-%20Bourse%202025-26.pdf",
    "https://ihmn.be/images/Documents/ihmn_mentions_legales_230601.pdf"
]

for url in pdf_urls:

    filename = url.split("/")[-1]

    print("\n===================")
    print("PDF:", filename)

    r = requests.get(url)

    with open(filename, "wb") as f:
        f.write(r.content)

    text = extract_text(filename)

    print(text[:1000])