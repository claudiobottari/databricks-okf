---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38344d9601b110729ab02ca4b67dc44f7fa2861e11ee77d037f03857cead3ac7
  pageDirectory: concepts
  sources:
    - regression-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pandas-compatibility-issue-with-automl-model-serving
    - PCIWAMS
  citations:
    - file: regression-with-automl-databricks-on-aws.md
title: Pandas Compatibility Issue with AutoML Model Serving
description: Common error and resolution for pandas version incompatibility when serving AutoML models with Databricks Model Serving
tags:
  - automl
  - troubleshooting
  - pandas
  - model-serving
timestamp: "2026-06-19T20:13:07.128Z"
---

# Pandas Compatibility Issue with AutoML Model Serving

The **Pandas Compatibility Issue with AutoML Model Serving** is a known incompatibility between the `pandas` library version used during AutoML model training and the version used by [Model Serving](/concepts/model-serving.md) endpoints on Databricks. This mismatch causes a `ModuleNotFoundError` when attempting to serve a model built with AutoML.

## Error Message

When serving a model trained with AutoML, the following error may occur:

```
No module named 'pandas.core.indexes.numeric'
```

^[regression-with-automl-databricks-on-aws.md]

## Cause

The error is due to an incompatible `pandas` version between the AutoML training environment and the model serving endpoint environment. The specific `pandas` version used to log the model during AutoML training is not compatible with the version available on the serving endpoint. ^[regression-with-automl-databricks-on-aws.md]

## Resolution

To resolve this error, add the correct `pandas` dependency to the model's environment specification. The recommended approach is to run the `add-pandas-dependency.py` script, which edits the `requirements.txt` and `conda.yaml` files for the logged model to include the appropriate `pandas` version: `pandas==1.5.3`. ^[regression-with-automl-databricks-on-aws.md]

### Steps to Fix

1. **Modify the script** to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md) where your model was logged.
2. **Re-register the model** to [Unity Catalog](/concepts/unity-catalog.md) or the [Model Registry](/concepts/mlflow-model-registry.md).
3. **Serve the new version** of the MLflow model at the serving endpoint.

^[regression-with-automl-databricks-on-aws.md]

## Related Concepts

- AutoML — Automated machine learning for regression, classification, and forecasting
- [Model Serving](/concepts/model-serving.md) — Infrastructure for deploying models to endpoints
- [MLflow](/concepts/mlflow.md) — Platform for managing the machine learning lifecycle
- [Unity Catalog](/concepts/unity-catalog.md) — Recommended model registry for latest features
- [Model Registry](/concepts/mlflow-model-registry.md) — Legacy model registry for managing model versions

## Sources

- regression-with-automl-databricks-on-aws.md

# Citations

1. [regression-with-automl-databricks-on-aws.md](/references/regression-with-automl-databricks-on-aws-cc5aa3d0.md)
