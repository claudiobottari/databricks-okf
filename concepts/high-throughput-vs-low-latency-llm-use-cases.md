---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b3ef2862e109bf4ddabbbaaad33113d86e9b97bbd40e84818cea6645a5f44755
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - high-throughput-vs-low-latency-llm-use-cases
    - HTVLLLUC
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: High Throughput vs Low Latency LLM Use Cases
description: "Classification of LLM application scenarios: high throughput for batch/non-user-facing tasks where latency can be sacrificed, and low latency for real-time interactive applications."
tags:
  - llm-serving
  - use-cases
  - architecture
timestamp: "2026-06-18T14:42:43.427Z"
---

# High Throughput vs Low Latency LLM Use Cases

**High Throughput vs Low Latency LLM Use Cases** refers to the fundamental trade-off between optimizing large language model (LLM) inference endpoints for maximal output volume versus minimal response time, and how the choice between these priorities depends on the application's user-facing requirements.

## Overview

LLM inference involves a two-step process: **prefill** (processing input tokens in parallel) and **decoding** (generating output tokens one at a time auto-regressively). Production applications typically operate under a latency budget, and the recommended approach is to **maximize throughput given that latency budget**. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The number of input tokens substantially impacts the required memory to process requests, while the number of output tokens dominates overall response latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Key Performance Metrics

Databricks divides LLM inference into the following sub-metrics: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Time to first token (TTFT):** How quickly users start seeing the model's output after entering their query. Low waiting times are essential for real-time interactions but less important for offline workloads. This metric is driven by the time required to process the prompt and generate the first output token.
- **Time per output token (TPOT):** The time to generate an output token for each querying user. This corresponds with how each user perceives the "speed" of the model. For example, a TPOT of 100 milliseconds per token equals 10 tokens per second, or approximately 450 words per minute — faster than a typical person can read.

Based on these metrics, total latency and throughput are defined as: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Latency** = TTFT + (TPOT) × (number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests

## The Latency-Throughput Trade-off

On Databricks, LLM serving endpoints can scale to match the load from multiple concurrent requests. There is an inherent trade-off between latency and throughput because concurrent requests are processed simultaneously. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

At low concurrent request loads, latency is at its lowest possible level. However, increasing the request load causes latency to rise, but throughput also increases — because two requests' worth of tokens per second can be processed in less than double the time. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

As the number of parallel requests continues to increase, throughput eventually plateaus, reaching a limit determined by the endpoint's provisioned capacity. Beyond this saturation point, additional requests wait in a queue, and total latency continues to increase without throughput gains. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Therefore, **controlling the number of parallel requests is core to balancing latency with throughput**: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

| Priority | Request Strategy | Use Case Examples |
|----------|-----------------|-------------------|
| **Low latency** | Send fewer concurrent requests to keep latency minimal | Real-time applications requiring immediate responses |
| **High throughput** | Saturate the endpoint with high concurrency | Batch inferences and other non-user-facing tasks |

## High Throughput Use Cases

High throughput use cases prioritize processing volume over per-request speed. These workloads typically include: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Batch inferences:** Processing large datasets of prompts in bulk, where completion time matters more than individual response speed.
- **Offline processing:** Non-user-facing tasks such as document summarization, data enrichment, or content classification.
- **Background jobs:** Scheduled or event-driven workloads that can tolerate queuing delays.

In these scenarios, practitioners send many concurrent requests to saturate the endpoint, accepting higher latency in exchange for maximizing the total output tokens per second. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Low Latency Use Cases

Low latency use cases prioritize per-request response speed over aggregate throughput. These are typically real-time, user-facing applications where waiting time directly impacts user experience: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Chatbots and conversational AI:** Users expect near-instantaneous responses in interactive dialogues.
- **Real-time assistants:** Applications that provide suggestions, completions, or analysis while the user is typing.
- **Interactive tools:** Any application where a delayed response would break workflow flow or user engagement.

For these use cases, practitioners send fewer concurrent requests to keep TTFT and TPOT minimal, even if the endpoint's overall throughput is underutilized. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Benchmarking

Databricks provides a benchmarking harness (available as an example notebook) that measures total latency across all requests and throughput metrics, plotting the throughput-versus-latency curve across different numbers of parallel requests. This allows practitioners to identify the optimal concurrency level for their specific latency and throughput requirements. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The benchmarking notebook specifically applies to provisioned throughput workloads using tokens-per-second-based models, including Meta Llama 3.1, 3.2, 3.3, DeepSeek R1, GTE v1.5, and BGE v1.5. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- LLM Inference Performance — Detailed metrics and sub-metrics for endpoint evaluation
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Capacity allocation for LLM serving endpoints
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks hosted model serving
- Batch Inference — High throughput processing patterns
- Real-time Serving — Low latency deployment architectures

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
