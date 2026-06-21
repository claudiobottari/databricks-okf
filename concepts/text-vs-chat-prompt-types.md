---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f4c25da92cc9f7617bade6424ec63b16a19bf330f706f9dc592a4a579014c01
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - text-vs-chat-prompt-types
    - TVCPT
    - Chat Prompts
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Text vs Chat Prompt Types
description: "MLflow Prompt Registry supports two prompt types: 'Text' for single completion-style templates and 'Chat' for role-based multi-message prompts targeting conversational models."
tags:
  - mlflow
  - prompt-types
  - llm-patterns
timestamp: "2026-06-19T17:58:47.455Z"
---

# Text vs Chat Prompt Types

The **Prompt Registry** supports two distinct prompt types: **Text** and **Chat. ** The type you choose determines the structure of your prompt template and which style of language model it targets. ^[create-and-edit-prompts-databricks-on-aws.md]

## Text Prompt Type

A **Text** prompt is a single text template. It is designed for use with **completion-style** language models—models that take a single input string and produce a text completion. ^[create-and-edit-prompts-databricks-on-aws.md]

When creating a Text prompt, you provide one block of template text. Variables are defined using `{{variable_name}}` syntax within that single block. The template is filled in at runtime by substituting the variable placeholders with actual values. ^[create-and-edit-prompts-databricks-on-aws.md]

**When to use:** Choose Text for models that accept a single prompt string, such as traditional completion APIs and many older-generation LLMs.

## Chat Prompt Type

A **Chat** prompt is a list of role-based messages. It is designed for use with **chat-style** or **conversational** models—models that expect a structured conversation history, typically with roles such as `system`, `user`, and `assistant`. ^[create-and-edit-prompts-databricks-on-aws.md]

Each message in a Chat prompt has two attributes:
- **Role**: The speaker in the conversation (e.g., `system`, `user`, `assistant`).
- **Content**: The text of that message, which can include `{{variable_name}}` placeholders.

This structure mirrors the input format of popular conversational models like GPT-4 and Claude, which use a messages array with role–content pairs. ^[create-and-edit-prompts-databricks-on-aws.md]

**When to use:** Choose Chat for models that accept a structured conversation, such as chat completion APIs and agentic evaluation workflows. ^[create-and-edit-prompts-databricks-on-aws.md]

## Selecting the Prompt Type

When creating a new prompt in the Databricks MLflow UI or via the MLflow Python SDK, the **Prompt type** field offers two options: **Text** and **Chat**. The UI displays these as radio buttons, and the SDK accepts the type implicitly based on the template structure (though the registry metadata records the type). ^[create-and-edit-prompts-databricks-on-aws.md]

The Prompt Registry stores the type as part of the prompt version metadata, allowing downstream tooling to validate that the prompt template is compatible with the target model. ^[create-and-edit-prompts-databricks-on-aws.md]

## Example: Text vs Chat in Practice

**Text prompt (completion-style):**
```
Summarize content you are provided with in {{num_sentences}} sentences.
Content: {{content}}
```
^[create-and-edit-prompts-databricks-on-aws.md]

**Chat prompt (conversational):**
```json
[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Summarize: {{content}} in {{num_sentences}} sentences."}
]
```
^[create-and-edit-prompts-databricks-on-aws.md]

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) – The system for registering, versioning, and discovering prompts.
- [Prompt Versioning](/concepts/prompt-versioning.md) – How prompts are managed with immutable versions.
- [LLM Completions](/concepts/completions-api.md) – The model API pattern that Text prompts target.
- [LLM Chat Completions](/concepts/chat-completions-api.md) – The model API pattern that Chat prompts target.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The MLflow subsystem for managing prompts and evaluations.
- Create and Edit Prompts – The full workflow for creating and managing both prompt types.

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
