---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6beba308e4cc1d863a48b6a513f5683165cc379eb609df981933847c8d501d88
  pageDirectory: concepts
  sources:
    - how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - devops-for-ml-on-databricks
    - DFMOD
    - CI/CD for Databricks
    - DevOps on Databricks
  citations:
    - file: how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
title: DevOps for ML on Databricks
description: Production and automation practices including model serving, jobs orchestration, Git folders, declarative automation bundles, and Terraform infrastructure-as-code.
tags:
  - devops
  - infrastructure
  - databricks
timestamp: "2026-06-19T19:06:56.840Z"
---

# DevOps for ML on Databricks

**DevOps for ML on Databricks** refers to the automation of production-level operations for machine learning workflows, including deployment, monitoring, scaling, and governance. It is part of the broader [CI/CD for Machine Learning](/concepts/cicd-for-machine-learning.md) practice that combines MLOps, DataOps, ModelOps, and DevOps principles on a unified platform. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Production and Automation

The Databricks platform provides several key capabilities to support ML models in production:

- End-to-end data and model lineage, from models in production back to the raw data source, on the same platform.
- Production-level [Model Serving](/concepts/model-serving.md) that automatically scales up or down based on business needs.
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) for automating and scheduling machine learning workflows.
- [Git folders](/concepts/databricks-git-folders-for-cicd.md) for code versioning and sharing from the workspace, following software engineering best practices.
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) to automate the creation and deployment of Databricks resources such as jobs, registered models, and serving endpoints.
- The Databricks Terraform provider to automate deployment infrastructure across clouds for ML inference jobs, serving endpoints, and featurization jobs.

^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Model Serving

For deploying models to production, [MLflow](/concepts/mlflow.md) simplifies the process by providing single-click deployment as a batch job or as a REST endpoint on an autoscaling cluster. The integration of Databricks [Feature Store](/concepts/feature-store.md) with MLflow ensures consistency of features for training and serving; MLflow models can automatically look up features from the Feature Store, even for low-latency online serving. Supported deployment options include code and containers, batch serving, low-latency online serving, on-device or edge serving, and multi‑cloud scenarios (e.g., training on one cloud and deploying on another). ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Jobs

[Lakeflow Jobs](/concepts/lakeflow-jobs.md) allow you to automate and schedule any type of workload, from ETL to machine learning. Databricks also supports integrations with popular third‑party orchestrators like Apache Airflow. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Git Folders

Databricks includes Git support in the workspace to help teams follow software engineering best practices by performing Git operations through the UI. Administrators and DevOps engineers can use APIs to set up automation with their favorite CI/CD tools. Databricks supports any type of Git deployment, including private networks. Best practices for code development using Git folders are described in the documentation on CI/CD workflows with Git integration. These techniques, together with the [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md), enable building automated deployment processes with GitHub Actions, Azure DevOps pipelines, or Jenkins jobs. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Unity Catalog for Governance and Security

The Databricks platform includes [Unity Catalog](/concepts/unity-catalog.md), which lets administrators set up fine‑grained access control, security policies, and governance for all data and AI assets across Databricks. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Integration into CI/CD Processes

DevOps for ML on Databricks is designed to integrate with existing CI/CD pipelines. The platform incorporates all components required for the ML lifecycle, including tools to build “configuration as code” to ensure reproducibility and “infrastructure as code” to automate cloud service provisioning. Logging and alerting services are also available to help detect and troubleshoot problems when they occur. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Sources

- how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md

# Citations

1. [how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md](/references/how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws-48551477.md)
