---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 31ca599c0a451b66e24e652d038130a592151c6704ae5fa544cf59d52f838623
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-performance-profiling
    - TPP
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: Trace Performance Profiling
description: Techniques for analyzing trace execution time distributions, computing percentile latencies (P50, P95, P99), and identifying performance outliers.
tags:
  - mlflow
  - performance
  - tracing
  - observability
timestamp: "2026-06-19T10:25:51.494Z"
---

# Trace Performance Profiling

**Trace Performance Profiling** refers to the systematic analysis of [GenAI traces](/concepts/mlflow-genai-trace.md) to measure latency, identify bottlenecks, and monitor resource usage across the execution of an agent or pipeline. By instrumenting code with [MLflow Tracing](/concepts/mlflow-tracing.md) and querying trace data, developers can obtain quantitative performance metrics at both the trace and span levels, enabling data-driven optimization.

## Overview

Performance profiling of traces answers questions such as: *How long does the pipeline typically take? Which step is the slowest? Are there outliers that indicate failures or resource contention?* The `mlflow.search_traces()` API returns trace metadata including `execution_time_ms`, which can be aggregated to compute percentiles, means, and maxima. These metrics help teams set service-level objectives (SLOs) and detect regressions. ^[examples-analyzing-traces-databricks-on-aws.md]

## Common Performance Metrics

A typical performance analysis calculates latency percentiles (P50, P95, P99) across a set of traces. The `profile_performance` utility in the source material demonstrates this pattern: ^[examples-analyzing-traces-databricks-on-aws.md]

```python
def profile_performance(function_name=None, percentiles=[50, 95, 99]):
    # Build filter, get traces, compute describe()
    # Print P50, P95, P99, mean, max
    # Identify outliers (>P99)
```

Key metrics extracted:

- **P50/P95/P99 latency** – standard percentiles of execution time
- **Mean latency** – average performance
- **Maximum latency** – worst‑case behaviour
- **Outlier count** – traces exceeding the P99 threshold

## Span‑Level Performance Breakdown

Traces contain a hierarchy of spans, each with its own `start_time_ns` and `end_time_ns`. By grouping spans by their `span_type` (e.g., `CHAIN`, `RETRIEVER`, `CHAT_MODEL`, `TOOL`), you can compute the time spent in each category and the percentage of total duration. The `analyze_trace` function provides this breakdown: ^[examples-analyzing-traces-databricks-on-aws.md]

```python
for span_type, duration_ms in sorted(time_by_type.items(),
                                     key=lambda x: x[1], reverse=True):
    percentage = (duration_ms / total_duration_ms) * 100
    print(f"  {span_type}: {duration_ms:.1f}ms ({percentage:.1f}%)")
```

A span hierarchy can also be reconstructed to show parent‑child relationships, making it easier to pinpoint nested bottlenecks. ^[examples-analyzing-traces-databricks-on-aws.md]

## LLM Token Usage Profiling

For spans of type `CHAT_MODEL` or `LLM`, attributes like `llm.token_usage.input_tokens`, `output_tokens`, and `total_tokens` are available. The `TraceAnalyzer.get_llm_usage_summary()` method aggregates token counts across all relevant spans, providing totals for input, output, and combined tokens, as well as the number of LLM calls. ^[examples-analyzing-traces-databricks-on-aws.md]

## Error Impact on Performance

Errors can skew latency metrics or cause premature termination. Monitoring both error counts and latency together gives a fuller picture of system health. The `monitor_errors` function in the source material shows how to query traces with `trace.status = 'ERROR'` and group them by function name. ^[examples-analyzing-traces-databricks-on-aws.md]

## Feature Flag Performance Comparison

When A/B testing changes via feature flags, performance profiling can compare latencies between control and treatment groups. The `analyze_feature_flag_performance` function retrieves traces filtered by a flag’s state and computes average latency for each variant. ^[examples-analyzing-traces-databricks-on-aws.md]

```python
def analyze_feature_flag_performance(experiment_id, flag_name):
    control_latency = [t.info.execution_time_ms for t in control_traces]
    treatment_latency = [t.info.execution_time_ms for t in treatment_traces]
    return {
        f"avg_latency_{flag_name}_off": avg_control_latency,
        f"avg_latency_{flag_name}_on": avg_treatment_latency,
    }
```

## Reusable Profile Utilities

The `TraceAnalyzer` class bundles several profiling methods into a single interface:

| Method | Purpose |
|--------|---------|
| `get_error_summary()` | Lists all trace‑level, span‑level, and assessment errors |
| `get_llm_usage_summary()` | Aggregates token counts and LLM call count |
| `get_retrieval_metrics()` | Extracts number of documents and relevance scores for retrievers |
| `get_span_hierarchy()` | Builds a tree‑view of spans with durations |
| `export_for_evaluation()` | Packages trace data for offline evaluation |

These utilities can be reused across experiments to standardise how performance is measured. ^[examples-analyzing-traces-databricks-on-aws.md]

## Best Practices

- **Define clear percentiles** – P95 and P99 are commonly used for tail‑latency SLOs.
- **Filter by environment or version** – Use tags (e.g., `environment`, `version`) to isolate performance data.
- **Monitor token usage** – Sudden spikes in token count can indicate prompt bloat or inefficient retrieval.
- **Compare before/after changes** – Profile performance before and after code or model updates to detect regressions.
- **Keep span granularity appropriate** – Too many fine‑grained spans add overhead; too few hide bottlenecks.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying instrumentation framework.
- Spans – Execution units that carry timing and attribute data.
- Trace Analysis – Broader analysis beyond performance (e.g., correctness, retrieval quality).
- mlflow.search_traces() API|Search traces programmatically – The `mlflow.search_traces()` API used for bulk retrieval.
- [Log assessments](/concepts/assessments.md) – Adding feedback to traces for quality monitoring.

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
