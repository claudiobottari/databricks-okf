---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 887c33cc28f5b14eddf19f45208cb8b15667b409659cf9d931d718db73bdce01
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
    - load-testing-for-serving-endpoints-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - locust-load-testing-framework
    - LLTF
    - load testing framework
    - Load Testing
    - Locust Framework
    - Locust framework
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Locust Load Testing Framework
description: An open-source framework for load testing production-grade endpoints, capable of modifying connection count and spawn rate while measuring endpoint performance.
tags:
  - load-testing
  - open-source
  - performance
timestamp: "2026-06-19T14:23:03.453Z"
---

# Locust Load Testing Framework

**Locust** is an open-source, Python-based load testing framework used for evaluating production-grade endpoints, including [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoints. It allows you to modify various parameters — such as the number of client connections and how fast client connections spawn — while measuring endpoint performance throughout the test.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Overview

Locust standardizes and automates the approach to load testing by providing a programmable framework where test behavior is defined in Python code. It is used in Databricks to validate that custom model serving endpoints meet latency and throughput requirements before production deployment.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Performance Characteristics

Locust relies on CPU resources to run its tests. Depending on the payload, it facilitates roughly 4000 requests per second per CPU core. In the Databricks Locust load test notebook, the `--processes -1` flag is set to allow Locust to auto-detect the number of CPU cores on the driver and fully utilize them. If Locust is being bottlenecked by the CPU, an output message appears.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Setup Requirements

### Cluster Configuration

The Locust load test notebook has been tested with the following cluster configuration:^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- Single node cluster
- 15.4 LTS ML runtime
- A CPU-optimized instance with at least 32 cores. Instances with more cores can generate higher queries or requests per second (RPS).

### Required Files

To run a load test, download and import the following files to your Databricks workspace:^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- `input.json` — Specifies the payload sent by all concurrent connections to the endpoint.
- `fast-load-test.py` — A script used by the Locust load test notebook to validate the authentication token and read the `input.json` file contents.

### Endpoint Configuration

The Locust load test notebook assumes the model is running on a CPU model serving endpoint. Recommended configuration when creating the serving endpoint:^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- Start with a “Small” (endpoint concurrency of 4) CPU endpoint with both minimum and maximum concurrency set to 4.
- Route optimization is enabled.
- Scale to Zero is disabled.

### Service Principal Authentication

To interact with the route-optimized endpoint, the Locust test must generate OAuth tokens with permissions to query the endpoint. The setup process involves:^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. Create a Databricks Service Principal.
2. Grant the service principal “Can Query” permissions on the Model Serving endpoint.
3. Create a [Databricks secret scope](/concepts/databricks-secret-scopes.md) with two keys: the service principal client ID and client secret.
4. Store the client ID and client secret in [Databricks secrets](/concepts/databricks-secret-scopes.md).

## Payload Configuration

### Specifying a Payload

The payload is specified in the `input.json` file. To ensure valid load test results, choose a payload that accurately represents the type of payload planned for production. For example, if the model is a fraud detection model evaluating one transaction per request, the payload should represent only one typical transaction.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Testing the Payload

Test the payload by copying and pasting the full `input.json` data into the **Query** window on the Databricks Model Serving endpoint to ensure the model responds with the desired outputs. To open the Query box:^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. Navigate to the **Serving UI** in your Databricks workspace.
2. Select the endpoint you want to use for load testing.
3. In the top rightmost corner, select the dropdown menu next to the **Use** button.
4. Select **Query**.

## Running the Load Test

### Initial Validation

The notebook first runs a very short 30-second duration load test against the endpoint to ensure the endpoint is online and responding.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Series of Tests

You can run a series of load tests with different amounts of client-side concurrency. After completing the series, the notebook:^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- Prints the content of any request failures or exceptions.
- Creates a plot of latency percentiles against client concurrency.

### Sizing Recommendation

The notebook presents a table of results. You select the row that best meets your latency requirements and input the application’s desired requests per second (RPS). The notebook then recommends how to size the endpoint to meet both RPS and latency goals. After updating the endpoint configuration to match the recommendations, you can run a final load test to confirm the endpoint meets requirements.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Scalability Considerations

The model serving endpoint concurrency needed to achieve a certain percentile of latency scales linearly with the number of concurrent connections. This means you can test on a small endpoint and calculate the required endpoint size before performing a final test.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Databricks Model Serving](/concepts/databricks-model-serving.md) — The serving infrastructure that Locust tests
- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) — Overview of load testing concepts
- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — Creating and managing serving endpoints
- Databricks Service Principal — Authentication for automated testing
- Databricks Secrets — Secure storage for authentication credentials
- OAuth Tokens — Token-based authentication for API access

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
