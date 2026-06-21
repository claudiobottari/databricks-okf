---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a43d4c4d9a50a96ba7823dacd139d9232472d220d1eefa9d0ec5d948cb1a6e2
  pageDirectory: concepts
  sources:
    - migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-prefix-format-benefits
    - TFB
    - Table-prefix Format
  citations:
    - file: migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md
title: Table-prefix Format Benefits
description: The table-prefix UC trace format provides faster time-range queries, richer attribute types, a dedicated annotations table, and support for multiple trace destinations per schema compared to the older schema-linked format
tags:
  - performance
  - mlflow
  - tracing
timestamp: "2026-06-19T19:32:34.655Z"
---

# Table-prefix Format Benefits

The **table-prefix format** is a Unity Catalog trace storage format introduced with the Public Preview release of [MLflow Tracing](/concepts/mlflow-tracing.md) on Databricks. It uses a three-part destination path (`catalog.schema.table_prefix`) and stores trace data in prefix-namespaced tables. Databricks recommends this format for all new and existing UC trace workloads. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Benefits

- **Faster time‑range queries**: The table‑prefix layout enables more efficient filtering and aggregation over time windows compared to the older schema‑linked format. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]
- **Richer attribute types**: The format supports a broader set of attribute types for trace data, improving the fidelity of stored information. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]
- **Dedicated annotations table**: Annotations (tags, assessments, metadata) are stored in a separate table (`<table_prefix>_otel_annotations`) rather than being embedded as log events in the logs table. This separation simplifies querying and management. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]
- **Multiple trace destinations per schema**: A single schema can host multiple experiments, each with its own table prefix, allowing independent trace destinations within the same [Catalog and Schema](/concepts/catalog-and-schema.md). ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Comparison with the Schema‑linked Format

| Feature | Schema‑linked (Beta) | Table‑prefix (Public Preview) |
| --- | --- | --- |
| Destination path | `catalog.schema` (two parts) | `catalog.schema.table_prefix` (three parts) |
| Span table name | Fixed: `mlflow_experiment_trace_otel_spans` | Prefixed: `<table_prefix>_otel_spans` |
| Annotations | Stored as log events in `_otel_logs` table | Dedicated `<table_prefix>_otel_annotations` table |
| Multiple experiments per schema | Not supported | Supported via different prefixes |
| Attribute types | Limited | Richer |

^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Migration

Traces stored in the older schema‑linked format can be migrated to the table‑prefix format using the `V1ToV2SqlMigration` class from the `databricks-migrations` package. The migration copies spans and annotations via Spark SQL and is idempotent, allowing safe reruns if interrupted. Source tables are not modified during migration and can be retained as a backup. ^[migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Trace Storage](/concepts/unity-catalog-trace-storage.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- symlink_format_manifest|Schema-linked format
- V1 to V2 Trace Migration

## Sources

- migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md

# Citations

1. [migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws.md](/references/migrate-beta-traces-to-the-latest-unity-catalog-table-format-databricks-on-aws-4136e9d1.md)
