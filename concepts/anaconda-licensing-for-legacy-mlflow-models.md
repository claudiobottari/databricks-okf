---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf2017459881dfb1c9c8af2225bb4b9a90bc53822c1c14d36af52c94c7ec1d81
  pageDirectory: concepts
  sources:
    - custom-models-overview-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anaconda-licensing-for-legacy-mlflow-models
    - ALFLMM
  citations:
    - file: custom-models-overview-databricks-on-aws.md
title: Anaconda Licensing for Legacy MLflow Models
description: Notice that MLflow models logged before v1.18 (Databricks Runtime 8.3 ML or earlier) may have a dependency on the Anaconda 'defaults' channel, which now requires a commercial license; newer models default to the community-managed 'conda-forge' channel.
tags:
  - licensing
  - mlflow
  - anaconda
  - compliance
timestamp: "2026-06-19T14:40:08.527Z"
---

# Anaconda Licensing for Legacy MLflow Models

**Anaconda Licensing for Legacy MLflow Models** refers to the licensing considerations and required actions for MLflow models logged with MLflow v1.17 or earlier (Databricks Runtime 8.3 ML or earlier). These legacy models were logged with the conda `defaults` channel as a dependency, which may require a commercial license under Anaconda Inc.'s updated terms of service. ^[custom-models-overview-databricks-on-aws.md]

## Background

Anaconda Inc. updated their terms of service for anaconda.org channels. Under the new terms, organizations may require a commercial license if they rely on Anaconda's packaging and distribution. Use of any Anaconda channels is governed by their terms of service. ^[custom-models-overview-databricks-on-aws.md]

MLflow models logged before [v1.18](https://mlflow.org/news/2021/06/18/1.18.0-release/index.html) (Databricks Runtime 8.3 ML or earlier) were logged by default with the conda `defaults` channel (`https://repo.anaconda.com/pkgs/`) as a dependency. Because of this license change, Databricks stopped using the `defaults` channel for models logged with MLflow v1.18 and above. The default channel for newer models is now `conda-forge`, which points to the community-managed `https://conda-forge.org/`. ^[custom-models-overview-databricks-on-aws.md]

## Identifying Affected Models

If you logged a model before MLflow v1.18 without explicitly excluding the `defaults` channel from the conda environment, that model may have an unintended dependency on the `defaults` channel. To confirm whether a model has this dependency, examine the `channels` value in the `conda.yaml` file packaged with the logged model. ^[custom-models-overview-databricks-on-aws.md]

A model's `conda.yaml` with a `defaults` channel dependency may look like this:

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

## Required Actions

Databricks cannot determine whether your use of the Anaconda repository to interact with your models is permitted under your relationship with Anaconda. If your use of the Anaconda.com repo through Databricks is permitted under Anaconda's terms, you do not need to take any action. ^[custom-models-overview-databricks-on-aws.md]

If you need to change the channel used in a model's environment, you can re-register the model to the [model registry](/concepts/mlflow-model-registry.md) with a new `conda.yaml`. Specify the channel using the `conda_env` parameter of the `log_model()` API. ^[custom-models-overview-databricks-on-aws.md]

### Changing the Channel

For more information on the `log_model()` API, consult the MLflow documentation for the specific model flavor being used — for example, `log_model` for scikit-learn. For more information on `conda.yaml` files, see the [MLflow documentation](https://www.mlflow.org/docs/latest/models.html#additional-logged-files). ^[custom-models-overview-databricks-on-aws.md]

## Sources

- custom-models-overview-databricks-on-aws.md

# Citations

1. [custom-models-overview-databricks-on-aws.md](/references/custom-models-overview-databricks-on-aws-920e65c5.md)
