---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: deb90b6ce968668ed1475a68ff956ff5ced09f30ca5e8014fe12a0093d84920a
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
    - mlops-stacks-model-development-process-as-code-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlops-stacks
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
    - file: mlops-stacks-model-development-process-as-code-databricks-on-aws.md
title: MLOps Stacks
description: Infrastructure-as-code templates for automating repeatable ML pipeline promotion from development to production on Databricks.
tags:
  - mlops
  - infrastructure-as-code
  - ci-cd
timestamp: "2026-06-19T18:11:36.000Z"
---

```yaml
---
title: MLOps Stacks
summary: Templates for enabling automated, repeatable promotion of ML models from development to production using infrastructure-as-code practices.
sources:
  - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  - mlops-stacks-model-development-process-as-code-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:36:17.732Z"
updatedAt: "2026-06-18T11:36:17.732Z"
tags:
  - databricks
  - mlops
  - ci-cd
  - infrastructure-as-code
aliases:
  - mlops-stacks
confidence: 1
provenanceState: merged
inferredParagraphs: 0
---

# MLOps Stacks

**MLOps Stacks** is a Databricks framework that implements the machine learning development and deployment process as code in a source-controlled repository. It provides templates for enabling automated, repeatable promotion from development to production using infrastructure-as-code, drawing on the full capabilities of the Databricks Data Intelligence Platform. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md] ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Overview

With MLOps Stacks, the entire model development process is implemented, saved, and tracked as code in a source-controlled repository. Automating the process facilitates more repeatable, predictable, and systematic deployments and makes it possible to integrate with a CI/CD process. Representing the model development process as code enables teams to deploy the code instead of deploying the model — deploying the code automates the ability to build the model, making it much easier to retrain when necessary. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

The environment created by MLOps Stacks implements the MLOps Workflow recommended by Databricks. You can customize the code to create stacks that match your organization's processes or requirements. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## How MLOps Stacks Works

You use the Databricks CLI to create an MLOps Stack. When you initiate a project, the software steps you through entering configuration details and then creates a directory containing the files that compose your project. This directory, or stack, implements the production MLOps workflow recommended by Databricks. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

### Project Components

The default MLOps Stack includes three main components: ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

- **ML code.** MLOps Stacks creates a set of templates for an ML project including notebooks for training, batch inference, and so on. The standardized template allows data scientists to get started quickly, unifies project structure across teams, and enforces modularized code ready for testing.
- **ML resources as code.** MLOps Stacks defines resources such as workspaces and pipelines for tasks like training and batch inference. Resources are defined in [[Declarative Automation Bundles]] to facilitate testing, optimization, and version control for the ML environment.
- **CI/CD.** You can use GitHub Actions or Azure DevOps to test and deploy ML code and resources, ensuring that all production changes are performed through automation and that only tested code is deployed to production.

## MLOps Project Flow

A default MLOps Stacks project includes an ML pipeline with CI/CD workflows to test and deploy automated model training and batch inference jobs across development, staging, and production Databricks workspaces. MLOps Stacks is configurable, so you can modify the project structure to meet your organization's processes. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

In the development workspace, data scientists iterate on ML code and file pull requests (PRs). PRs trigger unit tests and integration tests in an isolated staging Databricks workspace. When a PR is merged to main, model training and batch inference jobs that run in staging immediately update to run the latest code. After you merge a PR into main, you can cut a new release branch as part of your scheduled release process and deploy the code changes to production. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Project Structure

An MLOps Stack uses Declarative Automation Bundles — a collection of source files that serves as the end-to-end definition of a project. These source files include information about how they are to be tested and deployed. Collecting the files as a bundle makes it easy to co-version changes and use software engineering best practices such as source control, code review, testing, and CI/CD. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

When you create a project using MLOps Stacks, you define components such as: ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

- Notebooks for feature engineering, training, testing, and deployment
- Pipelines for training and testing
- Workspaces for each stage (development, staging, production)
- CI/CD workflows using GitHub Actions or Azure DevOps for automated testing and deployment

## Customization

Your organization can use the default stack or customize it as needed to add, remove, or revise components to fit your organization's practices. MLOps Stacks is designed with a modular structure to allow different ML teams to work independently on a project while following software engineering best practices and maintaining production-grade CI/CD. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Benefits

- **Repeatability and predictability.** Automation facilitates more systematic deployments. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **CI/CD integration.** Enables automated testing and deployment pipelines. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Code-based deployment.** Deploying code automates model building, making retraining easier. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Separation of concerns.** Data scientists develop models while ML engineers configure infrastructure. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Related Concepts

- MLOps Workflow — The recommended workflow that MLOps Stacks implements
- [[Declarative Automation Bundles]] — The infrastructure-as-code mechanism used by MLOps Stacks
- [[MLflow]] — The foundation for experiment tracking and model management
- [[Unity Catalog]] — Governance for data, features, models, and endpoints
- [[Model Serving]] — Deploying models as API endpoints
- [[Feature Store]] — Managed features for batch and real-time serving

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md
- mlops-stacks-model-development-process-as-code-databricks-on-aws.md
```

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
2. [mlops-stacks-model-development-process-as-code-databricks-on-aws.md](/references/mlops-stacks-model-development-process-as-code-databricks-on-aws-ed6ba77e.md)
