---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 32416f176c06ca75cc6f4c39434e5599bbb51b29822f6075d0bfc20021b15043
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-tags
    - MTT
    - mlflow.set_trace_tag
    - MLflow Tags
    - MLflow tags
    - Tags in MLflow Traces|tags
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: MLflow Trace Tags
description: Mutable key-value pairs attached to MLflow traces for dynamic metadata like user feedback, review status, and data quality assessments.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T22:08:32.861Z"
---

```markdown
---
title: MLflow Trace Tags
summary: Mutable key-value pairs attached to MLflow traces for organization, search, and filtering; can be updated after a trace is logged.
sources:
  - attach-custom-tags-and-metadata-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T17:35:41.435Z"
updatedAt: "2026-06-19T17:35:41.435Z"
tags:
  - mlflow
  - tracing
  - tags
aliases:
  - mlflow-trace-tags
  - MTT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# MLflow Trace Tags

**MLflow Trace Tags** are mutable key-value pairs that can be attached to [[MLflow Trace|MLflow Traces]] for organization, search, and filtering purposes. Unlike [[MLflow Trace Metadata]], which is immutable after logging, tags can be updated or deleted after a trace has been completed and logged to the backend store. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Overview

Tags are designed for dynamic information that may change over time, such as user feedback, review status, or data quality assessments. This mutability distinguishes them from metadata, which is write-once and intended for fixed information captured during trace execution. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

Common use cases for tags include:
- Marking traces for manual review
- Recording user feedback or ratings
- Tracking data quality assessments
- Adding workflow or pipeline stage identifiers

## Setting Tags During Trace Execution

When using automatic tracing or fluent APIs, you can add tags to the current trace during its execution using the [`mlflow.update_current_trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace) function. The following example adds a `"fruit": "apple"` tag to the trace created for a traced function: ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```python
@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(tags={"fruit": "apple"})
    return x + 1

my_func(10)
```

The `mlflow.update_current_trace` function adds the specified tag when the key is not already present. If the key already exists, it updates the key with the new value. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Setting and Deleting Tags on Completed Traces

To manage tags on traces that have already been completed and logged to the backend store, MLflow provides two dedicated methods: ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

- [`mlflow.set_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_trace_tag) — Sets a tag on a trace.
- [`mlflow.delete_trace_tag`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.delete_trace_tag) — Removes a tag from a trace.

The following example demonstrates both operations: ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

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

## Managing Tags via the MLflow UI

Tags can also be updated or deleted from the MLflow UI. Navigate to the trace tab and click the pencil icon next to the tag you want to update. This provides a visual interface for managing trace annotations without requiring code changes. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace Metadata]] — Immutable key-value pairs for fixed trace information
- [[MLflow Trace|MLflow Traces]] — The core trace object that tags are attached to
- mlflow.search_traces() API|Search Traces Programmatically — Filtering and querying traces using tags
- [[MLflow Experiment|MLflow Experiments]] — Organizational unit for traces and runs

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md
```

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
