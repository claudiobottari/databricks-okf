---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62a5465b48c3f1e6cadbee21af1a4af5f380c36d078c887cdd2c771f9556a733
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - third-party-client-api-timeouts
    - TCAT
    - third-party client APIs
    - Third-party client API configurations
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Third-Party Client API Timeouts
description: Timeouts caused by third-party client APIs (e.g., OpenAI Python client) used within custom PyFunc model pipelines, and how to configure their timeout parameters.
tags:
  - model-serving
  - third-party
  - timeouts
  - pyfunc
timestamp: "2026-06-19T18:16:42.649Z"
---

# Third-Party Client API Timeouts

**Third-Party Client API Timeouts** occur when a model serving endpoint uses external APIs (such as OpenAI, Anthropic, or other services) within its pipeline, and the client-side timeout configuration for those third-party APIs is exceeded before the request completes.

## Overview

Client-side timeouts from third-party client APIs typically return error messages containing **"timed out"** or **4xx Bad Request**. These timeouts can impact model serving endpoints that consist of pipelines using third-party client APIs, such as [custom PyFunc models](/concepts/custom-mlflow-pyfunc-model.md) or PyFunc custom schema agents. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Identifying Third-Party Client API Timeouts

To determine if a timeout is caused by third-party client APIs used in your model pipeline:

1. **Test the model locally** with sample inputs in a notebook.
   - If you see a **"timed out"** message, adjust any relevant parameters for the third-party client's timeout window.
   - Example error message: `APITimeoutError: Request timed out.`

2. **Test the model serving endpoint** using POST requests.
   - Check the **Service Logs** for your endpoint or the inference tables if you enabled them.
   - For inference table schema details, see Unity AI Gateway-enabled inference table schema.

^[debug-model-serving-timeouts-databricks-on-aws.md]

## OpenAI Client Example

When establishing an [OpenAI client](/concepts/openai-client-compatibility.md), you can configure the `timeout` parameter to change the maximum time before a request times out on the client-side. The default and maximum timeout for an OpenAI client is 10 minutes. ^[debug-model-serving-timeouts-databricks-on-aws.md]

The following example highlights how to configure a third-party client API's timeout:

```python
%pip install openai
dbutils.library.restartPython()

from openai import OpenAI
import os

# How to get your Databricks token: https://docs.databricks.com/en/dev-tools/auth/pat.html
DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')

client = OpenAI(
    timeout=10, # Number of seconds before client times out
    api_key=DATABRICKS_TOKEN,
    base_url="<WORKSPACE_URL>/serving-endpoints"
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are an AI assistant"
        },
        {
            "role": "user",
            "content": "Tell me about Large Language Models."
        }
    ],
    model="model_name",
    max_tokens=256
)
```

^[debug-model-serving-timeouts-databricks-on-aws.md]

For the OpenAI client, you can work around the maximum timeout window by enabling [streaming](/concepts/mosaic-streaming.md). ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Timeout Issues

### Idle Endpoints Warming Up

If an endpoint is scaled to 0 and receives a request that warms it up, it could potentially lead to a client-side timeout if the warm-up takes too long. This can be a cause of timeouts in pipelines that leverage steps like calls to provisioned throughput endpoints or AI Search indices. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Connection Timeout

Connection timeouts are related to the time a client waits to establish a connection with the server. If the connection is not established within this time, the client cancels the attempt. Check the service logs and inference tables of the Model Serving endpoint for any connection timeouts. The messaging varies by service. ^[debug-model-serving-timeouts-databricks-on-aws.md]

### Rate Limits

Multiple requests made over the rate limit of an endpoint might lead to failure for additional requests. For third-party clients, Databricks recommends reviewing the documentation of the third-party client you are using. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Concepts

- [Model Serving Timeouts](/concepts/model-serving-endpoint-timeouts.md) — Overview of all timeout types on Databricks
- [Server-Side Timeouts](/concepts/server-side-timeouts.md) — Timeouts originating from the serving infrastructure
- [MLflow HTTP Request Timeout](/concepts/mlflow-http-request-timeout-configuration.md) — Client-side timeout configuration for MLflow
- [Custom PyFunc Models](/concepts/custom-mlflow-pyfunc-model.md) — Model pipelines that may use third-party APIs
- [Debug Model Serving Endpoints](/concepts/model-serving-endpoint.md) — General debugging guidance

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
