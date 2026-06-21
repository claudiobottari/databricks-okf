---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d9380d389d99d77c3e67563eabf68958734198bf7e7064a5f575f7f60c3fd3e1
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anaconda-licensing-impact-on-legacy-mlflow-models
    - ALIOLMM
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Anaconda Licensing Impact on Legacy MLflow Models
description: MLflow models logged before v1.18 may have an unintended dependency on Anaconda's 'defaults' channel, requiring a commercial license per Anaconda's updated terms of service; affected customers can re-register models with a new conda.yaml.
tags:
  - anaconda
  - licensing
  - mlflow
  - legacy-models
timestamp: "2026-06-19T09:40:33.912Z"
---

# Anaconda Licensing Impact on Legacy MLflow Models

**Anaconda Licensing Impact on Legacy MLflow Models** describes how a change to Anaconda Inc.'s terms of service affects models logged with MLflow v1.17 or earlier (Databricks Runtime 8.3 ML or earlier), and explains the actions customers may need to take for compliance.

## Background

Anaconda Inc. updated their [terms of service](https://www.anaconda.com/terms-of-service) for anaconda.org channels. Under the new terms, users may require a commercial license if they rely on Anaconda's packaging and distribution. Your use of any Anaconda channels is governed by their terms of service. ^[custom-models-overview-databricks-on-aws.md]

## Impact on Legacy MLflow Models

MLflow models logged before v1.18 (Databricks Runtime 8.3 ML or earlier) were by default logged with the conda `defaults` channel (`https://repo.anaconda.com/pkgs/`) as a dependency. Because of this license change, Databricks stopped using the `defaults` channel for models logged with MLflow v1.18 and above. The default channel logged in newer versions is now `conda-forge`, which points at the community-managed `https://conda-forge.org/`. ^[custom-models-overview-databricks-on-aws.md]

If you logged a model before MLflow v1.18 without excluding the `defaults` channel from the conda environment, that model may have an unintended dependency on the `defaults` channel. ^[custom-models-overview-databricks-on-aws.md]

## Identifying Affected Models

To manually confirm whether a model has this dependency, examine the `channel` value in the `conda.yaml` file packaged with the logged model. A model's `conda.yaml` with a `defaults` channel dependency may look like this: ^[custom-models-overview-databricks-on-aws.md]

```yaml
channels:
- defaults
dependencies:
- python=3.8.8
- pip
- pip:
    - mlflow
    - scikit-learn==0.23.2
    - cloudpickle==1.6.0
name: mlflow-env
```

## Recommended Actions

Databricks does not force any changes, as they cannot determine whether your use of the Anaconda repository is permitted under your relationship with Anaconda. If your use of the Anaconda.com repo through Databricks is permitted under Anaconda's terms, no action is needed. ^[custom-models-overview-databricks-on-aws.md]

If you would like to change the channel used in a model's environment, you can re-register the model to the [Model Registry](/concepts/mlflow-model-registry.md) with a new `conda.yaml`. You can do this by specifying the channel in the `conda_env` parameter of `log_model()`. ^[custom-models-overview-databricks-on-aws.md]

## Scope

This notice applies **only** to models logged with MLflow v1.17 or earlier, which corresponds to Databricks Runtime 8.3 ML or earlier. If you are using a newer version, this section can be skipped. ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- [Custom Models on Databricks](/concepts/custom-models-on-databricks.md) — Overview of model serving and deployment
- MLflow Model Logging — Best practices for logging ML models
- [Model Registry](/concepts/mlflow-model-registry.md) — Registering and managing model versions
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — Deploying models to production
- Conda Environment Management — Managing Python environments for MLflow models
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — ML-optimized runtime versions

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
