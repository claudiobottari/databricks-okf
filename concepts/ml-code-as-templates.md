---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6d79b330d3687b78e337241ccb415ec73103d5c2ec197f098939eddb53d58af9
  pageDirectory: concepts
  sources:
    - mlops-stacks-model-development-process-as-code-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ml-code-as-templates
    - MCAT
  citations:
    - file: mlops-stacks-model-development-process-as-code-databricks-on-aws.md
title: ML Code as Templates
description: Standardized notebook templates for ML project components (training, batch inference, testing) created by MLOps Stacks to unify project structure and enforce modularized, test-ready code.
tags:
  - mlops
  - templates
  - databricks
timestamp: "2026-06-19T19:41:16.497Z"
---

# ML Code as Templates

**ML Code as Templates** is a design pattern in [MLOps Stacks](/concepts/mlops-stacks.md) where machine learning code — including notebooks for training, batch inference, and testing — is provided as standardized, reusable templates that can be customized for specific projects. This approach enforces modularized code structure, accelerates data scientist onboarding, and ensures consistency across ML projects within an organization. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Overview

In the MLOps Stacks framework, the entire model development process is implemented, saved, and tracked as code in a source-controlled repository. The ML code component of MLOps Stacks creates a set of templates for an ML project, including notebooks for training, batch inference, and other common tasks. These templates provide a standardized starting point that allows data scientists to get started quickly while unifying project structure across teams. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Benefits

Using ML code as templates offers several advantages:

- **Rapid onboarding**: Data scientists can begin development immediately using a familiar, standardized template structure rather than building project scaffolding from scratch. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Consistency**: Templates enforce a uniform project structure across different teams and projects, making code easier to review, test, and maintain. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Modularity**: The template structure encourages modularized code that is ready for testing and integration into CI/CD pipelines. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Customizability**: Organizations can customize the default templates to add, remove, or revise components to fit their specific practices and requirements. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## How It Works

When a data scientist or ML engineer initializes an MLOps Stacks project using `databricks bundle init mlops-stacks`, the system creates a directory containing template files that implement the production MLOps workflow recommended by Databricks. The templates include notebooks for feature engineering, training, testing, and deployment, along with pipeline definitions and CI/CD workflow configurations. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

The templates are designed with a modular structure that allows different ML teams to work independently on a project while following software engineering best practices. Production engineers can configure ML infrastructure that enables data scientists to develop, test, and deploy ML pipelines and models to production. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Relationship to Deploying Code vs. Deploying Models

Representing the model development process as code enables organizations to deploy the code instead of deploying the model. Deploying the code automates the ability to build the model, making it much easier to retrain the model when necessary. This approach facilitates more repeatable, predictable, and systematic deployments and integrates naturally with CI/CD processes. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Customization

Organizations can customize the default ML code templates to match their processes or requirements. The default stack can be modified to add, remove, or revise components as needed. Customization details are available in the [GitHub repository readme](https://github.com/databricks/mlops-stacks/blob/main/stack-customization.md). ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Related Concepts

- [MLOps Stacks](/concepts/mlops-stacks.md) — The framework that provides ML code as templates
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) — The bundle system used to define and deploy ML resources
- MLOps workflow — The recommended development and deployment process
- [CI/CD for ML](/concepts/cicd-for-ml-pipelines.md) — Automated testing and deployment of ML code
- Source-controlled ML projects — Version control for ML development

## Sources

- mlops-stacks-model-development-process-as-code-databricks-on-aws.md

# Citations

1. [mlops-stacks-model-development-process-as-code-databricks-on-aws.md](/references/mlops-stacks-model-development-process-as-code-databricks-on-aws-ed6ba77e.md)
