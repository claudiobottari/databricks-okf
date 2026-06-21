---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 019e28d6510109b44e135dc51d152d3a53dcdba7f50e6dd1c04d5ae72df77e51
  pageDirectory: concepts
  sources:
    - machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-for-ml
    - UCFM
  citations:
    - file: machine-learning-on-databricks-databricks-on-aws.md
    - file: data-profiling-metric-tables-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Unity Catalog for ML
description: Unified governance layer on Databricks that manages data, features, models, and functions with access control, lineage tracking, and discovery for ML assets.
tags:
  - databricks
  - unity-catalog
  - governance
  - data-management
timestamp: "2026-06-19T19:24:01.925Z"
---

---

title: "Unity Catalog for ML"
summary: "How Unity Catalog governs and manages machine learning assets, including models, functions, features, and data across the ML lifecycle."
sources:
  - machine-learning-on-databricks-databricks-on-aws.md.md
  - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md.md
  - data-profiling-metric-tables-databricks-on-aws.md.md
  - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md.md
kind: concept
createdAt: "2026-06-20T10:46:48.395Z"
updatedAt: "2026-06-20T10:46:48.395Z"
tags:
  - unity-catalog
  - machine-learning
  - governance
  - mlflow
  - databricks
aliases:
  - unity-catalog-for-ml
  - UC4ML
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Unity Catalog for ML

**Unity Catalog for ML** is the application of [Unity Catalog](/concepts/unity-catalog.md)—Databricks’ unified governance platform—to the machine learning lifecycle. It provides a single, centralized system for managing and governing data, models, functions, features, and other ML assets, enabling discovery, access control, lineage tracking, and compliance across the entire ML workflow. ^[machine-learning-on-databricks-databricks-on-aws.md]

## Overview

Unity Catalog for ML unifies the governance of all ML-related assets, including models, features, and functions, within a single catalog. This allows organizations to manage access control, track lineage, and discover assets across their ML infrastructure without switching between separate systems. ^[machine-learning-on-databricks-databricks-on-aws.md]

## Key Capabilities

### Model Governance and Lifecycle Management

Unity Catalog provides a centralized model registry for managing the complete model lifecycle. Models can be registered, versioned, and deployed with full governance. The registry supports:

- **Model lineage tracking** – Records how models were created, trained, and deployed.
- **Access control** – Models are governed by Unity Catalog’s unified permissions, ensuring only authorized users can view, modify, or deploy models. ^[machine-learning-on-databricks-databricks-on-aws.md]
- **Model discovery** – Users can search and browse models across workspaces. ^[machine-learning-on-databricks-databricks-on-aws.md]

### Feature and Function Governance

Features and user-defined functions (UDFs) created for ML workflows are also governed by Unity Catalog. This enables:

- **Feature discovery** – Data scientists can find and reuse features across projects. ^[machine-learning-on-databricks-databricks-on-aws.md]
- **Function governance** – UDFs used in model training or inference are subject to the same access controls and lineage tracking as other catalog objects. ^[machine-learning-on-databricks-databricks-on-aws.md]

### Data Profiling and Monitoring

Unity Catalog integrates with [Data Profiling](/concepts/data-profiling.md) to monitor data quality, model performance, and prediction drift. Profiling provides automated alerts and root cause analysis for data and model issues. ^[machine-learning-on-databricks-databricks-on-aws.md]

The [Profile Metrics Table](/concepts/profile-metrics-table.md) and [Drift Metrics Table](/concepts/drift-metrics-table.md) store statistics computed over time windows, enabling drift detection and data quality monitoring at the catalog level. ^[data-profiling-metric-tables-databricks-on-aws.md]

### Serverless Budget Policy

For serverless ML workloads, Unity Catalog supports [Serverless Budget Policy](/concepts/serverless-budget-policy.md) configuration. A serverless budget policy can be assigned to an [MLflow Experiment](/concepts/mlflow-experiment.md) to control spending on serverless workloads like scheduled scorers and agent evaluations. If the workspace's default policy is disabled, a `403 PERMISSION_DENIED` error occurs unless a policy is explicitly assigned. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Model Training and Evaluation

Unity Catalog governs the model training and evaluation process by providing a single source of truth for models. [MLflow](/concepts/mlflow.md) experiments are tracked against Unity Catalog, and models can be registered with full lineage. ^[machine-learning-on-databricks-databricks-on-aws.md]

## Use Cases

### Unified Data and Model Governance

Organizations can use Unity Catalog to apply the same governance policies to their training data, features, and models, ensuring consistency across the ML pipeline. ^[machine-learning-on-databricks-databricks-on-aws.md]

### Model Registry for Production

The model registry in Unity Catalog is used to manage model deployments to [Model Serving](/concepts/model-serving.md) endpoints. Models can be versioned, approved, and deployed with full audit trails. ^[machine-learning-on-databricks-databricks-on-aws.md]

### Feature Store Governance

Features created in the [Feature Store](/concepts/feature-store.md) are governed by Unity Catalog, providing a single source of truth for feature definitions and enabling feature discovery across teams. ^[machine-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The core governance platform for data and AI assets on Databricks.
- [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) – The model registry within Unity Catalog for managing the model lifecycle.
- [MLflow](/concepts/mlflow.md) – The open-source platform for tracking experiments and managing models.
- [Data Profiling](/concepts/data-profiling.md) – Statistical analysis of table columns for data quality monitoring.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – A control mechanism for serverless workload spending.
- [Feature Store](/concepts/feature-store.md) – A centralized repository for features used in ML models.
- [Model Serving](/concepts/model-serving.md) – Deploying models as scalable REST endpoints.

## Sources

- machine-learning-on-databricks-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- data-profiling-metric-tables-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [machine-learning-on-databricks-databricks-on-aws.md](/references/machine-learning-on-databricks-databricks-on-aws-34650b43.md)
2. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
3. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
