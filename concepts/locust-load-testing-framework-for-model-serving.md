---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 432827cb970e00d4989728193b6482b9722f1b47193f0f68db231180dccb5721
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - locust-load-testing-framework-for-model-serving
    - LLTFFMS
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Locust Load Testing Framework for Model Serving
description: Using the open-source Locust framework to run automated, parameterized load tests against Databricks Model Serving endpoints, with support for custom concurrency, spawn rates, and CPU-aware parallel execution.
tags:
  - load-testing
  - locust
  - model-serving
timestamp: "2026-06-18T14:42:48.632Z"
---

<answer>---</answer>

# Locust Load Testing Framework for Model Serving

The **Locust Load Testing Framework for Model Serving** provides a standardized, automated approach to evaluating the performance of [Model Serving](/concepts/model-serving.md) endpoints on Databricks. It uses the open-source Locust library to simulate concurrent client connections, measure latency and throughput, and recommend endpoint sizing to meet production requirements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Overview

Locust is an open-source load-testing framework commonly used for evaluating production-grade HTTP endpoints. It allows testers to modify parameters such as the number of concurrent client connections and the connection spawn rate while measuring endpoint performance throughout the test. Locust is used for all example code in the Databricks load test notebook because it standardizes and automates the approach. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

Locust relies on CPU resources to execute tests. Depending on the payload size, it can sustain approximately 4,000 requests per second per CPU core. The example notebook uses the `--processes -1` flag to allow Locust to auto-detect the number of CPU cores on the driver node and fully utilize them. If Locust becomes bottlenecked by the CPU, an output message appears. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Requirements

Before running a load test, you must download and import the following files to your Databricks workspace:

- `input.json` – A file that specifies the payload sent by all concurrent connections to the endpoint. The payload must be representative of the expected production use case.
- `fast-load-test.py` – A script used by the **Locust load test** notebook to validate the authentication token and read the contents of `input.json`.

The example notebook has been tested with the following cluster configuration:

- Single node cluster
- Databricks Runtime 15.4 LTS ML
- A CPU-optimized instance with at least 32 cores (more cores can generate higher queries per second)

^^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Environment Setup

### Endpoint Configuration

The load test notebook assumes the model is deployed on a CPU-based Model Serving endpoint. When creating the endpoint using the Serving UI, configure the following:

- Start with a **Small** endpoint (concurrency of 4), setting both minimum and maximum concurrency to 4.
- Enable **Route optimization**.
- Disable **Scale to Zero**.

These settings provide a consistent baseline for testing. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Service Principal Authentication

To interact with the route-optimized endpoint, the Locust test must generate OAuth tokens with query permissions. Follow these steps:

1. Create a Databricks Service Principal.
2. Grant the service principal **Can Query** permission on the Model Serving endpoint.
3. Create a [Databricks Secret Scope](/concepts/databricks-secret-scopes.md) with two keys:
   - `service_principal_client_id` – the ID of the service principal.
   - `service_principal_client_secret` – the client secret of the service principal.
4. Store both values as Databricks Secrets in the scope.

^^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Payload Specification

Place a representative payload into the `input.json` file. To ensure valid results, the payload should mirror the real-world input the endpoint will serve in production. For example, a fraud-detection model that processes one transaction per request should have a payload containing exactly one typical transaction. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

Before running the load test, verify the payload by pasting the full `input.json` data into the **Query** window of the endpoint (accessible from the Serving UI → endpoint → dropdown next to **Use** → **Query**). Confirm that the model responds with the expected outputs. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Running the Load Test

After configuring the endpoint, notebooks, and payload, step through the notebook execution. The notebook first runs a short 30-second load test to confirm the endpoint is online and responding. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

You can then run a series of load tests with varying levels of client-side concurrency. After the series completes, the notebook prints any request failures or exceptions and generates a plot of latency percentiles against client concurrency. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Interpreting Results and Sizing Recommendations

The notebook presents a table of results. You must select the row that best meets your latency requirements and enter the desired requests per second (RPS). The notebook then calculates a recommended endpoint size (concurrency level) to achieve both the latency and throughput goals. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

The model serving endpoint concurrency needed to reach a given latency percentile scales linearly with the number of concurrent connections. This means you can test on a small endpoint first and compute the required size for the final test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

After updating the endpoint configuration to match the notebook’s recommendation, run the final load test to verify that the endpoint meets both latency and RPS requirements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Best Practices

- **Use a representative payload.** The payload size and content directly affect performance; test with data that matches production patterns.
- **Start small.** Begin with the recommended small endpoint configuration to estimate concurrency needs before scaling up.
- **Monitor CPU usage on the Locust driver.** If Locust reports a CPU bottleneck, consider using an instance with more cores.
- **Ensure proper authentication.** Use a service principal with Can Query permissions and store credentials securely in a secret scope.
- **Validate the endpoint response first.** Always test the payload manually before running automated load tests.

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- Locust
- Service Principal
- Databricks Secrets
- Serving Endpoint Sizing
- [Endpoint Concurrency](/concepts/endpoint-sizing-and-concurrency-planning.md)

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

<answer>---</answer>

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
