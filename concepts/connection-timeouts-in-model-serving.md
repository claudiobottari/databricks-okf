---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9785552d9bbe13ded7f507ff08fcd9b06840d7cde05cc8eca8829266285a8ba3
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - connection-timeouts-in-model-serving
    - CTIMS
    - connection-timeouts-in-model-serving-pipelines
    - CTIMSP
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Connection Timeouts in Model Serving
description: Timeouts related to establishing a network connection between a client and the model serving server, commonly seen with JDBC/SQL endpoints and socket connections.
tags:
  - model-serving
  - connection
  - timeouts
  - networking
timestamp: "2026-06-18T15:11:28.561Z"
---

# Connection Timeouts in Model Serving

**Connection Timeouts in Model Serving** refers to the failure of a client to establish a network connection with a model serving endpoint within a predetermined time window. When the connection is not established within this time, the client cancels the attempt, resulting in a timeout error.

## Overview

Connection timeouts are distinct from server-side request processing timeouts or model deployment timeouts. They occur specifically during the initial handshake phase between the client and the server, before any actual request processing begins. The error messaging varies by service and client implementation. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Identifying Connection Timeouts

To determine if a timeout is a connection timeout, check the service logs and inference tables of the Model Serving endpoint for timeout-related errors. Common indicators include error messages containing the terms **"timed out"** or **"timeout"**. ^[debug-model-serving-timeouts-databricks-on-aws.md]

For example, a `SocketTimeout` error for a service reading or writing to a SQL endpoint over a JDBC connection may appear as follows: ^[debug-model-serving-timeouts-databricks-on-aws.md]

```
jdbc:spark://<server-hostname>:443;HttpPath=<http-path>;TransportMode=http;SSL=1[;property=value[;property=value]];SocketTimeout=300
```

## Common Causes

Connection timeouts can be caused by several factors related to the clients used in a model pipeline: ^[debug-model-serving-timeouts-databricks-on-aws.md]

- **Idle endpoints warming up**: If an endpoint is scaled to 0 and receives a request that triggers a warm-up, the warm-up process may take longer than the client's connection timeout. This is especially relevant in pipelines that leverage steps like calls to provisioned throughput endpoints or AI Search indices. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Network configuration issues**: Firewalls, DNS resolution delays, or network congestion can prevent timely connection establishment.
- **Client configuration**: Third-party client APIs or [MLflow](/concepts/mlflow.md) HTTP request configurations may have timeout windows that are too short for the expected connection time.

## Debugging Connection Timeouts

### Check Service Logs

Review the **Service Logs** for the model serving endpoint or the inference tables (if enabled) to identify connection timeout errors. For inference table schema details, see Unity AI Gateway-enabled inference table schema. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Test Locally

Test the model locally with sample inputs in a notebook to confirm it works as expected. If you encounter a **_"timed out"_** message, adjust relevant parameters for the client's timeout window. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Test with POST Requests

Send test POST requests to the model serving endpoint and examine the response times to determine whether the timeout occurs at connection establishment or during request processing. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Mitigation Strategies

- **Adjust client timeout parameters**: Configure the timeout settings in your client API to accommodate longer connection establishment times. For example, when using the [OpenAI client](/concepts/openai-client-compatibility.md), you can set the `timeout` parameter to a higher value. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Pre-warm idle endpoints**: Ensure that endpoints scaled to 0 are warmed up before sending production requests, or adjust scale-to-zero settings to prevent cold starts during critical operations.
- **Review network infrastructure**: Check for firewall rules, proxy configurations, or DNS issues that may delay connection establishment.
- **Monitor third-party client configurations**: For model serving endpoints that consist of pipelines using third-party client APIs — such as [custom PyFunc models](/concepts/custom-mlflow-pythonmodel.md) or PyFunc custom schema agents — review the timeout configurations of those clients. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Concepts

- [Server-Side Timeouts](/concepts/server-side-timeout.md) — Timeouts that occur during request processing after a connection is established.
- [Model Deployment Timeouts](/concepts/model-deployment-timeouts.md) — Timeouts that occur during container build or model deployment.
- Client-Side Timeouts — General timeouts originating from client configuration, including MLflow environment variables.
- [Rate Limits](/concepts/rate-limits-and-timeouts-in-model-serving.md) — Restrictions on request frequency that can lead to request failures.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The endpoints that serve models and may experience timeouts.
- [Resource and Payload Limits](/concepts/model-serving-resource-and-payload-limits.md) — Constraints that affect endpoint behavior and timeout likelihood.

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
