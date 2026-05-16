def get_clarification(state, query):

    query = query.lower()

    # Contact center / support
    if (
        "contact center" in query or
        "customer support" in query
    ):

        if (
            "english" not in query and
            "spanish" not in query
        ):

            return (
                "What language will "
                "customers primarily speak?"
            )

    # Full stack ambiguity
    if "full stack" in query:

        return (
            "Is this backend-heavy, "
            "frontend-heavy, or balanced "
            "full-stack work?"
        )

    # Leadership ambiguity
    if (
        "leadership" in query and
        not state["seniority"]
    ):

        return (
            "What seniority level "
            "is this leadership role?"
        )

    # Generic clarification
    if not state["role"]:

        return (
            "What role are you hiring for?"
        )

    if not state["seniority"]:

        return (
            "What seniority level "
            "is the role?"
        )

    return None