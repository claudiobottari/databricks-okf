---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44e6d0c5e64933e182e327c8b7b75a5bacf430a3bd6d33952692ab274b5572f1
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - guideline-authoring-best-practices
    - GABP
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Guideline Authoring Best Practices
description: Effective natural-language guidelines for LLM judges should be specific and measurable, use clear pass/fail conditions, explicitly reference context variables, and structure complex requirements with bullet points.
tags:
  - best-practices
  - llm-evaluation
  - genai
timestamp: "2026-06-19T14:29:51.026Z"
---

# Guideline Authoring Best Practices

**Guideline Authoring Best Practices** provides guidance for writing natural-language criteria used by [Guidelines LLM judges](/concepts/guidelines-llm-judge.md) to evaluate GenAI outputs. Well-written guidelines are crucial for accurate evaluation, as they directly determine the judge’s ability to return reliable pass/fail scores with meaningful rationale. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Overview

Guidelines judges apply business-friendly, flexible, and interpretable criteria without requiring code changes. They enable domain experts to define pass/fail conditions and iterate rapidly on new criteria. To maximize these benefits, guidelines must be precise, measurable, and context-aware. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Best Practices

### Be Specific and Measurable

Guidelines should state concrete conditions rather than vague expectations. Use clear, verifiable language that leaves no room for subjective interpretation.

- **Good:** ✅ "The response must not include specific pricing amounts or percentages"
- **Bad:** ❌ "Don't talk about money"

A measurable condition allows the judge to deterministically decide whether the output meets the requirement. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Use Clear Pass/Fail Conditions

Each guideline should define an unambiguous binary outcome. Avoid open-ended instructions that require the judge to infer intent.

- **Good:** ✅ "If asked about pricing, the response must direct users to the pricing page"
- **Bad:** ❌ "Handle pricing questions appropriately"

Clear pass/fail conditions reduce false positives and make evaluation results more actionable. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Reference Context Variables Explicitly

Guidelines can reference any key from the context dictionary that the judge receives. This enables dynamic evaluation against retrieved documents, user preferences, or business rules.

```python
context = {
    "request": "What is the refund policy?",
    "response": "You can return items within 30 days.",
    "retrieved_documents": ["Policy: Returns accepted within 30 days"]
}
guideline = "The response must only include information from retrieved_documents"
```

Referencing context variables explicitly makes guidelines self-contained and adaptable to different evaluation scenarios. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Structure Complex Requirements

When a guideline must check multiple conditions, use a bulleted list to make each requirement distinct and independently verifiable.

```python
guideline = """The response must:
- Include a greeting if first message
- Address the user's specific question
- End with an offer to help further
- Not exceed 150 words"""
```

Structured lists improve readability and allow the judge to evaluate each condition separately. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Additional Guidelines

- **Be specific and measurable** – Avoid vague language; state exact behaviors to check.
- **Use clear pass/fail conditions** – Ensure each criterion has a definite outcome.
- **Reference context explicitly** – Use keys from the context dictionary (e.g., `request`, `response`, `retrieved_documents`, `user_preferences`).
- **Structure complex requirements** – Use bulleted lists for multi-condition guidelines.

These practices help ensure that the judge produces consistent, interpretable, and actionable evaluations. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Benefits of Well-Written Guidelines

When guidelines follow the best practices above, [Guidelines judges](/concepts/guidelines-llm-judge.md) provide the following advantages:

- **Business-friendly**: Domain experts write criteria without coding.
- **Flexible**: Update criteria without code changes.
- **Interpretable**: Clear pass/fail conditions with detailed rationale.
- **Fast iteration**: Rapidly test and refine new criteria.

These benefits are realized only when guidelines are precise and structured correctly. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Real-World Examples

The source material provides extensive real-world examples for customer service chatbots and document extraction applications. In each example, guidelines are written as explicit, context-referencing lists of conditions. For instance, a guideline for handling duplicate charges reads:

```
The response must immediately validate the customer's concern:
- Acknowledge the duplicate charge without skepticism
- Must not ask for proof or screenshots initially
- Express understanding of the inconvenience...
```

Such structured, action-oriented guidelines enable the judge to score each interaction consistently. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [Guidelines LLM Judge](/concepts/guidelines-llm-judge.md) – The judge that applies global `Guidelines()` to all rows.
- [ExpectationsGuidelines judge](/concepts/expectationsguidelines-judge-per-row-guidelines.md) – The judge that applies per-row guidelines from an evaluation dataset.
- [Custom Judges](/concepts/custom-judges.md) – Building your own LLM-based scorers beyond the built-in guidelines judges.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The framework for evaluating and monitoring GenAI agents.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The data structure that supplies inputs, outputs, and optional expectations for per-row guidelines.

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
