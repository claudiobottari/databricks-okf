---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 73dbe624bdfb57fb6f4b3f0315317a4025738f7e8951321991c70998fe162861
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-endpoint-benchmarking-harness
    - LEBH
    - LLM endpoint benchmarking
    - Conduct your own LLM endpoint benchmarking
    - Databricks benchmarking harness
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: LLM Endpoint Benchmarking Harness
description: A systematic approach to benchmarking LLM endpoints by measuring total latency, throughput, and the throughput-versus-latency curve across varying numbers of parallel requests.
tags:
  - benchmarking
  - llm-serving
  - testing
timestamp: "2026-06-19T09:22:03.551Z"
---

# LLM Endpoint Benchmarking Harness

**LLM Endpoint Benchmarking Harness** is a Databricks-provided notebook tool for conducting load testing and performance evaluation of [LLM serving endpoints](/concepts/model-serving-endpoint.md) using provisioned throughput. The harness measures key performance metrics — latency and throughput — across varying levels of concurrent requests, enabling users to understand the trade-offs between response speed and processing capacity for their specific use cases. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Overview

The benchmarking harness is designed for provisioned throughput workloads that serve models based on *tokens per second*. It applies to models including Meta Llama 3.3, Meta Llama 3.2 (3B and 1B), Meta Llama 3.1, GTE v1.5 (English), BGE v1.5 (English), and DeepSeek R1 (not available in Unity Catalog). Models using *model units* (rather than tokens per second) to provision inference capacity follow a different mechanism. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## LLM Inference Metrics

LLM inference on Databricks is divided into two phases:

- **Prefill**: Input prompt tokens are processed in parallel.
- **Decoding**: Text is generated one token at a time in an auto-regressive manner until a stop token or user-defined condition is met. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The harness measures the following sub-metrics:

- **Time to First Token (TTFT)**: How quickly users start seeing output after entering their query. Driven by prompt processing time and generation of the first output token. Critical for real-time interactions, less important for offline workloads. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]
- **Time Per Output Token (TPOT)**: Time to generate an output token for each user querying the system. Corresponds to how each user perceives model "speed." For example, a TPOT of 100 ms per token equals 10 tokens per second (~450 words per minute). ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

From these sub-metrics, total latency and throughput are defined:

- **Latency** = TTFT + (TPOT × number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Latency-Throughput Trade-off

LLM serving endpoints on Databricks scale to match client load with multiple concurrent requests. There is an inherent trade-off between latency and throughput:

- At low concurrent request loads, latency is at its minimum.
- As request load increases, latency may rise, but throughput typically also increases because multiple requests' tokens per second can be processed in less than double the time. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Controlling the number of parallel requests is core to balancing latency with throughput:

- **Low latency use cases** (e.g., real-time applications requiring immediate responses): Send fewer concurrent requests to keep latency low.
- **High throughput use cases** (e.g., batch inferences, non-user-facing tasks): Saturate the endpoint with high concurrency, accepting higher latency for greater throughput. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Harness Output

The benchmarking notebook displays:

- **Total latency** across all requests
- **Throughput metrics**
- **Throughput versus latency curve** across different numbers of parallel requests ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

As concurrent users increase, both latency and throughput initially rise. However, throughput eventually plateaus when the provisioned throughput limit is reached — the endpoint cannot handle more parallel requests simultaneously, and additional requests wait in a queue, increasing total latency without improving throughput. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Usage

Users import the benchmarking notebook into their Databricks environment and specify the name of their LLM endpoint to run a load test. The harness automates the process of sending varying numbers of concurrent requests and collecting performance data. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Inference capacity provisioning based on tokens per second
- [Model Units in Provisioned Throughput](/concepts/provisioned-throughput.md) — Alternative provisioning mechanism for certain models
- LLM Serving Endpoints — Databricks managed endpoints for model inference
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — API layer for accessing LLMs on Databricks
- Latency Budget — Performance constraints for production applications

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
