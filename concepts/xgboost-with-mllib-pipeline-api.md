---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a4c2ffd3ed6cd9d0103a44d0aa534caa652ed83d552b16c99165e7585e142752
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - xgboost-with-mllib-pipeline-api
    - XWMPA
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: XGBoost with MLlib Pipeline API
description: Embedding XGBoost models as stages within MLlib ML pipelines for structured workflows
tags:
  - xgboost
  - mllib
  - ml-pipeline
  - scala
timestamp: "2026-06-19T18:35:03.899Z"
---

# XGBoost with MLlib Pipeline API

**XGBoost with MLlib Pipeline API** refers to the integration of the [XGBoost](/concepts/xgboostspark-module.md) gradient‑boosting library with Apache Spark’s [MLlib Pipeline](/concepts/mllib-pipelines-api.md) API for distributed training on Databricks. This approach allows users to embed XGBoost models as pipeline stages and to leverage MLlib’s cross‑validation framework for hyperparameter tuning. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Overview

The MLlib Pipeline API provides a uniform interface for building machine learning workflows composed of transformers and estimators. By wrapping XGBoost within a pipeline stage, data scientists can combine XGBoost with other MLlib components (e.g., feature transformers) and run the entire workflow on distributed Spark clusters. Databricks provides annotated example notebooks—written in Scala—that demonstrate this integration. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Examples

The following two examples are available as notebooks on Databricks:

### XGBoost Classification with ML Pipeline

This notebook shows how to embed an XGBoost classification model into an MLlib ML pipeline. The pipeline can include feature preprocessing steps such as VectorAssembler or StringIndexer, followed by an XGBoost estimator. The resulting pipeline model can be used for scoring new data. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

### XGBoost Regression with Cross‑Validation

This notebook demonstrates how to use [MLlib Cross‑Validation](/concepts/crossvalidator.md) to tune the hyperparameters of an XGBoost regression model. A grid of parameter values (e.g., learning rate, max depth, number of rounds) is evaluated using k‑fold cross‑validation within a pipeline, and the best‑performing model is selected automatically. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) – A distributed gradient‑boosting framework.
- [MLlib Pipeline](/concepts/mllib-pipelines-api.md) – Spark’s unified API for constructing machine learning workflows.
- [Cross-Validation](/concepts/crossvalidator.md) – A technique for model evaluation and hyperparameter tuning.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The ML‑optimized runtime that includes pre‑installed libraries for distributed training.
- Scala API – The Scala‑based interface used in the provided example notebooks.

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
