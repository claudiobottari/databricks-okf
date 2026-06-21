---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 155f611d28d92e294cefbbb14e5649fa1a2c3db70554524bc18259036503a3db
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-timeout-types
    - MSETT
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Model Serving Endpoint Timeout Types
description: "Three categories of timeouts encountered when using Databricks Model Serving: model deployment timeouts, server-side timeouts, and client-side timeouts."
tags:
  - model-serving
  - timeouts
  - debugging
timestamp: "2026-06-19T14:55:43.429Z"
---

# Model Serving Endpoint Timeout Types

**Model Serving Endpoint Timeout Types** describes the various timeouts encountered when deploying or calling [Model Serving](/concepts/model-serving.md) endpoints on Databricks. These timeouts are categorized into model deployment timeouts, server-side timeouts, client-side timeouts (including [MLflow](/concepts/mlflow.md)-specific and third‑party API configurations), and other edge cases such as idle endpoint warm‑up, connection timeouts, and rate limits. Understanding these categories helps diagnose and resolve timeout errors efficiently. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Model Deployment Timeouts

When deploying a model or updating an existing deployment, the process may time out if the container build and model deployment exceed a duration that depends on the endpoint workload configuration. The **Events** tab of the serving endpoint page records timeout messages; searching for `"timed out"` reveals them. The container build has no hard limit (it retries up to three times), but the deployment phase after the container is built applies separate limits:

- CPU workloads: 30 minutes
- GPU small or medium workloads: 60 minutes
- GPU large workloads: 120 minutes

If a timeout occurs, examine the build logs in the **Logs** tab to identify root causes such as library dependency issues, resource constraints, or configuration errors. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Server‑Side Timeouts

If the endpoint is healthy (as shown in the **Events** and **Logs** tabs) but requests still time out, the issue may be a server-side timeout. The default server-side timeout depends on the endpoint type:

| Endpoint type | Default server-side timeout |
|---------------|----------------------------|
| CPU and GPU serving endpoints | 597 seconds |
| Serverless GPU endpoints | 360 seconds |
| Foundation Model API (deprecated) | 15 seconds for completion / 180 seconds for chat |

To determine if a timeout is server-side, check whether the failure occurs consistently at the limit. If it fails earlier, the cause may be a configuration issue (e.g., errors in the service logs, model not working locally). ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Client‑Side Timeouts

Client-side timeouts typically return error messages containing `"timed out"` or a `4xx Bad Request`. They originate from the client making the request rather than from the server.

### MLflow Configuration

When using [MLflow](/concepts/mlflow.md) to send requests, two environment variables control timeout behaviour:

- **`MLFLOW_HTTP_REQUEST_TIMEOUT`**: Default 120 seconds. Specifies the timeout for MLflow HTTP requests.
- **`MLFLOW_HTTP_REQUEST_MAX_RETRIES`**: Default 7 seconds. Maximum number of retries with exponential backoff.

Because the client-side default (120 s) is lower than the server-side default (597 s), long‑running inferences may exceed the client timeout. To detect this, test the model locally in a notebook and measure request latency. If the notebook shows a `"Timed out while evaluating the model"` message, the MLflow timeout may need adjustment. Configure the variables via the **Serving UI** (under **Advanced configuration**) or programmatically with Python. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Third‑Party Client APIs

Custom PyFunc models or Agents (AI Agent Framework) that use third‑party APIs (e.g., [OpenAI Client](/concepts/openai-client-compatibility.md), AI Search) can also experience client-side timeouts. For example, the [OpenAI Client](/concepts/openai-client-compatibility.md) defaults to a maximum timeout of 10 minutes; you can adjust the `timeout` parameter when creating the client. If the model pipeline includes such APIs, test locally with sample inputs. A message like `APITimeoutError: Request timed out` indicates that the third‑party client’s timeout is too low. Check the **Service Logs** or inference tables for detailed error messages. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Other Timeouts

### Idle Endpoints Warming Up

If the endpoint is [Scale to Zero|scaled to 0](/concepts/compute-scale-out-and-scale-to-zero.md), a request that triggers warm‑up can cause a client-side timeout if the warm‑up takes too long. This is especially relevant for pipelines that depend on provisioned throughput endpoints or external indices. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Connection Timeout

Connection timeouts occur when a client waits for a TCP connection to be established but the server does not respond within the configured time. For instance, a JDBC connection to a SQL endpoint might set a `SocketTimeout` parameter. Look for error messages containing `"timed out"` or `"timeout"` in the service logs or inference tables. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Rate Limits

When the request rate exceeds the endpoint’s [Resource and Payload Limits|rate limit](/concepts/model-serving-resource-and-payload-limits.md), additional requests may fail with a timeout or error. Consult the limits documentation for the appropriate endpoint type. For third‑party clients, review the client’s own rate‑limiting documentation. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
