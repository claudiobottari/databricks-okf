---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a6cd5734d9e1eabe589eb79e49a731ee306a2811c3c3a982cb589f5686a14ac9
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - privileges-for-prompt-management
    - PFPM
    - Prompt management
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Privileges for Prompt Management
description: Required Unity Catalog permissions (CREATE FUNCTION, EXECUTE, MANAGE) for creating prompts and evaluation datasets, ensuring proper access control.
tags:
  - security
  - unity-catalog
  - permissions
timestamp: "2026-06-19T18:41:20.187Z"
---

# Privileges for Prompt Management

**Privileges for Prompt Management** refers to the Unity Catalog permissions required to create, manage, and evaluate prompts and evaluation datasets in MLflow on Databricks. These privileges control which users and service principals can register prompt versions, build evaluation datasets, and run comparative evaluations using [MLflow](/concepts/mlflow.md).

## Overview

Managing prompts in the MLflow Prompt Registry involves two main resources: prompt objects (stored as Unity Catalog functions) and evaluation datasets (stored as Unity Catalog tables). Both resources require specific [Unity Catalog](/concepts/unity-catalog.md) privileges on the containing [Catalog and Schema](/concepts/catalog-and-schema.md). Without these privileges, operations such as `mlflow.genai.register_prompt` or `mlflow.genai.datasets.create_dataset` will fail. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Required Privileges

To create prompts and evaluation datasets, a user or service principal must have the following privileges at the **catalog** and **schema** level: ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

- **`CREATE FUNCTION`** – Allows creation of prompt versions, because prompts are stored as Unity Catalog functions.
- **`EXECUTE`** – Allows invocation of prompts and evaluation functions.
- **`MANAGE`** – Allows management operations such as updating prompt metadata, changing aliases, and deleting prompts or datasets.

The same set of privileges is required for both the catalog and the schema where the prompts and evaluation datasets reside. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Granting Privileges

These privileges can be granted by a Unity Catalog [Metastore](/concepts/metastore.md) admin or a user with the `MANAGE` privilege on the target [Catalog and Schema](/concepts/catalog-and-schema.md). Use the SQL command pattern:

```sql
GRANT CREATE FUNCTION, EXECUTE, MANAGE ON CATALOG <catalog_name> TO <principal>;
GRANT CREATE FUNCTION, EXECUTE, MANAGE ON SCHEMA <schema_name> TO <principal>;
```

Replace `<catalog_name>` and `<schema_name>` with the appropriate names, and `<principal>` with the user or group name.

## Trial Account Note

If you are using a [Databricks trial account](https://docs.databricks.com/aws/en/getting-started/express-setup), you have the required permissions on the Unity Catalog schema `workspace.default`. No additional privilege grants are needed for prompt management in that schema. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) – Overview of the Unity Catalog privilege model.
- [Prompt Registry](/concepts/prompt-registry.md) – The service for versioning and managing prompts.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – A Unity Catalog table containing input-output examples for prompt evaluation.
- MLflow Prompt Management – End-to-end workflow for creating, evaluating, and deploying prompts.

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
