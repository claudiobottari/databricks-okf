---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4ebca9a6449574ca67dd8e92525f37ff046cec6ddb1975ab545645f876f53476
  pageDirectory: concepts
  sources:
    - migrate-to-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - stage-based-model-version-serving
    - SMVS
  citations:
    - file: migrate-to-model-serving-databricks-on-aws.md
title: Stage-based Model Version Serving
description: A migration pattern that creates separate serving endpoints for Staging and Production model versions, aligned with the MLflow model registry stage concept.
tags:
  - model-stages
  - deployment
  - mlflow
timestamp: "2026-06-19T19:35:42.899Z"
---

# Stage-based Model Version Serving

**Stage-based Model Version Serving** is a migration pattern that replicates the behavior of Legacy MLflow Model Serving (where a serving endpoint was automatically created for a model stage such as `Staging` or `Production`). In the new [Model Serving](/concepts/model-serving.md) experience, you explicitly create separate serving endpoints — one per stage — and update each endpoint’s configuration as model versions transition between stages. ^[migrate-to-model-serving-databricks-on-aws.md]

## Motivation

In Legacy MLflow Model Serving, a serving endpoint was tied to the stage of a registered model version (e.g., a version in the `Production` stage was automatically served). After migration to the new Model Serving, that automatic stage-to-endpoint mapping no longer exists. Stage-based model version serving provides a way to preserve the same logical separation by creating dedicated endpoints for each stage (typically `Staging` and `Production`) and manually keeping them in sync with stage transitions. ^[migrate-to-model-serving-databricks-on-aws.md]

## How it works

1. **Create separate endpoints** – For each registered model, create two serving endpoints: one for the `Staging` model version and one for the `Production` model version. For example, for a model named `modelA`, create `modelA-Staging` and `modelA-Production`. ^[migrate-to-model-serving-databricks-on-aws.md]

2. **Configure each endpoint** – In the endpoint configuration, specify the registered model name and the current version that resides in the corresponding stage. Use the `PUT /api/2.0/serving-endpoints/{name}/config` API to set the `entity_version` to the appropriate version number. ^[migrate-to-model-serving-databricks-on-aws.md]

3. **Update endpoints on stage transitions** – When a model version transitions from one stage to another (e.g., version 2 moves from `Staging` to `Production`), update the affected endpoints so that each endpoint still points to the correct version. The `Staging` endpoint would be updated to the new `Staging` version, and the `Production` endpoint would be updated to the newly promoted version. ^[migrate-to-model-serving-databricks-on-aws.md]

## Example workflow

Given a registered model `modelA`:

- Version 1 is in `Production`.
- Version 2 is in `Staging`.

Create two endpoints:

- `modelA-Staging` → serves version 2.
- `modelA-Production` → serves version 1.

When version 2 is promoted to `Production` and version 3 enters `Staging`:

- Update `modelA-Production` to serve version 2.
- Update `modelA-Staging` to serve version 3.

This is done via the `PUT /api/2.0/serving-endpoints/{name}/config` API, specifying the new `entity_version`. ^[migrate-to-model-serving-databricks-on-aws.md]

## API endpoints

- `POST /api/2.0/serving-endpoints` – create a new serving endpoint.
- `PUT /api/2.0/serving-endpoints/{name}/config` – update the configuration of an existing endpoint (used to change the served model version).
- `GET /api/2.0/serving-endpoints/{name}` – check endpoint readiness.
- `POST /serving-endpoints/{name}/invocations` – score a model through the endpoint. ^[migrate-to-model-serving-databricks-on-aws.md]

## Related concepts

- [Model Serving](/concepts/model-serving.md) – The new serverless inference infrastructure on Databricks.
- [Serving Endpoints](/concepts/serving-endpoint-acls.md) – REST API endpoints that host one or more models for inference.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Central repository for managing model versions and stages.
- [Legacy MLflow Model Serving](/concepts/legacy-mlflow-model-serving.md) – The deprecated experience that automatically served models based on stage.
- [Model Serving Migration](/concepts/model-serving-migration.md) – Overall process of moving from legacy to new Model Serving.

## Sources

- migrate-to-model-serving-databricks-on-aws.md

# Citations

1. [migrate-to-model-serving-databricks-on-aws.md](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
