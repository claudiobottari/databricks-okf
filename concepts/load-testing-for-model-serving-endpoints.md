---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c874d0f71e12ab88d82f28a32a6cd49b08cd81e36b02af394d300730ea523f4e
  pageDirectory: concepts
  sources:
    - optimize-model-serving-endpoints-for-production-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - load-testing-for-model-serving-endpoints
    - LTFMSE
    - Load Testing|load testing
    - Load test for Model Serving
  citations:
    - file: optimize-model-serving-endpoints-for-production-databricks-on-aws.md
title: Load Testing for Model Serving Endpoints
description: Testing methodology that measures endpoint performance under realistic traffic conditions to determine optimal provisioned concurrency, identify bottlenecks, and validate latency and throughput requirements.
tags:
  - model-serving
  - testing
  - performance
timestamp: "2026-06-19T19:51:38.618Z"
---

# Load Testing for Model Serving Endpoints

**Load testing** is a performance evaluation practice that measures how a [Model Serving](/concepts/model-serving.md) endpoint behaves under realistic traffic conditions. It is a key step in preparing serving endpoints for production workloads, particularly those requiring high throughput, low latency, and reliable performance. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## Objectives

Load testing helps end users:

- **Determine optimal provisioned concurrency settings** – By observing how the endpoint handles increasing load, you can set minimum and maximum concurrency values that balance cost and performance. For example, the required concurrency can be calculated as `Target QPS × Average Latency (seconds)`, and load testing validates that formula against real-world behavior. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]
- **Identify performance bottlenecks** – Load tests reveal where queuing, high latency, or resource exhaustion occurs. Common issues include insufficient provisioned concurrency, external API bottlenecks, or model complexity. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]
- **Validate latency and throughput requirements** – For applications with strict latency budgets (e.g., sub‑100 ms response times) or high query volumes (e.g., more than 50 k QPS), load testing confirms whether the endpoint can meet its service‑level objectives. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]
- **Understand the relationship between client concurrency and server concurrency** – The test results expose how many simultaneous client connections correspond to a given server‑side concurrency level, enabling better autoscaling and capacity planning. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## Relation to Other Optimization Strategies

Load testing is part of the **measure and improve performance** workflow. The results inform decisions about:

- **[Provisioned Concurrency](/concepts/provisioned-concurrency.md)** – The measured latency and throughput are used to set appropriate minimum and maximum concurrency thresholds.
- **[Route Optimization for Model Serving Endpoints|Route optimization](/concepts/route-optimization-for-serving-endpoints.md)** – For endpoints requiring more than 200 QPS, enabling route optimization can further reduce latency and improve the results observed in load tests.
- **[Client optimization](/concepts/client-side-serving-optimization.md)** – Insights from load testing may lead to adjustments in connection pooling, payload sizes, or retry strategies.

## When to Perform Load Testing

Consider load testing when you are:

- Preparing to move from development to production workloads.
- Experiencing scaling bottlenecks (e.g., HTTP 429 errors during traffic spikes).
- Setting provisioned concurrency for the first time or after a model update.
- Evaluating whether CPU instances are sufficient or if GPU instances are needed. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## Related Concepts

- Model Serving Endpoint Optimization
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md)
- Route Optimization
- [Performance Monitoring](/concepts/performance-monitoring-with-mlflow-traces.md)
- [Model Serving Troubleshooting](/concepts/model-serving-build-logs-troubleshooting.md)

## Sources

- optimize-model-serving-endpoints-for-production-databricks-on-aws.md

# Citations

1. [optimize-model-serving-endpoints-for-production-databricks-on-aws.md](/references/optimize-model-serving-endpoints-for-production-databricks-on-aws-6a182106.md)
