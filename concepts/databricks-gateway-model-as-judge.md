---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c81eb022f14b4e86ede2a7c85052a35bdc755803d1ed51754b8dd6f75a071f14
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-gateway-model-as-judge
    - DGMAJ
  citations:
    - file: arize-phoenix-scorers-databricks-on-aws.md
title: Databricks Gateway Model as Judge
description: Using Databricks-hosted LLM models (e.g., databricks-gpt-5-mini) as the evaluator model for scoring LLM outputs
tags:
  - databricks
  - llm-evaluation
  - llm-as-judge
timestamp: "2026-06-18T10:48:23.440Z"
---

# Databricks Gateway Model as Judge

**Databricks Gateway Model as Judge** refers to the practice of using a model served through Databricks Gateway (e.g., a Databricks-hosted foundation model endpoint) as the evaluator model in MLflow GenAI evaluation, particularly with third-party scorers like those from Arize Phoenix. In this pattern, the gateway model acts as an LLM judge that scores model outputs against criteria such as hallucination or relevance.^[arize-phoenix-scorers-databricks-on-aws.md]

## Overview

MLflow GenAI evaluation supports pluggable scorers that use an LLM to compute scores. When the scorer is configured with a model identifier pointing to a Databricks Gateway endpoint (e.g., `"databricks:/databricks-gpt-5-mini"`), the scorer routes evaluation requests through the gateway, leveraging its serving infrastructure and access controls. This enables organizations to use a single, centrally governed model as the judge across multiple evaluation tasks.^[arize-phoenix-scorers-databricks-on-aws.md]

## Usage with MLflow GenAI Evaluate

The `mlflow.genai.evaluate` API accepts a list of scorers. Phoenix scorers such as `Hallucination` and `Relevance` accept a `model` argument that specifies the gateway endpoint. By passing `model="databricks:/<gateway-endpoint>"`, the scorer sends prompts to that gateway model to obtain judgments.^[arize-phoenix-scorers-databricks-on-aws.md]

### Example

The following example uses `Hallucination` and `Relevance` scorers with the gateway model `databricks-gpt-5-mini`:

```python
import mlflow
from mlflow.genai.scorers.phoenix import Hallucination, Relevance

eval_dataset = [
    {
        "inputs": {"query": "What is MLflow?"},
        "outputs": "MLflow is an open-source AI engineering platform for agents and LLMs.",
        "expectations": {
            "context": "MLflow is an ML platform for experiment tracking and model deployment."
        },
    },
    {
        "inputs": {"query": "How do I track experiments?"},
        "outputs": "You can use mlflow.start_run() to begin tracking experiments.",
        "expectations": {
            "context": "MLflow provides APIs like mlflow.start_run() for experiment tracking."
        },
    },
]

results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        Hallucination(model="databricks:/databricks-gpt-5-mini"),
        Relevance(model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

^[arize-phoenix-scorers-databricks-on-aws.md]

Each scorer uses the specified gateway model to assess the outputs. The `Hallucination` scorer checks whether the output contradicts the provided context. The `Relevance` scorer measures how well the output addresses the input query. Both rely on the gateway model's judgment.^[arize-phoenix-scorers-databricks-on-aws.md]

## Advantages

- **Centralized governance**: All evaluation traffic flows through the same gateway endpoint, simplifying access control and monitoring.^[arize-phoenix-scorers-databricks-on-aws.md]
- **Consistency**: Using the same judge model across different evaluation runs reduces variability in scoring due to model changes.^[arize-phoenix-scorers-databricks-on-aws.md]
- **Integration with MLflow**: The pattern works seamlessly with `mlflow.genai.evaluate`, which can automatically log evaluation results to [MLflow Tracking](/concepts/mlflow-tracking.md) for audit and analysis.^[arize-phoenix-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The framework that supports LLM-based scorers.
- Databricks Gateway – The serving infrastructure that hosts foundation models as endpoints.
- Arize Phoenix – The library providing `Hallucination`, `Relevance`, and other scorers.
- [LLM-as-judge](/concepts/llm-as-a-judge.md) – The general technique of using a language model to evaluate outputs.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Databricks-hosted model endpoints that can be used as judge models.

## Sources

- arize-phoenix-scorers-databricks-on-aws.md

# Citations

1. [arize-phoenix-scorers-databricks-on-aws.md](/references/arize-phoenix-scorers-databricks-on-aws-53f4b817.md)
