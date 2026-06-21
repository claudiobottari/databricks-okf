---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51502f47a6e97fbf622df5379238a764ef72c9275c97d35349098afba7f4b2e5
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-schema-for-prompts
    - UCSFP
    - Unity Catalog Schemas
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Unity Catalog Schema for Prompts
description: Prompts are stored in Unity Catalog schemas, requiring CREATE FUNCTION, EXECUTE, and MANAGE privileges for user access.
tags:
  - unity-catalog
  - permissions
  - schema
timestamp: "2026-06-18T11:17:02.485Z"
---

# Unity Catalog Schema for Prompts

**Unity Catalog Schema for Prompts** refers to the Unity Catalog schema that stores prompts in the [MLflow Prompt Registry](/concepts/prompt-registry.md). A Unity Catalog schema with appropriate permissions is required to create, view, and manage prompts using the MLflow Python SDK or the Databricks MLflow UI.^[create-and-edit-prompts-databricks-on-aws.md]

## Prerequisites

To use a Unity Catalog schema for prompts, you must have the following privileges on the schema: `CREATE FUNCTION`, `EXECUTE`, and `MANAGE`.^[create-and-edit-prompts-databricks-on-aws.md]

If you are using a Databricks trial account, you have the required permissions on the Unity Catalog schema `main.default`.^[create-and-edit-prompts-databricks-on-aws.md]

## Setting the Prompt Registry Location

To link an MLflow experiment to a default Prompt Registry location, set an experiment tag using `mlflow.set_experiment_tags()`. This allows SDKs and tools to infer your Unity Catalog prompt schema automatically.^[create-and-edit-prompts-databricks-on-aws.md]

Use the `mlflow.promptRegistryLocation` tag with the value `catalog.schema`:

```python
import mlflow

# Link the current MLflow experiment to a UC schema for prompts
mlflow.set_experiment_tags({
    "mlflow.promptRegistryLocation": "main.default"
})
```

^[create-and-edit-prompts-databricks-on-aws.md]

## Creating Prompts in a Schema

When creating a prompt in the Databricks MLflow UI, if you haven't yet selected a schema for the experiment, the **New Prompt** dialog includes a **Target schema** field. Click **Choose** to open the schema picker, select the schema, and click **Confirm**. You must have `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` permissions on the selected schema.^[create-and-edit-prompts-databricks-on-aws.md]

When creating prompts programmatically, specify the prompt name using the format `catalog.schema.prompt_name`:

```python
import mlflow

uc_schema = "main.default"
prompt_name = "summarization_prompt"

prompt = mlflow.genai.register_prompt(
    name=f"{uc_schema}.{prompt_name}",
    template="Summarize content you are provided with in {{num_sentences}} sentences.\nContent: {{content}}",
    commit_message="Initial version of summarization prompt",
)
```

^[create-and-edit-prompts-databricks-on-aws.md]

## Searching for Prompts

To find prompts in a Unity Catalog schema, use `mlflow.genai.search_prompts()` with a filter string specifying the [Catalog and Schema](/concepts/catalog-and-schema.md):

```python
# REQUIRED format for Unity Catalog - specify [[catalog-and-schema|Catalog and Schema]]
results = mlflow.genai.search_prompts("catalog = 'main' AND schema = 'default'")

# Using variables for your schema
catalog_name = uc_schema.split('.')[0]  # 'main'
schema_name = uc_schema.split('.')[1]   # 'default'
results = mlflow.genai.search_prompts(f"catalog = '{catalog_name}' AND schema = '{schema_name}'")

# Limit results
results = mlflow.genai.search_prompts(
    filter_string=f"catalog = '{catalog_name}' AND schema = '{schema_name}'",
    max_results=50
)
```

^[create-and-edit-prompts-databricks-on-aws.md]

## Loading Prompts from a Schema

Load prompts from the registry using the URI syntax `prompts:/catalog.schema.prompt_name/version` or by specifying the full name and version:

```python
# Load a specific version using URI syntax
prompt = mlflow.genai.load_prompt(name_or_uri=f"prompts:/{uc_schema}.{prompt_name}/1")

# Alternative syntax without URI
prompt = mlflow.genai.load_prompt(name_or_uri=f"{uc_schema}.{prompt_name}", version="1")
```

^[create-and-edit-prompts-databricks-on-aws.md]

## Version Management

Prompt versions are immutable after creation. To edit a prompt, you must create a new version by calling `mlflow.genai.register_prompt()` with an existing prompt name. This Git-like versioning maintains complete history and enables rollbacks.^[create-and-edit-prompts-databricks-on-aws.md]

## Related Concepts

- [MLflow Prompt Registry](/concepts/prompt-registry.md) — The centralized registry for managing prompt templates
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs
- [Prompt Versioning](/concepts/prompt-versioning.md) — Managing immutable versions of prompts
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that provides schema management
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The MLflow module for generative AI workflows

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
