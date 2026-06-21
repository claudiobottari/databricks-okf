---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43bf98925520760d8f356821d4fff60b09bafbf9864f3253c5b9acae860cf209
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-inference-phases-prefill-and-decoding
    - "Decoding and LLM Inference Phases: Prefill"
    - LIPPAD
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: "LLM Inference Phases: Prefill and Decoding"
description: "LLMs perform inference in two distinct phases: prefill (parallel processing of input tokens) and decoding (auto-regressive generation of output tokens one at a time)."
tags:
  - llm-inference
  - performance
  - architecture
timestamp: "2026-06-19T09:21:38.040Z"
---

# LLM Inference Phases: Prefill and Decoding

**LLM Inference Phases** describe the two distinct stages that a large language model (LLM) goes through when generating a response: **prefill** (processing the input prompt in parallel) and **decoding** (generating output tokens one at a time). Understanding these phases is essential for reasoning about latency, throughput, and overall endpoint performance. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Prefill Phase

During the prefill phase, all tokens in the input prompt are processed by the model in parallel. This step produces the initial key-value cache and computes the hidden states that will be used during decoding. The time required for prefill is the dominant contributor to the **[Time to First Token (TTFT)](/concepts/time-to-first-token-ttft.md)**, which measures how quickly a user sees the beginning of the model’s output after submitting a query. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Decoding Phase

The decoding phase is **autoregressive**: the model generates one output token at a time. Each newly generated token is appended to the input sequence and fed back into the model as context for the next token. Generation continues until the model outputs a special stop token or a user-defined condition (such as a maximum token limit) is met. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The per-token generation speed is measured by **[Time per Output Token (TPOT)](/concepts/time-per-output-token-tpot.md)**, which reflects how each user perceives the “speed” of the model. For example, a TPOT of 100 ms per token corresponds to roughly 10 tokens per second, which is faster than a typical person can read. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Impact on Latency and Throughput

The overall **latency** of an LLM inference request is the sum of the prefill and decoding times:

```
Latency = TTFT + (TPOT × number of tokens to be generated)
```

**Throughput** is defined as the number of output tokens per second across all concurrent requests. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Because the number of input tokens drives the memory needed to process a request and the number of output tokens dominates response latency, the two phases impose different constraints:

- A large prompt increases prefill time and memory usage.
- A long generation increases the decoding phase and thus total latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Latency–Throughput Trade-off

On [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoints, concurrent requests are processed simultaneously. At low concurrency, latency is minimized; as the number of parallel requests increases, throughput typically rises, but latency may also increase because requests queue for compute resources. Controlling the number of parallel requests is therefore central to balancing latency against throughput. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **High-throughput use cases** (e.g., batch inference) benefit from saturating the endpoint with high concurrency, accepting higher latency in exchange for more tokens per second overall.
- **Low-latency use cases** (e.g., real-time chat) should keep concurrency low to minimize response waiting time. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Both phases are relevant to the benchmarking approach described in [Conduct your own LLM endpoint benchmarking](/concepts/llm-endpoint-benchmarking-harness.md), where tools measure TTFT, TPOT, and the throughput-versus-latency curve across different concurrency levels. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [Time to First Token (TTFT)](/concepts/time-to-first-token-ttft.md)
- [Time per Output Token (TPOT)](/concepts/time-per-output-token-tpot.md)
- Autoregressive Decoding
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [LLM Inference Performance Engineering](/concepts/llm-inference-prefill-and-decoding.md)

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
