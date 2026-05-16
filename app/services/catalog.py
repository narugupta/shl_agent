import json
from pathlib import Path


CATALOG_PATH = Path("app/data/catalog.json")


def load_catalog():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)