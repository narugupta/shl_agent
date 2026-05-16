ROLE_MAPPINGS = {
    "java developer": [
        "java",
        "backend",
        "software"
    ],

    "sales manager": [
        "sales",
        "negotiation",
        "leadership"
    ],

    "customer support": [
        "communication",
        "service",
        "support"
    ],

    "data analyst": [
        "analytics",
        "reasoning",
        "numerical"
    ],

    "leadership": [
        "leadership",
        "management"
    ]
}


def infer_role_skills(text):

    text = text.lower()

    matched_skills = []

    for role, skills in ROLE_MAPPINGS.items():

        if role in text:
            matched_skills.extend(skills)

    return list(set(matched_skills))