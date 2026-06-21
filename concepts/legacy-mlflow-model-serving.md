---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e1a76f7e0ab7b4bdcdef735d12a02b28916e60657f6ff275089744c5af15a2d
  pageDirectory: concepts
  sources:
    - migrate-to-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - legacy-mlflow-model-serving
    - LMMS
    - MLflow Model Serving
    - served MLflow models
  citations:
    - file: migrate-to-model-serving-databricks-on-aws.md
      start: 10
      end: 11
    - file: migrate-to-model-serving-databricks-on-aws.md
      start: 14
      end: 17
    - file: migrate-to-model-serving-databricks-on-aws.md
      start: 20
      end: 21
    - file: migrate-to-model-serving-databricks-on-aws.md
      start: 22
      end: 23
    - file: migrate-to-model-serving-databricks-on-aws.md
      start: 24
      end: 25
    - file: migrate-to-model-serving-databricks-on-aws.md
      start: 26
      end: 27
    - file: migrate-to-model-serving-databricks-on-aws.md
      start: 29
      end: 34
    - file: migrate-to-model-serving-databricks-on-aws.md
      start: 38
      end: 50
    - file: migrate-to-model-serving-databricks-on-aws.md
      start: 53
      end: 105
title: Legacy MLflow Model Serving
description: The older MLflow-based model serving experience on Databricks that reaches end of life on September 15, 2025, with new endpoint creation blocked after August 22, 2025.
tags:
  - model-serving
  - databricks
  - mlflow
  - deprecated
timestamp: "2026-06-19T19:35:25.816Z"
---

# Legacy MLflow Model Serving

**Legacy MLflow Model Serving** is the previous generation of Databricks’ model serving infrastructure, built on MLflow and separate from the current [Model Serving](/concepts/model-serving.md) experience that is backed by serverless compute. It is scheduled for retirement: starting **August 22, 2025**, customers will no longer be able to create new serving endpoints using Legacy MLflow Model Serving, and on **September 15, 2025**, the legacy experience will reach end of life and all existing endpoints can no longer be used.^[migrate-to-model-serving-databricks-on-aws.md#L10-L11]

## Requirements

To use Legacy MLflow Model Serving (or to migrate away from it), the following prerequisites apply:

- A registered model in the [MLflow Model Registry](/concepts/mlflow-model-registry.md).
- Appropriate permissions on registered models, as described in the serving endpoints access control guide.
- Serverless compute must be enabled on the workspace.^[migrate-to-model-serving-databricks-on-aws.md#L14-L17]

## Significant Changes Compared to Model Serving

The new Model Serving experience introduces several differences from the legacy offering:

- The request format and response format are slightly different. See Scoring a Model Endpoint for the new format protocol.^[migrate-to-model-serving-databricks-on-aws.md#L20-L21]
- The endpoint URL includes `serving-endpoints` instead of `model`.^[migrate-to-model-serving-databricks-on-aws.md#L22-L23]
- Model Serving provides full support for managing resources with API Workflows.^[migrate-to-model-serving-databricks-on-aws.md#L24-L25]
- Model Serving is production-ready and backed by the Databricks SLA.^[migrate-to-model-serving-databricks-on-aws.md#L26-L27]

## Identifying Legacy Endpoints

To find which serving endpoints still use Legacy MLflow Model Serving:

1. Go to the **Models** UI in the workspace.
2. Select the **Workspace Model Registry** filter.
3. Select the **Legacy serving enabled only** filter.

This shows only the models that have legacy serving enabled.^[migrate-to-model-serving-databricks-on-aws.md#L29-L34]

## Migration from Legacy MLflow Model Serving to Model Serving

Migrating involves creating a new Model Serving endpoint and transitioning workflows without disrupting the legacy endpoint until the switch is complete. The general UI-based steps are:

1. Register the model to [Unity Catalog](/concepts/unity-catalog.md).
2. Navigate to **Serving endpoints** on the sidebar of the machine learning workspace.
3. Follow the workflow in [Create Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) to create a serving endpoint with the model.
4. Update the application to use the new URL (with `serving-endpoints`) and the new scoring format.
5. Once transitioned, go to **Models** on the sidebar, select the model, and on the **Serving** tab select **Stop**.
6. Confirm the stop action.^[migrate-to-model-serving-databricks-on-aws.md#L38-L50]

If the model was deployed using the stage-based approach (model versions tied to `Staging` and `Production` stages), the migration can replicate that behavior by creating two separate endpoints:

- One endpoint (e.g., `modelA-Staging`) serving the model version in the `Staging` stage.
- Another endpoint (e.g., `modelA-Production`) serving the version in the `Production` stage.

These endpoints are created and updated via the Serving Endpoints API. Example requests for creation and configuration updates are shown in the migration guide.^[migrate-to-model-serving-databricks-on-aws.md#L53-L105]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The current serverless-based serving experience.
- [Unity Catalog](/concepts/unity-catalog.md) — Required for registering models during migration.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Where models are stored and staged.
- [Serving Endpoints](/concepts/serving-endpoint-acls.md) — The infrastructure that hosts models for inference.
- Serverless Compute — Compute model required to run Model Serving.
- Scoring a Model Endpoint — The new request/response format.
- [Create Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — Instructions for creating endpoints.
- API Workflows — Used to manage serving endpoints programmatically.

## Sources

- migrate-to-model-serving-databricks-on-aws.md

# Citations

1. [migrate-to-model-serving-databricks-on-aws.md:10-11](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
2. [migrate-to-model-serving-databricks-on-aws.md:14-17](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
3. [migrate-to-model-serving-databricks-on-aws.md:20-21](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
4. [migrate-to-model-serving-databricks-on-aws.md:22-23](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
5. [migrate-to-model-serving-databricks-on-aws.md:24-25](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
6. [migrate-to-model-serving-databricks-on-aws.md:26-27](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
7. [migrate-to-model-serving-databricks-on-aws.md:29-34](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
8. [migrate-to-model-serving-databricks-on-aws.md:38-50](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
9. [migrate-to-model-serving-databricks-on-aws.md:53-105](/references/migrate-to-model-serving-databricks-on-aws-7f642342.md)
