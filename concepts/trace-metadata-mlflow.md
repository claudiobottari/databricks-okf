---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f82056b496ec204adf422b71d5a52140ed279fed8f2db8149e6bf344b242d65a
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-metadata-mlflow
    - TM(
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: Trace Metadata (MLflow)
description: Immutable, write-once key-value pairs attached to MLflow traces for fixed information like model version or environment; cannot be updated after logging.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-18T10:49:00.395Z"
---

# Trace Metadata (MLflow)

**Trace Metadata** in MLflow refers to key-value pairs attached to traces for organization, search, and filtering. MLflow distinguishes between two types of trace annotations — **tags** and **metadata** — each with different mutability characteristics and use cases.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Tags vs. Metadata

| Property | Tags | Metadata |
|---|---|---|
| Mutability | Mutable — can be updated after a trace is logged | Immutable — write-once, cannot be changed after being set |
| Use case | Dynamic information that may change, such as user feedback, review status, or data quality assessments | Fixed information captured during execution, such as model version, environment, or system configuration |

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Setting Metadata and Tags During Trace Execution

When using automatic tracing or fluent APIs to create traces, you can add metadata or tags during the trace's execution using the `mlflow.update_current_trace` function.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Adding Metadata

Use `mlflow.update_current_trace(metadata={...})` to set immutable metadata on the current trace:

```python
import mlflow

@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(
        metadata={
            "model_version": "v1.2.3",
            "environment": "production"
        }
    )
    return x + 1

my_func(10)
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

Metadata is immutable once set. If you attempt to update metadata with a key that already exists, the operation is ignored and the original value remains unchanged.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Adding Tags

Use `mlflow.update_current_trace(tags={...})` to add mutable tags to the current trace:

```python
@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(tags={"fruit": "apple"})
    return x + 1

my_func(10)
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

The `update_current_trace` function adds the specified tag(s) when the key is not already present. If the key already exists, it updates the key with the new value.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Managing Tags on Completed Traces

To set or remove tags on a trace that has already been completed and logged in the backend store, use the following methods:^[attach-custom-tags-and-metadata-databricks-on-aws.md]

- `mlflow.set_trace_tag(trace_id, key, value)` — Sets a tag on a completed trace
- `mlflow.delete_trace_tag(trace_id, key)` — Removes a tag from a completed trace

```python
import mlflow

# Create and execute a traced function
@mlflow.trace
def process_data(data):
    return data.upper()

# Execute the function to create a trace
result = process_data("hello world")

# Get the trace_id from the most recent trace
trace_id = mlflow.get_last_active_trace_id()

# Set a tag on the trace
mlflow.set_trace_tag(trace_id=trace_id, key="review_status", value="approved")

# Set another tag
mlflow.set_trace_tag(trace_id=trace_id, key="data_quality", value="high")

# Delete a tag from the trace
mlflow.delete_trace_tag(trace_id=trace_id, key="data_quality")
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Managing Tags from the MLflow UI

You can also update or delete tags on a trace from the MLflow UI. Navigate to the trace tab, then click the pencil icon next to the tag you want to update.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Prerequisites

To use trace metadata features, ensure you have:^[attach-custom-tags-and-metadata-databricks-on-aws.md]

- MLflow and required packages installed: `pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"`
- An MLflow experiment created by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment)

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The core tracing framework for GenAI applications
- [MLflow Runs](/concepts/mlflow-run.md) — The fundamental unit of logged experiments
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The logging component of MLflow
- GenAI Tracing with MLflow — Tracing for generative AI applications
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) — Tracking users, sessions, versions, and environments in traces
- mlflow.search_traces() API|Search Traces Programmatically — Filtering and searching traces using tags and metadata

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
