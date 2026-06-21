---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6520f24680aa3107ed7d23d4152ace576e7e0a85dfbb96615d8000d0463992fb
  pageDirectory: concepts
  sources:
    - mlops-workflows-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - three-stage-mlops-environment-architecture
    - TMEA
  citations:
    - file: mlops-workflows-on-databricks-databricks-on-aws.md
title: Three-Stage MLOps Environment Architecture
description: The recommended practice of creating separate execution environments (Development, Staging, Production) for ML code and model development with clearly defined transitions between stages.
tags:
  - mlops
  - architecture
  - environments
timestamp: "2026-06-19T19:41:41.103Z"
---

## Three-Stage MLOps Environment Architecture

The **Three-Stage MLOps Environment Architecture** is a recommended approach for managing the lifecycle of machine learning models on the Databricks platform. It separates ML assets—code, data, and models—into **development**, **staging**, and **production** stages, each with its own execution environment, access controls, and Unity Catalog namespace. This structure enforces rigorous testing and governance before code reaches production. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Overview

Each execution environment consists of compute instances, runtimes, libraries, and automated jobs. Databricks recommends creating dedicated environments for each stage with clearly defined transitions. The three-stage pattern uses the common names: **Development**, **Staging**, and **Production**. Other configurations can be tailored to an organization’s needs. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

Key principles that underpin the architecture include:

- **Version control with Git** – Pipelines and code are stored in Git; moving logic between stages corresponds to moving code from the dev branch to the main branch to a release branch. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Data in a lakehouse** – Raw data and feature tables are stored as Delta tables in the cloud, with access controls for each environment. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Model management with MLflow** – Model development, parameters, metrics, and artifacts are tracked via MLflow. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Models in Unity Catalog** – Model versioning, governance, and deployment status are managed through Unity Catalog. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Deploy code, not models** – Promoting code (rather than model artifacts) ensures that all project code passes through the same review and integration testing, and that the production model is trained on production code. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Development Stage

The development stage focuses on **experimentation**. Data scientists explore data, develop features, train and tune models, and run evaluations—all within the **dev catalog** of Unity Catalog. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

Typical activities include:

- **Exploratory data analysis (EDA)** – Interactive notebook sessions to assess data quality and potential. AutoML can accelerate baseline model generation. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Model training and evaluation** – The training pipeline logs parameters, metrics, and artifacts to the MLflow Tracking server. After hyperparameter tuning and evaluation on held-out data, the final model artifact is registered in the dev catalog. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Model validation and deployment** – Separate validation pipelines run pre-deployment checks (e.g., format, metadata, compliance). If checks pass, the model can be assigned the “Challenger” alias. The deployment pipeline may promote a “Champion” alias or set up comparison infrastructure. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Code commit** – Data scientists commit changes to a development branch in Git. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

Data scientists in development ideally have read-only access to production data (prod catalog) to compare model performance and analyze predictions. If that is not possible, a snapshot of production data can be written to the dev catalog. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Staging Stage

The staging stage is the **testing environment**. ML engineers run CI (continuous integration) pipelines that validate all ML pipeline code—including feature engineering, model training, inference, and monitoring—to ensure it is ready for production. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

The workflow typically follows these steps:

1. **Pull request** – A developer creates a pull request against the main branch.
2. **Unit tests (CI)** – The PR automatically triggers unit tests. Failures block the merge.
3. **Integration tests (CI)** – All pipelines are run together in the staging environment, which should mirror production as closely as possible. For real-time serving, a temporary serving endpoint may be created and tested. To reduce cost or time, tests can use smaller data subsets or fewer training iterations.
4. **Merge to main** – If all tests pass, the code is merged into the main branch.
5. **Create release branch** – An ML engineer creates a release branch, which triggers the CI/CD system to update production jobs. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

The staging environment has its own catalog in Unity Catalog (often called “staging”). Assets here are generally temporary and retained only until testing is complete. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Production Stage

The production stage is the **live environment** owned by ML engineers. Pipelines here are executed with governed data, models are validated and deployed, inference is served, and monitoring ensures system health. Data scientists typically have read-only access to production assets for visibility. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

Key components of the production stage:

- **Model training** – Triggered by code changes or scheduled retraining. Production training uses limited hyperparameter tuning, logs to the production MLflow Tracking server, and registers the model in the **prod catalog** of Unity Catalog. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Model validation** – The model is loaded from Unity Catalog and checked against a series of validation gates (format, performance on slices, compliance). Passing models receive the “Challenger” alias; records and notifications are created for failures. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Model deployment** – The “Challenger” model is compared to the existing “Champion” model (offline or online A/B tests). If it outperforms, the “Champion” alias is reassigned. For real-time serving, a Model Serving endpoint is created or updated with zero-downtime. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Inference** – Batch or streaming pipelines read the “Champion” model and score new data. Predictions are written to production tables, flat files, or message queues. Model Serving endpoints serve real-time requests, automatically looking up features from online stores. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Data profiling and monitoring** – Data profiling monitors statistical properties (data drift, model accuracy, infrastructure metrics). Alerts and dashboards are set up, and retraining may be triggered automatically when metrics degrade. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Retraining** – Begins with scheduled periodic retraining and can evolve to event-driven retraining based on monitoring alerts. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## General Recommendations

- **Separate environments** – Use distinct Unity Catalog catalogs (dev, staging, prod) and workspaces or isolated resources for each stage. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Access control** – Grant appropriate read/write permissions per stage. Data scientists write to dev, have read-only access to prod. ML engineers own production compute. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Version everything** – Code in Git, data in Delta tables, models in MLflow and Unity Catalog. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Automate transitions** – Use CI/CD pipelines (Databricks workflows, Git actions) to promote code between stages. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- MLOps
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow](/concepts/mlflow.md)
- [Delta Tables](/concepts/delta-lake-table.md)
- Git Version Control
- [CI/CD for Machine Learning](/concepts/cicd-for-machine-learning.md)
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md)
- Data Profiling and Monitoring
- [Feature Store](/concepts/feature-store.md)
- Model Validation and Deployment Patterns

## Sources

- mlops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [mlops-workflows-on-databricks-databricks-on-aws.md](/references/mlops-workflows-on-databricks-databricks-on-aws-a1b056b9.md)
