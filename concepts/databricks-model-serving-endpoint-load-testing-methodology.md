---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5aaecab40b4a8ae52dd119754b0544b991585696fd1806a8e527df8fa38f9d17
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-model-serving-endpoint-load-testing-methodology
    - DMSELTM
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Databricks Model Serving Endpoint Load Testing Methodology
description: A step-by-step process for configuring, running, and analyzing load tests on Databricks custom model serving endpoints using Locust.
tags:
  - databricks
  - machine-learning
  - load-testing
  - model-serving
timestamp: "2026-06-19T14:23:56.855Z"
---

# Databricks Model Serving Endpoint Load Testing Methodology

**Databricks Model Serving Endpoint Load Testing Methodology** refers to the standardized process of evaluating custom model serving endpoint performance under controlled load conditions. This methodology uses Locust as the load testing framework to determine the optimal endpoint sizing required to meet specific latency and requests-per-second (RPS) requirements.

## Overview

Load testing for Databricks Model Serving endpoints helps practitioners determine the appropriate endpoint configuration—specifically concurrency settings—needed to achieve production performance targets. The recommended approach uses a small starting endpoint and scales proportionally based on test results, eliminating the need for large initial deployments. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

The key insight is that the model serving endpoint concurrency needed to achieve a certain latency percentile scales linearly with the number of concurrent connections. This allows testing on a small endpoint and calculating the required size before performing a final validation test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Framework: Locust

Locust is an open-source framework for load testing that standardizes and automates the evaluation of production-grade endpoints. The framework allows modification of various parameters—including the number of client connections and connection spawn rate—while measuring endpoint performance throughout the test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Performance Characteristics

Locust relies on CPU resources to run its tests. Depending on payload complexity, it facilitates roughly 4,000 requests per second per CPU core. In the load test notebook, the `--processes -1` flag is set to allow Locust to auto-detect the number of CPU cores on the driver and fully utilize them. If Locust becomes CPU-bottlenecked, an output message appears. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Requirements

### Files

The methodology requires downloading and importing the following files to the Databricks workspace:

- **input.json** — Specifies the payload sent by all concurrent connections to the endpoint.
- **fast-load-test.py** — Script used by the Locust load test notebook to validate authentication tokens and read the input.json file contents.

^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Cluster Configuration

The load test notebook has been tested with the following cluster configuration:

- Single node cluster
- 15.4 LTS ML runtime
- CPU-optimized instance with at least 32 cores. Instances with more cores can generate higher RPS.

^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Initial Endpoint Configuration

Before running the load test, the serving endpoint should be configured with specific baseline settings:

- Start with a "Small" CPU endpoint with both minimum and maximum concurrency set to 4
- Route optimization enabled
- Scale to Zero disabled

^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Authentication Setup

To interact with the route-optimized endpoint, the Locust test must generate OAuth tokens with permission to query the endpoint. The setup involves:

1. Creating a Databricks Service Principal
2. Granting the service principal "Can Query" permissions on the serving endpoint
3. Creating a Databricks secret scope with:
   - The service principal client ID (key: `service_principal_client_id`)
   - The service principal client secret (key: `service_principal_client_secret`)
4. Storing the client ID and client secret as [Databricks secrets](/concepts/databricks-secret-scopes.md)

^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Payload Specification

The `input.json` file specifies the payload sent by all concurrent connections. To ensure valid load test results, the payload must accurately represent the type of payload expected in production. For example, if the model is a fraud detection model evaluating one transaction per request, the payload should represent only one typical transaction. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Payload Validation

Before running the load test, the payload should be tested by copying and pasting the full `input.json` data into the **Query** window on the Databricks Model Serving endpoint. To open the Query box:

1. Navigate to the **Serving UI** in the Databricks workspace
2. Select the endpoint to test
3. Click the dropdown menu next to the **Use** button (top right)
4. Select **Query**

^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Load Test Procedure

### Step 1: Initial Validation

The notebook first runs a very short 30-second duration load test against the endpoint to ensure it is online and responding. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Step 2: Series of Load Tests

A series of load tests is executed with different amounts of client-side concurrency. After completing the series, the notebook:
- Prints any request failures or exceptions
- Creates a plot of latency percentiles against client concurrency

^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Step 3: Endpoint Sizing Recommendation

The notebook presents a table of results. The user selects the row that best meets their latency requirements and inputs the application's desired RPS. The notebook then responds with a recommendation for how to size the endpoint to meet both RPS and latency goals. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Step 4: Final Validation

After updating the Model Serving endpoint configuration to match the notebook's recommendations, the final load test is run to ensure the endpoint meets both latency and RPS requirements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — The endpoints being load tested
- [Serving Endpoint Concurrency](/concepts/model-serving-endpoint-concurrency-scaling.md) — The primary configuration variable adjusted based on test results
- [Endpoint Route Optimization](/concepts/limitations-of-route-optimization.md) — A recommended setting that enables efficient request routing
- OAuth Token Generation for Model Serving — Authentication method required for load testing
- Service Principals in Databricks — Identity used for programmatic endpoint access
- [Locust Load Testing Framework](/concepts/locust-load-testing-framework.md) — The open-source tool used for test execution
- [What is Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) — Conceptual overview of load testing on Databricks

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
