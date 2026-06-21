---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0454f316fa0b577f122ff0c4885d7a561e68682b81d14bb1dcfe8d426bf36f47
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-inference-prefill-and-decoding
    - Decoding and LLM Inference Prefill
    - LIPAD
    - LLM Inference Performance Engineering
    - Prefill and Decoding
    - llm-inference-phases-prefill-and-decoding
    - "Decoding and LLM Inference Phases: Prefill"
    - LIPPAD
    - llm-inference-two-step-process-prefill-and-decoding
    - "Decoding and LLM Inference Two-Step Process: Prefill"
    - LITPPAD
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: LLM Inference Prefill and Decoding
description: "The two-step process by which LLMs perform inference: prefill processing input tokens in parallel, followed by auto-regressive decoding that generates one token at a time."
tags:
  - llm-inference
  - fundamentals
  - architecture
timestamp: "2026-06-18T14:42:16.608Z"
---

# LLM Inference Prefill and Decoding

**LLM Inference Prefill and Decoding** refers to the two-phase process that large language models (LLMs) use to generate responses when serving user requests. Understanding these phases is essential for performance engineering, capacity planning, and optimizing the trade-off between latency and throughput in production LLM serving systems.

## Overview

LLMs perform inference in two distinct stages. First, the **prefill** phase processes all input prompt tokens in parallel. Then, the **decoding** phase generates output tokens one at a time in an auto-regressive manner, where each newly generated token is appended to the input and fed back into the model to produce the next token. Generation stops when the model outputs a special stop token or when a user-defined condition is met. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Prefill Phase

The prefill phase is where the model processes the entire input prompt simultaneously. Because all input tokens are processed in parallel, the number of input tokens has a substantial impact on the required memory to process requests. This phase is responsible for the **Time to First Token (TTFT)**, which measures how quickly users start seeing the model's output after entering their query. Low TTFT is essential for real-time interactions but less critical for offline batch workloads. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Decoding Phase

During decoding, the model generates text one token at a time in an auto-regressive sequence. Each output token is generated sequentially, and the number of output tokens dominates overall response latency. This phase determines the **Time Per Output Token (TPOT)**, which measures how long it takes to generate each individual token for a given user. A TPOT of 100 milliseconds per token translates to approximately 10 tokens per second, or about 450 words per minute — faster than a typical person can read. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Key Performance Metrics

Based on the prefill and decoding phases, Databricks defines the following inference sub-metrics:

- **Time to First Token (TTFT)**: Driven by the time required to process the prompt and generate the first output token. This metric reflects how quickly users see initial output.
- **Time Per Output Token (TPOT)**: The time to generate each subsequent output token. This metric corresponds to how each user perceives the "speed" of the model.

These metrics feed into the overall performance equations:

- **Latency** = TTFT + (TPOT × number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests

^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Balancing Latency and Throughput

Controlling the number of parallel requests into the system is core to balancing latency with throughput. Because Databricks [LLM serving endpoints](/concepts/model-serving-endpoint.md) can process concurrent requests simultaneously, there is a natural trade-off:

- **Low concurrent request loads** produce the lowest possible latency.
- **Increasing request load** may increase latency but also increases throughput, because two requests' worth of tokens per second can be processed in less than double the time.

This trade-off leads to different recommendations based on use case:

- **High throughput use cases** (e.g., batch inference, non-user-facing tasks) benefit from saturating the endpoint with many concurrent requests, even at the expense of higher latency.
- **Low latency use cases** (e.g., real-time applications requiring immediate responses) should send fewer concurrent requests to keep latency low.

^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Provisioned Throughput and Capacity Limits

In provisioned throughput mode, the endpoint's capacity limits the number of workers and parallel requests that can be handled simultaneously. As the number of parallel requests increases, throughput will eventually plateau — typically reaching a limit determined by the provisioned capacity (e.g., approximately 8,000 tokens per second in some configurations). Beyond this plateau, additional requests wait in a queue, causing total latency to continue increasing while throughput levels off. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [Time to First Token (TTFT)](/concepts/time-to-first-token-ttft.md) – The prefill-phase metric for initial response latency
- [Time per Output Token (TPOT)](/concepts/time-per-output-token-tpot.md) – The decoding-phase metric per-token generation speed
- LLM Serving Endpoints – Databricks-managed endpoints that scale to match load
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – Capacity-based inference allocation for LLM endpoints
- [Model Units](/concepts/model-units.md) – Alternative capacity unit for models that do not use tokens-per-second provisioning

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
