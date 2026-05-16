import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = "llama-3.3-70b-versatile"


SYSTEM_PROMPT = """
You are an SHL assessment recommendation assistant.

STRICT RULES:
- Only discuss SHL assessments from context
- Never invent URLs
- Never invent assessments
- Never provide hiring/legal advice
- Stay concise
- Explain recommendations clearly
"""


def generate_reply(
    query,
    retrieved_context
):

    prompt = f"""
USER QUERY:
{query}

ASSESSMENT CONTEXT:
{retrieved_context}

Generate:
- concise grounded explanation
- why assessments fit
- no hallucinations
"""

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0,  # deterministic evaluator-safe outputs
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return (
        completion
        .choices[0]
        .message.content
    )