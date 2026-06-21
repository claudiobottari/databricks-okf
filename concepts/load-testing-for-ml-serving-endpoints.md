---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 738f399ab132a6465fd59b4c33165bccc098a3bcfd29a74d0afb4f196e194781
  pageDirectory: concepts
  sources:
    - load-testing-for-serving-endpoints-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - load-testing-for-ml-serving-endpoints
    - LTFMSE
    - Load Testing for Serving Endpoints
    - Load testing for serving endpoints
    - What is Load Testing for Serving Endpoints
    - load testing for serving endpoints
  citations:
    - file: load-testing-for-serving-endpoints-databricks-on-aws.md
title: Load Testing for ML Serving Endpoints
description: The practice of simulating real-world traffic on model serving infrastructure to measure performance, identify bottlenecks, and correctly size endpoints for production workloads.
tags:
  - machine-learning
  - load-testing
  - model-serving
  - performance
timestamp: "2026-06-19T19:15:17.586Z"
---

# Load Testing for ML Serving Endpoints

**Load Testing for ML Serving Endpoints** is the process of simulating real-world usage patterns on model serving infrastructure to verify that endpoints meet production requirements for metrics such as latency and requests per second (RPS). It helps practitioners correctly size endpoints, identify bottlenecks, and ensure reliable performance under varying traffic conditions. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## What is a Load Test?

A load test measures an endpoint's performance under different levels of traffic, helping you size the endpoint correctly to avoid delays. The fundamental goal is to determine how much traffic a system can handle before performance degrades beyond acceptable thresholds. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

### Real-World Analogy

Consider a café. Each customer is a **client** sending a request, the barista represents the **server** processing model inferences, the time to prepare a drink is the **model implementation** time, and delays in ordering or paying represent **network overhead**. More customers arriving at once is **client concurrency**, and adding more baristas is like increasing **server concurrency**. Just as a café has a limit to how many customers it can serve before service quality drops, ML serving endpoints have limits that must be understood through load testing. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Key Metrics and Concepts

| Concept | Definition |
|---------|------------|
| RPS (Requests Per Second) | The number of inference requests the endpoint processes per second |
| Latency | The round-trip time a client experiences, including both networking latency and inference time |
| Client concurrency | The number of clients simultaneously sending requests |
| Server concurrency (provisioned concurrency) | The number of requests the endpoint can process in parallel |
| Queue | Requests that arrive faster than the server can process them, increasing end-to-end latency |

^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Relationship Between RPS, Latency, and Concurrency

For ML systems, business criteria generally include high-quality results, low latency, and high throughput. End-to-end latency consists of model execution time plus network overhead. Throughput (RPS) is inversely related to latency and directly related to concurrency: ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

- The more concurrency, the higher the throughput.
- The higher the latency, the lower the throughput.

There is an optimal ratio of client-side concurrency to server-side concurrency for any given application. One central goal of a load test is to determine this optimal ratio, which maximizes RPS while meeting latency requirements and avoiding queuing. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

If the endpoint cannot process requests fast enough, a queue forms, resulting in much longer end-to-end latency as requests wait before being processed. If requests continue arriving faster than they can be processed, the queue grows, further increasing latency. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Prerequisites

Before running a load test on an endpoint, you need to: ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

1. Understand the components and concepts related to load testing.
2. Define your production requirements (latency and throughput targets).
3. Find a representative payload for the [load testing framework](/concepts/locust-load-testing-framework.md) to use when benchmarking the endpoint.

## Latency Requirements

Based on business and customer requirements, define the ideal performance of your system. On a [Model Serving](/concepts/model-serving.md) endpoint, latency includes the full round-trip time a client experiences when sending data for inference, including both networking latency and inference time. Requirements must be realistic — for example, if a model takes 15ms to perform inference when loaded into memory, additional time for networking latency must be accounted for when served on an endpoint. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Load Test Scenarios

The relationship between client concurrency, server concurrency, and latency is dynamic and interdependent. The following scenarios illustrate this relationship: ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

### Scenario 1: Simple Setup

- Number of clients: 1
- Provisioned concurrency: 1
- Overhead latency: 10 ms
- Model execution time: 40 ms

A single client sends requests sequentially, waiting for a response before issuing the next request. Total latency per request is 50 ms (40 ms + 10 ms), resulting in 20 requests per second. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

### Scenario 2: Increase Provisioned Concurrency

- Number of clients: 1
- Provisioned concurrency: **2** (increased from 1)
- Overhead latency: 10 ms
- Model execution time: 40 ms

With a single client making sequential requests, total latency remains 50 ms, and the system still sees only 20 RPS. Increasing provisioned concurrency alone does not improve throughput if client concurrency is not also increased. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

### Scenario 3: Add Another Client

- Number of clients: **2** (increased from 1)
- Provisioned concurrency: 2
- Overhead latency: 10 ms
- Model execution time: 40 ms

Two clients making requests to an endpoint with two provisioned concurrency allows each request to be processed independently and simultaneously. Total latency remains 50 ms, but the system observes 40 RPS (20 RPS per client). Increasing both provisioned concurrency and client concurrency increases total throughput without penalty on latency. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

### Scenario 4: Reduce Provisioned Concurrency

- Number of clients: 2
- Provisioned concurrency: **1** (reduced from 2)
- Overhead latency: 10 ms
- Model execution time: 40 ms

Two clients make requests simultaneously, but the endpoint can only process one request at a time. This introduces queuing. Assuming the server allows queuing (enabled by default in [Databricks Model Serving](/concepts/databricks-model-serving.md)), the second client sees a latency of 90 ms: 10 ms (network overhead) + 40 ms (queuing wait time) + 40 ms (model execution time) — significantly worse than the 50 ms seen without queuing. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — Infrastructure for deploying ML models as API endpoints
- Production optimization for ML serving — Comprehensive guide to optimizing endpoints
- Locust — Load testing framework commonly used for ML serving endpoints
- Endpoint sizing — Determining the correct provisioned concurrency for expected traffic
- Latency optimization — Strategies for reducing end-to-end inference time

## Sources

- load-testing-for-serving-endpoints-databricks-on-aws.md

# Citations

1. [load-testing-for-serving-endpoints-databricks-on-aws.md](/references/load-testing-for-serving-endpoints-databricks-on-aws-784933e2.md)
