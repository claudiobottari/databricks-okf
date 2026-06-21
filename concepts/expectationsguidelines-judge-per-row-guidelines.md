---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8389d357bb74d38d0a196922a992eb8abc07e4348129536b69f77a9791656704
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - expectationsguidelines-judge-per-row-guidelines
    - EJ(G
    - ExpectationsGuidelines
    - ExpectationsGuidelines judge
    - ExpectationsGuidelines() Judge
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: ExpectationsGuidelines() Judge (Per-Row Guidelines)
description: A built-in MLflow scorer that evaluates against row-specific guidelines provided by domain experts in the evaluation dataset, enabling different criteria for each example.
tags:
  - mlflow
  - llm-evaluation
  - scoring
  - per-row-guidelines
timestamp: "2026-06-18T14:47:20.815Z"
---

# ExpectationsGuidelines() Judge (Per-Row Guidelines)

The **`ExpectationsGuidelines()` judge** is a built-in Guidelines LLM judge in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that evaluates GenAI outputs against row-specific guidelines rather than global criteria applied uniformly across an entire evaluation dataset. It is designed for offline evaluation scenarios where each example in an evaluation dataset may require different quality criteria defined by domain experts.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Overview

Unlike the `Guidelines()` judge which applies the same pass/fail criteria to every row, the `ExpectationsGuidelines()` judge reads per-row guidelines from the `expectations` field of each evaluation dataset entry. This allows different evaluation criteria for each example, making it suitable for scenarios where the expected behavior varies based on context, document type, or specific user scenarios.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## When to Use

Use this judge when:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- **Domain experts** have labeled specific examples with custom guidelines or expectations
- **Different rows require different evaluation criteria** — for example, customer service interactions involving cancellations may have different quality standards than billing dispute responses
- **You need scenario-specific validation** — such as document extraction tasks where the extraction rules differ for invoices, contracts, and medical records

## How It Works

The `ExpectationsGuidelines()` judge uses a specially-tuned LLM to evaluate whether text meets the row-specific criteria. The judge:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

1. **Receives context**: A JSON dictionary containing the data to evaluate, typically with `request` (app inputs) and `response` (app outputs) keys
2. **Applies per-row guidelines**: Natural language rules from the `expectations.guidelines` field of the current evaluation row
3. **Makes judgment**: Returns a binary pass/fail score with detailed rationale

The judge evaluates app inputs and outputs only, and is designed for offline evaluation — it is not available for [Production Monitoring](/concepts/production-monitoring.md).^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Dataset Format

To use `ExpectationsGuidelines()`, each row in your evaluation dataset must include an `expectations` key containing a `guidelines` array with one or more natural language criteria:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

```python
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
```

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Usage Example

```python
from mlflow.genai.scorers import ExpectationsGuidelines
import mlflow

# Evaluate with per-row guidelines
results = mlflow.genai.evaluate(
    data=data,
    scorers=[ExpectationsGuidelines()]
)
```

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Return Values

The judge returns an [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) object containing:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- `value`: `"yes"` (meets guidelines) or `"no"` (fails guidelines)
- `rationale`: Detailed explanation of why the content passed or failed
- `name`: The assessment name (auto-generated for `ExpectationsGuidelines()`)
- `error`: Error details if evaluation failed

## Reference Context Variables

In your per-row guidelines, you can reference any key from the context dictionary directly. The `request` and `response` keys are automatically extracted from the app's inputs and outputs:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- **Request**: Extracted from the `inputs` field — typically the user's question or conversation history
- **Response**: Extracted from the `outputs` field — the agent's generated response

For parsing details, see [Guidelines() Judge (Global Guidelines)](/concepts/guidelines-judge-global-guidelines.md).

## Real-World Applications

### Customer Service with Scenario-Specific Guidelines

Each customer interaction type can have its own set of quality criteria:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- **Urgent delivery issues**: Guidelines might require acknowledging both the delay and the urgent deadline, expressing genuine empathy, and not making excuses
- **Subscription cancellations**: Guidelines might require respecting the customer's decision, providing clear instructions, and avoiding guilt-inducing language
- **Billing disputes**: Guidelines might require validating the concern without skepticism, providing specific resolution details, and addressing potential financial impacts

### Document Extraction with Type-Specific Guidelines

Different document types can have specialized extraction criteria:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- **Invoices**: Line items must be extracted as arrays with description, quantity, unit price, and total; currency must be explicitly identified
- **Contracts**: Must differentiate between execution date, effective date, and expiration date; must identify all parties with full legal names
- **Medical records**: Must comply with HIPAA privacy standards; diagnoses must use ICD-10 codes when available

## Comparison with Guidelines() Judge

| Feature | `Guidelines()` | `ExpectationsGuidelines()` |
|---------|---------------|---------------------------|
| Scope | Global — same criteria for all rows | Per-row — different criteria per example |
| Guideline source | Defined at judge creation time | Read from dataset's `expectations.guidelines` |
| Use case | Uniform quality standards | Scenario-specific validation |
| Production monitoring | Supported | Not supported |
| Evaluation mode | Offline and production | Offline only |

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Best Practices for Per-Row Guidelines

When writing per-row guidelines for `ExpectationsGuidelines()`, follow these recommendations:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Be Specific and Measurable

✅ "The response must not include specific pricing amounts or percentages"
❌ "Don't talk about money"

### Use Clear Pass/Fail Conditions

✅ "If asked about pricing, the response must direct users to the pricing page"
❌ "Handle pricing questions appropriately"

### Reference Context Explicitly

✅ "The response must only use facts present in retrieved_context"
❌ "Be factual"

### Structure Complex Requirements

```
The response must:
- Include a greeting if first message
- Address the user's specific question
- End with an offer to help further
- Not exceed 150 words
```

## Related Concepts

- [Guidelines() Judge (Global Guidelines)](/concepts/guidelines-judge-global-guidelines.md) — The global alternative to per-row guidelines
- [Custom Judges](/concepts/custom-judges.md) — Creating arbitrary LLM-based scorers with `make_judge()`
- make_judge()|Make Judge API — The `make_judge()` function for custom evaluators
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring
- Align judges with human feedback — Improving judge accuracy with expert annotations
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing agent variants with consistent judges

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
