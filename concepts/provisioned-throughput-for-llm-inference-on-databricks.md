---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4175d15ed07a2c51fcbd725faeef17e3f2ece19f92fc078db444e4da8c27d040
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-for-llm-inference-on-databricks
    - PTFLIOD
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Provisioned Throughput for LLM Inference on Databricks
description: A capacity provisioning model for Databricks Foundation Model APIs where inference capacity is allocated in tokens per second for specific supported models (e.g., Meta Llama, GTE, BGE).
tags:
  - databricks
  - llm
  - capacity-planning
timestamp: "2026-06-18T11:06:36.268Z"
---

# Provisioned Throughput for LLM Inference on Databricks

**Provisioned throughput** is a mode of the [Foundation Model APIs](/concepts/foundation-model-apis.md) on Databricks that reserves dedicated inference capacity for an LLM endpoint, measured in **tokens per second**. This mode is designed for production workloads that require predictable performance and the ability to handle sustained concurrent requests without resource contention. The capacity is provisioned upfront, and the endpoint autoscales within that reserved limit to balance latency and throughput.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Supported models

The topics on this page apply to provisioned throughput workloads that provision inference capacity based on *tokens per second*. The following models are included:

- Meta Llama 3.3
- Meta Llama 3.2 3B
- Meta Llama 3.2 1B
- Meta Llama 3.1
- GTE v1.5 (English)
- BGE v1.5 (English)
- DeepSeek R1 (not available in Unity Catalog)

For models that use *model units* instead of tokens per second to provision inference capacity, see Model units in provisioned throughput.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## LLM inference two-step process

LLM inference on Databricks proceeds in two phases:

- **Prefill**: the tokens in the input prompt are processed in parallel.
- **Decoding**: text is generated one token at a time in an auto-regressive manner. Each generated token is appended to the input and fed back into the model. Generation stops when a special stop token is emitted or a user-defined condition is met.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The number of input tokens has a substantial impact on the required memory to process requests, while the number of output tokens dominates overall response latency.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Key performance metrics

Databricks divides LLM inference performance into two fundamental sub-metrics:

- **Time to first token (TTFT)**: how quickly users start seeing the model's output after entering their query. Low TTFT is essential for real-time interactions but less important for offline workloads. TTFT is driven by the time required to process the prompt and generate the first output token.
- **Time per output token (TPOT)**: the time to generate a single output token for each concurrent user. This metric corresponds with how fast each user perceives the model. For example, a TPOT of 100 ms per token yields approximately 10 tokens per second, or ~450 words per minute.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

From these sub-metrics, total latency and throughput are defined:

- **Latency** = TTFT + (TPOT × number of tokens to generate)
- **Throughput** = number of output tokens per second across all concurrent requests^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Latency–throughput trade-off

LLM serving endpoints on Databricks process multiple concurrent requests simultaneously. There is an inherent trade-off between latency and throughput:

- At low concurrency, latency is at its minimum because requests are processed without queuing.
- As concurrency increases, throughput rises because multiple requests’ tokens are processed in parallel, but latency also increases as requests may queue.

Controlling the number of parallel requests is the core mechanism for balancing latency and throughput. High-throughput use cases (e.g., batch inference, non-user-facing tasks) benefit from saturating the endpoint with many concurrent requests. Low-latency use cases (e.g., real-time applications) should send fewer concurrent requests to minimize latency.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Provisioned throughput capacity and plateau

Provisioned throughput limits the number of workers and concurrent requests the endpoint can handle. When the number of parallel requests exceeds what the provisioned capacity can serve simultaneously, additional requests are queued. As a result, throughput plateaus at the provisioned limit (e.g., approximately 8,000 tokens per second in example benchmarks), while total latency continues to increase as queued requests wait.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

![Throughput-Latency Graph](https://docs.databricks.com/aws/en/assets/images/llm-throughput-latency-0f922f80ed2a57469de2c4f5776e5ea3.png)

## Benchmarking an LLM endpoint

Databricks provides a recommended notebook (the "benchmarking harness") that performs a load test against an LLM endpoint. The notebook:

- Displays **total** latency across all requests and throughput metrics.
- Plots the throughput-versus-latency curve across different numbers of parallel request workers.
- Demonstrates how latency and throughput increase as more concurrent users query the endpoint.

You can import this notebook into your Databricks environment and specify the name of your LLM endpoint to run a load test.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

## Related concepts

- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The service layer that offers provisioned throughput endpoints
- Model units in provisioned throughput — Alternative capacity provisioning for certain models
- Latency and Throughput — Core performance measures for LLM inference
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) — Overview of model deployment and inference
- Autoscaling in Databricks Model Serving — How endpoints automatically scale within provisioned limits

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
