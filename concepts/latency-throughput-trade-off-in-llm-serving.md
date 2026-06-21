---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5762b7c989fcb276122bf0c7820016409602f38eba4966bb24370ff7f0ea2ffc
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - latency-throughput-trade-off-in-llm-serving
    - LTILS
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Latency-Throughput Trade-off in LLM Serving
description: The fundamental tension in LLM serving where increasing concurrent requests improves throughput at the cost of higher latency, requiring careful control of parallelism based on use case.
tags:
  - llm-serving
  - performance
  - optimization
timestamp: "2026-06-19T09:22:10.576Z"
---

```markdown
---
title: Latency-Throughput Trade-off in LLM Serving
summary: The fundamental trade-off where increasing concurrent requests to an LLM endpoint improves throughput but increases latency, requiring careful balancing based on use case (real-time vs. batch).
sources:
  - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:06:49.047Z"
updatedAt: "2026-06-18T11:06:49.047Z"
tags:
  - llm
  - performance
  - optimization
aliases:
  - latency-throughput-trade-off-in-llm-serving
  - LTILS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Latency-Throughput Trade-off in LLM Serving

**Latency-Throughput Trade-off in LLM Serving** refers to the fundamental performance tension in large language model inference endpoints: optimizing for low latency (fast individual response times) and high throughput (total tokens processed per second across all requests) are competing objectives that must be balanced based on application requirements.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## LLM Inference Process

LLMs perform inference in a two-step process:

- **Prefill**: The tokens in the input prompt are processed in parallel.
- **Decoding**: Text is generated one token at a time in an auto-regressive manner. Each generated token is appended to the input and fed back into the model to generate the next token. Generation stops when the LLM outputs a special stop token or when a user-defined condition is met.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Most production applications have a latency budget, and Databricks recommends maximizing throughput given that latency budget. The number of input tokens has a substantial impact on the required memory to process requests, while the number of output tokens dominates overall response latency.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Key Performance Metrics

LLM inference is divided into the following sub-metrics:

- **Time to first token (TTFT)**: How quickly users start seeing the model's output after entering their query. Low waiting times are essential in real-time interactions but less important in offline workloads. This metric is driven by the time required to process the prompt and then generate the first output token.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]
- **Time per output token (TPOT)**: Time to generate an output token for each user querying the system. This metric corresponds with how each user perceives the "speed" of the model. For example, a TPOT of 100 milliseconds per token would be 10 tokens per second, or approximately 450 words per minute, which is faster than a typical person can read.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Based on these metrics, total latency and throughput can be defined as follows:

- **Latency** = TTFT + (TPOT) × (number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## The Trade-off

On Databricks, LLM serving endpoints can scale to match the load sent by clients with multiple concurrent requests. There is a trade-off between latency and throughput because concurrent requests can be and are processed at the same time.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

At low concurrent request loads, latency is the lowest possible. However, if you increase the request load, latency might increase, but throughput likely also increases. This occurs because two requests' worth of tokens per second can be processed in less than double the time.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Therefore, controlling the number of parallel requests into your system is core to balancing latency with throughput:

- **Low latency use cases**: Send fewer concurrent requests to the endpoint to keep latency low. Examples include real-time applications that require immediate responses.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]
- **High throughput use cases**: Saturate the endpoint with lots of concurrent requests, since higher throughput is worth it even at the expense of latency. Examples include batch inferences and other non-user-facing tasks.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Throughput Plateau

As the number of parallel requests increases, throughput begins to plateau, reaching a limit determined by the provisioned throughput for the endpoint. This plateau occurs because the provisioned throughput limits the number of workers and parallel requests that can be made. As more requests are made beyond what the endpoint can handle simultaneously, total latency continues to increase as additional requests wait in the queue.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

![Throughput-Latency Graph](https://docs.databricks.com/aws/en/assets/images/llm-throughput-latency-0f922f80ed2a57469de2c4f5776e5ea3.png)

## Benchmarking

Databricks provides a benchmarking notebook that displays total latency across all requests and throughput metrics, and plots the throughput versus latency curve across different numbers of parallel requests. The endpoint autoscaling strategy balances between latency and throughput. In the benchmark, you observe that latency and throughput increase as more concurrent users query the endpoint.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- [[Provisioned Throughput]] — Inference capacity provisioning based on tokens per second or model units
- [[Foundation Model APIs]] — Databricks API for serving LLMs
- [[Model Serving Endpoint|Model Serving Endpoints]] — Endpoints that scale to match client load
- [[LLM Inference Prefill and Decoding|LLM Inference Performance Engineering]] — Best practices for optimizing LLM serving performance

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
```

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
