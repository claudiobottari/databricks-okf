---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b86372f627634aecb3c9e2e10bf8ef405abbfe665412d8fe66219e99f9dae165
  pageDirectory: concepts
  sources:
    - package-custom-artifacts-for-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-deployment-constraints
    - MSEDC
  citations:
    - file: package-custom-artifacts-for-model-serving-databricks-on-aws.md
title: Model Serving Endpoint Deployment Constraints
description: Databricks Model Serving endpoints require that all model dependencies be statically captured at deployment time; network-based lazy loading and direct Unity Catalog volume access at inference time are not supported for real-time workloads.
tags:
  - model-serving
  - databricks
  - deployment
timestamp: "2026-06-19T19:53:53.138Z"
---

# Model Serving Endpoint Deployment Constraints

**Model Serving Endpoint Deployment Constraints** are the requirements and restrictions that apply when deploying a model to a [Model Serving](/concepts/model-serving.md) endpoint on Databricks. These constraints ensure that all necessary file and artifact dependencies are available during real-time inference at scale.

## Overview

To serve a model reliably and performantly, the dependencies it requires—such as model weights, tokenizer caches, or other files—must be handled according to specific rules. Databricks Model Serving imposes constraints on how these artifacts are packaged and referenced, favoring static capture at deployment time over dynamic downloads. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Requirements

- **MLflow version**: MLflow 1.29 or above is required to package artifacts with models. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Artifact Packaging Constraints

The following constraints govern how artifacts from [Unity Catalog](/concepts/unity-catalog.md) volumes and external sources must be handled:

- **Unity Catalog volume artifacts must be packaged into the model artifact**. Model Serving requires that any artifact stored in a Unity Catalog volume be statically included in the model artifact itself using MLflow interfaces. Referencing volume paths dynamically at inference time is not supported for production-scale real-time workloads. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]
- **Network artifacts should be packaged with the model whenever possible**. While models are sometimes configured to download artifacts from the internet (e.g., HuggingFace tokenizers), real-time workloads at scale perform best when all required dependencies are statically captured at deployment time. Packaging these artifacts avoids network latency and availability issues. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## How to Satisfy the Constraints

Model artifacts and their dependencies can be packaged using the `artifacts` parameter of MLflow’s `log_model()` method. In a [custom MLflow Python model](/concepts/custom-mlflow-pythonmodel.md), the artifacts are made available via the `context.artifacts` dictionary and can be loaded in the standard way for the file type. This approach ensures that the model and all its dependencies are contained within a single deployable artifact. ^[package-custom-artifacts-for-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The platform for deploying models to real-time endpoints.
- Unity Catalog volumes — Storage locations for files that must be packaged into the model.
- [MLflow](/concepts/mlflow.md) — Framework for logging and packaging models and artifacts.
- Custom MLflow models — PyFunc models that can load packaged artifacts during inference.
- Inference optimization — Techniques for achieving low-latency model serving.

## Sources

- package-custom-artifacts-for-model-serving-databricks-on-aws.md

# Citations

1. [package-custom-artifacts-for-model-serving-databricks-on-aws.md](/references/package-custom-artifacts-for-model-serving-databricks-on-aws-e55bf1f8.md)
