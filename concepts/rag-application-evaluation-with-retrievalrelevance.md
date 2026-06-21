---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6ea4d98f20438929071935c8b9b0d86cbab393a50e5c7471baff5c0bc52c9f0
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rag-application-evaluation-with-retrievalrelevance
    - RAEWR
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: RAG Application Evaluation with RetrievalRelevance
description: A pattern for evaluating Retrieval-Augmented Generation applications by annotating a retriever function with @mlflow.trace(span_type='RETRIEVER') and passing RetrievalRelevance as a scorer to mlflow.genai.evaluate.
tags:
  - rag
  - mlflow
  - llm-evaluation
  - genai
timestamp: "2026-06-18T10:46:38.491Z"
---

# RAG Application Evaluation with RetrievalRelevance

**RetrievalRelevance** is a built-in LLM judge in MLflow that evaluates whether each document returned by a RAG application's retriever is relevant to the user's input request. It helps diagnose quality issues in retrieval-augmented generation (RAG) pipelines—if the retrieved context is not relevant, the generation step cannot produce a helpful response. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Overview

RetrievalRelevance is one of two built-in relevance judges provided by MLflow, alongside [RelevanceToQuery](/concepts/relevancetoquery.md), which evaluates whether a response directly addresses the user's input. Together, these judges help pinpoint the source of quality problems in RAG applications. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Prerequisites

Before using RetrievalRelevance, set up your environment:

1. Install MLflow and required packages:
   ```python
   %pip install --upgrade "mlflow[databricks]>=3.4.0" openai "databricks-connect>=16.1"
   dbutils.library.restartPython()
   ```
2. Create an MLflow experiment by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment). ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Requirements

RetrievalRelevance requires the MLflow Trace to contain at least one span with `span_type` set to `RETRIEVER`. This span type is automatically recognized when you annotate your retriever function with the appropriate [MLflow Tracing](/concepts/mlflow-tracing.md) decorator. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Using RetrievalRelevance

### Direct invocation

You can assess individual traces by retrieving them and passing them to the `retrieval_relevance` function:

```python
from mlflow.genai.scorers import retrieval_relevance
import mlflow

# Get a trace from a previous run
trace = mlflow.get_trace("<your-trace-id>")

# Assess if each retrieved document is relevant
feedbacks = retrieval_relevance(trace=trace)
print(feedbacks)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Evaluation on a dataset

For running full evaluation on a dataset, pass `RetrievalRelevance` to `mlflow.genai.evaluate`:

```python
import mlflow
from mlflow.genai.scorers import RetrievalRelevance
from mlflow.entities import Document
from typing import List

# Define a retriever function with proper span type
@mlflow.trace(span_type="RETRIEVER")
def retrieve_docs(query: str) -> List[Document]:
    # Simulated retrieval - in practice, this would query a vector database
    if "capital" in query.lower() and "france" in query.lower():
        return [
            Document(
                id="doc_1",
                page_content="Paris is the capital of France.",
                metadata={"source": "geography.txt"}
            ),
            Document(
                id="doc_2",
                page_content="The Eiffel Tower is located in Paris.",
                metadata={"source": "landmarks.txt"}
            )
        ]
    else:
        return [
            Document(
                id="doc_3",
                page_content="Python is a programming language.",
                metadata={"source": "tech.txt"}
            )
        ]

# Define your app that uses the retriever
@mlflow.trace
def rag_app(query: str):
    docs = retrieve_docs(query)
    return {"response": f"Found {len(docs)} relevant documents."}

# Create evaluation dataset
eval_dataset = [
    {"inputs": {"query": "What is the capital of France?"}},
    {"inputs": {"query": "How do I use Python?"}}
]

# Run evaluation with RetrievalRelevance scorer
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[
        RetrievalRelevance(
            model="databricks:/databricks-gpt-oss-120b",  # Optional
        )
    ]
)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Configuring the Judge Model

By default, RetrievalRelevance uses a Databricks-hosted LLM designed for GenAI quality assessments. You can change the judge model using the `model` argument. The model must be specified in the format `<provider>:/<model-name>`, where `<provider>` is a LiteLLM-compatible model provider. If you use `databricks` as the model provider, the model name is the same as the serving endpoint name. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RetrievalRelevance

# Use a different judge model
retrieval_judge = RetrievalRelevance(
    model="databricks:/databricks-claude-opus-4-5"
)
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Interpreting Results

The judge returns a `Feedback` object with the following fields: ^[answer-and-context-relevance-judges-databricks-on-aws.md]

- **`value`**: `"yes"` if the context is relevant to the query, `"no"` if not
- **`rationale`**: An explanation of why the judge found the context relevant or irrelevant

## Diagnostic Value

RetrievalRelevance helps distinguish between retrieval failures and generation failures in RAG pipelines. If multiple retrieved documents score low on relevance, the retrieval logic likely needs improvement before addressing generation quality. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related Concepts

- [RelevanceToQuery](/concepts/relevancetoquery.md) — The companion judge that evaluates response relevance to the user's query
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — MLflow's framework for evaluating generative AI applications
- RAG Application — Retrieval-augmented generation architectures
- [LLM Judges](/concepts/llm-judges.md) — MLflow's system of built-in and custom evaluation judges
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing system that captures span information needed by RetrievalRelevance

## Next Steps

- Explore other built-in judges for groundedness, safety, and correctness
- Create custom judges for specialized evaluation use cases
- Evaluate complete RAG applications with comprehensive scoring

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
