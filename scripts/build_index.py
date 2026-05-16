import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


# CPU mode keeps Render lightweight
model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    device="cpu"
)


with open(
    "app/data/catalog.json",
    "r",
    encoding="utf-8"
) as f:

    catalog = json.load(f)


documents = []


for item in catalog:

    keys = " ".join(
        item.get("keys", [])
    )

    job_levels = " ".join(
        item.get("job_levels", [])
    )

    duration = str(
        item.get("duration", "")
    )

    remote = str(
        item.get("remote", "")
    )

    adaptive = str(
        item.get("adaptive", "")
    )

    # Category inference improves retrieval filtering
    category = "general"

    lower_keys = keys.lower()

    if "personality" in lower_keys:
        category = "personality"

    elif "simulation" in lower_keys:
        category = "simulation"

    elif (
        "knowledge" in lower_keys or
        "skills" in lower_keys
    ):
        category = "technical"

    elif "ability" in lower_keys:
        category = "cognitive"

    item["category"] = category

    retrieval_text = f"""
    Name:
    {item.get('name', '')}

    Description:
    {item.get('description', '')}

    Test Type:
    {item.get('test_type', '')}

    Categories:
    {keys}

    Job Levels:
    {job_levels}

    Duration:
    {duration}

    Remote Testing:
    {remote}

    Adaptive:
    {adaptive}

    Category:
    {category}
    """

    documents.append(
        retrieval_text
    )


if not documents:

    raise ValueError(
        "No documents found. Check catalog.json"
    )


vectors = model.encode(
    documents,
    show_progress_bar=True
)


vectors = np.array(
    vectors
).astype("float32")


dimension = vectors.shape[1]


index = faiss.IndexFlatL2(
    dimension
)


index.add(vectors)


faiss.write_index(
    index,
    "app/data/faiss.index"
)


# Save updated catalog with category field
with open(
    "app/data/catalog.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        catalog,
        f,
        indent=2
    )


print("FAISS index built successfully")