---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a0f6a7d7538ec3eb8fa82c6832a8db4f6c95d9441fbb87d2d2fe542d065a9f0b
  pageDirectory: concepts
  sources:
    - mlops-stacks-model-development-process-as-code-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pull-request-driven-ml-development
    - PRDMD
    - Git-based ML Development
  citations:
    - file: mlops-stacks-model-development-process-as-code-databricks-on-aws.md
title: Pull Request Driven ML Development
description: Workflow where data scientists file pull requests to update ML code, triggering automated unit tests and integration tests in an isolated staging workspace before merging to main.
tags:
  - mlops
  - version-control
  - collaboration
timestamp: "2026-06-19T19:41:28.177Z"
---

# Pull Request Driven ML Development

**Pull Request Driven ML Development** is a software engineering practice applied to machine learning workflows where model development, testing, and deployment are managed through pull requests (PRs) in a source-controlled repository. This approach treats ML code as a first-class software artifact, enabling systematic review, automated testing, and controlled deployment of model changes.

## Overview

In pull request driven ML development, the entire model development process is implemented, saved, and tracked as code in a source-controlled repository. Automating the process in this way facilitates more repeatable, predictable, and systematic deployments and makes it possible to integrate with CI/CD processes. Representing the model development process as code enables teams to deploy the code instead of deploying the model, which automates the ability to build the model and makes it much easier to retrain when necessary. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Workflow

A typical pull request driven ML workflow follows a structured pipeline across multiple environments:

1. **Development**: Data scientists iterate on ML code in a development workspace, making changes to notebooks, training scripts, and configuration files. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
2. **Pull Request Creation**: Data scientists create pull requests to update ML code. These PRs serve as the mechanism for proposing, reviewing, and approving changes. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
3. **Automated Testing**: PRs trigger unit tests and integration tests in an isolated staging Databricks workspace. This ensures that only tested code progresses through the pipeline. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
4. **Merge to Main**: When a PR is merged to the main branch, model training and batch inference jobs that run in staging immediately update to run the latest code. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
5. **Release to Production**: After merging into main, teams can cut a new release branch as part of a scheduled release process and deploy the code changes to production. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Benefits

Pull request driven ML development provides several advantages over ad-hoc model development:

- **Repeatability**: The entire process is codified, making deployments predictable and systematic. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Code Review**: Changes undergo peer review before deployment, improving code quality and knowledge sharing. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Automated Testing**: CI/CD workflows automatically test changes in isolated environments before they reach production. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Version Control**: All changes are tracked in source control, providing a complete history of model evolution. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Separation of Concerns**: Different ML teams can work independently on a project while following software engineering best practices and maintaining production-grade CI/CD. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Implementation with MLOps Stacks

[MLOps Stacks](/concepts/mlops-stacks.md) provides a structured approach to implementing pull request driven ML development. When you create a project using MLOps Stacks, you define components such as notebooks for feature engineering, training, testing, and deployment, pipelines for training and testing, workspaces for each stage, and CI/CD workflows using GitHub Actions or Azure DevOps for automated testing and deployment. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

The environment created by MLOps Stacks implements the [MLOps workflow recommended by Databricks](/concepts/end-to-end-ml-workflow-on-databricks.md), which is designed around pull request driven development. The default stack includes three components: ML code templates, ML resources defined as code, and CI/CD automation. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Related Concepts

- [MLOps Stacks](/concepts/mlops-stacks.md) — A framework for implementing ML development and deployment as code
- [CI/CD for Machine Learning](/concepts/cicd-for-machine-learning.md) — Continuous integration and deployment practices applied to ML
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) — Source file collections that define end-to-end ML projects
- Model Versioning — Tracking different versions of ML models through source control
- Infrastructure as Code — Managing ML infrastructure through version-controlled definitions
- [Git-based ML Development](/concepts/pull-request-driven-ml-development.md) — Broader practice of using Git workflows for ML projects

## Sources

- mlops-stacks-model-development-process-as-code-databricks-on-aws.md

# Citations

1. [mlops-stacks-model-development-process-as-code-databricks-on-aws.md](/references/mlops-stacks-model-development-process-as-code-databricks-on-aws-ed6ba77e.md)
