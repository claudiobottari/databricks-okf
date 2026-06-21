---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee88ca3d03db1cef44f75e380b3c667d043d143521fc054684a0f233d3b22684
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tracedata-and-spans
    - Spans and TraceData
    - TAS
    - Creating Spans
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: TraceData and Spans
description: TraceData holds the execution data of a trace including spans (individual operations), full request/response data, and intermediate outputs from non-root spans.
tags:
  - mlflow
  - tracing
  - spans
timestamp: "2026-06-19T13:52:40.676Z"
---

# TraceData and Spans

**TraceData** and **Spans** are the two core structural components of an MLflow [Trace](/concepts/traces.md), representing the actual execution data of a traced operation. While [TraceInfo](/concepts/traceinfo.md) stores metadata about a trace, `TraceData` and `Span` objects capture the detailed execution flow, including individual operations, their inputs and outputs, timing, and hierarchical relationships.

## Overview

The MLflow [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) object consists of two main components: `TraceInfo` for metadata and `TraceData` for execution data. `TraceData` contains the complete request and response payloads as well as all Span objects that represent individual units of work within the trace. ^[access-trace-data-databricks-on-aws.md]

## TraceData

`TraceData` represents the actual execution data of a trace. It provides access to spans, intermediate outputs, and full request/response content.

### Accessing TraceData

Access `TraceData` through the `data` property of a `Trace` object:

```python
trace_data = trace.data
spans = trace.data.spans
full_request = trace.data.request  # Complete request text
full_response = trace.data.response  # Complete response text
```

^[access-trace-data-databricks-on-aws.md]

### Intermediate Outputs

`TraceData` also provides access to intermediate outputs from non-root spans:

```python
intermediate = trace.data.intermediate_outputs
if intermediate:
    for span_name, output in intermediate.items():
        print(f"  {span_name}: {output}")
```

^[access-trace-data-databricks-on-aws.md]

## Spans

Spans are the building blocks of traces, representing individual operations or units of work. The [`Span`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Span) class represents immutable, completed spans retrieved from traces. ^[access-trace-data-databricks-on-aws.md]

### Span Properties

Each span contains several categories of information:

**Identification properties:**

- `span_id`: Unique identifier for the span
- `name`: Human-readable name of the operation
- `span_type`: Type of operation (e.g., `CHAT_MODEL`, `LLM`, `TOOL`, `RETRIEVER`)
- `trace_id`: The trace this span belongs to
- `parent_id`: ID of the parent span (None for root spans)

**Timing information** (in nanoseconds):

- `start_time_ns`: When the operation began
- `end_time_ns`: When the operation completed

**Status information:**

- `status`: The span status object
- `status_code`: Success or failure code
- `status_description`: Error details if applicable

**Data:**

- `inputs`: Input data to the operation
- `outputs`: Output data from the operation
- `attributes`: Additional attributes (e.g., chat messages, token usage)

^[access-trace-data-databricks-on-aws.md]

```python
span = spans[0]
print(f"Span ID: {span.span_id}")
print(f"Name: {span.name}")
print(f"Type: {span.span_type}")
print(f"Duration: {(span.end_time_ns - span.start_time_ns) / 1_000_000:.2f}ms")
print(f"Status: {span.status}")
print(f"Inputs: {span.inputs}")
print(f"Outputs: {span.outputs}")
```

### Span Attributes

Spans can store additional attributes accessible via `get_attribute()` or through the `attributes` dictionary:

```python
from mlflow.tracing.constant import SpanAttributeKey

chat_span = trace.search_spans(span_type=SpanType.CHAT_MODEL)[0]

# Get all attributes
for key, value in chat_span.attributes.items():
    print(f"  {key}: {value}")

# Access specific attributes
messages = chat_span.get_attribute(SpanAttributeKey.CHAT_MESSAGES)
tools = chat_span.get_attribute(SpanAttributeKey.CHAT_TOOLS)

# Access token usage from span
input_tokens = chat_span.get_attribute("llm.token_usage.input_tokens")
output_tokens = chat_span.get_attribute("llm.token_usage.output_tokens")
```

^[access-trace-data-databricks-on-aws.md]

## Searching and Filtering Spans

Use the [`search_spans()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace.search_spans) method to find spans matching specific criteria:

```python
import re
from mlflow.entities import SpanType

# Search by exact name
retriever_spans = trace.search_spans(name="retrieve_documents")

# Search by regex pattern
pattern = re.compile(r".*_tool$")
tool_spans = trace.search_spans(name=pattern)

# Search by span type
chat_spans = trace.search_spans(span_type=SpanType.CHAT_MODEL)
llm_spans = trace.search_spans(span_type="CHAT_MODEL")  # String also works

# Search by span ID
specific_span = trace.search_spans(span_id=retriever_spans[0].span_id)

# Combine criteria
tool_fact_check = trace.search_spans(
    name="fact_check_tool",
    span_type=SpanType.TOOL
)
```

^[access-trace-data-databricks-on-aws.md]

## Span Hierarchy Analysis

Spans form a parent-child hierarchy that represents the nested execution structure. Root spans have no parent, while child spans represent sub-operations:

```python
# Build parent-child relationships
span_dict = {span.span_id: span for span in spans}
children = {}
for span in spans:
    if span.parent_id:
        if span.parent_id not in children:
            children[span.parent_id] = []
        children[span.parent_id].append(span)

# Find root spans
roots = [s for s in spans if s.parent_id is None]
```

^[access-trace-data-databricks-on-aws.md]

## Span Types

MLflow defines several `SpanType` constants that classify operations:

- `CHAT_MODEL`: Chat model invocations
- `LLM`: Language model calls
- `TOOL`: Tool/function calls
- `RETRIEVER`: Document retrieval operations
- `AGENT`: Agent loop execution
- `PARSER`: Output parsing
- `UNKNOWN`: Unclassified operations

^[access-trace-data-databricks-on-aws.md]

## Data Export and Conversion

### Converting Span to/from Dictionary

```python
# Convert span to dictionary
span_dict = span.to_dict()

# Recreate span from dictionary
from mlflow.entities import Span
reconstructed_span = Span.from_dict(span_dict)
```

^[access-trace-data-databricks-on-aws.md]

### Converting Trace to DataFrame

```python
# Convert trace to DataFrame row
row_data = trace.to_pandas_dataframe_row()

# Create DataFrame from multiple traces
import pandas as pd
trace_rows = [t.to_pandas_dataframe_row() for t in traces]
df = pd.DataFrame(trace_rows)
```

^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- [TraceInfo](/concepts/traceinfo.md) — Metadata component of a Trace object
- [Trace Search and Filtering](/concepts/mlflow-trace-search-and-filtering.md) — Querying traces and spans across experiments
- [Creating Spans](/concepts/tracedata-and-spans.md) — Instrumenting code to generate spans
- Custom Span Attributes — Adding domain-specific data to spans
- [Token Usage Tracking](/concepts/mlflow-token-usage-tracking.md) — Capturing LLM token consumption in spans
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Using execution traces for quality assessment

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
