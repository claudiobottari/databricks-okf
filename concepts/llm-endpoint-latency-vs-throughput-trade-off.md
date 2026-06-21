---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a94637c390378cb991c7c5188e053c9bbd92e83a183a1cc7323ab062d19c2b0c
  pageDirectory: concepts
  sources:
    - conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-endpoint-latency-vs-throughput-trade-off
    - LELVTT
    - Endpoint Latency and Throughput
  citations:
    - file: conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md
title: LLM Endpoint Latency vs Throughput Trade-off
description: The balancing act in LLM serving systems where increasing concurrent requests raises throughput at the cost of higher latency, controlled by managing parallel request load.
tags:
  - llm-serving
  - performance
  - optimization
timestamp: "2026-06-18T14:42:17.958Z"
---

## LLM Endpoint Latency vs Throughput Trade-off

**LLM Endpoint Latency vs Throughput Trade-off** refers to the balancing act between how quickly a single user receives a response (latency) and how many output tokens the system can generate overall per second (throughput) when serving large language model (LLM) inference requests. On Databricks, provisioned throughput endpoints are designed to scale with concurrent requests, but there is an inherent trade-off: increasing concurrency raises throughput at the cost of higher latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### LLM Inference Phases

LLM inference proceeds in two steps: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

1. **Prefill** – The tokens in the input prompt are processed in parallel.
2. **Decoding** – Text is generated one token at a time in an auto-regressive manner. Each generated token is appended to the input and fed back into the model to generate the next token. Generation stops when a special stop token or a user-defined condition is met.

The number of input tokens significantly impacts the required memory to process requests, while the number of output tokens dominates overall response latency. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Key Metrics

Databricks divides LLM inference into two sub-metrics: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Time to First Token (TTFT)** – How quickly users start seeing the model's output after entering their query. Low TTFT is essential for real-time interactions but less important for offline workloads. It is driven by the time required to process the prompt and generate the first output token.
- **Time per Output Token (TPOT)** – The time to generate an output token for each user querying the system. This metric corresponds to how each user perceives the "speed" of the model. For example, a TPOT of 100 ms per token equals 10 tokens per second, or roughly 450 words per minute (faster than typical reading speed).

Based on these components, total latency and throughput are defined as: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Latency** = TTFT + (TPOT × number of tokens to be generated)
- **Throughput** = number of output tokens per second across all concurrent requests

### The Trade-off

LLM serving endpoints on Databricks can scale to match the load sent by clients with multiple concurrent requests. At low concurrency, latency is at its lowest possible level. However, if you increase the request load, latency tends to rise, but throughput also tends to increase because two requests' worth of tokens per second can be processed in less than double the time. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

Controlling the number of parallel requests into the system is core to balancing latency with throughput: ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

- **Low-latency use cases** (e.g., real-time applications that require immediate responses) benefit from sending fewer concurrent requests to keep latency low.
- **High-throughput use cases** (e.g., batch inferences and other non-user-facing tasks) saturate the endpoint with many concurrent requests, accepting higher latency in exchange for higher throughput.

### Provisioned Throughput and the Plateau

The provisioned throughput for an endpoint limits the number of workers and parallel requests that can be made. As the number of parallel requests increases, throughput begins to plateau, reaching a limit (e.g., about 8,000 tokens per second in the benchmarking example). Beyond this point, additional requests wait in a queue, causing total latency to continue increasing while throughput no longer improves. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Benchmarking the Trade-off

Databricks provides a benchmarking harness (example notebook) that displays total latency across all requests and throughput metrics, and plots the throughput versus latency curve across different numbers of parallel requests. The notebook helps observe how latency and throughput increase together as concurrency rises, and where throughput plateaus due to endpoint capacity limits. ^[conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md]

### Related Concepts

- [Provisioned Throughput](/concepts/provisioned-throughput.md) – The inference capacity model (tokens per second or model units) that determines the maximum throughput of an endpoint.
- [Model Units](/concepts/model-units.md) – An alternative provisioning model for certain models (e.g., Mixtral, DeepSeek R1).
- [Time to First Token (TTFT)](/concepts/time-to-first-token-ttft.md) – The first component of end‑to‑end latency.
- [Time per Output Token (TPOT)](/concepts/time-per-output-token-tpot.md) – The per‑token generation speed perceived by a single user.
- Autoscaling – The mechanism that allows endpoints to add workers in response to concurrency.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – The service layer through which provisioned throughput endpoints are accessed.
- [LLM Inference Performance Engineering](/concepts/llm-inference-prefill-and-decoding.md) – Broader best practices for optimizing inference throughput and latency.

### Sources

- conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md

# Citations

1. [conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws.md](/references/conduct-your-own-llm-endpoint-benchmarking-databricks-on-aws-bf37642a.md)
