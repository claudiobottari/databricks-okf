---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9cf3fcab7e3bec19b31db3d785efd18b34eb1aaa98ebdb1fca82cdec49fb4096
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-context-metadata-in-mlflow
    - TCMIM
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: Trace Context Metadata in MLflow
description: Adding standardized and custom metadata/tags to MLflow traces for tracking execution details, user behavior, and application performance
tags:
  - mlflow
  - tracing
  - observability
  - metadata
timestamp: "2026-06-19T21:58:25.108Z"
---

# Trace Context Metadata in MLflow

**Trace Context Metadata in MLflow** refers to the structured metadata and tags that can be attached to [Traces] to capture execution details, user behavior, environment information, and application‑specific context. By adding contextual metadata to traces, developers can analyze performance, debug issues across environments, monitor user interactions, and improve the observability of GenAI applications. ^[add-context-to-traces-databricks-on-aws.md]

## Requirements

To use trace context metadata you must install the appropriate MLflow package. For production deployments, install the `mlflow-tracing` package:

```bash
pip install --upgrade mlflow-tracing
```

This package is optimised for production use with minimal dependencies. MLflow 3 is required for context tracking; MLflow 2.x is not supported due to performance limitations and missing features essential for production use. ^[add-context-to-traces-databricks-on-aws.md]

## Adding Context to Traces

To add metadata and tags to a trace during execution:

1. Instrument your application (most commonly using the `@mlflow.trace` decorator to trace functions automatically).
2. Call [`mlflow.update_current_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=trace#mlflow.update_current_trace) to attach context using `metadata` or `tags`.

```python
import mlflow

mlflow.update_current_trace(
    metadata={
        "mlflow.trace.user": user_id,
        "mlflow.trace.session": session_id,
    },
    tags={
        "query_category": "chat",  # Example custom tag
    },
)
```

Once a trace is logged, **metadata is immutable** while **tags are mutable**. ^[add-context-to-traces-databricks-on-aws.md]

## Standard Metadata Fields

MLflow provides standardised metadata fields for common context types:

### Track Users and Sessions

Two standard metadata fields are provided for user and session tracking:

- `mlflow.trace.user` – Associates a trace with a specific user.
- `mlflow.trace.session` – Groups traces belonging to a multi‑turn conversation.

Using these fields enables automatic filtering and grouping in the MLflow UI. Because metadata is immutable once logged, these identifiers remain fixed and reliable for analysis. ^[add-context-to-traces-databricks-on-aws.md]

### Track Environments and Versions

The execution environment and application version can be tracked using standard metadata fields. For example:

```python
mlflow.update_current_trace(
    metadata={
        "mlflow.source.type": os.getenv("APP_ENVIRONMENT", "development"),
    }
)
```

MLflow automatically populates [certain standard metadata fields](https://mlflow.org/docs/latest/genai/tracing/track-environments-context/#automatically-populated-tags) based on the execution environment. You can override any of these automatically populated values using `mlflow.update_current_trace()`. ^[add-context-to-traces-databricks-on-aws.md]

## Custom Metadata

Beyond the standard fields, you can attach arbitrary `metadata` keys to capture any application‑specific context, such as:

- Application version
- Deployment ID
- Deployment region
- Feature flags

Custom metadata is attached via the `metadata` argument of `mlflow.update_current_trace()`. ^[add-context-to-traces-databricks-on-aws.md]

## Accessing Metadata and Tags

Trace metadata and tags can be retrieved programmatically:

- From the pandas DataFrame returned by `mlflow.search_traces()`, using the `metadata` and `tags` columns.
- From `Trace` objects via `trace.info.trace_metadata` and `trace.info.tags`.

See [Search traces programmatically](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-via-sdk) for more details. ^[add-context-to-traces-databricks-on-aws.md]

## Best Practices

1. **Use consistent ID formats** – Standardise user and session IDs across your application.
2. **Define session boundaries** – Establish clear rules for when sessions start and end.
3. **Populate metadata from environment variables** – Avoid hard‑coding values; derive deployment environment, version, and region from environment variables.
4. **Combine context types** – Track user, session, and environment context together for complete traceability.
5. **Set up regular analysis** – Create dashboards to monitor user behaviour, session patterns, and version performance.
6. **Override defaults thoughtfully** – Only override automatically populated metadata when necessary. ^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Overview of the tracing system.
- [Trace](/concepts/traces.md) – A logged execution trace in MLflow.
- [GenAI Application Monitoring](/concepts/mlflow-genai-production-monitoring.md) – Using traces to monitor generative AI applications.
- [Trace Tags](/concepts/trace-tags.md) – Mutable key‑value pairs attached to traces.
- [Trace Metadata](/concepts/trace-metadata.md) – Immutable key‑value pairs attached to traces.

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
