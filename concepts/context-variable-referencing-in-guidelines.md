---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c5a7f9aeb6389e0fca2497c0a0d11dd3c62ec2df0e7a14275a53444afa2f62b
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - context-variable-referencing-in-guidelines
    - CVRIG
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Context Variable Referencing in Guidelines
description: Guidelines can reference any key from the evaluation context dictionary (e.g., request, response, retrieved_documents, user_preferences) to create dynamic, data-aware pass/fail rules.
tags:
  - mlflow
  - evalution
  - prompt-engineering
timestamp: "2026-06-19T17:55:28.833Z"
---

# Context Variable Referencing in Guidelines

**Context Variable Referencing in Guidelines** is a feature of the [Guidelines LLM Judge](/concepts/guidelines-llm-judge.md) in MLflow that allows you to reference any key from the evaluation context dictionary directly within a natural‑language guideline. This enables dynamic, data‑driven pass/fail criteria that adapt to the specific inputs, outputs, and metadata of each evaluation row. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## How to Reference Context Variables

When writing a guideline, simply include the context key name as a variable within the string. The judge will substitute the corresponding value from the context dictionary at evaluation time. The following examples illustrate common usage patterns. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Example 1: Validate against retrieved documents

```python
context = {
    "request": "What is the refund policy?",
    "response": "You can return items within 30 days for a full refund.",
    "retrieved_documents": [
        "Policy: Returns accepted within 30 days",
        "Policy: No refunds after 30 days"
    ]
}
guideline = "The response must only include information from retrieved_documents"
```

The judge will evaluate whether the `response` contains facts that come exclusively from the list in `retrieved_documents`. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Example 2: Check user preferences

```python
context = {
    "request": "Recommend a restaurant",
    "response": "I suggest trying the new steakhouse downtown",
    "user_preferences": {"dietary_restrictions": "vegetarian", "cuisine": "Italian"}
}
guideline = "The response must respect user_preferences when making recommendations"
```

The judge checks that the `response` aligns with the dietary and cuisine constraints stored in `user_preferences`. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Example 3: Enforce business rules

```python
context = {
    "request": "Can you apply a discount?",
    "response": "I've applied a 15% discount to your order",
    "max_allowed_discount": 10,
    "user_tier": "silver"
}
guideline = "The response must not exceed max_allowed_discount for the user_tier"
```

The judge verifies that the discount percentage in the `response` does not exceed the policy limit defined by `max_allowed_discount`, given the user’s tier. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Example 4: Multiple constraints

```python
context = {
    "request": "Tell me about product features",
    "response": "This product includes features A, B, and C",
    "approved_features": ["A", "B", "C", "D"],
    "deprecated_features": ["X", "Y", "Z"]
}
guideline = """The response must:
- Only mention approved_features
- Not include deprecated_features
"""
```

The judge enforces two rules simultaneously by referencing two separate context keys. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Best Practices for Referencing Context

- **Use descriptive key names** that clearly indicate what the variable holds (e.g., `max_allowed_discount` rather than `x`). ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Reference context explicitly** in every relevant guideline instead of relying on implicit assumptions. This improves readability and interpretability. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Structure complex requirements** with bullet points referencing different context variables for clarity. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [Guidelines LLM Judge](/concepts/guidelines-llm-judge.md) – The judge type that evaluates against natural‑language criteria.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The broader framework for evaluating GenAI applications.
- [Context Variables](/concepts/context-variables-in-guidelines.md) – The dictionary keys that populate the evaluation context (e.g., `request`, `response`, `retrieved_documents`).
- MLflow Evaluate API – The function that runs evaluation with provided data and scorers.

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
