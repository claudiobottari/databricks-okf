---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c8c9680ffe04aa82af3497baa27676378c95e1d94e4c1d619a14097a0a079e41
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - error-monitoring-with-mlflow-traces
    - EMWMT
    - Error Monitoring with Traces
    - Error Monitoring Pattern
    - Production Monitoring with Traces
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: Error Monitoring with MLflow Traces
description: Pattern for detecting and analyzing errors in production GenAI traces using mlflow.search_traces() with status and time-window filters.
tags:
  - mlflow
  - tracing
  - error-monitoring
  - observability
timestamp: "2026-06-19T18:44:28.602Z"
---

# Error Monitoring with MLflow Traces

**Error monitoring with MLflow traces** is the practice of programmatically scanning production traces to detect, analyze, and diagnose failures in [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications. By querying trace metadata with `mlflow.search_traces()`, teams can identify error patterns, group failures by function, and inspect recent error samples without manual log digging. ^[examples-analyzing-traces-databricks-on-aws.md]

## How Error Monitoring Works

MLflow records every execution of a traced function as a [trace](/concepts/traces.md), and each trace carries a `status` field that can be `OK` or `ERROR`. When a span (or the root span) raises an unhandled exception, the trace is marked as `ERROR` and the error details are captured in the span’s `status.description`. ^[examples-analyzing-traces-databricks-on-aws.md]

The core monitoring function filters traces by `trace.status = 'ERROR'` and a time window, then aggregates results to surface actionable insights. The example below monitors all errors that occurred in the last hour.

### Basic Error Monitor

```python
import mlflow
import time
import pandas as pd

def monitor_errors(experiment_name: str, hours: int = 1):
    """Monitor errors in the last N hours."""
    current_time_ms = int(time.time() * 1000)
    cutoff_time_ms = current_time_ms - (hours * 60 * 60 * 1000)

    failed_traces = mlflow.search_traces(
        filter_string=f"trace.status = 'ERROR' AND "
                       f"trace.timestamp_ms > {cutoff_time_ms}",
        order_by=["trace.timestamp_ms DESC"]
    )

    if len(failed_traces) == 0:
        print(f"No errors found in the last {hours} hour(s)")
        return

    print(f"Found {len(failed_traces)} errors in the last {hours} hour(s)\n")

    # Group by function name
    error_by_function = failed_traces.groupby('tags.mlflow.traceName').size()
    print("Errors by function:")
    print(error_by_function.to_string())

    # Show recent error samples
    print("\nRecent error samples:")
    for _, trace in failed_traces.head(5).iterrows():
        print(f"- {trace['request_preview'][:60]}...")
        print(f"  Function: {trace.get('tags.mlflow.traceName', 'unknown')}")
        print(f"  Time: {pd.to_datetime(trace['timestamp_ms'], unit='ms')}")
        print()

    return failed_traces
```

^[examples-analyzing-traces-databricks-on-aws.md]

The function returns the pandas DataFrame of failed traces so further analysis can be chained.

## Using the `TraceAnalyzer` Utility

The TraceAnalyzer class (defined in the same source) provides a reusable `get_error_summary()` method that extracts errors at three levels:^[examples-analyzing-traces-databricks-on-aws.md]

- **Trace-level errors** – the overall trace status is `ERROR`.
- **Span-level errors** – individual spans that failed, including the span name, type, and error message.
- **Assessment-level errors** – if [Assessments](/concepts/assessments.md) (human feedback or LLM judge scores) recorded an error during logging.

```python
analyzer = TraceAnalyzer(trace)
errors = analyzer.get_error_summary()
for error in errors:
    print(f"  - {error['level']}: {error.get('message', error.get('error'))}")
```

^[examples-analyzing-traces-databricks-on-aws.md]

## Analyzing Error Patterns

Once you have a DataFrame of failed traces, common analysis steps include:

- **Grouping by trace name** to identify which functions fail most often.
- **Grouping by error message** (from `trace.response_preview` or span `status.description`) to spot recurring issues.
- **Time‑series analysis** to detect error spikes that correlate with deployments or traffic changes.

The `request_preview` column provides a truncated version of the input that triggered the failure, helping with root‑cause investigation.

## Best Practices

- **Set a retention window** for error monitoring to focus on recent incidents and avoid stale data.
- **Use consistent trace naming** (via the `tags.mlflow.traceName` tag) so grouping by function is reliable.
- **Combine with performance monitoring** to distinguish between errors and latency anomalies.
- **Automate alerting** by scheduling the `monitor_errors()` function run and triggering notifications when error counts exceed thresholds.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying framework that captures execution traces.
- Span – Individual unit of work within a trace; error spans carry `status.description`.
- mlflow.search_traces() API|Search Traces Programmatically – The `mlflow.search_traces()` API and filter syntax.
- TraceAnalyzer – Utility class for multi-level error extraction.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Broader monitoring practices including latency and quality.
- [Log Assessments](/concepts/assessments.md) – Adding feedback and expectations to traces.

## Sources

- examples-analyzing-traces-databricks-on-aws.md

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
