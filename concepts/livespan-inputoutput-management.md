---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2ac1bacb8b2b7bc2a5bc4e94ae33fc8f6a604c1af6acca8a052fcdaf09965f66
  pageDirectory: concepts
  sources:
    - span-tracing-with-context-managers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - livespan-inputoutput-management
    - LIM
  citations:
    - file: span-tracing-with-context-managers-databricks-on-aws.md
title: LiveSpan Input/Output Management
description: Manual specification of span inputs and outputs via LiveSpan.set_inputs() and LiveSpan.set_outputs() when using context managers, unlike automatic capture with function decorators.
tags:
  - mlflow
  - tracing
  - api
  - observability
timestamp: "2026-06-19T23:06:12.126Z"
---

Here is the wiki page for "LiveSpan Input/Output Management".

---

## LiveSpan Input/Output Management

**LiveSpan Input/Output Management** refers to the process of explicitly setting the inputs and outputs of a span created via `mlflow.start_span()`. Unlike [Span Tracing with Function Decorators](/concepts/mlflowtrace-function-decorator.md), which automatically captures function arguments and return values, the context manager approach requires manual specification of inputs and outputs using the `LiveSpan` object returned by the context manager. ^[span-tracing-with-context-managers-databricks-on-aws.md]

### Overview

When using the `mlflow.start_span()` context manager to trace arbitrary code blocks, the span does not automatically know what data was passed in or produced. You must provide this information manually to ensure the trace is complete and useful for debugging or analysis. ^[span-tracing-with-context-managers-databricks-on-aws.md]

### Setting Inputs

Use the `set_inputs()` method on the `LiveSpan` object to record the input data. The method accepts a dictionary where keys are descriptive names and values are the actual input values. ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]

with [[mlflow|MLflow]].start_span(name="my_span") as span:
    x = 1
    y = 2
    span.set_inputs({"x": x, "y": y})
    z = x + y
    span.set_outputs(z)
```

^[span-tracing-with-context-managers-databricks-on-aws.md]

### Setting Outputs

Use the `set_outputs()` method to record the result of the traced code block. Outputs can be any Python object, including scalars, strings, lists, or dictionaries. ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
span.set_outputs(result_value)
```

^[span-tracing-with-context-managers-databricks-on-aws.md]

### Special Case: [RETRIEVER Spans](/concepts/retriever-spans.md)

For spans with `span_type=SpanType.RETRIEVER`, outputs must be a list of Document objects. Otherwise, the UI will not render the retrieved documents properly. ^[span-tracing-with-context-managers-databricks-on-aws.md]

```python
from [[mlflow|MLflow]].entities import Document, SpanType

@mlflow.trace(span_type=SpanType.RETRIEVER)
def retrieve_documents(query: str):
    span = [[mlflow|MLflow]].get_current_active_span()
    documents = [
        Document(
            page_content="The content of the document...",
            metadata={
                "doc_uri": "path/to/document.md",
                "chunk_id": "chunk_001",
                "relevance_score": 0.95,
                "source": "knowledge_base"
            },
            id="doc_123"
        )
    ]
    span.set_outputs(documents)
```

^[span-tracing-with-context-managers-databricks-on-aws.md]

### Accessing Inputs and Outputs from Completed [Traces](/concepts/traces.md)

After the trace is complete, you can retrieve inputs and outputs by searching spans in the trace object: ^[span-tracing-with-context-managers-databricks-on-aws.md]

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
```

^[span-tracing-with-context-managers-databricks-on-aws.md]

### Related Concepts

- mlflow.start_span() Context Manager|Span Tracing with Context Managers — The parent concept for creating spans manually.
- [Span Tracing with Function Decorators](/concepts/mlflowtrace-function-decorator.md) — Automatic input/output capture alternative.
- LiveSpan Attributes — Setting custom key-value metadata on spans.
- [Span Events](/concepts/spanevent-objects.md) — Recording occurrences during a span's lifetime.
- [Span Status](/concepts/spanstatus-api.md) — Defining success or error status on spans.
- Document Objects — Required output type for [RETRIEVER Spans](/concepts/retriever-spans.md).

### Sources

- span-tracing-with-context-managers-databricks-on-aws.md

# Citations

1. [span-tracing-with-context-managers-databricks-on-aws.md](/references/span-tracing-with-context-managers-databricks-on-aws-d67ed6d9.md)
