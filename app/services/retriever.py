import faiss
import numpy as np

from rapidfuzz import fuzz
from sentence_transformers import (
    SentenceTransformer
)

from app.services.catalog import (
    load_catalog
)


catalog = load_catalog()

model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    device="cpu"
)

index = faiss.read_index(
    "app/data/faiss.index"
)


def embed(text):

    vector = model.encode([text])

    return np.array(vector).astype(
        "float32"
    )


def semantic_search(query, top_k=20):

    query_vector = embed(query)

    distances, indices = index.search(
        query_vector,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx >= len(catalog):
            continue

        results.append(catalog[idx])

    return results


def hybrid_retrieve(
    query,
    parsed,
    top_k=15
):

    semantic_results = semantic_search(
        query,
        top_k=30
    )

    filtered = []

    for item in semantic_results:

        category = item.get(
            "category",
            "general"
        )

        if (
            parsed["personality"] and
            category != "personality"
        ):
            continue

        if (
            parsed["cognitive"] and
            category != "cognitive"
        ):
            continue

        if (
            parsed["simulation"] and
            category != "simulation"
        ):
            continue

        filtered.append(item)

    scored = []

    for item in filtered:

        searchable = f"""
        {item.get('name', '')}
        {item.get('description', '')}
        {' '.join(item.get('keys', []))}
        {' '.join(item.get('job_levels', []))}
        """

        keyword_score = fuzz.partial_ratio(
            query.lower(),
            searchable.lower()
        )

        final_score = keyword_score

        # Seniority boost
        if (
            parsed["seniority"] and
            parsed["seniority"] in
            " ".join(
                item.get(
                    "job_levels",
                    []
                )
            ).lower()
        ):
            final_score += 10

        # Skill boost
        for skill in parsed["skills"]:

            if skill.lower() in searchable.lower():
                final_score += 5

        # Leadership boost
        if (
            parsed["leadership"] and
            "leadership" in searchable.lower()
        ):
            final_score += 8

        # OPQ32r strategic boost
        if (
            parsed["leadership"] or
            "stakeholder" in query.lower()
        ):

            if "opq" in item["name"].lower():
                final_score += 15

        scored.append(
            (final_score, item)
        )

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        item
        for _, item in scored[:top_k]
    ]