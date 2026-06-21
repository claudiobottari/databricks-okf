---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b196f6fd259c61e06ae6c000501eb15da2e5d028cf4c03bf72b91e6947f39edf
  pageDirectory: concepts
  sources:
    - load-testing-for-serving-endpoints-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-concurrency
  citations:
    - file: load-testing-for-serving-endpoints-databricks-on-aws.md
    - file: debugging-guide-for-model-serving-databricks-on-aws.md
title: Provisioned Concurrency
description: The amount of parallel processing capacity allocated to a model serving endpoint; increasing provisioned concurrency allows more requests to be processed simultaneously, directly impacting throughput.
tags:
  - model-serving
  - capacity-planning
  - scaling
timestamp: "2026-06-19T19:15:51.663Z"
---

# Provisioned Concurrency

**Provisioned Concurrency** is a server-side capacity setting for Databricks Model Serving endpoints that determines the number of simultaneous inference requests the endpoint can process in parallel. It serves as a core lever for controlling throughput and latency under varying traffic loads. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## How Provisioned Concurrency Works

When a model serving endpoint receives requests, each request occupies a unit of provisioned concurrency for the duration of its processing. An endpoint can handle as many concurrent requests as its provisioned concurrency setting allows. If the number of incoming requests exceeds that capacity, excess requests are queued and processed in order, increasing end-to-end latency. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

The relationship between client concurrency (the number of clients sending requests), provisioned concurrency, and latency is dynamic. For any given application, there is an optimal ratio of client concurrency to provisioned concurrency that maximizes throughput (requests per second, RPS) while meeting latency targets and avoiding queuing. A key goal of load testing is to identify this optimal ratio. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Relationship with Latency and Throughput

Throughput (RPS) is inversely related to latency and directly related to concurrency:

- Higher provisioned concurrency enables higher throughput.
- Higher latency reduces throughput.
- Queuing occurs when the request arrival rate exceeds the processing capacity, further degrading latency.

^[load-testing-for-serving-endpoints-databricks-on-aws.md]

### Example Scenarios

The following simplified scenarios illustrate how provisioned concurrency, client concurrency, and latency interact. Assume a model execution time of 40 ms and network overhead of 10 ms. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

| Scenario | Clients | Provisioned Concurrency | Latency per request | Throughput (RPS) |
|----------|---------|------------------------|---------------------|------------------|
| Single client, one concurrency slot | 1 | 1 | 50 ms | 20 |
| Single client, two concurrency slots | 1 | 2 | 50 ms | 20 |
| Two clients, two concurrency slots | 2 | 2 | 50 ms | 40 |
| Two clients, one concurrency slot (queuing) | 2 | 1 | 90 ms | 22 |

In the first scenario, a single client sends requests sequentially to an endpoint with one provisioned concurrency slot. Total latency per request is 50 ms (40 ms model execution + 10 ms overhead), yielding 20 RPS. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

In the second scenario, provisioned concurrency is doubled to 2, but with a single client making sequential requests, the endpoint's extra capacity goes unused. Latency remains 50 ms and throughput stays at 20 RPS. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

In the third scenario, two clients send requests to an endpoint with two provisioned concurrency slots. Both requests can be processed simultaneously, so latency remains 50 ms per request, but throughput doubles to 40 RPS. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

In the last scenario, two clients compete for a single provisioned concurrency slot. The second client's request must wait for the first to finish, adding 40 ms of queue wait time. Latency increases to 90 ms, and throughput drops to approximately 22 RPS because the endpoint can only process one request at a time. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Workspace-Level Quota

Provisioned concurrency is subject to a workspace-level quota. The sum of provisioned concurrency across all endpoints in a workspace cannot exceed this limit. If the limit is reached, new endpoints cannot be created and existing endpoints cannot be scaled up until capacity is freed. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

### Quota Exceeded Error

A `Workspace exceeded provisioned concurrency quota` error indicates that the total provisioned concurrency across all endpoints has reached the workspace limit. To free up quota, delete or stop unused endpoints. The workspace limit can be increased by contacting your Databricks account team, subject to regional availability. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Errors Related to Provisioned Concurrency

### Too Many Concurrent Requests

A 429 error with the message `Too many concurrent requests. Consider increasing the provisioned concurrency of the served entity` indicates that the endpoint's current provisioned concurrency cannot handle the incoming traffic volume. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

If autoscaling is enabled, the system automatically provisions additional concurrency up to the endpoint's configured maximum to handle the load. If autoscaling is not enabled, you should manually increase provisioned concurrency or enable autoscaling to accommodate traffic spikes. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Best Practices

- **Perform load testing** to determine the optimal provisioned concurrency for your workload. This helps you size endpoints correctly to meet peak demand without excessive queuing. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]
- **Enable autoscaling** so the endpoint automatically adjusts provisioned concurrency in response to traffic spikes, up to a configured maximum. ^[debugging-guide-for-model-serving-databricks-on-aws.md]
- **Monitor endpoint performance** using logs, inference tables, and metrics to detect when provisioned concurrency is becoming a bottleneck.
- **Consider route-optimized endpoints** for workloads that need to avoid per-endpoint parallel request limits. These endpoints have no per-endpoint parallel request cap and can simplify capacity planning. ^[debugging-guide-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The Databricks service that uses provisioned concurrency
- Autoscaling — Automatic adjustment of provisioned concurrency
- [Load Testing](/concepts/locust-load-testing-framework.md) — Methodology for determining optimal concurrency settings
- Latency — End-to-end request time, affected by queuing
- Throughput — Requests per second, driven by concurrency and latency
- Queuing — Request backlog when capacity is exceeded

## Sources

- load-testing-for-serving-endpoints-databricks-on-aws.md
- debugging-guide-for-model-serving-databricks-on-aws.md

# Citations

1. [load-testing-for-serving-endpoints-databricks-on-aws.md](/references/load-testing-for-serving-endpoints-databricks-on-aws-784933e2.md)
2. [debugging-guide-for-model-serving-databricks-on-aws.md](/references/debugging-guide-for-model-serving-databricks-on-aws-67072c6a.md)
