---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee222dbd3706f4467bd867a680e00b421b67777a3721ab79d4157988f7fd3f50
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - client-side-timeout-third-party-client-apis
    - CT–TPCA
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Client-Side Timeout – Third Party Client APIs
description: Timeouts from third-party API clients (e.g., OpenAI SDK) used in custom PyFunc model pipelines, and how to configure their timeout parameters.
tags:
  - databricks
  - model-serving
  - timeouts
  - third-party
  - api
timestamp: "2026-06-19T09:55:47.673Z"
---

# Client-Side Timeout – Third Party Client APIs

**Client-Side Timeout – Third Party Client APIs** refers to timeouts that occur when a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) makes requests to external services through third-party client libraries (such as OpenAI, Anthropic, or other API clients) and those clients exceed their configured timeout windows. These timeouts are distinct from server-side timeouts or MLflow configuration timeouts and require debugging the third-party client configuration directly.

## Overview

Client-side timeouts from third-party client APIs typically return error messages containing **"timed out"** or **4xx Bad Request**. These errors can affect model serving endpoints that consist of pipelines using third-party client APIs, such as [custom PyFunc models](/concepts/custom-mlflow-pyfunc-model.md) or PyFunc custom schema agents. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Identifying Third-Party Client Timeouts

To determine if a timeout is caused by third-party client APIs used in your model pipeline, follow these debugging steps:

1. **Test the model locally** with sample inputs in a notebook. If you see a **"timed out"** message in the notebook, adjust any relevant parameters for the third-party client's timeout window. An example error message is: `APITimeoutError: Request timed out.` ^[debug-model-serving-timeouts-databricks-on-aws.md]

2. **Test the model serving endpoint** using POST requests. Check the **Service Logs** for your endpoint or the inference tables (if enabled). For inference table schema details, see Unity AI Gateway-enabled inference table schema. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## OpenAI Client Example

When you establish an OpenAI client, you can configure the `timeout` parameter to change the maximum time before a request times out on the client side. The default and maximum timeout for an OpenAI client is 10 minutes. ^[debug-model-serving-timeouts-databricks-on-aws.md]

The following example shows how to configure a third-party client API timeout:

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

For the OpenAI client, you can work around the maximum timeout window by enabling [streaming completions](/concepts/chat-completions-api.md). ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Related Timeout Types

Third-party client timeout issues can compound with other timeout types:

- **[Model Deployment Timeouts](/concepts/model-deployment-timeouts.md)** – Timeouts during container build and model deployment
- **[Server-Side Timeouts](/concepts/server-side-timeouts.md)** – Timeouts from the model serving endpoint itself
- **MLflow Client-Side Timeouts** – Timeouts caused by MLflow environment variable configurations
- **Idle Endpoint Warm-Up** – If an endpoint is scaled to 0 and receives a request, the warm-up period can lead to client-side timeouts, especially in pipelines that make calls to [Provisioned throughput endpoints](/concepts/provisioned-throughput-endpoints.md) or AI Search indices
- **[Connection Timeouts](/concepts/connection-timeout.md)** – Timeouts related to establishing a connection with the server, such as `SocketTimeout` for JDBC connections
- **[Rate Limits](/concepts/rate-limits-and-timeouts-in-model-serving.md)** – Multiple requests exceeding the endpoint's rate limit may cause failures; review the documentation of any third-party client you are using

## Best Practices

- **Test locally first** before deploying to a serving endpoint to identify timeout issues early
- **Configure appropriate timeouts** for each third-party client based on expected response times
- **Enable streaming** where possible to work around maximum timeout windows
- **Monitor service logs and inference tables** for timeout-related error messages
- **Review third-party client documentation** for specific timeout configuration options and limits

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- [Custom PyFunc Models](/concepts/custom-mlflow-pyfunc-model.md)
- PyFunc Custom Schema Agents
- [Debug Model Serving](/concepts/model-serving.md)
- [Resource and Payload Limits](/concepts/model-serving-resource-and-payload-limits.md)

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
