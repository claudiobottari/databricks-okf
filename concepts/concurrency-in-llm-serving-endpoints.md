---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 24d313e2777e5454cc38c421694d3cf801ddeed511ba2384b6fc8eb851607854
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - concurrency-in-llm-serving-endpoints
    - CILSE
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: Concurrency in LLM Serving Endpoints
description: The number of parallel requests sent to an LLM endpoint; controlling concurrency is central to balancing latency and throughput, with low concurrency for real-time uses and high concurrency for batch/offline uses.
tags:
  - llm
  - scaling
  - performance
timestamp: "2026-06-18T11:07:10.554Z"
---

# Concurrency in LLM Serving Endpoints

**Concurrency in LLM Serving Endpoints** refers to the number of parallel requests sent to an endpoint at the same time. Controlling concurrency is a core lever for balancing latency and [throughput](/concepts/provisioned-throughput.md) in production LLM applications. Databricks LLM serving endpoints process multiple concurrent requests simultaneously, and the endpoint’s autoscaling strategy dynamically adjusts resources to handle the offered load.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## How Concurrency Affects Performance

LLM inference proceeds in two stages: **prefill** (input tokens processed in parallel) and **decoding** (output tokens generated one at a time). Two key sub-metrics govern user-facing performance:

- **[Time to First Token](/concepts/time-to-first-token-ttft.md) (TTFT)** – how quickly the first output token appears after a query is submitted.
- **[Time per Output Token](/concepts/time-per-output-token-tpot.md) (TPOT)** – the time to generate each subsequent token.

Total request latency is `TTFT + (TPOT × number of output tokens)`. Endpoint throughput is the total number of output tokens per second across all concurrent requests.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

At low concurrency, each request enjoys minimal queuing and the lowest possible latency. As concurrency increases, the endpoint can process more requests in parallel, so throughput rises—two requests’ worth of tokens can be generated in less than double the time of a single request. However, latency also tends to increase because requests may wait for compute slots and because the model’s decoding step is inherently sequential per request.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Trade-Off: Low Latency vs. High Throughput

The number of parallel requests sent into the system is the primary control for managing the latency–throughput trade-off.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Low latency use cases** – real-time applications (e.g., chatbots, interactive assistants). These benefit from sending few concurrent requests to keep TTFT and total latency minimal.
- **High throughput use cases** – batch inference, offline processing. These can tolerate higher latency and send many concurrent requests to saturate the endpoint and maximize tokens per second.

Databricks recommends defining an acceptable latency budget for your application and then tuning concurrency to maximize throughput within that budget.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Autoscaling and Throughput Plateaus

Databricks LLM serving endpoints use an autoscaling strategy that balances latency and throughput by allocating compute capacity based on the incoming load. As more concurrent users query the endpoint, latency and throughput initially both increase. However, throughput eventually plateaus at a ceiling determined by the endpoint’s [Provisioned Throughput](/concepts/provisioned-throughput.md) capacity (measured in tokens per second). Once that ceiling is reached, additional concurrent requests simply queue, causing total latency to continue rising while throughput remains flat.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

This behavior is visible in throughput–latency curves produced by benchmarking. The plateau marks the point where the endpoint is fully utilized; further concurrency only adds queuing delay.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Benchmarking Concurrency

Databricks provides a benchmarking notebook that simulates different levels of concurrency and plots throughput versus latency. The notebook helps practitioners identify the concurrency level that optimally uses provisioned capacity without exceeding latency targets.^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

## Related Concepts

- LLM Inference
- [Provisioned Throughput](/concepts/provisioned-throughput.md)
- [Model Units](/concepts/model-units.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Time to First Token (TTFT)](/concepts/time-to-first-token-ttft.md)
- [Time per Output Token (TPOT)](/concepts/time-per-output-token-tpot.md)
- Autoscaling
- Endpoint Benchmarking

## Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
