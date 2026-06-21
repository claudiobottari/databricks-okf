---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b910816c60c6e96cff0e9fe714c78a2aae4d615f97cbe02a78ac834575d42b87
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-http-client-timeout-configuration
    - MHCTC
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: MLflow HTTP Client Timeout Configuration
description: Configuration of MLflow environment variables (MLFLOW_HTTP_REQUEST_TIMEOUT, MLFLOW_HTTP_REQUEST_MAX_RETRIES) to control client-side HTTP request timeouts for model serving.
tags:
  - mlflow
  - client-side
  - timeouts
  - configuration
timestamp: "2026-06-18T15:11:13.799Z"
---

# MLflow HTTP Client Timeout Configuration

**MLflow HTTP Client Timeout Configuration** refers to the environment variables that control how long the MLflow Python client waits for an HTTP request to complete and how many times it retries failed requests. These settings are important when deploying models via [model serving endpoints](/concepts/model-serving-endpoint.md) because a mismatch between client-side and server-side timeout values can cause premature request failures, even when the serving endpoint is healthy.

## Overview

Client-side timeouts in MLflow typically produce error messages that say **“timed out”** or **4xx Bad Request**. The most common cause is incorrect configuration of MLflow environment variables that govern HTTP request behavior. ^[debug-model-serving-timeouts-databricks-on-aws.md]

The two primary environment variables are:

- **`MLFLOW_HTTP_REQUEST_TIMEOUT`** – Specifies the timeout in seconds for individual MLflow HTTP requests. The default value is **120 seconds**. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **`MLFLOW_HTTP_REQUEST_MAX_RETRIES`** – Specifies the maximum number of retries with exponential backoff for MLflow HTTP requests. The default value is **7** (units not explicitly stated, but implicitly seconds or a count; the source lists it as “Default is 7 seconds” for the “maximum number of retries”, which appears to be a description of the retry interval or count). ^[debug-model-serving-timeouts-databricks-on-aws.md]

For the full list of timeout-related variables, see the [mlflow.environment_variables documentation](https://mlflow.org/docs/latest/python_api/mlflow.environment_variables.html). ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Default Values and Important Differences

The client-side HTTP request timeout default is **120 seconds**, which differs from the server-side default timeout of **597 seconds** for CPU and GPU serving endpoints. If a model workload is expected to take longer than 120 seconds, the MLflow client-side timeout will trigger before the server can respond. Adjust the environment variables accordingly to avoid premature timeouts. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Identifying MLflow-Related Timeouts

To determine whether a timeout is caused by MLflow environment variable configuration:

1. **Test the model locally** using sample inputs in a notebook. Examine the time it takes to process the requests. If requests take longer than the default timeouts, or if a “timed out” message appears in the notebook (e.g., `Timed out while evaluating the model. Verify that the model evaluates within the timeout.`), then the client timeout is likely too low. ^[debug-model-serving-timeouts-databricks-on-aws.md]
2. **Test the model serving endpoint** using POST requests. Check the **Service Logs** for the endpoint or [Inference Tables](/concepts/inference-tables.md) if they are enabled. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Configuring MLflow Environment Variables

Environment variables can be configured for a model deployment through the Serving UI or programmatically using Python.

### Serving UI

1. Select the endpoint to configure.
2. On the endpoint’s page, select **Edit** at the top right.
3. In **Entity Details**, expand **Advanced configuration** to add the relevant MLflow timeout environment variable (e.g., `MLFLOW_HTTP_REQUEST_TIMEOUT`). See [Add plain text environment variables](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving#plain-text). ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Python

You can set the environment variables programmatically using standard Python mechanisms (e.g., `os.environ['MLFLOW_HTTP_REQUEST_TIMEOUT'] = '300'`) before making requests. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Best Practices

- Compare the expected model inference time against the client-side timeout defaults. If your model consistently requires more than 120 seconds, increase `MLFLOW_HTTP_REQUEST_TIMEOUT` to a value that exceeds the actual response time but remains within the server-side limit (597 seconds).
- Adjust `MLFLOW_HTTP_REQUEST_MAX_RETRIES` if transient failures occur; note that the default maximum retry behavior already includes exponential backoff.
- Always test the model locally before deploying to confirm that the configured timeouts are sufficient.

## Related Concepts

- [Model Serving Timeouts](/concepts/model-serving-endpoint-timeouts.md) – Overview of all timeout types (deployment, server-side, client-side).
- [Model Deployment Timeouts](/concepts/model-deployment-timeouts.md) – Timeouts that occur when deploying or updating a serving endpoint.
- [Server-Side Timeouts](/concepts/server-side-timeouts.md) – Default timeouts for requests on the serving endpoint side.
- Client-Side Timeouts – General category covering MLflow and third-party client timeout issues.
- MLflow Environment Variables – Complete reference for MLflow configuration options.
- [Inference Tables](/concepts/inference-tables.md) – Logs and schema that can help diagnose timeout issues.

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
