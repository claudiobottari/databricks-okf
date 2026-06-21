---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6facd60f484172880d1c18f256f9cc2b5d8cdc642648f3ccda3279fd233da948
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - server-side-timeouts-for-model-serving-endpoints
    - STFMSE
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Server-side Timeouts for Model Serving Endpoints
description: Default request timeout durations on the server side for CPU and GPU model serving endpoints, distinguishing them from client-side timeouts.
tags:
  - model-serving
  - server-side
  - timeouts
timestamp: "2026-06-18T11:43:44.769Z"
---

# Server-side Timeouts for Model Serving Endpoints

**Server-side timeouts** occur when requests to a model serving endpoint take longer to process than the server's configured maximum allowed time. These timeouts are distinct from client-side timeouts and model deployment timeouts, and they are a common cause of request failures even when the endpoint appears healthy from its **Events** and **Logs** tabs. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Diagnosing Server-Side Timeouts

To determine if you are experiencing a server-side timeout, compare the timing of your failed requests against the default timeout limits for your endpoint type. If your request consistently fails at the timeout limit (rather than earlier), it is likely a server-side timeout. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Default Server-Side Timeout Values

The default server-side timeout varies depending on the type of model serving endpoint. The following table shows the default timeouts:

| Endpoint Type | Default Server-Side Timeout |
|---------------|------------------------------|
| CPU endpoints | 597 seconds |
| GPU endpoints | 597 seconds |
| GPU large workloads | 120 minutes |
| GPU small/medium workloads | 60 minutes |

^[debug-model-serving-timeouts-databricks-on-aws.md]

### Interpreting Timeout Behavior

- **Consistent failure at the timeout limit**: If your request fails at the exact limit (e.g., 597 seconds for CPU endpoints), this strongly indicates a server-side timeout.
- **Failure earlier than the limit**: If the request fails before reaching the timeout, the issue may be related to model configuration errors or resource constraints rather than a server-side timeout. In these cases, check the service logs and confirm that the model works locally (e.g., from a notebook) or on previous requests with earlier model versions. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Distinguishing Server-Side from Client-Side Timeouts

Server-side timeouts should be distinguished from client-side timeouts, which typically return error messages saying "timed out" or **4xx Bad Request**. Client-side timeouts are often caused by MLflow environment variable configurations (such as `MLFLOW_HTTP_REQUEST_TIMEOUT` defaults of 120 seconds) or by third-party client API configurations. The HTTP request timeouts on the client side are set to 120 seconds, which differs from the server-side default timeout of 597 seconds for CPU and GPU serving endpoints. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Causes of Server-Side Timeouts

Server-side timeouts can occur in several scenarios:

- **Idle endpoints warming up**: If an endpoint is [scaled to zero](/concepts/scale-to-zero-in-model-serving.md) and receives a request that triggers a cold start, the warm-up time may exceed the server-side timeout. This is especially relevant in pipelines that involve calls to [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) or AI Search indices. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Connection timeouts**: These occur when a client waits too long to establish a connection with the server. If the connection is not established within the timeout period, the client cancels the attempt. Common examples include SocketTimeout errors when connecting to a SQL endpoint over JDBC. Look for error messages containing "timed out" or "timeout". ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Rate limits**: Multiple requests made over the rate limit of an endpoint may lead to failures for additional requests. See [resource and payload limits](/concepts/model-serving-resource-and-payload-limits.md) for rate limits based on endpoint types. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Troubleshooting Steps

### 1. Check Service Logs

Examine the **Service Logs** for your endpoint or the [Inference Tables](/concepts/inference-tables.md) if you have enabled them. Look for timeout-related messages or errors. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### 2. Test Locally

Confirm that the model works locally using sample inputs, such as in a notebook, to ensure there are no underlying model errors. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### 3. Adjust Server-Side Timeout Configuration

If you need a longer timeout, you can configure the server-side timeout for your endpoint. The method for adjusting this depends on your model serving platform. For [Databricks Model Serving](/concepts/databricks-model-serving.md), you can:

- **Via the Serving UI**: On the endpoint's page, select **Edit** on the top right, expand **Advanced configuration** to add relevant timeout environment variables. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Via Python**: Configure MLflow environment variables programmatically. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### 4. Avoid Client-Side Timeouts

If your workload is expected to exceed the default 120-second client-side timeout, adjust MLflow environment variables such as `MLFLOW_HTTP_REQUEST_TIMEOUT` and `MLFLOW_HTTP_REQUEST_MAX_RETRIES` accordingly. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Concepts

- [Model serving endpoints](/concepts/model-serving-endpoint.md)
- [Model Deployment Timeouts](/concepts/model-deployment-timeouts.md)
- Client-side timeouts
- MLflow environment variables
- [Third-party client API configurations](/concepts/third-party-client-api-timeouts.md)
- [Resource and payload limits](/concepts/model-serving-resource-and-payload-limits.md)
- [Inference Tables](/concepts/inference-tables.md)

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
