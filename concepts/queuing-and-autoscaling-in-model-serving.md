---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aae736d6d0ac3aa0bc40af91dc2f8ccbdc670a2cf410ca970ad6f071f872aee2
  pageDirectory: concepts
  sources:
    - optimize-model-serving-endpoints-for-production-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - queuing-and-autoscaling-in-model-serving
    - Autoscaling in Model Serving and Queuing
    - QAAIMS
    - Scaling and Auto-scaling Model Serving
    - Autoscaling for Model Serving
  citations:
    - file: optimize-model-serving-endpoints-for-production-databricks-on-aws.md
title: Queuing and Autoscaling in Model Serving
description: How traffic surges cause request queuing when autoscaling cannot provision capacity fast enough, leading to increased latency and HTTP 429 errors. Mitigation includes setting minimum provisioned concurrency, enabling route optimization, and client-side retry logic.
tags:
  - model-serving
  - scaling
  - troubleshooting
  - error-handling
timestamp: "2026-06-19T19:51:51.180Z"
---

## Queuing and Autoscaling in Model Serving

**Queuing and Autoscaling in Model Serving** describes the behavior of managed serving endpoints when incoming request traffic exceeds current processing capacity, and the mechanisms that dynamically adjust capacity to meet demand. These concepts are central to maintaining low latency and high throughput in production [Model Serving](/concepts/model-serving.md) deployments.

### Autoscaling

Databricks Model Serving supports **autoscaling** to automatically adjust the number of concurrent request slots based on observed traffic patterns. The autoscaling system continuously monitors the load on the endpoint and adds or removes capacity to match demand. However, autoscaling requires a brief period to detect an increase in traffic and to provision additional infrastructure. During that interval, incoming requests may temporarily exceed the available processing slots, causing queuing. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

### Queuing

Queuing occurs when the request rate or concurrent in‑flight requests surpass the current processing capacity of the endpoint. This typically happens during sharp traffic spikes, workload bursts, or when the endpoint’s minimum provisioned concurrency is set too low for baseline traffic. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

Model Serving endpoints allow a limited amount of queuing to absorb short‑lived bursts. Requests that are queued wait before being processed, which **increases latency** for those requests. If the queue grows beyond a defined threshold, the endpoint returns **HTTP 429 (Too Many Requests)** errors to protect system stability. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

### Mitigation Strategies

**Provisioned concurrency** controls the number of simultaneous requests the endpoint can handle. Setting appropriate minimum and maximum concurrency ranges is the primary way to reduce queuing.

- **Minimum concurrency**: Should be set high enough to handle baseline traffic plus typical bursts without queuing.
- **Maximum concurrency**: Should be high enough to accommodate traffic spikes while controlling costs.
- **Autoscaling**: Should be enabled to dynamically adjust capacity between the minimum and maximum limits.

The required concurrency can be estimated using the formula:

```
Required Concurrency = Target QPS × Average Latency (seconds)
```

For example, if the target is 100 queries per second (QPS) and the average latency is 200 ms, the required concurrency is 100 × 0.2 = 20. Actual values should be validated through [Load Testing](/concepts/locust-load-testing-framework.md). ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

**Route optimization** improves the network path between clients and the model server, reducing overhead and increasing effective capacity. It is recommended for workloads exceeding 200 QPS or with strict latency requirements, and can help reduce queuing by lowering per‑request processing time. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

**Client‑side retry logic with exponential backoff** helps gracefully handle temporary queuing and HTTP 429 errors, reducing the chance of retry storms that can further overload the endpoint. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

### Load Testing

[Load Testing](/concepts/locust-load-testing-framework.md) is a key practice to determine optimal provisioned concurrency settings and understand how the endpoint behaves under realistic traffic. It helps identify the relationship between client concurrency and server concurrency, reveal queuing thresholds, and validate latency and throughput targets before moving to production. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

### Related Concepts

- [Provisioned Concurrency](/concepts/provisioned-concurrency.md)
- Route Optimization
- Autoscaling
- HTTP 429 Too Many Requests
- Exponential Backoff
- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md)
- Latency Optimization
- Cost Optimization for Model Serving

### Sources

- optimize-model-serving-endpoints-for-production-databricks-on-aws.md

# Citations

1. [optimize-model-serving-endpoints-for-production-databricks-on-aws.md](/references/optimize-model-serving-endpoints-for-production-databricks-on-aws-6a182106.md)
