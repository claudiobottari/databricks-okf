---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 985f617f31a594c4041545bb13ec74b32abbeb0af4a9e5e95b3798bf017cb1b7
  pageDirectory: concepts
  sources:
    - query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-annotation-data-formats
    - MADF
  citations:
    - file: query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md
title: MLflow Annotation Data Formats
description: The otel_annotations table structure for storing MLflow tracing entities (metadata, tags, assessments, run links) as typed rows with soft-delete semantics.
tags:
  - mlflow
  - annotations
  - data-format
  - tracing
timestamp: "2026-06-19T20:02:47.565Z"
---

# MLflow Annotation Data Formats

**MLflow Annotation Data Formats** describes the structure and storage of tracing-related metadata, tags, assessments, and run links within the `{table_prefix}_otel_annotations` table in [Unity Catalog](/concepts/unity-catalog.md). This table is append-only and uses soft-deletes, requiring deduplication on retrieval. Each annotation entity is stored as a single row with a typed `annotation_type` field, and its fields are split across top-level columns. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Schema

The `{table_prefix}_otel_annotations` table has the following columns. The `value` and `metadata` columns are of type `VARIANT` (JSON). ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

| Column | Type | Description |
|--------|------|-------------|
| `annotation_id` | STRING | Unique identifier for the annotation. |
| `target_type` | STRING | Either `"TRACE"` or `"SPAN"` indicating what the annotation targets. |
| `target_id` | STRING | For `TRACE`, the trace ID; for `SPAN`, `"{trace_id}:{span_id}"`. |
| `annotation_type` | STRING | One of `"METADATA"`, `"TAG"`, `"FEEDBACK"`, `"EXPECTATION"`, `"RUN_LINK"`. |
| `name` | STRING | Name of the annotation (e.g., tag key, assessment name). |
| `value` | VARIANT | Value of the annotation (JSON). |
| `comment` | STRING | Comment or rationale (used for assessments). |
| `metadata` | VARIANT | Additional metadata (JSON), used for assessments. |
| `created_at` | TIMESTAMP | When the annotation was created. |
| `created_by` | STRING | Who created the annotation. |
| `updated_at` | TIMESTAMP | When the annotation was last updated. |
| `updated_by` | STRING | Who last updated the annotation. |
| `deleted_at` | TIMESTAMP | If set, indicates the annotation is soft-deleted. |
| `deleted_by` | STRING | Who deleted the annotation. |

## Deduplication and Soft-Deletes

Because the annotations table is append-only and uses soft-deletes, you must deduplicate on retrieval by taking the latest row per `annotation_id` (ordering by `updated_at` descending) and filtering out rows where `deleted_at` is set. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## MLflow Metadata

Only one metadata row exists per trace. The `value` column is a JSON struct containing the trace's client request ID, metadata map, and request/response previews. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

- `annotation_type`: `"METADATA"`
- `target_type`: `"TRACE"`
- `name`: `"metadata"`
- `value`: Includes `client_request_id`, `trace_metadata`, `request_preview`, `response_preview`

## MLflow Tags

Each tag is stored as a separate row. Deduplicate within each trace using the `annotation_id`, which is derived deterministically from the trace ID and tag key. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

- `annotation_type`: `"TAG"`
- `target_type`: `"TRACE"`
- `name`: The tag key (STRING)
- `value`: The tag value (STRING)

## MLflow Assessments

Each assessment is stored as either a `FEEDBACK` or `EXPECTATION` row depending on its type. Deduplicate within each trace using the `annotation_id`, which matches the assessment ID. The rationale is stored in the top-level `comment` column. User-supplied assessment metadata is stored in the `metadata` column alongside internal MLflow-managed fields (keys prefixed with `mlflow.`), which should be ignored when reading user metadata. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

- `annotation_type`: `"FEEDBACK"` or `"EXPECTATION"`
- `target_type`: `"TRACE"`
- `name`: The assessment name
- `value`: Feedback value, expectation value, or JSON-serialized expectation string
- `comment`: The rationale
- `metadata`: User-supplied assessment metadata (ignoring `mlflow.`‑prefixed fields)

## [MLflow Run](/concepts/mlflow-run.md) Links

Each link between a trace and an [MLflow Run](/concepts/mlflow-run.md) is stored as a separate row. Deduplicate within each trace using the `annotation_id`, which is derived deterministically from the trace ID and run ID. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

- `annotation_type`: `"RUN_LINK"`
- `target_type`: `"TRACE"`
- `name`: `"run_link"`
- `value`: The run ID (STRING)

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of MLflow’s tracing subsystem.
- OpenTelemetry — The format used to store trace data in Unity Catalog.
- [Store OpenTelemetry traces in Unity Catalog](/concepts/opentelemetry-traces-in-unity-catalog.md) — Prerequisite for creating annotation tables.
- Query OpenTelemetry traces stored in Unity Catalog — How to query traces and views.
- Databricks SQL — Used to query the views built over annotations.

## Sources

- query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md

# Citations

1. [query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md](/references/query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws-046b043a.md)
