---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 998d3a0866c08d278ba43cc032c475a1421bbf3f61266ba0c7285f742870d18f
  pageDirectory: concepts
  sources:
    - mlflow-3-deployment-jobs-databricks-on-aws.md
    - mlflow-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-deployment-jobs
    - MDJ
    - MLflow Deployment Job
    - Approval mechanism for deployment jobs
    - Deployment Job
    - Deployment job
    - Deployment jobs
    - deployment jobs
    - deployment job|deployment jobs
  citations:
    - file: mlflow-3-deployment-jobs-databricks-on-aws.md
title: MLflow Deployment Jobs
description: Automated jobs that manage the full lifecycle of ML models on Databricks by automating evaluation, approval, and deployment tasks when new model versions are created.
tags:
  - mlflow
  - deployment
  - mlops
timestamp: "2026-06-19T19:38:07.402Z"
---

# MLflow Deployment Jobs

**MLflow Deployment Jobs** are automated workflows used to manage the full lifecycle of machine learning models on Databricks. They orchestrate tasks such as evaluation, approval, and deployment whenever a new model version is created, integrating with [Unity Catalog](/concepts/unity-catalog.md) models and [Lakeflow Jobs](/concepts/lakeflow-jobs.md). Deployment jobs simplify the setup of model deployment pipelines, incorporate human-in-the-loop approvals, and provide governed workflows with clear visibility into progress and historical context for each model version. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Overview

Deployment jobs are a core feature of [MLflow](/concepts/mlflow.md) 3 on Databricks. They are designed to streamline MLOps by fully automating the model deployment process. When a new model version is created, the deployment job triggers automatically, displaying its run status directly on the model and model version pages. Historical information about each deployment job run is tracked in an activity log, ensuring transparency and ease of management. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

While deployment jobs do not need to be used with MLflow 3 clients or model tracking, and can be enabled on older existing models in Unity Catalog, Databricks recommends using MLflow 3 for the best experience. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Integration with MLflow 3 Model Tracking

Databricks recommends using MLflow 3 Tracking to register models and perform evaluation in the deployment job. The new client automatically logs metrics from the evaluation portion of the deployment job, which are visible in the Unity Catalog model version UI. This allows users to use centralized metrics, parameters, and traces on the model version page to make informed decisions about progressing the model further in the deployment job lifecycle. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Integration with Unity Catalog CREATE MODEL VERSION ACL

Deployment jobs integrate with the Unity Catalog Create Model Version ACL. A user granted the `CREATE MODEL VERSION` ACL can register new model versions to the model. When the user registers a version, the deployment job automatically triggers to evaluate the model, and an approver can then manually approve or reject the version for deployment. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

**Important**: The deployment job auto-triggers using the model owner's credentials, meaning a user with `CREATE MODEL VERSION` permission on the Unity Catalog model can execute arbitrary code as part of the job. Databricks recommends setting up the deployment job using a service principal with minimal permissions to prevent privilege escalation. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Example Workflows

A simple example deployment job consists of three steps: evaluation, approval, and deployment. The evaluation step calls `mlflow.evaluate` to produce validation metrics on the inputted model version. The approval step allows a privileged user to determine if these metrics are satisfactory. Finally, the deployment step deploys the model version to a Databricks Model Serving endpoint. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

More complex deployment jobs can include staged rollouts with metrics collection. For example, additional tasks after approval might deploy the model to 1%, then 10%, collect and check metrics, decide whether to proceed or rollback, and finally deploy to 100% or roll back the model. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Creating a Deployment Job

To create a deployment job, you first need model versions created in a registered model. A deployment job must have two job parameters: `model_name` and `model_version`. Databricks recommends setting the max concurrent run limit to 1 (the default) to prevent deployment race conditions. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

There are two ways to create a deployment job: programmatically using a deployment notebook (recommended), or using the Jobs UI. In both cases, you provide each job task as a notebook, with evaluation, approval, and deployment tasks as templates. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

Databricks recommends setting the **Run As** field to a service principal with minimal permissions. For the approval task, Databricks recommends disabling retries, as the task is expected to fail initially. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Connecting the Deployment Job to a Model

After creating the Unity Catalog model and deployment job, you connect the job to the model as a deployment job using the UI or programmatically via the MLflow Client. After a deployment job is connected, it is linked on the model page. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

To connect programmatically, use `client.create_registered_model(model_name, deployment_job_id=<job-id>)` when creating a registered model, or `client.update_registered_model(model_name, deployment_job_id=<job-id>)` to update an existing one. To disconnect, specify an empty string for the deployment job ID. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Required Permissions

- The user needs **MANAGE or OWNER** on the model to connect the deployment job.
- The model owner needs **CAN MANAGE RUN or higher** permissions on the deployment job.
- When someone with **MANAGE or higher** updates the deployment job field on the model, both the updater **and** the model owner need **CAN MANAGE RUN or higher** on the deployment job. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Triggering the Deployment Job

The deployment job triggers automatically on any newly created model versions. It can also be manually triggered on existing and previously deployed versions from the model version page by clicking **Start deployment job**. The job can also be triggered directly from the Jobs UI or API by specifying the model name and version in the job parameters. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Required Permissions

- To manually trigger or repair the deployment job using the model version UI, the user must have **CAN MANAGE RUN or higher** ACLs on the deployment job.
- Because the job auto-triggers using the model owner's credentials when a new version is created, the model owner needs **CAN MANAGE RUN or higher** ACLs on the deployment job. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Approval Process (Experimental)

Databricks provides an experimental approval mechanism for deployment jobs, enabling a human-in-the-loop process. This feature uses Unity Catalog tags to determine whether the approval task should pass or fail. Approval tasks are identified by job task names starting with "approval" (case-insensitive). ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### How Approval Works

1. **Initial run**: The first run of the deployment job always fails on an approval task because the model version has not been approved yet and lacks the required Unity Catalog tag. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]
2. **Approval evaluation**: The approver reviews the model version and its evaluation metrics displayed on the model version page. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]
3. **Approval action**: If satisfactory, the approver clicks the **Approve** button. This action automatically repairs the job run and adds a Unity Catalog tag to the model version, where the tag key matches the approval task name and the tag value is set to `Approved`. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]
4. **Job continuation**: The repaired deployment job run resumes from the approval task, passing because the tag is now present, and proceeds to subsequent tasks such as deployment. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Required Permissions for Approvals

- **APPLY TAG** on the Unity Catalog model.
- **CAN MANAGE RUN** on the deployment job. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Governed Tags for Advanced Approvals

Using [Governed Tag Policy](/concepts/governed-tags-for-abac-policies.md), you can specify who has permission to approve and apply tags. This enables:
- Multiple independent approval groups in a deployment job (e.g., `Approval_Legal` and `Approval_Security`).
- Preventing the model owner from approving the job to ensure second-person approval.
- Standardizing approval checks across the [Metastore](/concepts/metastore.md), catalog, and schema. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Viewing Status and Activity Log

Once deployment jobs have been triggered on model versions, the current status is visible on the model page's **Overview** tab. Below the status, you can see historical activity in the Activity log, which is also shown on the model version page. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Required Permissions

- **EXECUTE** on the Unity Catalog model. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Template Notebooks

Databricks provides example template notebooks for creating simple deployment jobs consisting of evaluation, approval, and deployment tasks. These include evaluation notebooks for both GenAI and classic ML models, an approval notebook, a deployment notebook, and a notebook to create the deployment job programmatically. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) — The open source AI engineering platform underlying deployment jobs.
- [Unity Catalog](/concepts/unity-catalog.md) — Centralized governance for models, integrated with deployment jobs.
- [Model Serving](/concepts/model-serving.md) — Deploys models to REST API endpoints, used in the deployment step.
- [MLflow 3](/concepts/mlflow-3.md) — The latest version of MLflow on Databricks with enhanced features.
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — The job orchestration framework deployment jobs run on.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Centralized repository for managing model versions.
- Human-in-the-loop — Approval mechanism for machine learning pipelines.

## Sources

- mlflow-3-deployment-jobs-databricks-on-aws.md
- mlflow-on-databricks-databricks-on-aws.md

# Citations

1. [mlflow-3-deployment-jobs-databricks-on-aws.md](/references/mlflow-3-deployment-jobs-databricks-on-aws-732ab147.md)
