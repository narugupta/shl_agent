import requests


BASE_URL = "http://127.0.0.1:8000"


conversation = [
    {
        "role": "user",
        "content": (
            "Hiring a mid-level "
            "Java developer who "
            "works with stakeholders"
        )
    }
]


response = requests.post(
    f"{BASE_URL}/chat",
    json={"messages": conversation}
)

print(response.json())