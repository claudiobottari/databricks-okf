---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9934d943abd27fb2efe31bcd24e7d8751cf4e4da9f3bc07618543455dd57f334
  pageDirectory: concepts
  sources:
    - debug-model-serving-timeouts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - third-party-client-api-timeouts-in-model-serving-pipelines
    - TCATIMSP
  citations:
    - file: debug-model-serving-timeouts-databricks-on-aws.md
title: Third-Party Client API Timeouts in Model Serving Pipelines
description: Client-side timeouts caused by third-party client APIs (e.g., OpenAI) used within custom PyFunc model pipelines, and how to configure their timeout parameters.
tags:
  - model-serving
  - third-party-apis
  - timeouts
  - pyfunc
timestamp: "2026-06-18T15:11:16.964Z"
---

# Third-Party Client API Timeouts in Model Serving Pipelines

**Third-Party Client API Timeouts in Model Serving Pipelines** occur when a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) that uses a pipeline containing calls to external APIs (e.g., OpenAI, custom services) experiences client-side timeouts because the third-party client’s own timeout configuration is too short for the workload. These timeouts typically manifest as `"timed out"` or `4xx Bad Request` errors. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Causes

Third-party client API timeouts can affect model serving endpoints that consist of pipelines that use these client APIs, such as [custom PyFunc models](/concepts/custom-mlflow-pyfunc-model.md) and PyFunc custom schema agents. The timeout is configured on the client side (the code running inside the serving pipeline) and is independent of the server-side timeouts of the model serving endpoint itself. ^[debug-model-serving-timeouts-databricks-on-aws.md]

Common indicators:

- You see an error message like `APITimeoutError: Request timed out.` when testing locally.
- The request fails before reaching the server-side timeout limit.
- Multiple failures occur at a consistent duration that matches the configured client timeout.

## Debugging

To diagnose third-party client API timeout issues, follow these steps:

1. **Test the model locally with sample inputs** in a notebook. If you encounter a `"timed out"` message, adjust the relevant parameters for the third party client’s timeout window. ^[debug-model-serving-timeouts-databricks-on-aws.md]

2. **Test the model serving endpoint using POST requests** and examine the **Service Logs** (or [Inference Tables](/concepts/inference-tables.md) if enabled) for timeouts or errors. For inference table schema details, see the Unity AI Gateway documentation. ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Example: OpenAI Client

When using an OpenAI Python client, the `timeout` parameter controls the maximum time before a request times out on the client side. The default and maximum timeout for an OpenAI client is 10 minutes. ^[debug-model-serving-timeouts-databricks-on-aws.md]

The following example sets a 10‑second timeout to demonstrate how to adjust the parameter:

```python
from openai import OpenAI
import os

DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')

client = OpenAI(
    timeout=10,               # seconds
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

To work around a maximum timeout window, consider enabling [streaming completions](/concepts/chat-completions-api.md). ^[debug-model-serving-timeouts-databricks-on-aws.md]

## Best Practices

- **Review your third-party client’s documentation** for supported timeout values and any maximum limits. ^[debug-model-serving-timeouts-databricks-on-aws.md]
- **Set a realistic timeout** that accounts for the expected processing time of the pipeline, including external API calls.
- **Enable streaming** for long-running requests from the OpenAI client if you need to exceed the default 10‑minute maximum timeout.
- **Monitor logs** on the serving endpoint and capture client‑side timeouts in inference tables to help diagnose recurrent failures.
- **Separate concerns** by testing the external API interaction in isolation before integrating it into a serving pipeline.

## Related Concepts

- [Custom PyFunc Models](/concepts/custom-mlflow-pyfunc-model.md)
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- Client-Side Timeouts
- [MLflow HTTP Request Timeouts](/concepts/mlflow-http-request-timeout-configuration.md)
- Streaming Completions

## Sources

- debug-model-serving-timeouts-databricks-on-aws.md

# Citations

1. [debug-model-serving-timeouts-databricks-on-aws.md](/references/debug-model-serving-timeouts-databricks-on-aws-7b1685db.md)
