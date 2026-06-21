---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e1f33551c8d7489ae7a717f7e1d096fdf96f7e43b1dfeb3af96be5664513c3e1
  pageDirectory: concepts
  sources:
    - mlops-stacks-model-development-process-as-code-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - declarative-automation-bundles
    - DAB
  citations:
    - file: mlops-stacks-model-development-process-as-code-databricks-on-aws.md
    - file: create-and-run-jars-on-serverless-compute-databricks-on-aws.md
title: Declarative Automation Bundles
description: A collection of source files that serves as the end-to-end definition of a Databricks project, including ML resources like workspaces and pipelines defined as code for version control and testing.
tags:
  - databricks
  - infrastructure-as-code
  - mlops
timestamp: "2026-06-19T19:41:17.508Z"
---

# Declarative Automation Bundles

**Declarative Automation Bundles** is a Databricks framework that defines a project's full lifecycle — including source code, configuration, dependencies, and deployment instructions — as a collection of files managed under version control. The bundle serves as the end-to-end definition of a project, making it straightforward to co-version changes, enforce testing, and automate deployments through software engineering best practices such as source control, code review, and CI/CD. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Key Features

- **Template-based project creation.** A bundle can be initialized from a project template that pre-configures correct dependency versions (e.g., Scala, JDK, [Databricks Connect](/concepts/databricks-connect.md)) for the target runtime environment. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]
- **Resource definition as code.** Workspaces, pipelines, and other infrastructure are defined inside the bundle, enabling testing, optimization, and version control of the deployment environment. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]
- **End-to-end lifecycle management.** The bundle captures not only source files but also how they should be tested and deployed, allowing teams to co-version all aspects of a project together. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Using with MLOps Stacks

[MLOps Stacks](/concepts/mlops-stacks.md) uses Declarative Automation Bundles as its core project structure. When a data scientist or ML engineer runs `databricks bundle init mlops-stacks`, a complete project directory is created that implements the [MLOps workflow recommended by Databricks](/concepts/end-to-end-ml-workflow-on-databricks.md). The bundle includes ML code templates (notebooks for training, batch inference, etc.), resource definitions (workspaces, pipelines), and CI/CD workflows (GitHub Actions or Azure DevOps). Resources such as model training and batch inference pipelines are defined in the bundle, which facilitates testing, optimization, and version control of the ML environment. ^[mlops-stacks-model-development-process-as-code-databricks-on-aws.md]

## Using for JAR Deployment

For JAR tasks on [Serverless compute](/concepts/serverless-gpu-compute.md), Databricks strongly recommends Declarative Automation Bundles instead of manually building and deploying JARs. The bundle system automatically provides a template with the correct Scala, JDK, and Databricks Connect versions for the serverless environment, and it enables simple deployment of the compiled JAR to the workspace. This eliminates common version-mismatch errors and simplifies the build-to-deployment pipeline. ^[create-and-run-jars-on-serverless-compute-databricks-on-aws.md]

## Related Concepts

- Databricks CLI — The primary tool for initializing and managing bundles.
- [MLOps Stacks](/concepts/mlops-stacks.md) — A pre-built bundle template for ML development and deployment.
- [Serverless compute](/concepts/serverless-gpu-compute.md) — The target runtime for bundles that deploy JAR tasks.
- [Databricks Connect](/concepts/databricks-connect.md) — The Spark API surface used in serverless JAR bundles.
- CI/CD — Automated testing and deployment workflows defined alongside bundle resources.

## Sources

- create-and-run-jars-on-serverless-compute-databricks-on-aws.md
- mlops-stacks-model-development-process-as-code-databricks-on-aws.md

# Citations

1. [mlops-stacks-model-development-process-as-code-databricks-on-aws.md](/references/mlops-stacks-model-development-process-as-code-databricks-on-aws-ed6ba77e.md)
2. [create-and-run-jars-on-serverless-compute-databricks-on-aws.md](/references/create-and-run-jars-on-serverless-compute-databricks-on-aws-6a1a641b.md)
