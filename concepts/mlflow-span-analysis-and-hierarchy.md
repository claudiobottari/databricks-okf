---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6d6c9f254b9f5826464779e5ddd1a332f8a444bd0ca7ea6fedafa2b923a94a85
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-span-analysis-and-hierarchy
    - Hierarchy and MLflow Span Analysis
    - MSAAH
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: MLflow Span Analysis and Hierarchy
description: Techniques for analyzing span trees including parent-child relationships, critical path detection, and per-type timing statistics.
tags:
  - mlflow
  - tracing
  - analysis
timestamp: "2026-06-19T17:26:02.791Z"
---

# MLflow Span Analysis and Hierarchy

**MLflow Span Analysis and Hierarchy** refers to the set of tools and techniques for examining the structure, timing, and relationships of spans within MLflow traces. Spans are the building blocks of traces, representing individual operations or units of work, and they form a hierarchical tree structure that can be analyzed to understand application behavior. ^[access-trace-data-databricks-on-aws.md]

## Span Properties

Each Span object in MLflow has several key properties for analysis. Basic identification includes `span_id`, `name`, `span_type`, and `trace_id`. Timing information is recorded in nanoseconds, with `start_time_ns` and `end_time_ns` properties. Status information is available through `status`, `status_code`, and `status.description`. Inputs and outputs can be accessed via the `inputs` and `outputs` properties. ^[access-trace-data-databricks-on-aws.md]

## Span Hierarchy

Spans form a parent-child tree structure within a trace. The `parent_id` property indicates which span a given span belongs to — root spans have `parent_id` set to `None`. To reconstruct the hierarchy, you can build mapping dictionaries from span IDs to their children: ^[access-trace-data-databricks-on-aws.md]

```python
span_dict = {span.span_id: span for span in spans}
children = {}
for span in spans:
    if span.parent_id:
        if span.parent_id not in children:
            children[span.parent_id] = []
        children[span.parent_id].append(span)
```

This hierarchical structure allows for tree printing, root span identification, and analysis of parent-child relationships. ^[access-trace-data-databricks-on-aws.md]

## Searching and Filtering Spans

The `search_spans()` method on a [Trace](/concepts/traces.md) object provides flexible filtering by name, span type, span ID, or combinations of criteria. Name matching supports both exact strings and regex patterns. Span types can be specified using the `SpanType` enum or as strings. ^[access-trace-data-databricks-on-aws.md]

```python
retriever_spans = trace.search_spans(name="retrieve_documents")
chat_spans = trace.search_spans(span_type=SpanType.CHAT_MODEL)
tool_spans = trace.search_spans(name="fact_check_tool", span_type=SpanType.TOOL)
```

## Span Attributes

Spans can carry additional attributes accessed via the `get_attribute()` method or the `attributes` dictionary. The `SpanAttributeKey` enum provides standardized keys for common attributes like `CHAT_MESSAGES` and `CHAT_TOOLS`. Token usage information is accessible through attributes such as `llm.token_usage.input_tokens` and `llm.token_usage.output_tokens`. ^[access-trace-data-databricks-on-aws.md]

## Advanced Span Analysis

### Timing Analysis

Span timing analysis examines the duration of individual spans and groups of spans. Total execution time can be computed from start and end times, and category-specific timing can identify bottlenecks. For example, you can aggregate LLM time versus retrieval time to understand where processing is concentrated. ^[access-trace-data-databricks-on-aws.md]

### Critical Path Analysis

A critical path analysis identifies the longest duration path from a root span to a leaf span, revealing the most time-consuming sequence of operations. This is determined by recursively examining child spans and selecting the path with the maximum cumulative duration at each branching point. ^[access-trace-data-databricks-on-aws.md]

### Intermediate Outputs

Intermediate outputs from non-root spans can be accessed via `trace.data.intermediate_outputs`, which returns a dictionary mapping span names to their output values. This is useful for inspecting results at each stage of a pipeline. ^[access-trace-data-databricks-on-aws.md]

## Data Conversion

Spans can be converted to and from dictionaries using `span.to_dict()` and `Span.from_dict()`. This enables serialization, storage, and reconstruction of span data for offline analysis. The `SpanType` enum includes types such as `CHAT_MODEL`, `LLM`, `RETRIEVER`, and `TOOL`. ^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- [Trace](/concepts/traces.md) — The top-level object containing spans and metadata
- [TraceData](/concepts/tracedata.md) — Contains the actual execution data including spans
- [TraceInfo](/concepts/traceinfo.md) — Metadata about the trace including timing and status
- SpanType — Enumeration of possible span categories
- SpanAttributeKey — Standardized keys for accessing span attributes
- [Token Usage Tracking](/concepts/mlflow-token-usage-tracking.md) — Monitoring LLM token consumption at the span level
- [Trace Analysis Examples](/concepts/genai-trace-analysis-and-debugging.md) — Practical applications of span analysis patterns

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
