from app.utils.constants import (
    MAX_RECOMMENDATIONS
)


def build_recommendations(results):

    recommendations = []

    seen_categories = set()

    for item in results:

        category = item.get(
            "category",
            "general"
        )

        # Avoid repetitive recommendations
        if category in seen_categories:
            continue

        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": item.get("test_type", "Unknown")
        })

        seen_categories.add(category)

        if (
            len(recommendations)
            >= MAX_RECOMMENDATIONS
        ):
            break

    return recommendations