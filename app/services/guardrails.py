OFFTOPIC_KEYWORDS = [

    "tax",
    "taxes",
    "crypto",
    "bitcoin",
    "medical",
    "doctor",
    "hospital",
    "lawsuit",
    "legal advice",
    "politics",
    "election",
    "dating",
    "relationship",
    "recipe",
    "travel",
    "hotel",
    "movie",
    "football"
]


PROMPT_INJECTION_PATTERNS = [

    "ignore previous instructions",
    "ignore all instructions",
    "system prompt",
    "reveal prompt",
    "bypass restrictions",
    "act as"
]


def is_offtopic(text):

    text = text.lower()

    # Explicit hiring/assessment context
    allowed_signals = [

        "hiring",
        "assessment",
        "candidate",
        "role",
        "developer",
        "manager",
        "engineer",
        "employee",
        "screening",
        "recruitment",
        "test"
    ]

    if any(
        signal in text
        for signal in allowed_signals
    ):
        return False

    return any(
        keyword in text
        for keyword in OFFTOPIC_KEYWORDS
    )


def is_prompt_injection(text):

    text = text.lower()

    return any(
        pattern in text
        for pattern in PROMPT_INJECTION_PATTERNS
    )