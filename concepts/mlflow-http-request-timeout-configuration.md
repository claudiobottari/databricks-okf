---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fae959df8cd4d4e6d1f54e4645889d91070d5644243e1c638125801257229a23
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-http-request-timeout-configuration
    - MHRTC
    - MLflow HTTP Request Timeout
    - MLflow HTTP Request Timeouts
    - MLflow HTTP request timeout
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: MLflow HTTP Request Timeout Configuration
description: Client-side timeout configuration via MLflow environment variables MLFLOW_HTTP_REQUEST_TIMEOUT and MLFLOW_HTTP_REQUEST_MAX_RETRIES for model serving requests.
tags:
  - mlflow
  - timeouts
  - configuration
  - client-side
timestamp: "2026-06-19T14:55:56.897Z"
---

# MLflow HTTP Request Timeout Configuration

**MLflow HTTP Request Timeout Configuration** refers to the set of environment variables that control how long the MLflow client waits for an HTTP request to complete, and how many times it retries after a failure. These settings are critical when MLflow communicates with remote services such as [Model Serving](/concepts/model-serving.md) endpoints, tracking servers, or registry APIs, especially for workloads that may take longer than the default timeout. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Environment Variables

Two primary environment variables govern MLflow HTTP request behavior: ^[debug-model-serving-timeouts-databricks-on-aws.md]

| Variable | Default | Description |
|----------|---------|-------------|
| `MLFLOW_HTTP_REQUEST_TIMEOUT` | 120 seconds | Specifies the timeout in seconds for individual MLflow HTTP requests. |
| `MLFLOW_HTTP_REQUEST_MAX_RETRIES` | 7 | Specifies the maximum number of retries with exponential backoff for failed MLflow HTTP requests. |

These defaults may not match the server-side timeout of the endpoint. For example, CPU and GPU serving endpoints have a default server-side timeout of 597 seconds, which is much longer than the default client-side timeout of 120 seconds. If your workload consistently exceeds the client-side timeout, you should increase `MLFLOW_HTTP_REQUEST_TIMEOUT` accordingly. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Detecting Client-Side Timeouts

Client-side timeouts caused by MLflow environment variable configurations typically produce error messages that contain the phrase **_"timed out"_** or a **4xx Bad Request** status code. A common example is:

> `Timed out while evaluating the model. Verify that the model evaluates within the timeout.`

^[debug-model-serving-timeouts-databricks-on-aws.md]

To determine whether a timeout originates from MLflow's HTTP client configuration: ^[debug-model-serving-timeouts-databricks-on-aws.md]

1. **Test the model locally** (for example, in a notebook) using sample inputs. Measure the time it takes to process requests.
   - If requests take longer than the default timeouts or you see a **_"timed out"_** message, the MLflow client-side timeout is likely the cause.
2. **Test the model serving endpoint directly** using POST requests. Review the endpoint's service logs or inference tables (if enabled) for additional clues.

## Configuring MLflow Environment Variables

You can set the timeout and retry environment variables either through the Model Serving UI or programmatically in your code.

### Using the Serving UI

1. Navigate to the model serving endpoint page.
2. Click **Edit** at the top right.
3. Under **"Entity Details"**, expand **Advanced configuration**.
4. Add the relevant MLflow timeout environment variables as plain text environment variables.

See the documentation on [how to add plain text environment variables](/concepts/plain-text-environment-variables-in-model-serving.md) for full details. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Using Python

Set the environment variable in your Python environment before making MLflow requests:

```python
import os
os.environ["MLFLOW_HTTP_REQUEST_TIMEOUT"] = "300"   # 5 minutes
os.environ["MLFLOW_HTTP_REQUEST_MAX_RETRIES"] = "5"
```

Note that environment variables must be set before any MLflow imports or calls that trigger HTTP requests.

## Relationship to Server-Side Timeouts

Server-side timeouts (enforced by the model serving endpoint) and client-side timeouts (controlled by MLflow) are independent. A request may fail on the client side even if the server is still processing. To diagnose which side is timing out, compare the failure time to the default values: ^[debug-model-serving-timeouts-databricks-on-aws.md]

- If the request fails consistently at the MLflow client timeout limit (default 120 seconds), the issue is a client-side timeout.
- If the request fails before the MLflow client timeout, it may be due to a server-side timeout or other configuration issues.

## Best Practices

- **Align client and server timeouts.** Because the client default (120 s) is much shorter than the CPU/GPU serving endpoint default (597 s), increase `MLFLOW_HTTP_REQUEST_TIMEOUT` when you expect long-running inference requests.
- **Test with representative payloads.** Evaluate the model locally with inputs that match production size to estimate realistic request durations.
- **Monitor retry behavior.** An excessive number of retries may mask underlying performance problems. Review `MLFLOW_HTTP_REQUEST_MAX_RETRIES` based on observed failure patterns.

## Related Concepts

- [Model Serving Timeouts](/concepts/model-serving-endpoint-timeouts.md) — Overview of all timeout types (deployment, server-side, client-side)
- [Model Serving](/concepts/model-serving.md) — The serving infrastructure that handles inference requests
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The server that logs experiment data and may be subject to the same timeout settings
- [Debug After Container Build Failure](/concepts/container-build-debugging-for-model-serving.md) — Troubleshooting model deployment issues
- Environment Variables for MLflow — The full list of MLflow environment variables

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
