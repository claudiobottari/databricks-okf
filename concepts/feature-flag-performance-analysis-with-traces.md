---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 26f448a20754006ec6d0ec1802af656a81afe3c720b43a53f1ff211b5a9aaf6f
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-flag-performance-analysis-with-traces
    - FFPAWT
    - Feature Flag Performance Analysis
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: Feature Flag Performance Analysis with Traces
description: Pattern for comparing GenAI application performance across different feature flag states by filtering and aggregating trace latency data.
tags:
  - mlflow
  - tracing
  - feature-flags
  - experimentation
timestamp: "2026-06-19T18:45:18.047Z"
---



# Feature Flag Performance Analysis with Traces

**Feature Flag Performance Analysis with Traces** is a pattern for using [MLflow Tracing](/concepts/mlflow-tracing.md) to compare the latency and performance of production GenAI applications under different [Feature Flag](/concepts/feature-table.md) configurations. By annotating traces with feature flag metadata and then querying the resulting trace data, teams can measure the real-world impact of a flag change before fully rolling it out. ^[examples-analyzing-traces-databricks-on-aws.md]

## Overview

The core idea is to record the current state of each feature flag as a metadata attribute on every trace that is generated while the flag is active. After running the system for a period of time (or after a controlled experiment), the analyst searches for traces that match each flag state and computes aggregate latency statistics. The results are then returned as a simple dictionary of average latencies for the "off" and "on" states. ^[examples-analyzing-traces-databricks-on-aws.md]

## Implementation

The following pattern, adapted from the Databricks documentation, performs a side‑by‑side comparison of a single binary flag:

```python
def analyze_feature_flag_performance(
    experiment_id: str, flag_name: str
):
    """Analyze performance differences between feature flag states."""
    control_latency = []
    treatment_latency = []

    control_traces = client.search_traces(
        experiment_ids=[experiment_id],
        filter_string=f"metadata.feature_flag_{flag_name} = 'false'",
    )
    for t in control_traces:
        control_latency.append(t.info.execution_time_ms)

    treatment_traces = client.search_traces(
        experiment_ids=[experiment_id],
        filter_string=f"metadata.feature_flag_{flag_name} = 'true'",
    )
    for t in treatment_traces:
        treatment_latency.append(t.info.execution_time_ms)

    avg_control_latency = (
        sum(control_latency) / len(control_latency) if
        control_latency else 0
    )
    avg_treatment_latency = (
        sum(treatment_latency) / len(treatment_latency) if
        treatment_latency else 0
    )

    return {
        f"avg_latency_{flag_name}_off": avg_control_latency,
        f"avg_latency_{flag_name}_on": avg_treatment_latency,
    }

# Usage:
# perf_metrics = analyze_feature_flag_performance(
#     "your_exp_id", "new_retriever"
# )
# print(perf_metrics)
```

^[examples-analyzing-traces-databricks-on-aws.md]

### Key Steps

1. **Annotate the traces** with a metadata key like `feature_flag_<flag_name>` set to `'true'` or `'false'` at trace creation time. This is the responsibility of the application code that wraps the feature flag check. ^[examples-analyzing-traces-databricks-on-aws.md]
2. **Query** each state separately using `client.search_traces()` with a `filter_string` that matches the metadata value. ^[examples-analyzing-traces-databricks-on-aws.md]
3. **Collect** the `execution_time_ms` (or `execution_duration`) from each trace in that state. ^[examples-analyzing-traces-databricks-on-aws.md]
4. **Compute** the average (or any desired percentile) for each state and return a dictionary of summary metrics. ^[examples-analyzing-traces-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The tracing infrastructure that captures span-level and trace-level latency data.
- [Feature Flag](/concepts/feature-table.md) – A configuration toggle used to roll out new behavior gradually.
- A/B Testing with Traces – A broader methodology for comparing multiple variants using trace metadata.
- [Performance Monitoring with Traces](/concepts/performance-monitoring-with-mlflow-traces.md) – General techniques for profiling latency and identifying outliers.
- Experimental Design and Analysis – Principles for designing experiments so that flag‑based comparisons yield valid causal conclusions.
- mlflow.search_traces() API|Search traces programmatically – The `mlflow.search_traces()` API and filter syntax used to retrieve traces by metadata.

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
