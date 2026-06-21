---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c4e9a5b0974861f5c36bb9719e6eed59bdf9ef9ab4f6fbb2e1e1a400fbbbf033
  pageDirectory: concepts
  sources:
    - tracing-langgraph-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowlangchainautolog-for-langgraph
    - MFL
  citations:
    - file: tracing-langgraph-databricks-on-aws.md
title: mlflow.langchain.autolog() for LangGraph
description: The API call that enables automatic trace capture for LangGraph workflows, built on the LangChain autolog integration
tags:
  - mlflow
  - api
  - tracing
  - langchain
timestamp: "2026-06-19T23:13:28.731Z"
---

# [MLflow](/concepts/mlflow.md).langchain.autolog() for LangGraph

**mlflow.langchain.autolog()** is an [MLflow](/concepts/mlflow.md) function that enables [Automatic Tracing](/concepts/automatic-tracing.md) for LangGraph applications, building on [MLflow](/concepts/mlflow.md)'s existing LangChain integration. When called, it configures [MLflow](/concepts/mlflow.md) to automatically capture the execution of a LangGraph graph into a trace and log that trace to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-langgraph-databricks-on-aws.md]

## Overview

LangGraph is an open-source library for building stateful, multi-actor applications with [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md), commonly used to create agent and multi-agent workflows. [MLflow Tracing](/concepts/mlflow-tracing.md) provides [Automatic Tracing](/concepts/automatic-tracing.md) capability for LangGraph as an extension of its LangChain integration. By enabling auto-tracing through `mlflow.langchain.autolog()`, [MLflow](/concepts/mlflow.md) will automatically capture the graph execution—including each node, tool call, and LLM invocation—into a trace and log it to the active [MLflow Experiment](/concepts/mlflow-experiment.md). ^[tracing-langgraph-databricks-on-aws.md]

## Prerequisites

To use [MLflow Tracing](/concepts/mlflow-tracing.md) with LangGraph, you need to install [MLflow](/concepts/mlflow.md) (≥3.1 recommended) and the relevant LangGraph and LangChain packages. The full `mlflow[databricks]` package includes all features for local development and experimentation on Databricks. ^[tracing-langgraph-databricks-on-aws.md]

**Installation:**

```bash
pip install --upgrade "[[mlflow|MLflow]][databricks]>=3.1" langgraph langchain_core langchain_openai
```

## Usage

```python
import [[mlflow|MLflow]]
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

# Enable tracing for LangGraph (LangChain)
[[mlflow|MLflow]].langchain.autolog()

# Set up [[mlflow-tracking|MLflow Tracking]] to Databricks
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/langgraph-tracing-demo")

# Create and invoke a graph
llm = ChatOpenAI(model="gpt-4o-mini")
tools = [get_weather]
graph = create_react_agent(llm, tools)
result = graph.invoke({"messages": [{"role": "user", "content": "what is the weather in sf?"}]})
```

After calling `mlflow.langchain.autolog()`, any LangGraph graph invocation is automatically traced and logged to the experiment. ^[tracing-langgraph-databricks-on-aws.md]

## Adding Spans Within a Node or Tool

By combining auto-tracing with [Manual Tracing APIs](/concepts/manual-tracing-apis.md), you can add child spans inside a node or tool to get more detailed insights for a step. For example, in a `check_code` node that performs two different validations, you can create manual spans using `mlflow.start_span()` inside the node function: ^[tracing-langgraph-databricks-on-aws.md]

```python
def code_check(state: GraphState):
    # State
    messages = state["messages"]
    code_solution = state["generation"]
    # ... get solution components
    imports = code_solution.imports
    code = code_solution.code

    # Create a child span manually with [[mlflow|MLflow]].start_span() API
    with [[mlflow|MLflow]].start_span(name="import_check", span_type=SpanType.TOOL) as span:
        span.set_inputs(imports)
        exec(imports)
        span.set_outputs("ok")

    # Check execution
    try:
        code = imports + "\n" + code
        with [[mlflow|MLflow]].start_span(name="execution_check", span_type=SpanType.TOOL) as span:
            span.set_inputs(code)
            exec(code)
            span.set_outputs("ok")
    except Exception as e:
        # ... error handling
        pass
```

The `span_type` parameter accepts `SpanType.TOOL` or `SpanType.CHAIN` and helps categorize the span. This allows the `check_code` node to have child spans that record whether each validation passes or fails, with their exception details. ^[tracing-langgraph-databricks-on-aws.md]

## Disabling Auto-Tracing

Auto tracing for LangGraph can be disabled globally by calling `mlflow.langchain.autolog(disable=True)` or `mlflow.autolog(disable=True)`. ^[tracing-langgraph-databricks-on-aws.md]

## Notes

On [serverless compute clusters](/concepts/serverless-gpu-compute-databricks.md), autologging is not automatically enabled. You must explicitly call `mlflow.langchain.autolog()` to enable [Automatic Tracing](/concepts/automatic-tracing.md) for this integration. ^[tracing-langgraph-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The core tracing infrastructure that makes LangGraph tracing possible.
- LangGraph — An open-source library for building stateful, multi-actor applications with LLMs.
- LangChain — The broader framework. LangGraph tracing builds on LangChain's autologging integration.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for [MLflow](/concepts/mlflow.md) runs and [Traces](/concepts/traces.md).
- [Manual Tracing APIs](/concepts/manual-tracing-apis.md) — Methods for adding custom spans within nodes or tools.
- Agent Workflows — Common use case for LangGraph with multiple agents.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — How [MLflow Tracing](/concepts/mlflow-tracing.md) integrates with large-scale training.

## Sources

- tracing-langgraph-databricks-on-aws.md

# Citations

1. [tracing-langgraph-databricks-on-aws.md](/references/tracing-langgraph-databricks-on-aws-6240217a.md)
