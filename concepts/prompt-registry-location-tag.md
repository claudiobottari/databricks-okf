---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 02e0a399276e137610c50fcca8882a680e38503f5c0d200e8923f40cc862989f
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-registry-location-tag
    - PRLT
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Prompt Registry Location Tag
description: An MLflow experiment tag 'mlflow.promptRegistryLocation' that links an experiment to a Unity Catalog schema, allowing SDKs and tools to infer the prompt storage location automatically.
tags:
  - mlflow
  - configuration
  - experiment-tags
timestamp: "2026-06-18T14:50:43.706Z"
---

```
---
title: Prompt Registry Location Tag
summary: An MLflow experiment tag (mlflow.promptRegistryLocation) that links an experiment to a Unity Catalog schema for automatic prompt inference.
sources:
  - create-and-edit-prompts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - mlflow
  - configuration
  - unity-catalog
aliases:
  - prompt-registry-location-tag
  - mlflow.promptRegistryLocation
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Prompt Registry Location Tag

The **Prompt Registry Location Tag** is an [[MLflow]] experiment tag that links an experiment to a specific [[Unity Catalog]] schema for storing prompts. By setting the tag `mlflow.promptRegistryLocation` on an MLflow experiment, SDKs and tools can automatically infer the Unity Catalog prompt schema without requiring explicit schema specification in every prompt operation.^[create-and-edit-prompts-databricks-on-aws.md]

## Purpose

When working with the [[MLflow Prompt Registry]], prompts are stored in Unity Catalog schemas. The Prompt Registry Location Tag eliminates the need to repeatedly specify the target schema when creating, loading, or searching for prompts. Once the tag is set on an experiment, all subsequent prompt registry operations within that experiment context automatically use the specified Unity Catalog schema.^[create-and-edit-prompts-databricks-on-aws.md]

## Setting the Tag

Set the `mlflow.promptRegistryLocation` tag on an MLflow experiment using `mlflow.set_experiment_tags()`. The value must be a Unity Catalog schema in the format `catalog.schema`:^[create-and-edit-prompts-databricks-on-aws.md]

```python
import mlflow

mlflow.set_experiment_tags({
    "mlflow.promptRegistryLocation": "main.default"
})
```

After setting this tag, functions such as `mlflow.genai.register_prompt()` and `mlflow.genai.search_prompts()` will use the specified Unity Catalog schema as the default location for prompt operations.^[create-and-edit-prompts-databricks-on-aws.md]

## Prerequisites

For the tag to function correctly, the Unity Catalog schema specified in the tag value must exist, and the user must have the following privileges on that schema:^[create-and-edit-prompts-databricks-on-aws.md]

- `CREATE FUNCTION`
- `EXECUTE`
- `MANAGE`

If you are using a Databricks trial account, you have the required permissions on the Unity Catalog schema `main.default`.^[create-and-edit-prompts-databricks-on-aws.md]

## Behavior

Once the Prompt Registry Location Tag is set, all operations that require a prompt registry location will default to the specified schema. This includes:

- Creating new prompts with `mlflow.genai.register_prompt()` — the schema component of the prompt name is inferred from the tag.^[create-and-edit-prompts-databricks-on-aws.md]
- Searching for prompts with `mlflow.genai.search_prompts()` — the [[catalog-and-schema|Catalog and Schema]] filter is inferred.^[create-and-edit-prompts-databricks-on-aws.md]
- Loading prompts — the schema is inferred when using prompt URIs.^[create-and-edit-prompts-databricks-on-aws.md]

The tag does not prevent explicit schema specification; it only provides a default. Operations that explicitly specify a Unity Catalog schema override the tag value.^[create-and-edit-prompts-databricks-on-aws.md]

## UI Interaction

When creating a prompt through the Databricks MLflow UI, if no Prompt Registry Location Tag has been set on the experiment, the UI displays a **Target schema** field that prompts the user to choose a schema. Once the tag is set, this field may be pre-populated or omitted in subsequent operations.^[create-and-edit-prompts-databricks-on-aws.md]

## Related Concepts

- [[MLflow Prompt Registry]] — The system for versioning and managing prompts
- [[Unity Catalog]] — The governance layer where prompts are stored
- [[MLflow Experiment|MLflow Experiments]] — The organizational unit for MLflow runs
- Create and Edit Prompts — Guide for working with prompts in the registry
- [[Prompt Discovery and Search|Search Prompts]] — Finding prompts in Unity Catalog schemas

## Sources

- create-and-edit-prompts-databricks-on-aws.md
```

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
