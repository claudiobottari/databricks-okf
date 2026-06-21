---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8292136e9fd648de21e46f504672d7f6c36571b380377df7a99239adcc1093b9
  pageDirectory: concepts
  sources:
    - tracing-smolagents-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-token-tracking
    - MTTT
  citations:
    - file: tracing-smolagents-databricks-on-aws.md
title: MLflow Trace Token Tracking
description: Token usage tracking for LLM calls within MLflow traces, accessible via span attributes and trace info
tags:
  - mlflow
  - token-usage
  - cost-tracking
timestamp: "2026-06-19T23:13:04.251Z"
---

# [[mlflow-trace|MLflow Trace]] Token Tracking

**MLflow Trace Token Tracking** refers to the mechanism by which [MLflow](/concepts/mlflow.md) records token usage (input tokens, output tokens, and total tokens) for each large language model (LLM) call made during a traced agent workflow. This feature is part of the broader [MLflow Tracing](/concepts/mlflow-tracing.md) system and is available for integrations such as [Smolagents](/concepts/smolagents.md).

## Overview

When [MLflow Tracing](/concepts/mlflow-tracing.md) is enabled for a supported agent framework, each LLM call made by the agent is captured as a span. For spans that represent LLM interactions, [MLflow](/concepts/mlflow.md) automatically logs the token usage to the span attribute `mlflow.chat.tokenUsage`. This attribute contains a dictionary with three keys: `input_tokens`, `output_tokens`, and `total_tokens`. ^[tracing-smolagents-databricks-on-aws.md]

In addition to per‑span tracking, the overall trace info object exposes a `token_usage` field that aggregates the token counts across all LLM calls made during the trace. This gives a single summary of the total tokens consumed by the entire agent run. ^[tracing-smolagents-databricks-on-aws.md]

## Usage

Token tracking is automatically enabled when you activate autologging for the agent framework. For example, with [Smolagents](/concepts/smolagents.md):

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].[[smolagents|Smolagents]].autolog()

# ... run your agent workflow
```

After the workflow completes, you can retrieve the trace and inspect token usage. ^[tracing-smolagents-databricks-on-aws.md]

## Accessing Token Usage

The following example demonstrates how to access both the total token usage and the per‑LLM‑call token usage from a completed trace:

```python
import json
import [[mlflow|MLflow]]

[[mlflow|MLflow]].[[smolagents|Smolagents]].autolog()

# Run agent workflow
model = LiteLLMModel(model_id="openai/gpt-4o-mini", api_key=API_KEY)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)
result = agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?"
)

# Get the trace object
last_trace_id = [[mlflow|MLflow]].get_last_active_trace_id()
trace = [[mlflow|MLflow]].get_trace(trace_id=last_trace_id)

# Total token usage from trace info
total_usage = trace.info.token_usage
print("== Total token usage ==")
print(f"  Input tokens: {total_usage['input_tokens']}")
print(f"  Output tokens: {total_usage['output_tokens']}")
print(f"  Total tokens: {total_usage['total_tokens']}")

# Per-LLM-call token usage from span attributes
print("\n== Detailed usage for each LLM call ==")
for span in trace.data.spans:
    if usage := span.get_attribute("[[mlflow|MLflow]].chat.tokenUsage"):
        print(f"{span.name}:")
        print(f"  Input tokens: {usage['input_tokens']}")
        print(f"  Output tokens: {usage['output_tokens']}")
        print(f"  Total tokens: {usage['total_tokens']}")
```

^[tracing-smolagents-databricks-on-aws.md]

The per‑span attribute `mlflow.chat.tokenUsage` holds the same token breakdown for the specific LLM call, while `trace.info.token_usage` provides the aggregate sum across all spans in the trace. ^[tracing-smolagents-databricks-on-aws.md]

## Requirements

Token tracking works only with synchronous LLM calls. Asynchronous API methods and streaming responses are not traced by the current autologging implementation. ^[tracing-smolagents-databricks-on-aws.md] You must also have [MLflow 3](/concepts/mlflow-3.md).1 or later installed with the appropriate integration packages (e.g., `smolagents` and `openai`). ^[tracing-smolagents-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The broader tracing framework that captures spans and trace information.
- [Smolagents](/concepts/smolagents.md) — A lightweight agent framework that supports [MLflow Tracing](/concepts/mlflow-tracing.md).
- [autolog](/concepts/mlflow-autologging.md) — The mechanism for automatically enabling tracing and token tracking for supported libraries.
- [Trace info object](/concepts/traceinfo.md) — The object that contains aggregated metadata such as token usage.
- [Experiment UI](/concepts/mlflow-experiment.md) — The user interface where [Traces](/concepts/traces.md) and their token usage can be viewed.

## Sources

- tracing-smolagents-databricks-on-aws.md

# Citations

1. [tracing-smolagents-databricks-on-aws.md](/references/tracing-smolagents-databricks-on-aws-485dc1ff.md)
