---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 775b18bf85fdbb61ebf8c66861a84687b9c1c11c2cd4071d55dcf68872179567
  pageDirectory: concepts
  sources:
    - automatic-tracing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-foundation-model-api-tracing-via-openai-client
    - DFMATVOC
  citations:
    - file: automatic-tracing-databricks-on-aws.md
title: Databricks Foundation Model API Tracing via OpenAI Client
description: Technique of using the OpenAI Python client configured with Databricks credentials and endpoints to query Databricks-hosted models (e.g., Llama 4 Maverick) while MLflow automatically traces those calls.
tags:
  - databricks
  - openai
  - foundation-models
  - tracing
timestamp: "2026-06-19T22:10:44.930Z"
---

```yaml
---
title: Databricks Foundation Model API Tracing via OpenAI Client
summary: Using the OpenAI Python client configured with Databricks credentials and a serving‑endpoint base URL to automatically trace calls to Databricks Foundation Model APIs through MLflow’s `openai.autolog()`.
sources:
  - automatic-tracing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:30:09.898Z"
updatedAt: "2026-06-18T14:30:09.898Z"
tags:
  - mlflow
  - foundation-model-api
  - openai
  - databricks
aliases:
  - databricks-foundation-model-api-tracing-via-openai-client
  - DFMATVOC
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# Databricks Foundation Model API Tracing via OpenAI Client

**Databricks Foundation Model API Tracing via OpenAI Client** refers to the method of using [[MLflow]] automatic tracing to capture and monitor API calls made to [[Databricks Foundation Model APIs]] through the standard [[OpenAI client compatibility|OpenAI Python client library]]. This approach enables teams to instrument their GenAI applications with minimal code changes while preserving the familiar OpenAI SDK interface.

## Overview

Databricks provides access to foundation models — such as Llama 4 Maverick — through serving endpoints that expose a compatible OpenAI API. By configuring the standard OpenAI client with Databricks credentials and enabling `mlflow.openai.autolog()`, every inference request made through the client becomes part of an [[MLflow Trace]]. ^[automatic-tracing-databricks-on-aws.md]

## Setup

### Prerequisites

Install the required packages in a Databricks notebook: ^[automatic-tracing-databricks-on-aws.md]

```python
%pip install --upgrade "mlflow[databricks]>=3.1" openai>=1.0.0
dbutils.library.restartPython()
```

### Configure Credentials

Set the necessary environment variables: ^[automatic-tracing-databricks-on-aws.md]

```python
import os
os.environ["OPENAI_API_KEY"] = "your-api-key"
```

## Basic Automatic Tracing Example

The following example enables automatic tracing for OpenAI agents connecting to Databricks Foundation Model APIs: ^[automatic-tracing-databricks-on-aws.md]

```python
import mlflow
import os
from openai import OpenAI

# Databricks Foundation Model APIs use Databricks authentication.
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/databricks-sdk-autolog-example")

# Enable auto-tracing for OpenAI (which will trace Databricks Foundation Model API calls)
mlflow.openai.autolog()

# Create OpenAI client configured for Databricks
client = OpenAI(
    api_key=os.environ.get("DATABRICKS_TOKEN"),
    base_url=f"{os.environ.get('DATABRICKS_HOST')}/serving-endpoints"
)

# Query Llama 4 Maverick using OpenAI client
response = client.chat.completions.create(
    model="databricks-llama-4-maverick",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the key features of [MLflow Tracing](/concepts/mlflow-tracing.md)?"}
    ],
    max_tokens=150,
    temperature=0.7
)

print(response.choices[0].message.content)
# Your calls to Databricks Foundation Model APIs are automatically traced!
```

## How It Works

Calling `mlflow.openai.autolog()` once at the start of your application automatically instruments any subsequent calls made through the OpenAI client. Each `client.chat.completions.create()` invocation generates a Span within the current [[MLflow Trace]], capturing: ^[automatic-tracing-databricks-on-aws.md]

- The model name and endpoint configuration
- Input messages (prompts)
- Output responses
- Token usage (if available)
- Latency and timing information

## Combining with Manual Tracing

You can mix automatic tracing with manual @mlflow.trace decorators to create unified traces that capture custom business logic alongside the auto-traced foundation model calls. This is useful for: ^[automatic-tracing-databricks-on-aws.md]

- Multi-step workflows
- Pre-processing or post-processing logic
- Multi-agent systems with different providers

```python
import mlflow
from mlflow.entities import SpanType

mlflow.openai.autolog()

@mlflow.trace(span_type=SpanType.CHAIN)
def process_user_query(query: str):
    # First call: analyze the query
    analysis = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Analyze the user's query."},
            {"role": "user", "content": query}
        ]
    )
    analysis_result = analysis.choices[0].message.content

    # Second call: generate response based on analysis
    if "factual" in analysis_result.lower():
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Provide a factual response."},
                {"role": "user", "content": query}
            ]
        )
    else:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Provide a creative response."},
                {"role": "user", "content": query}
            ]
        )
    return response.choices[0].message.content
```

## Related Concepts

- [MLflow Automatic Tracing](/concepts/mlflow-automatic-tracing.md) — The general mechanism for instrumenting supported frameworks
- [Manual Tracing](/concepts/manual-tracing.md) — Using decorators for custom spans
- [Databricks Foundation Model APIs](/concepts/databricks-foundation-model-apis.md) — The serving endpoints behind the scenes
- OpenAI Python Library — The client SDK used for connectivity
- [[MLflow Trace|MLflow Traces]] — The data structure capturing the full execution path
- Serverless Autologging — Note that autologging must be explicitly enabled on serverless compute

## Sources

- automatic-tracing-databricks-on-aws.md

# Citations

1. [automatic-tracing-databricks-on-aws.md](/references/automatic-tracing-databricks-on-aws-ff944f8c.md)
