---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 935f23feb9b1874920ddc95bb20ace1bcc336267f2cc60887885389e02f6053c
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - global-vs-per-row-guidelines
    - GVPG
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Global vs Per-Row Guidelines
description: "Two strategies for applying evaluation criteria: uniform Guidelines() across all rows vs row-specific ExpectationsGuidelines() for domain-expert-labeled datasets."
tags:
  - mlflow
  - evaluation-patterns
  - genai
timestamp: "2026-06-19T17:55:31.841Z"
---

# Global vs Per-Row Guidelines

**Global vs Per-Row Guidelines** refers to two distinct approaches for defining evaluation criteria when using [LLM Judges](/concepts/llm-judges.md) in MLflow GenAI. Global guidelines apply uniformly across all evaluation rows or production traces, while per-row guidelines allow different criteria for each individual example in a dataset. The choice between them depends on whether your evaluation requires consistent standards across all inputs or scenario-specific criteria tailored to individual cases.

## Overview

MLflow provides two built-in judges for guidelines-based evaluation:

- **`Guidelines()`**: Applies the same set of guidelines to every row in an evaluation dataset or to every trace in production monitoring. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **`ExpectationsGuidelines()`**: Evaluates against row-specific guidelines provided by domain experts, allowing different evaluation criteria for each example in a dataset. This judge is available for offline evaluation only. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## How Guidelines Work

Both approaches use a specially-tuned LLM to evaluate whether text meets specified criteria. The judge:
1. **Receives context**: Any JSON dictionary containing the data to evaluate (for example, `request`, `response`, `retrieved_documents`, `user_preferences`). Keys from the context can be referenced directly in guidelines.
2. **Applies guidelines**: Natural language rules defining pass/fail conditions.
3. **Makes judgment**: Returns a binary pass/fail score with detailed rationale. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Global Guidelines (`Guidelines()`)

The `Guidelines()` judge is designed for scenarios where the same quality standards apply across all evaluations. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### When to Use

Use global guidelines when:
- You have consistent quality requirements that apply to every interaction, such as tone, compliance, or formatting rules.
- You want to monitor the same criteria across all production traces.
- You need to establish baseline quality standards for your application. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Example

```python
from mlflow.genai.scorers import Guidelines

# Define global standards for all customer interactions
tone_guidelines = Guidelines(
    name="customer_service_tone",
    guidelines="""The response must maintain our brand voice which is:
    - Professional yet warm and conversational (avoid corporate jargon)
    - Empathetic, acknowledging emotional context before jumping to solutions""")

compliance_guidelines = Guidelines(
    name="policy_compliance",
    guidelines=[
        """Refund and return policies:
        - The response must not promise refunds beyond the 30-day return window
        - The response must mention restocking fees for electronics (15%)""",
        """Data privacy and security:
        - The response must never ask for full credit card numbers, SSN, or passwords"""])

results = mlflow.genai.evaluate(
    data=customer_interactions,
    scorers=[tone_guidelines, compliance_guidelines])
```
^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Per-Row Guidelines (`ExpectationsGuidelines()`)

The `ExpectationsGuidelines()` judge evaluates each row against guidelines stored in the row's `expectations` field. Different rows can have entirely different criteria. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### When to Use

Use per-row guidelines when:
- Domain experts have labeled specific examples with custom guidelines.
- Different scenarios require different evaluation criteria.
- You need to test edge cases or specific behaviors with tailored rules. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Example

```python
from mlflow.genai.scorers import ExpectationsGuidelines

# Dataset with scenario-specific guidelines
customer_service_data = [
    {
        "inputs": {
            "messages": [{"role": "user", "content": "My package is 3 weeks late and I need it for an event tomorrow!"}]
        },
        "outputs": {
            "choices": [{"message": {"content": "I absolutely understand how stressful this must be..."}}]
        },
        "expectations": {
            "guidelines": [
                """The response must handle this urgent situation with exceptional care:
                - First acknowledge both the delay AND the urgent tomorrow deadline
                - Must NOT make excuses or blame shipping partners""",
                """The response must provide immediate actionable solutions:
                - Offer to check local store availability for same-day pickup
                - Include the executive customer service email for formal complaints"""]
        }
    },
    {
        "inputs": {
            "messages": [{"role": "user", "content": "How do I cancel my subscription?"}]
        },
        "outputs": {
            "choices": [{"message": {"content": "I can help you cancel your subscription right away. Here's how: ..."}}]
        },
        "expectations": {
            "guidelines": [
                """The response must respect the customer's decision to cancel:
                - No guilt-inducing language or excessive retention attempts
                - Must not hide the cancellation process behind multiple steps""",
                """The response must provide complete cancellation information:
                - State the exact steps to cancel online
                - Explain what happens to their data and history"""]
        }
    }
]

results = mlflow.genai.evaluate(
    data=customer_service_data,
    scorers=[ExpectationsGuidelines()])
```
^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Key Differences

| Aspect | Global Guidelines | Per-Row Guidelines |
|--------|-------------------|--------------------|
| **Judge class** | `Guidelines()` | `ExpectationsGuidelines()` |
| **Criteria scope** | Uniform across all rows | Different per row |
| **Guidelines source** | Defined in code at judge creation | Stored in dataset's `expectations` field |
| **Offline evaluation** | Supported | Supported |
| **Production monitoring** | Supported | Not supported (offline only) |
| **When to use** | Consistent quality standards | Domain expert labels, scenario-specific testing |

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Best Practices

For both approaches, follow these guidelines when writing effective criteria:

- **Be specific and measurable**: ✅ "The response must not include specific pricing amounts or percentages" ❌ "Don't talk about money"
- **Use clear pass/fail conditions**: ✅ "If asked about pricing, the response must direct users to the pricing page" ❌ "Handle pricing questions appropriately"
- **Reference context explicitly**: ✅ "The response must only use facts present in retrieved_context" ❌ "Be factual"
- **Structure complex requirements**: Use bullet lists to break down multi-part criteria. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Choosing Between Global and Per-Row

Use **global guidelines** when you need consistent quality standards across all interactions, such as brand voice, compliance rules, or output format requirements. Use **per-row guidelines** when different scenarios demand different evaluation criteria, such as handling urgent complaints differently from routine inquiries, or when domain experts have provided scenario-specific expectations. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) — Creating tailored evaluation criteria with `make_judge()`
- [LLM Judges](/concepts/llm-judges.md) — Overview of all judge types in MLflow GenAI
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework for GenAI applications
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring
- Align judges with human feedback — Improving judge accuracy with expert annotations

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
