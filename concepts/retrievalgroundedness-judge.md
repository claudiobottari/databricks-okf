---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4b523b47cff6aa3dd5660075c947949f5c7ade41f7d6ad42113f084fb0080724
  pageDirectory: concepts
  sources:
    - retrievalgroundedness-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - retrievalgroundedness-judge
    - Groundedness LLM Judge
    - Groundedness judge
  citations:
    - file: retrievalgroundedness-judge-databricks-on-aws.md
title: RetrievalGroundedness judge
description: An MLflow GenAI judge that evaluates whether a generated response is factually grounded in the retrieved context documents, detecting hallucination in RAG applications.
tags:
  - mlflow
  - rag
  - evaluation
  - groundedness
timestamp: "2026-06-19T20:14:53.591Z"
---

# RetrievalGroundedness judge

The **RetrievalGroundedness judge** is an [MLflow GenAI](/concepts/mlflow-3-for-genai.md) scorer that evaluates whether a model’s response is factually supported by the documents retrieved from a knowledge base. It is designed for use in [retrieval-augmented generation](/concepts/retrieval-augmented-generation-rag.md) (RAG) pipelines to quantify how grounded the generated answer is in the provided context. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Overview

The judge checks if each claim in the response can be traced to a specific piece of evidence in the retrieved documents. By default, the judge uses a custom Databricks-hosted model (`databricks:/databricks-gpt-oss-120b`) as the underlying evaluator, but users can supply a different model. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Usage

The `RetrievalGroundedness` scorer is imported from `mlflow.genai.scorers` and passed to the `scorers` argument of `mlflow.genai.evaluate()`. The evaluation expects a prediction function (`predict_fn`) that returns a dictionary containing a `"response"` key. The scorer is compatible with RAG applications that have a retriever decorated with `@mlflow.trace(span_type="RETRIEVER")` and a context-building step that joins document text. ^[retrievalgroundedness-judge-databricks-on-aws.md]

Example:

```python
from mlflow.genai.scorers import RetrievalGroundedness

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[
        RetrievalGroundedness(
            model="databricks:/databricks-gpt-oss-120b"
        )
    ]
)
```

## Configuration

The `RetrievalGroundedness` judge accepts an optional `model` parameter that specifies the evaluator LLM. If omitted, it defaults to the Databricks-hosted `databricks-gpt-oss-120b` model. Users can replace this with any model identifier that MLflow can route to, such as an OpenAI model (e.g., `gpt-4o`) when providing their own credentials. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – Framework that supports judges like RetrievalGroundedness.
- [LLM-as-judge](/concepts/llm-as-a-judge.md) – The paradigm of using an LLM to evaluate model outputs.
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) – The application pattern this judge is designed to assess.
- Groundedness metric – A broader category of evaluation metrics measuring factuality with respect to source material.

## Sources

- retrievalgroundedness-judge-databricks-on-aws.md

# Citations

1. [retrievalgroundedness-judge-databricks-on-aws.md](/references/retrievalgroundedness-judge-databricks-on-aws-595883b7.md)
