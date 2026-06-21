---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cd1c99f0cd2cd6d9f170339d4e7a09556c6868fb374f09efc96edd3c60a9a0dc
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-flag-ab-performance-analysis-using-traces
    - FFAPAUT
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: Feature flag A/B performance analysis using traces
description: Pattern for comparing latency distributions between control and treatment groups in feature flag experiments by filtering traces on metadata tags.
tags:
  - mlflow
  - a-b-testing
  - feature-flags
  - experimentation
timestamp: "2026-06-18T12:15:21.477Z"
---

# Feature Flag A/B Performance Analysis Using Traces

**Feature flag A/B performance analysis using traces** refers to the practice of comparing latency and other performance metrics between two variants of a GenAI application controlled by a feature flag, using execution traces captured by [MLflow Tracing](/concepts/mlflow-tracing.md). This approach enables data-driven decisions about which configuration delivers better performance before promoting changes to production.

## Overview

Feature flags allow teams to toggle between different application behaviors — such as using a new retriever algorithm, a different model, or an alternative prompt template. By instrumenting the application with [MLflow Tracing](/concepts/mlflow-tracing.md) and tagging traces with the feature flag's state, you can systematically compare performance characteristics across variants. ^[examples-analyzing-traces-databricks-on-aws.md]

The analysis typically focuses on latency (execution time), but can also examine token usage, error rates, and span-level performance breakdowns. The core workflow involves:

1. Adding the feature flag state as a trace attribute or [trace tag](/concepts/trace-tags.md)
2. Collecting traces from both control and treatment groups
3. Querying and comparing trace data programmatically

## Adding Feature Flag Context to Traces

To enable A/B analysis, each trace must carry metadata indicating which feature flag variant was active during execution. This is typically done by adding the flag state as a trace tag or attribute at the start of the traced operation.

```python
import mlflow

@mlflow.trace
def rag_pipeline(question: str):
    # Add feature flag state as trace metadata
    mlflow.update_current_trace(
        tags={
            "feature_flag_new_retriever": str(NEW_RETRIEVER_ENABLED),
            "experiment_id": "exp_ab_test_001"
        }
    )
    # ... rest of pipeline
```

By using consistent tag keys (e.g., `feature_flag_<flag_name>`), you can later filter traces by flag state when querying. ^[examples-analyzing-traces-databricks-on-aws.md]

## Querying Traces by Feature Flag State

The `mlflow.search_traces()` API allows filtering by trace tags and metadata. To compare performance between variants, you query separate trace sets for each flag state. ^[examples-analyzing-traces-databricks-on-aws.md]

```python
import mlflow

# Query control group (flag off)
control_traces = mlflow.search_traces(
    experiment_ids=["your_experiment_id"],
    filter_string="tag.`feature_flag_new_retriever` = 'false'",
)

# Query treatment group (flag on)
treatment_traces = mlflow.search_traces(
    experiment_ids=["your_experiment_id"],
    filter_string="tag.`feature_flag_new_retriever` = 'true'",
)
```

## Example: Latency Comparison

The most common A/B performance analysis compares latency distributions between control and treatment groups. ^[examples-analyzing-traces-databricks-on-aws.md]

```python
def analyze_feature_flag_performance(experiment_id: str, flag_name: str):
    """Analyze performance differences between feature flag states."""
    control_latency = []
    treatment_latency = []

    control_traces = mlflow.search_traces(
        experiment_ids=[experiment_id],
        filter_string=f"tag.`feature_flag_{flag_name}` = 'false'",
    )
    for t in control_traces:
        control_latency.append(t.info.execution_time_ms)

    treatment_traces = mlflow.search_traces(
        experiment_ids=[experiment_id],
        filter_string=f"tag.`feature_flag_{flag_name}` = 'true'",
    )
    for t in treatment_traces:
        treatment_latency.append(t.info.execution_time_ms)

    avg_control_latency = sum(control_latency) / len(control_latency) if control_latency else 0
    avg_treatment_latency = sum(treatment_latency) / len(treatment_latency) if treatment_latency else 0

    return {
        f"avg_latency_{flag_name}_off": avg_control_latency,
        f"avg_latency_{flag_name}_on": avg_treatment_latency
    }
```

This function returns the average latency for each variant, enabling a quick comparison. For more robust analysis, you can extend it to calculate percentiles (P50, P95, P99) and identify latency outliers. ^[examples-analyzing-traces-databricks-on-aws.md]

## Advanced Analysis

### Performance Profiling by Span Type

Beyond overall latency, you can analyze how the feature flag affects specific components of the pipeline — such as retrieval, LLM calls, or tool usage. Use the TraceAnalyzer utility to break down execution time by span type for each variant. ^[examples-analyzing-traces-databricks-on-aws.md]

### Error Rate Comparison

The same tag-based filtering can identify whether a feature flag variant introduces more errors. Query traces filtered by `trace.status = 'ERROR'` in combination with the flag state tag to compare error rates. ^[examples-analyzing-traces-databricks-on-aws.md]

### Token Usage Analysis

For LLM-based applications, A/B comparisons can include token consumption. By aggregating `llm.token_usage` attributes across spans for each variant, you can determine whether a change reduces cost or increases output quality. ^[examples-analyzing-traces-databricks-on-aws.md]

## Best Practices

- **Use consistent tag naming.** Adopt a convention like `feature_flag_<flag_name>` for all feature flag trace tags to simplify queries.
- **Filter by experiment ID.** Always scope queries to a specific experiment to avoid mixing unrelated traces.
- **Collect sufficient samples.** Ensure each variant has enough traces for statistically meaningful comparison.
- **Control for time windows.** Compare variants from the same time period to avoid confounding factors (e.g., traffic spikes or model rotations).
- **Combine with assessments.** Use `mlflow.log_feedback()` to add human feedback or [LLM judge](/concepts/llm-judges.md) assessments to traces, enabling quality comparisons alongside performance metrics. ^[examples-analyzing-traces-databricks-on-aws.md]

## Limitations

- The analysis assumes consistent tagging; missing or incorrect flag tags can produce misleading results.
- Latency comparisons may be affected by external factors (e.g., [Model Serving](/concepts/model-serving.md) queue times, network latency) that are not captured by the feature flag itself.
- For statistically rigorous conclusions, consider using dedicated A/B testing frameworks that control for sample size and significance thresholds.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework that captures execution information
- [Trace Tags and Attributes](/concepts/trace-tags-and-metadata.md) — Metadata used to tag traces with feature flag state
- mlflow.search_traces() API|Search Traces Programmatically — The API for querying traces by filters
- [Performance Monitoring with Traces](/concepts/performance-monitoring-with-mlflow-traces.md) — Broader performance analysis patterns
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Similar methodology for comparing agent behaviors using custom judges
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for grouping related traces
- [TraceAnalyzer Utility](/concepts/traceanalyzer-reusable-utility-class.md) — A reusable class for comprehensive trace analysis

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
