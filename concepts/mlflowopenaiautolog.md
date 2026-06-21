---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 171916ac4876903dfc1d920a7e94c47422790bb0561dac1176c4e77e5d31a830
  pageDirectory: concepts
  sources:
    - get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
    - get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
    - tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflowopenaiautolog
    - MLflow OpenAI Flavor
  citations:
    - file: get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
    - file: get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
    - file: tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md
title: mlflow.openai.autolog()
description: Automatic instrumentation for OpenAI SDK calls that captures request details, responses, token counts, and timing without manual instrumentation code.
tags:
  - mlflow
  - openai
  - autologging
  - instrumentation
timestamp: "2026-06-19T19:00:30.171Z"
---

# `mlflow.openai.autolog()`

**`mlflow.openai.autolog()`** is an MLflow API function that enables automatic instrumentation of calls made with the OpenAI SDK. When invoked, it captures the details of every OpenAI API call — such as the model invoked, the messages sent, the response received, token usage, and timing — and records them as spans within an MLflow trace. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md, get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md, tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md]

## Overview

Autologging is the simplest way to add [MLflow Tracing](/concepts/mlflow-tracing.md) to an application that uses the OpenAI Python client. After calling `mlflow.openai.autolog()`, any subsequent call to `client.chat.completions.create()` or similar OpenAI methods is automatically traced without modifying the call site. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

This function is part of a broader MLflow ecosystem that provides autologging integrations for 20+ libraries, making it easy to instrument common GenAI and ML frameworks with minimal code changes.

## Usage

### Basic Setup

```python
import mlflow

# Enable auto-tracing for all OpenAI calls
mlflow.openai.autolog()
```

^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

### Example with a Databricks-hosted Model

The following example creates an OpenAI client connected to Databricks-hosted foundation models, enables autologging, and traces a simple chat completion: ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

```python
import mlflow
from databricks_openai import DatabricksOpenAI

mlflow.openai.autolog()
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/tracing-quickstart")

client = DatabricksOpenAI()

@mlflow.trace
def my_app(input: str):
    response = client.chat.completions.create(
        model="databricks-claude-sonnet-4",
        temperature=0.1,
        max_tokens=200,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input},
        ],
    )
    return response.choices[0].message.content

result = my_app(input="What is MLflow?")
print(result)
```

### Example with OpenAI-hosted Models

When using the standard OpenAI SDK (rather than the Databricks OpenAI client), ensure the `OPENAI_API_KEY` environment variable is set before calling autolog: ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

```python
import os
import openai

os.environ["OPENAI_API_KEY"] = "<YOUR_API_KEY>"

client = openai.OpenAI()
model_name = "gpt-4o-mini"

# Subsequent calls are now auto-traced
```

## What Gets Captured

When `mlflow.openai.autolog()` is active, each OpenAI API call produces a **child span** within the overall trace. This child span captures: ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

- **Inputs**: The messages sent to the model (system prompt, user messages, etc.)
- **Outputs**: The response received from the model
- **Attributes**: Metadata such as the model name, token counts, and timing information

When combined with the [@mlflow.trace decorator](/concepts/mlflowtrace-decorator.md) on the application's entry-point function, the resulting trace shows a hierarchy: the root span represents the application function's inputs and outputs, while the child span captures the OpenAI request in detail. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Adding Context to Autologged Traces

Autologged traces can be enriched with custom metadata and tags using mlflow.update_current_trace()|`mlflow.update_current_trace()` within the traced function body. This allows attaching user IDs, session IDs, deployment environment, app version, or any other context that helps with analysis and debugging. ^[tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md]

```python
@mlflow.trace
def my_app(user_id: str, session_id: str, message: str) -> str:
    mlflow.update_current_trace(
        metadata={
            "mlflow.trace.user": user_id,
            "mlflow.trace.session": session_id,
        },
        tags={"query_category": "chat"},
    )
    # OpenAI call is autologged as a child span
    response = chat_completion(message)
    return response
```

^[tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md]

## Searching and Analyzing Autologged Traces

Once traces are captured, they can be queried programmatically with mlflow.search_traces()|`mlflow.search_traces()`. The metadata and tags added alongside autologged spans — such as user IDs, session IDs, or app versions — can be used in filter strings and analyzed to understand user behavior, session flows, or deployment performance. ^[tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md]

```python
traces = mlflow.search_traces(
    filter_string="metadata.`mlflow.trace.user` = 'user-123'",
    order_by=["timestamp DESC"],
)
```

## Limitations and Notes

- Autologging captures **only SDK-level calls** (e.g., `client.chat.completions.create()`). Application-level orchestration logic (such as prompt construction or response processing) is **not** automatically traced unless the developer also applies `@mlflow.trace` to those functions. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]
- The API key for OpenAI-hosted models must be set in the environment *before* the client is created. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying observability system
- @mlflow.trace — Decorator for manual instrumentation
- mlflow.update_current_trace() — Adding custom context to traces
- mlflow.search_traces() — Querying captured traces
- Autologging integrations — Other supported library integrations
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Containers for organizing traces and runs

## Sources

- get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
- get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
- tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md

# Citations

1. [get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws-860f2761.md)
2. [get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws-58181913.md)
3. [tutorial-trace-and-analyze-users-and-environments-databricks-on-aws.md](/references/tutorial-trace-and-analyze-users-and-environments-databricks-on-aws-7504deef.md)
