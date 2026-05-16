import json
import requests


BASE_URL = "http://127.0.0.1:8000"


with open(
    "tests/conversations.json",
    "r",
    encoding="utf-8"
) as f:

    conversations = json.load(f)


for convo in conversations:

    response = requests.post(
        f"{BASE_URL}/chat",
        json={
            "messages": convo["messages"]
        }
    )

    print("\nQUERY:")
    print(convo["messages"][-1]["content"])

    print("\nRESPONSE:")
    print(response.json())