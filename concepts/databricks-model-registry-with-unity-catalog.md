---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 30f287fac5d2a507127306fdcc5f8e791728e7834667c593d0a0a67fdfb62fb2
  pageDirectory: concepts
  sources:
    - mlflow-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-model-registry-with-unity-catalog
    - DMRWUC
    - Migrate model versions from Workspace Model Registry to Unity Catalog
  citations:
    - file: mlflow-on-databricks-databricks-on-aws.md
title: Databricks Model Registry with Unity Catalog
description: A centralized model repository integrated with Unity Catalog providing governance, cross-workspace access, lineage tracking, and model discovery for managing the model deployment lifecycle.
tags:
  - model-registry
  - unity-catalog
  - governance
timestamp: "2026-06-19T19:39:11.294Z"
---

# Databricks Model Registry with Unity Catalog

The **Databricks Model Registry with Unity Catalog** is a centralized model repository, user interface, and set of APIs that enables teams to manage the full lifecycle of machine learning models and generative AI agents. It combines MLflow Model Registry capabilities with Unity Catalog's centralized governance, allowing organizations to govern, track, version, and deploy models across workspaces. ^[mlflow-on-databricks-databricks-on-aws.md]

## Overview

MLflow Model Registry is a core component of the Databricks machine learning platform that serves as a centralized repository for managing model deployment. When integrated with [Unity Catalog](/concepts/unity-catalog.md), the Model Registry provides centralized governance for all AI and ML assets. This integration enables users to access models across different workspaces, track model lineage, and discover models for reuse within their organization. ^[mlflow-on-databricks-databricks-on-aws.md]

## Key Capabilities

The Databricks Model Registry with Unity Catalog provides several key capabilities for managing model lifecycles:

- **Centralized model management**: Store, version, and organize models in a unified catalog governed by Unity Catalog.
- **Cross-workspace access**: Access and share models across multiple Databricks workspaces using Unity Catalog's [Metastore](/concepts/metastore.md) capabilities.
- **Model lineage tracking**: Track the provenance of models, including the experiments, runs, and data used to create them.
- **Model discovery**: Search and discover models available within the organization for reuse.
- **Version control**: Manage multiple versions of a model with metadata, metrics, and parameters tracked for each version.
- **Deployment management**: Transition models through stages (such as Staging, Production, Archived) and deploy them to [Model Serving](/concepts/model-serving.md) endpoints.

^[mlflow-on-databricks-databricks-on-aws.md]

## MLflow 3 Improvements

MLflow 3 on Databricks introduces enhancements to the Model Registry. With MLflow 3, the model version page in Unity Catalog displays metrics, parameters, and metadata from multiple runs, providing a comprehensive view of each model version's performance. Additionally, Deployment Jobs can orchestrate the model lifecycle, including evaluation, approval, and deployment steps, with all events saved to an activity log available on the model version page. ^[mlflow-on-databricks-databricks-on-aws.md]

## Integration with Model Serving

Databricks [Model Serving](/concepts/model-serving.md) is tightly integrated with the Model Registry. Model Serving uses the registry for model versioning, dependency management, validation, and governance. Each model served through Model Serving is available as a REST API that can be integrated into web or client applications, making the registry a critical component for production deployments. ^[mlflow-on-databricks-databricks-on-aws.md]

## Role in the ML Lifecycle

The Model Registry with Unity Catalog sits at the center of the Databricks ML lifecycle, connecting:

1. **[Feature Store](/concepts/feature-store.md)** – Automated feature lookups for model training.
2. **Model Training** – Models are trained and logged to the registry.
3. **[MLflow Tracking](/concepts/mlflow-tracking.md)** – Experiment tracking logs parameters, metrics, and artifacts.
4. **Model Registry** – Centralizes AI models and artifacts with Unity Catalog governance.
5. **Model Serving** – Deploys registered models to REST API endpoints.
6. **Monitoring** – Automatically captures requests and responses for model monitoring.

^[mlflow-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance platform for data and AI assets.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – The open source component that powers model management.
- [Model Serving](/concepts/model-serving.md) – Deployment infrastructure for registered models.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Experiment tracking for model development.
- Deployment Jobs – MLflow 3 feature for managing the model lifecycle.
- [Logged Models](/concepts/logged-models.md) – MLflow 3 concept for tracking models across environments.

## Sources

- mlflow-on-databricks-databricks-on-aws.md

# Citations

1. [mlflow-on-databricks-databricks-on-aws.md](/references/mlflow-on-databricks-databricks-on-aws-bc75dc1f.md)
