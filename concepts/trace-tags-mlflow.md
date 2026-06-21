---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8abbb238fe0aa2ea0f4894757b360f136c08c4210996f82eb4caeedce00f378
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-tags-mlflow
    - TT(
    - Trace (MLflow)
    - Traces (MLflow)
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: Trace Tags (MLflow)
description: Mutable key-value pairs attached to MLflow traces for organization, search, and filtering; can be added or updated post-logging.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-18T10:48:35.811Z"
---

# Trace Tags (MLflow)

**Trace tags** in MLflow are key-value pairs attached to [[MLflow Trace|MLflow Traces]] for organization, search, and filtering. Unlike metadata, tags are mutable and can be updated after a trace is logged. Use tags for dynamic information that may change, such as user feedback, review status, or data quality assessments. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Tags versus Metadata

MLflow traces support two kinds of supplementary key-value pairs: ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

- **Tags** – Mutable. Can be updated after the trace is logged. Intended for information that may change, such as review status or data quality assessments.
- **Metadata** – Write-once. Immutable after logging. Intended for fixed information captured during execution, such as model version, environment, or system configuration.

This page focuses on tags. See [Trace Metadata (MLflow)](/concepts/trace-metadata-mlflow.md) for details on metadata.

## Prerequisites

To use trace tags, you need: ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

- MLflow 3.1.0 or later with the Databricks extras: `pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"`
- An [MLflow Experiment](/concepts/mlflow-experiment.md) created.

## Adding Tags During Trace Execution

If you are using automatic tracing or the MLflow Fluent API to create traces, you can add tags during the trace's execution by calling [`mlflow.update_current_trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace) with the `tags` argument. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

Example: ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```python
import mlflow

@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(tags={"fruit": "apple"})
    return x + 1

my_func(10)
```

If a tag key already exists, `mlflow.update_current_trace` updates it with the new value. If the key is not present, it adds the tag. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Modifying Tags After Trace Completion

To set or delete tags on a trace that has already been logged to the backend store, use: ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

- [`mlflow.set_trace_tag(trace_id, key, value)`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_trace_tag) – adds or updates a tag on an existing trace.
- [`mlflow.delete_trace_tag(trace_id, key)`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.delete_trace_tag) – removes a tag from an existing trace.

Example: ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```python
import mlflow

@mlflow.trace
def process_data(data):
    return data.upper()

result = process_data("hello world")
trace_id = mlflow.get_last_active_trace_id()

mlflow.set_trace_tag(trace_id=trace_id, key="review_status", value="approved")
mlflow.set_trace_tag(trace_id=trace_id, key="data_quality", value="high")
mlflow.delete_trace_tag(trace_id=trace_id, key="data_quality")
```

## Managing Tags via the UI

In the [MLflow UI](/concepts/mlflow.md), you can update or delete tags on a trace by navigating to the trace tab and clicking the pencil icon next to the tag you want to update. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

![Screenshot showing tag update interaction in the MLflow traces UI](https://assets.docs.databricks.com/_static/images/mlflow3/tracing/trace-set-tag.gif)

## Related Concepts

- [Trace Metadata (MLflow)](/concepts/trace-metadata-mlflow.md) – Immutable key-value pairs for traces
- [[MLflow Trace|MLflow Traces]] – The core trace object that tags are attached to
- MLflow Fluent API – The high-level API used to create and manage traces
- [Databricks Autologging](/concepts/databricks-autologging.md) – Automatic trace generation for common frameworks
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) – Organizing runs and traces under experiments

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
