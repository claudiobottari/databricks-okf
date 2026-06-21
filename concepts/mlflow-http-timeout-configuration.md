---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8a05233830b13b1618186ef9005ac7eb168eb2c79831207cb1427701622bc90
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-http-timeout-configuration
    - MHTC
    - MLflow Timeout Configuration
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: MLflow HTTP Timeout Configuration
description: MLflow environment variables (MLFLOW_HTTP_REQUEST_TIMEOUT, MLFLOW_HTTP_REQUEST_MAX_RETRIES) that control client-side HTTP request timeouts for MLflow operations.
tags:
  - mlflow
  - timeouts
  - environment-variables
  - configuration
timestamp: "2026-06-19T18:16:36.101Z"
---

# MLflow HTTP Timeout Configuration

**MLflow HTTP Timeout Configuration** refers to the environment variables and settings that control how long MLflow HTTP requests wait before timing out on the client side. These configurations are critical when deploying models with [Model Serving](/concepts/model-serving.md) endpoints, as mismatches between client-side and server-side timeouts can cause request failures.

## Overview

Client-side timeouts in MLflow typically return error messages containing **"timed out"** or **4xx Bad Request**. These timeouts occur when MLflow HTTP requests take longer than the configured timeout period to complete. The default client-side timeout differs from the server-side timeout, which can lead to unexpected failures if not properly configured. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Key Environment Variables

The two most important MLflow environment variables for timeout configuration are:

- **`MLFLOW_HTTP_REQUEST_TIMEOUT`**: Specifies the timeout in seconds for MLflow HTTP requests. The default timeout is **120 seconds**.
- **`MLFLOW_HTTP_REQUEST_MAX_RETRIES`**: Specifies the maximum number of retries with exponential backoff for MLflow HTTP requests. The default is **7 retries**.

For the complete list of timeout-related environment variables, see the [mlflow.environment_variables documentation](https://mlflow.org/docs/latest/python_api/mlflow.environment_variables.html). ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Client-Side vs. Server-Side Timeout Mismatch

A common source of timeout errors is the discrepancy between client-side and server-side timeout defaults:

- **Client-side default (MLflow HTTP)**: 120 seconds
- **Server-side default (CPU and GPU serving endpoints)**: 597 seconds

If your model workload consistently takes longer than 120 seconds to process, the client-side timeout will trigger before the server-side timeout, resulting in a **"timed out"** error. Adjust the `MLFLOW_HTTP_REQUEST_TIMEOUT` environment variable accordingly if you expect your workload to exceed the 120-second client-side timeout. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Diagnosing Timeout Issues

To determine if a timeout is caused by MLflow environment variable configuration:

1. **Test the model locally** using sample inputs in a notebook to confirm it works as expected before registering and deploying.
   - Examine the time it takes to process requests.
   - If requests take longer than the default timeouts or you get a **"timed out"** message in the notebook, the issue is likely client-side.
   - Example error message: `Timed out while evaluating the model. Verify that the model evaluates within the timeout.`

2. **Test the model serving endpoint** using POST requests.
   - Check the **Service Logs** for your endpoint or the inference tables if enabled.
   - For inference table schema details, see Unity AI Gateway-enabled inference table schema. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Configuring MLflow Environment Variables

You can configure MLflow environment variables using the Serving UI or programmatically using Python.

### Using the Serving UI

1. Select the endpoint you want to configure.
2. On the endpoint's page, select **Edit** on the top right.
3. In **"Entity Details"**, expand **Advanced configuration** to add the relevant MLflow timeout environment variable.

See [Add plain text environment variables](/concepts/plain-text-environment-variables-in-model-serving.md) for more details. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Using Python

Set the environment variable before making MLflow requests:

```python
import os
os.environ["MLFLOW_HTTP_REQUEST_TIMEOUT"] = "300"  # Set timeout to 300 seconds
```

## Related Concepts

- [Model Serving Timeouts](/concepts/model-serving-endpoint-timeouts.md) — Overview of all timeout types in model serving
- [Model Deployment Timeouts](/concepts/model-deployment-timeouts.md) — Timeouts during container build and deployment
- [Server-Side Timeouts](/concepts/server-side-timeouts.md) — Default timeout limits for serving endpoints
- Client-Side Timeouts — Third-party client API timeout configurations
- Model Serving Debugging — General debugging for model serving issues
- [Resource and Payload Limits](/concepts/model-serving-resource-and-payload-limits.md) — Rate limits and other constraints

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
