---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e7add21aa5b4e4201cb68ae768c049020b721acce202cc6c36f63e842a517568
  pageDirectory: concepts
  sources:
    - create-and-edit-prompts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-permissions-for-prompts
    - UCPFP
  citations:
    - file: create-and-edit-prompts-databricks-on-aws.md
title: Unity Catalog Permissions for Prompts
description: "Storing and managing prompts in the MLflow Prompt Registry requires specific Unity Catalog schema privileges: CREATE FUNCTION, EXECUTE, and MANAGE."
tags:
  - unity-catalog
  - permissions
  - access-control
timestamp: "2026-06-18T14:50:26.190Z"
---

# Unity Catalog Permissions for Prompts

**Unity Catalog Permissions for Prompts** define the minimum privileges a user or service principal must have on a Unity Catalog schema to create, view, and manage prompts in the MLflow Prompt Registry. These permissions are enforced when using either the Databricks MLflow UI or the MLflow Python SDK.

## Overview

Prompts are stored as functions (or function-like objects) within a Unity Catalog schema. To interact with prompts—whether creating, reading, or updating them—a user needs specific permissions on that schema. The required permissions are **`CREATE FUNCTION`**, **`EXECUTE`**, and **`MANAGE`**. ^[create-and-edit-prompts-databricks-on-aws.md]

## Required Permissions

| Permission | Purpose |
|-----------|---------|
| `CREATE FUNCTION` | Allows the user to register new prompts (versions) in the schema. Each prompt version is stored as a function. |
| `EXECUTE` | Allows the user to read and use prompts, for example by calling `mlflow.genai.load_prompt()`. |
| `MANAGE` | Allows the user to manage prompt metadata, tags, and versions, and to create or edit prompts in the UI. |

All three permissions must be granted on the schema that will store the prompts. Without them, users cannot view prompts or create new versions. ^[create-and-edit-prompts-databricks-on-aws.md]

## Granting Permissions

While the source material does not provide specific SQL syntax for granting these permissions, the typical Unity Catalog approach would involve granting the privileges to a user or group on the target schema. Work with your Unity Catalog administrator to ensure the required permissions are in place.

## Using with Databricks Trial Accounts

If you are using a [Databricks trial account](https://docs.databricks.com/aws/en/getting-started/express-setup), the permissions are pre-configured on the `main.default` schema. You can immediately create and manage prompts in that schema without additional setup. ^[create-and-edit-prompts-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The central governance layer for data and AI assets.
- [MLflow Prompt Registry](/concepts/mlflow-prompt-registry.md) – The system for versioning and managing prompts.
- Unity Catalog Schema – The organizational unit within a catalog that holds objects like prompts.
- [MLflow](/concepts/mlflow.md) – The open-source platform for managing machine learning workflows.
- [Permissions in Unity Catalog](/concepts/manage-permission-in-unity-catalog.md) – How to grant and revoke privileges on catalogs, schemas, and objects.

## Sources

- create-and-edit-prompts-databricks-on-aws.md

# Citations

1. [create-and-edit-prompts-databricks-on-aws.md](/references/create-and-edit-prompts-databricks-on-aws-9f1640e3.md)
