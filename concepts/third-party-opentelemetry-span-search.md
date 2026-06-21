---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 19b86276f422830b4f6fa6e86fcdab39d8e62d55b3e249015dce0fbe1c90b973
  pageDirectory: concepts
  sources:
    - search-traces-programmatically-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - third-party-opentelemetry-span-search
    - TOSS
  citations:
    - file: search-traces-programmatically-databricks-on-aws.md
title: Third-Party OpenTelemetry Span Search
description: Ability to search traces ingested from third-party OpenTelemetry tools (e.g., Langfuse) using the span.attributes.* prefix in filter strings.
tags:
  - mlflow
  - opentelemetry
  - third-party
timestamp: "2026-06-19T20:20:07.979Z"
---

# Third-Party OpenTelemetry Span Search

**Third-Party OpenTelemetry Span Search** refers to the ability to search and filter traces ingested from external OpenTelemetry-compatible tools—such as Langfuse—using the `span.attributes.*` prefix in the `filter_string` argument of [`mlflow.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_traces). This mechanism allows users to query traces by OTel span attributes when the traces were collected by third-party instrumentation. ^[search-traces-programmatically-databricks-on-aws.md]

## Usage

When constructing the `filter_string` for `mlflow.search_traces()`, use the `span.attributes.*` prefix followed by the specific attribute name and value. The standard SQL-like query syntax applies: string values must be wrapped in single quotes, numeric values must not be quoted, and multiple conditions can be combined with `AND` (the `OR` operator is not supported). ^[search-traces-programmatically-databricks-on-aws.md]

For example, to find all spans where an OpenTelemetry attribute `service.name` equals `my-service`:

```python
traces = mlflow.search_traces(
    filter_string="span.attributes.'service.name' = 'my-service'"
)
```

The attribute name must be enclosed in backticks if it contains dots. ^[search-traces-programmatically-databricks-on-aws.md]

## Context

This search capability is available on [Databricks-Managed MLflow](/concepts/databricks-managed-mlflow.md) for traces that have been ingested from third-party OpenTelemetry tools. It is not the default search path; for traces collected natively by MLflow, the standard `trace.*`, `tag.*`, and `metadata.*` prefixes are used. The `span.attributes.*` prefix is specifically intended for third-party OpenTelemetry spans. ^[search-traces-programmatically-databricks-on-aws.md]

Related documentation includes the guide *[Search for traces by OTel span attributes](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/third-party/otel-span-attributes#search-for-traces-by-otel-span-attributes)*, which provides further details and examples. ^[search-traces-programmatically-databricks-on-aws.md]

## Related Concepts

- OpenTelemetry
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Trace Search – The general mechanism for querying traces in MLflow.
- mlflow.search_traces() – The API used for programmatic trace search.
- [Databricks-Managed MLflow](/concepts/databricks-managed-mlflow.md) – The environment where this feature is supported.

## Sources

- search-traces-programmatically-databricks-on-aws.md

# Citations

1. [search-traces-programmatically-databricks-on-aws.md](/references/search-traces-programmatically-databricks-on-aws-0153c5e0.md)
