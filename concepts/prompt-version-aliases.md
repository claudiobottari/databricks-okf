---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2fb1d557f4450d71821760bb54bcc87a71f14fa6a7964454dc73943202962f31
  pageDirectory: concepts
  sources:
    - prompt-registry-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-version-aliases
    - PVA
  citations:
    - file: prompt-registry-examples-databricks-on-aws.md
title: Prompt Version Aliases
description: Assigning aliases (e.g. 'production', 'staging') to specific prompt versions to manage deployment stages without referencing version numbers.
tags:
  - mlflow
  - prompt-management
  - deployment
timestamp: "2026-06-19T19:58:42.570Z"
---

# Prompt Version Aliases

**Prompt Version Aliases** are human-readable labels that can be assigned to specific versions of a prompt in the Prompt Registry, allowing users to reference a prompt version by a meaningful name (such as "production" or "staging") instead of a numeric version number. ^[prompt-registry-examples-databricks-on-aws.md]

## Overview

Aliases provide a way to tag prompt versions with semantic labels that reflect their lifecycle stage or purpose. Once an alias is set, it can be used to load the associated prompt version, enabling workflows where the underlying prompt version can be updated without changing the alias reference in application code. ^[prompt-registry-examples-databricks-on-aws.md]

## Setting an Alias

The `mlflow.genai.set_prompt_alias()` function assigns an alias to a specific version of a prompt. The function takes three parameters: the prompt name, the alias string, and the version number to associate with that alias. ^[prompt-registry-examples-databricks-on-aws.md]

```python
import mlflow

# Promote version 3 to production
mlflow.genai.set_prompt_alias(
    name="mycatalog.myschema.chat_assistant",
    alias="production",
    version=3
)

# Set up staging for testing
mlflow.genai.set_prompt_alias(
    name="mycatalog.myschema.chat_assistant",
    alias="staging",
    version=4
)
```

^[prompt-registry-examples-databricks-on-aws.md]

## Common Use Cases

- **Production alias**: Assign the alias `"production"` to the current best version of a prompt deployed for end users. ^[prompt-registry-examples-databricks-on-aws.md]
- **Staging alias**: Assign the alias `"staging"` to a candidate version undergoing pre-release testing. ^[prompt-registry-examples-databricks-on-aws.md]
- **Rollback scenarios**: If a production issue is detected, the `"production"` alias can be reassigned to a previous known-good version. ^[prompt-registry-examples-databricks-on-aws.md]

## Loading Prompts by Alias

Once an alias is set, it can be used in the prompt URI format to load the associated version. For example, a prompt with the URI `prompts:/docs.default.customer_support/production` would load whichever version currently has the `"production"` alias. ^[prompt-registry-examples-databricks-on-aws.md]

## API Reference

- [`mlflow.genai.set_prompt_alias`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.set_prompt_alias) — Sets an alias on a specific prompt version. ^[prompt-registry-examples-databricks-on-aws.md]
- [`mlflow.genai.load_prompt`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.load_prompt) — Loads a prompt by name, version, or alias URI. ^[prompt-registry-examples-databricks-on-aws.md]
- [`mlflow.genai.register_prompt`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.register_prompt) — Registers a new prompt in the registry. ^[prompt-registry-examples-databricks-on-aws.md]

## Related Concepts

- [Prompt Registry](/concepts/prompt-registry.md) — The central system for managing prompt versions and aliases.
- [Prompt Versioning](/concepts/prompt-versioning.md) — How prompts are tracked and versioned over time.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational units for MLflow runs and prompt evaluation.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — A related concept for managing model versions (analogous to prompt versioning).

## Sources

- prompt-registry-examples-databricks-on-aws.md

# Citations

1. [prompt-registry-examples-databricks-on-aws.md](/references/prompt-registry-examples-databricks-on-aws-c1a1a7e0.md)
