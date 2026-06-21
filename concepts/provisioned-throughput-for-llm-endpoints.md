---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea7d56f33d29a25bcf55369371d425d73df6b6c27a509c68c4a463fa71be58c0
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-for-llm-endpoints
    - PTFLE
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Provisioned Throughput for LLM Endpoints
description: A capacity planning model where inference capacity is provisioned based on tokens per second, with endpoint scaling limited by provisioned throughput leading to a throughput plateau.
tags:
  - llm-serving
  - capacity-planning
  - scaling
timestamp: "2026-06-19T09:21:53.765Z"
---

# Provisioned Throughput for LLM Endpoints

**Provisioned Throughput for LLM Endpoints** refers to a deployment mode for [Foundation Model APIs](/concepts/foundation-model-apis.md) on Databricks where inference capacity is reserved and measured in tokens per second, providing predictable performance for production workloads. This mode is distinct from pay-per-token serverless inference and is designed for applications that require consistent latency and throughput.

## Overview

Provisioned throughput allocates dedicated inference capacity to an endpoint, measured in tokens per second. This ensures that the endpoint can handle a specified volume of requests without being affected by other users' workloads. Databricks recommends this mode for production applications that have defined latency budgets and require reliable performance. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Supported Models

Provisioned throughput based on tokens per second is available for the following models:

- Meta Llama 3.3
- Meta Llama 3.2 3B
- Meta Llama 3.2 1B
- Meta Llama 3.1
- GTE v1.5 (English)
- BGE v1.5 (English)
- DeepSeek R1 (not available in Unity Catalog)

Some models use Model units in provisioned throughput instead of tokens per second to provision inference capacity. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## LLM Inference Process

LLMs perform inference in two distinct phases that affect latency and throughput metrics:

- **Prefill**: The input prompt tokens are processed in parallel. The number of input tokens has a substantial impact on the required memory to process requests.
- **Decoding**: Text is generated one token at a time in an auto-regressive manner. Each generated token is appended to the input and fed back into the model to generate the next token. Generation stops when the LLM outputs a special stop token or when a user-defined condition is met. The number of output tokens dominates overall response latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Performance Metrics

Databricks divides LLM inference performance into the following sub-metrics:

- **Time to First Token (TTFT)**: How quickly users start seeing the model's output after entering their query. Low waiting times are essential for real-time interactions but less important for offline workloads. This metric is driven by the time required to process the prompt and generate the first output token.
- **Time Per Output Token (TPOT)**: The time to generate an output token for each user querying the system. This metric corresponds with how each user perceives the "speed" of the model. For example, a TPOT of 100 milliseconds per token equals 10 tokens per second, or approximately 450 words per minute. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Based on these sub-metrics, total latency and throughput are defined as:

- **Latency** = TTFT + (TPOT × number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Latency-Throughput Trade-off

LLM serving endpoints on Databricks can scale to match the load sent by clients with multiple concurrent requests. There is an inherent trade-off between latency and throughput:

- At low concurrent request loads, latency is the lowest possible.
- As request load increases, latency may increase, but throughput also increases because concurrent requests can be processed simultaneously. Two requests worth of tokens per second can be processed in less than double the time.

Controlling the number of parallel requests is core to balancing latency with throughput. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Use Case Guidance

- **High throughput use cases**: Batch inferences and other non-user-facing tasks. Send more concurrent requests to saturate the endpoint, accepting higher latency in exchange for greater throughput.
- **Low latency use cases**: Real-time applications that require immediate responses. Send fewer concurrent requests to keep latency low. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Benchmarking

Databricks provides a benchmarking harness notebook that can be imported into a Databricks environment to run load tests against an LLM endpoint. The notebook:

- Displays total latency across all requests and throughput metrics
- Plots the throughput versus latency curve across different numbers of parallel requests
- Demonstrates how latency and throughput increase as more concurrent users query the endpoint

As the number of parallel requests increases, throughput begins to plateau, reaching a limit determined by the provisioned throughput for the endpoint. This plateau occurs because the provisioned throughput limits the number of workers and parallel requests that can be made. Beyond this limit, total latency continues to increase as additional requests wait in the queue. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The API layer for serving LLMs on Databricks
- Model units in provisioned throughput — Alternative provisioning model for certain models
- [LLM Inference Performance Engineering](/concepts/llm-inference-prefill-and-decoding.md) — Best practices for optimizing inference performance
- Endpoint Autoscaling — How Databricks balances latency and throughput automatically
- [Time to First Token (TTFT)](/concepts/time-to-first-token-ttft.md) — Key latency metric for real-time applications
- Throughput Optimization — Strategies for maximizing tokens per second

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
