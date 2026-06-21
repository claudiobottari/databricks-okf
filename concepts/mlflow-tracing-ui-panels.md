---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 564c6e1244415c385f491c4e06c977900684ed042e52126fd802aa9f55db28ea
  pageDirectory: concepts
  sources:
    - tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-ui-panels
    - MTUP
  citations:
    - file: tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md
title: MLflow Tracing UI Panels
description: MLflow provides a Chat tab for rich message visualization (supported by converse/converse_stream APIs) and an Inputs/Outputs tab for raw payload inspection, including configuration parameters.
tags:
  - mlflow
  - ui
  - observability
timestamp: "2026-06-19T23:08:47.976Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) UI Panels

The **MLflow Tracing UI Panels** are the visual components in the [MLflow](/concepts/mlflow.md) user interface that display detailed information about traced invocations of large language models (LLMs), agents, and other AI workflows. When [Automatic Tracing](/concepts/automatic-tracing.md) is enabled for integrations such as Amazon Bedrock, [MLflow](/concepts/mlflow.md) captures execution data and presents it through several specialized panels within the trace view. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Chat Tab

The **Chat** tab provides a rich, chat-like interface for displaying input and output messages from LLM interactions. This panel is designed to render conversational exchanges in a human-readable format, showing prompts and completion responses as messages in a conversation thread. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

The Chat tab is only supported for certain APIs — specifically the `converse` and `converse_stream` APIs from Amazon Bedrock. For other API types, this panel is not available, and [MLflow](/concepts/mlflow.md) displays only the Inputs/Outputs tab instead. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

When tracing streaming calls, the Chat tab shows the aggregated output message — the complete response assembled from all chunks. The individual stream chunks are displayed separately in the **Events** tab. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

The Chat tab also highlights function calling metadata automatically captured by [MLflow Tracing](/concepts/mlflow-tracing.md). Function definitions and tool instructions returned in the model's response are visually emphasized within the chat interface. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Inputs / Outputs Tab

The **Inputs / Outputs** tab displays the raw input and output payloads for each traced invocation. This panel shows the complete, unmodified request and response data, including configuration parameters such as model name, temperature, max tokens, and top-p settings. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

This panel is available for all supported APIs and serves as the primary display for tracing data when the Chat panel is not supported (for example, when using the `invoke_model` or `invoke_model_with_response_stream` APIs). ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Events Tab

The **Events** tab displays individual stream chunks when tracing streaming API calls. When a streaming response is consumed — for example, by iterating through chunks in a for-loop — each chunk is recorded as a separate event in this panel. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

This panel provides granular visibility into the streaming behavior of LLM invocations, showing the sequence of partial responses as they are received from the model. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

## Trace Call Chain

When using [Manual Tracing](/concepts/manual-tracing.md) features like the `@mlflow.trace` decorator alongside [Automatic Tracing](/concepts/automatic-tracing.md), [MLflow](/concepts/mlflow.md) resolves the full call chain across multiple decorated functions and LLM invocations. The UI displays spans for each traced component — such as agent logic and tool calls — connected in a hierarchical tree structure that shows the execution flow. ^[tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md]

For function-calling agents (ReAct patterns), the trace UI shows:

- **AGENT** spans for the top-level agent logic
- **TOOL** spans for individual function calls made by the agent
- **LLM** spans for each model invocation within the agent's execution

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — Overview of the tracing system for LLM workflows
- Amazon Bedrock Integration — Specific integration that populates these UI panels
- Span Types — The different span categories (AGENT, TOOL, LLM) displayed in the trace call chain
- [Streaming Trace Behavior](/concepts/streaming-trace-behavior-in-mlflow.md) — How streaming responses are handled and displayed
- [Function Calling](/concepts/llm-function-calling.md) — Tool-use patterns visible in the Chat tab

## Sources

- tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md

# Citations

1. [tracing-amazon-bedrock-with-mlflow-databricks-on-aws.md](/references/tracing-amazon-bedrock-with-mlflow-databricks-on-aws-2f3942c6.md)
