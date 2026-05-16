import json

with open(
    "app/data/catalog.json",
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)

for item in data:

    if "test_type" not in item:

        print(item["name"])