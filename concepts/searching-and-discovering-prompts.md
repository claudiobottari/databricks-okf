---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 853183cefdc43d5d94a64643e652b83527dfcaaa9dd055d42ce81cd111daad36
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - searching-and-discovering-prompts
    - Discovering Prompts and Searching
    - SADP
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Searching and Discovering Prompts
description: Prompts can be discovered and filtered using mlflow.genai.search_prompts() with filter strings for catalog and schema, with optional max_results limiting.
tags:
  - search
  - discovery
  - mlflow-sdk
timestamp: "2026-06-19T09:32:34.200Z"
---

# Searching and Discovering Prompts

**Searching and Discovering Prompts** refers to the process of programmatically finding and listing prompts stored in the [MLflow Prompt Registry](/concepts/prompt-registry.md) within a Unity Catalog schema. This capability enables teams to explore available prompt templates, discover prompts created by other team members, and integrate prompt discovery into automated workflows.

## Overview

The MLflow Prompt Registry stores prompts as versioned objects in [Unity Catalog](/concepts/unity-catalog.md) schemas. The `mlflow.genai.search_prompts()` function provides a programmatic way to search for prompts based on [Catalog and Schema](/concepts/catalog-and-schema.md) filters. This is useful for discovering prompts across a team or organization, auditing prompt usage, and building tooling that works with registered prompts. ^[create-and-edit-prompts-databricks-on-aws.md]

## Searching for Prompts

### Required Format

When searching for prompts in Unity Catalog, you must specify the [Catalog and Schema](/concepts/catalog-and-schema.md) in the filter string. The search function requires this format to scope the results to the correct Unity Catalog location. ^[create-and-edit-prompts-databricks-on-aws.md]

The following example shows the required syntax for searching across a specific [Catalog and Schema](/concepts/catalog-and-schema.md):

```python
# REQUIRED format for Unity Catalog - specify [[catalog-and-schema|Catalog and Schema]]
results = mlflow.genai.search_prompts("catalog = 'main' AND schema = 'default'")
```

^[create-and-edit-prompts-databricks-on-aws.md]

### Using Variables

You can construct the filter string dynamically using variables, which is useful when your Unity Catalog schema path is stored in a configuration or derived from another source:

```python
# Using variables for your schema
catalog_name = uc_schema.split('.')[0]  # 'main'
schema_name = uc_schema.split('.')[1]   # 'default'

results = mlflow.genai.search_prompts(f"catalog = '{catalog_name}' AND schema = '{schema_name}'")
```

^[create-and-edit-prompts-databricks-on-aws.md]

### Limiting Results

To control the number of prompts returned, use the optional `max_results` parameter:

```python
# Limit results
results = mlflow.genai.search_prompts(
    filter_string=f"catalog = '{catalog_name}' AND schema = '{schema_name}'",
    max_results=50
)
```

^[create-and-edit-prompts-databricks-on-aws.md]

## Prerequisites

Before searching for prompts, ensure your environment meets the following requirements:

- [MLflow](/concepts/mlflow.md) must be installed with the Databricks integration (`mlflow[databricks]>=3.1.0`).
- You must have a Unity Catalog schema with the appropriate permissions (`CREATE FUNCTION`, `EXECUTE`, and `MANAGE`) to view prompts in that schema. ^[create-and-edit-prompts-databricks-on-aws.md]
- Your MLflow experiment should be linked to a Unity Catalog schema, typically by setting the `mlflow.promptRegistryLocation` experiment tag. ^[create-and-edit-prompts-databricks-on-aws.md]

## Related Concepts

- Create and Edit Prompts — The process of creating new prompts and managing their versions before searching for them.
- [Unity Catalog Schemas](/concepts/unity-catalog-schema-for-prompts.md) — The organizational structure where prompts are stored and searched.
- [Prompt Registry Versioning](/concepts/prompt-registry-version-control.md) — How prompts are versioned and tracked over time.
- Evaluate Prompt Versions — Comparing different prompt versions to identify the best performer, often after discovering them through search.
- [MLflow Prompt Registry](/concepts/prompt-registry.md) — The central registry for storing and managing prompt templates.
- [Track Prompts with App Versions](/concepts/prompt-versioning.md) — Linking prompt versions to application versions for end-to-end lineage.

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
