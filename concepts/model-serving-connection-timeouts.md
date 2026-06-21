---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c1d01012d9bc95a1e1a827b4b328dac73d6ffdc88b28ba80b0ce940b5d9d48c
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-connection-timeouts
    - MSCT
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Model Serving Connection Timeouts
description: Timeouts related to establishing network connections between clients and model serving endpoints, such as JDBC SocketTimeout configurations.
tags:
  - model-serving
  - connection
  - timeouts
  - networking
timestamp: "2026-06-19T18:17:01.621Z"
---

# Model Serving Connection Timeouts

**Model Serving Connection Timeouts** occur when a client fails to establish a connection with a model serving endpoint within a specified time. These timeouts can result from server-side limits, client configuration, endpoint idle states, or rate limits. Understanding the different types of timeouts and their causes helps in diagnosing and resolving connection issues. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Connection Timeout

A connection timeout is the time a client waits to establish a connection with the server. If the connection is not established within this limit, the client cancels the attempt. The exact error messaging varies by service. For example, a `SocketTimeout` may appear when a service reads or writes to a SQL endpoint over a JDBC connection. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Common Causes

### Client-Side Timeout Configuration

Client-side timeouts typically return error messages containing **“timed out”** or **4xx Bad Request**. Two common sources are [MLflow](/concepts/mlflow.md) environment variables and third-party client APIs. ^[debug-model-serving-timeouts-databricks-on-aws.md]

**MLflow environment variables** that affect timeouts include:

- `MLFLOW_HTTP_REQUEST_TIMEOUT` – default 120 seconds.
- `MLFLOW_HTTP_REQUEST_MAX_RETRIES` – default 7 seconds (maximum retries with exponential backoff).

Note that the client-side HTTP request timeout (120 seconds) differs from the server-side default timeout of 597 seconds for CPU and GPU serving endpoints. If a workload is expected to exceed 120 seconds, the MLflow environment variables should be adjusted accordingly. ^[debug-model-serving-timeouts-databricks-on-aws.md]

**Third-party client APIs** (e.g., [OpenAI client](/concepts/openai-client-compatibility.md)) can also cause connection timeouts if their timeout parameters are not configured appropriately. The OpenAI client default and maximum timeout is 10 minutes. The `timeout` parameter can be set to a shorter value to avoid long waits. Streaming can be used to work around the maximum timeout window. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Server-Side Timeouts

If an endpoint is healthy according to the **Events** and **Logs** tabs but requests time out, the issue may be server-side. Server-side default timeouts vary by endpoint type. Requests that consistently fail at the timeout limit are likely due to a server-side timeout. If a request fails earlier, configuration issues should be investigated. ^[debug-model-serving-timeouts-databricks-on-aws.md]

| Endpoint type | Default server-side timeout |
|---------------|----------------------------|
| CPU workloads | 30 minutes |
| GPU small/medium | 60 minutes |
| GPU large | 120 minutes |

### Idle Endpoints

If an endpoint is scaled to 0 and receives a request that warms it up, the warm‑up time can lead to a client-side timeout. This is especially relevant in pipelines that include calls to provisioned throughput endpoints or AI Search indices. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Rate Limits

Making multiple requests over the endpoint’s rate limit can cause subsequent requests to fail. See [Resource and payload limits](/concepts/model-serving-resource-and-payload-limits.md) for rate limits per endpoint type. For third-party clients, review the provider’s documentation. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Diagnosing Connection Timeouts

To diagnose connection timeouts:

1. Check the **Service Logs** of the model serving endpoint and any enabled [Inference Tables](/concepts/inference-tables.md).
2. Look for error messages containing **“timed out”** or **“timeout”**.
3. Test the model locally with sample inputs (e.g., in a notebook) to confirm it evaluates within expected time.
4. Test the endpoint using POST requests and compare response times against the default timeouts.

The **Events** tab of the model serving endpoint page records timeout messages for deployment-related issues; search on **“timed out”** to find them. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Resolving Connection Timeouts

- **MLflow variables:** Set `MLFLOW_HTTP_REQUEST_TIMEOUT` and `MLFLOW_HTTP_REQUEST_MAX_RETRIES` via the Serving UI (edit endpoint → Advanced configuration) or programmatically with `mlflow.set_experiment_tag`.
- **Third-party clients:** Adjust the client’s `timeout` parameter (e.g., OpenAI client’s `timeout=10` seconds).
- **Idle endpoints:** Configure the endpoint to avoid scaling to 0 if warm‑up delays are unacceptable, or increase client timeouts.
- **Server-side timeouts:** If the workload exceeds default timeouts, consider upgrading the endpoint compute size or optimizing the model inference speed.
- **Rate limits:** Reduce request frequency or request an increase in the endpoint’s rate limit.

For deployment timeouts (container build and model deployment), check the build logs on the **Logs** tab. The container build retries up to 3 times; the subsequent deployment waits 30 minutes (CPU), 60 minutes (GPU small/medium), or 120 minutes (GPU large) before timing out. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- [MLflow](/concepts/mlflow.md)
- [Custom PyFunc models](/concepts/custom-mlflow-pythonmodel.md)
- [Inference Tables](/concepts/inference-tables.md)
- [Resource and payload limits](/concepts/model-serving-resource-and-payload-limits.md)
- [Endpoint scaling](/concepts/model-serving-endpoint-scaling.md)
- Agent Framework

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
