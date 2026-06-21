---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 822daddc3aa727665a51c19025561ca4d5f7f5442a10b892bb343c2d8f9226c8
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - span-search-and-analysis
    - Analysis and Span Search
    - SSAA
    - Span Analysis
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: Span Search and Analysis
description: API for searching spans by name (exact or regex), span type, span ID, and combined criteria; supports building span hierarchy trees, computing timing statistics by type, and identifying critical paths.
tags:
  - mlflow
  - tracing
  - spans
  - analysis
timestamp: "2026-06-19T08:51:03.280Z"
---

Here is the wiki page for "Span Search and Analysis".

---

## Span Search and Analysis

**Span Search and Analysis** refers to the process of programmatically finding and examining spans within a trace to understand the performance, execution path, and behavior of individual operations in a [MLflow Tracing](/concepts/mlflow-tracing.md) workflow. Since spans are the basic building blocks of traces—each representing a single unit of work such as an LLM call, tool invocation, or retrieval step—searching and analyzing them is essential for debugging, performance optimization, and quality assessment.

### Accessing Spans

All spans in a trace are accessible via `trace.data.spans`, which returns a list of immutable `Span` objects representing completed operations.^[access-trace-data-databricks-on-aws.md]

```python
spans = trace.data.spans
print(f"Total spans: {len(spans)}")
```

### Span Properties

Each `Span` object exposes properties that describe the operation it represents:^[access-trace-data-databricks-on-aws.md]

| Property | Description |
|----------|-------------|
| `span_id` | Unique identifier for the span |
| `name` | Human-readable operation name, e.g., `"retrieve_documents"` |
| `span_type` | Category of the span (e.g., `CHAT_MODEL`, `TOOL`, `RETRIEVER`, `LLM`) |
| `trace_id` | Identifies which trace the span belongs to |
| `parent_id` | Identifies the parent span; `None` for root spans |
| `start_time_ns` | Start time in nanoseconds since epoch |
| `end_time_ns` | End time in nanoseconds since epoch |
| `status` | Status object with `status_code` and optional `description` |
| `inputs` | Input data passed to the operation |
| `outputs` | Output data produced by the operation |

Duration can be computed as `(end_time_ns - start_time_ns) / 1_000_000` to obtain milliseconds.^[access-trace-data-databricks-on-aws.md]

### Searching Spans

The `trace.search_spans()` method provides structured filtering to find specific spans without iterating through the full list manually. It supports several filtering criteria:^[access-trace-data-databricks-on-aws.md]

| Filter Parameter | Description | Example |
|------------------|-------------|---------|
| `name` | Exact name or regex pattern | `search_spans(name="retrieve_documents")` |
| `span_type` | Type as `SpanType` enum value or string | `search_spans(span_type=SpanType.CHAT_MODEL)` |
| `span_id` | Specific span ID | `search_spans(span_id=some_id)` |

Multiple criteria can be combined to narrow results:^[access-trace-data-databricks-on-aws.md]

```python
tool_fact_check = trace.search_spans(
    name="fact_check_tool",
    span_type=SpanType.TOOL
)
```

### Span Attributes

Spans can carry additional metadata accessible via the `attributes` dictionary or the `get_attribute()` method. These attributes provide operation-specific details, such as chat messages or token usage for LLM calls:^[access-trace-data-databricks-on-aws.md]

```python
from mlflow.tracing.constant import SpanAttributeKey

chat_span = trace.search_spans(span_type=SpanType.CHAT_MODEL)[0]
messages = chat_span.get_attribute(SpanAttributeKey.CHAT_MESSAGES)
input_tokens = chat_span.get_attribute("llm.token_usage.input_tokens")
```

### Intermediate Outputs

Non-root spans' outputs can be accessed via `trace.data.intermediate_outputs`, which returns a dictionary mapping span names to their output values. This is useful for inspecting intermediary results without manually walking the span tree.^[access-trace-data-databricks-on-aws.md]

### Analyzing Span Hierarchies

Spans form a parent-child tree within a trace. Analysis functions can traverse this hierarchy to:^[access-trace-data-databricks-on-aws.md]

- Build a visual tree of the execution flow with durations and status indicators.
- Compute aggregate statistics, such as total LLM time compared to retrieval time.
- Identify the **critical path** — the longest-duration chain from root to leaf, highlighting the main bottleneck.

```python
def analyze_span_tree(trace):
    spans = trace.data.spans
    # Build parent-child relationships
    children = {}
    for span in spans:
        if span.parent_id:
            children.setdefault(span.parent_id, []).append(span)
    # Find root spans and print tree
    ...
```

### Span Serialization

Spans can be converted to and from dictionaries using `to_dict()` and `Span.from_dict()`, enabling JSON serialization and deserialization for storage or transfer.^[access-trace-data-databricks-on-aws.md]

### Related Concepts

- [Trace Data Access](/concepts/tracedata.md) — Accessing full trace-level metadata, request, and response data
- [Assessments on Traces](/concepts/assessments-on-traces.md) — Scoring traces and spans with evaluations
- SpanType Enumeration — The categorization of spans into types like `CHAT_MODEL`, `TOOL`, `RETRIEVER`
- SpanAttributeKey — Standardized keys for accessing span metadata
- Critical Path Analysis — Identifying the longest execution path in a trace

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
