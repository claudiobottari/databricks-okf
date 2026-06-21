---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 397cebbebd7a50c5c155fb09a53dbf95944c277d5002c0492177a2e8f35661d7
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - registering-and-deploying-automl-forecasting-models
    - Deploying AutoML Forecasting Models and Registering
    - RADAFM
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: Registering and Deploying AutoML Forecasting Models
description: Process to register AutoML-trained forecasting models to Unity Catalog or Model Registry and deploy them to custom model serving endpoints on Databricks.
tags:
  - model-serving
  - deployment
  - databricks
  - automl
timestamp: "2026-06-19T18:53:45.727Z"
---

# Registering and Deploying AutoML Forecasting Models

**Registering and Deploying AutoML Forecasting Models** describes the post‑training workflow for making an AutoML‑generated forecast model available for production use on Databricks. After a forecasting experiment completes, the best model can be registered to a model registry and then deployed to a serving endpoint.

## Overview

AutoML forecasting experiments are run using the classic compute experience on Databricks Runtime 10.0 ML or above. The UI defaults to [serverless forecasting](/concepts/databricks-serverless-forecasting.md), but users can switch to their own compute by selecting **revert back to the old experience**. Once an experiment finishes, the user can register and deploy a model through the AutoML UI. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Registering a Model

1. On the experiment results page, locate the top row showing the best model based on the primary metric.
2. Click the link in the **Models** column for the model you want to register.
3. Click the **register model** button (icon shown in the UI) to register it to [Unity Catalog](/concepts/unity-catalog.md) or the [Model Registry](/concepts/mlflow-model-registry.md).

Databricks recommends registering models to Unity Catalog for access to the latest features. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Deploying a Model

After registration, the model can be deployed to a **custom model serving endpoint**. This is done through the [Model Serving](/concepts/model-serving.md) interface. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Troubleshooting: Pandas Version Mismatch

When serving a model built with AutoML using Model Serving, you may encounter the error:

```
No module named 'pandas.core.indexes.numeric'
```

This is caused by an incompatible pandas version between the AutoML training environment and the serving endpoint. To resolve it:

1. Download the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py).
2. Edit the script to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md) that logged your model.
3. Run the script to update the logged model’s `requirements.txt` and `conda.yaml` to include `pandas==1.5.3`.
4. Re‑register the model to Unity Catalog or the Model Registry.
5. Try serving the new version of the model. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Related Concepts

- [AutoML Forecasting](/concepts/automl-forecast.md) – The automated process of training forecast models.
- [Model Registry](/concepts/mlflow-model-registry.md) – Repository for managing model versions.
- [Unity Catalog](/concepts/unity-catalog.md) – Recommended catalog for model governance.
- [Model Serving](/concepts/model-serving.md) – Infrastructure for serving models as REST endpoints.
- [MLflow](/concepts/mlflow.md) – Underlying experiment tracking and model management.
- [Forecasting Data Preparation](/concepts/automl-forecasting-data-preparation.md) – Settings that influence model quality.
- Forecasting API – Programmatic interface for AutoML forecasting.

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
