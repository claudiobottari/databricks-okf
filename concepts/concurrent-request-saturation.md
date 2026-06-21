---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5174bb75d442dae12d1803a0f48cd2fd3e1f035dba9445d336ff45a42e4c83a4
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - concurrent-request-saturation
    - CRS
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Concurrent Request Saturation
description: The phenomenon where increasing parallel requests beyond an endpoint's provisioned capacity causes throughput to plateau while latency continues to rise due to queueing.
tags:
  - llm-inference
  - scalability
  - performance
timestamp: "2026-06-19T17:50:45.775Z"
---

# Concurrent Request Saturation

**Concurrent Request Saturation** is the point at which an LLM serving endpoint's throughput stops increasing — or begins to plateau — as the number of parallel requests rises. It is a fundamental limit imposed by the provisioned inference capacity of the endpoint. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Overview

LLM serving endpoints on Databricks can scale to match the load sent by clients with multiple concurrent requests. There is a trade-off between latency and throughput: concurrent requests can be processed at the same time, so at low concurrent load, latency is the lowest possible, but throughput is also low. Increasing the request load may increase latency, but throughput typically also increases because "two requests worth of tokens per second can be processed in less than double the time." ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Controlling the number of parallel requests into the system is therefore core to balancing latency with throughput. The key insight is that you can process multiple requests' worth of tokens per second in less than double the time. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## The Saturation Plateau

As the number of concurrent requests increases, throughput eventually plateaus, reaching a limit determined by the provisioned throughput for the endpoint. This plateau occurs because the provisioned throughput for the endpoint limits the number of workers and parallel requests that can be handled simultaneously. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

When more requests are made than what the endpoint can handle simultaneously, additional requests wait in a queue. The total latency continues to increase, but throughput does not — this is the saturation point. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Use Cases and Trade-offs

The optimal level of concurrency depends on the use case:

- **Low latency use cases** (e.g., real-time applications that require immediate responses): Send fewer concurrent requests to keep latency low. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]
- **High throughput use cases** (e.g., batch inferences and other non-user-facing tasks): Saturate the endpoint with lots of concurrency requests, since higher throughput is worth it even at the expense of latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Measuring Saturation

The [Databricks benchmarking harness](/concepts/llm-endpoint-benchmarking-harness.md) displays the total latency across all requests and throughput metrics, and plots a throughput-versus-latency curve across different numbers of parallel requests. As the number of parallel requests increases, you observe the throughput begin to plateau, reaching the limit imposed by the provisioned throughput. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The benchmark notebook measures both:
- **Time to first token (TTFT)**: How quickly users start seeing output after entering their query.
- **Time per output token (TPOT)**: Time to generate an output token for each user.
- **Latency** = TTFT + (TPOT) × (number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrency requests

## Related Concepts

- LLM inference performance engineering – Best practices for balancing latency and throughput.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – The capacity mechanism that limits concurrent request processing.
- Model units in provisioned throughput – Defines how inference capacity is provisioned.
- [Endpoint autoscaling](/concepts/model-serving-endpoint-scaling.md) – Databricks strategy for balancing between latency and throughput.

## Sources

- conduct-your-own-llm-endpoint-b benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
