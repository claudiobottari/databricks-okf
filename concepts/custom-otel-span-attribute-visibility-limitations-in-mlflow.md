---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d6fd8dcd2aa3f3948a8a14d44127d69f04713b0dbdaa971872a26746d9fb909
  pageDirectory: concepts
  sources:
    - set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-otel-span-attribute-visibility-limitations-in-mlflow
    - COSAVLIM
  citations:
    - file: set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md
title: Custom OTel Span Attribute Visibility Limitations in MLflow
description: Custom OTel span attributes set via span.set_attribute() outside recognized mappings are not surfaced as MLflow trace tags, though preserved on the underlying span.
tags:
  - open-telemetry
  - mlflow
  - limitations
  - tracing
timestamp: "2026-06-19T23:03:56.162Z"
---

# Custom OTel Span Attribute Visibility Limitations in [MLflow](/concepts/mlflow.md)

When you send [Traces](/concepts/traces.md) from a custom OpenTelemetry-instrumented application to Databricks [MLflow](/concepts/mlflow.md), only a specific set of span attributes are recognized and mapped to MLflow’s [Trace Metadata](/concepts/trace-metadata.md). Custom OTel span attributes that you set with `span.set_attribute()` outside the documented OTel-to-MLflow mappings are **not** surfaced as [MLflow Trace Tags](/concepts/mlflow-trace-tags.md). ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Where Custom Attributes Are Not Visible

Custom OTel span attributes do not appear in the following locations:

- The **Tags** column or the unified trace view in the [MLflow Tracing](/concepts/mlflow-tracing.md) UI. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]
- The `_traces_unified` [Unity Catalog](/concepts/unity-catalog.md) table. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]
- The `tags` field returned by [`mlflow.search_traces()`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).html#mlflow.search_traces). ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Where Custom Attributes Are Preserved

Although the attributes are not promoted to [MLflow Trace Tags](/concepts/mlflow-trace-tags.md), they are preserved on the underlying OTel span. They remain:

- Visible in the **Attributes** tab of the [[mlflow-trace|MLflow Trace]] UI. ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]
- Queryable through the `<prefix>_otel_spans.attributes` field of the OTel spans table in [Unity Catalog](/concepts/unity-catalog.md). ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Workaround: Use [MLflow](/concepts/mlflow.md) Tag APIs

To attach searchable tags that appear in the unified trace view, the `_traces_unified` table, and the `tags` field of `mlflow.search_traces()`, use the [MLflow Trace Tags](/concepts/mlflow-trace-tags.md) APIs instead of custom OTel span attributes. See [Attach custom tags and metadata](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/attach-tags/). ^[set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md]

## Related Concepts

- OpenTelemetry – The observability framework used for instrumentation.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The [MLflow](/concepts/mlflow.md) feature that ingests and displays [Traces](/concepts/traces.md).
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) where trace data is stored.
- [MLflow Trace Tags](/concepts/mlflow-trace-tags.md) – The mechanism to attach custom searchable metadata to [Traces](/concepts/traces.md).
- mlflow.search_traces() – The API used to query [Traces](/concepts/traces.md) programmatically.

## Sources

- set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md

# Citations

1. [set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws.md](/references/set-opentelemetry-span-attributes-for-mlflow-databricks-on-aws-8961c630.md)
