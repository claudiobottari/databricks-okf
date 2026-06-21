---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6e3c3a9a43fc07cae2e0722c9efdd72957186272c055c6bcae6891a80b21e238
  pageDirectory: concepts
  sources:
    - mlops-stacks-model-development-process-as-code-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deploying-code-instead-of-models
    - DCIOM
  citations:
    - file: mlops-stacks-model-development-process-as-code-databricks-on-aws.md
title: Deploying Code Instead of Models
description: The MLOps Stacks philosophy of deploying the code that builds the model rather than the model artifact itself, simplifying retraining by automating model construction from source.
tags:
  - mlops
  - deployment
  - philosophy
timestamp: "2026-06-19T19:41:26.435Z"
---

# Deploying Code Instead of Models

**Deploying Code Instead of Models** is a principle in MLOps where the entire model development process — including feature engineering, training, testing, and deployment logic — is implemented, saved, and tracked as code in a source-controlled repository. Instead of packaging and deploying a serialized model artifact directly, the code that builds the model is deployed, and the model is constructed during the deployment or retraining process. This approach is core to [MLOps Stacks](/concepts/mlops-stacks.md) on Databricks. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Overview

With MLOps Stacks, the model development process is represented as code. Automating the process in this way facilitates more repeatable, predictable, and systematic deployments and makes it possible to integrate with your CI/CD pipeline (e.g., GitHub Actions or Azure DevOps). Representing the model development process as code enables you to deploy the code instead of deploying the model. Deploying the code automates the ability to build the model, making it much easier to retrain the model when necessary. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## How It Works in MLOps Stacks

When a project is created using MLOps Stacks, the software defines components such as notebooks for feature engineering, training, testing, and deployment, pipelines for training and testing, workspaces for each stage, and CI/CD workflows. The environment implements the recommended MLOps workflow from Databricks. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

The default stack includes three main components:

- **ML code** – Standardised templates (notebooks) for training, batch inference, etc.
- **ML resources as code** – Resources like workspaces and pipelines are defined in [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) to facilitate testing, optimisation, and version control.
- **CI/CD** – GitHub Actions or Azure DevOps test and deploy ML code and resources, ensuring that only tested code reaches production. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

The project flow works as follows:

1. Data scientists develop models in a development workspace and file pull requests (PRs).
2. PRs trigger unit tests and integration tests in an isolated staging workspace.
3. When a PR is merged to the main branch, model training and batch inference jobs in staging immediately update to run the latest code.
4. After merging to main, a release branch is cut as part of the scheduled release process, and the code changes are deployed to production. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

Because the entire pipeline is defined in version-controlled code, deploying the code automatically rebuilds the model, making retraining a natural part of the deployment process.

## Benefits

- **Reproducibility** – Every model version is tied to a specific commit of training code, configuration, and data references.
- **Automated retraining** – Since the code builds the model, retraining can be triggered automatically on a schedule or by changes in data or code.
- **Systematic deployments** – CI/CD pipelines enforce testing and validation before code reaches production.
- **Collaboration** – Multiple teams (data scientists, ML engineers) can work independently using the same modular, version-controlled project structure. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Related Concepts

- [MLOps Stacks](/concepts/mlops-stacks.md) – The tool that implements the "code instead of models" approach on Databricks.
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) – Resource definitions that co-version ML code and infrastructure.
- [CI/CD for ML](/concepts/cicd-for-ml-pipelines.md) – Continuous integration and deployment pipelines for machine learning.
- Model Retraining – The process of rebuilding a model, made easier by deploying code.
- Version Control for ML – Managing ML code, configurations, and experiments in source control.

## Sources

- mlops-stacks-model-development-process-as-code-databricks-on-aws.md

# Citations

1. [mlops-stacks-model-development-process-as-code-databricks-on-aws.md](/references/mlops-stacks-model-development-process-as-code-databricks-on-aws-ed6ba77e.md)
