---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7ea93265668fac322e7dc48cc015da3e8270d472e4ea8c67908faad6250102e4
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
    - use-prompts-in-deployed-applications-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - prompt-template-variables
    - PTV
    - Template Variables
    - template variable
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
    - file: use-prompts-in-deployed-applications-databricks-on-aws.md
title: Prompt Template Variables
description: Double-brace syntax ({{variable_name}}) for defining dynamic placeholders in prompt templates that are filled at runtime.
tags:
  - mlflow
  - prompt-templates
  - llmops
timestamp: "2026-06-19T17:58:16.250Z"
---

# Prompt Template Variables

**Prompt Template Variables** are placeholders defined inside a prompt string that are replaced with concrete values at runtime. They enable dynamic, reusable prompts that can be adapted to different inputs without editing the prompt template itself. Prompt template variables are a core feature of the [MLflow Prompt Registry](/concepts/prompt-registry.md), allowing developers to separate prompt structure from the data it operates on. ^[create-and-edit-prompts-databricks-on-aws.md]

## Syntax

Variables are expressed using double curly braces: `{{variable_name}}`. The variable name should be descriptive of the data it represents. For example, a summarization prompt might use `{{num_sentences}}` for the desired number of output sentences and `{{content}}` for the text to summarize. ^[create-and-edit-prompts-databricks-on-aws.md]

```text
Summarize the following content in {{num_sentences}} sentences:
{{content}}
```

Variables can appear anywhere in the prompt template, including in system messages, user messages, and assistant messages for [Chat Prompts](/concepts/text-vs-chat-prompt-types.md).

## Defining Variables When Creating a Prompt

When you create a prompt using the MLflow Python SDK, you embed `{{variable_name}}` markers directly in the template string. Both text (completion-style) prompts and chat prompts support variables. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
import mlflow

# Define a prompt template with variables
template = """\
Summarize content you are provided with in {{num_sentences}} sentences.
Content: {{content}}
"""

# Register the prompt in the Prompt Registry
prompt = mlflow.genai.register_prompt(
    name="main.default.summarization_prompt",
    template=template,
    commit_message="Initial version of summarization prompt"
)
```

In the Databricks MLflow UI, you enter the template text including variable placeholders in the **Prompt** field of the new prompt dialog. The UI also accepts `{{variable_name}}` syntax. ^[create-and-edit-prompts-databricks-on-aws.md]

## Filling Variables at Runtime

When you load a prompt from the registry and use it in an application, you call `.format()` on the loaded prompt object, passing keyword arguments that correspond to the variable names. The method replaces each `{{variable_name}}` placeholder with the provided value. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
# Load the prompt
prompt = mlflow.genai.load_prompt(
    "prompts:/main.default.summarization_prompt/1"
)

# Fill variables with concrete values
formatted_prompt = prompt.format(
    content="This guide shows you how to integrate prompts "
            "from the MLflow Prompt Registry...",
    num_sentences=1
)
```

The resulting `formatted_prompt` is a string with the placeholders replaced by the supplied values. This string can then be passed to an LLM, for example as part of an API call. ^[create-and-edit-prompts-databricks-on-aws.md]

## Variables in Chat Prompts

Chat prompts use a list of role‑based messages (e.g., `system`, `user`). Each message in the list can contain `{{variable_name}}` placeholders. When you create a chat prompt in the MLflow UI, you select **Chat** as the **Prompt type** and then enter role‑labeled messages with variable markers. The same `.format()` method fills variables across all messages. ^[create-and-edit-prompts-databricks-on-aws.md]

## Using Variables with Prompt Aliases

Templates containing variables can be referenced in deployed applications using [Prompt Aliases](/concepts/prompt-aliases.md). The prompt URI format is `prompts:/{catalog}.{schema}.{prompt_name}@{alias}`. The MLflow client caches the prompt template, so the prompt registry does not introduce latency to your agent at runtime. Variables are still filled with `.format()` after loading the prompt by alias. ^[use-prompts-in-deployed-applications-databricks-on-aws.md]

## Best Practices

- **Use descriptive variable names** that clearly indicate what data the placeholder expects (e.g., `{{user_name}}`, `{{document_text}}`, `{{output_language}}`).
- **Keep sensitive data out of the template**. Variables should only carry dynamic content; never embed API keys or secrets in the prompt string itself.
- **Validate inputs** before calling `.format()` to prevent unexpected errors or injection of malformed content.
- **Version your prompts** when variable structure changes. Because prompt versions are immutable, a change to the set of variables requires creating a new version. See [Prompt Versioning](/concepts/prompt-versioning.md).

## Related Concepts

- [MLflow Prompt Registry](/concepts/prompt-registry.md) – Central repository for versioned prompts.
- [Chat Prompts](/concepts/text-vs-chat-prompt-types.md) – Role‑based prompt structures that also support template variables.
- [Prompt Versioning](/concepts/prompt-versioning.md) – Immutable versioning of prompts including their variable definitions.
- [Prompt Aliases](/concepts/prompt-aliases.md) – Static tags for referencing prompt versions in production.
- mlflow.genai.register_prompt() – API for creating prompts with variables.
- mlflow.genai.load_prompt() – API for loading prompts and formatting them.
- [Unity Catalog](/concepts/unity-catalog.md) – Schema where prompts are stored; variables are defined at the prompt level, not the catalog level.

## Sources

- create-and-edit-prompts-databricks-on-aws.md
- use-prompts-in-deployed-applications-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
2. [use-prompts-in-deployed-applications-databricks-on-aws.md](/references/use-prompts-in-deployed-applications-databricks-on-aws-4f504a27.md)
