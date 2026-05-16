UNSUPPORTED_SKILLS = {

    "rust": (
        "SHL does not currently offer "
        "a dedicated Rust assessment, "
        "but related backend and "
        "programming assessments "
        "can still help evaluate "
        "candidates."
    )
}


def detect_constraints(query):

    query = query.lower()

    messages = []

    for skill, message in (
        UNSUPPORTED_SKILLS.items()
    ):

        if skill in query:
            messages.append(message)

    return messages