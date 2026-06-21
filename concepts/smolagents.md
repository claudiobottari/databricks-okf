---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d327f9d456287abc91768943b1f929cc8bcff43d8eb59d019933a56a4562b25e
  pageDirectory: concepts
  sources:
    - tracing-smolagents-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - smolagents
  citations:
    - file: tracing-smolagents-databricks-on-aws.md
    - file: tracing-smolagents-dabricks-on-aws.md
title: Smolagents
description: A lightweight agent framework by HuggingFace emphasizing minimalism and composability
tags:
  - agent-framework
  - python
  - llm
timestamp: "2026-06-19T23:13:33.872Z"
---

# Smolagents

**Smolagents** is a lightweight agent framework developed by Hugging Face that emphasizes minimalism and composability. It provides a simple, code-driven approach for building AI agents that perform tasks using tools and large language models (LLMs). ^[tracing-smolagents-databricks-on-aws.md]

## Overview

Smolagents is designed to be a minimal and composable framework for building AI agents. It focuses on providing the essential building blocks for agent creation without unnecessary complexity, making it suitable for both experimentation and production use cases. ^[tracing-smolagents-databricks-on-aws.md]

## Core Components

### CodeAgent
The primary agent type in Smolagents is the CodeAgent, which executes tasks by generating and running code. CodeAgents use an underlying LLM model to interpret user requests and determine which tools to use. ^[tracing-smolagents-databricks-on-aws.md]

### LiteLLMModel
The [LiteLLMModel](/concepts/external-models.md) provides a unified interface for connecting to various LLM providers. By default, it supports OpenAI's GPT models but can be configured to work with other providers through a model ID specification. ^[tracing-smolagents-dabricks-on-aws.md]

## Integration with [MLflow](/concepts/mlflow.md)

Smolagents integrates with [MLflow Tracing](/concepts/mlflow-tracing.md) to provide observability into agent workflows. The integration is enabled through `mlflow.smolagents.autolog()`, which captures [Traces](/concepts/traces.md) of agent executions automatically. ^[tracing-smolagents-databricks-on-aws.md]

### Tracing Capabilities

[MLflow](/concepts/mlflow.md)'s auto-tracing for Smolagents provides:
- **Complete trace capture**: Records every step of the agent's execution, including tool calls and LLM interactions
- **Token tracking**: Logs token usage through the `mlflow.chat.tokenUsage` attribute, providing input and output token counts for each LLM call
- **Synchronous only**: Auto-tracing only supports synchronous calls; asynchronous API and streaming methods are not traced ^[tracing-smolagents-databricks-on-aws.md]

### Limitations

[MLflow](/concepts/mlflow.md) auto-tracing only supports synchronous calls. Asynchronous API and streaming methods are not traced. Additionally, on serverless compute clusters, autologging must be explicitly enabled by calling `mlflow.smolagents.autolog()` for each integration. ^[tracing-smolagents-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with Smolagents, you need:
- **MLflow 3+**: Recommended for the best tracing experience
- **Smolagents package**: Install via pip
- **LLM provider API keys**: Configure environment variables for your chosen provider ^[tracing-smolagents-databricks-on-aws.md]

### Installation

For development:
```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" smolagents openai
```

For production, use [AI Gateway](/concepts/ai-gateway.md) or Databricks secrets for secure API key management. ^[tracing-smolagents-databricks-on-aws.md]

## Token Tracking Example

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].smolagents.autolog()

model = LiteLLMModel(model_id="openai/gpt-4o-mini", api_key=API_KEY)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)
result = agent.run("Could you give me the 118th number in the Fibonacci sequence?")

# Access token usage
trace = [[mlflow|MLflow]].get_trace(trace_id=last_trace_id)
total_usage = trace.info.token_usage
```

This shows how to retrieve detailed token usage information including input tokens, output tokens, and total tokens for each LLM call. ^[tracing-smolagents-databricks-on-aws.md]

## Disabling Auto-Tracing

To disable auto-tracing:
```python
[[mlflow|MLflow]].smolagents.autolog(disable=True)
```

Or globally:
```python
[[mlflow|MLflow]].autolog(disable=True)
```

^[tracing-smolagents-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) - The tracing infrastructure that provides observability
- AI Agents - The broader category of agent-based systems
- CodeAgent - Smolagents' primary agent implementation
- [LiteLLMModel](/concepts/external-models.md) - Smolagents' model abstraction layer
- [Hugging Face](/concepts/hugging-face-trainer.md) - The organization behind Smolagents

## Sources

- tracing-smolagents-databricks-on-aws.md

# Citations

1. [tracing-smolagents-databricks-on-aws.md](/references/tracing-smolagents-databricks-on-aws-485dc1ff.md)
2. tracing-smolagents-dabricks-on-aws.md
