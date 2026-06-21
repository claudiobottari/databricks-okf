---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 69eea3a5792152c594e99c2e341cd3000549901a37c53c1a2ba39dc778c3fb74
  pageDirectory: concepts
  sources:
    - load-testing-for-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - relationship-between-rps-latency-and-concurrency
    - Concurrency and Relationship Between RPS, Latency,
    - RBRLAC
  citations:
    - file: load-testing-for-serving-endpoints-databricks-on-aws.md
title: Relationship Between RPS, Latency, and Concurrency
description: Throughput (requests per second) is inversely related to latency and directly related to concurrency; there is an optimal ratio of client-side to server-side concurrency that maximizes RPS while meeting latency targets.
tags:
  - performance
  - throughput
  - latency
  - concurrency
timestamp: "2026-06-19T19:16:19.047Z"
---

# Relationship Between RPS, Latency, and Concurrency

**RPS** (Requests Per Second), **latency**, and **concurrency** are three fundamental performance metrics in serving systems. Their relationship is interdependent and directly impacts system performance, throughput, and user experience.

## Overview

The relationship between RPS, latency, and concurrency is governed by a simple but important principle: throughput (RPS) is inversely related to latency and directly related to concurrency. Higher latency reduces throughput, while higher concurrency increases throughput—but only up to an optimal point. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Core Relationship

The fundamental relationship can be summarized as:

- **The more concurrency, the higher the throughput** — Increasing the number of simultaneous requests being processed allows more work to be completed in the same time period. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]
- **The higher the latency, the lower the throughput** — Longer processing time per request reduces the number of requests that can be completed per second. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Optimal Ratio

A central goal of load testing is to determine the optimal ratio of client-side concurrency to server-side concurrency for any given application. This optimal ratio:

- Maximizes RPS
- Meets your latency requirements
- Avoids queuing

This ratio can be used to accurately size your [serving endpoint](/concepts/serving-endpoint-acls.md) to meet the most demanding loads. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## How It Works

End-to-end latency consists of:

1. **Model execution time** — The time the model takes to process an inference
2. **Network overhead** — The time for data to travel between client and server

These two components determine the base latency for a single request. As concurrency increases, the system can handle more requests simultaneously, but there is a limit to this parallelization. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Queue Dynamics

When an endpoint is unable to process requests fast enough, a queue begins to form. This queue typically results in much longer end-to-end latency, as each request must wait before being processed. If requests continue to arrive faster than they can be processed, the queue grows, further increasing latency. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Practical Example

Consider a caf\u00e9 analogy: a barista (server) can work on multiple orders (requests) simultaneously. If the barista works on four hamburgers at once rather than one at a time, they can handle more orders per second. However, there is a limit\u2014if the barista needs to add cheese to 1000 burgers, the parallelization adds too much latency.

The same applies to serving endpoints: there is an optimal point where increasing concurrency improves throughput without degrading latency beyond acceptable limits. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Scenarios

### Scenario 1: Simple Setup

With one client and one provisioned concurrency:
- Total latency: 50 ms (40 ms model execution + 10 ms overhead)
- RPS: 20 (one request every 50 ms)

### Scenario 2: Increased Provisioned Concurrency

Doubling provisioned concurrency without adding clients does not increase RPS:
- Latency remains 50 ms
- RPS remains 20
- The additional capacity is unused

### Scenario 3: Adding Clients

Matching client count to provisioned concurrency:
- Two clients, two provisioned concurrency
- Each request processed independently
- Latency: 50 ms
- RPS: 40 (20 QPS per client)

### Scenario 4: Reduced Provisioned Concurrency

When client count exceeds provisioned concurrency:
- Two clients, one provisioned concurrency
- Second request must queue
- Latency: 90 ms (10 ms overhead + 40 ms queuing + 40 ms execution)
- This is significantly worse than the 50 ms baseline

This scenario demonstrates how queuing adversely affects both latency and RPS. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- Load testing — The process of measuring system performance under different traffic levels
- Serving endpoint — The infrastructure that processes model inferences
- [Provisioned Concurrency](/concepts/provisioned-concurrency.md) — The number of simultaneous requests an endpoint can handle
- Queue — The line of waiting requests that forms when demand exceeds capacity
- Throughput — The rate of successful request completion
- Latency requirements — Business-defined performance criteria for acceptable response times

## Sources

- load-testing-for-serving-endpoints-databricks-on-aws.md

# Citations

1. [load-testing-for-serving-endpoints-databricks-on-aws.md](/references/load-testing-for-serving-endpoints-databricks-on-aws-784933e2.md)
