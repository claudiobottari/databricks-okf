---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d40a7a2fc9dc884f56f03bb89afbb98b1f2839be7d9304bf938e0342945076cf
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tracedata-and-span-objects
    - Span Objects and TraceData
    - TASO
    - Trace objects
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: TraceData and Span Objects
description: TraceData holds the actual execution spans, each with properties like span_id, name, type, parent_id, timing, status, inputs/outputs, and attributes.
tags:
  - mlflow
  - spans
  - execution-data
timestamp: "2026-06-18T10:37:57.111Z"
---

# TraceData and Span Objects

The MLflow `Trace` object consists of two main components: `TraceInfo` (metadata) and `TraceData` (the actual execution data). The `TraceData` object contains all spans, full request and response payloads, and intermediate outputs. Span objects represent individual operations or units of work within a trace and are immutable once retrieved. ^[access-trace-data-databricks-on-aws.md]

## TraceData

`TraceData` holds the execution-level data of a trace. You access it through `trace.data`. It provides three primary collections:

- **Spans** — A list of `Span` objects representing each operation.
- **Request / Response** — The full request and response payloads as JSON strings (from the root span, for backward compatibility).
- **Intermediate outputs** — A dictionary mapping span names to their outputs for non-root spans.

Python:

```python
spans = trace.data.spans
request_json = trace.data.request
response_json = trace.data.response
intermediate = trace.data.intermediate_outputs
```

^[access-trace-data-databricks-on-aws.md]

## Span Objects

The `Span` class (from `mlflow.entities`) represents an immutable, completed span retrieved from a trace. Each span has the following key properties:

| Property | Description |
|---|---|
| `span_id` | Unique identifier for the span |
| `name` | Human-readable name of the operation |
| `span_type` | The type of operation (e.g., `CHAT_MODEL`, `LLM`, `TOOL`, `RETRIEVER`) — see `SpanType` enum |
| `trace_id` | Identifier of the parent trace |
| `parent_id` | Identifier of the parent span, or `None` for root spans |
| `start_time_ns` | Start time in nanoseconds |
| `end_time_ns` | End time in nanoseconds |
| `status` | A `SpanStatus` object with `status_code` and `description` |
| `inputs` | Input arguments to the operation |
| `outputs` | Output from the operation |
| `attributes` | A dictionary of custom attributes |

^[access-trace-data-databricks-on-aws.md]

### Accessing Span Properties

```python
span = spans[0]
print(f"Span ID: {span.span_id}")
print(f"Name: {span.name}")
print(f"Type: {span.span_type}")
print(f"Start time: {span.start_time_ns}")
print(f"End time: {span.end_time_ns}")
duration_ms = (span.end_time_ns - span.start_time_ns) / 1_000_000
print(f"Duration: {duration_ms:.2f}ms")
print(f"Status: {span.status.status_code} - {span.status.description}")
print(f"Inputs: {span.inputs}")
print(f"Outputs: {span.outputs}")
```

^[access-trace-data-databricks-on-aws.md]

### Searching for Specific Spans

The `Trace.search_spans()` method lets you locate spans by name (exact string or regex), `span_type`, or `span_id`. You can combine criteria.

```python
import re
from mlflow.entities import SpanType

# By exact name
retriever_spans = trace.search_spans(name="retrieve_documents")

# By regex pattern
pattern = re.compile(r".*_tool$")
tool_spans = trace.search_spans(name=pattern)

# By span type
chat_spans = trace.search_spans(span_type=SpanType.CHAT_MODEL)

# By span ID
specific_span = trace.search_spans(span_id=retriever_spans[0].span_id)

# Combined criteria
tool_fact_check = trace.search_spans(
    name="fact_check_tool",
    span_type=SpanType.TOOL
)
```

^[access-trace-data-databricks-on-aws.md]

### Intermediate Outputs

For non-root spans, the intermediate outputs (the output of each span) are available as a dictionary:

```python
intermediate = trace.data.intermediate_outputs
if intermediate:
    for span_name, output in intermediate.items():
        print(f"  {span_name}: {output}")
```

^[access-trace-data-databricks-on-aws.md]

### Span Attributes

Use `span.get_attribute()` to retrieve specific attributes, or iterate `span.attributes`. The `SpanAttributeKey` constant (from `mlflow.tracing.constant`) provides typed keys for common attributes such as chat messages and tools.

```python
from mlflow.tracing.constant import SpanAttributeKey

chat_span = trace.search_spans(span_type=SpanType.CHAT_MODEL)[0]

# All attributes
for key, value in chat_span.attributes.items():
    print(f"  {key}: {value}")

# Specific attribute
custom = chat_span.get_attribute("custom_attribute")

# Chat-specific attributes
messages = chat_span.get_attribute(SpanAttributeKey.CHAT_MESSAGES)
tools = chat_span.get_attribute(SpanAttributeKey.CHAT_TOOLS)

# Token usage
input_tokens = chat_span.get_attribute("llm.token_usage.input_tokens")
output_tokens = chat_span.get_attribute("llm.token_usage.output_tokens")
```

^[access-trace-data-databricks-on-aws.md]

### Converting Spans to and from Dictionaries

```python
span_dict = span.to_dict()
reconstructed_span = Span.from_dict(span_dict)
```

^[access-trace-data-databricks-on-aws.md]

## Advanced Span Analysis

The following example function analyzes the span hierarchy, calculates statistics (total time, LLM time, retrieval time), and finds the critical path (longest chain of spans from root to leaf):

```python
def analyze_span_tree(trace):
    spans = trace.data.spans
    # Build children mapping
    span_dict = {span.span_id: span for span in spans}
    children = {}
    for span in spans:
        if span.parent_id:
            children.setdefault(span.parent_id, []).append(span)
    roots = [s for s in spans if s.parent_id is None]

    def print_tree(span, indent=0):
        duration_ms = (span.end_time_ns - span.start_time_ns) / 1_000_000
        status_icon = "✓" if span.status.status_code == SpanStatusCode.OK else "✗"
        print(f"{'  ' * indent}{status_icon} {span.name} ({span.span_type}) - {duration_ms:.1f}ms")
        for child in sorted(children.get(span.span_id, []), key=lambda s: s.start_time_ns):
            print_tree(child, indent + 1)

    print("Span Hierarchy:")
    for root in roots:
        print_tree(root)

    # Statistics
    total_time = sum((s.end_time_ns - s.start_time_ns) for s in spans) / 1_000_000
    llm_time = sum((s.end_time_ns - s.start_time_ns) for s in spans if s.span_type in [SpanType.LLM, SpanType.CHAT_MODEL]) / 1_000_000
    retrieval_time = sum((s.end_time_ns - s.start_time_ns) for s in spans if s.span_type == SpanType.RETRIEVER) / 1_000_000
    print(f"\nTotal spans: {len(spans)}, Total time: {total_time:.1f}ms, LLM: {llm_time:.1f}ms, Retrieval: {retrieval_time:.1f}ms")

    # Critical path
    def find_critical_path(span):
        child_paths = [find_critical_path(c) for c in children.get(span.span_id, [])]
        span_duration = (span.end_time_ns - span.start_time_ns) / 1_000_000
        if child_paths:
            best_path, best_duration = max(child_paths, key=lambda x: x[1])
            return [span] + best_path, span_duration + best_duration
        return [span], span_duration

    if roots:
        critical_paths = [find_critical_path(root) for root in roots]
        critical_path, critical_duration = max(critical_paths, key=lambda x: x[1])
        print(f"\nCritical Path ({critical_duration:.1f}ms total):")
        for span in critical_path:
            duration_ms = (span.end_time_ns - span.start_time_ns) / 1_000_000
            print(f"  → {span.name} ({duration_ms:.1f}ms)")
```

^[access-trace-data-databricks-on-aws.md]

## Data Export and Conversion

### Convert TraceData to Dictionary

```python
data_dict = trace.data.to_dict()
```

^[access-trace-data-databricks-on-aws.md]

### Convert Entire Trace to Pandas DataFrame Row

```python
row = trace.to_pandas_dataframe_row()
# Returns a dict with keys like 'trace_id', 'state', 'execution_duration', etc.
```

^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- [TraceInfo](/concepts/traceinfo.md) — Metadata about the trace (ID, status, timing, tags, token usage, assessments)
- [[MLflow Trace]] — The top-level entity that combines TraceInfo and TraceData
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The overall framework for instrumenting and collecting traces
- SpanType — Enumeration of span types (CHAT_MODEL, LLM, TOOL, RETRIEVER, etc.)
- SpanAttributeKey — Constants for accessing common span attributes

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
