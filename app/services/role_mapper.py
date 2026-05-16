ROLE_MAPPINGS = {

    "java developer": [
        "java",
        "backend",
        "software",
        "programming"
    ],

    "python developer": [
        "python",
        "backend",
        "automation",
        "coding"
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

    "finance analyst": [
        "finance",
        "analytics",
        "numerical reasoning"
    ],

    "project manager": [
        "leadership",
        "stakeholder management",
        "planning"
    ],

    "business analyst": [
        "analytics",
        "communication",
        "stakeholder"
    ],

    "hr specialist": [
        "personality",
        "communication",
        "culture fit"
    ],

    "graduate trainee": [
        "aptitude",
        "learning ability"
    ]
}


def infer_role_skills(text):

    text = text.lower()

    matched_skills = []

    for role, skills in ROLE_MAPPINGS.items():

        if role in text:
            matched_skills.extend(skills)

    return list(set(matched_skills))