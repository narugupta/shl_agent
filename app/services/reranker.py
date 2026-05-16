def rerank(results, parsed):

    scored = []

    for item in results:

        score = 0

        text = (
            item["name"] +
            " " +
            item["description"]
        ).lower()

        for skill in parsed["skills"]:

            if skill in text:
                score += 4

        if (
            parsed["personality"] and
            "personality" in text
        ):
            score += 6

        if (
            parsed["cognitive"] and
            "cognitive" in text
        ):
            score += 6

        if (
            parsed["leadership"] and
            "leadership" in text
        ):
            score += 5

        scored.append((score, item))

    scored.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        item
        for _, item in scored
    ]