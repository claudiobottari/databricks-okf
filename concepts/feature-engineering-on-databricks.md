---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5e3bb72f0d5af73d8dd4e02ab9a1155b8b8cb6bfbef5bf333a7d1b3819c68d3
  pageDirectory: concepts
  sources:
    - machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-engineering-on-databricks
    - FEOD
    - Feature Engineering in Databricks
    - Feature serving on Databricks
  citations:
    - file: machine-learning-on-databricks-databricks-on-aws.md
title: Feature Engineering on Databricks
description: Databricks feature store service for creating, managing, and serving ML features with automated data pipelines and feature discovery.
tags:
  - databricks
  - feature-store
  - feature-engineering
  - mlops
timestamp: "2026-06-19T19:21:10.273Z"
---

# Feature Engineering on Databricks

**Feature Engineering on Databricks** refers to the process of creating, managing, and serving features for machine learning models using Databricks' integrated platform. Feature engineering is a critical step in the ML lifecycle that transforms raw data into meaningful input variables that improve model performance.

## Overview

Databricks provides a comprehensive feature engineering solution through its [Feature Store](/concepts/feature-store.md), which enables teams to create, manage, and serve features with automated data pipelines and feature discovery. The platform integrates feature engineering directly into the broader ML workflow, from data preparation through production monitoring. ^[machine-learning-on-databricks-databricks-on-aws.md]

## Key Capabilities

### Feature Creation and Management

The Databricks Feature Store allows data scientists and engineers to create features using familiar tools like Databricks notebooks and [Databricks Runtime for ML](/concepts/databricks-runtime-for-ml.md). Features can be developed collaboratively using Python, R, Scala, or SQL, and are stored in a centralized repository with [Unity Catalog](/concepts/unity-catalog.md) governance. ^[machine-learning-on-databricks-databricks-on-aws.md]

### Automated Feature Engineering

AutoML on Databricks includes automated feature engineering capabilities that can automatically build high-quality features with minimal code. This includes automated feature selection, transformation, and hyperparameter tuning to accelerate model development. ^[machine-learning-on-databricks-databricks-on-aws.md]

### Feature Serving

Features created in the Feature Store can be served for both training and inference through automated data pipelines. This ensures consistency between training and production environments, reducing the risk of training-serving skew. ^[machine-learning-on-databricks-databricks-on-aws.md]

## Integration with ML Workflows

Feature engineering on Databricks is tightly integrated with the complete ML lifecycle:

- **Data Preparation**: Features are built from data loaded and prepared using [Lakeflow Jobs](/concepts/lakeflow-jobs.md) and ETL pipelines. ^[machine-learning-on-databricks-databricks-on-aws.md]
- **Model Training**: Features are accessed during training of both classic ML models and deep learning models using [Distributed training](/concepts/workload-yaml-for-distributed-training.md) frameworks. ^[machine-learning-on-databricks-databricks-on-aws.md]
- **Model Deployment**: Features are served to [Model Serving](/concepts/model-serving.md) endpoints for real-time inference with automatic scaling and GPU support. ^[machine-learning-on-databricks-databricks-on-aws.md]
- **Monitoring**: Feature quality and drift are monitored through [Data Profiling](/concepts/data-profiling.md) and [Anomaly Detection](/concepts/anomaly-detection.md) tools. ^[machine-learning-on-databricks-databricks-on-aws.md]

## Governance and Discovery

Features are governed through [Unity Catalog](/concepts/unity-catalog.md), which provides unified access control, lineage tracking, and discovery across the organization. This enables teams to find and reuse existing features, reducing duplication and improving consistency across ML projects. ^[machine-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — Centralized repository for managing and serving features
- AutoML — Automated model building including feature engineering
- [Databricks Runtime for ML](/concepts/databricks-runtime-for-ml.md) — Pre-configured environment with ML libraries
- [Unity Catalog](/concepts/unity-catalog.md) — Governance and discovery for data and features
- [Model Serving](/concepts/model-serving.md) — Deploying models with feature serving
- [Data Profiling](/concepts/data-profiling.md) — Monitoring feature quality and drift
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking for feature engineering experiments

## Sources

- machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [machine-learning-on-databricks-databricks-on-aws.md](/references/machine-learning-on-databricks-databricks-on-aws-34650b43.md)
