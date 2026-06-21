---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db3220a11e2c9d603c46230c76b242e096781d1fcb4c11916874bd673df16030
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - performance-profiling-with-trace-percentiles
    - PPWTP
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: Performance Profiling with Trace Percentiles
description: Technique for analyzing GenAI trace performance by calculating latency percentiles (P50, P95, P99) and identifying outlier traces.
tags:
  - mlflow
  - tracing
  - performance
  - monitoring
timestamp: "2026-06-19T18:44:33.534Z"
---

# Performance Profiling with Trace Percentiles

**Performance Profiling with Trace Percentiles** is a technique for analyzing the latency characteristics of GenAI applications by computing percentile statistics (e.g., P50, P95, P99) from the `execution_time_ms` field of collected traces. This approach helps identify performance bottlenecks, detect latency outliers, and establish baseline performance metrics for production monitoring.

## Overview

Trace percentiles provide a robust way to understand the performance distribution of your GenAI application. Unlike simple averages, percentile-based profiling reveals the full spectrum of user experiences, including tail latency. In production environments, a system that performs well on average may still have unacceptable latency for a significant portion of requests. ^[examples-analyzing-traces-databricks-on-aws.md]

The core workflow involves:
1. Retrieving traces using `mlflow.search_traces()`.
2. Extracting the `execution_time_ms` column from the results.
3. Computing percentile values (commonly P50, P95, and P99) from the latency distribution.
4. Identifying and analyzing outlier traces that exceed the P99 threshold.

## Computing Trace Percentiles

The following function demonstrates how to compute and display percentile performance metrics from a set of traces:

```python
def profile_performance(function_name: str = None, percentiles: list = [50, 95, 99]):
    """Profile performance metrics for traces."""
    # Build filter
    filter_parts = []
    if function_name:
        filter_parts.append(f"tag.`mlflow.traceName` = '{function_name}'")
    filter_string = " AND ".join(filter_parts) if filter_parts else None

    # Get traces
    traces = mlflow.search_traces(filter_string=filter_string)

    if len(traces) == 0:
        print("No traces found")
        return

    # Calculate percentiles
    perf_stats = traces['execution_time_ms'].describe(
        percentiles=[p/100 for p in percentiles]
    )

    print(f"Performance Analysis ({len(traces)} traces)")
    print("=" * 40)
    for p in percentiles:
        print(f"P{p}: {perf_stats[f'{p}%']:.1f}ms")
    print(f"Mean: {perf_stats['mean']:.1f}ms")
    print(f"Max: {perf_stats['max']:.1f}ms")

    # Find outliers (>P99)
    if 99 in percentiles:
        p99_threshold = perf_stats['99%']
        outliers = traces[traces['execution_time_ms'] > p99_threshold]
        if len(outliers) > 0:
            print(f"\nOutliers (>{p99_threshold:.0f}ms): {len(outliers)} traces")
            for _, trace in outliers.head(3).iterrows():
                print(f"- {trace['execution_time_ms']:.0f}ms: {trace['request_preview'][:50]}...")

    return traces
```

^[examples-analyzing-traces-databricks-on-aws.md]

## Key Percentile Metrics

The most commonly used percentiles for performance profiling are:

- **P50 (Median)**: Represents the typical latency experienced by half of all requests. Useful for understanding normal operating conditions. ^[examples-analyzing-traces-databricks-on-aws.md]
- **P95**: The latency threshold that 95% of requests fall below. This metric captures the experience of the majority of users while excluding the worst outliers. ^[examples-analyzing-traces-databricks-on-aws.md]
- **P99**: The latency threshold that 99% of requests fall below. This is the primary tail latency metric and is critical for identifying requests that experience unusual delays. ^[examples-analyzing-traces-databricks-on-aws.md]

## Outlier Detection

Traces that exceed the P99 threshold are classified as outliers. These represent the slowest 1% of requests. Analyzing outliers can reveal performance issues such as:

- Underlying infrastructure bottlenecks
- Slow downstream API calls or model inference
- Resource contention under load
- Unusual request patterns (e.g., very large inputs)

The `profile_performance` function identifies these outliers and provides a preview of their request content for further investigation. ^[examples-analyzing-traces-databricks-on-aws.md]

## Performance Breakdown by Span Type

Beyond overall trace latency, performance profiling can be extended to understand time spent in each component of the application. For a given trace, you can calculate the duration breakdown by span type:

```python
# Calculate time spent in each span type
time_by_type = {}
for span in trace.data.spans:
    duration_ms = (span.end_time_ns - span.start_time_ns) / 1_000_000
    if span.span_type not in time_by_type:
        time_by_type[span.span_type] = 0
    time_by_type[span.span_type] += duration_ms

print("Time by span type:")
for span_type, duration_ms in sorted(time_by_type.items(),
                                     key=lambda x: x[1], reverse=True):
    percentage = (duration_ms / total_duration_ms) * 100
    print(f"  {span_type}: {duration_ms:.1f}ms ({percentage:.1f}%)")
```

This breakdown helps identify which components—retrieval, LLM generation, tool calls—are contributing most to overall latency. ^[examples-analyzing-traces-databricks-on-aws.md]

## Error Monitoring

While percentiles focus on successful or completed traces, performance profiling should be combined with error monitoring for a complete picture. Traces with an `ERROR` status should be monitored separately, as they may complete very quickly (due to early termination) or very slowly (due to retries). The following pattern monitors errors in a recent time window:

```python
def monitor_errors(experiment_name: str, hours: int = 1):
    """Monitor errors in the last N hours."""
    current_time_ms = int(time.time() * 1000)
    cutoff_time_ms = current_time_ms - (hours * 60 * 60 * 1000)

    failed_traces = mlflow.search_traces(
        filter_string=f"trace.status = 'ERROR' AND "
                     f"trace.timestamp_ms > {cutoff_time_ms}",
        order_by=["trace.timestamp_ms DESC"]
    )
    # ... analyze error patterns ...
```

^[examples-analyzing-traces-databricks-on-aws.md]

## Use Cases

- **Production monitoring**: Continuously compute P50/P95/P99 for running applications to detect latency regressions. ^[examples-analyzing-traces-databricks-on-aws.md]
- **A/B testing**: Compare latency percentiles across different model versions, prompt strategies, or feature flag configurations to evaluate performance impact. ^[examples-analyzing-traces-databricks-on-aws.md]
- **Capacity planning**: Use P99 latency trends to determine when infrastructure scaling is needed.
- **SLA validation**: Verify that latency stays within defined service level agreements by measuring the percentage of requests meeting target thresholds.

## Related Concepts

- Trace Analysis — General techniques for analyzing GenAI traces.
- [Error Monitoring with Traces](/concepts/error-monitoring-with-mlflow-traces.md) — Monitoring and analyzing errors in production traces.
- Outlier Detection — Identifying and investigating anomalous trace behavior.
- [Span Analysis](/concepts/span-search-and-analysis.md) — Detailed examination of individual span performance within a trace.
- [Feature Flag Performance Analysis](/concepts/feature-flag-performance-analysis-with-traces.md) — Comparing latency distributions across different feature configurations.

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
