---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 292a0558358235b9f019a6b7acfb6b2d0b8c127861b4a10b7163ec3ff8190b47
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rate-limits-and-timeouts-in-model-serving
    - Timeouts in Model Serving and Rate Limits
    - RLATIMS
    - Rate Limits
    - Rate limits
    - Rate limits for model serving
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Rate Limits and Timeouts in Model Serving
description: How exceeding rate limits on model serving endpoints can lead to request failures and timeouts, with references to resource and payload limits.
tags:
  - model-serving
  - rate-limiting
  - timeouts
  - databricks
timestamp: "2026-06-18T15:11:34.328Z"
---

# Rate Limits and Timeouts in Model Serving

**Rate Limits and Timeouts in Model Serving** refers to the various constraints and timing boundaries that can affect requests to model serving endpoints. Understanding these limits helps diagnose failures, optimize performance, and design robust applications that interact with deployed models.

## Overview

When serving models, timeouts can occur at multiple stages: during model deployment, on the server side while processing a request, or on the client side while waiting for a response. Rate limits control the maximum number of requests an endpoint can handle. Each type of timeout and limit has distinct causes and mitigation strategies. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Model Deployment Timeouts

Model deployment timeouts happen when the container build and deployment process exceed expected durations. The **Events** tab of the model serving endpoint page records timeout messages; search on `"timed out"` to find them. ^[debug-model-serving-timeouts-databricks-on-aws.md]

The container build has no hard limit but retries up to 3 times. After the container is built, the deployment step has the following maximum wait times before timeout:

| Workload Type | Timeout Duration |
|---------------|------------------|
| CPU           | 30 minutes       |
| GPU small or medium | 60 minutes |
| GPU large     | 120 minutes      |

^[debug-model-serving-timeouts-databricks-on-aws.md]

If a timeout message appears, navigate to the **Logs** tab and examine the build logs to determine the cause. Common issues include library dependency conflicts, resource constraints, and configuration problems. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Server-Side Timeouts

Server-side timeouts occur when the endpoint is healthy but request processing exceeds the default timeout configured on the server. The default timeout varies by endpoint type:

| Endpoint Type | Default Server-Side Timeout |
|---------------|-----------------------------|
| CPU serving endpoints | 597 seconds |
| GPU serving endpoints | 597 seconds |
| Other endpoint types | Varies (see table) |

If requests consistently fail exactly at the limit, the cause is likely a server-side timeout. If they fail earlier, check for configuration issues, service logs, or confirm the model works locally (e.g., from a notebook). ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Client-Side Timeouts

Client-side timeouts occur when the client (the caller) waits too long for a response. Error messages typically include `"timed out"` or **4xx Bad Request**. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### MLflow Configuration

MLflow environment variables control client-side timeout behavior:

- **`MLFLOW_HTTP_REQUEST_TIMEOUT`**: Specifies the timeout in seconds for MLflow HTTP requests. Default is **120 seconds**.
- **`MLFLOW_HTTP_REQUEST_MAX_RETRIES`**: Specifies the maximum number of retries with exponential backoff. Default is **7**.

Note that the client-side default (120 seconds) is much shorter than the server-side default (597 seconds) for CPU and GPU endpoints. Adjust the MLflow environment variables if your workload is expected to exceed 120 seconds. ^[debug-model-serving-timeouts-databricks-on-aws.md]

To diagnose client-side timeouts, test the model locally in a notebook. If a `"Timed out while evaluating the model"` message appears, increase the timeout. Environment variables can be configured using the Serving UI (under **Edit** → **Advanced configuration**) or programmatically with Python. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Third Party Client APIs

Third party client APIs (e.g., OpenAI client) can also cause client-side timeouts. These are common in model serving endpoints that use [custom PyFunc models](/concepts/custom-mlflow-pythonmodel.md) or PyFunc custom schema agents. ^[debug-model-serving-timeouts-databricks-on-aws.md]

To diagnose, test the model locally. If a message like `APITimeoutError: Request timed out` appears, adjust the relevant timeout parameter of the third party library. For example, the OpenAI client allows setting a `timeout` parameter (in seconds) when creating the client; the default and maximum is 10 minutes. Streaming can help work around the maximum timeout window. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Other Timeouts

### Idle Endpoints Warming Up

If an endpoint is [scaled to zero](/concepts/scale-to-zero-in-model-serving.md) and receives a request that triggers a warm-up, the startup latency can cause a client-side timeout. This is especially relevant in pipelines that depend on provisioned throughput endpoints or AI Search indexes. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Connection Timeout

Connection timeouts refer to the time a client waits to establish a connection with the server. If the connection is not established within this window, the client cancels. Check service logs and inference tables for error messages containing `"timed out"` or `"timeout"`. For example, a `SocketTimeout` for a JDBC connection to a SQL endpoint may appear as:

```
jdbc:spark://<server-hostname>:443;SocketTimeout=300
```

^[debug-model-serving-timeouts-databricks-on-aws.md]

## Rate Limits

Multiple requests made above the rate limit of an endpoint may cause failures for additional requests. Rate limits are defined per endpoint type; see [Resource and Payload Limits](/concepts/model-serving-resource-and-payload-limits.md) for details. For third party clients, consult the respective documentation to understand their rate limiting behavior. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Best Practices

- **Match client and server timeouts**: Adjust client-side timeouts (especially MLflow environment variables) to be longer than the expected server processing time, but be aware of third party client maximums.
- **Monitor with logs**: Use the **Events** and **Logs** tabs on the serving endpoint page to identify timeout root causes. Enable inference tables for deeper analysis.
- **Test locally**: Always validate the model with sample inputs in a notebook to rule out model-level issues before deploying.
- **Plan for cold starts**: For endpoints that scale to zero, consider pre-warming or adjusting client timeout to accommodate the warm-up latency.
- **Respect rate limits**: Understand the capacity of your endpoint and throttle requests accordingly, especially in automated pipelines.

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [Resource and Payload Limits](/concepts/model-serving-resource-and-payload-limits.md)
- [Custom PyFunc Models](/concepts/custom-mlflow-pythonmodel.md)
- [Scaling and Auto-scaling Model Serving](/concepts/queuing-and-autoscaling-in-model-serving.md)
- Debugging Model Serving Deployments
- MLflow Environment Variables

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
