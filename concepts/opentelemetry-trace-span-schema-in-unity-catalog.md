---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 17c738310d6d7c2b62d354437a319660ac8804b3e25a9bb953978684b0c32ca6
  pageDirectory: concepts
  sources:
    - query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opentelemetry-trace-span-schema-in-unity-catalog
    - OTSSIUC
  citations:
    - file: query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md
title: OpenTelemetry Trace Span Schema in Unity Catalog
description: The detailed schema of the trace_unified view including span structures, events, links, status, resource, and instrumentation scope fields.
tags:
  - opentelemetry
  - schema
  - spans
  - unity-catalog
timestamp: "2026-06-19T20:04:15.948Z"
---

# OpenTelemetry Trace Span Schema in Unity Catalog

The **OpenTelemetry Trace Span Schema in Unity Catalog** refers to the data structure used when storing trace data from MLflow in OpenTelemetry format within [Unity Catalog](/concepts/unity-catalog.md). When traces are stored in this format, they become queryable through the MLflow Python SDK or via Databricks SQL using automatically created Unity Catalog views. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Overview

When trace data is stored in OpenTelemetry format in Unity Catalog, the MLflow service automatically creates Databricks SQL Views alongside the underlying tables. These views transform the raw OpenTelemetry data into the MLflow format for easier querying. Databricks recommends querying the views or using the API instead of relying on the underlying tables, because the schemas for those tables can change over time. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## `{table_prefix}_trace_unified` View

This view provides a unified look across all trace data grouped by each trace ID. Each row contains the raw span data and trace info metadata. The metadata includes MLflow tags, metadata, and assessments. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### Schema

The view includes the following columns:

- `trace_id`: STRING
- `client_request_id`: STRING
- `request_time`: TIMESTAMP
- `state`: STRING
- `execution_duration_ms`: DECIMAL(30,9)
- `request`: STRING
- `response`: STRING
- `trace_metadata`: MAP<STRING, STRING>
- `tags`: MAP<STRING, STRING>
- `spans`: LIST<STRUCT> — contains the full OpenTelemetry Span data structure
- `assessments`: LIST<STRUCT> — contains assessment information including expectations and feedback

^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### Span Structure

The `spans` column contains a list of structs with the following schema:

- `trace_id`: STRING
- `span_id`: STRING
- `trace_state`: STRING
- `parent_span_id`: STRING
- `flags`: INT
- `name`: STRING
- `kind`: STRING
- `start_time_unix_nano`: BIGINT
- `end_time_unix_nano`: BIGINT
- `attributes`: MAP<STRING, STRING>
- `dropped_attributes_count`: INT
- `events`: LIST<STRUCT> — each event has `time_unix_nano`, `name`, `attributes`, and `dropped_attributes_count`
- `dropped_events_count`: INT
- `links`: LIST<STRUCT> — each link has `trace_id`, `span_id`, `trace_state`, `attributes`, `dropped_attributes_count`, and `flags`
- `dropped_links_count`: INT
- `status`: STRUCT — contains `message` and `code`
- `resource`: STRUCT — contains `attributes` and `dropped_attributes_count`
- `resource_schema_url`: STRING
- `instrumentation_scope`: STRUCT — contains `name`, `version`, `attributes`, and `dropped_attributes_count`
- `span_schema_url`: STRING

^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## `{table_prefix}_trace_metadata` View

This view contains just the MLflow tags, metadata, and assessments grouped by trace ID. It is more performant than the unified view for retrieving MLflow-specific data. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### Schema

- `trace_id`: STRING
- `client_request_id`: STRING
- `tags`: MAP<STRING, STRING>
- `trace_metadata`: MAP<STRING, STRING>
- `assessments`: LIST<STRUCT> — containing assessment details with `assessment_id`, `assessment_name`, `source`, `create_time`, `last_update_time`, `expectation`, `feedback`, `rationale`, `metadata`, `span_id`, `overrides`, and `valid`

^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## MLflow Annotation Data Formats

The data for [MLflow Tracing](/concepts/mlflow-tracing.md) entities like metadata, tags, assessments, and links to runs are stored in the `{table_prefix}_otel_annotations` table. Each entity is stored as a single row with a typed `annotation_type`, and its fields are split across top-level columns (`name`, `value`, `comment`, `metadata`). ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

The annotations table is append-only with soft-deletes, so you must de-duplicate on retrieval by taking the latest row per `annotation_id` (ordering by `updated_at` descending) and filtering out rows where `deleted_at` is set. The `value` and `metadata` columns are `VARIANT` (JSON). ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### Table Columns

- `annotation_id`: STRING
- `target_type`: STRING ("TRACE" or "SPAN")
- `target_id`: STRING ("{trace_id}" for TRACE, "{trace_id}:{span_id}" for SPAN)
- `annotation_type`: STRING ("METADATA", "TAG", "FEEDBACK", "EXPECTATION", "RUN_LINK")
- `name`: STRING
- `value`: VARIANT
- `comment`: STRING
- `metadata`: VARIANT
- `created_at`: TIMESTAMP
- `created_by`: STRING
- `updated_at`: TIMESTAMP
- `updated_by`: STRING
- `deleted_at`: TIMESTAMP
- `deleted_by`: STRING

^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### Annotation Types Detail

- **MLflow metadata** (`annotation_type: "METADATA"`, `target_type: "TRACE"`, `name: "metadata"`): Only one row exists per trace. The `value` column is a JSON struct containing the trace's client request ID, metadata map, and request/response previews. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

- **MLflow tags** (`annotation_type: "TAG"`, `target_type: "TRACE"`): Each tag is stored as a separate row. You can de-duplicate them within each trace using the `annotation_id` attribute, which is derived deterministically from the trace ID and tag key. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

- **MLflow assessments** (`annotation_type: "FEEDBACK"` or `"EXPECTATION"`, `target_type: "TRACE"`): Each assessment is stored depending on its type. You can de-duplicate them within each trace using the `annotation_id` attribute, which matches the assessment ID. The rationale is stored in the top-level `comment` column. User-supplied assessment metadata is stored in the `metadata` column alongside internal MLflow-managed fields (keys prefixed with `mlflow.`), which you should ignore when reading user metadata. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

- **MLflow run links** (`annotation_type: "RUN_LINK"`, `target_type: "TRACE"`, `name: "run_link"`): Each link between a trace and an [MLflow Run](/concepts/mlflow-run.md) is stored as a separate row. You can de-duplicate them within each trace using the `annotation_id` attribute, which is derived deterministically from the trace ID and run ID. The `value` column contains the run ID as a STRING. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Performance Considerations

For large trace volumes, query performance on the standard views can degrade. To maintain performance, Databricks recommends creating a [Materialized View](/concepts/materialized-views-in-databricks.md) over the standard views and incrementally updating it. For best performance on recent data, use the API to query traces. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

To diagnose slow queries, inspect query profiles in the SQL warehouse query history. If scheduling time is high, queries are waiting due to heavy load on the warehouse. For consistently slow queries, use a larger SQL warehouse, tighten upper and lower bounds on `trace.timestamp_ms`, and remove other filter predicates where possible. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- OpenTelemetry
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Databricks SQL Views
- [Materialized Views](/concepts/materialized-views-in-databricks.md)
- Databricks SQL Warehouse

## Sources

- query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md

# Citations

1. [query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md](/references/query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws-046b043a.md)
