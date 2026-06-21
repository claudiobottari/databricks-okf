---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 13f1544d7e20f9e2d0c15243d109a2428f774e41a04399c85bb0461ae45c8bfc
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-throughput-vs-latency-trade-off
    - LTVLT
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: LLM Throughput vs Latency Trade-off
description: The fundamental tension in LLM serving where increasing concurrent requests boosts throughput but also raises latency, requiring careful load control based on use case.
tags:
  - llm-inference
  - performance
  - system-design
timestamp: "2026-06-19T14:22:46.639Z"
---

# LLM Throughput vs Latency Trade-off

**LLM Throughput vs Latency Trade-off** refers to the fundamental performance balancing act in LLM serving where increasing the number of concurrent requests processed by an endpoint improves overall throughput but at the cost of higher per-request latency. Understanding and controlling this trade-off is essential for optimizing LLM inference performance across different use cases.

## Overview

LLM inference on Databricks measures performance in tokens per second for provisioned throughput mode. The trade-off between latency and throughput arises because LLM serving endpoints can process multiple concurrent requests simultaneously. At low concurrent request loads, latency is at its lowest possible level. However, increasing the request load may increase latency while also increasing throughput, because two requests' worth of tokens per second can be processed in less than double the time. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Controlling the number of parallel requests into the system is the core mechanism for balancing latency with throughput. For low latency use cases, send fewer concurrent requests to the endpoint. For high throughput use cases, saturate the endpoint with more concurrency requests, accepting higher latency in exchange for greater throughput. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## LLM Inference Process

LLMs perform inference in a two-step process:

1. **Prefill**: The tokens in the input prompt are processed in parallel.
2. **Decoding**: Text is generated one token at a time in an auto-regressive manner. Each generated token is appended to the input and fed back into the model to generate the next token. Generation stops when the LLM outputs a special stop token or when a user-defined condition is met.

The number of input tokens substantially impacts the required memory to process requests, while the number of output tokens dominates overall response latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Key Performance Metrics

Databricks divides LLM inference into the following sub-metrics:

- **Time to first token (TTFT)**: How quickly users start seeing the model's output after entering their query. Low waiting times are essential for real-time interactions but less important for offline workloads. This metric is driven by the time required to process the prompt and generate the first output token.
- **Time per output token (TPOT)**: The time to generate an output token for each user querying the system. This metric corresponds with how each user perceives the "speed" of the model. For example, a TPOT of 100 milliseconds per token would be 10 tokens per second, or approximately 450 words per minute, which is faster than a typical person can read.

Based on these metrics:
- **Latency** = TTFT + (TPOT) × (number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests

^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Trade-off Behavior

When increasing the number of parallel requests, both latency and throughput increase. However, as the number of parallel requests continues to increase, throughput begins to plateau, reaching a limit determined by the provisioned throughput for the endpoint. This plateau occurs because the provisioned throughput limits the number of workers and parallel requests that can be handled simultaneously. Beyond that limit, total latency continues to increase as additional requests wait in a queue. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Use Case Guidance

| Use Case Type | Goal | Strategy |
|---------------|------|----------|
| High throughput | Maximize tokens per second | Send many concurrent requests, even at the expense of latency |
| Low latency | Minimize response time | Send fewer concurrent requests to keep latency low |

High throughput use cases might include [batch inference](/concepts/batch-inference-on-databricks.md) and other non-user-facing tasks. Low latency use cases might include real-time applications that require immediate responses. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Best Practices

Databricks recommends maximizing throughput given the latency budget for your production application. The endpoint autoscaling strategy balances between latency and throughput. For benchmarking, use the Databricks benchmarking harness notebook to display total latency across all requests and throughput metrics, and plot the throughput-versus-latency curve across different numbers of parallel requests. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [Provisioned Throughput for Foundation Model APIs](/concepts/provisioned-throughput-foundation-model-apis.md)
- [Model Units in Provisioned Throughput](/concepts/provisioned-throughput.md)
- [LLM Inference Performance Engineering](/concepts/llm-inference-prefill-and-decoding.md)
- [Foundation Model APIs on Databricks](/concepts/foundation-models-apis-on-databricks.md)
- Batch Inference
- Real-Time Inference

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
