---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 440b169eb3c0e8eaf284e679410754f25fa8daf7be6b79056a026c8db8ae985f
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mutability-rules-for-trace-tags-vs-metadata
    - MRFTTVM
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: Mutability Rules for Trace Tags vs Metadata
description: The distinction that tags are mutable after trace logging while metadata becomes immutable once a trace is logged, influencing how context should be attached.
tags:
  - mlflow
  - tracing
  - data-model
timestamp: "2026-06-18T14:19:44.259Z"
---

# Mutability Rules for Trace Tags vs Metadata

**Mutability Rules for Trace Tags vs Metadata** define the difference in how tags and metadata can be modified after a trace is logged in [MLflow Tracing](/concepts/mlflow-tracing.md). Understanding these rules is essential for designing reliable instrumentation in production GenAI applications, particularly when choosing where to store mutable versus immutable context.

## Overview

When adding context to traces, MLflow supports two distinct fields for storing data: `tags` and `metadata`. These fields differ fundamentally in their mutability: after a trace is logged and completed, **tags are mutable** but **metadata are immutable**. ^[add-context-to-traces-databricks-on-aws.md]

This distinction is by design. Unlike tags, metadata cannot be updated once the trace is logged, making it ideal for immutable identifiers like user and session IDs. ^[add-context-to-traces-databricks-on-aws.md]

## Tag Mutability

Tags are intended for data that may need to be updated or added after the trace has been recorded. They can be modified after a trace is logged. ^[add-context-to-traces-databricks-on-aws.md]

### Use Cases for Tags

- Application-specific context that may change after logging
- Categorization data such as `query_category`
- Ad-hoc annotations added during post-processing analysis

## Metadata Immutability

Metadata fields are **immutable** in the logged trace. Once a trace is completed and logged, metadata values cannot be changed. ^[add-context-to-traces-databricks-on-aws.md]

### Use Cases for Metadata

Metadata is ideal for data that must be reliably associated with a trace after logging: ^[add-context-to-traces-databricks-on-aws.md]

- **User identifiers** — The `mlflow.trace.user` field for associating traces with specific users
- **Session identifiers** — The `mlflow.trace.session` field for grouping traces belonging to multi-turn conversations
- **Execution environment** — The `mlflow.source.type` field for environment-specific analysis
- **Application version** — Deployment identifiers that should remain constant for a trace
- **Any other immutable context** — Data that should not be overwritten after the trace is complete

## Setting Tags and Metadata During Execution

Both tags and metadata are set during the application's execution by calling [`mlflow.update_current_trace()`](https://docs.databricks.com/aws/en/api_reference/python_api/mlflow.html?highlight=trace#mlflow.update_current_trace). After the application completes and a trace is logged, tags remain mutable while metadata becomes immutable. ^[add-context-to-traces-databricks-on-aws.md]

```python
import mlflow

mlflow.update_current_trace(
    metadata={
        "mlflow.trace.user": user_id,
        "mlflow.trace.session": session_id,
    },
    tags={
        "query_category": "chat",  # Example of a custom tag
    },
)
```

^[add-context-to-traces-databricks-on-aws.md]

## Accessing Tags and Metadata After Logging

After a trace is logged, tags and metadata can be accessed via: ^[add-context-to-traces-databricks-on-aws.md]

- The `metadata` and `tags` fields in the pandas DataFrame returned by `mlflow.search_traces()`
- The [`Trace.info.trace_metadata`](https://docs.databricks.com/aws/en/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo.trace_metadata) and [`Trace.info.tags`](https://docs.databricks.com/aws/en/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo.tags) fields from [`Trace`](https://docs.databricks.com/aws/en/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) objects

## Best Practices

- **Use metadata for immutable identifiers** — Standard metadata fields like `mlflow.trace.user` and `mlflow.trace.session` should be set as metadata to prevent accidental overwriting. ^[add-context-to-traces-databricks-on-aws.md]
- **Use tags for mutable context** — Store data that may need to be updated after logging (such as classification categories or post-hoc annotations) in tags. ^[add-context-to-traces-databricks-on-aws.md]
- **Set immutable data early** — Because metadata cannot be updated after the trace completes, ensure user, session, and environment identifiers are set during the application's execution, not after the trace is logged.
- **Plan for post-logging modifications** — If you anticipate needing to annotate or recategorize traces after they are logged, store that data in tags rather than metadata.

## Related Concepts

- [Adding Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) — The broader pattern for enriching traces with metadata and tags
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework that provides these mutability guarantees
- [Trace Info](/concepts/traceinfo.md) — The entity object that exposes trace metadata and tags after logging
- Searching Traces Programmatically — Using `mlflow.search_traces()` to access trace metadata and tags

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
