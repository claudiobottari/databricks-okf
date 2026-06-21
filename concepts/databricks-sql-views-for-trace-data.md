---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8ee3f680a656d878bed12946a4626fbad1c50f25214daea3bae67a29db0afd90
  pageDirectory: concepts
  sources:
    - query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-sql-views-for-trace-data
    - DSVFTD
  citations:
    - file: query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md
title: Databricks SQL Views for Trace Data
description: Databricks SQL views (trace_unified and trace_metadata) that transform OpenTelemetry table data into MLflow format for SQL-based trace querying.
tags:
  - databricks-sql
  - views
  - tracing
  - unity-catalog
timestamp: "2026-06-19T20:02:38.441Z"
---

# Databricks SQL Views for Trace Data

**Databricks SQL Views for Trace Data** are automatically created Databricks SQL views that transform OpenTelemetry trace data stored in Unity Catalog into the MLflow format, enabling querying of traces using standard SQL. These views are maintained alongside the underlying OpenTelemetry-compliant tables by the MLflow service. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Overview

When trace data is stored in OpenTelemetry format in Unity Catalog, the MLflow service automatically creates Databricks SQL views that transform the raw OpenTelemetry data into the MLflow trace format. Databricks recommends querying these views (or using the [MLflow Tracing API](/concepts/mlflow-tracing.md)) instead of querying the underlying tables directly, because the schemas for those tables can change over time. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Available Views

### `{table_prefix}_trace_unified`

This view provides a unified look across all trace data grouped by each trace ID. Each row contains the raw span data and the trace info metadata, including MLflow tags, metadata, and assessments. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

The schema includes:

- `trace_id`: STRING — The unique identifier for the trace.
- `client_request_id`: STRING — The client-side request identifier.
- `request_time`: TIMESTAMP — When the request was made.
- `state`: STRING — The state of the trace.
- `execution_duration_ms`: DECIMAL(30,9) — Duration of the trace execution.
- `request`: STRING — The request payload.
- `response`: STRING — The response payload.
- `trace_metadata`: MAP<STRING, STRING> — Metadata associated with the trace.
- `tags`: MAP<STRING, STRING> — MLflow tags.
- `spans`: LIST<STRUCT> — The spans contained in the trace, including span ID, parent span ID, name, kind, timestamps, attributes, events, links, status, resource, and instrumentation scope.
- `assessments`: LIST<STRUCT> — Assessment data including assessment ID, name, source, timestamps, expectation, feedback, rationale, metadata, and validity.

^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### `{table_prefix}_trace_metadata`

This view contains just the MLflow tags, metadata, and assessments grouped by trace ID. It is more performant than the unified view for retrieving MLflow-specific data. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

The schema includes:

- `trace_id`: STRING
- `client_request_id`: STRING
- `tags`: MAP<STRING, STRING>
- `trace_metadata`: MAP<STRING, STRING>
- `assessments`: LIST<STRUCT> — Same assessment structure as the unified view.

^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Performance Considerations

For large trace volumes, query performance on these views can degrade. To maintain performance, create a [materialized view](/concepts/materialized-views-in-databricks.md) over the SQL views and incrementally update it. For best performance on recent data, use the [MLflow Tracing API](/concepts/mlflow-tracing.md) to query traces instead of SQL. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Querying with Databricks SQL

To query traces using Databricks SQL, specify a Databricks SQL warehouse to execute queries. You can use standard SQL to filter, aggregate, and analyze trace data from these views. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Diagnosing Slow Queries

To diagnose slow queries, inspect query profiles in the SQL warehouse query history:

1. Go to the **SQL warehouses** page in your Databricks workspace.
2. Select your SQL warehouse and click the **Query history** tab.
3. Look for queries with **MLflow** specified as the source.
4. Click a query to view its query profile.

In the query profile, inspect the following:

- **Scheduling time**: If scheduling time is high, queries are waiting due to heavy load on the warehouse. Switch to a different SQL warehouse.
- **Overall query performance**: For consistently slow queries, use a larger SQL warehouse, tighten upper and lower bounds on `trace.timestamp_ms`, and remove other filter predicates where possible.

^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [OpenTelemetry Traces in Unity Catalog](/concepts/opentelemetry-traces-in-unity-catalog.md) — How trace data is stored in OpenTelemetry format.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The [MLflow Tracing](/concepts/mlflow-tracing.md) system for monitoring AI applications.
- Databricks SQL Warehouses — Compute resources for executing SQL queries.
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Performance optimization for large trace volumes.
- [MLflow Tracing API](/concepts/mlflow-tracing.md) — Programmatic API for querying traces.

## Sources

- query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md

# Citations

1. [query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md](/references/query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws-046b043a.md)
