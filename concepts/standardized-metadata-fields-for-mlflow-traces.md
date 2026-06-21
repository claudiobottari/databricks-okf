---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a7d032298a5bda6660eef15311fcef0acbcb3540f0474ca910d49ad3ddab63da
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - standardized-metadata-fields-for-mlflow-traces
    - SMFFMT
    - Standard metadata fields for MLflow traces
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: Standardized Metadata Fields for MLflow Traces
description: Predefined metadata keys like mlflow.trace.user, mlflow.trace.session, and mlflow.source.type that MLflow recognizes for filtering, grouping, and UI features in trace analysis.
tags:
  - mlflow
  - metadata
  - tracing
  - schemas
timestamp: "2026-06-19T13:53:52.914Z"
---

# Standardized Metadata Fields for MLflow Traces

**Standardized Metadata Fields for MLflow Traces** are predefined key-value pairs that MLflow provides to capture important contextual information—such as user identity, session grouping, execution environment, and application version—when instrumenting GenAI applications with traces. These fields enable consistent filtering, grouping, and analysis of trace data across environments and user segments. ^[add-context-to-traces-databricks-on-aws.md]

## Overview

Adding context to traces allows developers to track execution details, analyze user behavior, debug issues across environments, and monitor application performance. MLflow supports both standardized metadata fields for common context types and custom metadata for application-specific information. The system distinguishes between **tags** (mutable after a trace is logged) and **metadata** (immutable after the trace is logged). ^[add-context-to-traces-databricks-on-aws.md]

## Requirements

To use standardized metadata fields, you must install the `mlflow-tracing` package and use MLflow 3. MLflow 2.x is not supported due to performance limitations and missing features essential for production use. ^[add-context-to-traces-databricks-on-aws.md]

```bash
pip install --upgrade mlflow-tracing
```

The `mlflow-tracing` package is optimized for production with minimal dependencies and better performance characteristics. ^[add-context-to-traces-databricks-on-aws.md]

## Implementation

Context is added during application execution by calling `mlflow.update_current_trace()` with `metadata` and/or `tags` dictionaries. After a trace is logged, tags can be modified, but metadata becomes immutable. ^[add-context-to-traces-databricks-on-aws.md]

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

To read metadata and tags from logged traces, use the `metadata` and `tags` fields in the pandas DataFrame returned by `mlflow.search_traces()`, or access `Trace.info.trace_metadata` and `Trace.info.tags` on [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) objects. ^[add-context-to-traces-databricks-on-aws.md]

## Standard Metadata Fields

### Users and Sessions

Two standard metadata fields are provided for tracking user identity and conversation flow:

- `mlflow.trace.user` – associates traces with specific users.
- `mlflow.trace.session` – groups traces belonging to multi-turn conversations.

These fields enable user behavior analysis, conversation flow tracking, personalization insights, quality per user, and session continuity. Because metadata is immutable once the trace is logged, these fields are ideal for immutable identifiers like user and session IDs. ^[add-context-to-traces-databricks-on-aws.md]

### Environments and Versions

Standard fields for tracking deployment context:

- `mlflow.source.type` – identifies the execution environment (e.g., `development`, `staging`, `production`).
- `mlflow.source.name` – identifies the application version or name.

These fields are **automatically populated** by MLflow from environment variables, but can be overridden using `mlflow.update_current_trace()`. Overriding is useful when the automatic detection does not meet your requirements—for example, setting a custom name with `mlflow.update_current_trace(metadata={"mlflow.source.name": "custom_name"})`. ^[add-context-to-traces-databricks-on-aws.md]

## Custom Metadata

In addition to standardized fields, you can add any custom `metadata` keys to capture application-specific context, such as:

- Application version
- Deployment ID
- Deployment region
- Feature flags

Custom metadata follows the same immutability rules as standard metadata fields. ^[add-context-to-traces-databricks-on-aws.md]

## Tags

Tags are separate from metadata and remain mutable after a trace is logged. They are useful for attaching transient or updatable information, such as `query_category` or processing stage. Tags can be added via the `tags` parameter of `mlflow.update_current_trace()`. ^[add-context-to-traces-databricks-on-aws.md]

## Best Practices

1. **Consistent ID formats** – Use standardized formats for user and session IDs across your application.
2. **Session boundaries** – Define clear rules for when sessions start and end.
3. **Environment variables** – Populate metadata from environment variables rather than hard-coding values.
4. **Combine context types** – Track user, session, and environment context together for complete traceability.
5. **Regular analysis** – Set up dashboards to monitor user behavior, session patterns, and version performance.
6. **Override defaults thoughtfully** – Only override automatically populated metadata when necessary.

^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]]
- mlflow.update_current_trace()
- mlflow.search_traces() API|Search traces programmatically
- Trace analysis examples
- GenAI application instrumentation

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
