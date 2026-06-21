---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f5694242091ad4feb80a4f96b649c37f4b421bf316c89e3b3e0da772492836c
  pageDirectory: concepts
  sources:
    - get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-instrumentation-with-mlflowopenaiautolog
    - AIWM
  citations:
    - file: get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
title: Automatic Instrumentation with mlflow.openai.autolog()
description: A feature that automatically captures trace data from OpenAI SDK calls (including Databricks-hosted LLMs) without requiring manual instrumentation of each API invocation.
tags:
  - instrumentation
  - openai
  - mlflow
  - autologging
timestamp: "2026-06-19T10:44:43.249Z"
---

# Automatic Instrumentation with mlflow.openai.autolog()

**Automatic Instrumentation with `mlflow.openai.autolog()`** is a feature of [MLflow Tracing](/concepts/mlflow-tracing.md) that automatically captures trace data from OpenAI SDK calls without requiring manual instrumentation code. By calling `mlflow.openai.autolog()`, developers enable MLflow to intercept and record every OpenAI API request made by the application, including model selection, token usage, timing, and response content. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Overview

The `mlflow.openai.autolog()` function is a convenience method that simplifies [GenAI application observability](/concepts/genai-observability.md). Instead of wrapping individual API calls with tracing decorators or manual span creation, developers enable automatic instrumentation once at application startup. All subsequent calls through the OpenAI SDK — including chat completions, embeddings, and other endpoints — are automatically traced and recorded as spans within an MLflow trace. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Usage

### Basic Setup

The following example shows how to enable automatic instrumentation for an application that uses OpenAI's chat completions API: ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

```python
import mlflow
from databricks_openai import DatabricksOpenAI

# Enable MLflow's autologging to instrument your application with Tracing
mlflow.openai.autolog()

# Set up MLflow tracking to Databricks
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/docs-demo")

# Create an OpenAI client
client = DatabricksOpenAI()

# This call is automatically instrumented by mlflow.openai.autolog()
response = client.chat.completions.create(
    model="databricks-claude-sonnet-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is MLflow?"},
    ],
)
```

### Combining with Manual Tracing

For applications with custom logic beyond OpenAI SDK calls, `mlflow.openai.autolog()` can be combined with the [@mlflow.trace decorator](/concepts/mlflowtrace-decorator.md) to capture the full application flow. The decorator instruments the entry point function, while autologging captures the details of each OpenAI call: ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

```python
@mlflow.trace
def my_app(input: str):
    # This call is automatically instrumented by mlflow.openai.autolog()
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input},
        ],
    )
    return response.choices[0].message.content
```

## What Gets Traced

When `mlflow.openai.autolog()` is enabled, each OpenAI API call generates a child span within the application's trace. The captured information includes: ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

- **Inputs**: The messages and parameters sent to the model
- **Outputs**: The response received from the model
- **Attributes**: Metadata such as model name, token counts, and timing information

This automatic instrumentation provides useful information about application behavior, including what was asked, what response was generated, how long the request took, and how many tokens were used (affecting cost). ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Troubleshooting

### No Traces Appearing

If traces do not appear in the [MLflow Experiment](/concepts/mlflow-experiment.md) after running your application: ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

1. Verify that `mlflow.openai.autolog()` is called **before** any OpenAI SDK calls.
2. Confirm that the MLflow tracking URI and experiment ID are correctly set.
3. Check that the Databricks host and token environment variables (`DATABRICKS_HOST`, `DATABRICKS_TOKEN`) are properly configured.

### Incomplete Trace Data

If traces are missing the OpenAI API call details (only showing the root function span but not the child OpenAI span): ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

1. Ensure `mlflow.openai.autolog()` is called before the OpenAI client is instantiated.
2. Verify that the correct OpenAI client is being used (e.g., `DatabricksOpenAI()` for Databricks-hosted models or `openai.OpenAI()` for OpenAI-hosted models).

### Authentication Errors

If you encounter authentication errors when traces are sent to Databricks: ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

1. Verify that the `DATABRICKS_TOKEN` environment variable contains a valid personal access token.
2. Confirm the `DATABRICKS_HOST` environment variable points to the correct workspace URL.
3. Ensure the token has the necessary permissions to write traces to the experiment.

## Best Practices

- **Call autolog early**: Invoke `mlflow.openai.autolog()` at the start of your application, before any SDK calls, to ensure all API requests are captured. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]
- **Combine with manual tracing**: Use the `@mlflow.trace` decorator on your application's entry points to create a root span that encompasses the entire workflow, with OpenAI calls appearing as child spans. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]
- **Set environment variables**: Configure `DATABRICKS_HOST`, `DATABRICKS_TOKEN`, `MLFLOW_TRACKING_URI`, `MLFLOW_REGISTRY_URI`, and `MLFLOW_EXPERIMENT_ID` as environment variables to connect your local development environment to Databricks. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying observability framework for GenAI applications
- [Manual Tracing with @mlflow.trace](/concepts/manual-tracing.md) — Adding custom spans to complement automatic instrumentation
- OpenAI Integration — Detailed documentation of the OpenAI autologging integration
- GenAI Application Observability — Best practices for monitoring AI applications
- [MLflow Experiment](/concepts/mlflow-experiment.md) — The container where traces are stored and visualized

## Limitations

- Automatic instrumentation only captures calls made through the OpenAI SDK. Custom logic, preprocessing, or postprocessing steps are not traced unless manually instrumented with `@mlflow.trace`. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]
- The autologging function must be called before any OpenAI client is instantiated or any API call is made. ^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

## Sources

- get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md

# Citations

1. [get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws-58181913.md)
