---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 28014be1adb527b69137ad4a2f23fc618383ed996f58566e3b25dfd6b1f57b84
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-inference-latency
    - LIL
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: LLM Inference Latency
description: Total response time calculated as TTFT plus the product of TPOT and number of generated tokens, representing end-to-end user-perceived delay.
tags:
  - llm-inference
  - performance-metrics
  - latency
timestamp: "2026-06-19T17:50:10.386Z"
---

# LLM Inference Latency

**LLM Inference Latency** refers to the total time required for a large language model (LLM) to process an input prompt and generate a complete output response. It is a critical performance metric for production applications, particularly those requiring real-time or near-real-time interactions.

## Components of LLM Inference

LLM inference proceeds in two distinct phases:

1. **Prefill**: The tokens in the input prompt are processed in parallel. This phase computes representations for all input tokens simultaneously.
2. **Decoding**: Text is generated one token at a time in an auto-regressive manner. Each generated token is appended to the input and fed back into the model to generate the next token. Generation stops when the LLM outputs a special stop token or when a user-defined condition is met.

^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The number of input tokens substantially impacts the required memory to process requests, while the number of output tokens dominates overall response latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Key Latency Metrics

Databricks divides LLM inference into the following sub-metrics:

### Time to First Token (TTFT)

**TTFT** measures how quickly users start seeing the model's output after entering their query. Low waiting times for a response are essential in real-time interactions but less important in offline workloads. This metric is driven by the time required to process the prompt and then generate the first output token. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Time per Output Token (TPOT)

**TPOT** measures the time to generate an output token for each user querying the system. This metric corresponds with how each user perceives the "speed" of the model. For example, a TPOT of 100 milliseconds per token would be 10 tokens per second, or approximately 450 words per minute, which is faster than a typical person can read. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Total Latency and Throughput

Based on these metrics, total latency and throughput can be defined as:

- **Latency** = TTFT + (TPOT × number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests

^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Latency-Throughput Trade-off

On Databricks, LLM Serving Endpoints are able to scale to match the load sent by clients with multiple concurrent requests. There is a fundamental trade-off between latency and throughput because concurrent requests can be processed at the same time. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- At **low concurrent request loads**, latency is the lowest possible.
- As **request load increases**, latency might increase, but throughput also tends to increase because two requests worth of tokens per second can be processed in less than double the time. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Controlling the number of parallel requests into the system is core to balancing latency with throughput:
- **Low latency use cases** (e.g., real-time applications requiring immediate responses): send fewer concurrent requests to keep latency low.
- **High throughput use cases** (e.g., batch inferences and other non-user-facing tasks): saturate the endpoint with more concurrency requests, accepting higher latency in exchange for greater throughput. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Throughput Plateau

As the number of parallel requests increases, throughput eventually begins to plateau, reaching a limit determined by the provisioned throughput for the endpoint. This plateau occurs because the provisioned throughput limits the number of workers and parallel requests that can be handled. Beyond this limit, total latency continues to increase as additional requests wait in the queue. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Provisioned Throughput and Benchmarking

Databricks measures tokens per second for [Provisioned Throughput](/concepts/provisioned-throughput.md) mode for [Foundation Model APIs](/concepts/foundation-model-apis.md). The benchmarking harness provided by Databricks displays total latency across all requests and throughput metrics, plotting the throughput versus latency curve across different numbers of parallel requests. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [Time to First Token (TTFT)](/concepts/time-to-first-token-ttft.md)
- [Time per Output Token (TPOT)](/concepts/time-per-output-token-tpot.md)
- LLM Serving Endpoints
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Model Units in Provisioned Throughput](/concepts/provisioned-throughput.md)
- [LLM Inference Performance Engineering](/concepts/llm-inference-prefill-and-decoding.md)

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
