---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 201b696eb9f735bef59a8f6380d32b8dc67f447c3f264696a830f4bf5131246c
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-commitment-to-open-source-ml-ecosystem
    - DCTOME
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Databricks Commitment to Open-Source ML Ecosystem
description: Full support for open-source ML frameworks (scikit-learn, PyTorch, TensorFlow, etc.) with open formats via Delta Lake, open-source MLflow, and open-source Unity Catalog APIs for portability.
tags:
  - open-source
  - portability
  - delta-lake
timestamp: "2026-06-18T15:06:22.029Z"
---

# Databricks Commitment to Open-Source ML Ecosystem

**Databricks Commitment to Open-Source ML Ecosystem** refers to the company’s strategy of building its data and machine learning (ML) platform on top of, and actively contributing to, open‑source tools and formats. Rather than locking users into proprietary APIs, Databricks ensures that code, models, features, and governance metadata remain portable and interoperable with the broader ML community.

## Overview

Databricks provides full support for the open‑source ML ecosystem. The platform integrates with popular open‑source ML frameworks—such as scikit-learn, [XGBoost](/concepts/xgboostspark-module.md), LightGBM, PyTorch, TensorFlow, Hugging Face Transformers, and Ray—and adds enterprise‑grade governance, observability, and operational tooling (collectively known as MLOps). This approach allows teams to use their preferred libraries while benefiting from managed infrastructure, lineage tracking, and scalable compute on Databricks.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Open Framework Support

Users can run any open‑source ML framework on Databricks without vendor lock‑in. Models trained using scikit‑learn, PyTorch, TensorFlow, or any other open‑source library can be exported in open model formats and deployed both inside and outside of Databricks. The platform’s [Feature Store](/concepts/feature-store.md) and [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) are pre‑configured to work with common open‑source libraries, and the [Genie Code](/concepts/genie-code.md) AI assistant can generate code that uses those libraries.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Open Formats and Governance

Databricks stores data and AI assets in open, portable formats.

* **{{MLflow}}** – MLflow is an open‑source project created by Databricks and now used by more than 10,000 organizations. It provides experiment tracking, model registry, and deployment workflows. All tracking data, model artifacts, and pipeline definitions are stored in open formats that can be exported and used independently of Databricks.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
* **{{Unity Catalog}}** – Data and AI governance in Databricks is built upon the open‑source Unity Catalog APIs. Metadata, policies, and lineage are stored in a portable, open interface.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
* **{{Delta Lake}}** – Data storage is based on the open [Delta Lake](/concepts/delta-lake.md) format. Feature data and training datasets remain in open, portable files that can be read by any Delta Lake‑compatible engine.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

Because all three are open source, users retain full ownership of their data and models and can move them between environments or cloud providers without re‑architecting.

## Impact on MLOps

The open‑source foundation enables a portable MLOps stack. Models trained with open‑source libraries can be tracked in open‑format MLflow runs, registered in an open Unity Catalog, and deployed to batch or real‑time endpoints. This interoperability reduces switching costs and encourages community innovation around the same core technologies. Databricks also contributes back to these projects, improving performance and adding enterprise features while keeping the core open.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Related Concepts

- [Open-source ML frameworks on Databricks](/concepts/open-source-ml-ecosystem-on-databricks.md)
- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Lake](/concepts/delta-lake.md)
- [MLOps Stacks](/concepts/mlops-stacks.md)
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md)
- [Feature Store](/concepts/feature-store.md)

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
