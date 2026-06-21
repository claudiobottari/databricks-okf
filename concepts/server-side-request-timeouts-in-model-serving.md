---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fae46cef0ea841b3f3955935f8f4774591fa41f8e80cb01335c218ea7fe866b9
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - server-side-request-timeouts-in-model-serving
    - SRTIMS
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Server-Side Request Timeouts in Model Serving
description: Timeouts caused by the serving endpoint taking too long to respond to a request, with default limits varying by endpoint type (CPU vs GPU).
tags:
  - model-serving
  - server-side
  - timeouts
  - databricks
timestamp: "2026-06-18T15:11:01.615Z"
---

# Server-Side Request Timeouts in Model Serving

**Server-Side Request Timeouts** occur when a [Model Serving](/concepts/model-serving.md) endpoint fails to process a request within the time limit enforced by the serving infrastructure. These timeouts are distinct from client-side or connection timeouts and are typically caused by slow model inference, resource contention, or misconfigured endpoint settings. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Default Server-Side Timeout Limits

The default server-side timeout varies by endpoint type, as shown in the table below. If a request consistently fails at exactly these limits, the timeout is almost certainly on the server side. ^[debug-model-serving-timeouts-databricks-on-aws.md]

| Endpoint Type | Default Server-Side Timeout |
|---------------|-----------------------------|
| CPU serving endpoints | 597 seconds |
| GPU serving endpoints | 597 seconds |
| Provisioned throughput endpoints | Varies (see [resource limits](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-limits)) |

^[debug-model-serving-timeouts-databricks-on-aws.md]

> **Note:** The client-side HTTP request timeout (set by `MLFLOW_HTTP_REQUEST_TIMEOUT`) defaults to 120 seconds, which is much shorter than the server-side limit. If your workload takes between 120 and 597 seconds, the client may time out before the server does. Adjust client-side timeouts accordingly. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## How to Identify a Server-Side Timeout

1. **Check the endpoint’s health** – Ensure the Events and Logs tabs of the serving endpoint show no errors or deployment failures. ^[debug-model-serving-timeouts-databricks-on-aws.md]
2. **Compare failure timing** – If the request fails at exactly the default server-side timeout (e.g., 597 seconds), it is likely a server-side timeout. If it fails earlier, the cause may be a configuration issue or client-side timeout. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Troubleshooting Steps

If you suspect a server-side timeout:

- **Review service logs** – The Logs tab provides detailed error messages and can reveal slow model calls or resource bottlenecks. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Test the model locally** – Run inference with sample inputs in a notebook to confirm the model works as expected. Compare processing time against the endpoint’s timeout. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Optimize model performance** – Slow inference may require model optimization (e.g., reduced input size, model quantization) or upgrading to a larger endpoint type (see CPU vs GPU serving).
- **Scale the endpoint** – If concurrency is high, consider enabling scaling to 0 or increasing the number of replicas to reduce queueing delays. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Timeouts

Other timeout types that may interact with server-side limits include:

- Client-Side Timeouts in Model Serving – Caused by MLflow environment variables or third-party client configurations.
- [Connection Timeouts](/concepts/connection-timeout.md) – Occur when a client fails to establish a TCP connection within a configured window.
- Idle Endpoint Warm-up – If an endpoint is scaled to 0, the first request may trigger a cold start and exceed client timeouts.
- [Rate Limits](/concepts/rate-limits-and-timeouts-in-model-serving.md) – Excessive requests may be dropped before reaching the server, returning 429 or similar errors. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
