---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f19fff6a0c272b430ff6932b56a34e54806562e4da20551296296beff118f394
  pageDirectory: concepts
  sources:
    - express-deployments-for-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-notebook-environments
    - SNE
    - Serverless Notebook
    - Serverless Notebook Notebooks
    - Serverless Notebooks
    - Serverless Notebooks|serverless notebook
    - Serverless notebooks
    - serverless notebook
    - serverless-notebook-environments-databricks
    - SNE(
  citations:
    - file: express-deployments-for-model-serving-endpoints-databricks-on-aws.md
title: Serverless Notebook Environments
description: Databricks compute environments (client versions 3 or 4) required for express model deployments, where model artifacts are packaged during registration.
tags:
  - compute
  - serverless
  - notebooks
timestamp: "2026-06-19T18:46:46.767Z"
---

# Serverless Notebook Environments

**Serverless Notebook Environments** on Databricks provide a fully managed, on-demand compute environment for running notebooks without the need to configure and manage clusters. They are a key component in the [MLflow](/concepts/mlflow.md) model registration and deployment workflow, enabling faster and more consistent serving of custom models. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Overview

Serverless notebook environments eliminate the infrastructure overhead of traditional clusters by automatically provisioning compute resources when a notebook is attached. For model serving, these environments are particularly valuable because they can be packaged and staged during model registration, which accelerates endpoint deployment and ensures the serving environment matches the training environment. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Role in Express Deployments

Express deployments (formerly called serverless optimized deployments) take advantage of packaging and staging model artifacts **in serverless notebook environments** during model registration. This approach results in:

- **Accelerated endpoint deployment** – The model and its environment are pre‑packaged, avoiding the need to build a container at deployment time.
- **Consistent environments** – The serving environment is the same as the training environment, reducing environment‑related errors.

This contrasts with non‑express deployments, where model artifacts and environments are packaged into containers only at deployment time, and the serving environment may not match the training environment. ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Requirements for Express Deployments

To use serverless notebook environments for express deployments, the following conditions must be met:

- The model must be a custom model (not a foundation model API).
- The model must be logged and registered in a **Serverless Notebook** using client version **3 or 4**.
- The model must be logged and registered with `mlflow>=3.1`.
- The model must be registered in [Unity Catalog](/concepts/unity-catalog.md) and served with CPU.
- The model’s maximum environment size must be 1 GB.

^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Configuration

The client version of the serverless environment can be adjusted to meet the requirements for express deployments (see [Configure the serverless environment](https://docs.databricks.com/aws/en/compute/serverless/dependencies)). ^[express-deployments-for-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Express Deployments](/concepts/express-deployments-databricks.md) – The deployment method that leverages serverless notebook environments.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – The infrastructure for serving models in production.
- [MLflow](/concepts/mlflow.md) – The platform for managing the ML lifecycle, including model registration.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Another serverless compute option for GPU workloads.

## Sources

- express-deployments-for-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [express-deployments-for-model-serving-endpoints-databricks-on-aws.md](/references/express-deployments-for-model-serving-endpoints-databricks-on-aws-00f4ae5c.md)
