---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 081a27c8c8181e544076e2f07dc0989c8292f71f1d4761ba8ee944188ad4a75d
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - client-side-timeout-mlflow-configuration
    - CT–MC
    - Client-Side Timeout (MLflow)
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Client-Side Timeout – MLflow Configuration
description: Timeouts caused by MLflow environment variables (MLFLOW_HTTP_REQUEST_TIMEOUT, MLFLOW_HTTP_REQUEST_MAX_RETRIES) that can be tuned for long-running model inference.
tags:
  - databricks
  - mlflow
  - timeouts
  - configuration
timestamp: "2026-06-19T09:56:22.651Z"
---

Here is the wiki page for "Client-Side Timeout – MLflow Configuration".

## Client-Side Timeout – MLflow Configuration

**Client-Side Timeout – MLflow Configuration** refers to the timeout settings configured on the client side of an MLflow Model Serving request. Unlike [Server-Side Timeouts](/concepts/server-side-timeouts.md), which are enforced by the serving endpoint itself, client-side timeouts are controlled by the calling application's configuration. When a client-side timeout occurs, it typically returns error messages that say "timed out" or **4xx Bad Request**. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Common Causes

The most common cause of client-side timeouts in MLflow stems from the default values of MLflow environment variables. The HTTP request timeout on the client-side defaults to **120 seconds**, which is significantly shorter than the default server-side timeout of **597 seconds** for CPU and GPU serving endpoints. If a workload is expected to exceed the 120-second limit without adjusting these variables, the client will time out before the server can respond. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Relevant Environment Variables

The following are the most common MLflow environment variables for timeouts. A full list is available in the [mlflow.environment_variables documentation](https://mlflow.org/docs/latest/python_api/mlflow.environment_variables.html). ^[debug-model-serving-timeouts-databricks-on-aws.md]

- **MLFLOW_HTTP_REQUEST_TIMEOUT**: Specifies the timeout in seconds for MLflow HTTP requests. Default is 120 seconds. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **MLFLOW_HTTP_REQUEST_MAX_RETRIES**: Specifies the maximum number of retries with exponential backoff for MLflow HTTP requests. Default is 7. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Debugging Client-Side Timeouts

To determine if a timeout is caused by an MLflow environment variable configuration, use one of the following methods:^[debug-model-serving-timeouts-databricks-on-aws.md]

1.  **Test the model locally** using sample inputs in a notebook to confirm it works as expected and examine processing time. ^[debug-model-serving-timeouts-databricks-on-aws.md]
    - If requests take longer than the default timeouts, or you see a message like: `Timed out while evaluating the model. Verify that the model evaluates within the timeout.` ^[debug-model-serving-timeouts-databricks-on-aws.md]
2.  **Test the model serving endpoint** using POST requests and examine the **Service Logs** or inference tables. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Configuring MLflow Environment Variables

To resolve client-side timeouts, you can configure the relevant MLflow environment variables. This can be done through the Serving UI or programmatically using Python.^[debug-model-serving-timeouts-databricks-on-aws.md]

- **Serving UI**: Select the endpoint, click **Edit**, expand **Advanced configuration** under **Entity Details**, and add the relevant MLflow timeout environment variable. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Best Practice

The documentation notes that the default HTTP request timeout on the client-side (120 seconds) differs from the server-side's default (597 seconds). Accordingly, you should adjust the MLflow environment variables if you expect your workload to exceed the 120-second client-side timeout. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Related Concepts

- [Model Deployment Timeouts](/concepts/model-deployment-timeouts.md) – Timeouts that occur when deploying or updating a serving endpoint.
- [Server-Side Timeouts](/concepts/server-side-timeouts.md) – Timeouts enforced by the model serving endpoint.
- Client-Side Timeouts (Third Party) – Similar timeout issues caused by third-party client APIs.
- Model Serving Endpoint Limits – Rate limits and payload constraints.
- [Debugging Model Serving](/concepts/model-serving.md) – General guidance for troubleshooting serving endpoints.

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
