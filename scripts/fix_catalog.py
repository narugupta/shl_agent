import json


INPUT = "app/data/catalog.json"
OUTPUT = "app/data/catalog_clean.json"


with open(
    INPUT,
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)


clean = []

seen = set()


BLOCKED_WORDS = [

    "report",
    "guide",
    "cards",
    "profile",
    "framework",
    "development report",
    "narrative report",
    "candidate report",
    "manager report",
    "selection report",
    "profiler",
    "feedback system"
]


for item in data:

    name = item.get(
        "name",
        ""
    ).strip()

    if not name:
        continue

    lower_name = name.lower()

    # Remove non-assessment artifacts
    if any(
        word in lower_name
        for word in BLOCKED_WORDS
    ):
        continue

    # Deduplicate
    if lower_name in seen:
        continue

    seen.add(lower_name)

    url = item.get(
        "link",
        ""
    )

    if not url:
        continue

    # Normalize booleans
    remote = (
        str(
            item.get(
                "remote",
                ""
            )
        ).lower() == "yes"
    )

    adaptive = (
        str(
            item.get(
                "adaptive",
                ""
            )
        ).lower() == "yes"
    )

    keys = item.get(
        "keys",
        []
    )

    lower_keys = " ".join(
        keys
    ).lower()

    category = "general"

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

    retrieval_text = f"""
    {name}

    {item.get('description', '')}

    {' '.join(keys)}

    {' '.join(item.get('job_levels', []))}

    duration {item.get('duration', '')}

    remote {remote}

    adaptive {adaptive}

    {category}
    """

    clean.append({

        "name": name,

        "url": url,

        "description": item.get(
            "description",
            ""
        ),

        "test_type": (
            item.get(
                "test_type",
                "Unknown"
            )
        ),

        "duration": item.get(
            "duration",
            ""
        ),

        "remote": remote,

        "adaptive": adaptive,

        "job_levels": item.get(
            "job_levels",
            []
        ),

        "keys": keys,

        "category": category,

        "retrieval_text": retrieval_text
    })


with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        clean,
        f,
        indent=2,
        ensure_ascii=False
    )


print(
    f"Clean catalog size: {len(clean)}"
)