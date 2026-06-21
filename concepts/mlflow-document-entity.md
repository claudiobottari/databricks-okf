---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d6db1fbc82a5d1fa0f061dab12c687bbf9d15926af1dfe5389b58ca43df0479f
  pageDirectory: concepts
  sources:
    - retrievalsufficiency-judge-databricks-on-aws.md
    - span-concepts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-document-entity
    - MDE
    - MLflow Document
  citations:
    - file: span-concepts-databricks-on-aws.md
    - file: retrievalsufficiency-judge-databricks-on-aws.md
title: MLflow Document Entity
description: A data class in mlflow.entities representing a retrieved document with an id, page_content, and metadata dictionary.
tags:
  - mlflow
  - document
  - entities
timestamp: "2026-06-19T20:15:12.242Z"
---

# MLflow Document Entity

The **MLflow Document entity** (`mlflow.entities.Document`) is a structured data class used to represent a retrieved document chunk in the context of [MLflow Tracing](/concepts/mlflow-tracing.md) for GenAI applications. It is part of the [Trace data model](/concepts/tracedata.md) and is primarily used to define the output schema for [`RETRIEVER` spans](span-concepts-databricks-on-aws.md).

## Purpose

The Document entity provides a standardized way to record retrieval results so that MLflow can render them in the UI, unlock evaluation features, and maintain lineage tracking. When a span’s output is a list of `Document` objects, the trace captures the content, metadata, and unique identifier of each retrieved chunk. ^[span-concepts-databricks-on-aws.md]

## Schema

Each `Document` object has the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `page_content` | `str` | Text content of the retrieved document chunk |
| `metadata` | `Optional[Dict[str, Any]]` | Additional metadata, including `doc_uri` (the document source URI, e.g., a Unity Catalog volume path) and `chunk_id` (identifier if the chunk belongs to a larger document) |
| `id` | `Optional[str]` | Unique identifier for the document chunk |

^[span-concepts-databricks-on-aws.md]

## Usage in a `RETRIEVER` span

The `RETRIEVER` span type expects a fixed output schema: a list of dictionaries each containing `page_content`, `metadata`, and optionally `id`. The `Document` entity helps construct this output correctly. The typical workflow inside a `@mlflow.trace(span_type=SpanType.RETRIEVER)` function or a context manager is:

1. Retrieve raw documents from a data store.
2. Create a list of `Document` objects with the required fields.
3. Set the list as the span’s output using `span.set_outputs(outputs)`.

Example (from the official documentation):

```python
import mlflow
from mlflow.entities import SpanType, Document

@mlflow.trace(span_type=SpanType.RETRIEVER)
def retrieve_relevant_documents(query: str):
    docs = search_store(query)                     # returns (content, doc_uri) tuples
    span = mlflow.get_current_active_span()
    outputs = [
        Document(page_content=doc, metadata={"doc_uri": uri})
        for doc, uri in docs
    ]
    span.set_outputs(outputs)
    return docs
```

^[span-concepts-databricks-on-aws.md]

## Usage beyond tracing

The `Document` entity is also imported and used directly in evaluation scenarios. For example, when defining a custom retriever function for use with the [RetrievalSufficiency Judge](/concepts/retrievalsufficiency-judge.md), you create `Document` objects with explicit `id`, `page_content`, and `metadata` fields:

```python
from mlflow.entities import Document
from typing import List

@mlflow.trace(span_type="RETRIEVER")
def retrieve_docs(query: str) -> List[Document]:
    # ...
    return [
        Document(
            id="doc_1",
            page_content="Paris is the capital of France.",
            metadata={"source": "geography.txt"}
        ),
        # ...
    ]
```

^[retrievalsufficiency-judge-databricks-on-aws.md]

## Related concepts

- Span – The fundamental building block of a trace; a `RETRIEVER` span uses `Document` for its output.
- [SpanType.RETRIEVER](/concepts/retriever-spans.md) – The predefined span type for retrieval operations.
- [Trace](/concepts/traces.md) – The top-level data structure that contains a tree of spans.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The overall observability framework for GenAI applications.
- [RetrievalSufficiency Judge](/concepts/retrievalsufficiency-judge.md) – An evaluation scorer that relies on `Document` entities to assess whether retrieved context is sufficient.

## Sources

- span-concepts-databricks-on-aws.md
- retrievalsufficiency-judge-databricks-on-aws.md

# Citations

1. [span-concepts-databricks-on-aws.md](/references/span-concepts-databricks-on-aws-a55a7529.md)
2. [retrievalsufficiency-judge-databricks-on-aws.md](/references/retrievalsufficiency-judge-databricks-on-aws-ecbf8897.md)
