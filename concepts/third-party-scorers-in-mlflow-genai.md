---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c76513047a10ab8d6be2a282f8f58fc2afff73b489e8c1ecee65b5c7aafc536
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - third-party-scorers-in-mlflow-genai
    - TSIMG
    - Third-Party Scorers
    - Third-party Scorers
    - Third-party scorers
  citations:
    - file: arize-phoenix-scorers-databricks-on-aws.md
title: Third-Party Scorers in MLflow GenAI
description: MLflow's extensibility mechanism allowing third-party evaluation scorers (like Arize Phoenix) to be used in GenAI evaluations
tags:
  - mlflow
  - extensibility
  - llm-evaluation
timestamp: "2026-06-19T22:08:22.016Z"
---

# Third-Party Scorers in MLflow GenAI

**Third-Party Scorers in MLflow GenAI** refers to the integration of evaluation metrics from external libraries—such as Arize Phoenix—into the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation framework. These scorers allow users to assess model outputs using specialized, community-maintained evaluation criteria without leaving the MLflow ecosystem.

## Overview

MLflow GenAI provides a pluggable scoring system that supports third-party scorers alongside built-in metrics. Third-party scorers are imported from external packages and used as arguments to `mlflow.genai.evaluate()`, enabling custom evaluation logic for [LLM evaluation](/concepts/llm-as-a-judge-evaluation.md) and [agent evaluation](/concepts/mlflow-agent-evaluation.md) workflows. ^[arize-phoenix-scorers-databricks-on-aws.md]

## Supported Third-Party Scorers

### Arize Phoenix Scorers

The Arize Phoenix library provides scorers for evaluating hallucination and relevance in LLM outputs. These scorers require a model endpoint for scoring, typically specified using the `databricks:/` URI format to reference a Databricks serving endpoint. ^[arize-phoenix-scorers-databricks-on-aws.md]

Available scorers include:

- **Hallucination** – Evaluates whether the model output contains information not supported by the provided context.
- **Relevance** – Assesses how relevant the model output is to the given query and context.

## Usage

Third-party scorers are imported from their respective packages and passed as a list to the `scorers` parameter of `mlflow.genai.evaluate()`. Each scorer is instantiated with a `model` argument that specifies the scoring model endpoint. ^[arize-phoenix-scorers-databricks-on-aws.md]

### Example: Arize Phoenix Scorers

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

## Dataset Structure

When using third-party scorers that require context (such as hallucination and relevance evaluation), the evaluation dataset should include an `expectations` field containing a `context` key. This context provides the reference information against which the model output is evaluated. ^[arize-phoenix-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The evaluation framework for generative AI models.
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md) – General concepts for evaluating large language models.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – Evaluation of AI agent systems.
- Built-in Scorers in MLflow – Native evaluation metrics provided by MLflow.
- [Databricks Model Serving](/concepts/databricks-model-serving.md) – Endpoints used as scoring models for third-party scorers.

## Sources

- arize-phoenix-scorers-databricks-on-aws.md

# Citations

1. [arize-phoenix-scorers-databricks-on-aws.md](/references/arize-phoenix-scorers-databricks-on-aws-53f4b817.md)
