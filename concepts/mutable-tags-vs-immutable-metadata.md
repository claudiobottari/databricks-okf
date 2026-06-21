---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e297c833507dd1dae5897afbf9100a49f3d0026d57671e7b6ae773ed793b5bd
  pageDirectory: concepts
  sources:
    - add-context-to-traces-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mutable-tags-vs-immutable-metadata
    - MTVIM
    - mutable-tags-vs-immutable-metadata-in-mlflow-traces
    - MTVIMIMT
    - Immutable Metadata vs Mutable Tags
  citations:
    - file: add-context-to-traces-databricks-on-aws.md
title: Mutable Tags vs Immutable Metadata
description: In MLflow tracing, tags on logged traces can be mutated after logging while metadata becomes immutable once the trace is logged, making metadata suitable for immutable identifiers like user IDs.
tags:
  - mlflow
  - tracing
  - data-model
timestamp: "2026-06-19T17:27:50.222Z"
---

# Mutable Tags vs Immutable Metadata

**Mutable Tags vs Immutable Metadata** describes the behavioral difference between `tags` and `metadata` fields in [MLflow Tracing](/concepts/mlflow-tracing.md). After a trace is logged, tags remain mutable (updateable), while metadata becomes immutable (read-only). This distinction guides which type of context to use for different kinds of trace information.

## Overview

When adding context to traces using `mlflow.update_current_trace()`, users can provide both `tags` and `metadata` dictionaries. The key difference is that `tags` can be modified after the trace is logged, whereas `metadata` is fixed once the trace completes and is stored. This immutability makes metadata suitable for identifiers that must not change, while tags are appropriate for mutable attributes like categorization labels. ^[add-context-to-traces-databricks-on-aws.md]

## Behavioral Differences

| Property | Tags | Metadata |
|---|---|---|
| Mutable after logging | Yes | No |
| Use case | Categorization, mutable attributes | Immutable identifiers (user IDs, session IDs) |
| UI filtering | Supported | Supported when using standard metadata fields |

^[add-context-to-traces-databricks-on-aws.md]

## Immutability of Metadata

MLflow enforces that `metadata` keys cannot be updated once the trace is logged. This makes metadata ideal for storing immutable identifiers like user IDs (`mlflow.trace.user`) and session IDs (`mlflow.trace.session`). Because these identifiers must remain consistent for accurate analysis and auditing, their immutability is a deliberate design choice. ^[add-context-to-traces-databricks-on-aws.md]

## Mutability of Tags

Tags can be modified after the trace is logged. This makes them suitable for labeling traces with attributes that may change during or after execution — for example, assigning a `query_category` tag like `"chat"` or updating tags during post-processing. ^[add-context-to-traces-databricks-on-aws.md]

## Accessing Tags and Metadata

Both tags and metadata can be accessed from trace logs using:
- The `metadata` and `tags` fields in the pandas DataFrame returned by `mlflow.search_traces()`
- The `Trace.info.trace_metadata` and `Trace.info.tags` fields from [Trace](/concepts/traces.md) objects

## Best Practices

- Use metadata for **immutable identifiers** such as user IDs, session IDs, environment names, and application versions.
- Use tags for **mutable categorization** such as query categories, feature flags, or processing stages.
- When using standard metadata fields (e.g., `mlflow.trace.user`, `mlflow.trace.session`), MLflow automatically enables filtering and grouping in the UI.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework that supports tags and metadata
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) — How to add tags and metadata during trace execution
- [Trace](/concepts/traces.md) — The MLflow entity that stores tags and metadata
- [Standard Metadata Fields](/concepts/standardized-metadata-fields-for-traces.md) — Predefined metadata keys like `mlflow.trace.user` and `mlflow.trace.session`

## Sources

- add-context-to-traces-databricks-on-aws.md

# Citations

1. [add-context-to-traces-databricks-on-aws.md](/references/add-context-to-traces-databricks-on-aws-1d18f107.md)
