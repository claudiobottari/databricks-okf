---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dceb4e684cd02bc136493ab980eaaa12a88515f8ff50e12f131c263f5be8d80f
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowupdate_current_trace-api
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: mlflow.update_current_trace API
description: Function used during trace execution to add metadata or tags to the currently active trace via fluent or automatic tracing APIs.
tags:
  - mlflow
  - api
  - tracing
timestamp: "2026-06-19T17:36:45.850Z"
---

# `mlflow.update_current_trace()` API

The **`mlflow.update_current_trace()`** function adds metadata and tags to the currently active trace while a traced function is executing. It enables you to enrich tracing context with dynamic information captured during execution, such as user identity, session identifiers, environment, model version, or any other application-specific data. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Overview

`mlflow.update_current_trace()` works with automatic tracing or fluent APIs to modify the active trace during its execution. It accepts two keyword arguments: `metadata` for immutable key-value pairs and `tags` for mutable key-value pairs. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Syntax

```python
mlflow.update_current_trace(metadata=None, tags=None)
```

### Parameters

- **`metadata`** (dict, optional): Immutable key-value pairs. Once set, metadata cannot be updated. If you try to update metadata with a key that already exists, the operation is ignored and the original value remains unchanged. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

- **`tags`** (dict, optional): Mutable key-value pairs. Tags can be added or updated during trace execution. If a tag key is already present, the specified value replaces the existing value. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Usage Examples

### Adding Metadata

The following example adds the `"model_version": "v1.2.3"` and `"environment": "production"` metadata to the trace created for the `my_func` function:

```python
import mlflow

@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(
        metadata={"model_version": "v1.2.3", "environment": "production"}
    )
    return x + 1

my_func(10)
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Adding Tags

The following example adds the `"fruit": "apple"` tag to the trace created for the `my_func` function:

```python
@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(tags={"fruit": "apple"})
    return x + 1

my_func(10)
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Key Characteristics

| Property | Metadata | Tags |
|----------|----------|------|
| **Mutability** | Immutable after setting | Mutable; can be updated |
| **Update behavior** | Ignores updates to existing keys | Replaces value for existing keys |
| **Use cases** | Fixed information captured during execution | Dynamic information that may change |
| **Examples** | Model version, environment, system configuration | User feedback, review status, data quality assessments |

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Post-Execution Tag Management

For traces already completed and logged to the backend store, use these separate methods instead of `mlflow.update_current_trace()`:

- **[mlflow.set_trace_tag](/concepts/mlflow-trace-tags.md)**: Set a tag on a completed trace.
- **mlflow.delete_trace_tag**: Remove a tag from a completed trace.

```python
import mlflow

@mlflow.trace
def process_data(data):
    return data.upper()

result = process_data("hello world")
trace_id = mlflow.get_last_active_trace_id()

# Set tags on the completed trace
mlflow.set_trace_tag(trace_id=trace_id, key="review_status", value="approved")
mlflow.set_trace_tag(trace_id=trace_id, key="data_quality", value="high")

# Delete a tag from the completed trace
mlflow.delete_trace_tag(trace_id=trace_id, key="data_quality")
```

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Best Practices

1. **Use metadata for fixed identifiers** – Store immutable information like model version, environment, and system configuration as metadata.
2. **Use tags for dynamic information** – Store mutable information like review status, data quality assessments, and user feedback as tags.
3. **Set context during execution** – Call `mlflow.update_current_trace()` inside the traced function to capture state that isn't available at decoration time.
4. **Consider metadata immutability** – Once set, metadata cannot be changed, so choose metadata keys carefully.
5. **Use post-execution methods for hindsight** – Use [mlflow.set_trace_tag](/concepts/mlflow-trace-tags.md) and mlflow.delete_trace_tag for information that becomes available after trace completion.

## Requirements

- MLflow version 3.1.0 or higher with the `mlflow[databricks]` extra installed.
- An existing MLflow experiment set up by following the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment).

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The tracing framework for observing GenAI agent executions.
- @mlflow.trace – Decorator that enables automatic tracing of a function.
- [mlflow.set_trace_tag](/concepts/mlflow-trace-tags.md) – Set a tag on a completed trace.
- mlflow.delete_trace_tag – Remove a tag from a completed trace.
- [Tags](/concepts/tag-based-access-gating.md) – Mutable key-value pairs on a trace.
- [Metadata](/concepts/trace-metadata.md) – Immutable key-value pairs on a trace.
- mlflow.search_traces()|mlflow.search_traces – API for retrieving logged traces.
- mlflow.get_last_active_trace_id – Get the trace ID of the most recently active trace.

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
