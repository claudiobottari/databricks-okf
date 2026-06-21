---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 71039839a89326b7bf71e31c7a2e474da75be44c6aec5726a2d76a9aa8a2bf1d
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - performance-monitoring-with-mlflow-traces
    - PMWMT
    - Performance Monitoring with Traces
    - GenAI App Performance Monitoring
    - Performance Monitoring
    - Performance Monitoring Pattern
    - Performance monitoring
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: Performance monitoring with MLflow traces
description: Pattern for profiling GenAI trace performance by calculating latency percentiles (P50, P95, P99) and identifying outlier traces using execution_time_ms.
tags:
  - mlflow
  - performance-monitoring
  - genai-tracing
timestamp: "2026-06-18T12:14:30.731Z"
---

# Performance monitoring with MLflow traces

**Performance monitoring with MLflow traces** refers to the practice of using MLflow’s tracing infrastructure to measure, analyze, and optimize the latency of GenAI applications in production. By programmatically querying trace data and computing statistical distributions, teams can identify bottlenecks, detect regressions, and compare the performance impact of configuration changes.

## Overview

MLflow traces capture detailed execution information for each GenAI pipeline invocation, including start and end times for every span. Using the `mlflow.search_traces()` API, you can retrieve traces over a time window, filter by function names or tags, and extract metrics such as execution duration. These metrics form the basis for performance analysis. ^[examples-analyzing-traces-databricks-on-aws.md]

## Key latency metrics

A typical performance-monitoring workflow computes percentile-based statistics across a set of traces: ^[examples-analyzing-traces-databricks-on-aws.md]

```python
def profile_performance(function_name: str = None, percentiles: list = [50, 95, 99]):
    filter_parts = []
    if function_name:
        filter_parts.append(f"tag.`mlflow.traceName` = '{function_name}'")
    filter_string = " AND ".join(filter_parts) if filter_parts else None

    traces = mlflow.search_traces(filter_string=filter_string)
    if len(traces) == 0:
        print("No traces found")
        return

    perf_stats = traces['execution_time_ms'].describe(percentiles=[p/100 for p in percentiles])
    print(f"Performance Analysis ({len(traces)} traces)")
    print("=" * 40)
    for p in percentiles:
        print(f"P{p}: {perf_stats[f'{p}%']:.1f}ms")
    print(f"Mean: {perf_stats['mean']:.1f}ms")
    print(f"Max: {perf_stats['max']:.1f}ms")

    # Identify outliers (>P99)
    if 99 in percentiles:
        p99_threshold = perf_stats['99%']
        outliers = traces[traces['execution_time_ms'] > p99_threshold]
        if len(outliers) > 0:
            print(f"\nOutliers (>{p99_threshold:.0f}ms): {len(outliers)} traces")
            for _, trace in outliers.head(3).iterrows():
                print(f"- {trace['execution_time_ms']:.0f}ms: {trace['request_preview'][:50]}...")
    return traces
```

This function gives you:
- **Latency percentiles** – P50, P95, P99 (or custom percentiles) to understand the distribution.
- **Mean and maximum** latency.
- **Outlier detection** – traces above the P99 threshold, which may indicate incidents or degraded performance.

## Performance breakdown by span type

Beyond overall latency, you can drill into the time spent in each span type (e.g., retriever, chat model, tool). The root span’s total duration provides a reference, and you compute each child span’s proportion: ^[examples-analyzing-traces-databricks-on-aws.md]

```python
root_span = next((s for s in trace.data.spans if s.parent_id is None), None)
if root_span:
    total_duration_ns = root_span.end_time_ns - root_span.start_time_ns
    time_by_type = {}
    for span in trace.data.spans:
        duration_ms = (span.end_time_ns - span.start_time_ns) / 1_000_000
        time_by_type[span.span_type] = time_by_type.get(span.span_type, 0) + duration_ms
    for span_type, duration_ms in sorted(time_by_type.items(), key=lambda x: x[1], reverse=True):
        percentage = (duration_ms / (total_duration_ns / 1_000_000)) * 100
        print(f"  {span_type}: {duration_ms:.1f}ms ({percentage:.1f}%)")
```

This analysis reveals which component of the pipeline is the dominant bottleneck – for example, an expensive LLM call versus slow vector-store retrieval.

## Feature flag comparison

When you roll out a change (e.g., a new retriever or model), you can tag traces with a feature flag identifier and compare the latency distributions between the control and treatment groups: ^[examples-analyzing-traces-databricks-on-aws.md]

```python
def analyze_feature_flag_performance(experiment_id, flag_name):
    control_traces = client.search_traces(
        experiment_ids=[experiment_id],
        filter_string=f"metadata.feature_flag_{flag_name} = 'false'",
    )
    treatment_traces = client.search_traces(
        experiment_ids=[experiment_id],
        filter_string=f"metadata.feature_flag_{flag_name} = 'true'",
    )
    control_latency = [t.info.execution_time_ms for t in control_traces]
    treatment_latency = [t.info.execution_time_ms for t in treatment_traces]
    avg_control = sum(control_latency)/len(control_latency) if control_latency else 0
    avg_treatment = sum(treatment_latency)/len(treatment_latency) if treatment_latency else 0
    return {f"avg_latency_{flag_name}_off": avg_control,
            f"avg_latency_{flag_name}_on": avg_treatment}
```

The resulting averages let you quantify the performance impact of the flag – for instance, an increase of 50 ms when the new retriever is enabled.

## Error correlation

Performance monitoring becomes more powerful when combined with error analysis. You can monitor error rates over the same time window and check whether outliers or high-latency spans coincide with failures. See [Error Monitoring with MLflow Traces](/concepts/error-monitoring-with-mlflow-traces.md) for patterns that complement performance metrics. ^[examples-analyzing-traces-databricks-on-aws.md]

## Best practices

- **Set a baseline.** Record percentiles (P50, P95, P99) for a clean period before introducing changes.
- **Filter by function or tag.** Group traces by `mlflow.traceName` or custom tags to isolate specific pipelines.
- **Use percentiles over averages.** Averages can hide long-tail latency; P95 and P99 reflect the user experience more accurately.
- **Track outliers promptly.** Investigate traces above the P99 threshold to identify transient failures or resource contention.
- **Automate monitoring.** Schedule the `profile_performance` function periodically and alert on significant increases in P95 or P99.

## Related concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying framework for capturing spans and traces.
- mlflow.search_traces() – The API used to query trace data programmatically.
- [Error Monitoring with MLflow Traces](/concepts/error-monitoring-with-mlflow-traces.md) – Companion analysis for detecting failures.
- [Trace span types](/concepts/trace-spans.md) – Categories such as `CHAIN`, `RETRIEVER`, `CHAT_MODEL`, and `TOOL`.
- [Adding context to traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) – How to tag traces with environment, user ID, and feature flag metadata.
- Building evaluation datasets from traces – Converting trace data for offline evaluation.

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
