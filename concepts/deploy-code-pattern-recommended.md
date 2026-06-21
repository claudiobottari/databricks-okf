---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2ca08ee69f53dad6388b1ef57a91f6aec12523e0b4bfa3c599a27e9c40e5475f
  pageDirectory: concepts
  sources:
    - model-deployment-patterns-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deploy-code-pattern-recommended
    - DCP(
    - Deploy Code Pattern
  citations:
    - file: model-deployment-patterns-databricks-on-aws.md
title: Deploy Code Pattern (recommended)
description: A model deployment pattern where training code is promoted through development, staging, and production environments, and the model is retrained in each environment using that environment's data.
tags:
  - mlops
  - deployment
  - databricks
timestamp: "2026-06-19T19:41:55.200Z"
---

# Deploy Code Pattern (recommended)

The **deploy code pattern** is the recommended approach for moving ML artifacts through staging and into production, as described in the [recommended MLOps workflow](https://docs.databricks.com/aws/en/machine-learning/mlops/mlops-workflow). In this pattern, the code used to train models is developed in the development environment and then promoted unchanged to staging and production environments. The model is trained in each environment: initially in development as part of model development, in staging on a limited subset of data for integration tests, and in production on the full production dataset to produce the final model. ^[model-deployment-patterns-databricks-on-aws.md]

## Advantages

- **Restricted production data access**: In organizations where access to production data is limited, this pattern allows the model to be trained on production data in the production environment. ^[model-deployment-patterns-databricks-on-aws.md]
- **Safer automated retraining**: Because the training code is reviewed, tested, and approved for production, automated model retraining is more reliable. ^[model-deployment-patterns-databricks-on-aws.md]
- **Consistent lifecycle for supporting code**: Pipelines for feature engineering, inference, and monitoring follow the same promotion path as the training code, undergoing integration tests in staging. ^[model-deployment-patterns-databricks-on-aws.md]

## Disadvantages

- **Learning curve**: Data scientists may face a steep learning curve when handing off code to collaborators. Predefined project templates and workflows can mitigate this. ^[model-deployment-patterns-databricks-on-aws.md]

## Data Scientist Responsibilities

In the deploy code pattern, data scientists must be able to review training results from the production environment, as they have the knowledge to identify and fix ML‑specific issues. ^[model-deployment-patterns-databricks-on-aws.md]

## Hybrid Approach

If the model must be trained in staging over the full production dataset, a hybrid approach can be used: deploy code to staging, train the model there, then deploy the model artifact to production. This saves training costs in production but adds an extra operation cost in staging. ^[model-deployment-patterns-databricks-on-aws.md]

## Related Concepts

- MLOps workflow – The recommended end-to-end workflow that incorporates this pattern.
- [Deploy Models Pattern](/concepts/deploy-models-pattern.md) – The alternative pattern where the model artifact is promoted instead of the code.
- Model training in production – How training occurs in the production environment using reviewed code.
- [Unity Catalog](/concepts/unity-catalog.md) – Typically each environment (development, staging, production) corresponds to a catalog.

## Sources

- model-deployment-patterns-databricks-on-aws.md

# Citations

1. [model-deployment-patterns-databricks-on-aws.md](/references/model-deployment-patterns-databricks-on-aws-231ed92b.md)
