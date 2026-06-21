---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd53a94730366147fc31471c96c4594407927bc17491082229950ccf2fd2fdb0
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-benchmarking-for-llm-endpoints
    - PTBFLE
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Provisioned Throughput Benchmarking for LLM Endpoints
description: The practice of load-testing an LLM serving endpoint by measuring tokens per second across varying concurrency levels to understand capacity limits and latency-throughput curves.
tags:
  - benchmarking
  - llm-serving
  - performance
timestamp: "2026-06-18T14:42:24.376Z"
---

# Provisioned Throughput Benchmarking for LLM Endpoints

**Provisioned Throughput Benchmarking for LLM Endpoints** refers to the practice of measuring and optimizing the performance of LLM serving endpoints that are configured with reserved inference capacity based on tokens per second. Databricks provides a recommended benchmarking notebook and a set of performance metrics to help users characterize endpoint behavior under varying concurrency levels. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Applicability

The benchmarking methodology described on this page applies to provisioned throughput workloads that serve models using *tokens per second* as the provisioning unit. The supported models include:

- Meta Llama 3.3
- Meta Llama 3.2 3B
- Meta Llama 3.2 1B
- Meta Llama 3.1
- GTE v1.5 (English)
- BGE v1.5 (English)
- DeepSeek R1 (not available in Unity Catalog)

For models that use *model units* (instead of tokens per second) to provision inference capacity, see Model units in provisioned throughput. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## LLM Inference Overview

LLM inference proceeds in two phases:

1. **Prefill** – The input prompt tokens are processed in parallel.
2. **Decoding** – The model generates text one token at a time in an auto-regressive fashion. Each newly generated token is appended to the input and fed back into the model to produce the next token. Generation stops when a special stop token is emitted or a user-defined condition is met.

Production applications typically operate under a latency budget, and Databricks recommends maximizing throughput within that budget. The number of input tokens substantially impacts the memory required to process requests, while the number of output tokens dominates the overall response latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Key Performance Metrics

Databricks divides inference performance into two sub-metrics:

- **Time to First Token (TTFT)** – Measures how quickly users see the first output token after submitting a query. TTFT is driven by the time to process the prompt and generate the first output token. It is essential for real-time interactions but less critical for offline workloads.
- **Time per Output Token (TPOT)** – Measures the time to generate each subsequent output token for a single user. TPOT reflects the perceived “speed” of the model. For example, a TPOT of 100 ms per token yields 10 tokens per second (~450 words per minute), which is faster than typical human reading speed. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

From these sub-metrics, total **latency** and **throughput** are defined as:

- **Latency** = TTFT + (TPOT × number of output tokens)
- **Throughput** = total output tokens per second across all concurrent requests ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Latency–Throughput Trade-off

LLM serving endpoints on Databricks auto-scale to match the load from multiple concurrent requests. There is an inherent trade–off between latency and throughput: concurrent requests are processed in parallel. At low concurrency, latency is minimal but throughput is low. As the number of parallel requests increases, latency rises but throughput also increases because two requests’ tokens can be processed in less than double the time.

Controlling the number of parallel requests is the primary mechanism for balancing latency with throughput:
- **High‑throughput use cases** (e.g., batch inference, non‑user‑facing tasks) benefit from saturating the endpoint with high concurrency, accepting higher latency in exchange for higher token throughput.
- **Low‑latency use cases** (e.g., real‑time interactive applications) send fewer concurrent requests to keep latency low. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Databricks Benchmarking Harness

Databricks provides a benchmarking notebook (importable into any Databricks environment) that performs a load test against a specified LLM endpoint. The notebook outputs:
- Total latency across all requests.
- Throughput metrics (tokens per second).
- A throughput‑vs‑latency curve as the number of parallel requests varies.

The Databricks endpoint autoscaling strategy balances latency and throughput. The notebook demonstrates that as concurrent users increase, both latency and throughput initially rise. However, at a certain point throughput plateaus — the provisioned throughput capacity limits how many workers can handle parallel requests. Beyond that limit, additional requests queue and total latency continues to increase while throughput stays nearly constant.

![Throughput-Latency Graph](https://docs.databricks.com/aws/en/assets/images/llm-throughput-latency-0f922f80ed2a57469de2c4f5776e5ea3.png)

For a deeper discussion of Databricks’ philosophy on LLM performance benchmarking, see the blog post LLM Inference Performance Engineering: Best Practices. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Time to First Token (TTFT)](/concepts/time-to-first-token-ttft.md)
- [Time per Output Token (TPOT)](/concepts/time-per-output-token-tpot.md)
- [Foundation Model APIs on Databricks](/concepts/foundation-models-apis-on-databricks.md)
- Model units in provisioned throughput

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
