---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 304b97a720ac6b651622958d58ff4dd4b2eb53c875ca902c860dfaac6483769c
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - representative-payload-design-for-load-testing
    - RPDFLT
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Representative Payload Design for Load Testing
description: "The principle that load test payloads must accurately reflect real production traffic characteristics, such as request size and data structure, to produce valid performance measurements. Example: a fraud-detection endpoint should send one transaction per request, not batches."
tags:
  - load-testing
  - testing-methodology
timestamp: "2026-06-18T14:42:38.666Z"
---

# Representative Payload Design for Load Testing

**Representative Payload Design for Load Testing** refers to the practice of selecting and configuring the input data payload sent during load tests to accurately reflect real-world production usage patterns. The validity of load test results depends critically on how well the test payload mirrors the actual payloads the endpoint will process in production. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Overview

When configuring a load test for a [Model Serving Endpoint](/concepts/model-serving-endpoint.md), the payload sent by all concurrent connections must be carefully chosen. If the endpoint is sensitive to payload size, structure, or content, an unrepresentative payload can produce misleading latency and throughput measurements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Key Principles

### Match Production Payload Characteristics

The payload should accurately represent the type of payload planned for production use. For example, if the model is a fraud detection system that evaluates credit card transactions one at a time in real time, the test payload should represent only one typical transaction rather than a batch of transactions. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Consider Payload Sensitivity

Some endpoints are sensitive to the size of the input payload. For such endpoints, ensuring the input payload is representative of expected production usage is especially important. Payload size can affect both latency and the number of requests per second (RPS) the endpoint can sustain. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Implementation

### Specifying the Payload

The payload is specified in an `input.json` file that accompanies the load test notebook. This file defines the data sent by all concurrent connections during the test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Testing the Payload

Before running the full load test, the payload should be validated by:

1. Navigating to the **Serving UI** in the Databricks workspace.
2. Selecting the endpoint to be load tested.
3. Opening the dropdown menu next to the **Use** button and selecting **Query**.
4. Pasting the full `input.json` data into the **Query** window.
5. Verifying that the model responds with the desired outputs. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Relationship to Endpoint Sizing

The model serving endpoint concurrency needed to achieve a certain percentile of latency scales linearly with the number of concurrent connections. This means testing can be performed on a small endpoint with a representative payload, and the required endpoint size can be calculated before performing the final test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Best Practices

- **Use realistic data.** Avoid synthetic or simplified payloads that do not reflect production data characteristics.
- **Test payload validity first.** Always verify the payload produces correct model outputs before running load tests.
- **Consider payload variability.** If production payloads vary significantly in size or structure, consider testing with multiple representative payloads.
- **Document payload assumptions.** Record the payload characteristics used during testing to ensure reproducibility and to inform future test iterations.

## Related Concepts

- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md) — The broader practice of evaluating endpoint performance under load
- [Model Serving Endpoint Configuration](/concepts/model-serving-endpoint-configuration-api.md) — Configuring endpoint concurrency, scaling, and routing
- [Locust Load Testing Framework](/concepts/locust-load-testing-framework.md) — The open-source framework used for running load tests
- [Endpoint Latency and Throughput](/concepts/llm-endpoint-latency-vs-throughput-trade-off.md) — Key performance metrics measured during load testing
- Service Principal Authentication — Required authentication setup for load testing

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
