---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60e6c3b18d254a28fbe35b6dcd08360304bf9121b5deb5b52c2253615afcbfb2
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-configuration-for-load-testing
    - ECFLT
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Endpoint Configuration for Load Testing
description: "Specific configuration recommendations for starting load tests: Small CPU endpoint with concurrency of 4, route optimization enabled, and scale to zero disabled"
tags:
  - databricks
  - configuration
  - serving-endpoint
timestamp: "2026-06-18T11:07:43.601Z"
---

# Endpoint Configuration for Load Testing

**Endpoint configuration for load testing** refers to the process of setting up and tuning [Model Serving](/concepts/model-serving.md) endpoints on Databricks to optimize performance under various load conditions. Using the open-source Locust framework, you can run systematic load tests to determine the right endpoint configuration for your latency and throughput requirements.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Initial Endpoint Configuration

The load test notebook assumes your model runs on a CPU-based [Model Serving Endpoint](/concepts/model-serving-endpoint.md). When creating your serving endpoint using the Serving UI, configure the following settings:^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- Start with a **Small** CPU endpoint with both minimum and maximum concurrency set to **4**.
- Enable **route optimization**.
- Disable **Scale to Zero**.

## Service Principal Authentication

To interact with the route-optimized endpoint, the load test requires OAuth tokens with permissions to query the endpoint. Set up authentication as follows:^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. Create a Databricks Service Principal.
2. Navigate to the Model Serving endpoint page, click **Permissions**, and grant the service principal **Can Query** permissions.
3. [Create a Databricks secret scope](/concepts/databricks-secret-scopes.md) with two keys:
   - `service_principal_client_id` — the ID of your Databricks service principal.
   - `service_principal_client_secret` — the client secret for the Databricks service principal.
4. Store the client ID and client secret in [Databricks secrets](/concepts/databricks-secret-scopes.md).

## Payload Configuration

The payload used during load testing should accurately represent the type of payload you expect in production. For example, if your model evaluates one credit card transaction per request, ensure your payload contains only one typical transaction.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

Specify your payload in the `input.json` file placed alongside the load test notebook. Test the payload by pasting the full `input.json` data into the **Query** window on your Databricks Model Serving endpoint and confirming the model responds with the desired outputs. To open the Query box:^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. Navigate to the **Serving UI**.
2. Select the endpoint for load testing.
3. In the top-right corner, select the dropdown next to the **Use** button.
4. Select **Query**.

## Running the Load Test

After configuring the endpoint, notebooks, and payload, execute the notebook step by step. The notebook first runs a short 30-second load test to verify the endpoint is online and responding.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

You can then run a series of load tests with varying levels of client-side concurrency. After the series completes, the notebook:^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- Prints any request failures or exceptions.
- Creates a plot of latency percentiles against client concurrency.
- Presents a table of results where you select the row that best meets your latency requirements.
- Accepts your application's desired requests per second (RPS).
- Recommends how to size your endpoint to meet both RPS and latency goals.

After updating your endpoint configuration to match the recommendations, run the final load test to confirm the endpoint meets both latency and RPS requirements.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Endpoint Sizing Relationship

The serving endpoint concurrency needed to achieve a target latency percentile scales linearly with the number of concurrent connections. This means you can test on a small endpoint and calculate the required endpoint size before performing the final test.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Cluster Configuration for Load Testing

The Locust load test notebook requires a Databricks cluster with the following configuration:^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

- **Single node cluster**
- **15.4 LTS ML runtime**
- **CPU-optimized instance** with at least 32 cores

Locust uses CPU resources to run tests, handling roughly 4,000 requests per second per CPU core depending on payload. The notebook uses the `--processes -1` flag to let Locust auto-detect CPU cores on the driver and fully utilize them. Monitor the Locust output — if Locust is bottlenecked by CPU, an output message appears.^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) — Overview of load testing concepts
- Locust — Open-source load testing framework
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — Databricks model serving infrastructure
- [Create Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — Endpoint creation guide
- Route Optimization — Feature that improves endpoint routing efficiency
- Service Principals — Authentication for automated access

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
