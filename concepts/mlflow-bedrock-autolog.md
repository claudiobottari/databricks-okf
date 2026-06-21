---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed566222cc1e9da8b82dc10a47a9503612e53cd98a3a632e53d0f503bdc610de
  pageDirectory: concepts
  sources:
    - tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-bedrock-autolog
    - MBA
  citations:
    - file: tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
title: MLflow Bedrock Autolog
description: A function (mlflow.bedrock.autolog) that enables automatic tracing of Amazon Bedrock LLM invocations, capturing prompts, responses, latencies, model names, metadata, function calls, and exceptions.
tags:
  - mlflow
  - tracing
  - bedrock
timestamp: "2026-06-19T23:09:14.695Z"
---

Here is the wiki page for "[MLflow](/concepts/mlflow.md) Bedrock Autolog".

---

## [MLflow](/concepts/mlflow.md) Bedrock Autolog

**MLflow Bedrock Autolog** is a feature within [MLflow](/concepts/mlflow.md) that enables automatic [Tracing](/concepts/mlflow-tracing.md) for calls to Amazon Bedrock. By calling the `mlflow.bedrock.autolog()` function, [MLflow](/concepts/mlflow.md) automatically captures [Traces](/concepts/traces.md) for large language model (LLM) invocations and logs them to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

### Overview

When enabled, `mlflow.bedrock.autolog()` instruments the Amazon Bedrock runtime client so that every call to supported APIs is automatically traced. [MLflow](/concepts/mlflow.md) captures prompts, completion responses, latencies, the model name, and additional metadata such as `temperature` or `max_tokens` if specified. It also captures any function calling metadata returned in the response and any exceptions that are raised. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

On Serverless Compute clusters, autologging is not automatically enabled; you must explicitly call `mlflow.bedrock.autolog()` to activate tracing for this integration. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

### Supported APIs

[MLflow](/concepts/mlflow.md) supports [Automatic Tracing](/concepts/automatic-tracing.md) for the following Amazon Bedrock runtime APIs:

- `converse`
- `converse_stream`
- `invoke_model`
- `invoke_model_with_response_stream`

^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

### Basic Example

The following example enables autologging, sets the [MLflow tracking URI](/concepts/mlflow-tracking-uri.md) to a Databricks workspace, creates a Bedrock runtime client, and makes a `converse` call. The trace is automatically logged to the experiment.

```python
import boto3
import [[mlflow|MLflow]]

# Enable auto-tracing for Amazon Bedrock
[[mlflow|MLflow]].bedrock.autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] to Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/bedrock-tracing-demo")

# Create a boto3 client for invoking the Bedrock API
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="<REPLACE_WITH_YOUR_AWS_REGION>",
)

response = bedrock.converse(
    modelId="anthropic.claude-3-5-sonnet-20241022-v2:0",
    messages=[...],
    inferenceConfig={...},
)
```

^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

### Prerequisites

To use [MLflow](/concepts/mlflow.md) Bedrock Autolog, you must install [MLflow](/concepts/mlflow.md) (version 3 or later is highly recommended) and the AWS SDK for Python (`boto3`). For development environments, install the full [MLflow](/concepts/mlflow.md) package with Databricks extras:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" boto3
```

^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

### Raw Inputs and Outputs

By default, [MLflow](/concepts/mlflow.md) renders [Traces](/concepts/traces.md) in a rich chat-like UI for the `converse` and `converse_stream` APIs. To view the raw input and output payload (including configuration parameters), click the **Inputs / Outputs** tab in the [MLflow](/concepts/mlflow.md) UI. For the `invoke_model` and `invoke_model_with_response_stream` APIs, only the `Inputs / Outputs` tab is displayed. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

### Streaming

[MLflow](/concepts/mlflow.md) supports tracing streaming calls to Amazon Bedrock. The trace shows the aggregated output in the `Chat` tab, while individual chunks are displayed in the `Events` tab. [MLflow](/concepts/mlflow.md) does not create a span immediately when the streaming response is returned; instead, it creates a span when the streaming chunks are consumed (e.g., in a for-loop). ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

### Function Calling Agent

[MLflow Tracing](/concepts/mlflow-tracing.md) automatically captures function calling metadata. Combined with the `@mlflow.trace` decorator (using `SpanType.TOOL` or `SpanType.AGENT`), you can define a function-calling agent (ReAct) and fully trace its execution. [MLflow](/concepts/mlflow.md) handles call-chain resolution and records execution metadata. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

### Disabling Auto-Tracing

Auto tracing for Amazon Bedrock can be disabled globally by calling:

```python
[[mlflow|MLflow]].bedrock.autolog(disable=True)
# or
[[mlflow|MLflow]].autolog(disable=True)
```

^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The framework for capturing and visualizing LLM call [Traces](/concepts/traces.md).
- Amazon Bedrock – The managed service providing foundation models.
- [Automated Logging (autolog)](/concepts/automatic-tracing-autolog.md) – The general [MLflow](/concepts/mlflow.md) mechanism that enables automatic logging without explicit instrumentation.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – Relevant for controlling [MLflow](/concepts/mlflow.md) serverless workload spending on Databricks.
- Function Calling Agent – A pattern for building ReAct-style agents that [MLflow](/concepts/mlflow.md) can trace.

### Sources

- tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md

# Citations

1. [tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md](/references/tracing-amazon-bedrock-with-mlflow-databricks-on-aws-2f3942c6.md)
