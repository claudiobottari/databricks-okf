---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 020ba06651671e80035d4dc724e8ac62173376bd6d78115a65b45b7d91e79ee8
  pageDirectory: concepts
  sources:
    - migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deployment-jobs-for-model-lifecycle
    - DJFML
  citations:
    - file: migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
title: Deployment Jobs for model lifecycle
description: Automated jobs that trigger on new model versions to manage evaluation, approval, and deployment workflows in Unity Catalog, replacing stage transitions from the Workspace Model Registry.
tags:
  - mlops
  - automation
  - deployment
timestamp: "2026-06-19T19:35:55.099Z"
---

# Deployment Jobs for model lifecycle

**Deployment Jobs** are a mechanism in [Unity Catalog](/concepts/unity-catalog.md) for managing the lifecycle of a model version. Unlike the fixed stages used in the [Workspace Model Registry](/concepts/workspace-model-registry.md) (e.g., `Staging`, `Production`), deployment jobs provide a flexible, task-based workflow that automates the evaluation, approval, and deployment of model versions. They replace the stage-based lifecycle model with a customizable pipeline that can accommodate complex MLOps workflows. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Overview

In the Workspace Model Registry, the lifecycle of a model version was tracked by a fixed set of stages, and human approval was required for stage transition requests. In Unity Catalog, each task in a deployment job corresponds to a "stage", allowing you to define an arbitrary number of steps (e.g., validation, staging, production rollout). Deployment jobs support human approval steps integrated into the pipeline. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Triggering

A deployment job is automatically triggered whenever a new model version is created. The job then runs the configured pipeline (evaluation, approval, deployment) without manual intervention. This automation streamlines the model promotion process. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Migration from Workspace Model Registry

When migrating models to Unity Catalog, you can create a deployment job to mirror the old stage transitions. For example, if you had email notifications set for stage transition requests, you can migrate them as follows:

- **New model version created:** Configure the deployment job to trigger on model version creation and send an email notification when the job is triggered.
- **Stage transition request:** Corresponds to an approval task within the deployment job; set email notifications for that task's success or failure.
- **Stage transitions:** Correspond to job tasks; set email notifications for the task's success or failure.
- **Comments:** Comments from the Workspace Model Registry are not supported in Unity Catalog.

^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Notifications and Advanced Triggers

You can set notifications on the deployment job to trigger on events such as the creation or approval of a model version. Additionally, if you had webhooks set up for events in the Workspace Model Registry, you can implement them in Unity Catalog using **model event job triggers**. These triggers allow you to automate [Lakeflow Jobs](/concepts/lakeflow-jobs.md) based on the creation of new models, model versions, or model aliases in Unity Catalog. Note that model event job triggers are currently in Private Preview. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance and catalog layer for all data assets, including models.
- [Workspace Model Registry](/concepts/workspace-model-registry.md) – The legacy model registry with fixed stages.
- Aliases and tags – Unity Catalog’s replacement for stages; aliases are used for referencing models, tags for labeling.
- [MLflow](/concepts/mlflow.md) – The open-source platform for managing the ML lifecycle; deployment jobs are an MLflow 3 feature.
- Model lifecycle – The overall process of training, registering, evaluating, approving, and deploying models.
- Model event job trigger – A Private Preview feature for automating jobs based on model events.

## Sources

- migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md](/references/migrate-workflows-and-models-to-unity-catalog-databricks-on-aws-ef30b915.md)
