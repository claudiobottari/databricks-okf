---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9e0b0c85ed66baf40836936b511f41178dd6a512128928411672eff3c9c93dbb
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-ml-governance
    - UCMG
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Unity Catalog ML Governance
description: Applying Unity Catalog's fine-grained access controls, lineage tracking, and governance to machine learning assets including data, features, models, and endpoints for a complete audit trail.
tags:
  - governance
  - unity-catalog
  - mlops
  - databricks
timestamp: "2026-06-19T09:50:13.940Z"
---

# Unity Catalog ML Governance

**Unity Catalog ML Governance** refers to the governance layer that Unity Catalog provides for machine learning (ML) assets on Databricks. It unifies governance of data, features, models, and endpoints, offering fine-grained access controls, full lineage tracking, and auditability across the ML lifecycle. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Overview

Unity Catalog serves as the central governance platform for both data and ML workloads. All ML assets — including training data, features, models, and serving endpoints — are managed under Unity Catalog with fine-grained access controls, enabling organizations to enforce consistent security and compliance policies across the entire ML pipeline. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Key Capabilities

### Data and Feature Governance

Features are managed in a [Feature Store](/concepts/feature-store.md) with a single, governed source of truth for both batch and real-time serving. Data can be prepared for ML using any data engineering tools (e.g., [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md)) while remaining fully governed by Unity Catalog’s access controls. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Model Governance and Lineage

[MLflow](/concepts/mlflow.md) integrates with Unity Catalog and Git to provide tracking and lineage for data and code assets. Each model version in the registry links back to the training run, dataset, environment, and git commit that produced it, creating a complete audit trail for any deployed model. This ensures reproducible, auditable ML development. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### End-to-End Governance

Data, features, models, and endpoints are fully governed by Unity Catalog together with [AI Gateway](/concepts/ai-gateway.md). This unified governance covers the entire ML lifecycle from raw data ingestion through feature engineering, model training, deployment, and production monitoring. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Open Source Foundation

Unity Catalog ML Governance is built upon the open-source [Unity Catalog](/concepts/unity-catalog.md) APIs. Data storage is based on the open [Delta Lake](/concepts/delta-lake.md) format, ensuring that feature data and training datasets remain in open, portable files. This enables governance capabilities that are portable across environments and not locked into a single vendor. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Related Concepts

- MLOps – The operational practices that Unity Catalog governance supports.
- [Databricks-Managed MLflow](/concepts/databricks-managed-mlflow.md) – The experiment and model registry with Unity Catalog integration.
- [Fine-grained access controls](/concepts/dynamic-views-for-fine-grained-access-control.md) – The mechanism for securing ML assets.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – One of the assets governed by Unity Catalog.

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
