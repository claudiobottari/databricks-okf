---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f59f02c3569b6e70c9b3ba076e5da5838630bd30fab44b2dcec8af9f5f2bfcc4
  pageDirectory: concepts
  sources:
    - log-load-and-register-mlflow-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-model-serving-and-deployment
    - Deployment and MLflow Model Serving
    - MMSAD
    - Deploy Python Code with Model Serving
    - Deploy models using Model Serving
    - MLflow Model Deployment
    - MLflow model deployment
    - deploy the model in model serving
  citations:
    - file: log-load-and-register-mlflow-models-databricks-on-aws.md
title: MLflow Model Serving and Deployment
description: Deploying MLflow models as REST endpoints via Model Serving on Databricks, including validation before deployment and automatic updates based on model version availability.
tags:
  - mlflow
  - model-serving
  - deployment
timestamp: "2026-06-19T19:16:20.941Z"
---

# MLflow Model Serving and Deployment

**MLflow Model Serving and Deployment** refers to the process of hosting a trained MLflow Model as an online REST API endpoint for real-time inference. On Databricks, this is primarily done through **Model Serving**, which automatically manages the infrastructure for registered models. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Prerequisites

Before deploying a model, it must be registered in a model registry. For Databricks, the recommended registry is **[Unity Catalog](/concepts/unity-catalog.md)**, which provides a centralized, governed model store across workspaces. Models created with [MLflow 3](/concepts/mlflow-3.md) can expose parameters and metrics directly in the registry. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Deploying a Model for Online Serving

To deploy a model for online serving:

1. **Register the model** in the Unity Catalog model registry using `mlflow.register_model()` or the Databricks UI.
2. Use **[Model Serving](/concepts/model-serving.md)** to create a REST endpoint from the registered model version.
3. The endpoint is updated automatically as new model versions become available, supporting seamless rollouts and rollbacks. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

### Validation Before Deployment

Before deploying a model, it is recommended to verify that the model is capable of being served. MLflow provides the `mlflow.models.predict()` API to validate model behavior prior to production deployment. See the [MLflow documentation on model validation](https://www.mlflow.org/docs/latest/models.html#validate-models-before-deployment) for details. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Related Concepts

- MLflow Models – The standard format for packaging machine learning models.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Centralized model store used to manage model versions and stages.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ governance solution for managing data and models across workspaces.
- [Model Serving](/concepts/model-serving.md) – Databricks’ managed service for hosting MLflow models as REST endpoints.
- REST API Endpoints – The inference interface for deployed models.

## Sources

- log-load-and-register-mlflow-models-databricks-on-aws.md

# Citations

1. [log-load-and-register-mlflow-models-databricks-on-aws.md](/references/log-load-and-register-mlflow-models-databricks-on-aws-dc2ad486.md)
