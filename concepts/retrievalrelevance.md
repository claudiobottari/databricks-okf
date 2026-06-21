---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 65002d10e5ec91b6f95e6690a183214853ca2f03b793fc267d985b046453eb8f
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - retrievalrelevance
    - retrievalrelevance-judge
    - Retrieval Relevance Judge
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
title: RetrievalRelevance
description: An MLflow LLM judge that evaluates whether each document returned by a retriever is relevant to the user's input request, requiring RETRIEVER spans in traces
tags:
  - llm-judge
  - rag
  - retrieval
  - mlflow
timestamp: "2026-06-19T09:00:00.770Z"
---

# RetrievalRelevance

**RetrievalRelevance** is a built-in [LLM judge](/concepts/llm-judges.md) provided by [MLflow](/concepts/mlflow.md) that evaluates whether each document returned by a retriever in a GenAI application is relevant to the user's input request. It is designed specifically for [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) workflows and helps diagnose quality issues at the retrieval stage — if retrieved documents lack relevance, the generation step cannot produce a helpful response. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Overview

RetrievalRelevance assesses relevance at the document level: for each retrieved document in a trace, the judge returns a binary "yes" or "no" verdict along with a rationale explaining its reasoning. This allows developers to pinpoint which documents are unhelpful and debug retrieval quality before it affects the final answer. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

The judge works by analyzing MLflow [Traces](/concepts/traces.md) and requires that the trace contain at least one span with `span_type` set to `RETRIEVER`. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Usage

### Prerequisites

Install MLflow 3.4.0 or later with the Databricks extras:

```python
%pip install --upgrade "mlflow[databricks]>=3.4.0"
```

You also need an existing [MLflow Experiment](/concepts/mlflow-experiment.md) to log traces. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Invoking the Judge

You can use RetrievalRelevance in two ways:

1. **Direct invocation** on a previously captured trace:

```python
from mlflow.genai.scorers import retrieval_relevance
import mlflow

trace = mlflow.get_trace("<your-trace-id>")
feedbacks = retrieval_relevance(trace=trace)
print(feedbacks)
```

Each element in the returned list corresponds to a retrieved document and contains a `Feedback` object with `value` ("yes"/"no") and `rationale`. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

2. **Inside `mlflow.genai.evaluate()`** for batch evaluation:

```python
import mlflow
from mlflow.genai.scorers import RetrievalRelevance

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=rag_app,
    scorers=[
        RetrievalRelevance(
            model="databricks:/databricks-gpt-oss-120b"  # Optional override
        )
    ]
)
```

When used with `evaluate()`, the judge automatically extracts traces from the predictions and scores each retriever span. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Creating a RAG Application with Retriever Traces

To use RetrievalRelevance, your retriever function must be decorated with `@mlflow.trace(span_type="RETRIEVER")` so that MLflow captures the retriever span correctly: ^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
from mlflow.entities import Document
from typing import List

@mlflow.trace(span_type="RETRIEVER")
def retrieve_docs(query: str) -> List[Document]:
    # In practice, query a vector database
    return [Document(id="doc_1", page_content="Paris is the capital of France.")]
```

## Judge Model Selection

By default, RetrievalRelevance uses a [Databricks-hosted LLM](/concepts/databricks-hosted-llms.md) designed for GenAI quality assessments. You can override the model by passing the `model` argument with a LiteLLM-compatible provider string: ^[answer-and-context-relevance-judges-databricks-on-aws.md]

```python
from mlflow.genai.scorers import RetrievalRelevance

retrieval_judge = RetrievalRelevance(
    model="databricks:/databricks-claude-opus-4-5"
)
```

## Interpreting Results

The judge returns a `Feedback` object for each document with:

- **`value`**: `"yes"` if the document is relevant to the input request, `"no"` if not.
- **`rationale`**: A natural language explanation of the judge's decision.

By analyzing these results, you can identify which retrieved documents are unhelpful and adjust your retrieval strategy or chunking strategy accordingly. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Relationship to Other Relevance Judges

RetrievalRelevance is one of two built-in relevance judges in MLflow:

- **`RetrievalRelevance`**: Evaluates document-level relevance — whether each retrieved document pertains to the user's request.
- **[RelevanceToQuery](/concepts/relevancetoquery.md)**: Evaluates response-level relevance — whether the final generated answer addresses the user's input.

These judges work together to diagnose quality issues: if retrieval is poor, the generation step cannot produce a helpful response. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

## Related Concepts

- [LLM Judges](/concepts/llm-judges.md) — AI-based evaluators for GenAI quality
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — Architecture where retrieval relevance is critical
- [[MLflow Trace|MLflow Traces]] — The execution traces that RetrievalRelevance analyzes
- [Retriever](/concepts/retriever-spans.md) — The component whose documents are evaluated
- [RelevanceToQuery](/concepts/relevancetoquery.md) — The companion judge for response-level relevance
- [Custom Judges](/concepts/custom-judges.md) — Build your own evaluation criteria with make_judge()|make_judge
- [Evaluation metrics](/concepts/gluonts-evaluator.md) — Broader set of GenAI quality metrics

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
