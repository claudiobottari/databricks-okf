---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd4f9270241957caeddf0c10a3151d556cd9a868eda315d588e91d58f777cba3
  pageDirectory: concepts
  sources:
    - retrievalsufficiency-judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-span-for-retrieval
    - MTSFR
  citations:
    - file: retrievalsufficiency-judge-databricks-on-aws.md
title: MLflow Trace Span for Retrieval
description: A pattern using @mlflow.trace(span_type='RETRIEVER') to instrument and trace document retrieval functions for observability during RAG evaluation.
tags:
  - mlflow
  - tracing
  - observability
  - rag
timestamp: "2026-06-19T20:15:29.875Z"
---

# MLflow Trace Span for Retrieval

**MLflow Trace Span for Retrieval** is a specialized tracing mechanism in [MLflow](/concepts/mlflow.md) that enables instrumenting retrieval operations within a [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) pipeline. By annotating functions with the `@mlflow.trace` decorator and specifying the `span_type="RETRIEVER"` parameter, developers can create dedicated trace spans that capture and log retrieval-related operations for monitoring, debugging, and evaluation purposes. ^[retrievalsufficiency-judge-databricks-on-aws.md]

## Overview

In RAG applications, the retrieval step involves fetching relevant documents from a knowledge base or vector store based on a user's query. MLflow Trace Span for Retrieval allows developers to wrap this retrieval logic in a traceable span that automatically captures inputs, outputs, metadata, and performance metrics. This instrumentation is particularly useful for [MLflow Tracing](/concepts/mlflow-tracing.md) workflows where understanding the quality and behavior of the retrieval component is critical. ^[retrievalsufficiency-judge-databricks-on-aws.md]

## Span Type: `RETRIEVER`

When defining a retrieval function, the `span_type` parameter is set to `"RETRIEVER"` to indicate that the span represents a retrieval operation. This type classification enables MLflow to properly associate the span with retrieval-specific evaluation tools and scoring mechanisms, such as the [RetrievalSufficiency Judge](/concepts/retrievalsufficiency-judge.md). ^[retrievalsufficiency-judge-databricks-on-aws.md]

## Implementation

To create a retrieval trace span, decorate a retrieval function with `@mlflow.trace(span_type="RETRIEVER")`. The function should accept a query string and return a list of [MLflow Document](/concepts/mlflow-document-entity.md) objects, each containing the retrieved content and associated metadata. ^[retrievalsufficiency-judge-databricks-on-aws.md]

### Example

```python
from mlflow.entities import Document
from typing import List

@mlflow.trace(span_type="RETRIEVER")
def retrieve_docs(query: str) -> List[Document]:
    # Simulated retrieval logic
    if "capital of france" in query.lower():
        return [
            Document(
                id="doc_1",
                page_content="Paris is the capital of France.",
                metadata={"source": "geography.txt"}
            ),
            Document(
                id="doc_2",
                page_content="France is a country in Western Europe.",
                metadata={"source": "countries.txt"}
            )
        ]
    elif "mlflow components" in query.lower():
        return [
            Document(
                id="doc_3",
                page_content="MLflow has multiple components including Tracing and Evaluation.",
                metadata={"source": "mlflow_intro.txt"}
            )
        ]
    else:
        return [
            Document(
                id="doc_4",
                page_content="General information about data science.",
                metadata={"source": "ds_basics.txt"}
            )
        ]
```

^[retrievalsufficiency-judge-databricks-on-aws.md]

## Integration with RAG Evaluation

Once a retrieval function is instrumented with a trace span, it can be integrated into a full RAG application for evaluation. The traced retrieval span works with [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) to assess retrieval sufficiency, allowing developers to measure whether the retrieved context provides enough information to answer a query correctly. ^[retrievalsufficiency-judge-databricks-on-aws.md]

### Full RAG Pipeline Example

```python
@mlflow.trace
def rag_app(query: str):
    # Retrieve documents
    docs = retrieve_docs(query)
    context = "\n".join([doc.page_content for doc in docs])
    
    # Generate response
    messages = [
        {"role": "system", "content": f"Answer based on this context: {context}"},
        {"role": "user", "content": query}
    ]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )
    return {"response": response.choices[0].message.content}
```

^[retrievalsufficiency-judge-databricks-on-aws.md]

## Use with RetrievalSufficiency Scorer

The retrieval trace span enables the [RetrievalSufficiency](/concepts/retrievalsufficiency-judge.md) scorer to inspect the documents returned by the retrieval step and evaluate whether the context is sufficient to answer the question. This integration allows for automated assessment of retrieval quality as part of an [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) run. ^[retrievalsufficiency-judge-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader tracing framework for instrumenting AI applications.
- [MLflow Document](/concepts/mlflow-document-entity.md) — The data entity used to represent retrieved documents.
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — The architectural pattern that combines retrieval with generation.
- [RetrievalSufficiency Judge](/concepts/retrievalsufficiency-judge.md) — An evaluation judge that assesses whether retrieved context is sufficient.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework for generative AI applications.
- Trace Span Types — The classification system for different types of trace spans.

## Sources

- retrievalsufficiency-judge-databricks-on-aws.md

# Citations

1. [retrievalsufficiency-judge-databricks-on-aws.md](/references/retrievalsufficiency-judge-databricks-on-aws-ecbf8897.md)
