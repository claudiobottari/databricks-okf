---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4fc14aa52e097039059ccb5fd2d3f063d075becfeb71f8bcfc52ce21ecd8bbc9
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-model-registry-quota-limits
    - WMRQL
  citations:
    - file: manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
title: Workspace Model Registry Quota Limits
description: Quota limits imposed on the total number of registered models and model versions per workspace in the Workspace Model Registry, effective May 2024, with recommendations for cleanup and retention strategies.
tags:
  - limits
  - quotas
  - governance
  - databricks
timestamp: "2026-06-19T19:25:36.709Z"
---

# Workspace Model Registry Quota Limits

The Workspace Model Registry imposes quota limits on the total number of registered models and model versions per workspace. These limits help manage resource usage and ensure system stability. If you exceed the registry quotas, Databricks recommends that you delete registered models and model versions that you no longer need, and adjust your model registration and retention strategy to stay under the limit. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Effective Date

These quota limits took effect starting **May 2024** for all Databricks workspaces. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Specific Limits

The specific numeric limits for registered models and model versions are documented in the Databricks Resource Limits page. The Workspace Model Registry quota section on that page details the per‑workspace maximums. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Checking Current Usage

Each workspace’s current usage can be inventoried using a Databricks notebook provided in the documentation. The notebook illustrates how to inventory and delete model registry entities. You can run this notebook to see how many registered models and versions you have and identify candidates for cleanup. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Staying Under the Limit

1. **Delete unused models and versions** – Remove models or versions that are no longer needed, especially those in the `None` or `Archived` stage.
2. **Archive instead of delete** – Consider transitioning model versions to the `Archived` stage rather than deleting them if you may need them later. However, archiving still counts toward the quota, so eventual deletion may be necessary.
3. **Adjust registration strategy** – Avoid registering every training run as a new model version. Use a consistent naming convention and versioning scheme to reduce clutter.
4. **Retain only production‑ready models** – Only register models that are ready for deployment or that need to be shared across workspaces.

## Requesting a Limit Increase

If you require an increase to your workspace limits, reach out to your Databricks account team. The account team can evaluate your request and adjust the quota as needed. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Related Concepts

- [Workspace Model Registry](/concepts/workspace-model-registry.md) – The legacy model registry for managing ML model lifecycles.
- Databricks Resource Limits – The page that lists the exact numeric quotas for the Workspace Model Registry.
- [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) – The recommended alternative for model management across workspaces.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – The underlying open‑source component used by the Workspace Model Registry.

## Sources

- manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md](/references/manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws-666e92b6.md)
