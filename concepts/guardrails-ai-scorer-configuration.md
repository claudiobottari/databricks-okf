---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15241adc6768e1f5c1900732d69fa77a6d303de5d242a7b7ca398d457811f8fe
  pageDirectory: concepts
  sources:
    - guardrails-ai-scorers-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - guardrails-ai-scorer-configuration
    - GASC
  citations:
    - file: guardrails-ai-scorers-databricks-on-aws.md
title: Guardrails AI scorer configuration
description: Guardrails AI scorers accept validator-specific parameters as keyword arguments to the constructor for customization
tags:
  - configuration
  - scorer
  - customization
timestamp: "2026-06-19T10:47:02.819Z"
---

---

title: Guardrails AI scorer configuration
summary: Configuring Guardrails AI validators as MLflow scorers for rule-based evaluation of LLM outputs, including safety, PII detection, and content quality checks.
sources:
  - guardrails-ai-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - guardrails-ai
  - mlflow
  - evaluation
  - configuration
aliases:
  - guardrails-ai-scorer-configuration
  - GASC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0

---

# Guardrails AI scorer configuration

**Guardrails AI scorer configuration** refers to the process of instantiating and tuning [Guardrails AI](/concepts/guardrails-ai-framework.md) validators for use as scorers within [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation workflows. These scorers provide rule-based validation of LLM outputs — covering safety, Personally Identifiable Information (PII) detection, content quality, and more — without requiring additional LLM calls. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Requirements

To use Guardrails AI scorers, install the `guardrails-ai` Python package:

```python
%pip install guardrails-ai
```

^[guardrails-ai-scorers-databricks-on-aws.md]

## Creating a Guardrails AI scorer

You can create a scorer either by directly instantiating a predefined class or by dynamically loading a validator by name.

### Direct instantiation

Each supported validator is available as a class in the `mlflow.genai.scorers.guardrails` module. Pass validator-specific keyword arguments to the constructor. For example:

```python
from mlflow.genai.scorers.guardrails import ToxicLanguage, DetectPII

toxicity_scorer = ToxicLanguage(threshold=0.7)
pii_scorer = DetectPII(pii_entities=["CREDIT_CARD", "SSN", "EMAIL_ADDRESS"])
```

^[guardrails-ai-scorers-databricks-on-aws.md]

### Dynamic creation with `get_scorer`

Use `get_scorer()` to create a scorer by passing the validator name as a string. This is useful when the validator type is determined at runtime:

```python
from mlflow.genai.scorers.guardrails import get_scorer

scorer = get_scorer(
    validator_name="ToxicLanguage",
    threshold=0.7,
)
feedback = scorer(outputs="This is a professional response.")
```

^[guardrails-ai-scorers-databricks-on-aws.md]

## Configuration parameters

Guardrails AI scorers accept validator-specific parameters as keyword arguments to the constructor. The exact set of parameters depends on the validator; consult the Guardrails Hub for full details. Below are common parameters for several validators:

- **ToxicLanguage** – `threshold` (float, default 0.5, range 0–1), `validation_method` (e.g., `"sentence"`).
- **DetectPII** – `pii_entities` (list of strings, e.g., `["CREDIT_CARD", "SSN", "EMAIL_ADDRESS"]`).
- **DetectJailbreak** – `threshold` (float, default 0.5, range 0–1).

Example configuration:

```python
from mlflow.genai.scorers.guardrails import ToxicLanguage, DetectPII, DetectJailbreak

# Toxicity detection with custom threshold and sentence-level validation
scorer = ToxicLanguage(threshold=0.7, validation_method="sentence")

# PII detection with specific entity types
pii_scorer = DetectPII(pii_entities=["CREDIT_CARD", "SSN", "EMAIL_ADDRESS"])

# Jailbreak detection with higher sensitivity
jailbreak_scorer = DetectJailbreak(threshold=0.9)
```

^[guardrails-ai-scorers-databricks-on-aws.md]

## Using in evaluation

Pass one or more Guardrails AI scorers to `mlflow.genai.evaluate()` via the `scorers` parameter. Each scorer returns a `feedback` object that includes a `.value` attribute (e.g., `"yes"` or `"no"` for binary validators).

```python
import mlflow
from mlflow.genai.scorers.guardrails import ToxicLanguage, DetectPII

eval_dataset = [
    {"inputs": {"query": "What is MLflow?"}, "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs."},
    {"inputs": {"query": "How do I contact support?"}, "outputs": "You can reach us at support@example.com or call 555-0123."},
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

## Available scorers

MLflow ships with Guardrails AI scorers for safety and content quality, including:

- `ToxicLanguage` – Detects toxic or offensive language.
- `DetectPII` – Detects personally identifiable information.
- `DetectJailbreak` – Detects jailbreak attempts.

For additional validators, see the Guardrails Hub and the [Guardrails AI documentation](https://www.guardrailsai.com/). ^[guardrails-ai-scorers-databricks-on-aws.md]

## Related concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – Platform for evaluating and monitoring GenAI agents.
- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers for deeper quality analysis.
- Guardrails Hub – Community repository of Guardrails validators.
- Rule-based evaluation – Evaluation without LLM calls, as with Guardrails AI scorers.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying scorers to monitor live agent behavior.

## Sources

- guardrails-ai-scorers-databricks-on-aws.md

# Citations

1. [guardrails-ai-scorers-databricks-on-aws.md](/references/guardrails-ai-scorers-databricks-on-aws-14c3c865.md)
