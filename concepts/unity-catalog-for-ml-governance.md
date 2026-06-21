---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 016803afac68cc626b1a04cf3331d043c8f9287eb9fee5afcb8ac77d082c29d0
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-for-ml-governance
    - UCFMG
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Unity Catalog for ML Governance
description: A unified governance layer for data, features, models, AI endpoints, and inference tables, built on open-source Unity Catalog APIs with fine-grained access controls.
tags:
  - governance
  - mlops
  - data-management
timestamp: "2026-06-19T18:11:23.337Z"
---

```markdown
---
title: Unity Catalog for ML Governance
summary: Unified data and AI governance layer on Databricks that governs features, models, endpoints, and inference data with fine-grained access controls and lineage tracking.
sources:
  - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:36:02.002Z"
updatedAt: "2026-06-19T14:48:16.455Z"
tags:
  - governance
  - machine-learning
  - data-management
aliases:
  - unity-catalog-for-ml-governance
  - UCFMG
confidence: 0.92
provenanceState: merged
inferredParagraphs: 0
---

# Unity Catalog for ML Governance

**Unity Catalog for ML Governance** refers to the practice of using [[Unity Catalog]] as the central governance layer for machine learning (ML) assets — including features, models, model versions, and serving endpoints — across the full ML lifecycle. By unifying data and AI governance under a single system, organizations can apply consistent access controls, lineage tracking, and auditability to both data and ML artifacts. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Overview

Databricks provides a unified platform for the full data science and ML lifecycle, from raw data ingestion through feature engineering, model training, deployment, and production monitoring. Unity Catalog serves as the governance backbone for this platform, managing all data and ML assets with fine-grained access controls. This integration allows organizations to adjust data engineering and ML boundaries to fit their structure while maintaining a single source of truth for governance. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

A well-designed ML platform connects data engineering, interactive data science, and production ML in a single governed system. Key governance capabilities include unified governance of data and ML assets, unified governance of model endpoints through [[AI Gateway]], a unified security approach, and unified administration of data and ML tooling. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Key Capabilities

### Feature Governance

Features are managed in a [[Feature Store]] for both batch and real-time serving, with a single, governed source of truth for features under Unity Catalog. All feature data remains in open, portable [[Delta Lake]] format. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Model Registry and Lineage

Each model version in the registry links back to the training run, dataset, environment, and git commit that produced it, providing a complete audit trail for any deployed model. This integration with [[MLflow]] and Git provides tracking and lineage for data and code assets. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Inference Table Governance

Real-time model serving logs to inference tables governed in Unity Catalog, ensuring that production inference data is subject to the same access controls and governance policies as other data assets. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Data Quality Monitoring

[[Data quality monitoring]] provides monitoring with custom metrics, dashboards, and alerts for ML-related data assets, all governed through Unity Catalog. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Model Serving Governance

Unity Catalog governance extends to model serving endpoints through [[AI Gateway]], which provides usage tracking, payload logging, and security controls for models deployed as REST endpoints. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## MLOps and Governance

Databricks provides a full suite of tools for ML operations (MLOps) and governance. [[MLOps Stacks]] provides templates for enabling automated, repeatable promotion from development to production using infrastructure-as-code. Data, features, models, and endpoints are fully governed by Unity Catalog and AI Gateway. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Open Standards Foundation

Unity Catalog for ML governance is built upon open standards:

- **Data and AI governance** uses the open-source [[Unity Catalog]] APIs
- **Data storage** is based on the open [[Delta Lake]] format
- **Model artifacts** are stored in open formats that can be exported and run outside Databricks
- **Experiment tracking** data, model artifacts, and pipeline definitions are stored in open formats via [[MLflow]]

^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Related Concepts

- [[MLflow]] — Open-source platform for ML lifecycle management
- [[Feature Store]] — Governed feature management for ML
- [[AI Gateway]] — Governance layer for AI model serving
- [[Unity Catalog]] — Central governance system for data and AI assets
- [[Data Quality Monitoring]] — Monitoring with custom metrics and alerts governed through Unity Catalog
- [[MLOps Stacks]] — Templates for automated ML promotion using infrastructure-as-code
- [[Delta Lake]] — Open storage format for governed data

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md
```

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
