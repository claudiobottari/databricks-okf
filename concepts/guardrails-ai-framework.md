---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a87b2095ec489fb1b61fea0ef96e212fb1f56650bb6b0a7515d09533933c98c9
  pageDirectory: concepts
  sources:
    - guardrails-ai-scorers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - guardrails-ai-framework
    - GAF
    - Guardrails
    - Guardrails AI
  citations:
    - file: guardrails-ai-scorers-databricks-on-aws.md
title: Guardrails AI Framework
description: A community-driven framework for validating LLM outputs using a hub of validators for safety, PII detection, content quality, and more.
tags:
  - llm-validation
  - framework
  - ai-safety
timestamp: "2026-06-19T19:02:33.228Z"
---

---

title: Guardrails AI Framework
summary: A framework for validating LLM outputs using community-driven validators for safety, PII detection, and content quality
sources:
  - guardrails-ai-scorers-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:46:45.337Z"
updatedAt: "2026-06-19T10:46:45.337Z"
tags:
  - llm-validation
  - guardrails
  - safety
aliases:
  - guardrails-ai-framework
  - GAF
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0

---

# Guardrails AI Framework

**Guardrails AI** is a framework for validating outputs from large language models (LLMs) using a community-driven hub of pre-built validators. It is designed to help developers deploy safe, reliable, and high-quality LLM-based applications by providing rule-based checks that do not require additional LLM calls. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Overview

Guardrails AI provides a collection of validators that cover common LLM output concerns, including:

- **Safety** – Detecting toxic language, hate speech, or harmful content.
- **PII (Personally Identifiable Information)** – Identifying sensitive data such as credit card numbers, social security numbers, or email addresses.
- **Content quality** – Evaluating response quality, relevance, and tone.
- **Jailbreak detection** – Identifying attempts to bypass content safety guidelines.

The framework is designed to be used as a rule-based evaluation layer, running checks on the output of an LLM without needing to invoke another model. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Integration with MLflow

[MLflow GenAI](/concepts/mlflow-3-for-genai.md) integrates with Guardrails AI so that Guardrails validators can be used directly as [[scorers]] (evaluation functions) within the MLflow ecosystem. This integration allows developers to:

- Apply Guardrails validators to LLM outputs during [evaluation](/concepts/evaluation-run.md).
- Use the same `mlflow.genai.evaluate()` API that MLflow provides for other scorers.
- Pass validator-specific parameters (e.g., threshold, validation method) as keyword arguments to the constructor.

Available integrated scorers include `ToxicLanguage`, `DetectPII`, and `DetectJailbreak`. ^[guardrails-ai-scorers-databricks-on-aws.md]

### Example: Using Guardrails scorers with MLflow

```python
import mlflow
from mlflow.genai.scorers.guardrails import ToxicLanguage, DetectPII

scorer = ToxicLanguage(threshold=0.7)
feedback = scorer(
    outputs="This is a professional and helpful response."
)
print(feedback.value)  # "yes" or "no"
```

Using within an `mlflow.genai.evaluate()` call: ^[guardrails-ai-scorers-databricks-on-aws.md]

```python
results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        ToxicLanguage(threshold=0.7),
        DetectPII(),
    ],
)
```

## Creating a Scorer by Name

Validators can be dynamically selected by name using the `get_scorer` function: ^[guardrails-ai-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.guardrails import get_scorer

scorer = get_scorer(
    validator_name="ToxicLanguage",
    threshold=0.7,
)
```

## Configuration

Guardrails AI scorers accept validator-specific parameters as keyword arguments. For example: ^[guardrails-ai-scorers-databricks-on-aws.md]

- **Toxicity detection** – `threshold` (sensitivity), `validation_method` (e.g., `"sentence"`).
- **PII detection** – `pii_entities` (list of entity types such as `CREDIT_CARD`, `SSN`).
- **Jailbreak detection** – `threshold` (custom sensitivity level).

For a complete list of parameters and available validators, reference the [Guardrails AI documentation](/concepts/guardrails-ai-scorers-integration.md) and the Guardrails Hub. ^[guardrails-ai-scorers-databricks-on-aws.md]

## Why use Guardrails AI with MLflow

- **No extra LLM calls.** Guardrails validators are rule-based, so they do not require any additional model invocations, reducing cost and latency. ^[guardrails-ai-scorers-databricks-on-aws.md]
- **Community-driven.** Validators are continuously contributed to and updated by the open-source community.
- **Easy integration.** The `mlflow.genai.scorers.guardrails` module provides direct access to the same evaluation API used for [Custom Judges](/concepts/custom-judges.md) and model-based scorers.

## Requirements

To use Guardrails AI with MLflow, install the `guardrails-ai` package: ^[guardrails-ai-scorers-databricks-on-aws.md]

```
%pip install guardrails-ai
```

## Related Concepts

- LLM safety evaluation
- PII detection and redaction
- Content quality assessment
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md)
- Community validators

## Sources

- guardrails-ai-scorers-databricks-on-aws.md

# Citations

1. [guardrails-ai-scorers-databricks-on-aws.md](/references/guardrails-ai-scorers-databricks-on-aws-14c3c865.md)
