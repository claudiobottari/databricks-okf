---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b404b8d77ea225c47d1ba1ab106d4841f4fd78018910a0ac3424c324c2259189
  pageDirectory: concepts
  sources:
    - guardrails-ai-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-guardrails-integration
    - MGI
    - mlflow-guardrails-ai-scorer-integration
    - MGASI
  citations:
    - file: guardrails-ai-scorers-databricks-on-aws.md
title: MLflow Guardrails Integration
description: MLflow integrates Guardrails AI validators as scorers for rule-based LLM output evaluation without requiring additional LLM calls.
tags:
  - mlflow
  - integration
  - llm-evaluation
timestamp: "2026-06-19T19:02:44.842Z"
---

# MLflow Guardrails Integration

**MLflow Guardrails Integration** enables the use of [Guardrails AI](/concepts/guardrails-ai-framework.md) validators as scorers within MLflow's evaluation framework. This integration allows developers to validate LLM outputs for safety, PII detection, content quality, and other concerns using rule-based evaluation without requiring additional LLM calls. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Overview

Guardrails AI is a framework for validating LLM outputs using a community-driven hub of validators. MLflow integrates with Guardrails AI so that Guardrails validators can be used directly as scorers in MLflow evaluation workflows. This provides a lightweight, rule-based approach to output validation that does not incur the cost or latency of additional LLM inference. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Requirements

To use Guardrails AI scorers, install the `guardrails-ai` package:

```python
%pip install guardrails-ai
```

^[guardrails-ai-scorers-databricks-on-aws.md]

## Quick Start

Guardrails AI scorers can be called directly or used within MLflow's evaluation API.

### Direct Usage

To call a Guardrails AI scorer directly:

```python
from mlflow.genai.scorers.guardrails import ToxicLanguage

scorer = ToxicLanguage(threshold=0.7)
feedback = scorer(
    outputs="This is a professional and helpful response.",
)
print(feedback.value)  # "yes" or "no"
```

^[guardrails-ai-scorers-databricks-on-aws.md]

### Usage with mlflow.genai.evaluate()

To use Guardrails AI scorers within the [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) framework:

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

### Safety and Content Quality

These scorers validate LLM outputs for safety, PII detection, and content quality concerns. Available scorers include:

- **ToxicLanguage** — Detects toxic or harmful language in outputs
- **DetectPII** — Identifies personally identifiable information (PII) in outputs
- **DetectJailbreak** — Detects jailbreak attempts or prompt injection

^[guardrails-ai-scorers-databricks-on-aws.md]

## Creating a Scorer by Name

You can dynamically create a scorer using `get_scorer` by passing the validator name as a string:

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

Guardrails AI scorers accept validator-specific parameters as keyword arguments to the constructor. This allows customization of thresholds, validation methods, and entity types:

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

^[guardrails-ai-scorers-databricks-on-aws.md]

For validator-specific parameters and additional validators, see the [Guardrails AI documentation](https://www.guardrailsai.com/) and the [Guardrails Hub](https://guardrailsai.com/hub). ^[guardrails-ai-scorers-databricks-on-aws.md]

## Related Concepts

- [Guardrails AI](/concepts/guardrails-ai-framework.md) — The underlying framework for LLM output validation
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that integrates Guardrails scorers
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md) — Broader context for evaluating large language model outputs
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — MLflow's generative AI capabilities
- Content Safety — Related topic for safe LLM deployment

## Sources

- guardrails-ai-scorers-databricks-on-aws.md

# Citations

1. [guardrails-ai-scorers-databricks-on-aws.md](/references/guardrails-ai-scorers-databricks-on-aws-14c3c865.md)
