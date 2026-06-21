---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c19ebb3c0eae23819a8a708e6dcf24907fb5f8de9b96a5af5b9829af0519cf8
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - server-side-timeout
    - server-side-request-timeout
    - SRT
    - server-side-request-timeouts-in-model-serving
    - SRTIMS
    - server-side-timeouts-for-model-serving-endpoints
    - STFMSE
    - server-side-timeouts
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Server-Side Timeout
description: Request processing time limits enforced by the model serving endpoint, varying by workload type (CPU/GPU small, medium, large).
tags:
  - databricks
  - model-serving
  - timeouts
  - server-side
timestamp: "2026-06-19T09:55:41.730Z"
---

Here is the wiki page for "Server-Side Timeout".

---

## Server-Side Timeout

A **Server-Side Timeout** occurs when a request to a model serving endpoint is cancelled by the server before the model has finished processing, because the request duration exceeds the system's defined limit. This is distinct from a client-side timeout, where the client making the request cancels the connection.

### Default Timeout Values

The default server-side timeout varies by endpoint type. If a request consistently fails at the exact limit listed below, it is likely a server-side timeout. If a request fails earlier than this limit, the cause is more likely a configuration issue or a client-side timeout. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Diagnostic Steps

To determine if a timeout is a server-side timeout, observe whether the failure occurs at the configured server-side limit. If the request fails precisely at this boundary, it indicates a server-side timeout. ^[debug-model-serving-timeouts-databricks-on-aws.md]

If a request fails earlier, potential causes include:
- Configuration issues within the model or endpoint.
- Client-side timeouts from tools like [MLflow](/concepts/mlflow.md) or third-party APIs.
- Network latency or connection issues. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Common Causes

#### Slow Inference or Complex Models
If the model takes longer to process a request than the server-side timeout allows, the request will be terminated. This can be investigated by testing the model locally in a notebook to measure inference time. ^[debug-model-serving-timeouts-databricks-on-aws.md]

#### Downstream Service Latency
Pipelines that rely on external services (e.g., provisioned throughput endpoints, AI Search indices) can introduce latency that pushes the total request duration over the server-side limit. This is especially common when an endpoint is "warming up" from an idle state. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Mitigation Strategies

- **Optimize model inference**: Profile and optimize the model's code to reduce inference time.
- **Review pipeline dependencies**: Ensure that all components in a model pipeline respond within expected timeframes.
- **Adjust client-side settings**: If the server-side limit is sufficient but the client-side timeout is too short, configure the relevant timeout environment variable (e.g., `MLFLOW_HTTP_REQUEST_TIMEOUT`) or third-party client timeout parameter (e.g., `timeout` for the [OpenAI client](/concepts/openai-client-compatibility.md)). ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Related Concepts

- [Model Deployment Timeouts](/concepts/model-deployment-timeouts.md)
- Client-Side Timeout
- [MLflow Timeout Configuration](/concepts/mlflow-http-timeout-configuration.md)
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- Pipeline Latency
- [Connection Timeout](/concepts/connection-timeout.md)

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
