---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4773b04c92b7d05644d9a010a7e0411bc70725a5687251d3bd5dff51f4c0f932
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - governance-of-ml-and-ai-assets-in-unity-catalog
    - AI Assets in Unity Catalog and Governance of ML
    - GOMAAAIUC
  citations:
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
title: Governance of ML and AI Assets in Unity Catalog
description: Unified governance of data, ML assets, model endpoints, and ML tooling through Unity Catalog, AI Gateway, and Databricks AI Security providing a single security and administration layer.
tags:
  - governance
  - unity-catalog
  - security
timestamp: "2026-06-19T17:49:55.822Z"
---

# Governance of ML and AI Assets in Unity Catalog

**Governance of ML and AI Assets in Unity Catalog** refers to the unified management, security, and lineage capabilities that Databricks provides for machine learning and artificial intelligence assets within the Unity Catalog framework. This includes models, features, experiments, endpoints, and related data assets across the full ML lifecycle.

## Overview

Unity Catalog serves as the governance layer for both data and ML assets. A well-designed ML platform connects data engineering, interactive data science, and production ML in a single governed system. Unity Catalog provides unified governance for these assets, enabling consistent access control, audit logging, and lineage tracking across the entire ML lifecycle. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Key Governance Capabilities

Unity Catalog delivers several governance capabilities that apply to ML and AI assets:

- **Unified governance of data and ML assets** – Models, features, experiments, and training data are managed under the same governance framework as other data assets.
- **Unified governance of model endpoints** – The [Unity AI Gateway](/concepts/unity-ai-gateway.md) (now known as AI Gateway) provides governance for serving endpoints, including access control and monitoring.
- **Unified security approach** – A single security model applies across data and ML tooling, supported by Databricks AI Security practices.
- **Unified administration of data and ML tooling** – Administrators can manage permissions, budgets, and policies for both data and ML resources from a central interface.

^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Components of ML Platform Governance

Unity Catalog supports governance for the key components of an ML platform:

- **Data assets** – Files, tables, processing pipelines, and [Feature Store](/concepts/feature-store.md) features are governed as catalog objects.
- **Experimentation tools** – Notebooks and visualizations are integrated with Unity Catalog for lineage and access control.
- **Training infrastructure** – Customizable environments and flexible compute resources are governed through policies.
- **Deployment and monitoring infrastructure** – Batch and real-time serving endpoints are governed through the AI Gateway.
- **MLOps and governance tools** – Orchestration, CI/CD, lineage, access management, and audit logging are all available within the Unity Catalog framework.

^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The underlying governance platform for data and AI assets.
- [Unity AI Gateway](/concepts/unity-ai-gateway.md) – Governance for model serving endpoints.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model registry integrated with Unity Catalog.
- [Feature Store](/concepts/feature-store.md) – Managed feature tables with governance and lineage.
- Databricks AI Security – Security framework for AI workloads.
- [ML Platform](/concepts/ml-platform.md) – The broader infrastructure that Unity Catalog governs.
- [Model Serving](/concepts/model-serving.md) – Deployment endpoints governed by AI Gateway.

## Sources

- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
