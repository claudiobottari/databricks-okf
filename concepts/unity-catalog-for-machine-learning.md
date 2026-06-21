---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa5f8defd6be05a06083ef245c97c6059a4be228286394ca6d7d6218767a9b07
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
    - machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - unity-catalog-for-machine-learning
    - UCFML
  citations:
    - file: machine-learning-on-databricks-databricks-on-aws.md
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
title: Unity Catalog for Machine Learning
description: Unified governance of data, ML assets, and model endpoints, providing access management, audit logging, and lineage for the full ML lifecycle.
tags:
  - governance
  - unity-catalog
  - mlops
timestamp: "2026-06-19T09:21:38.567Z"
---

# Unity Catalog for Machine Learning

**Unity Catalog for Machine Learning** refers to the use of Unity Catalog as the unified governance layer for ML assets — including models, features, functions, and experiments — across the full machine learning lifecycle on Databricks. It provides centralized access control, lineage tracking, discovery, and audit capabilities for both data and ML artifacts.^[machine-learning-on-databricks-databricks-on-aws.md]

## Overview

Unity Catalog extends its governance model beyond data tables to cover the key artifacts produced during ML development and production. This includes models registered in the model registry, feature tables in the feature store, user-defined functions used for inference or feature engineering, and experiment metadata tracked by MLflow. By managing all these assets in a single catalog, organizations can enforce consistent security policies, trace the provenance of predictions back to training data, and discover reusable ML assets across teams.^[machine-learning-on-databricks-databricks-on-aws.md]

## Governed Assets

### Models

Models stored in Unity Catalog benefit from unified access control, lineage tracking, and version management. The model registry in Unity Catalog allows teams to manage the full model lifecycle, including staging, testing, and deployment to production endpoints.^[machine-learning-on-databricks-databricks-on-aws.md]

### Features

Feature tables created and managed in the [Feature Store](/concepts/feature-store.md) are governed by Unity Catalog, enabling discovery and reuse of features across projects while maintaining consistent access policies.^[machine-learning-on-databricks-databricks-on-aws.md]

### Functions

User-defined functions (UDFs) used for feature engineering, model inference, or data transformation can be registered in Unity Catalog, making them discoverable and governable alongside other assets.^[machine-learning-on-databricks-databricks-on-aws.md]

### Experiments and Runs

MLflow experiment tracking integrates with Unity Catalog to provide lineage between experiments, models, and the data used for training. This enables reproducibility and auditability of the ML development process.^[machine-learning-on-databricks-databricks-on-aws.md]

## Key Capabilities

### Unified Access Control

Unity Catalog applies a single permission model across data, models, features, and functions. Administrators can grant `SELECT`, `MODIFY`, or `MANAGE` privileges on ML assets using the same RBAC and [ABAC](/concepts/abac-attribute-based-access-control.md) mechanisms used for data tables.^[machine-learning-on-databricks-databricks-on-aws.md]

### Lineage Tracking

Unity Catalog captures lineage relationships between ML assets — for example, which training dataset produced a given model version, or which feature table was used for a particular inference run. This lineage is visible in the Catalog Explorer and can be queried programmatically.^[machine-learning-on-databricks-databricks-on-aws.md]

### Discovery

Users can search for models, features, and functions across catalogs and schemas using the Catalog Explorer or the Unity Catalog API. Tags and descriptions help teams find relevant assets quickly.^[machine-learning-on-databricks-databricks-on-aws.md]

### Audit Logging

All operations on ML assets — including model registration, deployment, and access — are recorded in audit logs, supporting compliance and security investigations.^[machine-learning-on-databricks-databricks-on-aws.md]

## Integration with MLflow

Unity Catalog serves as the backend for the [MLflow Model Registry](/concepts/mlflow-model-registry.md) when models are registered with Unity Catalog as the tracking URI. This integration means that model versions, stage transitions, and deployment metadata are all stored in Unity Catalog and subject to its governance policies.^[machine-learning-on-databricks-databricks-on-aws.md]

## Integration with Model Serving

Models governed by Unity Catalog can be deployed to [Model Serving](/concepts/model-serving.md) endpoints. The serving infrastructure respects the access controls defined in Unity Catalog, ensuring that only authorized users and service principals can query deployed models.^[machine-learning-on-databricks-databricks-on-aws.md]

## Integration with AI Gateway

The [AI Gateway](/concepts/ai-gateway.md) for serving endpoints provides additional governance capabilities — including usage tracking, payload logging, and rate limiting — for models served through Unity Catalog. This creates a unified security approach for both data and ML endpoints.^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Benefits for ML Teams

- **Consistent governance**: Apply the same security policies to ML assets as to data assets, reducing administrative overhead and compliance risk.^[machine-learning-on-databricks-databricks-on-aws.md]
- **Improved discoverability**: Find and reuse models, features, and functions across teams, reducing duplication and accelerating development.^[machine-learning-on-databricks-databricks-on-aws.md]
- **Full lineage**: Trace from production predictions back through model versions, training runs, and source data for debugging and audit.^[machine-learning-on-databricks-databricks-on-aws.md]
- **Simplified MLOps**: Manage the entire model lifecycle — from experiment to production — within a single governed platform.^[machine-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) — Managing model lifecycle with centralized governance
- [Feature Store](/concepts/feature-store.md) — Governed feature management
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking integrated with Unity Catalog
- [Model Serving](/concepts/model-serving.md) — Deploying governed models to production
- [AI Gateway](/concepts/ai-gateway.md) — Governance for model endpoints
- [Unity Catalog Overview](/concepts/unity-catalog.md) — General introduction to Unity Catalog
- ABAC Policies — Attribute-based access control for ML assets
- MLOps Workflows — Automated ML pipelines with Unity Catalog governance

## Sources

- machine-learning-on-databricks-databricks-on-aws.md
- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [machine-learning-on-databricks-databricks-on-aws.md](/references/machine-learning-on-databricks-databricks-on-aws-34650b43.md)
2. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
