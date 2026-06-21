---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e53fa740811b1bbc8440655c43a1d61ba673b357725c505f9f6f56b24d117c79
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-concurrency-scaling
    - MSECS
    - Endpoint Concurrency and Scaling
    - Endpoint concurrency and scale
    - Model Serving Concurrency
    - Serving Endpoint Concurrency
    - Serving endpoint concurrency
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Model Serving Endpoint Concurrency Scaling
description: The relationship between endpoint concurrency, client-side connections, and latency percentiles, where required concurrency scales linearly with concurrent connections for achieving target latency.
tags:
  - model-serving
  - scaling
  - performance
timestamp: "2026-06-19T09:22:18.547Z"
---

# Model Serving Endpoint Concurrency Scaling

**Model Serving Endpoint Concurrency Scaling** refers to the relationship between the number of concurrent client connections to a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) and the endpoint’s configured concurrency (the number of model replicas or workers available to process requests simultaneously). Understanding this scaling behavior is essential for sizing an endpoint to meet both throughput (queries per second, QPS) and latency requirements.

## Overview

The concurrency required to achieve a given latency percentile scales linearly with the number of concurrent client connections. Because of this linear relationship, you can run load tests on a small endpoint configuration (for example, concurrency of 4) and then calculate the final endpoint size needed to handle production traffic before performing a final validation test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## How Concurrency Scaling Works

Each concurrent client connection competes for endpoint capacity. As the number of simultaneous requests increases, queuing and processing delays can push latency upward. The endpoint’s concurrency setting determines how many requests it can process in parallel. The scaling is linear: doubling the number of concurrent connections roughly doubles the concurrency needed to maintain the same tail latency. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Determining Required Concurrency

The recommended workflow to find the right concurrency for a production endpoint is:

1. **Start with a small baseline endpoint.** Create a CPU endpoint with minimum and maximum concurrency both set to 4. Enable route optimization and disable scale-to-zero. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

2. **Run a series of load tests** with incrementally higher numbers of simulated client connections. Use the Locust open-source load-testing framework (as shown in the provided notebook example) to vary client concurrency while measuring endpoint latency percentiles. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

3. **Analyze the results.** After the series of tests, plot latency percentiles (e.g., p50, p95, p99) against client concurrency. The notebook presents a table of results. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

4. **Select the acceptable latency row** and input the application’s desired requests per second (RPS). The notebook then recommends the endpoint concurrency needed to meet both the latency target and the RPS goal. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

5. **Update the endpoint configuration** to match the recommendation, then run a final load test to confirm the endpoint meets both latency and throughput requirements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Load Test Procedure

The load test is a short (30-second) initial check to confirm the endpoint is online and responding, followed by the full series of tests with varying client concurrency. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Requirements

- A Databricks Service Principal with “Can Query” permission on the endpoint, used to generate OAuth tokens. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- A single-node cluster (15.4 LTS ML runtime) with at least 32 CPU cores. More cores allow higher request generation (roughly 4000 requests per second per CPU core). ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- An `input.json` file containing a representative payload: one that matches the size and structure of production requests. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Payload Consideration

The payload sent by Locust clients must be representative of actual production traffic. For example, if the model is a fraud-detection system that evaluates one transaction per request, the payload should include exactly one transaction. Test the payload by pasting it into the [Serving UI](/concepts/serving-ui.md)’s **Query** window before running the load test to ensure the endpoint responds correctly. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Best Practices

- **Start small.** Use an endpoint with concurrency 4 to discover headroom before scaling up. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- **Enable route optimization** and **disable scale-to-zero** during testing to keep behavior consistent. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- **Monitor Locust CPU usage.** If Locust is CPU-bottlenecked, an output message will appear; add CPU cores to the cluster if needed. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- **Choose a payload that matches production** in size and content to get valid latency and throughput measurements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- [Create custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md)
- [Load Testing](/concepts/locust-load-testing-framework.md)
- [Serving UI](/concepts/serving-ui.md)
- Locust
- Service Principal
- GPU Scheduling (for GPU endpoints)

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
