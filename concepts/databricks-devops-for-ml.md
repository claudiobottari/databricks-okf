---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b2062cc4cb383aab944f0c1dec500c93930bfe2daa5441dcf5fde34a5f39c89
  pageDirectory: concepts
  sources:
    - how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-devops-for-ml
    - DDFM
  citations:
    - file: how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
title: Databricks DevOps for ML
description: Production and automation capabilities including model serving, Jobs for scheduling, Git folders for version control, and infrastructure-as-code tools like Bundles and Terraform.
tags:
  - devops
  - automation
  - infrastructure
timestamp: "2026-06-19T10:49:00.965Z"
---

# Databricks DevOps for ML

**Databricks DevOps for ML** refers to the set of practices, tools, and platform capabilities that enable continuous integration and continuous delivery (CI/CD) for machine learning solutions on the Databricks Data Intelligence Platform. It brings together techniques from MLOps, DataOps, ModelOps, and DevOps to automate the building, testing, deployment, and monitoring of both code and data assets. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Overview

CI/CD for machine learning extends beyond traditional software CI/CD by also applying automation to data pipelines, input data, training data, and model predictions. Databricks provides a single, unified platform that integrates all components required for the ML lifecycle, including tools for “configuration as code” and “infrastructure as code,” as well as logging and alerting services. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

The following elements should be tracked in an automated CI/CD workflow for ML:

- Training data, including data quality, schema changes, and distribution changes. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- Input data pipelines. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- Code for training, validating, and serving the model. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- Model predictions and performance. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## DataOps: Reliable and Secure Data

Good ML models depend on reliable data pipelines and infrastructure. With Databricks, the entire data pipeline—from data ingestion to model serving outputs—resides on a single platform using the same toolset, which facilitates productivity, reproducibility, sharing, and troubleshooting. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

Databricks provides dedicated tools and workflows for common DataOps tasks, ensuring data quality and schema consistency throughout the lifecycle.

## ModelOps: Model Development and Lifecycle

Model development requires tracking experiments and managing the model lifecycle. The Databricks platform includes [MLflow](/concepts/mlflow.md) for model development tracking and the [MLflow Model Registry](/concepts/mlflow-model-registry.md) to manage staging, serving, and storing model artifacts. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

After a model is released to production, changes in input data or the environment can affect performance. Databricks supports monitoring both prediction performance and input data for changes in quality or statistical characteristics that may necessitate retraining. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

Common ModelOps tasks—such as experiment tracking, model versioning, and transition management—are facilitated by MLflow’s tracking and registry capabilities.

## DevOps: Production and Automation

Databricks supports ML models in production through several key DevOps-oriented features:

- **End-to-end data and model lineage:** From production models back to raw data sources, all on the same platform. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- **Production-level Model Serving:** Automatically scales up or down based on business needs. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- **Jobs:** Automates jobs and creates scheduled ML workflows. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- **Git folders:** Provides code versioning and sharing from the workspace, enabling teams to follow software engineering best practices. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- **Declarative Automation Bundles:** Automates the creation and deployment of Databricks resources, such as jobs, registered models, and serving endpoints. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- **Databricks Terraform provider:** Automates deployment infrastructure across clouds for ML inference jobs, serving endpoints, and featurization jobs. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

### Model Serving

Databricks simplifies model deployment with MLflow, offering single-click deployment as a batch job for large amounts of data or as a REST endpoint on an autoscaling cluster. The integration with the Databricks Feature Store ensures consistency of features for training and serving, and MLflow models can automatically look up features from the Feature Store, even for low latency online serving. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

Supported deployment options include:

- Code and containers. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- Batch serving. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- Low-latency online serving. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- On-device or edge serving. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- Multi‑cloud (e.g., training on one cloud and deploying on another). ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

For more detail, see [Model Serving](/concepts/model-serving.md).

### Jobs

[Lakeflow Jobs](/concepts/lakeflow-jobs.md) enable automation and scheduling of any workload, from ETL to ML. Databricks also supports integrations with popular third‑party orchestrators like Apache Airflow. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

### Git Folders

[Git folders](/concepts/databricks-git-folders-for-cicd.md) provide Git support within the Databricks workspace, allowing teams to perform Git operations through the UI and to use APIs for automation with CI/CD tools. Databricks supports any type of Git deployment, including private networks. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

Best practices for CI/CD with Git integration are documented in [CI/CD workflows with Git integration and Databricks Git folders](/concepts/databricks-git-folders-and-cicd-integration.md). Together with the [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md), teams can build automated deployment processes using GitHub Actions, Azure DevOps pipelines, or Jenkins jobs. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

### Unity Catalog for Governance and Security

[Unity Catalog](/concepts/unity-catalog.md) provides fine‑grained access control, security policies, and governance for all data and AI assets across the platform. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- MLOps
- [CI/CD for Machine Learning](/concepts/cicd-for-machine-learning.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [Feature Store](/concepts/feature-store.md)
- Databricks Bundles

## Sources

- how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md

# Citations

1. [how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md](/references/how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws-48551477.md)
