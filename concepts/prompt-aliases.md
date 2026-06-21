---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7049879d0724350d7d232be9ac51c0f5c8db410e0f0756490d0be4f9135b0a21
  pageDirectory: concepts
  sources:
    - prompt-registry-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-aliases
  citations:
    - file: prompt-registry-databricks-on-aws.md
title: Prompt Aliases
description: Mutable pointers (e.g., 'production', 'staging') that reference specific prompt versions, enabling safe deployment strategies like A/B testing and gradual rollouts.
tags:
  - mlflow
  - deployment
  - prompt-management
  - mlops
timestamp: "2026-06-19T19:58:29.525Z"
---

# Prompt Aliases

**Prompt Aliases** are mutable, human-readable references that point to specific versions of a prompt in the [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md). They enable teams to deploy prompts safely by decoupling application code from fixed version numbers, supporting A/B testing, gradual rollouts, and production deployment patterns. ^[prompt-registry-databricks-on-aws.md]

## Overview

In the Prompt Registry's Git-like versioning model, aliases serve as mutable pointers to specific, immutable prompt versions. This design allows teams to update which version of a prompt an application uses without modifying code — simply change the alias assignment in the registry. ^[prompt-registry-databricks-on-aws.md]

Common aliases include `"production"`, `"staging"`, and `"champion"`, though any string can be used as an alias. Using standard aliases like `"production"` makes deployment and rollback workflows clear and consistent across teams. ^[prompt-registry-databricks-on-aws.md]

## How Aliases Work

The Prompt Registry follows a model analogous to Git: ^[prompt-registry-databricks-on-aws.md]

| Concept | Description |
|---------|-------------|
| **Prompts** | Named entities stored in Unity Catalog |
| **Versions** | Immutable snapshots with auto-incrementing numbers |
| **Aliases** | Mutable pointers to specific versions |
| **Tags** | Version-specific key-value pairs |

Aliases can be reassigned to point to a different version at any time. When an alias is updated, all applications referencing `prompts:/catalog.schema.prompt_name@alias` automatically begin using the new version. ^[prompt-registry-databricks-on-aws.md]

## Setting and Using Aliases

### Setting an Alias via the SDK

Use `mlflow.genai.set_prompt_alias()` to assign an alias to a specific prompt version:

```python
import mlflow

# Set a production alias
mlflow.genai.set_prompt_alias(
    name="docs.default.customer_support",
    alias="production",
    version=1
)
```

^[prompt-registry-databricks-on-aws.md]

### Loading a Prompt by Alias

Prompts are loaded by URI using the scheme `prompts:/` followed by the prompt name and alias, separated by `@`:

```python
prompt = mlflow.genai.load_prompt(
    name_or_uri="prompts:/docs.default.customer_support@production"
)
formatted_prompt = prompt.format(question="How do I reset my password?")
```

^[prompt-registry-databricks-on-aws.md]

### Typical Alias Lifecycle

A common workflow uses aliases for staging and production deployment:

1. Create version 1 of a prompt and assign alias `"staging"`
2. Test the prompt in a staging environment
3. Reassign the `"production"` alias to version 1 after testing passes
4. Create version 2, assign `"staging"` to version 2 for testing
5. When ready, reassign `"production"` to version 2 for production rollout
6. If issues arise, reassign `"production"` back to version 1 for rollback

## Benefits

- **No code changes for updates**: Non-engineers can modify prompts through the UI without requiring application deployments ^[prompt-registry-databricks-on-aws.md]
- **Safe rollbacks**: Quickly revert to a previous version by changing alias assignment ^[prompt-registry-databricks-on-aws.md]
- **A/B testing**: Compare prompt versions by having different aliases point to different versions for evaluation ^[prompt-registry-databricks-on-aws.md]
- **Gradual rollouts**: Phase changes by updating aliases incrementally across environments ^[prompt-registry-databricks-on-aws.md]

## Related Concepts

- [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md) — Centralized repository for managing prompt templates
- [Prompt Versioning](/concepts/prompt-versioning.md) — Immutable snapshots with auto-incrementing version numbers
- [Prompt Evaluation](/concepts/prompt-version-evaluation.md) — Systematic comparison of prompt versions
- Deploy Prompts to Production — End-to-end deployment workflows using aliases

## Sources

- prompt-registry-databricks-on-aws.md

# Citations

1. [prompt-registry-databricks-on-aws.md](/references/prompt-registry-databricks-on-aws-71dbf9b1.md)
