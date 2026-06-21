---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f42cba3c0e3cccf65d1507274622d05c29658d3ec6f45ea9ec42447032acd427
  pageDirectory: concepts
  sources:
    - query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-trace-storage-for-opentelemetry
    - UCTSFO
  citations:
    - file: query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Trace Storage for OpenTelemetry
description: Architecture and approach for storing OpenTelemetry trace data in Unity Catalog tables, enabling query via MLflow SDK and Databricks SQL.
tags:
  - observability
  - tracing
  - unity-catalog
  - opentelemetry
timestamp: "2026-06-19T20:03:01.861Z"
---

# Unity Catalog Trace Storage for OpenTelemetry

**Unity Catalog Trace Storage for OpenTelemetry** is a Databricks feature that stores trace data in OpenTelemetry-compliant format within Unity Catalog tables, enabling querying through the MLflow Python SDK or Databricks SQL. This provides a structured, queryable foundation for observability and AI system monitoring.

## Overview

When traces are stored in Unity Catalog, the underlying data is maintained in OpenTelemetry-compliant table formats. The MLflow service automatically creates Databricks SQL views alongside these tables, transforming the OpenTelemetry data into the MLflow format for easier querying. Databricks recommends querying the views or using the API instead of relying on the underlying tables, because the schemas for those tables can change over time. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Querying Traces

### Using the MLflow Python SDK

To search and load trace objects with the MLflow Python SDK, you must:

1. Set the `MLFLOW_TRACING_SQL_WAREHOUSE_ID` environment variable to specify a Databricks SQL warehouse for executing search queries.
2. Use the `locations` argument of `mlflow.search_traces` to specify one or more MLflow experiments or Unity Catalog schemas containing traces.
3. Specify either the name of a Unity Catalog schema, or the ID of an MLflow experiment linked to a Unity Catalog schema. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

Example search query:

```python
import os
import mlflow
from mlflow.entities.trace_location import UnityCatalog

catalog_name = "<UC_CATALOG>"
schema_name = "<UC_SCHEMA>"
table_prefix = "<UC_TABLE_PREFIX>"

mlflow.set_tracking_uri("databricks")
os.environ["MLFLOW_TRACING_SQL_WAREHOUSE_ID"] = "<SQL_WAREHOUSE_ID>"

traces = mlflow.search_traces(
    filter_string="trace.status = 'OK'",
    order_by=["timestamp_ms DESC"],
    include_spans=False,
)
```

To load a specific trace by UUID: ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

```python
trace_uuid = "<TRACE_UUID>"
trace = mlflow.get_trace(
    trace_id=f"trace:/{catalog_name}.{schema_name}.{table_prefix}/{trace_uuid}"
)
```

### Using Databricks SQL

Databricks SQL provides two views stored alongside the OpenTelemetry tables: ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

#### `{table_prefix}_trace_unified`

This view provides a unified look across all trace data grouped by each trace ID. Each row contains the raw span data and trace info metadata, including MLflow tags, metadata, and assessments. The schema includes fields such as `trace_id`, `request_time`, `state`, `execution_duration_ms`, `request`, `response`, `trace_metadata`, `tags`, `spans`, and `assessments`. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

#### `{table_prefix}_trace_metadata`

This view contains just the MLflow tags, metadata, and assessments grouped by trace ID. It is more performant than the unified view for retrieving MLflow data alone. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### Performance Considerations

For large trace volumes, query performance on these views can degrade. To maintain performance, create a [materialized view](/concepts/materialized-views-in-databricks.md) over them and incrementally update it. For best performance on recent data, use the Trace Query API instead. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Annotation Data Formats

[MLflow Tracing](/concepts/mlflow-tracing.md) entities such as metadata, tags, assessments, and run links are stored in the `{table_prefix}_otel_annotations` table. This table is append-only with soft-deletes, so you must de-duplicate on retrieval by taking the latest row per `annotation_id` (ordering by `updated_at` descending) and filtering out rows where `deleted_at` is set. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

The table schema includes: `annotation_id`, `target_type` (TRACE or SPAN), `target_id`, `annotation_type` (METADATA, TAG, FEEDBACK, EXPECTATION, RUN_LINK), `name`, `value` (VARIANT), `comment`, `metadata` (VARIANT), `created_at`, `created_by`, `updated_at`, `updated_by`, `deleted_at`, and `deleted_by`. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### Entity Types

- **Metadata**: One row per trace. The `value` column contains a JSON struct with `client_request_id`, `trace_metadata`, `request_preview`, and `response_preview`. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

- **Tags**: Each tag is a separate row. De-duplicate using `annotation_id`, which is derived deterministically from the trace ID and tag key. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

- **Assessments**: Stored as FEEDBACK or EXPECTATION rows. The rationale is in the `comment` column. User-supplied metadata is in the `metadata` column, alongside internal MLflow-managed fields (prefixed with `mlflow.`) that should be ignored when reading user metadata. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

- **Run Links**: Links between a trace and an [MLflow Run](/concepts/mlflow-run.md). De-duplicate using `annotation_id`, derived from the trace ID and run ID. The `value` column contains the run ID. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Diagnosing Query Performance

To diagnose slow queries, inspect query profiles in the SQL warehouse query history:

1. Go to the **SQL warehouses** page in your Databricks workspace.
2. Select your SQL warehouse and click the **Query history** tab.
3. Look for queries with **MLflow** specified as the source.
4. Click a query to view its query profile.

In the query profile, check the following:

- **Scheduling time**: If high, queries are waiting due to heavy load on the warehouse. Switch to a different SQL warehouse in the MLflow UI or configure a different warehouse in your client.
- **Overall query performance**: For consistently slow queries, use a larger SQL warehouse, tighten upper and lower bounds on `trace.timestamp_ms`, and remove other filter predicates where possible. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- OpenTelemetry — The open standard for observability data used as the storage format
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and storage layer for trace data
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The system that generates and manages trace data
- Databricks SQL Warehouses — The compute resource for executing trace queries
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Performance optimization for large trace volumes
- Trace Query API — Alternative query method for better performance on recent data

## Sources

- query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md

# Citations

1. [query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md](/references/query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws-046b043a.md)
