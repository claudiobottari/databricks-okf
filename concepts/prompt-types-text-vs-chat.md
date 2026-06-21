---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 36bbd601b9bc5547dbcaed0f41ae0398ba52e05de0cf8e7e9c0531b0347b799a
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-types-text-vs-chat
    - PTTVC
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: "Prompt Types: Text vs Chat"
description: "Two prompt types supported in the MLflow Prompt Registry: Text (single completion-style template) and Chat (list of role-based messages for conversational models)."
tags:
  - mlflow
  - prompt-management
  - llm
timestamp: "2026-06-19T14:32:52.368Z"
---

# Prompt Types: Text vs Chat

When creating prompts in the [Prompt Registry](/concepts/prompt-registry.md), you choose between two prompt types: **Text** and **Chat**. The type determines how the prompt is structured and which model families it targets.

## Overview

The Prompt Registry supports two prompt types when you create a new prompt. Your choice depends on whether you are building a completion-style prompt or a conversational, role-based prompt.^[create-and-edit-prompts-databricks-on-aws.md]

## Text Prompts

**Text** prompts use a single text template without role labels. They are intended for completion-style prompting, where the model receives a string of text and generates a continuation.^[create-and-edit-prompts-databricks-on-aws.md]

Use the Text type when your workflow does not require explicit system, user, or assistant roles — for example, one-shot text generation tasks, summarization, or extraction.

## Chat Prompts

**Chat** prompts use a list of role-based messages (for example, `system` and `user`). They are intended for conversational models that expect structured, multi-turn inputs.^[create-and-edit-prompts-databricks-on-aws.md]

Use the Chat type when you need to separate the model's system instructions from user input, or when you are building a dialogue-style application. Each message in the list carries a role label, and the entire message list is sent to the model in order.

## Template Variables

Both prompt types support `{{variable_name}}` syntax to define variables that you fill in at runtime.^[create-and-edit-prompts-databricks-on-aws.md]

For example, a Text prompt template:
```
Summarize the following content in {{num_sentences}} sentences:
{{content}}
```

A Chat prompt template might use variables inside each message's content field, such as `{{user_message}}` in the user role and `{{system_instructions}}` in the system role.

## When to Use Each Type

| Prompt Type | Best For | Model Style |
|-------------|----------|-------------|
| **Text** | Single-turn completion tasks, simple generation | Completion-style models |
| **Chat** | Conversational agents, assistant-style interactions, multi-turn applications | Chat-style models |

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) — Centralized prompt version management
- [Prompt Versioning](/concepts/prompt-versioning.md) — Immutable version history for prompts
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The broader framework for prompt management and evaluation
- Template Variables — Runtime substitution in prompt templates

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
