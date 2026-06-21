---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ced2a730fe65fe84abc41eb1a03900f238e38ec9701397ed644fd68efab45d60
  pageDirectory: concepts
  sources:
    - upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-privileges-for-ml-workflows
    - UCPFMW
  citations:
    - file: upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Privileges for ML Workflows
description: Access control requirements including USE CATALOG, USE SCHEMA, CREATE MODEL, EXECUTE, and CREATE MODEL VERSION privileges needed for model operations in Unity Catalog
tags:
  - security
  - access-control
  - unity-catalog
  - machine-learning
timestamp: "2026-06-19T23:19:23.097Z"
---

# [Unity Catalog](/concepts/unity-catalog.md) Privileges for ML Workflows

**Unity Catalog Privileges for ML Workflows** are the set of access control permissions required to execute model training, deployment, and inference workflows that target models stored in [Unity Catalog](/concepts/unity-catalog.md) on Databricks. These privileges are enforced on the catalog, schema, and registered model objects, and must be granted to the principal (user or service principal) running the workflow.

## Required Privileges

To perform any ML workflow that produces or consumes [Unity Catalog](/concepts/unity-catalog.md) models, the principal must have the `USE CATALOG` and `USE SCHEMA` privileges on the [Catalog and Schema](/concepts/catalog-and-schema.md) that contain the model. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

Additional privileges are required for specific operations:

| Operation | Required Privilege |
|-----------|-------------------|
| Create a registered model | `CREATE MODEL` on the schema |
| Load or deploy a model | `EXECUTE` on the registered model |
| Create a new model version | Ownership of the registered model, or `CREATE MODEL VERSION` on the registered model |
| Set an alias on a registered model | Ownership of the registered model |

^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

> **Note:** The `CREATE MODEL VERSION` privilege is listed in the [Unity Catalog](/concepts/unity-catalog.md) privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference#create-model-version).

## Compute Requirements

In addition to privilege grants, the compute resource configured for the workflow must have access to [Unity Catalog](/concepts/unity-catalog.md). This is determined by the [access mode](https://docs.databricks.com/aws/en/compute/configure#access-mode) of the cluster or SQL warehouse used by the job. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The underlying governance layer for data and AI assets.
- [MLflow](/concepts/mlflow.md) – The model lifecycle management tool used to register and load models.
- [Model Serving](/concepts/model-serving.md) – Deployment path for serving endpoints, which uses the `EXECUTE` privilege.
- Aliases on Registered Models – Managed with ownership of the model.
- Upgrade ML Workflows to Target Models in Unity Catalog – The broader migration guide that discusses privilege requirements in context.

## Sources

- upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md](/references/upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws-c3150366.md)
