---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: acc895dbd8d6aaaa51f295b30d965e68f42b57872db043c18786e1d4c6a759df
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - model-registration-and-deployment-from-automl
    - Deployment from AutoML and Model Registration
    - MRADFA
  citations:
    - file: classification-with-automl-databricks-on-aws.md
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: Model Registration and Deployment from AutoML
description: Process of registering the best AutoML model to Unity Catalog or Model Registry and deploying it to a custom model serving endpoint on Databricks.
tags:
  - automl
  - model-serving
  - deployment
  - databricks
timestamp: "2026-06-19T14:12:17.448Z"
---

# Model Registration and Deployment from AutoML

**Model Registration and Deployment from AutoML** refers to the workflow of taking the best-performing model from an AutoML experiment and making it available for production inference through [MLflow Model Registry](/concepts/mlflow-model-registry.md) and [Databricks Model Serving](/concepts/databricks-model-serving.md).

## Overview

After an AutoML experiment completes, users can register and deploy the best model directly from the AutoML UI. The top row of the runs table displays the best model based on the chosen primary evaluation metric. From there, users can register the model to either [Unity Catalog](/concepts/unity-catalog.md) or the [Model Registry](/concepts/mlflow-model-registry.md), and subsequently deploy it to a custom model serving endpoint.^[classification-with-automl-databricks-on-aws.md, forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Registering a Model

To register a model from the AutoML results:

1. Select the link in the **Models** column for the model you want to register.
2. Use the register model button to register the model to Unity Catalog or the Model Registry.

Databricks recommends registering models to Unity Catalog for the latest features.^[classification-with-automl-databricks-on-aws.md, forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Deploying a Model

After registration, you can deploy the model to a custom model serving endpoint. This makes the model available for real-time inference through the [Databricks Model Serving](/concepts/databricks-model-serving.md) infrastructure.^[classification-with-automl-databricks-on-aws.md, forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Known Issues

### Pandas Version Incompatibility

When serving a model built using AutoML with Model Serving, you may encounter the error:

```
No module named 'pandas.core.indexes.numeric'
```

This error is due to an incompatible `pandas` version between AutoML and the model serving endpoint environment. To resolve it, run the `add-pandas-dependency.py` script, which edits the `requirements.txt` and `conda.yaml` files for your logged model to include the appropriate `pandas` dependency version: `pandas==1.5.3`.^[classification-with-automl-databricks-on-aws.md, forecasting-with-automl-classic-compute-databricks-on-aws.md]

The resolution steps are:

1. Modify the script to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md) where your model was logged.
2. Re-register the model to Unity Catalog or the model registry.
3. Try serving the new version of the MLflow model.

^[classification-with-automl-databricks-on-aws.md, forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Related Concepts

- AutoML — Automated machine learning for finding the best model
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Model versioning and lifecycle management
- [Unity Catalog](/concepts/unity-catalog.md) — Recommended catalog for model registration
- [Databricks Model Serving](/concepts/databricks-model-serving.md) — Infrastructure for deploying models to endpoints
- Classification with AutoML — AutoML workflow for classification problems
- Forecasting with AutoML — AutoML workflow for time-series forecasting
- Regression with AutoML — AutoML workflow for regression problems

## Sources

- classification-with-automl-databricks-on-aws.md
- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
2. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
