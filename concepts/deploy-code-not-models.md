---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 620b203354fc04f8d8f0778e859461885f2807c23223f5837520aba117830478
  pageDirectory: concepts
  sources:
    - mlops-workflows-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deploy-code-not-models
    - DCNM
  citations:
    - file: mlops-workflows-on-databricks-databricks-on-aws.md
title: Deploy Code, Not Models
description: A MLOps principle recommending that during ML development, code (rather than models) should be promoted from one environment to the next, ensuring all code undergoes code review and integration testing.
tags:
  - mlops
  - deployment
  - best-practices
timestamp: "2026-06-19T19:41:38.040Z"
---

# Deploy Code, Not Models

**Deploy Code, Not Models** is a principle in MLOps that recommends promoting code (rather than trained model artifacts) between development, staging, and production environments during the machine learning lifecycle. In most situations, Databricks recommends this approach to ensure that all ML pipeline code undergoes the same [code review](/concepts/custom-review-app-ui.md) and integration testing processes, and that the production version of a model is always trained using production code. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Rationale

Promoting code instead of models enforces consistency across environments. When only the code is moved forward, every environment runs the same training logic, feature engineering steps, and inference pipelines. This guarantees that any model trained in production has been built with code that passed the same quality gates as other software changes. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

In contrast, directly promoting trained model artifacts can bypass code review and testing, potentially introducing subtle differences between environments or deploying models that were trained on different code paths. The “deploy code, not models” principle helps avoid these risks by tying model training to the code that produces it. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## How It Works in Practice

Under this principle, the ML pipeline code – including training, validation, deployment, and monitoring logic – is stored in a version control system (e.g., Git). Changes flow through a standard CI/CD pipeline:

- Development code is reviewed and tested in a staging environment.
- After successful integration tests, the code is merged into a release branch.
- The release branch triggers a production job that trains the model using the merged code and production data.

By keeping the training logic under version control, the resulting model artifact is always traceable to a specific commit. The model itself is then registered in [Unity Catalog](/concepts/unity-catalog.md) with an alias (e.g., “Champion” or “Challenger”) for serving. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Relationship to Model Deployment Patterns

The “deploy code, not models” recommendation is part of a broader discussion of model deployment patterns. For a detailed examination of the trade-offs between promoting code and promoting models, see [Model deployment patterns](/concepts/deploy-models-pattern.md). The choice depends on factors such as regulatory requirements, retraining frequency, and organizational maturity. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- MLOps workflows on Databricks – The overall workflow that includes development, staging, and production stages.
- [Model Serving](/concepts/model-serving.md) – Infrastructure for deploying models as REST APIs; models are referenced by aliases that are updated through the code promotion process.
- [MLflow](/concepts/mlflow.md) – Used to track models and link them to the code and data that produced them.
- [CI/CD for ML](/concepts/cicd-for-ml-pipelines.md) – Continuous integration and delivery pipelines that implement the “deploy code” principle.
- [Unity Catalog](/concepts/unity-catalog.md) – Central governance for models, allowing alias-based deployment that decouples model serving from training code.

## Sources

- mlops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [mlops-workflows-on-databricks-databricks-on-aws.md](/references/mlops-workflows-on-databricks-databricks-on-aws-a1b056b9.md)
