---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 91df863824102886ef6fc4e86abc8232573430d5fcb05393da72451629ac1bd1
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-schema-as-prompt-registry-backend
    - UCSAPRB
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Unity Catalog Schema as Prompt Registry Backend
description: Prompts are stored in Unity Catalog schemas, which require specific permissions (CREATE FUNCTION, EXECUTE, MANAGE) and are linked to MLflow experiments via a tag.
tags:
  - databricks
  - unity-catalog
  - mlflow
  - permissions
timestamp: "2026-06-19T17:58:19.563Z"
---

# Unity Catalog Schema as Prompt Registry Backend

**Unity Catalog Schema as Prompt Registry Backend** refers to the use of a [Unity Catalog](/concepts/unity-catalog.md) schema as the storage and management layer for the [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md). When a Unity Catalog schema is configured as the prompt registry backend, all prompts, their versions, and associated metadata are stored within that schema, enabling governance, discovery, and lineage tracking across the Databricks platform.

## Overview

The MLflow Prompt Registry uses a Unity Catalog schema as its backend to store and manage prompt templates. This integration provides a centralized, governed location for prompt artifacts, leveraging Unity Catalog's existing permission model and metadata management capabilities. ^[create-and-edit-prompts-databricks-on-aws.md]

## Prerequisites

To use a Unity Catalog schema as a prompt registry backend, the schema must have the following permissions granted to the user or service principal:

- `CREATE FUNCTION`
- `EXECUTE`
- `MANAGE`

These permissions are required to view, create, and manage prompts within the schema. For Databricks trial accounts, the `main.default` schema comes with these permissions pre-configured. ^[create-and-edit-prompts-databricks-on-aws.md]

## Configuration

### Linking an Experiment to a Schema

To associate an MLflow experiment with a Unity Catalog schema for prompts, set the `mlflow.promptRegistryLocation` experiment tag to the desired [Catalog and Schema](/concepts/catalog-and-schema.md) name: ^[create-and-edit-prompts-databricks-on-aws.md]

```python
import mlflow

mlflow.set_experiment_tags({
    "mlflow.promptRegistryLocation": "main.default"
})
```

This tag allows SDKs and tools to automatically infer the Unity Catalog prompt schema location without requiring explicit specification in every API call. ^[create-and-edit-prompts-databricks-on-aws.md]

### Creating Prompts in a Schema

When creating a prompt, the prompt name includes the fully qualified Unity Catalog path in the format `catalog.schema.prompt_name`: ^[create-and-edit-prompts-databricks-on-aws.md]

```python
uc_schema = "main.default"
prompt_name = "summarization_prompt"

prompt = mlflow.genai.register_prompt(
    name=f"{uc_schema}.{prompt_name}",
    template="Summarize content in {{num_sentences}} sentences.\nContent: {{content}}",
    commit_message="Initial version of summarization prompt"
)
```

### Selecting a Schema in the UI

When creating a prompt through the Databricks MLflow UI, if no schema has been selected for the experiment, the **Target schema** field appears in the new prompt dialog. Users must select a Unity Catalog schema where they have the required permissions. ^[create-and-edit-prompts-databricks-on-aws.md]

## Prompt Versioning

Prompt versions are immutable after creation. Each new version is stored as a separate entry within the Unity Catalog schema, maintaining a complete version history. This Git-like versioning enables rollbacks and change tracking. ^[create-and-edit-prompts-databricks-on-aws.md]

## Searching and Discovery

Prompts stored in a Unity Catalog schema can be discovered using the `mlflow.genai.search_prompts()` function, which requires specifying the [Catalog and Schema](/concepts/catalog-and-schema.md) in the filter string: ^[create-and-edit-prompts-databricks-on-aws.md]

```python
results = mlflow.genai.search_prompts(
    filter_string="catalog = 'main' AND schema = 'default'",
    max_results=50
)
```

## Benefits

Using a Unity Catalog schema as the prompt registry backend provides:

- **Centralized governance**: Prompts are stored in a governed location with Unity Catalog's permission model
- **Lineage tracking**: Prompt versions are linked to MLflow experiments and models
- **Discovery**: Prompts can be searched and discovered across the organization
- **Version control**: Immutable versions with full history and rollback capability

## Related Concepts

- [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md) — The overall system for managing prompt templates
- [Unity Catalog](/concepts/unity-catalog.md) — The underlying governance and metadata platform
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and evaluations
- [Prompt Versioning](/concepts/prompt-versioning.md) — The Git-like version management for prompts
- [Prompt Templates](/concepts/prompt-templates-with-variables.md) — The template syntax and structure used in prompts

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
