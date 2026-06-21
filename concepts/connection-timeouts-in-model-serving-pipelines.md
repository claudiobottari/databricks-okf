---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 86dc9acc57536c28ad8b7b0189ba7aef2b35fa9a432615d199a107c5dc208981
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - connection-timeouts-in-model-serving-pipelines
    - CTIMSP
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Connection Timeouts in Model Serving Pipelines
description: Timeouts related to establishing network connections (e.g., JDBC SocketTimeout) between model serving endpoints and downstream services like SQL endpoints or AI Search indices.
tags:
  - model-serving
  - networking
  - timeouts
timestamp: "2026-06-18T11:44:25.235Z"
---

# Connection Timeouts in Model Serving Pipelines

**Connection timeouts** occur when a client attempts to establish a connection with a model serving endpoint, but the connection is not established within the configured timeout period. When this happens, the client cancels the connection attempt. These timeouts can manifest at different stages of a model serving pipeline, from deployment through to client-side request processing. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Types of Timeouts

### Model Deployment Timeouts

When deploying or updating a model using [Model Serving](/concepts/model-serving.md), the process may time out if the container build and model deployment exceed a certain duration that is dependent on the endpoint workload configuration. The deployment process after the container is built will wait up to 30 minutes for CPU workloads, 60 minutes for GPU small or medium workloads, and 120 minutes for GPU large workloads before timing out. The container build itself has no hard limit but retries up to 3 times. ^[debug-model-serving-timeouts-databricks-on-aws.md]

Timeout messages are recorded in the **Events** tab of the model serving endpoint page. Search for "timed out" to find them. If you encounter a timeout, navigate to the **Logs** tab and examine the build logs to determine the cause. Common causes include library dependency issues, resource constraints, and configuration issues. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Server-Side Timeouts

If your endpoint appears healthy according to the **Events** and **Logs** tabs but requests time out when making calls, the timeout may be occurring on the server side. The default timeout varies depending on the type of model serving endpoint. ^[debug-model-serving-timeouts-databricks-on-aws.md]

To determine if you are experiencing a server-side timeout:

- If your request consistently fails at the default timeout limit, it's likely a server-side timeout.
- If your request fails earlier than the limit, it may be due to configuration issues or [MLflow](/concepts/mlflow.md) environment variable settings.

Check the service logs and confirm that the model has worked locally (for example, from a notebook) or on previous requests on earlier versions. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Client-Side Timeouts

Client-side timeouts typically return error messages that say "timed out" or return `4xx Bad Request` responses. Two common sources of client-side timeouts are [MLflow](/concepts/mlflow.md) environment variable configurations and third-party client APIs used in model pipelines. ^[debug-model-serving-timeouts-databricks-on-aws.md]

#### MLflow Environment Variable Configuration

The most common MLflow environment variables for timeouts are:

- **MLFLOW_HTTP_REQUEST_TIMEOUT**: Specifies the timeout in seconds for MLflow HTTP requests. Default is 120 seconds.
- **MLFLOW_HTTP_REQUEST_MAX_RETRIES**: Specifies the maximum number of retries with exponential backoff. Default is 7.

Note that the MLflow client-side timeout defaults to 120 seconds, which differs from the server-side default timeout of 597 seconds for CPU and GPU serving endpoints. You may need to adjust these variables if your workload is expected to exceed the 120-second client-side timeout. ^[debug-model-serving-timeouts-databricks-on-aws.md]

To configure MLflow environment variables, use the Serving UI or Python:

**Using the Serving UI:** Select the endpoint, click **Edit**, expand **Advanced configuration**, and add the relevant MLflow timeout environment variable.

**Using Python:** Set environment variables programmatically before making requests. ^[debug-model-serving-timeouts-databricks-on-aws.md]

#### Third-Party Client API Timeouts

Third-party client APIs can cause client-side timeouts depending on their configuration. These can impact model serving endpoints that consist of pipelines using those APIs. To determine if a timeout is caused by a third-party client API: ^[debug-model-serving-timeouts-databricks-on-aws.md]

1. Test the model locally with sample inputs in a notebook.
2. If you see a "timed out" message, adjust the relevant timeout parameters for the third-party client.

For example, when using the OpenAI client, you can configure the `timeout` parameter to change the maximum time before a request times out on the client side. The default and maximum timeout is 10 minutes. For the OpenAI client, you can work around the maximum timeout by enabling streaming. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Idle Endpoints and Warm-Up Timeouts

If an endpoint is scaled to 0 (zero instances) and receives a request that triggers a warm-up, the warm-up process can lead to a client-side timeout if it takes too long. This is particularly relevant for pipelines that use steps relying on provisioned throughput endpoints or AI Search indices. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Connection Timeout

Connection timeouts are specifically related to the time a client waits to establish a connection with the server. If the connection is not established within this time, the client cancels the attempt. For example, a `SocketTimeout` (for a service reading/writing to a SQL endpoint over a JDBC connection) may appear as: ^[debug-model-serving-timeouts-databricks-on-aws.md]

```
jdbc:spark://<server-hostname>:443;HttpPath=<http-path>;TransportMode=http;SSL=1[;property=value[;property=value]];SocketTimeout=300
```

Look for error messages containing "timed out" or "timeout" in the service logs and inference tables of the [Model Serving](/concepts/model-serving.md) endpoint. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Rate Limits

Multiple requests made over the rate limit of an endpoint may lead to failures for additional requests. See resource and payload limits for rate limits based on endpoint types. For third-party clients, review the documentation of the specific client you are using. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Debugging Steps

1. Check the **Events** tab for "timed out" messages.
2. Examine build logs on the **Logs** tab for deployment issues.
3. Test the model locally (e.g., from a notebook) to confirm it works as expected.
4. Check service logs for your endpoint and inference tables (if enabled).
5. Review MLflow environment variable configurations and third-party client API timeout settings.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The service that hosts and serves ML models
- Model Serving Limits — Resource and payload constraints for serving endpoints
- [MLflow](/concepts/mlflow.md) — The ML lifecycle platform that manages model deployments
- OpenAI — A common third-party client API for LLM serving
- Scaled to 0 — Endpoint scaling configuration that affects warm-up timeouts
- [Provisioned Throughput](/concepts/provisioned-throughput.md) — Throughput settings for serving endpoints

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
