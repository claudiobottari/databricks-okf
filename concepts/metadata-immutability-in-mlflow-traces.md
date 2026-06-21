---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 193048633feb73d0c0a3c6c2319133b2ad2ae20ccd1c5b706445d226cc201f88
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metadata-immutability-in-mlflow-traces
    - MIIMT
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: Metadata Immutability in MLflow Traces
description: The constraint that trace metadata is immutable once set — attempting to update an existing metadata key is silently ignored.
tags:
  - MLflow
  - tracing
  - design-patterns
timestamp: "2026-06-18T14:28:07.340Z"
---

# Metadata Immutability in MLflow Traces

**Metadata immutability** is a core property of [[MLflow Trace|MLflow Traces]]: once metadata has been logged to a trace, its key-value pairs cannot be modified or overwritten. This write-once behavior ensures that execution-time context captured during a trace remains stable and verifiable for auditing, reproducibility, and downstream analysis. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## How Metadata Immutability Works

When you set metadata on a trace using `mlflow.update_current_trace()`, the provided key-value pairs are recorded at that point in the trace's execution. Any subsequent attempt to update an already-set metadata key is silently ignored — the original value persists unchanged. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```python
import mlflow

@mlflow.trace
def my_func(x):
    mlflow.update_current_trace(metadata={"model_version": "v1.2.3", "environment": "production"})
    # Any later call trying to change "model_version" will be ignored
    return x + 1

my_func(10)
```

If you attempt to update metadata with a key that already exists, the operation will be ignored and the original value will remain unchanged. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Metadata vs. Tags

The immutability distinction between metadata and tags is by design, supporting different use cases:

| Property | Metadata | Tags |
|----------|----------|------|
| Mutability | Immutable (write-once) | Mutable (can be updated) |
| When set | During trace execution only | During or after trace execution |
| Modification behavior | Updates to existing keys are silently ignored | Existing keys are overwritten with new values |
| Deletion | Not supported | Supported via `mlflow.delete_trace_tag()` |
| Typical use | Fixed information captured during execution (model version, environment, system configuration) | Dynamic information that may change (user feedback, review status, data quality assessments) |

^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### When to Use Each

- **Use metadata** for information that must remain fixed and verifiable after the trace is created. This includes model version identifiers, deployment environment names, system configuration parameters, or any other context that should be immutable for auditing or compliance purposes. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]
- **Use [Tags in MLflow Traces|tags](/concepts/mlflow-trace-tags.md)** for information that may change over time, such as user feedback ratings, review statuses, or data quality assessments. Tags can be added, updated, or deleted even after a trace is completed and logged. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Setting Metadata During Trace Execution

Metadata can only be set during the execution of a traced function or span. Use `mlflow.update_current_trace()` within the body of a function decorated with `@mlflow.trace` to attach metadata to the currently active trace. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

```python
import mlflow

@mlflow.trace
def process_data(data):
    mlflow.update_current_trace(metadata={
        "model_version": "v1.2.3",
        "environment": "production",
        "run_id": "abc123"
    })
    return data.upper()

process_data("hello world")
```

This approach ensures that the metadata is recorded as part of the trace's execution context and becomes immutable after the function completes. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Searching and Filtering with Metadata

Because metadata is immutable and reliably recorded, it serves as a stable foundation for searching and filtering traces programmatically. You can use metadata keys and values to identify traces from specific model versions, environments, or execution configurations, confident that those values will not have changed since the trace was created. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

To search traces using metadata, see mlflow.search_traces() API|Search Traces Programmatically. ^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Related Concepts

- Tags in MLflow Traces — Mutable key-value pairs for dynamic trace metadata
- [[MLflow Trace|MLflow Traces]] — The overall tracing system for capturing execution context
- mlflow.search_traces() API|Search Traces Programmatically — Filtering and searching traces via SDK
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) — Tracking users, sessions, versions, and environments

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
