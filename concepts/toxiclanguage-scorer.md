---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37b73abb92d40b74ed442549c1590385f7f392c9074ab0564b3e3ee4cbd7fd43
  pageDirectory: concepts
  sources:
    - guardrails-ai-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - toxiclanguage-scorer
  citations:
    - file: guardrails-ai-scorers-databricks-on-aws.md
title: ToxicLanguage Scorer
description: A Guardrails AI scorer for toxicity detection in LLM outputs, configurable with threshold and validation method parameters.
tags:
  - scorer
  - safety
  - toxicity-detection
  - guardrails
timestamp: "2026-06-19T19:02:52.440Z"
---

# ToxicLanguage scorer

The **ToxicLanguage scorer** is a rule-based evaluation component from the [Guardrails AI](/concepts/guardrails-ai-framework.md) framework that detects toxic or harmful language in LLM outputs. MLflow integrates with Guardrails AI so that this validator can be used as a scorer without requiring additional LLM calls. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Overview

The ToxicLanguage scorer validates the safety of generated text by classifying whether it contains toxic content. It is one of several available Guardrails AI scorers that also include [DetectPII](/concepts/detectpii-scorer.md) and [DetectJailbreak](/concepts/detectjailbreak-scorer.md) for safety and content quality validation. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Requirements

To use the ToxicLanguage scorer, install the `guardrails-ai` package: ^[guardrails-ai-scorers-databricks-on-aws.md]

```python
%pip install guardrails-ai
```

## Usage

### Direct invocation

Import the scorer and call it directly with an output string to receive a feedback object with a `value` of `"yes"` or `"no"`: ^[guardrails-ai-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.guardrails import ToxicLanguage

scorer = ToxicLanguage(threshold=0.7)
feedback = scorer(
    outputs="This is a professional and helpful response.",
)
print(feedback.value)  # "yes" or "no"
```

### Use with `mlflow.genai.evaluate()`

Pass the scorer in the `scorers` list of `mlflow.genai.evaluate()` to evaluate multiple outputs in a dataset: ^[guardrails-ai-scorers-databricks-on-aws.md]

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

### Dynamic creation by name

Use `get_scorer()` to create the scorer dynamically by passing the validator name as a string: ^[guardrails-ai-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.guardrails import get_scorer

scorer = get_scorer(
    validator_name="ToxicLanguage",
    threshold=0.7,
)
feedback = scorer(outputs="This is a professional response.")
```

## Configuration

The ToxicLanguage scorer accepts validator-specific parameters as keyword arguments to its constructor. The following parameters are shown in the source: ^[guardrails-ai-scorers-databricks-on-aws.md]

| Parameter | Description |
|-----------|-------------|
| `threshold` | A float (e.g., `0.7`) that sets the sensitivity for toxicity detection. |
| `validation_method` | A string (e.g., `"sentence"`) that controls how validation is applied (e.g., per-sentence). |

For additional validators and parameter details, refer to the [Guardrails AI documentation](https://www.guardrailsai.com/) and the [Guardrails Hub](https://guardrailsai.com/hub). ^[guardrails-ai-scorers-databricks-on-aws.md]

## Related Concepts

- [Guardrails AI](/concepts/guardrails-ai-framework.md) — The framework providing this and other validators.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation API that integrates Guardrails scorers.
- [DetectPII](/concepts/detectpii-scorer.md) — A companion scorer for personally identifiable information detection.
- [DetectJailbreak](/concepts/detectjailbreak-scorer.md) — A companion scorer for jailbreak attempt detection.

## Sources

- guardrails-ai-scorers-databricks-on-aws.md

# Citations

1. [guardrails-ai-scorers-databricks-on-aws.md](/references/guardrails-ai-scorers-databricks-on-aws-14c3c865.md)
