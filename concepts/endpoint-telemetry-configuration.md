---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82036dd0b898ade1576dbf0b2af337985d564f865fdd024e71e37e77329c297c
  pageDirectory: concepts
  sources:
    - persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-telemetry-configuration
    - ETC
  citations:
    - file: persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
title: Endpoint Telemetry Configuration
description: Process for enabling telemetry on custom model serving endpoints through either the Databricks UI or REST API, including specifying Unity Catalog destination and table prefix.
tags:
  - model-serving
  - configuration
  - api
  - databricks
timestamp: "2026-06-19T19:55:01.400Z"
---

# Endpoint Telemetry Configuration

**Endpoint Telemetry Configuration** refers to the setup that persists OpenTelemetry logs, traces, and metrics from [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md) endpoints to [Unity Catalog](/concepts/unity-catalog.md) tables. This telemetry data enables root cause analysis, endpoint health monitoring, and compliance auditing using standard SQL queries. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Requirements

Before enabling endpoint telemetry, the following prerequisites must be met: ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

- The workspace must be enabled for Unity Catalog. Default storage (Arclight) is not supported.
- The user or service principal must have `USE CATALOG`, `USE SCHEMA`, `CREATE TABLE`, and `MODIFY` permissions on the destination [Catalog and Schema](/concepts/catalog-and-schema.md) where the telemetry tables will be created.
- An existing [custom model serving endpoint](/concepts/model-serving-endpoint.md) must be deployed, or permissions to create one must be present.
- The workspace must be in one of the supported regions: `us-east-1`, `us-east-2`, `us-west-2`, `eu-central-1`, `ap-southeast-1`, `ap-southeast-2`, `ap-northeast-1`, `ca-central-1`, or `eu-west-1`.

## Configuration Steps

### Step 1: Instrument Model Code

Add instrumentation to the model code to capture telemetry. Standard Python `logging` output is automatically captured without requiring the OpenTelemetry SDK. The root logging level defaults to `WARNING`. To capture lower‑severity logs, the level can be changed inside `load_context()`. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

For custom metrics and traces, the OpenTelemetry SDK can be instrumented to create counters, record spans, and attach custom attributes. The model must be written to a separate file before logging to avoid serialization errors. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

### Step 2: Prepare the Unity Catalog Destination

Before creating the endpoint, ensure a [Catalog and Schema](/concepts/catalog-and-schema.md) exist to receive the telemetry data. Databricks automatically creates the necessary tables (`<prefix>_otel_logs`, `<prefix>_otel_spans`, `<prefix>_otel_metrics`) in that schema if they do not already exist. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

### Step 3: Enable Endpoint Telemetry

Telemetry can be enabled when creating a new endpoint or added to an existing one, either through the UI or the API. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

- **Using the UI:** Navigate to **Serving**, create or edit an endpoint, expand the **Endpoint telemetry** section, and specify the destination catalog, schema, and an optional table prefix.
- **Using the API:** Include a `telemetry_config` block in the endpoint creation or update request, specifying the full Unity Catalog table names for logs, metrics, and traces.

### Step 4: Verify and Query Telemetry Data

After the endpoint receives traffic, telemetry data streams to the configured tables. Use [Catalog Explorer](/concepts/catalog-explorer.md) or the SQL Editor to locate and query the tables. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

Common queries include viewing all logs, filtering by severity and time range, and using columns such as `timestamp`, `severity_text`, `body`, `trace_id`, `span_id`, and `attributes`.

## Limitations

The following limitations apply to endpoint telemetry: ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

- Schema evolution on the target table is not supported.
- Only managed [Delta Tables](/concepts/delta-lake-table.md) are supported; external storage and Arclight default storage are not supported.
- The table location must be in the same region as the workspace.
- Table names must contain only ASCII letters, digits, and underscores.
- Recreating a target table is not supported.
- Only single availability zone (single‑az) durability is supported.
- Delivery is at‑least‑once; an acknowledgment means the record is durable.
- Each record must be less than 10 MB, each request less than 30 MB, and each log line less than 1 MB.
- Telemetry latency degrades beyond 2,500 queries per second (QPS).
- Logs appear in the Unity Catalog table a few seconds after they are emitted.

## Troubleshooting

If logs are not appearing in the table, the root logging level may be too restrictive. By default only `WARNING` and above are captured. To lower the threshold, override `load_context()` in the model and set the root logger to `DEBUG` or the desired level. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md)
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- OpenTelemetry
- [Delta Tables](/concepts/delta-lake-table.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- SQL Editor

## Sources

- persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md

# Citations

1. [persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md](/references/persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws-49ce2f2e.md)
