---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d8b12f19c2c71c2d896e18756575fc41c7b71cfb02886b7cfdf2930226033ac
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-configuration-for-performance-testing
    - MSECFPT
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Model Serving Endpoint Configuration for Performance Testing
description: Recommended Databricks endpoint configuration settings including CPU instance type, concurrency levels, route optimization, and scale-to-zero settings for load testing.
tags:
  - databricks
  - configuration
  - model-serving
  - optimization
timestamp: "2026-06-19T14:24:02.891Z"
---

# Model Serving Endpoint Configuration for Performance Testing

**Model Serving Endpoint Configuration for Performance Testing** refers to the recommended settings and procedures for preparing a Databricks custom model serving endpoint so that load tests yield reliable latency and throughput benchmarks. Proper configuration ensures that test results can be used to size endpoints for production traffic.

## Overview

Load testing helps validate that a serving endpoint meets requests per second (RPS) and latency targets under realistic concurrency. The process relies on the Locust framework to simulate multiple client connections, measure performance, and produce a recommendation for endpoint sizing. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Endpoint Configuration

Before running a load test, the endpoint must be configured with specific settings to obtain repeatable results. The load test notebook assumes a **CPU model serving endpoint** with the following settings: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- Start with a **Small** endpoint (concurrency of 4).
- Set both **minimum and maximum concurrency** to 4.
- Enable **Route optimization**.
- Disable **Scale to zero**.

Route optimization is essential because the load test generates OAuth tokens to interact with the endpoint. Without route optimization, token‑based authentication may not work correctly. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Service Principal Setup

To authenticate with the route‑optimized endpoint, the load test uses a Service Principal and OAuth tokens. The following steps prepare authentication: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. Create a Databricks service principal.
2. Give the service principal **Can Query** permission on the serving endpoint.
3. Create a Databricks secret scope and store two secrets:
   - The service principal’s client ID (e.g., `service_principal_client_id`).
   - The service principal’s client secret (e.g., `service_principal_client_secret`).

## Payload Considerations

The payload sent by Locust during the test must be representative of production traffic. Provide a realistic input in the `input.json` file. For example, if the model processes one transaction per request, the payload should contain exactly one typical transaction. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Testing the Payload

Before running the load test, validate the payload by pasting the full `input.json` into the endpoint’s **Query** window in the Serving UI. Confirm that the model returns the expected output. To open the Query window: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. Navigate to the **Serving UI**.
2. Select the endpoint.
3. Click the dropdown next to the **Use** button and choose **Query**.

## Locust Load Test Framework

Locust is an open‑source load testing tool used in the provided notebook. It measures endpoint performance while varying the number of concurrent clients and spawn rate. Locust uses CPU resources; roughly 4000 requests per second per CPU core can be achieved depending on payload size. The notebook sets `--processes -1` so that Locust automatically uses all available cores on the driver. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Running the Load Test

The notebook runs a short 30‑second initial test to confirm the endpoint is online and responding. After that, a series of tests with different client‑side concurrency values is executed. The notebook prints any request failures or exceptions and produces a plot of latency percentiles versus concurrency. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Results and Scaling Recommendations

After completing the test series, a table of results appears. The user selects the row that best meets their latency requirements and inputs the desired RPS. The notebook then calculates a recommended endpoint size (concurrency) to meet those targets. After updating the endpoint configuration accordingly, a final load test can be run to verify that the latency and RPS goals are satisfied. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

Because endpoint concurrency scales linearly with the number of concurrent connections, testing on a small endpoint (concurrency 4) and then scaling up the computed concurrency is a valid approach. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- Locust – The open‑source load testing framework used in the notebook.
- Service Principal – Authentication identity for programmatic access.
- OAuth tokens – Token‑based authentication used with route‑optimized endpoints.
- [Model Serving Concurrency](/concepts/model-serving-endpoint-concurrency-scaling.md) – Relationship between concurrent connections and endpoint throughput.
- Route Optimization – Setting that enables token‑based authentication and improved routing.

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
