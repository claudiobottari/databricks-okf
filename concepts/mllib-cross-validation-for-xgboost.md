---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37c3f877758f6cd824a277c4cbd239abae8ab288e6457bc2b537c8480b47b403
  pageDirectory: concepts
  sources:
    - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mllib-cross-validation-for-xgboost
    - MCFX
  citations:
    - file: distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
title: MLlib Cross-Validation for XGBoost
description: Using MLlib cross-validation tools to tune hyperparameters of XGBoost models in Scala
tags:
  - machine-learning
  - hyperparameter-tuning
  - cross-validation
  - xgboost
timestamp: "2026-06-18T12:05:06.004Z"
---

---
title: MLlib Cross-Validation for XGBoost
summary: Using MLlib's cross-validation mechanism to tune XGBoost models within an ML pipeline on Databricks.
sources:
  - distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
tags:
  - xgboost
  - mllib
  - cross-validation
  - scala
  - databricks
provenanceState: extracted
inferredParagraphs: 0
---

# MLlib Cross-Validation for XGBoost

**MLlib Cross-Validation for XGBoost** refers to the practice of using [Apache Spark's MLlib](/concepts/apache-spark-mllib.md) cross-validation functionality to tune [XGBoost](/concepts/xgboostspark-module.md) models within a ML Pipeline on Databricks. This approach combines the distributed training capabilities of XGBoost with MLlib's built-in model evaluation and parameter selection tools. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Using MLlib Cross-Validation with XGBoost

A dedicated example notebook demonstrates XGBoost regression with cross-validation using the Scala API. The notebook shows how to embed an XGBoost model into an MLlib ML Pipeline and then apply MLlib's cross-validation mechanism to tune the model's hyperparameters. By iterating over a grid of parameters and evaluating performance on cross-validation folds, users can select the best-performing model configuration. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

The notebook is part of a pair of examples: the first illustrates embedding an XGBoost classifier into an ML Pipeline, and the second (the cross-validation example) focuses on regression with hyperparameter tuning. Both examples are available in the Databricks documentation. ^[distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md]

## Related Concepts

- [XGBoost](/concepts/xgboostspark-module.md) — The gradient-boosted tree algorithm used for training
- MLlib — Spark's machine learning library that provides cross-validation utilities
- ML Pipeline — The pipeline framework for chaining transformers and estimators
- [Cross-Validation (Spark)](/concepts/crossvalidator.md) — MLlib's `CrossValidator` for hyperparameter tuning
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — General techniques for optimizing model parameters
- Scala — The programming language used in the example notebooks
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime that includes pre-installed XGBoost and Spark MLlib

## Sources

- distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md

# Citations

1. [distributed-training-of-xgboost-models-using-scala-databricks-on-aws.md](/references/distributed-training-of-xgboost-models-using-scala-databricks-on-aws-760f6d64.md)
