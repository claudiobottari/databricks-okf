---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8add0841b8faf4f1b7fad51a60f33572ec9d096857a225a20c04dcb885711984
  pageDirectory: concepts
  sources:
    - built-in-llm-judges-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tool-call-evaluation-judges
    - TCEJ
    - ToolCallEfficiency judge
  citations:
    - file: built-in-llm-judges-databricks-on-aws.md
title: Tool call evaluation judges
description: Built-in LLM judges (ToolCallCorrectness, ToolCallEfficiency) that assess whether tool calls and arguments are correct for a user query, and whether they are made without redundancy.
tags:
  - llm-evaluation
  - tool-use
  - function-calling
  - mlflow
timestamp: "2026-06-18T10:55:31.932Z"
---

# Tool call evaluation judges

**Tool call evaluation judges** are a category of [Built-in LLM Judges](/concepts/built-in-llm-judges.md) that specifically evaluate the quality of tool (or function) calls made by an LLM agent. They assess whether the model correctly selects and invokes the right tools with appropriate arguments, and whether the tool usage pattern is efficient and free from unnecessary redundancy. ^[built-in-llm-judges-databricks-on-aws.md]

These judges are designed for GenAI applications that rely on external [tool calling](/concepts/llm-function-calling.md) or function-calling workflows, such as AI agents that invoke APIs, databases, or other services through structured function calls.

## Available judges

Two tool‑call‑specific judges are currently provided in the built-in set:

| Judge | Arguments | Requires ground truth | What it evaluates |
|-------|-----------|-----------------------|-------------------|
| **`ToolCallCorrectness`** | `inputs`, `outputs`, `expectations` | Yes | Are the tool calls and arguments correct for the user query? |
| **`ToolCallEfficiency`** | `inputs`, `outputs` | No | Are the tool calls efficient without unnecessary redundancy? |

^[built-in-llm-judges-databricks-on-aws.md]

### `ToolCallCorrectness`

The `ToolCallCorrectness` judge evaluates whether the LLM’s tool calls and their arguments are correct for the given user query. It requires a ground‑truth `expectations` column so that the judge can compare the model’s output against the known correct set of tool calls. Use this judge when you have a ground‑truth dataset and need to verify that the agent invokes the right tools with the right parameters. ^[built-in-llm-judges-databricks-on-aws.md]

### `ToolCallEfficiency`

The `ToolCallEfficiency` judge evaluates whether the tool calls are efficient — specifically, whether the model avoids unnecessary redundancy in its tool‑calling pattern. It does **not** require ground truth; it assesses efficiency purely from the `inputs` and `outputs` of the system. A high‑efficiency score means the model makes the fewest and most relevant tool calls needed to complete the task. ^[built-in-llm-judges-databricks-on-aws.md]

## Detailed documentation

For the complete specification, including scoring rubric, prompt templates, and configuration options, see the MLflow predefined scorers documentation pages for each judge:

- [`ToolCallCorrectness` documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/tool-call/correctness/)
- [`ToolCallEfficiency` documentation](https://mlflow.org/docs/latest/genai/eval-monitor/scorers/llm-judge/tool-call/efficiency/)

## Related concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – The category of predefined LLM‑based scorers that includes tool‑call judges
- [Tool calling](/concepts/llm-function-calling.md) – The function‑calling pattern that these judges evaluate
- [Custom LLM Judges](/concepts/custom-llm-judges.md) – An alternative when built‑in tool‑call judges do not fit your use case
- MLflow predefined scorers – The full list of predefined scorers in MLflow
- AI agents – Applications that commonly use tool‑calling patterns

## Sources

- built-in-llm-judges-databricks-on-aws.md

# Citations

1. [built-in-llm-judges-databricks-on-aws.md](/references/built-in-llm-judges-databricks-on-aws-15825704.md)
