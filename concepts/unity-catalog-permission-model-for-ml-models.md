---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8aa0dfb12befd4463bbdb2ece567caf693a54f548aba5b3212d9da890b51a13
  pageDirectory: concepts
  sources:
    - migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-permission-model-for-ml-models
    - UCPMFMM
  citations:
    - file: migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
title: Unity Catalog permission model for ML models
description: Account-level Unity Catalog privileges replace workspace-level permissions for models, with a mapping from registry permissions (e.g., Can Read, Can Edit) to Unity Catalog privileges (e.g., EXECUTE, MANAGE), requiring USE CATALOG and USE SCHEMA for all actions.
tags:
  - access-control
  - unity-catalog
  - security
timestamp: "2026-06-19T19:36:03.916Z"
---

# Unity Catalog Permission Model for ML Models

The **Unity Catalog permission model for ML models** provides centralized, account-level access control for machine learning models registered in Unity Catalog. It replaces the workspace-level permissions of the legacy Workspace Model Registry with a unified privilege system that applies across all workspaces in a Databricks account. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Overview

Models in Unity Catalog inherit the same [Unity Catalog access control](/concepts/unity-catalog-access-control-models.md) framework used for tables, schemas, and other securable objects. This enables centralized management of permissions, auditing of model access, and easy sharing of models across workspaces and environments. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Relationship to Workspace Model Registry Permissions

When migrating models from the Workspace Model Registry to Unity Catalog, each workspace-level permission is mapped to a corresponding Unity Catalog privilege. The exact mapping is defined in the Unity Catalog [privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference). ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

In addition to the model-specific privileges, **all actions** on a model in Unity Catalog require the following foundational privileges:

- `USE CATALOG` on the parent catalog.
- `USE SCHEMA` on the parent schema.

^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Assigning Permissions

To assign permissions to a model in Unity Catalog, use Catalog Explorer, SQL `GRANT` statements, or the Databricks REST API. For detailed instructions, see the documentation on [controlling access to models](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#control-access-to-models). ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Key Benefits

- **Centralized governance**: Permissions are managed at the account level, not per workspace.
- **Auditing**: All model access is logged via Unity Catalog audit logs.
- **Cross-workspace sharing**: A model registered in one catalog can be accessed by users in any workspace that has access to that catalog.
- **Granular control**: Privileges can be granted at the model, model version, or alias level.

## Related Concepts

- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) – The full set of securable object privileges.
- [Unity Catalog Models](/concepts/unity-catalog-for-ml-models.md) – How models are registered and managed in Unity Catalog.
- Migrating Models to Unity Catalog – Steps for moving from Workspace Model Registry.
- [Model Aliases and Stages](/concepts/model-aliases.md) – How stages are replaced by aliases in Unity Catalog.
- Deployment Jobs – Automating model lifecycle with Unity Catalog.

## Sources

- migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md](/references/migrate-workflows-and-models-to-unity-catalog-databricks-on-aws-ef30b915.md)
