---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7e1197c373f16892b6a17bbab3c8d6001e02c4b2a37d869555fde9fa7376240
  pageDirectory: concepts
  sources:
    - how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cicd-for-machine-learning-databricks
    - CFML(
    - Classic Machine Learning on Databricks
    - Machine Learning on Databricks
    - Machine Learning (ML)
  citations:
    - file: how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
title: CI/CD for Machine Learning (Databricks)
description: Automated process for developing, deploying, monitoring, and maintaining ML applications, applied to code, data pipelines, and model artifacts.
tags:
  - mlops
  - ci-cd
  - machine-learning
timestamp: "2026-06-19T10:48:57.311Z"
---

# CI/CD for Machine Learning (Databricks)

**CI/CD for Machine Learning (Databricks)** describes how the Databricks Data Intelligence Platform supports continuous integration and continuous delivery (CI/CD) for machine learning solutions. CI/CD for ML merges practices from MLOps, DataOps, ModelOps, and DevOps to automate the building, testing, and deployment of models, data pipelines, and infrastructure. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Machine Learning Elements That Need CI/CD

A key challenge in ML development is that different teams (data engineers, data scientists, operations) often use different tools and release schedules. Databricks provides a single, unified platform with integrated tools to improve consistency and repeatability. In an automated CI/CD workflow for ML, the following should be tracked:

- Training data, including data quality, schema changes, and distribution changes.
- Input data pipelines.
- Code for training, validating, and serving the model.
- Model predictions and performance.

^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## DataOps: Reliable and Secure Data

Databricks enables DataOps by keeping the entire pipeline—from data ingestion to served model outputs—on a single platform. This unification facilitates productivity, reproducibility, sharing, and troubleshooting. Common DataOps tasks (such as data validation, schema enforcement, and monitoring) are supported by the platform's toolset. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## ModelOps: Model Development and Lifecycle

For model development, Databricks includes [MLflow](/concepts/mlflow.md) for tracking experiments and the [MLflow Model Registry](/concepts/mlflow-model-registry.md) for managing the model lifecycle (staging, serving, artifact storage). After deployment, changes in input data quality or statistical characteristics can affect model performance, so monitoring prediction performance alongside input data is recommended. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## DevOps: Production and Automation

The platform supports production ML workloads with several capabilities:

- **End-to-end data and model lineage** — from production models back to raw data sources.
- **Production-level Model Serving** — automatically scales based on business needs.
- **Jobs** — automates and schedules any workload (ETL, ML) via [Lakeflow Jobs](/concepts/lakeflow-jobs.md).
- **Git folders** — provides Git integration inside the workspace for code versioning and sharing, supporting CI/CD workflows with GitHub Actions, Azure DevOps, or Jenkins.
- **Declarative Automation Bundles** — automates creation and deployment of Databricks resources (jobs, registered models, serving endpoints).
- **Databricks Terraform provider** — automates cross-cloud deployment infrastructure for ML inference jobs, serving endpoints, and featurization jobs.
- **Unity Catalog** — provides fine-grained access control, security policies, and governance for all data and AI assets.

^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

### Model Serving Options

MLflow simplifies deployment to production with one-click deployment as a batch job or as a REST endpoint on an autoscaling cluster. The integration of Databricks Feature Store with MLflow ensures feature consistency between training and serving. Supported deployment options include:

- Code and containers.
- Batch serving.
- Low-latency online serving.
- On-device or edge serving.
- Multi-cloud (e.g., train on one cloud, deploy on another).

^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) — Experiment tracking and model management.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Model lifecycle management.
- [Unity Catalog](/concepts/unity-catalog.md) — Governance and security for data and AI assets.
- [Model Serving](/concepts/model-serving.md) — Deployment options for ML models.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — Automated and scheduled workloads.
- [Git folders](/concepts/databricks-git-folders-for-cicd.md) — Git integration in the Databricks workspace.
- Databricks Bundles — Declarative automation for resources.
- DataOps — Reliable and secure data pipelines.
- ModelOps — Model development and monitoring.

## Sources

- how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md

# Citations

1. [how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md](/references/how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws-48551477.md)
