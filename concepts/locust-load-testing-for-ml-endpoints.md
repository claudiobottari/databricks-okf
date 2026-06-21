---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 23ff0aed528e89248145d13c8377ce06d2528bc61e1c9fd70a6cb888b853b283
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - locust-load-testing-for-ml-endpoints
    - LLTFME
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Locust Load Testing for ML Endpoints
description: Using the open-source Locust framework to run distributed load tests against Databricks Model Serving endpoints, configured to auto-detect CPU cores for maximum request throughput.
tags:
  - load-testing
  - model-serving
  - locust
timestamp: "2026-06-19T17:50:22.670Z"
---

# Locust Load Testing for ML Endpoints

**Locust Load Testing for ML Endpoints** is a methodology for evaluating the performance of [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoints using the open-source Locust framework. This approach standardizes and automates load testing to help optimize endpoint configuration for production workloads. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Overview

Locust is an open-source framework for load testing that is commonly used for evaluating production-grade endpoints. It allows you to modify various parameters — such as the number of client connections and how fast client connections spawn — while measuring endpoint performance throughout the test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

The load testing approach described here is designed for CPU model serving endpoints on Databricks. It uses a provided **Locust load test** notebook along with supporting files to run a series of tests and generate endpoint sizing recommendations. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Requirements

To configure a load test, you need to download and import the following files to your Databricks workspace: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- **input.json** — Specifies the payload sent by all concurrent connections to your endpoint. The payload should be representative of expected production usage.
- **fast-load-test.py** — A script used by the Locust load test notebook to validate authentication tokens and read the input.json file contents.

### Cluster Configuration

The Locust load test notebook has been tested with the following cluster configuration: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- Single node cluster
- 15.4 LTS ML runtime
- CPU-optimized instance with at least 32 cores (instances with more cores can generate higher requests per second)

## How Locust Works

Locust relies on CPU resources to run its tests. Depending on the payload, it facilitates roughly 4,000 requests per second per CPU core. In the Locust load test notebook, the `--processes -1` flag is set to allow Locust to auto-detect the number of CPU cores on your driver and fully utilize them. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

If Locust becomes bottlenecked by the CPU, an output message appears in the Locust output. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Setup

### Endpoint Configuration

The load test notebook assumes your model is running on a CPU model serving endpoint with the following configuration: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- Start with a "Small" CPU endpoint (endpoint concurrency of 4), with both minimum and maximum concurrency set to 4
- Route optimization enabled
- Scale to Zero disabled

### Service Principal Authentication

To interact with the route-optimized endpoint, the Locust test needs to generate OAuth tokens with permissions to query the endpoint. The setup involves: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. Create a Databricks Service Principal
2. Grant the service principal "Can Query" permissions on the Model Serving endpoint
3. Create a [Databricks secret scope](/concepts/databricks-secret-scopes.md) with two keys:
   - The service principal client ID
   - The service principal client secret
4. Store the client ID and client secret as [Databricks secrets](/concepts/databricks-secret-scopes.md)

### Payload Specification

The payload in `input.json` should accurately represent the type of payload you plan to send in production. For example, if your model is a fraud detection model evaluating one transaction per request, the payload should represent only one typical transaction. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

Before running the load test, test your payload by pasting the full `input.json` data into the **Query** window on your Databricks Model Serving endpoint to ensure the model responds with the desired outputs. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Running the Load Test

The load test notebook follows this workflow: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. **Initial validation** — Runs a very short 30-second duration load test to ensure the endpoint is online and responding
2. **Series of tests** — Runs multiple load tests with different amounts of client-side concurrency
3. **Results analysis** — Prints any request failures or exceptions, and creates a plot of latency percentiles against client concurrency
4. **Sizing recommendation** — Presents a table of results; you select the row that best meets your latency requirements and input the application's desired requests per second (RPS). The notebook recommends how to size your endpoint to meet both RPS and latency goals
5. **Final validation** — After updating the endpoint configuration to match the recommendation, runs a final load test to confirm the endpoint meets both latency and RPS requirements

## Scaling Relationship

The model serving endpoint concurrency needed to achieve a certain percentile of latency scales linearly with the number of concurrent connections. This means you can test on a small endpoint and calculate the size endpoint you need before performing a final test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The serving infrastructure being tested
- Endpoint Sizing and Optimization — Using load test results to configure endpoints
- Route Optimization — Feature that improves endpoint performance
- OAuth Token Authentication — Authentication method used by the load test
- Performance Testing Best Practices — General guidance for load testing ML systems

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
