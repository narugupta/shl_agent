import re
from typing import Dict

from app.utils.constants import (
    PERSONALITY_KEYWORDS,
    TECH_KEYWORDS
)


SENIORITY_KEYWORDS = [
    "junior",
    "mid",
    "senior",
    "lead",
    "manager"
]


ROLE_PATTERNS = [
    r"hiring\s+(?:a|an)?\s*([a-zA-Z\s\-]+)",
    r"looking for\s+(?:a|an)?\s*([a-zA-Z\s\-]+)",
    r"need\s+(?:a|an)?\s*([a-zA-Z\s\-]+)"
]


def extract_role(text):

    text = text.lower()

    for pattern in ROLE_PATTERNS:

        match = re.search(pattern, text)

        if match:

            role = match.group(1).strip()

            # Remove trailing phrases
            role = role.split("with")[0]
            role = role.split("who")[0]
            role = role.split("for")[0]

            return role.strip()

    return None


def build_state(messages) -> Dict:

    text = " ".join([
        m.content.lower()
        for m in messages
    ])

    state = {
        "role": None,
        "seniority": None,
        "personality": False,
        "technical": False,
        "compare_mode": False,
        "compare_targets": [],
        "query": text
    }

    # Generic role extraction
    extracted_role = extract_role(text)

    if extracted_role:
        state["role"] = extracted_role

    # Seniority detection
    for level in SENIORITY_KEYWORDS:

        if level in text:
            state["seniority"] = level

    # Technical detection
    if any(k in text for k in TECH_KEYWORDS):
        state["technical"] = True

    # Personality detection
    if any(k in text for k in PERSONALITY_KEYWORDS):
        state["personality"] = True

    # Compare flow detection
    if (
        "compare" in text or
        "difference" in text or
        " vs " in text or
        " versus " in text
    ):
        state["compare_mode"] = True

    return state


def enough_information(state):

    score = 0

    if state["role"]:
        score += 1

    if state["seniority"]:
        score += 1

    # Allow recommendation if strong signal exists
    if (
        state["technical"] or
        state["personality"]
    ):
        score += 1

    return score >= 2