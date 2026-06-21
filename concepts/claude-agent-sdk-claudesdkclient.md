---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c81321f8044a5e7e5efd61fff82ffb90a047c87085fcdb9c3182f5575236d64
  pageDirectory: concepts
  sources:
    - tracing-claude-code-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - claude-agent-sdk-claudesdkclient
    - CAS(
    - Claude Agent SDK
  citations:
    - file: tracing-claude-code-databricks-on-aws.md
title: Claude Agent SDK (ClaudeSDKClient)
description: Anthropic's SDK client for building agentic interactions with Claude, supporting async query/response streaming patterns.
tags:
  - claude
  - agent-sdk
  - anthropic
  - async
timestamp: "2026-06-19T23:09:50.300Z"
---

Here is the wiki page for "Claude Agent SDK (ClaudeSDKClient)".

---

## Claude Agent SDK (ClaudeSDKClient)

The **Claude Agent SDK (ClaudeSDKClient)** is a client library for interacting with the Claude Agent SDK from Anthropic. It provides an asynchronous interface for sending queries to Claude and receiving streaming responses. On Databricks, the SDK can be used in conjunction with [MLflow](/concepts/mlflow.md) and [MLflow Tracing](/concepts/mlflow-tracing.md) to automatically trace agent interactions for evaluation and monitoring. ^[tracing-claude-code-databricks-on-aws.md]

### Overview

The `ClaudeSDKClient` is used within an `async with` context manager. After sending a query via `client.query()`, the response is received as a stream of messages using `client.receive_response()`. This pattern enables real-time processing of Claude's output as it is generated. ^[tracing-claude-code-databricks-on-aws.md]

### Usage with [MLflow Tracing](/concepts/mlflow-tracing.md)

To enable [Automatic Tracing](/concepts/automatic-tracing.md) of Claude Agent SDK calls, import `mlflow.anthropic` and call `mlflow.anthropic.autolog()` before running the agent. This integration captures the full interaction trace — including inputs, outputs, and intermediate steps — and logs it to an [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-claude-code-databricks-on-aws.md]

The following example demonstrates a basic agent loop with tracing:

```python
import asyncio
from claude_agent_sdk import ClaudeSDKClient
import [[mlflow|MLflow]].anthropic

[[mlflow|MLflow]].anthropic.autolog()

async def run_agent(query: str) -> str:
    """Run Claude Agent SDK and return response"""
    async with ClaudeSDKClient() as client:
        await client.query(query)
        response_text = ""
        async for message in client.receive_response():
            response_text += str(message) + "\n\n"
        return response_text
```

^[tracing-claude-code-databricks-on-aws.md]

### Evaluation with [MLflow](/concepts/mlflow.md)

The traced agent can be evaluated using [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md). A synchronous wrapper function is typically created to call the async agent, which is then passed to `mlflow.evaluate()` along with evaluation data and [LLM-as-Judge](/concepts/llm-as-a-judge.md) [[scorers|Scorers]]. ^[tracing-claude-code-databricks-on-aws.md]

```python
def predict_fn(query: str) -> str:
    """Synchronous wrapper for evaluation"""
    return asyncio.run(run_agent(query))

relevance = make_judge(
    name="relevance",
    instructions=(
        "Evaluate if the response in {{ outputs }} is relevant to "
        "the question in {{ inputs }}. Return either 'pass' or 'fail'."
    ),
    model="openai:/gpt-4o",
)

[[mlflow|MLflow]].set_experiment("claude_evaluation")
evaluate(data=eval_data, predict_fn=predict_fn, scorers=[relevance])
```

^[tracing-claude-code-databricks-on-aws.md]

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — Automatic capture of LLM and agent interaction [Traces](/concepts/traces.md).
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Framework for evaluating model and agent outputs.
- [LLM-as-Judge](/concepts/llm-as-a-judge.md) — Using a language model to evaluate outputs programmatically.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for runs and evaluations.
- Anthropic Claude — The underlying language model powering the agent.

### Sources

- tracing-claude-code-databricks-on-aws.md

# Citations

1. [tracing-claude-code-databricks-on-aws.md](/references/tracing-claude-code-databricks-on-aws-cfc0e415.md)
