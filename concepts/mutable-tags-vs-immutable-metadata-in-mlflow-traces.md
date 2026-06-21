---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5def5840affc4d991f7efa3a7d2d1dc6a93e519631b170dbb73aecd300614b29
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mutable-tags-vs-immutable-metadata-in-mlflow-traces
    - MTVIMIMT
    - Immutable Metadata vs Mutable Tags
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
      start: 31
      end: 34
    - file: add-context-to-traces-databricks-on-aws.md
      start: 53
      end: 53
    - file: add-context-to-traces-databricks-on-aws.md
      start: 65
      end: 70
    - file: add-context-to-traces-databricks-on-aws.md
      start: 33
      end: 33
    - file: add-context-to-traces-databricks-on-aws.md
      start: 37
      end: 38
    - file: add-context-to-traces-databricks-on-aws.md
      start: 56
      end: 58
    - file: add-context-to-traces-databricks-on-aws.md
      start: 76
      end: 76
title: Mutable Tags vs Immutable Metadata in MLflow Traces
description: Distinction between tags (mutable after trace logging) and metadata (immutable after trace logging) in MLflow trace context
tags:
  - mlflow
  - tracing
  - data-model
timestamp: "2026-06-19T21:59:07.919Z"
---

# Mutable Tags vs Immutable Metadata in MLflow Traces

**Mutable Tags vs Immutable Metadata** is a design distinction in [[MLflow Trace|MLflow Traces]] where **tags can be updated** after a trace is logged, while **metadata becomes fixed** and cannot be modified. This difference influences which contextual information you should store in each field.

## Overview

When adding context to [[MLflow Trace|MLflow Traces]], you use two fields—`tags` and `metadata`—that differ in their mutability after the trace is logged. Both are set during trace execution via [`mlflow.update_current_trace()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.update_current_trace), but only tags remain modifiable once the trace is finalized. ^[add-context-to-traces-databricks-on-aws.md:31-34]

## Mutability After Logging

The core difference is that **tags are mutable** and **metadata are immutable** after the trace is logged. ^[add-context-to-traces-databricks-on-aws.md:31-34]

- **Tags**: You can update or remove tags on a trace even after the trace has been recorded and stored. This makes tags ideal for attributes that may change over time, such as a manual classification or a post-hoc label.
- **Metadata**: Once the trace is logged, metadata cannot be updated. Any attempt to modify metadata after logging is ignored or raises an error. This immutability makes metadata suitable for identifiers and other contextual data that must remain fixed for the lifetime of the trace. ^[add-context-to-traces-databricks-on-aws.md:53]

## Standard Metadata Fields

MLflow defines several standard metadata fields that capture common contextual information. Because metadata is immutable, these fields are intended for stable, identity‑style data:

- `mlflow.trace.user` – Associates the trace with a specific user (ideal for user behavior analysis).
- `mlflow.trace.session` – Groups traces belonging to a multi-turn conversation.
- `mlflow.source.type` – Indicates the execution environment (e.g., `development`, `staging`, `production`).
- `mlflow.source.name` – Automatically populated but can be overridden before logging.

The documentation explicitly notes: "Unlike tags, metadata cannot be updated once the trace is logged, making it ideal for immutable identifiers like user and session IDs." ^[add-context-to-traces-databricks-on-aws.md:53]

## Custom Fields

You can add **custom metadata** keys for any application‑specific context (e.g., application version, deployment ID, region, feature flags). Custom metadata also becomes immutable once the trace is logged. ^[add-context-to-traces-databricks-on-aws.md:65-70]

Custom **tags** can be used for mutable attributes, such as a query category or a flag that may be updated after the trace is recorded. An example from the documentation shows setting a tag `"query_category": "chat"` during execution. ^[add-context-to-traces-databricks-on-aws.md:33]

## When to Use Tags vs Metadata

| Use Case | Recommended Field | Rationale |
|---|---|---|
| User ID, session ID, environment name | **Metadata** | These identifiers must not change after logging to maintain trace integrity. |
| Volatile labels, post‑hoc annotations, manual classification | **Tags** | Tags can be updated later if the classification or annotation needs to be corrected or refined. |
| Automatically populated context (e.g., `mlflow.source.name`) | **Metadata** (can be overridden during execution) | Once logged, these fields are fixed, preserving the execution context. |
| Feature flags, deployment region, custom runtime info | **Metadata** or **Tags** | Use metadata if the value should never change; use tags if it might be updated after analysis. |

## Accessing Tags and Metadata

After logging, both tags and metadata are accessible via:

- The pandas DataFrame returned by `mlflow.search_traces()` (using the `tags` and `metadata` columns).
- The [`Trace.info.trace_metadata`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo.trace_metadata) and [`Trace.info.tags`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.TraceInfo.tags) fields on [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) objects. ^[add-context-to-traces-databricks-on-aws.md:37-38]

## Best Practices

1. **Use metadata for immutable identifiers**: User IDs, session IDs, and environment names belong in metadata to guarantee trace integrity. ^[add-context-to-traces-databricks-on-aws.md:53]
2. **Use tags for mutable context**: If you expect to update or correct a context value after the trace is logged (e.g., a human‑reviewed quality label), use tags.
3. **Populate metadata from environment variables** rather than hard‑coding values, especially for deployment‑related fields. ^[add-context-to-traces-databricks-on-aws.md:56-58]
4. **Only override automatically populated metadata when necessary** – the defaults are sufficient for most use cases. ^[add-context-to-traces-databricks-on-aws.md:76]

## Related Concepts

- [[MLflow Trace|MLflow Traces]] — The core object that holds both tags and metadata.
- mlflow.update_current_trace()|mlflow.update_current_trace — The API function used to set tags and metadata during trace execution.
- [Trace](/concepts/traces.md) — The entity class providing access to tags and metadata after logging.
- [Assessments on Traces](/concepts/assessments-on-traces.md) — Another form of annotation (assessments) attached to traces; assessments are not directly related to tags/metadata but are part of the trace evaluation system.

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md:31-34](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
2. [add-context-to-traces-databricks-on-aws.md:53-53](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
3. [add-context-to-traces-databricks-on-aws.md:65-70](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
4. [add-context-to-traces-databricks-on-aws.md:33-33](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
5. [add-context-to-traces-databricks-on-aws.md:37-38](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
6. [add-context-to-traces-databricks-on-aws.md:56-58](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
7. [add-context-to-traces-databricks-on-aws.md:76-76](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
