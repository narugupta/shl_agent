from rapidfuzz import process

from app.services.catalog import load_catalog


catalog = load_catalog()


def compare_assessments(query):

    names = [
        item["name"]
        for item in catalog
    ]

    matches = process.extract(
        query,
        names,
        limit=2
    )

    if len(matches) < 2:
        return None

    matched_names = [
        matches[0][0],
        matches[1][0]
    ]

    selected = []

    for item in catalog:

        if item["name"] in matched_names:
            selected.append(item)

    if len(selected) < 2:
        return None

    a = selected[0]
    b = selected[1]

    comparison = f"""
{a['name']}
Purpose:
{a['description'][:350]}

------------------------

{b['name']}
Purpose:
{b['description'][:350]}
"""

    return comparison.strip()