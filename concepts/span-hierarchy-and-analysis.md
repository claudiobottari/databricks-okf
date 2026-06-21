---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c35e18691f3ef4b46511bb52973da455b58c854828db7972d17ec09e79a82e6
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - span-hierarchy-and-analysis
    - Analysis and Span Hierarchy
    - SHAA
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: Span Hierarchy and Analysis
description: Spans form a parent-child hierarchy within a trace, and can be analyzed for relationships, critical paths, timing statistics, and categorized by span type (LLM, CHAT_MODEL, RETRIEVER, TOOL, etc.).
tags:
  - mlflow
  - tracing
  - spans
  - analysis
timestamp: "2026-06-19T13:52:38.695Z"
---

---
title: Span Hierarchy and Analysis
summary: Spans form a parent-child hierarchy representing nested operations; tools exist for analyzing span trees, critical paths, and per-type timing statistics.
sources:
  - access-trace-data-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:38:14.054Z"
updatedAt: "2026-06-18T10:38:14.054Z"
tags:
  - mlflow
  - spans
  - analysis
aliases:
  - span-hierarchy-and-analysis
  - Analysis and Span Hierarchy
  - SHAA
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Span Hierarchy and Analysis

**Span hierarchy and analysis** refers to the structural organization of spans within a trace and the techniques used to examine their relationships, timing, and performance characteristics. Spans are the building blocks of traces, representing individual operations or units of work in a request's execution path. Understanding span hierarchy enables developers to identify bottlenecks, trace execution flows, and optimize application performance. ^[access-trace-data-databricks-on-aws.md]

## Span Hierarchy Structure

A trace consists of multiple spans organized in a parent-child tree structure. Each span represents a discrete operation, such as an LLM call, a retrieval operation, or a tool execution. The hierarchy begins with root spans (spans with no parent) and branches into child spans that represent sub-operations. ^[access-trace-data-databricks-on-aws.md]

### Root Spans

Root spans are the top-level spans in a trace hierarchy. They have no parent ID (`parent_id` is `None`) and represent the entry point of the traced operation. A trace can have multiple root spans if the execution involves parallel or independent operations. ^[access-trace-data-databricks-on-aws.md]

### Parent-Child Relationships

Each span can have one parent and multiple children. The `parent_id` property links a child span to its parent, creating the hierarchical structure. Child spans represent sub-operations that occur within the context of their parent span. ^[access-trace-data-databricks-on-aws.md]

## Span Properties

Every span in a trace exposes the following properties: ^[access-trace-data-databricks-on-aws.md]

| Property | Description |
|---|---|
| `span_id` | Unique identifier for the span |
| `name` | Human-readable name of the operation |
| `span_type` | Category of the operation (e.g., `CHAT_MODEL`, `LLM`, `RETRIEVER`, `TOOL`) |
| `trace_id` | Identifier of the parent trace |
| `parent_id` | Identifier of the parent span (`None` for root spans) |
| `start_time_ns` | Start time in nanoseconds |
| `end_time_ns` | End time in nanoseconds |
| `status` | Status object with `status_code` and `description` |
| `inputs` | Input data for the operation |
| `outputs` | Output data from the operation |
| `attributes` | Key-value metadata associated with the span |

## Span Types

The `SpanType` enum defines common span categories: ^[access-trace-data-databricks-on-aws.md]

- `CHAT_MODEL` — Chat model invocations
- `LLM` — General LLM operations
- `RETRIEVER` — Document retrieval operations
- `TOOL` — Tool or function calls
- `AGENT` — Agent orchestration steps
- `PARSER` — Output parsing operations
- `CHAIN` — Chain or pipeline operations
- `EMBEDDING` — Embedding generation

## Analyzing Span Hierarchy

### Building the Span Tree

To analyze the hierarchy, you can build parent-child relationships from the flat list of spans: ^[access-trace-data-databricks-on-aws.md]

```python
def build_span_tree(spans):
    """Build parent-child relationships from spans."""
    span_dict = {span.span_id: span for span in spans}
    children = {}
    for span in spans:
        if span.parent_id:
            if span.parent_id not in children:
                children[span.parent_id] = []
            children[span.parent_id].append(span)

    # Find root spans (no parent)
    roots = [s for s in spans if s.parent_id is None]
    return roots, children
```

### Visualizing the Hierarchy

You can print the span tree with indentation to visualize the execution flow: ^[access-trace-data-databricks-on-aws.md]

```python
def print_span_tree(span, children, indent=0):
    duration_ms = (span.end_time_ns - span.start_time_ns) / 1_000_000
    status_icon = "✓" if span.status.status_code == SpanStatusCode.OK else "✗"
    print(f"{'  ' * indent}{status_icon} {span.name} ({span.span_type}) - {duration_ms:.1f}ms")

    for child in sorted(children.get(span.span_id, []),
                        key=lambda s: s.start_time_ns):
        print_span_tree(child, children, indent + 1)
```

## Performance Analysis

### Span Statistics

Calculate aggregate statistics across all spans to understand where time is spent: ^[access-trace-data-databricks-on-aws.md]

```python
def calculate_span_statistics(spans):
    total_time = sum((s.end_time_ns - s.start_time_ns) / 1_000_000 for s in spans)

    llm_time = sum((s.end_time_ns - s.start_time_ns) / 1_000_000
                   for s in spans if s.span_type in [SpanType.LLM, SpanType.CHAT_MODEL])

    retrieval_time = sum((s.end_time_ns - s.start_time_ns) / 1_000_000
                        for s in spans if s.span_type == SpanType.RETRIEVER)

    print(f"Total spans: {len(spans)}")
    print(f"Total time: {total_time:.1f}ms")
    print(f"LLM time: {llm_time:.1f}ms ({llm_time/total_time*100:.1f}%)")
    print(f"Retrieval time: {retrieval_time:.1f}ms ({retrieval_time/total_time*100:.1f}%)")
```

### Critical Path Analysis

The critical path is the longest duration path from a root span to a leaf span, representing the minimum time required for the entire operation: ^[access-trace-data-databricks-on-aws.md]

```python
def find_critical_path(span, children):
    """Find the longest path from this span to any leaf."""
    child_paths = []
    for child in children.get(span.span_id, []):
        path, duration = find_critical_path(child, children)
        child_paths.append((path, duration))

    span_duration = (span.end_time_ns - span.start_time_ns) / 1_000_000

    if child_paths:
        best_path, best_duration = max(child_paths, key=lambda x: x[1])
        return [span] + best_path, span_duration + best_duration
    else:
        return [span], span_duration
```

## Searching and Filtering Spans

The `search_spans()` method on a [Trace](/concepts/traces.md) object provides flexible filtering capabilities: ^[access-trace-data-databricks-on-aws.md]

```python
# Search by exact name
retriever_spans = trace.search_spans(name="retrieve_documents")

# Search by regex pattern
import re
tool_spans = trace.search_spans(name=re.compile(r".*_tool$"))

# Search by span type
chat_spans = trace.search_spans(span_type=SpanType.CHAT_MODEL)

# Search by span ID
specific_span = trace.search_spans(span_id=retriever_spans[0].span_id)

# Combine criteria
tool_fact_check = trace.search_spans(
    name="fact_check_tool",
    span_type=SpanType.TOOL
)
```

## Span Attributes

Spans can carry custom attributes that provide additional context about the operation. For chat model spans, special attributes are available via `SpanAttributeKey`: ^[access-trace-data-databricks-on-aws.md]

```python
from mlflow.tracing.constant import SpanAttributeKey

# Access chat-specific attributes
messages = chat_span.get_attribute(SpanAttributeKey.CHAT_MESSAGES)
tools = chat_span.get_attribute(SpanAttributeKey.CHAT_TOOLS)

# Access token usage from span
input_tokens = chat_span.get_attribute("llm.token_usage.input_tokens")
output_tokens = chat_span.get_attribute("llm.token_usage.output_tokens")
```

## Intermediate Outputs

Non-root spans can expose intermediate outputs, which are the outputs of individual operations within the trace: ^[access-trace-data-databricks-on-aws.md]

```python
intermediate = trace.data.intermediate_outputs
if intermediate:
    for span_name, output in intermediate.items():
        print(f"  {span_name}: {output}")
```

## Serialization and Conversion

Spans can be converted to and from dictionaries for serialization or analysis: ^[access-trace-data-databricks-on-aws.md]

```python
# Convert span to dictionary
span_dict = span.to_dict()

# Recreate span from dictionary
from mlflow.entities import Span
reconstructed_span = Span.from_dict(span_dict)
```

## Best Practices

- **Always check span status** before analyzing timing data — failed spans may have misleading durations.
- **Sort child spans by start time** when printing the hierarchy to maintain chronological order.
- **Use span types for filtering** rather than names when possible, as types are standardized across different implementations.
- **Calculate critical path** to identify the true bottleneck in parallel execution flows.
- **Compare span-level token usage** with trace-level token usage to verify consistency.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework that generates spans
- [Trace Data Access](/concepts/tracedata.md) — How to access and work with trace objects
- [Trace Analysis Examples](/concepts/genai-trace-analysis-and-debugging.md) — Practical examples of trace analysis
- Span Types — The complete list of span type categories
- [Token Usage Tracking](/concepts/mlflow-token-usage-tracking.md) — How token counts are captured in spans

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
