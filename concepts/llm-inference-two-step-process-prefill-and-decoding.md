---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8be3adadb64a8e20867f8afe598a7f7c066f0bbeabacdb7d8b5bfc98f055f8e0
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-inference-two-step-process-prefill-and-decoding
    - "Decoding and LLM Inference Two-Step Process: Prefill"
    - LITPPAD
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: "LLM Inference Two-Step Process: Prefill and Decoding"
description: "LLM inference consists of two sequential phases: parallel prompt processing (prefill) followed by auto-regressive token generation (decoding)."
tags:
  - llm-inference
  - architecture
  - performance
timestamp: "2026-06-19T14:22:44.837Z"
---

```markdown
---
title: "LLM Inference Two-Step Process: Prefill and Decoding"
summary: LLM inference is divided into a parallel prefill phase (processing input prompt tokens) and an autoregressive decoding phase (generating output tokens one at a time).
sources:
  - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:06:31.965Z"
updatedAt: "2026-06-18T11:06:31.965Z"
tags:
  - llm
  - inference
  - architecture
aliases:
  - llm-inference-two-step-process-prefill-and-decoding
  - "Decoding and LLM Inference Two-Step Process: Prefill"
  - LITPPAD
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# LLM Inference Two-Step Process: Prefill and Decoding

LLMs perform inference in a two-step process: **prefill** and **decoding**. In the prefill phase, the input prompt tokens are processed in parallel. In the decoding phase, text is generated one token at a time in an auto-regressive manner; each generated token is appended to the input and fed back into the model to generate the next token. Generation stops when the LLM outputs a special stop token or when a user-defined condition is met. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Impact on Performance

The number of input tokens has a substantial impact on the required memory to process requests. The number of output tokens dominates overall response latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Key Sub-Metrics

Databricks divides LLM inference into the following sub-metrics: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Time to first token (TTFT)**: How quickly users start seeing the model's output after entering their query. Low waiting times are essential in real-time interactions but less important in offline workloads. TTFT is driven by the time required to process the prompt and then generate the first output token.
- **Time per output token (TPOT)**: Time to generate an output token for each user querying the system. This metric corresponds with how each user perceives the “speed” of the model. For example, a TPOT of 100 ms per token yields 10 tokens per second (~450 words per minute), faster than a typical person can read. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md] The specific example of 100 ms and 450 words per minute is stated in the source. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Latency and Throughput

Based on TTFT and TPOT, total latency and throughput are defined as follows: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Latency** = TTFT + (TPOT) × (number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests

## Latency-Throughput Trade-Off

There is a trade-off between latency and throughput. At low concurrent request loads, latency is lowest. Increasing the request load raises latency, but throughput also tends to increase because multiple requests can be processed simultaneously on the same endpoint. At very high concurrency, throughput plateaus as the endpoint's provisioned capacity is reached, and additional requests queue, further increasing latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Controlling the number of parallel requests is therefore core to balancing latency with throughput. High-throughput use cases (e.g., batch inference, non-user-facing tasks) benefit from saturating the endpoint with many concurrent requests. Low-latency use cases (e.g., real-time applications) should send fewer concurrent requests to keep latency low. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Databricks Endpoint Autoscaling

Databricks LLM serving endpoints automatically scale to match the load sent by clients. The endpoint's autoscaling strategy balances between latency and throughput. The number of concurrent requests that can be processed simultaneously is limited by the [[provisioned throughput]] capacity (measured in tokens per second for supported models). ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [[Time to First Token (TTFT)]]
- [[Time per Output Token (TPOT)]]
- Latency
- Throughput
- [[Provisioned Throughput]]
- [[Foundation Model APIs]]
- Autoregressive Decoding
- [[Model Serving|LLM Serving]]
- Concurrency

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
```

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
