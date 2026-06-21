---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 12d2028c8a1190f9bc75b485b9f64c143785687ea63aa0641dbe4ef8093901bb
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-llm-endpoint-benchmarking-methodology
    - DLEBM
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Databricks LLM Endpoint Benchmarking Methodology
description: Databricks recommends maximizing throughput within a given latency budget using a benchmarking harness that measures total latency, throughput, and the throughput-latency curve across varying concurrency levels.
tags:
  - databricks
  - benchmarking
  - llm-serving
timestamp: "2026-06-19T14:23:47.454Z"
---

# Databricks LLM Endpoint Benchmarking Methodology

**Databricks LLM Endpoint Benchmarking Methodology** defines the standardized approach for measuring and evaluating the performance of LLM serving endpoints on the Databricks platform. This methodology focuses on two primary metrics—latency and throughput—and provides a systematic framework for understanding the trade-offs between them under varying concurrency loads.

## Overview

LLM endpoint benchmarking on Databricks is designed to help users characterize the performance of their served models, particularly those using provisioned throughput mode for Foundation Model APIs. The benchmarking methodology is provided through a recommended notebook example that performs load testing against a specified LLM endpoint. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The methodology applies to provisioned throughput workloads that serve models provisioning inference capacity based on *tokens per second*. Supported models include Meta Llama 3.3, Meta Llama 3.2 (1B and 3B), Meta Llama 3.1, GTE v1.5 (English), BGE v1.5 (English), and DeepSeek R1. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## LLM Inference Process

LLMs perform inference in a two-step process that directly informs the benchmarking metrics:

- **Prefill:** Tokens in the input prompt are processed in parallel. The number of input tokens has a substantial impact on the required memory to process requests.
- **Decoding:** Text is generated one token at a time in an auto-regressive manner. Each generated token is appended to the input and fed back into the model to generate the next token. Generation stops when the LLM outputs a special stop token or when a user-defined condition is met. The number of output tokens dominates overall response latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Key Performance Metrics

Databricks divides LLM inference into the following sub-metrics:

### Time to First Token (TTFT)

TTFT measures how quickly users start seeing the model's output after entering their query. Low waiting times for a response are essential in real-time interactions but less important in offline workloads. This metric is driven by the time required to process the prompt and then generate the first output token. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Time per Output Token (TPOT)

TPOT measures the time to generate an output token for each user that is querying the system. This metric corresponds with how each user perceives the "speed" of the model. For example, a TPOT of 100 milliseconds per token would be 10 tokens per second, or approximately 450 words per minute, which is faster than a typical person can read. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Derived Metrics

From TTFT and TPOT, total latency and throughput can be defined as follows:

- **Latency** = TTFT + (TPOT) × (the number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrency requests

^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## The Latency vs. Throughput Trade-off

On Databricks, LLM serving endpoints can scale to match the load sent by clients with multiple concurrent requests. There is a fundamental trade-off between latency and throughput:

- At **low concurrent request loads**, latency is the lowest possible.
- As **request load increases**, latency may increase, but throughput likely also increases. This occurs because two requests' worth of tokens per second can be processed in less than double the time due to batching efficiency.

^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Use Case Guidance

Controlling the number of parallel requests is core to balancing latency with throughput:

- **High throughput use cases** (e.g., batch inferences and non-user-facing tasks): Saturate the endpoint with lots of concurrency requests, since higher throughput is worth the expense of higher latency.
- **Low latency use cases** (e.g., real-time applications requiring immediate responses): Send fewer concurrent requests to keep latency low.

^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Databricks Benchmarking Harness

The Databricks benchmarking harness is provided as a notebook that can be imported into a Databricks environment. The notebook displays:

- The **total** latency across all requests and throughput metrics.
- A throughput versus latency curve plotted across different numbers of parallel requests.

^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Observations from Benchmarking

As more concurrent users query the endpoint, both latency and throughput increase initially. However, as the number of parallel requests continues to increase, throughput begins to plateau, reaching a limit determined by the provisioned throughput for the endpoint. This plateau occurs because the provisioned throughput limits the number of workers and parallel requests that can be made. Beyond this point, total latency continues to increase as additional requests wait in the queue. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Model Units Consideration

For models that use *model units* (rather than tokens per second) to provision inference capacity, see the documentation on Model units in provisioned throughput. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Best Practices for Production

Databricks recommends maximizing throughput given a latency budget for most production applications. The benchmarking methodology enables users to characterize the latency-throughput curve for their specific endpoint configuration and workload profile, allowing informed capacity planning and performance optimization. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md) — The inference capacity model for Foundation Model APIs
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving infrastructure for LLMs on Databricks
- LLM Inference Optimization — Techniques for improving inference performance
- [Model Units in Provisioned Throughput](/concepts/provisioned-throughput.md) — Capacity model for supported models
- [Serving Endpoint Scaling](/concepts/model-serving-endpoint-scaling.md) — How Databricks endpoints scale with load
- Latency Budget Planning — Defining performance requirements for production deployments

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
