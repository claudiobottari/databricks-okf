---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d8894fdfe21d90e592616858fe2dadbac995119fb644e4a6477299bba5ef288
  pageDirectory: concepts
  sources:
    - persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-telemetry
    - MSET
  citations:
    - file: persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
title: Model Serving Endpoint Telemetry
description: A Databricks feature that persists OpenTelemetry logs, traces, and metrics from custom model serving endpoints to Unity Catalog tables for monitoring and compliance.
tags:
  - model-serving
  - observability
  - unity-catalog
  - databricks
timestamp: "2026-06-19T19:54:45.067Z"
---

# Model Serving Endpoint Telemetry

**Model Serving Endpoint Telemetry** is a Databricks feature (in Beta) that persists OpenTelemetry logs, traces, and metrics from [custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md) into [Unity Catalog](/concepts/unity-catalog.md) tables. This enables root cause analysis, endpoint health monitoring, and compliance auditing using standard SQL queries. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Requirements

To configure endpoint telemetry, the workspace must be enabled for Unity Catalog (default Arclight storage is not supported). The user must have `USE CATALOG`, `USE SCHEMA`, `CREATE TABLE`, and `MODIFY` permissions on the destination [Catalog and Schema](/concepts/catalog-and-schema.md). An existing custom model serving endpoint (or permissions to create one) is required. The workspace must be in a supported AWS region: `us-east-1`, `us-east-2`, `us-west-2`, `eu-central-1`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`, `ca-central-1`, or `eu-west-1`. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Step 1: Instrument Your Model Code

Add application logging to the model using standard Python `logging`; no OpenTelemetry SDK instrumentation is required for basic logging. The root logging level defaults to `WARNING`. To capture lower-severity logs, change the level in the model’s `load_context` method. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

Optionally, instrument custom metrics and traces using the OpenTelemetry SDK — for example, creating counters, recording spans, and attaching attributes. Due to model serialization limitations, the model class must be written to a separate file before logging with MLflow, and the pip requirements must include `opentelemetry-sdk` and `opentelemetry-exporter-otlp-proto-http`. The model is then logged and registered using `mlflow.pyfunc.log_model` and `mlflow.register_model` with `env_pack="databricks_model_serving"`. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Step 2: Prepare the Unity Catalog Destination

Before creating the endpoint, ensure the target [Catalog and Schema](/concepts/catalog-and-schema.md) exist (e.g., `my_catalog.observability`). Databricks automatically creates the required tables in that schema if they do not already exist. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Step 3: Enable Endpoint Telemetry

Telemetry can be enabled when creating a new serving endpoint or added to an existing one. In the UI, navigate to **Serving** → **Create serving endpoint**. Under **Endpoint telemetry** (marked Preview), select the Unity Catalog location ([Catalog and Schema](/concepts/catalog-and-schema.md)). Optionally provide a table prefix; the generated tables are named `<prefix>_otel_logs`, `<prefix>_otel_spans`, and `<prefix>_otel_metrics`. If no prefix is given, no prefix is used. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

Alternatively, use the [Serving Endpoints API](https://docs.databricks.com/aws/en/api/workspace/serving-endpoints) to enable telemetry by including a `telemetry_config` block with fully qualified table names under `table_names` (keys: `logs_table`, `metrics_table`, `traces_table`). ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Step 4: Verify and Query Telemetry Data

After the endpoint receives traffic, telemetry data streams to the configured Unity Catalog tables. In Catalog Explorer or the SQL Editor, locate the `<prefix>_otel_logs` table and run a `SELECT *` query to verify data is flowing. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

Use `DESCRIBE TABLE` to view the full schema of any telemetry table. Key columns include `timestamp`, `severity_text`, `body`, `trace_id`, `span_id`, and `attributes` (a map containing event-specific metadata). Common queries include checking for errors in the last hour by filtering on `severity_text = 'ERROR'` and `timestamp > current_timestamp() - INTERVAL 1 HOUR`. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Troubleshooting

If logs do not appear in the table, the root logging level may be set to `WARNING`. In the model’s `load_context` method, retrieve the root logger and set its level (and all handlers) to `DEBUG` to capture lower-severity messages. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Limitations

- Schema evolution on the target table is not supported.
- Only managed [Delta tables](/concepts/delta-lake-table.md) are supported; external storage and Arclight default storage are not.
- The table location must be in the same region as the workspace.
- Table names may contain only ASCII letters, digits, and underscores.
- Recreating a target table is not supported.
- Only single availability zone (single-az) durability is supported.
- Delivery is at-least-once.
- Individual records must be less than 10 MB; requests less than 30 MB; log lines less than 1 MB.
- Telemetry latency degrades beyond 2500 QPS.
- Logs appear in the Unity Catalog table a few seconds after emission. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Sources

- persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md

# Citations

1. [persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md](/references/persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws-49ce2f2e.md)
