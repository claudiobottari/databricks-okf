---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 27c7104629a87dea6796c42af9c9d2d03660bc6d324e1248dfff899dfb71bae9
  pageDirectory: concepts
  sources:
    - tracing-claude-code-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-anthropic-autologging
    - MAA
  citations:
    - file: tracing-claude-code-databricks-on-aws.md
title: MLflow Anthropic Autologging
description: Automatic tracing of Anthropic Claude SDK calls via mlflow.anthropic.autolog() for capturing agent interactions and tool calls in MLflow traces.
tags:
  - mlflow
  - tracing
  - anthropic
  - claude
timestamp: "2026-06-19T23:09:45.617Z"
---

# [MLflow](/concepts/mlflow.md) Anthropic Autologging

**MLflow Anthropic Autologging** is a feature within the [MLflow](/concepts/mlflow.md) ecosystem that automatically captures and [Traces](/concepts/traces.md) interactions with Anthropic's Claude models, including those using the Claude Agent SDK. When enabled, it instruments Anthropic API calls to record detailed trace data for monitoring, debugging, and evaluation purposes without requiring manual instrumentation code.

## Overview

The `mlflow.anthropic.autolog()` function enables [Automatic Tracing](/concepts/automatic-tracing.md) of Anthropic Claude model interactions. This is particularly useful when building agentic applications with the Claude Agent SDK, as it captures the full execution flow including queries, responses, and intermediate steps. The autologging integration works seamlessly with [MLflow Tracing](/concepts/mlflow-tracing.md) to provide observability into LLM-powered applications. ^[tracing-claude-code-databricks-on-aws.md]

## Usage

To enable Anthropic autologging, call `mlflow.anthropic.autolog()` at the beginning of your application code, before any Anthropic API calls are made. This instruments the Anthropic SDK to automatically create [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md) for each interaction. ^[tracing-claude-code-databricks-on-aws.md]

```python
import [[mlflow|MLflow]].anthropic

[[mlflow|MLflow]].anthropic.autolog()
```

After enabling autologging, all subsequent Anthropic API calls are automatically traced. The [Traces](/concepts/traces.md) capture input prompts, model responses, token usage, and other metadata that can be viewed in the [MLflow](/concepts/mlflow.md) UI or programmatically. ^[tracing-claude-code-databricks-on-aws.md]

## Integration with [MLflow](/concepts/mlflow.md) Evaluation

Anthropic autologging integrates with [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) to provide end-to-end traceability when evaluating Claude-based agents. When combined with `mlflow.evaluate()`, the autologged [Traces](/concepts/traces.md) are automatically associated with [Evaluation Runs](/concepts/evaluation-runs.md), allowing you to inspect individual agent interactions alongside evaluation metrics. ^[tracing-claude-code-databricks-on-aws.md]

```python
import [[mlflow|MLflow]]
from [[mlflow|MLflow]].genai import evaluate

[[mlflow|MLflow]].set_experiment("claude_evaluation")
evaluate(data=eval_data, predict_fn=predict_fn, scorers=[relevance])
```

## Claude Agent SDK Support

The autologging integration supports the Claude Agent SDK (`claude_agent_sdk`), which provides an asynchronous client for interacting with Claude models. When using the SDK's `ClaudeSDKClient`, autologging captures the full conversation flow including streaming responses received via `receive_response()`. ^[tracing-claude-code-databricks-on-aws.md]

```python
from claude_agent_sdk import ClaudeSDKClient

async with ClaudeSDKClient() as client:
    await client.query(query)
    async for message in client.receive_response():
        response_text += str(message) + "\n\n"
```

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The underlying tracing infrastructure that captures and stores trace data
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Framework for evaluating LLM outputs with custom [[scorers|Scorers]] and judges
- MLflow Anthropic Integration — Broader integration between [MLflow](/concepts/mlflow.md) and Anthropic models
- [LLM Observability](/concepts/genai-observability.md) — The practice of monitoring and debugging LLM applications
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluating the performance of AI agent systems

## Sources

- tracing-claude-code-databricks-on-aws.md

# Citations

1. [tracing-claude-code-databricks-on-aws.md](/references/tracing-claude-code-databricks-on-aws-cfc0e415.md)
