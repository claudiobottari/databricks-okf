---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0fd95205fbbf9c190e315d11518150db0a0dd123f04792c498dfcfec73b5e019
  pageDirectory: concepts
  sources:
    - prompt-registry-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-registry-register_prompt
    - PRR
    - Prompt Registry delete_prompt
    - register_prompt
  citations:
    - file: prompt-registry-examples-databricks-on-aws.md
title: Prompt Registry register_prompt
description: Registering a new prompt in the Prompt Registry with template variables, commit messages, and metadata tags.
tags:
  - mlflow
  - prompt-management
  - prompt-registry
timestamp: "2026-06-19T19:58:26.720Z"
---

# Prompt Registry register_prompt

## Overview

`mlflow.genai.register_prompt` is an API function in the Prompt Registry that creates a new prompt with a specified name, template, and optional metadata. The function registers the prompt in the MLflow Prompt Registry, making it available for versioning, loading, and deployment. ^[prompt-registry-examples-databricks-on-aws.md]

## Syntax

```python
mlflow.genai.register_prompt(
    name="catalog.schema.prompt_name",
    template="Your prompt template with {{placeholders}}",
    commit_message="Description of changes",
    tags={...}
)
```

## Parameters

- **`name`** (string, required): The fully qualified name of the prompt in the format `catalog.schema.prompt_name`. For Unity Catalog registries, the name must include both the [Catalog and Schema](/concepts/catalog-and-schema.md). ^[prompt-registry-examples-databricks-on-aws.md]
- **`template`** (string, required): The prompt template content, which can include placeholders using double curly brace syntax (e.g., `{{num_sentences}}`, `{{content}}`). ^[prompt-registry-examples-databricks-on-aws.md]
- **`commit_message`** (string, required): A description of the changes made in this prompt version. ^[prompt-registry-examples-databricks-on-aws.md]
- **`tags`** (dictionary, optional): Key-value metadata pairs to attach to the prompt. Useful for tracking information such as tested models, latency measurements, team assignments, and project names. ^[prompt-registry-examples-databricks-on-aws.md]

## API Reference

The full API reference is available at [`mlflow.genai.register_prompt`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.register_prompt). ^[prompt-registry-examples-databricks-on-aws.md]

## Example

The following example registers a summarization prompt with a template that accepts `num_sentences`, `content`, and `focus_areas` as input parameters: ^[prompt-registry-examples-databricks-on-aws.md]

```python
import mlflow

prompt = mlflow.genai.register_prompt(
    name="mycatalog.myschema.summarization",
    template="""Summarize the following text in {{num_sentences}} sentences:
Text: {{content}}
Focus on: {{focus_areas}}""",
    commit_message="Added focus areas parameter",
    tags={
        "tested_with": "gpt-4",
        "avg_latency_ms": "1200",
        "team": "content",
        "project": "summarization-v2"
    }
)
```

## Related Operations

- Prompt Registry load_prompt — Loads a registered prompt by name and version for use in applications.
- Prompt Registry search_prompts — Searches for prompts in a [Catalog and Schema](/concepts/catalog-and-schema.md).
- Prompt Registry set_prompt_alias — Assigns aliases like "production" or "staging" to specific prompt versions.
- Prompt Registry delete_prompt — Deletes a prompt and all its versions from the registry.
- Prompt Registry delete_prompt_version — Deletes a specific version of a prompt.

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) — The MLflow system for managing, versioning, and deploying prompts.
- [Prompt Templates](/concepts/prompt-templates-with-variables.md) — Structured prompt content with placeholder variables.
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) that stores prompt registries, requiring [Catalog and Schema](/concepts/catalog-and-schema.md) specification.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs, which can be linked to prompts.

## Sources

- prompt-registry-examples-databricks-on-aws.md

# Citations

1. [prompt-registry-examples-databricks-on-aws.md](/references/prompt-registry-examples-databricks-on-aws-c1a1a7e0.md)
