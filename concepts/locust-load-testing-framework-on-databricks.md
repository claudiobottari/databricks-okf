---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e7c0554d7d9fcbb56a78c42338aa76a0cea2e158e6be2662879bebbe97628cb3
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - locust-load-testing-framework-on-databricks
    - LLTFOD
    - locust-load-testing-framework-for-model-serving
    - LLTFFMS
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Locust Load Testing Framework on Databricks
description: Using the open-source Locust framework to run automated, configurable load tests against Databricks Model Serving endpoints, supporting parameter tuning for client connections, spawn rates, and multi-CPU utilization.
tags:
  - load-testing
  - model-serving
  - databricks
timestamp: "2026-06-19T09:22:16.509Z"
---

# Locust Load Testing Framework on Databricks

**Locust** is an open‑source load‑testing framework that Databricks recommends for evaluating production‑grade custom model serving endpoints. It allows engineers to modify parameters such as the number of concurrent client connections and the spawn rate, while measuring endpoint performance throughout the test. Locust standardises and automates the approach to load testing on Databricks. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Requirements

To use the provided example notebook and scripts, you must download and import three files into your Databricks workspace:

- **input.json** – specifies the payload that all concurrent connections send to the endpoint. The payload should be representative of real‑world usage (e.g., a single fraud‑detection transaction per request).
- **fast‑load‑test.py** – a helper script used by the Locust load‑test notebook to validate the authentication token and read `input.json`.
- **Locust load test notebook** – the main notebook that orchestrates the tests.

The notebook and scripts have been tested with a single‑node cluster running **15.4 LTS ML runtime** and a CPU‑optimised instance with at least 32 cores. Instances with more cores can generate higher queries per second (RPS). ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## How Locust Operates on Databricks

Locust relies on CPU resources to run its tests. Depending on the payload, it can sustain roughly **4 000 requests per second per CPU core**. The notebook sets the flag `--processes -1` so that Locust auto‑detects the number of CPU cores on the driver and fully utilises them. If Locust becomes CPU‑bottlenecked, an output message appears. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Environment Setup

### Endpoint Configuration

The notebook assumes the model serving endpoint is CPU‑based and was created with the following settings:

- Start with a **Small** endpoint (concurrency of 4) – both minimum and maximum concurrency set to 4.
- Route optimisation enabled.
- Scale‑to‑Zero disabled.

Because endpoint concurrency scales linearly with the number of concurrent connections, you can test on a small endpoint first and then calculate the required size for production. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Service Principal Authentication

To generate OAuth tokens that can query the endpoint, you need a Databricks service principal with **Can Query** permissions on the endpoint. Follow these steps:

1. Create a Databricks service principal.
2. Grant it “Can Query” permission on the serving endpoint.
3. Create a [Databricks secret scope](/concepts/databricks-secret-scopes.md).
4. Store the service principal’s client ID and client secret as secrets in that scope.

The notebook reads these secrets to authenticate. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Payload Specification

The `input.json` file must contain a payload that accurately represents what the endpoint will receive in production. Test the payload by pasting its contents into the **Query** window of your endpoint (accessible from the Serving UI → endpoint → Use → Query) to verify that the model returns the desired outputs. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Running the Load Test

After configuring the endpoint, service principal, and payload, execute the notebook step‑by‑step:

1. **Initial quick test** – a 30‑second load test verifies the endpoint is online and responding.
2. **Series of tests** – you can run multiple load tests with varying client‑side concurrency levels.
3. **Review failures** – cells print any request failures or exceptions that occurred during the tests.
4. **Latency analysis** – a plot of latency percentiles against client concurrency is generated.
5. **Size recommendation** – you select the row that best meets your latency requirements and input the desired RPS. The notebook then recommends how to size the endpoint (concurrency settings) to achieve both RPS and latency goals.
6. **Final validation** – after updating the endpoint configuration according to the recommendation, you run a final load test to confirm performance. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Interpreting Results

The notebook presents a table of results. You choose the row that satisfies your latency SLO. The notebook then uses that selection together with the target RPS to compute the recommended concurrency scale. After applying the new configuration, the final test validates that the endpoint meets both latency and throughput requirements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md)
- Databricks service principal
- OAuth token generation for model serving
- [Serving endpoint concurrency](/concepts/model-serving-endpoint-concurrency-scaling.md)
- [Route optimisation for serving endpoints](/concepts/route-optimization-for-serving-endpoints.md)

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
