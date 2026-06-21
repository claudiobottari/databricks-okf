---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d81886f0f0fc40e3ee7113c0b54f79c909e890c8e76800785b4d80af8c54bb3
  pageDirectory: concepts
  sources:
    - query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-search-and-retrieval-api
    - Retrieval API and MLflow Trace Search
    - MTSARA
  citations:
    - file: query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md
title: MLflow Trace Search and Retrieval API
description: Using MLflow Python SDK (search_traces, get_trace) with SQL warehouse configuration to query OpenTelemetry traces stored in Unity Catalog.
tags:
  - mlflow
  - python-sdk
  - tracing
  - api
timestamp: "2026-06-19T20:03:01.221Z"
---

# MLflow Trace Search and Retrieval API

The **MLflow Trace Search and Retrieval API** allows users to query and load OpenTelemetry trace data that has been stored in [Unity Catalog](/concepts/unity-catalog.md) tables. The API is available through the [MLflow](/concepts/mlflow.md) Python SDK and via Databricks SQL views. This enables both programmatic access for downstream applications and interactive SQL-based exploration for analysis on Databricks. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Prerequisites

Before using the search and retrieval API, trace data must be stored in Unity Catalog tables and traces must be generated. See the documentation on [storing OpenTelemetry traces in Unity Catalog](./Store-OpenTelemetry-traces-stored-in-Unity-Catalog-databricks-on-aws.md) for setup instructions. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Query Traces Using the MLflow Python SDK

The MLflow Python SDK provides `mlflow.search_traces()` and `mlflow.get_trace()` functions for searching and loading trace objects. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### Environment Variable

Set the `MLFLOW_TRACING_SQL_WAREHOUSE_ID` environment variable to specify the ID of a Databricks SQL warehouse that will execute search queries. This is required for both search and load operations. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

```python
import os
os.environ["MLFLOW_TRACING_SQL_WAREHOUSE_ID"] = "<SQL_WAREHOUSE_ID>"
```

### Searching Traces

Use `mlflow.search_traces()` with the following key arguments:

- `locations` – One or more MLflow experiments or Unity Catalog schemas containing traces. You can specify the name of a Unity Catalog schema (e.g., `"my_catalog.my_schema"`) or the ID of an MLflow experiment linked to a Unity Catalog schema.
- `filter_string` – A filter expression (e.g., `"trace.status = 'OK'"`).
- `order_by` – A list of ordering expressions (e.g., `["timestamp_ms DESC"]`).
- `include_spans` – Whether to include span data in the results.

Example: ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

```python
import mlflow
from mlflow.entities.trace_location import UnityCatalog

mlflow.set_tracking_uri("databricks")
mlflow.set_experiment(
    experiment_name="...",
    trace_location=UnityCatalog(
        catalog_name="my_catalog",
        schema_name="my_schema",
        table_prefix="my_prefix",
    ),
)

os.environ["MLFLOW_TRACING_SQL_WAREHOUSE_ID"] = "<SQL_WAREHOUSE_ID>"

traces = mlflow.search_traces(
    filter_string="trace.status = 'OK'",
    order_by=["timestamp_ms DESC"],
    include_spans=False,
)
```

The result is a list of `Trace` objects. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### Loading a Single Trace

Use `mlflow.get_trace()` with a trace ID in the format `trace:/<catalog>.<schema>.<table_prefix>/<trace_uuid>`. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

```python
trace = mlflow.get_trace(
    trace_id="trace:/my_catalog.my_schema.my_prefix/13ffa97d571048d69d21da12240d5863"
)
```

## Query Traces Using Databricks SQL

The MLflow service automatically creates Databricks SQL views alongside the underlying OpenTelemetry tables. These views transform the OpenTelemetry data into the MLflow format, making it easier to query. Databricks recommends querying the views or using the SDK API rather than querying the underlying tables, because the schemas for those tables can change over time. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

For large trace volumes, query performance on the views can degrade. To improve performance, create a [Materialized Views|materialized view](/concepts/materialized-views-in-databricks.md) over the views and incrementally update it. For best performance on recent data, use the SDK API. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### `{table_prefix}_trace_unified` View

This view provides a unified look across all trace data, grouped by trace ID. Each row contains the raw span data (including trace ID, span ID, parent span ID, name, kind, start/end timestamps, attributes, events, links, status, resource, instrumentation scope) and MLflow-specific metadata (tags, trace metadata, assessments). ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

Key columns:

- `trace_id`, `client_request_id`, `request_time`, `state`, `execution_duration_ms`, `request`, `response`
- `trace_metadata` (MAP<STRING, STRING>)
- `tags` (MAP<STRING, STRING>)
- `spans` (LIST<STRUCT>)
- `assessments` (LIST<STRUCT>) – includes assessment ID, name, source, expectation, feedback, rationale, metadata, span ID, overrides, valid flag.

### `{table_prefix}_trace_metadata` View

This view contains only the MLflow tags, metadata, and assessments grouped by trace ID. It is more performant than the unified view for retrieving MLflow-specific data. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

Key columns:

- `trace_id`, `client_request_id`
- `tags` (MAP<STRING, STRING>)
- `trace_metadata` (MAP<STRING, STRING>)
- `assessments` (LIST<STRUCT>) – same structure as in the unified view.

## MLflow Annotation Data Formats

The underlying data for [MLflow Tracing](/concepts/mlflow-tracing.md) entities such as metadata, tags, assessments, and run links is stored in the `{table_prefix}_otel_annotations` table. Each entity is stored as a single row with a typed `annotation_type`, and its fields are split across top-level columns. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

The annotations table is append-only with soft-deletes. When querying it directly, de-duplicate by taking the latest row per `annotation_id` (ordering by `updated_at` descending) and filtering out rows where `deleted_at` is set. The `value` and `metadata` columns are of type `VARIANT` (JSON). ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### Entity Types

- **MLflow metadata** – Single row per trace (`annotation_type: "METADATA"`). The `value` column is a JSON struct containing `client_request_id`, `trace_metadata`, `request_preview`, `response_preview`.
- **MLflow tags** – One row per tag-key (`annotation_type: "TAG"`). The `name` column is the tag key, `value` is the tag value. De-duplicate using `annotation_id` (deterministic from trace ID and tag key).
- **MLflow assessments** – Stored as `FEEDBACK` or `EXPECTATION` rows. The rationale is in the top-level `comment` column; user-supplied metadata is in the `metadata` column (ignore keys prefixed with `mlflow.`). De-duplicate using `annotation_id`.
- **MLflow run links** – Each link between a trace and a run is one row (`annotation_type: "RUN_LINK"`). The `value` column contains the run ID. De-duplicate using `annotation_id`.

## Analyze Query Performance

To diagnose slow queries, inspect query profiles in the SQL warehouse query history: ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

1. Go to the **SQL warehouses** page in your Databricks workspace.
2. Select your SQL warehouse and click the **Query history** tab.
3. Look for queries with **MLflow** specified as the source.
4. Click a query to view its profile.

In the profile, inspect:

- **Scheduling time** – High values indicate queuing due to warehouse load. Switch to a different SQL warehouse or configure a different one in your client.
- **Overall query performance** – For consistently slow queries, use a [larger SQL warehouse](https://docs.databricks.com/aws/en/compute/sql-warehouse/create), tighten upper and lower bounds on `trace.timestamp_ms`, and remove other filter predicates where possible.

## Related Concepts

- OpenTelemetry – The observability framework used to format trace data.
- [Unity Catalog](/concepts/unity-catalog.md) – The metadata store where trace tables and views are registered.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Organizational unit for runs and traces.
- Databricks SQL Warehouses – Compute resources for executing SQL queries.
- [Materialized Views](/concepts/materialized-views-in-databricks.md) – Performance optimization for large trace volumes.

## Sources

- query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md

# Citations

1. [query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md](/references/query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws-046b043a.md)
