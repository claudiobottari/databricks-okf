---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c765f563010544e58c9b37a29f3e70f7dd0fb01adb60e393c26594093b15c9b
  pageDirectory: concepts
  sources:
    - prompt-registry-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-versioning
    - App and Prompt Versioning
    - App and prompt versioning
    - Prompt Versions
    - PromptVersion
    - prompt version
    - prompt versions
    - Evaluating Prompt Versions
    - Evaluation of Prompt Versions
    - Prompt Version (MLflow)
    - Prompt Version Control
    - Prompts
    - Track Prompts with App Versions
    - Track prompts with app versions
    - Tracking Prompts with App Versions
    - prompts
  citations:
    - file: prompt-registry-databricks-on-aws.md
title: Prompt Versioning
description: Git-like version control for prompt templates, providing immutable snapshots with auto-incrementing version numbers, commit messages, and rollback capabilities.
tags:
  - mlflow
  - version-control
  - prompt-management
  - mlops
timestamp: "2026-06-19T19:58:08.391Z"
---

# Prompt Versioning

**Prompt versioning** is the practice of managing changes to prompt templates over time, enabling teams to track iterations, roll back to previous states, and systematically compare different versions to identify the best performing prompt. Versioning is a core capability of the [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md), which provides a Git-like model for prompt lifecycle management.^[prompt-registry-databricks-on-aws.md]

## Overview

Prompt versioning follows a Git-like model where prompt templates are stored as named entities in a [Unity Catalog](/concepts/unity-catalog.md) schema, and each change produces an immutable snapshot with an auto-incrementing version number. The Prompt Registry supports versions, aliases, and tags, enabling teams to version and track prompts with commit messages and rollback capabilities.^[prompt-registry-databricks-on-aws.md]

Each version can carry a commit message — a short description that helps track changes across versions — and version-specific tags (key-value pairs) for metadata such as author, use case, or improvement notes.^[prompt-registry-databricks-on-aws.md]

## Version Immutability

Prompt versions are immutable after creation. To edit a prompt, you must create a new version. This immutability ensures complete lineage and enables reliable rollbacks: any previous version can be loaded by its version number or by an alias such as `"production"`.^[prompt-registry-databricks-on-aws.md]

## Creating a New Version

### Using the Python SDK

To create a new version, call `mlflow.genai.register_prompt()` with the same name under an existing prompt, passing a new template and an optional commit message:^[prompt-registry-databricks-on-aws.md]

```python
import mlflow

# Register a new version of an existing prompt
updated_prompt = mlflow.genai.register_prompt(
    name="docs.default.customer_support",
    template="You are a helpful assistant. Answer this question: {{question}}",
    commit_message="Added detailed instructions for better output quality",
    tags={
        "author": "data-science-team@company.com",
        "improvement": "Added specific guidelines for summary quality"
    }
)
```

The returned `updated_prompt.version` shows the auto-incremented version number.^[prompt-registry-databricks-on-aws.md]

### Using the Databricks MLflow UI

1. On the **Prompts** tab of your MLflow experiment, locate the prompt you want to edit.
2. Click the **New version** button (next to the prompt name).
3. Type your revised prompt content and click **Save**.^[prompt-registry-databricks-on-aws.md]

## Comparing Prompt Versions

The MLflow UI and SDK provide tools to compare different prompt versions side-by-side, enabling systematic evaluation:^[prompt-registry-databricks-on-aws.md]

1. On the **Prompts** tab, click the prompt name.
2. At the upper left, click **Compare** and select the versions to compare.

The comparison view highlights differences between templates, allowing teams to assess which version better satisfies quality criteria before promoting it to production.^[prompt-registry-databricks-on-aws.md]

## Loading a Specific Version

Versions can be loaded by URI syntax, specifying either the version number or an alias:^[prompt-registry-databricks-on-aws.md]

```python
# Load by version number
prompt = mlflow.genai.load_prompt(
    name_or_uri="prompts:/docs.default.customer_support/2"
)

# Load by version parameter (equivalent)
prompt = mlflow.genai.load_prompt(
    name_or_uri="docs.default.customer_support",
    version="2"
)

# Load by alias (e.g., "production")
prompt = mlflow.genai.load_prompt(
    name_or_uri="prompts:/docs.default.customer_support@production"
)
```

## Versioning and Aliases

[Aliases](/concepts/model-aliases.md) are mutable references that point to specific prompt versions. They enable safe deployment strategies: a `"production"` alias can be moved to a new version after validation, while a `"staging"` alias points to a candidate version for A/B testing. Aliases are managed with `mlflow.genai.set_prompt_alias()`.^[prompt-registry-databricks-on-aws.md]

## Versioning and Lineage Tracking

Prompt versions are linked to [MLflow experiments](/concepts/mlflow-experiment.md) and evaluation results, providing full lineage from prompt template through application output. The Prompt Registry tracks version history, enabling audit trails and governance through Unity Catalog integration.^[prompt-registry-databricks-on-aws.md]

## Best Practices

- **Always include a commit message.** Commit messages help teams understand what changed and why across versions.
- **Use version-specific tags.** Tags such as `"author"`, `"use_case"`, or `"improvement"` provide metadata that aids search and discovery.
- **Systematically compare versions.** Use the compare UI or evaluate prompts workflows to validate that a new version meets quality criteria before promoting it.
- **Maintain immutable history.** Never overwrite a version; create a new one. This preserves the ability to roll back to any previous state.

## Related Concepts

- [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md) — The centralized repository for prompt management
- [Aliases](/concepts/model-aliases.md) — Mutable pointers to specific prompt versions for safe deployment
- [Prompt Templates](/concepts/prompt-templates-with-variables.md) — The template strings with `{{variable}}` syntax stored in the registry
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer providing schema and permissions for prompts
- [Prompt Evaluation](/concepts/prompt-version-evaluation.md) — Systematically comparing prompt versions using quality scorers

## Sources

- prompt-registry-databricks-on-aws.md

# Citations

1. [prompt-registry-databricks-on-aws.md](/references/prompt-registry-databricks-on-aws-71dbf9b1.md)
