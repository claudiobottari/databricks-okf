---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: abdf6af96cb1e9875acba34692e4f174be9bd3be7eead7a0139c1a6621a9515e
  pageDirectory: concepts
  sources:
    - mlflow-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - logged-models
  citations:
    - file: mlflow-on-databricks-databricks-on-aws.md
title: Logged Models
description: A concept in MLflow 3 that tracks a model's progress throughout its lifecycle by persisting metadata, metrics, parameters, and artifacts across environments and runs for comparison and debugging.
tags:
  - mlflow-3
  - model-lifecycle
  - tracking
timestamp: "2026-06-19T19:39:02.594Z"
---

# Logged Models

**Logged Models** are a core concept in [MLflow 3](/concepts/mlflow-3.md) that provide a persistent, lifecycle-wide representation of a model throughout its development and deployment stages. A `LoggedModel` is created automatically whenever a model is logged using `log_model()`, and it persists across different environments, experiments, and runs. ^[mlflow-on-databricks-databricks-on-aws.md]

## Overview

When you log a model with MLflow, a `LoggedModel` is created that remains available throughout the model's entire lifecycle. This logged model contains links to all associated artifacts, including metadata, metrics, parameters, and the code used to generate the model. Unlike a run-specific record, a Logged Model persists beyond individual runs and provides a unified view of the model's evolution. ^[mlflow-on-databricks-databricks-on-aws.md]

## Purpose and Benefits

Logged Models help you track a model's progress across different stages of development. By maintaining a persistent record, you can:

- Compare multiple models against each other to identify the most performant version
- Find the best-performing model across different experiments and runs
- Track down information during debugging by accessing historical artifacts, metrics, and parameters
- Maintain continuity when moving between development, evaluation, and production environments

^[mlflow-on-databricks-databricks-on-aws.md]

## Relationship to Other MLflow Concepts

Logged Models work alongside Deployment Jobs in MLflow 3 to provide comprehensive model lifecycle management. While Logged Models focus on tracking and comparing model versions, Deployment Jobs handle the operational aspects of the lifecycle, including steps like evaluation, approval, and deployment. Both concepts are governed by [Unity Catalog](/concepts/unity-catalog.md), with all events saved to an activity log accessible on the model version page. ^[mlflow-on-databricks-databricks-on-aws.md]

## Use Cases

### Model Comparison and Selection
Use Logged Models to compare different versions of a model across various runs. The persistent link to metrics and parameters allows you to objectively evaluate which version performs best for your use case. ^[mlflow-on-databricks-databricks-on-aws.md]

### Debugging and Troubleshooting
When issues arise in production, Logged Models provide a trail of artifacts, metadata, and parameters that can help identify when and why a model's behavior changed. ^[mlflow-on-databricks-databricks-on-aws.md]

### Lifecycle Tracking
As a model moves from development through evaluation to production, Logged Models maintain a continuous record, making it easier to understand the full history and context of any given model version. ^[mlflow-on-databricks-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational units for tracking work during model development
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Centralized repository for managing model deployment
- [Model Serving](/concepts/model-serving.md) — Deployment of models as REST API endpoints
- [MLflow 3 Installation and Setup](/concepts/mlflow-3-installation.md) — Getting started with the MLflow 3 environment

## Sources

- mlflow-on-databricks-databricks-on-aws.md

# Citations

1. [mlflow-on-databricks-databricks-on-aws.md](/references/mlflow-on-databricks-databricks-on-aws-bc75dc1f.md)
