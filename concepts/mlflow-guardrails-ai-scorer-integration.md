---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 34aaed6efb6904d12a6fccf2f2db088837884e805075d955928dff06abb02e32
  pageDirectory: concepts
  sources:
    - guardrails-ai-scorers-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-guardrails-ai-scorer-integration
    - MGASI
  citations:
    - file: guardrails-ai-scorers-databricks-on-aws.md
title: MLflow Guardrails AI scorer integration
description: MLflow integrates Guardrails AI validators as scorers for rule-based LLM evaluation without requiring LLM calls
tags:
  - mlflow
  - integration
  - llm-evaluation
timestamp: "2026-06-19T10:46:51.419Z"
---

# MLflow Guardrails AI Scorer Integration

**MLflow Guardrails AI Scorer Integration** allows you to use [Guardrails AI](/concepts/guardrails-ai-framework.md) validators as scorers within the MLflow evaluation framework. Guardrails AI is a framework for validating LLM outputs using a community-driven hub of validators for safety, PII detection, content quality, and more. By integrating with MLflow, you can apply rule-based evaluation without requiring additional LLM calls, making it efficient for continuous quality monitoring and offline evaluation. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Requirements

Install the `guardrails-ai` package to use the integration:

```python
%pip install guardrails-ai
```

^[guardrails-ai-scorers-databricks-on-aws.md]

## Quick Start

You can call a Guardrails AI scorer directly by instantiating a scorer class and invoking it on output text:

```python
from mlflow.genai.scorers.guardrails import ToxicLanguage

scorer = ToxicLanguage(threshold=0.7)
feedback = scorer(
    outputs="This is a professional and helpful response.",
)
print(feedback.value)  # "yes" or "no"
```

^[guardrails-ai-scorers-databricks-on-aws.md]

To use Guardrails AI scorers in an [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) run with `mlflow.genai.evaluate()`, pass them in the `scorers` list:

```python
import mlflow
from mlflow.genai.scorers.guardrails import ToxicLanguage, DetectPII

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

## Available Guardrails AI Scorers

The integration provides scorers for safety and content quality, including:

- **ToxicLanguage** – Detects toxic language in outputs.
- **DetectPII** – Detects personally identifiable information (PII) such as credit card numbers, Social Security numbers, and email addresses.
- **DetectJailbreak** – Detects attempts to jailbreak the LLM.

^[guardrails-ai-scorers-databricks-on-aws.md]

## Creating a Scorer by Name

You can dynamically create a scorer using the `get_scorer` function by passing the validator name as a string:

```python
from mlflow.genai.scorers.guardrails import get_scorer

scorer = get_scorer(
    validator_name="ToxicLanguage",
    threshold=0.7,
)
feedback = scorer(
    outputs="This is a professional response.",
)
```

^[guardrails-ai-scorers-databricks-on-aws.md]

## Configuration

Guardrails AI scorers accept validator-specific parameters as keyword arguments to the constructor. For example, you can customize the threshold, validation method, or PII entity types:

```python
from mlflow.genai.scorers.guardrails import ToxicLanguage, DetectPII, DetectJailbreak

# Toxicity detection with custom threshold
scorer = ToxicLanguage(
    threshold=0.7,
    validation_method="sentence",
)

# PII detection with custom entity types
pii_scorer = DetectPII(
    pii_entities=["CREDIT_CARD", "SSN", "EMAIL_ADDRESS"],
)

# Jailbreak detection with custom sensitivity
jailbreak_scorer = DetectJailbreak(
    threshold=0.9,
)
```

For the full list of validator-specific parameters and additional validators, see the [Guardrails AI documentation](/concepts/guardrails-ai-scorers-integration.md) and the Guardrails Hub. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Related Concepts

- [Guardrails AI](/concepts/guardrails-ai-framework.md) — The underlying framework for validators.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API used to run scorers.
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers for agent evaluation, complementary to rule-based Guardrails scorers.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous quality monitoring.
- Third-Party Scorer Integration — General pattern for integrating external evaluation tools.

## Sources

- guardrails-ai-scorers-databricks-on-aws.md

# Citations

1. [guardrails-ai-scorers-databricks-on-aws.md](/references/guardrails-ai-scorers-databricks-on-aws-14c3c865.md)
