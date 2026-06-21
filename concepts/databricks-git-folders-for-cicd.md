---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e9c758d5bb7059e620672f68e1b35b0215c3004eb0bb66eaac5b99e21aef2b07
  pageDirectory: concepts
  sources:
    - how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-git-folders-for-cicd
    - DGFFC
    - Databricks Git Folders
    - Databricks Git folders
    - Databricks Git folder
    - Databricks Git folders|Databricks Git folder
    - Databricks Repos (Git Folders)
    - Git folder
    - Git folders
  citations:
    - file: how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
title: Databricks Git Folders for CI/CD
description: Built-in Git integration in the Databricks workspace that enables version control, code sharing, and automated CI/CD workflows via APIs and third-party tools.
tags:
  - version-control
  - ci-cd
  - git
timestamp: "2026-06-19T10:49:11.035Z"
---

# Databricks Git Folders for CI/CD

**Databricks Git Folders** provide Git version control directly within the Databricks workspace, enabling teams to follow software engineering best practices for code versioning and collaboration as part of a CI/CD workflow for machine learning. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Overview

Git folders are a core DevOps tool on the Databricks platform, supporting the automated building, testing, and deployment of ML code. They allow users to perform Git operations (clone, commit, push, pull) through the UI while also exposing APIs that administrators and DevOps engineers can use to integrate with external CI/CD systems. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Key Features

- **UI-based Git operations**: Users can perform common Git actions directly from the workspace interface without leaving Databricks. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- **API-driven automation**: Administrators and DevOps engineers can use the Databricks REST API to automate Git operations, enabling integration with existing CI/CD pipelines. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]
- **Any Git deployment**: Databricks supports any type of Git deployment, including private networks. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Integration with CI/CD Tools

Using Git folders together with the Databricks REST API, teams can build automated deployment processes with popular CI/CD tools such as GitHub Actions, Azure DevOps pipelines, or Jenkins jobs. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

For detailed best practices on setting up CI/CD workflows with Git integration, see the Databricks documentation on [CI/CD workflows with Git integration and Databricks Git folders](/concepts/databricks-git-folders-and-cicd-integration.md) and Use CI/CD. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Role in ML CI/CD

Git folders are one of several DevOps tools that Databricks provides for production and automation. Alongside [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md), [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md), the Databricks Terraform provider, and [Model Serving](/concepts/model-serving.md), Git folders help ensure that code versioning and sharing are integrated into the ML lifecycle from development through deployment. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

By bringing Git version control into the workspace, Git folders enable teams to:
- Track changes to notebooks and code files.
- Collaborate via branches, pull requests, and code review.
- Reproduce experiments from specific code versions.
- Automate testing and deployment of ML pipelines. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) – Model tracking, evaluation, and registry.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) – Automated and scheduled workload execution.
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) – Infrastructure-as-code for Databricks resources.
- Databricks Terraform provider – Cloud infrastructure provisioning.
- [Model Serving](/concepts/model-serving.md) – Deployment of models at scale.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and security for data and AI assets.
- [CI/CD for Machine Learning](/concepts/cicd-for-machine-learning.md) – Broader MLOps practices on Databricks.

## Sources

- how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md

# Citations

1. [how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md](/references/how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws-48551477.md)
