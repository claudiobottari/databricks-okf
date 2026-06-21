---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ccd9045a601fc737493ecc0cf725ad7f06a5b37286c91cd4b6492ebbf228fddb
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provisioned-throughput-benchmarking
    - PTB
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Provisioned Throughput Benchmarking
description: The methodology of measuring tokens per second under varying concurrent request loads to find the saturation point where throughput plateaus due to provisioned capacity limits.
tags:
  - llm-inference
  - benchmarking
  - databricks
timestamp: "2026-06-19T17:50:51.191Z"
---

# Provisioned Throughput Benchmarking

**Provisioned Throughput Benchmarking** is a Databricks-recommended methodology for evaluating the performance of Large Language Model (LLM) endpoints operating under provisioned throughput capacity, where inference capacity is measured in tokens per second rather than model units.

## Overview

Provisioned Throughput Benchmarking applies to Foundation Model API endpoints that provision inference capacity based on **tokens per second**. This benchmarking approach is designed for models that measure throughput in terms of token generation rates rather than model units. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Applicable Models

The following models support provisioned throughput benchmarking with tokens-per-second capacity provisioning:

- Meta Llama 3.3
- Meta Llama 3.2 3B
- Meta Llama 3.2 1B
- Meta Llama 3.1
- GTE v1.5 (English)
- BGE v1.5 (English)
- DeepSeek R1
- Other models using token-based provisioning

See Model units in provisioned throughput for models that use model units instead of tokens per second. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## LLM Inference Architecture

Databricks divides LLM inference into a two-step process that forms the basis for benchmarking metrics:

### Prefill and Decoding

**Prefill** processes input prompt tokens in parallel, while **Decoding** generates text one token at a time in an autoregressive manner. Generation stops when the model outputs a special stop token or when a user-defined condition is met. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Key Performance Metrics

- **Time to First Token (TTFT)**: How quickly users start seeing the model's output after entering their query. Low waiting times are essential for real-time interactions but less critical for offline workloads. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]
- **Time Per Output Token (TPOT)**: Time to generate an output token for each user querying the system. This metric corresponds with how each user perceives the "speed" of the model. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Derived Metrics

From these sub-metrics, total performance can be calculated:

- **Latency** = TTFT + (TPOT × number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests

These formulas demonstrate that the number of output tokens dominates overall response latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Latency-Throughput Trade-off

LLM serving endpoints on Databricks can scale to match load from concurrent requests. There is a fundamental trade-off between latency and throughput: concurrent requests are processed at the same time, so at low concurrency loads latency is minimal, but increasing the request load may increase both latency and throughput. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Use Case Considerations

- **High throughput use cases**: Batch inferences and other non-user-facing tasks benefit from saturating endpoints with high concurrency requests.
- **Low latency use cases**: Real-time applications requiring immediate responses should send fewer concurrent requests to keep latency low.

## Benchmarking Harness

The Databricks benchmarking harness is the recommended tool for conducting LLM endpoint benchmarking. It measures total latency across all requests and throughput metrics, then plots throughput versus latency curves across different numbers of parallel requests. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Throughput Plateau

As the number of parallel requests increases, throughput begins to plateau, reaching a limit determined by the provisioned throughput capacity. This plateau occurs because the endpoint's provisioned throughput limits the number of workers and parallel requests that can be handled simultaneously. Beyond this limit, additional requests wait in the queue, causing total latency to continue increasing. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [Model Units in Provisioned Throughput](/concepts/provisioned-throughput.md) – Alternative provisioning model for non-token-based models
- [LLM Inference Performance Engineering](/concepts/llm-inference-prefill-and-decoding.md) – Databricks best practices blog for LLM performance
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The API framework for provisioned throughput endpoints
- Token-Based Capacity Provisioning – How inference capacity is measured and allocated
- Autoscaling Strategy – How Databricks endpoints balance latency and throughput

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
