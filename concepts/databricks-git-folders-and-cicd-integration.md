---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a4d1815c8f644137af7b2703ca9d9fc2c7dad2df833ef265318e6dcd1d8be07
  pageDirectory: concepts
  sources:
    - how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-git-folders-and-cicd-integration
    - CI/CD Integration and Databricks Git Folders
    - DGFACI
    - CI/CD workflows with Git integration and Databricks Git folders
  citations:
    - file: how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
title: Databricks Git Folders and CI/CD Integration
description: Git integration in the Databricks workspace enabling version control, code sharing, and automated CI/CD pipelines with tools like GitHub Actions and Jenkins.
tags:
  - devops
  - version-control
  - databricks
timestamp: "2026-06-19T19:06:46.693Z"
---

# Databricks Git Folders and CI/CD Integration

**Databricks Git Folders** (often referred to as "repos") provide native Git version control within the Databricks workspace. They allow teams to perform Git operations – such as commit, push, pull, and branch management – directly through the UI, enabling software engineering best practices for code development on the platform. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## DevOps and Automation

Git folders are a key component of Databricks’ DevOps support. They enable code versioning and sharing from the workspace, which helps teams follow software engineering best practices. Administrators and DevOps engineers can use the Databricks APIs to set up automation with their preferred CI/CD tools. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

Databricks supports any type of Git deployment, including private networks, making it possible to integrate with existing version control infrastructure. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Integration with CI/CD Pipelines

The combination of Git folders, the Databricks REST API, and popular CI/CD tools allows teams to build automated deployment processes. For example, teams can set up pipelines using:

- **GitHub Actions**
- **Azure DevOps pipelines**
- **Jenkins jobs**

These integrations automate the building, testing, and deployment of notebooks, code, and other Databricks artifacts (such as jobs, registered models, and serving endpoints) when changes are pushed to a Git branch. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- [Databricks Git Folders](/concepts/databricks-git-folders-for-cicd.md) – The core feature for Git integration in the workspace.
- [MLflow](/concepts/mlflow.md) – Used for experiment tracking, model registry, and deployment.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) – [Lakeflow Jobs](/concepts/lakeflow-jobs.md) for automating and scheduling workloads.
- [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) – Enables programmatic interaction with the platform.
- [CI/CD for Machine Learning](/concepts/cicd-for-machine-learning.md) – Broader MLOps practices on Databricks.
- MLOps – Lifecycle management for ML models, including CI/CD.
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) – Another automation tool for deploying Databricks resources.

## Sources

- how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md

# Citations

1. [how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md](/references/how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws-48551477.md)
