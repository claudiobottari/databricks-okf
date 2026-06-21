---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43c26d4fa19ce7c6c831c14d2cf82cc18849625009bb0184e706640926388713
  pageDirectory: concepts
  sources:
    - prompt-registry-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-template-formats
    - PTF
  citations:
    - file: prompt-registry-databricks-on-aws.md
title: Prompt Template Formats
description: "Two supported prompt storage formats in the Prompt Registry: simple string prompts and conversation-style (chat) prompts, both using double-brace syntax for template variables."
tags:
  - mlflow
  - prompts
  - templates
  - llm
timestamp: "2026-06-19T19:58:56.880Z"
---

# Prompt Template Formats

**Prompt Template Formats** refer to the structural patterns in which prompt templates can be stored and managed within the MLflow Prompt Registry. These formats determine how templates are represented, how variables are interpolated, and how prompts can be consumed by different GenAI frameworks.

## Overview

The MLflow Prompt Registry supports two primary template formats: **simple prompts** (single string) and **conversation-style prompts** (structured multi-turn dialogues). Both formats can contain template variables using the double-brace syntax `{{variable}}`. This syntax allows dynamic content insertion at runtime, making prompts reusable across different contexts and users. ^[prompt-registry-databricks-on-aws.md]

## Simple Prompt Format

A **simple prompt** is a single string template that contains one or more placeholder variables. This format is suitable for straightforward instructions or queries where the entire prompt is a single message.

```python
simple_prompt = mlflow.genai.register_prompt(
    name="mycatalog.myschema.greeting",
    template="Hello {{name}}, how can I help you today?",
    commit_message="Simple greeting"
)
```

^[prompt-registry-databricks-on-aws.md]

## Conversation-Style Prompt Format

A **conversation or chat-style prompt** is structured as a list of message dictionaries, each with a `role` and `content` field. This format enables multi-turn interactions where different roles (e.g., `system`, `user`) can each contain their own template variables.

```python
complex_prompt = mlflow.genai.register_prompt(
    name="mycatalog.myschema.analysis",
    template=[
        {"role": "system", "content": "You are a helpful {{style}} assistant."},
        {"role": "user", "content": "{{question}}"},
    ],
    commit_message="Multi-variable analysis template"
)
```

^[prompt-registry-databricks-on-aws.md]

## Template Variable Syntax

Both formats use the **double-brace syntax** (`{{variable}}`) to denote template variables. When a prompt is rendered, these placeholders are replaced with the values provided at runtime:

```python
rendered = complex_prompt.format(
    style="edgy",
    question="What is a good costume for a rainy Halloween?"
)
```

^[prompt-registry-databricks-on-aws.md]

## Single-Brace Format Compatibility

LangChain, LlamaIndex, and other libraries support **single-brace syntax** (Python f-string syntax: `{variable}`) for prompt templates. MLflow provides compatibility via the `to_single_brace_format()` method, which converts prompts from the registry into the single-brace format expected by those frameworks.

```python
from langchain_core.prompts import ChatPromptTemplate

# Load from registry
mlflow_prompt = mlflow.genai.load_prompt("prompts:/mycatalog.myschema.chat@production")

# Convert to LangChain format
langchain_template = mlflow_prompt.to_single_brace_format()
chat_prompt = ChatPromptTemplate.from_template(langchain_template)

# Use in chain
chain = chat_prompt | llm | output_parser
```

^[prompt-registry-databricks-on-aws.md]

## Framework Integration

The Prompt Registry supports integration with multiple GenAI frameworks, including LangChain, LlamaIndex, and others. Each framework may have its own preferred template syntax, but the registry's conversion utilities ensure compatibility across ecosystems. The double-brace (mustache syntax) is the native format for the registry, while the single-brace conversion provides backward compatibility with frameworks that expect Python f-string style interpolation. ^[prompt-registry-databricks-on-aws.md]

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) – Centralized repository for managing prompt templates
- [Prompt Versioning](/concepts/prompt-versioning.md) – Git-like versioning for prompt templates
- [Prompt Aliases](/concepts/prompt-aliases.md) – Mutable pointers to specific prompt versions
- Template Variables – Placeholders for dynamic content in prompts
- [Multi-Turn Conversations](/concepts/multi-turn-conversation-judges.md) – Structured interaction patterns in conversation-style prompts

## Sources

- prompt-registry-databricks-on-aws.md

# Citations

1. [prompt-registry-databricks-on-aws.md](/references/prompt-registry-databricks-on-aws-71dbf9b1.md)
