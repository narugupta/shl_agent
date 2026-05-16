from fastapi.testclient import (
    TestClient
)

from app.main import app


client = TestClient(app)


def test_refinement():

    payload = {
        "messages": [
            {
                "role": "user",
                "content": (
                    "Hiring a Java developer"
                )
            },
            {
                "role": "assistant",
                "content": (
                    "What seniority level?"
                )
            },
            {
                "role": "user",
                "content": (
                    "Mid-level. Add "
                    "personality tests too."
                )
            }
        ]
    }

    response = client.post(
        "/chat",
        json=payload
    )

    assert response.status_code == 200