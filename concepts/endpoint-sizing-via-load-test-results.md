---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 16e46a6f4d69fa7aad0a8cc2fee370fad3f5c83072f07dce851811fccf6f65b6
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-sizing-via-load-test-results
    - ESVLTR
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Endpoint Sizing via Load Test Results
description: Methodology for calculating required endpoint concurrency from load test results by correlating client-side concurrency with latency percentiles and RPS targets to recommend final endpoint size.
tags:
  - sizing
  - concurrency
  - scaling
  - load-testing
timestamp: "2026-06-19T17:50:33.544Z"
---

# Endpoint Sizing via Load Test Results

**Endpoint Sizing via Load Test Results** is a methodology for determining the optimal concurrency configuration for a Databricks Model Serving endpoint based on empirical load testing. By running controlled load tests with varying client-side concurrency and measuring latency percentiles, you can calculate the endpoint size needed to meet specific requests per second (RPS) and latency requirements.

## Overview

The sizing process uses the Locust open-source load testing framework to simulate concurrent client connections against a serving endpoint. The key insight is that endpoint concurrency scales linearly with the number of concurrent connections, allowing you to test on a small endpoint and calculate the required size before performing a final validation test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Prerequisites

### Endpoint Configuration

The load test notebook assumes the model runs on a CPU model serving endpoint with the following configuration:

- Start with a "Small" CPU endpoint (endpoint concurrency of 4)
- Set both minimum and maximum concurrency to 4
- Enable route optimization
- Disable Scale to Zero

^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Service Principal Setup

To interact with the route-optimized endpoint, the Locust test must generate OAuth tokens with permissions to query the endpoint:

1. Create a Databricks Service Principal
2. Grant the Service Principal "Can Query" permissions on the Model Serving endpoint
3. Create a Databricks secret scope with two keys:
   - The service principal client ID
   - The service principal client secret

^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Payload Configuration

The `input.json` file specifies the payload sent by all concurrent connections. To ensure valid results, choose a payload that accurately represents production usage. For example, if your model processes one transaction per request, the payload should represent only one typical transaction. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Load Test Process

### Initial Validation

The notebook first runs a short 30-second load test to verify the endpoint is online and responding. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Series of Load Tests

You run a series of load tests with different amounts of client-side concurrency. After completion, the notebook:

- Prints any request failures or exceptions
- Creates a plot of latency percentiles against client concurrency
- Presents a table of results for selection

^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Sizing Calculation

From the results table, you select the row that best meets your latency requirements and input the application's desired RPS. The notebook then recommends how to size your endpoint to meet both RPS and latency goals. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Final Validation

After updating the Model Serving endpoint configuration to match the recommendations, you run a final load test to confirm the endpoint meets both latency and RPS requirements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Locust Framework Details

Locust is an open-source framework for load testing that standardizes and automates the approach. Key characteristics:

- Relies on CPU resources to run tests
- Facilitates approximately 4000 requests per second per CPU core (depending on payload)
- The `--processes -1` flag allows Locust to auto-detect and fully utilize all CPU cores on the driver

^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Cluster Configuration

The load test notebook has been tested with:

- Single node cluster
- 15.4 LTS ML runtime
- CPU-optimized instance with at least 32 cores (more cores can generate higher RPS)

^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – The endpoints being sized through load testing
- [Endpoint Concurrency](/concepts/endpoint-sizing-and-concurrency-planning.md) – The configuration parameter determined by load test results
- Route Optimization – A feature that must be enabled for the sizing methodology to work
- Service Principals – Required for authentication during load testing
- Latency Percentiles – Key metrics used to evaluate endpoint performance
- Requests Per Second (RPS) – The throughput target used in sizing calculations

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
