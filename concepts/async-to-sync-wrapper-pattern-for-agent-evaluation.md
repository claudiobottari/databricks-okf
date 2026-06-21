---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 98d4b4f5cac26f956d87eb95dfea73aece6379bda428ba906bb8768cb95afcd7
  pageDirectory: concepts
  sources:
    - tracing-claude-code-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - async-to-sync-wrapper-pattern-for-agent-evaluation
    - AWPFAE
  citations:
    - file: tracing-claude-code-databricks-on-aws.md
title: Async-to-Sync Wrapper Pattern for Agent Evaluation
description: A pattern wrapping asynchronous Claude agent execution inside a synchronous predict function to enable compatibility with MLflow's evaluation API.
tags:
  - async
  - pattern
  - evaluation
  - wrapping
timestamp: "2026-06-19T23:10:00.137Z"
---

#Async-to-Sync Wrapper Pattern for Agent Evaluation

The **Async-to-Sync Wrapper Pattern for Agent Evaluation** is a technique used to bridge asynchronous agent SDKs (which provide `async` interfaces) with evaluation frameworks that require a synchronous callable. It enables tools like MLflow `evaluate` to run evaluations against async agents by wrapping the async logic in a synchronous function that internally awaits the agent’s response. ^[tracing-claude-code-databricks-on-aws.md]

## Problem

Many modern agent SDKs — such as the Claude Agent SDK — expose their main interaction loop as an `async` function (e.g., `async def run_agent(query: str) -> str`). Evaluation frameworks like `mlflow.evaluate` expect a synchronous `predict_fn` that takes a single input and returns a single output. Directly passing an `async` function fails because the evaluator cannot `await` it. ^[tracing-claude-code-databricks-on-aws.md]

## Implementation

The pattern defines a synchronous wrapper function that calls `asyncio.run()` on the async agent function. This wrapper can then be passed as the `predict_fn` argument to `evaluate`. The source example demonstrates this for a Claude-based agent: ^[tracing-claude-code-databricks-on-aws.md]

```python
import asyncio

async def run_agent(query: str) -> str:
    async with ClaudeSDKClient() as client:
        await client.query(query)
        response_text = ""
        async for message in client.receive_response():
            response_text += str(message) + "\n\n"
        return response_text

def predict_fn(query: str) -> str:
    """Synchronous wrapper for evaluation"""
    return asyncio.run(run_agent(query))
```

The `predict_fn` function takes a single string input (`query`) and returns the agent’s response as a string, satisfying the evaluator’s synchronous signature. Every call to `predict_fn` creates a new event loop, runs the agent to completion, and returns the result. ^[tracing-claude-code-databricks-on-aws.md]

## Usage in Evaluation

After defining the wrapper, the evaluation pipeline proceeds as normal: ^[tracing-claude-code-databricks-on-aws.md]

- Enable [MLflow Anthropic Autolog](/concepts/mlflow-anthropic-autolog.md) with `mlflow.anthropic.autolog()` to automatically capture [Traces](/concepts/traces.md) during evaluation.
- Create evaluation [[scorers|Scorers]] using `mlflow.genai.judges.make_judge` or other custom [[scorers|Scorers]].
- Set an [MLflow Experiment](/concepts/mlflow-experiment.md) with `mlflow.set_experiment("claude_evaluation")`.
- Call `evaluate(data=eval_data, predict_fn=predict_fn, scorers=[relevance])`.

The `predict_fn` wrapper ensures the async agent is called within the evaluation loop, while `autolog` captures the internal [Traces](/concepts/traces.md) (e.g., tool calls, intermediate messages) for further analysis. ^[tracing-claude-code-databricks-on-aws.md]

## Best Practices

- **Autolog placement**: Call `mlflow.anthropic.autolog()` *before* defining the wrapper to ensure all agent activity is traced during evaluation. ^[tracing-claude-code-databricks-on-aws.md]
- **Single‑use event loop**: `asyncio.run()` is safe to call repeatedly inside the wrapper because it creates a new event loop for each invocation. Avoid reusing a persistent loop across multiple evaluation calls.
- **Error handling**: Wrap the `asyncio.run()` call in try/except if the agent may raise exceptions during evaluation.

## Related Concepts

- [MLflow Evaluate](/concepts/mlflow-genai-evaluate-api.md) – The evaluation API that requires a synchronous `predict_fn`.
- [MLflow Anthropic Autolog](/concepts/mlflow-anthropic-autolog.md) – [Automatic Tracing](/concepts/automatic-tracing.md) of Claude agents during evaluation.
- MLflow make_judge|MLflow GenAI Judges – Pre‑built LLM‑based [[scorers|Scorers]] for attributes like relevance and correctness.
- [Claude Agent SDK](/concepts/claude-agent-sdk-claudesdkclient.md) – The async SDK used in the example.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – Broader topic of evaluating AI agent performance.

## Sources

- tracing-claude-code-databricks-on-aws.md

# Citations

1. [tracing-claude-code-databricks-on-aws.md](/references/tracing-claude-code-databricks-on-aws-cfc0e415.md)
