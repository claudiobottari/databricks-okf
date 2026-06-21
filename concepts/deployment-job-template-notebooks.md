---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 677ab2573e93ac388203e6d9f4fc8afb77c896cd63b766aa4eca9de3ee6d3d56
  pageDirectory: concepts
  sources:
    - mlflow-3-deployment-jobs-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deployment-job-template-notebooks
    - DJTN
  citations:
    - file: mlflow-3-deployment-jobs-databricks-on-aws.md
title: Deployment Job Template Notebooks
description: Reference notebooks for evaluation, approval, deployment, and job creation that serve as customizable templates for building deployment jobs on Databricks.
tags:
  - mlflow
  - notebooks
  - templates
timestamp: "2026-06-19T19:37:07.355Z"
---

# Deployment Job Template Notebooks

**Deployment Job Template Notebooks** are pre-built notebook templates provided by Databricks that define the individual tasks within an [MLflow Deployment Job](/concepts/mlflow-deployment-jobs.md) workflow. These templates serve as the building blocks for creating automated model deployment pipelines that handle evaluation, approval, and deployment of model versions in [Unity Catalog](/concepts/unity-catalog.md). ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Overview

Deployment job template notebooks are designed to be imported into a Databricks workspace and customized for specific use cases. Each notebook corresponds to a distinct stage in the deployment pipeline. The templates cover three core tasks: evaluation, approval, and deployment. A separate orchestration notebook creates and configures the Databricks Job that ties these tasks together into a deployment job. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Available Template Notebooks

### Evaluation Notebook for Classic ML

This notebook template evaluates a traditional machine learning model using `mlflow.evaluate()`. It is designed to work with models created from the [MLflow 3 traditional ML workflow](/concepts/mlflow-3-traditional-ml-workflow.md) example. Users must update the **REQUIRED** items in the notebook to configure it for their specific model and evaluation criteria. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Evaluation Notebook for GenAI

This notebook template evaluates a GenAI external model. Like the classic ML evaluation notebook, it uses `mlflow.evaluate()` and requires users to update the **REQUIRED** items to match their model and evaluation needs. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Approval Notebook

This notebook template implements the human-in-the-loop approval mechanism for deployment jobs. It checks for a Unity Catalog Tag on the model version to determine whether the approval task should pass or fail. The approval task is identified by a job task name that starts with "approval" (case-insensitive). When the tag value is set to `Approved`, the task passes; otherwise, it fails. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

The approval notebook can be customized to fit specific workflow requirements. Databricks recommends disabling retries on approval tasks since the task is expected to fail on the first run (before approval has been granted). ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Deployment Notebook

This notebook template handles the deployment of a model version to a [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoint. It is triggered after the approval task passes and deploys the approved model version to production. Users can customize this notebook to implement staged rollouts or other deployment strategies. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Create Deployment Job Notebook

This orchestration notebook programmatically creates the deployment job using the Databricks SDK. It defines the job structure, configures tasks, sets job parameters, and connects the job to a Unity Catalog model. Users must update the **REQUIRED** items to specify their Unity Catalog model and the appropriate task notebooks. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

Key configuration elements in this notebook include:
- Setting `model_name` and `model_version` as job-level parameters
- Setting the max concurrent run limit to 1 (default) to prevent deployment race conditions
- Configuring the **Run As** field to a service principal with minimal permissions
- Connecting the deployment job to the model using `client.update_registered_model()` or `client.create_registered_model()` ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Usage Workflow

The recommended workflow for using deployment job template notebooks is:

1. Create and register a Unity Catalog model (e.g., using the [MLflow 3 traditional ML workflow](/concepts/mlflow-3-traditional-ml-workflow.md) example)
2. Import the evaluation notebook template and customize it
3. Import the approval notebook template and customize it
4. Import the deployment notebook template and customize it
5. Import the create deployment job notebook, update the **REQUIRED** items, and run it to create the deployment job ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Customization

The template notebooks are designed to be starting points that can be customized for more complex deployment workflows. For example, a staged rollout might include additional tasks after the approval task to deploy to 1%, then 10%, collect metrics, decide whether to proceed or rollback, and finally deploy to 100% or rollback the model. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Related Concepts

- [MLflow Deployment Jobs](/concepts/mlflow-deployment-jobs.md) — The overall framework for automating model lifecycle management
- [Unity Catalog Models](/concepts/unity-catalog-for-ml-models.md) — The model registry where deployment jobs are connected
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — The job execution platform that runs deployment job tasks
- MLflow 3 Model Tracking — Recommended client for registering models and logging evaluation metrics
- Human-in-the-Loop Approvals — The approval mechanism for deployment jobs
- [Databricks Model Serving](/concepts/databricks-model-serving.md) — The deployment target for approved model versions

## Sources

- mlflow-3-deployment-jobs-databricks-on-aws.md

# Citations

1. [mlflow-3-deployment-jobs-databricks-on-aws.md](/references/mlflow-3-deployment-jobs-databricks-on-aws-732ab147.md)
