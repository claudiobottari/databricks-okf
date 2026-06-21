---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a7ba3224eb0d7280bdc45058210a573858abfcb20162dabda4c4283686cc160
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-and-feature-engineering
    - Feature Engineering and Feature Store
    - FSAFE
    - Feature Engineering in Databricks|Feature Store
    - Feature Store and Feature Engineering release notes
    - Feature Store vs Feature Engineering
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Feature Store and Feature Engineering
description: Managed Feature Store in Unity Catalog providing a single governed source of truth for features, supporting both batch and real-time serving with Genie Code-assisted discovery and transformation.
tags:
  - feature-engineering
  - mlops
  - data-preparation
timestamp: "2026-06-18T15:05:47.863Z"
---

# Feature Store and Feature Engineering

**Feature Store and Feature Engineering** refers to the unified platform capabilities within Databricks for preparing, storing, serving, and governing features used in machine learning models. The Feature Store provides a single, governed source of truth for features that can be used for both batch and real-time serving. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Overview

Feature engineering is the process of transforming raw data into meaningful features that improve the performance of machine learning models. On Databricks, data can be prepared for ML using any data engineering tools, such as [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md). The resulting features are managed in a Feature Store that supports both batch inference and real-time serving, ensuring consistency between training and production environments. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Feature Store Capabilities

### Single Source of Truth

The Feature Store consolidates all feature data under a unified governance framework. With all data managed under [Unity Catalog](/concepts/unity-catalog.md) with fine-grained access controls, organizations can adjust data engineering and ML boundaries to fit their structure. This governance extends to feature data, training datasets, and model artifacts. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Batch and Real-Time Serving

Features stored in the Feature Store can be served for both batch inference (applying models efficiently to large datasets) and real-time serving (providing models as low-latency API endpoints). This dual capability ensures that the same features used during training are available during production inference, reducing training-serving skew. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Feature Engineering with Genie Code

[Genie Code](/concepts/genie-code.md) accelerates feature discovery and preparation by browsing [Unity Catalog](/concepts/unity-catalog.md) to discover relevant tables, suggesting feature transformations, and generating code for ingestion and feature pipelines. Data scientists can use natural language chat, UIs, or code to build feature engineering workflows. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Open Standards and Portability

Feature data and training datasets are stored on the open [Delta Lake](/concepts/delta-lake.md) format, ensuring portability across systems. The Feature Store integrates with [MLflow](/concepts/mlflow.md) for experiment tracking, enabling reproducibility by linking each model version back to the training run, dataset, environment, and git commit that produced it. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — Governance framework for data and AI assets
- [Feature Store](/concepts/feature-store.md) — Central repository for feature data
- [Delta Lake](/concepts/delta-lake.md) — Open storage format for feature data
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model registry
- Batch Inference — Applying models to large datasets offline
- [Model Serving](/concepts/model-serving.md) — Real-time and batch model deployment
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — Tool for data preparation pipelines
- [Genie Code](/concepts/genie-code.md) — AI-assisted data discovery and feature engineering

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
