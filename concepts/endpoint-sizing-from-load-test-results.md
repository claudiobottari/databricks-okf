---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 766629bfd6ab07035f7828b64bd9cef2ee454c5ea814c514c360fb7ee1625880
  pageDirectory: concepts
  sources:
    - configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - endpoint-sizing-from-load-test-results
    - ESFLTR
  citations:
    - file: configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md
title: Endpoint Sizing from Load Test Results
description: A methodology that uses a small concurrency endpoint for load testing, then calculates the production endpoint size needed to meet target requests-per-second and latency requirements based on observed metrics.
tags:
  - model-serving
  - capacity-planning
  - optimization
timestamp: "2026-06-19T09:23:12.312Z"
---

# Endpoint Sizing from Load Test Results

**Endpoint sizing from load test results** is a methodology for determining the optimal [endpoint concurrency](/concepts/endpoint-sizing-and-concurrency-planning.md) and provisioned capacity for a [Custom model serving endpoint](/concepts/custom-model-serving-endpoint-support.md) on Databricks. By running controlled Locust load tests with varying client concurrency levels and analyzing the resulting latency percentiles, you can calculate the endpoint configuration needed to meet target requests-per-second (RPS) and latency goals. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Prerequisites

Before running a load test, the endpoint, authentication, and payload must be configured:

- **Endpoint configuration**: Start with a CPU endpoint set to a minimum and maximum concurrency of 4 ("Small"). Enable Route optimization and disable **Scale to Zero**. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- **Authentication**: Create a Databricks Service Principal with `Can Query` permissions on the endpoint and store its credentials in a [Databricks secret scope](/concepts/databricks-secret-scopes.md). ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- **Payload**: Prepare a representative `input.json` file — e.g., one transaction per request for a fraud detection model — to mirror production traffic. Test the payload by pasting it into the Serving UI **Query** window to ensure the model returns the desired output. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

The load test notebook runs on a single-node cluster with at least 32 CPU cores (Databricks recommends a CPU-optimized instance) using the 15.4 LTS ML runtime. The `--processes -1` flag lets Locust auto-detect and use all available CPU cores. Locust generates roughly 4000 requests per second per CPU core, depending on payload size. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Running the Load Test Series

The **Locust load test** notebook runs a series of short 30-second tests, each at a different client-side concurrency level. After each test, it records latency percentiles, RPS, and any failures. Results are displayed in a table; you select the row that best meets your latency requirements. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Sizing Calculation

After selecting the row that satisfies your latency goals, you provide the **desired RPS** for production. The notebook calculates the required concurrency and number of provisioned concurrency units based on the linear relationship between concurrency and endpoint capacity: the concurrency needed to achieve a given percentile latency scales linearly with the number of concurrent connections. This means you can test on a small endpoint (concurrency=4) and then calculate the size needed before performing a final validation test. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Validating the Recommended Size

Update the endpoint's minimum and maximum concurrency to match the notebook's recommendation, then run the **final load test** to confirm both latency and RPS targets are met. If results are acceptable, the sizing is validated. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Additional Considerations

- Keep an eye on the Locust output; if Locust is being bottlenecked by the CPU, a warning message appears. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]
- Review request failures printed by the notebook to debug authentication errors or malformed payloads before concluding. ^[configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- Endpoint concurrency
- Route optimization
- Locust
- [Custom model serving endpoint](/concepts/custom-model-serving-endpoint-support.md)
- Databricks Service Principal
- [Databricks secret scope](/concepts/databricks-secret-scopes.md)

## Sources

- configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws.md](/references/configure-a-load-test-for-custom-model-serving-endpoints-databricks-on-aws-cafc0e58.md)
