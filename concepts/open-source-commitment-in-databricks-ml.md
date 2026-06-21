---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74140dd40adcb2dbc86b71df7389ab0a964d42b5ce695107cf8509d937a8faf9
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - open-source-commitment-in-databricks-ml
    - OSCIDM
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Open Source Commitment in Databricks ML
description: Databricks' commitment to the open-source ML ecosystem by supporting frameworks like scikit-learn, PyTorch, TensorFlow, and Hugging Face, and storing artifacts in open formats based on open-source MLflow, Unity Catalog, and Delta Lake.
tags:
  - databricks
  - open-source
  - ecosystem
  - portability
timestamp: "2026-06-18T11:36:35.027Z"
---

# Open Source Commitment in Databricks ML

Databricks provides a unified platform for the full data science and machine learning lifecycle, from raw data ingestion through feature engineering, model training, deployment, and production monitoring. The platform integrates with popular open‑source ML frameworks and adds enterprise‑grade governance, observability, and operational tooling—collectively known as MLOps. A core principle of the platform is a strong commitment to open source, ensuring that users are never locked into proprietary formats or APIs. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Open Source Support

Databricks fully supports the open‑source ML ecosystem. Users can leverage any open‑source ML framework on the platform, including scikit-learn, [XGBoost](/concepts/xgboostspark-module.md), LightGBM, PyTorch, TensorFlow, Hugging Face Transformers, Ray, and many others. Model artifacts can be stored in open formats using either [MLflow](/concepts/mlflow.md) or custom tools, allowing models to be exported and run outside Databricks without any vendor lock‑in. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Key Open Source Components

### MLflow

[MLflow](/concepts/mlflow.md) is an open‑source platform, created by Databricks and adopted by more than 10,000 organizations. It provides experiment tracking, model registry, and deployment capabilities. All experiment tracking data, model artifacts, and pipeline definitions are stored in open formats, making them portable across environments. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Unity Catalog

Data and AI governance on Databricks is built upon the open‑source [Unity Catalog](/concepts/unity-catalog.md) APIs. This ensures that governance policies, metadata, and access controls remain interoperable and can be managed with standard tools. Unity Catalog unifies governance of data and ML workloads, and its APIs are open and extensible. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Delta Lake

All data storage, including feature data and training datasets, is based on the open [Delta Lake](/concepts/delta-lake.md) format. Delta Lake provides ACID transactions, scalable metadata handling, and unified batch and streaming capabilities. Because data is stored in open, portable files, users can access their data with any Delta Lake–compatible engine, both inside and outside Databricks. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Benefits of the Open Source Commitment

- **Portability:** Models, experiments, and data can be moved between Databricks and other environments without transformation.
- **Interoperability:** Open APIs and formats allow integration with the broader open‑source ecosystem, including community‑developed tools and libraries.
- **No vendor lock‑in:** Organizations can adopt Databricks for its managed services while retaining full ownership and control of their assets in standard formats.
- **Community innovation:** By contributing to and building on open‑source projects, Databricks ensures that users benefit from ongoing community improvements and wide adoption. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Conclusion

Databricks’ commitment to open source is reflected in its support for a wide range of open‑source ML frameworks and its use of open standards—MLflow, Unity Catalog, and Delta Lake—as foundational components of the platform. This approach gives data scientists and ML engineers the flexibility to choose the best tools for their work while maintaining governance, reproducibility, and portability across the ML lifecycle. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
