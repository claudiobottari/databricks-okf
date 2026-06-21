---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 419c519eba73646944e1efeee83cd60da77a764dfbf82a68e0203be13c1688c8
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-metadata
    - Table Metadata
    - Table metadata
    - Metadata
    - Trace Metadata vs Tags
    - mlflow-trace-metadata
    - MTM
    - MLflow metadata
    - MLflow Trace Metadata Management
    - trace-metadata-in-mlflow
    - TMIM
    - trace-metadata-mlflow
    - TM(
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
title: Trace Metadata
description: Immutable write-once key-value pairs attached to MLflow traces for fixed information such as model version, environment, or system configuration.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T14:03:58.996Z"
---

# Trace Metadata

**Trace Metadata** refers to immutable key-value pairs attached to an [[MLflow Trace]] to capture fixed information about the execution, such as model version, environment, or system configuration. Unlike [Trace Tags](/concepts/trace-tags.md), metadata is write-once and cannot be updated after it is logged.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Characteristics

- **Immutability:** Once a metadata key is set, its value cannot be changed. Attempting to update an existing key is silently ignored; the original value remains unchanged.^[attach-custom-tags-and-metadata-databricks-on-aws.md]
- **Purpose:** Use metadata for information that is determined at runtime and should not change, such as the version of a deployed model, the training environment, or a unique run identifier.^[attach-custom-tags-and-metadata-databricks-on-aws.md]
- **Contrast with tags:** Tags are mutable and can be set or deleted after a trace is logged. Metadata is fixed once written.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Setting Trace Metadata

Metadata can be added to a trace during its execution using the [`mlflow.update_current_trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace) function. This function is intended for use inside a traced function (decorated with `@mlflow.trace`). The metadata argument accepts a dictionary of string keys and values.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

### Example

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

In this example, the metadata keys `model_version` and `environment` are permanently recorded on the trace created for `my_func`. Attempting to call `mlflow.update_current_trace` again with the same key (e.g., `model_version`) will have no effect.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Requirements

- MLflow version 3.1.0 or later (with the Databricks extras) is required.^[attach-custom-tags-and-metadata-databricks-on-aws.md]
- Metadata can only be set during the active execution of a traced function; there is no API to modify metadata after the trace has been finalized.^[attach-custom-tags-and-metadata-databricks-on-aws.md]

## Related Concepts

- [Trace Tags](/concepts/trace-tags.md) – Mutable annotations that can be added or removed post-hoc.
- [[MLflow Trace|MLflow Traces]] – The overall mechanism for recording execution details.
- Attach Custom Traces and Metadata – Full guide for managing trace annotations.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The broader system for experiment logging, of which traces are a part.

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
