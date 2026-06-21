---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e955ed103d993b49d91ba6fc9bee6718aac63323740c534723b1d31445087990
  pageDirectory: concepts
  sources:
    - tracing-groq-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - groq-sdk-integration-with-mlflow
    - GSIWM
    - Groq SDK Integration
  citations:
    - file: tracing-groq-databricks-on-aws.md
title: Groq SDK Integration with MLflow
description: Integration enabling MLflow to automatically trace Groq chat completion requests
tags:
  - groq
  - mlflow
  - integration
  - tracing
timestamp: "2026-06-19T23:11:56.175Z"
---

# Groq SDK Integration with [MLflow](/concepts/mlflow.md)

**Groq SDK Integration with MLflow** provides [Automatic Tracing](/concepts/automatic-tracing.md) capability when using the Groq SDK, enabling developers to record and analyze LLM API calls made through Groq's inference platform. The integration is powered by [MLflow Tracing](/concepts/mlflow-tracing.md), which captures trace data for synchronous Groq API calls during interactive development.

## Enabling Auto-Tracing

To enable [Automatic Tracing](/concepts/automatic-tracing.md) for Groq, call [`mlflow.groq.autolog()`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).groq.html#mlflow.groq.autolog). Once enabled, any usage of the Groq SDK will automatically generate [Traces](/concepts/traces.md) that record the inputs, outputs, and metadata of API calls. ^[tracing-groq-databricks-on-aws.md]

```python
import groq
import [[mlflow|MLflow]]

# Turn on auto tracing for Groq
[[mlflow|MLflow]].groq.autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] on Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/groq-demo")
```

^[tracing-groq-databricks-on-aws.md]

**Important note:** On Serverless Compute clusters, autologging is not automatically enabled. You must explicitly call `mlflow.groq.autolog()` to enable [Automatic Tracing](/concepts/automatic-tracing.md) for this integration. ^[tracing-groq-databricks-on-aws.md]

## Supported API Calls

The integration supports synchronous API calls made through the Groq SDK. After enabling autologging, calls such as `client.chat.completions.create()` are automatically traced. ^[tracing-groq-databricks-on-aws.md]

```python
client = groq.Groq()

message = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs.",
        }
    ],
)
print(message.choices[0].message.content)
```

^[tracing-groq-databricks-on-aws.md]

The generated [Traces](/concepts/traces.md) can be explored in the Trace UI, which provides tools for debugging and observing application behavior. ^[tracing-groq-databricks-on-aws.md]

## Limitations

- Only **synchronous** API calls are traced. ^[tracing-groq-databricks-on-aws.md]
- Asynchronous API methods and streaming responses are **not** traced. ^[tracing-groq-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto-tracing for Groq can be disabled globally by calling either of the following: ^[tracing-groq-databricks-on-aws.md]

- `mlflow.groq.autolog(disable=True)` — disables only the Groq integration
- `mlflow.autolog(disable=True)` — disables all auto-logging integrations

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing framework that captures and organizes trace data
- Trace UI — Interface for debugging and analyzing traced application behavior
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md) — Setting up quality assessment for Groq-powered applications
- Serverless Compute — Compute environment where autologging is not enabled by default
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for grouping related [Traces](/concepts/traces.md) and runs

## Sources

- tracing-groq-databricks-on-aws.md

# Citations

1. [tracing-groq-databricks-on-aws.md](/references/tracing-groq-databricks-on-aws-121d088c.md)
