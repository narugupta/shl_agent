from fastapi.testclient import (
    TestClient
)

from app.main import app


client = TestClient(app)


def test_compare():

    payload = {
        "messages": [
            {
                "role": "user",
                "content": (
                    "Compare OPQ and GSA"
                )
            }
        ]
    }

    response = client.post(
        "/chat",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "reply" in data