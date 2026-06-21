---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 443c17048d27dec80c786a8443a2880bf0e457d11f187be70812d2b9d912b222
  pageDirectory: concepts
  sources:
    - mlops-workflows-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-for-model-lifecycle-tracking
    - MFMLT
  citations:
    - file: mlops-workflows-on-databricks-databricks-on-aws.md
title: MLflow for Model Lifecycle Tracking
description: Using MLflow to track model development, log code snapshots, parameters, metrics, artifacts, and manage the model lifecycle across environments.
tags:
  - mlflow
  - tracking
  - model-management
timestamp: "2026-06-19T19:42:00.816Z"
---

## MLflow for Model Lifecycle Tracking

**MLflow for Model Lifecycle Tracking** describes how the [MLflow](/concepts/mlflow.md) platform is used on Databricks to record, manage, and govern machine learning models as they move from experimentation to production. The platform provides a unified set of tools for logging model metadata, versioning artifacts, and managing deployment status across development, staging, and production environments. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### MLflow Tracking

The core of lifecycle tracking is [MLflow Tracking](/concepts/mlflow-tracking.md), which records the model development process by saving code snapshots, model parameters, metrics, and other metadata. During training, the pipeline logs parameters, metrics, artifacts, and the final model artifact to the MLflow Tracking server. This creates a persistent link between the model, the input data it was trained on, and the code used to generate it. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

For governance requirements, additional artifacts can be saved using MLflow tracking, such as plain-text descriptions and model interpretations (e.g., SHAP plots). In the production environment, the tracking server also stores logs for model evaluation results, allowing offline comparisons between candidate models and the current production model. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Model Registry with Unity Catalog

MLflow integrates with [Unity Catalog](/concepts/unity-catalog.md) to provide a centralized model registry for versioning, governance, and deployment status. Models are registered to a catalog corresponding to the environment they were trained in (e.g., `dev`, `staging`, `prod`). After training, the model artifact is saved as a registered model version at a specified model path in Unity Catalog, and the training task yields a model URI that subsequent validation and deployment pipelines can consume. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Model Aliases (Champion / Challenger)

The lifecycle is managed through aliases assigned to model versions. The production model is given the **Champion** alias, while a newly validated candidate receives the **Challenger** alias. The deployment pipeline can perform offline or online comparisons between the two aliases, tracking results using the MLflow Tracking server. If the Challenger performs better, it replaces the Champion alias. This alias-based approach decouples model deployment from inference pipelines, allowing batch or streaming jobs to always load the current Champion version without code changes. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Integration Across Environments

MLflow is used consistently across the three stages of the MLOps workflow:

- **Development** – Data scientists log experiments to the development workspace’s MLflow Tracking server and register models to the dev catalog.
- **Staging** – Integration tests trigger the same pipelines; models are registered to a staging catalog for testing.
- **Production** – Automated retraining and deployment pipelines log to the production MLflow Tracking server and register models to the production catalog.

This uniformity ensures that all model metadata—including evaluation results, tags, and artifact location—is traceable from experimentation through production. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Deployment and Monitoring

The model lifecycle extends to deployment: Model Serving endpoints are configured using the model path and version (or alias) from Unity Catalog. Databricks Model Serving and data profiling automatically collect inference tables (requests and responses) for monitoring. While the source focuses on MLflow’s tracking and registry role, the logged information feeds directly into monitoring dashboards and alerting pipelines. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Champion vs Challenger Model Deployment](/concepts/championchallenger-model-deployment-strategy.md)
- [Model Serving](/concepts/model-serving.md)
- MLOps
- [Data Profiling](/concepts/data-profiling.md)

## Sources

- mlops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [mlops-workflows-on-databricks-databricks-on-aws.md](/references/mlops-workflows-on-databricks-databricks-on-aws-a1b056b9.md)
