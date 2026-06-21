---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8206e8d9e53c4c85df365991ba1d3d5111fdef43f5b3115cf86bb4edfc028734
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-per-output-token-tpot
    - TPOT(
    - Time per Output Token
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Time per Output Token (TPOT)
description: A performance metric measuring the time to generate each subsequent output token per user, directly influencing perceived model speed.
tags:
  - llm-inference
  - performance-metrics
  - latency
timestamp: "2026-06-19T17:50:18.417Z"
---

```markdown
---
title: Time Per Output Token (TPOT)
summary: A performance metric measuring the time required to generate each output token per user, corresponding to the perceived speed of the model.
sources:
  - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:06:46.157Z"
updatedAt: "2026-06-19T14:22:47.377Z"
tags:
  - llm-inference
  - performance-metrics
  - latency
aliases:
  - time-per-output-token-tpot
  - TPOT
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# Time Per Output Token (TPOT)

**Time Per Output Token (TPOT)** is a latency metric that measures the time required to generate each subsequent output token for each user querying an LLM serving system. It represents how end users perceive the "speed" of the model during the response generation phase.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Definition and Interpretation

TPOT captures the per-token generation time during the decoding phase of LLM inference, where text is generated one token at a time in an auto-regressive manner. Each generated token is appended to the input and fed back into the model to generate the next token until a stop condition is met.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

For example, a TPOT of 100 milliseconds per token translates to 10 tokens per second, or approximately 450 words per minute — faster than a typical person can read.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

TPOT is one of two primary sub-metrics used to characterize LLM inference performance. The other is [[Time to First Token (TTFT)]], which measures how quickly users see the first character of the response after submitting their query.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Role in Latency and Throughput

Total end-to-end latency for a single request is calculated as:

> **Latency = TTFT + (TPOT × number of tokens to be generated)**^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Throughput — the number of output tokens per second across all concurrent requests — is inversely related to TPOT at a given concurrency level.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Trade-off with Concurrency

On LLM serving endpoints, concurrent requests can be processed in parallel. At low concurrency, latency (including TPOT) is at its lowest possible value. As concurrency increases, TPOT and overall latency may rise, but throughput typically also increases because multiple requests' tokens per second can be processed in less than double the time.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The optimal balance depends on the use case:

- **Low-latency applications** (e.g., real-time chat) benefit from low concurrency to keep TPOT small.
- **High-throughput workloads** (e.g., batch inference) can tolerate higher TPOT in exchange for higher overall token throughput.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Relationship to LLM Inference Phases

LLM inference occurs in two phases:

1. **Prefill**: Input prompt tokens are processed in parallel. The number of input tokens has a substantial impact on required memory.
2. **Decoding**: Text is generated one token at a time. The number of output tokens dominates overall response latency.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

TPOT specifically measures performance during the decoding phase, while TTFT is driven by the time required to process the prompt and generate the first output token.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Measuring TPOT

A recommended benchmarking notebook measures TPOT along with other metrics. The notebook sends requests at varying concurrency levels and plots the throughput-latency curve. TPOT is derived from the response timing recorded during these load tests.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The benchmarking harness displays total latency across all requests and throughput metrics, showing how latency and throughput increase as more concurrent users query the endpoint. As the number of parallel requests increases, throughput eventually plateaus when the provisioned throughput limit is reached, while total latency continues to increase as additional requests wait in the queue.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [[Time to First Token (TTFT)]] – Companion metric for perceiving response start
- [[LLM inference latency]] – Overall end-to-end response time
- Throughput (LLM) – Tokens per second across all users
- [[Provisioned throughput]] – Capacity planning for model serving
- Benchmarking LLM endpoints – Methodology for measuring TPOT and related metrics
- [[LLM Inference Prefill and Decoding|Prefill and Decoding]] – The two phases of LLM inference

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
```

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
