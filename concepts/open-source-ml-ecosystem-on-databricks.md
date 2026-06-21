---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 836189a1939c0f862634aa9d6ee9257979b0a51f814af0901c009ea87e1403d3
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - open-source-ml-ecosystem-on-databricks
    - OMEOD
    - Open-source ML frameworks on Databricks
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Open-Source ML Ecosystem on Databricks
description: Full support for popular open-source ML frameworks (scikit-learn, PyTorch, TensorFlow, etc.) and open formats (Delta Lake, MLflow, Unity Catalog APIs) ensuring portability.
tags:
  - open-source
  - machine-learning
  - interoperability
timestamp: "2026-06-19T18:11:37.151Z"
---

# Open-Source ML Ecosystem on Databricks

The **open-source ML ecosystem on Databricks** encompasses the full range of open-source machine learning frameworks, tools, and formats that are natively supported on the Databricks platform. Databricks integrates popular open-source ML libraries with enterprise-grade governance, observability, and operational tooling, collectively known as MLOps. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Supported Open-Source Frameworks

Databricks supports virtually any open-source ML framework. This includes widely used libraries such as scikit-learn, XGBoost, LightGBM, PyTorch, TensorFlow, Hugging Face Transformers, and Ray. Users can install and use these frameworks in pre-configured or customizable environments, whether on serverless CPU or GPU-accelerated compute resources. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## MLflow: Open-Source Experiment Tracking

[MLflow](/concepts/mlflow.md) is an open-source platform, created by Databricks and used by over 10,000 organizations, that provides the foundation for reproducible and auditable ML development. On Databricks, MLflow integrates with [Unity Catalog](/concepts/unity-catalog.md) and Git to provide tracking and lineage for data and code assets. Each model version in the registry links back to the training run, dataset, environment, and git commit that produced it, providing a complete audit trail for any deployed model. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

MLflow stores experiment tracking data, model artifacts, and pipeline definitions in open formats that can be exported and run outside Databricks. This ensures portability and avoids vendor lock-in for ML workflows. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Open Data and Governance Formats

Data and AI governance on Databricks are built upon open-source foundations. The [Unity Catalog](/concepts/unity-catalog.md) APIs are open-source, and all data storage is based on the open [Delta Lake](/concepts/delta-lake.md) format. Feature data and training datasets remain in open, portable files that can be accessed outside the Databricks environment. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Model Artifact Portability

Model artifacts stored in MLflow use open formats that support export and inference outside Databricks. This allows organizations to train models on Databricks and deploy them to other environments, or to bring models trained elsewhere into Databricks for serving or monitoring. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Unified Platform Integration

The open-source ecosystem is integrated across the full ML lifecycle on Databricks:

- **Data preparation**: Features are managed in a [Feature Store](/concepts/feature-store.md) using open Delta Lake formats, governed by open Unity Catalog APIs. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
- **Model training**: Any open-source framework can be used with flexible, scalable compute resources. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
- **Model deployment**: Both [batch inference](/concepts/batch-inference-on-databricks.md) and real-time serving are supported, with models stored in open MLflow formats. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
- **Monitoring**: Production monitoring uses inference tables governed in Unity Catalog, and data quality monitoring provides alerts and dashboards. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Feature Store](/concepts/feature-store.md)
- MLOps
- [Model Serving](/concepts/model-serving.md)
- Batch Inference
- [Open-Source vs Managed MLflow](/concepts/open-source-vs-databricks-managed-mlflow.md)
- Hugging Face Transformers on Databricks

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
