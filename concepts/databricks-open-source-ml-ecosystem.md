---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a12a42c40598b74fcad795b0ddd70196feb99a33ad65fe0d3d367716aa0e33f
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-open-source-ml-ecosystem
    - DOSME
    - Open-Source ML Ecosystem
    - databricks-commitment-to-open-source-ml-ecosystem
    - DCTOME
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Databricks Open Source ML Ecosystem
description: Databricks' full support for the open-source ML ecosystem including frameworks like scikit-learn, PyTorch, TensorFlow, and Hugging Face, with open formats for artifacts (MLflow), governance (Unity Catalog APIs), and storage (Delta Lake).
tags:
  - open-source
  - interoperability
  - ml-frameworks
  - databricks
timestamp: "2026-06-19T09:50:45.403Z"
---

# Databricks Open Source ML Ecosystem

The **Databricks Open Source ML Ecosystem** refers to the collection of open-source technologies that Databricks builds upon and contributes to, enabling machine learning workflows from data ingestion through production monitoring. Databricks integrates these open-source frameworks with enterprise-grade governance, observability, and operational tooling, collectively known as MLOps. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Core Open Source Components

### MLflow

[MLflow](/concepts/mlflow.md) is an open-source platform for the complete machine learning lifecycle, created by Databricks and used by over 10,000 organizations. It provides experiment tracking, model packaging, model registry, and deployment capabilities. On Databricks, managed MLflow integrates with [Unity Catalog](/concepts/unity-catalog.md) and Git to provide full lineage, ensuring each model version links back to its training run, dataset, environment, and git commit. All experiment tracking data, model artifacts, and pipeline definitions are stored in open, portable formats. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Unity Catalog

Data and AI governance in Databricks are built upon the open-source [Unity Catalog](/concepts/unity-catalog.md) APIs. Unity Catalog provides fine-grained access controls for data and ML assets, with data storage based on the open [Delta Lake](/concepts/delta-lake.md) format. This ensures that feature data and training datasets remain in open, portable files that can be exported and used outside Databricks. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Delta Lake

[Delta Lake](/concepts/delta-lake.md) is an open-source storage layer that brings reliability and performance to data lakes. It serves as the foundation for data storage on Databricks, enabling ACID transactions, scalable metadata handling, and unified batch and streaming processing. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Supported Open Source Frameworks

Databricks provides full support for a wide range of open-source ML frameworks. Users can leverage any of the following tools directly on the platform:

- scikit-learn
- [XGBoost](/concepts/xgboostspark-module.md) and LightGBM
- PyTorch
- TensorFlow
- Hugging Face Transformers
- Ray

All model artifacts can be stored in open formats that can be exported and run outside Databricks, ensuring no vendor lock-in. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Open Format Commitment

A key principle of the Databricks open source ML ecosystem is portability. Feature data, training datasets, model artifacts, and experiment tracking data are all stored in open, portable formats. This allows organizations to move workloads between Databricks and other environments as needed, maintaining flexibility and avoiding proprietary lock-in. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## ML Capabilities Across the Lifecycle

The open source ecosystem supports each stage of the ML lifecycle:

### Training

Pre-configured and customizable environments allow users to bring custom ML libraries. Serverless CPU and GPU-accelerated compute resources enable scaling up and scaling out on demand. The [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) provides high-performance compute for deep learning workloads. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Experiment Tracking

Databricks-managed MLflow provides the foundation for reproducible, auditable ML development. Its open-source tracking API records parameters, metrics, and artifacts for each run. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Deployment

Models can be served for both batch inference and real-time serving using open formats. MLflow Model Serving provides low-latency API endpoints that can be deployed to production. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Monitoring

Production models log to inference tables governed in Unity Catalog, with [Data Quality Monitoring](/concepts/data-quality-monitoring.md) providing custom metrics, dashboards, and alerts based on open standards. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## MLOps and Governance

[MLOps Stacks](/concepts/mlops-stacks.md) provides open-source templates for enabling automated, repeatable promotion from development to production using infrastructure-as-code. All data, features, models, and endpoints are governed through Unity Catalog and the [AI Gateway](/concepts/ai-gateway.md). ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Benefits of the Open Source Ecosystem

- **Portability**: Models and data stored in open formats can be exported and run outside Databricks
- **Flexibility**: Full support for any open-source ML framework
- **Community**: Leverages widely adopted tools maintained by large open-source communities
- **No vendor lock-in**: Open APIs and formats prevent dependency on proprietary systems
- **Interoperability**: Seamless integration between data engineering and ML workloads

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-built ML environment with open-source libraries
- [Feature Store](/concepts/feature-store.md) – Managed feature serving built on Delta Lake
- [Model Serving](/concepts/model-serving.md) – Real-time and batch inference endpoints
- [Genie Code](/concepts/genie-code.md) – AI-assisted data science assistant
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md) – Guidance for PyTorch, TensorFlow, and other frameworks

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
