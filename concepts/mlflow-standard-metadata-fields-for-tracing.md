---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e52ae7d26b17840e2d5d6e704de59c39dfaacf03f08c4ff6ca730959c5188dd5
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-standard-metadata-fields-for-tracing
    - MSMFFT
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: MLflow Standard Metadata Fields for Tracing
description: Predefined metadata keys like mlflow.trace.user and mlflow.trace.session that MLflow recognizes for filtering, grouping, and UI integration in trace analytics.
tags:
  - mlflow
  - tracing
  - metadata
timestamp: "2026-06-18T14:19:12.941Z"
---

# MLflow Standard Metadata Fields for Tracing

**MLflow Standard Metadata Fields for Tracing** are predefined key-value pairs that you can attach to traces to capture contextual information such as user identity, session membership, deployment environment, and application version. These fields enable filtering, grouping, and analysis of traces in the MLflow UI and SDK. ^[add-context-to-traces-databricks-on-aws.md]

## Overview

When instrumenting a GenAI application with [MLflow Tracing](/concepts/mlflow-tracing.md), you can add context by calling `mlflow.update_current_trace()` with `metadata` and/or `tags`. Metadata fields are **immutable** once the trace is logged, while tags are mutable. Standard metadata fields are a set of specially recognized keys that MLflow uses to enable automatic UI features such as filtering and grouping. ^[add-context-to-traces-databricks-on-aws.md]

## Standard Fields for Users and Sessions

MLflow provides two standard metadata fields for tracking user identity and conversation flow:

| Field | Purpose |
|-------|---------|
| `mlflow.trace.user` | Associates traces with a specific user ID. |
| `mlflow.trace.session` | Groups traces that belong to the same multi-turn conversation or session. |

^[add-context-to-traces-databricks-on-aws.md]

When you set these fields, MLflow automatically enables filtering and grouping in the UI. Unlike tags, metadata cannot be updated after the trace is logged, making these fields suitable for immutable identifiers like user and session IDs. ^[add-context-to-traces-databricks-on-aws.md]

### Example

```python
import mlflow

mlflow.update_current_trace(
    metadata={
        "mlflow.trace.user": user_id,
        "mlflow.trace.session": session_id,
    }
)
```

^[add-context-to-traces-databricks-on-aws.md]

## Standard Fields for Environments and Versions

For deployment context, MLflow provides standard metadata fields that describe the execution environment and application version. These fields support environment-specific analysis and regression detection across versions.

The source notes that deployment metadata should generally be extracted from environment variables rather than hard-coded. Common examples include:

| Example Field | Description |
|---------------|-------------|
| `mlflow.source.type` | Execution environment (e.g., `development`, `staging`, `production`). |
| `mlflow.source.name` | Application or deployment name. |

^[add-context-to-traces-databricks-on-aws.md]

### Example

```python
import mlflow
import os

mlflow.update_current_trace(
    metadata={
        "mlflow.source.type": os.getenv("APP_ENVIRONMENT", "development"),
    }
)
```

^[add-context-to-traces-databricks-on-aws.md]

## Automatically Populated Metadata

MLflow automatically sets certain standard metadata fields based on the execution environment. These auto-populated values can be overridden using `mlflow.update_current_trace()` if the automatic detection does not meet your requirements. For example:

```python
mlflow.update_current_trace(metadata={"mlflow.source.name": "custom_name"})
```

^[add-context-to-traces-databricks-on-aws.md]

The full list of auto-populated fields is documented in the [MLflow Tracing](/concepts/mlflow-tracing.md) documentation](https://mlflow.org/docs/latest/genai/tracing/track-environments-context/#automatically-populated-tags) (referenced in the source). ^[add-context-to-traces-databricks-on-aws.md]

## Custom Metadata

In addition to the standard fields, you can add any custom metadata keys to capture application-specific context such as application version, deployment ID, deployment region, or feature flags. ^[add-context-to-traces-databricks-on-aws.md]

## Best Practices

1. **Consistent ID formats** – Use standardized formats for user and session IDs across your application.
2. **Session boundaries** – Define clear rules for when sessions start and end.
3. **Environment variables** – Populate metadata from environment variables rather than hard-coding values.
4. **Combine context types** – Track user, session, and environment context together for complete traceability.
5. **Override defaults thoughtfully** – Only override automatically populated metadata when necessary.

^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The tracing system that uses these metadata fields.
- [Trace Context](/concepts/mlflow-trace-context.md) – Broader concept of adding metadata to traces.
- mlflow.search_traces() API|Search Traces Programmatically – Using `mlflow.search_traces()` to query traces by metadata.
- Add Context to Traces Tutorial – Full tutorial on adding user, session, and environment metadata.

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
