---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d0b2f1c4fcd9ff73d74ec4ebd0313e72557c88873bf4162b65a8ab58f436659
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-llm-serving-endpoint-autoscaling
    - DLSEA
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Databricks LLM Serving Endpoint Autoscaling
description: Databricks' strategy for dynamically scaling LLM serving endpoints that balances latency and throughput, where throughput plateaus at provisioned capacity limits as concurrency increases.
tags:
  - databricks
  - llm-serving
  - autoscaling
timestamp: "2026-06-18T14:42:30.654Z"
---

# Databricks LLM Serving Endpoint Autoscaling

**Databricks LLM Serving Endpoint Autoscaling** refers to the built-in ability of Databricks serving endpoints to dynamically adjust their capacity to match the incoming request load. The autoscaling strategy aims to balance latency and throughput by managing how many concurrent requests the endpoint processes at once. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Overview

LLM serving endpoints on Databricks are designed to scale with the load sent by clients. When multiple concurrent requests arrive, the endpoint can process them simultaneously, but the number of parallel requests that can be handled is bounded by the provisioned capacity of the endpoint. As the concurrency level increases, both latency and throughput tend to rise—until a plateau is reached where throughput stops growing and additional requests are queued, further increasing latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Latency-Throughput Trade-off

The autoscaling strategy explicitly navigates the fundamental trade-off between latency and throughput:

- At **low concurrency**, latency is at its lowest because requests are processed with minimal queuing.
- As **concurrency increases**, throughput improves because the endpoint can handle more output tokens per second. However, latency also increases because resources are shared among more requests.
- Beyond a certain point, **throughput plateaus** due to the provisioned throughput limit. Additional requests wait in a queue, which pushes latency higher without further throughput gains. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Controlling the number of parallel requests sent to an endpoint is therefore the primary way to balance these two metrics for a given use case. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Use Case Guidance

- **High throughput use cases** (e.g., batch inferences, non-user-facing tasks) benefit from saturating the endpoint with many concurrent requests, even if latency is higher. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]
- **Low latency use cases** (e.g., real-time applications) should limit concurrency to keep response times minimal. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Scaling Limits

The autoscaling capacity is ultimately constrained by the [Provisioned Throughput](/concepts/provisioned-throughput.md) of the endpoint, which is defined in terms of tokens per second (or [Model Units](/concepts/model-units.md) for certain models). When the number of parallel requests exceeds what the provisioned infrastructure can sustain, throughput flattens and requests are queued, increasing end-to-end latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Benchmarking Autoscaling Behavior

Databricks provides a benchmarking notebook that lets you observe the autoscaling behavior of your endpoint. The notebook measures total latency across all requests and throughput, then plots the latency-versus-throughput curve across different levels of concurrency. This plot shows how the endpoint scales and where the throughput plateau occurs, helping you choose the right concurrency for your use case. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Key Metrics

Autoscaling performance is expressed through the following sub-metrics defined by Databricks:

- **Time to First Token (TTFT)** – how quickly the first output token appears after a query.
- **Time Per Output Token (TPOT)** – the time to generate each subsequent token.
- **Latency** = TTFT + (TPOT × number of output tokens).
- **Throughput** = total number of output tokens per second across all concurrent requests.

These metrics form the basis for understanding how the endpoint responds to scaling. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md) — The pre-allocated inference capacity that limits scaling.
- [Model Units](/concepts/model-units.md) — Capacity unit for some provisioned throughput models.
- TTFT and TPOT — The two components of inference latency.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The serving layer that hosts the endpoints.
- [LLM Inference Performance Engineering](/concepts/llm-inference-prefill-and-decoding.md) — Broader best practices for tuning inference.

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
