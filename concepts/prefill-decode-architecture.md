---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 35fbbc38537f84cb69bf299bee9c37e6e80912f1b1a9a88be40ac6fb75452111
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prefill-decode-architecture
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Prefill-Decode Architecture
description: The two-phase LLM inference process where input tokens are processed in parallel (prefill) followed by auto-regressive token-by-token generation (decode).
tags:
  - llm-inference
  - architecture
  - transformer
timestamp: "2026-06-19T17:50:08.861Z"
---

## Prefill-Decode Architecture

The **Prefill-Decode Architecture** describes how large language models (LLMs) perform inference in two distinct phases: a parallel *prefill* stage, followed by an auto-regressive *decode* stage. This division is fundamental to understanding LLM serving performance metrics such as latency and throughput.

### Prefill Phase

During the prefill phase, all tokens in the input prompt are processed in parallel. The model computes hidden states and key-value (KV) cache entries for every prompt token simultaneously, leveraging the parallel processing capabilities of GPUs. The time required for this phase is a major component of the **time to first token** (TTFT), because the model cannot begin generating output until prefill is complete. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Decode Phase

In the decode phase, the model generates output tokens one at a time in an auto-regressive manner. Each newly generated token is appended to the input sequence and fed back into the model, using the KV cache from the prefill stage to avoid recomputing previous token representations. Generation continues until the model emits a special stop token or meets a user-defined stopping condition. The per-token generation time is the **time per output token** (TPOT), and the total number of output tokens dominates the overall response latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Relationship to Inference Metrics

LLM inference metrics are directly derived from the prefill-decode architecture:

- **Time to First Token (TTFT)** – Driven by the prefill time plus the time to generate the first output token. A low TTFT is critical for real-time interactive use cases. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]
- **Time per Output Token (TPOT)** – The per-token generation speed during the decode phase. For example, a TPOT of 100 ms/token yields a generation rate of 10 tokens/second, which is faster than typical human reading speed. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]
- **Latency** – TTFT + (TPOT × number of generated tokens). ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]
- **Throughput** – The number of output tokens generated per second across all concurrent requests. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Implications for Serving

The prefill-decode architecture creates a fundamental trade-off between latency and throughput. Processing multiple concurrent requests increases throughput because the system can interleave decode steps from different users, but it also increases queuing delays and per-request latency. Applications with low-latency requirements should limit concurrency, while high-throughput batch inference tasks can saturate the endpoint with many parallel requests. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Related Concepts

- [Time to First Token (TTFT)](/concepts/time-to-first-token-ttft.md)
- [Time per Output Token (TPOT)](/concepts/time-per-output-token-tpot.md)
- LLM Inference
- Latency
- Throughput
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Provisioned Throughput](/concepts/provisioned-throughput.md)

### Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
