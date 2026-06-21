---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8090e502713bae04d3a55f95cd69fc34f564e6e951522016dc61d19ed1390c53
  pageDirectory: concepts
  sources:
    - create-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compute-scale-out-and-scale-to-zero
    - Scale-to-Zero and Compute Scale-Out
    - CSAS
    - Scale to Zero|scaled to 0
  citations:
    - file: create-custom-model-serving-endpoints-databricks-on-aws.md
title: Compute Scale-Out and Scale-to-Zero
description: Model serving endpoints support Small/Medium/Large compute scale-out sizes (0-4, 8-16, 16-64 concurrent requests) and optional scale-to-zero, though scale-to-zero incurs cold-start latency and is not recommended for production.
tags:
  - model-serving
  - scaling
  - compute
timestamp: "2026-06-18T11:22:38.186Z"
---

# Compute Scale-Out and Scale-to-Zero

**Compute Scale-Out** and **Scale-to-Zero** are configuration options for [model serving endpoints](/concepts/model-serving-endpoint.md) in Databricks Model Serving. They control how much compute capacity is allocated to a served model and how that capacity behaves during idle periods. The right settings balance throughput, latency, and cost.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

## Compute Scale-Out

Compute Scale-Out determines the number of concurrent requests a served model can process at the same time. It is set per served entity (model version) when creating or updating an endpoint.

- The available sizes are **Small** (0–4 concurrent requests), **Medium** (8–16 requests), and **Large** (16–64 requests).^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- As a rough guideline, the scale-out number should equal the expected queries per second (QPS) multiplied by the model’s inference time.^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- For GPU endpoints, concurrency maps to the number of replicas: one replica per 4 units of concurrency. For example, `min_provisioned_concurrency` of 12 provisions 3 replicas.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

Choosing the appropriate scale-out size ensures that the endpoint has enough capacity to handle the anticipated request volume without excessive queuing or throttling.

## Scale-to-Zero

The Scale-to-Zero option lets an endpoint reduce its resource allocation to zero when it is not receiving requests. This can save cost during low‑usage periods.

- Scale-to-zero is **not recommended for production endpoints**, because capacity is not guaranteed when the endpoint is scaled down.^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- When a request arrives at a scaled‑to‑zero endpoint, the system must allocate new compute resources. This introduces a **cold start** — additional latency while the model loads and becomes ready to serve traffic.^[create-custom-model-serving-endpoints-databricks-on-aws.md]

For development, testing, or infrequently used endpoints, scale-to-zero can reduce waste. For production workloads, keeping a minimum number of provisioned replicas (e.g., setting a minimum concurrency) avoids cold starts and ensures consistent responsiveness.

## Best Practices

- **For production endpoints:** Disable scale-to-zero and set a minimum concurrency that matches your baseline traffic. This reserves capacity and eliminates cold-start latency.^[create-custom-model-serving-endpoints-databricks-on-aws.md]
- **For development or experimentation:** Enable scale-to-zero to reduce costs when the endpoint is idle. Accept that the first request may experience a delay.
- **Tune scale-out size empirically.** Start with the formula `QPS × model run time`, then adjust upward if you observe request queuing or downward if the endpoint is underutilized.
- **Monitor endpoint metrics** (e.g., request latency, queue depth, utilization) and adjust the scale-out configuration accordingly.

## Related Concepts

- [Model serving endpoints](/concepts/model-serving-endpoint.md)
- Cold start
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)
- Serving endpoint configuration
- [GPU workload types in Model Serving](/concepts/gpu-workload-types-for-model-serving.md)

## Sources

- create-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [create-custom-model-serving-endpoints-databricks-on-aws.md](/references/create-custom-model-serving-endpoints-databricks-on-aws-8aa3cc25.md)
