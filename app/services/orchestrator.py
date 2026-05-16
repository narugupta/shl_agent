from app.services.state import (
    build_state
)

from app.services.query_parser import (
    parse_query
)

from app.services.guardrails import (
    is_offtopic,
    is_prompt_injection
)

from app.services.compare import (
    compare_assessments
)

from app.services.retriever import (
    hybrid_retrieve
)

from app.services.reranker import (
    rerank
)

from app.services.recommendation import (
    build_recommendations
)

from app.services.llm import (
    generate_reply
)

from app.services.clarifier import (
    get_clarification
)

from app.services.constraints import (
    detect_constraints
)

from app.utils.logger import logger


def orchestrate(messages):

    latest_user_message = (
        messages[-1].content
    )

    logger.info(
        f"User query: {latest_user_message}"
    )

    if is_offtopic(
        latest_user_message
    ):

        return {
            "reply": (
                "I can only help with "
                "SHL assessment "
                "selection and comparison."
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    if is_prompt_injection(
        latest_user_message
    ):

        return {
            "reply": (
                "I can only recommend "
                "official SHL assessments."
            ),
            "recommendations": [],
            "end_of_conversation": False
        }

    state = build_state(messages)

    # Compare flow
    if state["compare_mode"]:

        comparison = compare_assessments(
            latest_user_message
        )

        if comparison:

            return {
                "reply": comparison,
                "recommendations": [],
                "end_of_conversation": False
            }

    clarification = get_clarification(
        state,
        state["query"]
    )

    if clarification:

        return {
            "reply": clarification,
            "recommendations": [],
            "end_of_conversation": False
        }

    parsed = parse_query(
        state["query"]
    )

    logger.info(parsed)

    retrieved = hybrid_retrieve(
        state["query"],
        parsed,
        top_k=20
    )

    reranked = rerank(
        retrieved,
        parsed
    )

    context = ""

    for item in reranked[:8]:

        context += f"""
NAME:
{item['name']}

DESCRIPTION:
{item['description'][:350]}

TYPE:
{item.get('test_type', 'Unknown')}

URL:
{item.get('url', '')}
"""

    reply = generate_reply(
        state["query"],
        context
    )

    constraint_messages = detect_constraints(
        state["query"]
    )

    if constraint_messages:

        reply = (
            "\n".join(
                constraint_messages
            )
            + "\n\n"
            + reply
        )

    recommendations = (
        build_recommendations(
            reranked[:8]
        )
    )

    logger.info(recommendations)

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": True
    }