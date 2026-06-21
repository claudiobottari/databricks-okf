---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: def2c01485ee53e1b7c6102050302f0c3a3327062fe94c42b2e5cf6aa41ee80c
  pageDirectory: concepts
  sources:
    - persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-telemetry-table-structure
    - UCTTS
  citations:
    - file: persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
title: Unity Catalog Telemetry Table Structure
description: Automatically generated Delta tables (_otel_logs, _otel_spans, _otel_metrics) in Unity Catalog that store endpoint telemetry with configurable table prefix.
tags:
  - unity-catalog
  - delta-tables
  - schema
  - databricks
timestamp: "2026-06-19T19:54:56.852Z"
---

# Unity Catalog Telemetry Table Structure

**Unity Catalog Telemetry Table Structure** refers to the schema and naming convention of the Delta tables automatically created by Databricks when you enable endpoint telemetry for a [custom model serving endpoint](/concepts/custom-model-serving-endpoint-support.md). These tables store OpenTelemetry logs, spans, and metrics emitted by your model code, allowing you to perform root‑cause analysis, monitor endpoint health, and meet compliance requirements using standard SQL queries. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Table Naming

When you enable telemetry, Databricks creates three tables in the configured Unity Catalog schema. The table names follow the pattern `<prefix>_otel_logs`, `<prefix>_otel_spans`, and `<prefix>_otel_metrics`, where `<prefix>` is an optional string you provide. If no prefix is set, the tables are named `otel_logs`, `otel_spans`, and `otel_metrics`. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

When using the API, you can override these names by specifying `logs_table`, `metrics_table`, and `traces_table` in the `telemetry_config.table_names` map. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Schema Columns

All three tables share a common set of OpenTelemetry‑aligned columns. The exact schema can be inspected with `DESCRIBE TABLE <table_name>`. The documented columns include:

| Column | Type | Description |
|--------|------|-------------|
| `timestamp` | `TIMESTAMP` | Time when the telemetry record was emitted. |
| `severity_text` | `STRING` | Severity level of the log (e.g., `ERROR`, `WARNING`). (Primarily relevant for `_otel_logs`.) |
| `body` | `STRING` | The log message body. |
| `trace_id` | `STRING` | OpenTelemetry trace identifier for correlating related records. |
| `span_id` | `STRING` | OpenTelemetry span identifier within the trace. |
| `attributes` | `MAP<STRING, STRING>` | Map of key‑value pairs containing event‑specific metadata, such as `input_shape` or `input_columns`. |

^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

Tables for spans and metrics have analogous columns appropriate for their telemetry type (span name, duration, metric name, metric value, etc.). The precise column list can be obtained by running `DESCRIBE TABLE` on the individual tables.

## Query Examples

The following queries demonstrate how to retrieve telemetry data from these tables.

### View all log records

```sql
SELECT *
FROM <catalog>.<schema>.<prefix>_otel_logs
LIMIT 10;
```

### Check for errors in the last hour

```sql
SELECT
  timestamp,
  severity_text,
  body,
  attributes
FROM <catalog>.<schema>.<prefix>_otel_logs
WHERE
  severity_text = 'ERROR'
  AND timestamp > current_timestamp() - INTERVAL 1 HOUR
ORDER BY timestamp DESC;
```

^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- OpenTelemetry – The framework used for log, trace, and metric instrumentation.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance catalog where the tables are stored.
- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md) – The endpoint type that supports telemetry persistence.
- [Delta Tables](/concepts/delta-lake-table.md) – The managed table format used for storage.
- [Model Serving Endpoint Telemetry](/concepts/model-serving-endpoint-telemetry.md) – Overview of the telemetry feature.

## Limitations

- Delivery is at‑least‑once; acknowledgements guarantee durability.
- Log lines must be less than 1 MB; each record must be less than 10 MB.
- Logs appear in the table a few seconds after emission.
- Schema evolution on the target table is not supported.
- Only managed Delta tables are supported (not external storage or Arclight).
- The table location must be in the same region as the workspace.
- Only single‑zone durability is supported.

^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Sources

- persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md

# Citations

1. [persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md](/references/persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws-49ce2f2e.md)
