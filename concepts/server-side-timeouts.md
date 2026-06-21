---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad43f7772e64a21dc22c8a943844568a7156ef9940d095e8c44e12dc156604d5
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - server-side-timeouts
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Server-Side Timeouts
description: Default request timeout durations on the server side of Databricks Model Serving endpoints, varying by endpoint type (CPU vs GPU with different sizes).
tags:
  - model-serving
  - server-side
  - timeouts
timestamp: "2026-06-19T18:16:33.395Z"
---

# Server-Side Timeouts

**Server-side timeouts** occur when a request to a model serving endpoint takes longer than the server's configured maximum wait time, causing the server to terminate the request before a response is returned. These timeouts are distinct from client-side timeouts, which are controlled by the calling application's timeout settings. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Identifying Server-Side Timeouts

If your model serving endpoint appears healthy according to the **Events** and **Logs** tabs, but requests consistently fail at a specific time limit, the timeout is likely server-side. A request that consistently fails at the server's timeout limit indicates a server-side timeout, whereas a request that fails earlier than that limit may be caused by configuration issues. ^[debug-model-serving-timeouts-databricks-on-aws.md]

To confirm a server-side timeout, compare the failure time of your requests against the default server-side timeout limits for your endpoint type. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Default Server-Side Timeout Limits

The default server-side timeout varies depending on the type of model serving endpoint. The following table shows the default server-side timeouts for requests sent to model serving endpoints:

| Endpoint Type | Default Server-Side Timeout |
|---------------|----------------------------|
| CPU serving endpoints | 597 seconds |
| GPU serving endpoints | 597 seconds |

^[debug-model-serving-timeouts-databricks-on-aws.md]

## Troubleshooting

If you suspect a server-side timeout, take the following steps:

1. **Check service logs**: Examine the service logs to determine if there are any other errors that might explain the timeout behavior. ^[debug-model-serving-timeouts-databricks-on-aws.md]
2. **Test the model locally**: Confirm that the model works locally (for example, from a notebook) or has worked on previous requests with earlier versions. ^[debug-model-serving-timeouts-databricks-on-aws.md]
3. **Compare with client-side timeouts**: Note that the default client-side timeout for [MLflow](/concepts/mlflow.md) HTTP requests is 120 seconds, which differs from the server-side default of 597 seconds. If your workload exceeds 120 seconds, you may experience a client-side timeout before the server-side timeout is reached. Adjust MLflow environment variables accordingly if you expect your workload to exceed the client-side timeout. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Concepts

- [Model Deployment Timeouts](/concepts/model-deployment-timeouts.md) — Timeouts that occur during the model deployment process
- Client-Side Timeouts — Timeouts controlled by the calling application or client library
- [MLflow HTTP Request Timeout](/concepts/mlflow-http-request-timeout-configuration.md) — The MLflow environment variable that controls client-side timeout behavior
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The infrastructure that hosts and serves models
- [Debug Model Serving](/concepts/model-serving.md) — General debugging approaches for model serving issues

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
