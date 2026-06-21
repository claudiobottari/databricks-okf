---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0c3d73e045b3aee91d0e1757d45cb2edb7f3d4f174eaaf92b6497fd1853abf82
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pandas-version-compatibility-for-automl-model-serving
    - PVCFAMS
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: Pandas Version Compatibility for AutoML Model Serving
description: Known issue where mismatched pandas versions between AutoML training and model serving endpoints cause 'No module named pandas.core.indexes.numeric' error, resolved by pinning pandas==1.5.3.
tags:
  - troubleshooting
  - model-serving
  - pandas
  - databricks
timestamp: "2026-06-19T18:53:57.702Z"
---

# Pandas Version Compatibility for AutoML Model Serving

**Pandas Version Compatibility for AutoML Model Serving** refers to a known incompatibility between the `pandas` library version used during AutoML model training and the version available in the model serving endpoint environment. This mismatch causes the error `No module named 'pandas.core.indexes.numeric'` when serving the model. The issue can be resolved by explicitly pinning a compatible `pandas` version in the model’s deployment artifacts.

## Error: `No module named 'pandas.core.indexes.numeric'`

When serving a model built using AutoML with Model Serving, the following error may occur:

```
No module named 'pandas.core.indexes.numeric'
```

This error is caused by an incompatible `pandas` version between the AutoML training environment and the model serving endpoint environment. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Root Cause

AutoML trains models in a Databricks cluster with a specific `pandas` version (typically 1.5.3). The model serving endpoint, however, may run a different `pandas` version. When the model tries to load or use `pandas` internals that were present during training but are missing or renamed in the serving environment, the import fails with the `No module named 'pandas.core.indexes.numeric'` error. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Resolution

The error can be resolved by running the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py). This script edits the `requirements.txt` and `conda.yaml` files in the logged MLflow model to include the appropriate `pandas` dependency version: `pandas==1.5.3`. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Steps to Fix

1. **Modify the script** to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md) where your model was logged. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
2. **Re-register the model** to [Unity Catalog](/concepts/unity-catalog.md) or the [Model Registry](/concepts/mlflow-model-registry.md). ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
3. **Try serving the new version** of the MLflow model. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

The script ensures that the serving environment installs `pandas==1.5.3`, matching the version used during AutoML training.

## Best Practices

- **Pin dependencies explicitly** – Always specify the exact `pandas` version (or other critical libraries) in your model’s `requirements.txt` and `conda.yaml` to avoid version mismatches between training and serving. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- **Test after re-registration** – After applying the script and re-registering, deploy the new model version to a serving endpoint to confirm the issue is resolved. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- **Monitor version changes** – When upgrading [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) or the `pandas` library, verify serving compatibility before deploying models to production. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Related Concepts

- AutoML – Automated machine learning on Databricks.
- [Model Serving](/concepts/model-serving.md) – Infrastructure for deploying and serving ML models.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Version management for registered models.
- [Unity Catalog](/concepts/unity-catalog.md) – Centralized governance for ML assets.
- Pandas (library) – Python data manipulation library.
- [Model Serving Endpoint Configuration](/concepts/model-serving-endpoint-configuration-api.md) – Environment setup for serving endpoints.

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
