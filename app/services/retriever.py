import faiss
import numpy as np

from rapidfuzz import fuzz
from sentence_transformers import (
    SentenceTransformer
)

from app.services.catalog import load_catalog


catalog = load_catalog()

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
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


def hybrid_retrieve(query, top_k=15):

    semantic_results = semantic_search(
        query,
        top_k=25
    )

    scored = []

    for item in semantic_results:

        searchable = f"""
        {item['name']}
        {item['description']}
        """

        keyword_score = fuzz.partial_ratio(
            query.lower(),
            searchable.lower()
        )

        final_score = keyword_score

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