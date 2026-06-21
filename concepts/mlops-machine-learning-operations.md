---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1ee77f01d3b705dac80468413fdc24776254c4d4ae147cd76b47737e08c869a0
  pageDirectory: concepts
  sources:
    - mlops-workflows-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlops-machine-learning-operations
    - M(LO
    - Machine Learning Pipelines
  citations:
    - file: mlops-workflows-on-databricks-databricks-on-aws.md
title: MLOps (Machine Learning Operations)
description: A set of processes and automated steps for managing code, data, and models to improve performance, stability, and long-term efficiency of ML systems, combining DevOps, DataOps, and ModelOps.
tags:
  - machine-learning
  - mlops
  - workflow
timestamp: "2026-06-19T19:42:45.906Z"
---

# MLOps (Machine Learning Operations)

**MLOps (Machine Learning Operations)** is a set of processes and automated practices for managing code, data, and models throughout the machine learning lifecycle. It combines principles from DevOps, DataOps, and ModelOps to improve the performance, stability, and long-term efficiency of ML systems. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Overview

MLOps extends traditional software operations practices to the unique challenges of machine learning, where assets such as code, data, and models must be developed, tested, and deployed across multiple environments. The Databricks platform enables organizations to manage these assets on a single platform with unified access control, reducing the risks and delays associated with moving data between systems. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## General Recommendations for MLOps

### Create a Separate Environment for Each Stage

An execution environment is the place where models and data are created or consumed by code. Each execution environment consists of compute instances, their runtimes and libraries, and automated jobs. Databricks recommends creating separate environments for the different stages of ML code and model development:

- **Development** – Focused on experimentation and feature development
- **Staging** – Focused on testing and integration verification
- **Production** – Focused on deployment and monitoring

Other configurations can be used to meet specific organizational needs. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Access Control and Versioning

- **Use Git for version control.** Pipelines and code should be stored in Git. Moving ML logic between stages can be interpreted as moving code from the development branch to the staging branch to the release branch. Use [Databricks Git folders](/concepts/databricks-git-folders-for-cicd.md) to integrate with your Git provider. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Store data in a lakehouse architecture using Delta tables.** Both raw data and feature tables should be stored as [Delta tables](/concepts/delta-lake-table.md) with access controls. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Manage model development with MLflow.** Use [MLflow](/concepts/mlflow.md) to track the model development process and save code snapshots, model parameters, metrics, and other metadata. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
- **Use Models in Unity Catalog** to manage model versioning, governance, and deployment status. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Deploy Code, Not Models

In most situations, Databricks recommends promoting *code* rather than *models* from one environment to the next. This approach ensures that all ML code goes through the same code review and integration testing processes, and that the production version of the model is trained on production code. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Recommended MLOps Workflow

The following sections describe a typical MLOps workflow covering three stages: development, staging, and production.

### Development Stage

The focus of the development stage is experimentation. Data scientists develop features and models and run experiments to optimize performance. The output is ML pipeline code that can include feature computation, model training, inference, and monitoring. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

1. **Data sources** – The development environment is represented by the dev catalog in Unity Catalog. Data scientists have read-write access to the dev catalog and ideally read-only access to production data for analysis. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
2. **Exploratory data analysis (EDA)** – Data scientists explore data interactively using notebooks to assess whether available data can solve the business problem. AutoML can accelerate this process by generating baseline models. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
3. **Code** – All pipelines and project files are stored in a development branch of the project repository. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
4. **Train model** – The model training pipeline includes training, tuning, and evaluation. Model parameters, metrics, and artifacts are logged to the MLflow Tracking server. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
5. **Validate and deploy model** – Validation checks confirm format, metadata, and compliance. If successful, the model can be assigned a "Challenger" alias in Unity Catalog. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
6. **Commit code** – Changes are committed into source control. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Staging Stage

The focus of this stage is testing ML pipeline code to ensure production readiness. All code is tested, including feature engineering pipelines, inference code, and monitoring. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

1. **Data** – The staging environment has its own catalog in Unity Catalog for testing. Assets are generally temporary. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
2. **Merge code** – A pull request triggers unit tests. If tests fail, the request is rejected. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
3. **Integration tests** – All pipelines run together to ensure correctness. The staging environment should match production as closely as possible. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
4. **Merge to staging branch** – If tests pass, code is merged into the main branch. Periodic integration tests can be scheduled. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
5. **Create a release branch** – A release branch triggers the CI/CD system to update production jobs. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Production Stage

ML engineers own the production environment where ML pipelines are deployed and executed. These pipelines trigger model training, validate and deploy new model versions, publish predictions, and monitor the process. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

1. **Train model** – Tables from the production catalog are used. Logs are recorded to the production MLflow Tracking server. Model quality is evaluated on held-out production data. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
2. **Validate model** – Validation checks are executed. If successful, the "Challenger" alias is assigned. Results are recorded using annotations. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
3. **Deploy model** – The "Challenger" model is compared to the "Champion" model offline or online. If it performs better, it replaces the "Champion" alias. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
4. **Model Serving** – [Model Serving](/concepts/model-serving.md) endpoints can be configured with multiple models and traffic splits for online comparisons. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
5. **Inference** – Batch or streaming inference reads production data, computes features, and scores the "Champion" model. The inference pipeline automatically uses the updated model version. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
6. **Data profiling** – [Data Profiling](/concepts/data-profiling.md) monitors statistical properties such as data drift and model performance. Metrics are published to tables for analysis and alerts can be configured. ^[mlops-workflows-on-databricks-databricks-on-aws.md]
7. **Retraining** – Scheduled or triggered retraining can be configured. If monitoring metrics indicate issues, SQL alerts can trigger retraining workflows. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- DevOps
- DataOps
- ModelOps
- [LLMOps](/concepts/large-language-models-llms-on-databricks.md)
- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Serving](/concepts/model-serving.md)
- [Data Profiling](/concepts/data-profiling.md)
- CI/CD
- [Feature Store](/concepts/feature-store.md)

## Sources

- mlops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [mlops-workflows-on-databricks-databricks-on-aws.md](/references/mlops-workflows-on-databricks-databricks-on-aws-a1b056b9.md)
