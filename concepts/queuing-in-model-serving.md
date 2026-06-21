---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 54648705ded7d9e419cdd77b331e97dc15509ab04ec478c826b408ea9ceee294
  pageDirectory: concepts
  sources:
    - load-testing-for-serving-endpoints-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - queuing-in-model-serving
    - QIMS
  citations:
    - file: load-testing-for-serving-endpoints-databricks-on-aws.md
title: Queuing in Model Serving
description: When incoming requests exceed provisioned concurrency, requests queue up, causing increased end-to-end latency due to additional wait time before processing begins.
tags:
  - queuing
  - latency
  - bottlenecks
timestamp: "2026-06-19T19:15:35.576Z"
---

# Queuing in Model Serving

**Queuing in Model Serving** occurs when a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) receives more simultaneous requests than it has provisioned concurrency to process. Instead of dropping excess requests, the system places them in a queue and processes them sequentially as capacity becomes available. This queuing behavior is enabled by default in Databricks Model Serving. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Mechanics of Queuing

When a queue forms, each waiting request accumulates additional latency equal to its time spent waiting before being processed. This added latency is compounded by the time required for model execution. If requests continue to arrive faster than the endpoint can process them, the queue grows continuously, which further increases latency for all subsequent requests. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Impact on System Performance

Queuing has a direct and measurable impact on both throughput and end-to-end latency. In a simple example with two clients sending requests to an endpoint that has only one provisioned concurrency unit, the second client sees a latency of 90 ms: 10 ms (network overhead) + 40 ms (queuing wait time) + 40 ms (model execution time). This is significantly worse than the 50 ms latency seen when no queue is present. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

The relationship between concurrency, latency, and throughput is as follows:

- **The more concurrency, the higher the throughput.** Additional provisioned capacity allows more requests to be processed in parallel, reducing queue formation.
- **The higher the latency, the lower the throughput.** When requests spend extra time waiting in a queue, the effective throughput decreases because the system's processing rate is constrained by the backlog of waiting work.

Generally, there is an optimal ratio of client-side concurrency to server-side concurrency for any given application. One of the central goals of load testing is to determine that optimal ratio, which maximizes requests per second, meets latency requirements, and avoids queuing. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Why Queuing Matters in Production

If an endpoint is unable to process requests fast enough, a line begins to form — this is a queue. The forming of a queue typically results in much longer end-to-end latency because each request spends additional time waiting before being processed. For this reason, it is important to understand what sort of peak demand an endpoint may experience and ensure it is sized correctly with a load test. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Queuing vs. Request Dropping

Queuing is distinct from request dropping. In a queuing system, all requests are eventually processed (subject to system capacity and timeouts). In a request-dropping system, the endpoint would return an error immediately when capacity is exceeded. Queuing is the default behavior in Databricks Model Serving, which means that under high load, the system will accept all requests and process them as capacity becomes available — but at the cost of increased latency for the requests that must wait. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Provisioned Concurrency](/concepts/provisioned-concurrency.md) — The amount of parallel processing capacity allocated to an endpoint
- [Load Testing](/concepts/locust-load-testing-framework.md) — The process of measuring endpoint performance under different traffic levels to determine the optimal concurrency ratio
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) — The Databricks infrastructure that serves model inferences
- Latency — End-to-end time for a request, including queuing wait time
- Throughput — Number of requests processed per unit time, inversely related to latency
- Production Optimization — Strategies for tuning model serving performance

## Sources

- load-testing-for-serving-endpoints-databricks-on-aws.md

# Citations

1. [load-testing-for-serving-endpoints-databricks-on-aws.md](/references/load-testing-for-serving-endpoints-databricks-on-aws-784933e2.md)
