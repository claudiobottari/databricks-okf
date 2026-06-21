---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 49e833ac9f99be864f070c6f6298f55f6dc060fb2629c894dda00e57c4bb6569
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-schema-requirements-for-prompts
    - UCSRFP
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Unity Catalog Schema Requirements for Prompts
description: Prompts are stored in Unity Catalog schemas requiring specific permissions (CREATE FUNCTION, EXECUTE, MANAGE) and are linked to MLflow experiments via the mlflow.promptRegistryLocation tag.
tags:
  - unity-catalog
  - permissions
  - databricks
  - mlflow
timestamp: "2026-06-19T14:32:41.666Z"
---

# Unity Catalog Schema Requirements for Prompts

**Unity Catalog Schema Requirements for Prompts** defines the necessary permissions and schema configuration needed to store, view, and manage prompts in the [MLflow Prompt Registry](/concepts/prompt-registry.md) using [Unity Catalog](/concepts/unity-catalog.md).

## Overview

To use the MLflow Prompt Registry, you must have a Unity Catalog schema configured with specific permissions. The schema serves as the storage location for prompt definitions and their version history. Without the correct schema setup, you cannot create, view, or manage prompts.^[create-and-edit-prompts-databricks-on-aws.md]

## Required Permissions

To create or view prompts in a Unity Catalog schema, you must have the following privileges on that schema:^[create-and-edit-prompts-databricks-on-aws.md]

- `CREATE FUNCTION`
- `EXECUTE`
- `MANAGE`

These permissions are required for both programmatic access via the MLflow Python SDK and for using the Databricks MLflow UI.^[create-and-edit-prompts-databricks-on-aws.md]

## Default Schema for Trial Accounts

If you are using a Databricks trial account, you automatically have the required permissions on the Unity Catalog schema `main.default`. This allows you to begin working with prompts immediately without additional configuration.^[create-and-edit-prompts-databricks-on-aws.md]

## Configuring the Schema

### Setting the Default Schema for an Experiment

You can link an MLflow experiment to a default Prompt Registry location by setting an experiment tag. This allows SDKs and tools to automatically infer your Unity Catalog prompt schema.^[create-and-edit-prompts-databricks-on-aws.md]

Use the `mlflow.promptRegistryLocation` tag with the value `catalog.schema`:

```python
import mlflow

# Link the current MLflow experiment to a UC schema for prompts
mlflow.set_experiment_tags({
    "mlflow.promptRegistryLocation": "main.default"
})
```

### Selecting a Schema in the UI

When creating a new prompt in the Databricks MLflow UI, if you haven't yet selected a schema for the experiment, the **New Prompt** dialog includes a **Target schema** field. To choose a schema:^[create-and-edit-prompts-databricks-on-aws.md]

1. Next to the **Target schema** field, click **Choose** to open the schema picker.
2. In the picker, select the schema you want and click **Confirm**.

You must have the `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` permissions on the selected schema.^[create-and-edit-prompts-databricks-on-aws.md]

## Searching for Prompts

When searching for prompts using `mlflow.genai.search_prompts()`, you must specify the [Catalog and Schema](/concepts/catalog-and-schema.md) in the filter string:^[create-and-edit-prompts-databricks-on-aws.md]

```python
# REQUIRED format for Unity Catalog - specify [[catalog-and-schema|Catalog and Schema]]
results = mlflow.genai.search_prompts("catalog = 'main' AND schema = 'default'")
```

## Related Concepts

- [MLflow Prompt Registry](/concepts/prompt-registry.md) — The system for storing and versioning prompts
- Create and Edit Prompts — How to create and manage prompt versions
- [Unity Catalog](/concepts/unity-catalog.md) — The underlying catalog system for data and AI assets
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs
- [Prompt Version Management](/concepts/prompt-version-management.md) — Managing prompt versions with Git-like semantics

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
