---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 315bfb0d4daa6d3dd80838e4f98b074fde9999c03664d36b9fedda6e72805df4
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-to-first-token-ttft
    - TTFT(
    - Time to First Token
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Time to First Token (TTFT)
description: A latency metric measuring how quickly users see the first output token after submitting a query, driven by prompt processing and first token generation time.
tags:
  - llm-inference
  - performance-metrics
  - latency
timestamp: "2026-06-19T17:49:57.276Z"
---

# Time to First Token (TTFT)

**Time to First Token (TTFT)** is a performance metric that measures how quickly users begin seeing a model's output after submitting their query. It captures the time required to process the input prompt and generate the very first output token. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Definition

LLM inference is a two-step process:

1. **Prefill** – the input prompt tokens are processed in parallel.
2. **Decoding** – text is generated one token at a time in an auto-regressive manner, with each generated token appended to the input and fed back to produce the next token.

TTFT represents the time spent on prefilling the prompt **plus** generating the first output token. It is one of two sub-metrics used to break down inference performance; the other is [Time per Output Token (TPOT)](/concepts/time-per-output-token-tpot.md). ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Importance

Low TTFT is essential for **real-time interactions** where users expect an immediate response. In offline workloads (such as batch inference), the user is not actively waiting, so TTFT is less critical. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Low TTFT use cases:** Real-time applications that require immediate responses.
- **High TTFT-tolerant use cases:** Batch inferences and other non-user-facing tasks.

## Relationship to Other Metrics

TTFT contributes to the overall latency of a request. Together with TPOT and the number of output tokens to be generated, total latency is defined as: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

**Latency = TTFT + (TPOT × number of tokens to be generated)**

Throughput is defined separately as the number of output tokens per second **across all concurrent requests**. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Trade-off with Throughput

There is an inherent trade-off between TTFT (latency) and [throughput](/concepts/provisioned-throughput.md). At low concurrent request loads, TTFT is at its lowest possible value. As the number of concurrent requests increases, latency tends to rise, but throughput typically also improves because multiple requests can be processed in parallel—two requests' worth of tokens per second can be handled in less than double the time. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Controlling the number of parallel requests sent to an endpoint is therefore core to balancing latency against throughput: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Low latency use cases:** Send fewer concurrent requests to keep TTFT low.
- **High throughput use cases:** Saturate the endpoint with many concurrent requests, accepting higher TTFT in exchange for greater throughput.

## Benchmarking

Benchmarking notebooks typically report TTFT as one of the sub-metrics, alongside TPOT and total latency. The benchmark displays the total latency across all requests and plots the throughput-vs-latency curve for varying numbers of parallel requests. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

As the number of parallel requests increases, throughput eventually plateaus. This plateau corresponds to the endpoint's capacity limit. Beyond that limit, additional requests queue and total latency continues to rise. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Factors Affecting TTFT

The number of input tokens has a substantial impact on the required memory to process requests, which can affect TTFT. The number of output tokens, however, dominates overall response latency rather than TTFT specifically. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [Time per Output Token (TPOT)](/concepts/time-per-output-token-tpot.md) – Companion sub-metric measuring generation speed per token.
- Latency – End-to-end response time for a single request: TTFT + (TPOT × tokens).
- Throughput – Total output tokens per second across all concurrent requests.
- LLM inference – The two-step (prefill + decoding) process that TTFT measures.
- [Provisioned Throughput](/concepts/provisioned-throughput.md) – The capacity model that governs the trade-off between TTFT and throughput.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Managed serving layer for LLMs.

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
