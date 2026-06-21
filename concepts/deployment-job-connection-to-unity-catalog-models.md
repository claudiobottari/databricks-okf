---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 167514543c21f1e7aa21b7dd03696422541aa2b8b93a050c5e0626e908ee9ea4
  pageDirectory: concepts
  sources:
    - mlflow-3-deployment-jobs-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deployment-job-connection-to-unity-catalog-models
    - DJCTUCM
  citations:
    - file: mlflow-3-deployment-jobs-databricks-on-aws.md
title: Deployment Job Connection to Unity Catalog Models
description: The process of linking a deployment job to a Unity Catalog registered model via the MLflow client or UI, enabling automatic triggering when new model versions are created.
tags:
  - mlflow
  - unity-catalog
  - mlops
timestamp: "2026-06-19T19:36:54.354Z"
---

# Deployment Job Connection to Unity Catalog Models

**Deployment Job Connection to Unity Catalog Models** refers to the process of linking a [Deployment Job](/concepts/mlflow-deployment-jobs.md) to a [Unity Catalog](/concepts/unity-catalog.md) registered model so that the job automatically triggers on new model versions and manages the model's lifecycle — including evaluation, approval, and deployment. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Overview

After creating a Unity Catalog model and a deployment job, you must connect the job to the model. Once connected, the deployment job is linked on the model page and automatically triggers whenever a new model version is created. The job can also be manually triggered on existing or previously deployed versions. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Connection Methods

### Using the UI

On the model's **Overview** tab, click **Connect deployment job** in the **Deployment job** section. Select the deployment job from the dropdown list (which supports search by job name or ID) and click **Save changes**. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Using the MLflow Client (Programmatic)

The recommended approach for programmatic connection uses the MLflow Tracking Client. You can connect a deployment job when creating a new registered model, or by updating an existing one: ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

```python
import mlflow
from mlflow.tracking.client import MlflowClient

client = MlflowClient(registry_uri="databricks-uc")
# model_name should be in the format <catalog>.<schema>.<model>

try:
  if client.get_registered_model(model_name):
    client.update_registered_model(model_name, deployment_job_id=created_job.job_id)
except mlflow.exceptions.RestException:
  client.create_registered_model(model_name, deployment_job_id=created_job.job_id)
```

To disconnect a deployment job, call `client.update_registered_model(model_name, deployment_job_id="")`. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Required Permissions

The following permissions are necessary to connect and trigger deployment jobs: ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

- To connect a deployment job: **MANAGE** or **OWNER** on the model.
- The model owner must have **CAN MANAGE RUN** or higher permissions on the deployment job.
- If a user other than the model owner updates the deployment job field, both the updater **and** the model owner must have **CAN MANAGE RUN** or higher permissions on the deployment job.

## Auto-trigger Behavior

When a new model version is created, the deployment job automatically triggers using the model owner's credentials. This means that granting a user [Unity Catalog Privileges#CREATE MODEL VERSION|CREATE MODEL VERSION](/concepts/unity-catalog-privileges-and-ownership-model.md) permission on a Unity Catalog model allows that user to execute arbitrary code as part of the job. Databricks recommends setting up the deployment job using a Service Principal with minimal permissions to prevent privilege escalation. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Related Concepts

- [Deployment Job](/concepts/mlflow-deployment-jobs.md) — The automated job that manages model evaluation, approval, and deployment.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where models are registered and managed.
- MLflow 3 Model Tracking — Recommended for registering models and performing evaluation.
- Model Version Lifecycle — The stages a model version passes through during deployment.
- Service Principal — Recommended identity for running deployment jobs securely.

## Sources

- mlflow-3-deployment-jobs-databricks-on-aws.md

# Citations

1. [mlflow-3-deployment-jobs-databricks-on-aws.md](/references/mlflow-3-deployment-jobs-databricks-on-aws-732ab147.md)
