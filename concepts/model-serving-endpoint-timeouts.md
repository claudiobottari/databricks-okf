---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 225f7360080f47da71614319024c7f0d075ee482a802aa7650ffe590ff13ce42
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-timeouts
    - MSET
    - Model Serving Endpoint Limits
    - Serving Endpoint Timeout
    - Debug model serving timeouts
    - Model Serving Timeouts
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Model Serving Endpoint Timeouts
description: Overview of the various timeout categories (deployment, server-side, client-side) encountered when using Databricks Model Serving endpoints.
tags:
  - model-serving
  - timeouts
  - databricks
timestamp: "2026-06-19T18:16:37.911Z"
---

# Model Serving Endpoint Timeouts

**Model Serving Endpoint Timeouts** refer to the various timeout scenarios that can occur when deploying, updating, or making inference requests to [model serving endpoints](/concepts/model-serving-endpoint.md) on Databricks. Understanding the three primary categories—deployment, server-side, and client-side timeouts—is essential for debugging and optimizing model serving performance. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Model Deployment Timeouts

When deploying a model or updating an existing deployment, the process may time out due to container build issues, resource constraints, or configuration errors. The **Events** tab of the model serving endpoint page records timeout messages; search for `"timed out"` to find them. ^[debug-model-serving-timeouts-databricks-on-aws.md]

The container build step has no hard time limit but retries up to 3 times. After the container is built, the deployment step waits up to the following durations before timing out, depending on the workload configuration:

- **CPU workloads**: 30 minutes
- **GPU small or medium workloads**: 60 minutes
- **GPU large workloads**: 120 minutes

^[debug-model-serving-timeouts-databricks-on-aws.md]

If a `"timed out"` message appears in the Events tab, navigate to the **Logs** tab and examine the build logs to determine the cause. Common issues include library dependency problems, resource constraints, and configuration errors. See [Debug after container build failure](/concepts/container-build-debugging-for-model-serving.md) for further guidance. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Server-Side Timeouts

If your endpoint is healthy according to the Events and Logs tabs but you experience timeouts when making calls, the timeout may be server-side. The default server-side timeout varies by endpoint type; for CPU and GPU serving endpoints it is 597 seconds. ^[debug-model-serving-timeouts-databricks-on-aws.md]

To determine if you experienced a server-side timeout:

- If your request consistently fails at the default timeout limit, it is likely a server-side timeout.
- If your request fails earlier than the limit, it may be due to configuration issues. Check the service logs for errors and confirm that the model works locally (e.g., from a notebook) or on previous requests with earlier versions. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Client-Side Timeouts: MLflow Configuration

Client-side timeouts typically return error messages containing `"timed out"` or `4xx Bad Request`. Common causes are MLflow environment variable configurations. The most relevant MLflow timeout variables are: ^[debug-model-serving-timeouts-databricks-on-aws.md]

- **`MLFLOW_HTTP_REQUEST_TIMEOUT`**: Specifies the timeout in seconds for MLflow HTTP requests. Default is 120 seconds.
- **`MLFLOW_HTTP_REQUEST_MAX_RETRIES`**: Specifies the maximum number of retries with exponential backoff. Default is 7 retries.

**Important note**: The client-side HTTP request timeout defaults to 120 seconds, which differs from the server-side default timeout of 597 seconds for CPU and GPU serving endpoints. Adjust the MLflow environment variables accordingly if your workload is expected to exceed the 120-second client-side timeout. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Debugging MLflow Client-Side Timeouts

To determine if a timeout is caused by an MLflow environment variable configuration:

1. **Test the model locally** using sample inputs in a notebook to confirm it works as expected before registering and deploying. Examine the time it takes to process requests. If requests take longer than the default timeouts or you see a `"timed out"` message (e.g., `Timed out while evaluating the model. Verify that the model evaluates within the timeout.`), the issue is client-side.
2. **Test the model serving endpoint** using POST requests. Check the **Service Logs** for your endpoint or the inference tables if enabled. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Configuring MLflow Environment Variables

Configure MLflow environment variables using the Serving UI or programmatically:

- **Serving UI**: Select the endpoint, click **Edit**, expand **Advanced configuration**, and add the relevant MLflow timeout environment variable.
- **Python**: Set the environment variable programmatically before making requests. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Client-Side Timeouts: Third-Party Client APIs

Client-side timeouts can also originate from third-party client APIs used in model pipelines, such as [custom PyFunc models](/concepts/custom-mlflow-pyfunc-model.md) or PyFunc custom schema agents. These timeouts typically return error messages containing `"timed out"` or `4xx Bad Request`. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Debugging Third-Party Client Timeouts

1. **Test the model locally** with sample inputs in a notebook. If you see a `"timed out"` message (e.g., `APITimeoutError: Request timed out.`), adjust the relevant timeout parameters for the third-party client.
2. **Test the model serving endpoint** using POST requests. Check the **Service Logs** or inference tables for details. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### OpenAI Client Example

When establishing an [OpenAI client](/concepts/openai-client-compatibility.md), you can configure the `timeout` parameter to change the maximum time before a request times out on the client side. The default and maximum timeout for an OpenAI client is 10 minutes. ^[debug-model-serving-timeouts-databricks-on-aws.md]

```python
from openai import OpenAI
import os

DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')

client = OpenAI(
    timeout=10,  # Number of seconds before client times out
    api_key=DATABRICKS_TOKEN,
    base_url="<WORKSPACE_URL>/serving-endpoints"
)

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are an AI assistant"},
        {"role": "user", "content": "Tell me about Large Language Models."}
    ],
    model="model_name",
    max_tokens=256
)
```

For the OpenAI client, you can work around the maximum timeout window by enabling [streaming](/concepts/mosaic-streaming.md). ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Other Timeouts

### Idle Endpoints Warming Up

If an endpoint is scaled to 0 and receives a request that warms it up, the warm-up process could potentially lead to a client-side timeout if it takes too long. This is a common cause of timeouts in pipelines that leverage steps like calls to provisioned throughput endpoints or AI Search indices. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Connection Timeout

Connection timeouts relate to the time a client waits to establish a connection with the server. If the connection is not established within this time, the client cancels the attempt. Check the service logs and inference tables of the model serving endpoint for any connection timeouts. The messaging varies by service. ^[debug-model-serving-timeouts-databricks-on-aws.md]

For example, a `SocketTimeout` for a service reading/writing to a SQL endpoint over a JDBC connection may appear as:
```
jdbc:spark://<server-hostname>:443;HttpPath=<http-path>;TransportMode=http;SSL=1[;property=value[;property=value]];SocketTimeout=300
```

Look for error messages containing `"timed out"` or `"timeout"`. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Rate Limits

Multiple requests made over the rate limit of an endpoint might lead to failure for additional requests. See [Resource and payload limits](/concepts/model-serving-resource-and-payload-limits.md) for rate limits based on endpoint types. For third-party clients, review the documentation of the specific client you are using. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [Debug after container build failure](/concepts/container-build-debugging-for-model-serving.md)
- [Custom PyFunc Models](/concepts/custom-mlflow-pyfunc-model.md)
- PyFunc Custom Schema Agents
- [Resource and Payload Limits](/concepts/model-serving-resource-and-payload-limits.md)
- Scale to Zero
- Streaming Completions
- [Inference Tables](/concepts/inference-tables.md)

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
