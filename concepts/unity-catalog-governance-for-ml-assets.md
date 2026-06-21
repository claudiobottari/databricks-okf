---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f144577cd6ad2fdd6b1f2d924bbfeffb9e32ef3217c2c7b61f9f6e2900d62b5
  pageDirectory: concepts
  sources:
    - open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-governance-for-ml-assets
    - UCGFMA
  citations:
    - file: open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md
title: Unity Catalog governance for ML assets
description: Centralized governance of ML models, feature tables, vector indexes, and tools through Unity Catalog, with fine-grained access control and authentication passthrough for agent, data, and tool access.
tags:
  - governance
  - unity-catalog
  - mlflow
timestamp: "2026-06-19T19:49:47.907Z"
---

# Unity Catalog Governance for ML Assets

**Unity Catalog governance for ML assets** refers to the centralized management, security, and auditing of machine learning artifacts — including models, feature tables, vector indexes, and tools — through [Unity Catalog](/concepts/unity-catalog.md) on the Databricks platform. This governance model is a key differentiator of managed MLflow on Databricks compared to open source MLflow. ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

## Key Capabilities

### Centralized governance

Unity Catalog provides a single, central location to govern all ML assets. Models, feature tables, vector indexes, tools, and other objects are governed under Unity Catalog, enabling consistent access control and lineage across the data and AI lifecycle. ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

### Access control

Access to ML assets follows the standard Databricks governance patterns. [Unity Catalog objects](/concepts/unity-catalog-securable-objects.md), such as registered models, are protected by Unity Catalog [privileges](/concepts/privileges-and-ownership.md), while workspace-level objects, such as MLflow experiments, continue to use [workspace permissions](/concepts/workspace-level-restrictions.md). This ensures that permissions are applied uniformly whether the resource lives in the catalog or the workspace. ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

### Authentication for agent interactions

When deploying agents, authentication for agent, data, and tool access can be precisely controlled using both authentication passthrough and on-behalf-of-user authentication. These mechanisms integrate with Unity Catalog to enforce fine-grained permissions at runtime. ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

### Auditing

Unity Catalog governance is complemented by [system tables](/concepts/mlflow-system-tables.md) that provide usage and audit logs for managed MLflow. This allows organizations to track who accessed which ML asset and when, supporting compliance and security requirements. ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Managed MLflow on Databricks](/concepts/managed-mlflow-on-databricks.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Feature Store](/concepts/feature-store.md)
- Vector Search
- [Model Serving](/concepts/model-serving.md)
- Databricks system tables
- Workspace permissions
- [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md)

## Sources

- open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md

# Citations

1. [open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md](/references/open-source-vs-managed-mlflow-on-databricks-databricks-on-aws-ce848b0f.md)
