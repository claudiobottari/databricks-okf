---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff5090e74765ea9bda1aeda18d8442adc89f999667eb053bc136a7e5901aa985
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - server-side-request-timeout
    - SRT
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Server-Side Request Timeout
description: Default timeout limits for requests sent to model serving endpoints, varying by endpoint type (CPU vs GPU).
tags:
  - model-serving
  - timeouts
  - server-side
timestamp: "2026-06-19T14:55:51.406Z"
---

## Server-Side Request Timeout

**Server-Side Request Timeout** occurs when a request to a [Model Serving](/concepts/model-serving.md) endpoint takes longer than the server allows, causing the server to terminate the request before a response is sent. This is distinct from [Client-Side Timeout (MLflow)](/concepts/client-side-timeout-mlflow-configuration.md) or [Model Deployment Timeout](/concepts/model-deployment-timeout.md), which happen at different stages of the request lifecycle. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Default Timeout Durations

The server-side timeout limit depends on the type of endpoint. If a request consistently fails at these exact thresholds, the cause is most likely a server-side timeout. ^[debug-model-serving-timeouts-databricks-on-aws.md]

| Endpoint type | Default server-side timeout |
|---------------|----------------------------|
| CPU workloads | 597 seconds (~10 minutes)  |
| GPU small or medium | 597 seconds (~10 minutes) |
| GPU large      | 597 seconds (~10 minutes)  |

Source data from the "Server-side timeouts" table; all three types share the same 597-second default. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Diagnosis

To determine if a timeout is server-side:

1. Check the endpoint’s **Events** and **Logs** tabs to confirm the endpoint is healthy (no deployment or build errors).
2. Observe when the request fails:
   - If it fails **at** the default timeout limit (e.g., 597 seconds), it is likely a server-side timeout.
   - If it fails **before** the limit, investigate configuration issues, client-side timeouts, or upstream dependencies. ^[debug-model-serving-timeouts-databricks-on-aws.md]

Additional troubleshooting steps include testing the model locally (e.g., in a notebook) to measure inference time, and reviewing service logs or [Inference Tables](/concepts/inference-tables.md) for error details. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Related Timeout Types

- **Idle endpoint warming up**: If an endpoint has [Scale-to-Zero](/concepts/scale-to-zero-in-model-serving.md) enabled and receives a request, warming up may cause a client-side timeout if it takes too long. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Connection timeout**: Occurs when a client cannot establish a connection to the server within a configured time (e.g., `SocketTimeout` for JDBC connections). ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Rate limiting**: Exceeding an endpoint’s rate limit may cause additional requests to fail, which can be confused with timeouts. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Related Concepts

- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- [Client-Side Timeout (MLflow)](/concepts/client-side-timeout-mlflow-configuration.md)
- [Model Deployment Timeout](/concepts/model-deployment-timeout.md)
- [Inference Tables](/concepts/inference-tables.md)
- [Resource and Payload Limits](/concepts/model-serving-resource-and-payload-limits.md)
- [Scale-to-Zero](/concepts/scale-to-zero-in-model-serving.md)

### Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
