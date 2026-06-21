---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 19d9d294afbea37016c5e8290022c899a141fdf625c1a576ec95ea23b1cb842f
  pageDirectory: concepts
  sources:
    - prompt-registry-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-brace-format-compatibility
    - SFC
  citations:
    - file: prompt-registry-databricks-on-aws.md
title: Single-Brace Format Compatibility
description: MLflow's conversion mechanism between its native double-brace template syntax and the single-brace Python f-string syntax used by LangChain, LlamaIndex, and other GenAI frameworks.
tags:
  - mlflow
  - compatibility
  - langchain
  - llamaindex
timestamp: "2026-06-19T19:58:45.030Z"
---

# Single-Brace Format Compatibility

**Single-Brace Format Compatibility** refers to the ability to convert prompt templates stored in the [Prompt Registry](/concepts/prompt-registry.md) from the native double-brace syntax (`{{variable}}`) to a single-brace syntax (`{variable}`) for compatibility with downstream frameworks such as LangChain and LlamaIndex.

## Background

The MLflow Prompt Registry stores prompt templates using a double-brace syntax: `"Hello {{name}}"`. This is the native format for templates registered via `mlflow.genai.register_prompt()` and is also used with `mlflow.genai.load_prompt()` when formatting prompts directly with the `.format()` method. ^[prompt-registry-databricks-on-aws.md]

## Compatibility Need

LangChain, LlamaIndex, and some other libraries support single-brace syntax (Python f-string syntax) for prompt templates, such as `"Hello {name}"`. When integrating a prompt from the Prompt Registry into these frameworks, the double-brace format is not directly compatible and must be converted. ^[prompt-registry-databricks-on-aws.md]

## Conversion Method

MLflow provides a `to_single_brace_format()` method on loaded prompts to perform this conversion. The following example demonstrates the workflow for using a Prompt Registry prompt with LangChain:

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

The same pattern applies when integrating with LlamaIndex, where the converted single-brace template can be passed to LlamaIndex's prompt constructs. ^[prompt-registry-databricks-on-aws.md]

## Supported Frameworks

The conversion method is explicitly documented as compatible with:

- LangChain
- LlamaIndex

Other frameworks that use single-brace (Python f-string) syntax for prompt templates may also benefit from this conversion, though only LangChain and LlamaIndex are explicitly mentioned in the documentation. ^[prompt-registry-databricks-on-aws.md]

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) — Centralized repository for managing prompt templates
- [Prompt Template Formats](/concepts/prompt-template-formats.md) — Overview of simple and conversation-style prompts
- [Prompt Version Management](/concepts/prompt-version-management.md) — Versioning, aliases, and lifecycle management
- LangChain Integration — Using Databricks prompts within LangChain applications
- LlamaIndex Integration — Using Databricks prompts within LlamaIndex applications

## Sources

- prompt-registry-databricks-on-aws.md

# Citations

1. [prompt-registry-databricks-on-aws.md](/references/prompt-registry-databricks-on-aws-71dbf9b1.md)
