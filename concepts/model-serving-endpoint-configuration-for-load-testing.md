---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 34054fae8c41bb33fd87b5162457299ab663a350725b9cc50712c8ab305219a3
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-configuration-for-load-testing
    - MSECFLT
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Model Serving Endpoint Configuration for Load Testing
description: "Recommended endpoint configuration for load testing: start with a Small CPU endpoint with min/max concurrency of 4, enable route optimization, and disable scale-to-zero."
tags:
  - model-serving
  - endpoint-configuration
  - load-testing
timestamp: "2026-06-19T17:50:19.042Z"
---

# Model Serving Endpoint Configuration for Load Testing

**Model Serving Endpoint Configuration for Load Testing** refers to the setup and configuration of [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) on Databricks to evaluate endpoint performance under simulated production traffic. Proper configuration ensures that load test results accurately reflect how an endpoint will perform in production. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Overview

Load testing a model serving endpoint involves configuring the endpoint with specific settings, preparing a representative payload, and using tools like Locust to simulate concurrent client connections. The test results inform decisions about endpoint sizing, concurrency, and latency requirements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Endpoint Configuration Requirements

For valid load testing results, the endpoint should be configured with specific settings when created using the [Serving UI](/concepts/serving-ui.md): ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- **Initial size**: Start with a "Small" CPU endpoint that has a minimum and maximum concurrency of 4. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- **Route optimization**: This feature must be enabled. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- **Scale to Zero**: This feature must be disabled. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

The model serving endpoint concurrency required to achieve a certain percentile of latency scales linearly with the number of concurrent connections. This property allows testing on a small endpoint and calculating the needed production endpoint size before performing a final validation test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Payload Specification

A representative payload is critical for load test validity. The payload must be specified in an `input.json` file that accompanies the load test notebook. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

Choose a payload that accurately represents the type of payload expected in production. For example, if a fraud detection model will evaluate one transaction per request in production, the test payload should represent only one typical transaction. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Testing the Payload

Before running the load test, verify the payload by pasting the full `input.json` data into the **Query** window on the Databricks Model Serving endpoint: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. Navigate to the **Serving UI** in the Databricks workspace.
2. Select the endpoint for load testing.
3. In the top right corner, select the dropdown menu next to the **Use** button.
4. Select **Query**.

Confirm that the model responds with the desired outputs. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Authentication and Service Principal Setup

To interact with the route-optimized endpoint during load testing, the test must generate OAuth tokens with query permissions. The following steps prepare authentication: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. Create a Databricks Service Principal.
2. Navigate to the Model Serving endpoint webpage, click **Permissions**, and grant the service principal **Can Query** level permissions.
3. Create a [Databricks secret scope](/concepts/databricks-secret-scopes.md) containing two keys:
   - The client ID of the Databricks service principal.
   - The client secret for the Databricks service principal.
4. Store the client ID and client secret as [Databricks secrets](/concepts/databricks-secret-scopes.md) in the scope. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Cluster Configuration for the Load Test Notebook

The load test notebook requires a specific cluster configuration: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- **Cluster type**: Single node cluster.
- **Runtime**: 15.4 LTS ML runtime.
- **Instance type**: CPU-optimized instance with at least 32 cores. Instances with more cores can generate higher queries or requests per second (RPS). ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Running the Load Test

After configuring the endpoint, notebooks, and payload, the load test notebook executes the following sequence: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. **Verification test**: Runs a very short 30-second duration load test against the endpoint to confirm it is online and responding.
2. **Load test series**: Runs a series of load tests with different amounts of client-side concurrency.
3. **Results analysis**: Prints any request failures or exceptions, and creates a plot of latency percentiles against client concurrency.
4. **Sizing recommendation**: After reviewing a table of results, the user selects the row that best meets latency requirements and inputs the application's desired RPS. The notebook responds with a recommended endpoint size.
5. **Final validation**: After updating the endpoint configuration to match the notebook's recommendations, the user runs a final load test to confirm the endpoint meets both latency and RPS requirements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) – Overview of load testing concepts and methodology.
- Locust – Open source framework used for the load test implementation.
- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) – How to create and manage serving endpoints.
- [Create Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) – Step-by-step endpoint creation guide.
- Databricks Secrets – Secure credential storage for authentication.
- [Serving UI](/concepts/serving-ui.md) – Interface for endpoint management and querying.

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
