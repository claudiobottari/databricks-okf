---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d69a8d72afe6102ba6e7b85efb285c3562f5036df0f027442517ab95b6ea93c2
  pageDirectory: concepts
  sources:
    - view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-metadata-filters
    - TMF
    - Trace Metadata Fields
  citations:
    - file: view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
title: Trace Metadata Filters
description: Structured search queries in the MLflow UI that allow filtering traces by metadata fields such as user, session, source type, and app version using a SQL-like syntax on metadata fields.
tags:
  - mlflow
  - tracing
  - metadata
  - filtering
timestamp: "2026-06-19T23:26:56.065Z"
---

# [Trace Metadata](/concepts/trace-metadata.md) Filters

**Trace Metadata Filters** allow you to query and narrow the trace list in the [MLflow](/concepts/mlflow.md) UI by searching against metadata attributes attached to each trace. These filters enable you to find specific [Traces](/concepts/traces.md) based on user, session, environment, application version, or any custom metadata key-value pair.

## Overview

[Traces](/concepts/traces.md) in [MLflow](/concepts/mlflow.md) can carry metadata — key-value pairs that describe the context of a trace, such as the user who triggered it, the session it belongs to, the source environment, or the application version. The [MLflow](/concepts/mlflow.md) UI provides a dedicated filtering syntax to query [Traces](/concepts/traces.md) by these metadata fields. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

You can access the metadata filters through the "Filters" dropdown in the **Traces** tab of an experiment view. The filter input supports structured queries against the `metadata` field. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Filter Syntax

[Traces](/concepts/traces.md) are filtered using the `metadata.` prefix followed by the key name in backtick-delimited notation. The basic syntax is:

```
metadata.`key_name` = 'value'
```

The UI supports combining multiple conditions with `AND` and other logical operators. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Common Filter Examples

**Find all [Traces](/concepts/traces.md) for a specific user:** ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]
```
metadata.`mlflow.trace.user` = 'user-123'
```

**Find all [Traces](/concepts/traces.md) in a session:** ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]
```
metadata.`mlflow.trace.session` = 'session-abc-456'
```

**Find [Traces](/concepts/traces.md) for a user within a specific session:** ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]
```
metadata.`mlflow.trace.user` = 'user-123' AND metadata.`mlflow.trace.session` = 'session-abc-456'
```

**Find [Traces](/concepts/traces.md) from production environment:** ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]
```
metadata.`mlflow.source.type` = 'production'
```

**Find [Traces](/concepts/traces.md) from a specific app version:** ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]
```
metadata.app_version = '1.0.0'
```

ℹ️ The `mlflow.trace.user` key is automatically captured when you pass user context to [Traces](/concepts/traces.md). Similarly, `mlflow.trace.session` is populated when you group [Traces](/concepts/traces.md) into sessions. Custom metadata keys — such as `app_version` in the example above — are arbitrary key-value pairs you can attach when creating or logging a trace.

## Standard Metadata Fields

[MLflow](/concepts/mlflow.md) defines several standard metadata keys that are commonly used for filtering:

| Metadata Key | Description |
|---|---|
| `mlflow.trace.user` | The user identifier who triggered the trace |
| `mlflow.trace.session` | The session identifier grouping related [Traces](/concepts/traces.md) (e.g., in a conversation) |
| `mlflow.source.type` | The source environment of the trace (e.g., `production`) |
| Custom keys | Any user-defined key-value pairs attached to a trace |

These fields become filterable in the UI when they are populated on the [Traces](/concepts/traces.md). ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Usage in the UI

To apply a metadata filter:

1. Open the experiment containing your [Traces](/concepts/traces.md).
2. Click the **Traces** tab.
3. Click the **Filters** dropdown.
4. Enter a query using the `metadata.` syntax, such as `metadata.`mlflow.trace.user` = 'user-123'`.

The trace list updates to show only [Traces](/concepts/traces.md) matching the filter. You can combine multiple conditions or use other filter fields (like `State`, `Trace name`, or `Assessments`) alongside metadata filters for more targeted queries. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Common Debugging Scenarios

Metadata filters are especially useful in these debugging workflows:

- **Find [Traces](/concepts/traces.md) from a particular user**: If you have tracked user information and it's available as a filter option, use the metadata query `metadata.`mlflow.trace.user` = 'user_example_123'`. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]
- **Identify slow [Traces](/concepts/traces.md) for a specific session**: Combine a session metadata filter with a sort by execution time to locate performance bottlenecks for a particular conversation.
- **Trace production issues**: Filter by `metadata.`mlflow.source.type` = 'production'` to focus on [Traces](/concepts/traces.md) from the live environment, then further filter by state (`ERROR`) or assessment criteria.

## Limitations

The trace list returns at most 1,000 [Traces](/concepts/traces.md). Filters — including metadata filters — apply only to this visible set, not the full experiment. To guarantee that an older trace appears, narrow the time range to include it. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

Experiments not in [Unity Catalog](/concepts/unity-catalog.md) are capped at 100,000 [Traces](/concepts/traces.md). To remove both limits and enable searching across all [Traces](/concepts/traces.md) in a time range, consider migrating to [traces in Unity Catalog](/concepts/model-traces-in-unity-catalog.md). ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework that captures and stores trace data.
- [Add Context to Traces](/concepts/best-practices-for-adding-context-to-mlflow-traces.md) — How to attach user, session, and custom metadata to [Traces](/concepts/traces.md).
- [Traces in Unity Catalog](/concepts/model-traces-in-unity-catalog.md) — Extended storage and query capabilities for [Traces](/concepts/traces.md).
- View Traces in the MLflow UI — General guidance on viewing and navigating trace data.
- [Query Traces via SDK](/concepts/searching-otel-traces-via-mlflow-sdk.md) — Programmatic alternative to UI-based filtering.

## Sources

- view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md

# Citations

1. [view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md](/references/view-traces-in-the-databricks-mlflow-ui-databricks-on-aws-d0ec6f89.md)
