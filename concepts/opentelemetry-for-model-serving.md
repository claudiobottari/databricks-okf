---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2aa57eb316b25b3d75eff1fc076b67b692b0af24c29c4b2e33685aca545ce48
  pageDirectory: concepts
  sources:
    - monitor-model-quality-and-endpoint-health-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opentelemetry-for-model-serving
    - OFMS
    - OpenTelemetry for custom model serving endpoints
  citations:
    - file: monitor-model-quality-and-endpoint-health-databricks-on-aws.md
title: OpenTelemetry for Model Serving
description: Persists system logs, application logs, metrics, and traces to Unity Catalog Delta tables using OpenTelemetry for long-term retention and compliance.
tags:
  - observability
  - logging
  - unity-catalog
  - opentelemetry
timestamp: "2026-06-19T19:46:53.745Z"
---

# OpenTelemetry for Model Serving

**OpenTelemetry for Model Serving** is a monitoring tool on Databricks that persists standard system logs, custom application logs, metrics, and traces to [Unity Catalog](/concepts/unity-catalog.md) Delta tables using the OpenTelemetry standard. It is designed for long-term retention of telemetry data from custom model serving endpoints. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Overview

OpenTelemetry for Model Serving enables you to collect and store observability data from your deployed models beyond the ephemeral logs available through the Serving UI. The telemetry is written to Delta tables managed by Unity Catalog, allowing you to retain data for compliance, historical debugging, and post‑incident analysis. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

This tool is one of several monitoring options provided by [Model Serving](/concepts/model-serving.md). Unlike the real‑time streaming logs available in the **Logs** tab, OpenTelemetry‑based telemetry persists data for querying over extended periods. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Configuration

You configure telemetry settings in the [Serving UI](/concepts/serving-ui.md) or via the Serving Endpoints REST API when you create the endpoint. During endpoint creation, you specify the Unity Catalog location where the telemetry data will be stored. Once the endpoint is operational, OpenTelemetry automatically collects and writes system logs, application logs, metrics, and traces to the specified Delta tables. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

> **Note:** This feature is available only for custom model serving endpoints (i.e., endpoints serving models built on Databricks, not external model endpoints). ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Querying Telemetry Data

After the data is persisted, you can query the telemetry using Unity Catalog SQL or from a Databricks Notebook. This allows you to run complex analytical queries, join telemetry data with other tables, and build custom dashboards for production monitoring. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

Typical use cases for querying include:
- Historical debugging of model prediction errors.
- Auditing model behavior over time for compliance requirements.
- Analyzing latency or error patterns across different model versions or traffic slices.

## Use Cases

OpenTelemetry for Model Serving is particularly useful when:
- You need to retain logs, metrics, and traces for longer than the default 14‑day retention of endpoint health metrics or the 30‑day retention of build logs.
- Compliance or regulatory requirements mandate long‑term storage of prediction and system telemetry.
- You want to perform retrospective analysis of production issues using SQL against a structured data lakehouse.

## Related Concepts

- [Ephemeral Service Logs](/concepts/ephemeral-service-logs.md) – Real‑time streaming logs for debugging during deployment.
- [Endpoint Health Metrics](/concepts/endpoint-health-metrics.md) – Infrastructure metrics (latency, request rate, CPU, memory) with 14‑day default retention.
- [AI Gateway‑enabled inference tables](/concepts/ai-gateway-inference-tables.md) – Alternative logging mechanism that captures prediction requests and responses.
- [Unity Catalog](/concepts/unity-catalog.md) – Centralized governance and storage layer for the telemetry Delta tables.
- OpenTelemetry – The open standard used for exporting telemetry data.

## Sources

- monitor-model-quality-and-endpoint-health-databricks-on-aws.md

# Citations

1. [monitor-model-quality-and-endpoint-health-databricks-on-aws.md](/references/monitor-model-quality-and-endpoint-health-databricks-on-aws-9318b2eb.md)
