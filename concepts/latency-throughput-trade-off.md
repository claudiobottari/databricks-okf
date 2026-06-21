---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e64f212b76d52f2c599388d1e862c1ae78a8aaf23f0acbbc336ad6fdfc1b567
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - latency-throughput-trade-off
    - latency–throughput tradeoff
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Latency-Throughput Trade-off
description: The fundamental tension in LLM serving where increasing concurrent requests improves throughput at the cost of higher per-request latency, requiring workload-specific balancing.
tags:
  - llm-inference
  - optimization
  - serving
timestamp: "2026-06-19T17:50:11.642Z"
---

## Latency-Throughput Trade-off

The **Latency-Throughput Trade-off** is a fundamental design consideration in LLM Serving|Model Serving systems. It describes the inverse relationship between how quickly individual requests receive a response (latency) and how many output tokens the system can generate per second across all concurrent users (throughput). Balancing this trade-off is essential for meeting application requirements—real-time interactions demand low latency, while offline batch jobs prioritize high throughput. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Definitions of Latency and Throughput

On Databricks, LLM inference latency and throughput are decomposed into sub-metrics:

- **Time to First Token (TTFT)**: How quickly users start seeing the model’s output after submitting a query. TTFT is driven by prompt processing and generation of the first token.
- **Time per Output Token (TPOT)**: The time to generate one output token for each user. A TPOT of 100 ms/token corresponds to ~10 tokens per second per user.

Using these sub-metrics, total latency and throughput are defined as:

- **Latency** = TTFT + (TPOT × number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests

^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### How Concurrency Affects the Trade-off

LLM serving endpoints on Databricks can process multiple concurrent requests simultaneously. At low concurrency, each request experiences minimal queuing and the lowest possible latency, but the total throughput is low because fewer requests are being served. As concurrency increases, the system can process more requests in parallel, raising throughput. However, latency also rises because requests must wait in a queue and compete for GPU compute. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Beyond a certain concurrency level, throughput plateaus due to [Provisioned Throughput](/concepts/provisioned-throughput.md) limits—the endpoint cannot allocate more workers or processing capacity. Additional requests then only increase latency without improving throughput. This plateau is visible in Databricks benchmarking graphs, where the throughput curve flattens while latency continues to climb. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Practical Implications

Controlling the number of parallel requests sent to an endpoint is the core mechanism for balancing latency and throughput:

- **Low‑latency use cases** (e.g., real‑time chatbots, interactive applications) require fewer concurrent requests to keep latency low, accepting lower throughput.
- **High‑throughput use cases** (e.g., batch inference, offline processing) should saturate the endpoint with many concurrent requests, tolerating higher latency to maximize tokens per second.

^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Databricks Endpoint Autoscaling and Benchmarking

Databricks endpoints have an autoscaling strategy that attempts to balance latency and throughput. The official LLM Endpoint Benchmarking|benchmarking notebook shows how latency and throughput increase together as concurrency rises, and how throughput eventually reaches a ceiling set by provisioned throughput capacity. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Related Concepts

- [Time to First Token (TTFT)](/concepts/time-to-first-token-ttft.md)
- [Time per Output Token (TPOT)](/concepts/time-per-output-token-tpot.md)
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Model Serving](/concepts/model-serving.md)
- Concurrent Requests
- [LLM Inference Performance Engineering](/concepts/llm-inference-prefill-and-decoding.md)

### Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
