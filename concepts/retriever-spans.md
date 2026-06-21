---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9da8dc613fc16a0b418acee938f7653b9f97edc4fbc97fdadd8fe7f3d39ba64
  pageDirectory: concepts
  sources:
    - span-tracing-with-context-managers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - retriever-spans
    - RETRIEVER Span
    - RETRIEVER span
    - Retriever
    - SpanType.RETRIEVER
  citations:
    - file: span-tracing-with-context-managers-databricks-on-aws.md
title: RETRIEVER Spans
description: Specialized MLflow span type for document retrieval operations that must output a list of Document objects with page_content, metadata, and optional ID fields.
tags:
  - mlflow
  - tracing
  - retrieval
  - RAG
timestamp: "2026-06-19T23:05:45.416Z"
---

# RETRIEVER Spans

**RETRIEVER Spans** are a specialized span type in [MLflow Tracing](/concepts/mlflow-tracing.md) used to capture and represent document retrieval operations within a traced application. They are designed specifically for recording interactions with a data store, such as a vector database, search engine, or knowledge base, where documents are fetched in response to a query.

## Overview

RETRIEVER spans are defined using the `SpanType.RETRIEVER` enumeration from the `mlflow.entities` module. They are one of several span types available in [MLflow](/concepts/mlflow.md)'s tracing framework, which also includes types like `CHAIN`, `LLM`, `AGENT`, `TOOL`, and `EMBEDDING`. ^[span-tracing-with-context-managers-databricks-on-aws.md]

The defining characteristic of RETRIEVER spans is that they must output a list of `Document` objects. This requirement ensures that the span's output is structured in a way that enables proper rendering in the [MLflow](/concepts/mlflow.md) UI and allows downstream tools to parse and analyze retrieved content. ^[span-tracing-with-context-managers-databricks-on-aws.md]

## Creating RETRIEVER Spans

RETRIEVER spans can be created using either the mlflow.start_span() Context Manager|span tracing with context managers|`mlflow.start_span()` context manager or the `@mlflow.trace` function decorator. When using the decorator approach, set the `span_type` parameter to `SpanType.RETRIEVER`. ^[span-tracing-with-context-managers-databricks-on-aws.md]

### Required Output Format

The span's output must be set to a list of `Document` objects. Each `Document` has the following attributes:

- `page_content` (str): The textual content of the document.
- `metadata` (dict, optional): A dictionary containing metadata such as:
  - `doc_uri`: The URI or path to the source document.
  - `chunk_id`: An identifier for the specific chunk or section.
  - `relevance_score`: A numerical score indicating relevance to the query.
  - `source`: The name of the knowledge base or data store.
- `id` (str, optional): An optional unique identifier for the document.

^[span-tracing-with-context-managers-databricks-on-aws.md]

### Example

The following example demonstrates creating a RETRIEVER span using the function decorator approach:

```python
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].entities import Document, SpanType

@mlflow.trace(span_type=SpanType.RETRIEVER)
def retrieve_documents(query: str):
    span = [[mlflow|MLflow]].get_current_active_span()

    # Create Document objects (required for RETRIEVER spans)
    documents = [
        Document(
            page_content="The content of the document...",
            metadata={
                "doc_uri": "path/to/document.md",
                "chunk_id": "chunk_001",
                "relevance_score": 0.95,
                "source": "knowledge_base"
            },
            id="doc_123"  # Optional document ID
        ),
        Document(
            page_content="Another relevant section...",
            metadata={
                "doc_uri": "path/to/other.md",
                "chunk_id": "chunk_042",
                "relevance_score": 0.87
            }
        )
    ]

    # Set outputs as Document objects for proper UI rendering
    span.set_outputs(documents)

    # Return in your preferred format
    return [doc.to_dict() for doc in documents]

retrieve_documents(query="What is ML?")
```

^[span-tracing-with-context-managers-databricks-on-aws.md]

## Accessing RETRIEVER Span Outputs

After a trace is completed, you can query the RETRIEVER span's outputs using the trace API. The following pattern shows how to access the retrieved documents:

```python
last_trace_id = [[mlflow|MLflow]].get_last_active_trace_id()
trace = [[mlflow|MLflow]].get_trace(last_trace_id)

retriever_span = trace.search_spans(span_type=SpanType.RETRIEVER)[0]

if retriever_span.outputs:
    for doc in retriever_span.outputs:
        if isinstance(doc, dict):
            content = doc.get('page_content', '')
            uri = doc.get('metadata', {}).get('doc_uri', '')
            score = doc.get('metadata', {}).get('relevance_score', 0)
            print(f"Document from {uri} (score: {score})")
```

^[span-tracing-with-context-managers-databricks-on-aws.md]

## Use Cases

RETRIEVER spans are most commonly used in [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) applications, where a retrieval step is followed by a generation step. In such architectures, the RETRIEVER span captures:

- The query sent to the data store.
- The documents retrieved, including their content and metadata.
- The relevance scores or other ranking information.
- The source URIs for attribution and provenance tracking.

They can also be used in search applications, question-answering systems, and any workflow where document retrieval is a distinct, traceable operation.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall tracing framework for instrumenting GenAI applications.
- Span Types — The taxonomy of span types including LLM, CHAIN, AGENT, TOOL, EMBEDDING, and RETRIEVER.
- mlflow.start_span() Context Manager|Span Tracing with Context Managers — Using `mlflow.start_span()` for more granular tracing.
- [Function Decorators](/concepts/mlflowtrace-function-decorator.md) — The simpler approach for tracing entire functions with `@mlflow.trace`.
- Document Entity — The `mlflow.entities.Document` class used as the output format.
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — The primary architecture where RETRIEVER spans are applied.
- Trace API — Methods for querying and analyzing logged [Traces](/concepts/traces.md).

## Sources

- span-tracing-with-context-managers-databricks-on-aws.md

# Citations

1. [span-tracing-with-context-managers-databricks-on-aws.md](/references/span-tracing-with-context-managers-databricks-on-aws-d67ed6d9.md)
