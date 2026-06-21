---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6b38a15b3241e3680682a159ef904357ef0d0f34949ce6e9a0e9769a2dae1700
  pageDirectory: concepts
  sources:
    - persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - telemetry-data-querying-and-analysis
    - Analysis and Telemetry Data Querying
    - TDQAA
  citations:
    - file: persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
title: Telemetry Data Querying and Analysis
description: Patterns for querying persisted endpoint telemetry data using SQL, including filtering by severity, timestamp, trace IDs, and custom attributes for root cause analysis.
tags:
  - sql
  - observability
  - monitoring
  - analytics
timestamp: "2026-06-19T19:55:07.716Z"
---

# Telemetry Data Querying and Analysis

**Telemetry Data Querying and Analysis** refers to the process of inspecting, filtering, and deriving insights from operational telemetry data — including logs, traces, and metrics — that is persisted from [custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md) to [Unity Catalog](/concepts/unity-catalog.md) tables. This capability enables root cause analysis, endpoint health monitoring, and compliance verification using standard SQL queries.

## Overview

When endpoint telemetry is enabled for a custom model serving endpoint, telemetry data streams to configured Unity Catalog tables. These tables are automatically created in the specified [Catalog and Schema](/concepts/catalog-and-schema.md), and follow the naming convention `<prefix>_otel_logs`, `<prefix>_otel_spans`, and `<prefix>_otel_metrics`. The telemetry data includes standard Python logging output, custom OpenTelemetry metrics and traces, and associated metadata such as timestamps and severity levels. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Table Schema

Each telemetry table contains columns that support detailed querying and correlation:

- `timestamp` – When the log, span, or metric was recorded
- `severity_text` – The severity level (e.g., `ERROR`, `WARNING`) for logs
- `body` – The log message body
- `trace_id` – Identifier for correlating spans and logs across a request
- `span_id` – Identifier for individual spans within a trace
- `attributes` – A map column containing event-specific metadata

To view the full schema of any telemetry table, run:
```sql
DESCRIBE TABLE <catalog>.<schema>.<prefix>_otel_logs;
```

^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Common Query Patterns

### Basic Data Verification

After the endpoint receives traffic, verify that telemetry data is flowing:
```sql
SELECT * FROM <catalog>.<schema>.<prefix>_otel_logs
LIMIT 10;
```

### Error Investigation

Check for errors in the last hour to identify issues:
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

## Use Cases

- **Root cause analysis**: Correlate error logs, traces, and metrics using `trace_id` and `span_id` to understand the full context of a failure.
- **Endpoint health monitoring**: Track error rates, latency, and prediction counts over time by querying metrics and logs tables.
- **Compliance**: Retain and audit telemetry data in Unity Catalog for regulatory requirements.
- **Performance optimization**: Analyze span timing data to identify bottlenecks in model inference pipelines.

^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Data Flow and Latency

Telemetry data is delivered with **at-least-once** semantics — an acknowledgement from the server means the record is durable and written to the Delta table. Logs appear in the Unity Catalog table a few seconds after they are emitted. However, telemetry latency degrades beyond 2500 queries per second (QPS) for a given endpoint. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Limitations

- Schema evolution on the target table is not supported.
- Only managed Delta tables are supported; external storage and Arclight default storage are not supported.
- The table location must be in the same region as your workspace.
- Only table names with ASCII letters, digits, and underscores are supported.
- Recreating a target table is not supported.
- Only single availability zone (single-az) durability is supported.
- Records must be less than 10 MB each; requests must be less than 30 MB each; log lines must be less than 1 MB each.

^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Troubleshooting

If logs are not appearing in the table, the root logging level may be set too high. By default, the root logging level is `WARNING` to reduce overhead. To capture lower-severity logs, change the level in your model code:

```python
class MyModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        for handler in root.handlers:
            handler.setLevel(logging.DEBUG)
```

^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) – The source of telemetry data.
- [Unity Catalog](/concepts/unity-catalog.md) – The destination where telemetry tables are stored.
- OpenTelemetry – The instrumentation framework used for logging, traces, and metrics.
- [Model Serving Monitoring](/concepts/databricks-model-serving-monitoring.md) – Broader monitoring practices for deployed models.
- [Root Cause Analysis](/concepts/inference-tables-for-root-cause-analysis.md) – A primary use case for telemetry data querying.
- [Delta Tables](/concepts/delta-lake-table.md) – The table format used for telemetry storage.
- SQL Analytics – Querying capabilities for analyzing telemetry data.

## Sources

- persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md

# Citations

1. [persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md](/references/persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws-49ce2f2e.md)
