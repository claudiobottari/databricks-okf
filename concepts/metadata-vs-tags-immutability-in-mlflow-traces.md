---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6fcbfa4b3f1008d14493aaf30ccd95a81c7abe0c415eae826b8fa1fbd11a23aa
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metadata-vs-tags-immutability-in-mlflow-traces
    - MVTIIMT
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: Metadata vs Tags Immutability in MLflow Traces
description: "A key distinction: once a trace is logged, metadata fields are immutable (ideal for stable identifiers like user and session IDs), while tags remain mutable (suitable for updatable annotations)."
tags:
  - mlflow
  - metadata
  - tags
  - tracing
timestamp: "2026-06-19T13:53:52.411Z"
---

# Metadata vs Tags Immutability in MLflow Traces

In [MLflow Tracing](/concepts/mlflow-tracing.md), **metadata** and **tags** are two mechanisms for attaching additional context to a trace. The critical distinction between them is their immutability after the trace is logged: metadata become immutable, while tags remain mutable. This design choice reflects their intended purposes – metadata for permanent identifiers and tags for modifiable annotations. ^[add-context-to-traces-databricks-on-aws.md]

## Key Differences

| Property | Metadata | Tags |
|----------|----------|------|
| **Mutability after logging** | Immutable – cannot be changed once the trace is logged | Mutable – can be updated after the trace is logged |
| **Purpose** | Permanent, identity-related information (e.g., user ID, session ID, environment) | Modifiable annotations (e.g., query category, experiment label) |
| **Standard fields** | `mlflow.trace.user`, `mlflow.trace.session`, `mlflow.source.type`, etc. | No standard fields; user-defined |
| **Override behavior** | Automatically populated metadata can be overridden during execution | N/A |

^[add-context-to-traces-databricks-on-aws.md]

## Setting Context During Execution

Both metadata and tags are set before the trace is logged, using [`mlflow.update_current_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=trace#mlflow.update_current_trace). At this stage – while the trace is still being recorded – both are mutable. The immutability boundary is crossed when the trace is finalized and persisted. ^[add-context-to-traces-databricks-on-aws.md]

```python
import mlflow

mlflow.update_current_trace(
    metadata={
        "mlflow.trace.user": user_id,        # immutable after logging
        "mlflow.trace.session": session_id,  # immutable after logging
    },
    tags={
        "query_category": "chat",            # mutable after logging
    },
)
```

^[add-context-to-traces-databricks-on-aws.md]

## Why Immutability Matters for Metadata

MLflow’s standard metadata fields – such as `mlflow.trace.user` and `mlflow.trace.session` – are designed to carry fixed identifiers that should not change after the trace is recorded. This immutability makes metadata the ideal place for:

- **User and session IDs** – to prevent accidental overwrites that could break trace-to-user associations
- **Environment markers** – to guarantee that a trace’s deployment context (development, staging, production) remains authoritative
- **Custom permanent fields** – any application-specific identifier that must stay constant

^[add-context-to-traces-databricks-on-aws.md]

## When to Use Tags

Tags, because they remain mutable, are suitable for information that may need to be updated after a trace is logged. For example:

- **Query category** – reclassifying a trace after manual review
- **Priority flags** – marking traces for investigation
- **Temporary annotations** – adding notes during debugging sessions

^[add-context-to-traces-databricks-on-aws.md]

## Accessing Metadata and Tags

After logging, both metadata and tags can be retrieved via the `metadata` and `tags` fields in the pandas DataFrame returned by `mlflow.search_traces()`, or via the [`Trace.info.trace_metadata`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo.trace_metadata) and [`Trace.info.tags`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo.tags) properties on [Trace](/concepts/traces.md) objects. ^[add-context-to-traces-databricks-on-aws.md]

## Automatically Populated Metadata

MLflow automatically populates several standard metadata fields based on the execution environment (e.g., `mlflow.source.type`). These auto-populated values can be overridden during trace execution (before logging), but once the trace is logged, they become immutable like any other metadata. ^[add-context-to-traces-databricks-on-aws.md]

## Best Practices

1. **Use metadata for fixed identity** – Assign user IDs, session IDs, and deployment environment to metadata fields to guarantee they cannot be altered after logging.
2. **Use tags for mutable annotations** – Store any data that you might want to update later (e.g., reclassification, manual labels) as tags.
3. **Override auto-populated metadata sparingly** – Only override when the automatic detection is incorrect for your use case.
4. **Combine both in one call** – Always use `mlflow.update_current_trace()` to set both metadata and tags together when the context is fully known.

^[add-context-to-traces-databricks-on-aws.md]

## Related Concepts

- [Add context to traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md)
- [Trace](/concepts/traces.md) – The object that holds metadata and tags
- mlflow.search_traces() API|Search traces programmatically – How to retrieve metadata and tags via `mlflow.search_traces()`
- Tutorial: Trace and analyze users and environments
- [Standard metadata fields for MLflow traces](/concepts/standardized-metadata-fields-for-traces.md)

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
