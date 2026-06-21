---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 67d58068efa0b9b689c495402ee623c9ddd6c420e4b4d41c8049d998f48b2cd3
  pageDirectory: concepts
  sources:
    - tracing-smolagents-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowsmolagentsautolog
  citations:
    - file: tracing-smolagents-databricks-on-aws.md
title: mlflow.smolagents.autolog
description: The API function that enables automatic trace capture for Smolagents agent runs
tags:
  - mlflow
  - api
  - instrumentation
timestamp: "2026-06-19T23:13:02.110Z"
---

# `mlflow.[Smolagents](/concepts/smolagents.md).autolog`

`mlflow.[Smolagents](/concepts/smolagents.md).autolog()` is a function in the [MLflow](/concepts/mlflow.md) Python API that enables [Automatic Tracing](/concepts/automatic-tracing.md) of workflows built with the [Smolagents](/concepts/smolagents.md) lightweight agent framework. When called, it instruments [Smolagents](/concepts/smolagents.md) calls so that execution [Traces](/concepts/traces.md) are captured and logged to the currently active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-smolagents-databricks-on-aws.md]

## Overview

[Smolagents](/concepts/smolagents.md) is a minimalist agent framework from Hugging Face that emphasizes composability. [MLflow Tracing](/concepts/mlflow-tracing.md) integrates with [Smolagents](/concepts/smolagents.md) to capture streamlined [Traces](/concepts/traces.md) of lightweight agent workflows. The integration is activated by invoking `mlflow.[Smolagents](/concepts/smolagents.md).autolog()` before running any agent code. ^[tracing-smolagents-databricks-on-aws.md]

[MLflow](/concepts/mlflow.md) auto-tracing supports only synchronous calls; asynchronous API and streaming methods are not traced. ^[tracing-smolagents-databricks-on-aws.md]

On serverless compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks is not automatically enabled. You must explicitly call the appropriate `mlflow.<library>.autolog()` function for the integrations you want to trace. ^[tracing-smolagents-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with [Smolagents](/concepts/smolagents.md), install [MLflow](/concepts/mlflow.md) (version 3 recommended for the best experience) and the required [Smolagents](/concepts/smolagents.md) packages. ^[tracing-smolagents-databricks-on-aws.md]

- **Development environment**: Install the full [MLflow](/concepts/mlflow.md) package with Databricks extras and [Smolagents](/concepts/smolagents.md):
  ```bash
  pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" [[smolagents|Smolagents]] openai
  ```
- **Production environment**: Use the same installation, and ensure API keys are managed securely (e.g., via [AI Gateway](/concepts/ai-gateway.md) or Databricks secrets). ^[tracing-smolagents-databricks-on-aws.md]

Before running examples, configure environment variables. Outside Databricks notebooks, set `DATABRICKS_HOST` and `DATABRICKS_TOKEN`. Inside Databricks notebooks, credentials are automatically set. Also configure LLM provider API keys (e.g., `OPENAI_API_KEY`). ^[tracing-smolagents-databricks-on-aws.md]

## Example Usage

After calling `mlflow.[Smolagents](/concepts/smolagents.md).autolog()`, run [Smolagents](/concepts/smolagents.md) workflows as usual. [Traces](/concepts/traces.md) automatically appear in the experiment UI. ^[tracing-smolagents-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]

# Turn on auto tracing for [[smolagents|Smolagents]]
[[mlflow|MLflow]].[[smolagents|Smolagents]].autolog()

from [[smolagents|Smolagents]] import CodeAgent, LiteLLMModel

model = LiteLLMModel(model_id="openai/gpt-4o-mini", api_key=API_KEY)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)
result = agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)
```

^[tracing-smolagents-databricks-on-aws.md]

## Token Tracking Usage

[MLflow](/concepts/mlflow.md) logs token usage for each agent call to the `mlflow.chat.tokenUsage` attribute on the span. Total token usage across the entire trace is available in the `token_usage` field of the trace info object. ^[tracing-smolagents-databricks-on-aws.md]

The following example shows how to retrieve token usage after a trace is created:

```python
import [[mlflow|MLflow]]

[[mlflow|MLflow]].[[smolagents|Smolagents]].autolog()

# ... run agent ...

last_trace_id = [[mlflow|MLflow]].get_last_active_trace_id()
trace = [[mlflow|MLflow]].get_trace(trace_id=last_trace_id)

# Print total token usage
total_usage = trace.info.token_usage
print("== Total token usage: ==")
print(f"  Input tokens: {total_usage['input_tokens']}")
print(f"  Output tokens: {total_usage['output_tokens']}")
print(f"  Total tokens: {total_usage['total_tokens']}")

# Print per-LLM-call token usage
print("\n== Detailed usage for each LLM call: ==")
for span in trace.data.spans:
    if usage := span.get_attribute("[[mlflow|MLflow]].chat.tokenUsage"):
        print(f"{span.name}:")
        print(f"  Input tokens: {usage['input_tokens']}")
        print(f"  Output tokens: {usage['output_tokens']}")
        print(f"  Total tokens: {usage['total_tokens']}")
```

^[tracing-smolagents-databricks-on-aws.md]

## Disabling Auto-tracing

Auto-tracing can be disabled by calling `mlflow.[Smolagents](/concepts/smolagents.md).autolog(disable=True)` or globally with `mlflow.autolog(disable=True)`. ^[tracing-smolagents-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying tracing system that captures execution spans.
- [Smolagents](/concepts/smolagents.md) – The lightweight agent framework being traced.
- CodeAgent – A concrete agent class commonly used with this integration.
- [LiteLLMModel](/concepts/external-models.md) – The model wrapper used in the examples.
- [MLflow experiments](/concepts/mlflow-experiment.md) – Where [Traces](/concepts/traces.md) are stored and viewed.
- [mlflow.autolog](/concepts/mlflow-autologging.md) – The global autologging function.

## Sources

- tracing-smolagents-databricks-on-aws.md

# Citations

1. [tracing-smolagents-databricks-on-aws.md](/references/tracing-smolagents-databricks-on-aws-485dc1ff.md)
