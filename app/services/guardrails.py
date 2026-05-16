from app.utils.constants import (
    OFFTOPIC_KEYWORDS,
    INJECTION_PATTERNS
)


def is_offtopic(text: str) -> bool:
    text = text.lower()

    return any(
        keyword in text
        for keyword in OFFTOPIC_KEYWORDS
    )


def is_prompt_injection(text: str) -> bool:
    text = text.lower()

    return any(
        pattern in text
        for pattern in INJECTION_PATTERNS
    )