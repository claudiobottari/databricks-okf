---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a5d14798576e6f0ec28c340ee15dcac51fbfc1517dd7defad4b1f9eaf3ff4768
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - endpoint-sizing-and-concurrency-planning
    - Concurrency Planning and Endpoint Sizing
    - ESACP
    - Endpoint Concurrency
    - endpoint concurrency
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Endpoint Sizing and Concurrency Planning
description: Methodology for testing on small endpoints and scaling up based on linear relationships between concurrency, latency, and RPS to determine production endpoint size.
tags:
  - capacity-planning
  - scaling
  - performance
  - latency
timestamp: "2026-06-19T14:23:59.329Z"
---

# Endpoint Sizing and Concurrency Planning

**Endpoint Sizing and Concurrency Planning** is the process of determining the appropriate number of concurrent connections and the corresponding endpoint configuration (e.g., [Model Serving on Databricks](/concepts/model-serving-on-databricks.md)) needed to meet target latency and requests-per-second (RPS) requirements. It relies on load testing with representative payloads and systematically scaling endpoint concurrency to find the optimal balance between performance and cost.

## Overview

The fundamental principle behind endpoint sizing is that the concurrency required to achieve a particular latency percentile scales linearly with the number of concurrent client connections. This means you can start with a small endpoint—for example, a “Small” endpoint with a minimum and maximum concurrency of 4—and calculate the larger endpoint size needed before performing a final test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

By running a series of controlled load tests at different client‑side concurrency levels, you can measure how latency percentiles change and then select the concurrency level that best meets your service‑level objectives (SLOs). The results are used to produce a recommendation for the endpoint’s concurrency setting. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Methodology

### 1. Configure a Baseline Endpoint

Create a CPU Model Serving endpoint with the following initial settings (via the Serving UI):

- **Size:** Small (concurrency of 4)
- **Minimum and maximum concurrency:** 4
- **Route optimization:** Enabled
- **Scale to zero:** Disabled

These settings provide a predictable baseline for load testing. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 2. Prepare a Representative Payload

The payload sent by the load test must be representative of real production usage. For instance, if your model processes one transaction per request, the payload should contain exactly one typical transaction. Using a non‑representative payload will invalidate the latency results. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

Before running the full test, verify that the payload produces the expected outputs by using the **Query** window on the endpoint page. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 3. Set Up Authentication

To interact with the endpoint, the load test must generate OAuth tokens. The recommended approach is to:

1. Create a Databricks Service Principal.
2. Grant the service principal **Can Query** permission on the endpoint.
3. Store the client ID and client secret in a [Databricks Secret Scope](/concepts/databricks-secret-scopes.md).
4. Reference those secrets in the load test notebook. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 4. Run a Series of Load Tests

Using Locust (an open‑source load testing framework), the notebook runs short 30‑second tests at increasing client concurrency levels. Locust is configured with the `--processes -1` flag to auto‑detect CPU cores and maximize throughput. Each test measures latency percentiles and records any request failures. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 5. Select the Optimal Row

After gathering test results, you are presented with a table of concurrency levels and corresponding latency percentiles. Choose the row that best meets your latency requirements. Then, input your desired RPS. The notebook calculates and returns a recommendation for how to size the endpoint (i.e., the concurrency setting) to achieve both your RPS and latency goals. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 6. Validate the New Configuration

Update the endpoint configuration to match the recommended concurrency, then run a final load test to confirm that the endpoint meets the target latency and RPS. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Key Considerations

- **Payload size matters.** If your endpoint is sensitive to payload size, the load test must use a payload that mirrors production usage. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- **CPU resources on the test client.** Locust generates roughly 4000 requests per second per CPU core. Use a cluster with at least 32 CPU cores to achieve sufficient test throughput. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- **Route optimization and scale‑to‑zero.** Route optimization should be enabled for predictable scaling, and scale‑to‑zero should be disabled to avoid cold‑start delays during testing. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- **Linear scalability.** Because the required endpoint concurrency scales linearly with client concurrency, testing on a small endpoint and extrapolating to a larger one is a valid approach. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md)
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md)
- Locust
- Service Principal Authentication for Model Serving
- [Route Optimization for Model Serving](/concepts/route-optimization-for-model-serving.md)
- Latency Percentile SLOs

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
