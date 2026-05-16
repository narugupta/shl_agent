# Evaluation Methodology

This project was evaluated across four dimensions:

- retrieval quality
- recommendation relevance
- groundedness
- conversational behavior

---

# 1. Retrieval Quality

The retrieval pipeline uses hybrid search:

- semantic vector retrieval (FAISS)
- keyword-aware reranking (RapidFuzz)

Evaluation focused on whether relevant SHL assessments appeared within the top retrieved candidates for realistic hiring queries.

Example queries:
- Java backend developer
- finance analyst
- project manager
- contact center hiring

Metrics considered:
- Recall@10
- relevance of retrieved assessment categories
- diversity of retrieved assessment types

---

# 2. Recommendation Relevance

Recommendations were manually validated against:
- role requirements
- seniority
- technical skill alignment
- leadership requirements
- personality requirements

The system was iteratively tuned to produce balanced recommendation stacks including:
- technical tests
- cognitive tests
- personality assessments
- simulations

---

# 3. Groundedness

All recommendations are constrained to:
- catalog-derived assessments
- catalog URLs only
- catalog-grounded comparison responses

The system explicitly refuses:
- off-topic queries
- prompt injection attempts
- non-SHL recommendations

This minimizes hallucination risk.

---

# 4. Conversational Evaluation

The system was tested against:
- vague queries
- refinement flows
- comparison requests
- unsupported skills
- prompt injection attempts
- off-topic prompts

Example behaviors tested:
- clarification before recommendation
- refinement after user edits
- role-specific follow-up questions
- graceful handling of unsupported technologies

---

# 5. Public Trace Testing

The provided SHL public conversation traces were used to:
- evaluate conversational flow
- improve clarification quality
- tune reranking logic
- improve Recall@10 behavior

Patterns from traces informed:
- leadership assessment boosting
- clarification strategy
- recommendation diversity
- language-aware screening

---

# 6. Failure Prevention

Additional safeguards included:
- recommendation count limits
- schema validation
- missing-field handling
- duplicate filtering
- catalog cleanup

The API was repeatedly tested to ensure:
- no hallucinated URLs
- no server crashes
- valid response schema
- stateless behavior

---

# 7. Automated Tests

Pytest-based endpoint tests validate:
- API schema correctness
- refinement behavior
- comparison flow
- response generation
