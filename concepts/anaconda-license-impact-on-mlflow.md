---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7b1b3405afda33088271a1b5f2f5cd945318ff9432ca1d434b513ff136cc0c0
  pageDirectory: concepts
  sources:
    - log-load-and-register-mlflow-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anaconda-license-impact-on-mlflow
    - ALIOM
  citations:
    - file: log-load-and-register-mlflow-models-databricks-on-aws.md
title: Anaconda License Impact on MLflow
description: Changes to Anaconda's terms of service that led Databricks to stop using the defaults channel as default for MLflow models, switching to conda-forge, and implications for models logged before MLflow v1.18.
tags:
  - mlflow
  - licensing
  - anaconda
  - conda
timestamp: "2026-06-19T19:16:37.751Z"
---

# Anaconda License Impact on MLflow

**Anaconda License Impact on MLflow** refers to the changes in how MLflow handles model dependencies following Anaconda Inc.'s updated terms of service, which may require a commercial license for users who rely on Anaconda's packaging and distribution channels.

## Background

Anaconda Inc. updated their [terms of service](https://www.anaconda.com/terms-of-service) for anaconda.org channels. Under the new terms, users may require a commercial license if they rely on Anaconda's packaging and distribution. For more information, see the [Anaconda Commercial Edition FAQ](https://www.anaconda.com/blog/anaconda-commercial-edition-faq). ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Impact on MLflow Model Logging

MLflow models logged before [v1.18](https://mlflow.org/news/2021/06/18/1.18.0-release/index.html) (Databricks Runtime 8.3 ML or earlier) were by default logged with the conda `defaults` channel (`https://repo.anaconda.com/pkgs/`) as a dependency. Because of Anaconda's license change, Databricks stopped using the `defaults` channel for models logged using MLflow v1.18 and above. The default channel is now `conda-forge`, which points at the community-managed [https://conda-forge.org/](https://conda-forge.org/). ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Identifying Affected Models

If you logged a model before MLflow v1.18 without excluding the `defaults` channel from the conda environment, that model may have an unintended dependency on the `defaults` channel. To check whether a model has this dependency, examine the `channel` value in the `conda.yaml` file that is packaged with the logged model. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

An example `conda.yaml` with a `defaults` channel dependency may look like this:

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

## Databricks' Position

Because Databricks cannot determine whether your use of the Anaconda repository to interact with your models is permitted under your relationship with Anaconda, Databricks is not forcing its customers to make any changes. If your use of the Anaconda.com repo through Databricks is permitted under Anaconda's terms, you do not need to take any action. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Remediation

If you want to change the channel used in a model's environment, you can re-register the model to the [MLflow Model Registry](/concepts/mlflow-model-registry.md) with a new `conda.yaml`. You can do this by specifying the channel in the `conda_env` parameter of `log_model()`. ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

For more information on the `log_model()` API, see the MLflow Models documentation for the model flavor you are working with (for example, [log_model for scikit-learn](https://www.mlflow.org/docs/latest/python_api/mlflow.sklearn.html#mlflow.sklearn.log_model)). For more information on `conda.yaml` files, see the [MLflow documentation](https://www.mlflow.org/docs/latest/models.html#additional-logged-files). ^[log-load-and-register-mlflow-models-databricks-on-aws.md]

## Related Concepts

- MLflow Models — Standard format for packaging machine learning models
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Centralized model store for managing model lifecycle
- Conda Environments — Package dependency management for MLflow models
- Conda Forge — Community-managed alternative to Anaconda's defaults channel
- Model Logging Best Practices — How to properly log model dependencies

## Sources

- log-load-and-register-mlflow-models-databricks-on-aws.md

# Citations

1. [log-load-and-register-mlflow-models-databricks-on-aws.md](/references/log-load-and-register-mlflow-models-databricks-on-aws-dc2ad486.md)
