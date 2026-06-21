---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b7a73e071035b46343c5dba47e32be98f3340ac4eb1eae7d3964734364a4ad1c
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ml-platform
  citations:
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
title: ML Platform
description: The combined infrastructure, tooling, and governance layer that supports the full ML lifecycle on Databricks
tags:
  - machine-learning
  - platform
  - governance
timestamp: "2026-06-19T14:22:19.594Z"
---

# ML Platform

An **ML platform** is the combined infrastructure, tooling, and governance layer that supports the full machine learning (ML) lifecycle, from raw data to production models. A well-designed ML platform connects data engineering, interactive data science, and production ML in a single governed system. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Key Components

The core components of an ML platform include: ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

- **Data assets** — such as files, tables, processing pipelines, and feature stores.
- **Experimentation tools** — notebooks and visualizations with simple collaboration and AI assistance.
- **Training infrastructure** — customizable environments and flexible compute resources.
- **Deployment and monitoring infrastructure** — for batch and real-time serving, with production dashboards and alerts.
- **MLOps and governance tools** — for orchestration, CI/CD, lineage, access management, and audit logging.

These components work together to enable teams to scope use cases, explore data, prepare features, train models, evaluate quality, register and stage models, deploy to production, and monitor and retrain models over time.

## Governance Capabilities

A robust ML platform provides unified governance of both data and ML assets. Key governance capabilities include: ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

- **Unified governance of data and ML assets** — provided by [Unity Catalog](/concepts/unity-catalog.md).
- **Unified governance of model endpoints** — provided by the Unity AI Gateway for serving endpoints.
- **Unified security approach** — see Databricks AI Security.
- **Unified administration** — of data and ML tooling, covering access management and audit logging.

This unified layer ensures that data, models, and endpoints are managed under a consistent set of policies, simplifying compliance and reducing operational overhead.

## Relation to the ML Lifecycle

The ML platform supports every stage of the [ML Lifecycle](/concepts/ml-lifecycle.md), from scoping the use case through monitoring and retraining. By integrating data engineering, experimentation, training, deployment, and monitoring into a single governed environment, the platform reduces friction between teams and accelerates the path from idea to production.

## AI-Assisted Development

An ML platform increasingly incorporates AI-assisted development tools. On Databricks, this includes Genie Code, an AI assistant integrated across notebooks and the workspace that can be used for development, debugging, and ongoing operations. Genie Code can help at every step of the workflow, including discovering relevant models and data, prototyping pipelines for featurization and model training, and analyzing production model serving endpoints. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — unified governance for data and ML assets
- [Model Serving](/concepts/model-serving.md) — real-time and batch inference infrastructure
- [Feature Store](/concepts/feature-store.md) — managed feature engineering and sharing
- [MLflow](/concepts/mlflow.md) — experiment tracking, model registry, and deployment
- MLOps — orchestration, CI/CD, and monitoring practices
- [AI Runtime](/concepts/ai-runtime.md) — optimized runtime for training and inference
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — environment for ML workloads
- [ML Lifecycle](/concepts/ml-lifecycle.md) — the end-to-end journey from raw data to production models

## Sources

- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
