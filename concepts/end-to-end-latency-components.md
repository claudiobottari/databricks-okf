---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e07661fa879df0d36f6ec0d999d8ec2d5e88a3009f063b3293637b055caa3b6d
  pageDirectory: concepts
  sources:
    - load-testing-for-serving-endpoints-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - end-to-end-latency-components
    - ELC
  citations:
    - file: load-testing-for-serving-endpoints-databricks-on-aws.md
title: End-to-End Latency Components
description: "Total latency for a model inference request consists of two main parts: network overhead (communication time) and model execution time (inference computation), both of which must be accounted for when setting realistic performance requirements."
tags:
  - latency
  - networking
  - model-inference
  - performance
timestamp: "2026-06-19T19:15:55.017Z"
---

# End-to-End Latency Components

**End-to-End Latency** refers to the total time a client experiences when sending a request to a model serving endpoint and receiving a response. It encompasses all processing stages from the moment the client initiates the request until the final result is returned.

## Definition

End-to-end latency is the complete round-trip time that a client experiences when sending data for inference to a model serving endpoint. This includes not only the model execution time but also all networking overhead and any queuing delays that may occur when the system is under load. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Components

End-to-end latency consists of two primary components:

### Model Execution Time

The time required for the model to process the input and generate a prediction. This is the core computational work performed by the serving infrastructure. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

### Network Overhead

The additional time incurred by network communication between the client and server, including data transmission, protocol handling, and any other communication-related delays. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Relationship with Throughput

End-to-end latency and throughput (measured in requests per second or queries per second) are inversely related:

- **Higher concurrency** generally results in **higher throughput**
- **Higher latency** typically results in **lower throughput**

There is an optimal ratio of client-side concurrency to server-side concurrency for any given application. One of the central goals of load testing is to determine this optimal ratio that maximizes requests per second (RPS) while meeting latency requirements and avoiding queuing. ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Queuing Effects

When an endpoint is unable to process requests fast enough, requests begin to queue. This queuing significantly increases end-to-end latency because each request must now wait additional time before being processed. The relationship between queuing and latency is as follows:

- If requests continue to arrive faster than they can be processed, the queue grows
- A growing queue further increases latency for subsequent requests
- This creates a compounding effect where latency continues to increase under sustained overload

## Example: Impact of Provisioned Concurrency

The relationship between client concurrency, server concurrency, and latency is dynamic and interdependent. Consider these scenarios:

### Scenario 1: Simple Setup
- Single client sends requests sequentially
- Total latency per request: 40ms (model execution) + 10ms (network overhead) = 50ms
- Result: 20 requests per second ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

### Scenario 2: Increased Provisioned Concurrency
- Single client with doubled provisioned concurrency
- Total latency remains 50ms (40ms + 10ms)
- System still sees only 20 QPS ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

### Scenario 3: Multiple Clients
- Two clients with two provisioned concurrency
- Each request independently processed simultaneously (assuming perfect load balancing)
- Total latency: 50ms
- System observes 40 requests per second ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

### Scenario 4: Queuing Under Reduced Concurrency
- Two clients but reduced to one provisioned concurrency
- Second request must wait: 10ms (network) + 40ms (queuing) + 40ms (execution) = 90ms
- This is significantly worse than the 50ms seen without queuing ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Importance for Production

Understanding end-to-end latency components is essential for:

- [Load Testing](/concepts/locust-load-testing-framework.md) - Sizing endpoints correctly to handle production workloads
- [Model Serving](/concepts/model-serving.md) - Configuring serving infrastructure for optimal performance
- Production Optimization - Identifying bottlenecks and improving system performance

Before running a load test, you must:
1. Understand the components and concepts related to load testing
2. Define your production requirements
3. Find a representative payload for the load testing framework ^[load-testing-for-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- Throughput - Requests processed per unit time, inversely related to latency
- Concurrency - Number of requests being processed simultaneously
- Queuing Theory - Mathematical study of waiting lines in systems
- Model Inference Time - The computational time for model execution
- Network Latency - Communication delays in distributed systems

## Sources

- load-testing-for-serving-endpoints-databricks-on-aws.md

# Citations

1. [load-testing-for-serving-endpoints-databricks-on-aws.md](/references/load-testing-for-serving-endpoints-databricks-on-aws-784933e2.md)
