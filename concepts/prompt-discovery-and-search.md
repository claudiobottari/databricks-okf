---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8696568f54cb1fcb0e328c851ca56e640bf2446958f6eae9a5addc40a5113cb5
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-discovery-and-search
    - Search and Prompt Discovery
    - PDAS
    - Search Prompts
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Prompt Discovery and Search
description: Searching prompts using filter strings on catalog and schema with the mlflow.genai.search_prompts() function.
tags:
  - mlflow
  - search
  - discovery
timestamp: "2026-06-19T17:58:26.376Z"
---

# Prompt Discovery and Search

**Prompt Discovery and Search** refers to the process of finding and retrieving prompts stored in the [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md) using programmatic search capabilities. The MLflow Python SDK provides a `search_prompts` function that enables users to discover prompts across [Unity Catalog](/concepts/unity-catalog.md) schemas.

## Overview

The MLflow Prompt Registry stores prompts as versioned entities within Unity Catalog schemas. To discover and retrieve prompts programmatically, users can call `mlflow.genai.search_prompts()` with a filter string that specifies the [Catalog and Schema](/concepts/catalog-and-schema.md) location. ^[create-and-edit-prompts-databricks-on-aws.md]

## Search Syntax

The `search_prompts` function requires a filter string in a specific format for Unity Catalog. The filter must specify both the `catalog` and `schema` parameters: ^[create-and-edit-prompts-databricks-on-aws.md]

```python
results = mlflow.genai.search_prompts("catalog = 'main' AND schema = 'default'")
```

This syntax is required — the function will not work without explicitly naming both the [Catalog and Schema](/concepts/catalog-and-schema.md). ^[create-and-edit-prompts-databricks-on-aws.md]

## Usage Examples

### Basic Search

To search for all prompts within a specific Unity Catalog schema: ^[create-and-edit-prompts-databricks-on-aws.md]

```python
import mlflow

# REQUIRED format for Unity Catalog - specify [[catalog-and-schema|Catalog and Schema]]
results = mlflow.genai.search_prompts("catalog = 'main' AND schema = 'default'")
```

### Using Variables

When working with dynamic schema names, construct the filter string using variables: ^[create-and-edit-prompts-databricks-on-aws.md]

```python
catalog_name = uc_schema.split('.')[0]  # 'main'
schema_name = uc_schema.split('.')[1]   # 'default'

results = mlflow.genai.search_prompts(
    f"catalog = '{catalog_name}' AND schema = '{schema_name}'"
)
```

### Limiting Results

To control the number of returned prompts, use the `max_results` parameter: ^[create-and-edit-prompts-databricks-on-aws.md]

```python
results = mlflow.genai.search_prompts(
    filter_string=f"catalog = '{catalog_name}' AND schema = '{schema_name}'",
    max_results=50
)
```

## Prerequisites

To search for prompts, users must have the following permissions on the Unity Catalog schema: `CREATE FUNCTION`, `EXECUTE`, and `MANAGE`. These permissions are required for any interaction with prompts in the registry, including discovery and search. ^[create-and-edit-prompts-databricks-on-aws.md]

## Related Concepts

- [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md) — The central repository for storing and managing prompt versions.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that organizes prompts within catalogs and schemas.
- [Prompt Versioning](/concepts/prompt-versioning.md) — The Git-like versioning system that maintains prompt history.
- Prompt Loading — The process of retrieving a specific prompt version for use in applications.
- [Prompt Evaluation](/concepts/prompt-version-evaluation.md) — Comparing different prompt versions to identify the best performer.

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
