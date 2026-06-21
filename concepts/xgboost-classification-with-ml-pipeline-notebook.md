---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7ca64ea2d230b5373d62f31ae0915e91db4f7e4200054b8217f4f9383a68a0a6
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - xgboost-classification-with-ml-pipeline-notebook
    - XCWMPN
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: XGBoost Classification with ML Pipeline Notebook
description: An example Databricks notebook demonstrating XGBoost classification embedded in an MLlib ML pipeline
tags:
  - xgboost
  - classification
  - notebook
  - databricks
timestamp: "2026-06-19T18:35:14.813Z"
---

# XGBoost Classification with ML Pipeline Notebook

The **XGBoost Classification with ML Pipeline Notebook** is a Databricks example notebook that demonstrates how to embed an [XGBoost](/concepts/xgboostspark-module.md) classification model into an MLlib ML Pipeline. It is one of two example notebooks provided in the Databricks documentation for distributed training of XGBoost models using Scala; the companion notebook covers regression with cross‑validation. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Purpose

The notebook shows the recommended workflow for integrating a third‑party machine learning library (XGBoost) with Spark’s [MLlib Pipelines API](/concepts/mllib-pipelines-api.md). By wrapping the XGBoost classifier as a Pipeline stage, users can combine it with standard preprocessing transformers and tune hyperparameters using MLlib’s built‑in evaluation and cross‑validation tools. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Context

This notebook is part of the **Use XGBoost on Databricks** section of the Databricks documentation and is authored in Scala. It assumes familiarity with [XGBoost](/concepts/xgboostspark-module.md), MLlib, and the [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) environment. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) – Optimized gradient boosting library for classification and regression.
- MLlib – Apache Spark’s scalable machine learning library.
- ML Pipeline – A DataFrame‑based API for defining and chaining machine learning workflows.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The pre‑configured environment that includes XGBoost and MLlib.
- Cross-validation – Used in the companion notebook for hyperparameter tuning of XGBoost regression models.

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
