---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60b23d5fb12a6b5a707470bc58423496272226166f101397ebcaebd12559c955
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
    - tracing-deepseek-databricks-on-aws.md
    - tracing-openai-swarm-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-openai-autolog
    - MOA
  citations:
    - file: tracing-openai-databricks-on-aws.md
    - file: tracing-openai-agents-databricks-on-aws.md
    - file: tracing-openai-swarm-databricks-on-aws.md
    - file: tutorial-search-traces-programmatically-databricks-on-aws.md
title: MLflow OpenAI Autolog
description: Automatic instrumentation of OpenAI API calls by MLflow to capture traces, inputs, and outputs without manual logging code.
tags:
  - mlflow
  - openai
  - tracing
  - instrumentation
timestamp: "2026-06-19T21:53:47.004Z"
---

# MLflow OpenAI Autolog

**MLflow OpenAI Autolog** is a feature that enables automatic [MLflow Tracing](/concepts/mlflow-tracing.md) for OpenAI API calls. By calling `mlflow.openai.autolog()`, MLflow captures traces for LLM invocations and logs them to the active MLflow Experiment without requiring manual instrumentation of each call.^[tracing-openai-databricks-on-aws.md, tracing-openai-agents-databricks-on-aws.md, tracing-openai-swarm-databricks-on-aws.md]

## How It Works

When autolog is enabled, MLflow automatically wraps the OpenAI client methods to record detailed information about every API call. The captured data is logged as traces in the active MLflow Experiment, viewable in the MLflow UI or retrievable programmatically via `mlflow.search_traces()`.^[tracing-openai-databricks-on-aws.md, tutorial-search-traces-programmatically-databricks-on-aws.md]

On serverless compute clusters, autologging for GenAI tracing frameworks is **not** automatically enabled. You must explicitly enable it by calling the appropriate `mlflow.<library>.autolog()` function for each integration you want to trace.^[tracing-openai-databricks-on-aws.md, tracing-openai-agents-databricks-on-aws.md]

## What Is Captured

MLflow trace automatically captures the following information about OpenAI calls:^[tracing-openai-databricks-on-aws.md]

- **Prompts and completion responses**
- **Latencies** (execution time)
- **Model name**
- **Additional metadata** such as `temperature` and `max_tokens` (if specified)
- **Function calling** details if returned in the response
- **Any exception** if raised

For streaming responses, MLflow captures the concatenated output and the individual chunks (accessible in the `Event` tab of the span UI).^[tracing-openai-databricks-on-aws.md]

For function calling, the tool instruction in the response is highlighted. Additionally, tool functions can be annotated with `@mlflow.trace` to create a trace span for tool execution.^[tracing-openai-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with OpenAI, install MLflow and the OpenAI SDK:^[tracing-openai-databricks-on-aws.md]

```bash
pip install --upgrade "mlflow[databricks]>=3.1" openai
```

MLflow 3 is highly recommended for the best tracing experience.^[tracing-openai-databricks-on-aws.md]

You must configure your environment with:
- **Databricks credentials** (if using Databricks tracking): set `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables (automatically set inside Databricks notebooks).
- **OpenAI API key**: set `OPENAI_API_KEY`. For production, use [AI Gateway](/concepts/ai-gateway.md) or [Databricks secrets](/concepts/databricks-secret-scopes.md) instead of hardcoded values.^[tracing-openai-databricks-on-aws.md]

## Supported APIs

MLflow supports automatic tracing for the following OpenAI APIs:^[tracing-openai-databricks-on-aws.md]

| API | Support |
|-----|---------|
| `openai.chat.completions.create` | Yes |
| Streaming (`stream=True`) | Yes (since MLflow 2.15.0) |
| Async (`AsyncOpenAI`) | Yes (since MLflow 2.21.0) |
| Structured outputs | Yes (since MLflow 2.21.0) |
| `openai.embeddings.create` | Not listed explicitly (check docs) |
| `openai.images.generate` | Not listed explicitly (check docs) |

Note: The source explicitly lists `chat.completions.create` with streaming and async variants as supported. For other APIs, refer to the [MLflow GitHub feature requests](https://github.com/mlflow/mlflow/issues).^[tracing-openai-databricks-on-aws.md]

## Basic Usage

Enable autolog at the start of your code:^[tracing-openai-databricks-on-aws.md]

```python
import mlflow
import openai

# Enable auto-tracing for OpenAI
mlflow.openai.autolog()

# Set up MLflow tracking to Databricks (if not using notebook defaults)
mlflow.set_tracking_uri("databricks")
mlflow.set_experiment("/Shared/openai-tracing-demo")

# Use OpenAI as usual
client = openai.OpenAI()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What is the capital of France?"}],
    temperature=0.1,
    max_tokens=100,
)
```

The traces are automatically logged to the active experiment without additional code.^[tracing-openai-databricks-on-aws.md]

## Integration with Other OpenAI Frameworks

`mlflow.openai.autolog()` also enables tracing for higher-level frameworks built on OpenAI:

- **OpenAI Agents SDK**: Traces agent interactions, handoffs, function calls, and guardrails.^[tracing-openai-agents-databricks-on-aws.md]
- **OpenAI Swarm**: Traces multi-agent workflows using the Swarm client.^[tracing-openai-swarm-databricks-on-aws.md]

In each case, the underlying LLM calls are instrumented, and MLflow captures the full execution traces.^[tracing-openai-agents-databricks-on-aws.md, tracing-openai-swarm-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto tracing for OpenAI can be disabled globally by calling:^[tracing-openai-databricks-on-aws.md, tracing-openai-agents-databricks-on-aws.md]

```python
mlflow.openai.autolog(disable=True)
```

Alternatively, all [MLflow Autologging](/concepts/mlflow-autologging.md) can be disabled:

```python
mlflow.autolog(disable=True)
```

## Using with Databricks Secrets

For secure API key management in production, retrieve the key from [Databricks secrets](/concepts/databricks-secret-scopes.md):^[tracing-openai-databricks-on-aws.md]

```python
os.environ["OPENAI_API_KEY"] = dbutils.secrets.get(
    scope="openai-secrets",
    key="api-key"
)
```

Then proceed with `mlflow.openai.autolog()` as usual.^[tracing-openai-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying tracing framework that records LLM calls
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for traces and runs
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Using traces in GenAI evaluation workflows
- OpenAI — The API provider whose calls are traced
- [AI Gateway](/concepts/ai-gateway.md) — Alternative for secure API key management

## Sources

- tracing-openai-databricks-on-aws.md
- tracing-openai-agents-databricks-on-aws.md
- tracing-openai-swarm-databricks-on-aws.md
- tutorial-search-traces-programmatically-databricks-on-aws.md
- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [tracing-openai-databricks-on-aws.md](/references/tracing-openai-databricks-on-aws-b94e8d1d.md)
2. [tracing-openai-agents-databricks-on-aws.md](/references/tracing-openai-agents-databricks-on-aws-db457d66.md)
3. [tracing-openai-swarm-databricks-on-aws.md](/references/tracing-openai-swarm-databricks-on-aws-42054ece.md)
4. [tutorial-search-traces-programmatically-databricks-on-aws.md](/references/tutorial-search-traces-programmatically-databricks-on-aws-4b1ea59e.md)
