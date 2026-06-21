---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c5b15a83e02208f2a5553991453f1a4463adbb517536c288265076dd6321c4b
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - searching-and-filtering-traces-and-spans
    - Filtering Traces and Spans and Searching
    - SAFTAS
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: Searching and Filtering Traces and Spans
description: API methods (search_spans, search_assessments, search_traces) for finding specific spans and assessments by name, regex pattern, type, span ID, or combined criteria.
tags:
  - mlflow
  - tracing
  - search
  - filtering
timestamp: "2026-06-19T21:57:10.054Z"
---

# Searching and Filtering Traces and Spans

**Searching and Filtering Traces and Spans** refers to the techniques and API methods used to locate specific traces and spans within [MLflow Tracing](/concepts/mlflow-tracing.md) data. These capabilities allow practitioners to programmatically find relevant execution data for analysis, debugging, and monitoring of AI applications.

## Searching Traces

MLflow provides the `mlflow.search_traces()` function to retrieve traces matching specific criteria. This function returns a list of [Trace](/concepts/traces.md) objects that can then be examined in detail. ^[access-trace-data-databricks-on-aws.md]

## Searching Spans Within a Trace

Once a trace is retrieved, you can search for specific spans within that trace using the `trace.search_spans()` method. This method accepts several criteria to narrow down results: ^[access-trace-data-databricks-on-aws.md]

### Search by Name

You can search for spans by their exact name or by a regular expression pattern: ^[access-trace-data-databricks-on-aws.md]

```python
import re

# Search by exact name
retriever_spans = trace.search_spans(name="retrieve_documents")

# Search by regex pattern
pattern = re.compile(r".*_tool$")
tool_spans = trace.search_spans(name=pattern)
```

### Search by Span Type

Spans can be filtered by their SpanType, such as `CHAT_MODEL`, `LLM`, `TOOL`, or `RETRIEVER`. You can pass either the enum value or a string: ^[access-trace-data-databricks-on-aws.md]

```python
from mlflow.entities import SpanType

chat_spans = trace.search_spans(span_type=SpanType.CHAT_MODEL)
llm_spans = trace.search_spans(span_type="CHAT_MODEL")  # String also works
```

### Search by Span ID

To retrieve a specific span by its unique identifier: ^[access-trace-data-databricks-on-aws.md]

```python
specific_span = trace.search_spans(span_id=retriever_spans[0].span_id)
```

### Combining Multiple Criteria

You can combine name and span type filters together: ^[access-trace-data-databricks-on-aws.md]

```python
tool_fact_check = trace.search_spans(
    name="fact_check_tool",
    span_type=SpanType.TOOL
)
```

### Retrieving All Spans of a Type

To get all spans of a particular type without a name filter: ^[access-trace-data-databricks-on-aws.md]

```python
all_tools = trace.search_spans(span_type=SpanType.TOOL)
for tool in all_tools:
    print(f"Tool: {tool.name}")
```

## Accessing All Spans

All spans in a trace are available through the `trace.data.spans` property, which returns a list of Span objects. This provides access to complete span data including timing information, inputs, outputs, and status: ^[access-trace-data-databricks-on-aws.md]

```python
spans = trace.data.spans
print(f"Total spans: {len(spans)}")
```

## Searching Assessments

In addition to spans, you can search for assessments (evaluations) associated with a trace using `trace.search_assessments()`. This method supports filtering by name, type (`"feedback"` or `"expectation"`), and span ID: ^[access-trace-data-databricks-on-aws.md]

```python
# Search by name
helpfulness = trace.search_assessments(name="helpfulness")

# Search by type
feedback_only = trace.search_assessments(type="feedback")

# Search by span ID
span_assessments = trace.search_assessments(span_id=retriever_span.span_id)
```

## Working with Filtered Results

Once you have identified specific spans, you can examine their properties in detail. Common span attributes include: ^[access-trace-data-databricks-on-aws.md]

- `span_id` — Unique identifier for the span
- `name` — Human-readable name of the operation
- `span_type` — Type of operation (CHAT_MODEL, TOOL, RETRIEVER, etc.)
- `parent_id` — ID of the parent span (None for root spans)
- `start_time_ns` / `end_time_ns` — Timing information in nanoseconds
- `status` — Status code and description
- `inputs` / `outputs` — The data flowing through the span
- `attributes` — Custom and predefined attributes

## Related Concepts

- [Trace](/concepts/traces.md) — The top-level object containing trace metadata and execution data
- Span — Individual operations within a trace
- SpanType — Classification of span operations
- Access Trace Data — Complete guide to working with trace objects
- Analyzing Traces — Examples of trace analysis use cases
- [TraceInfo](/concepts/traceinfo.md) — Metadata about a trace including IDs, timestamps, and status
- [TraceData](/concepts/tracedata.md) — The execution data component containing spans and request/response data

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
