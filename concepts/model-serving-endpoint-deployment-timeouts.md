---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2fab14b9fba3d92ee2d474105d913f23099455dce10b086017bc18a0dacd626d
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-deployment-timeouts
    - MSEDT
    - Model Serving Endpoint Requirements|model serving endpoint requirements
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Model Serving Endpoint Deployment Timeouts
description: Timeouts that occur when deploying or updating a model serving endpoint, including container build retries and post-build deployment duration limits for CPU and GPU workloads.
tags:
  - model-serving
  - deployment
  - timeouts
timestamp: "2026-06-18T11:43:27.206Z"
---

# Model Serving Endpoint Deployment Timeouts

When deploying or querying a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) on Databricks, you may encounter timeouts at different stages of the lifecycle. This page describes the types of timeouts you might see—deployment timeouts, server‑side request timeouts, and client‑side timeouts—and provides guidance on how to diagnose and resolve them. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Model Deployment Timeouts

During the initial deployment of a model or an update to an existing deployment, the process can time out if the combined time for building the container and serving the model exceeds a duration that depends on the endpoint’s workload configuration. The **Events** tab of the model serving endpoint page records timeout messages; search for `"timed out"` to find them. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Container Build and Retry

The container build step has no hard time limit, but it can retry up to 3 times. If the build continues to fail after all retries, check the **Logs** tab to examine the build logs. Common causes include library dependency issues, resource constraints, or misconfiguration. See [Debug after container build failure](/concepts/container-build-debugging-for-model-serving.md) for detailed troubleshooting. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Deployment After Build

Once the container is built, the platform waits for the model deployment to become healthy. The timeout depends on the endpoint’s workload type:

- **CPU workloads**: up to **30 minutes**
- **GPU Small or GPU Medium workloads**: up to **60 minutes**
- **GPU Large workloads**: up to **120 minutes**

If the deployment does not become ready within these windows, a timeout event is recorded. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Server‑Side Timeouts

When the endpoint is healthy but individual inference requests are timing out, the timeout may be on the server‑side. The default server‑side timeout varies by endpoint type:

| Endpoint Type | Default Request Timeout |
|---------------|------------------------|
| CPU or GPU serving endpoints | 597 seconds (approx. 10 minutes) |
| Provisioned Throughput endpoints | 180 seconds (3 minutes) |

If a request consistently fails at the timeout limit, it is likely a server‑side timeout. If it fails earlier, inspect the service logs for other errors and verify that the model works locally (e.g., in a notebook) or has succeeded on previous requests with older model versions. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Client‑Side Timeouts

Client‑side timeouts typically return errors containing **"timed out"** or a **4xx Bad Request**. They can originate from [MLflow](/concepts/mlflow.md) environment variables or from third‑party client APIs used inside your model pipeline.

### MLflow Environment Variables

Two common MLflow environment variables control HTTP timeouts:

- **`MLFLOW_HTTP_REQUEST_TIMEOUT`** – timeout in seconds for MLflow HTTP requests. Default is **120 seconds**.
- **`MLFLOW_HTTP_REQUEST_MAX_RETRIES`** – maximum number of retries with exponential backoff. Default is **7**.

Note that the default client‑side timeout (120 s) is much lower than the server‑side default (597 s for CPU/GPU endpoints). If your workload is expected to take longer than 120 s, adjust the environment variables accordingly. ^[debug-model-serving-timeouts-databricks-on-aws.md]

#### Configuring MLflow Environment Variables

**Via the Serving UI**  
1. Select the endpoint and click **Edit**.  
2. Under **Entity Details**, expand **Advanced configuration**.  
3. Add the desired MLflow timeout environment variable.

**Programmatically using Python** – Set the variables in your deployment code or environment before registering the model.

### Third‑Party Client APIs

If your model pipeline (e.g., a [custom PyFunc model](/concepts/custom-mlflow-pyfunc-model.md) or a custom schema agent) calls external services, those clients may have their own timeout defaults. For example, an OpenAI client has a default timeout of 10 minutes, but you can override it with the `timeout` parameter:

```python
from openai import OpenAI
client = OpenAI(
    timeout=10,  # seconds before client times out
    api_key=DATABRICKS_TOKEN,
    base_url="<WORKSPACE_URL>/serving-endpoints"
)
```

To debug third‑party client timeouts, test the model locally with sample inputs. If you see messages like `APITimeoutError: Request timed out`, adjust the client’s timeout window. You can also check the endpoint’s **Service Logs** or enable [Inference Tables](/concepts/inference-tables.md) to capture request‑level details. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Other Timeouts

### Idle Endpoint Warm‑Up

Endpoints that have been scaled to 0 will need to warm up when they receive a new request. If the warm‑up takes longer than the client’s timeout, the request may fail. This is especially relevant in pipelines that depend on external services such as provisioned throughput endpoints or AI Search indices. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Connection Timeout

A connection timeout occurs when a client waits too long to establish a TCP connection to the server. For example, a JDBC connection to a SQL endpoint might time out if the `SocketTimeout` is set too low:

```
jdbc:spark://<server-hostname>:443;HttpPath=<http-path>;SocketTimeout=300
```

Look for error messages with **"timed out"** or **"timeout"** in your service logs and inference tables. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Rate Limits

If you send requests beyond the [resource and payload limits](/concepts/model-serving-resource-and-payload-limits.md) of the endpoint, additional requests may be throttled and return errors. For third‑party providers, review their rate‑limit documentation. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
