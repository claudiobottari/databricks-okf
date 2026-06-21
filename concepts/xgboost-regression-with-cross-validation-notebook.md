---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 367f7a755c1c84997ba68d737666b132531932855a24c6b596f3bf78a70a2f9c
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - xgboost-regression-with-cross-validation-notebook
    - XRWCN
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: XGBoost Regression with Cross-Validation Notebook
description: An example Databricks notebook demonstrating XGBoost regression tuned via MLlib cross-validation
tags:
  - xgboost
  - regression
  - cross-validation
  - databricks
timestamp: "2026-06-19T18:35:13.081Z"
---

# XGBoost Regression with Cross-Validation Notebook

The **XGBoost Regression with Cross-Validation Notebook** is a Databricks example notebook that demonstrates how to use MLlib’s cross‑validation functionality to tune hyperparameters for an [XGBoost](/concepts/xgboostspark-module.md) regression model using the Scala API. It is one of two example notebooks provided in the official Databricks documentation for distributed training of XGBoost models with Scala. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Overview

This notebook builds an XGBoost regression pipeline and then wraps it with MLlib’s `CrossValidator` to perform hyperparameter tuning. The tuning process searches over a user‑defined parameter grid (e.g., number of rounds, maximum depth, learning rate) and selects the best model based on a chosen evaluation metric. The workflow demonstrates how to embed an XGBoost model inside an MLlib ML Pipeline and then apply cross‑validation for more robust model selection. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

The companion notebook, **XGBoost Classification with ML Pipeline Notebook**, covers the classification case. Together they illustrate how to leverage MLlib’s distributed training capabilities alongside XGBoost’s gradient‑boosting algorithms on Databricks. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Prerequisites and Environment

The notebook assumes a Databricks cluster running **Databricks Runtime ML**, which bundles the XGBoost4J‑Spark library and the MLlib cross‑validation utilities. Users should be familiar with the Scala API for both XGBoost and Spark MLlib. The notebook code is designed to run in a notebook attached to such a cluster. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) – Gradient‑boosting framework used for regression and classification.
- [MLlib Cross-Validation](/concepts/crossvalidator.md) – MLlib’s `CrossValidator` and `ParamGridBuilder` for hyperparameter tuning.
- ML Pipeline – Spark MLlib’s pipeline abstraction for chaining transformers and estimators.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The pre‑configured environment that includes XGBoost and distributed ML libraries.
- ParameterGrid – The set of hyperparameter combinations to search during cross‑validation.

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
