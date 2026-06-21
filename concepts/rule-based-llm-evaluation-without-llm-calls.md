---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 67184d81036d0c55ac3175b0a81a15502c349b983d3ba97eeeb2dbe298b89148
  pageDirectory: concepts
  sources:
    - guardrails-ai-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rule-based-llm-evaluation-without-llm-calls
    - RLEWLC
  citations:
    - file: guardrails-ai-scorers-databricks-on-aws.md
title: Rule-based LLM Evaluation without LLM Calls
description: Guardrails AI scorers perform rule-based validation of LLM outputs without requiring additional LLM inference calls, offering a lightweight evaluation approach.
tags:
  - llm-evaluation
  - rule-based
  - efficiency
timestamp: "2026-06-19T19:03:05.440Z"
---

# Rule-based LLM Evaluation without LLM Calls

**Rule-based LLM Evaluation without LLM Calls** refers to the practice of assessing language model outputs using deterministic rules and validators rather than making additional calls to a large language model. This approach reduces cost and latency while providing consistent, interpretable quality checks on safety, PII detection, content quality, and other criteria. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Overview

MLflow integrates with [Guardrails AI](https://www.guardrailsai.com/), a framework that provides a community-driven hub of validators for tasks such as safety, PII detection, and content quality. These validators can be used as [MLflow Scorers](/concepts/mlflow-scorers.md) to perform rule-based evaluation of LLM outputs without requiring any LLM calls. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Requirements

To use Guardrails AI scorers in MLflow, install the `guardrails-ai` package:

```python
%pip install guardrails-ai
```

^[guardrails-ai-scorers-databricks-on-aws.md]

## Quick start

### Using a scorer directly

Guardrails AI scorers can be instantiated and called directly on a string output:

```python
from mlflow.genai.scorers.guardrails import ToxicLanguage

scorer = ToxicLanguage(threshold=0.7)
feedback = scorer(
    outputs="This is a professional and helpful response.",
)
print(feedback.value)  # "yes" or "no"
```

^[guardrails-ai-scorers-databricks-on-aws.md]

### Using scorers with `mlflow.genai.evaluate()`

Scorers can also be used as part of an [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation run:

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

## Available Guardrails AI scorers

Guardrails AI provides validators that assess LLM outputs for safety, PII, and content quality. The following scorers are available through the `mlflow.genai.scorers.guardrails` module:

- `ToxicLanguage` – Detects toxic or offensive language in the output. ^[guardrails-ai-scorers-databricks-on-aws.md]
- `DetectPII` – Identifies personally identifiable information such as credit card numbers, SSNs, and email addresses. ^[guardrails-ai-scorers-databricks-on-aws.md]
- `DetectJailbreak` – Detects attempts to jailbreak the model or bypass safety guidelines. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Create a scorer by name

A Guardrails AI scorer can be created dynamically by passing the validator name as a string to the `get_scorer` function:

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

Guardrails AI scorers accept validator-specific parameters as keyword arguments to the constructor. Common configuration options include thresholds and lists of entities to detect: ^[guardrails-ai-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.guardrails import ToxicLanguage, DetectPII, DetectJailbreak

# Toxicity detection with custom threshold and sentence-level validation
scorer = ToxicLanguage(
    threshold=0.7,
    validation_method="sentence",
)

# PII detection with specific entity types
pii_scorer = DetectPII(
    pii_entities=["CREDIT_CARD", "SSN", "EMAIL_ADDRESS"],
)

# Jailbreak detection with custom sensitivity
jailbreak_scorer = DetectJailbreak(
    threshold=0.9,
)
```

For a complete list of validator-specific parameters and additional validators, see the [Guardrails AI documentation](https://www.guardrailsai.com/) and the [Guardrails Hub](https://guardrailsai.com/hub). ^[guardrails-ai-scorers-databricks-on-aws.md]

## Related concepts

- [MLflow](/concepts/mlflow.md) – Open-source platform for managing the ML lifecycle, including evaluation and scoring.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – MLflow’s support for generative AI agents and LLM evaluation.
- [LLM evaluation](/concepts/llm-as-a-judge-evaluation.md) – Broader topic of assessing LLM outputs through various methods.
- Content Safety – Ensuring LLM outputs do not contain harmful or toxic content.
- PII Detection – Identifying personally identifiable information in model outputs.
- Jailbreak Detection – Detecting attempts to manipulate an LLM into violating its guidelines.

## Sources

- guardrails-ai-scorers-databricks-on-aws.md

# Citations

1. [guardrails-ai-scorers-databricks-on-aws.md](/references/guardrails-ai-scorers-databricks-on-aws-14c3c865.md)
