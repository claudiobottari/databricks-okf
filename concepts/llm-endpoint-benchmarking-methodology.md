---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: baafe24bb8f512eaffeec0d2c63339141fdd92160e52dc3226ab951341bf6d0b
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-endpoint-benchmarking-methodology
    - LEBM
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: LLM Endpoint Benchmarking Methodology
description: A Databricks-recommended approach using a benchmarking harness notebook that measures total latency vs. throughput across varying concurrency levels to characterize endpoint performance.
tags:
  - databricks
  - testing
  - llm
timestamp: "2026-06-18T11:07:37.580Z"
---

# LLM Endpoint Benchmarking Methodology

**LLM Endpoint Benchmarking Methodology** refers to the structured approach for measuring and evaluating the performance of [LLM serving endpoints](/concepts/model-serving-endpoint.md) in Databricks, specifically for provisioned throughput workloads that serve models based on tokens per second. Databricks provides a recommended benchmarking notebook and framework to help users conduct load tests and understand performance characteristics.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Scope and Applicability

This benchmarking methodology applies to provisioned throughput workloads serving models that provision inference capacity based on **tokens per second**. The following models are supported:

- Meta Llama 3.3
- Meta Llama 3.2 3B
- Meta Llama 3.2 1B
- Meta Llama 3.1
- GTE v1.5 (English)
- BGE v1.5 (English)
- DeepSeek R1 (not available in Unity Catalog)

For models that use **model units** (rather than tokens per second) to provision inference capacity, see Model units in provisioned throughput.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## LLM Inference Fundamentals

LLMs perform inference in a two-step process:

- **Prefill**: The tokens in the input prompt are processed in parallel.
- **Decoding**: Text is generated one token at a time in an auto-regressive manner. Each generated token is appended to the input and fed back into the model to generate the next token. Generation stops when the LLM outputs a special stop token or when a user-defined condition is met.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Most production applications have a latency budget, and Databricks recommends maximizing throughput given that latency budget. The number of input tokens has a substantial impact on the required memory to process requests, while the number of output tokens dominates overall response latency.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Key Performance Metrics

Databricks divides LLM inference into the following sub-metrics:

### Time to First Token (TTFT)

**Time to first token** measures how quickly users start seeing the model's output after entering their query. Low waiting times for a response are essential in real-time interactions, but less important in offline workloads. This metric is driven by the time required to process the prompt and then generate the first output token.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Time per Output Token (TPOT)

**Time per output token** measures the time to generate an output token for each user querying the system. This metric corresponds with how each user perceives the "speed" of the model. For example, a TPOT of 100 milliseconds per token would be 10 tokens per second, or approximately 450 words per minute, which is faster than a typical person can read.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Derived Metrics

Based on TTFT and TPOT, total latency and throughput are defined as follows:

- **Latency** = TTFT + (TPOT × number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests

## Latency-Throughput Trade-off

On Databricks, LLM serving endpoints can scale to match the load sent by clients with multiple concurrent requests. There is a fundamental trade-off between latency and throughput. Concurrent requests can be and are processed at the same time:^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **At low concurrent request loads**, latency is the lowest possible.
- **As request load increases**, latency may increase, but throughput likely also increases. This is because two requests' worth of tokens per second can be processed in less than double the time.

Controlling the number of parallel requests into your system is core to balancing latency with throughput:^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Low latency use cases** (e.g., real-time applications requiring immediate responses) benefit from fewer concurrent requests to keep latency low.
- **High throughput use cases** (e.g., batch inferences and non-user-facing tasks) benefit from saturating the endpoint with many concurrent requests, accepting higher latency in exchange for higher throughput.

## Benchmarking Harness

Databricks provides a benchmarking example notebook that serves as the standard benchmarking harness. The notebook displays the **total** latency across all requests and throughput metrics, and plots the throughput versus latency curve across different numbers of parallel requests.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

The Databricks endpoint autoscaling strategy balances between latency and throughput. In the notebook output, you observe that latency and throughput increase as more concurrent users query the endpoint.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Understanding the Plateau

As the number of parallel requests increases, the throughput begins to plateau, reaching a limit determined by the provisioned throughput for the endpoint. This plateau occurs because the provisioned throughput limits the number of workers and parallel requests that can be made. As more requests are made beyond what the endpoint can handle simultaneously, total latency continues to increase as additional requests wait in the queue.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Running a Benchmark

To run a benchmark, import the benchmarking notebook into your Databricks environment and specify the name of your LLM endpoint. The notebook will execute a load test and generate the latency-throughput curve.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Best Practices

- **Match concurrency to use case**: Use fewer concurrent requests for real-time applications and higher concurrency for batch processing.
- **Monitor TTFT for interactive applications**: Time to first token is critical for user-facing applications where response time matters.
- **Establish a latency budget**: Determine the maximum acceptable latency for your application and maximize throughput within that constraint.
- **Benchmark with realistic payloads**: Test with input and output token counts that match your production workload characteristics.
- **Understand your endpoint's capacity limits**: The provisioned throughput determines the maximum throughput and the point at which latency begins to increase significantly.

## Related Concepts

- [LLM serving endpoints](/concepts/model-serving-endpoint.md) — The Databricks infrastructure for deploying LLMs
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Capacity provisioning for Foundation Model APIs
- Model units in provisioned throughput — Alternative provisioning model for certain models
- Latency optimization — Strategies for reducing response times
- Throughput optimization — Strategies for maximizing tokens per second
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Databricks API for accessing foundation models

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
