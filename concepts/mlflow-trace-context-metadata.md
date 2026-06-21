---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4b5233553dcedb3cd06391ecddc4ff6707c7ffd15248c149051fc89961c76ac1
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-context-metadata
    - MTCM
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: MLflow Trace Context Metadata
description: Standardized metadata fields (mlflow.trace.user, mlflow.trace.session, mlflow.source.type, etc.) that can be attached to traces to track users, sessions, environments, and versions in GenAI applications.
tags:
  - mlflow
  - tracing
  - metadata
timestamp: "2026-06-18T10:39:51.073Z"
---

# MLflow Trace Context Metadata

**MLflow Trace Context Metadata** refers to the standardized and custom metadata fields and tags that you can attach to [[MLflow Trace|MLflow Traces]] to capture execution details, user behavior, environment information, and application‑specific context. Adding context to traces enables you to track execution details, analyze user behavior, debug issues across environments, and monitor application performance. ^[add-context-to-traces-databricks-on-aws.md]

MLflow provides standardized metadata fields for common context types (e.g., user ID, session ID, execution environment) plus the flexibility to add custom metadata keys specific to your application. Context can be both mutable (tags) and immutable (metadata) after a trace is logged. ^[add-context-to-traces-databricks-on-aws.md]

## Requirements

To use trace context metadata, install the appropriate tracing package. For production deployments, install the `mlflow-tracing` package:

```bash
pip install --upgrade mlflow-tracing
```

The `mlflow-tracing` package is optimized for production use with minimal dependencies and better performance characteristics. MLflow 3 is required for context tracking; MLflow 2.x is not supported due to performance limitations and missing features essential for production use. ^[add-context-to-traces-databricks-on-aws.md]

## Implementation

To add metadata and tags to traces:

1. **Trace your application** – Most commonly, use the `@mlflow.trace` decorator to trace functions automatically.
2. **Call `mlflow.update_current_trace()`** during your application’s execution to attach context.

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

After your application completes and a trace is logged, **tags** remain mutable but **metadata** become immutable in the logged trace. ^[add-context-to-traces-databricks-on-aws.md]

## Types of Context Metadata

MLflow standardizes several metadata fields to capture important contextual information, while also allowing custom keys for application‑specific needs.

### Track Users and Sessions

Tracking users and sessions is essential for understanding user behavior, analyzing conversation flows, and improving personalization. MLflow provides two standard metadata fields:

| Metadata key | Purpose |
|---|---|
| `mlflow.trace.user` | Associates traces with specific users |
| `mlflow.trace.session` | Groups traces belonging to multi‑turn conversations |

When you use these standard metadata fields, MLflow automatically enables filtering and grouping in the UI. Because metadata is immutable after logging, these fields are ideal for permanent identifiers like user and session IDs. ^[add-context-to-traces-databricks-on-aws.md]

### Track Environments and Versions

Tracking the execution environment and application version allows you to debug performance and quality issues relative to the code. MLflow supplies standard metadata fields such as `mlflow.source.type` for environment context.

Your application should generally extract deployment metadata from environment variables rather than hard‑coding values. For example:

```python
import mlflow
import os

mlflow.update_current_trace(
    metadata={
        "mlflow.source.type": os.getenv("APP_ENVIRONMENT", "development"),
    }
)
```

MLflow automatically populates certain standard metadata fields based on your execution environment. You can override any automatically populated field using `mlflow.update_current_trace()`, which is useful when the automatic detection does not meet your requirements (e.g., override `mlflow.source.name` with a custom value). ^[add-context-to-traces-databricks-on-aws.md]

### Add Custom Metadata

You can use custom `metadata` keys to capture any other application‑specific context, such as:

- Application version
- Deployment ID
- Deployment region
- Feature flags

Custom metadata is added in the same `metadata` dictionary passed to `mlflow.update_current_trace()`. ^[add-context-to-traces-databricks-on-aws.md]

## Accessing Metadata

You can access metadata and tags in trace logs through:

- The `metadata` and `tags` fields in the Pandas DataFrame returned by `mlflow.search_traces()`.
- The `Trace.info.trace_metadata` and `Trace.info.tags` fields from [[MLflow Trace]] objects.

```python
trace = mlflow.get_trace(trace_id)
print(trace.info.trace_metadata)
print(trace.info.tags)
```

^[add-context-to-traces-databricks-on-aws.md]

## Best Practices

- **Consistent ID formats** – Use standardized formats for user and session IDs across your application.
- **Session boundaries** – Define clear rules for when sessions start and end.
- **Environment variables** – Populate metadata from environment variables rather than hard‑coding values.
- **Combine context types** – Track user, session, and environment context together for complete traceability.
- **Regular analysis** – Set up dashboards to monitor user behavior, session patterns, and version performance.
- **Override defaults thoughtfully** – Only override automatically populated metadata when necessary.

^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]] – The core execution records that context metadata annotates.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The framework for capturing, storing, and analyzing traces.
- MLflow Tags vs Metadata – Understanding the mutability differences.
- mlflow.search_traces() API|Search Traces Programmatically – Querying traces using `mlflow.search_traces()`.

## Sources

* add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
