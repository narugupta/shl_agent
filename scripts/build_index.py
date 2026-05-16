import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


with open("app/data/catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)


documents = []

for item in catalog:
    text = f"""
    {item['name']}
    {item['description']}
    {item['test_type']}
    """

    documents.append(text)


if not documents:
    raise ValueError(
        "No documents found. Check catalog.json"
    )

vectors = model.encode(documents)

vectors = np.array(vectors).astype("float32")

dimension = vectors.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(vectors)

faiss.write_index(index, "app/data/faiss.index")

print("FAISS index built")