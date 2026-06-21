---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5ce3bdf5a73e226fe177ad6e629fe5f501edac81b42d7ac8ddee8c66748e6aeb
  pageDirectory: concepts
  sources:
    - optimize-model-serving-endpoints-for-production-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-concurrency-for-serving-endpoints
    - PCFSE
  citations:
    - file: optimize-model-serving-endpoints-for-production-databricks-on-aws.md
title: Provisioned Concurrency for Serving Endpoints
description: Controls how many simultaneous requests a model serving endpoint can process, with autoscaling support. Calculated as Target QPS times Average Latency. Used to handle baseline traffic and spikes while controlling costs.
tags:
  - model-serving
  - scaling
  - infrastructure
  - capacity-planning
timestamp: "2026-06-19T19:51:36.446Z"
---

# Provisioned Concurrency for Serving Endpoints

**Provisioned concurrency** controls how many simultaneous requests your [Model Serving Endpoint](/concepts/model-serving-endpoint.md) can process at once. It is an infrastructure optimization that helps balance throughput, latency, and cost for production workloads. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## Configuration Guidelines

When configuring provisioned concurrency, you set a minimum and maximum concurrency level, and you can optionally enable autoscaling:

- **Minimum concurrency** – Set high enough to handle baseline traffic without causing queuing.
- **Maximum concurrency** – Set high enough to accommodate traffic spikes while still controlling costs.
- **Autoscaling** – When enabled, Databricks dynamically adjusts capacity based on demand, which helps handle variable traffic patterns.

^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## Calculating Required Concurrency

To determine an appropriate concurrency level, use the following formula:

```
Required Concurrency = Target QPS × Average Latency (seconds)
```

**Example**: If your target is 100 queries per second (QPS) and the average latency is 200 milliseconds, the required concurrency is:

```
Required Concurrency = 100 × 0.2 = 20
```

Always perform [Load Testing|load testing](/concepts/load-testing-for-model-serving-endpoints.md) to measure actual latency under realistic traffic and to refine concurrency settings. ^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## Role in Autoscaling and Queuing

Provisioned concurrency works closely with the endpoint’s autoscaling mechanism. When traffic suddenly spikes, autoscaling needs time to detect the increase and provision additional capacity. During that window, incoming requests may exceed the current capacity and start to queue. If queuing exceeds a defined threshold, the endpoint returns HTTP 429 (Too Many Requests) errors.

To minimize queuing:

- Set the minimum provisioned concurrency high enough to cover baseline traffic plus typical bursts.
- Consider enabling Route Optimization for higher capacity limits.
- Implement retry logic with exponential backoff in client applications.

^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## When to Optimize Provisioned Concurrency

You should evaluate provisioned concurrency settings when:

- Your application sends more than 50k QPS to a single endpoint.
- You have strict latency requirements (sub-100ms response times).
- Endpoints experience queuing or HTTP 429 errors during traffic spikes.
- You are moving from development to production workloads.

^[optimize-model-serving-endpoints-for-production-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- Route Optimization
- [Load Testing](/concepts/locust-load-testing-framework.md)
- Autoscaling
- Queuing
- HTTP 429 Too Many Requests
- Optimize Model Serving Endpoints for Production

## Sources

- optimize-model-serving-endpoints-for-production-databricks-on-aws.md

# Citations

1. [optimize-model-serving-endpoints-for-production-databricks-on-aws.md](/references/optimize-model-serving-endpoints-for-production-databricks-on-aws-6a182106.md)
