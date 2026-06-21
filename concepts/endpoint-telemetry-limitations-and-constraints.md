---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ae3ddc9a126c9c8e85f9ac68be72e7e7170b0e4dd62277ba32559bccb8b41802
  pageDirectory: concepts
  sources:
    - persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-telemetry-limitations-and-constraints
    - Constraints and Endpoint Telemetry Limitations
    - ETLAC
  citations:
    - file: persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md
title: Endpoint Telemetry Limitations and Constraints
description: Boundaries of the telemetry feature including no schema evolution, managed Delta tables only, region restrictions, at-least-once delivery, size limits, and QPS thresholds.
tags:
  - model-serving
  - constraints
  - databricks
  - limits
timestamp: "2026-06-19T19:55:09.070Z"
---

# Endpoint Telemetry Limitations and Constraints

**Endpoint Telemetry Limitations and Constraints** refers to the set of technical boundaries and operational restrictions that apply when persisting OpenTelemetry logs, traces, and metrics from custom model serving endpoints to Unity Catalog tables on Databricks. Understanding these constraints is essential for designing reliable telemetry pipelines and avoiding unexpected failures.

## Table Schema and Storage Constraints

Schema evolution on the target telemetry table is not supported. Once the table is created by the endpoint telemetry system, its schema cannot be modified. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

Only managed Delta tables are supported as the destination for telemetry data. External storage locations and the default Arclight storage are not supported. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

Recreating a target table after it has been created is not supported. If the table is dropped or needs to be replaced, a new endpoint configuration or a different table name must be used. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Regional and Naming Constraints

The Unity Catalog table location must be in the same region as the workspace. Cross-region telemetry storage is not supported. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

Only table names containing ASCII letters, digits, and underscores are supported. Special characters or non-ASCII characters in table names will cause errors. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Durability and Delivery Constraints

Only single availability zone (single-az) durability is supported for the telemetry tables. Multi-zone durability is not available. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

Delivery of telemetry records is at-least-once. An acknowledgement from the server indicates the record is durable and written to the Delta table, but duplicate records may occur in rare circumstances. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Size and Throughput Constraints

Individual records must be less than 10 MB each. Records exceeding this limit will be rejected. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

Individual requests must be less than 30 MB each. Requests exceeding this limit will be rejected. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

Individual log lines must be less than 1 MB each. Log lines exceeding this limit will be truncated or rejected. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Performance Constraints

Telemetry latency degrades beyond 2500 queries per second (QPS). At higher throughput levels, the time between emission and availability in the Unity Catalog table may increase significantly. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

Logs appear in the Unity Catalog table a few seconds after they are emitted under normal conditions. This latency may increase under high load or when approaching the 2500 QPS threshold. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Logging Level Default

The root logging level defaults to `WARNING` to reduce overhead. Lower-severity logs (such as `INFO` or `DEBUG`) are not captured unless explicitly configured in the model code. ^[persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md) — The serving infrastructure that generates telemetry data
- [Unity Catalog](/concepts/unity-catalog.md) — The destination for persisted telemetry tables
- OpenTelemetry — The observability framework used for logs, traces, and metrics
- [Model Serving Endpoint Telemetry](/concepts/model-serving-endpoint-telemetry.md) — Overview of the telemetry persistence feature
- [Delta Tables](/concepts/delta-lake-table.md) — The table format used for telemetry storage
- At-Least-Once Delivery — The delivery semantics for telemetry records

## Sources

- persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md

# Citations

1. [persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws.md](/references/persist-custom-model-serving-data-to-unity-catalog-databricks-on-aws-49ce2f2e.md)
