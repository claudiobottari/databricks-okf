---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c8b28ff87b25e3ddb6334442ac86b65ea570fdbcfe766bffcb30863c61e06fd
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-schema-permissions-for-prompts
    - UCSPFP
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Unity Catalog Schema Permissions for Prompts
description: Storing prompts requires a Unity Catalog schema with CREATE FUNCTION, EXECUTE, and MANAGE privileges, and the schema acts as the storage location for registered prompts.
tags:
  - unity-catalog
  - permissions
  - databricks
timestamp: "2026-06-19T09:31:37.753Z"
---

# Unity Catalog Schema Permissions for Prompts

**Unity Catalog Schema Permissions for Prompts** refers to the specific privileges required on a Unity Catalog schema to create, view, and manage prompts in the MLflow Prompt Registry. These permissions control which users and service principals can store and access prompt templates within a given schema.

## Required Permissions

To create or view prompts in a Unity Catalog schema, a user must have the following three privileges on that schema: ^[create-and-edit-prompts-databricks-on-aws.md]

- `CREATE FUNCTION`
- `EXECUTE`
- `MANAGE`

These permissions are required regardless of whether you use the Databricks MLflow UI or the MLflow Python SDK to interact with prompts. ^[create-and-edit-prompts-databricks-on-aws.md]

## Default Permissions in Trial Accounts

If you are using a Databricks trial account, you automatically have the required permissions on the Unity Catalog schema `main.default`. This allows you to begin working with prompts immediately without additional configuration. ^[create-and-edit-prompts-databricks-on-aws.md]

## Setting the Prompt Registry Location

When using the Python SDK, you must link your MLflow experiment to a Unity Catalog schema by setting the `mlflow.promptRegistryLocation` experiment tag. The tag value must be in the format `catalog.schema`. This tells the SDK and tools where to store and look up prompts. ^[create-and-edit-prompts-databricks-on-aws.md]

```python
import mlflow

mlflow.set_experiment_tags({
    "mlflow.promptRegistryLocation": "main.default"
})
```

## Selecting a Schema in the UI

When creating a prompt through the Databricks MLflow UI, if you have not yet selected a schema for the experiment, the **New Prompt** dialog includes a **Target schema** field. You must choose a schema where you have `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` permissions. ^[create-and-edit-prompts-databricks-on-aws.md]

## Searching for Prompts

To search for prompts within a specific schema using the Python SDK, you must specify both the [Catalog and Schema](/concepts/catalog-and-schema.md) in the filter string: ^[create-and-edit-prompts-databricks-on-aws.md]

```python
results = mlflow.genai.search_prompts(
    "catalog = 'main' AND schema = 'default'"
)
```

## Related Concepts

- [MLflow Prompt Registry](/concepts/prompt-registry.md) — The system for storing and versioning prompts
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages schema permissions
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit linked to prompt registry locations
- Create and Edit Prompts — The workflow for managing prompt versions

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
