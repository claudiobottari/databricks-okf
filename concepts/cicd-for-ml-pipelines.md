---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8e601ec0a0fdf4cb48f41e6311c37b8ae73a4b395c440c8b6b74782b1548db8
  pageDirectory: concepts
  sources:
    - mlops-stacks-model-development-process-as-code-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cicd-for-ml-pipelines
    - CFMP
    - CI/CD for ML
  citations:
    - file: mlops-stacks-model-development-process-as-code-databricks-on-aws.md
title: CI/CD for ML Pipelines
description: Integration of GitHub Actions or Azure DevOps with MLOps Stacks to automatically test and deploy ML code and resources across workspaces, ensuring only tested code reaches production.
tags:
  - ci-cd
  - mlops
  - automation
timestamp: "2026-06-19T19:41:20.612Z"
---

# CI/CD for ML Pipelines

**CI/CD for ML Pipelines** refers to the practice of applying continuous integration and continuous delivery (CI/CD) principles to machine learning development and deployment. By representing the entire model development process – including feature engineering, training, testing, and deployment – as code in a source-controlled repository, teams can automate testing and deployment of ML pipelines, making releases more repeatable, predictable, and systematic. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## How CI/CD Works for ML Pipelines

On the Databricks platform, CI/CD for ML pipelines is typically implemented using **[MLOps Stacks](/concepts/mlops-stacks.md)**. MLOps Stacks creates a project that defines all components of the ML development and deployment process as code: notebooks for feature engineering, training, testing, and deployment; pipelines for training and testing; Databricks workspaces for each stage (development, staging, production); and CI/CD workflows using GitHub Actions or Azure DevOps for automated testing and deployment. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

The CI/CD runner automatically runs notebooks, creates jobs, and performs other tasks in the staging and production workspaces. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## The CI/CD Pipeline Flow

In a default MLOps Stacks project, the CI/CD pipeline follows this flow:

1. **Development**: Data scientists iterate on ML code in a development workspace. When changes are ready, they create a pull request (PR) against the main branch. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
2. **Automated testing**: The PR automatically triggers unit tests and integration tests in an isolated staging Databricks workspace. Only tested code progresses. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
3. **Merge to main**: When the PR is merged to main, model training and batch inference jobs that run in staging immediately update to use the latest code. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
4. **Release to production**: After a merge to main, a release branch is cut as part of a scheduled release process. Code changes are then deployed to production. This ensures that all production changes are performed through automation and that only tested code reaches production. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Key Components

A CI/CD setup for ML pipelines built with MLOps Stacks includes three core components:

- **ML code as code**: Standardized templates for notebooks (training, batch inference, etc.) that enforce modular, tested structures. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **ML resources as code**: Pipelines, workspaces, and other infrastructure defined using [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md), enabling version control, testing, and optimization of the ML environment. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **CI/CD workflows**: Using GitHub Actions or Azure DevOps to test and deploy both ML code and ML resources, ensuring all production changes go through automated gates. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Benefits

- **Deploy code, not models**: Representing the development process as code means deploying the code automatically rebuilds the model, making retraining much easier. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Repeatability and predictability**: Automation reduces manual errors and makes deployments systematic. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Isolation and testing**: Staging workspace testing before production deployment ensures only validated changes are promoted. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Related Concepts

- [MLOps Stacks](/concepts/mlops-stacks.md)
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md)
- Continuous Integration and Continuous Delivery (CI/CD)
- GitHub Actions
- Azure DevOps
- ML pipeline
- Model retraining
- [Batch inference](/concepts/batch-inference-pipelines.md)
- [Feature engineering](/concepts/featureengineeringclient-api.md)
- Databricks workspaces
- Service principal

## Sources

- mlops-stacks-model-development-process-as-code-databricks-on-aws.md

# Citations

1. [mlops-stacks-model-development-process-as-code-databricks-on-aws.md](/references/mlops-stacks-model-development-process-as-code-databricks-on-aws-ed6ba77e.md)
