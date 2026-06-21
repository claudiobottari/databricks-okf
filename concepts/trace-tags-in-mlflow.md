---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2117491410b8ba5666a0cb61e652f6e15291fcc603853d0264ed3827231889fd
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-tags-in-mlflow
    - TTIM
    - Traces in MLflow
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: Trace Tags in MLflow
description: Mutable key-value pairs attached to MLflow traces for organization, search, and filtering, updatable during or after trace execution.
tags:
  - MLflow
  - tracing
  - observability
timestamp: "2026-06-18T14:27:43.023Z"
---

# Trace Tags in MLflow

**Trace Tags** are key-value pairs that can be attached to [[MLflow Trace|MLflow Traces]] to organize, search, and filter them. Tags are **mutable**—they can be updated after a trace has been logged—making them suitable for dynamic information such as user feedback, review status, or data quality assessments. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

This contrasts with **Trace Metadata**, which is write-once and immutable after logging; metadata is intended for fixed information captured during execution, such as model version, environment, or system configuration. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Setting Tags During Trace Execution

If you are using automatic tracing or the fluent APIs to create traces, you can add tags during the trace's execution using the `mlflow.update_current_trace()` function. This function adds the specified tag(s) to the current trace when the key is not already present; if the key is already present, it updates the key with the new value. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

The following example adds the `"fruit": "apple"` tag to the trace created for the `my_func` function:

```python
@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(tags={"fruit": "apple"})
    return x + 1

my_func(10)
```
^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Setting and Deleting Tags on Completed Traces

To set tags on a trace that has already been completed and logged in the backend store, use the `mlflow.set_trace_tag()` method to set a tag on a trace, and the `mlflow.delete_trace_tag()` method to remove a tag from a trace. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

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

## Updating Tags in the MLflow UI

Alternatively, you can update or delete tags on a trace from the MLflow UI. To do this, navigate to the **Traces** tab, then click on the pencil icon next to the tag you want to update. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

![Traces tag update](https://assets.docs.databricks.com/_static/images/mlflow3/tracing/trace-set-tag.gif)^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Prerequisites

Before using trace tags, you must:

1. Install MLflow and required packages:
   ```bash
   pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"
   ```
2. Create an MLflow experiment by following the setup your environment quickstart. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Related Concepts

- [Trace Metadata](/concepts/trace-metadata.md) — immutable key-value pairs for fixed information
- [[MLflow Trace|MLflow Traces]] — the trace data structure that tags attach to
- Searching Traces Programmatically — filtering and searching traces using tags and metadata
- [Adding Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) — tracking users, sessions, versions, and environments

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
