import json
import time
import requests

from bs4 import BeautifulSoup


BASE_URL = "https://www.shl.com"

CATALOG_URL = (
    "https://www.shl.com/solutions/products/product-catalog/"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0"
    )
}


def get_soup(url):
    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    response.raise_for_status()

    return BeautifulSoup(response.text, "html.parser")


print("Loading catalog page...")

soup = get_soup(CATALOG_URL)

links = soup.find_all("a", href=True)

product_urls = set()


for link in links:
    href = link["href"]

    # Product detail pages
    if "/products/" in href:

        if href.startswith("/"):
            href = BASE_URL + href

        product_urls.add(href)


print(f"Found {len(product_urls)} product URLs")


results = []


for idx, url in enumerate(product_urls):

    try:
        print(f"[{idx+1}/{len(product_urls)}] Scraping {url}")

        psoup = get_soup(url)

        title_tag = psoup.find("h1")

        if not title_tag:
            continue

        title = title_tag.get_text(strip=True)

        paragraphs = psoup.find_all("p")

        description = " ".join(
            p.get_text(" ", strip=True)
            for p in paragraphs
        )

        description = description[:3000]

        results.append({
            "name": title,
            "url": url,
            "description": description,
            "test_type": "Unknown"
        })

        time.sleep(0.5)

    except Exception as e:
        print("ERROR:", e)


print(f"\nCollected {len(results)} assessments")


with open(
    "app/data/catalog.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(results, f, indent=2)


print("Saved catalog.json")