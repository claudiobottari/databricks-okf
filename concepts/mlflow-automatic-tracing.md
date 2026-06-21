---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 099755320ea818c6d1c136d8ca777a97a5364e7988d38db3e72fbac5414af111
  pageDirectory: concepts
  sources:
    - mlflow-tracing-integrations-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-automatic-tracing
    - MAT
    - MLflow Auto Tracing
    - Auto‑tracing
  citations:
    - file: mlflow-tracing-integrations-databricks-on-aws.md
title: MLflow Automatic Tracing
description: One-line automatic instrumentation for GenAI libraries to capture LLM calls, tool usage, and agent interactions without significant code changes.
tags:
  - mlflow
  - tracing
  - observability
timestamp: "2026-06-19T19:41:06.970Z"
---

```yaml
---
title: MLflow Automatic Tracing
summary: One-line autolog() instrumentation to automatically capture traces from 20+ supported generative AI libraries without manual code changes.
sources:
  - mlflow-tracing-integrations-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:40:33.485Z"
updatedAt: "2026-06-19T10:40:33.485Z"
tags:
  - mlflow
  - tracing
  - instrumentation
  - generative-ai
aliases:
  - mlflow-automatic-tracing
  - MAT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Automatic Tracing

**MLflow Automatic Tracing** provides a one-line instrumentation approach for capturing traces from generative AI applications built on popular libraries and frameworks. By calling `mlflow.<library>.autolog()`, developers can instantly gain visibility into LLM calls, tool usage, agent interactions, and other intermediate steps without modifying their application logic. This is the recommended starting point for most tracing use cases. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## How Automatic Tracing Works

When `mlflow.<library>.autolog()` is called, MLflow intercepts the library's key functions (such as LLM completion calls, embedding requests, or chain executions) and automatically generates [[MLflow Trace|MLflow Traces]] that record inputs, outputs, timing, and metadata. Each trace captures the full execution path, including nested calls to other supported libraries when multiple integrations are enabled. ^[mlflow-tracing-integrations-databricks-on-aws.md]

> **Note:** On serverless compute clusters, autologging for generative AI tracing frameworks is not automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for each integration you want to trace. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Supported Libraries

Automatic tracing is integrated with a wide array of popular generative AI libraries and frameworks. The top integrations include:

- OpenAI
- LangChain
- LangGraph
- Anthropic
- DSPy
- Databricks (Foundation Model endpoints)
- Bedrock
- AutoGen

For each library, the exact call is `mlflow.<library_name>.autolog()`. For example, to enable tracing for OpenAI: `mlflow.openai.autolog()`. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Enabling Automatic Tracing

### Single Library

Add one line before your library code, then set up MLflow tracking (if running outside Databricks notebooks):

```python
import mlflow
import openai

mlflow.openai.autolog()

# Set up MLflow tracking (not strictly needed in Databricks notebooks)
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/my-genai-app")

client = openai.OpenAI()
response = client.chat.completions.create(...)
```

^[mlflow-tracing-integrations-databricks-on-aws.md]

### Multiple Libraries

For applications that combine several libraries, enable automatic tracing for each:

```python
import mlflow

mlflow.langchain.autolog()
mlflow.openai.autolog()

# Your code using both LangChain and OpenAI
```

MLflow will generate a single, cohesive trace that combines steps from all enabled integrations. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Disabling Automatic Tracing

To disable auto tracing for a specific library, pass `disable=True`:

```python
mlflow.openai.autolog(disable=True)
```

To disable all autologging integrations at once:

```python
mlflow.autolog(disable=True)
```

^[mlflow-tracing-integrations-databricks-on-aws.md]

## Secure API Key Management

For production environments, Databricks recommends using [[AI Gateway]] or Databricks Secrets to manage API keys. AI Gateway is the preferred method and offers additional governance features. Never commit API keys directly in code or notebooks. ^[mlflow-tracing-integrations-databricks-on-aws.md]

## Related Concepts

- [[MLflow Tracing]] — The overall tracing framework
- [[Manual Tracing (MLflow)]] — Deeper control using decorator and low-level APIs
- [[AI Gateway]] — Recommended method for securing API keys
- Databricks Secrets — Alternative secure credential storage

## Sources

- mlflow-tracing-integrations-databricks-on-aws.md
```

# Citations

1. [mlflow-tracing-integrations-databricks-on-aws.md](/references/mlflow-tracing-integrations-databricks-on-aws-22e947f8.md)
