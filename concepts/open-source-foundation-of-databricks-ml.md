---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 67db7d48f9132a5837d0f43691a59234a89256d19115285137442b5e55c8d6ca
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - open-source-foundation-of-databricks-ml
    - OFODM
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Open-Source Foundation of Databricks ML
description: Databricks ML platform built on open-source technologies including MLflow, Unity Catalog APIs, and Delta Lake, ensuring portability of models, features, and data.
tags:
  - open-source
  - machine-learning
  - portability
timestamp: "2026-06-19T14:48:39.853Z"
---

Here is the wiki page for "Open-Source Foundation of Databricks ML".

---

## Open-Source Foundation of Databricks ML

Databricks’ machine learning platform is built upon a foundation of open-source projects, including **MLflow**, **Unity Catalog**, and **Delta Lake**. This open-source core ensures that data, models, and pipelines remain portable and that users can leverage the broader open-source ML ecosystem without vendor lock-in. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Open-Source ML Ecosystem Support

Databricks provides full support for the open-source ML ecosystem. You can use any major open-source ML framework on the platform, including **scikit-learn**, **XGBoost**, **LightGBM**, **PyTorch**, **TensorFlow**, **Hugging Face Transformers**, and **Ray**. Model artifacts are stored in open formats that can be exported and run outside Databricks. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Key Open-Source Components

#### MLflow
[MLflow](/concepts/mlflow.md) is an open-source project created by Databricks and used by over 10,000 organizations. It provides the foundation for experiment tracking, model management, and deployment. All experiment tracking data, model artifacts, and pipeline definitions are stored in open formats. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

The openness of MLflow means that:
- Experiment tracking data and model artifacts can be exported and run outside Databricks. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
- You can use any open-source ML framework on Databricks without restriction. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

#### Unity Catalog
Data and AI governance are built upon the open-source [Unity Catalog](/concepts/unity-catalog.md) APIs. This allows organizations to manage data access, lineage, and discovery using standards that are portable across platforms. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

#### Delta Lake
Data storage is based upon the open [Delta Lake](/concepts/delta-lake.md) format. This means your feature data, training datasets, and model artifacts remain in open, portable files that can be read by any compatible system. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Portability and Open Formats

Databricks’ commitment to open-source ensures that any component of the ML lifecycle can be exported and used outside of the Databricks environment. This includes:

- **Model artifacts** stored in open formats (e.g., MLflow Model format). ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
- **Experiment tracking data** stored in open formats. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
- **Pipeline definitions** stored in open formats. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
- **Feature data** and **training datasets** stored in open [Delta Lake](/concepts/delta-lake.md) files. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Related Concepts

- [MLflow](/concepts/mlflow.md) — Open-source experiment tracking and model management.
- [Unity Catalog](/concepts/unity-catalog.md) — Open-source data governance and lineage.
- [Delta Lake](/concepts/delta-lake.md) — Open-source storage format for data lakes.
- [Open-Source ML Ecosystem](/concepts/databricks-open-source-ml-ecosystem.md) — Broader context of frameworks and tools used on Databricks.
- [Mlflow vs. Managed MLflow](/concepts/databricks-managed-mlflow.md) — Comparison of open-source and managed MLflow.
- [Databricks Machine Learning Platform](/concepts/databricks-ml-platform.md) — Overview of the full ML lifecycle on Databricks.

### Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
