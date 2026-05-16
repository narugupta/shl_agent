# SHL Assessment Recommendation Agent

Conversational AI agent for intelligent SHL assessment recommendation, refinement, and comparison.

Built for the SHL Labs Agentic AI Engineering assessment.

---

# Overview

Hiring managers often start with vague hiring intent rather than precise assessment requirements. Traditional keyword-based filtering systems fail when users do not know the correct SHL assessment vocabulary.

This project solves that problem through a conversational retrieval-based agent that:

- Clarifies ambiguous hiring requirements
- Recommends relevant SHL assessments
- Supports conversational refinement
- Compares assessments using catalog-grounded data
- Refuses off-topic and prompt-injection attempts
- Operates fully statelessly through API-based conversation history

The system exclusively recommends assessments from the SHL product catalog.

---

# Evaluation

Detailed evaluation methodology is documented in:

```text
EVALUATION.md
```
# Features

## Conversational Recommendation
Supports natural hiring queries such as:

- "Hiring a Java backend developer"
- "Need a project manager with leadership skills"
- "Looking for customer support agents"

---

## Clarification Handling
The agent intelligently asks follow-up questions when queries are ambiguous.

Examples:
- Backend-heavy or frontend-heavy?
- What language will customers speak?
- What seniority level is the role?

---

## Refinement Support
The agent updates recommendations dynamically during conversation.

Example:
- "Add personality tests too"
- "Actually this is for graduates"

---

## Assessment Comparison
Supports grounded comparison between SHL assessments.

Example:
- "Compare OPQ and GSA"

---

## Safety Guardrails
The system refuses:
- off-topic queries
- legal/medical/tax advice
- prompt injection attempts
- non-SHL recommendation requests

---

# Tech Stack

## Backend
- FastAPI
- Uvicorn

## Retrieval & Search
- FAISS vector search
- Sentence Transformers
- RapidFuzz hybrid reranking

## LLM
- Groq API
- Llama 3

## Data Processing
- Python
- JSON-based catalog pipeline

## Deployment
- Docker
- Render

---

# Architecture

```text
User Query
    ↓
State Builder
    ↓
Guardrails
    ↓
Clarification Engine
    ↓
Query Parser
    ↓
Hybrid Retrieval
    ├── Semantic Search (FAISS)
    └── Keyword Reranking
    ↓
Recommendation Builder
    ↓
LLM Response Generation
    ↓
Structured API Response

# Deployment
 - https://shl-agent-mwvt.onrender.com/
