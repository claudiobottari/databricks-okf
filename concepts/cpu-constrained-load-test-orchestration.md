---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a8e723dc02c6affd30f2f340817adfbb1564d4bdf605af09d92a990d7d2072d
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cpu-constrained-load-test-orchestration
    - CLTO
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: CPU-Constrained Load Test Orchestration
description: Locust's throughput is limited by CPU resources at roughly 4000 requests per second per core; the test notebook uses the --processes -1 flag to auto-detect and utilize all available CPU cores on the driver, and recommends CPU-optimized instances with at least 32 cores for the test cluster.
tags:
  - load-testing
  - infrastructure
  - performance
timestamp: "2026-06-18T14:42:54.608Z"
---

# CPU-Constrained Load Test Orchestration

**CPU-Constrained Load Test Orchestration** refers to the practice of designing and executing load tests where the CPU capacity of the test runner (typically the client machine or cluster) is the primary bottleneck, rather than the target serving endpoint. Proper orchestration ensures that the load generator can produce enough concurrent requests to stress the endpoint without itself being throttled by limited CPU resources. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## How Locust Uses CPU

In the context of [Model Serving](/concepts/model-serving.md) load testing, Locust is the recommended open-source framework. Locust’s worker processes consume CPU to maintain client connections, send requests, and collect metrics. Each CPU core can sustain approximately **4,000 requests per second (RPS)** on typical payloads. This relationship is linear: doubling the CPU cores roughly doubles the achievable client‑side RPS. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

When using the `--processes -1` flag, Locust automatically detects the number of CPU cores on the driver and spawns one worker per core. This maximizes throughput on multi‑core instances. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Configuring for CPU Constraints

### Instance Selection

A CPU‑optimized instance with **at least 32 cores** is recommended for running load tests. Instances with more cores can generate higher RPS, making it easier to saturate the target endpoint. For Databricks, a single‑node cluster with the 15.4 LTS ML runtime is a typical starting point. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Payload Considerations

The payload sent during the load test must be **representative of production traffic**. If the payload is large, each request consumes more CPU for serialization and transport, reducing the effective RPS per core. The input.json file used by Locust should reflect the expected production payload (e.g., one credit‑card transaction for a fraud‑detection model). ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Endpoint Pre‑Configuration

Before running a CPU‑constrained load test, the target endpoint should be configured with a fixed minimum and maximum concurrency (e.g., 4 for a “Small” endpoint), route optimization enabled, and scale‑to‑zero disabled. This ensures the endpoint does not throttle or autoscale unexpectedly during the test, isolating the client‑side CPU bottleneck. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Monitoring CPU Bottlenecks

During the load test, monitor the Locust output for messages indicating a CPU bottleneck. If Locust cannot keep up with the configured number of concurrent users because CPU is saturated, an explicit warning message appears. When this occurs, the measured latency percentiles reflect client‑side queuing, not true endpoint performance. To resolve, either reduce concurrency or scale the client cluster to a larger CPU‑optimized instance. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Recommendations

- **Start small:** Use a low concurrency setting (e.g., a few hundred simultaneous users) to validate the endpoint is online and responding. Then gradually increase concurrency while observing Locust’s CPU usage.
- **Scale the client vertically:** If CPU becomes the bottleneck, move to an instance with more cores. A single multi‑core driver is preferred over a distributed worker cluster because it simplifies coordination and avoids network overhead.
- **Validate endpoint capacity separately:** The load test should measure endpoint latency under different concurrency levels; the client must not be the limiting factor. Run a short 30‑second test first to confirm the endpoint responds before a full test.
- **Use the notebook’s recommendation step:** After a series of tests, the notebook provides a recommended endpoint size based on observed RPS and latency goals. Follow that recommendation and re‑test to confirm. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- Locust – Open‑source load testing framework used for evaluation.
- [Model Serving](/concepts/model-serving.md) – Serving machine learning models on Databricks.
- [Serving Endpoints](/concepts/serving-endpoint-acls.md) – Configuration and management of serving endpoints.
- GPU vs CPU Serving – Trade‑offs between GPU‑ and CPU‑based endpoints.
- Load Testing Best Practices – General guidance for endpoint load testing.
- CPU-Optimized Instances – Instance types recommended for load‑test drivers.

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
