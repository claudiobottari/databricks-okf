---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5016e848af75afd5c5c913003d169098a023828fe70195b487067e859de72d1f
  pageDirectory: concepts
  sources:
    - tracing-mistral-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mistral-ai-python-sdk
    - MAPS
    - Mistral AI
    - Mistral AI Client
  citations:
    - file: tracing-mistral-databricks-on-aws.md
title: Mistral AI Python SDK
description: The official Mistral AI Python client library (mistralai) that provides a chat completion API for interacting with Mistral's large language models.
tags:
  - mistral-ai
  - python-sdk
  - llm
  - api
timestamp: "2026-06-19T23:12:25.630Z"
---

# Mistral AI Python SDK

The **Mistral AI Python SDK** is a client library that provides a Python interface to the Mistral AI API. It enables developers to interact with Mistral’s language models programmatically, including capabilities such as chat completion. On Databricks, the SDK is commonly used together with [MLflow](/concepts/mlflow.md) to trace and monitor model interactions. ^[tracing-mistral-databricks-on-aws.md]

## Auto‑Tracing with [MLflow](/concepts/mlflow.md)

When used on Databricks, the Mistral AI Python SDK can be integrated with MLflow’s auto‑tracing feature by calling `mlflow.mistral.autolog()`. This automatically captures [Traces](/concepts/traces.md) for subsequent calls to the SDK, such as `client.chat.complete()`, allowing full visibility into prompts, responses, and latency within the [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-mistral-databricks-on-aws.md]

## Setup on Databricks

To use the SDK with tracing on Databricks, the [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) must be set to `"databricks"` and an experiment path specified: ^[tracing-mistral-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].mistral.autolog()
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/mistral-demo")
```

After this configuration, [Traces](/concepts/traces.md) of Mistral API calls are automatically recorded in the specified experiment.

## Creating a Client

A Mistral client is instantiated by providing an API key, typically sourced from the environment variable `MISTRAL_API_KEY`: ^[tracing-mistral-databricks-on-aws.md]

```python
from mistralai import Mistral
client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
```

## Chat Completion

The SDK provides the `client.chat.complete()` method to send a conversation to a Mistral model and receive a generated response. The method accepts a model identifier (e.g., `"mistral-small-latest"`) and a list of messages with `role` and `content` fields. ^[tracing-mistral-databricks-on-aws.md]

```python
chat_response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {
            "role": "user",
            "content": "Who is the best French painter? Answer in one short sentence.",
        },
    ],
)
```

The response object contains a `choices` list; the generated text is accessed via `chat_response.choices[0].message`. ^[tracing-mistral-databricks-on-aws.md]

## Related Concepts

- [Mistral AI](/concepts/mistral-ai-python-sdk.md) – The company and model family behind the SDK.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Mechanism for recording and inspecting LLM calls.
- [LLM Observability](/concepts/genai-observability.md) – Monitoring and debugging of language model interactions.
- Environment Variables – Recommended way to supply API keys securely.

## Sources

- tracing-mistral-databricks-on-aws.md

# Citations

1. [tracing-mistral-databricks-on-aws.md](/references/tracing-mistral-databricks-on-aws-6af10854.md)
