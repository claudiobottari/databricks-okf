---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d81434e14059e5ace303de45bd3ca4202baeb97cf6d1ef1809d48d86b99f1242
  pageDirectory: concepts
  sources:
    - load-testing-for-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - client-vs-server-concurrency-ratio
    - CVSCR
  citations:
    - file: load-testing-for-serving-endpoints-databricks-on-aws.md
title: Client vs Server Concurrency Ratio
description: The optimal performance point for an ML serving system is determined by the ratio of client-side concurrency (number of simultaneous requesters) to server-side concurrency (provisioned parallel capacity), which load testing aims to identify.
tags:
  - concurrency
  - capacity-planning
  - performance-optimization
timestamp: "2026-06-19T19:15:51.904Z"
---

# Client vs Server Concurrency Ratio

The **Client vs Server Concurrency Ratio** is a key performance consideration in load testing of [Model Serving](/concepts/model-serving.md) endpoints. It describes the relationship between the number of concurrent clients sending requests and the server's provisioned concurrency capacity, directly impacting throughput and latency under production workloads. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Overview

For any given application, there is an optimal ratio of client-side concurrency to server-side concurrency that maximizes throughput while meeting latency requirements and avoiding queuing. This ratio represents the point at which the system is neither underutilized nor overwhelmed by excess demand. A primary goal of load testing is to determine this optimal ratio for your specific application. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Relationship Between RPS, Latency, and Concurrency

Throughput (requests per second or RPS) is inversely related to latency and directly related to concurrency:

- **More concurrency** generally leads to higher throughput.
- **Higher latency** reduces achievable throughput.

The optimal client-to-server concurrency ratio maximizes RPS while meeting latency requirements and avoiding queuing. This ratio can be used to accurately size your endpoint to handle peak demand. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Impact of Imbalanced Ratios

### More Clients Than Server Concurrency

When the number of concurrent clients exceeds the server's provisioned concurrency, requests begin to queue. This queuing introduces additional waiting time, significantly increasing end-to-end latency. The effect compounds if requests continue to arrive faster than they can be processed — the queue grows, further degrading latency. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

For example, with two clients sending requests simultaneously to a server that can only process one request at a time, the second client experiences additional queuing latency equal to the processing time of the first request. The total end-to-end latency becomes: network overhead + queuing wait time + model execution time (for the queued request). ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

### More Server Concurrency Than Clients

When provisioned concurrency exceeds the number of active clients, the excess server capacity remains unused. This underutilization does not improve performance but increases infrastructure costs without corresponding throughput gains. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## The Cafeteria Analogy

The relationship can be understood through a real-world analogy to a café:

- Each customer represents a **client** sending a request.
- Baristas represent the **server** processing inferences.
- Adding more baristas or more machines is like increasing **server concurrency**.
- More customers arriving simultaneously is **client concurrency**.

As in a café, there is a limit to parallel work. A chef might optimally cook four hamburgers simultaneously (sharing common preparation steps), but attempting to cook 1,000 hamburgers at once introduces excessive overhead that increases latency. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Determining the Optimal Ratio

Load testing helps identify the optimal client-to-server concurrency ratio for your specific application. The ideal ratio:

1. Maximizes requests per second (RPS).
2. Meets your defined latency requirements.
3. Avoids queuing and excessive latency degradation.

Because the optimal ratio depends on factors including [Model Serving](/concepts/model-serving.md) implementation time, network overhead, and the nature of parallel processing in your application, it must be empirically determined through systematic load testing rather than assumed. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Load Testing](/concepts/locust-load-testing-framework.md) — The process of measuring endpoint performance under different traffic levels.
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md) — The server-side capacity allocated to process requests in parallel.
- Queuing Theory — The study of wait times and queue behavior in systems with limited processing capacity.
- Model Serving Endpoint Sizing — Using load test results to correctly size endpoints for production workloads.
- Latency Requirements — Defined performance criteria that the optimal ratio must satisfy.
- Throughput Optimization — Strategies for maximizing requests per second.

## Sources

- load-testing-for-serving-endpoints-databricks-on-aws.md

# Citations

1. [load-testing-for-serving-endpoints-databricks-on-aws.md](/references/load-testing-for-serving-endpoints-databricks-on-aws-784933e2.md)
