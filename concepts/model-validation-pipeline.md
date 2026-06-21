---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 945de1547dfcb5da3ade5964bab4f278d23cc183610667d025f7e297b9a5614d
  pageDirectory: concepts
  sources:
    - mlops-workflows-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-validation-pipeline
    - MVP
    - Model Validation
  citations:
    - file: mlops-workflows-on-databricks-databricks-on-aws.md
title: Model Validation Pipeline
description: A structured pipeline that loads a model from Unity Catalog, runs validation checks (format, metadata, performance, compliance), and determines whether a model should proceed to deployment by assigning aliases.
tags:
  - mlops
  - validation
  - pipeline
timestamp: "2026-06-19T19:41:44.508Z"
---

# Model Validation Pipeline

The **Model Validation Pipeline** is a component of the MLOps Workflow that evaluates a trained model against a set of predefined checks before it is allowed to proceed to deployment. It serves as a quality gate between model training and model deployment, ensuring that only models meeting organizational standards are promoted to production. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Overview

The model validation pipeline takes the model URI from the model training pipeline, loads the model from [Unity Catalog](/concepts/unity-catalog.md), and runs a series of validation checks. The primary function of this pipeline is to determine whether a model should proceed to the deployment step. If the model passes pre-deployment checks, it can be assigned the "Challenger" alias in Unity Catalog. If the checks fail, the process ends, and users can be configured to receive notifications of the validation failure. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Validation Checks

Validation checks depend on the organizational context and use case. They can include: ^[mlops-workflows-on-databricks-databricks-on-aws.md]

- **Fundamental checks:** Confirming correct model format and required metadata.
- **Performance evaluations:** Confirming model performance on selected data slices.
- **Compliance checks:** Predefined checks required for highly regulated industries, such as verifying tags, documentation, or other governance requirements.

## Integration with the MLOps Workflow

The model validation pipeline is typically implemented as a task within a multitask Databricks Workflow. The model training task yields a model URI, which is passed to the model validation task using task values. This architecture ensures that the validation step receives the correct model artifact for evaluation. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Development Stage

In the development environment, data scientists develop the model validation pipeline alongside the model training and deployment pipelines. The validation logic is tested iteratively as part of the experimentation process. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Production Stage

In the production environment, the model validation pipeline executes after model training. It loads the model from Unity Catalog using the model URI and runs the configured validation checks. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Outcomes and Tagging

Based on the outcome of the validation checks, the pipeline can use tags to add key-value attributes to the model version. For example, a tag `model_validation_status` could be created with the value set to "PENDING" as the tests execute, and then updated to "PASSED" or "FAILED" when the pipeline is complete. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

If the model successfully passes all validation checks, the "Challenger" alias is assigned to the model version in Unity Catalog. If the model does not pass all validation checks, the process exits and users can be automatically notified. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Visibility and Debugging

Because the model is registered to Unity Catalog, data scientists working in the development environment can load the model version from the production catalog to investigate if the model fails validation. Regardless of the outcome, results are recorded to the registered model in the production catalog using annotations to the model version. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- MLOps Workflow — The overall process for managing ML code, data, and models across development, staging, and production stages.
- Model Training Pipeline — The upstream pipeline that produces the model artifact validated by this pipeline.
- Model Deployment Pipeline — The downstream pipeline that promotes validated models to production.
- [Champion/Challenger Model Strategy](/concepts/championchallenger-model-deployment-strategy.md) — The alias-based approach for comparing and promoting model versions.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where models are registered and aliases are managed.
- Databricks Workflow — The orchestration framework for running multitask pipelines.
- Task Values — The mechanism for passing data between workflow tasks.

## Sources

- mlops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [mlops-workflows-on-databricks-databricks-on-aws.md](/references/mlops-workflows-on-databricks-databricks-on-aws-a1b056b9.md)
