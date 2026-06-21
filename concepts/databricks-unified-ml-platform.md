---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d407ad593e68ffadc34fa0ed3fba6a448a9549a413e00ea057490abc9755fe3f
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-unified-ml-platform
    - DUMP
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Databricks Unified ML Platform
description: A single, integrated platform covering the full data science and machine learning lifecycle from raw data ingestion through feature engineering, model training, deployment, and production monitoring.
tags:
  - databricks
  - machine-learning
  - platform
timestamp: "2026-06-18T11:36:04.275Z"
---

# Databricks Unified ML Platform

The **Databricks Unified ML Platform** is an integrated environment that covers the full data science and machine learning lifecycle — from raw data ingestion through feature engineering, model training, deployment, and production monitoring. It combines open-source frameworks with enterprise-grade governance, observability, and operational tooling, collectively referred to as MLOps.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Exploratory Data Analysis

Databricks simplifies exploratory data analysis (EDA) with interactive, collaborative, and AI-assisted tools. Data scientists can explore data using natural language chat, user interfaces, or code, and collaborate through real-time co-editing and Git-based code sharing. [Genie Code](/concepts/genie-code.md) provides fully automated EDA or acts as an interactive assistant.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Prepare and Serve Features

Data and ML workloads are unified under [Unity Catalog](/concepts/unity-catalog.md) with fine-grained access controls, allowing teams to adjust data engineering and ML boundaries as needed. Data can be prepared using any data engineering tool, such as [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md). Features are managed in a [Feature Store](/concepts/feature-store.md) for both batch and real-time serving, providing a single, governed source of truth. Genie Code accelerates data discovery and preparation by browsing Unity Catalog, suggesting transformations, and generating code for ingestion and feature pipelines.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Train ML Models

The platform offers flexible training environments for ML and deep learning models. Pre-configured and customizable environments support custom libraries, and serverless CPU/GPU compute enables scaling on demand. [Genie Code](/concepts/genie-code.md) provides intelligent AutoML, taking natural language requests to build full multi-notebook workflows for featurization, training, tuning, evaluation, and deployment.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Track and Manage Experiments

[Databricks-Managed MLflow](/concepts/databricks-managed-mlflow.md) forms the foundation for reproducible, auditable ML development. Its integration with Unity Catalog and Git provides full lineage: each model version in the registry links back to the training run, dataset, environment, and git commit that produced it, delivering a complete audit trail for any deployed model.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Deploy and Serve Models

Databricks supports both [batch inference](/concepts/batch-inference-on-databricks.md) and [real-time model serving](/concepts/model-serving.md). Batch inference applies models efficiently to large datasets, while real-time serving exposes models as low-latency API endpoints. Genie Code can generate deployment code and diagnose issues for model serving endpoints.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Evaluate and Monitor

Flexible evaluation tools support training-time assessment, and continuous monitoring is available for production deployments. Real-time serving logs to [Inference Tables](/concepts/inference-tables.md) governed in Unity Catalog, and [Data Quality Monitoring](/concepts/data-quality-monitoring.md) provides custom metrics, dashboards, and alerts.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## MLOps and Governance

The platform provides a full MLOps suite. [MLOps Stacks](/concepts/mlops-stacks.md) offers templates for automated, repeatable promotion from development to production using infrastructure-as-code. All data, features, models, and endpoints are governed by Unity Catalog and [AI Gateway](/concepts/ai-gateway.md).^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Open Source Support

Databricks fully supports the open-source ML ecosystem. Any open-source framework can be used — scikit-learn, XGBoost, PyTorch, TensorFlow, Hugging Face, Ray, and more. [MLflow](/concepts/mlflow.md) is open-source and stores experiment data, model artifacts, and pipeline definitions in open formats. [Unity Catalog](/concepts/unity-catalog.md) and [Delta Lake](/concepts/delta-lake.md) are also open-source, ensuring data portability and freedom from vendor lock-in.^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Summary

The Databricks Unified ML Platform integrates all stages of the ML lifecycle into a single, governed environment. It leverages open standards and provides enterprise-grade tooling for collaboration, automation, and observability, enabling teams to move from experimentation to production reliably and at scale.

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
