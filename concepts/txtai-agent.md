---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e609a86df2a4bf8a32910fbed2b4bf8f1fb8a74f02be0b1141a1ca948f493825
  pageDirectory: concepts
  sources:
    - tracing-txtai-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - txtai-agent
  citations:
    - file: tracing-txtai-databricks-on-aws.md
title: txtai Agent
description: An agent framework in txtai that uses tools (like semantic search) and LLMs to autonomously research and answer questions, traceable via MLflow
tags:
  - txtai
  - agent
  - llm
  - autonomous
timestamp: "2026-06-19T23:13:44.071Z"
---

# [txtai](/concepts/txtai.md) Agent

The **txtai Agent** is an autonomous workflow component within the [txtai](/concepts/txtai.md) ecosystem that uses a language model to reason, plan, and execute multi-step tasks by calling external tools. It is designed for research-oriented and knowledge-intensive tasks that require iterative searching, analysis, and report generation. ^[tracing-txtai-databricks-on-aws.md]

## Overview

A [txtai](/concepts/txtai.md) Agent combines a language model (LLM) with a set of user-defined tools to accomplish complex objectives. The agent follows a "reason-then-act" loop: it receives a command, decides which tool to call, processes the results, and continues iterating until it determines that sufficient information has been gathered. The agent's behavior is controlled through parameters such as `max_iterations`, which limits the number of reasoning steps it can take. ^[tracing-txtai-databricks-on-aws.md]

## Architecture

The agent is initialized with:
- A **tools** list containing one or more callable functions that the agent can invoke
- An **llm** parameter specifying the language model to use for reasoning
- Optional parameters such as `max_iterations` to control the agent's depth of search

Each tool must have a docstring describing its purpose, expected input format, and return value, as the agent uses this documentation to decide when and how to call the tool. ^[tracing-txtai-databricks-on-aws.md]

## Example Use Case: Astronomy Research

A common example of the [txtai](/concepts/txtai.md) Agent involves researching astronomy topics using similarity search against a pre-loaded embeddings database: ^[tracing-txtai-databricks-on-aws.md]

```python
from [[txtai|txtai]] import Agent, Embeddings

def search(query):
    """
    Searches a database of astronomy data.
    Make sure to call this tool only with a string input, never use JSON.
    Args:
        query: concepts to search for using similarity search
    Returns:
        list of search results with for each match
    """
    return embeddings.search(
        "SELECT id, text, distance FROM [[txtai|txtai]] WHERE similar(:query)", 
        10, 
        parameters={"query": query},
    )

embeddings = Embeddings()
embeddings.load(provider="huggingface-hub", container="neuml/txtai-astronomy")

agent = Agent(
    tools=[search],
    llm="hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4",
    max_iterations=10,
)

researcher = """{command}
Do the following:
- Search for results related to the topic.
- Analyze the results
- Continue querying until conclusive answers are found
- Write a Markdown report"""

agent(
    researcher.format(
        command="""Write a detailed list with explanations of 10 candidate stars 
        that could potentially be habitable to life."""
    ),
    maxlength=16000,
)
```

In this flow, the agent searches an astronomy embeddings database, analyzes results, formulates follow-up queries, and ultimately produces a Markdown report. ^[tracing-txtai-databricks-on-aws.md]

## Tracing with [MLflow](/concepts/mlflow.md)

When [MLflow Tracing](/concepts/mlflow-tracing.md) is enabled via `mlflow.[txtai](/concepts/txtai.md).autolog()`, the [txtai](/concepts/txtai.md) Agent's execution is automatically traced. Each tool invocation, reasoning step, and LLM call is captured as a trace and logged to the active [MLflow Experiment](/concepts/mlflow-experiment.md). This allows developers to observe the agent's decision-making process and debug its behavior. ^[tracing-txtai-databricks-on-aws.md]

### Prerequisites for Tracing

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with [txtai](/concepts/txtai.md) Agent:

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" [[txtai|txtai]] mlflow-txtai
```

Enable autologging before creating the agent:

```python
import [[mlflow|MLflow]]
[[mlflow|MLflow]].[[txtai|txtai]].autolog()
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/txtai-agent-demo")
```

^[tracing-txtai-databricks-on-aws.md]

On serverless compute clusters, [Autologging for GenAI Tracing](/concepts/autologging-for-genai-tracing.md) frameworks must be explicitly enabled; it is not automatic. ^[tracing-txtai-databricks-on-aws.md]

## Related Concepts

- [txtai](/concepts/txtai.md) — The all-in-one embeddings database and LLM orchestration framework
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Observability system for capturing agent [Traces](/concepts/traces.md)
- [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) — Another [txtai](/concepts/txtai.md) pipeline pattern for question answering
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluating agent quality on Databricks
- Embeddings Search — The similarity search mechanism used by the agent's tools

## Sources

- tracing-txtai-databricks-on-aws.md

# Citations

1. [tracing-txtai-databricks-on-aws.md](/references/tracing-txtai-databricks-on-aws-a07dafba.md)
