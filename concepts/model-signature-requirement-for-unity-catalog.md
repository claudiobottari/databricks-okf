---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 68a17290f27eef1852e3dee4b318306b289f47e203e342123532a3978ed347d8
  pageDirectory: concepts
  sources:
    - migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-signature-requirement-for-unity-catalog
    - MSRFUC
  citations:
    - file: migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md
title: Model signature requirement for Unity Catalog
description: Models registered in Unity Catalog require a signature; if none exists, the MLFLOW_SKIP_SIGNATURE_CHECK_FOR_UC_REGISTRY_MIGRATION environment variable (MLflow ≥3.4.0) can bypass the requirement during migration.
tags:
  - mlflow
  - model-registry
  - validation
timestamp: "2026-06-19T19:35:55.297Z"
---

# Model Signature Requirement for Unity Catalog

**Model Signature Requirement for Unity Catalog** refers to the mandatory condition that MLflow models registered in [Unity Catalog](/concepts/unity-catalog.md) must include a model signature. This requirement applies when copying model versions from the [Workspace Model Registry](/concepts/workspace-model-registry.md) to Unity Catalog using the `copy_model_version()` API.

## Overview

Models in Unity Catalog require a model signature to be registered. When migrating model versions from the Workspace Model Registry to Unity Catalog, if the source model version does not have a signature, the migration will fail unless a specific workaround is applied. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Migration Behavior

When using `copy_model_version()` with MLflow client version 3.4.0 or above, the API checks whether the source model version has a signature. If the workspace model version lacks a signature, Databricks recommends creating one by following the instructions in the [MLflow documentation on model signatures](https://mlflow.org/docs/latest/ml/model/signatures/). ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Workaround: Skipping the Signature Check

As an alternative to adding a signature, you can use the environment variable `MLFLOW_SKIP_SIGNATURE_CHECK_FOR_UC_REGISTRY_MIGRATION`. This environment variable is only available when using `copy_model_version()` and requires MLflow version 3.4.0 or above. When this environment variable is set to `"true"`, a signature is not required for the migration. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Best Practices

Databricks recommends that you add a signature to your model rather than relying on the environment variable workaround. Model signatures provide important metadata about the expected input and output schema of the model, which improves governance, discoverability, and interoperability within Unity Catalog. ^[migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance and metadata layer for Databricks assets
- [Workspace Model Registry](/concepts/workspace-model-registry.md) — The legacy model registry that does not require signatures
- [Model Signature](/concepts/model-signatures-in-unity-catalog.md) — MLflow metadata defining model input and output schema
- Migrate models to Unity Catalog — The overall migration process
- copy_model_version() — The API used to copy model versions between registries

## Sources

- migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md

# Citations

1. [migrate-workflows-and-models-to-unity-catalog-databricks-on-aws.md](/references/migrate-workflows-and-models-to-unity-catalog-databricks-on-aws-ef30b915.md)
