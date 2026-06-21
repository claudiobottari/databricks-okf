---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f18fad50db23677998e919b8dfa60f1f16c1b85805d0a4571cefed14be079aae
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-and-tokens-per-second
    - Tokens Per Second and Provisioned Throughput
    - PTATPS
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Provisioned Throughput and Tokens Per Second
description: A model for provisioning inference capacity on Databricks based on tokens per second, with a throughput ceiling reached when the endpoint's provisioned capacity is saturated.
tags:
  - databricks
  - provisioned-throughput
  - scaling
timestamp: "2026-06-19T14:23:00.843Z"
---

# Provisioned Throughput and Tokens Per Second

**Provisioned Throughput** is a serving mode for [Foundation Model APIs](/concepts/foundation-model-apis.md) on Databricks that allocates inference capacity based on a specified *tokens per second* rate. It is used for models that provision capacity in tokens per second rather than using [Model Units](/concepts/model-units.md). ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Supported Models

Provisioned throughput workloads that serve models by provisioned *tokens per second* apply to:

- Meta Llama 3.3
- Meta Llama 3.2 3B
- Meta Llama 3.2 1B
- Meta Llama 3.1
- GTE v1.5 (English)
- BGE v1.5 (English)
- DeepSeek R1 (not available in Unity Catalog)

For models that use *model units* (not tokens per second) to provision inference capacity, see the documentation on Model units in provisioned throughput. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## LLM Inference Metrics

LLM inference on Databricks measures **tokens per second** for provisioned throughput mode. Inference proceeds in two steps:

- **Prefill** – the tokens in the input prompt are processed in parallel.
- **Decoding** – text is generated one token at a time in an auto‑regressive manner. Each generated token is appended to the input and fed back into the model to generate the next token. Generation stops when the LLM outputs a special stop token or when a user‑defined condition is met. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The number of input tokens substantially affects the memory required to process requests, while the number of output tokens dominates overall response latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The key sub‑metrics are:

- **Time to first token (TTFT)** – how quickly users start seeing the model’s output after entering their query. Low waiting times are essential for real‑time interactions but less important for offline workloads.
- **Time per output token (TPOT)** – the time to generate an output token for each user. TPOT corresponds to the perceived “speed” of the model (e.g., a TPOT of 100 ms/token yields 10 tokens per second, or ~450 words per minute, faster than typical reading speed). ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

**Latency** and **throughput** are defined as:

- **Latency** = TTFT + (TPOT × number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Latency and Throughput Trade‑off

LLM serving endpoints automatically scale to match the load from concurrent requests. There is an inherent trade‑off:

- At **low concurrency**, latency is the lowest possible.
- As concurrency increases, latency may rise, but throughput typically also increases because two requests’ worth of tokens can be processed in less than double the time. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Controlling the number of parallel requests sent to an endpoint is central to balancing latency with throughput:

- **High throughput use cases** (e.g., batch inference, non‑user‑facing tasks) benefit from saturating the endpoint with many concurrent requests, accepting higher latency in exchange for more total tokens per second.
- **Low latency use cases** (e.g., real‑time applications) benefit from sending fewer concurrent requests to keep individual response times low. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Most production applications have a latency budget. Databricks recommends maximizing throughput given that latency budget. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Databricks Benchmarking Harness

The Databricks benchmarking harness is a notebook (available as a load test example) that evaluates LLM endpoint performance. It displays the total latency across all requests and throughput metrics, then plots the **throughput‑vs‑latency curve** for different numbers of parallel requests. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

In a typical run, both latency and throughput increase as concurrency rises. However, throughput eventually plateaus – for example, reaching a limit of about 8000 tokens per second – because the provisioned throughput for the endpoint caps the number of workers and parallel requests. Beyond that plateau, additional requests wait in a queue, causing total latency to continue increasing without throughput gains. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The endpoint autoscaling strategy balances latency and throughput during this process. For a deeper dive, see the LLM Inference Performance Engineering: Best Practices blog post. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- Model units in provisioned throughput
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Time to First Token (TTFT)](/concepts/time-to-first-token-ttft.md)
- [Time per Output Token (TPOT)](/concepts/time-per-output-token-tpot.md)
- LLM Inference Performance Engineering: Best Practices

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
