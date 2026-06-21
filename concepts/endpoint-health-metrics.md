---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6a3aba8d34d1b39440e1b76e97274d33a90c4e1aab895eb46cffd00144c1762
  pageDirectory: concepts
  sources:
    - monitor-model-quality-and-endpoint-health-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-health-metrics
    - EHM
    - Serving Endpoint Health Metrics
    - Endpoint Health Monitoring
  citations:
    - file: monitor-model-quality-and-endpoint-health-databricks-on-aws.md
title: Endpoint Health Metrics
description: Infrastructure metrics including latency, request rate, error rate, CPU usage, and memory usage for model serving endpoints.
tags:
  - monitoring
  - performance
  - infrastructure
timestamp: "2026-06-19T19:46:52.625Z"
---

# Endpoint Health Metrics

**Endpoint Health Metrics** provide infrastructure-level insights for model serving endpoints on Databricks, including key performance indicators such as latency, request rate, error rate, CPU usage, and memory usage. These metrics are essential for understanding the overall performance and health of the serving infrastructure. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Key Metrics

The infrastructure metrics captured include:
- **Latency** – Time taken to process requests.
- **Request rate** – Number of requests received per unit time.
- **Error rate** – Proportion of requests that result in errors.
- **CPU usage** – Central processing unit utilization of the serving infrastructure.
- **Memory usage** – Memory consumption of the serving environment.

These metrics allow operators to detect performance degradation, resource bottlenecks, and abnormal error patterns. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Access and Retention

Endpoint health metrics are available by default in the **Serving UI** for the last 14 days. For longer-term monitoring or integration with existing observability toolchains, the data can be streamed in real-time to external observability tools. ^[monitor-model-quality-and-endpoint-health-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – The platform that hosts and serves models.
- [Ephemeral Service Logs](/concepts/ephemeral-service-logs.md) – Real-time debug logs from the serving endpoint.
- [OpenTelemetry for custom model serving endpoints](/concepts/opentelemetry-for-model-serving.md) – Persisted logs, metrics, and traces in Unity Catalog.
- Build logs – Logs from the environment build process.
- [AI Gateway-enabled inference tables](/concepts/ai-gateway-inference-tables.md) – Logging of prediction requests and responses.
- Monitoring and diagnostics for serving endpoints – Overview of all monitoring tools.

## Sources

- monitor-model-quality-and-endpoint-health-databricks-on-aws.md

# Citations

1. [monitor-model-quality-and-endpoint-health-databricks-on-aws.md](/references/monitor-model-quality-and-endpoint-health-databricks-on-aws-9318b2eb.md)
