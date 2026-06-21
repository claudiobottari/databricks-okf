---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43a2feda0945851bc5dae93d5b7ea72c7a861854ff5eef7c2fbf0f161715afc6
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - route-optimized-endpoint-configuration-for-load-testing
    - RECFLT
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Route-Optimized Endpoint Configuration for Load Testing
description: "Prerequisite configuration for Databricks Model Serving endpoints under test: start with a Small CPU endpoint (min/max concurrency=4), enable route optimization, and disable scale-to-zero to ensure consistent baseline measurements."
tags:
  - model-serving
  - configuration
timestamp: "2026-06-18T14:42:48.175Z"
---

# Route-Optimized Endpoint Configuration for Load Testing

**Route-Optimized Endpoint Configuration for Load Testing** refers to the specific endpoint settings and infrastructure setup required to properly evaluate the performance of a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) under load using tools like Locust. Route optimization is a key feature that must be enabled on the endpoint before conducting load tests to ensure accurate results.

## Overview

When configuring a load test for a custom model serving endpoint on Databricks, the endpoint must be set up with specific parameters to ensure the test produces meaningful results. Route optimization is one of the critical configuration options that must be enabled. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Endpoint Configuration Requirements

### Initial Endpoint Setup

The load test notebook assumes the model is running on a CPU model serving endpoint. When creating the endpoint using the Serving UI, the following configuration is recommended: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- Start with a **"Small"** CPU endpoint with an endpoint concurrency of **4**
- Set both the **minimum and maximum concurrency** to **4**
- **Enable route optimization**
- **Disable Scale to Zero**

### Why Route Optimization Matters

Route optimization is a feature that improves how requests are distributed across the endpoint's compute resources. Enabling it ensures that the load test accurately reflects how the endpoint will perform under production traffic patterns. Without route optimization enabled, the load test results may not represent real-world performance characteristics. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Scaling Relationship

The model serving endpoint concurrency needed to achieve a certain percentile of latency scales linearly with the number of concurrent connections. This linear relationship allows you to test on a small endpoint (such as the recommended "Small" configuration with concurrency of 4) and calculate the size endpoint you need before performing a final validation test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Load Test Workflow

### 1. Configure the Endpoint

Create or update your serving endpoint with route optimization enabled, a fixed concurrency of 4, and Scale to Zero disabled. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 2. Set Up Authentication

To interact with the route-optimized endpoint, the load test must generate OAuth tokens with query permissions. This requires: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. Creating a Databricks Service Principal
2. Granting the service principal **"Can Query"** permissions on the endpoint
3. Creating a [Databricks secret scope](/concepts/databricks-secret-scopes.md) with the service principal's client ID and client secret

### 3. Run Initial Tests

The load test notebook runs a short 30-second duration test to verify the endpoint is online and responding. After this validation, a series of tests with different client-side concurrency levels are executed. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### 4. Analyze Results and Resize

The notebook produces a table of latency percentiles against client concurrency. Based on your latency requirements and desired requests per second (RPS), the notebook recommends how to size the endpoint. After updating the endpoint configuration to match the recommendation, a final load test confirms the endpoint meets both latency and RPS requirements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) — Overview of load testing concepts and methodology
- Locust — The open-source load testing framework used in the example notebook
- [Model Serving Endpoint Configuration](/concepts/model-serving-endpoint-configuration-api.md) — General endpoint setup and management
- Service Principal Authentication — OAuth token generation for endpoint access
- [Endpoint Concurrency and Scaling](/concepts/model-serving-endpoint-concurrency-scaling.md) — Understanding how concurrency affects performance

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
