---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2daabb579b2c61e2e26e27be0fb4839c25c29fbe3038db3842a9a8dae83eb4a5
  pageDirectory: concepts
  sources:
    - set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - session-and-user-association-in-mlflow-traces
    - User Association in MLflow Traces and Session
    - SAUAIMT
  citations:
    - file: set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
title: Session and User Association in MLflow Traces
description: Associating traces with sessions and users via the session.id and user.id OpenTelemetry span attributes for trace-level metadata and the session tab in MLflow UI.
tags:
  - open-telemetry
  - mlflow
  - tracing
  - user-session
timestamp: "2026-06-19T23:03:46.574Z"
---

## Session and User Association in [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md)

**Session and User Association in [MLflow](/concepts/mlflow.md) Traces** refers to the mechanism by which OpenTelemetry-instrumented applications can attach session and user identifiers to spans, enabling trace-level grouping and filtering in the Databricks [MLflow](/concepts/mlflow.md) UI. This association is achieved by setting specific OpenTelemetry span attributes, which [MLflow](/concepts/mlflow.md) reads and displays as [Trace Metadata](/concepts/trace-metadata.md). ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

### Setting `session.id` and `user.id`

To associate a trace with a Session (OpenTelemetry) or User (OpenTelemetry) identifier, call `span.set_attribute()` on any span with the respective attribute key. The canonical keys are `session.id` and `user.id`, as defined by the OpenTelemetry semantic conventions. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
span.set_attribute("session.id", "conversation-123")
span.set_attribute("user.id", "user-456")
```

[MLflow](/concepts/mlflow.md) reads these attributes from the **root span** of the trace and displays them as trace-level metadata in the [MLflow](/concepts/mlflow.md) UI. Setting `session.id` additionally enables the **session tab** in the trace UI, which groups all [Traces](/concepts/traces.md) sharing the same session identifier. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

### Searching and Filtering by Session or User

After ingesting OpenTelemetry [Traces](/concepts/traces.md) into [Unity Catalog](/concepts/unity-catalog.md), you can filter [Traces](/concepts/traces.md) by session or user using `mlflow.search_traces()` with the `span.attributes.*` prefix in the filter string. The attribute name after the prefix matches the OTel attribute key exactly. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].set_experiment(experiment_id="<experiment-id>")

# Find [[traces|Traces]] from a specific session
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.session.id = 'conversation-123'"
)

# Find [[traces|Traces]] from a specific user
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.user.id = 'user-456'"
)
```

For a complete reference of filter syntax, see mlflow.search_traces() API|Search traces programmatically. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

### Limitations

Custom OTel span attributes—including `session.id` and `user.id`—are **not** surfaced as [MLflow Trace Tags](/concepts/mlflow-trace-tags.md). They do not appear in:
- The **Tags** column or the unified trace view in the [MLflow](/concepts/mlflow.md) UI.
- The `_traces_unified` [Unity Catalog](/concepts/unity-catalog.md) table.
- The `tags` field returned by `mlflow.search_traces()`.

These attributes are preserved on the underlying span and remain visible in the **Attributes** tab of the trace UI. They are also queryable through the `<prefix>_otel_spans.attributes` field of the OTel spans table. To attach searchable tags that appear in the unified trace view, use the MLflow tag APIs instead. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

### Related Concepts

- [OpenTelemetry Span Attributes](/concepts/opentelemetry-mlflow-span-attribute-mapping.md) – General guidance on setting OTel attributes for [MLflow](/concepts/mlflow.md).
- MLflow Trace UI – How [Traces](/concepts/traces.md) and spans are displayed.
- Session Tab (MLflow) – UI component enabled by setting `session.id`.
- [Searching Traces by OTel Attributes](/concepts/span-attributes-and-search.md) – Using `span.attributes.*` prefix in filter strings.

## Sources

- set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md

# Citations

1. [set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md](/references/set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws-8961c630.md)
