---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b0f4aca131b5b3cd2b74ef958620822c4e1adf97f195f6feaf50276085ae9e0
  pageDirectory: concepts
  sources:
    - tracing-claude-code-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-mlflow-agent-evaluation-workflow
    - DMAEW
  citations:
    - file: tracing-claude-code-databricks-on-aws.md
title: Databricks MLflow Agent Evaluation Workflow
description: End-to-end workflow on Databricks for evaluating Claude agent responses using MLflow datasets, custom scorers, and experiment tracking.
tags:
  - databricks
  - mlflow
  - evaluation
  - workflow
timestamp: "2026-06-19T23:10:02.665Z"
---

# Databricks [MLflow Agent Evaluation](/concepts/mlflow-agent-evaluation.md) Workflow

The **Databricks [MLflow Agent Evaluation](/concepts/mlflow-agent-evaluation.md) Workflow** enables developers to trace and evaluate responses from AI agents—such as those built with the Claude Agent SDK—using the `mlflow.genai` evaluation module. By combining [Automatic Tracing](/concepts/automatic-tracing.md) with [Custom Judge Scorers](/concepts/custom-judge-scorers.md), the workflow provides a structured way to measure agent performance against a set of test queries. ^[tracing-claude-code-databricks-on-aws.md]

## Workflow Overview

The evaluation workflow consists of five main steps:

1. **Set up tracing** – Enable automatic logging of agent interactions.
2. **Define a predict function** – Wrap the agent call in a synchronous function suitable for batch evaluation.
3. **Create evaluation scorers** – Define one or more judge [[scorers|Scorers]] using the `make_judge` helper to evaluate response quality.
4. **Prepare evaluation data** – Assemble a set of input queries (and optionally expected outputs) into a pandas DataFrame.
5. **Run evaluation** – Call `mlflow.genai.evaluate()` to execute the agent on the test data and compute scores.

## Step 1: Set up Tracing

Before evaluation, enable [Automatic Tracing](/concepts/automatic-tracing.md) for the agent framework. For the Claude Agent SDK, call `mlflow.anthropic.autolog()`. This captures detailed [Traces](/concepts/traces.md) of each agent query, including intermediate steps and final responses. ^[tracing-claude-code-databricks-on-aws.md]

Tracing is essential for debugging and for understanding how the agent arrived at its answer, especially when scores are unexpected.

## Step 2: Define a Predict Function

The agent logic must be wrapped in a synchronous function that accepts an input (e.g., a query string) and returns a response string. This function is passed as the `predict_fn` argument to `mlflow.genai.evaluate()`. For asynchronous agents, use `asyncio.run()` inside the synchronous wrapper. ^[tracing-claude-code-databricks-on-aws.md]

The example below defines `predict_fn(query)` that runs a Claude Agent SDK query and collects the response text.

## Step 3: Create Evaluation [[scorers|Scorers]]

[[scorers|Scorers]] define how each agent response is evaluated. The `mlflow.genai.judges` module provides `make_judge` to create a [Judge Scorer](/concepts/llm-judges-and-scorers.md) that uses a large language model (e.g., GPT-4o) to judge responses based on custom instructions. The judge receives the input and output and returns a pass/fail verdict. ^[tracing-claude-code-databricks-on-aws.md]

For example, a [Relevance Scorer](/concepts/relevance-scorer.md) instructs the judge to check whether the response is relevant to the query:

```python
relevance = make_judge(
    name="relevance",
    instructions=(
        "Evaluate if the response in {{ outputs }} is relevant to "
        "the question in {{ inputs }}. Return either 'pass' or 'fail'."
    ),
    model="openai:/gpt-4o",
)
```

Multiple [[scorers|Scorers]] can be combined in a list to assess different quality dimensions.

## Step 4: Prepare Evaluation Data

Create a pandas DataFrame where each row contains an `inputs` dictionary (e.g., `{"query": "What is machine learning?"}`). Optionally, an `outputs` column can hold expected responses for metrics like accuracy.

The evaluation data should represent the range of queries the agent is expected to handle.

## Step 5: Run the Evaluation

Set the [MLflow Experiment](/concepts/mlflow-experiment.md) and call `mlflow.genai.evaluate()` with the data, predict function, and [[scorers|Scorers]]. The function runs each query through the agent, collects [Traces](/concepts/traces.md), and computes judge scores. Results are logged to the experiment. ^[tracing-claude-code-databricks-on-aws.md]

```python
[[mlflow|MLflow]].set_experiment("claude_evaluation")
evaluate(data=eval_data, predict_fn=predict_fn, scorers=[relevance])
```

## Complete Example

The following code snippet demonstrates the entire workflow using the Claude Agent SDK: ^[tracing-claude-code-databricks-on-aws.md]

```python
import asyncio
import pandas as pd
from claude_agent_sdk import ClaudeSDKClient
import [[mlflow|MLflow]].anthropic
from [[mlflow|MLflow]].genai import evaluate, scorer
from [[mlflow|MLflow]].genai.judges import make_judge

[[mlflow|MLflow]].anthropic.autolog()

async def run_agent(query: str) -> str:
    """Run Claude Agent SDK and return response"""
    async with ClaudeSDKClient() as client:
        await client.query(query)
        response_text = ""
        async for message in client.receive_response():
            response_text += str(message) + "\n\n"
        return response_text

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

eval_data = pd.DataFrame(
    [
        {"inputs": {"query": "What is machine learning?"}},
        {"inputs": {"query": "Explain neural networks"}},
    ]
)

[[mlflow|MLflow]].set_experiment("claude_evaluation")
evaluate(data=eval_data, predict_fn=predict_fn, scorers=[relevance])
```

## Related Concepts

- [MLflow](/concepts/mlflow.md) – Open-source platform for managing ML experiments.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – General methodology for evaluating AI agent responses.
- [Judge Scorer](/concepts/llm-judges-and-scorers.md) – An [MLflow](/concepts/mlflow.md) scorer that uses an LLM to judge response quality.
- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md) – The core evaluation function in the `mlflow.genai` module.
- [Claude Agent SDK](/concepts/claude-agent-sdk-claudesdkclient.md) – The framework for building Claude-powered agents.
- [Autologging](/concepts/mlflow-autologging.md) – Automatic tracking and tracing of model runs and agent interactions.

## Sources

- tracing-claude-code-databricks-on-aws.md

# Citations

1. [tracing-claude-code-databricks-on-aws.md](/references/tracing-claude-code-databricks-on-aws-cfc0e415.md)
