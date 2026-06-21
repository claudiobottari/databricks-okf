---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a61be14bf3b6dbc858c2a15f9284a9dae50ee88c122c618d9ab241ffa28b7876
  pageDirectory: concepts
  sources:
    - guardrails-ai-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - detectpii-scorer
    - DetectPII
  citations:
    - file: guardrails-ai-scorers-databricks-on-aws.md
title: DetectPII Scorer
description: A Guardrails AI scorer for detecting personally identifiable information such as credit card numbers, SSNs, and email addresses in LLM outputs.
tags:
  - scorer
  - pii-detection
  - privacy
  - guardrails
timestamp: "2026-06-19T19:03:15.140Z"
---

# DetectPII Scorer

The **DetectPII scorer** is a rule-based evaluator provided by [Guardrails AI](/concepts/guardrails-ai-framework.md) that detects personally identifiable information (PII) in LLM outputs, such as credit card numbers, Social Security numbers, email addresses, and phone numbers. It is integrated into [MLflow](/concepts/mlflow.md) through the `mlflow.genai.scorers.guardrails` module and can be used with `mlflow.genai.evaluate()` or called directly as a standalone scorer. The scorer performs validation without requiring an LLM call, making it efficient for privacy checks in production evaluation pipelines. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Requirements

Install the `guardrails-ai` package to use the DetectPII scorer:

```python
%pip install guardrails-ai
```

^[guardrails-ai-scorers-databricks-on-aws.md]

## Quick Start

### Direct Usage

```python
from mlflow.genai.scorers.guardrails import DetectPII

pii_scorer = DetectPII()
feedback = pii_scorer(outputs="Email: user@example.com, Phone: 555-0123")
print(feedback.value)  # "yes" or "no"
```

^[guardrails-ai-scorers-databricks-on-aws.md]

### Usage with `mlflow.genai.evaluate()`

```python
import mlflow
from mlflow.genai.scorers.guardrails import DetectPII, ToxicLanguage

eval_dataset = [
    {
        "inputs": {"query": "What is MLflow?"},
        "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs.",
    },
    {
        "inputs": {"query": "How do I contact support?"},
        "outputs": "You can reach us at support@example.com or call 555-0123.",
    },
]

results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        ToxicLanguage(threshold=0.7),
        DetectPII(),
    ],
)
```

^[guardrails-ai-scorers-databricks-on-aws.md]

## Creating a Scorer by Name

You can dynamically create a DetectPII scorer using `get_scorer()` by passing the validator name as a string:

```python
from mlflow.genai.scorers.guardrails import get_scorer

pii_scorer = get_scorer(
    validator_name="DetectPII",
    pii_entities=["EMAIL_ADDRESS", "PHONE_NUMBER"],
)
feedback = pii_scorer(outputs="Contact: jane@example.com")
```

^[guardrails-ai-scorers-databricks-on-aws.md]

## Configuration

Guardrails AI scorers accept validator-specific parameters as keyword arguments to the constructor. The primary configuration parameter for the DetectPII scorer is `pii_entities`, which lets you specify which PII entity types to detect: ^[guardrails-ai-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.guardrails import DetectPII

pii_scorer = DetectPII(
    pii_entities=["CREDIT_CARD", "SSN", "EMAIL_ADDRESS"],
)
```

For additional validator-specific parameters, see the [Guardrails AI documentation](/concepts/guardrails-ai-scorers-integration.md) and the Guardrails Hub. ^[guardrails-ai-scorers-databricks-on-aws.md]

## How It Works

The DetectPII scorer is a rule-based validator from the Guardrails AI framework. It scans text outputs for patterns matching common PII entities — such as credit card numbers, Social Security numbers, email addresses, and phone numbers — and returns a binary feedback value (`"yes"` or `"no"`) indicating whether any of the specified PII entities were found. The validation is deterministic and does not incur LLM API costs, making it an efficient choice for privacy screening in evaluation workflows. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Related Concepts

- [Guardrails AI](/concepts/guardrails-ai-framework.md) — The framework providing rule-based validators for LLM output validation
- [ToxicLanguage Scorer](/concepts/toxiclanguage-scorer.md) — Another Guardrails AI scorer for toxicity detection
- [DetectJailbreak Scorer](/concepts/detectjailbreak-scorer.md) — Guardrails AI scorer for jailbreak attempt detection
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The `mlflow.genai.evaluate()` API for comprehensive model evaluation
- [Third-party scorers](/concepts/third-party-scorers-in-mlflow-genai.md) — Overview of integrating external scorers in MLflow

## Sources

- guardrails-ai-scorers-databricks-on-aws.md

# Citations

1. [guardrails-ai-scorers-databricks-on-aws.md](/references/guardrails-ai-scorers-databricks-on-aws-14c3c865.md)
