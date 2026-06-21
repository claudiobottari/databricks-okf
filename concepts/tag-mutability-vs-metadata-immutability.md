---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08d15808d1065529b63e82e0443e98ea73c793b7b1ac23c4e8805aad5b0f992f
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tag-mutability-vs-metadata-immutability
    - TMVMI
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
      start: 75
      end: 83
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
      start: 85
      end: 110
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
      start: 112
      end: 114
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
      start: 43
      end: 60
title: Tag Mutability vs Metadata Immutability
description: Design distinction in MLflow tracing where tags are mutable (updateable after logging) while metadata is write-once and immutable once set.
tags:
  - mlflow
  - tracing
  - design
timestamp: "2026-06-19T14:04:21.171Z"
---

# Tag Mutability vs Metadata Immutability

**Tag Mutability vs Metadata Immutability** describes the fundamental difference in how tags and metadata can be modified after being attached to [[MLflow Trace|MLflow Traces]]. Tags are mutable and can be updated or deleted at any time, while metadata is write-once and immutable after it is logged.

## Overview

When adding key-value pairs to traces for organization, search, and filtering, both tags and metadata serve similar purposes but have distinct lifecycle characteristics. Understanding these differences is essential for choosing the right storage type for different kinds of information.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

| Property | Tags | Metadata |
|----------|------|----------|
| **Mutability** | Mutable — can be updated after a trace is logged | Immutable — write-once, cannot be changed after logging |
| **Update behavior** | If a key exists, the value is updated with the new value | If a key already exists, the operation is ignored and the original value remains unchanged |
| **Deletion** | Can be deleted individually | Not deletable |

## Tags: Mutable Information

Use tags for dynamic information that may change over time, such as user feedback, review status, or data quality assessments. Tags provide flexibility for post-hoc annotation of traces.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Setting Tags During Execution

When using [Automatic Tracing](/concepts/automatic-tracing.md) or fluent APIs, use `mlflow.update_current_trace(tags={...})` to add tags to the current trace during its execution. If a tag key is not already present, it is added; if the key is already present, the value is updated with the new value.^[attach-custom-tags-and-metadata-databricks-on-aws.md:75-83]

```python
@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(tags={"fruit": "apple"})
    return x + 1

my_func(10)
```

### Setting and Deleting Tags After Completion

To set tags on a trace that has already been completed and logged in the backend store, use `mlflow.set_trace_tag`. To remove a tag, use `mlflow.delete_trace_tag`.^[attach-custom-tags-and-metadata-databricks-on-aws.md:85-110]

```python
import mlflow

@mlflow.trace
def process_data(data):
    return data.upper()

result = process_data("hello world")

trace_id = mlflow.get_last_active_trace_id()

# Set tags after trace completion
mlflow.set_trace_tag(trace_id=trace_id, key="review_status", value="approved")
mlflow.set_trace_tag(trace_id=trace_id, key="data_quality", value="high")

# Delete a tag
mlflow.delete_trace_tag(trace_id=trace_id, key="data_quality")
```

Alternatively, tags can be updated or deleted from the [MLflow UI](/concepts/mlflow.md) by navigating to the trace tab and clicking the pencil icon next to the tag.^[attach-custom-tags-and-metadata-databricks-on-aws.md:112-114]

## Metadata: Immutable Information

Use metadata for fixed information captured during execution, such as model version, environment, or system configuration. Because metadata cannot be changed after it is set, it is ideal for recording immutable facts about a trace's origin.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Setting Metadata During Execution

Use `mlflow.update_current_trace(metadata={...})` to add metadata to the trace during its execution. If you try to update metadata with a key that already exists, the operation is ignored and the original value remains unchanged.^[attach-custom-tags-and-metadata-databricks-on-aws.md:43-60]

```python
import mlflow

@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(metadata={
        "model_version": "v1.2.3",
        "environment": "production"
    })
    return x + 1

my_func(10)
```

### No Post-Completion Modification

There is no equivalent of `set_trace_tag` for metadata. Once a trace is completed and logged, metadata cannot be added, updated, or deleted. All metadata must be set during trace execution.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Best Practices

- **Use tags for post-hoc annotations** such as human feedback, review approvals, or quality scores that may be updated after the trace is logged.
- **Use metadata for immutable execution context** such as the exact model version, environment name, or system configuration that was in effect when the trace was created.
- **Set metadata early in execution** because it cannot be added after the trace completes.
- **Leverage tag deletion** to clean up temporary or incorrect annotations without affecting the permanent record.

## Related Concepts

- [[MLflow Trace|MLflow Traces]] — The core tracing infrastructure
- [Automatic Tracing](/concepts/automatic-tracing.md) — How traces are automatically captured
- Attach Context to Traces — Tracking users, sessions, versions, and environments
- mlflow.search_traces() API|Search Traces Programmatically — Filtering and searching traces using tags and metadata
- [MLflow UI](/concepts/mlflow.md) — User interface for viewing and managing traces

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
2. [attach-custom-tags-and-metadata-databricks-on-aws.md:75-83](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
3. [attach-custom-tags-and-metadata-databricks-on-aws.md:85-110](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
4. [attach-custom-tags-and-metadata-databricks-on-aws.md:112-114](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
5. [attach-custom-tags-and-metadata-databricks-on-aws.md:43-60](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
