---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cbb8cb3799f922a57fda8048f4c34e6251ad01f8e728648a3c1d73b55d95d10b
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ml-platform
    - DMP
    - Databricks AI Platform
    - Databricks platform
    - Databricks Machine Learning Platform
    - databricks-ml-lifecycle-platform
    - DMLP
    - databricks-unified-ml-platform
    - DUMP
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Databricks ML Platform
description: Unified platform for the full data science and machine learning lifecycle on Databricks, integrating open-source frameworks with enterprise MLOps tooling.
tags:
  - machine-learning
  - platform
  - databricks
timestamp: "2026-06-19T14:47:54.070Z"
---

## Databricks ML Platform

**Databricks ML Platform** is a unified platform for the full data science and machine learning (ML) lifecycle, from raw data ingestion through feature engineering, model training, deployment, and production monitoring. It integrates popular open-source ML frameworks with enterprise-grade governance, observability, and operational tooling, collectively known as MLOps. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Exploratory Data Analysis

Databricks simplifies exploratory data analysis (EDA) by providing interactive, collaborative, and AI-assisted tools. Data scientists can explore data using natural language chat, user interfaces, or code, and collaborate using real-time co-editing and Git-based code sharing. The Genie Code tool can perform fully automated EDA or act as an interactive assistant. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Prepare and Serve Features

Data preparation for ML is streamlined by unifying governance of data and ML workloads through [Unity Catalog](/concepts/unity-catalog.md), with fine-grained access controls. Data can be prepared using any Data Engineering tool, such as Lakeflow Spark Declarative Pipelines. Features are managed in a [Feature Store](/concepts/feature-store.md) for both batch and real-time serving, providing a single, governed source of truth for features. [Genie Code](/concepts/genie-code.md) also accelerates data discovery and preparation by browsing Unity Catalog, suggesting feature transformations, and generating code for ingestion and feature pipelines. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Train ML Models

Databricks offers flexible tools for training ML and deep learning models. Pre-configured and customizable environments allow the use of custom ML libraries, and serverless CPU and GPU-accelerated compute resources enable scaling up and scaling out on demand. Genie Code provides intelligent AutoML, taking natural language requests and building full multi-notebook workflows for featurization, training, tuning, evaluation, and deployment. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Track and Manage Experiments

Databricks-managed MLflow provides the foundation for reproducible, auditable ML development. Its integrations with [Unity Catalog](/concepts/unity-catalog.md) and Git provide tracking and lineage for data and code assets. Each model version in the [Model Registry](/concepts/mlflow-model-registry.md) links back to the training run, dataset, environment, and git commit that produced it, ensuring a complete audit trail for any deployed model. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Deploy and Serve Models

Databricks supports both Batch Inference and [Model Serving](/concepts/model-serving.md) for real-time serving. Batch inference applies models efficiently to large datasets, while real-time serving provides models as low-latency API endpoints. Genie Code can generate code for model deployment and also diagnose issues and performance for model serving endpoints. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Evaluate and Monitor

Databricks provides flexible evaluation for training and continuous monitoring for production. Real-time serving logs to inference tables governed in [Unity Catalog](/concepts/unity-catalog.md), and data quality monitoring provides custom metrics, dashboards, and alerts. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### MLOps and Governance

The platform offers a full suite of MLOps and governance tools. [MLOps Stacks](/concepts/mlops-stacks.md) provides templates for enabling automated, repeatable promotion from development to production using infrastructure-as-code. Data, features, models, and endpoints are fully governed by [Unity Catalog](/concepts/unity-catalog.md) and [AI Gateway](/concepts/ai-gateway.md). ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Open Source Support

Databricks fully supports the open-source ML ecosystem. Any open-source ML framework can be used, including scikit-learn, XGBoost, LightGBM, PyTorch, TensorFlow, Hugging Face Transformers, and Ray. MLflow, created by Databricks and used by over 10,000 organizations, is open-source, and experiment tracking data, model artifacts, and pipeline definitions are stored in open formats. Data and AI governance are built upon the open-source [Unity Catalog](/concepts/unity-catalog.md) APIs, and data storage is based on the open [Delta Lake](/concepts/delta-lake.md) format. Feature data and training datasets remain in open, portable files. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
