---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 52bf1e43f38b9ffc497c87eab24ef1b428688ecd85e9dedc9db3ac51e9321643
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - load-test-payload-specification
    - LTPS
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Load Test Payload Specification
description: Guidelines for choosing representative payloads in load tests to accurately reflect production usage patterns and validate them via the Serving UI query interface
tags:
  - databricks
  - payload
  - testing
timestamp: "2026-06-18T11:07:45.739Z"
---

# Load Test Payload Specification

**Load Test Payload Specification** refers to the definition and configuration of the request payload used when load testing [Model Serving Endpoints](/concepts/model-serving-endpoint.md) on Databricks. The payload specification determines what data is sent by all concurrent connections during a load test and directly impacts the validity and relevance of test results.

## Payload File Structure

The payload is specified in an `input.json` file that is placed alongside the **Locust load test** notebook. This file contains the complete request body that every concurrent client connection sends to the serving endpoint during the test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Representativeness Requirements

The payload must accurately represent the type of data your endpoint will process in production. If the endpoint is sensitive to payload size, ensure the input payload is representative of expected production usage. An unrepresentative payload can produce misleading load test results that do not reflect real-world performance. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

For example, if testing a fraud detection model that evaluates one credit card transaction per request in real time, the payload should represent only one typical transaction — not a batch of transactions. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Payload Validation

Before running the load test, validate the payload by pasting the complete `input.json` data into the **Query** window on the Databricks Model Serving endpoint and confirming the model responds with the desired outputs. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

To access the Query window:

1. Navigate to the **Serving UI** in your Databricks workspace.
2. Select the endpoint you want to load test.
3. In the top right corner, select the dropdown menu next to the **Use** button.
4. Select **Query**. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Impact on Test Validity

The payload specification directly affects load test validity because the serving endpoint's latency and throughput can vary significantly based on payload size and content. A payload that is too small may overestimate endpoint capacity, while a payload that is too large may underestimate it. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

The model serving endpoint concurrency needed to achieve a certain percentile of latency scales linearly with the number of concurrent connections. This allows testing on a small endpoint first and calculating the required endpoint size before performing the final test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) — Overview of load testing methodology
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The endpoints being tested
- Locust — The open-source framework used for load testing
- [Endpoint Concurrency](/concepts/endpoint-sizing-and-concurrency-planning.md) — How concurrent connections affect performance
- [Serving UI](/concepts/serving-ui.md) — Interface for querying and managing endpoints

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
