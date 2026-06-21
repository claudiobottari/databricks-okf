---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f0d939cec82f60805dbcee5b52f5b47fbfd9d34352b0c4c5f86fc43b9cc7691
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlops-stacks-on-databricks
    - MSOD
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: MLOps Stacks on Databricks
description: Infrastructure-as-code templates on Databricks for automating repeatable ML model promotion from development to production with CI/CD.
tags:
  - mlops
  - devops
  - automation
timestamp: "2026-06-19T14:48:11.476Z"
---

# MLOps Stacks on Databricks

**MLOps Stacks on Databricks** is a set of templates that enables automated, repeatable promotion of machine learning models from development to production using infrastructure-as-code (IaC). ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Overview

MLOps Stacks is part of Databricks’ broader MLOps and governance toolkit. It provides pre-built templates that codify the deployment pipeline, allowing teams to define and manage their ML infrastructure declaratively. By using IaC, MLOps Stacks ensures that the same environment and configuration can be reliably reproduced across stages—from experimentation to staging to production—reducing manual errors and drift. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Features

- **Automated promotion**: Templates define the steps and gates required to move a model version from development through staging to production, enforcing best practices and compliance. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
- **Repeatability**: Because the pipeline is described as code, any team member can replicate the same deployment process, and changes are tracked via version control. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]
- **Integration with Unity Catalog**: MLOps Stacks works in concert with [Unity Catalog](/concepts/unity-catalog.md), [Feature Store](/concepts/feature-store.md), [Model Serving](/concepts/model-serving.md), and other Databricks capabilities to provide end-to-end governance. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Related concepts

- Infrastructure as Code (IaC)
- MLOps
- [MLflow](/concepts/mlflow.md) – for experiment tracking and model registry
- [Unity Catalog](/concepts/unity-catalog.md) – for data and AI governance
- [Model Serving](/concepts/model-serving.md) – for deploying models to production

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
