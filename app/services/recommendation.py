from app.utils.constants import (
    MAX_RECOMMENDATIONS
)


def build_recommendations(results):

    recommendations = []

    for item in results[:MAX_RECOMMENDATIONS]:

        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": item["test_type"]
        })

    return recommendations