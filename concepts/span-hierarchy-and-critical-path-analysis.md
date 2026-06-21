---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c71edb1d46a09f3febd4a9831069341319cb5f8a07f5e9b8454b72c1a72c10c0
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - span-hierarchy-and-critical-path-analysis
    - Critical Path Analysis and Span Hierarchy
    - SHACPA
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: Span Hierarchy and Critical Path Analysis
description: Technique for analyzing trace span trees including parent-child relationships, identifying root spans, computing duration statistics, and finding the critical path (longest duration path from root to leaf).
tags:
  - mlflow
  - tracing
  - analysis
  - performance
timestamp: "2026-06-18T14:18:01.750Z"
---

# Span Hierarchy and Critical Path Analysis

**Span Hierarchy and Critical Path Analysis** is a technique for understanding the structure and performance of [trace](/concepts/traces.md) execution by analyzing the parent‑child relationships among span|spans and identifying the longest‑duration path from a root span to a leaf. This analysis helps pinpoint where most time is spent in a complex, multi‑step operation such as an LLM chain or agent workflow.

## Overview

MLflow traces contain a collection of spans, each representing a unit of work. Spans are linked by parent‑child IDs, forming a tree. `analyze_span_tree()` is a utility function that:

1. Builds the parent‑child relationship map from the span list.  
2. Identifies root spans (those with no parent).  
3. Prints the tree with timing and status information.  
4. Computes aggregate statistics (total time, LLM time, retrieval time).  
5. Finds the **critical path** – the longest duration sequence of spans from a root to a leaf.

All logic shown below is derived directly from the source implementation. ^[access-trace-data-databricks-on-aws.md]

## Span Hierarchy Construction

The first step is to index spans by their `span_id` and then group child spans under each parent. Roots are spans where `parent_id` is `None`.

```python
def analyze_span_tree(trace):
    """Analyze the span hierarchy and relationships."""
    spans = trace.data.spans
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
    # ... (continued below)
```

^[access-trace-data-databricks-on-aws.md]

## Printing the Tree

The tree is printed recursively, showing the span name, type, duration in milliseconds, and a status icon (`✓` for OK, `✗` for error). Children are sorted by start time.

```python
    def print_tree(span, indent=0):
        duration_ms = (span.end_time_ns - span.start_time_ns) / 1_000_000
        status_icon = "✓" if span.status.status_code == SpanStatusCode.OK else "✗"
        print(f"{'  ' * indent}{status_icon} {span.name} "
              f"({span.span_type}) - {duration_ms:.1f}ms")
        for child in sorted(children.get(span.span_id, []),
                            key=lambda s: s.start_time_ns):
            print_tree(child, indent + 1)
    print("Span Hierarchy:")
    for root in roots:
        print_tree(root)
```

^[access-trace-data-databricks-on-aws.md]

## Span Statistics

After printing the hierarchy, the function calculates aggregate metrics:

- **Total time** – sum of all span durations.  
- **LLM time** – sum of durations for spans of type `LLM` or `CHAT_MODEL`.  
- **Retrieval time** – sum of durations for spans of type `RETRIEVER`.  
- Percentages relative to total time.

```python
    total_time = sum((s.end_time_ns - s.start_time_ns) / 1_000_000
                     for s in spans)
    llm_time = sum((s.end_time_ns - s.start_time_ns) / 1_000_000
                   for s in spans if s.span_type in [SpanType.LLM, SpanType.CHAT_MODEL])
    retrieval_time = sum((s.end_time_ns - s.start_time_ns) / 1_000_000
                        for s in spans if s.span_type == SpanType.RETRIEVER)
    print(f"\nSpan Statistics:")
    print(f"  Total spans: {len(spans)}")
    print(f"  Total time: {total_time:.1f}ms")
    print(f"  LLM time: {llm_time:.1f}ms ({llm_time/total_time*100:.1f}%)")
    print(f"  Retrieval time: {retrieval_time:.1f}ms "
          f"({retrieval_time/total_time*100:.1f}%)")
```

^[access-trace-data-databricks-on-aws.md]

## Critical Path Finding

The critical path is defined as the longest‑duration path from a root span to a leaf. It is found by a recursive function that for each span:

- Determines the duration of the span itself.  
- For each child span, recursively finds the child’s critical path and its total duration.  
- Selects the child with the largest total duration.  
- Returns the concatenated path and the cumulative duration.

```python
    def find_critical_path(span):
        child_paths = []
        for child in children.get(span.span_id, []):
            path, duration = find_critical_path(child)
            child_paths.append((path, duration))
        span_duration = (span.end_time_ns - span.start_time_ns) / 1_000_000
        if child_paths:
            best_path, best_duration = max(child_paths, key=lambda x: x[1])
            return [span] + best_path, span_duration + best_duration
        else:
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

## Usage

Call the function with any retrieved [[MLflow Trace]] object to see a full analysis:

```python
trace = mlflow.search_traces()[0]   # or obtain a trace object
analyze_span_tree(trace)
```

^[access-trace-data-databricks-on-aws.md]

## Related Concepts

- Span – Individual unit of work in a trace.  
- [Trace](/concepts/traces.md) – The complete record of an operation, composed of spans.  
- Access Trace Data – How to retrieve trace and span information.  
- SpanType – Enum classifying spans (e.g., `CHAT_MODEL`, `TOOL`, `RETRIEVER`).  
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The overarching tracing framework.

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
