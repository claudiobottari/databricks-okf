---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 75375da7386b39674a886c1b9378df4db27e815d89903d11ce86cb98d5313e8f
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-automatically-populated-trace-metadata
    - MAPTM
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: MLflow Automatically Populated Trace Metadata
description: Standard metadata fields that MLflow automatically sets based on the execution environment, which can be overridden using mlflow.update_current_trace().
tags:
  - mlflow
  - tracing
  - metadata
timestamp: "2026-06-19T08:53:26.937Z"
---

# MLflow Automatically Populated Trace Metadata

**MLflow Automatically Populated Trace Metadata** are standard metadata fields that MLflow sets on each trace based on the execution environment in which the application runs. These fields provide automatic context about the source and environment of a trace without requiring explicit developer action. ^[add-context-to-traces-databricks-on-aws.md]

## How Automatic Population Works

When a traced application executes, MLflow inspects the runtime environment and writes certain metadata keys—such as the source name (`mlflow.source.name`) or source type—into the trace's metadata dictionary. The exact set of automatically populated fields is defined by the MLflow runtime and is documented in the [MLflow official documentation](https://mlflow.org/docs/latest/genai/tracing/track-environments-context/#automatically-populated-tags). ^[add-context-to-traces-databricks-on-aws.md]

## Overriding Automatically Populated Fields

You can override any automatically populated metadata field by calling [`mlflow.update_current_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace) with a `metadata` dictionary before the trace is completed. For example, to replace the automatic source name with a custom value: ^[add-context-to-traces-databricks-on-aws.md]

```python
import mlflow

mlflow.update_current_trace(
    metadata={
        "mlflow.source.name": "custom_name"
    }
)
```

Override only when the automatic detection does not match your requirements. ^[add-context-to-traces-databricks-on-aws.md]

## Mutability and Lifetime

Automatically populated metadata follows the same immutability rules as all other trace metadata: once a trace is logged, its `metadata` dictionary cannot be changed. To modify these fields, call `mlflow.update_current_trace()` *during execution* before the trace is finalized. ^[add-context-to-traces-databricks-on-aws.md]

Tags, on the other hand, remain mutable after logging and can be used for fields that need post-hoc updates. ^[add-context-to-traces-databricks-on-aws.md]

## Best Practices

- **Do not rely on automatic metadata for critical identifiers** — if a field must be present with a specific value, explicitly set it via `mlflow.update_current_trace()`.
- **Prefer environment variables** for deployment-specific overrides, as recommended in the general [add-context-to-traces](add-context-to-traces-databricks-on-aws.md) guidance.
- **Review the automatically populated fields** in the MLflow documentation to understand what is captured by default before deciding which fields to override. ^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [Add context to traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) – General guide for enriching traces with metadata and tags.
- [MLflow Trace Metadata](/concepts/mlflow-trace-metadata.md) – The full set of standard and custom metadata fields available.
- mlflow.update_current_trace() – API method for setting or overriding trace metadata.
- [Standard metadata fields for traces](/concepts/standardized-metadata-fields-for-traces.md) – Reference for `mlflow.trace.*` and `mlflow.source.*` fields.
- mlflow.search_traces() API|Search traces programmatically – How to query traces by metadata using `mlflow.search_traces()`.

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
