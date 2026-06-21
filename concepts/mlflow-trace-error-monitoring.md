---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c8c388e07170b1555943ee509aa7c91dea50116bd7ed3d9831365626450a0a9
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-error-monitoring
    - MTEM
    - MLflow monitoring API
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: MLflow Trace Error Monitoring
description: Patterns for programmatically monitoring and analyzing trace errors using mlflow.search_traces() with status filters, time windows, and error aggregation by function name.
tags:
  - mlflow
  - error-monitoring
  - tracing
  - observability
timestamp: "2026-06-19T10:25:46.088Z"
---

# MLflow Trace Error Monitoring

**MLflow Trace Error Monitoring** refers to the practice of systematically detecting, collecting, and analyzing error events across [GenAI](/concepts/mlflow-genai-evaluate-api.md) application traces using the [MLflow Tracing](/concepts/mlflow-tracing.md) SDK. By querying traces with an `ERROR` status and examining span-level failures, teams can identify recurring issues, diagnose root causes, and track error trends over time. ^[examples-analyzing-traces-databricks-on-aws.md]

## Core Concepts

Error monitoring relies on the `mlflow.search_traces()` API to retrieve traces that have a `trace.status` of `ERROR`. A typical monitoring function filters traces within a configurable time window (e.g., the last *N* hours) and orders them by descending timestamp to surface the most recent failures first. ^[examples-analyzing-traces-databricks-on-aws.md]

```python
failed_traces = mlflow.search_traces(
    filter_string=f"trace.status = 'ERROR' AND "
                  f"trace.timestamp_ms > {cutoff_time_ms}",
    order_by=["trace.timestamp_ms DESC"]
)
```

### Error Analysis

Once error traces are retrieved, common analysis steps include:

- **Grouping by function name**: Using `tags.mlflow.traceName` to count how many errors occur per traced function. This highlights which parts of the application are most failure-prone.
- **Sampling recent errors**: Displaying the request preview, function name, and timestamp of the most recent error traces for quick inspection.

A complete monitoring function returns the `failed_traces` DataFrame for further programmatic evaluation. ^[examples-analyzing-traces-databricks-on-aws.md]

## The `TraceAnalyzer` Utility

The `TraceAnalyzer` class provides a reusable `get_error_summary()` method that extracts errors from three levels of a trace:

1. **Trace-level**: Checks if the trace’s overall state is `ERROR`.
2. **Span-level**: Iterates through all spans and collects any span whose status code is `ERROR`, capturing the span name, type, description, and ID.
3. **Assessment-level**: Looks for errors logged in assessments (e.g., via `mlflow.log_feedback()`).

This structured summary makes it easy to programmatically alert on or visualize error patterns. ^[examples-analyzing-traces-databricks-on-aws.md]

## Example Usage

The following snippet demonstrates a typical error monitoring workflow:

```python
monitor_errors("my_experiment", hours=1)
```

This function prints the error count, a breakdown by traced function, and the five most recent error samples. It also returns the raw `failed_traces` DataFrame for further analysis. ^[examples-analyzing-traces-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of the tracing system and span model.
- mlflow.search_traces() API|Search Traces API – Details on `mlflow.search_traces()` filtering and ordering.
- Trace Status – Possible values (OK, ERROR, etc.) and their meanings.
- [Span Analysis](/concepts/span-search-and-analysis.md) – Inspecting individual spans for errors and performance.
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – Using traces to assess agent quality and correctness.
- [Log Assessments](/concepts/assessments.md) – Adding human or LLM-judge feedback to traces.

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
