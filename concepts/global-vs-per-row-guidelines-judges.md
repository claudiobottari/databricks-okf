---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58a7d7cccb0a0fa90ac807c3ad774654cb3558723a9df462c5a2f822a0783ade
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - global-vs-per-row-guidelines-judges
    - GVPGJ
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Global vs Per-Row Guidelines Judges
description: "MLflow provides two built-in guidelines judges: `Guidelines()` for uniform global rules across all rows, and `ExpectationsGuidelines()` for per-row guidelines labeled by domain experts in the evaluation dataset."
tags:
  - llm-evaluation
  - mlflow
  - genai
timestamp: "2026-06-19T14:29:44.532Z"
---

# Global vs Per-Row Guidelines Judges

**Global vs Per-Row Guidelines Judges** refers to two distinct approaches for applying [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation. The `Guidelines()` judge applies uniform criteria across all rows in a dataset, while the `ExpectationsGuidelines()` judge applies row-specific criteria defined by domain experts. Choosing between them depends on whether your evaluation requires consistent standards or per-example customization.

## Overview

Guidelines judges use a specially-tuned LLM to evaluate whether text meets specified pass/fail criteria. The judge receives context (such as `request`, `response`, `retrieved_documents`), applies natural language rules, and returns a binary pass/fail score with detailed rationale. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

MLflow provides two built-in guidelines judges that differ in how guidelines are applied:

- **`Guidelines()`**: Applies global guidelines uniformly to all rows. Evaluates app inputs and outputs only. Works in both offline evaluation and production monitoring.
- **`ExpectationsGuidelines()`**: Applies per-row guidelines labeled by domain experts in an evaluation dataset. Evaluates app inputs and outputs only. For offline evaluation only.

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## `Guidelines()` Judge: Global Guidelines

The `Guidelines` judge applies the same set of guidelines to every row in your evaluation dataset or every trace in production monitoring. It automatically extracts `request` and `response` data from your trace and evaluates it against your guidelines. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### When to Use

Use global guidelines when you have consistent quality standards that apply across all interactions, such as:

- **Compliance**: "Must not include pricing information"
- **Style/tone**: "Maintain professional, empathetic tone"
- **Requirements**: "Must include specific disclaimers"
- **Accuracy**: "Use only facts from provided context"

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Example

```python
from mlflow.genai.scorers import Guidelines
import mlflow

# Define global standards for all interactions
tone_guidelines = Guidelines(
    name="customer_service_tone",
    guidelines="""The response must maintain our brand voice which is:
    - Professional yet warm and conversational (avoid corporate jargon)
    - Empathetic, acknowledging emotional context before jumping to solutions
    - Proactive in offering help without being pushy"""
)

# Evaluate with global guidelines
results = mlflow.genai.evaluate(
    data=customer_interactions,
    scorers=[tone_guidelines]
)
```

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Parameters

The `Guidelines` judge accepts a `model` argument to specify a custom judge model. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the model provider, the model name is the same as the serving endpoint name. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## `ExpectationsGuidelines()` Judge: Per-Row Guidelines

The `ExpectationsGuidelines` judge evaluates against row-specific guidelines from domain experts. This allows different evaluation criteria for each example in your dataset. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### When to Use

Use per-row guidelines when:

- You have domain experts who have labeled specific examples with custom guidelines
- Different rows require different evaluation criteria
- Different scenarios (e.g., billing issues, cancellations, technical support) need distinct quality standards

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Example

```python
from mlflow.genai.scorers import ExpectationsGuidelines
import mlflow

# Dataset with per-row guidelines
data = [
    {
        "inputs": {"question": "What is the capital of France?"},
        "outputs": "The capital of France is Paris.",
        "expectations": {
            "guidelines": ["The response must be factual and concise"]
        }
    },
    {
        "inputs": {"question": "How to learn Python?"},
        "outputs": "You can read a book or take a course.",
        "expectations": {
            "guidelines": ["The response must be helpful and encouraging"]
        }
    }
]

# Evaluate with per-row guidelines
results = mlflow.genai.evaluate(
    data=data,
    scorers=[ExpectationsGuidelines()]
)
```

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Dataset Structure

For per-row guidelines, each entry in the evaluation dataset must include an `expectations` dictionary containing a `guidelines` key with a list of guideline strings. The judge evaluates the output against only the guidelines specified for that particular row. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Comparison

| Feature | `Guidelines()` | `ExpectationsGuidelines()` |
|---------|----------------|---------------------------|
| Scope | Global (same for all rows) | Per-row (different per example) |
| Use case | Consistent standards across all interactions | Scenario-specific criteria from domain experts |
| Offline evaluation | ✅ | ✅ |
| Production monitoring | ✅ | ❌ |
| Dataset requirements | Standard inputs/outputs | Must include `expectations.guidelines` per row |
| Custom judge model | ✅ (via `model` argument) | Not specified |

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Best Practices

### Reference Context Variables

Both judges support referencing context variables directly in guidelines. Include any key from your context dictionary — such as `request`, `response`, `retrieved_documents`, or `user_preferences` — directly in your guideline text. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

```python
guideline = "The response must only include information from retrieved_documents"
```

### Writing Effective Guidelines

- **Be specific and measurable**: ✅ "The response must not include specific pricing amounts or percentages" ❌ "Don't talk about money"
- **Use clear pass/fail conditions**: ✅ "If asked about pricing, the response must direct users to the pricing page" ❌ "Handle pricing questions appropriately"
- **Reference context explicitly**: ✅ "The response must only use facts present in retrieved_context" ❌ "Be factual"
- **Structure complex requirements**: Use bullet points for multi-part guidelines

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Return Values

Both judges return an [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) object containing:

- `value`: `"yes"` (meets guidelines) or `"no"` (fails guidelines)
- `rationale`: Detailed explanation of why the content passed or failed
- `name`: The assessment name (either provided or auto-generated)
- `error`: Error details if evaluation failed

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) — The underlying mechanism for pass/fail evaluation
- [Custom Judges](/concepts/custom-judges.md) — Building judges for specific needs beyond guidelines
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring
- Align judges with human feedback — Improving judge accuracy with expert annotations

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
