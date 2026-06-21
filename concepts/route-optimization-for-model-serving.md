---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: faef18039fbf92fe98d85ea1a50255a6e710189d2d0f78aad19ff9ca8905226c
  pageDirectory: concepts
  sources:
    - optimize-model-serving-endpoints-for-production-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - route-optimization-for-model-serving
    - ROFMS
    - Cost Optimization for Model Serving
    - Production Optimization for Model Serving
    - Production optimization for ML serving
    - route-optimization-databricks-model-serving
    - RO(MS
  citations:
    - file: optimize-model-serving-endpoints-for-production-databricks-on-aws.md
title: Route Optimization for Model Serving
description: A Databricks-specific optimization that improves the network path for inference requests, resulting in faster, more direct communication between clients and models. Supports workloads above 200 QPS and sub-50ms overhead.
tags:
  - model-serving
  - infrastructure
  - optimization
  - networking
timestamp: "2026-06-19T19:51:26.089Z"
---

# Route Optimization for Model Serving

**Route Optimization for Model Serving** is an infrastructure feature in Databricks Model Serving that improves the network path for inference requests. When enabled on a serving endpoint, it establishes a faster, more direct communication channel between clients and the model, reducing network overhead and latency. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## Performance Benefits

Route optimization provides the most significant infrastructure improvement for high-throughput workloads. Key performance benefits include:

- **Reduced latency**: Requests take a shorter network path, lowering per-request overhead.
- **Improved throughput**: Higher request rates can be sustained without queuing.
- **Higher capacity limits**: The endpoint can handle more concurrent connections before hitting throttling thresholds.
- **Lower overhead**: Network-level optimisations reduce the processing burden on each inference call.

^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## When to Use Route Optimization

Route optimization is recommended for:

- Workloads that require more than 200 queries per second (QPS).
- Applications with strict latency requirements, particularly when the added network overhead must stay below 50 ms.
- Production deployments that serve multiple concurrent users and need consistent performance.

^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## Requirements and Limitations

- **Endpoint type**: Route optimization is only available for **custom model serving endpoints**. Foundation Model APIs and external models do not support it. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]
- **Authentication**: OAuth tokens are required for querying route-optimized endpoints. Personal access tokens are not supported. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]
- **Setup**: Detailed instructions for enabling route optimization are documented separately (see [Route optimization on serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/route-optimization)). Querying a route-optimized endpoint also requires a dedicated procedure (see [Query route-optimized serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/query-route-optimization)). ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## Integration with Other Optimizations

Route optimization complements other performance strategies. For example, it raises the capacity limits that can be reached before a serving endpoint starts queuing requests, making it a valuable addition when tuning [Provisioned Concurrency](/concepts/provisioned-concurrency.md) and implementing client-side retry logic with exponential backoff. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – The core deployment unit for models in Databricks.
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md) – Controls how many simultaneous requests an endpoint can handle.
- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) – Used to determine optimal concurrency settings and validate route optimisation benefits.
- Performance Monitoring for Model Serving – Tools to monitor endpoint health after enabling route optimization.
- Client-side Optimizations – Practices such as connection pooling that further improve throughput.

## Sources

- optimize-model-serving-endpoints-for-production-databricks-on-aws.md

# Citations

1. [optimize-model-serving-endpoints-for-production-databricks-on-aws.md](/references/optimize-model-serving-endpoints-for-production-databricks-on-aws-6a182106.md)
