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

    for level in SENIORITY_KEYWORDS:
        if level in text:
            state["seniority"] = level

    if any(k in text for k in TECH_KEYWORDS):
        state["technical"] = True
        state["role"] = "software engineer"

    if any(k in text for k in PERSONALITY_KEYWORDS):
        state["personality"] = True

    # Compare mode detection
    if (
        "compare" in text or
        "difference" in text or
        " vs " in text
    ):
        state["compare_mode"] = True

    return state


def enough_information(state):

    score = 0

    if state["role"]:
        score += 1

    if state["seniority"]:
        score += 1

    return score >= 2