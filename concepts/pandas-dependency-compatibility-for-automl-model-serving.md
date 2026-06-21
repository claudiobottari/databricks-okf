---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f389da9add2a196072d0409f567874c99a7d521bc60acfa8595057887d8e1ac8
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pandas-dependency-compatibility-for-automl-model-serving
    - PDCFAMS
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: Pandas Dependency Compatibility for AutoML Model Serving
description: Known pandas version incompatibility error when serving AutoML-built models, resolved by pinning pandas==1.5.3 via a helper script that edits the model's requirements.txt and conda.yaml.
tags:
  - troubleshooting
  - pandas
  - model-serving
timestamp: "2026-06-19T10:37:30.017Z"
---

# Pandas Dependency Compatibility for AutoML Model Serving

**Pandas Dependency Compatibility for AutoML Model Serving** refers to a known incompatibility issue where AutoML-trained models fail during serving due to mismatched pandas versions between the training and serving environments. The error manifests as a missing module import and requires explicitly pinning the pandas version in the model's deployment dependencies.

## The Error

When serving a model built using AutoML with Model Serving, you may encounter the error `No module named 'pandas.core.indexes.numeric'`. This error occurs because of an incompatible pandas version between the AutoML training environment and the model serving endpoint environment.^[classification-with-automl-databricks-on-aws.md]

## Root Cause

AutoML models are trained using a specific version of pandas that is included in the [Databricks Runtime ML](/concepts/databricks-runtime-ml.md). When the model is deployed to a [Model Serving](/concepts/model-serving.md) endpoint, the serving environment may have a different pandas version installed. If the training environment used a newer pandas version that introduced modules not available in the serving environment's older pandas version, the import error occurs.^[classification-with-automl-databricks-on-aws.md]

## Solution

The recommended fix is to run the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py). This script edits the `requirements.txt` and `conda.yaml` files for your logged model to include the appropriate pandas dependency version: `pandas==1.5.3`.^[classification-with-automl-databricks-on-aws.md]

To apply the fix:

1. Modify the script to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md) where your model was logged.
2. Re-register the model to Unity Catalog or the model registry.
3. Try serving the new version of the MLflow model.

After updating the dependencies, the model should be compatible with the serving environment.^[classification-with-automl-databricks-on-aws.md]

## Prevention

To avoid this issue when serving models, ensure that the pandas version specified in the model's environment matches the version available in the [Model Serving](/concepts/model-serving.md) endpoint. Using the script to explicitly pin `pandas==1.5.3` provides a consistent dependency across training and serving environments.^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- [AutoML Classification](/concepts/automl-classification-classify.md) — The primary workflow that generates models affected by this compatibility issue
- [Model Serving](/concepts/model-serving.md) — The deployment target where pandas version mismatches become apparent
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Where models are stored and versioned before serving
- [Unity Catalog](/concepts/unity-catalog.md) — Recommended model registration destination for the latest features
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime environment used for AutoML training that determines the initial pandas version
- [AutoML Forecasting](/concepts/automl-forecast.md) — Another AutoML workflow that may encounter similar dependency issues

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
