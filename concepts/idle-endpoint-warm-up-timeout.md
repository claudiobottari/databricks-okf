---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b2e2148499f30bb85553a7cad22ce65d431be2c734a4e228c91255368a059184
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idle-endpoint-warm-up-timeout
    - IEWT
    - idle-endpoint-warm-up-timeouts
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Idle Endpoint Warm-Up Timeout
description: Timeouts that can occur when a scaled-to-zero serving endpoint receives a request and must warm up, potentially exceeding the client-side timeout.
tags:
  - databricks
  - model-serving
  - scaling
  - timeouts
timestamp: "2026-06-19T09:55:58.215Z"
---

# Idle Endpoint Warm-Up Timeout

An **Idle Endpoint Warm-Up Timeout** occurs when a [Model Serving](/concepts/model-serving.md) endpoint that has been scaled to zero receives an inference request and fails to complete the warm-up process within the client’s configured timeout window. This type of timeout is categorized under client-side timeouts in Databricks Model Serving. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## How It Happens

When an endpoint is configured with [scale-to-zero](/concepts/scale-to-zero-in-model-serving.md), it shuts down all compute resources during periods of inactivity. The first request that arrives after a period of idleness triggers a cold start: the system must allocate a new container, load the model, and initialize any dependencies before it can serve the request. If this warm-up phase takes longer than the client’s timeout setting (for example, the default 120-second [MLflow HTTP request timeout](/concepts/mlflow-http-timeout-configuration.md)), the client cancels the request and returns a timeout error. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Impact on Pipelines

Idle endpoint warm-up timeouts are especially problematic in multi-step pipelines that chain calls to provisioned throughput endpoints, AI Search indices, or other downstream services. A single slow warm-up can cascade, causing the entire pipeline to fail with a “timed out” or 4xx error. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Mitigation

To reduce the likelihood of warm-up timeouts:

- **Adjust client-side timeout settings.** Increase the timeout value in the calling application (e.g., `MLFLOW_HTTP_REQUEST_TIMEOUT` for MLflow clients, or the `timeout` parameter for third-party HTTP clients like the OpenAI Python client) to accommodate the expected warm-up duration. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Disable scale-to-zero** for latency-sensitive workloads. Keeping a minimum number of always-on instances avoids cold starts entirely.
- **Warm up the endpoint proactively** by sending a dummy request during off-peak hours, keeping the endpoint ready.
- **Use provisioned throughput** endpoints, which maintain a fixed capacity and do not scale to zero.

For general guidelines on debugging model serving timeouts, including server-side and deployment timeouts, see [Debug model serving timeouts](/concepts/model-serving-endpoint-timeouts.md). ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- [Scale-to-zero](/concepts/scale-to-zero-in-model-serving.md)
- Client-side timeout
- [Server-Side Timeout](/concepts/server-side-timeout.md)
- [MLflow HTTP request timeout](/concepts/mlflow-http-timeout-configuration.md)
- [Provisioned Throughput Endpoint](/concepts/provisioned-throughput-endpoint.md)

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
