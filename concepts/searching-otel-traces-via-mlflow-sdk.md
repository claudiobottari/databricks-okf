---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 59adbe261b5bb219419b1ac03473c59ee2ae4e6c8939d2bfdd9d47921580b5a5
  pageDirectory: concepts
  sources:
    - set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - searching-otel-traces-via-mlflow-sdk
    - SOTVMS
    - Query Traces via SDK
    - Query traces via SDK
  citations:
    - file: set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
title: Searching OTel Traces via MLflow SDK
description: Using the span.attributes.* prefix in mlflow.search_traces() filter_string to query ingested OTel traces by attribute values like session.id, user.id, or token counts.
tags:
  - mlflow
  - open-telemetry
  - search
  - sdk
timestamp: "2026-06-19T23:04:52.494Z"
---

# Searching OTel [Traces](/concepts/traces.md) via [MLflow](/concepts/mlflow.md) SDK

**Searching OTel [Traces](/concepts/traces.md) via [MLflow](/concepts/mlflow.md) SDK** refers to the programmatic approach for filtering and retrieving OpenTelemetry (OTel) [Traces](/concepts/traces.md) that have been ingested into Databricks [MLflow](/concepts/mlflow.md), using the `mlflow.search_traces()` function with a `filter_string` parameter that leverages the `span.attributes.*` prefix.

## Overview

After ingesting OTel [Traces](/concepts/traces.md) into [Unity Catalog](/concepts/unity-catalog.md), you can search for them programmatically using the [MLflow SDK](/concepts/mlflow.md). The key mechanism for filtering is the `span.attributes.*` prefix in the `filter_string` parameter of `mlflow.search_traces()`. The attribute name that follows the prefix is the same OTel attribute name that was set with `span.set_attribute()` during instrumentation. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Prerequisites

Before searching for OTel [Traces](/concepts/traces.md) via the SDK, you must have:

- A Databricks workspace with the OTel tracing preview enabled
- The OTLP exporter configured to send [Traces](/concepts/traces.md) to your workspace
- An application instrumented with the OpenTelemetry SDK that sets the appropriate span attributes
- The [Traces](/concepts/traces.md) successfully ingested into [Unity Catalog](/concepts/unity-catalog.md)

^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Search Syntax

The `filter_string` uses the `span.attributes.<attribute_name>` format, where `<attribute_name>` is any OTel span attribute you set during instrumentation. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

### Basic Filtering

To set the experiment context and filter [Traces](/concepts/traces.md), use:

```python
import [[mlflow|MLflow]]

[[mlflow|MLflow]].set_experiment(experiment_id="<experiment-id>")
```

The `experiment_id` is visible in the [MLflow](/concepts/mlflow.md) UI URL and experiment details panel. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

### Supported Filter Examples

#### Filter by Session ID

Find [Traces](/concepts/traces.md) associated with a specific session (set using `session.id` during instrumentation):

```python
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.session.id = 'conversation-123'"
)
```

^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

#### Filter by User ID

Find [Traces](/concepts/traces.md) from a specific user (set using `user.id`):

```python
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.user.id = 'user-456'"
)
```

^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

#### Filter by Model Name

Find [Traces](/concepts/traces.md) from a specific model (set using `gen_ai.request.model`), using `LIKE` for pattern matching:

```python
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.gen_ai.request.model LIKE '%gpt%'"
)
```

^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

#### Filter by Operation Type

Find [Traces](/concepts/traces.md) by operation type (set using `gen_ai.operation.name`):

```python
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.gen_ai.operation.name = 'chat'"
)
```

^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

#### Filter by Token Usage

Find [Traces](/concepts/traces.md) with high token counts (set using `gen_ai.usage.input_tokens`), using numeric comparison operators:

```python
[[traces|Traces]] = [[mlflow|MLflow]].search_traces(
    filter_string="span.attributes.gen_ai.usage.input_tokens > 1000"
)
```

^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Full `filter_string` Syntax

For the complete `filter_string` syntax including all supported operators and comparators, see mlflow.search_traces() API|Search traces programmatically. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Limitations

Custom OTel span attributes set with `span.set_attribute()` outside the recognized OTel-to-MLflow mappings are not surfaced as [MLflow Trace Tags](/concepts/mlflow-trace-tags.md). This means they do not appear in:

- The **Tags** column or the unified trace view in the [MLflow](/concepts/mlflow.md) UI
- The `_traces_unified` [Unity Catalog](/concepts/unity-catalog.md) table
- The `tags` field returned by `mlflow.search_traces()`

These attributes are preserved on the underlying span. They remain visible in the **Attributes** tab of the [[mlflow-trace|MLflow Trace]] UI and are queryable through the `<_prefix>_otel_spans.attributes` field of the OTel spans table. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

To attach searchable tags that appear in the unified trace view, use the MLflow tag APIs instead. See [Attach custom tags and metadata](/concepts/trace-tags-and-metadata.md). ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Related Concepts

- [Set OpenTelemetry Span Attributes for MLflow](/concepts/opentelemetry-mlflow-span-attribute-mapping.md) — How to set the span attributes that are searchable via this API
- [OpenTelemetry (OTel)](/concepts/opentelemetry-compatibility.md) — The observability framework used for instrumentation
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of the tracing system on Databricks
- [Unity Catalog](/concepts/unity-catalog.md) — The storage layer where trace data is ingested
- mlflow.search_traces() API|Search traces programmatically — Full syntax reference for the `filter_string` parameter
- Query OpenTelemetry traces stored in Unity Catalog — Alternative approach using Databricks SQL for large-scale queries

## Sources

- set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md

# Citations

1. [set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md](/references/set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws-8961c630.md)
