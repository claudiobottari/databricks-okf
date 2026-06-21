---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4a0584ed38768d577b8074dd564774635237012e8a3173085329fb4c9f91e8a4
  pageDirectory: concepts
  sources:
    - serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-llm-serving-telemetry-and-monitoring
    - Monitoring and Custom LLM Serving Telemetry
    - CLSTAM
  citations:
    - file: serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
title: Custom LLM Serving Telemetry and Monitoring
description: Observability infrastructure for custom LLM serving endpoints, including live logs, persisted logs and metrics to Unity Catalog Delta tables, and automatic scraping of vLLM Prometheus metrics.
tags:
  - monitoring
  - telemetry
  - observability
timestamp: "2026-06-19T23:02:27.945Z"
---

# Custom LLM Serving Telemetry and Monitoring

**Custom LLM Serving Telemetry and Monitoring** refers to the observability infrastructure available for custom LLM serving endpoints deployed on [Databricks Model Serving](/concepts/databricks-model-serving.md). It provides real-time logs, automatically persisted logs and metrics to [Unity Catalog](/concepts/unity-catalog.md), and the ability to query telemetry data via SQL or notebooks. This infrastructure is built on the same foundation as standard [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md) endpoints, with additional vLLM-specific metrics. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Live Logs

The **Logs** tab on the endpoint page in the [Serving UI](/concepts/serving-ui.md) displays `stdout` and `stderr` output from the vLLM process in real time. Users can also retrieve this output programmatically through the [Serving Endpoints Logs API](https://docs.databricks.com/api/workspace/servingendpoints/logs). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Persisted Logs and Metrics

When telemetry is enabled, both logs and metrics are persisted to [Unity Catalog](/concepts/unity-catalog.md) Delta tables for long-term retention, SQL querying, and compliance. Full setup instructions, requirements, and table schemas are documented in [Persist custom [Model Serving](/concepts/model-serving.md) data to [Unity Catalog](/concepts/unity-catalog.md)](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-model-serving-uc-logs). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### Logs

`stdout` and `stderr` from the vLLM process are captured automatically, without requiring any application-side logging code. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### Metrics

Databricks automatically scrapes the vLLM server’s Prometheus `/metrics` endpoint and persists the metrics alongside logs. The default set of collected metrics includes: ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

- Per-request latency
- Throughput
- Token counts
- Queue depth
- KV-cache utilization

## Querying Telemetry Data

During the Beta phase, there is no UI for visualizing persisted logs or metrics. Users must query the data directly in [Unity Catalog](/concepts/unity-catalog.md) using SQL or a notebook. The metric and log schemas are documented in the [Persist custom [Model Serving](/concepts/model-serving.md) data to [Unity Catalog](/concepts/unity-catalog.md)](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-model-serving-uc-logs) page. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

A dedicated notebook titled **Custom LLM serving metrics notebook** is linked from the documentation to demonstrate how to parse and visualize the persisted vLLM metrics. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Limitations

The following limitations apply during Beta: ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

- No UI for visualizing logs or metrics. All telemetry data must be queried directly in [Unity Catalog](/concepts/unity-catalog.md).
- Only the LLM chat task (`llm/v1/chat`) is supported.
- No autoscaling between replicas (scale-to-zero is supported on most GPU types except `GPU_XLARGE`).
- No route optimization.

## Related Concepts

- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md)
- vLLM
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Tables](/concepts/delta-lake-table.md)
- Prometheus
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- Serving Endpoints Logs API
- [AI Playground](/concepts/ai-playground.md)

## Sources

- serve-custom-llms-with-custom-model-serving-databricks-on-aws.md

# Citations

1. [serve-custom-llms-with-custom-model-serving-databricks-on-aws.md](/references/serve-custom-llms-with-custom-model-serving-databricks-on-aws-ee23a7aa.md)
