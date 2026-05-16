from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "ok"
    }


def test_chat():

    payload = {
        "messages": [
            {
                "role": "user",
                "content": (
                    "Hiring a senior "
                    "Java developer"
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
    assert "recommendations" in data
    assert "end_of_conversation" in data