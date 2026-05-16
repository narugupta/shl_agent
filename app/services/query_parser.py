import re

from app.services.role_mapper import (
    infer_role_skills
)


def parse_query(text):

    text = text.lower()

    parsed = {
        "skills": [],
        "seniority": None,
        "personality": False,
        "cognitive": False,
        "leadership": False,
        "simulation": False,
        "language": None,
        "max_duration": None
    }

    inferred_skills = infer_role_skills(
        text
    )

    parsed["skills"].extend(
        inferred_skills
    )

    explicit_skills = [
        "java",
        "python",
        "aws",
        "docker",
        "sql",
        "angular",
        "spring",
        "communication",
        "stakeholder",
        "analytics",
        "sales",
        "leadership"
    ]

    for skill in explicit_skills:

        if skill in text:
            parsed["skills"].append(skill)

    levels = [
        "junior",
        "mid",
        "senior",
        "lead",
        "manager"
    ]

    for level in levels:

        if level in text:
            parsed["seniority"] = level

    if (
        "personality" in text or
        "culture fit" in text
    ):
        parsed["personality"] = True

    if (
        "cognitive" in text or
        "aptitude" in text or
        "reasoning" in text
    ):
        parsed["cognitive"] = True

    if (
        "leadership" in text or
        "stakeholder" in text
    ):
        parsed["leadership"] = True

    if "simulation" in text:
        parsed["simulation"] = True

    if "spanish" in text:
        parsed["language"] = "spanish"

    if "english" in text:
        parsed["language"] = "english"

    duration_match = re.search(
        r"(\d+)\s*minutes",
        text
    )

    if duration_match:

        parsed["max_duration"] = int(
            duration_match.group(1)
        )

    parsed["skills"] = list(
        set(parsed["skills"])
    )

    return parsed