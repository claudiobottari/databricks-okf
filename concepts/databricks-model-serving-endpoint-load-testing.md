---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: de120e540128f95f6cb3875e1204ade6952be9b65786bcf4dab3257e54ea8df7
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-model-serving-endpoint-load-testing
    - DMSELT
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Databricks Model Serving Endpoint Load Testing
description: Process of configuring and running load tests on Databricks Model Serving endpoints to optimize performance, latency, and throughput
tags:
  - databricks
  - model-serving
  - load-testing
timestamp: "2026-06-18T11:07:09.587Z"
---

# Databricks Model Serving Endpoint Load Testing

**Databricks Model Serving Endpoint Load Testing** is the process of evaluating the performance of a custom model serving endpoint under controlled concurrent traffic using the Locust framework. This page describes how to set up, configure, and run a load test with the provided example notebook and supporting files. The goal is to determine the endpoint size needed to meet your latency and requests-per-second (RPS) requirements before moving to production. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Requirements

To run a load test, download the following files into your Databricks workspace:

- **input.json** – defines the payload sent by each concurrent connection. The payload must be representative of production traffic.
- **fast-load-test.py** – helper script used by the Locust load test notebook to validate the authentication token and read the payload.

The example notebook and files have been tested with a single-node cluster running the **15.4 LTS ML runtime** and a CPU-optimized instance with at least **32 cores**. Instances with more cores can generate higher query rates. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Locust Framework

[Locust](https://locust.io/) is an open-source load-testing framework. It allows you to vary parameters such as the number of client connections and the spawn rate while monitoring endpoint performance. The provided notebook uses Locust with the `--processes -1` flag, which auto-detects CPU cores on the driver to maximize throughput. Locust can sustain roughly **4,000 requests per second per CPU core**, depending on payload. If Locust becomes CPU-bound, a warning message appears in the output. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Environment Setup

Perform the following steps outside the notebook before running the load test.

### Endpoint Configuration

The load test assumes your model is deployed on a CPU-serving endpoint. When creating the endpoint in the [Serving UI](/concepts/serving-ui.md):

- Start with a **Small** endpoint (concurrency of 4).
- Set both **minimum** and **maximum concurrency** to 4.
- Enable **Route optimization**.
- Disable **Scale to Zero**.

The concurrency needed for a target latency scales linearly with the number of concurrent connections. This means you can load-test a small endpoint first and then calculate the production endpoint size. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Service Principal Authentication

The load test must generate OAuth tokens to query the route-optimized endpoint. Follow these steps:

1. Create a Databricks Service Principal.
2. In the Model Serving endpoint’s **Permissions** tab, grant the service principal **Can Query** permissions.
3. Create a [Databricks secret scope](/concepts/databricks-secret-scopes.md) and store two keys:
   - `service_principal_client_id` – the ID of the service principal.
   - `service_principal_client_secret` – the client secret of the service principal.

The notebook reads these secrets to authenticate without hard‑coding credentials. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Notebook Setup

After importing the notebook into your workspace, configure the following parameters:

### Specify a Payload

Edit the `input.json` file to contain a single representative request. For example, if your model processes one credit‑card transaction per request, the payload should contain exactly one transaction. A payload that is too large or too small will skew latency measurements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Test the Payload

Before running the load test, verify that the payload works:

1. In the **Serving UI**, select your endpoint.
2. Click the dropdown next to the **Use** button and choose **Query**.
3. Paste the full contents of `input.json` and confirm the model returns the expected output.

If the payload is valid, the load test results will be meaningful. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Running the Load Test

Once the endpoint, notebooks, and payload are ready, execute the notebook cells in order.

1. **Short validation test** – A 30‑second test that verifies the endpoint is online and responding.
2. **Series of load tests** – The notebook runs multiple tests with different client‑side concurrency levels. After this series, it displays a table of results, request failures, and a plot of latency percentiles versus concurrency.
3. **Select a row** – From the results table, choose the row that meets your latency requirements, and enter your application’s desired RPS.
4. **Endpoint sizing recommendation** – The notebook calculates the endpoint concurrency needed to satisfy both the RPS and latency goals.
5. **Verification test** – After updating the endpoint’s min/max concurrency to match the recommendation, run the final load test to confirm performance.

The entire workflow is designed to be iterative: you start with a small endpoint, determine the required size, resize, and validate. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Summary

Databricks Model Serving Endpoint Load Testing, using Locust and the provided notebook, provides a systematic way to size a serving endpoint for production. By controlling concurrency, payload representativeness, and authentication, you can obtain reliable latency and throughput measurements and make data‑driven infrastructure decisions.

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
