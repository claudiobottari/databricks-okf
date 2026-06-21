---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2bc72fc95723402096f7944dc468cd9bd028fefd8460ef8045eb8066d78fb91f
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-mlops-stacks
    - DMS
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: Databricks MLOps Stacks
description: Templates for enabling automated, repeatable model promotion from development to production using infrastructure-as-code, forming part of Databricks' MLOps and governance suite.
tags:
  - mlops
  - infrastructure-as-code
  - databricks
  - cicd
timestamp: "2026-06-19T09:50:20.494Z"
---

# Databricks MLOps Stacks

**Databricks MLOps Stacks** are infrastructure-as-code templates that enable automated, repeatable promotion of machine learning models from development to production. They provide a standardized framework for implementing MLOps practices on the Databricks platform, helping teams establish consistent deployment pipelines and governance workflows. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Overview

MLOps Stacks are part of Databricks' broader MLOps and governance tooling. They provide pre-built templates that codify best practices for model deployment, including infrastructure definitions, CI/CD pipelines, and environment promotion strategies. By using these stacks, teams can reduce the manual effort required to set up production-grade ML pipelines and ensure consistency across projects. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Key Features

### Infrastructure as Code

MLOps Stacks use infrastructure-as-code principles to define the resources and configurations needed for each stage of the ML lifecycle. This includes compute resources, model serving endpoints, and pipeline definitions, all managed through version-controlled templates. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Automated Promotion

The stacks enable automated, repeatable promotion of models through environments — from development to staging to production. This automation reduces the risk of manual errors and ensures that each promotion follows the same validated process. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Integration with Unity Catalog

MLOps Stacks integrate with [Unity Catalog](/concepts/unity-catalog.md) to provide governance over data, features, models, and endpoints throughout the ML lifecycle. This integration ensures that all ML assets are discoverable, auditable, and governed under a unified access control framework. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Relationship to Other MLOps Tools

MLOps Stacks complement other Databricks MLOps capabilities:

- **[Databricks-Managed MLflow](/concepts/databricks-managed-mlflow.md)** provides experiment tracking and model registry functionality, while MLOps Stacks provide the deployment infrastructure and CI/CD pipelines that operationalize those models.
- **[AI Gateway](/concepts/ai-gateway.md)** manages model serving and governance for production endpoints, which MLOps Stacks help provision and configure.
- **[Model Serving](/concepts/model-serving.md)** endpoints are one of the resources that MLOps Stacks can define and manage through infrastructure-as-code templates.

## Use Cases

- **Standardizing ML deployments** across multiple teams or projects within an organization
- **Enabling CI/CD for ML models** with automated testing and validation gates
- **Establishing governance guardrails** for model promotion and deployment
- **Reducing time to production** by providing reusable, battle-tested deployment templates

## Related Concepts

- MLOps — The broader practice of operationalizing machine learning
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model registry
- [Unity Catalog](/concepts/unity-catalog.md) — Data and AI governance
- [AI Gateway](/concepts/ai-gateway.md) — Model serving and governance
- [Model Serving](/concepts/model-serving.md) — Real-time and batch inference endpoints
- [CI/CD for ML](/concepts/cicd-for-ml-pipelines.md) — Continuous integration and deployment practices for machine learning

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
