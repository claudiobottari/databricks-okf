---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48e36486d4f568ad128a31e387e1e20fd068e037d909ff07c0c3a475affad700
  pageDirectory: concepts
  sources:
    - retrievalgroundedness-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rag-evaluation-with-mlflow
    - REWM
    - Evaluation with MLflow
  citations:
    - file: retrievalgroundedness-judge-databricks-on-aws.md
title: RAG evaluation with MLflow
description: The practice of evaluating Retrieval-Augmented Generation pipelines using MLflow's evaluation tools, including defining retriever functions, constructing prompts with context, and scoring responses.
tags:
  - mlflow
  - rag
  - evaluation
timestamp: "2026-06-19T20:15:00.244Z"
---

# RAG Evaluation with MLflow

**RAG evaluation with MLflow** refers to the process of assessing the quality of [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications using MLflow's evaluation framework. MLflow provides built-in scorers, such as the [RetrievalGroundedness judge](/concepts/retrievalgroundedness-judge.md), that measure how well a RAG system's responses are supported by the retrieved context documents. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Overview

RAG applications combine a retrieval step—where relevant documents are fetched from a knowledge base—with a generation step, where a [Large Language Model (LLM)](/concepts/large-language-models-llms-on-databricks.md) produces a response based on the retrieved context. Evaluating these systems requires specialized metrics that go beyond general text quality, focusing on whether the generated answer is factually grounded in the provided documents. ^[retrievalgroundedness-judge-databricks-on-aws.md]

MLflow's evaluation framework supports RAG evaluation through custom scorers and built-in judges. The `RetrievalGroundedness` scorer is one such judge that evaluates whether the model's response is supported by the retrieved context. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Key Components

### Retrieval Function

A RAG evaluation requires a retriever function that fetches relevant documents for a given query. In MLflow, this function should be decorated with `@mlflow.trace(span_type="RETRIEVER")` to properly instrument the retrieval step for tracing and evaluation. The retriever returns a list of `Document` objects, each containing an `id`, `page_content`, and optional `metadata`. ^[retrievalgroundedness-judge-databricks-on-aws.md]

### RAG Application

The RAG application itself is typically defined as a traced function using `@mlflow.trace`. This function orchestrates the retrieval and generation steps: it calls the retriever to get relevant documents, constructs a prompt with the retrieved context, and sends it to an LLM to generate a response. ^[retrievalgroundedness-judge-databricks-on-aws.md]

### Evaluation Dataset

The evaluation dataset consists of input queries that the RAG system should answer. Each entry in the dataset contains an `inputs` dictionary with the query string. MLflow runs the RAG application on each query and then applies the scorers to evaluate the outputs. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Using the RetrievalGroundedness Scorer

The `RetrievalGroundedness` scorer from `mlflow.genai.scorers` evaluates whether the generated response is grounded in the retrieved context. It can be configured with a specific model for evaluation, or it defaults to a custom Databricks model. ^[retrievalgroundedness-judge-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RetrievalGroundedness

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[
        RetrievalGroundedness(
            model="databricks:/databricks-gpt-oss-120b",  # Optional
        )
    ]
)
```

The scorer automatically uses the documents retrieved during the RAG application's execution to assess groundedness. It does not require separate document inputs in the evaluation dataset. ^[retrievalgroundedness-judge-databricks-on-aws.md]

## Evaluation Workflow

1. **Define the retriever**: Create a function that returns relevant `Document` objects for a given query, decorated with `@mlflow.trace(span_type="RETRIEVER")`.
2. **Define the RAG app**: Create a traced function that calls the retriever, constructs a prompt with context, and generates a response using an LLM.
3. **Prepare the dataset**: Create a list of dictionaries with `inputs` containing the query.
4. **Run evaluation**: Call `mlflow.genai.evaluate()` with the dataset, the RAG function, and the desired scorers.
5. **Review results**: MLflow returns evaluation results including groundedness scores for each query.

## Related Concepts

- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md)
- [RetrievalGroundedness judge](/concepts/retrievalgroundedness-judge.md)
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- [LLM Evaluation Metrics](/concepts/llm-as-a-judge-evaluation-metrics.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Document Retrieval
- Groundedness in LLM Outputs

## Sources

- retrievalgroundedness-judge-databricks-on-aws.md

# Citations

1. [retrievalgroundedness-judge-databricks-on-aws.md](/references/retrievalgroundedness-judge-databricks-on-aws-595883b7.md)
