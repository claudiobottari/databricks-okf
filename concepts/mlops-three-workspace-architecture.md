---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d61062b3a6e8444f8ed0520d4f80e615eaf845006c0f0a65bd1bb2ca397e5828
  pageDirectory: concepts
  sources:
    - mlops-stacks-model-development-process-as-code-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlops-three-workspace-architecture
    - MTA
  citations:
    - file: mlops-stacks-model-development-process-as-code-databricks-on-aws.md
title: MLOps Three-Workspace Architecture
description: The recommended Databricks MLOps pattern using separate development, staging, and production Databricks workspaces to isolate model development, testing, and production deployment.
tags:
  - mlops
  - architecture
  - databricks
timestamp: "2026-06-19T19:41:17.950Z"
---

## MLOps Three-Workspace Architecture

**MLOps Three-Workspace Architecture** is the default environment structure created by [MLOps Stacks](/concepts/mlops-stacks.md) on Databricks. It separates the model development and deployment lifecycle into three distinct Databricks workspaces: **development**, **staging**, and **production**. This architecture enforces isolation between iterative experimentation, automated testing, and production serving, enabling repeatable, predictable, and systematic deployments. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

The three-workspace architecture is a core component of the MLOps workflow recommended by Databricks. It is implemented through [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md), which define resources such as workspaces, pipelines, and jobs as code, facilitating version control and CI/CD integration. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

### Development workspace

Data scientists and ML engineers develop models on the Databricks platform or on their local system within the development workspace. They iterate on ML code, including notebooks for feature engineering, training, testing, and deployment. Changes are submitted through pull requests, which trigger the CI/CD pipeline. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

### Staging workspace

When a pull request is created, automated unit tests and integration tests run in an isolated staging workspace. This workspace mirrors the production environment and validates that the code changes work correctly before they are promoted. After a pull request is merged into the main branch, model training and batch inference jobs in staging automatically update to run the latest code, providing a pre-production validation step. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

### Production workspace

After code is merged into main, a new release branch can be created as part of a scheduled release process. The release branch deploys the code changes to the production workspace, where automated model training and batch inference jobs execute using the tested and validated code. All production changes are performed through automation, ensuring that only tested code reaches production. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

### Benefits of the three-workspace architecture

- **Separation of concerns** – Different teams (data scientists, ML engineers) work independently across environments while following software engineering best practices. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **CI/CD integration** – Pull requests trigger testing in staging, and merges to main or release branches deploy to production, ensuring that all production changes are automated and tested. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Reproducibility** – Because the development process is represented as code in a source-controlled repository, the model can be rebuilt automatically, making retraining straightforward. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **Environment consistency** – Resources such as workspaces and pipelines are defined in Declarative Automation Bundles, allowing instance types and configurations to be version-controlled and tested across stages. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

### Related concepts

- [MLOps Stacks](/concepts/mlops-stacks.md) – The framework that implements the three-workspace architecture.
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) – The mechanism for defining resources as code.
- CI/CD – Continuous integration and delivery pipelines for testing and deployment.
- [Model Training](/concepts/databricks-model-training.md) – Automated job that runs in each workspace.
- Batch Inference – Automated job that runs in staging and production.
- [Databricks Workspace](/concepts/databricks-workspace-feature-store-ui.md) – The isolated environment for each stage.

### Sources

- mlops-stacks-model-development-process-as-code-databricks-on-aws.md

# Citations

1. [mlops-stacks-model-development-process-as-code-databricks-on-aws.md](/references/mlops-stacks-model-development-process-as-code-databricks-on-aws-ed6ba77e.md)
