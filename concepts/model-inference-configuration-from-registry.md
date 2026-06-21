---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a5ffcb8e709320f6fdeb659f71799fe6066be2d5f8ad3825d7faf763c26c9de
  pageDirectory: concepts
  sources:
    - manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-inference-configuration-from-registry
    - MICFR
  citations:
    - file: manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md
title: Model Inference Configuration from Registry
description: Capability to configure batch, streaming (via Lakeflow Spark Declarative Pipelines), and real-time inference (via Model Serving) directly from registered models in the Workspace Model Registry.
tags:
  - inference
  - model-serving
  - databricks
  - mlflow
timestamp: "2026-06-19T19:25:35.713Z"
---

# Model Inference Configuration from Registry

**Model Inference Configuration from Registry** refers to the process of setting up and configuring inference workflows—batch, streaming, or real-time—for models registered in the [Workspace Model Registry (legacy)](/concepts/workspace-model-registry.md). After a model is registered, the registry provides tools to automatically generate notebooks for batch or streaming inference, or to create endpoints for real-time serving via [Model Serving](/concepts/model-serving.md).

## Overview

Once a model is registered in the Workspace Model Registry, you can configure inference directly from the registry UI. The **Configure model inference** dialog allows you to select the model version, specify input data sources, and define output locations for predictions. The generated notebooks are saved in your user folder under dedicated directories for each inference type. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Batch Inference

To configure batch inference, navigate to the registered model page or model version page and click the **Use model for inference** button. In the dialog, select the **Batch inference** tab. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

1. From the **Model version** drop-down, select the version to use. The first two items are the current Production and Staging versions (if they exist). Selecting one of these options means the notebook automatically uses that stage's version at runtime, so you do not need to update the notebook as the model evolves. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]
2. Click **Browse** next to **Input table** to select the input data table. For Unity Catalog-enabled workspaces, the dialog allows selection from three levels: `<catalog-name>.<database-name>.<table-name>`. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]
3. Predictions are saved by default to `dbfs:/FileStore/batch-inference` in a folder named after the model. Each run writes a new file with a timestamp appended. You can change the output folder or choose to overwrite files. To save predictions to a Unity Catalog location, you must edit the generated notebook. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

The generated notebook is saved in your user folder under `Batch-Inference/<model-name>`. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Streaming Inference (Lakeflow Spark Declarative Pipelines)

To configure streaming inference, select the **Streaming (Lakeflow Spark Declarative Pipelines)** tab in the Configure model inference dialog. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

1. Select the model version from the drop-down, with the same Production/Staging shortcut as batch inference. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]
2. Browse and select the input table. The generated notebook creates a data transform that uses the input table as a source and integrates the MLflow PySpark inference UDF to perform model predictions. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]
3. Provide the output Lakeflow Spark Declarative Pipelines name. The notebook creates a live table with that name to store predictions. You can customize the target dataset—for example, define a streaming live table, add schema information, or add data quality constraints. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]
4. You can then create a new pipeline with this notebook or add it to an existing pipeline as an additional notebook library. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

The generated notebook is saved in your user folder under `DLT-Inference/<model-name>`. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Real-Time Inference

For real-time inference, the registry provides a link to [Model Serving](/concepts/model-serving.md), which exposes MLflow models as scalable REST API endpoints. To create a serving endpoint, see the documentation on creating custom model serving endpoints. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Anaconda Environment Considerations

MLflow models logged before v1.18 (Databricks Runtime 8.3 ML or earlier) were logged with the conda `defaults` channel as a dependency. Due to Anaconda's updated terms of service, models logged with MLflow v1.18 and above use the `conda-forge` channel by default. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

If a model has an unintended `defaults` channel dependency, you can re-register the model with a new `conda.yaml` by specifying the channel in the `conda_env` parameter of `log_model()`. ^[manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md]

## Related Concepts

- [Workspace Model Registry (legacy)](/concepts/workspace-model-registry.md) — The registry that stores and manages model versions.
- [Model Serving](/concepts/model-serving.md) — Real-time inference via REST API endpoints.
- [MLflow experiments](/concepts/mlflow-experiment.md) — The tracking component that logs model runs.
- [Batch inference](/concepts/batch-inference-pipelines.md) — Offline scoring of large datasets.
- Streaming inference — Continuous scoring of streaming data.
- [Model version stages](/concepts/model-versioning-and-stage-transitions.md) — Staging, Production, and Archived stages for model lifecycle management.

## Sources

- manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md

# Citations

1. [manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws.md](/references/manage-model-lifecycle-using-the-workspace-model-registry-legacy-databricks-on-aws-666e92b6.md)
