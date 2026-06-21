---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 858d5dd8bd6c6ecf3d448445d2725863b1e7ec92330d88ea7f15948ac15641ed
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anaconda-licensing-implications-for-legacy-mlflow-models
    - ALIFLMM
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Anaconda licensing implications for legacy MLflow models
description: MLflow models logged before v1.18 defaulted to Anaconda's 'defaults' conda channel; Anaconda's updated terms of service may require a commercial license. Affected models can be re-registered with a new conda.yaml specifying 'conda-forge' instead.
tags:
  - licensing
  - mlflow
  - anaconda
  - legacy-models
timestamp: "2026-06-19T18:03:53.576Z"
---

# Anaconda Licensing Implications for Legacy MLflow Models

**Anaconda licensing implications for legacy MLflow models** refers to the potential licensing impact on MLflow models logged before MLflow v1.18 (Databricks Runtime 8.3 ML or earlier) that inadvertently include a dependency on the Anaconda `defaults` channel. Due to a change in Anaconda Inc.'s terms of service, such a dependency may require a commercial license for certain uses.

## Background

Anaconda Inc. updated its [terms of service](https://www.anaconda.com/terms-of-service) for the `anaconda.org` channels. Under the new terms, organizations that rely on Anaconda's packaging and distribution may need a commercial license. See the [Anaconda Commercial Edition FAQ](https://www.anaconda.com/blog/anaconda-commercial-edition-faq) for details. ^[custom-models-overview-databricks-on-aws.md]

## Default Channel Change in MLflow

MLflow models logged before **v1.18** (corresponding to Databricks Runtime 8.3 ML or earlier) were, by default, logged with the conda `defaults` channel (`https://repo.anaconda.com/pkgs/`) as a dependency. Starting with MLflow v1.18, Databricks changed the default channel to `conda-forge` (`https://conda-forge.org/`), a community-managed repository. ^[custom-models-overview-databricks-on-aws.md]

## Identifying Affected Models

A legacy model may inadvertently depend on the `defaults` channel if it was logged without explicitly excluding that channel. To check, examine the `channels` value in the `conda.yaml` file packaged with the logged model. An example `conda.yaml` with a `defaults` dependency looks like:

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

^[custom-models-overview-databricks-on-aws.md]

## Remediation Options

Because Databricks cannot determine whether your use of the Anaconda repository for your models is permitted under your relationship with Anaconda, Databricks does not force any changes. If your use of the `anaconda.com` repo through Databricks is already permitted under Anaconda's terms, no action is needed. ^[custom-models-overview-databricks-on-aws.md]

If you wish to change the channel used in a model's environment, you can re-register the model to the [model registry](/concepts/mlflow-model-registry.md) with a new `conda.yaml`. This is done by specifying the desired channel in the `conda_env` parameter of `log_model()`. ^[custom-models-overview-databricks-on-aws.md]

For more details on the `log_model()` API, refer to the MLflow documentation for the appropriate model flavor (e.g., [log_model for scikit-learn](https://www.mlflow.org/docs/latest/python_api/mlflow.sklearn.html#mlflow.sklearn.log_model)). For information on `conda.yaml` files, see the [MLflow documentation](https://www.mlflow.org/docs/latest/models.html#additional-logged-files). ^[custom-models-overview-databricks-on-aws.md]

## Related Concepts

- MLflow model logging — How models are packaged and logged for deployment.
- Conda environment — The environment specification format used by MLflow.
- [Model registry](/concepts/mlflow-model-registry.md) — Central repository for managing model versions.
- [Custom model serving on Databricks](/concepts/custom-llm-serving-on-databricks.md) — Deployment of custom ML models with Model Serving.
- [Databricks Runtime for ML](/concepts/databricks-runtime-for-ml.md) — The runtime versioning that determines the default MLflow version.

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
