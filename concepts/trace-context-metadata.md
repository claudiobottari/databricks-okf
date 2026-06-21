---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d6600b34e804c44af98d57c506386bd265bfd8690b18977bcccd71f5846157d5
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-context-metadata
    - TCM
    - trace-context-metadata-in-mlflow
    - TCMIM
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: Trace Context Metadata
description: The practice of adding standard and custom metadata fields (tags and metadata) to MLflow traces to track execution details, user behavior, and environment information.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-18T14:19:07.472Z"
---

# Trace Context Metadata

**Trace Context Metadata** refers to structured data attached to [Traces](/concepts/traces.md) to capture execution details, user identity, session information, deployment environment, and application‑specific properties. By enriching traces with metadata, you can analyze user behavior, debug issues across environments, and monitor application performance in production. MLflow provides both standardized metadata fields for common context types and the flexibility to add custom keys. ^[add-context-to-traces-databricks-on-aws.md]

## Requirements

Metadata can only be added in MLflow 3 or later. MLflow 2.x is not supported due to performance limitations and missing features essential for production use. For production deployments, install the `mlflow-tracing` package:

```bash
pip install --upgrade mlflow-tracing
```

^[add-context-to-traces-databricks-on-aws.md]

## Implementation

After instrumenting your application (for example, using the `@mlflow.trace` decorator), you add context metadata and tags at runtime by calling mlflow.update_current_trace()|mlflow.update_current_trace:

```python
import mlflow

mlflow.update_current_trace(
    metadata={
        "mlflow.trace.user": user_id,
        "mlflow.trace.session": session_id,
    },
    tags={
        "query_category": "chat",  # custom tag
    },
)
```

^[add-context-to-traces-databricks-on-aws.md]

- **metadata** – immutable after the trace is logged; ideal for identifiers like user and session IDs.
- **tags** – mutable after logging; suitable for categories or labels that may change.

To access stored metadata in trace logs, use the `metadata` and `tags` fields in the pandas DataFrame returned by mlflow.search_traces()|mlflow.search_traces, or the `Trace.info.trace_metadata` and `Trace.info.tags` fields on [Trace](/concepts/traces.md) objects. ^[add-context-to-traces-databricks-on-aws.md]

## Types of Context Metadata

MLflow defines standard metadata keys for the most common context requirements. You can combine multiple keys and add your own custom keys.

### Users and Sessions

- `mlflow.trace.user` – associates traces with a specific user.
- `mlflow.trace.session` – groups traces belonging to a multi‑turn conversation.

These fields enable user behavior analysis, conversation flow tracking, per‑user quality metrics, and session continuity. Because metadata is immutable, these identifiers are reliable for filtering and grouping in the MLflow UI. ^[add-context-to-traces-databricks-on-aws.md]

### Environments and Versions

- `mlflow.source.type` – typically set to `production`, `staging`, or `development`.
- `mlflow.source.name` – identifies the application or deployment source.

MLflow automatically populates several standard metadata fields based on the execution environment. You can override any auto‑populated value by passing the same key to `mlflow.update_current_trace()`; for example:

```python
mlflow.update_current_trace(metadata={"mlflow.source.name": "custom_name"})
```

For deployment metadata, it is best practice to read values from environment variables rather than hard‑coding them:

```python
import os

mlflow.update_current_trace(
    metadata={
        "mlflow.source.type": os.getenv("APP_ENVIRONMENT", "development"),
    }
)
```

^[add-context-to-traces-databricks-on-aws.md]

Environment and version metadata enables environment‑specific analysis, performance/quality regression detection across app versions, and faster root cause analysis when issues occur. ^[add-context-to-traces-databricks-on-aws.md]

### Custom Metadata

You can attach any application‑specific context using custom keys under the `metadata` dictionary. Examples include:

- Application version
- Deployment ID
- Deployment region
- Feature flags

^[add-context-to-traces-databricks-on-aws.md]

## Best Practices

- **Use consistent ID formats** – adopt standardized schemes for user and session IDs across your application.
- **Define session boundaries** – establish clear rules for when a session starts and ends.
- **Read metadata from environment variables** – avoid hard‑coding values, especially for environment names and version strings.
- **Combine context types** – track user, session, and environment context together for complete traceability.
- **Set up regular analysis** – use dashboards to monitor user behavior, session patterns, and version performance.
- **Override defaults thoughtfully** – only override automatically populated metadata when the default does not meet your requirements.

^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — the overarching framework for instrumenting GenAI applications
- [Traces](/concepts/traces.md) — the execution records that metadata enriches
- mlflow.update_current_trace()|mlflow.update_current_trace — the API used to attach metadata and tags
- mlflow.search_traces()|mlflow.search_traces — how to query traces and their metadata programmatically
- Trace Metadata Fields — reference of all standard keys

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
