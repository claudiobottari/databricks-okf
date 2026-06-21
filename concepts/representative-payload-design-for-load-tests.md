---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dcd733bb1192a78b995fe8e15a60f2fd3711e51d24ab5ad3df3c96785c8a4b6a
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - representative-payload-design-for-load-tests
    - RPDFLT
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Representative Payload Design for Load Tests
description: Ensuring load test validity by using payloads that accurately represent production traffic, matching the size and structure of real requests such as a single credit card transaction for fraud detection models.
tags:
  - payload
  - load-testing
  - best-practices
timestamp: "2026-06-19T17:50:25.906Z"
---

# Representative Payload Design for Load Tests

**Representative Payload Design for Load Tests** refers to the practice of constructing the input data sent during a load test so that it closely mirrors the payload characteristics expected in production. A well-designed payload is critical for obtaining valid and actionable load test results, particularly for custom model serving endpoints where payload size, structure, and content affect latency and throughput. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Importance

If the endpoint is sensitive to the size of the payload, the input payload used during testing must match the expected production usage. For example, a fraud detection model that processes one credit card transaction per request should be tested with a payload representing a single typical transaction, not a batch of many transactions. Using an unrepresentative payload can lead to misleading latency or throughput measurements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Specifying the Payload

In the recommended load test workflow for Databricks Model Serving, the payload is specified in an `input.json` file that is placed alongside the load test notebook. This file contains the data that every concurrent connection sends to the endpoint during the test. The file should be crafted to match the expected production input format and content. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Validating the Payload

Before running the full load test, the payload should be validated by:

1. Copying the full contents of `input.json` into the **Query** window on the Databricks Model Serving endpoint page.
2. Verifying that the endpoint returns the desired outputs.

This step confirms that the endpoint accepts the payload and produces correct results under normal conditions. To access the Query window, navigate to the **Serving UI**, select the endpoint, click the dropdown next to the **Use** button, and choose **Query**. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Relationship to Endpoint Sizing

Because model serving endpoint concurrency scales linearly with the number of concurrent connections, it is possible to test with a small endpoint (using the representative payload) and then calculate the required endpoint size to meet target latency and requests per second (RPS). A final load test on the properly sized endpoint confirms that both latency and RPS requirements are satisfied. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Load test for Model Serving](/concepts/load-testing-for-model-serving-endpoints.md) – The overall process of running load tests on Databricks serving endpoints.
- Endpoint concurrency – How concurrent connections affect endpoint performance.
- [Serving UI](/concepts/serving-ui.md) – The interface for querying endpoints and validating payloads.

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
