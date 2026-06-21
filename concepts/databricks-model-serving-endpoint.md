---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 506c393ad9f35e1daf6b5672295bca832de308e7188da1d0e1e5e3d740514d76
  pageDirectory: concepts
  sources:
    - model-serving-concepts-databricks-on-aws.md
    - track-and-export-serving-endpoint-health-metrics-to-prometheus-and-datadog-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-model-serving-endpoint
    - DMSE
    - Databricks Serving Endpoint
    - Databricks serving endpoint
    - Databricks serving endpoint|model serving endpoint
  citations:
    - file: model-serving-concepts-databricks-on-aws.md
    - file: track-and-export-serving-endpoint-health-metrics-to-prometheus-and-datadog-databricks-on-aws.md
title: Databricks Model Serving Endpoint
description: A REST API endpoint (POST /api/2.0/serving-endpoints) for deploying and managing machine learning models for inference on Databricks.
tags:
  - databricks
  - model-serving
  - api
timestamp: "2026-06-19T19:43:32.020Z"
---

# Databricks Model Serving Endpoint

A **Databricks Model Serving Endpoint** is a managed REST API endpoint that hosts one or more machine learning models for real-time inference. It provides infrastructure for serving models at scale, with built-in traffic management, provisioning, and health monitoring capabilities. The endpoint is created and configured through the Databricks REST API, CLI, or UI. ^[model-serving-concepts-databricks-on-aws.md]

## Key Features

### Traffic Splitting

An endpoint can serve multiple model versions simultaneously by defining a **traffic configuration** that specifies the percentage of requests routed to each served entity. For example, you could send 60% of traffic to a smaller model and 40% to a larger model, enabling A/B testing or gradual rollouts. Traffic percentages are assigned via the `routes` array in the endpoint configuration payload. ^[model-serving-concepts-databricks-on-aws.md]

### Provisioned Throughput

Each served entity can have `min_provisioned_throughput` and `max_provisioned_throughput` values (measured in queries per second or tokens per second). Setting a minimum ensures baseline capacity, while the maximum allows the endpoint to scale up under load. Provisioned throughput is managed per-model within the endpoint. ^[model-serving-concepts-databricks-on-aws.md]

### Multi-Model Endpoints

A single endpoint can host several models (e.g., a 70B-parameter model alongside an 8B-parameter model) by listing multiple `served_entities` in the configuration. Each entity is referenced by its model name and version in Unity Catalog or the Model Registry. ^[model-serving-concepts-databricks-on-aws.md]

## Health Metrics and Export

Model serving endpoints emit a set of **health metrics** that measure infrastructure behavior, including:

- `cpu_usage_percentage` – CPU utilization.
- `mem_usage_percentage` – Memory utilization.
- `request_latency_ms` – Request latency (histogram).
- `request_count_total` – Total request count.
- `request_4xx_count_total` – Number of 4xx client errors.
- `request_5xx_count_total` – Number of 5xx server errors.
- `provisioned_concurrent_requests_total` – Number of concurrent requests against provisioned capacity.

^[track-and-export-serving-endpoint-health-metrics-to-prometheus-and-datadog-databricks-on-aws.md]

These metrics can be exported in OpenMetrics format via the API endpoint `GET /api/2.0/serving-endpoints/{endpoint_name}/metrics`. Databricks supports integration with both Prometheus and Datadog for scraping and monitoring. ^[track-and-export-serving-endpoint-health-metrics-to-prometheus-and-datadog-databricks-on-aws.md]

### Prometheus Integration

To export metrics to a local Prometheus instance:

1.  Create a `prometheus.yml` configuration file pointing to the Databricks metrics endpoint and authenticating with a Bearer token (PAT).
2.  Start Prometheus using Docker with the configuration mounted.
3.  Query metrics such as `cpu_usage_percentage` from the Prometheus UI at `http://localhost:9090`.

^[track-and-export-serving-endpoint-health-metrics-to-prometheus-and-datadog-databricks-on-aws.md]

### Datadog Integration

To send metrics to Datadog:

1.  Install the Datadog agent and the OpenMetrics integration.
2.  Configure an OpenMetrics check in a `conf.yaml` file pointing to the Databricks metrics endpoint, listing the desired metrics and their types (e.g., gauge, histogram).
3.  Start the agent and verify it is collecting metric samples.

Alternatively, Datadog offers a native Databricks integration that connects to model serving endpoints without requiring custom configuration. ^[track-and-export-serving-endpoint-health-metrics-to-prometheus-and-datadog-databricks-on-aws.md]

## API Usage

Endpoints are created and managed via the Databricks Serving Endpoint API. The following is a representative payload for creating a multi-model endpoint with traffic splitting:

```json
POST /api/2.0/serving-endpoints
{
  "name": "multi-pt-model",
  "config": {
    "served_entities": [
      {
        "name": "meta_llama_v3_1_70b_instruct",
        "entity_name": "system.ai.meta_llama_v3_1_70b_instruct",
        "entity_version": "4",
        "min_provisioned_throughput": 0,
        "max_provisioned_throughput": 2400
      },
      {
        "name": "meta_llama_v3_1_8b_instruct",
        "entity_name": "system.ai.meta_llama_v3_1_8b_instruct",
        "entity_version": "4",
        "min_provisioned_throughput": 0,
        "max_provisioned_throughput": 1240
      }
    ],
    "traffic_config": {
      "routes": [
        {
          "served_model_name": "meta_llama_v3_1_8b_instruct",
          "traffic_percentage": "60"
        },
        {
          "served_model_name": "meta_llama_v3_1_70b_instruct",
          "traffic_percentage": "40"
        }
      ]
    }
  }
}
```

^[model-serving-concepts-databricks-on-aws.md]

To check endpoint health, use:

```bash
curl -n -X GET \
  -H "Authorization: Bearer [PAT]" \
  https://[DATABRICKS_HOST]/api/2.0/serving-endpoints/[ENDPOINT_NAME]
```

^[track-and-export-serving-endpoint-health-metrics-to-prometheus-and-datadog-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) – Overview of deploying models on Databricks.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Configuration for scaling model serving capacity.
- Prometheus – Monitoring system for time-series metrics.
- Datadog – Monitoring platform with native Databricks integration.
- [MLflow](/concepts/mlflow.md) – Lifecycle management for models deployed to endpoints.
- [Serving Endpoint Health Metrics](/concepts/endpoint-health-metrics.md) – Detailed metrics reference.

## Sources

- model-serving-concepts-databricks-on-aws.md
- track-and-export-serving-endpoint-health-metrics-to-prometheus-and-datadog-databricks-on-aws.md

# Citations

1. [model-serving-concepts-databricks-on-aws.md](/references/model-serving-concepts-databricks-on-aws-b4c5ea15.md)
2. [track-and-export-serving-endpoint-health-metrics-to-prometheus-and-datadog-databricks-on-aws.md](/references/track-and-export-serving-endpoint-health-metrics-to-prometheus-and-datadog-databricks-on-aws-63a21a43.md)
