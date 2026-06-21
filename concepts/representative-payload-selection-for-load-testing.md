---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f65288a6c3a6c71cd30701f052a10a2a0e93264b01d5f2c025a7c05220d2e15
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - representative-payload-selection-for-load-testing
    - RPSFLT
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Representative Payload Selection for Load Testing
description: The practice of choosing input payloads that accurately mirror real production traffic patterns to ensure valid and meaningful load test results.
tags:
  - testing
  - best-practices
  - machine-learning
timestamp: "2026-06-19T14:23:30.711Z"
---

## Representative Payload Selection for Load Testing

**Representative Payload Selection for Load Testing** is the practice of choosing an input payload for a load test that accurately reflects the type, size, and structure of requests the endpoint will receive in production. Using a non-representative payload can lead to misleading latency and throughput measurements, making it difficult to correctly size the serving endpoint.

### Importance

When configuring a load test for a [Model Serving](/concepts/model-serving.md) endpoint, the payload sent by every concurrent connection is defined in a file (e.g., `input.json`). If the endpoint is sensitive to payload size or content, an unrepresentative payload can skew the test results. For example, a payload that is too small may understate real-world latency, while an overly large payload may overstate it. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

Choosing a representative payload ensures that the load test’s findings—such as required concurrency and recommended endpoint size—are valid for the expected production workload. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### How to Select a Representative Payload

1. **Model the expected production request.**  
   Consider the structure, data types, and size of a typical real-world request. For example, if the model is a fraud detection system that evaluates credit card transactions in real time, and each request contains exactly one transaction, the payload should represent a single typical transaction. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

2. **Account for payload-size sensitivity.**  
   If the endpoint’s performance is affected by payload length (e.g., large prompts for an LLM or high-dimensional feature vectors), the test payload must closely match the expected production size. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

3. **Use a consistent payload for all connections.**  
   In a load test using a framework like Locust, the same `input.json` payload is sent by every concurrent connection. Therefore, the payload should be the most common or representative sample of the traffic pattern, not an outlier. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Verifying the Payload

Before running the load test, verify that the chosen payload produces the desired outputs from the endpoint: ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

1. Navigate to the **Serving UI** in your Databricks workspace.
2. Select the endpoint to test.
3. Open the **Query** window (from the dropdown menu next to the **Use** button).
4. Paste the full payload data and confirm that the model responds correctly and with expected latency.

This step helps catch format errors or unexpected behaviors early. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Relationship to Endpoint Sizing

The concurrency required to achieve a target latency percentile scales linearly with the number of concurrent connections. Because the payload selection directly influences latency at a given concurrency, using a representative payload allows you to test on a small endpoint first and then calculate the endpoint size needed for production. After scaling, a final load test with the same payload validates that the larger endpoint meets both RPS and latency requirements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

### Related Concepts

- [Load Testing for Serving Endpoints](/concepts/load-testing-for-ml-serving-endpoints.md)
- [Endpoint Concurrency and Scaling](/concepts/model-serving-endpoint-concurrency-scaling.md)
- Latency Measurement in Model Serving
- [Locust Load Testing Framework](/concepts/locust-load-testing-framework.md)
- Model Serving Query Interface

### Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
