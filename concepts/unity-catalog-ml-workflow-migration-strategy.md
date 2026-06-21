---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15e4b0ebff6c43d28e098e7629b942c4822e5415f1c10253fc90cc85c3ce7acc
  pageDirectory: concepts
  sources:
    - upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-ml-workflow-migration-strategy
    - UCMWMS
  citations:
    - file: upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog ML Workflow Migration Strategy
description: Recommended approach for migrating existing Databricks ML workflows to Unity Catalog by creating parallel pipelines instead of cut-over
tags:
  - machine-learning
  - unity-catalog
  - migration
  - databricks
timestamp: "2026-06-19T23:19:16.115Z"
---

# [Unity Catalog](/concepts/unity-catalog.md) ML Workflow Migration Strategy

The **Unity Catalog ML Workflow Migration Strategy** is a recommended incremental approach for upgrading existing Databricks Workflows – including model training, deployment, and inference pipelines – to use models managed in [Unity Catalog](/concepts/unity-catalog.md). The strategy involves creating parallel pipelines that target [Unity Catalog](/concepts/unity-catalog.md) while the original workflows continue to run, then switching downstream consumers after validation. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Requirements

Before migrating, the principal executing the workflow must have the following [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md):

- `USE CATALOG` and `USE SCHEMA` on the [Catalog and Schema](/concepts/catalog-and-schema.md) that hold the model.
- `CREATE MODEL` to create a new registered model.
- `EXECUTE` on the registered model to load or deploy it.
- `CREATE MODEL VERSION` (or be the model owner) to create a new version.
- Owner of the registered model to set an alias.

Additionally, the compute resource allocated to the workflow must use an [Access Mode](/concepts/standard-access-mode.md) that is compatible with [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Recommended Migration Strategy

Databricks advises an **incremental parallel pipeline** approach. Rather than modifying existing production workflows directly, create a separate clone of each workflow that targets [Models in Unity Catalog](/concepts/models-in-unity-catalog.md). After validating the quality and performance of the Unity Catalog–based pipeline, downstream consumers can be switched over — for example, by reading the batch inference output from the new pipeline or by gradually increasing traffic to [Unity Catalog](/concepts/unity-catalog.md) models in a [Model Serving Endpoint](/concepts/model-serving-endpoint.md). ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

### Model Training Workflow

1. **[Clone](https://docs.databricks.com/aws/en/jobs/configure-job#aux-job) the training workflow**. Verify that the principal and compute meet the requirements described above.
2. **Modify the training code** in the cloned workflow (by editing the notebook or switching to a new git branch). Install the required [MLflow](/concepts/mlflow.md) version and configure the [MLflow](/concepts/mlflow.md) client to target [Unity Catalog](/concepts/unity-catalog.md). Update the training code to register models directly to [Unity Catalog](/concepts/unity-catalog.md).
3. Train and register models as described in the [Train and Register Unity Catalog–Compatible Models](/concepts/unity-catalog-for-ml-models.md) documentation. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

### Model Deployment Workflow

1. **Clone the deployment workflow**. Ensure the principal and compute meet the requirements.
2. **Update model validation logic** to load model versions from [Unity Catalog](/concepts/unity-catalog.md) (using `mlflow.pyfunc.load_model()` with a [Unity Catalog](/concepts/unity-catalog.md) model URI).
3. Use Unity Catalog Model Aliases (e.g., “Champion”) to manage production rollouts and stage transitions. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

### Model Inference Workflow

#### Batch Inference

1. **Clone the batch inference workflow** and confirm requirements.
2. Modify the code to load the model from [Unity Catalog](/concepts/unity-catalog.md) and produce batch predictions.

#### [Model Serving](/concepts/model-serving.md)

For real-time serving, there is no need to clone the existing endpoint. Instead, use the **traffic split** feature of [Model Serving](/concepts/model-serving.md) to route a small fraction of traffic to a Unity Catalog–registered model version. Gradually increase the traffic split as results are reviewed, until 100% of traffic is rerouted. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Promoting Models Across Environments

Model promotion across environments (e.g., staging to production) works differently with [Unity Catalog](/concepts/unity-catalog.md). Refer to the [Promote a Model Across Environments](/concepts/model-version-promotion-across-environments.md) guide for the recommended process. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Manual Approval with Job Webhooks

Although automated deployment with integrated checks and tests is preferred, manual approval steps can be introduced using Job Notifications. After a model training job completes successfully, a job webhook can call out to an external CI/CD system to request manual approval. Once approved, the CI/CD system can deploy the model version — for example, by setting the “Champion” alias on it to serve traffic. ^[upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md]

## Sources

- upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws.md](/references/upgrade-ml-workflows-to-target-models-in-unity-catalog-databricks-on-aws-c3150366.md)
