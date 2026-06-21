---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 668b726eed1e5b506212c8f9fd0f1a3b418facd05e19efc3a80f16353d311856
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-registry-permissions-and-access-control
    - Access Control and Model Registry Permissions
    - MRPAAC
  citations:
    - file: manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
title: Model Registry Permissions and Access Control
description: Role-based access control system for the Workspace Model Registry where users must have at least CAN MANAGE to configure permissions, and model versions inherit permissions from their parent model.
tags:
  - security
  - access-control
  - mlflow
  - databricks
timestamp: "2026-06-19T19:25:27.125Z"
---

# Model Registry Permissions and Access Control

**Model Registry Permissions and Access Control** governs who can view, manage, and transition versions of registered models in the Databricks Workspace Model Registry. Permission settings control access at the model level, and version-specific permissions are not supported — a model version inherits the permissions of its parent registered model. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Overview

Access control for the Workspace Model Registry uses a set of permission levels that determine what actions a user, group, or service principal can perform on a registered model. Only users with **CAN MANAGE** permission can configure permissions on a model. For details on the available permission levels, see the MLflow model ACLs documentation. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Setting Permissions

### Per‑Model Permissions

To set permissions on a specific registered model using the UI:

1. In the sidebar, click **Models**.
2. Select a model name.
3. Click **Permissions**. The Permission Settings dialog opens.
4. In the **Select User, Group or Service Principal…** drop-down, choose a principal.
5. Select a permission level from the permission drop-down.
6. Click **Add** and then **Save**.

The model version page does not have its own permission configuration; all versions of a model follow the parent model’s permissions. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

### Registry‑Wide Permissions

Workspace administrators and users who hold **CAN MANAGE** permission at the registry-wide level can set default permission levels on **all** models in the workspace. This is done by clicking **Permissions** on the **Models** page (the page that lists all registered models). ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Permission Inheritance

A model version always inherits the permissions of its parent registered model. It is not possible to set permissions on individual model versions. This means that any access control you configure for a model applies uniformly to all its versions. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Stage Transition Permissions

Transitioning a model version between stages (for example, from `Staging` to `Production`) requires the appropriate permission level for the model. If a user does not have permission to make a direct transition, they can **request** a stage transition. A user with sufficient permission can then approve, reject, or cancel the request. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Search and Visibility

When you search for models in the registry, only models for which you have at least **CAN READ** permission are returned. This ensures that users only see models they are authorized to access. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Related Concepts

- [Workspace Model Registry](/concepts/workspace-model-registry.md) – The legacy registry that uses these permission controls.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – The general MLflow concept underlying the Workspace Model Registry.
- [Model Stage Transitions](/concepts/model-versioning-and-stage-transitions.md) – Workflow that requires appropriate permissions.
- [Unity Catalog Model Permissions](/concepts/unity-catalog-permissions-model.md) – The newer permission model for models in Unity Catalog.
- MLflow model ACLs – Reference for the specific permission levels (CAN READ, CAN EDIT, CAN MANAGE, etc.).

## Sources

- manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md](/references/manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws-666e92b6.md)
