---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2bc1236db20b915a1d17d6c4ccf88fe369946ee2efb41a4c800cc3e7bbe5e1ed
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-foundation-model-api-pattern
    - DFMAP
  citations:
    - file: arize-phoenix-scorers-databricks-on-aws.md
title: Databricks Foundation Model API Pattern
description: The 'databricks:/model-name' URI pattern used to reference Databricks-hosted foundation models for LLM-as-a-judge scoring
tags:
  - databricks
  - model-serving
  - llm
timestamp: "2026-06-19T17:35:40.270Z"
---

# Databricks Foundation Model API Pattern

The **Databricks Foundation Model API Pattern** refers to the use of the `databricks:/` URI scheme when specifying model endpoints in Databricks MLflow APIs, particularly for model evaluation and scoring. This pattern allows users to reference models served by Databricks’ own Foundation Model API (such as `databricks-gpt-5-mini`) directly from MLflow functionality.

## Usage in MLflow GenAI Scorers

When using MLflow GenAI scorers like `Hallucination` or `Relevance`, the model argument can be set to a URI that follows the pattern `databricks:/<model-name>`. The source material demonstrates this with the model `databricks:/databricks-gpt-5-mini`. ^[arize-phoenix-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers.phoenix import Hallucination, Relevance

scorers = [
    Hallucination(model="databricks:/databricks-gpt-5-mini"),
    Relevance(model="databricks:/databricks-gpt-5-mini"),
]
```

This pattern tells MLflow to route inference requests to the Databricks-hosted Foundation Model API endpoint for the named model, rather than to an external or custom deployment.

## Context

The Foundation Model API is Databricks’ managed service for serving large language models (LLMs) and other foundation models. The `databricks:/` prefix is a shorthand that integrates seamlessly with MLflow’s evaluation and scoring infrastructure, enabling users to leverage Databricks’ hosted models without needing to configure custom endpoints.

Related concepts include [MLflow GenAI](/concepts/mlflow-3-for-genai.md), [Foundation Model API](/concepts/foundation-model-apis.md), and Model Evaluation on Databricks.

## Limitations

The provided source material does not describe the full specification of the `databricks:/` URI pattern, supported model names, authentication requirements, or cost implications. Users should consult the official Databricks documentation for complete details on the Foundation Model API.

## Sources

- arize-phoenix-scorers-databricks-on-aws.md

# Citations

1. [arize-phoenix-scorers-databricks-on-aws.md](/references/arize-phoenix-scorers-databricks-on-aws-53f4b817.md)
