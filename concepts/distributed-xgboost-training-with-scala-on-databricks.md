---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5fd470649cc913da14a17c581df208b349a894cae69659f2aaa2df7d7b61a2d9
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-xgboost-training-with-scala-on-databricks
    - DXTWSOD
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: Distributed XGBoost training with Scala on Databricks
description: Using XGBoost for distributed model training within Scala notebooks on Databricks, integrated with Apache Spark MLlib.
tags:
  - xgboost
  - scala
  - distributed-training
  - databricks
timestamp: "2026-06-18T15:31:41.474Z"
---

# Distributed XGBoost Training with Scala on Databricks

**Distributed XGBoost Training with Scala on Databricks** refers to the use of XGBoost — a popular gradient-boosting framework — within [Apache Spark MLlib](/concepts/apache-spark-mllib.md) pipelines, written in Scala, on the Databricks platform. This approach enables scalable, distributed model training on tabular data by combining XGBoost’s algorithmic performance with Spark’s distributed computing engine.

## Overview

Databricks provides example notebooks that demonstrate how to train XGBoost models using Scala and integrate them with MLlib, Spark’s machine learning library. The examples cover two common workflows: embedding an XGBoost model into an ML pipeline, and using MLlib cross-validation for hyperparameter tuning. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

These notebooks run on [Databricks Runtime ML](/concepts/databricks-runtime-ml.md), which includes pre-installed XGBoost libraries and Spark integration.

## Feature Highlights

- **ML Pipeline Integration**: XGBoost models can be used as a stage in an MLlib [Pipeline](/concepts/mllib-pipelines-api.md), allowing seamless chaining with feature transformers, vector assemblers, and other estimators. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]
- **Cross-Validation Support**: MLlib’s [CrossValidator](/concepts/crossvalidator.md) can be applied to tune XGBoost hyperparameters in a distributed fashion. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Available Examples

The source documentation provides two notebook-based examples:

1. **XGBoost Classification with ML Pipeline** – Demonstrates how to embed an XGBoost classifier into an MLlib pipeline. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]
2. **XGBoost Regression with Cross-Validation** – Shows how to use cross-validation to tune an XGBoost regression model. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

Both notebooks are written in Scala and leverage the `xgboost-spark` package, which provides a Spark-compatible API for XGBoost.

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) — The gradient-boosting framework used for classification and regression.
- MLlib — Spark’s distributed machine learning library.
- ML Pipeline — A workflow abstraction in Spark ML for composing transformers and estimators.
- [Cross-Validation](/concepts/crossvalidator.md) — A resampling technique for model evaluation and hyperparameter tuning.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The Databricks runtime that includes ML libraries like XGBoost.
- Scala — The programming language used in these notebooks.

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
