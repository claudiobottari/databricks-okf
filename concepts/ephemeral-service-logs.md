---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9bd47ba2ae79ea8ea4f4c5c523906d473e5d1b344b669bd613c837000d355b59
  pageDirectory: concepts
  sources:
    - monitor-model-quality-and-endpoint-health-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ephemeral-service-logs
    - ESL
    - Service Logs
  citations:
    - file: monitor-model-quality-and-endpoint-health-databricks-on-aws.md
title: Ephemeral Service Logs
description: Real-time stdout/stderr logs from model serving endpoints, useful for debugging during deployment.
tags:
  - logging
  - debugging
  - model-serving
timestamp: "2026-06-19T19:47:18.773Z"
---

# Ephemeral Service Logs

**Ephemeral Service Logs** capture the `stdout` and `stderr` streams from a model serving endpoint on Databricks. These logs provide real-time visibility into the execution of model deployments, making them a primary tool for debugging during model deployment. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Overview

Ephemeral service logs are designed for short-term, interactive debugging rather than long-term storage or compliance use cases. They are accessible through the **Logs tab** in the Serving UI, where logs are streamed in real-time as the endpoint processes requests. Logs can also be exported programmatically through the REST API. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Usage

To capture output in ephemeral service logs, use standard Python logging within your model serving code. Calls to `logging.warning(...)` or `logging.error(...)` are immediately displayed in the logs, making them effective for surfacing issues during development and testing. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Comparison with Other Logging Tools

Ephemeral service logs serve a different purpose than other monitoring tools available for model serving endpoints:

| Tool | Purpose | Retention |
|------|---------|-----------|
| **Ephemeral service logs** | Real-time debugging during deployment | Not specified for long-term retention |
| **OpenTelemetry logs** | Historical debugging, compliance, production analysis | Persisted to Unity Catalog Delta tables |
| **Build logs** | Diagnosing model deployment and dependency issues | Up to 30 days |

^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

While ephemeral service logs are ideal for immediate troubleshooting, [OpenTelemetry for custom model serving endpoints](/concepts/opentelemetry-for-model-serving.md) should be configured when long-term log retention, compliance requirements, or historical analysis using SQL queries are needed. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Access Methods

- **Serving UI**: View logs in real-time through the **Logs tab** on the endpoint dashboard.
- **REST API**: Export logs programmatically using the [Serving Endpoints Logs API](https://docs.databricks.com/api/workspace/servingendpoints/logs).

^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Best Practices

- Use `logging.warning()` and `logging.error()` for output that should be immediately visible in the logs.
- For debugging during initial model deployment, ephemeral service logs provide the fastest feedback loop.
- Consider using [AI Gateway-enabled inference tables](/concepts/ai-gateway-inference-tables.md) or [OpenTelemetry for custom model serving endpoints](/concepts/opentelemetry-for-model-serving.md) for production monitoring, audit trails, and long-term analysis.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The platform that deploys and serves models on Databricks.
- [OpenTelemetry for custom model serving endpoints](/concepts/opentelemetry-for-model-serving.md) — Persistent logging and tracing solution.
- [AI Gateway-enabled inference tables](/concepts/ai-gateway-inference-tables.md) — Automatic logging of prediction requests and responses.
- Build logs — Logs from the model deployment environment creation process.
- [Endpoint Health Metrics](/concepts/endpoint-health-metrics.md) — Infrastructure performance metrics like latency, request rate, and CPU usage.

## Sources

- monitor-model-quality-and-endpoint-health-databricks-on-aws.md

# Citations

1. [monitor-model-quality-and-endpoint-health-databricks-on-aws.md](/references/monitor-model-quality-and-endpoint-health-databricks-on-aws-9318b2eb.md)
